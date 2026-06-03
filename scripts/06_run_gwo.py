from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])
sys.path.insert(0, str(ROOT))

from src.utils.io import write_text
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("gwo_placeholder", "logs/experiments/gwo.log")
    message = (
        "Grey Wolf Optimizer is intentionally deferred until the validated "
        "Random Search vs GA vs PSO benchmark is stable."
    )
    write_text("outputs/reports/gwo_placeholder.md", f"# Grey Wolf Optimizer\n\n{message}\n")
    logger.info(message)


if __name__ == "__main__":
    main()
