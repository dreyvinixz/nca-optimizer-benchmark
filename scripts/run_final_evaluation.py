#!/usr/bin/env python3
"""One-pass final evaluation with the pre-registered model set and fixed test blocks."""
import argparse
import hashlib
import json
import resource
import subprocess
import time
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
import tensorflow as tf
import yaml
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, brier_score_loss, f1_score, log_loss, matthews_corrcoef, mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


TARGETS = {"trend_5m": "y5", "trend_10m": "y10", "trend_15m": "y15"}


def build_mlp(input_dim, seed, multi=False, regression=False):
    tf.keras.utils.set_random_seed(seed)
    inputs = tf.keras.layers.Input(shape=(input_dim,))
    x = tf.keras.layers.Dense(32, activation="relu")(inputs)
    x = tf.keras.layers.Dropout(0.10, seed=seed)(x)
    x = tf.keras.layers.Dense(16, activation="relu")(x)
    if multi:
        outputs = {name: tf.keras.layers.Dense(1, activation="sigmoid", name=name)(x) for name in TARGETS}
        model = tf.keras.Model(inputs, outputs)
        model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss={name: tf.keras.losses.BinaryCrossentropy() for name in TARGETS})
    else:
        outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
        model = tf.keras.Model(inputs, outputs)
        model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss="mse" if regression else "binary_crossentropy")
    return model


def probabilities(model, x):
    classes = list(model.classes_)
    return model.predict_proba(x)[:, classes.index(1)] if 1 in classes else np.zeros(len(x))


