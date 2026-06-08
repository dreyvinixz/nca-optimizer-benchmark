"""Random Search baseline optimizer using the shared objective function."""

from __future__ import annotations

from typing import Any
import logging

logger = logging.getLogger("random_search")

import numpy as np
from joblib import Parallel, delayed  # type: ignore

from src.benchmark import append_optimizer_outputs, clear_optimizer_outputs
from src.objective import evaluate_best_on_test, evaluate_candidate, vector_to_candidate, get_bounds
from src.optimizers.parallel import get_parallel_settings


def run_random_search(data: Any, config: dict[str, Any], model_type: str) -> None:
    """Run Random Search sequentially over all seeds."""
    logger.info(f"Starting Random Search for model: {model_type}...")
    
    mode = config["experiment"]["benchmark"].get("experiment_mode", "quick_test")
    mode_config = config["experiment"]["benchmark"][mode]
    evaluations_per_seed = int(mode_config["evaluations_per_seed"])
    seeds = mode_config.get("seeds", [1])
    
    lower, upper, var_types = get_bounds(config["search_spaces"], model_type)

    for seed in seeds:
        rows: list[dict[str, Any]] = []
        convergence: list[dict[str, Any]] = []
        rng = np.random.default_rng(int(seed))
        
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
            return f"random_search|{model_type}|{seed}|{backend}|{feature_set}|{cand_str}"

        with Parallel(**get_parallel_settings(config)) as parallel:
            # Batching to mimic generations logging
            chunk_size = 10
            for chunk_start in range(0, evaluations_per_seed, chunk_size):
                chunk_end = min(chunk_start + chunk_size, evaluations_per_seed)
                size = chunk_end - chunk_start
                
                population = []
                for _ in range(size):
                    ind = []
                    for j in range(len(lower)):
                        if var_types[j] == "categorical" or var_types[j] == "int":
                            ind.append(rng.integers(int(lower[j]), int(upper[j]) + 1))
                        else:
                            ind.append(rng.uniform(lower[j], upper[j]))
                    population.append(ind)
                population = np.array(population, dtype=float)
                
                to_eval = []
                cached_results = []
                for idx in range(size):
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
                            model_type, "random_search", cand, int(seed), config, data, evaluation_id + idx + 1
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
                    seed_fitnesses.append(row["fitness"])
                    rows.append(row)
                    if row["fitness"] > best_fitness:
                        best_fitness = row["fitness"]
                        best_vector = population[idx].copy()
                    convergence.append(
                        {
                            "model_type": model_type,
                            "optimizer": "random_search",
                            "seed": int(seed),
                            "evaluation_id": evaluation_id,
                            "best_fitness_so_far": float(best_fitness),
                            "mean_fitness_so_far": float(np.mean(seed_fitnesses)),
                        }
                    )

        assert best_vector is not None
        logger.info(f"Model {model_type} - Seed {seed} - Cache hits: {hits}/{evaluations_per_seed}")
        best_candidate = vector_to_candidate(best_vector, config["search_spaces"], model_type)
        best_test, seed_predictions = evaluate_best_on_test(model_type, "random_search", best_candidate, int(seed), config, data)
        best_test["best_validation_fitness"] = float(best_fitness)
        best_test["worst_validation_fitness"] = float(min((r["fitness"] for r in rows), default=0.0))
        
        seed_results = {
            "runs": rows,
            "best": [best_test],
            "convergence": convergence,
            "predictions": seed_predictions,
        }
        append_optimizer_outputs(f"{model_type}_random_search", seed_results, config)

    logger.info(f"Random Search for {model_type} completed.")

if __name__ == "__main__":
    from src.benchmark import prepare_benchmark
    data, config = prepare_benchmark()
    run_random_search(data, config, "mlp")
