"""Print progress for the article official benchmark."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "outputs" / "article_official"
STATUS_PATH = OUTPUT_ROOT / "reports" / "article_official_status.json"
MODELS = ["mlp", "rf", "svm", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]


def _count_rows(path: Path) -> int:
    if not path.exists():
        return 0
    try:
        return len(pd.read_csv(path))
    except Exception:
        return -1


def main() -> None:
    if STATUS_PATH.exists():
        status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
        print(f"Started: {status.get('started_at')}")
        print(f"Updated: {status.get('updated_at', '-')}")
        print(f"Current: {status.get('current')}")
        print(f"Completed: {len(status.get('completed', []))}")
        print(f"Failed: {len(status.get('failed', []))}")
        print(f"Log: {status.get('log_path')}")
        expected = int(status.get("expected_rows_per_combination", 5000))
    else:
        print(f"Status file not found: {STATUS_PATH}")
        expected = 5000

    print()
    print("Progress by model/optimizer")
    print("model,optimizer,runs,best,convergence")
    for model in MODELS:
        for optimizer in OPTIMIZERS:
            stem = f"{model}_{optimizer}"
            runs = _count_rows(OUTPUT_ROOT / "metrics" / f"{stem}_runs.csv")
            best = _count_rows(OUTPUT_ROOT / "metrics" / f"{stem}_best_by_seed.csv")
            conv = _count_rows(OUTPUT_ROOT / "metrics" / "convergence" / f"{stem}_convergence.csv")
            marker = "DONE" if runs >= expected and best >= 5 and conv >= expected else "..."
            print(f"{model},{optimizer},{runs},{best},{conv},{marker}")


if __name__ == "__main__":
    main()
