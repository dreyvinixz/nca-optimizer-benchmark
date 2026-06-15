"""Central candidate evaluation shared by all optimizers and models."""

from __future__ import annotations

import time
import json
from pathlib import Path
from typing import Any

import numpy as np

from src.evaluation.metrics import compute_classification_metrics
from src.models.mlp import fit_predict_mlp as fit_predict_mlp_cpu
from src.models.svm_model import fit_predict_svm
from src.models.rf_model import fit_predict_rf
from src.models.cnn import fit_predict_cnn

CV_FOLDS = 3

def get_bounds(search_space: dict[str, Any], model_type: str) -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Return lower bounds, upper bounds, and variable types for a model's search space."""
    space = search_space.get(model_type, {})
    lower = []
    upper = []
    types = []
    for key, spec in space.items():
        if spec["type"] == "categorical":
            lower.append(0.0)
            upper.append(float(len(spec["values"]) - 1))
            types.append("categorical")
        elif spec["type"] == "int":
            lower.append(float(spec["min"]))
            upper.append(float(spec["max"]))
            types.append("int")
        elif spec["type"] == "float":
            if spec.get("scale") == "log10":
                lower.append(np.log10(float(spec["min"])))
                upper.append(np.log10(float(spec["max"])))
            else:
                lower.append(float(spec["min"]))
                upper.append(float(spec["max"]))
            types.append("float")
    return np.array(lower), np.array(upper), types

def normalize_candidate(candidate: dict[str, Any], search_space: dict[str, Any], model_type: str) -> dict[str, Any]:
    """Clamp and cast candidate hyperparameters to valid search-space values with discrete mapping."""
    space = search_space.get(model_type, {})
    normalized = {}
    
    for key, spec in space.items():
        if key not in candidate and f"{key}_index" not in candidate:
            continue
            
        val_type = spec["type"]
        
        if val_type == "categorical":
            values = spec["values"]
            idx_key = f"{key}_index"
            
            # If the candidate was provided via continuous optimizer (index)
            if idx_key in candidate:
                idx = int(round(float(candidate[idx_key])))
                idx = max(0, min(len(values) - 1, idx))
                normalized[key] = values[idx]
            # If it's already categorical (GA might provide it directly if using mixed representation)
            elif key in candidate:
                val = candidate[key]
                if val in values:
                    normalized[key] = val
                else:
                    # Treat as index if it's numeric but key doesn't have _index
                    try:
                        idx = int(round(float(val)))
                        idx = max(0, min(len(values) - 1, idx))
                        normalized[key] = values[idx]
                    except (ValueError, TypeError):
                        normalized[key] = values[0]
                        
        elif val_type == "int":
            val = int(round(float(candidate[key])))
            normalized[key] = max(int(spec["min"]), min(int(spec["max"]), val))
            
        elif val_type == "float":
            val = float(candidate[key])
            normalized[key] = max(float(spec["min"]), min(float(spec["max"]), val))
            
    return normalized


def vector_to_candidate(vector: np.ndarray, search_space: dict[str, Any], model_type: str) -> dict[str, Any]:
    """Decode a continuous optimizer vector into a candidate dictionary."""
    space = search_space.get(model_type, {})
    cand = {}
    for i, (key, spec) in enumerate(space.items()):
        val = float(vector[i])
        if spec["type"] == "categorical":
            cand[f"{key}_index"] = val
        elif spec["type"] == "float" and spec.get("scale") == "log10":
            cand[key] = 10 ** val
        else:
            cand[key] = val
    return normalize_candidate(cand, search_space, model_type)


def _dispatch_model(
    model_type: str,
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidate: dict[str, Any],
    model_config: dict[str, Any],
    seed: int,
) -> tuple[np.ndarray, np.ndarray, dict[str, Any], str]:
    if model_type == "mlp":
        if model_config.get("backend") == "cuda":
            from src.models.mlp_cuda import fit_predict_mlp_cuda
            return fit_predict_mlp_cuda(X_train, y_train, X_eval, candidate, model_config, seed)
        else:
            from src.models.mlp import fit_predict_mlp as fit_predict_mlp_cpu
            return fit_predict_mlp_cpu(X_train, y_train, X_eval, candidate, model_config, seed)
    elif model_type == "svm":
        from src.models.svm_model import fit_predict_svm
        return fit_predict_svm(X_train, y_train, X_eval, candidate, model_config, seed)
    elif model_type == "rf":
        from src.models.rf_model import fit_predict_rf
        return fit_predict_rf(X_train, y_train, X_eval, candidate, model_config, seed)
    elif model_type == "cnn":
        if model_config.get("backend") == "cuda":
            from src.models.cnn_cuda import fit_predict_cnn_cuda
            return fit_predict_cnn_cuda(X_train, y_train, X_eval, candidate, model_config, seed)
        else:
            from src.models.cnn import fit_predict_cnn
            return fit_predict_cnn(X_train, y_train, X_eval, candidate, model_config, seed)
    else:
        raise ValueError(f"Unknown model_type: {model_type}")


