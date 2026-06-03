"""Particle Swarm Optimization using the shared objective function."""

from __future__ import annotations

from typing import Any

import numpy as np

from src.objective import evaluate_best_on_test, evaluate_candidate, vector_to_candidate
from src.optimizers.ga import _bounds


def run_pso(data: Any, config: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    convergence: list[dict[str, Any]] = []
    best_rows: list[dict[str, Any]] = []
    predictions: list[dict[str, Any]] = []
    pso_config = config["experiment"]["benchmark"]["pso"]
    particles = int(pso_config["particles"])
    iterations = int(pso_config["iterations"])
    inertia = float(pso_config["inertia"])
    cognitive = float(pso_config["cognitive"])
    social = float(pso_config["social"])
    lower, upper = _bounds(config)
    span = upper - lower

    for seed in config["experiment"]["benchmark"]["seeds"]:
        rng = np.random.default_rng(int(seed))
        position = rng.uniform(lower, upper, size=(particles, len(lower)))
        velocity = rng.uniform(-0.1 * span, 0.1 * span, size=(particles, len(lower)))
        personal_best = position.copy()
        personal_best_fitness = np.full(particles, -np.inf)
        global_best = position[0].copy()
        global_best_fitness = -np.inf
        evaluation_id = 0
        seed_fitnesses: list[float] = []

        for _ in range(iterations):
            for idx in range(particles):
                evaluation_id += 1
                candidate = vector_to_candidate(position[idx], config["search_spaces"])
                row = evaluate_candidate(candidate, data, config, int(seed), evaluation_id, "pso")
                rows.append(row)
                seed_fitnesses.append(row["fitness"])
                if row["fitness"] > personal_best_fitness[idx]:
                    personal_best_fitness[idx] = row["fitness"]
                    personal_best[idx] = position[idx].copy()
                if row["fitness"] > global_best_fitness:
                    global_best_fitness = row["fitness"]
                    global_best = position[idx].copy()
                convergence.append(
                    {
                        "optimizer": "pso",
                        "seed": int(seed),
                        "evaluation_id": evaluation_id,
                        "best_fitness_so_far": float(global_best_fitness),
                        "mean_fitness_so_far": float(np.mean(seed_fitnesses)),
                    }
                )

            r1 = rng.random(size=position.shape)
            r2 = rng.random(size=position.shape)
            velocity = (
                inertia * velocity
                + cognitive * r1 * (personal_best - position)
                + social * r2 * (global_best - position)
            )
            position = np.clip(position + velocity, lower, upper)

        best_candidate = vector_to_candidate(global_best, config["search_spaces"])
        best_test, seed_predictions = evaluate_best_on_test(best_candidate, data, config, int(seed), "pso")
        best_test["best_validation_fitness"] = float(global_best_fitness)
        best_rows.append(best_test)
        predictions.extend(seed_predictions)

    return {"runs": rows, "best": best_rows, "convergence": convergence, "predictions": predictions}
