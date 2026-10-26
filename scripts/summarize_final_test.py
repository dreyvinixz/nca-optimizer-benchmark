#!/usr/bin/env python3
"""Complete aggregate test summaries from the one-pass frozen predictions."""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, average_precision_score, balanced_accuracy_score,
    brier_score_loss, cohen_kappa_score, f1_score, log_loss,
    matthews_corrcoef, mean_absolute_error, mean_squared_error,
    precision_score, recall_score, roc_auc_score,
)


TARGETS = {"trend_5m": "y5", "trend_10m": "y10", "trend_15m": "y15"}
MODEL_OUTPUTS = {
    "majority_constant": {**{t: (f"p_dummy_{t}", f"pred_dummy_{t}") for t in TARGETS}, "majority": ("p_dummy_majority", "pred_dummy_majority")},
    "causal_5m_momentum": {t: (f"p_momentum_{t}", f"pred_momentum_{t}") for t in TARGETS},
    "logistic_regression": {t: (f"p_logistic_{t}", f"pred_logistic_{t}") for t in TARGETS},
    "hist_gradient_boosting": {t: (f"p_hist_{t}", f"pred_hist_{t}") for t in TARGETS},
    "independent_mlp": {t: (f"p_ind_{t}", f"pred_ind_{t}") for t in TARGETS},
    "shared_multitask_mlp": {t: (f"p_shared_{t}", f"pred_shared_{t}") for t in TARGETS},
    "majority_mlp": {"majority": ("p_majority", None)},
}