def _mcc_f1_fitness(metrics: dict[str, Any], config: dict[str, Any]) -> tuple[float, str]:
    weights = config["experiment"]["objective"]["fitness"]
    fitness = float(weights["mcc_weight"] * metrics["mcc"] + weights["f1_weight"] * metrics["f1"])
    formula = f"{weights['mcc_weight']} * MCC + {weights['f1_weight']} * F1"
    return fitness, formula


def _accuracy_holdout_fitness(acc_train: float, acc_val: float) -> tuple[float, str]:
    return float(0.4 * acc_train + 0.6 * acc_val), "0.4*Acc_train + 0.6*Acc_val"


def _fitness_formula_for_mode(fitness_mode: str, config: dict[str, Any]) -> str:
    if fitness_mode == "mcc_f1":
        return _mcc_f1_fitness({"mcc": 0.0, "f1": 0.0}, config)[1]
    if fitness_mode == "accuracy_holdout":
        return "0.4*Acc_train + 0.6*Acc_val"
    if fitness_mode == "mcc_f1_cv":
        return "mean(0.6*MCC_val_fold + 0.4*F1_val_fold)"
    if fitness_mode == "accuracy_cv":
        return "mean(0.4*Acc_train_fold + 0.6*Acc_val_fold)"
    return fitness_mode


def _mean_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    keys = ["mcc", "f1", "auc_roc", "auc_pr", "accuracy", "precision", "recall", "balanced_accuracy"]
    return {
        key: float(np.nanmean([row.get(key, np.nan) for row in rows]))
        for key in keys
    }

