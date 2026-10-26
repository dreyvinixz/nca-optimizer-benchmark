#!/usr/bin/env python3
"""Small one-root, one-fold MLP capacity pilot; uses development dates only."""
import argparse
import json
import resource
import time
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
import yaml
from sklearn.preprocessing import StandardScaler


class EpochTimer(tf.keras.callbacks.Callback):
    def on_epoch_begin(self, epoch, logs=None):
        self.started = time.perf_counter()

    def on_epoch_end(self, epoch, logs=None):
        self.seconds.append(time.perf_counter() - self.started)

    def __init__(self):
        super().__init__()
        self.seconds = []


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--protocol", type=Path, default=Path("config/experiment_protocol.yaml"))
    ap.add_argument("--report", type=Path, default=Path("reports/mlp_pilot.json"))
    a = ap.parse_args()
    contract = yaml.safe_load(a.contract.read_text(encoding="utf-8"))
    protocol = yaml.safe_load(a.protocol.read_text(encoding="utf-8"))
    manifest = json.loads(a.parquet.with_suffix(".manifest.json").read_text(encoding="utf-8"))
    fold = manifest["expanding_folds"][0]
    test_start = manifest["date_ranges"]["test"][0]
    if fold["validation_dates"][1] >= test_start:
        raise ValueError("Pilot fold overlaps test")
    features = contract["features"]["generated"]
    frame = pd.read_parquet(a.parquet, filters=[("date", "<", test_start)])
    usable = frame[features].notna().all(axis=1)
    frame = frame.loc[usable & frame.ticker.str.startswith("WIN")].copy()
    train = frame.date.between(*fold["train_dates"]) & frame.y5.notna()
    valid = frame.date.between(*fold["validation_dates"]) & frame.y5.notna()
    x_train = frame.loc[train, features].to_numpy(dtype=np.float32)
    x_valid = frame.loc[valid, features].to_numpy(dtype=np.float32)
    y_train = frame.loc[train, "y5"].astype(int).to_numpy(dtype=np.float32)
    y_valid = frame.loc[valid, "y5"].astype(int).to_numpy(dtype=np.float32)
    scaler = StandardScaler().fit(x_train)
    x_train = scaler.transform(x_train).astype(np.float32)
    x_valid = scaler.transform(x_valid).astype(np.float32)
    seed = int(protocol["reproducibility"]["seed"])
    tf.keras.utils.set_random_seed(seed)
    gpus = tf.config.list_physical_devices("GPU")
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    if gpus:
        device = "/GPU:0"
    else:
        device = "/CPU:0"
    timer = EpochTimer()
    start = time.perf_counter()
    with tf.device(device):
        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(len(features),)),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dropout(0.10, seed=seed),
            tf.keras.layers.Dense(16, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss="binary_crossentropy", metrics=["binary_accuracy"])
        history = model.fit(x_train, y_train, validation_data=(x_valid, y_valid), batch_size=256, epochs=5, shuffle=False, verbose=0, callbacks=[timer])
        val_loss, val_accuracy = model.evaluate(x_valid, y_valid, batch_size=256, verbose=0)
    elapsed = time.perf_counter() - start
    gpu_mem = None
    if gpus:
        try:
            gpu_mem = tf.config.experimental.get_memory_info("GPU:0")
        except Exception as exc:
            gpu_mem = {"unavailable": str(exc)}
    report = {
        "status": "completed_pretest_capacity_pilot",
        "device": device, "visible_gpus": [str(g.name) for g in gpus],
        "root": "WIN", "target": "trend_5m", "fold": fold,
        "train_rows": len(x_train), "validation_rows": len(x_valid),
        "features": features, "scaler": "StandardScaler fit on pilot training rows only",
        "architecture": [len(features), 32, 16, 1], "dropout": 0.10,
        "batch_size": 256, "epochs": 5, "shuffle": False, "seed": seed,
        "epoch_seconds": [round(x, 4) for x in timer.seconds],
        "samples_per_second": round(len(x_train) * 5 / sum(timer.seconds), 2),
        "total_seconds_including_compile_eval": round(elapsed, 2),
        "validation_loss": float(val_loss), "validation_binary_accuracy": float(val_accuracy),
        "gpu_memory_info_bytes": gpu_mem,
        "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "tensorflow": tf.__version__, "contract_hash": manifest["contract_hash"],
        "protocol_hash": manifest["protocol_hash"], "test_start_excluded": test_start,
    }
    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
