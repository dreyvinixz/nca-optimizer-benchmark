#!/usr/bin/env python3
"""Run a compact MLP on the same four pre-test expanding validation folds."""
import argparse
import json
import resource
import time
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
import yaml
from sklearn.metrics import balanced_accuracy_score, f1_score, matthews_corrcoef
from sklearn.preprocessing import StandardScaler


class EpochTimer(tf.keras.callbacks.Callback):
    def __init__(self):
        super().__init__()
        self.seconds = []

    def on_epoch_begin(self, epoch, logs=None):
        self.started = time.perf_counter()

    def on_epoch_end(self, epoch, logs=None):
        self.seconds.append(time.perf_counter() - self.started)


def score(y, pred):
    return {
        "mcc": float(matthews_corrcoef(y, pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
        "macro_f1": float(f1_score(y, pred, labels=[0, 1], average="macro", zero_division=0)),
        "prevalence_1": float(np.mean(y == 1)),
        "confusion_00": int(np.sum((y == 0) & (pred == 0))),
        "confusion_01": int(np.sum((y == 0) & (pred == 1))),
        "confusion_10": int(np.sum((y == 1) & (pred == 0))),
        "confusion_11": int(np.sum((y == 1) & (pred == 1))),
    }


def main():
    started = time.perf_counter()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--protocol", type=Path, default=Path("config/experiment_protocol.yaml"))
    ap.add_argument("--output", type=Path, default=Path("reports/mlp_cv_summary.csv"))
    a = ap.parse_args()
    contract = yaml.safe_load(a.contract.read_text(encoding="utf-8"))
    protocol = yaml.safe_load(a.protocol.read_text(encoding="utf-8"))
    manifest = json.loads(a.parquet.with_suffix(".manifest.json").read_text(encoding="utf-8"))
    features = contract["features"]["generated"]
    targets = {"trend_5m": "y5", "trend_10m": "y10", "trend_15m": "y15", "majority": "y_majority"}
    test_start = manifest["date_ranges"]["test"][0]
    frame = pd.read_parquet(a.parquet, filters=[("date", "<", test_start)])
    frame = frame.loc[frame[features].notna().all(axis=1)].copy()
    if frame.empty or frame.date.max() >= test_start or (frame.split == "test").any():
        raise ValueError("MLP CV input is empty or contains held-out test data")
    gpus = tf.config.list_physical_devices("GPU")
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    device = "/GPU:0" if gpus else "/CPU:0"
    seed = int(protocol["reproducibility"]["seed"])
    records, fold_rows, epoch_times = [], [], []
    total_fit_seconds = 0.0
    for fold in manifest["expanding_folds"]:
        train_dates = frame.date.between(*fold["train_dates"])
        val_dates = frame.date.between(*fold["validation_dates"])
        if frame.loc[train_dates | val_dates, "split"].eq("test").any():
            raise ValueError(f"Fold {fold['fold']} contains test dates")
        for target_index, (target_name, target_col) in enumerate(targets.items()):
            train = frame.loc[train_dates & frame[target_col].notna()]
            valid = frame.loc[val_dates & frame[target_col].notna()]
            x_train = train[features].to_numpy(dtype=np.float32)
            x_valid = valid[features].to_numpy(dtype=np.float32)
            y_train = train[target_col].astype(int).to_numpy(dtype=np.float32)
            y_valid = valid[target_col].astype(int).to_numpy(dtype=np.int32)
            if len(x_train) == 0 or len(x_valid) == 0 or np.unique(y_train).size < 2:
                raise ValueError(f"Insufficient MLP data in fold {fold['fold']} target {target_name}")
            scaler = StandardScaler().fit(x_train)
            x_train = scaler.transform(x_train).astype(np.float32)
            x_valid = scaler.transform(x_valid).astype(np.float32)
            tf.keras.backend.clear_session()
            tf.keras.utils.set_random_seed(seed + fold["fold"] * 10 + target_index)
            timer = EpochTimer()
            t0 = time.perf_counter()
            with tf.device(device):
                model = tf.keras.Sequential([
                    tf.keras.layers.Input(shape=(len(features),)),
                    tf.keras.layers.Dense(32, activation="relu"),
                    tf.keras.layers.Dropout(0.10, seed=seed + fold["fold"]),
                    tf.keras.layers.Dense(16, activation="relu"),
                    tf.keras.layers.Dense(1, activation="sigmoid"),
                ])
                model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss="binary_crossentropy")
                model.fit(x_train, y_train, batch_size=256, epochs=5, shuffle=False, verbose=0, callbacks=[timer])
                pred = (model.predict(x_valid, batch_size=256, verbose=0).ravel() >= 0.5).astype(np.int32)
            elapsed = time.perf_counter() - t0
            total_fit_seconds += elapsed
            epoch_times.extend(timer.seconds)
            fold_rows.append({"fold": fold["fold"], "target": target_name, "train_rows": len(train), "validation_rows": len(valid), "fit_predict_seconds": round(elapsed, 4), "epoch_seconds": [round(x, 4) for x in timer.seconds]})
            for root in ["ALL", *contract["universe"]["primary_roots"]]:
                mask = np.ones(len(valid), dtype=bool) if root == "ALL" else valid.ticker.str.startswith(root).to_numpy()
                if not mask.any():
                    continue
                record = {
                    "fold": fold["fold"], "target": target_name, "model": "compact_mlp", "root": root,
                    "train_rows": len(train), "validation_rows": int(mask.sum()),
                    "train_start": fold["train_dates"][0], "train_end": fold["train_dates"][1],
                    "validation_start": fold["validation_dates"][0], "validation_end": fold["validation_dates"][1],
                    "fit_predict_seconds": round(elapsed, 4), "seed": seed + fold["fold"] * 10 + target_index,
                    "contract_hash": manifest["contract_hash"], "protocol_hash": manifest["protocol_hash"],
                    "source_market_sha256": manifest["source_sha256"]["market"],
                    "source_labels_sha256": manifest["source_sha256"]["labels"],
                }
                record.update(score(y_valid[mask], pred[mask]))
                records.append(record)
            del model
    a.output.parent.mkdir(parents=True, exist_ok=True)
    results = pd.DataFrame(records)
    results.to_csv(a.output, index=False)
    try:
        gpu_memory = tf.config.experimental.get_memory_info("GPU:0") if gpus else None
    except Exception as exc:
        gpu_memory = {"unavailable": str(exc)}
    run = {
        "status": "completed_pretest_validation_only", "device": device,
        "visible_gpus": [str(g.name) for g in gpus], "test_start_excluded": test_start,
        "usable_pretest_rows": len(frame), "targets": targets, "folds": fold_rows,
        "architecture": [len(features), 32, 16, 1], "dropout": 0.10,
        "batch_size": 256, "epochs": 5, "shuffle": False, "base_seed": seed,
        "mean_epoch_seconds": round(float(np.mean(epoch_times)), 4),
        "total_model_fit_predict_seconds": round(total_fit_seconds, 2),
        "runtime_seconds": round(time.perf_counter() - started, 2),
        "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "gpu_memory_info_bytes": gpu_memory, "tensorflow": tf.__version__,
        "contract_hash": manifest["contract_hash"], "protocol_hash": manifest["protocol_hash"],
        "source_sha256": manifest["source_sha256"], "metrics_file": str(a.output),
    }
    a.output.with_suffix(".json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
    overall = results[results.root == "ALL"].groupby("target").agg(
        mcc_mean=("mcc", "mean"), mcc_sd=("mcc", "std"),
        bacc_mean=("balanced_accuracy", "mean"), bacc_sd=("balanced_accuracy", "std"),
        f1_mean=("macro_f1", "mean"), f1_sd=("macro_f1", "std"),
    ).reset_index()
    lines = ["# Compact MLP cross-validation (development data only)", "",
             "Four expanding folds; Parquet read filters out all test dates. Scaler fit only on each fold's training rows.", "",
             f"- Device: `{device}`; visible GPU(s): {', '.join(run['visible_gpus']) or 'none'}; total runtime {run['runtime_seconds']} s; peak RSS {run['peak_rss_kib']:,} KiB.",
             f"- Architecture 11–32–16–1, dropout 0.10, batch 256, five epochs, no row shuffle. Mean epoch time {run['mean_epoch_seconds']} s.",
             "- Metrics are mean ± standard deviation across folds; this is descriptive because expanding training folds overlap.",
             "- B0 target labels remain retrospective; these validation scores do not establish causal state accuracy or trading performance.",
             "", "| Target | MCC | Balanced accuracy | Macro F1 |", "|---|---:|---:|---:|"]
    for _, row in overall.iterrows():
        lines.append(f"| {row.target} | {row.mcc_mean:.3f} ± {row.mcc_sd:.3f} | {row.bacc_mean:.3f} ± {row.bacc_sd:.3f} | {row.f1_mean:.3f} ± {row.f1_sd:.3f} |")
    a.output.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(run, indent=2))


if __name__ == "__main__":
    main()
