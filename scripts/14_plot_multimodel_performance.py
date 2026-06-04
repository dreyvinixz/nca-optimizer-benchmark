"""Plot multi-model performance comparison."""

import logging
import warnings
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=UserWarning)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("multimodel_plot")

def main():
    models = ["mlp", "svm", "rf", "cnn"]
    optimizers = ["random_search", "ga", "pso", "de", "gwo"]
    
    # Load all best_by_seed files
    data_frames = []
    for model in models:
        for opt in optimizers:
            path = Path(f"outputs/phase2/metrics/{model}_{opt}_best_by_seed.csv")
            if path.exists():
                df = pd.read_csv(path)
                df["Model"] = model.upper()
                df["Optimizer"] = opt.upper().replace("_", " ")
                data_frames.append(df)
                
    if not data_frames:
        logger.error("No data found to plot. Run the benchmark first.")
        return
        
    full_df = pd.concat(data_frames, ignore_index=True)
    
    # Set beautiful style
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
    
    # Plot MCC boxplot
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    if "mcc_test" in full_df.columns:
        sns.boxplot(
            data=full_df, 
            x="Model", 
            y="mcc_test", 
            hue="Optimizer", 
            ax=axes[0],
            palette="viridis"
        )
        axes[0].set_title("Matthews Correlation Coefficient (MCC) on Test Set")
        axes[0].set_ylabel("MCC Score")
        axes[0].set_xlabel("Model Architecture")
    
    if "f1_test" in full_df.columns:
        sns.boxplot(
            data=full_df, 
            x="Model", 
            y="f1_test", 
            hue="Optimizer", 
            ax=axes[1],
            palette="viridis"
        )
        axes[1].set_title("F1-Score on Test Set")
        axes[1].set_ylabel("F1 Score")
        axes[1].set_xlabel("Model Architecture")
    
    plt.tight_layout()
    
    out_dir = Path("outputs/phase2/figures")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "multimodel_performance_comparison.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    logger.info(f"Saved performance comparison to {out_path}")
    
    # Also plot convergence
    convergence_dfs = []
    for model in models:
        for opt in optimizers:
            path = Path(f"outputs/phase2/metrics/convergence/{model}_{opt}_convergence.csv")
            if path.exists():
                df = pd.read_csv(path)
                # Keep only seed 1 for a cleaner convergence plot
                df = df[df["seed"] == 1]
                df["Model"] = model.upper()
                df["Optimizer"] = opt.upper().replace("_", " ")
                convergence_dfs.append(df)
                
    if convergence_dfs:
        conv_df = pd.concat(convergence_dfs, ignore_index=True)
        fig2 = plt.figure(figsize=(10, 6))
        sns.lineplot(
            data=conv_df,
            x="evaluation_id",
            y="best_fitness_so_far",
            hue="Optimizer",
            style="Model",
            palette="viridis",
            linewidth=2
        )
        plt.title("Convergence Trajectory (Seed 1) - Best Fitness So Far")
        plt.xlabel("Evaluations (Budget)")
        plt.ylabel("Fitness (0.6 MCC + 0.4 F1)")
        plt.tight_layout()
        conv_path = out_dir / "multimodel_convergence.png"
        plt.savefig(conv_path, dpi=300, bbox_inches="tight")
        logger.info(f"Saved convergence plot to {conv_path}")

if __name__ == "__main__":
    main()
