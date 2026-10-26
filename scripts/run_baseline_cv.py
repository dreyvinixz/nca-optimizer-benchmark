#!/usr/bin/env python3
"""Run CPU-only baseline CV on pre-test expanding folds; never score test rows."""
import argparse
import json
import platform
import resource
import time
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score, matthews_corrcoef
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import yaml


def metrics(y_true, y_pred):
    return {
        "mcc": float(matthews_corrcoef(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, labels=[0, 1], average="macro", zero_division=0)),
        "prevalence_1": float(np.mean(y_true == 1)),
        "confusion_00": int(np.sum((y_true == 0) & (y_pred == 0))),
        "confusion_01": int(np.sum((y_true == 0) & (y_pred == 1))),
        "confusion_10": int(np.sum((y_true == 1) & (y_pred == 0))),
        "confusion_11": int(np.sum((y_true == 1) & (y_pred == 1))),
    }


def main():
    started = time.perf_counter()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--protocol", type=Path, default=Path("config/experiment_protocol.yaml"))
    ap.add_argument("--output", type=Path, default=Path("reports/baseline_cv_summary.csv"))
    ap.add_argument("--report", type=Path, default=Path("reports/baseline_cv.md"))
    a = ap.parse_args()
    contract = yaml.safe_load(a.contract.read_text(encoding="utf-8"))
    protocol = yaml.safe_load(a.protocol.read_text(encoding="utf-8"))
    manifest = json.loads(a.parquet.with_suffix(".manifest.json").read_text(encoding="utf-8"))
    features = contract["features"]["generated"]
    targets = {"trend_5m": "y5", "trend_10m": "y10", "trend_15m": "y15", "majority": "y_majority"}
    test_start = manifest["date_ranges"]["test"][0]
    # Filter out the held-out test period at read time. It cannot be scored here.
    frame = pd.read_parquet(a.parquet, filters=[("date", "<", test_start)])
    ready = frame[features].notna().all(axis=1)
    frame = frame.loc[ready].copy()
    if frame.empty or frame.date.max() >= test_start or (frame.split == "test").any():
        raise ValueError("Pre-test CV input contains no usable rows or includes held-out test dates")
    seed = int(protocol["reproducibility"]["seed"])
    records = []
    fold_log = []
    for fold in manifest["expanding_folds"]:
        train_start, train_end = fold["train_dates"]
        val_start, val_end = fold["validation_dates"]
        train_date = frame.date.between(train_start, train_end)
        val_date = frame.date.between(val_start, val_end)
        if frame.loc[train_date, "split"].eq("test").any() or frame.loc[val_date, "split"].eq("test").any():
            raise ValueError(f"Fold {fold['fold']} crosses into test")
        fold_log.append({"fold": fold["fold"], "train_dates": fold["train_dates"], "validation_dates": fold["validation_dates"], "train_ready_rows": int(train_date.sum()), "validation_ready_rows": int(val_date.sum())})
        for target_name, target_col in targets.items():
            train_mask = train_date & frame[target_col].notna()
            val_mask = val_date & frame[target_col].notna()
            train = frame.loc[train_mask]
            valid = frame.loc[val_mask]
            if train.empty or valid.empty or train[target_col].nunique() < 2:
                raise ValueError(f"Insufficient train/validation data for {target_name}, fold {fold['fold']}")
            x_train = train[features].to_numpy(dtype=np.float32)
            y_train = train[target_col].astype(int).to_numpy()
            x_valid = valid[features].to_numpy(dtype=np.float32)
            y_valid = valid[target_col].astype(int).to_numpy()
            models = {
                "majority": DummyClassifier(strategy="most_frequent"),
                "logistic_regression": Pipeline([
                    ("scaler", StandardScaler()),
                    ("model", LogisticRegression(C=1.0, max_iter=250, random_state=seed)),
                ]),
                "hist_gradient_boosting": HistGradientBoostingClassifier(
                    learning_rate=0.1, max_iter=50, max_leaf_nodes=15,
                    l2_regularization=1.0, early_stopping=False, random_state=seed,
                ),
            }
            for model_name, model in models.items():
                t0 = time.perf_counter()
                model.fit(x_train, y_train)
                pred = model.predict(x_valid)
                elapsed = time.perf_counter() - t0
                for root in ["ALL", *contract["universe"]["primary_roots"]]:
                    mask = np.ones(len(valid), dtype=bool) if root == "ALL" else valid.ticker.str.startswith(root).to_numpy()
                    if not mask.any():
                        continue
                    row = {
                        "fold": fold["fold"], "target": target_name, "model": model_name, "root": root,
                        "train_rows": len(train), "validation_rows": int(mask.sum()),
                        "train_start": train_start, "train_end": train_end,
                        "validation_start": val_start, "validation_end": val_end,
                        "fit_predict_seconds": round(elapsed, 4),
                        "seed": seed, "contract_hash": manifest["contract_hash"],
                        "protocol_hash": manifest["protocol_hash"],
                        "source_market_sha256": manifest["source_sha256"]["market"],
                        "source_labels_sha256": manifest["source_sha256"]["labels"],
                    }
                    row.update(metrics(y_valid[mask], pred[mask]))
                    records.append(row)
            # A causal momentum direction baseline uses only the completed
            # current five-minute return. The previous B0 label is excluded:
            # B4 has no confirmation timestamp proving it was observable then.
            momentum = (valid.log_return_5m.to_numpy() >= 0).astype(int)
            for root in ["ALL", *contract["universe"]["primary_roots"]]:
                mask = np.ones(len(valid), dtype=bool) if root == "ALL" else valid.ticker.str.startswith(root).to_numpy()
                if not mask.any():
                    continue
                row = {"fold": fold["fold"], "target": target_name, "model": "causal_5m_momentum", "root": root,
                       "train_rows": len(train), "validation_rows": int(mask.sum()),
                       "train_start": train_start, "train_end": train_end,
                       "validation_start": val_start, "validation_end": val_end,
                       "fit_predict_seconds": 0.0, "seed": seed,
                       "contract_hash": manifest["contract_hash"], "protocol_hash": manifest["protocol_hash"],
                       "source_market_sha256": manifest["source_sha256"]["market"],
                       "source_labels_sha256": manifest["source_sha256"]["labels"]}
                row.update(metrics(y_valid[mask], momentum[mask]))
                records.append(row)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    results = pd.DataFrame(records)
    results.to_csv(a.output, index=False)
    try:
        peak_memory_kib = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    except Exception:
        peak_memory_kib = None
    run = {
        "status": "completed_pretest_validation_only",
        "test_start_date_excluded": test_start,
        "rows_loaded_before_test_filter": "Parquet reader applies date filter; only returned pre-test rows used",
        "usable_pretest_rows": len(frame), "usable_features": features,
        "targets": targets, "folds": fold_log,
        "candidate_models": ["majority", "logistic_regression", "hist_gradient_boosting", "causal_5m_momentum"],
        "persistence_baseline": "omitted because B4 has no confirmation timestamp establishing past-label availability",
        "metrics_file": str(a.output), "report_file": str(a.report), "runtime_seconds": round(time.perf_counter() - started, 2),
        "peak_rss_kib": peak_memory_kib, "python": platform.python_version(), "pandas": pd.__version__, "numpy": np.__version__, "scikit_learn": sklearn.__version__,
        "contract_hash": manifest["contract_hash"], "protocol_hash": manifest["protocol_hash"],
        "source_sha256": manifest["source_sha256"],
    }
    a.output.with_suffix(".json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
    overall = results[results.root == "ALL"].groupby(["target", "model"], sort=True).agg(
        mcc_mean=("mcc", "mean"), mcc_sd=("mcc", "std"),
        bacc_mean=("balanced_accuracy", "mean"), bacc_sd=("balanced_accuracy", "std"),
        f1_mean=("macro_f1", "mean"), f1_sd=("macro_f1", "std"),
        validation_rows_mean=("validation_rows", "mean"), seconds_mean=("fit_predict_seconds", "mean"),
    ).reset_index()
    rootwise = results[(results.model == "logistic_regression") & (results.root != "ALL")].groupby(["target", "root"], sort=True).agg(
        mcc_mean=("mcc", "mean"), mcc_sd=("mcc", "std"),
        bacc_mean=("balanced_accuracy", "mean"), bacc_sd=("balanced_accuracy", "std"),
        f1_mean=("macro_f1", "mean"), f1_sd=("macro_f1", "std"),
    ).reset_index()
    def score(x, s):
        return f"{x:.3f} ± {s:.3f}"
    lines = [
        "# CPU baseline cross-validation (development data only)", "",
        "Four expanding folds on pre-test dates. The final test period was excluded by the Parquet reader and has no metrics in this report.", "",
        f"- Run time: {run['runtime_seconds']} s; peak RSS: {run['peak_rss_kib']:,} KiB.",
        f"- Eligible pre-test rows: {run['usable_pretest_rows']:,}; feature rows with incomplete warm-up are excluded, no imputation is fitted.",
        f"- Input date cutoff: before `{test_start}`. Scalers are inside the logistic regression Pipeline, fitted only on each fold's training rows.",
        f"- Hashes: contract `{run['contract_hash']}`, protocol `{run['protocol_hash']}`, market `{run['source_sha256']['market']}`, B4 `{run['source_sha256']['labels']}`.",
        "- Metrics are mean ± standard deviation across four chronological validation blocks. Folds have expanding, overlapping training periods, so this spread is descriptive, not an independent confidence interval.",
        "- B0 labels are retrospective. These scores measure prediction of that label construction, not causal market-state accuracy or trading performance.",
        "- Persistence of the previous B0 label is omitted: B4 does not store the confirmation time proving that label was available at the next minute.",
        "", "## Pooled roots", "", "| Target | Model | MCC | Balanced accuracy | Macro F1 | Mean validation rows | Mean fit + predict seconds |", "|---|---|---:|---:|---:|---:|---:|",
    ]
    for _, row in overall.iterrows():
        lines.append(f"| {row.target} | {row.model} | {score(row.mcc_mean,row.mcc_sd)} | {score(row.bacc_mean,row.bacc_sd)} | {score(row.f1_mean,row.f1_sd)} | {row.validation_rows_mean:,.0f} | {row.seconds_mean:.3f} |")
    lines += ["", "## Logistic regression by root", "", "| Target | Root | MCC | Balanced accuracy | Macro F1 |", "|---|---|---:|---:|---:|"]
    for _, row in rootwise.iterrows():
        lines.append(f"| {row.target} | {row.root} | {score(row.mcc_mean,row.mcc_sd)} | {score(row.bacc_mean,row.bacc_sd)} | {score(row.f1_mean,row.f1_sd)} |")
    lines += ["", "Full fold, class prevalence, confusion matrices, and per-root outputs are in `baseline_cv_summary.csv`. No hyperparameter search was performed.", ""]
    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.report.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(run, indent=2))


if __name__ == "__main__":
    main()
