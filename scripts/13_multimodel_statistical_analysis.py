"""Perform statistical analysis across multi-model benchmark."""

import logging
from pathlib import Path
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("multimodel_stats")

def bootstrap_paired_diff(data1: np.ndarray, data2: np.ndarray, n_bootstraps: int = 10000) -> float:
    diffs = data1 - data2
    mean_diff = np.mean(diffs)
    shifted_diffs = diffs - mean_diff
    bootstrapped_means = np.random.choice(shifted_diffs, size=(n_bootstraps, len(diffs)), replace=True).mean(axis=1)
    p_value = np.mean(np.abs(bootstrapped_means) >= np.abs(mean_diff))
    return float(p_value)

def main():
    models = ["mlp", "svm", "rf", "cnn"]
    optimizers = ["random_search", "ga", "pso", "de", "gwo"]
    metrics = ["f1_test", "mcc_test", "auc_roc_test"]

    data_dict = {}
    for model in models:
        for opt in optimizers:
            path = Path(f"outputs/phase2/metrics/{model}_{opt}_best_by_seed.csv")
            if path.exists():
                data_dict[f"{model}_{opt}"] = pd.read_csv(path)

    if not data_dict:
        logger.error("No data found to analyze.")
        return

    test_rows = []

    # 1. Optimizer comparisons within the same model
    for model in models:
        pairs = [
            ("ga", "random_search"), ("pso", "random_search"), 
            ("de", "random_search"), ("gwo", "random_search"),
            ("pso", "ga"), ("de", "gwo")
        ]
        for opt1, opt2 in pairs:
            k1 = f"{model}_{opt1}"
            k2 = f"{model}_{opt2}"
            if k1 not in data_dict or k2 not in data_dict:
                continue

            df1 = data_dict[k1].sort_values("seed")
            df2 = data_dict[k2].sort_values("seed")
            
            common_seeds = set(df1["seed"]).intersection(set(df2["seed"]))
            if not common_seeds:
                continue
                
            df1 = df1[df1["seed"].isin(common_seeds)].sort_values("seed")
            df2 = df2[df2["seed"].isin(common_seeds)].sort_values("seed")

            for metric in metrics:
                if metric not in df1.columns or metric not in df2.columns:
                    continue
                vals1 = df1[metric].to_numpy()
                vals2 = df2[metric].to_numpy()
                mean_diff = np.mean(vals1 - vals2)
                p_value = bootstrap_paired_diff(vals1, vals2)
                std_diff = np.std(vals1 - vals2, ddof=1) if len(vals1) > 1 else 1e-8
                effect_size = mean_diff / (std_diff + 1e-8)
                
                interp = "significant improvement" if (p_value < 0.05 and mean_diff > 0) else \
                         "significant degradation" if (p_value < 0.05 and mean_diff < 0) else \
                         "higher observed" if mean_diff > 0 else "lower observed"

                test_rows.append({
                    "model_type": model,
                    "comparison_type": "intra_model",
                    "comparison": f"{opt1} vs {opt2}",
                    "metric": metric.replace("_test", ""),
                    "mean_difference": mean_diff,
                    "p_value": p_value,
                    "effect_size_d": effect_size,
                    "interpretation": interp
                })

    # 2. Model comparisons (best optimizer of model A vs best optimizer of model B)
    # We'll just compare MLP_RMSprop (wait, we test the full optimizer result, so let's compare MLP vs SVM for same optimizer)
    for opt in optimizers:
        pairs = [("mlp", "svm"), ("mlp", "rf"), ("svm", "rf")]
        for m1, m2 in pairs:
            k1 = f"{m1}_{opt}"
            k2 = f"{m2}_{opt}"
            if k1 not in data_dict or k2 not in data_dict:
                continue

            df1 = data_dict[k1].sort_values("seed")
            df2 = data_dict[k2].sort_values("seed")
            
            common_seeds = set(df1["seed"]).intersection(set(df2["seed"]))
            if not common_seeds:
                continue
                
            df1 = df1[df1["seed"].isin(common_seeds)].sort_values("seed")
            df2 = df2[df2["seed"].isin(common_seeds)].sort_values("seed")

            for metric in metrics:
                if metric not in df1.columns or metric not in df2.columns:
                    continue
                vals1 = df1[metric].to_numpy()
                vals2 = df2[metric].to_numpy()
                mean_diff = np.mean(vals1 - vals2)
                p_value = bootstrap_paired_diff(vals1, vals2)
                std_diff = np.std(vals1 - vals2, ddof=1) if len(vals1) > 1 else 1e-8
                effect_size = mean_diff / (std_diff + 1e-8)
                
                interp = "significant improvement" if (p_value < 0.05 and mean_diff > 0) else \
                         "significant degradation" if (p_value < 0.05 and mean_diff < 0) else \
                         "higher observed" if mean_diff > 0 else "lower observed"

                test_rows.append({
                    "model_type": "cross_model",
                    "comparison_type": f"{opt}_fixed",
                    "comparison": f"{m1} vs {m2}",
                    "metric": metric.replace("_test", ""),
                    "mean_difference": mean_diff,
                    "p_value": p_value,
                    "effect_size_d": effect_size,
                    "interpretation": interp
                })

    tests_df = pd.DataFrame(test_rows)
    Path("outputs/phase2/tables").mkdir(parents=True, exist_ok=True)
    tests_df.to_csv("outputs/phase2/tables/multimodel_pairwise_tests.csv", index=False)
    
    Path("outputs/phase2/reports").mkdir(parents=True, exist_ok=True)
    with open("outputs/phase2/reports/multimodel_statistical_analysis.md", "w") as f:
        f.write("# Multimodel Statistical Analysis\n\n")
        f.write("## Pairwise Tests\n")
        f.write(tests_df.round(4).to_markdown(index=False))

    logger.info("Statistical analysis generated successfully.")

if __name__ == "__main__":
    main()
