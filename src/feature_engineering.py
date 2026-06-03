"""Feature engineering helpers for future benchmark extensions.

The first NCA benchmark intentionally reuses the legacy technical indicators
already present in `data/raw/merged_output.csv`. This module
keeps feature-engineering utilities in `src/` so future work can add indicators
without modifying legacy experiment code.
"""

from __future__ import annotations

import pandas as pd


def validate_required_price_columns(frame: pd.DataFrame) -> None:
    """Validate OHLCV columns needed by future indicator-generation routines."""
    required = {"open", "high", "low", "close", "volume"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"Missing price columns for feature engineering: {missing}")


def add_moving_average_spreads(
    frame: pd.DataFrame,
    source_column: str = "close",
    windows: tuple[int, ...] = (3, 5, 7, 9),
) -> pd.DataFrame:
    """Add simple moving averages and pairwise spreads.

    This is not used by the initial benchmark, because those indicators already
    exist in the legacy dataset. It is provided for controlled future datasets.
    """
    output = frame.copy()
    for window in windows:
        output[f"SMA_{window}"] = output[source_column].rolling(window=window, min_periods=window).mean()

    for i, larger in enumerate(windows):
        for smaller in windows[:i]:
            output[f"SMA_{larger}-{smaller}"] = output[f"SMA_{larger}"] - output[f"SMA_{smaller}"]
    return output


def add_exponential_moving_average_spreads(
    frame: pd.DataFrame,
    source_column: str = "close",
    windows: tuple[int, ...] = (3, 5, 7, 9),
) -> pd.DataFrame:
    """Add exponential moving averages and pairwise spreads."""
    output = frame.copy()
    for window in windows:
        output[f"EMA_{window}"] = output[source_column].ewm(span=window, adjust=False).mean()

    for i, larger in enumerate(windows):
        for smaller in windows[:i]:
            output[f"EMA_{larger}-{smaller}"] = output[f"EMA_{larger}"] - output[f"EMA_{smaller}"]
    return output
