#!/usr/bin/env python3
"""Session/block inference for paired Phase 5 predictions; development only."""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon
from sklearn.metrics import balanced_accuracy_score, brier_score_loss, log_loss, matthews_corrcoef
import yaml


def holm_adjust(p_values):
    order = np.argsort(p_values)
    adjusted = np.empty(len(p_values), dtype=float)
    running = 0.0
    m = len(p_values)
    for rank, index in enumerate(order):
        running = max(running, (m - rank) * float(p_values[index]))
        adjusted[index] = min(1.0, running)
    return adjusted


def block_bootstrap_mean(diffs, block_len, replicates, seed):
    rng = np.random.default_rng(seed)
    n = len(diffs)
    nblocks = int(np.ceil(n / block_len))
    samples = np.empty(replicates, dtype=float)
    for i in range(replicates):
        starts = rng.integers(0, n, size=nblocks)
        indices = np.concatenate([(start + np.arange(block_len)) % n for start in starts])[:n]
        samples[i] = np.mean(diffs[indices])
    return np.quantile(samples, [0.025, 0.975]).tolist()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--predictions", type=Path, default=Path("tmp/phase5_multiscale_predictions.parquet"))
    ap.add_argument("--protocol", type=Path, default=Path("config/final_evaluation.yaml"))
    ap.add_argument("--output", type=Path, default=Path("reports/development_inference.csv"))
    ap.add_argument("--report", type=Path, default=Path("reports/development_inference.md"))
    a = ap.parse_args()
    protocol = yaml.safe_load(a.protocol.read_text(encoding="utf-8"))
    frame = pd.read_parquet(a.predictions)
    if frame.empty or frame.date.max() >= protocol["final_test"]["first_date"]:
        raise SystemExit("Development predictions overlap the final test period")
    frame["date"] = frame.date.astype(str)
    common = frame[["y5", "y10", "y15"]].notna().all(axis=1)
    targets = {"trend_5m": ("y5", "pred_ind_trend_5m", "pred_shared_trend_5m", "p_ind_trend_5m", "p_shared_trend_5m"),
               "trend_10m": ("y10", "pred_ind_trend_10m", "pred_shared_trend_10m", "p_ind_trend_10m", "p_shared_trend_10m"),
               "trend_15m": ("y15", "pred_ind_trend_15m", "pred_shared_trend_15m", "p_ind_trend_15m", "p_shared_trend_15m")}
    session_results = []
    inferential = []
    p_values = []
    for target, (y_col, p_ind, p_shared, prob_ind, prob_shared) in targets.items():
        diffs = []
        for date, group in frame.loc[common].groupby("date", sort=True):
            y = group[y_col].astype(int).to_numpy()
            pred_i = group[p_ind].astype(int).to_numpy()
            pred_s = group[p_shared].astype(int).to_numpy()
            bacc_i = float(balanced_accuracy_score(y, pred_i))
            bacc_s = float(balanced_accuracy_score(y, pred_s))
            mcc_i = float(matthews_corrcoef(y, pred_i))
            mcc_s = float(matthews_corrcoef(y, pred_s))
            diff = mcc_i - mcc_s
            diffs.append(diff)
            session_results.append({"date": date, "target": target, "n": len(group), "classes_present": int(np.unique(y).size), "independent_mcc": mcc_i, "shared_mcc": mcc_s, "difference_independent_minus_shared": diff, "independent_balanced_accuracy": bacc_i, "shared_balanced_accuracy": bacc_s})
        diffs = np.asarray(diffs)
        if len(diffs) < 10:
            raise ValueError(f"Too few paired sessions for {target}: {len(diffs)}")
        try:
            p = float(wilcoxon(diffs, zero_method="pratt", alternative="two-sided", method="approx").pvalue)
        except ValueError:
            p = 1.0
        p_values.append(p)
        ci = block_bootstrap_mean(diffs, int(protocol["development_inference"]["confidence_interval"]["block_length_sessions"]), int(protocol["development_inference"]["confidence_interval"]["replicates"]), int(protocol["development_inference"]["confidence_interval"]["seed"]))
        group = frame.loc[common]
        y_all = group[y_col].astype(int).to_numpy()
        inferential.append({"target": target, "sessions": int(len(diffs)), "sessions_with_both_classes": int(sum(x["classes_present"] == 2 for x in session_results if x["target"] == target)), "mean_session_mcc_difference": float(diffs.mean()), "median_session_mcc_difference": float(np.median(diffs)), "positive_session_differences": int((diffs > 0).sum()), "wilcoxon_p_unadjusted": p, "bootstrap_ci95_block5": ci,
                            "independent_brier": float(brier_score_loss(y_all, group[prob_ind].to_numpy())), "shared_brier": float(brier_score_loss(y_all, group[prob_shared].to_numpy())), "independent_log_loss": float(log_loss(y_all, group[prob_ind].to_numpy(), labels=[0, 1])), "shared_log_loss": float(log_loss(y_all, group[prob_shared].to_numpy(), labels=[0, 1]))})
    adjusted = holm_adjust(p_values)
    for row, p_adj in zip(inferential, adjusted):
        row["wilcoxon_p_holm_3_targets"] = float(p_adj)
    daily = pd.DataFrame(session_results)
    by_root = []
    for root in ["WIN", "IND"]:
        root_mask = frame.ticker.str.startswith(root)
        for target, (y_col, p_ind, p_shared, _, _) in targets.items():
            sub = frame.loc[root_mask & common]
            for date, group in sub.groupby("date", sort=True):
                y = group[y_col].astype(int).to_numpy()
                by_root.append({"root": root, "date": date, "target": target, "n": len(group), "independent_bacc": float(balanced_accuracy_score(y, group[p_ind].astype(int))), "shared_bacc": float(balanced_accuracy_score(y, group[p_shared].astype(int)))})
    a.output.parent.mkdir(parents=True, exist_ok=True)
    daily.to_csv(a.output, index=False)
    report = ["# Development generalization and paired inference", "", "Exploratory analysis of the 40 out-of-fold validation sessions only. The final test dates are absent. The daily session is the inference unit; candle counts are never used as independent sample size.", "", "The primary paired contrast is independent MLP minus shared multi-task MLP on per-session MCC, restricted to the common three-target intersection. Two-sided Wilcoxon signed-rank p-values are Holm-adjusted across the three targets. Confidence intervals use a 5-session circular moving-block bootstrap (10,000 replicates). These CV comparisons remain developmental and do not replace the fixed final test.", "", "| Target | Sessions | Both classes present | Mean MCC diff | 95% block-bootstrap CI | Wilcoxon p | Holm p | Independent/shared Brier | Independent/shared log loss |", "|---|---:|---:|---:|---|---:|---:|---:|---:|"]
    for row in inferential:
        ci = row["bootstrap_ci95_block5"]
        report.append(f"| {row['target']} | {row['sessions']} | {row['sessions_with_both_classes']} | {row['mean_session_mcc_difference']:.4f} | [{ci[0]:.4f}, {ci[1]:.4f}] | {row['wilcoxon_p_unadjusted']:.4g} | {row['wilcoxon_p_holm_3_targets']:.4g} | {row['independent_brier']:.4f} / {row['shared_brier']:.4f} | {row['independent_log_loss']:.4f} / {row['shared_log_loss']:.4f} |")
    report += ["", "## Root summary", "", "| Root | Target | Sessions | Independent mean BAcc | Shared mean BAcc |", "|---|---|---:|---:|---:|"]
    root_summary = pd.DataFrame(by_root).groupby(["root", "target"]).agg(sessions=("date", "nunique"), independent=("independent_bacc", "mean"), shared=("shared_bacc", "mean")).reset_index()
    for _, row in root_summary.iterrows():
        report.append(f"| {row.root} | {row.target} | {row.sessions} | {row.independent:.4f} | {row.shared:.4f} |")
    report += ["", "Brier and log loss describe probability forecasts of reproducing the retrospective B0 labels. Calibration against these labels is not independent truth. The report is not a profitability analysis.", ""]
    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.report.write_text("\n".join(report), encoding="utf-8")
    a.output.with_suffix(".json").write_text(json.dumps({"status": "development_only_no_test", "targets": inferential, "holm_family": 3, "date_count": int(daily.date.nunique())}, indent=2) + "\n", encoding="utf-8")
    print(a.report)


if __name__ == "__main__":
    main()
