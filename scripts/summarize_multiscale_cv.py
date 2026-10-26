#!/usr/bin/env python3
"""Render compact, test-free summaries from completed Phase 5 fold metrics."""
import argparse
import json
from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import yaml


def fmt(mean, sd):
    if pd.isna(mean):
        return "—"
    return f"{mean:.3f}" if pd.isna(sd) else f"{mean:.3f} ± {sd:.3f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metrics", type=Path, default=Path("reports/multiscale_cv_summary.csv"))
    ap.add_argument("--run", type=Path, default=Path("reports/multiscale_cv_summary.json"))
    ap.add_argument("--manifest", type=Path, default=Path("data/derived/win_ind_features_v1.manifest.json"))
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--predictions", type=Path, default=Path("tmp/phase5_multiscale_predictions.parquet"))
    ap.add_argument("--output", type=Path, default=Path("reports/multiscale_cv.md"))
    a = ap.parse_args()
    metrics = pd.read_csv(a.metrics)
    run = json.loads(a.run.read_text(encoding="utf-8"))
    manifest = json.loads(a.manifest.read_text(encoding="utf-8"))
    if run["status"] != "completed_pretest_multiscale_cv" or run["test_metrics_opened"]:
        raise SystemExit("Run metadata does not establish a completed pre-test-only CV")
    protocol = yaml.safe_load(a.contract.read_text(encoding="utf-8"))
    feature_cols = protocol["features"]["generated"]
    test_start = manifest["date_ranges"]["test"][0]
    pretest = pd.read_parquet(a.parquet, filters=[("date", "<", test_start)])
    pretest = pretest.loc[pretest[feature_cols].notna().all(axis=1)]
    predictions = pd.read_parquet(a.predictions)
    constants = []
    for fold in manifest["expanding_folds"]:
        train = pretest.loc[pretest.date.between(*fold["train_dates"]) & pretest.y_soft.notna()]
        all_validation = predictions.loc[predictions.fold == fold["fold"]]
        validation = all_validation.loc[all_validation.y_soft.notna()]
        train_mean = float(train.y_soft.mean())
        for root in ["ALL", *protocol["universe"]["primary_roots"]]:
            all_root_mask = np.ones(len(all_validation), dtype=bool) if root == "ALL" else all_validation.ticker.str.startswith(root).to_numpy()
            valid_root_mask = np.ones(len(validation), dtype=bool) if root == "ALL" else validation.ticker.str.startswith(root).to_numpy()
            part = validation.loc[valid_root_mask]
            if part.empty:
                continue
            true = part.y_soft.to_numpy(dtype=float)
            pred = [train_mean] * len(part)
            denominator = int(all_root_mask.sum())
            constants.append({"fold": fold["fold"], "architecture": "training_mean_constant", "target": "mean_score", "root": root, "sample": "common_intersection", "coverage": float(len(part) / denominator) if denominator else 0.0, "n": len(part), "mae": float(mean_absolute_error(true, pred)), "mse": float(mean_squared_error(true, pred)), "train_mean_score": train_mean, "train_rows": len(train)})
    if constants and not metrics["architecture"].eq("training_mean_constant").any():
        metrics = pd.concat([metrics, pd.DataFrame(constants)], ignore_index=True)
        metrics.to_csv(a.metrics, index=False)
    overall = metrics[(metrics.root == "ALL") & metrics["architecture"].isin(["independent", "shared_multitask"]) & metrics["sample"].isin(["common_intersection", "selective_unanimous_predictions"])].groupby(["architecture", "target", "sample"]).agg(
        mcc_mean=("mcc", "mean"), mcc_sd=("mcc", "std"),
        bacc_mean=("balanced_accuracy", "mean"), bacc_sd=("balanced_accuracy", "std"),
        f1_mean=("macro_f1", "mean"), f1_sd=("macro_f1", "std"),
        coverage_mean=("coverage", "mean"),
    ).reset_index()
    hard = metrics[(metrics.root == "ALL") & metrics["architecture"].eq("majority_target")].groupby("architecture").agg(
        mcc_mean=("mcc", "mean"), mcc_sd=("mcc", "std"),
        bacc_mean=("balanced_accuracy", "mean"), bacc_sd=("balanced_accuracy", "std"),
        f1_mean=("macro_f1", "mean"), f1_sd=("macro_f1", "std"),
    ).loc["majority_target"]
    soft = metrics[(metrics.root == "ALL") & metrics["architecture"].eq("soft_score_regression")][["mae", "mse"]].agg(["mean", "std"])
    soft_constant = metrics[(metrics.root == "ALL") & metrics["architecture"].eq("training_mean_constant")][["mae", "mse"]].agg(["mean", "std"])
    rootwise = metrics[(metrics.root != "ALL") & metrics["architecture"].isin(["independent", "shared_multitask"]) & metrics["sample"].eq("common_intersection")].groupby(["architecture", "target", "root"]).agg(mcc_mean=("mcc", "mean"), mcc_sd=("mcc", "std"), bacc_mean=("balanced_accuracy", "mean"), bacc_sd=("balanced_accuracy", "std"), coverage_mean=("coverage", "mean")).reset_index()
    lines = [
        "# Multi-scale model comparison (pre-test folds)", "",
        "Four expanding validation folds; the final test period was excluded. Full fold/root metrics are in `multiscale_cv_summary.csv`; the row-level prediction cache is local in ignored `tmp/`.", "",
        f"- Device `{run['device']}`, runtime {run['runtime_seconds']} s, peak RSS {run['peak_rss_kib']:,} KiB, temporary prediction cache {run['prediction_bytes']:,} bytes.",
        "- Independent and shared models use identical folds and the common three-label intersection for paired headline scores. Fold mean ± SD is descriptive because expanding training windows overlap.",
        "- Selective acceptance requires unanimous predictions from the model's three heads; coverage is listed with performance. The rule uses model predictions, not future target values.",
        "- Reference unanimous/discordant target strata are descriptive and unavailable at prediction time; do not use them as an operational filter.",
        "- `mean_score` remains a deterministic vote fraction. Its regression errors do not make it a calibrated or independently validated probability.",
        "- Labels remain retrospective B0 references; results do not establish causal market-state accuracy or trading performance. No test metrics were opened.",
        "", "## Paired independent vs shared-head scores", "",
        "| Architecture | Target | Sample | MCC | Balanced accuracy | Macro F1 | Coverage |", "|---|---|---|---:|---:|---:|---:|",
    ]
    for _, r in overall.iterrows():
        lines.append(f"| {r.architecture} | {r.target} | {r['sample']} | {fmt(r.mcc_mean,r.mcc_sd)} | {fmt(r.bacc_mean,r.bacc_sd)} | {fmt(r.f1_mean,r.f1_sd)} | {r.coverage_mean:.3f} |")
    lines += ["", "## Hard majority and soft-score models", "", f"- Majority MLP on the common intersection: MCC {fmt(hard.mcc_mean,hard.mcc_sd)}, balanced accuracy {fmt(hard.bacc_mean,hard.bacc_sd)}, macro-F1 {fmt(hard.f1_mean,hard.f1_sd)}.", f"- Mean-score regression on the common intersection: MAE {fmt(soft.loc['mean','mae'],soft.loc['std','mae'])}, MSE {fmt(soft.loc['mean','mse'],soft.loc['std','mse'])}; the training-mean constant baseline gives MAE {fmt(soft_constant.loc['mean','mae'],soft_constant.loc['std','mae'])}, MSE {fmt(soft_constant.loc['mean','mse'],soft_constant.loc['std','mse'])}.", "", "## Independent and shared scores by root", "", "| Architecture | Target | Root | MCC | Balanced accuracy | Coverage |", "|---|---|---|---:|---:|---:|"]
    for _, r in rootwise.iterrows():
        lines.append(f"| {r.architecture} | {r.target} | {r.root} | {fmt(r.mcc_mean,r.mcc_sd)} | {fmt(r.bacc_mean,r.bacc_sd)} | {r.coverage_mean:.3f} |")
    lines += ["", "## Provenance", "", f"- Contract/protocol SHA-256: `{manifest['contract_hash']}` / `{manifest['protocol_hash']}`.", f"- Market/B4 SHA-256: `{manifest['source_sha256']['market']}` / `{manifest['source_sha256']['labels']}`.", "- The previous-label persistence model remains omitted because B4 has no confirmation timestamp proving that a prior label was observable.", ""]
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {a.output}")


if __name__ == "__main__":
    main()
