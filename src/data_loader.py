"""Dataset loading for the NCA optimizer benchmark."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from src.utils.io import project_path


@dataclass(frozen=True)
class LoadedDataset:
    frame: pd.DataFrame
    feature_columns: list[str]
    target_column: str
    datetime_column: str


def load_legacy_dataset(
    dataset_path: str | Path,
    datetime_column: str,
    target_column: str,
    label_mapping: dict[str, int],
) -> LoadedDataset:
    """Load the legacy IJCNN CSV, validate key columns, map labels, and sort by time."""
    path = project_path(dataset_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    frame = pd.read_csv(path, parse_dates=[datetime_column])
    required = {datetime_column, target_column}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")

    frame = frame[frame[target_column].isin(label_mapping.keys())].copy()
    frame[target_column] = frame[target_column].map(label_mapping).astype(int)
    frame = frame.sort_values(datetime_column).reset_index(drop=True)

    excluded_columns = {datetime_column, target_column, "id_ticker"}
    feature_columns = [
        column for column in frame.columns
        if column not in excluded_columns
    ]
    if not feature_columns:
        raise ValueError("No feature columns were found after excluding datetime and target.")

    return LoadedDataset(
        frame=frame,
        feature_columns=feature_columns,
        target_column=target_column,
        datetime_column=datetime_column,
    )
