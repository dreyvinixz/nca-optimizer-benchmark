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


def evaluate_candidate(
    model_type: str,
    optimizer_name: str,
    candidate: dict[str, Any],
    seed: int,
    config: dict[str, Any],
    prepared_data: Any,
    evaluation_id: int,
) -> dict[str, Any]:
    """Train on temporal train split and score on validation split."""
    candidate = normalize_candidate(candidate, config["search_spaces"], model_type)
    model_config = config["experiment"]["model"]
    
    started = time.perf_counter()
    if model_type == "mlp":
        if model_config.get("backend") == "cuda":
            from src.models.mlp_cuda import fit_predict_mlp_cuda

            y_pred, y_proba, _, backend = fit_predict_mlp_cuda(
                prepared_data.X_train_scaled, prepared_data.y_train, prepared_data.X_val_scaled, candidate, model_config, seed + evaluation_id
            )
        else:
            y_pred, y_proba, _, backend = fit_predict_mlp_cpu(
                prepared_data.X_train_scaled, prepared_data.y_train, prepared_data.X_val_scaled, candidate, model_config, seed + evaluation_id
            )
    elif model_type == "svm":
        y_pred, y_proba, _, backend = fit_predict_svm(
            prepared_data.X_train_scaled, prepared_data.y_train, prepared_data.X_val_scaled, candidate, model_config, seed + evaluation_id
        )
    elif model_type == "rf":
        y_pred, y_proba, _, backend = fit_predict_rf(
            prepared_data.X_train_scaled, prepared_data.y_train, prepared_data.X_val_scaled, candidate, model_config, seed + evaluation_id
        )
    elif model_type == "cnn":
        if model_config.get("backend") == "cuda":
            from src.models.cnn_cuda import fit_predict_cnn_cuda

            y_pred, y_proba, _, backend = fit_predict_cnn_cuda(
                prepared_data.X_train_scaled, prepared_data.y_train, prepared_data.X_val_scaled, candidate, model_config, seed + evaluation_id
            )
        else:
            y_pred, y_proba, _, backend = fit_predict_cnn(
                prepared_data.X_train_scaled, prepared_data.y_train, prepared_data.X_val_scaled, candidate, model_config, seed + evaluation_id
            )
    else:
        raise ValueError(f"Unknown model_type: {model_type}")
        
    train_time = time.perf_counter() - started
    metrics = compute_classification_metrics(prepared_data.y_val, y_pred, y_proba)
    weights = config["experiment"]["objective"]["fitness"]
    fitness = weights["mcc_weight"] * metrics["mcc"] + weights["f1_weight"] * metrics["f1"]

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
        "fitness_formula": f"{weights['mcc_weight']} * MCC + {weights['f1_weight']} * F1",
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
    model_config = config["experiment"]["model"]
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
    weights = config["experiment"]["objective"]["fitness"]
    fitness = weights["mcc_weight"] * metrics["mcc"] + weights["f1_weight"] * metrics["f1"]

    summary = {
        "model_type": model_type,
        "optimizer": optimizer_name,
        "seed": seed,
        "runtime_seconds_test": float(runtime),
        "model_backend": backend,
        "official_experiment": config["experiment"]["benchmark"].get("official_experiment", False),
        "fitness_formula": f"{weights['mcc_weight']} * MCC + {weights['f1_weight']} * F1",
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
