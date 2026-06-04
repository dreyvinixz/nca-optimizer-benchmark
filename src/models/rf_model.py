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
    
    model.fit(X_train, y_train)
    proba = model.predict_proba(X_eval)[:, 1]
    pred = model.predict(X_eval)
    
    return pred, proba, model, "scikit-learn"