def evaluate_candidate(
    model_type: str,
    optimizer_name: str,
    candidate: dict[str, Any],
    seed: int,
    config: dict[str, Any],
    prepared_data: Any,
    evaluation_id: int,
) -> dict[str, Any]:
    """Train on temporal train split and score on validation split, or use CV."""
    candidate = normalize_candidate(candidate, config["search_spaces"], model_type)
    model_config = config["experiment"]["model"].copy()
    model_config["probability"] = False  # Disable SVM proba for massive speedup
    
    fitness_mode = config["experiment"]["objective"].get("fitness_mode", "mcc_f1")
    
    started = time.perf_counter()
    
    if fitness_mode == "accuracy_cv":
        from sklearn.model_selection import TimeSeriesSplit
        from sklearn.metrics import accuracy_score
        
        X_full_train_scaled = np.vstack([prepared_data.X_train_scaled, prepared_data.X_val_scaled])
        y_full_train = np.concatenate([prepared_data.y_train, prepared_data.y_val])
        
        tscv = TimeSeriesSplit(n_splits=3)
        fold_fitnesses = []
        acc_trains = []
        acc_vals = []
        
        backend = "unknown"
        for train_idx, val_idx in tscv.split(X_full_train_scaled):
            X_tr, X_v = X_full_train_scaled[train_idx], X_full_train_scaled[val_idx]
            y_tr, y_v = y_full_train[train_idx], y_full_train[val_idx]
            
            X_eval_combined = np.vstack([X_tr, X_v])
            y_pred_comb, _, _, backend = _dispatch_model(
                model_type, X_tr, y_tr, X_eval_combined, candidate, model_config, seed + evaluation_id
            )
            
            y_pred_tr = y_pred_comb[:len(X_tr)]
            y_pred_v = y_pred_comb[len(X_tr):]
            
            acc_tr = float(accuracy_score(y_tr, y_pred_tr))
            acc_v = float(accuracy_score(y_v, y_pred_v))
            
            fold_fitness = 0.4 * acc_tr + 0.6 * acc_v
            fold_fitnesses.append(fold_fitness)
            acc_trains.append(acc_tr)
            acc_vals.append(acc_v)
            
        fitness = float(np.mean(fold_fitnesses))
        acc_train_mean = float(np.mean(acc_trains))
        acc_val_mean = float(np.mean(acc_vals))
        
        metrics = {
            "mcc": 0.0, "f1": 0.0, "auc_roc": 0.0, "auc_pr": 0.0,
            "accuracy": acc_val_mean, "precision": 0.0, "recall": 0.0,
            "balanced_accuracy": 0.0,
        }
        fitness_formula = "mean(0.4*Acc_tr + 0.6*Acc_val)"

    elif fitness_mode == "mcc_f1_cv":
        from sklearn.model_selection import TimeSeriesSplit

        X_full_train_scaled = np.vstack([prepared_data.X_train_scaled, prepared_data.X_val_scaled])
        y_full_train = np.concatenate([prepared_data.y_train, prepared_data.y_val])

        tscv = TimeSeriesSplit(n_splits=CV_FOLDS)
        fold_fitnesses = []
        fold_metrics = []
        acc_trains = []

        backend = "unknown"
        for train_idx, val_idx in tscv.split(X_full_train_scaled):
            X_tr, X_v = X_full_train_scaled[train_idx], X_full_train_scaled[val_idx]
            y_tr, y_v = y_full_train[train_idx], y_full_train[val_idx]

            X_eval_combined = np.vstack([X_tr, X_v])
            y_pred_comb, y_proba_comb, _, backend = _dispatch_model(
                model_type, X_tr, y_tr, X_eval_combined, candidate, model_config, seed + evaluation_id
            )

            y_pred_tr = y_pred_comb[:len(X_tr)]
            y_pred_v = y_pred_comb[len(X_tr):]
            y_proba_v = y_proba_comb[len(X_tr):]

            metrics_v = compute_classification_metrics(y_v, y_pred_v, y_proba_v)
            fold_fitness, _ = _mcc_f1_fitness(metrics_v, config)
            fold_fitnesses.append(fold_fitness)
            fold_metrics.append(metrics_v)
            acc_trains.append(float(np.mean(y_pred_tr == y_tr)))

        fitness = float(np.mean(fold_fitnesses))
        metrics = _mean_metrics(fold_metrics)
        acc_train_mean = float(np.mean(acc_trains))
        fitness_formula = "mean(0.6*MCC_val_fold + 0.4*F1_val_fold)"

    elif fitness_mode == "accuracy_holdout":
        from sklearn.metrics import accuracy_score

        X_eval_combined = np.vstack([prepared_data.X_train_scaled, prepared_data.X_val_scaled])
        y_pred_comb, y_proba_comb, _, backend = _dispatch_model(
            model_type, prepared_data.X_train_scaled, prepared_data.y_train, X_eval_combined,
            candidate, model_config, seed + evaluation_id
        )
        y_pred_train = y_pred_comb[:len(prepared_data.X_train_scaled)]
        y_pred_val = y_pred_comb[len(prepared_data.X_train_scaled):]
        y_proba_val = y_proba_comb[len(prepared_data.X_train_scaled):]

        acc_train_mean = float(accuracy_score(prepared_data.y_train, y_pred_train))
        metrics = compute_classification_metrics(prepared_data.y_val, y_pred_val, y_proba_val)
        fitness, fitness_formula = _accuracy_holdout_fitness(acc_train_mean, float(metrics["accuracy"]))
        
    elif fitness_mode == "mcc_f1":
        y_pred, y_proba, _, backend = _dispatch_model(
            model_type, prepared_data.X_train_scaled, prepared_data.y_train, prepared_data.X_val_scaled,
            candidate, model_config, seed + evaluation_id
        )
        metrics = compute_classification_metrics(prepared_data.y_val, y_pred, y_proba)
        fitness, fitness_formula = _mcc_f1_fitness(metrics, config)
        acc_train_mean = 0.0
    else:
        raise ValueError(
            "Unknown fitness_mode: "
            f"{fitness_mode}. Expected one of: mcc_f1, accuracy_holdout, mcc_f1_cv, accuracy_cv."
        )

    train_time = time.perf_counter() - started

    row = {
        "model_type": model_type,
        "optimizer": optimizer_name,
        "seed": seed,
        "candidate_id": evaluation_id,
        "fitness": float(fitness),
        "mcc": float(metrics["mcc"]),
        "f1": float(metrics["f1"]),
        "auc_roc": float(metrics["auc_roc"]),
        "auc_pr": float(metrics["auc_pr"]),
        "accuracy": float(metrics["accuracy"]),
        "precision": float(metrics["precision"]),
        "recall": float(metrics["recall"]),
        "train_time_seconds": float(train_time),
        "eval_time_seconds": 0.0, # Handled jointly with fit_predict
        "model_backend": backend,
        "official_experiment": config["experiment"]["benchmark"].get("official_experiment", False),
        "cache_hit": False,
        "cache_key": "",
        "parallel_enabled": config["experiment"]["benchmark"].get("parallel_enabled", False),
        "n_jobs": config["experiment"]["benchmark"].get("n_jobs", 1),
        "parallel_backend": config["experiment"]["benchmark"].get("parallel_backend", "none"),
        "fitness_formula": fitness_formula,
        "fitness_mode": fitness_mode,
        "acc_train": acc_train_mean,
        "decoded_hyperparameters": json.dumps(candidate)
    }
    return row


