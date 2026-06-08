"""Particle Swarm Optimization (PSO) using the shared objective function."""

from __future__ import annotations

from typing import Any
import logging

logger = logging.getLogger("pso")

import numpy as np
from joblib import Parallel, delayed  # type: ignore

from src.benchmark import append_optimizer_outputs, clear_optimizer_outputs
from src.objective import evaluate_best_on_test, evaluate_candidate, vector_to_candidate, get_bounds
from src.optimizers.parallel import get_parallel_settings


def run_pso(data: Any, config: dict[str, Any], model_type: str) -> None:
    """Run Particle Swarm Optimization sequentially over all seeds."""
    logger.info(f"Starting Particle Swarm Optimization for model: {model_type}...")
    
    mode = config["experiment"]["benchmark"].get("experiment_mode", "quick_test")
    mode_config = config["experiment"]["benchmark"][mode]
    pso_config = config["experiment"]["benchmark"]["pso"]
    
    n_particles = int(pso_config["particles"])
    iterations = int(mode_config.get("iterations", 10))
    seeds = mode_config.get("seeds", [1])
    
    w = float(pso_config["inertia"])
    c1 = float(pso_config["cognitive"])
    c2 = float(pso_config["social"])

    lower, upper, var_types = get_bounds(config["search_spaces"], model_type)
    dim = len(lower)

    for seed in seeds:
        rows: list[dict[str, Any]] = []
        convergence: list[dict[str, Any]] = []
        rng = np.random.default_rng(int(seed))
        
        # Initialize continuously for PSO
        positions = rng.uniform(lower, upper, size=(n_particles, dim))
        velocities = np.zeros_like(positions)
        
        pbest_positions = positions.copy()
        pbest_fitness = np.full(n_particles, -np.inf)
        
        gbest_position = np.zeros(dim)
        gbest_fitness = -np.inf
        
        evaluation_id = 0
        seed_fitnesses: list[float] = []
        cache: dict[str, dict[str, Any]] = {}
        hits = 0

        def get_cache_key(cand: dict[str, Any]) -> str:
            cand_str = "-".join([f"{k}:{v}" for k, v in cand.items()])
            backend = config["experiment"]["model"]["backend"]
            feature_set = config["experiment"]["data"]["selected_feature_set"]
            return f"pso|{model_type}|{seed}|{backend}|{feature_set}|{cand_str}"

        with Parallel(**get_parallel_settings(config)) as parallel:
            for iteration in range(iterations):
                logger.info(f"Model {model_type} - Seed {seed} - Iteration {iteration + 1}/{iterations}")

                to_eval = []
                cached_results = []
                for idx in range(n_particles):
                    cand = vector_to_candidate(positions[idx], config["search_spaces"], model_type)
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
                            model_type, "pso", cand, int(seed), config, data, evaluation_id + idx + 1
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
                    fitness = res["fitness"]
                    seed_fitnesses.append(fitness)
                    rows.append(res)

                    if fitness > pbest_fitness[idx]:
                        pbest_fitness[idx] = fitness
                        pbest_positions[idx] = positions[idx].copy()

                    if fitness > gbest_fitness:
                        gbest_fitness = fitness
                        gbest_position = positions[idx].copy()

                    convergence.append({
                        "model_type": model_type,
                        "optimizer": "pso",
                        "seed": int(seed),
                        "evaluation_id": evaluation_id,
                        "best_fitness_so_far": float(gbest_fitness),
                        "mean_fitness_so_far": float(np.mean(seed_fitnesses)),
                    })

                # Update velocities and positions
                r1 = rng.random(size=(n_particles, dim))
                r2 = rng.random(size=(n_particles, dim))
                velocities = (w * velocities +
                              c1 * r1 * (pbest_positions - positions) +
                              c2 * r2 * (gbest_position - positions))
                positions = positions + velocities
                positions = np.clip(positions, lower, upper)

        logger.info(f"Model {model_type} - Seed {seed} - Cache hits: {hits}/{iterations * n_particles}")
        best_candidate = vector_to_candidate(gbest_position, config["search_spaces"], model_type)
        best_test, seed_predictions = evaluate_best_on_test(model_type, "pso", best_candidate, int(seed), config, data)
        best_test["best_validation_fitness"] = float(gbest_fitness)
        best_test["worst_validation_fitness"] = float(min((r["fitness"] for r in rows), default=0.0))

        seed_results = {
            "runs": rows,
            "best": [best_test],
            "convergence": convergence,
            "predictions": seed_predictions,
        }
        append_optimizer_outputs(f"{model_type}_pso", seed_results, config)

    logger.info(f"Particle Swarm Optimization for {model_type} completed.")

if __name__ == "__main__":
    from src.benchmark import prepare_benchmark
    data, config = prepare_benchmark()
    run_pso(data, config, "mlp")
