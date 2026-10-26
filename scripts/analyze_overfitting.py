#!/usr/bin/env python3
"""Measure in-sample versus chronological validation fit without reading test data."""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
import yaml
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, average_precision_score, balanced_accuracy_score,
    brier_score_loss, f1_score, log_loss, matthews_corrcoef,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from run_final_evaluation import TARGETS, build_mlp


def score(y, p):
    y = np.asarray(y, dtype=int)
    p = np.asarray(p, dtype=float)
    pred = (p >= 0.5).astype(int)
    return {
        "n": int(len(y)),
        "accuracy": float(accuracy_score(y, pred)),
        "mcc": float(matthews_corrcoef(y, pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
        "macro_f1": float(f1_score(y, pred, labels=[0, 1], average="macro", zero_division=0)),
        "brier": float(brier_score_loss(y, p)),
        "log_loss": float(log_loss(y, np.clip(p, 1e-7, 1 - 1e-7), labels=[0, 1])),
        "roc_auc": float(roc_auc_score(y, p)) if np.unique(y).size == 2 else np.nan,
        "pr_average_precision": float(average_precision_score(y, p)) if np.unique(y).size == 2 else np.nan,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--protocol", type=Path, default=Path("config/final_evaluation.yaml"))
    ap.add_argument("--csv", type=Path, default=Path("reports/overfitting_train_validation.csv"))
    ap.add_argument("--report", type=Path, default=Path("reports/overfitting_assessment.md"))
    a = ap.parse_args()

    contract = yaml.safe_load(a.contract.read_text(encoding="utf-8"))
    protocol = yaml.safe_load(a.protocol.read_text(encoding="utf-8"))
    features = contract["features"]["generated"]
    frame = pd.read_parquet(a.parquet, filters=[("split", "in", ["train", "validation"])])
    if set(frame.split.unique()) - {"train", "validation"}:
        raise ValueError("Diagnostic input unexpectedly contains rows outside train/validation")
    frame = frame.loc[frame[features].notna().all(axis=1)].copy()
    train = frame.loc[frame.split == "train"].copy()
    validation = frame.loc[frame.split == "validation"].copy()
    if train.empty or validation.empty:
        raise ValueError("Train and validation partitions must both contain eligible rows")

    seed = int(protocol["training"]["seed"])
    tf.config.set_visible_devices([], "GPU")
    results = []

    def add(model_name, target, split, y, p):
        results.append({"model": model_name, "target": target, "split": split, **score(y, p)})

    # Frozen CPU baselines; fit once on the full frozen training partition.
    for target, ycol in TARGETS.items():
        usable = train[ycol].notna()
        x_train = train.loc[usable, features].to_numpy(dtype=np.float32)
        y_train = train.loc[usable, ycol].astype(int).to_numpy()
        x_val = validation[features].to_numpy(dtype=np.float32)
        y_val = validation.loc[validation[ycol].notna(), ycol].astype(int).to_numpy()
        x_val_target = validation.loc[validation[ycol].notna(), features].to_numpy(dtype=np.float32)

        logistic = Pipeline([
            ("scale", StandardScaler()),
            ("model", LogisticRegression(C=1.0, max_iter=250, random_state=seed)),
        ]).fit(x_train, y_train)
        hist = HistGradientBoostingClassifier(
            learning_rate=0.1, max_iter=50, max_leaf_nodes=15,
            l2_regularization=1.0, early_stopping=False, random_state=seed,
        ).fit(x_train, y_train)
        for name, model in (("logistic_regression", logistic), ("hist_gradient_boosting", hist)):
            add(name, target, "train_apparent", y_train, model.predict_proba(x_train)[:, list(model.classes_).index(1)])
            add(name, target, "validation", y_val, model.predict_proba(x_val_target)[:, list(model.classes_).index(1)])

    # Independent MLPs reproduce the frozen scaler, architecture, seed offsets,
    # five epochs, batch size, and deterministic row order from the final run.
    for i, (target, ycol) in enumerate(TARGETS.items()):
        usable = train[ycol].notna()
        xtr_raw = train.loc[usable, features].to_numpy(dtype=np.float32)
        ytr = train.loc[usable, ycol].astype(np.float32).to_numpy()
        xva_raw = validation.loc[validation[ycol].notna(), features].to_numpy(dtype=np.float32)
        yva = validation.loc[validation[ycol].notna(), ycol].astype(int).to_numpy()
        scaler = StandardScaler().fit(xtr_raw)
        xtr = scaler.transform(xtr_raw).astype(np.float32)
        xva = scaler.transform(xva_raw).astype(np.float32)
        tf.keras.backend.clear_session()
        model = build_mlp(len(features), seed + i)
        model.fit(xtr, ytr, batch_size=256, epochs=5, shuffle=False, verbose=0)
        add("independent_mlp", target, "train_apparent", ytr.astype(int), model.predict(xtr, batch_size=256, verbose=0).ravel())
        add("independent_mlp", target, "validation", yva, model.predict(xva, batch_size=256, verbose=0).ravel())
        del model

    # Shared masked-head MLP, using the same all-label-row feature scaler as
    # the frozen evaluator. Validation is scored only for observed labels.
    xtr_raw = train[features].to_numpy(dtype=np.float32)
    xva_raw = validation[features].to_numpy(dtype=np.float32)
    scaler = StandardScaler().fit(xtr_raw)
    xtr = scaler.transform(xtr_raw).astype(np.float32)
    xva = scaler.transform(xva_raw).astype(np.float32)
    labels, weights = {}, {}
    for target, ycol in TARGETS.items():
        mask = train[ycol].notna().to_numpy(dtype=np.float32)
        labels[target] = train[ycol].fillna(0).to_numpy(dtype=np.float32).reshape(-1, 1)
        weights[target] = mask.reshape(-1, 1)
    tf.keras.backend.clear_session()
    shared = build_mlp(len(features), seed + 10, multi=True)
    shared.fit(xtr, labels, sample_weight=weights, batch_size=256, epochs=5, shuffle=False, verbose=0)
    ptr = shared.predict(xtr, batch_size=256, verbose=0)
    pva = shared.predict(xva, batch_size=256, verbose=0)
    if isinstance(ptr, list):
        ptr, pva = dict(zip(TARGETS, ptr)), dict(zip(TARGETS, pva))
    for target, ycol in TARGETS.items():
        ytr_mask = train[ycol].notna().to_numpy()
        yva_mask = validation[ycol].notna().to_numpy()
        add("shared_multitask_mlp", target, "train_apparent", train.loc[ytr_mask, ycol].astype(int), np.asarray(ptr[target]).ravel()[ytr_mask])
        add("shared_multitask_mlp", target, "validation", validation.loc[yva_mask, ycol].astype(int), np.asarray(pva[target]).ravel()[yva_mask])
    del shared

    metrics = pd.DataFrame(results)
    wide = metrics.pivot(index=["model", "target"], columns="split", values=["mcc", "balanced_accuracy", "macro_f1", "brier", "log_loss", "roc_auc", "pr_average_precision"])
    wide.columns = [f"{metric}_{split}" for metric, split in wide.columns]
    wide = wide.reset_index()
    wide["mcc_gap_train_minus_validation"] = wide.mcc_train_apparent - wide.mcc_validation
    wide["macro_f1_gap_train_minus_validation"] = wide.macro_f1_train_apparent - wide.macro_f1_validation
    wide["brier_gap_validation_minus_train"] = wide.brier_validation - wide.brier_train_apparent
    wide["log_loss_gap_validation_minus_train"] = wide.log_loss_validation - wide.log_loss_train_apparent
    wide.to_csv(a.csv, index=False)

    lines = [
        "# Overfitting diagnostic: train apparent fit versus chronological validation",
        "",
        "This diagnostic reads only the frozen train and validation partitions. It does not read or score final-test rows, change thresholds, select models, or tune hyperparameters. The final test is excluded from this script's Parquet filter.",
        "",
        "The CPU baselines and MLPs use the frozen final-evaluation settings and fit once on all eligible training sessions. The reported train metrics are apparent in-sample scores, so a train-validation gap is an overfit warning signal, not an unbiased estimate of future performance. Validation is the chronological holdout.",
        "",
        "| Model | Target | n train | n validation | MCC train | MCC val | MCC gap | Macro-F1 train | Macro-F1 val | Brier train | Brier val | Log loss train | Log loss val | ROC-AUC train | ROC-AUC val |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    detail = metrics.pivot(index=["model", "target"], columns="split", values=["n", "mcc", "macro_f1", "brier", "log_loss", "roc_auc"])
    for (model, target), row in detail.iterrows():
        fmt = lambda key: "—" if pd.isna(row[key]) else f"{row[key]:.4f}"
        n_train = int(row[("n", "train_apparent")])
        n_val = int(row[("n", "validation")])
        mcc_gap = row[("mcc", "train_apparent")] - row[("mcc", "validation")]
        lines.append(
            f"| {model} | {target} | {n_train} | {n_val} | "
            f"{fmt(('mcc', 'train_apparent'))} | {fmt(('mcc', 'validation'))} | {mcc_gap:.4f} | "
            f"{fmt(('macro_f1', 'train_apparent'))} | {fmt(('macro_f1', 'validation'))} | "
            f"{fmt(('brier', 'train_apparent'))} | {fmt(('brier', 'validation'))} | "
            f"{fmt(('log_loss', 'train_apparent'))} | {fmt(('log_loss', 'validation'))} | "
            f"{fmt(('roc_auc', 'train_apparent'))} | {fmt(('roc_auc', 'validation'))} |"
        )
    lines += [
        "",
        "Interpretation must be combined with the four expanding-fold CV results and the separate frozen test report. Folds overlap in their training windows; their standard deviations are descriptive rather than independent confidence intervals. Test metrics must not be used for model or threshold selection.",
        "",
    ]
    a.report.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {a.report} and {a.csv}; read {len(train):,} train and {len(validation):,} validation rows; final test not loaded")


if __name__ == "__main__":
    main()
