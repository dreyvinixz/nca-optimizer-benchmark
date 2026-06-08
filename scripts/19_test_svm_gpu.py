"""Test script to validate and benchmark SVM on CPU vs GPU (cuML)."""

import time
import logging
import sys
import numpy as np
from copy import deepcopy

from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.benchmark import prepare_benchmark
from src.models.svm_model import fit_predict_svm

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def main():
    logging.info("Loading data via prepare_benchmark...")
    data, _ = prepare_benchmark()
    
    X_train = data.X_train_scaled if data.X_train_scaled is not None else data.X_train
    y_train = data.y_train
    X_val = data.X_val_scaled if data.X_val_scaled is not None else data.X_val
    y_val = data.y_val

    candidate = {
        "C": 1.0,
        "gamma": 0.1,
        "kernel": "rbf"
    }

    logging.info(f"Train shape: {X_train.shape}, Val shape: {X_val.shape}")

    # Test CPU (scikit-learn)
    logging.info("Running SVM on CPU (scikit-learn)...")
    config_cpu = {"backend": "cpu"}
    t0 = time.time()
    pred_cpu, proba_cpu, _, backend_cpu = fit_predict_svm(X_train, y_train, X_val, candidate, config_cpu, 42)
    t1 = time.time()
    time_cpu = t1 - t0
    logging.info(f"CPU Time: {time_cpu:.2f}s | Backend used: {backend_cpu}")

    # Test GPU (cuML)
    logging.info("Running SVM on GPU (cuML)...")
    config_gpu = {"backend": "cuda"}
    t0 = time.time()
    pred_gpu, proba_gpu, _, backend_gpu = fit_predict_svm(X_train, y_train, X_val, candidate, config_gpu, 42)
    t1 = time.time()
    time_gpu = t1 - t0
    logging.info(f"GPU Time: {time_gpu:.2f}s | Backend used: {backend_gpu}")

    speedup = time_cpu / time_gpu if time_gpu > 0 else 0
    logging.info(f"Speedup: {speedup:.1f}x")

    diff = np.mean(np.abs(proba_cpu - proba_gpu))
    logging.info(f"Mean Absolute Difference between predictions: {diff:.6f}")

if __name__ == "__main__":
    main()
