"""SVM model training."""

from __future__ import annotations

from typing import Any
import numpy as np
from sklearn.svm import SVC

from src.utils.seeds import set_global_seed
import logging

logger = logging.getLogger(__name__)

def fit_predict_svm(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidate: dict[str, Any],
    model_config: dict[str, Any],
    seed: int,
) -> tuple[np.ndarray, np.ndarray, Any, str]:
    """Train the SVM and predict evaluation data."""
    set_global_seed(seed)
    
    C = float(candidate["C"])
    kernel = candidate["kernel"]
    # Linear kernel should ignore gamma
    gamma = float(candidate["gamma"]) if kernel == "rbf" else "scale"
    
    backend = model_config.get("backend", "cpu").lower()
    
    if backend == "cuda":
        try:
            from cuml.svm import SVC
            model = SVC(
                C=C,
                gamma=gamma,
                kernel=kernel,
                probability=True,
                max_iter=50000,
            )
            backend_used = "cuml"
        except ImportError:
            logger.warning("cuML not installed or import failed. Falling back to sklearn SVM on CPU.")
            from sklearn.svm import SVC
            model = SVC(
                C=C,
                gamma=gamma,
                kernel=kernel,
                probability=True,
                random_state=seed,
                max_iter=50000,
            )
            backend_used = "scikit-learn"
    else:
        from sklearn.svm import SVC
        model = SVC(
            C=C,
            gamma=gamma,
            kernel=kernel,
            probability=True,
            random_state=seed,
            max_iter=50000,
        )
        backend_used = "scikit-learn"
    
    model.fit(X_train, y_train)
    proba = model.predict_proba(X_eval)[:, 1]
    pred = model.predict(X_eval)
    
    return pred, proba, model, backend_used
