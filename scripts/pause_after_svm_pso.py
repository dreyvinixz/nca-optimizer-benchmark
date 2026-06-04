"""Stop the overnight official runner after SVM/PSO completes.

This is intentionally separate from the long-running benchmark process because
the current run was already launched. It watches the official SVM/PSO output
files and terminates the article runner as soon as that combination is complete.
"""

from __future__ import annotations

import json
import os
import signal
import subprocess
import time
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "outputs" / "article_official"
REPORTS = OUTPUT_ROOT / "reports"
RUNS = OUTPUT_ROOT / "metrics" / "svm_pso_runs.csv"
BEST = OUTPUT_ROOT / "metrics" / "svm_pso_best_by_seed.csv"
STATUS = REPORTS / "article_official_status.json"
PAUSED = REPORTS / "paused_after_svm_pso.txt"
EXPECTED_RUNS = 5000
EXPECTED_BEST = 5


def _csv_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        lines = sum(1 for _ in handle)
    return max(0, lines - 1)


def _runner_pids() -> list[int]:
    result = subprocess.run(
        ["pgrep", "-f", r"\.venv_wsl/bin/python scripts/run_article_official_benchmark\.py"],
        text=True,
        capture_output=True,
        check=False,
    )
    pids = []
    for line in result.stdout.splitlines():
        try:
            pid = int(line.strip())
        except ValueError:
            continue
        if pid != os.getpid():
            pids.append(pid)
    return pids


def _status_current() -> object:
    if not STATUS.exists():
        return None
    try:
        return json.loads(STATUS.read_text(encoding="utf-8")).get("current")
    except Exception:
        return None


def main() -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    while True:
        runs = _csv_rows(RUNS)
        best = _csv_rows(BEST)
        current = _status_current()
        if runs >= EXPECTED_RUNS and best >= EXPECTED_BEST:
            pids = _runner_pids()
            for pid in pids:
                os.kill(pid, signal.SIGTERM)
            PAUSED.write_text(
                "\n".join(
                    [
                        f"paused_at={datetime.now().isoformat(timespec='seconds')}",
                        "reason=SVM/PSO completed; user will run SVM/DE and SVM/GWO elsewhere; CNN later.",
                        f"svm_pso_runs={runs}",
                        f"svm_pso_best={best}",
                        f"terminated_pids={pids}",
                        f"status_current={current}",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            return
        time.sleep(10)


if __name__ == "__main__":
    main()
