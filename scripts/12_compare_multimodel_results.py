"""Generate summary statistics for multi-model benchmark."""

import logging
from pathlib import Path
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("multimodel_summary")

def bootstrap_ci(data: np.ndarray, n_bootstraps: int = 10000, ci: float = 95.0) -> tuple[float, float]:
    if len(data) == 0:
        return (0.0, 0.0)
    bootstrapped_means = np.random.choice(data, size=(n_bootstraps, len(data)), replace=True).mean(axis=1)
    lower = np.percentile(bootstrapped_means, (100 - ci) / 2)
    upper = np.percentile(bootstrapped_means, 100 - (100 - ci) / 2)
    return float(lower), float(upper)

def main():
    models = ["mlp", "svm", "rf", "cnn"]
    optimizers = ["random_search", "ga", "pso", "de", "gwo"]
    metrics = ["f1_test", "mcc_test", "auc_roc_test", "auc_pr_test", "best_validation_fitness", "runtime_seconds_test"]

    summary_rows = []
    
    for model in models:
        for opt in optimizers:
            path = Path(f"outputs/phase2/metrics/{model}_{opt}_best_by_seed.csv")
            if not path.exists():
                logger.warning(f"File not found: {path}")
                continue
                
            df = pd.read_csv(path)
            for metric in metrics:
                if metric not in df.columns:
                    continue
                vals = df[metric].dropna().to_numpy()
                if len(vals) == 0:
                    continue
                
                ci_low, ci_high = bootstrap_ci(vals)
                summary_rows.append({
                    "model_type": model,
                    "optimizer": opt,
                    "metric": metric.replace("_test", ""),
                    "mean": np.mean(vals),
                    "std": np.std(vals),
                    "median": np.median(vals),
                    "min": np.min(vals),
                    "max": np.max(vals),
                    "ci_95_lower": ci_low,
                    "ci_95_upper": ci_high,
                    "n_seeds": len(vals)
                })

    if not summary_rows:
        logger.error("No data found to analyze.")
        return

    summary_df = pd.DataFrame(summary_rows)
    Path("outputs/phase2/tables").mkdir(parents=True, exist_ok=True)
    summary_df.to_csv("outputs/phase2/tables/multimodel_summary_statistics.csv", index=False)
    
    Path("outputs/phase2/reports").mkdir(parents=True, exist_ok=True)
    with open("outputs/phase2/reports/multimodel_benchmark_summary.md", "w") as f:
        f.write("# Multimodel Benchmark Summary\n\n")
        f.write("## Summary Statistics\n")
        f.write(summary_df.round(4).to_markdown(index=False))

    logger.info("Summary statistics generated successfully.")

if __name__ == "__main__":
    main()
