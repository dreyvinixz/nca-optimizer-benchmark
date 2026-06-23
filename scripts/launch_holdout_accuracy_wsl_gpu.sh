#!/usr/bin/env bash
# Launch Exp. 2 (Holdout + Accuracy) in WSL/GPU without running pre-tests.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

source scripts/wsl_cuda_env.sh

mkdir -p logs/experiments outputs/article_official_accuracy_holdout/reports

STAMP="$(date +%Y%m%d_%H%M%S)"
LOG_PATH="logs/experiments/holdout_accuracy_wsl_gpu_${STAMP}.log"
PID_PATH="outputs/article_official_accuracy_holdout/reports/holdout_accuracy_wsl_gpu.pid"

PYTHONUNBUFFERED=1 nohup .venv_wsl/bin/python scripts/run_article_official_benchmark.py \
  --fitness-mode accuracy_holdout \
  --seeds 1 2 3 \
  --evaluations-per-seed 1000 \
  > "$LOG_PATH" 2>&1 &

PID="$!"
printf "%s\n" "$PID" > "$PID_PATH"

echo "Started WSL/GPU Holdout + Accuracy"
echo "PID: $PID"
echo "Log: $LOG_PATH"
echo "PID file: $PID_PATH"
