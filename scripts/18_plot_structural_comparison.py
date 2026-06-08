"""Plot comparison of structural combinations for the preliminary benchmark."""

import json
import logging
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    root_dir = Path("outputs/structural_benchmark")
    if not root_dir.exists():
        logging.error(f"Directory {root_dir} does not exist. Run 17_run_structural_benchmark.py first.")
        return
        
    results = []
    
    for combination_dir in root_dir.iterdir():
        if not combination_dir.is_dir() or combination_dir.name == "figures":
            continue
            
        combo_name = combination_dir.name
        
        for model in ["mlp", "cnn"]:
            metrics_file = combination_dir / "metrics" / f"{model}_random_search_best_by_seed.csv"
            
            if metrics_file.exists():
                df = pd.read_csv(metrics_file)
                for _, row in df.iterrows():
                    results.append({
                        "Model": model.upper(),
                        "Structure": combo_name.replace("_", " + ").upper(),
                        "Validation Fitness": float(row["best_validation_fitness"])
                    })
                
    if not results:
        logging.error("No valid results found to plot.")
        return
        
    df_results = pd.DataFrame(results)
    
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
    plt.figure(figsize=(10, 6))
    
    # Barplot with error bars across the seeds
    sns.barplot(data=df_results, x="Structure", y="Validation Fitness", hue="Model", palette="viridis", errorbar="sd", capsize=0.1)
    
    # Add stripplot for individual points, using dodge to align with hue
    sns.stripplot(data=df_results, x="Structure", y="Validation Fitness", hue="Model", dodge=True, color="black", alpha=0.5, jitter=True, legend=False)
    
    plt.title("Preliminary Structural Benchmark (Validation Fitness)")
    plt.ylabel("Validation Fitness (MCC + F1)")
    plt.xlabel("Internal Architecture (Optimizer + Activation)")
    
    out_dir = root_dir / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "structural_comparison.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    
    logging.info(f"Plot saved to {out_path}")

if __name__ == "__main__":
    main()
