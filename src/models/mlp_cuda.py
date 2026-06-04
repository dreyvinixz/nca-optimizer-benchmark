"""CUDA-accelerated MLP training via ctypes.

Wraps libmlp_cuda.so built from cuda/mlp_cuda.cu.
Provides the same interface as fit_predict_mlp() so it can be used
as a drop-in backend replacement.

Usage:
    from src.models.mlp_cuda import fit_predict_mlp_cuda
    pred, proba, info, backend = fit_predict_mlp_cuda(
        X_train, y_train, X_eval, candidate, model_config, seed
    )
"""

from __future__ import annotations

import ctypes
import os
from pathlib import Path
from typing import Any

import numpy as np

# ---- Locate shared library ------------------------------------------------

_ROOT = Path(__file__).resolve().parents[2]
_LIB_SEARCH_PATHS = [
    Path(os.environ["NCA_MLP_CUDA_LIB"]) if os.environ.get("NCA_MLP_CUDA_LIB") else None,
    _ROOT / "cuda" / "libmlp_cuda.so",
    Path.cwd() / "cuda" / "libmlp_cuda.so",
]
if os.name != "nt":
    _LIB_SEARCH_PATHS.append(
        Path("/mnt/c/mysystems/projects/nca-optimizer-benchmark/cuda/libmlp_cuda.so")
    )

_lib: ctypes.CDLL | None = None


def _load_lib() -> ctypes.CDLL:
    global _lib
    if _lib is not None:
        return _lib

    checked_paths = []
    seen = set()
    for p in _LIB_SEARCH_PATHS:
        if p is None:
            continue
        path_text = str(p)
        if path_text in seen:
            continue
        seen.add(path_text)
        checked_paths.append(path_text)
        if p.exists():
            _lib = ctypes.CDLL(str(p.resolve()))
            _setup_signatures(_lib)
            return _lib

    raise FileNotFoundError(
        "libmlp_cuda.so not found. Compile with `cd cuda && make` or set "
        f"NCA_MLP_CUDA_LIB. Checked: {checked_paths}"
    )


def _setup_signatures(lib: ctypes.CDLL) -> None:
    """Declare C function signatures for type safety."""
    FP = ctypes.POINTER(ctypes.c_float)
    IP = ctypes.POINTER(ctypes.c_int)
    UP = ctypes.POINTER(ctypes.c_uint)

    lib.mlp_train_predict.restype = ctypes.c_int
    lib.mlp_train_predict.argtypes = [
        FP, FP, ctypes.c_int,          # X_train, y_train, n_train
        FP, ctypes.c_int,              # X_eval, n_eval
        ctypes.c_int,                  # input_dim
        ctypes.c_int,                  # hidden_neurons
        ctypes.c_float,                # learning_rate
        ctypes.c_float,                # l2_alpha
        ctypes.c_float,                # dropout_rate
        ctypes.c_int,                  # batch_size
        ctypes.c_int,                  # max_epochs
        ctypes.c_int,                  # patience
        ctypes.c_int,                  # use_tanh
        ctypes.c_int,                  # use_adam
        ctypes.c_uint,                 # seed
        FP, FP,                        # y_pred_out, y_proba_out
        FP, FP,                        # train_time_out, val_loss_out
    ]

    lib.mlp_train_predict_batch.restype = ctypes.c_int
    lib.mlp_train_predict_batch.argtypes = [
        FP, FP, ctypes.c_int,          # X_train, y_train, n_train
        FP, ctypes.c_int,              # X_eval, n_eval
        ctypes.c_int,                  # input_dim
        ctypes.c_int,                  # n_candidates
        IP, FP, FP, FP, IP, IP, IP, UP,  # per-candidate params
        ctypes.c_int, ctypes.c_int,    # max_epochs, patience
        FP, FP, FP, FP,               # outputs
    ]


# ---- Helpers ---------------------------------------------------------------

def _as_float_ptr(arr: np.ndarray) -> ctypes.POINTER(ctypes.c_float):
    return arr.ctypes.data_as(ctypes.POINTER(ctypes.c_float))


def _as_int_ptr(arr: np.ndarray) -> ctypes.POINTER(ctypes.c_int):
    return arr.ctypes.data_as(ctypes.POINTER(ctypes.c_int))


def _as_uint_ptr(arr: np.ndarray) -> ctypes.POINTER(ctypes.c_uint):
    return arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint))


# ---- Public API: single model ---------------------------------------------

