#!/usr/bin/env python3
"""Chronological baseline evaluation and feature-ranking stability for v2."""
import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
import yaml
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.feature_selection import mutual_info_classif
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, balanced_accuracy_score,
                             confusion_matrix, f1_score, roc_auc_score,
                             average_precision_score, brier_score_loss,
                             log_loss)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def scores(y, pred, prob):
    cm = confusion_matrix(y, pred, labels=[0, 1])
    tn, fp, fn, tp = (int(cm[0, 0]), int(cm[0, 1]), int(cm[1, 0]), int(cm[1, 1]))
    mcc_denominator = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    return {
        "accuracy": float(accuracy_score(y, pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
        "macro_f1": float(f1_score(y, pred, labels=[0, 1], average="macro", zero_division=0)),
        "mcc": float((tp * tn - fp * fn) / mcc_denominator) if mcc_denominator else 0.0,
        "precision_0": float(tn / (tn + fn)) if tn + fn else 0.0,
        "precision_1": float(tp / (tp + fp)) if tp + fp else 0.0,
        "recall_0": float(tn / (tn + fp)) if tn + fp else 0.0,
        "recall_1": float(tp / (tp + fn)) if tp + fn else 0.0,
        "roc_auc": float(roc_auc_score(y, prob)) if len(np.unique(y)) == 2 else float("nan"),
        "pr_auc": float(average_precision_score(y, prob)) if len(np.unique(y)) == 2 else float("nan"),
        "brier": float(brier_score_loss(y, prob)),
        "log_loss": float(log_loss(y, prob, labels=[0, 1])),
        "prevalence_1": float(np.mean(y)),
        "confusion_00": int(cm[0, 0]), "confusion_01": int(cm[0, 1]),
        "confusion_10": int(cm[1, 0]), "confusion_11": int(cm[1, 1]),
    }


def make_hgb(seed):
    return HistGradientBoostingClassifier(
        learning_rate=0.08, max_iter=60, max_leaf_nodes=15,
        l2_regularization=1.0, early_stopping=False, random_state=seed,
    )


def ranks_for_fold(x, y, inner_x, inner_y, columns, seed, cfg):
    mi = mutual_info_classif(x, y, random_state=seed, n_neighbors=3)
    mi_order = np.argsort(-mi, kind="stable")

    l1 = make_pipeline(StandardScaler(), LogisticRegression(
        l1_ratio=1.0, solver="liblinear", C=0.1, max_iter=400,
        random_state=seed,
    ))
    l1.fit(x, y)
    l1_coef = np.abs(l1[-1].coef_[0])
    l1_order = np.argsort(-l1_coef, kind="stable")

    selector = make_hgb(seed)
    selector.fit(x, y)
    perm = permutation_importance(
        selector, inner_x, inner_y, scoring="balanced_accuracy",
        n_repeats=int(cfg["selection"]["permutation_repeats"]),
        max_samples=min(int(cfg["selection"]["permutation_max_samples"]), len(inner_y)),
        random_state=seed,
        n_jobs=int(cfg["selection"]["permutation_n_jobs"]),
    ).importances_mean
    perm_order = np.argsort(-perm, kind="stable")
    values = {"mutual_information": mi, "l1_logistic": l1_coef,
              "inner_temporal_permutation": perm}
    orders = {"mutual_information": mi_order, "l1_logistic": l1_order,
              "inner_temporal_permutation": perm_order}
    detail = []
    for method, order in orders.items():
        rank_by_index = np.empty(len(columns), dtype=int)
        rank_by_index[order] = np.arange(1, len(columns) + 1)
        for i, name in enumerate(columns):
            detail.append({"method": method, "feature": name,
                           "rank": int(rank_by_index[i]),
                           "importance": float(values[method][i])})
    return orders, detail


def main():
    started = time.perf_counter()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", type=Path, default=Path("config/intraday_direction_v2.yaml"))
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/intraday_direction_v2_features.parquet"))
    ap.add_argument("--output", type=Path, default=Path("reports/intraday_direction_v2_selection.csv"))
    ap.add_argument("--folds", type=int, default=5, help="Use fewer folds for a timed pilot.")
    ap.add_argument("--top-k", type=int, nargs="+", default=[10, 20, 0], help="0 means all features.")
    args = ap.parse_args()
    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    frame = pd.read_parquet(args.parquet)
    manifest_path = args.parquet.with_suffix(".manifest.json")
    build_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    features = build_manifest["feature_columns"]
    date_values = frame.date.astype(str)
    feature_ready = frame[features].notna().all(axis=1)
    seed = int(cfg["training_diagnostics"]["random_seeds"][0])
    dates = sorted(frame.date.astype(str).unique())
    fold_count = min(args.folds, int(cfg["temporal_evaluation"]["outer_folds"]))
    initial = int(cfg["temporal_evaluation"]["initial_train_sessions"])
    val_n = int(cfg["temporal_evaluation"]["outer_validation_sessions"])
    if len(dates) < initial + fold_count * val_n:
        raise ValueError(f"Need at least {initial + fold_count * val_n} sessions; found {len(dates)}")
    first_val = len(dates) - fold_count * val_n
    if first_val < initial:
        raise ValueError("Insufficient initial training sessions for requested folds")
    folds = []
    for f in range(fold_count):
        val_start_idx = first_val + f * val_n
        train_dates = dates[:val_start_idx]
        val_dates = dates[val_start_idx:val_start_idx + val_n]
        folds.append((f + 1, train_dates, val_dates))

    result_rows, rank_rows, fold_rows = [], [], []
    rank_corr_rows = []
    horizons = cfg["forecast_target"]["horizons_observed_bars"]
    bands = list(cfg["time_of_day"]["bands"])
    topks = args.top_k
    model_names = ["logistic_regression", "hist_gradient_boosting"]
    for fold_no, train_dates, val_dates in folds:
        train_date_mask = date_values.isin(train_dates)
        val_date_mask = date_values.isin(val_dates)
        inner_dates = train_dates[-int(cfg["selection"]["permutation_inner_validation_sessions"]):]
        fit_dates = train_dates[:-len(inner_dates)]
        if not fit_dates:
            raise ValueError("No inner selector training dates")
        for horizon in horizons:
            target = f"target_up_{horizon}m"
            for band in bands:
                task = train_date_mask & frame.time_band.eq(band) & frame[target].notna() & feature_ready
                val_task = val_date_mask & frame.time_band.eq(band) & frame[target].notna() & feature_ready
                inner_mask = date_values.isin(inner_dates) & frame.time_band.eq(band) & frame[target].notna() & feature_ready
                fit_mask = date_values.isin(fit_dates) & frame.time_band.eq(band) & frame[target].notna() & feature_ready
                if task.sum() == 0 or val_task.sum() == 0 or inner_mask.sum() == 0 or fit_mask.sum() == 0:
                    continue
                tr = frame.loc[task]
                va = frame.loc[val_task]
                x_train = tr[features].to_numpy(dtype=np.float32)
                y_train = tr[target].astype(int).to_numpy()
                x_val = va[features].to_numpy(dtype=np.float32)
                y_val = va[target].astype(int).to_numpy()
                if np.unique(y_train).size < 2:
                    continue
                # Fixed, no-selection reference forecasts.
                majority_prob = float(np.mean(y_train))
                for base_name, base_prob in (
                    ("majority_prevalence", np.full(len(va), majority_prob)),
                    ("causal_5m_momentum", (va.log_return_5m.to_numpy() > 0).astype(float)),
                ):
                    base_pred = (base_prob >= 0.5).astype(int)
                    base_row = {"fold": fold_no, "horizon": horizon, "band": band,
                                "selection_method": "none_baseline", "top_k": "none", "root": "ALL",
                                "feature_count": 0, "model": base_name,
                                "train_rows": len(tr), "validation_rows": len(va),
                                "fit_predict_seconds": 0.0, "train_start": train_dates[0],
                                "train_end": train_dates[-1], "validation_start": val_dates[0],
                                "validation_end": val_dates[-1]}
                    base_row.update(scores(y_val, base_pred, base_prob))
                    result_rows.append(base_row)
                    for root in ("WIN", "IND"):
                        root_mask = va.ticker.str.startswith(root).to_numpy()
                        if root_mask.any():
                            root_row = dict(base_row, root=root, validation_rows=int(root_mask.sum()))
                            root_row.update(scores(y_val[root_mask], base_pred[root_mask], base_prob[root_mask]))
                            result_rows.append(root_row)
                # Rankers only see the pre-inner chronological training slice.
                inner_fit = frame.loc[fit_mask]
                inner_val = frame.loc[inner_mask]
                if inner_fit[target].nunique() < 2 or inner_val[target].nunique() < 2:
                    continue
                orders, details = ranks_for_fold(
                    inner_fit[features].to_numpy(dtype=np.float32),
                    inner_fit[target].astype(int).to_numpy(),
                    inner_val[features].to_numpy(dtype=np.float32),
                    inner_val[target].astype(int).to_numpy(), features, seed + fold_no, cfg,
                )
                for item in details:
                    rank_rows.append({"fold": fold_no, "horizon": horizon, "band": band, **item})
                method_names = list(orders)
                rank_maps = {}
                for name, order in orders.items():
                    rank_map = np.empty(len(features), dtype=float)
                    rank_map[order] = np.arange(1, len(features) + 1, dtype=float)
                    rank_maps[name] = rank_map
                for i, left in enumerate(method_names):
                    for right in method_names[i + 1:]:
                        rho = float(pd.Series(rank_maps[left]).corr(pd.Series(rank_maps[right]), method="spearman"))
                        rank_corr_rows.append({"fold": fold_no, "horizon": horizon, "band": band,
                                               "method_a": left, "method_b": right,
                                               "spearman_rank_correlation": rho})
                fold_rows.append({"fold": fold_no, "horizon": horizon, "band": band,
                                  "train_start": train_dates[0], "train_end": train_dates[-1],
                                  "inner_fit_end": fit_dates[-1], "inner_validation_start": inner_dates[0],
                                  "inner_validation_end": inner_dates[-1], "validation_start": val_dates[0],
                                  "validation_end": val_dates[-1], "train_rows": len(tr),
                                  "inner_fit_rows": len(inner_fit), "inner_validation_rows": len(inner_val),
                                  "validation_rows": len(va)})
                for method, order in orders.items():
                    for requested_k in topks:
                        k = len(features) if requested_k == 0 else min(requested_k, len(features))
                        chosen = order[:k]
                        for model_name in model_names:
                            if model_name == "logistic_regression":
                                model = make_pipeline(StandardScaler(), LogisticRegression(
                                    C=1.0, max_iter=400, random_state=seed + fold_no,
                                ))
                            else:
                                model = make_hgb(seed + fold_no)
                            fit_started = time.perf_counter()
                            model.fit(x_train[:, chosen], y_train)
                            probability = model.predict_proba(x_val[:, chosen])[:, 1]
                            prediction = (probability >= 0.5).astype(int)
                            row = {"fold": fold_no, "horizon": horizon, "band": band,
                                   "selection_method": method,
                                   "top_k": "all" if requested_k == 0 else min(requested_k, len(features)),
                                   "feature_count": len(chosen), "model": model_name, "root": "ALL",
                                   "train_rows": len(tr), "validation_rows": len(va),
                                   "fit_predict_seconds": round(time.perf_counter() - fit_started, 4),
                                   "train_start": train_dates[0], "train_end": train_dates[-1],
                                   "validation_start": val_dates[0], "validation_end": val_dates[-1]}
                            row.update(scores(y_val, prediction, probability))
                            result_rows.append(row)
                            for root in ("WIN", "IND"):
                                root_mask = va.ticker.str.startswith(root).to_numpy()
                                if root_mask.any():
                                    root_row = dict(row, root=root, validation_rows=int(root_mask.sum()))
                                    root_row.update(scores(y_val[root_mask], prediction[root_mask], probability[root_mask]))
                                    result_rows.append(root_row)
        print(f"fold {fold_no}/{fold_count} complete; results={len(result_rows)} rankings={len(rank_rows)}", flush=True)
        checkpoint_dir = Path("tmp/intraday_direction_v2")
        checkpoint_dir.mkdir(parents=True, exist_ok=True)
        pd.DataFrame([r for r in result_rows if r["fold"] == fold_no]).to_csv(
            checkpoint_dir / f"metrics_fold_{fold_no}.csv", index=False)
        pd.DataFrame([r for r in rank_rows if r["fold"] == fold_no]).to_csv(
            checkpoint_dir / f"rankings_fold_{fold_no}.csv", index=False)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    results = pd.DataFrame(result_rows)
    ranks = pd.DataFrame(rank_rows)
    results.to_csv(args.output, index=False)
    rank_path = args.output.with_name(args.output.stem + "_rankings.csv")
    ranks.to_csv(rank_path, index=False)
    # Mean rank and top-10/20 frequency are calculated within each target task.
    stability = ranks.groupby(["horizon", "band", "method", "feature"], as_index=False).agg(
        mean_rank=("rank", "mean"), rank_sd=("rank", "std"),
        top10_frequency=("rank", lambda s: float(np.mean(s <= 10))),
        top20_frequency=("rank", lambda s: float(np.mean(s <= 20))),
        folds_ranked=("rank", "count"), mean_importance=("importance", "mean"),
    )
    stability_path = args.output.with_name(args.output.stem + "_stability.csv")
    stability.to_csv(stability_path, index=False)
    rank_corr_path = args.output.with_name(args.output.stem + "_rank_correlations.csv")
    rank_corr = pd.DataFrame(rank_corr_rows)
    rank_corr.to_csv(rank_corr_path, index=False)
    run = {
        "status": "development_only_rolling_origin_no_final_test",
        "config_sha256": digest(args.config), "parquet_sha256": digest(args.parquet),
        "build_manifest_sha256": digest(manifest_path),
        "source_market_sha256": build_manifest["source_sha256"],
        "feature_count": len(features), "feature_columns": features,
        "folds": fold_rows, "fold_count": fold_count,
        "selector_methods": ["mutual_information", "l1_logistic", "inner_temporal_permutation"],
        "ranking_scope": "training slice and inner validation only; outer validation excluded",
        "models": model_names, "top_k": ["all" if k == 0 else k for k in topks],
        "results_csv": str(args.output), "rankings_csv": str(rank_path),
        "stability_csv": str(stability_path),
        "rank_correlations_csv": str(rank_corr_path),
        "independent_future_test_available": False,
        "runtime_seconds": round(time.perf_counter() - started, 2),
        "scikit_learn": sklearn.__version__, "result_rows": len(results),
        "ranking_rows": len(ranks),
    }
    if not results.empty:
        summary = results.groupby(["horizon", "band", "root", "selection_method", "top_k", "model"], as_index=False).agg(
            mcc_mean=("mcc", "mean"), mcc_sd=("mcc", "std"),
            balanced_accuracy_mean=("balanced_accuracy", "mean"),
            macro_f1_mean=("macro_f1", "mean"), roc_auc_mean=("roc_auc", "mean"),
            pr_auc_mean=("pr_auc", "mean"), brier_mean=("brier", "mean"),
            validation_rows_mean=("validation_rows", "mean"),
        )
        summary_path = args.output.with_name(args.output.stem + "_summary.csv")
        summary.to_csv(summary_path, index=False)
        report_path = args.output.with_name(args.output.stem + ".md")
        best = summary.sort_values(["horizon", "band", "mcc_mean"], ascending=[True, True, False])
        top = stability.sort_values(["horizon", "band", "method", "mean_rank"])
        report = [
            "# Baseline direcional intradiária v2 — resultados de desenvolvimento", "",
            "Validação rolling-origin. Todas as datas disponíveis são desenvolvimento; o teste histórico já aberto não é teste independente desta hipótese. Nenhuma conclusão de rentabilidade é avaliada.", "",
            f"- Indicadores: {len(features)}; folds executados: {fold_count}; métricas por modelo/fold: {len(results)}.",
            f"- Ranking de features: {rank_path.name}; estabilidade: {stability_path.name}; correlações Spearman: {rank_corr_path.name}.",
            "- Ranking de permutação usa somente o bloco temporal interno do treino. Cada bloco externo permanece fora da seleção. Métricas por WIN/IND usam previsões do modelo conjunto.", "",
            "## Melhores combinações por horizonte/faixa/raiz (MCC médio; apenas resumo exploratório)", "",
            "| Horizonte | Faixa | Raiz | Seletor | K | Modelo | MCC ± DP | Balanced accuracy | Macro-F1 | ROC-AUC | PR-AUC |", "|---:|---|---|---|---:|---|---:|---:|---:|---:|---:|",
        ]
        for (h, band, root), group in best.groupby(["horizon", "band", "root"], sort=True):
            for _, row in group.head(1).iterrows():
                sd = row.mcc_sd if pd.notna(row.mcc_sd) else 0.0
                report.append(f"| {h}m | {band} | {root} | {row.selection_method} | {row.top_k} | {row.model} | {row.mcc_mean:.3f} ± {sd:.3f} | {row.balanced_accuracy_mean:.3f} | {row.macro_f1_mean:.3f} | {row.roc_auc_mean:.3f} | {row.pr_auc_mean:.3f} |")
        report += ["", "## Top 10 por método e tarefa", "", "| Horizonte | Faixa | Método | Features (ordem média) |", "|---:|---|---|---|"]
        for (h, band, method), group in top.groupby(["horizon", "band", "method"], sort=True):
            names = ", ".join(group.head(10).feature.tolist())
            report.append(f"| {h}m | {band} | {method} | {names} |")
        if not rank_corr.empty:
            correlations = rank_corr.groupby(["horizon", "band", "method_a", "method_b"], as_index=False).spearman_rank_correlation.mean()
            report += ["", "## Concordância média dos rankings", "", "| Horizonte | Faixa | Método A | Método B | Spearman |", "|---:|---|---|---|---:|"]
            for _, row in correlations.iterrows():
                report.append(f"| {row.horizon}m | {row.band} | {row.method_a} | {row.method_b} | {row.spearman_rank_correlation:.3f} |")
            pair_means = rank_corr.groupby(["method_a", "method_b"]).spearman_rank_correlation.mean()
            report += ["", "Médias globais de Spearman: " + "; ".join(
                f"{a} vs. {b} = {v:.3f}" for (a, b), v in pair_means.items()) + "."]
        pooled_summary = summary[summary.root == "ALL"]
        if not pooled_summary.empty:
            best_pooled = pooled_summary.sort_values("mcc_mean", ascending=False).iloc[0]
            report += [
                "", "## Limitações e leitura exploratória", "",
                "As médias pooled devem ser comparadas com a referência de prevalência: métricas agregadas ficam próximas do acaso e o momentum causal foi negativo nos três horizontes. Não aparece uma vantagem consistente de top-10/top-20 sobre todas as features.",
                f"A maior média MCC pooled entre as combinações avaliadas foi {best_pooled.mcc_mean:.3f} ({best_pooled.horizon}m, {best_pooled.band}, {best_pooled.selection_method}, K={best_pooled.top_k}, {best_pooled.model}); como foi escolhida entre muitas combinações, é exploratória e não confirmatória.",
                "A regressão logística emitiu avisos de não convergência no limite de 400 iterações em alguns ajustes. Seus resultados são provisórios até repetir esses ajustes com limite maior e registrar convergência por fold.",
                "As métricas por raiz usam previsões do modelo conjunto, não modelos independentes. As oscilações por raiz/bloco devem ser lidas com cobertura, prevalência e matriz de confusão.",
                "Não houve avaliação executável com custos nem teste futuro intocado. O período jan–jun/2026 permanece desenvolvimento.",
            ]
        report += ["", "Os melhores valores foram usados para descrição dos folds de desenvolvimento. Como várias tarefas/configurações foram comparadas, não são estimativas confirmatórias nem justificam escolher um vencedor sem avaliação futura bloqueada.", ""]
        report_path.write_text("\n".join(report), encoding="utf-8")
        run["summary_csv"] = str(summary_path)
        run["report_md"] = str(report_path)
    args.output.with_suffix(".json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(run, indent=2))


if __name__ == "__main__":
    main()
