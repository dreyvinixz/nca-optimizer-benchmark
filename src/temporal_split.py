"""Chronological train/validation/test splitting."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class TemporalSplit:
    X_train: np.ndarray
    y_train: np.ndarray
    X_val: np.ndarray
    y_val: np.ndarray
    X_test: np.ndarray
    y_test: np.ndarray
    test_metadata: pd.DataFrame
    feature_names: list[str]


def make_temporal_split(
    frame: pd.DataFrame,
    feature_names: list[str],
    target_column: str,
    datetime_column: str,
    train_size: float,
    validation_size: float,
    test_size: float,
) -> TemporalSplit:
    """Split data chronologically into train, validation, and test subsets."""
    total = train_size + validation_size + test_size
    if abs(total - 1.0) > 1e-8:
        raise ValueError(f"Split fractions must sum to 1.0, got {total}.")

    ordered = frame.sort_values(datetime_column).reset_index(drop=True)
    n_rows = len(ordered)
    if n_rows < 10:
        raise ValueError("Temporal split requires at least 10 rows.")

    train_end = int(n_rows * train_size)
    val_end = train_end + int(n_rows * validation_size)
    if train_end <= 0 or val_end <= train_end or val_end >= n_rows:
        raise ValueError("Invalid temporal split sizes for dataset length.")

    X = ordered[feature_names].to_numpy(dtype="float32")
    y = ordered[target_column].to_numpy(dtype="int32")

    test_metadata = ordered.iloc[val_end:][[datetime_column, target_column]].copy()
    return TemporalSplit(
        X_train=X[:train_end],
        y_train=y[:train_end],
        X_val=X[train_end:val_end],
        y_val=y[train_end:val_end],
        X_test=X[val_end:],
        y_test=y[val_end:],
        test_metadata=test_metadata.reset_index(drop=True),
        feature_names=feature_names,
    )
