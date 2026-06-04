"""CNN-1D model training with TensorFlow for financial time-series classification."""

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


def fit_predict_cnn(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_eval: np.ndarray,
    candidate: dict[str, Any],
    model_config: dict[str, Any],
    seed: int,
) -> tuple[np.ndarray, np.ndarray, Any, str]:
    """Train a 1D-CNN and predict evaluation data.

    The input features are reshaped to (samples, features, 1) so that
    Conv1D filters slide across the feature dimension, learning local
    cross-indicator patterns automatically.
    """
    import tensorflow as tf  # type: ignore

    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)

    set_global_seed(seed)

    # Decode hyperparameters
    n_filters = int(candidate["n_filters"])
    kernel_size = int(candidate["kernel_size"])
    dense_neurons = int(candidate["dense_neurons"])
    l2_alpha = float(candidate["l2_alpha"])
    dropout_rate = float(candidate["dropout_rate"])
    learning_rate = float(candidate["learning_rate"])
    batch_size = int(candidate["batch_size"])
    activation = candidate.get("activation", model_config.get("activation", "relu"))
    optimizer_name = candidate.get("optimizer", model_config.get("optimizer", "adam")).lower()

    n_features = X_train.shape[1]

    # Clamp kernel_size to avoid exceeding feature dimension
    kernel_size = min(kernel_size, n_features)

    # Reshape to (samples, features, 1) for Conv1D
    X_train_3d = X_train.reshape(-1, n_features, 1)
    X_eval_3d = X_eval.reshape(-1, n_features, 1)

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(n_features, 1)),
        tf.keras.layers.Conv1D(
            filters=n_filters,
            kernel_size=kernel_size,
            activation=activation,
            kernel_regularizer=tf.keras.regularizers.l2(l2_alpha),
            padding="same",
        ),
        tf.keras.layers.GlobalMaxPooling1D(),
        tf.keras.layers.Dense(
            dense_neurons,
            activation=activation,
            kernel_regularizer=tf.keras.regularizers.l2(l2_alpha),
        ),
        tf.keras.layers.Dropout(dropout_rate),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ])

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
        X_train_3d,
        y_train,
        epochs=int(model_config.get("max_epochs", 10)),
        batch_size=batch_size,
        validation_split=0.15,
        callbacks=callbacks,
        verbose=0,
        shuffle=False,
    )

    proba = model.predict(X_eval_3d, verbose=0).reshape(-1)
    pred = (proba >= 0.5).astype(int)

    # Save history before clearing session
    model._keras_history = history.history

    tf.keras.backend.clear_session()
    return pred, proba, model, "tensorflow"
