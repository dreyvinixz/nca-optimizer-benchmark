"""Simple real-coded Genetic Algorithm using the shared objective function."""

from __future__ import annotations

from typing import Any

import numpy as np

from src.objective import evaluate_best_on_test, evaluate_candidate, vector_to_candidate


def _bounds(config: dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    mlp = config["search_spaces"]["mlp"]
    lower = np.array([
        mlp["hidden_neurons"]["min"],
        np.log10(float(mlp["learning_rate"]["min"])),
        np.log10(float(mlp["l2_alpha"]["min"])),
        mlp["dropout_rate"]["min"],
        0,
    ], dtype=float)
    upper = np.array([
        mlp["hidden_neurons"]["max"],
        np.log10(float(mlp["learning_rate"]["max"])),
        np.log10(float(mlp["l2_alpha"]["max"])),
        mlp["dropout_rate"]["max"],
        len(mlp["batch_size"]["values"]) - 1,
    ], dtype=float)
    return lower, upper


def _tournament(rng: np.random.Generator, population: np.ndarray, fitness: np.ndarray, size: int) -> np.ndarray:
    indices = rng.choice(len(population), size=size, replace=False)
    return population[indices[np.argmax(fitness[indices])]].copy()


def run_ga(data: Any, config: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    convergence: list[dict[str, Any]] = []
    best_rows: list[dict[str, Any]] = []
    predictions: list[dict[str, Any]] = []
    ga_config = config["experiment"]["benchmark"]["ga"]
    pop_size = int(ga_config["population_size"])
    generations = int(ga_config["generations"])
    lower, upper = _bounds(config)

    for seed in config["experiment"]["benchmark"]["seeds"]:
        rng = np.random.default_rng(int(seed))
        population = rng.uniform(lower, upper, size=(pop_size, len(lower)))
        fitness = np.full(pop_size, -np.inf)
        best_fitness = -np.inf
        best_vector: np.ndarray | None = None
        evaluation_id = 0
        seed_fitnesses: list[float] = []

        for _ in range(generations):
            for idx in range(pop_size):
                evaluation_id += 1
                candidate = vector_to_candidate(population[idx], config["search_spaces"])
                row = evaluate_candidate(candidate, data, config, int(seed), evaluation_id, "ga")
                fitness[idx] = row["fitness"]
                seed_fitnesses.append(row["fitness"])
                rows.append(row)
                if row["fitness"] > best_fitness:
                    best_fitness = row["fitness"]
                    best_vector = population[idx].copy()
                convergence.append(
                    {
                        "optimizer": "ga",
                        "seed": int(seed),
                        "evaluation_id": evaluation_id,
                        "best_fitness_so_far": float(best_fitness),
                        "mean_fitness_so_far": float(np.mean(seed_fitnesses)),
                    }
                )

            elite = population[int(np.argmax(fitness))].copy()
            next_population = [elite]
            while len(next_population) < pop_size:
                p1 = _tournament(rng, population, fitness, int(ga_config["tournament_size"]))
                p2 = _tournament(rng, population, fitness, int(ga_config["tournament_size"]))
                child = p1.copy()
                if rng.random() < float(ga_config["crossover_probability"]):
                    mask = rng.random(len(lower)) < 0.5
                    child[mask] = p2[mask]
                if rng.random() < float(ga_config["mutation_probability"]):
                    scale = (upper - lower) * float(ga_config["mutation_scale"])
                    child += rng.normal(0.0, scale)
                next_population.append(np.clip(child, lower, upper))
            population = np.vstack(next_population)

        assert best_vector is not None
        best_candidate = vector_to_candidate(best_vector, config["search_spaces"])
        best_test, seed_predictions = evaluate_best_on_test(best_candidate, data, config, int(seed), "ga")
        best_test["best_validation_fitness"] = float(best_fitness)
        best_rows.append(best_test)
        predictions.extend(seed_predictions)

    return {"runs": rows, "best": best_rows, "convergence": convergence, "predictions": predictions}
