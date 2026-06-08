"""Simple real-coded Genetic Algorithm using the shared objective function."""

from __future__ import annotations

from typing import Any
import logging

logger = logging.getLogger("ga")

import numpy as np
from joblib import Parallel, delayed  # type: ignore

from src.benchmark import append_optimizer_outputs, clear_optimizer_outputs
from src.objective import evaluate_best_on_test, evaluate_candidate, vector_to_candidate, get_bounds
from src.optimizers.parallel import get_parallel_settings

def _tournament(rng: np.random.Generator, population: np.ndarray, fitness: np.ndarray, size: int) -> np.ndarray:
    indices = rng.choice(len(population), size=size, replace=False)
    return population[indices[np.argmax(fitness[indices])]].copy()


def run_ga(data: Any, config: dict[str, Any], model_type: str) -> None:
    """Run Genetic Algorithm sequentially over all seeds."""
    logger.info(f"Starting Genetic Algorithm for model: {model_type}...")
    
    mode = config["experiment"]["benchmark"].get("experiment_mode", "quick_test")
    mode_config = config["experiment"]["benchmark"][mode]
    ga_config = config["experiment"]["benchmark"]["ga"]
    
    pop_size = int(ga_config["population_size"])
    generations = int(mode_config.get("generations", 10))
    seeds = mode_config.get("seeds", [1])
    
    lower, upper, var_types = get_bounds(config["search_spaces"], model_type)

    for seed in seeds:
        rows: list[dict[str, Any]] = []
        convergence: list[dict[str, Any]] = []
        rng = np.random.default_rng(int(seed))
        
        # Initialize population based on bounds and types
        population = []
        for _ in range(pop_size):
            ind = []
            for j in range(len(lower)):
                if var_types[j] == "categorical" or var_types[j] == "int":
                    ind.append(rng.integers(int(lower[j]), int(upper[j]) + 1))
                else:
                    ind.append(rng.uniform(lower[j], upper[j]))
            population.append(ind)
        population = np.array(population, dtype=float)
        
        fitness = np.full(pop_size, -np.inf)
        best_fitness = -np.inf
        best_vector: np.ndarray | None = None
        evaluation_id = 0
        seed_fitnesses: list[float] = []
        cache: dict[str, dict[str, Any]] = {}
        hits = 0

        def get_cache_key(cand: dict[str, Any]) -> str:
            cand_str = "-".join([f"{k}:{v}" for k, v in cand.items()])
            backend = config["experiment"]["model"]["backend"]
            feature_set = config["experiment"]["data"]["selected_feature_set"]
            return f"ga|{model_type}|{seed}|{backend}|{feature_set}|{cand_str}"

        with Parallel(**get_parallel_settings(config)) as parallel:
            for gen in range(generations):
                logger.info(f"Model {model_type} - Seed {seed} - Generation {gen + 1}/{generations}")
                
                to_eval = []
                cached_results = []
                for idx in range(pop_size):
                    cand = vector_to_candidate(population[idx], config["search_spaces"], model_type)
                    key = get_cache_key(cand)
                    if key in cache:
                        res = cache[key].copy()
                        res["evaluation_id"] = evaluation_id + idx + 1
                        res["candidate_id"] = evaluation_id + idx + 1
                        res["cache_hit"] = True
                        res["cache_key"] = key
                        cached_results.append((idx, res))
                        hits += 1
                    else:
                        to_eval.append((idx, cand, key))

                parallel_results = []
                if to_eval:
                    parallel_results = parallel(
                        delayed(evaluate_candidate)(
                            model_type, "ga", cand, int(seed), config, data, evaluation_id + idx + 1
                        )
                        for idx, cand, _ in to_eval
                    )
                    for (idx, cand, key), res in zip(to_eval, parallel_results):
                        res["cache_hit"] = False
                        res["cache_key"] = key
                        cache[key] = res
                        cached_results.append((idx, res))
                
                cached_results.sort(key=lambda x: x[0])
                ordered_results = [res for _, res in cached_results]
                
                for idx, row in enumerate(ordered_results):
                    evaluation_id += 1
                    fitness[idx] = row["fitness"]
                    seed_fitnesses.append(row["fitness"])
                    rows.append(row)
                    if row["fitness"] > best_fitness:
                        best_fitness = row["fitness"]
                        best_vector = population[idx].copy()
                    convergence.append(
                        {
                            "model_type": model_type,
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
                        for j in range(len(lower)):
                            if rng.random() < float(ga_config.get("mutation_scale", 0.10)): # Per gene
                                if var_types[j] == "categorical" or var_types[j] == "int":
                                    child[j] = rng.integers(int(lower[j]), int(upper[j]) + 1)
                                else:
                                    scale = (upper[j] - lower[j]) * 0.1
                                    child[j] += rng.normal(0.0, scale)
                                    
                    child = np.clip(child, lower, upper)
                    next_population.append(child)
                population = np.vstack(next_population)

        assert best_vector is not None
        logger.info(f"Model {model_type} - Seed {seed} - Cache hits: {hits}/{generations * pop_size}")
        best_candidate = vector_to_candidate(best_vector, config["search_spaces"], model_type)
        best_test, seed_predictions = evaluate_best_on_test(model_type, "ga", best_candidate, int(seed), config, data)
        best_test["best_validation_fitness"] = float(best_fitness)
        best_test["worst_validation_fitness"] = float(min((r["fitness"] for r in rows), default=0.0))
        
        seed_results = {
            "runs": rows,
            "best": [best_test],
            "convergence": convergence,
            "predictions": seed_predictions,
        }
        append_optimizer_outputs(f"{model_type}_ga", seed_results, config)

    logger.info(f"Genetic Algorithm for {model_type} completed.")

if __name__ == "__main__":
    from src.benchmark import prepare_benchmark
    data, config = prepare_benchmark()
    run_ga(data, config, "mlp")
