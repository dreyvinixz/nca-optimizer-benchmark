from __future__ import annotations

import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])
sys.path.insert(0, str(ROOT))

from src.benchmark import prepare_benchmark, save_optimizer_outputs
from src.optimizers.ga import run_ga
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("ga", "logs/experiments/ga.log")
    data, config = prepare_benchmark()
    logger.info("Running GA benchmark")
    results = run_ga(data, config)
    save_optimizer_outputs("ga", results, config)
    logger.info("GA outputs saved")


if __name__ == "__main__":
    main()
