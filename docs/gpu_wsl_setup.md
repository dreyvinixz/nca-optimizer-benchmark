# GPU WSL2 Setup

This project uses a CUDA C/C++ shared library for fast MLP training and a Python
wrapper for benchmark orchestration.

## Verified Local Status

Verified in the current WSL2 Ubuntu 26.04 environment:

- NVIDIA GPU visible through `nvidia-smi`: GTX 1650 Max-Q, driver 610.47.
- CUDA Toolkit installed through apt: `nvcc` 13.1.
- C/C++ toolchain installed: GCC/G++ 15.2 and GNU Make 4.4.
- Python environment created at `.venv_wsl` with Python 3.12.13 through `uv`.
- Python dependencies installed, including `tensorflow[and-cuda]`.
- `cuda/libmlp_cuda.so` compiled and loaded successfully.
- TensorFlow sees the GPU when `scripts/wsl_cuda_env.sh` is sourced.
- GPU benchmark and CPU comparison completed.

## Environment Helper

Before running TensorFlow GPU checks or CUDA benchmark scripts, source:

```bash
cd /mnt/c/mysystems/projects/nca-optimizer-benchmark
source scripts/wsl_cuda_env.sh
```

This adds `/usr/local/cuda/bin` to `PATH` and builds `LD_LIBRARY_PATH` from:

- `/usr/lib/wsl/lib`
- `.venv_wsl/lib/python3.12/site-packages/nvidia/*/lib`
- `/usr/local/cuda/targets/x86_64-linux/lib`

## Rebuild CUDA Library

```bash
cd /mnt/c/mysystems/projects/nca-optimizer-benchmark
source scripts/wsl_cuda_env.sh
cd cuda
make clean
make
make test
cd ..
```

## Verify TensorFlow GPU

```bash
cd /mnt/c/mysystems/projects/nca-optimizer-benchmark
source scripts/wsl_cuda_env.sh
.venv_wsl/bin/python - <<'PY'
import tensorflow as tf
print(tf.__version__)
print(tf.config.list_physical_devices("GPU"))
PY
```

Expected result includes one GPU device.

## Run Benchmark

```bash
cd /mnt/c/mysystems/projects/nca-optimizer-benchmark
source scripts/wsl_cuda_env.sh
.venv_wsl/bin/python scripts/gpu_benchmark_test.py
.venv_wsl/bin/python scripts/gpu_vs_cpu_comparison.py
```

Outputs are written under `outputs/phase2/gpu_test/`.

## Ubuntu 26.04 Notes

The deadsnakes PPA currently lists Ubuntu 22.04 and 24.04 as supported series,
not Ubuntu 26.04:

https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa

For that reason, this environment uses `uv python install 3.12` instead of the
deadsnakes PPA.

TensorFlow's Linux/WSL GPU installation guide recommends installing the CUDA
extra:

```bash
python -m pip install "tensorflow[and-cuda]"
```

Reference:

https://www.tensorflow.org/install/gpu

CUDA Toolkit 13.1 on Ubuntu 26.04 needed a small local header compatibility
workaround because glibc declares `rsqrt` and `rsqrtf` with an exception
specifier. A backup was saved at:

```text
/usr/local/cuda/targets/x86_64-linux/include/crt/math_functions.h.nca-bak
```
