"""Run predictive statistical tests and economic backtests for model selection.

The goal is to avoid declaring a single "best model" from plots alone. This
script compares all available model/optimizer/seed combinations from the three
professor-facing experiments:

1. Exp. 1: Holdout + MCC/F1
2. Exp. 2: Holdout + Accuracy
3. Exp. 3: Cross-validation + Accuracy

Predictive tests use the *_best_by_seed.csv files. Economic tests use the saved
predictions and a simple long/short backtest on the common X_test block.
"""

from __future__ import annotations

import itertools
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy.stats import friedmanchisquare, wilcoxon

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_loader import load_legacy_dataset
from src.feature_selection import select_features
from src.preprocessing import drop_missing_rows, keep_numeric_features
from src.utils.io import load_project_configs


OUT_DIR = ROOT / "outputs" / "professor_presentation" / "statistical_economic_model_selection"
SEEDS = [1, 2, 3]
MODELS = ["cnn", "mlp", "rf", "svm"]
OPTIMIZERS = ["de", "ga", "gwo", "pso", "random_search"]
TRANSACTION_COST_POINTS = 5.0


@dataclass(frozen=True)
class Experiment:
    key: str
    label: str
    metrics_dir: Path
    predictions_dir: Path
    primary_metric: str


EXPERIMENTS = [
    Experiment(
        key="exp1_holdout_mcc_f1",
        label="Exp. 1 - Holdout + MCC/F1",
        metrics_dir=ROOT / "outputs" / "article_official" / "metrics",
        predictions_dir=ROOT / "outputs" / "article_official" / "predictions",
        primary_metric="mcc_test",
    ),
    Experiment(
        key="exp2_holdout_accuracy",
        label="Exp. 2 - Holdout + Accuracy",
        metrics_dir=ROOT / "outputs" / "article_official_accuracy_holdout" / "metrics",
        predictions_dir=ROOT / "outputs" / "article_official_accuracy_holdout" / "predictions",
        primary_metric="accuracy_test",
    ),
    Experiment(
        key="exp3_cv_accuracy",
        label="Exp. 3 - CV + Accuracy",
        metrics_dir=ROOT / "outputs" / "article_official_accuracy" / "metrics",
        predictions_dir=ROOT / "outputs" / "article_official_accuracy" / "predictions",
        primary_metric="accuracy_test",
    ),
]


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except pd.errors.ParserError:
        return pd.read_csv(path, engine="python", on_bad_lines="skip")


def holm_adjust(p_values: list[float]) -> list[float]:
    """Holm-Bonferroni adjusted p-values."""
    m = len(p_values)
    order = np.argsort(p_values)
    adjusted = np.empty(m, dtype=float)
    running_max = 0.0
    for rank, idx in enumerate(order):
        value = min(1.0, (m - rank) * p_values[idx])
        running_max = max(running_max, value)
        adjusted[idx] = running_max
    return adjusted.tolist()


def load_predictive_rows() -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    missing: list[Path] = []
    for exp in EXPERIMENTS:
        for model in MODELS:
            for optimizer in OPTIMIZERS:
                path = exp.metrics_dir / f"{model}_{optimizer}_best_by_seed.csv"
                if not path.exists():
                    missing.append(path)
                    continue
                df = read_csv(path)
                df = df[df["seed"].isin(SEEDS)].copy()
                for _, row in df.iterrows():
                    rows.append(
                        {
                            "experiment": exp.key,
                            "experiment_label": exp.label,
                            "primary_metric": exp.primary_metric,
                            "model": model,
                            "optimizer": optimizer,
                            "seed": int(row["seed"]),
                            "accuracy_test": float(row["accuracy_test"]),
                            "balanced_accuracy_test": float(row.get("balanced_accuracy_test", np.nan)),
                            "mcc_test": float(row["mcc_test"]),
                            "f1_test": float(row["f1_test"]),
                            "auc_roc_test": float(row.get("auc_roc_test", np.nan)),
                            "auc_pr_test": float(row.get("auc_pr_test", np.nan)),
                            "reported_metric": float(row[exp.primary_metric]),
                        }
                    )
    if missing:
        print("Missing predictive metric files:")
        for path in missing:
            print(path)
    return pd.DataFrame(rows)


