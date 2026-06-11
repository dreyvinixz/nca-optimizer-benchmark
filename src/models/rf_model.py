"""Random Forest model training."""

from __future__ import annotations

from typing import Any
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from src.utils.seeds import set_global_seed

def fit_predict_rf(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidate: dict[str, Any],
    model_config: dict[str, Any],
    seed: int,
) -> tuple[np.ndarray, np.ndarray, Any, str]:
    """Train the Random Forest and predict evaluation data."""
    set_global_seed(seed)
    
    n_estimators = int(candidate["n_estimators"])
    max_depth = int(candidate["max_depth"])
    min_samples_split = int(candidate["min_samples_split"])
    min_samples_leaf = int(candidate["min_samples_leaf"])
    max_features = candidate.get("max_features", "sqrt")
    class_weight = candidate.get("class_weight", None)
    
    backend = model_config.get("backend", "cpu").lower()
    
    if backend == "cuda":
        try:
            from cuml.ensemble import RandomForestClassifier
            
            # cuML RF accepts float for all features, None breaks it in some versions
            mf = 1.0 if max_features is None else max_features
            
            model = RandomForestClassifier(
                n_estimators=n_estimators,
                max_depth=max_depth,
                min_samples_split=min_samples_split,
                min_samples_leaf=min_samples_leaf,
                max_features=mf,
                n_streams=8,
                random_state=seed,
            )
            backend_used = "cuml"
        except ImportError:
            import logging
            logging.getLogger(__name__).warning("cuML not installed. Falling back to sklearn RF on CPU.")
            from sklearn.ensemble import RandomForestClassifier
            model = RandomForestClassifier(
                n_estimators=n_estimators,
                max_depth=max_depth,
                min_samples_split=min_samples_split,
                min_samples_leaf=min_samples_leaf,
                max_features=max_features,
                class_weight=class_weight,
                random_state=seed,
                n_jobs=1,
            )
            backend_used = "scikit-learn"
    else:
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_features=max_features,
            class_weight=class_weight,
            random_state=seed,
            n_jobs=1,
        )
        backend_used = "scikit-learn"
    
    model.fit(X_train, y_train)
    proba = model.predict_proba(X_eval)[:, 1]
    pred = model.predict(X_eval)
    
    return pred, proba, model, backend_used
