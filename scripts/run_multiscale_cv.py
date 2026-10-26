#!/usr/bin/env python3
"""Paired separate-head vs shared multi-scale MLP evaluation on pre-test folds."""
import argparse
import json
import resource
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
import yaml
from sklearn.metrics import balanced_accuracy_score, f1_score, matthews_corrcoef, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler


TARGETS = {"trend_5m": "y5", "trend_10m": "y10", "trend_15m": "y15"}


def binary_model(input_dim, seed, multi=False, regression=False):
    tf.keras.utils.set_random_seed(seed)
    x_in = tf.keras.layers.Input(shape=(input_dim,))
    x = tf.keras.layers.Dense(32, activation="relu")(x_in)
    x = tf.keras.layers.Dropout(0.10, seed=seed)(x)
    x = tf.keras.layers.Dense(16, activation="relu")(x)
    if multi:
        out = {name: tf.keras.layers.Dense(1, activation="sigmoid", name=name)(x) for name in TARGETS}
        model = tf.keras.Model(x_in, out)
        model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss={name: tf.keras.losses.BinaryCrossentropy() for name in TARGETS})
    else:
        out = tf.keras.layers.Dense(1, activation="sigmoid")(x)
        model = tf.keras.Model(x_in, out)
        model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss="mse" if regression else "binary_crossentropy")
    return model