def cls_metrics(y, pred, prob=None):
    y = np.asarray(y, dtype=int)
    pred = np.asarray(pred, dtype=int)
    row = {
        "n": int(len(y)), "mcc": float(matthews_corrcoef(y, pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
        "macro_f1": float(f1_score(y, pred, labels=[0, 1], average="macro", zero_division=0)),
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
    return row


def bootstrap_paired_mcc(test_predictions, target, block_len, reps, seed):
    frame = test_predictions.loc[test_predictions[["y5", "y10", "y15"]].notna().all(axis=1)].copy()
    ycol = TARGETS[target]
    dates = sorted(frame.date.unique())
    if len(dates) < block_len:
        return None
    daily = {}
    for date in dates:
        g = frame.loc[frame.date == date]
        y = g[ycol].astype(int).to_numpy()
        pi = g[f"p_ind_{target}"].to_numpy() >= 0.5
        ps = g[f"p_shared_{target}"].to_numpy() >= 0.5
        daily[date] = (y, pi.astype(int), ps.astype(int))
    rng = np.random.default_rng(seed)
    nblocks = int(np.ceil(len(dates) / block_len))
    differences = np.empty(reps, dtype=float)
    for i in range(reps):
        starts = rng.integers(0, len(dates), size=nblocks)
        chosen = [(start + np.arange(block_len)) % len(dates) for start in starts]
        indices = np.concatenate(chosen)[:len(dates)]
        ys, pis, pss = [], [], []
        for idx in indices:
            y, pi, ps = daily[dates[int(idx)]]
            ys.extend(y); pis.extend(pi); pss.extend(ps)
        differences[i] = matthews_corrcoef(ys, pis) - matthews_corrcoef(ys, pss)
    return {"mean_mcc_difference_independent_minus_shared": float(np.mean(differences)), "ci95": np.quantile(differences, [0.025, 0.975]).tolist(), "sessions": len(dates), "block_length": block_len, "replicates": reps}


def main():
    started = time.perf_counter()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--config", type=Path, default=Path("config/final_evaluation.yaml"))
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--predictions", type=Path, default=Path("tmp/final_test_predictions.parquet"))
    ap.add_argument("--metrics", type=Path, default=Path("reports/final_test_metrics.csv"))
    ap.add_argument("--report", type=Path, default=Path("reports/final_test.md"))
    a = ap.parse_args()
    config = yaml.safe_load(a.config.read_text(encoding="utf-8"))
    contract = yaml.safe_load(a.contract.read_text(encoding="utf-8"))
    manifest = json.loads(a.parquet.with_suffix(".manifest.json").read_text(encoding="utf-8"))
    if hashlib.sha256(a.contract.read_bytes()).hexdigest() != manifest["contract_hash"]:
        raise ValueError("Current data contract differs from the one used to build the feature cache")
    protocol_path = Path("config/experiment_protocol.yaml")
    if hashlib.sha256(protocol_path.read_bytes()).hexdigest() != manifest["protocol_hash"]:
        raise ValueError("Current experiment protocol differs from the one used to build the feature cache")
    if config["status"] != "preregistered_before_final_test":
        raise ValueError("Final evaluation configuration is not frozen")
    if config["development_protocol_sha256"] != manifest["protocol_hash"] or config["data_contract_sha256"] != manifest["contract_hash"]:
        raise ValueError("Final evaluation configuration does not match the feature cache hashes")
    committed_config = subprocess.check_output(["git", "show", "HEAD:config/final_evaluation.yaml"], text=True).replace("\r\n", "\n")
    current_config = a.config.read_text(encoding="utf-8").replace("\r\n", "\n")
    if committed_config != current_config:
        raise ValueError("Final evaluation config differs from the committed pre-registration")
    subprocess.check_call(["git", "cat-file", "-e", "HEAD:scripts/run_final_evaluation.py"])
    committed_script = subprocess.check_output(["git", "show", "HEAD:scripts/run_final_evaluation.py"], text=True).replace("\r\n", "\n")
    current_script = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    if committed_script != current_script:
        raise ValueError("Final evaluation script differs from the committed version")
    required_models = {"majority_constant", "causal_5m_momentum", "logistic_regression", "hist_gradient_boosting", "independent_mlp", "shared_multitask_mlp", "majority_mlp", "soft_score_mlp", "soft_score_training_mean"}
    if set(config["candidate_models"]["models"]) != required_models:
        raise ValueError("Candidate model set differs from the pre-registered script")
    model_specs = config["candidate_models"]["models"]
    for name in ("independent_mlp", "shared_multitask_mlp", "majority_mlp", "soft_score_mlp"):
        spec = model_specs[name]
        if spec.get("layers") != [32, 16] or spec.get("dropout") != 0.1 or spec.get("epochs") != 5 or spec.get("batch_size") != 256:
            raise ValueError(f"MLP settings differ from the frozen script: {name}")
    if config["training"]["shuffle"] or config["training"]["decision_threshold"] != 0.5 or config["final_test_inference"]["report_p_values"] is not False:
        raise ValueError("Training/evaluation rules differ from the frozen script")
    features = contract["features"]["generated"]
    # The run includes fixed validation and test periods; train rows are never read.
    frame = pd.read_parquet(a.parquet, filters=[("split", "in", ["validation", "test"])])
    frame = frame.loc[frame[features].notna().all(axis=1)].copy()
    frame["date"] = frame.date.astype(str)
    test = frame.loc[frame.split == "test"]
    observed_dates = sorted(test.date.unique())
    expected_dates = []
    for block in config["final_test"]["blocks"]:
        dates = sorted(test.loc[test.date.between(block["start"], block["end"]), "date"].unique())
        if len(dates) != block["sessions"]:
            raise ValueError(f"Test block {block['block']} expected {block['sessions']} sessions, found {len(dates)}")
        expected_dates.extend(dates)
    if observed_dates != expected_dates or len(observed_dates) != config["final_test"]["sessions"]:
        raise ValueError("Observed test dates differ from the frozen date blocks")
    train = pd.read_parquet(a.parquet, filters=[("split", "==", "train")])
    train = train.loc[train[features].notna().all(axis=1)].copy()
    validation = frame.loc[frame.split == "validation"].copy()
    if train.split.eq("test").any() or validation.split.eq("test").any():
        raise ValueError("Train/validation data contains test rows")
    seed = int(config["training"]["seed"])
    gpus = tf.config.list_physical_devices("GPU")
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)
    device = "/GPU:0" if gpus else "/CPU:0"
    predictions = frame[["id_ticker", "ticker", "date", "time", "split", "y5", "y10", "y15", "y_majority", "y_soft"]].copy()
    block_map = {}
    for block in config["final_test"]["blocks"]:
        block_map.update({date: block["block"] for date in observed_dates if block["start"] <= date <= block["end"]})
    predictions["test_block"] = predictions.date.map(block_map)
    x_val_raw = validation[features].to_numpy(dtype=np.float32)
    x_test_raw = test[features].to_numpy(dtype=np.float32)
    log = []

    # Non-neural baselines.
    for target, col in {**TARGETS, "majority": "y_majority"}.items():
        use = train[col].notna()
        y = train.loc[use, col].astype(int).to_numpy()
        x = train.loc[use, features].to_numpy(dtype=np.float32)
        dummy = DummyClassifier(strategy="most_frequent").fit(x, y)
        for split_name, xx in (("validation", x_val_raw), ("test", x_test_raw)):
            pred = dummy.predict(xx).astype(int)
            p = probabilities(dummy, xx)
            predictions.loc[predictions.split == split_name, f"p_dummy_{target}"] = p
            predictions.loc[predictions.split == split_name, f"pred_dummy_{target}"] = pred
        log.append({"model": "majority_constant", "target": target, "train_rows": len(y)})
        if target in TARGETS:
            for split_name, xx in (("validation", x_val_raw), ("test", x_test_raw)):
                pred = (xx[:, features.index("log_return_5m")] >= 0).astype(int)
                predictions.loc[predictions.split == split_name, f"p_momentum_{target}"] = pred.astype(float)
                predictions.loc[predictions.split == split_name, f"pred_momentum_{target}"] = pred
            scaler_pipe = Pipeline([("scale", StandardScaler()), ("model", LogisticRegression(C=1.0, max_iter=250, random_state=seed))]).fit(x, y)
            hist = HistGradientBoostingClassifier(learning_rate=0.1, max_iter=50, max_leaf_nodes=15, l2_regularization=1.0, early_stopping=False, random_state=seed).fit(x, y)
            scaler_pipe_model, hist_model = scaler_pipe, hist
            for model_name, model in (("logistic", scaler_pipe_model), ("hist", hist_model)):
                for split_name, xx in (("validation", x_val_raw), ("test", x_test_raw)):
                    p = model.predict_proba(xx)[:, list(model.classes_).index(1)] if hasattr(model, "classes_") else model.predict_proba(xx)[:, list(model.named_steps["model"].classes_).index(1)]
                    predictions.loc[predictions.split == split_name, f"p_{model_name}_{target}"] = p
                    predictions.loc[predictions.split == split_name, f"pred_{model_name}_{target}"] = (p >= 0.5).astype(int)
                log.append({"model": model_name, "target": target, "train_rows": len(y)})

    # Independent one-head MLPs.
    for i, (target, col) in enumerate(TARGETS.items()):
        usable = train[col].notna()
        x_train_raw = train.loc[usable, features].to_numpy(dtype=np.float32)
        y_train = train.loc[usable, col].astype(np.float32).to_numpy().reshape(-1, 1)
        scaler = StandardScaler().fit(x_train_raw)
        x_train = scaler.transform(x_train_raw).astype(np.float32)
        x_val = scaler.transform(x_val_raw).astype(np.float32)
        x_test = scaler.transform(x_test_raw).astype(np.float32)
        tf.keras.backend.clear_session()
        model = build_mlp(len(features), seed + i)
        t0 = time.perf_counter()
        with tf.device(device):
            model.fit(x_train, y_train, batch_size=256, epochs=5, shuffle=False, verbose=0)
            pv = model.predict(x_val, batch_size=256, verbose=0).ravel()
            pt = model.predict(x_test, batch_size=256, verbose=0).ravel()
        predictions.loc[predictions.split == "validation", f"p_ind_{target}"] = pv
        predictions.loc[predictions.split == "test", f"p_ind_{target}"] = pt
        predictions.loc[predictions.split == "validation", f"pred_ind_{target}"] = (pv >= 0.5).astype(int)
        predictions.loc[predictions.split == "test", f"pred_ind_{target}"] = (pt >= 0.5).astype(int)
        log.append({"model": "independent_mlp", "target": target, "train_rows": len(y_train), "fit_predict_seconds": round(time.perf_counter() - t0, 3)})
        del model

    # Shared, masked three-head MLP.
    scaler = StandardScaler().fit(train[features].to_numpy(dtype=np.float32))
    x_train = scaler.transform(train[features].to_numpy(dtype=np.float32)).astype(np.float32)
    x_val = scaler.transform(x_val_raw).astype(np.float32)
    x_test = scaler.transform(x_test_raw).astype(np.float32)
    labels, weights = {}, {}
    for target, col in TARGETS.items():
        mask = train[col].notna().to_numpy(dtype=np.float32)
        labels[target] = train[col].fillna(0).to_numpy(dtype=np.float32).reshape(-1, 1)
        weights[target] = mask.reshape(-1, 1)
    tf.keras.backend.clear_session()
    shared = build_mlp(len(features), seed + 10, multi=True)
    t0 = time.perf_counter()
    with tf.device(device):
        shared.fit(x_train, labels, sample_weight=weights, batch_size=256, epochs=5, shuffle=False, verbose=0)
        pv = shared.predict(x_val, batch_size=256, verbose=0)
        pt = shared.predict(x_test, batch_size=256, verbose=0)
    if isinstance(pv, list):
        pv, pt = dict(zip(TARGETS, pv)), dict(zip(TARGETS, pt))
    for target in TARGETS:
        predictions.loc[predictions.split == "validation", f"p_shared_{target}"] = np.asarray(pv[target]).ravel()
        predictions.loc[predictions.split == "test", f"p_shared_{target}"] = np.asarray(pt[target]).ravel()
        predictions.loc[predictions.split == "validation", f"pred_shared_{target}"] = (np.asarray(pv[target]).ravel() >= 0.5).astype(int)
        predictions.loc[predictions.split == "test", f"pred_shared_{target}"] = (np.asarray(pt[target]).ravel() >= 0.5).astype(int)
    log.append({"model": "shared_multitask_mlp", "targets": list(TARGETS), "train_rows": len(train), "fit_predict_seconds": round(time.perf_counter() - t0, 3)})
    del shared

    # Independent hard-majority and soft-score models.
    common_train = train.loc[train.y_majority.notna() & train.y_soft.notna()]
    soft_training_mean = float(common_train.y_soft.mean())
    scaler = StandardScaler().fit(common_train[features].to_numpy(dtype=np.float32))
    x_common = scaler.transform(common_train[features].to_numpy(dtype=np.float32)).astype(np.float32)
    x_val_common = scaler.transform(x_val_raw).astype(np.float32)
    x_test_common = scaler.transform(x_test_raw).astype(np.float32)
    for target, labels_train, regression, seed_offset in (("majority", common_train.y_majority.astype(np.float32).to_numpy().reshape(-1, 1), False, 20), ("soft", common_train.y_soft.astype(np.float32).to_numpy().reshape(-1, 1), True, 21)):
        tf.keras.backend.clear_session()
        model = build_mlp(len(features), seed + seed_offset, regression=regression)
        t0 = time.perf_counter()
        with tf.device(device):
            model.fit(x_common, labels_train, batch_size=256, epochs=5, shuffle=False, verbose=0)
            pv = model.predict(x_val_common, batch_size=256, verbose=0).ravel()
            pt = model.predict(x_test_common, batch_size=256, verbose=0).ravel()
        predictions.loc[predictions.split == "validation", f"p_{target}"] = pv
        predictions.loc[predictions.split == "test", f"p_{target}"] = pt
        log.append({"model": "majority_mlp" if target == "majority" else "soft_score_mlp", "target": target, "train_rows": len(common_train), "fit_predict_seconds": round(time.perf_counter() - t0, 3)})
        del model
    for split_name in ("validation", "test"):
        predictions.loc[predictions.split == split_name, "p_soft_constant"] = soft_training_mean

    a.predictions.parent.mkdir(parents=True, exist_ok=True)
    predictions.to_parquet(a.predictions, index=False, compression="zstd")
    metric_rows = []
    model_targets = {
        "majority_constant": {**{t: (f"p_dummy_{t}", f"pred_dummy_{t}") for t in TARGETS}, "majority": ("p_dummy_majority", "pred_dummy_majority")},
        "causal_5m_momentum": {t: (f"p_momentum_{t}", f"pred_momentum_{t}") for t in TARGETS},
        "logistic_regression": {t: (f"p_logistic_{t}", f"pred_logistic_{t}") for t in TARGETS},
        "hist_gradient_boosting": {t: (f"p_hist_{t}", f"pred_hist_{t}") for t in TARGETS},
        "independent_mlp": {t: (f"p_ind_{t}", f"pred_ind_{t}") for t in TARGETS},
        "shared_multitask_mlp": {t: (f"p_shared_{t}", f"pred_shared_{t}") for t in TARGETS},
        "majority_mlp": {"majority": ("p_majority", None)},
    }
    for split_name in ("validation", "test"):
        split_frame = predictions.loc[predictions.split == split_name].copy()
        for model_name, outputs in model_targets.items():
            for target, (p_col, pred_col) in outputs.items():
                y_col = TARGETS.get(target, "y_majority")
                for root in ["ALL", "WIN", "IND"]:
                    root_mask = np.ones(len(split_frame), dtype=bool) if root == "ALL" else split_frame.ticker.str.startswith(root).to_numpy()
                    valid = root_mask & split_frame[y_col].notna().to_numpy()
                    for block in ([None] if split_name == "validation" else [1, 2, 3]):
                        mask = valid if block is None else valid & split_frame.test_block.eq(block).to_numpy()
                        if not mask.any():
                            continue
                        y = split_frame.loc[mask, y_col].astype(int).to_numpy()
                        p = split_frame.loc[mask, p_col].to_numpy(dtype=float)
                        pred = (p >= 0.5).astype(int) if pred_col is None else split_frame.loc[mask, pred_col].astype(int).to_numpy()
                        row = {"split": split_name, "model": model_name, "target": target, "root": root, "test_block": block, **cls_metrics(y, pred, p if model_name not in ("causal_5m_momentum",) else None)}
                        metric_rows.append(row)
        soft_mask = split_frame.y_soft.notna()
        for root in ["ALL", "WIN", "IND"]:
            root_mask = np.ones(len(split_frame), dtype=bool) if root == "ALL" else split_frame.ticker.str.startswith(root).to_numpy()
            valid = root_mask & soft_mask.to_numpy()
            for block in ([None] if split_name == "validation" else [1, 2, 3]):
                mask = valid if block is None else valid & split_frame.test_block.eq(block).to_numpy()
                if mask.any():
                    y = split_frame.loc[mask, "y_soft"].to_numpy(dtype=float)
                    for model_name, pred_col in (("soft_score_mlp", "p_soft"), ("soft_score_training_mean", "p_soft_constant")):
                        p = split_frame.loc[mask, pred_col].to_numpy(dtype=float)
                        metric_rows.append({"split": split_name, "model": model_name, "target": "mean_score", "root": root, "test_block": block, "n": int(mask.sum()), "mae": float(mean_absolute_error(y, p)), "mse": float(mean_squared_error(y, p))})
    metrics = pd.DataFrame(metric_rows)
    a.metrics.parent.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(a.metrics, index=False)
    test_rows = predictions.loc[predictions.split == "test"]
    bootstrap = {target: bootstrap_paired_mcc(test_rows, target, config["final_test_inference"]["block_length_sessions"], config["final_test_inference"]["replicates"], config["final_test_inference"]["seed"]) for target in TARGETS}
    run = {"status": "completed_once_only_final_test", "test_metrics_opened": True, "test_dates": observed_dates, "blocks": config["final_test"]["blocks"], "test_rows_with_complete_features": len(test_rows), "prediction_path": str(a.predictions), "prediction_bytes": a.predictions.stat().st_size, "metrics_path": str(a.metrics), "fit_log": log, "paired_test_mcc_block_bootstrap": bootstrap, "device": device, "visible_gpus": [str(x.name) for x in gpus], "runtime_seconds": round(time.perf_counter() - started, 2), "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss), "python": __import__("platform").python_version(), "pandas": pd.__version__, "numpy": np.__version__, "scikit_learn": sklearn.__version__, "tensorflow": tf.__version__, "config_sha256": __import__("hashlib").sha256(a.config.read_bytes()).hexdigest(), "protocol_sha256": manifest["protocol_hash"], "contract_sha256": manifest["contract_hash"], "source_sha256": manifest["source_sha256"]}
    a.metrics.with_suffix(".json").write_text(json.dumps(run, indent=2) + "\n", encoding="utf-8")
    a.report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Final test evaluation", "", "Pre-registered models were fit on the fixed training dates. Validation and final test were scored once; no hyperparameters were changed after opening the test.", "", f"- Final test sessions: {len(observed_dates)} ({observed_dates[0]}–{observed_dates[-1]}); rows with complete features: {len(test_rows):,}.", f"- Device: {device}; runtime {run['runtime_seconds']} s; peak RSS {run['peak_rss_kib']:,} KiB.", "- Main paired contrast: independent vs shared MLP, same sample intersection. Paired bootstrap resamples five-session blocks; test p-values are not reported.", "- Probability scores estimate reproduction of retrospective B0 labels only. They are not independently validated market probabilities; there is no profitability claim.", "", "## Paired primary contrast: test block-bootstrap of MCC difference", "", "| Target | Independent minus shared MCC | 95% session-block CI |", "|---|---:|---:|"]
    for target, result in bootstrap.items():
        if result:
            ci = result["ci95"]
            lines.append(f"| {target} | {result['mean_mcc_difference_independent_minus_shared']:.4f} | [{ci[0]:.4f}, {ci[1]:.4f}] |")
    lines += ["", "## Complete metrics", "", "All models, targets, roots, and three pre-fixed test blocks are in `final_test_metrics.csv`. The JSON sidecar records fit times, memory, hashes, and exact dates.", ""]
    a.report.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(run, indent=2))


if __name__ == "__main__":
    main()
