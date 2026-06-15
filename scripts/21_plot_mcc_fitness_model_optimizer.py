"""Plot MCC/F1 fitness benchmark performance by model and optimizer."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
METRICS_DIR = ROOT / "outputs" / "article_official" / "metrics"
OUT_DIR = ROOT / "outputs" / "comparative_analysis"

MODELS = ["mlp", "rf", "svm", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]
OPTIMIZER_LABELS = {
    "random_search": "Random Search",
    "ga": "GA",
    "pso": "PSO",
    "de": "DE",
    "gwo": "GWO",
}


def load_mcc_fitness_results() -> pd.DataFrame:
    frames = []
    for model in MODELS:
        for optimizer in OPTIMIZERS:
            path = METRICS_DIR / f"{model}_{optimizer}_best_by_seed.csv"
            if not path.exists():
                print(f"Missing file: {path.relative_to(ROOT)}")
                continue

            df = pd.read_csv(path)
            df = df[df["seed"].isin([1, 2, 3])].copy()
            df["model_label"] = model.upper()
            df["optimizer_label"] = OPTIMIZER_LABELS[optimizer]
            frames.append(df)

    if not frames:
        raise SystemExit("No MCC/F1 benchmark files found.")
    return pd.concat(frames, ignore_index=True)


def plot_metric(df: pd.DataFrame, metric: str, ylabel: str, stem: str) -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.15)
    fig, ax = plt.subplots(figsize=(12, 6.5))

    model_order = [model.upper() for model in MODELS]
    optimizer_order = [OPTIMIZER_LABELS[optimizer] for optimizer in OPTIMIZERS]
    colors = sns.color_palette("tab10", n_colors=len(optimizer_order))
    summary = (
        df.groupby(["model_label", "optimizer_label"])[metric]
        .agg(mean="mean", std="std", n="count")
        .reset_index()
    )
    summary["sem"] = summary["std"] / np.sqrt(summary["n"])

    x = np.arange(len(model_order))
    width = 0.15
    offsets = (np.arange(len(optimizer_order)) - (len(optimizer_order) - 1) / 2) * width

    for opt_idx, optimizer in enumerate(optimizer_order):
        means = []
        sems = []
        seed_points = []
        for model in model_order:
            row = summary[(summary["model_label"] == model) & (summary["optimizer_label"] == optimizer)]
            means.append(float(row["mean"].iloc[0]))
            sems.append(float(row["sem"].iloc[0]))
            values = df[(df["model_label"] == model) & (df["optimizer_label"] == optimizer)][metric].to_numpy()
            seed_points.append(values)

        positions = x + offsets[opt_idx]
        ax.bar(
            positions,
            means,
            width,
            yerr=sems,
            capsize=3,
            color=colors[opt_idx],
            edgecolor="white",
            linewidth=0.7,
            label=optimizer,
            error_kw={"elinewidth": 1.6, "capthick": 1.6, "alpha": 0.85},
        )
        for pos, values in zip(positions, seed_points):
            jitter = np.linspace(-width * 0.22, width * 0.22, len(values))
            ax.scatter(pos + jitter, values, s=13, color="#222222", alpha=0.72, zorder=4)

    ax.set_title(f"MCC/F1 fitness benchmark - {ylabel} by model and optimizer")
    ax.set_xlabel("Model")
    ax.set_ylabel(ylabel)
    ax.set_xticks(x)
    ax.set_xticklabels(model_order)
    ax.grid(axis="y", alpha=0.35)
    ax.text(
        0.5,
        -0.22,
        "Barras = media das seeds 1, 2 e 3; hastes = erro padrao da media (DP/sqrt(n)); pontos = seeds individuais.",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=9.5,
        color="#555555",
    )
    ax.legend(title="Optimizer", frameon=False, ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.12))
    fig.tight_layout(rect=(0, 0.04, 1, 1))

    outputs = [OUT_DIR / f"{stem}.png", OUT_DIR / f"{stem}.pdf"]
    for path in outputs:
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return outputs


def main() -> None:
    df = load_mcc_fitness_results()
    summary = (
        df.groupby(["model_label", "optimizer_label"])[["mcc_test", "accuracy_test"]]
        .agg(["mean", "std"])
        .reset_index()
    )
    summary.columns = ["_".join(col).rstrip("_") for col in summary.columns]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = OUT_DIR / "mcc_fitness_model_optimizer_summary.csv"
    summary.to_csv(summary_path, index=False)

    paths = [summary_path]
    paths.extend(plot_metric(df, "mcc_test", "MCC on X_test", "mcc_fitness_mcc_test_by_model_optimizer"))
    paths.extend(
        plot_metric(
            df,
            "accuracy_test",
            "Accuracy on X_test",
            "mcc_fitness_accuracy_test_by_model_optimizer",
        )
    )

    print("Saved MCC/F1 fitness plots:")
    for path in paths:
        print(f"- {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
