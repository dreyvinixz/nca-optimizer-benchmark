"""Shared setup and persistence for benchmark scripts."""

from __future__ import annotations

from typing import Any

from src.data_loader import load_legacy_dataset
from src.feature_selection import select_features
from src.preprocessing import drop_missing_rows, keep_numeric_features
from src.temporal_split import TemporalSplit, make_temporal_split
from src.utils.io import ensure_output_directories, load_project_configs, save_csv


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
    return data, config


def save_optimizer_outputs(optimizer_name: str, results: dict[str, list[dict[str, Any]]], config: dict[str, Any]) -> None:
    paths = config["paths"]["outputs"]
    save_csv(results["runs"], f"{paths['metrics']}/{optimizer_name}_runs.csv")
    save_csv(results["best"], f"{paths['metrics']}/{optimizer_name}_best_by_seed.csv")
    save_csv(results["convergence"], f"{paths['convergence']}/{optimizer_name}_convergence.csv")
    save_csv(results["predictions"], f"{paths['predictions']}/{optimizer_name}_predictions.csv")
