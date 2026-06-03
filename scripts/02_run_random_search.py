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
from src.optimizers.random_search import run_random_search
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("random_search", "logs/experiments/random_search.log")
    data, config = prepare_benchmark()
    logger.info("Running Random Search benchmark")
    results = run_random_search(data, config)
    save_optimizer_outputs("random_search", results, config)
    logger.info("Random Search outputs saved")


if __name__ == "__main__":
    main()
