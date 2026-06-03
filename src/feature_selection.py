"""Feature selection helpers for historical Information Gain features."""

from __future__ import annotations


def indices_to_feature_names(indices: list[int], feature_columns: list[str]) -> list[str]:
    """Convert historical feature indices into column names.

    The indices are interpreted over the modeling feature columns, excluding
    datetime and target labels, matching the legacy ICCSA/IJCNN pipeline.
    """
    names: list[str] = []
    for index in indices:
        if index < 0 or index >= len(feature_columns):
            raise IndexError(
                f"Feature index {index} is outside the available feature range "
                f"0..{len(feature_columns) - 1}."
            )
        names.append(feature_columns[index])
    return names


def select_features(feature_columns: list[str], selected_indices: list[int]) -> list[str]:
    return indices_to_feature_names(selected_indices, feature_columns)
