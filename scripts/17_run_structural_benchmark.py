"""Run preliminary structural benchmark to compare Optimizer and Activation synergies."""

import logging
import sys
from copy import deepcopy
from pathlib import Path
from itertools import product

# Add root to sys path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.benchmark import prepare_benchmark
from src.optimizers.random_search import run_random_search

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
    )

def main():
    configure_logging()
    data, base_config = prepare_benchmark()
    
    # We will test the 4 structural combinations using Random Search as a fast proxy
    optimizers = ["rmsprop"]
    activations = ["relu"]
    models_to_test = ["mlp"]
    combinations = list(product(optimizers, activations))
    
    # Set quick test mode
    base_config["experiment"]["benchmark"]["experiment_mode"] = "quick_test"
    base_config["experiment"]["benchmark"]["quick_test"]["seeds"] = [42, 123, 2024]
    base_config["experiment"]["benchmark"]["quick_test"]["evaluations_per_seed"] = 50
    
    output_root = Path("outputs/structural_benchmark")
    output_root.mkdir(parents=True, exist_ok=True)
    
    for opt, act in combinations:
        logging.info(f"Running Preliminary Structural Benchmark: {opt.upper()} + {act.upper()}")
        config = deepcopy(base_config)
        
        # Override the MLP structural configs
        config["experiment"]["model"]["optimizer"] = opt
        config["experiment"]["model"]["activation"] = act
        
        # Redirect outputs so they don't pollute the official benchmark
        struct_id = f"{opt}_{act}"
        outputs = config["paths"]["outputs"]
        outputs["root"] = str(output_root / struct_id)
        outputs["metrics"] = str(output_root / struct_id / "metrics")
        outputs["convergence"] = str(output_root / struct_id / "metrics" / "convergence")
        outputs["predictions"] = str(output_root / struct_id / "predictions")
        
        for path in outputs.values():
            if isinstance(path, str):
                Path(path).mkdir(parents=True, exist_ok=True)
            
        for model_type in models_to_test:
            # Skip if already run
            test_file = Path(outputs["metrics"]) / f"{model_type}_random_search_best_by_seed.csv"
            if test_file.exists():
                logging.info(f"Skipping {model_type.upper()} for {opt}+{act} (already exists)")
                continue
                
            if model_type == "mlp":
                config["experiment"]["model"]["backend"] = "cuda"
            elif model_type == "cnn":
                config["experiment"]["model"]["backend"] = "cuda"
                
            logging.info(f"Running Random Search for {model_type.upper()} on {opt}+{act} with backend={config['experiment']['model']['backend']}")
            run_random_search(data, config, model_type)
        
    logging.info("Structural Benchmark Preliminary Run Complete.")

if __name__ == "__main__":
    main()
