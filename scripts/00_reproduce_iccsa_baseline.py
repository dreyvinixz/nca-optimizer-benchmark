from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])
sys.path.insert(0, str(ROOT))

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

from src.benchmark import prepare_benchmark
from src.evaluation.metrics import compute_classification_metrics
from src.utils.io import project_path, write_text
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("reproduce_iccsa", "logs/experiments/reproduce_iccsa.log")
    data, _ = prepare_benchmark()
    logger.info("Training temporal Random Forest baseline with InfoGain_[7] features")

    # Match the final-refit rule used after hyperparameter selection in the
    # official benchmark: training and validation are combined only after no
    # further selection is performed, and the locked test remains untouched.
    X_train_val = pd.concat(
        [pd.DataFrame(data.X_train), pd.DataFrame(data.X_val)], ignore_index=True
    ).to_numpy()
    y_train_val = pd.concat(
        [pd.Series(data.y_train), pd.Series(data.y_val)], ignore_index=True
    ).to_numpy()
    scaler = StandardScaler()
    X_train_val_scaled = scaler.fit_transform(X_train_val)
    X_test_scaled = scaler.transform(data.X_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train_val_scaled, y_train_val)
    proba = model.predict_proba(X_test_scaled)[:, 1]
    pred = (proba >= 0.5).astype(int)
    metrics = compute_classification_metrics(data.y_test, pred, proba)

    rows = [{
        "model": "random_forest_default_temporal_refit",
        "fit_partition": "training_plus_validation",
        "n_estimators": 100,
        "random_state": 42,
        **metrics,
    }]
    output_path = project_path("outputs/metrics/iccsa_baseline_temporal.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(output_path, index=False)

    write_text(
        "outputs/reports/iccsa_baseline_temporal.md",
        "\n".join(
            [
                "# ICCSA Baseline Reproduction",
                "",
                "This is a default Random Forest reference under the journal temporal protocol.",
                "It uses the ICCSA Information Gain feature subset, then follows the journal final-refit rule by fitting on training plus validation before locked testing.",
                "It is not a byte-for-byte rerun of the conference script, which used random sampling across the whole period.",
                "",
                f"- Accuracy: {metrics['accuracy']:.4f}",
                f"- Balanced accuracy: {metrics['balanced_accuracy']:.4f}",
                f"- F1: {metrics['f1']:.4f}",
                f"- MCC: {metrics['mcc']:.4f}",
                f"- AUC-ROC: {metrics['auc_roc']:.4f}",
                f"- AUC-PR: {metrics['auc_pr']:.4f}",
            ]
        ),
    )
    logger.info("ICCSA baseline reproduction outputs saved")


if __name__ == "__main__":
    main()
