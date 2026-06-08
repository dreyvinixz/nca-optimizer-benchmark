"""Run all 5 baseline optimizers against all 4 models with resumability."""

import logging
import sys
import pandas as pd
from pathlib import Path
from copy import deepcopy

# Add root to sys path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.benchmark import prepare_benchmark
from src.optimizers.random_search import run_random_search
from src.optimizers.ga import run_ga
from src.optimizers.pso import run_pso
from src.optimizers.de import run_de
from src.optimizers.gwo import run_gwo

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("run_all_baselines")

OPTIMIZERS = {
    "random_search": run_random_search,
    "ga": run_ga,
    "pso": run_pso,
    "de": run_de,
    "gwo": run_gwo
}

MODELS = ["mlp", "cnn", "svm", "rf"]

def get_completed_seeds(model_type: str, algo_name: str, config: dict) -> set[int]:
    """Check which seeds are fully completed by reading best_by_seed.csv."""
    optimizer_name = f"{model_type}_{algo_name}"
    metrics_path = Path(config["paths"]["outputs"]["metrics"]) / f"{optimizer_name}_best_by_seed.csv"
    if not metrics_path.exists():
        return set()
    try:
        df = pd.read_csv(metrics_path)
        if "seed" in df.columns:
            return set(df["seed"].astype(int).unique())
        return set()
    except Exception as e:
        logger.warning(f"Failed to read {metrics_path}: {e}")
        return set()

def main():
    logger.info("Initializing Official Baseline Run...")
    
    # 1. Load configuration and dataset
    data, base_config = prepare_benchmark()
    
    mode = base_config["experiment"]["benchmark"].get("experiment_mode", "quick_test")
    mode_config = base_config["experiment"]["benchmark"][mode]
    
    if mode != "official_run":
        logger.warning(f"Experiment mode is set to '{mode}'. Setting it to 'official_run'.")
        base_config["experiment"]["benchmark"]["experiment_mode"] = "official_run"
        mode = "official_run"
        mode_config = base_config["experiment"]["benchmark"][mode]
    
    target_seeds = list(mode_config.get("seeds", [1, 2, 3]))
    
    logger.info(f"Target Models: {MODELS}")
    logger.info(f"Target Optimizers: {list(OPTIMIZERS.keys())}")
    logger.info(f"Target Seeds: {target_seeds}")
    logger.info(f"Budget per seed: {mode_config.get('evaluations_per_seed', 0)} evals")
    
    total_tasks = len(MODELS) * len(OPTIMIZERS)
    current_task = 0
    
    for model in MODELS:
        for algo_name, algo_runner in OPTIMIZERS.items():
            current_task += 1
            logger.info("="*60)
            logger.info(f"Task {current_task}/{total_tasks}: Running {algo_name.upper()} on {model.upper()}")
            logger.info("="*60)
            
            # Check for resumability
            completed = get_completed_seeds(model, algo_name, base_config)
            remaining_seeds = [s for s in target_seeds if s not in completed]
            
            if not remaining_seeds:
                logger.info(f"Skipping {algo_name} on {model} - all {len(target_seeds)} seeds completed.")
                continue
                
            if len(remaining_seeds) < len(target_seeds):
                logger.info(f"Resuming {algo_name} on {model}. Completed: {completed}. Remaining: {remaining_seeds}")
            
            # Inject remaining seeds into a copy of config
            run_config = deepcopy(base_config)
            run_config["experiment"]["benchmark"][mode]["seeds"] = remaining_seeds
            
            # Launch the optimizer runner
            try:
                algo_runner(data, run_config, model)
            except Exception as e:
                logger.error(f"Failed during {algo_name} on {model}: {e}")
                logger.error("Continuing to next task...")
                
    logger.info("Official Baseline Run Completed!")

if __name__ == "__main__":
    main()
