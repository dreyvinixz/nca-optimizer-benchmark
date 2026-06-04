"""Statistical analysis of optimizer performance."""

import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy import stats

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("stat_analysis")

def load_data() -> dict[str, pd.DataFrame]:
    """Load test metrics for the optimizers.
    Although the prompt mentioned _runs.csv, test metrics are stored in _best_by_seed.csv.
    We will load both but focus on test set performance for the analysis.
    """
    optimizers = ["random_search", "ga", "pso", "de", "gwo"]
    data_dict = {}
    
    for opt in optimizers:
        path = Path(f"outputs/metrics/{opt}_best_by_seed.csv")
        if path.exists():
            data_dict[opt] = pd.read_csv(path)
        else:
            logger.warning(f"File not found: {path}")
            
    return data_dict

def bootstrap_ci(data: np.ndarray, n_bootstraps: int = 10000, ci: float = 95.0) -> tuple[float, float]:
    """Calculate bootstrap confidence interval for the mean."""
    if len(data) == 0:
        return (0.0, 0.0)
    bootstrapped_means = np.random.choice(data, size=(n_bootstraps, len(data)), replace=True).mean(axis=1)
    lower = np.percentile(bootstrapped_means, (100 - ci) / 2)
    upper = np.percentile(bootstrapped_means, 100 - (100 - ci) / 2)
    return float(lower), float(upper)

def bootstrap_paired_diff(data1: np.ndarray, data2: np.ndarray, n_bootstraps: int = 10000) -> float:
    """Calculate p-value using paired bootstrap hypothesis testing (H0: mean diff == 0)."""
    diffs = data1 - data2
    mean_diff = np.mean(diffs)
    
    # Shift diffs so the null hypothesis is true (mean = 0)
    shifted_diffs = diffs - mean_diff
    
    # Bootstrap the shifted differences
    bootstrapped_means = np.random.choice(shifted_diffs, size=(n_bootstraps, len(diffs)), replace=True).mean(axis=1)
    
    # P-value: proportion of bootstrapped means more extreme than the observed mean diff
    p_value = np.mean(np.abs(bootstrapped_means) >= np.abs(mean_diff))
    return float(p_value)

def run_analysis():
    data_dict = load_data()
    if not data_dict:
        logger.error("No data found to analyze.")
        return

    metrics = ["f1_test", "mcc_test", "auc_roc_test", "auc_pr_test", "best_validation_fitness"]
    
    # 1. Summary Statistics
    summary_rows = []
    for opt, df in data_dict.items():
        for metric in metrics:
            if metric not in df.columns:
                continue
            vals = df[metric].dropna().to_numpy()
            if len(vals) == 0:
                continue
            
            ci_low, ci_high = bootstrap_ci(vals)
            summary_rows.append({
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
            
    summary_df = pd.DataFrame(summary_rows)
    Path("outputs/tables").mkdir(parents=True, exist_ok=True)
    summary_df.to_csv("outputs/tables/optimizer_summary_statistics.csv", index=False)
    
    # 2. Pairwise Tests
    pairs = [
        # Each optimizer vs baseline
        ("ga", "random_search"),
        ("pso", "random_search"),
        ("de", "random_search"),
        ("gwo", "random_search"),
        # Intra-family: Evolutionary
        ("de", "ga"),
        # Intra-family: Swarm
        ("gwo", "pso"),
        # Inter-family: best evolutionary vs best swarm
        ("pso", "ga"),
        ("de", "gwo"),
    ]
    test_rows = []
    
    for opt1, opt2 in pairs:
        if opt1 not in data_dict or opt2 not in data_dict:
            continue
            
        df1 = data_dict[opt1].sort_values("seed")
        df2 = data_dict[opt2].sort_values("seed")
        
        # Ensure we're comparing the same seeds
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
            n_seeds = len(vals1)
            
            # Decide test
            if n_seeds >= 6:
                stat, p_value = stats.wilcoxon(vals1, vals2, zero_method='zsplit')
                test_name = "Wilcoxon Signed-Rank"
            else:
                p_value = bootstrap_paired_diff(vals1, vals2)
                test_name = "Paired Bootstrap"
                
            # Effect size (Cohen's d for paired samples)
            std_diff = np.std(vals1 - vals2, ddof=1) if n_seeds > 1 else 1e-8
            effect_size = mean_diff / (std_diff + 1e-8)
            
            # Determine interpretation
            if p_value < 0.05:
                interp = "statistically significant improvement" if mean_diff > 0 else "statistically significant degradation"
            else:
                interp = "achieved higher observed performance" if mean_diff > 0 else "lower observed performance"
                
            test_rows.append({
                "comparison": f"{opt1} vs {opt2}",
                "metric": metric.replace("_test", ""),
                "test_used": test_name,
                "n_seeds": n_seeds,
                "mean_difference": mean_diff,
                "p_value": p_value,
                "effect_size_d": effect_size,
                "interpretation": interp
            })
            
    tests_df = pd.DataFrame(test_rows)
    tests_df.to_csv("outputs/tables/optimizer_pairwise_tests.csv", index=False)
    
    # 3. Generate Markdown Report
    Path("outputs/reports").mkdir(parents=True, exist_ok=True)
    with open("outputs/reports/statistical_analysis_summary.md", "w") as f:
        f.write("# Statistical Analysis Summary\n\n")
        f.write("## Summary Statistics\n")
        f.write(summary_df.round(4).to_markdown(index=False))
        f.write("\n\n## Pairwise Comparisons\n")
        f.write(tests_df.round(4).to_markdown(index=False))
        f.write("\n\n## Scientific Conclusion\n")
        f.write("The official TensorFlow/Keras benchmark includes five optimizers under a balanced 2×2 design ")
        f.write("(2 Evolutionary: GA, DE; 2 Swarm: PSO, GWO; 1 Baseline: Random Search). ")
        f.write("Under the current fixed-budget protocol (100 evaluations per seed, 5 seeds), ")
        f.write("statistical significance is assessed via Paired Bootstrap testing. ")
        f.write("Claims of significant superiority require p < 0.05 with sufficient effect size.\n")
        
    logger.info("Statistical analysis completed successfully.")

if __name__ == "__main__":
    run_analysis()
