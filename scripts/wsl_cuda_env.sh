#!/usr/bin/env bash
# Source this before WSL GPU runs:
#   source scripts/wsl_cuda_env.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_SITE="$ROOT/.venv_wsl/lib/python3.12/site-packages"

NVIDIA_LIBS=""
if [ -d "$VENV_SITE/nvidia" ]; then
    NVIDIA_LIBS="$(find "$VENV_SITE/nvidia" -maxdepth 3 -type d -name lib | paste -sd: -)"
fi

export PATH="/usr/local/cuda/bin:$PATH"
export LD_LIBRARY_PATH="/usr/lib/wsl/lib${NVIDIA_LIBS:+:$NVIDIA_LIBS}:/usr/local/cuda/targets/x86_64-linux/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export TF_CPP_MIN_LOG_LEVEL="${TF_CPP_MIN_LOG_LEVEL:-2}"
