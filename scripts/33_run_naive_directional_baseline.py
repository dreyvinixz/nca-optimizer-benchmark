from __future__ import annotations

"""Evaluate a leakage-free majority-direction baseline on the locked test block."""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])
sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd

from src.benchmark import prepare_benchmark
from src.evaluation.metrics import compute_classification_metrics
from src.utils.io import project_path, write_text
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("naive_directional_baseline", "logs/experiments/naive_directional_baseline.log")
    data, _ = prepare_benchmark()

    train_uptrend_rate = float(np.mean(data.y_train))
    predicted_class = int(train_uptrend_rate >= 0.5)
    y_pred = np.full(len(data.y_test), predicted_class, dtype=int)
    y_proba = np.full(len(data.y_test), train_uptrend_rate, dtype=float)
    metrics = compute_classification_metrics(data.y_test, y_pred, y_proba)

    direction = "uptrend" if predicted_class == 1 else "downtrend"
    row = {
        "model": "naive_majority_direction_temporal",
        "selection_source": "training_partition_only",
        "train_uptrend_rate": train_uptrend_rate,
        "predicted_direction": direction,
        **metrics,
    }
    output_path = project_path("outputs/metrics/naive_majority_direction_temporal.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([row]).to_csv(output_path, index=False)

    write_text(
        "outputs/reports/naive_majority_direction_temporal.md",
        "\n".join(
            [
                "# Naive Majority-Direction Baseline",
                "",
                "The predicted direction is selected exclusively from the training partition.",
                "It is a predictive reference and is not a deployable trading strategy.",
                "",
                f"- Training uptrend rate: {train_uptrend_rate:.4f}",
                f"- Predicted direction: {direction}",
                f"- Accuracy: {metrics['accuracy']:.4f}",
                f"- Balanced accuracy: {metrics['balanced_accuracy']:.4f}",
                f"- F1: {metrics['f1']:.4f}",
                f"- MCC: {metrics['mcc']:.4f}",
                f"- AUC-ROC: {metrics['auc_roc']:.4f}",
                f"- AUC-PR: {metrics['auc_pr']:.4f}",
            ]
        ),
    )
    logger.info("Naive majority-direction baseline outputs saved")


if __name__ == "__main__":
    main()
