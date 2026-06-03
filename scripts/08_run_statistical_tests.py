from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])
sys.path.insert(0, str(ROOT))

import itertools

import pandas as pd
from scipy.stats import wilcoxon

from src.utils.io import project_path, write_text
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("statistical_tests", "logs/experiments/statistical_tests.log")
    optimizers = ["random_search", "ga", "pso"]
    frames = []
    for optimizer in optimizers:
        path = project_path(f"outputs/metrics/{optimizer}_best_by_seed.csv")
        if not path.exists():
            raise FileNotFoundError(f"Missing optimizer output: {path}")
        frame = pd.read_csv(path)
        frame["optimizer"] = optimizer
        frames.append(frame[["optimizer", "seed", "mcc_test", "f1_test", "auc_roc_test"]])

    data = pd.concat(frames, ignore_index=True)
    rows = []
    for metric in ["mcc_test", "f1_test", "auc_roc_test"]:
        pivot = data.pivot(index="seed", columns="optimizer", values=metric)
        for left, right in itertools.combinations(optimizers, 2):
            stat, p_value = wilcoxon(pivot[left], pivot[right], zero_method="zsplit")
            rows.append(
                {
                    "metric": metric,
                    "optimizer_a": left,
                    "optimizer_b": right,
                    "wilcoxon_statistic": float(stat),
                    "p_value_uncorrected": float(p_value),
                    "note": "Exploratory first-stage test; final paper should add Holm correction and more seeds.",
                }
            )

    output_path = project_path("outputs/statistical_tests/wilcoxon_first_stage.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(output_path, index=False)
    write_text(
        "outputs/reports/statistical_tests_first_stage.md",
        "# First-Stage Statistical Tests\n\nExploratory Wilcoxon signed-rank tests were generated from current 5-seed outputs. Final journal tests still require more seeds, Friedman testing, Holm correction, and effect sizes.\n",
    )
    logger.info("First-stage statistical test outputs saved")


if __name__ == "__main__":
    main()
