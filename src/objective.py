"""Central candidate evaluation shared by all optimizers."""

from __future__ import annotations

import time
from typing import Any

import numpy as np

from src.evaluation.metrics import compute_classification_metrics
from src.models.mlp import fit_predict_mlp


def normalize_candidate(candidate: dict[str, Any], search_space: dict[str, Any]) -> dict[str, Any]:
    """Clamp and cast candidate hyperparameters to valid MLP search-space values."""
    mlp_space = search_space["mlp"]
    batch_values = list(mlp_space["batch_size"]["values"])

    hidden = int(round(float(candidate["hidden_neurons"])))
    hidden = max(int(mlp_space["hidden_neurons"]["min"]), min(int(mlp_space["hidden_neurons"]["max"]), hidden))

    learning_rate = float(candidate["learning_rate"])
    learning_rate = max(float(mlp_space["learning_rate"]["min"]), min(float(mlp_space["learning_rate"]["max"]), learning_rate))

    l2_alpha = float(candidate["l2_alpha"])
    l2_alpha = max(float(mlp_space["l2_alpha"]["min"]), min(float(mlp_space["l2_alpha"]["max"]), l2_alpha))

    dropout = float(candidate["dropout_rate"])
    dropout = max(float(mlp_space["dropout_rate"]["min"]), min(float(mlp_space["dropout_rate"]["max"]), dropout))

    if "batch_size_index" in candidate:
        idx = int(round(float(candidate["batch_size_index"])))
        batch_size = batch_values[max(0, min(len(batch_values) - 1, idx))]
    else:
        batch_size = int(candidate["batch_size"])
        batch_size = min(batch_values, key=lambda value: abs(value - batch_size))

    return {
        "hidden_neurons": hidden,
        "learning_rate": learning_rate,
        "l2_alpha": l2_alpha,
        "dropout_rate": dropout,
        "batch_size": int(batch_size),
    }


def vector_to_candidate(vector: np.ndarray, search_space: dict[str, Any]) -> dict[str, Any]:
    """Decode a continuous optimizer vector into an MLP candidate."""
    return normalize_candidate(
        {
            "hidden_neurons": vector[0],
            "learning_rate": 10 ** float(vector[1]),
            "l2_alpha": 10 ** float(vector[2]),
            "dropout_rate": vector[3],
            "batch_size_index": vector[4],
        },
        search_space,
    )


def candidate_to_log(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "hidden_neurons": int(candidate["hidden_neurons"]),
        "learning_rate": float(candidate["learning_rate"]),
        "l2_alpha": float(candidate["l2_alpha"]),
        "dropout_rate": float(candidate["dropout_rate"]),
        "batch_size": int(candidate["batch_size"]),
    }


def evaluate_candidate(
    candidate: dict[str, Any],
    data: Any,
    config: dict[str, Any],
    seed: int,
    evaluation_id: int,
    optimizer_name: str,
) -> dict[str, Any]:
    """Train on temporal train split and score on validation split."""
    candidate = normalize_candidate(candidate, config["search_spaces"])
    started = time.perf_counter()
    y_pred, y_proba, _, _, backend = fit_predict_mlp(
        data.X_train,
        data.y_train,
        data.X_val,
        candidate,
        config["experiment"]["model"],
        seed + evaluation_id,
    )
    runtime = time.perf_counter() - started
    metrics = compute_classification_metrics(data.y_val, y_pred, y_proba)
    weights = config["experiment"]["objective"]["fitness"]
    fitness = weights["mcc_weight"] * metrics["mcc"] + weights["f1_weight"] * metrics["f1"]

    row = {
        "experiment_name": config["experiment"]["experiment"]["name"],
        "optimizer": optimizer_name,
        "seed": seed,
        "evaluation_id": evaluation_id,
        "fitness": float(fitness),
        "runtime_seconds": float(runtime),
        "backend": backend,
    }
    row.update({f"{key}_val": value for key, value in metrics.items()})
    row.update(candidate_to_log(candidate))
    return row


def evaluate_best_on_test(
    candidate: dict[str, Any],
    data: Any,
    config: dict[str, Any],
    seed: int,
    optimizer_name: str,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Retrain on train+validation data and score the untouched test split."""
    candidate = normalize_candidate(candidate, config["search_spaces"])
    X_train_full = np.vstack([data.X_train, data.X_val])
    y_train_full = np.concatenate([data.y_train, data.y_val])

    started = time.perf_counter()
    y_pred, y_proba, _, _, backend = fit_predict_mlp(
        X_train_full,
        y_train_full,
        data.X_test,
        candidate,
        config["experiment"]["model"],
        seed + 100000,
    )
    runtime = time.perf_counter() - started
    metrics = compute_classification_metrics(data.y_test, y_pred, y_proba)

    summary = {
        "experiment_name": config["experiment"]["experiment"]["name"],
        "optimizer": optimizer_name,
        "seed": seed,
        "runtime_seconds_test": float(runtime),
        "backend": backend,
    }
    summary.update({f"{key}_test": value for key, value in metrics.items()})
    summary.update(candidate_to_log(candidate))

    predictions: list[dict[str, Any]] = []
    datetime_column = config["experiment"]["data"]["datetime_column"]
    for idx, (pred, proba) in enumerate(zip(y_pred, y_proba)):
        meta = data.test_metadata.iloc[idx].to_dict()
        predictions.append(
            {
                "optimizer": optimizer_name,
                "seed": seed,
                "row_id": idx,
                "datetime": meta.get(datetime_column),
                "y_true": int(data.y_test[idx]),
                "y_pred": int(pred),
                "y_proba": float(proba),
            }
        )
    return summary, predictions
