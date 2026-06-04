#!/usr/bin/env bash
# Launch the official article benchmark detached in WSL.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

source scripts/wsl_cuda_env.sh

mkdir -p logs/experiments outputs/article_official/reports
STAMP="$(date +%Y%m%d_%H%M%S)"
LOG_PATH="logs/experiments/article_official_nohup_${STAMP}.log"
PID_PATH="outputs/article_official/reports/article_official.pid"

PYTHONUNBUFFERED=1 nohup .venv_wsl/bin/python scripts/run_article_official_benchmark.py "$@" > "$LOG_PATH" 2>&1 &
PID="$!"
printf "%s\n" "$PID" > "$PID_PATH"

echo "Started article official benchmark"
echo "PID: $PID"
echo "Log: $LOG_PATH"
echo "PID file: $PID_PATH"