def fit_predict_mlp_cuda(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidate: dict[str, Any],
    model_config: dict[str, Any],
    seed: int,
) -> tuple[np.ndarray, np.ndarray, dict[str, Any], str]:
    """Train MLP on GPU and predict, matching fit_predict_mlp interface."""
    lib = _load_lib()

    # Ensure contiguous float32
    X_train = np.ascontiguousarray(X_train, dtype=np.float32)
    y_train = np.ascontiguousarray(y_train, dtype=np.float32)
    X_eval = np.ascontiguousarray(X_eval, dtype=np.float32)

    n_train, input_dim = X_train.shape
    n_eval = X_eval.shape[0]

    # Extract hyper-parameters
    hidden_neurons = int(candidate["hidden_neurons"])
    learning_rate = float(candidate["learning_rate"])
    l2_alpha = float(candidate["l2_alpha"])
    dropout_rate = float(candidate["dropout_rate"])
    batch_size = int(candidate["batch_size"])

    activation = candidate.get("activation", model_config.get("activation", "tanh"))
    optimizer = candidate.get("optimizer", model_config.get("optimizer", "rmsprop")).lower()

    use_tanh = 1 if activation == "tanh" else 0
    use_adam = 1 if optimizer == "adam" else 0

    max_epochs = int(model_config.get("max_epochs", 10))
    patience = int(model_config.get("early_stopping_patience", 3))

    # Output buffers
    y_pred = np.zeros(n_eval, dtype=np.float32)
    y_proba = np.zeros(n_eval, dtype=np.float32)
    train_time = np.zeros(1, dtype=np.float32)
    val_loss = np.zeros(1, dtype=np.float32)

    rc = lib.mlp_train_predict(
        _as_float_ptr(X_train), _as_float_ptr(y_train), n_train,
        _as_float_ptr(X_eval), n_eval,
        input_dim, hidden_neurons,
        learning_rate, l2_alpha, dropout_rate,
        batch_size, max_epochs, patience,
        use_tanh, use_adam, seed,
        _as_float_ptr(y_pred), _as_float_ptr(y_proba),
        _as_float_ptr(train_time), _as_float_ptr(val_loss),
    )

    if rc != 0:
        raise RuntimeError("CUDA MLP training failed (see stderr for details)")

    info = {
        "train_time_cuda": float(train_time[0]),
        "val_loss": float(val_loss[0]),
        "_keras_history": None,
    }

    return y_pred.astype(int), y_proba, info, "cuda"


# ---- Public API: batch (population) training --------------------------------

def fit_predict_mlp_cuda_batch(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidates: list[dict[str, Any]],
    model_config: dict[str, Any],
    seeds: list[int],
) -> list[tuple[np.ndarray, np.ndarray, dict[str, Any], str]]:
    """Train N MLPs concurrently on GPU. Returns list of results."""
    lib = _load_lib()

    if len(candidates) == 0:
        return []
    if len(seeds) != len(candidates):
        raise ValueError("seeds must have the same length as candidates")

    X_train = np.ascontiguousarray(X_train, dtype=np.float32)
    y_train = np.ascontiguousarray(y_train, dtype=np.float32)
    X_eval = np.ascontiguousarray(X_eval, dtype=np.float32)

    n_train, input_dim = X_train.shape
    n_eval = X_eval.shape[0]
    n_cand = len(candidates)

    max_epochs = int(model_config.get("max_epochs", 10))
    patience = int(model_config.get("early_stopping_patience", 3))

    # Build per-candidate parameter arrays
    h_neurons = np.array([int(c["hidden_neurons"]) for c in candidates], dtype=np.int32)
    lrs = np.array([float(c["learning_rate"]) for c in candidates], dtype=np.float32)
    l2s = np.array([float(c["l2_alpha"]) for c in candidates], dtype=np.float32)
    drops = np.array([float(c["dropout_rate"]) for c in candidates], dtype=np.float32)
    bsizes = np.array([int(c["batch_size"]) for c in candidates], dtype=np.int32)
    tanhs = np.array([
        1 if c.get("activation", model_config.get("activation", "tanh")) == "tanh" else 0
        for c in candidates
    ], dtype=np.int32)
    adams = np.array([
        1 if c.get("optimizer", model_config.get("optimizer", "rmsprop")).lower() == "adam" else 0
        for c in candidates
    ], dtype=np.int32)
    seed_arr = np.array(seeds, dtype=np.uint32)

    # Output buffers
    y_pred_all = np.zeros(n_cand * n_eval, dtype=np.float32)
    y_proba_all = np.zeros(n_cand * n_eval, dtype=np.float32)
    times_all = np.zeros(n_cand, dtype=np.float32)
    losses_all = np.zeros(n_cand, dtype=np.float32)

    rc = lib.mlp_train_predict_batch(
        _as_float_ptr(X_train), _as_float_ptr(y_train), n_train,
        _as_float_ptr(X_eval), n_eval,
        input_dim, n_cand,
        _as_int_ptr(h_neurons), _as_float_ptr(lrs),
        _as_float_ptr(l2s), _as_float_ptr(drops),
        _as_int_ptr(bsizes), _as_int_ptr(tanhs), _as_int_ptr(adams),
        _as_uint_ptr(seed_arr),
        max_epochs, patience,
        _as_float_ptr(y_pred_all), _as_float_ptr(y_proba_all),
        _as_float_ptr(times_all), _as_float_ptr(losses_all),
    )

    if rc != 0:
        raise RuntimeError("CUDA batch MLP training failed")

    results = []
    for c in range(n_cand):
        pred = y_pred_all[c * n_eval : (c + 1) * n_eval].astype(int)
        proba = y_proba_all[c * n_eval : (c + 1) * n_eval]
        info = {
            "train_time_cuda": float(times_all[c]),
            "val_loss": float(losses_all[c]),
            "_keras_history": None,
        }
        results.append((pred, proba, info, "cuda"))

    return results


# Drop-in name for callers that import this module as a backend replacement.
fit_predict_mlp = fit_predict_mlp_cuda