def evaluate_best_on_test(
    model_type: str,
    optimizer_name: str,
    candidate: dict[str, Any],
    seed: int,
    config: dict[str, Any],
    data: Any,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Retrain on train+validation data and score the untouched test split."""
    candidate = normalize_candidate(candidate, config["search_spaces"], model_type)
    model_config = config["experiment"]["model"].copy()
    model_config["probability"] = True  # Enable probability for final test scoring
    
    X_train_full = np.vstack([data.X_train, data.X_val])
    y_train_full = np.concatenate([data.y_train, data.y_val])

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_train_full_scaled = scaler.fit_transform(X_train_full).astype("float32")
    X_test_scaled = scaler.transform(data.X_test).astype("float32")

    started = time.perf_counter()
    model: Any = None
    if model_type == "mlp":
        if model_config.get("backend") == "cuda":
            from src.models.mlp_cuda import fit_predict_mlp_cuda

            y_pred, y_proba, model, backend = fit_predict_mlp_cuda(
                X_train_full_scaled, y_train_full, X_test_scaled, candidate, model_config, seed + 100000
            )
        else:
            y_pred, y_proba, model, backend = fit_predict_mlp_cpu(
                X_train_full_scaled, y_train_full, X_test_scaled, candidate, model_config, seed + 100000
            )
    elif model_type == "svm":
        y_pred, y_proba, _, backend = fit_predict_svm(
            X_train_full_scaled, y_train_full, X_test_scaled, candidate, model_config, seed + 100000
        )
    elif model_type == "rf":
        y_pred, y_proba, _, backend = fit_predict_rf(
            X_train_full_scaled, y_train_full, X_test_scaled, candidate, model_config, seed + 100000
        )
    elif model_type == "cnn":
        if model_config.get("backend") == "cuda":
            from src.models.cnn_cuda import fit_predict_cnn_cuda

            y_pred, y_proba, model, backend = fit_predict_cnn_cuda(
                X_train_full_scaled, y_train_full, X_test_scaled, candidate, model_config, seed + 100000
            )
        else:
            y_pred, y_proba, model, backend = fit_predict_cnn(
                X_train_full_scaled, y_train_full, X_test_scaled, candidate, model_config, seed + 100000
            )
    else:
        raise ValueError(f"Unknown model_type: {model_type}")

    runtime = time.perf_counter() - started
    metrics = compute_classification_metrics(data.y_test, y_pred, y_proba)
    fitness_mode = config["experiment"]["objective"].get("fitness_mode", "mcc_f1")

    summary = {
        "model_type": model_type,
        "optimizer": optimizer_name,
        "seed": seed,
        "runtime_seconds_test": float(runtime),
        "model_backend": backend,
        "official_experiment": config["experiment"]["benchmark"].get("official_experiment", False),
        "fitness_mode": fitness_mode,
        "fitness_formula": _fitness_formula_for_mode(fitness_mode, config),
        "decoded_hyperparameters": json.dumps(candidate)
    }
    summary.update({f"{key}_test": value for key, value in metrics.items()})

    predictions: list[dict[str, Any]] = []
    datetime_column = config["experiment"]["data"]["datetime_column"]
    for idx, (pred, proba) in enumerate(zip(y_pred, y_proba)):
        meta = data.test_metadata.iloc[idx].to_dict()
        predictions.append(
            {
                "model_type": model_type,
                "optimizer": optimizer_name,
                "seed": seed,
                "row_id": idx,
                "datetime": meta.get(datetime_column),
                "y_true": int(data.y_test[idx]),
                "y_pred": int(pred),
                "y_proba": float(proba),
            }
        )
        
    if hasattr(model, "_keras_history") and model._keras_history:
        try:
            import pandas as pd
            history_df = pd.DataFrame(model._keras_history)
            metrics_path = Path(config["paths"]["outputs"]["metrics"])
            metrics_path.mkdir(parents=True, exist_ok=True)
            history_df.to_csv(metrics_path / f"{model_type}_{optimizer_name}_seed{seed}_keras_history.csv", index=False)
        except Exception as e:
            import logging
            logging.getLogger("objective").warning(f"Failed to save keras history: {e}")

    return summary, predictions
