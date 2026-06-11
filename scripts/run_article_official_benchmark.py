"""Run the article-grade official benchmark.

Hardware policy:
    - MLP: CUDA C backend on GPU.
    - CNN: TensorFlow GPU.
    - RF/SVM: CPU through scikit-learn, with candidate-level parallelism.

The official budget is 1000 fitness evaluations per seed. For population-based
optimizers with population size 10, this is 100 generations/iterations.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import shutil
import sys
import time
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import pandas as pd

from src.benchmark import prepare_benchmark
from src.optimizers.de import run_de
from src.optimizers.ga import run_ga
from src.optimizers.gwo import run_gwo
from src.optimizers.pso import run_pso
from src.optimizers.random_search import run_random_search


MODELS = ["mlp", "rf", "svm", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]
RUNNERS: dict[str, Callable[[Any, dict[str, Any], str], None]] = {
    "random_search": run_random_search,
    "ga": run_ga,
    "pso": run_pso,
    "de": run_de,
    "gwo": run_gwo,
}


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--models", nargs="+", default=MODELS, choices=MODELS)
    parser.add_argument("--optimizers", nargs="+", default=OPTIMIZERS, choices=OPTIMIZERS)
    parser.add_argument("--output-root", default="outputs/article_official")
    parser.add_argument("--force", action="store_true", help="Archive and rerun completed outputs too.")
    parser.add_argument("--stop-on-error", action="store_true")
    parser.add_argument("--cpu-jobs", type=int, default=-1)
    parser.add_argument("--seeds", nargs="+", type=int, default=[1, 2, 3, 4, 5])
    parser.add_argument("--evaluations-per-seed", type=int, default=1000)
    parser.add_argument("--generations", type=int, default=None)
    parser.add_argument("--iterations", type=int, default=None)
    parser.add_argument("--fitness-mode", choices=["mcc_f1", "accuracy_cv"], default="mcc_f1")
    return parser


def _configure_logging(output_root: Path) -> Path:
    log_dir = ROOT / "logs" / "experiments"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"article_official_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
        force=True,
    )
    logging.info("Article official output root: %s", output_root)
    logging.info("Log file: %s", log_path)
    return log_path


def _configure_outputs(config: dict[str, Any], output_root: Path) -> None:
    outputs = config["paths"]["outputs"]
    outputs["root"] = str(output_root)
    outputs["metrics"] = str(output_root / "metrics")
    outputs["convergence"] = str(output_root / "metrics" / "convergence")
    outputs["predictions"] = str(output_root / "predictions")
    outputs["figures"] = str(output_root / "figures")
    outputs["tables"] = str(output_root / "tables")
    outputs["reports"] = str(output_root / "reports")
    outputs["statistical_tests"] = str(output_root / "statistical_tests")
    outputs["backtests"] = str(output_root / "backtests")
    for value in outputs.values():
        Path(value).mkdir(parents=True, exist_ok=True)


def _configure_official_budget(config: dict[str, Any], args: argparse.Namespace) -> None:
    benchmark = config["experiment"]["benchmark"]
    generations = args.generations or max(1, args.evaluations_per_seed // int(benchmark["ga"]["population_size"]))
    iterations = args.iterations or max(1, args.evaluations_per_seed // int(benchmark["pso"]["particles"]))
    benchmark["experiment_mode"] = "official_run"
    benchmark["official_experiment"] = True
    benchmark["official_run"]["seeds"] = args.seeds
    benchmark["official_run"]["evaluations_per_seed"] = args.evaluations_per_seed
    benchmark["official_run"]["generations"] = generations
    benchmark["official_run"]["iterations"] = iterations
    benchmark["official_run"]["official_experiment"] = True


def _configure_hardware(config: dict[str, Any], model_type: str, cpu_jobs: int) -> None:
    benchmark = config["experiment"]["benchmark"]
    model = config["experiment"]["model"]
    if model_type in ("mlp", "svm"):
        model["backend"] = "cuda"
        benchmark["parallel_enabled"] = False
        benchmark["n_jobs"] = 1
        benchmark["parallel_backend"] = "loky"
        benchmark["parallel_prefer"] = "processes"
    elif model_type == "rf":
        model["backend"] = "cuda"
        benchmark["parallel_enabled"] = True
        benchmark["n_jobs"] = 4
        benchmark["parallel_backend"] = "loky"
        benchmark["parallel_prefer"] = "processes"
    elif model_type == "cnn":
        model["backend"] = "cuda"
        benchmark["parallel_enabled"] = False
        benchmark["n_jobs"] = 1
        benchmark["parallel_backend"] = "loky"
        benchmark["parallel_prefer"] = "processes"
    else:
        model["backend"] = "auto"
        benchmark["parallel_enabled"] = True
        benchmark["n_jobs"] = cpu_jobs
        benchmark["parallel_backend"] = "loky"
        benchmark["parallel_prefer"] = "processes"


def _expected_rows(config: dict[str, Any]) -> int:
    mode = config["experiment"]["benchmark"]["official_run"]
    return int(mode["evaluations_per_seed"]) * len(mode["seeds"])


def _output_files(config: dict[str, Any], model_type: str, optimizer: str) -> list[Path]:
    outputs = config["paths"]["outputs"]
    stem = f"{model_type}_{optimizer}"
    return [
        Path(outputs["metrics"]) / f"{stem}_runs.csv",
        Path(outputs["metrics"]) / f"{stem}_best_by_seed.csv",
        Path(outputs["convergence"]) / f"{stem}_convergence.csv",
        Path(outputs["predictions"]) / f"{stem}_predictions.csv",
    ]


def _is_complete(config: dict[str, Any], model_type: str, optimizer: str) -> bool:
    runs, best, convergence, predictions = _output_files(config, model_type, optimizer)
    if not runs.exists() or not best.exists() or not convergence.exists() or not predictions.exists():
        return False
    try:
        return (
            len(pd.read_csv(runs)) >= _expected_rows(config)
            and len(pd.read_csv(convergence)) >= _expected_rows(config)
            and len(pd.read_csv(best)) >= len(config["experiment"]["benchmark"]["official_run"]["seeds"])
        )
    except Exception:
        return False


def _archive_existing(files: list[Path], output_root: Path, model_type: str, optimizer: str) -> None:
    existing = [path for path in files if path.exists()]
    if not existing:
        return
    archive_dir = output_root / "restarts" / datetime.now().strftime("%Y%m%d_%H%M%S") / model_type / optimizer
    archive_dir.mkdir(parents=True, exist_ok=True)
    for path in existing:
        shutil.move(str(path), archive_dir / path.name)
    logging.warning("Archived partial/old outputs for %s/%s to %s", model_type, optimizer, archive_dir)


def _write_status(output_root: Path, status: dict[str, Any]) -> None:
    status_path = output_root / "reports" / "article_official_status.json"
    status_path.parent.mkdir(parents=True, exist_ok=True)
    status_path.write_text(json.dumps(status, indent=2), encoding="utf-8")


def main() -> None:
    args = _build_parser().parse_args()
    if args.fitness_mode == "accuracy_cv" and args.output_root == "outputs/article_official":
        args.output_root = "outputs/article_official_accuracy"
        
    output_root = ROOT / args.output_root
    output_root.mkdir(parents=True, exist_ok=True)
    log_path = _configure_logging(output_root)

    data, base_config = prepare_benchmark()
    if "objective" not in base_config["experiment"]:
        base_config["experiment"]["objective"] = {}
    base_config["experiment"]["objective"]["fitness_mode"] = args.fitness_mode
    
    _configure_outputs(base_config, output_root)
    _configure_official_budget(base_config, args)

    status: dict[str, Any] = {
        "started_at": datetime.now().isoformat(timespec="seconds"),
        "output_root": str(output_root),
        "log_path": str(log_path),
        "models": args.models,
        "optimizers": args.optimizers,
        "expected_rows_per_combination": _expected_rows(base_config),
        "completed": [],
        "skipped": [],
        "failed": [],
        "current": None,
    }
    _write_status(output_root, status)

    logging.info(
        "Official budget: %s evaluations/seed, %s seeds, %s expected rows per model/optimizer.",
        args.evaluations_per_seed,
        len(args.seeds),
        _expected_rows(base_config),
    )
    logging.info("Model order: %s", args.models)
    logging.info("Optimizer order: %s", args.optimizers)

    for model_type in args.models:
        for optimizer in args.optimizers:
            config = deepcopy(base_config)
            _configure_hardware(config, model_type, args.cpu_jobs)
            combo = {"model": model_type, "optimizer": optimizer}
            status["current"] = combo
            _write_status(output_root, status)

            files = _output_files(config, model_type, optimizer)
            if _is_complete(config, model_type, optimizer) and not args.force:
                logging.info("Skipping complete combination: %s/%s", model_type, optimizer)
                status["skipped"].append(combo)
                status["current"] = None
                _write_status(output_root, status)
                continue

            if args.force or any(path.exists() for path in files):
                _archive_existing(files, output_root, model_type, optimizer)

            logging.info(
                "Starting %s/%s with backend=%s n_jobs=%s",
                model_type,
                optimizer,
                config["experiment"]["model"].get("backend"),
                config["experiment"]["benchmark"].get("n_jobs"),
            )
            started = time.perf_counter()
            try:
                RUNNERS[optimizer](data, config, model_type)
                elapsed = time.perf_counter() - started
                complete = _is_complete(config, model_type, optimizer)
                result = {
                    **combo,
                    "elapsed_seconds": round(elapsed, 3),
                    "complete": complete,
                }
                status["completed"].append(result)
                logging.info("Finished %s/%s in %.1fs complete=%s", model_type, optimizer, elapsed, complete)
            except Exception as exc:
                elapsed = time.perf_counter() - started
                result = {
                    **combo,
                    "elapsed_seconds": round(elapsed, 3),
                    "error": repr(exc),
                }
                status["failed"].append(result)
                logging.exception("Failed %s/%s after %.1fs", model_type, optimizer, elapsed)
                if args.stop_on_error:
                    status["current"] = None
                    _write_status(output_root, status)
                    raise
            finally:
                status["current"] = None
                status["updated_at"] = datetime.now().isoformat(timespec="seconds")
                _write_status(output_root, status)

    status["finished_at"] = datetime.now().isoformat(timespec="seconds")
    _write_status(output_root, status)
    logging.info("Article official benchmark runner finished.")


if __name__ == "__main__":
    main()
