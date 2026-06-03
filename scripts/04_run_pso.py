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
from src.optimizers.pso import run_pso
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("pso", "logs/experiments/pso.log")
    data, config = prepare_benchmark()
    logger.info("Running PSO benchmark")
    results = run_pso(data, config)
    save_optimizer_outputs("pso", results, config)
    logger.info("PSO outputs saved")


if __name__ == "__main__":
    main()
