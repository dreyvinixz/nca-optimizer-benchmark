"""Print progress for the article official benchmark."""

from __future__ import annotations

import json
import argparse
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODELS = ["mlp", "rf", "svm", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", default="outputs/article_official")
    return parser


def _count_rows(path: Path) -> int:
    if not path.exists():
        return 0
    try:
        return len(pd.read_csv(path))
    except Exception:
        return -1


def main() -> None:
    args = _build_parser().parse_args()
    output_root = ROOT / args.output_root
    status_path = output_root / "reports" / "article_official_status.json"

    if status_path.exists():
        status = json.loads(status_path.read_text(encoding="utf-8"))
        print(f"Started: {status.get('started_at')}")
        print(f"Updated: {status.get('updated_at', '-')}")
        print(f"Fitness mode: {status.get('fitness_mode', '-')}")
        print(f"Output root: {status.get('output_root', output_root)}")
        print(f"Current: {status.get('current')}")
        print(f"Completed: {len(status.get('completed', []))}")
        print(f"Failed: {len(status.get('failed', []))}")
        print(f"Log: {status.get('log_path')}")
        expected = int(status.get("expected_rows_per_combination", 5000))
        expected_best = len(status.get("seeds", [])) or 3
    else:
        print(f"Status file not found: {status_path}")
        expected = 5000
        expected_best = 3

    print()
    print("Progress by model/optimizer")
    print("model,optimizer,runs,best,convergence")
    for model in MODELS:
        for optimizer in OPTIMIZERS:
            stem = f"{model}_{optimizer}"
            runs = _count_rows(output_root / "metrics" / f"{stem}_runs.csv")
            best = _count_rows(output_root / "metrics" / f"{stem}_best_by_seed.csv")
            conv = _count_rows(output_root / "metrics" / "convergence" / f"{stem}_convergence.csv")
            marker = "DONE" if runs >= expected and best >= expected_best and conv >= expected else "..."
            print(f"{model},{optimizer},{runs},{best},{conv},{marker}")


if __name__ == "__main__":
    main()
