"""Run Multimodel Official Benchmark."""

import logging
from src.benchmark import prepare_benchmark
from src.optimizers.random_search import run_random_search
from src.optimizers.ga import run_ga
from src.optimizers.pso import run_pso
from src.optimizers.de import run_de
from src.optimizers.gwo import run_gwo

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("official")

def main():
    data, config = prepare_benchmark()
    
    # Force official mode
    config["experiment"]["benchmark"]["experiment_mode"] = "official_run"
    
    models = ["mlp", "svm", "rf", "cnn"]
    
    for model_type in models:
        logger.info(f"--- Running Official Benchmark for {model_type} ---")
        run_random_search(data, config, model_type)
        run_ga(data, config, model_type)
        run_pso(data, config, model_type)
        run_de(data, config, model_type)
        run_gwo(data, config, model_type)

    logger.info("Official benchmark completed for all models and optimizers.")

if __name__ == "__main__":
    main()
