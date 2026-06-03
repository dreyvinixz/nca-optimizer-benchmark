"""Preprocessing helpers for the benchmark pipeline."""

from __future__ import annotations

import pandas as pd


def keep_numeric_features(frame: pd.DataFrame, feature_columns: list[str]) -> list[str]:
    """Return selected columns that are numeric and usable by the MLP."""
    numeric = frame[feature_columns].select_dtypes(include=["number"]).columns
    return list(numeric)


def drop_missing_rows(frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Drop rows with missing values in modeling columns."""
    return frame.dropna(subset=columns).reset_index(drop=True)
