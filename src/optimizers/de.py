"""Differential Evolution (DE/best/1/bin) using the shared objective function."""

from __future__ import annotations

from typing import Any
import logging

logger = logging.getLogger("de")

import numpy as np
from joblib import Parallel, delayed  # type: ignore

from src.benchmark import append_optimizer_outputs, clear_optimizer_outputs
from src.objective import evaluate_best_on_test, evaluate_candidate, vector_to_candidate, get_bounds
from src.optimizers.parallel import get_parallel_settings


def run_de(data: Any, config: dict[str, Any], model_type: str) -> None:
    """Run Differential Evolution sequentially over all seeds."""
    logger.info(f"Starting Differential Evolution for model: {model_type}...")
    
    mode = config["experiment"]["benchmark"].get("experiment_mode", "quick_test")
    mode_config = config["experiment"]["benchmark"][mode]
    de_config = config["experiment"]["benchmark"]["de"]
    
    pop_size = int(de_config["population_size"])
    generations = int(mode_config.get("generations", 10))
    seeds = mode_config.get("seeds", [1])
    
    F = float(de_config["mutation_factor"])
    CR = float(de_config["crossover_rate"])
    
    lower, upper, var_types = get_bounds(config["search_spaces"], model_type)

    for seed in seeds:
        rows: list[dict[str, Any]] = []
        convergence: list[dict[str, Any]] = []
        rng = np.random.default_rng(int(seed))
        
        population = rng.uniform(lower, upper, size=(pop_size, len(lower)))
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
            return f"de|{model_type}|{seed}|{backend}|{feature_set}|{cand_str}"

        with Parallel(**get_parallel_settings(config)) as parallel:
            # --- Initial evaluation of the population ---
            logger.info(f"Model {model_type} - Seed {seed} - Evaluating initial population")
            init_candidates = [
                vector_to_candidate(population[idx], config["search_spaces"], model_type)
                for idx in range(pop_size)
            ]
            init_results = parallel(
                delayed(evaluate_candidate)(
                    model_type, "de", cand, int(seed), config, data, idx + 1
                )
                for idx, cand in enumerate(init_candidates)
            )
            for idx, res in enumerate(init_results):
                evaluation_id += 1
                key = get_cache_key(init_candidates[idx])
                res["cache_hit"] = False
                res["cache_key"] = key
                cache[key] = res
                fitness[idx] = res["fitness"]
                seed_fitnesses.append(res["fitness"])
                rows.append(res)
                if res["fitness"] > best_fitness:
                    best_fitness = res["fitness"]
                    best_vector = population[idx].copy()
                convergence.append({
                    "model_type": model_type,
                    "optimizer": "de",
                    "seed": int(seed),
                    "evaluation_id": evaluation_id,
                    "best_fitness_so_far": float(best_fitness),
                    "mean_fitness_so_far": float(np.mean(seed_fitnesses)),
                })

            # --- DE generations ---
            for gen in range(1, generations):
                logger.info(f"Model {model_type} - Seed {seed} - Generation {gen + 1}/{generations}")

                best_idx = int(np.argmax(fitness))
                trials = np.empty_like(population)
                for i in range(pop_size):
                    idxs = [j for j in range(pop_size) if j != i]
                    r1, r2 = rng.choice(idxs, size=2, replace=False)

                    mutant = population[best_idx] + F * (population[r1] - population[r2])
                    mutant = np.clip(mutant, lower, upper)

                    trial = population[i].copy()
                    j_rand = rng.integers(len(lower))
                    for j in range(len(lower)):
                        if rng.random() < CR or j == j_rand:
                            trial[j] = mutant[j]
                    trials[i] = trial

                to_eval = []
                cached_results = []
                for idx in range(pop_size):
                    cand = vector_to_candidate(trials[idx], config["search_spaces"], model_type)
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
                            model_type, "de", cand, int(seed), config, data, evaluation_id + idx + 1
                        )
                        for idx, cand, _ in to_eval
                    )
                    for (idx, cand, key), res in zip(to_eval, parallel_results):
                        res["cache_hit"] = False
                        res["cache_key"] = key
                        cache[key] = res
                        cached_results.append((idx, res))

                cached_results.sort(key=lambda x: x[0])

                for idx, res in cached_results:
                    evaluation_id += 1
                    trial_fitness = res["fitness"]
                    seed_fitnesses.append(trial_fitness)
                    rows.append(res)

                    if trial_fitness >= fitness[idx]:
                        population[idx] = trials[idx].copy()
                        fitness[idx] = trial_fitness

                    if trial_fitness > best_fitness:
                        best_fitness = trial_fitness
                        best_vector = trials[idx].copy()

                    convergence.append({
                        "model_type": model_type,
                        "optimizer": "de",
                        "seed": int(seed),
                        "evaluation_id": evaluation_id,
                        "best_fitness_so_far": float(best_fitness),
                        "mean_fitness_so_far": float(np.mean(seed_fitnesses)),
                    })

        assert best_vector is not None
        logger.info(f"Model {model_type} - Seed {seed} - Cache hits: {hits}/{generations * pop_size}")
        best_candidate = vector_to_candidate(best_vector, config["search_spaces"], model_type)
        best_test, seed_predictions = evaluate_best_on_test(model_type, "de", best_candidate, int(seed), config, data)
        best_test["best_validation_fitness"] = float(best_fitness)
        best_test["worst_validation_fitness"] = float(min((r["fitness"] for r in rows), default=0.0))

        seed_results = {
            "runs": rows,
            "best": [best_test],
            "convergence": convergence,
            "predictions": seed_predictions,
        }
        append_optimizer_outputs(f"{model_type}_de", seed_results, config)

    logger.info(f"Differential Evolution for {model_type} completed.")

if __name__ == "__main__":
    from src.benchmark import prepare_benchmark
    data, config = prepare_benchmark()
    run_de(data, config, "mlp")
