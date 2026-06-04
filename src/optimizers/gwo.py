"""Grey Wolf Optimizer (GWO) using the shared objective function."""

from __future__ import annotations

from typing import Any
import logging

logger = logging.getLogger("gwo")

import numpy as np
from joblib import Parallel, delayed  # type: ignore

from src.benchmark import append_optimizer_outputs, clear_optimizer_outputs
from src.objective import evaluate_best_on_test, evaluate_candidate, vector_to_candidate, get_bounds


def run_gwo(data: Any, config: dict[str, Any], model_type: str) -> None:
    """Run Grey Wolf Optimizer sequentially over all seeds."""
    logger.info(f"Starting Grey Wolf Optimizer for model: {model_type}...")
    
    mode = config["experiment"]["benchmark"].get("experiment_mode", "quick_test")
    mode_config = config["experiment"]["benchmark"][mode]
    gwo_config = config["experiment"]["benchmark"]["gwo"]
    
    n_wolves = int(gwo_config["wolves"])
    iterations = int(mode_config.get("iterations", 10))
    seeds = mode_config.get("seeds", [1])
    
    lower, upper, var_types = get_bounds(config["search_spaces"], model_type)
    dim = len(lower)

    for seed in seeds:
        rows: list[dict[str, Any]] = []
        convergence: list[dict[str, Any]] = []
        rng = np.random.default_rng(int(seed))
        positions = rng.uniform(lower, upper, size=(n_wolves, dim))
        fitness = np.full(n_wolves, -np.inf)
        evaluation_id = 0
        seed_fitnesses: list[float] = []
        cache: dict[str, dict[str, Any]] = {}
        hits = 0

        alpha_pos = np.zeros(dim)
        alpha_score = -np.inf
        beta_pos = np.zeros(dim)
        beta_score = -np.inf
        delta_pos = np.zeros(dim)
        delta_score = -np.inf

        def get_cache_key(cand: dict[str, Any]) -> str:
            cand_str = "-".join([f"{k}:{v}" for k, v in cand.items()])
            backend = config["experiment"]["model"]["backend"]
            feature_set = config["experiment"]["data"]["selected_feature_set"]
            return f"gwo|{model_type}|{seed}|{backend}|{feature_set}|{cand_str}"

        with Parallel(n_jobs=-1, backend="loky", prefer="processes") as parallel:
            for iteration in range(iterations):
                logger.info(f"Model {model_type} - Seed {seed} - Iteration {iteration + 1}/{iterations}")

                to_eval = []
                cached_results = []
                for idx in range(n_wolves):
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
                            model_type, "gwo", cand, int(seed), config, data, evaluation_id + idx + 1
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
                    fitness[idx] = res["fitness"]
                    seed_fitnesses.append(res["fitness"])
                    rows.append(res)

                    if res["fitness"] > alpha_score:
                        delta_score = beta_score
                        delta_pos = beta_pos.copy()
                        beta_score = alpha_score
                        beta_pos = alpha_pos.copy()
                        alpha_score = res["fitness"]
                        alpha_pos = positions[idx].copy()
                    elif res["fitness"] > beta_score:
                        delta_score = beta_score
                        delta_pos = beta_pos.copy()
                        beta_score = res["fitness"]
                        beta_pos = positions[idx].copy()
                    elif res["fitness"] > delta_score:
                        delta_score = res["fitness"]
                        delta_pos = positions[idx].copy()

                    convergence.append({
                        "model_type": model_type,
                        "optimizer": "gwo",
                        "seed": int(seed),
                        "evaluation_id": evaluation_id,
                        "best_fitness_so_far": float(alpha_score),
                        "mean_fitness_so_far": float(np.mean(seed_fitnesses)),
                    })

                a = 2.0 - 2.0 * (iteration / max(iterations - 1, 1))

                for idx in range(n_wolves):
                    for j in range(dim):
                        r1, r2 = rng.random(), rng.random()
                        A1 = 2 * a * r1 - a
                        C1 = 2 * r2
                        D_alpha = abs(C1 * alpha_pos[j] - positions[idx][j])
                        X1 = alpha_pos[j] - A1 * D_alpha

                        r1, r2 = rng.random(), rng.random()
                        A2 = 2 * a * r1 - a
                        C2 = 2 * r2
                        D_beta = abs(C2 * beta_pos[j] - positions[idx][j])
                        X2 = beta_pos[j] - A2 * D_beta

                        r1, r2 = rng.random(), rng.random()
                        A3 = 2 * a * r1 - a
                        C3 = 2 * r2
                        D_delta = abs(C3 * delta_pos[j] - positions[idx][j])
                        X3 = delta_pos[j] - A3 * D_delta

                        positions[idx][j] = (X1 + X2 + X3) / 3.0

                positions = np.clip(positions, lower, upper)

        logger.info(f"Model {model_type} - Seed {seed} - Cache hits: {hits}/{iterations * n_wolves}")
        best_candidate = vector_to_candidate(alpha_pos, config["search_spaces"], model_type)
        best_test, seed_predictions = evaluate_best_on_test(model_type, "gwo", best_candidate, int(seed), config, data)
        best_test["best_validation_fitness"] = float(alpha_score)

        seed_results = {
            "runs": rows,
            "best": [best_test],
            "convergence": convergence,
            "predictions": seed_predictions,
        }
        append_optimizer_outputs(f"{model_type}_gwo", seed_results, config)

    logger.info(f"Grey Wolf Optimizer for {model_type} completed.")

if __name__ == "__main__":
    from src.benchmark import prepare_benchmark
    data, config = prepare_benchmark()
    run_gwo(data, config, "mlp")
