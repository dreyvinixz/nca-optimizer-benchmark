"""Generate publication-ready figures from optimizer metrics."""

import logging
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("figures")

# Styling for paper-ready plots
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.titlesize': 18,
    'figure.dpi': 300,
    'font.family': 'serif',
})

# Optimizer metadata
OPTIMIZERS = {
    "random_search": {"label": "Random Search", "color": "#7f8c8d", "marker": "o"},
    "ga": {"label": "GA", "color": "#2980b9", "marker": "s"},
    "de": {"label": "DE", "color": "#8e44ad", "marker": "^"},
    "pso": {"label": "PSO", "color": "#c0392b", "marker": "D"},
    "gwo": {"label": "GWO", "color": "#d35400", "marker": "v"}
}

def load_best_by_seed() -> pd.DataFrame:
    dfs = []
    for opt, meta in OPTIMIZERS.items():
        path = Path(f"outputs/metrics/{opt}_best_by_seed.csv")
        if path.exists():
            df = pd.read_csv(path)
            df['optimizer'] = opt
            df['optimizer_label'] = meta['label']
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

def load_convergence() -> pd.DataFrame:
    dfs = []
    for opt, meta in OPTIMIZERS.items():
        path = Path(f"outputs/metrics/convergence/{opt}_convergence.csv")
        if path.exists():
            df = pd.read_csv(path)
            # Ensure evaluation_id is standard
            df['optimizer_label'] = meta['label']
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

def plot_convergence(df: pd.DataFrame, out_dir: Path):
    if df.empty:
        return
        
    plt.figure(figsize=(10, 6))
    
    # Calculate mean and CI for each evaluation step across seeds
    for opt, meta in OPTIMIZERS.items():
        opt_df = df[df['optimizer'] == opt]
        if opt_df.empty:
            continue
            
        # Group by evaluation_id (up to 100 max)
        grouped = opt_df.groupby('evaluation_id')['best_fitness_so_far'].agg(['mean', 'std', 'count'])
        grouped['ci'] = 1.96 * grouped['std'] / np.sqrt(grouped['count'])
        
        # Plot
        evals = grouped.index.values
        mean_fit = grouped['mean'].values
        ci = grouped['ci'].values
        
        plt.plot(evals, mean_fit, label=meta['label'], color=meta['color'], linewidth=2)
        plt.fill_between(evals, mean_fit - ci, mean_fit + ci, color=meta['color'], alpha=0.15)
        
    plt.title('Convergence Analysis across Optimizers (95% CI)')
    plt.xlabel('Number of Objective Function Evaluations')
    plt.ylabel('Best Fitness So Far (0.6 MCC + 0.4 F1)')
    plt.legend(loc='lower right')
    plt.xlim(0, 100)
    plt.tight_layout()
    
    plt.savefig(out_dir / 'convergence_plot.pdf', format='pdf', bbox_inches='tight')
    plt.savefig(out_dir / 'convergence_plot.png', dpi=300, bbox_inches='tight')
    plt.close()
    logger.info("Saved convergence_plot.pdf")

def plot_boxplots(df: pd.DataFrame, out_dir: Path):
    if df.empty:
        return
        
    metrics = {
        'f1_test': 'F1 Score (Test)',
        'mcc_test': 'MCC (Test)',
        'auc_roc_test': 'AUC-ROC (Test)',
        'best_validation_fitness': 'Validation Fitness'
    }
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    order = [m['label'] for m in OPTIMIZERS.values() if m['label'] in df['optimizer_label'].values]
    palette = {m['label']: m['color'] for m in OPTIMIZERS.values()}
    
    for idx, (metric, title) in enumerate(metrics.items()):
        if metric not in df.columns:
            continue
            
        sns.boxplot(
            data=df, 
            x='optimizer_label', 
            y=metric, 
            order=order,
            palette=palette,
            ax=axes[idx],
            showmeans=True,
            meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":8}
        )
        axes[idx].set_title(title)
        axes[idx].set_xlabel('')
        axes[idx].set_ylabel('Score')
        
    plt.tight_layout()
    plt.savefig(out_dir / 'metrics_boxplots.pdf', format='pdf', bbox_inches='tight')
    plt.savefig(out_dir / 'metrics_boxplots.png', dpi=300, bbox_inches='tight')
    plt.close()
    logger.info("Saved metrics_boxplots.pdf")

def main():
    out_dir = Path("outputs/figures")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    logger.info("Loading metrics...")
    df_best = load_best_by_seed()
    df_conv = load_convergence()
    
    logger.info("Generating Convergence Plot...")
    plot_convergence(df_conv, out_dir)
    
    logger.info("Generating Boxplots...")
    plot_boxplots(df_best, out_dir)
    
    logger.info("Figure generation complete!")

if __name__ == "__main__":
    main()
