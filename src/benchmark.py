"""Shared setup and persistence for benchmark scripts."""

from __future__ import annotations

import dataclasses
from typing import Any

from sklearn.preprocessing import StandardScaler

from src.data_loader import load_legacy_dataset
from src.feature_selection import select_features
from src.preprocessing import drop_missing_rows, keep_numeric_features
from src.temporal_split import TemporalSplit, make_temporal_split
from src.utils.io import append_csv, ensure_output_directories, load_project_configs, project_path, save_csv


def prepare_benchmark() -> tuple[TemporalSplit, dict[str, Any]]:
    """Load configs, prepare the temporal split, and return data plus config."""
    config = load_project_configs()
    ensure_output_directories(config["paths"])

    exp = config["experiment"]
    dataset = load_legacy_dataset(
        config["paths"]["dataset"]["merged_output"],
        exp["data"]["datetime_column"],
        exp["data"]["target_column"],
        exp["data"]["label_mapping"],
    )
    numeric_features = keep_numeric_features(dataset.frame, dataset.feature_columns)
    selected = select_features(numeric_features, exp["data"]["selected_feature_indices"])
    modeling_columns = selected + [dataset.target_column, dataset.datetime_column]
    frame = drop_missing_rows(dataset.frame, modeling_columns)

    split_cfg = exp["split"]
    data = make_temporal_split(
        frame=frame,
        feature_names=selected,
        target_column=dataset.target_column,
        datetime_column=dataset.datetime_column,
        train_size=float(split_cfg["train_size"]),
        validation_size=float(split_cfg["validation_size"]),
        test_size=float(split_cfg["test_size"]),
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(data.X_train).astype("float32")
    X_val_scaled = scaler.transform(data.X_val).astype("float32")
    X_test_scaled = scaler.transform(data.X_test).astype("float32")

    data = dataclasses.replace(
        data,
        X_train_scaled=X_train_scaled,
        X_val_scaled=X_val_scaled,
        X_test_scaled=X_test_scaled,
        scaler=scaler
    )

    return data, config


def clear_optimizer_outputs(optimizer_name: str, config: dict[str, Any]) -> None:
    paths = config["paths"]["outputs"]
    files = [
        f"{paths['metrics']}/{optimizer_name}_runs.csv",
        f"{paths['metrics']}/{optimizer_name}_best_by_seed.csv",
        f"{paths['convergence']}/{optimizer_name}_convergence.csv",
        f"{paths['predictions']}/{optimizer_name}_predictions.csv",
    ]
    for path in files:
        resolved = project_path(path)
        if resolved.exists():
            resolved.unlink()


def append_optimizer_outputs(optimizer_name: str, results: dict[str, list[dict[str, Any]]], config: dict[str, Any]) -> None:
    paths = config["paths"]["outputs"]
    append_csv(results["runs"], f"{paths['metrics']}/{optimizer_name}_runs.csv")
    append_csv(results["best"], f"{paths['metrics']}/{optimizer_name}_best_by_seed.csv")
    append_csv(results["convergence"], f"{paths['convergence']}/{optimizer_name}_convergence.csv")
    append_csv(results["predictions"], f"{paths['predictions']}/{optimizer_name}_predictions.csv")
