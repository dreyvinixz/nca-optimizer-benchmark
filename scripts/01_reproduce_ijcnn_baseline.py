from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])
sys.path.insert(0, str(ROOT))

import pandas as pd

from src.utils.io import project_path, write_text
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("reproduce_ijcnn", "logs/experiments/reproduce_ijcnn.log")
    log_path = project_path("experiments/train_model/logs/mlpreal_training.log")

    historical = {
        "model": "MLP + GA + RMSprop",
        "source": str(log_path.relative_to(project_path("."))) if log_path.exists() else "paper_context",
        "test_accuracy": 0.6585,
        "precision": 0.6755,
        "recall": 0.6789,
        "f1": 0.6772,
        "auc_roc": 0.7032,
        "auc_pr": 0.7029,
        "protocol_note": "Historical IJCNN-style balanced random sampling; not the new journal protocol.",
    }

    if log_path.exists():
        text = log_path.read_text(encoding="utf-8", errors="replace")
        matches = re.findall(r"AUC-ROC:\s*([0-9.]+).*?AUC-PR.*?:\s*([0-9.]+)", text, flags=re.S)
        if matches:
            historical["parsed_auc_roc_last"] = float(matches[-1][0])
            historical["parsed_auc_pr_last"] = float(matches[-1][1])

    output_path = project_path("outputs/metrics/ijcnn_historical_baseline.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([historical]).to_csv(output_path, index=False)

    write_text(
        "outputs/reports/ijcnn_historical_baseline.md",
        "\n".join(
            [
                "# IJCNN Historical Baseline",
                "",
                "This file records the historical GA-based MLP baseline from the IJCNN extension.",
                "It is preserved for lineage and reviewer-response context.",
                "",
                "- Model: MLP + GA + RMSprop",
                "- Test accuracy: approximately 65.85%",
                "- AUC-ROC: approximately 0.7032",
                "- AUC-PR: approximately 0.7029",
                "",
                "The new NCA benchmark does not reuse this random-sampling protocol as its main experiment.",
            ]
        ),
    )
    logger.info("IJCNN historical baseline report saved")


if __name__ == "__main__":
    main()
