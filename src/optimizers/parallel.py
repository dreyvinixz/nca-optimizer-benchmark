"""Shared joblib parallel settings for optimizers."""

from __future__ import annotations

from typing import Any


def get_parallel_settings(config: dict[str, Any]) -> dict[str, Any]:
    """Read joblib settings from experiment config."""
    benchmark = config["experiment"]["benchmark"]
    return {
        "n_jobs": int(benchmark.get("n_jobs", 1)),
        "backend": benchmark.get("parallel_backend", "loky"),
        "prefer": benchmark.get("parallel_prefer", "processes"),
    }