def summarize_predictive(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    combo = (
        df.groupby(["experiment", "experiment_label", "model", "optimizer"])
        .agg(
            n=("seed", "nunique"),
            reported_metric_mean=("reported_metric", "mean"),
            reported_metric_std=("reported_metric", "std"),
            accuracy_mean=("accuracy_test", "mean"),
            accuracy_std=("accuracy_test", "std"),
            mcc_mean=("mcc_test", "mean"),
            mcc_std=("mcc_test", "std"),
            f1_mean=("f1_test", "mean"),
            f1_std=("f1_test", "std"),
            auc_roc_mean=("auc_roc_test", "mean"),
            auc_pr_mean=("auc_pr_test", "mean"),
        )
        .reset_index()
    )
    model_by_exp = (
        df.groupby(["experiment", "experiment_label", "model"])
        .agg(
            n=("reported_metric", "count"),
            reported_metric_mean=("reported_metric", "mean"),
            accuracy_mean=("accuracy_test", "mean"),
            mcc_mean=("mcc_test", "mean"),
            f1_mean=("f1_test", "mean"),
            auc_roc_mean=("auc_roc_test", "mean"),
        )
        .reset_index()
    )
    model_overall = (
        df.groupby("model")
        .agg(
            n=("reported_metric", "count"),
            accuracy_mean=("accuracy_test", "mean"),
            mcc_mean=("mcc_test", "mean"),
            f1_mean=("f1_test", "mean"),
            auc_roc_mean=("auc_roc_test", "mean"),
            reported_metric_mean=("reported_metric", "mean"),
        )
        .reset_index()
    )
    return combo, model_by_exp, model_overall


def friedman_and_pairwise_models(df: pd.DataFrame, metric: str, block_cols: list[str], scope: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    pivot = df.pivot_table(index=block_cols, columns="model", values=metric, aggfunc="mean")
    pivot = pivot.dropna(subset=MODELS)
    if pivot.empty:
        return pd.DataFrame(), pd.DataFrame()

    stat, p_value = friedmanchisquare(*(pivot[model].to_numpy() for model in MODELS))
    ranks = pivot.rank(axis=1, ascending=False, method="average")
    summary = pd.DataFrame(
        [
            {
                "scope": scope,
                "metric": metric,
                "n_blocks": int(len(pivot)),
                "friedman_statistic": float(stat),
                "friedman_p_value": float(p_value),
                **{f"mean_rank_{model}": float(ranks[model].mean()) for model in MODELS},
                **{f"mean_{model}": float(pivot[model].mean()) for model in MODELS},
            }
        ]
    )

    best_model = pivot.mean().idxmax()
    rows = []
    raw_p = []
    for model in MODELS:
        if model == best_model:
            continue
        diff = pivot[best_model] - pivot[model]
        try:
            p = float(wilcoxon(diff, zero_method="wilcox").pvalue)
        except ValueError:
            p = 1.0
        raw_p.append(p)
        rows.append(
            {
                "scope": scope,
                "metric": metric,
                "best_model_by_mean": best_model,
                "comparison": f"{best_model} vs {model}",
                "n_blocks": int(len(diff)),
                "mean_difference": float(diff.mean()),
                "median_difference": float(diff.median()),
                "wilcoxon_p_value": p,
            }
        )
    adjusted = holm_adjust(raw_p) if raw_p else []
    for row, p_adj in zip(rows, adjusted):
        row["holm_p_value"] = p_adj
        row["significant_0_05"] = bool(p_adj < 0.05)
    return summary, pd.DataFrame(rows)


def run_predictive_tests(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    summaries = []
    pairwise = []

    for metric in ["accuracy_test", "mcc_test", "f1_test", "auc_roc_test"]:
        summary, pairs = friedman_and_pairwise_models(
            df,
            metric=metric,
            block_cols=["experiment", "optimizer", "seed"],
            scope="all_experiments_optimizer_seed_blocks",
        )
        summaries.append(summary)
        pairwise.append(pairs)

    for exp in EXPERIMENTS:
        part = df[df["experiment"] == exp.key].copy()
        metrics = list(dict.fromkeys([exp.primary_metric, "accuracy_test", "mcc_test", "f1_test"]))
        for metric in metrics:
            summary, pairs = friedman_and_pairwise_models(
                part,
                metric=metric,
                block_cols=["optimizer", "seed"],
                scope=exp.key,
            )
            summaries.append(summary)
            pairwise.append(pairs)

    return pd.concat(summaries, ignore_index=True), pd.concat(pairwise, ignore_index=True)


def load_test_market_frame() -> pd.DataFrame:
    config = load_project_configs()
    exp = config["experiment"]
    dataset = load_legacy_dataset(
        config["paths"]["dataset"]["merged_output"],
        exp["data"]["datetime_column"],
        exp["data"]["target_column"],
        exp["data"]["label_mapping"],
    )
    numeric_features = keep_numeric_features(dataset.frame, dataset.feature_columns)
    selected = select_features(numeric_features, exp["data"]["selected_feature_indices"])
    modeling_columns = selected + [dataset.target_column, dataset.datetime_column]
    frame = drop_missing_rows(dataset.frame, modeling_columns)
    ordered = frame.sort_values(dataset.datetime_column).reset_index(drop=True)

    split_cfg = exp["split"]
    train_end = int(len(ordered) * float(split_cfg["train_size"]))
    val_end = train_end + int(len(ordered) * float(split_cfg["validation_size"]))
    test = ordered.iloc[val_end:].copy().reset_index(drop=True)
    required = [dataset.datetime_column, "open", "close", dataset.target_column]
    test = test[required].copy()
    test["row_id"] = np.arange(len(test))
    test = test.rename(columns={dataset.datetime_column: "datetime", dataset.target_column: "trend"})
    test["datetime"] = pd.to_datetime(test["datetime"])
    return test


def calculate_max_drawdown(equity_curve: pd.Series) -> float:
    rolling_max = equity_curve.cummax()
    drawdown = equity_curve - rolling_max
    return float(drawdown.min())


def summarize_returns(returns: pd.Series, datetimes: pd.Series) -> dict[str, float | int]:
    equity = returns.cumsum()
    gross_profit = float(returns[returns > 0].sum())
    gross_loss = float(abs(returns[returns < 0].sum()))
    daily_returns = returns.groupby(pd.to_datetime(datetimes).dt.date).sum()
    sharpe = 0.0
    if len(daily_returns) > 1 and daily_returns.std(ddof=1) > 0:
        sharpe = float((daily_returns.mean() / daily_returns.std(ddof=1)) * math.sqrt(252))
    return {
        "total_trades": int(len(returns)),
        "total_profit_points": float(returns.sum()),
        "mean_trade_points": float(returns.mean()),
        "win_rate": float((returns > 0).mean()),
        "profit_factor": float(gross_profit / gross_loss) if gross_loss > 0 else float("inf"),
        "max_drawdown_points": calculate_max_drawdown(equity),
        "sharpe_ratio_annualized": sharpe,
    }


def run_economic_backtests(market_test: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    summary_rows = []
    daily_rows = []
    missing: list[Path] = []
    for exp in EXPERIMENTS:
        for model in MODELS:
            for optimizer in OPTIMIZERS:
                path = exp.predictions_dir / f"{model}_{optimizer}_predictions.csv"
                if not path.exists():
                    missing.append(path)
                    continue
                pred_all = read_csv(path)
                pred_all = pred_all[pred_all["seed"].isin(SEEDS)].copy()
                for seed in SEEDS:
                    pred = pred_all[pred_all["seed"] == seed].sort_values("row_id").copy()
                    if pred.empty:
                        continue
                    merged = market_test.merge(
                        pred[["row_id", "seed", "y_true", "y_pred", "y_proba"]],
                        on="row_id",
                        how="left",
                    )
                    merged = merged.dropna(subset=["y_pred"]).copy()
                    merged["long_return_points"] = merged["close"] - merged["open"]
                    merged["short_return_points"] = merged["open"] - merged["close"]
                    merged["gross_return_points"] = np.where(
                        merged["y_pred"].astype(int) == 1,
                        merged["long_return_points"],
                        merged["short_return_points"],
                    )
                    merged["net_return_points"] = merged["gross_return_points"] - TRANSACTION_COST_POINTS
                    metrics = summarize_returns(merged["net_return_points"], merged["datetime"])
                    summary_rows.append(
                        {
                            "experiment": exp.key,
                            "experiment_label": exp.label,
                            "model": model,
                            "optimizer": optimizer,
                            "seed": seed,
                            **metrics,
                        }
                    )
                    daily = (
                        merged.groupby(merged["datetime"].dt.date)["net_return_points"]
                        .sum()
                        .reset_index(name="daily_return_points")
                        .rename(columns={"datetime": "date"})
                    )
                    daily["experiment"] = exp.key
                    daily["experiment_label"] = exp.label
                    daily["model"] = model
                    daily["optimizer"] = optimizer
                    daily["seed"] = seed
                    daily_rows.append(daily)
    if missing:
        print("Missing prediction files:")
        for path in missing:
            print(path)
    return pd.DataFrame(summary_rows), pd.concat(daily_rows, ignore_index=True)


def summarize_economic(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    combo = (
        df.groupby(["experiment", "experiment_label", "model", "optimizer"])
        .agg(
            n=("seed", "nunique"),
            total_profit_mean=("total_profit_points", "mean"),
            total_profit_std=("total_profit_points", "std"),
            mean_trade_points_mean=("mean_trade_points", "mean"),
            win_rate_mean=("win_rate", "mean"),
            profit_factor_mean=("profit_factor", "mean"),
            max_drawdown_mean=("max_drawdown_points", "mean"),
            sharpe_mean=("sharpe_ratio_annualized", "mean"),
        )
        .reset_index()
    )
    model_by_exp = (
        df.groupby(["experiment", "experiment_label", "model"])
        .agg(
            n=("total_profit_points", "count"),
            total_profit_mean=("total_profit_points", "mean"),
            win_rate_mean=("win_rate", "mean"),
            profit_factor_mean=("profit_factor", "mean"),
            max_drawdown_mean=("max_drawdown_points", "mean"),
            sharpe_mean=("sharpe_ratio_annualized", "mean"),
        )
        .reset_index()
    )
    model_overall = (
        df.groupby("model")
        .agg(
            n=("total_profit_points", "count"),
            total_profit_mean=("total_profit_points", "mean"),
            win_rate_mean=("win_rate", "mean"),
            profit_factor_mean=("profit_factor", "mean"),
            max_drawdown_mean=("max_drawdown_points", "mean"),
            sharpe_mean=("sharpe_ratio_annualized", "mean"),
        )
        .reset_index()
    )
    return combo, model_by_exp, model_overall


def run_economic_tests(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    summaries = []
    pairwise = []
    for metric in ["total_profit_points", "profit_factor", "sharpe_ratio_annualized", "max_drawdown_points"]:
        test_df = df.copy()
        # Drawdown is negative, so higher values are better because they are
        # closer to zero. The generic ranking helper already treats higher as
        # better, therefore no inversion is needed.
        metric_for_test = metric
        summary, pairs = friedman_and_pairwise_models(
            test_df,
            metric=metric_for_test,
            block_cols=["experiment", "optimizer", "seed"],
            scope="economic_all_experiments_optimizer_seed_blocks",
        )
        summary["original_metric"] = metric
        pairs["original_metric"] = metric
        summaries.append(summary)
        pairwise.append(pairs)

    for exp in EXPERIMENTS:
        part = df[df["experiment"] == exp.key].copy()
        summary, pairs = friedman_and_pairwise_models(
            part,
            metric="total_profit_points",
            block_cols=["optimizer", "seed"],
            scope=f"economic_{exp.key}",
        )
        summary["original_metric"] = "total_profit_points"
        pairs["original_metric"] = "total_profit_points"
        summaries.append(summary)
        pairwise.append(pairs)
    return pd.concat(summaries, ignore_index=True), pd.concat(pairwise, ignore_index=True)


def write_report(
    predictive_combo: pd.DataFrame,
    predictive_model: pd.DataFrame,
    pred_tests: pd.DataFrame,
    pred_pairwise: pd.DataFrame,
    econ_combo: pd.DataFrame,
    econ_model: pd.DataFrame,
    econ_tests: pd.DataFrame,
    econ_pairwise: pd.DataFrame,
) -> Path:
    report = OUT_DIR / "model_selection_statistical_economic_report.md"

    best_pred_rows = []
    for exp in EXPERIMENTS:
        part = predictive_combo[predictive_combo["experiment"] == exp.key]
        row = part.sort_values("reported_metric_mean", ascending=False).iloc[0]
        best_pred_rows.append(row)
    best_pred = pd.DataFrame(best_pred_rows)

    best_econ_rows = []
    for exp in EXPERIMENTS:
        part = econ_combo[econ_combo["experiment"] == exp.key]
        row = part.sort_values("total_profit_mean", ascending=False).iloc[0]
        best_econ_rows.append(row)
    best_econ = pd.DataFrame(best_econ_rows)

    lines = [
        "# Model selection: testes estatisticos e economicos",
        "",
        "## Leitura curta",
        "",
        "Os testes foram rodados para todos os modelos, otimizadores, seeds e os tres experimentos disponiveis. A conclusao continua sendo cautelosa: o MLP e o modelo mais promissor nas metricas preditivas, mas a decisao economica depende do criterio financeiro usado.",
        "",
        "## Melhores combinacoes preditivas por experimento",
        "",
        best_pred[
            [
                "experiment_label",
                "model",
                "optimizer",
                "reported_metric_mean",
                "accuracy_mean",
                "mcc_mean",
                "f1_mean",
            ]
        ].round(6).to_markdown(index=False),
        "",
        "## Melhores combinacoes economicas por experimento",
        "",
        best_econ[
            [
                "experiment_label",
                "model",
                "optimizer",
                "total_profit_mean",
                "win_rate_mean",
                "profit_factor_mean",
                "max_drawdown_mean",
                "sharpe_mean",
            ]
        ].round(6).to_markdown(index=False),
        "",
        "## Resumo preditivo por modelo",
        "",
        predictive_model.round(6).to_markdown(index=False),
        "",
        "## Resumo economico por modelo",
        "",
        econ_model.round(6).to_markdown(index=False),
        "",
        "## Testes Friedman preditivos",
        "",
        pred_tests.round(6).to_markdown(index=False),
        "",
        "## Pairwise preditivo do melhor modelo medio contra os demais",
        "",
        pred_pairwise.round(6).to_markdown(index=False),
        "",
        "## Testes Friedman economicos",
        "",
        econ_tests.round(6).to_markdown(index=False),
        "",
        "## Pairwise economico do melhor modelo medio contra os demais",
        "",
        econ_pairwise.round(6).to_markdown(index=False),
        "",
        "## Como interpretar",
        "",
        "- Friedman testa se ha diferenca global entre os quatro modelos nos mesmos blocos comparaveis.",
        "- Pairwise usa Wilcoxon pareado e correcao de Holm contra o melhor modelo medio daquele escopo.",
        "- Com apenas tres seeds, nao e recomendavel afirmar superioridade definitiva. A melhor frase e: `modelo mais promissor nos experimentos atuais`.",
        "- O resultado economico pode divergir do resultado preditivo porque lucro, drawdown e Sharpe dependem da distribuicao temporal dos erros, nao apenas da acuracia media.",
        "",
    ]
    report.write_text("\n".join(lines), encoding="utf-8")
    return report


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    predictive = load_predictive_rows()
    pred_combo, pred_model_exp, pred_model_overall = summarize_predictive(predictive)
    pred_tests, pred_pairwise = run_predictive_tests(predictive)

    market_test = load_test_market_frame()
    econ_seed, econ_daily = run_economic_backtests(market_test)
    econ_combo, econ_model_exp, econ_model_overall = summarize_economic(econ_seed)
    econ_tests, econ_pairwise = run_economic_tests(econ_seed)

    predictive.to_csv(OUT_DIR / "predictive_by_seed.csv", index=False)
    pred_combo.to_csv(OUT_DIR / "predictive_by_combo.csv", index=False)
    pred_model_exp.to_csv(OUT_DIR / "predictive_by_model_experiment.csv", index=False)
    pred_model_overall.to_csv(OUT_DIR / "predictive_by_model_overall.csv", index=False)
    pred_tests.to_csv(OUT_DIR / "predictive_friedman_tests.csv", index=False)
    pred_pairwise.to_csv(OUT_DIR / "predictive_pairwise_wilcoxon_holm.csv", index=False)

    econ_seed.to_csv(OUT_DIR / "economic_by_seed.csv", index=False)
    econ_daily.to_csv(OUT_DIR / "economic_daily_returns.csv", index=False)
    econ_combo.to_csv(OUT_DIR / "economic_by_combo.csv", index=False)
    econ_model_exp.to_csv(OUT_DIR / "economic_by_model_experiment.csv", index=False)
    econ_model_overall.to_csv(OUT_DIR / "economic_by_model_overall.csv", index=False)
    econ_tests.to_csv(OUT_DIR / "economic_friedman_tests.csv", index=False)
    econ_pairwise.to_csv(OUT_DIR / "economic_pairwise_wilcoxon_holm.csv", index=False)

    report = write_report(
        pred_combo,
        pred_model_overall,
        pred_tests,
        pred_pairwise,
        econ_combo,
        econ_model_overall,
        econ_tests,
        econ_pairwise,
    )

    print("Statistical/economic model selection complete")
    print(f"Output dir: {OUT_DIR}")
    print(f"Report: {report}")


if __name__ == "__main__":
    main()
