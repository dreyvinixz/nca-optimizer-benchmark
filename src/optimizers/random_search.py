"""Random Search optimizer baseline."""

from __future__ import annotations

import math
from typing import Any

import numpy as np

from src.objective import evaluate_best_on_test, evaluate_candidate


def sample_candidate(rng: np.random.Generator, search_space: dict[str, Any]) -> dict[str, Any]:
    mlp = search_space["mlp"]
    lr = 10 ** rng.uniform(math.log10(float(mlp["learning_rate"]["min"])), math.log10(float(mlp["learning_rate"]["max"])))
    l2 = 10 ** rng.uniform(math.log10(float(mlp["l2_alpha"]["min"])), math.log10(float(mlp["l2_alpha"]["max"])))
    return {
        "hidden_neurons": int(rng.integers(int(mlp["hidden_neurons"]["min"]), int(mlp["hidden_neurons"]["max"]) + 1)),
        "learning_rate": float(lr),
        "l2_alpha": float(l2),
        "dropout_rate": float(rng.uniform(float(mlp["dropout_rate"]["min"]), float(mlp["dropout_rate"]["max"]))),
        "batch_size": int(rng.choice(mlp["batch_size"]["values"])),
    }


def run_random_search(data: Any, config: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    convergence: list[dict[str, Any]] = []
    best_rows: list[dict[str, Any]] = []
    predictions: list[dict[str, Any]] = []
    evaluations = int(config["experiment"]["benchmark"]["evaluations_per_seed"])

    for seed in config["experiment"]["benchmark"]["seeds"]:
        rng = np.random.default_rng(int(seed))
        seed_rows: list[dict[str, Any]] = []
        best_fitness = -np.inf
        best_candidate: dict[str, Any] | None = None
        for evaluation_id in range(1, evaluations + 1):
            candidate = sample_candidate(rng, config["search_spaces"])
            row = evaluate_candidate(candidate, data, config, int(seed), evaluation_id, "random_search")
            seed_rows.append(row)
            rows.append(row)
            if row["fitness"] > best_fitness:
                best_fitness = row["fitness"]
                best_candidate = candidate
            convergence.append(
                {
                    "optimizer": "random_search",
                    "seed": int(seed),
                    "evaluation_id": evaluation_id,
                    "best_fitness_so_far": float(best_fitness),
                    "mean_fitness_so_far": float(np.mean([r["fitness"] for r in seed_rows])),
                }
            )
        assert best_candidate is not None
        best_test, seed_predictions = evaluate_best_on_test(best_candidate, data, config, int(seed), "random_search")
        best_validation = max(seed_rows, key=lambda item: item["fitness"])
        best_test["best_validation_fitness"] = best_validation["fitness"]
        best_rows.append(best_test)
        predictions.extend(seed_predictions)

    return {"runs": rows, "best": best_rows, "convergence": convergence, "predictions": predictions}