def classification_metrics(y, pred):
    return {
        "n": int(len(y)), "mcc": float(matthews_corrcoef(y, pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
        "macro_f1": float(f1_score(y, pred, labels=[0, 1], average="macro", zero_division=0)),
        "prevalence_1": float(np.mean(y == 1)),
    }


def main():
    started = time.perf_counter()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--protocol", type=Path, default=Path("config/experiment_protocol.yaml"))
    ap.add_argument("--predictions", type=Path, default=Path("tmp/phase5_multiscale_predictions.parquet"))
    ap.add_argument("--metrics", type=Path, default=Path("reports/multiscale_cv_summary.csv"))
    ap.add_argument("--report", type=Path, default=Path("reports/multiscale_cv.md"))
    a = ap.parse_args()
    contract = yaml.safe_load(a.contract.read_text(encoding="utf-8"))
    protocol = yaml.safe_load(a.protocol.read_text(encoding="utf-8"))
    manifest = json.loads(a.parquet.with_suffix(".manifest.json").read_text(encoding="utf-8"))
    features = contract["features"]["generated"]
    test_start = manifest["date_ranges"]["test"][0]
    frame = pd.read_parquet(a.parquet, filters=[("date", "<", test_start)])
    frame = frame.loc[frame[features].notna().all(axis=1)].copy()
    if frame.empty or frame.date.max() >= test_start or frame.split.eq("test").any():
        raise ValueError("Phase 5 data includes test dates")
    gpus = tf.config.list_physical_devices("GPU")
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    device = "/GPU:0" if gpus else "/CPU:0"
    base_seed = int(protocol["reproducibility"]["seed"])
    prediction_parts, training_log = [], []

    for fold in manifest["expanding_folds"]:
        train_range = frame.date.between(*fold["train_dates"])
        val_range = frame.date.between(*fold["validation_dates"])
        train_all = frame.loc[train_range]
        valid = frame.loc[val_range].copy()
        if valid.empty or valid.date.max() >= test_start:
            raise ValueError(f"Fold {fold['fold']} overlaps test or has no validation rows")
        x_valid_raw = valid[features].to_numpy(dtype=np.float32)
        fold_seed = base_seed + fold["fold"] * 100

        # Three independently trained models, one for each time scale.
        individual_probs = {}
        for i, (target, col) in enumerate(TARGETS.items()):
            train = train_all.loc[train_all[col].notna()]
            x_train_raw = train[features].to_numpy(dtype=np.float32)
            y_train = train[col].astype(np.float32).to_numpy().reshape(-1, 1)
            scaler = StandardScaler().fit(x_train_raw)
            x_train = scaler.transform(x_train_raw).astype(np.float32)
            x_valid = scaler.transform(x_valid_raw).astype(np.float32)
            seed = fold_seed + i
            tf.keras.backend.clear_session()
            model = binary_model(len(features), seed)
            t0 = time.perf_counter()
            with tf.device(device):
                model.fit(x_train, y_train, batch_size=256, epochs=5, shuffle=False, verbose=0)
                individual_probs[target] = model.predict(x_valid, batch_size=256, verbose=0).ravel()
            training_log.append({"fold": fold["fold"], "model": "independent", "target": target, "train_rows": len(train), "fit_predict_seconds": round(time.perf_counter() - t0, 3)})
            del model

        # Shared encoder and three heads; null labels are masked with sample weights.
        shared_train = train_all
        scaler = StandardScaler().fit(shared_train[features].to_numpy(dtype=np.float32))
        x_train = scaler.transform(shared_train[features].to_numpy(dtype=np.float32)).astype(np.float32)
        x_valid = scaler.transform(x_valid_raw).astype(np.float32)
        y_dict, weights = {}, {}
        for target, col in TARGETS.items():
            mask = shared_train[col].notna().to_numpy(dtype=np.float32)
            y_dict[target] = shared_train[col].fillna(0).to_numpy(dtype=np.float32).reshape(-1, 1)
            weights[target] = mask.reshape(-1, 1)
        tf.keras.backend.clear_session()
        shared = binary_model(len(features), fold_seed + 50, multi=True)
        t0 = time.perf_counter()
        with tf.device(device):
            shared.fit(x_train, y_dict, sample_weight=weights, batch_size=256, epochs=5, shuffle=False, verbose=0)
            shared_probs = shared.predict(x_valid, batch_size=256, verbose=0)
        training_log.append({"fold": fold["fold"], "model": "shared_multitask", "target": "three_heads", "train_rows": len(shared_train), "fit_predict_seconds": round(time.perf_counter() - t0, 3)})
        if isinstance(shared_probs, list):
            shared_probs = dict(zip(TARGETS, shared_probs))
        del shared

        # Independent majority model on the common three-label intersection.
        majority_train = train_all.loc[train_all.y_majority.notna()]
        scaler_majority = StandardScaler().fit(majority_train[features].to_numpy(dtype=np.float32))
        x_maj_train = scaler_majority.transform(majority_train[features].to_numpy(dtype=np.float32)).astype(np.float32)
        x_maj_valid = scaler_majority.transform(x_valid_raw).astype(np.float32)
        tf.keras.backend.clear_session()
        majority = binary_model(len(features), fold_seed + 60)
        t0 = time.perf_counter()
        with tf.device(device):
            majority.fit(x_maj_train, majority_train.y_majority.astype(np.float32).to_numpy().reshape(-1, 1), batch_size=256, epochs=5, shuffle=False, verbose=0)
            majority_prob = majority.predict(x_maj_valid, batch_size=256, verbose=0).ravel()
        training_log.append({"fold": fold["fold"], "model": "majority_target", "target": "majority", "train_rows": len(majority_train), "fit_predict_seconds": round(time.perf_counter() - t0, 3)})
        del majority

        # Soft-target regression on the all-scale intersection only.
        soft_train = train_all.loc[train_all.y_soft.notna()]
        soft_train_mean = float(soft_train.y_soft.mean())
        scaler_soft = StandardScaler().fit(soft_train[features].to_numpy(dtype=np.float32))
        x_soft_train = scaler_soft.transform(soft_train[features].to_numpy(dtype=np.float32)).astype(np.float32)
        x_soft_valid = scaler_soft.transform(x_valid_raw).astype(np.float32)
        tf.keras.backend.clear_session()
        soft_model = binary_model(len(features), fold_seed + 70, regression=True)
        t0 = time.perf_counter()
        with tf.device(device):
            soft_model.fit(x_soft_train, soft_train.y_soft.to_numpy(dtype=np.float32).reshape(-1, 1), batch_size=256, epochs=5, shuffle=False, verbose=0)
            soft_predictions = soft_model.predict(x_soft_valid, batch_size=256, verbose=0).ravel()
        training_log.append({"fold": fold["fold"], "model": "soft_score_regression", "target": "mean_score", "train_rows": len(soft_train), "fit_predict_seconds": round(time.perf_counter() - t0, 3)})
        del soft_model

        base = valid[["ticker", "date", "time", "y5", "y10", "y15", "y_majority", "y_soft"]].copy()
        base["fold"] = fold["fold"]
        for target in TARGETS:
            base[f"p_ind_{target}"] = individual_probs[target]
            base[f"pred_ind_{target}"] = (individual_probs[target] >= 0.5).astype(np.int8)
            prob = shared_probs[target]
            if isinstance(prob, dict):
                prob = prob["probabilities"]
            base[f"p_shared_{target}"] = np.asarray(prob).reshape(-1)
            base[f"pred_shared_{target}"] = (np.asarray(prob).reshape(-1) >= 0.5).astype(np.int8)
        base["p_majority"] = majority_prob
        base["pred_majority"] = (majority_prob >= 0.5).astype(np.int8)
        base["pred_soft"] = soft_predictions
        base["pred_soft_constant"] = soft_train_mean
        base["label_disagreement"] = ((base.y5 != base.y10).astype(int) + (base.y5 != base.y15).astype(int) + (base.y10 != base.y15).astype(int)) / 2
        base["positive_vote_count"] = base[["y5", "y10", "y15"]].sum(axis=1, min_count=3)
        prediction_parts.append(base)
        print(f"completed fold {fold['fold']} on {device}", flush=True)

    predictions = pd.concat(prediction_parts, ignore_index=True)
    a.predictions.parent.mkdir(parents=True, exist_ok=True)
    predictions.to_parquet(a.predictions, index=False, compression="zstd")
    records = []
    architectures = {"independent": "pred_ind_", "shared_multitask": "pred_shared_"}
    for (fold_no, architecture), pred_frame in [(key, part) for fold_no, part in predictions.groupby("fold") for key in [(fold_no, name) for name in architectures]]:
        common = pred_frame[["y5", "y10", "y15"]].notna().all(axis=1)
        prefix = architectures[architecture]
        unanimous = (pred_frame[prefix + "trend_5m"] == pred_frame[prefix + "trend_10m"]) & (pred_frame[prefix + "trend_10m"] == pred_frame[prefix + "trend_15m"])
        for target, col in TARGETS.items():
            pred_col = prefix + target
            for root in ["ALL", *contract["universe"]["primary_roots"]]:
                root_mask = np.ones(len(pred_frame), dtype=bool) if root == "ALL" else pred_frame.ticker.str.startswith(root).to_numpy()
                masks = {"available_head": root_mask & pred_frame[col].notna().to_numpy(),
                         "common_intersection": root_mask & common.to_numpy(),
                         "selective_unanimous_predictions": root_mask & common.to_numpy() & unanimous.to_numpy(),
                         "reference_unanimous_labels": root_mask & common.to_numpy() & pred_frame.label_disagreement.eq(0).to_numpy(),
                         "reference_discordant_labels": root_mask & common.to_numpy() & pred_frame.label_disagreement.gt(0).to_numpy()}
                for sample, mask in masks.items():
                    if not mask.any():
                        continue
                    y = pred_frame.loc[mask, col].astype(int).to_numpy()
                    yhat = pred_frame.loc[mask, pred_col].astype(int).to_numpy()
                    denominator = root_mask.sum() if sample == "available_head" else (root_mask & common.to_numpy()).sum()
                    row = {"fold": fold_no, "architecture": architecture, "target": target, "root": root, "sample": sample,
                           "coverage": float(mask.sum() / denominator) if denominator else 0.0,
                           **classification_metrics(y, yhat)}
                    records.append(row)
    # Metrics for the independent majority model and soft-score regression.
    for fold_no, part in predictions.groupby("fold"):
        common = part.y_soft.notna()
        for root in ["ALL", *contract["universe"]["primary_roots"]]:
            root_mask = np.ones(len(part), dtype=bool) if root == "ALL" else part.ticker.str.startswith(root).to_numpy()
            mask = root_mask & common.to_numpy()
            if mask.any():
                y = part.loc[mask, "y_majority"].astype(int).to_numpy()
                pred = (part.loc[mask, "p_majority"].to_numpy() >= 0.5).astype(int)
                records.append({"fold": fold_no, "architecture": "majority_target", "target": "majority", "root": root, "sample": "common_intersection", "coverage": float(mask.sum() / root_mask.sum()), **classification_metrics(y, pred)})
                soft_true = part.loc[mask, "y_soft"].to_numpy(dtype=float)
                soft_pred = part.loc[mask, "pred_soft"].to_numpy(dtype=float)
                records.append({"fold": fold_no, "architecture": "soft_score_regression", "target": "mean_score", "root": root, "sample": "common_intersection", "coverage": float(mask.sum() / root_mask.sum()), "n": int(mask.sum()), "mae": float(mean_absolute_error(soft_true, soft_pred)), "mse": float(mean_squared_error(soft_true, soft_pred))})
                constant = part.loc[mask, "pred_soft_constant"].to_numpy(dtype=float)
                records.append({"fold": fold_no, "architecture": "training_mean_constant", "target": "mean_score", "root": root, "sample": "common_intersection", "coverage": float(mask.sum() / root_mask.sum()), "n": int(mask.sum()), "mae": float(mean_absolute_error(soft_true, constant)), "mse": float(mean_squared_error(soft_true, constant)), "train_mean_score": float(constant[0])})
    metrics = pd.DataFrame(records)
    a.metrics.parent.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(a.metrics, index=False)
    run = {"status": "completed_pretest_multiscale_cv", "device": device, "visible_gpus": [str(g.name) for g in gpus], "test_start_excluded": test_start,
           "prediction_rows": len(predictions), "predictions_path": str(a.predictions), "prediction_bytes": a.predictions.stat().st_size,
           "training_runs": training_log, "runtime_seconds": round(time.perf_counter() - started, 2),
           "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
           "gpu_memory_info_bytes": tf.config.experimental.get_memory_info("GPU:0") if gpus else None,
           "seed": base_seed, "epochs": 5, "batch_size": 256, "test_metrics_opened": False,
           "contract_hash": manifest["contract_hash"], "protocol_hash": manifest["protocol_hash"], "source_sha256": manifest["source_sha256"]}
    a.metrics.with_suffix(".json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
    # Fold-mean summaries are descriptive. Keep every paired row metric in CSV.
    paired = metrics[(metrics.root == "ALL") & metrics.architecture.isin(["independent", "shared_multitask"]) & metrics["sample"].isin(["common_intersection", "selective_unanimous_predictions"])]
    aggregate = paired.groupby(["architecture", "target", "sample"]).agg(mcc_mean=("mcc", "mean"), mcc_sd=("mcc", "std"), bacc_mean=("balanced_accuracy", "mean"), bacc_sd=("balanced_accuracy", "std"), f1_mean=("macro_f1", "mean"), f1_sd=("macro_f1", "std"), coverage_mean=("coverage", "mean")).reset_index()
    lines = ["# Multi-scale model comparison (pre-test folds)", "", "Four expanding validation folds; no test dates were read into the evaluation frame. Full per-fold and per-root results are in `multiscale_cv_summary.csv`; row predictions are local in ignored `tmp/`.", "", f"- Device: {device}; runtime {run['runtime_seconds']} s; peak RSS {run['peak_rss_kib']:,} KiB; prediction cache {run['prediction_bytes']:,} bytes.", "- Separate and shared-head results use the same common intersection for paired comparison. Means ± SD are descriptive across overlapping expanding folds, not inferential intervals.", "- Selective acceptance requires unanimous predictions across all three model heads; coverage is reported next to performance. This rule uses model outputs available at prediction time.", "- Reference-label unanimity/discordance strata are also in the CSV, with coverage; they are descriptive because the true label disagreement is unavailable at inference.", "- The soft `mean_score` experiment is evaluated as regression against a deterministic vote fraction; it is not interpreted as a true probability.", "- B0 labels remain retrospective, and none of these results establish trading performance.", "", "| Architecture | Target | Sample | MCC | Balanced accuracy | Macro F1 | Coverage |", "|---|---|---|---:|---:|---:|---:|"]
    for _, row in aggregate.iterrows():
        lines.append(f"| {row.architecture} | {row.target} | {row.sample} | {row.mcc_mean:.3f} ± {row.mcc_sd:.3f} | {row.bacc_mean:.3f} ± {row.bacc_sd:.3f} | {row.f1_mean:.3f} ± {row.f1_sd:.3f} | {row.coverage_mean:.3f} |")
    lines += ["", "## Runtime/memory and provenance", "", f"- Contract/protocol SHA-256: `{manifest['contract_hash']}` / `{manifest['protocol_hash']}`.", f"- Market/B4 SHA-256: `{manifest['source_sha256']['market']}` / `{manifest['source_sha256']['labels']}`.", "- The previous-label persistence baseline remains excluded because B4 lacks a confirmation timestamp.", ""]
    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.report.write_text("\n".join(lines), encoding="utf-8")
    subprocess.run([sys.executable, "scripts/summarize_multiscale_cv.py", "--metrics", str(a.metrics), "--run", str(a.metrics.with_suffix('.json')), "--manifest", str(a.parquet.with_suffix('.manifest.json')), "--contract", str(a.contract), "--parquet", str(a.parquet), "--predictions", str(a.predictions), "--output", str(a.report)], check=True)
    print(json.dumps(run, indent=2))


if __name__ == "__main__":
    main()