def classification_metrics(y, pred, prob=None):
    y = np.asarray(y, dtype=int)
    pred = np.asarray(pred, dtype=int)
    row = {
        "n": int(len(y)),
        "accuracy": float(accuracy_score(y, pred)),
        "mcc": float(matthews_corrcoef(y, pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
        "macro_f1": float(f1_score(y, pred, labels=[0, 1], average="macro", zero_division=0)),
        "weighted_f1": float(f1_score(y, pred, labels=[0, 1], average="weighted", zero_division=0)),
        "precision_0": float(precision_score(y, pred, pos_label=0, zero_division=0)),
        "recall_0": float(recall_score(y, pred, pos_label=0, zero_division=0)),
        "f1_0": float(f1_score(y, pred, labels=[0], average="macro", zero_division=0)),
        "precision_1": float(precision_score(y, pred, pos_label=1, zero_division=0)),
        "recall_1": float(recall_score(y, pred, pos_label=1, zero_division=0)),
        "f1_1": float(f1_score(y, pred, labels=[1], average="macro", zero_division=0)),
        "specificity": float(recall_score(y, pred, pos_label=0, zero_division=0)),
        "cohen_kappa": float(cohen_kappa_score(y, pred, labels=[0, 1])),
        "prevalence_1": float(np.mean(y == 1)),
        "confusion_00": int(np.sum((y == 0) & (pred == 0))),
        "confusion_01": int(np.sum((y == 0) & (pred == 1))),
        "confusion_10": int(np.sum((y == 1) & (pred == 0))),
        "confusion_11": int(np.sum((y == 1) & (pred == 1))),
    }
    if prob is not None:
        p = np.clip(np.asarray(prob, dtype=float), 1e-7, 1 - 1e-7)
        row["brier"] = float(brier_score_loss(y, p))
        row["log_loss"] = float(log_loss(y, p, labels=[0, 1]))
        row["roc_auc"] = float(roc_auc_score(y, p)) if np.unique(y).size == 2 else np.nan
        row["pr_average_precision"] = float(average_precision_score(y, p)) if np.unique(y).size == 2 else np.nan
        bins = np.linspace(0.0, 1.0, 11)
        bin_ids = np.digitize(p, bins[1:-1], right=False)
        row["ece_10bin"] = float(sum(
            np.mean(bin_ids == b) * abs(np.mean(p[bin_ids == b]) - np.mean(y[bin_ids == b]))
            for b in range(10) if np.any(bin_ids == b)
        ))
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predictions", type=Path, default=Path("tmp/final_test_predictions.parquet"))
    parser.add_argument("--metrics", type=Path, default=Path("reports/final_test_metrics.csv"))
    parser.add_argument("--contract-metrics", type=Path, default=Path("reports/final_test_contract_metrics.csv"))
    parser.add_argument("--report", type=Path, default=Path("reports/final_test.md"))
    args = parser.parse_args()

    predictions = pd.read_parquet(args.predictions)
    test = predictions.loc[predictions.split == "test"].copy()
    old_metrics = pd.read_csv(args.metrics)
    overall = []
    grouped_test = []
    for model, outputs in MODEL_OUTPUTS.items():
        for target, (p_col, pred_col) in outputs.items():
            y_col = TARGETS.get(target, "y_majority")
            for root in ("ALL", "WIN", "IND"):
                root_mask = np.ones(len(test), dtype=bool) if root == "ALL" else test.ticker.str.startswith(root).to_numpy()
                for block in ("overall", 1, 2, 3):
                    block_mask = np.ones(len(test), dtype=bool) if block == "overall" else test.test_block.eq(block).to_numpy()
                    valid = root_mask & block_mask & test[y_col].notna().to_numpy()
                    if not valid.any():
                        continue
                    y = test.loc[valid, y_col].astype(int).to_numpy()
                    p = test.loc[valid, p_col].to_numpy(dtype=float)
                    pred = (p >= 0.5).astype(int) if pred_col is None else test.loc[valid, pred_col].astype(int).to_numpy()
                    row = {"split": "test", "model": model, "target": target, "root": root, "test_block": block, **classification_metrics(y, pred, None if model == "causal_5m_momentum" else p)}
                    grouped_test.append(row)
                    if block == "overall":
                        overall.append(row)

    for model, p_col in (("soft_score_mlp", "p_soft"), ("soft_score_training_mean", "p_soft_constant")):
        valid_soft = test.y_soft.notna()
        for root in ("ALL", "WIN", "IND"):
            root_mask = np.ones(len(test), dtype=bool) if root == "ALL" else test.ticker.str.startswith(root).to_numpy()
            valid = valid_soft.to_numpy() & root_mask
            y = test.loc[valid, "y_soft"].to_numpy(dtype=float)
            p = test.loc[valid, p_col].to_numpy(dtype=float)
            overall.append({"split": "test", "model": model, "target": "mean_score", "root": root, "test_block": "overall", "n": int(valid.sum()), "mae": float(mean_absolute_error(y, p)), "mse": float(mean_squared_error(y, p))})

    # Rebuild all test aggregates, including fixed blocks, from the exact saved
    # one-pass predictions. Validation rows from the frozen runner are retained.
    old_metrics = old_metrics.loc[old_metrics.split != "test"]
    metrics = pd.concat([old_metrics, pd.DataFrame(grouped_test)], ignore_index=True)
    metrics.to_csv(args.metrics, index=False)

    contract_rows = []
    for ticker, contract in test.groupby("ticker", sort=True):
        for model, outputs in MODEL_OUTPUTS.items():
            for target, (p_col, pred_col) in outputs.items():
                y_col = TARGETS.get(target, "y_majority")
                valid = contract[y_col].notna().to_numpy()
                if not valid.any():
                    continue
                y = contract.loc[valid, y_col].astype(int).to_numpy()
                p = contract.loc[valid, p_col].to_numpy(dtype=float)
                pred = (p >= 0.5).astype(int) if pred_col is None else contract.loc[valid, pred_col].astype(int).to_numpy()
                contract_rows.append({"model": model, "target": target, "ticker": ticker, **classification_metrics(y, pred, None if model == "causal_5m_momentum" else p)})
        valid_soft = contract.y_soft.notna().to_numpy()
        for model, p_col in (("soft_score_mlp", "p_soft"), ("soft_score_training_mean", "p_soft_constant")):
            y = contract.loc[valid_soft, "y_soft"].to_numpy(dtype=float)
            p = contract.loc[valid_soft, p_col].to_numpy(dtype=float)
            contract_rows.append({"model": model, "target": "mean_score", "ticker": ticker, "n": int(valid_soft.sum()), "mae": float(mean_absolute_error(y, p)), "mse": float(mean_squared_error(y, p))})
    contract_metrics = pd.DataFrame(contract_rows)
    contract_metrics.to_csv(args.contract_metrics, index=False)

    run_path = args.metrics.with_suffix(".json")
    run = json.loads(run_path.read_text(encoding="utf-8"))
    run["pooled_metrics_supplement"] = {
        "method": "recomputed_from_saved_one_pass_predictions",
        "model_refit_or_rerun": False,
        "rows_added": len(overall),
        "test_group_rows": len(grouped_test),
        "supplementary_metrics": ["accuracy", "precision_recall_f1_per_class", "weighted_f1", "specificity", "cohen_kappa", "roc_auc", "pr_average_precision", "ece_10bin"],
        "auc_probability_source": "saved model scores; omitted for hard-label momentum baseline and continuous mean_score regression target",
        "contract_level_rows": len(contract_metrics),
        "contract_level_path": str(args.contract_metrics),
    }
    run_path.write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")

    common = test[["y5", "y10", "y15"]].notna().all(axis=1)
    primary = {}
    for target, y_col in TARGETS.items():
        frame = test.loc[common]
        y = frame[y_col].astype(int).to_numpy()
        pi = frame[f"pred_ind_{target}"].astype(int).to_numpy()
        ps = frame[f"pred_shared_{target}"].astype(int).to_numpy()
        primary[target] = {
            "n_common": int(len(frame)),
            "independent_mcc": float(matthews_corrcoef(y, pi)),
            "shared_mcc": float(matthews_corrcoef(y, ps)),
            "observed_difference_independent_minus_shared": float(matthews_corrcoef(y, pi) - matthews_corrcoef(y, ps)),
        }

    report = [
        "# Final test evaluation",
        "",
        "Pre-registered models were fit on the fixed training dates. Validation and final test were scored once; no hyperparameters were changed after opening the test.",
        "",
        f"- Final test sessions: {test.date.nunique()} ({test.date.min()}–{test.date.max()}); rows with complete features: {len(test):,}.",
        f"- Device: {run['device']}; runtime {run['runtime_seconds']} s; peak RSS {run['peak_rss_kib']:,} KiB.",
        "- The complete table contains pooled test metrics and all three pre-fixed test blocks by model, target, and root.",
        "- Main contrast uses the common sample with all three targets observed. Bootstrap resamples five-session blocks; test p-values are not reported.",
        "- Probability scores estimate reproduction of retrospective B0 labels only. They are not independently validated market probabilities; there is no profitability claim.",
        "",
        "## Primary paired contrast: pooled MCC and session-block bootstrap",
        "",
        "| Target | Common n | Independent MCC | Shared MCC | Observed difference | Bootstrap 95% CI |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for target, values in primary.items():
        ci = run["paired_test_mcc_block_bootstrap"][target]["ci95"]
        report.append(f"| {target} | {values['n_common']} | {values['independent_mcc']:.4f} | {values['shared_mcc']:.4f} | {values['observed_difference_independent_minus_shared']:.4f} | [{ci[0]:.4f}, {ci[1]:.4f}] |")
    report += ["", "The confidence intervals include zero for all three paired differences. Independent and shared MLPs therefore show no clear separation on this test sample.", "", "## Primary overall metrics (both roots)", "", "| Model | Target | n | MCC | Balanced accuracy | Macro F1 | Brier | Log loss | MAE | MSE |", "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    pooled = pd.DataFrame(overall)
    pooled = pooled.loc[pooled.root == "ALL"].sort_values(["target", "model"])
    for _, row in pooled.iterrows():
        def fmt(column):
            return "—" if column not in row or pd.isna(row[column]) else f"{row[column]:.4f}"
        report.append(f"| {row.model} | {row.target} | {int(row.n)} | {fmt('mcc')} | {fmt('balanced_accuracy')} | {fmt('macro_f1')} | {fmt('brier')} | {fmt('log_loss')} | {fmt('mae')} | {fmt('mse')} |")
    report += ["", "## Supplementary classification metrics", "", "These metrics were computed from the saved one-pass predictions after the primary evaluation. They were not used to refit models, choose models, or tune thresholds. Binary classification metrics use the frozen 0.5 threshold. ROC-AUC uses continuous saved scores; PR-AUC is reported as average precision (AP). ECE uses 10 fixed-width probability bins.", "", "| Model | Target | n | Accuracy | Precision (class 1) | Recall (class 1) | F1 macro | ROC-AUC | PR-AUC (AP) | Specificity | Cohen kappa | ECE |", "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for _, row in pooled.iterrows():
        report.append(f"| {row.model} | {row.target} | {int(row.n)} | {fmt('accuracy')} | {fmt('precision_1')} | {fmt('recall_1')} | {fmt('macro_f1')} | {fmt('roc_auc')} | {fmt('pr_average_precision')} | {fmt('specificity')} | {fmt('cohen_kappa')} | {fmt('ece_10bin')} |")
    report += ["", "## Existing and regression metrics", "", "The complete CSV also retains MCC, balanced accuracy, class-wise precision/recall/F1, prevalence, all four confusion-matrix cells, Brier score, log loss, ECE, MAE, and MSE. MAE/MSE apply to the continuous `mean_score` target; threshold-based classification and AUC metrics do not apply to it.", "", "## Confusion matrices for primary models", "", "Each cell is shown as `actual 0/1 × predicted 0/1`: TN, FP, FN, TP.", "", "| Target | Model | TN | FP | FN | TP |", "|---|---|---:|---:|---:|---:|"]
    for _, row in pooled.loc[pooled.target.isin(TARGETS) & pooled.model.isin(["independent_mlp", "shared_multitask_mlp", "hist_gradient_boosting"])].sort_values(["target", "model"]).iterrows():
        report.append(f"| {row.target} | {row.model} | {int(row.confusion_00)} | {int(row.confusion_01)} | {int(row.confusion_10)} | {int(row.confusion_11)} |")
    report += ["", "## Primary models by root", "", "| Target | Root | Model | n | MCC | Balanced accuracy | Macro F1 |", "|---|---|---|---:|---:|---:|---:|"]
    root_rows = pd.DataFrame(overall)
    root_rows = root_rows.loc[root_rows.root.isin(["WIN", "IND"]) & root_rows.target.isin(TARGETS) & root_rows.model.isin(["independent_mlp", "shared_multitask_mlp", "hist_gradient_boosting"])]
    for _, row in root_rows.sort_values(["target", "root", "model"]).iterrows():
        report.append(f"| {row.target} | {row.root} | {row.model} | {int(row.n)} | {row.mcc:.4f} | {row.balanced_accuracy:.4f} | {row.macro_f1:.4f} |")
    report += ["", "## Primary models by fixed time block", "", "| Target | Block | Model | n | MCC | Balanced accuracy | Macro F1 |", "|---|---:|---|---:|---:|---:|---:|"]
    block_rows = metrics.loc[(metrics.split == "test") & (metrics.root == "ALL") & metrics.target.isin(TARGETS) & metrics.model.isin(["independent_mlp", "shared_multitask_mlp", "hist_gradient_boosting"]) & metrics.test_block.notna() & (metrics.test_block.astype(str) != "overall")]
    for _, row in block_rows.sort_values(["target", "test_block", "model"]).iterrows():
        report.append(f"| {row.target} | {int(float(row.test_block))} | {row.model} | {int(row.n)} | {row.mcc:.4f} | {row.balanced_accuracy:.4f} | {row.macro_f1:.4f} |")
    report += ["", "## Contract-level sensitivity (descriptive)", "", "Performance is also retained per ticker/contract in `final_test_contract_metrics.csv`; the contracts remain separate, with no continuous-series stitching. These small-contract summaries are descriptive and are not used for model selection or inferential claims.", ""]
    soft = pooled.loc[pooled.target == "mean_score"].set_index("model")
    soft_mae_gain = 1 - soft.loc["soft_score_mlp", "mae"] / soft.loc["soft_score_training_mean", "mae"]
    soft_mse_gain = 1 - soft.loc["soft_score_mlp", "mse"] / soft.loc["soft_score_training_mean", "mse"]
    report += [
        "",
        "## Interpretation",
        "",
        "The independent and shared MLPs are effectively tied: all three paired confidence intervals include zero. On the 5-minute target, the independent MLP is close to logistic regression and HistGradientBoosting; on 10- and 15-minute targets, HistGradientBoosting has the highest pooled MCC among the listed models. Root-level results are broadly similar, while the 15-minute scores increase in the final time block for all three displayed models.",
        f"The soft-score MLP improves over the training-mean constant by {soft_mae_gain:.1%} in MAE and {soft_mse_gain:.1%} in MSE. This measures reproduction of the B0 vote fraction only.",
        "",
        "These are predictions of retrospective B0 labels, not independent market truth. The analysis covers only WIN/IND in January–June 2026, has no executable trading or profitability evaluation, and does not establish an edge. B1/B2/Fuzzy coverage is insufficient for an independent-label comparison.",
        "",
        "Reproduction: run the committed one-pass model evaluator only before opening the final test, then run `scripts/summarize_final_test.py` to derive pooled and subgroup tables from its saved predictions. The supplement script does not fit models or rerun test scoring. The final test was already opened for this study; do not use it for further model or hyperparameter selection.",
        "",
    ]
    args.report.write_text("\n".join(report), encoding="utf-8")
    print(f"Added {len(overall)} pooled metric rows; wrote {args.report}")


if __name__ == "__main__":
    main()
