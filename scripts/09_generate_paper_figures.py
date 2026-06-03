from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])
sys.path.insert(0, str(ROOT))

from src.utils.io import project_path, write_text
from src.utils.logger import get_logger


def main() -> None:
    logger = get_logger("paper_figures", "logs/experiments/paper_figures.log")
    source_dir = project_path("outputs/figures")
    target_dir = project_path("article/figures")
    target_dir.mkdir(parents=True, exist_ok=True)

    copied = []
    for source in source_dir.glob("*.png"):
        target = target_dir / source.name
        shutil.copy2(source, target)
        copied.append(target.name)

    write_text(
        "article/figures/README.md",
        "# Article Figures\n\nGenerated paper-preview figures copied from `outputs/figures`:\n\n"
        + "\n".join(f"- {name}" for name in copied)
        + "\n",
    )
    logger.info("Copied %s figure(s) to article/figures", len(copied))


if __name__ == "__main__":
    main()
