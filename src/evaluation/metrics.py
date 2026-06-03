"""Classification metrics for optimizer benchmark outputs."""

from __future__ import annotations

import json
from typing import Any

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    matthews_corrcoef,
    precision_score,
    recall_score,
    roc_auc_score,
)


def _safe_auc(metric_fn: Any, y_true: np.ndarray, y_proba: np.ndarray) -> float:
    try:
        if len(np.unique(y_true)) < 2:
            return float("nan")
        return float(metric_fn(y_true, y_proba))
    except Exception:
        return float("nan")


def compute_classification_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_proba: np.ndarray | None = None,
) -> dict[str, Any]:
    """Compute required binary classification metrics."""
    if y_proba is None:
        y_proba = y_pred.astype(float)

    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "mcc": float(matthews_corrcoef(y_true, y_pred)),
        "auc_roc": _safe_auc(roc_auc_score, y_true, y_proba),
        "auc_pr": _safe_auc(average_precision_score, y_true, y_proba),
        "confusion_matrix": json.dumps(cm.tolist()),
    }
