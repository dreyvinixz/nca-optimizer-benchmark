"""MLP model training with TensorFlow preference and sklearn fallback."""

from __future__ import annotations

from typing import Any

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"

import numpy as np

from src.utils.seeds import set_global_seed

_TENSORFLOW_AVAILABLE: bool | None = None


def _train_with_tensorflow(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidate: dict[str, Any],
    model_config: dict[str, Any],
    seed: int,
) -> tuple[np.ndarray, np.ndarray, Any]:
    import tensorflow as tf  # type: ignore

    for gpu in tf.config.list_physical_devices("GPU"):
        try:
            tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError:
            pass

    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)

    set_global_seed(seed)
    hidden_neurons = int(candidate["hidden_neurons"])
    l2_alpha = float(candidate["l2_alpha"])
    dropout_rate = float(candidate["dropout_rate"])
    learning_rate = float(candidate["learning_rate"])
    batch_size = int(candidate["batch_size"])

    activation = candidate.get("activation", model_config.get("activation", "tanh"))
    optimizer_name = candidate.get("optimizer", model_config.get("optimizer", "rmsprop")).lower()

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(X_train.shape[1],)),
            tf.keras.layers.Dense(
                hidden_neurons,
                activation=activation,
                kernel_regularizer=tf.keras.regularizers.l2(l2_alpha),
            ),
            tf.keras.layers.Dropout(dropout_rate),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )

    if optimizer_name == "adam":
        opt = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    else:
        opt = tf.keras.optimizers.RMSprop(learning_rate=learning_rate)

    model.compile(
        optimizer=opt,
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor=model_config.get("validation_metric", "val_loss"),
            patience=int(model_config.get("early_stopping_patience", 3)),
            restore_best_weights=True,
            verbose=0,
        )
    ]
    history = model.fit(
        X_train,
        y_train,
        epochs=int(model_config.get("max_epochs", 10)),
        batch_size=batch_size,
        validation_split=0.15,
        callbacks=callbacks,
        verbose=0,
        shuffle=False,
    )
    proba = model.predict(X_eval, verbose=0).reshape(-1)
    pred = (proba >= 0.5).astype(int)
    
    # Save history before clearing session
    model._keras_history = history.history
    
    tf.keras.backend.clear_session()
    return pred, proba, model


def _sigmoid(values: np.ndarray) -> np.ndarray:
    values = np.clip(values, -50, 50)
    return 1.0 / (1.0 + np.exp(-values))


def _train_with_numpy_mlp(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidate: dict[str, Any],
    model_config: dict[str, Any],
    seed: int,
) -> tuple[np.ndarray, np.ndarray, Any]:
    """Fast single-hidden-layer MLP fallback.

    Hidden weights are seeded and fixed; output weights are solved with ridge
    regression. This keeps the benchmark executable when TensorFlow is absent.
    """
    set_global_seed(seed)
    rng = np.random.default_rng(seed)
    hidden_neurons = int(candidate["hidden_neurons"])
    input_dim = X_train.shape[1]
    weights = rng.normal(0.0, 1.0 / np.sqrt(input_dim), size=(input_dim, hidden_neurons))
    bias = rng.normal(0.0, 0.1, size=(hidden_neurons,))

    hidden_train = np.tanh(X_train @ weights + bias)
    dropout_rate = float(candidate["dropout_rate"])
    if dropout_rate > 0:
        mask = rng.random(hidden_neurons) >= dropout_rate
        if not np.any(mask):
            mask[rng.integers(0, hidden_neurons)] = True
        hidden_train = hidden_train[:, mask]
        weights = weights[:, mask]
        bias = bias[mask]

    hidden_train = np.column_stack([hidden_train, np.ones(hidden_train.shape[0])])
    alpha = max(float(candidate["l2_alpha"]), 1e-8)
    regularizer = alpha * np.eye(hidden_train.shape[1])
    regularizer[-1, -1] = 0.0
    target = y_train.astype(float)
    output_weights = np.linalg.solve(hidden_train.T @ hidden_train + regularizer, hidden_train.T @ target)

    hidden_eval = np.tanh(X_eval @ weights + bias)
    hidden_eval = np.column_stack([hidden_eval, np.ones(hidden_eval.shape[0])])
    raw = hidden_eval @ output_weights
    temperature = max(float(candidate["learning_rate"]) * 100.0, 1e-4)
    proba = _sigmoid((raw - 0.5) / temperature)
    pred = (proba >= 0.5).astype(int)
    model = {"weights": weights, "bias": bias, "output_weights": output_weights}
    return pred, proba, model


def fit_predict_mlp(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidate: dict[str, Any],
    model_config: dict[str, Any],
    seed: int,
) -> tuple[np.ndarray, np.ndarray, Any, str]:
    """Train the MLP and predict evaluation data."""
    global _TENSORFLOW_AVAILABLE
    backend = model_config.get("backend", "auto")
    if backend in {"auto", "tensorflow"} and _TENSORFLOW_AVAILABLE is not False:
        try:
            pred, proba, model = _train_with_tensorflow(
                X_train, y_train, X_eval, candidate, model_config, seed
            )
            _TENSORFLOW_AVAILABLE = True
            return pred, proba, model, "tensorflow"
        except Exception:
            _TENSORFLOW_AVAILABLE = False
            if backend == "tensorflow":
                raise
            if not model_config.get("allow_numpy_fallback", False):
                raise RuntimeError(
                    "TensorFlow is required for official experiments. "
                    "NumPy fallback is only allowed for software smoke tests. "
                    "Please install TensorFlow or set 'allow_numpy_fallback: true' in experiment_config.yaml."
                )

    pred, proba, model = _train_with_numpy_mlp(
        X_train, y_train, X_eval, candidate, model_config, seed
    )
    return pred, proba, model, "numpy_mlp"
