"""Run the quick GA + MLP benchmark with the CUDA backend.

Expected WSL2 usage:
    cd /mnt/c/mysystems/projects/nca-optimizer-benchmark
    source .venv_wsl/bin/activate
    cd cuda && make && cd ..
    python scripts/gpu_benchmark_test.py
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd

from src.benchmark import prepare_benchmark
from src.evaluation.metrics import compute_classification_metrics
from src.models.mlp_cuda import fit_predict_mlp_cuda, fit_predict_mlp_cuda_batch
from src.objective import get_bounds, normalize_candidate, vector_to_candidate


def _fitness(metrics: dict[str, float], config: dict[str, Any]) -> float:
    weights = config["experiment"]["objective"]["fitness"]
    return float(weights["mcc_weight"] * metrics["mcc"] + weights["f1_weight"] * metrics["f1"])


def _fitness_formula(config: dict[str, Any]) -> str:
    weights = config["experiment"]["objective"]["fitness"]
    return f"{weights['mcc_weight']} * MCC + {weights['f1_weight']} * F1"


def _result_row(
    *,
    seed: int,
    generation: int | None,
    evaluation_id: int,
    candidate: dict[str, Any],
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_proba: np.ndarray,
    info: dict[str, Any],
    backend: str,
    config: dict[str, Any],
    wall_time_seconds: float,
    batch_total_time: float | None = None,
    batch_candidate_count: int | None = None,
) -> dict[str, Any]:
    metrics = compute_classification_metrics(y_true, y_pred, y_proba)
    benchmark_cfg = config["experiment"]["benchmark"]
    mode = benchmark_cfg.get("experiment_mode", "quick_test")
    official = bool(benchmark_cfg.get(mode, {}).get("official_experiment", False))

    row = {
        "model_type": "mlp",
        "optimizer": "ga",
        "seed": int(seed),
        "candidate_id": int(evaluation_id),
        "evaluation_id": int(evaluation_id),
        "fitness": _fitness(metrics, config),
        "mcc": float(metrics["mcc"]),
        "f1": float(metrics["f1"]),
        "auc_roc": float(metrics["auc_roc"]),
        "auc_pr": float(metrics["auc_pr"]),
        "accuracy": float(metrics["accuracy"]),
        "precision": float(metrics["precision"]),
        "recall": float(metrics["recall"]),
        "train_time_seconds": float(info["train_time_cuda"]),
        "eval_time_seconds": 0.0,
        "model_backend": backend,
        "official_experiment": official,
        "cache_hit": False,
        "cache_key": "",
        "parallel_enabled": batch_total_time is not None,
        "n_jobs": int(batch_candidate_count or 1),
        "parallel_backend": "cuda_batch" if batch_total_time is not None else "cuda_single",
        "cuda_kernel_time": float(info["train_time_cuda"]),
        "wall_time_per_eval": float(wall_time_seconds),
        "fitness_formula": _fitness_formula(config),
        "decoded_hyperparameters": json.dumps(candidate),
    }
    if generation is not None:
        row["generation"] = int(generation)
    if batch_total_time is not None:
        row["batch_total_time"] = float(batch_total_time)
        row["batch_candidate_count"] = int(batch_candidate_count or 1)
    return row


def evaluate_candidate_cuda(
    candidate: dict[str, Any],
    seed: int,
    config: dict[str, Any],
    data: Any,
    evaluation_id: int,
) -> dict[str, Any]:
    """Evaluate one candidate with the CUDA backend."""
    model_config = config["experiment"]["model"]
    candidate = normalize_candidate(candidate, config["search_spaces"], "mlp")

    started = time.perf_counter()
    y_pred, y_proba, info, backend = fit_predict_mlp_cuda(
        data.X_train_scaled,
        data.y_train,
        data.X_val_scaled,
        candidate,
        model_config,
        seed + evaluation_id,
    )
    wall_time = time.perf_counter() - started

    return _result_row(
        seed=seed,
        generation=None,
        evaluation_id=evaluation_id,
        candidate=candidate,
        y_true=data.y_val,
        y_pred=y_pred,
        y_proba=y_proba,
        info=info,
        backend=backend,
        config=config,
        wall_time_seconds=wall_time,
    )


def evaluate_batch_cuda(
    population: np.ndarray,
    seed: int,
    config: dict[str, Any],
    data: Any,
    eval_start: int,
    generation: int,
) -> list[dict[str, Any]]:
    """Evaluate an entire GA population through the CUDA batch API."""
    model_config = config["experiment"]["model"]
    candidates = [
        normalize_candidate(
            vector_to_candidate(vec, config["search_spaces"], "mlp"),
            config["search_spaces"],
            "mlp",
        )
        for vec in population
    ]
    seeds = [seed + eval_start + i + 1 for i in range(len(candidates))]

    started = time.perf_counter()
    batch_results = fit_predict_mlp_cuda_batch(
        data.X_train_scaled,
        data.y_train,
        data.X_val_scaled,
        candidates,
        model_config,
        seeds,
    )
    batch_total_time = time.perf_counter() - started
    wall_per_eval = batch_total_time / max(len(candidates), 1)

    rows = []
    for idx, (y_pred, y_proba, info, backend) in enumerate(batch_results):
        rows.append(
            _result_row(
                seed=seed,
                generation=generation,
                evaluation_id=eval_start + idx + 1,
                candidate=candidates[idx],
                y_true=data.y_val,
                y_pred=y_pred,
                y_proba=y_proba,
                info=info,
                backend=backend,
                config=config,
                wall_time_seconds=wall_per_eval,
                batch_total_time=batch_total_time,
                batch_candidate_count=len(candidates),
            )
        )
    return rows


def _tournament(
    rng: np.random.Generator,
    population: np.ndarray,
    fitness: np.ndarray,
    size: int,
) -> np.ndarray:
    indices = rng.choice(len(population), size=size, replace=False)
    return population[indices[np.argmax(fitness[indices])]].copy()


def _initial_population(
    rng: np.random.Generator,
    lower: np.ndarray,
    upper: np.ndarray,
    var_types: list[str],
    pop_size: int,
) -> np.ndarray:
    population = []
    for _ in range(pop_size):
        individual = []
        for idx, kind in enumerate(var_types):
            if kind in {"categorical", "int"}:
                individual.append(rng.integers(int(lower[idx]), int(upper[idx]) + 1))
            else:
                individual.append(rng.uniform(lower[idx], upper[idx]))
        population.append(individual)
    return np.array(population, dtype=float)


def run_ga_cuda(data: Any, config: dict[str, Any]) -> pd.DataFrame:
    """Run the quick-test GA with CUDA MLP evaluations."""
    benchmark_cfg = config["experiment"]["benchmark"]
    mode = benchmark_cfg.get("experiment_mode", "quick_test")
    mode_config = benchmark_cfg[mode]
    ga_config = benchmark_cfg["ga"]

    pop_size = int(ga_config["population_size"])
    generations = int(mode_config.get("generations", 10))
    seed = int(mode_config.get("seeds", [1])[0])
    lower, upper, var_types = get_bounds(config["search_spaces"], "mlp")

    print()
    print("=" * 60)
    print("  GPU BENCHMARK - GA + MLP (CUDA)")
    print(f"  Generations: {generations} | Population: {pop_size}")
    print(f"  Seed: {seed} | Total evals: {generations * pop_size}")
    print("=" * 60)
    print()

    rng = np.random.default_rng(seed)
    population = _initial_population(rng, lower, upper, var_types, pop_size)
    fitness = np.full(pop_size, -np.inf)
    best_fitness = -np.inf
    rows: list[dict[str, Any]] = []
    evaluation_id = 0
    total_start = time.perf_counter()

    for gen in range(generations):
        gen_start = time.perf_counter()
        batch_rows = evaluate_batch_cuda(population, seed, config, data, evaluation_id, gen + 1)

        for idx, row in enumerate(batch_rows):
            evaluation_id += 1
            fitness[idx] = row["fitness"]
            rows.append(row)
            best_fitness = max(best_fitness, row["fitness"])

        gen_time = time.perf_counter() - gen_start
        avg_wall = float(np.mean([r["wall_time_per_eval"] for r in batch_rows]))
        print(
            f"  Gen {gen + 1:3d}/{generations} | "
            f"Best: {best_fitness:.4f} | "
            f"Gen time: {gen_time:.2f}s | "
            f"Wall/eval: {avg_wall:.3f}s"
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
                for idx, kind in enumerate(var_types):
                    if rng.random() < float(ga_config.get("mutation_scale", 0.10)):
                        if kind in {"categorical", "int"}:
                            child[idx] = rng.integers(int(lower[idx]), int(upper[idx]) + 1)
                        else:
                            scale = (upper[idx] - lower[idx]) * 0.1
                            child[idx] += rng.normal(0.0, scale)
            next_population.append(np.clip(child, lower, upper))
        population = np.vstack(next_population)

    total_time = time.perf_counter() - total_start
    print()
    print("=" * 60)
    print(f"  COMPLETED - Total wall time: {total_time:.1f}s ({total_time / 60:.1f}min)")
    print(f"  Best fitness: {best_fitness:.4f}")
    print(f"  Avg wall/eval: {np.mean([r['wall_time_per_eval'] for r in rows]):.3f}s")
    print("=" * 60)
    print()

    return pd.DataFrame(rows)


def _total_gpu_wall_seconds(df: pd.DataFrame) -> float:
    if {"seed", "generation", "batch_total_time"}.issubset(df.columns):
        return float(df.drop_duplicates(["seed", "generation"])["batch_total_time"].sum())
    if "wall_time_per_eval" in df.columns:
        return float(df["wall_time_per_eval"].sum())
    return float(df["train_time_seconds"].sum())


def main() -> None:
    try:
        data, config = prepare_benchmark()
        df_gpu = run_ga_cuda(data, config)
    except FileNotFoundError as exc:
        print(str(exc))
        print("Build the CUDA library first with: cd cuda && make")
        raise SystemExit(1) from exc

    output_dir = Path(config["paths"]["outputs"]["root"]) / "gpu_test"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "mlp_ga_gpu_runs.csv"
    df_gpu.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")

    print()
    print("--- GPU Summary ---")
    print(f"  Total evaluations: {len(df_gpu)}")
    print(f"  Avg CUDA time:     {df_gpu['train_time_seconds'].mean():.3f}s")
    print(f"  Avg wall/eval:     {df_gpu['wall_time_per_eval'].mean():.3f}s")
    print(f"  Total wall time:   {_total_gpu_wall_seconds(df_gpu):.1f}s")


if __name__ == "__main__":
    main()
