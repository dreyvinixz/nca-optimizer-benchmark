"""Create restrained, IJCNN-style figures for the reconstructed NCA article.

The figures use the same visual logic as the precursor: a process overview,
model-specific optimisation trajectories, and compact comparative summaries.
All reported runs use the three seeds common to both temporal holdout protocols.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "article" / "manuscript" / "figures"
SEEDS = [1, 2, 3]
MODELS = ["rf", "svm", "mlp", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]
MODEL_LABELS = {"rf": "Random Forest", "svm": "SVM", "mlp": "MLP", "cnn": "1D-CNN"}
SHORT_MODELS = {"rf": "RF", "svm": "SVM", "mlp": "MLP", "cnn": "1D-CNN"}
OPT_LABELS = {"random_search": "RS", "ga": "GA", "pso": "PSO", "de": "DE", "gwo": "GWO"}
OPT_COLORS = {
    "random_search": "#222222", "ga": "#2B6CB0", "pso": "#4A5568",
    "de": "#718096", "gwo": "#A0AEC0",
}
GRID = "#D8DEE6"
INK = "#1A202C"
PROTOCOLS = {
    "MCC/F1 fitness": ROOT / "outputs" / "article_official" / "metrics",
    "Accuracy fitness": ROOT / "outputs" / "article_official_accuracy_holdout" / "metrics",
}
ECONOMIC = ROOT / "outputs" / "professor_presentation" / "statistical_economic_model_selection" / "economic_by_model_experiment.csv"


def style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 8.2, "axes.labelsize": 8.2,
        "xtick.labelsize": 7.4, "ytick.labelsize": 7.4, "legend.fontsize": 7.0,
        "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.facecolor": "white",
    })


def save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(FIGURES / filename, format="pdf", bbox_inches="tight", pad_inches=0.035)
    plt.close(fig)


def read_best_records() -> pd.DataFrame:
    frames = []
    for protocol, directory in PROTOCOLS.items():
        for model in MODELS:
            for optimizer in OPTIMIZERS:
                csv_path = directory / f"{model}_{optimizer}_best_by_seed.csv"
                frame = pd.read_csv(csv_path)
                frame = frame[frame["seed"].isin(SEEDS)].copy()
                if frame["seed"].nunique() != len(SEEDS):
                    raise RuntimeError(f"Missing common seed in {csv_path}")
                frame["protocol"] = protocol
                frame["model"] = model
                frame["optimizer"] = optimizer
                frames.append(frame)
    return pd.concat(frames, ignore_index=True)


def box(ax, x: float, y: float, width: float, height: float, title: str, detail: str, fill: str = "#F7FAFC") -> None:
    patch = FancyBboxPatch(
        (x, y), width, height, boxstyle="round,pad=0.018,rounding_size=0.045",
        linewidth=0.95, edgecolor=INK, facecolor=fill,
    )
    ax.add_patch(patch)
    ax.text(x + width / 2, y + height * 0.63, title, ha="center", va="center", weight="bold", color=INK, fontsize=8.3)
    ax.text(x + width / 2, y + height * 0.31, detail, ha="center", va="center", color="#4A5568", fontsize=6.75, linespacing=1.2)


def arrow(ax, start: tuple[float, float], end: tuple[float, float]) -> None:
    ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "-|>", "lw": 1.0, "color": INK})


def workflow() -> None:
    fig, ax = plt.subplots(figsize=(7.05, 3.55))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.4)
    ax.axis("off")
    box(ax, 0.45, 4.35, 3.15, 1.05, "Input data", "WIN five-minute futures\nN = 15,057")
    box(ax, 4.43, 4.35, 3.15, 1.05, "Technical indicators", "66 price, moving-average,\nand volatility descriptors")
    box(ax, 8.40, 4.35, 3.15, 1.05, "Feature selection", "Information Gain\nseven retained descriptors")
    arrow(ax, (3.60, 4.87), (4.43, 4.87))
    arrow(ax, (7.58, 4.87), (8.40, 4.87))
    box(ax, 0.45, 1.82, 3.15, 1.22, "Locked test", "Predictive metrics and\neconomic backtest", "#E9EFF5")
    box(ax, 4.10, 1.82, 3.15, 1.22, "Model training", "RF | SVM | MLP | CNN\ncommon seeds 1--3", "#EDF2F7")
    box(ax, 7.75, 1.82, 3.80, 1.22, "Search design", "RS | GA | PSO | DE | GWO\n1,000 evaluations per seed\nMCC/F1 fitness or accuracy fitness", "#EDF2F7")
    arrow(ax, (9.98, 4.35), (9.65, 3.04))
    arrow(ax, (7.75, 2.43), (7.25, 2.43))
    arrow(ax, (4.10, 2.43), (3.60, 2.43))
    ax.text(6.0, 6.00, "Controlled workflow for intraday neural optimization", ha="center", va="center", fontsize=9.6, weight="bold", color=INK)
    save(fig, "ijcnn_style_workflow.pdf")


def temporal_partition() -> None:
    fig, ax = plt.subplots(figsize=(6.15, 2.5))
    total = 15057
    segments = [
        (0, 9034, "#4A5568", "Training", "9,034 bars (60%)"),
        (9034, 3011, "#718096", "Validation", "3,011 bars (20%)"),
        (12045, 3012, "#A0AEC0", "Locked test", "3,012 bars (20%)"),
    ]
    for start, width, colour, label, detail in segments:
        ax.add_patch(Rectangle((start, 0.56), width, 0.33, facecolor=colour, edgecolor="white", linewidth=1.2))
        ax.text(start + width / 2, 0.73, label, ha="center", va="center", color="white", weight="bold", fontsize=7.3)
        ax.text(start + width / 2, 0.34, detail, ha="center", va="center", color=INK, fontsize=6.9)
    for boundary in [9034, 12045]:
        ax.axvline(boundary, ymin=0.38, ymax=0.91, color=INK, lw=0.75, ls=(0, (3, 3)))
    ax.annotate("chronological order", xy=(total, 1.13), xytext=(0, 1.13), ha="center", va="center", fontsize=8.3, weight="bold", color=INK, arrowprops={"arrowstyle": "-|>", "lw": 0.9, "color": INK})
    ax.text(13551, 0.97, "not accessed during\nfeature selection or search", ha="center", va="bottom", fontsize=6.8, color=INK, weight="bold")
    ax.set(xlim=(0, total), ylim=(0.0, 1.35), yticks=[])
    ax.set_xticks([0, 3000, 6000, 9034, 12045, 15057])
    ax.set_xlabel("Chronological five-minute bar index", weight="bold")
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "ijcnn_style_partition.pdf")


def model_convergence(model: str) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(6.25, 2.75), gridspec_kw={"wspace": 0.33})
    settings = [
        ("MCC/F1 fitness", r"Best validation fitness: $0.60\,\mathrm{MCC}+0.40\,F_1$"),
        ("Accuracy fitness", r"Best validation fitness: $0.40\,\mathrm{Acc}_{train}+0.60\,\mathrm{Acc}_{val}$"),
    ]
    for ax, (protocol, ylabel) in zip(axes, settings):
        directory = PROTOCOLS[protocol] / "convergence"
        for optimizer in OPTIMIZERS:
            frame = pd.read_csv(directory / f"{model}_{optimizer}_convergence.csv")
            frame = frame[frame["seed"].isin(SEEDS)]
            summary = frame.groupby("evaluation_id")["best_fitness_so_far"].agg(["mean", "std"]).fillna(0.0)
            ax.plot(summary.index, summary["mean"], lw=1.25, color=OPT_COLORS[optimizer], label=OPT_LABELS[optimizer])
            ax.fill_between(summary.index, summary["mean"] - summary["std"], summary["mean"] + summary["std"], color=OPT_COLORS[optimizer], alpha=0.08, linewidth=0)
        ax.set_title(protocol, weight="bold", color=INK, pad=6)
        ax.set_xlabel("Candidate evaluation", weight="bold")
        ax.set_ylabel(ylabel, weight="bold")
        ax.set_xlim(1, 1000)
        ax.grid(color=GRID, lw=0.75)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[1].legend(loc="lower right", frameon=True, edgecolor=GRID, ncol=1)
    fig.suptitle(f"{MODEL_LABELS[model]}: optimisation trajectories", y=1.02, weight="bold", fontsize=9.6)
    save(fig, f"ijcnn_style_{model}_convergence.pdf")


def model_performance(records: pd.DataFrame) -> None:
    summary = records.groupby(["protocol", "model"], as_index=False)[["accuracy_test", "mcc_test"]].mean()
    fig, axes = plt.subplots(1, 2, figsize=(6.25, 3.0), gridspec_kw={"wspace": 0.34})
    protocols = ["MCC/F1 fitness", "Accuracy fitness"]
    colours = ["#4A5568", "#9AA5B1"]
    x = np.arange(len(MODELS))
    for ax, metric, label in zip(axes, ["accuracy_test", "mcc_test"], ["Held-out test accuracy", "Held-out test MCC"]):
        width = 0.35
        for offset, protocol, colour in [(-width / 2, protocols[0], colours[0]), (width / 2, protocols[1], colours[1])]:
            values = summary[summary["protocol"] == protocol].set_index("model").reindex(MODELS)[metric]
            bars = ax.bar(x + offset, values, width=width, color=colour, edgecolor=INK, linewidth=0.45, label=protocol)
            for bar, value in zip(bars, values):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + (0.004 if metric == "accuracy_test" else 0.006), f"{value:.3f}", ha="center", va="bottom", fontsize=6.2, rotation=90)
        ax.set_xticks(x, [SHORT_MODELS[m] for m in MODELS])
        ax.set_ylabel(label, weight="bold")
        ax.grid(axis="y", color=GRID, lw=0.75)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylim(0.52, 0.68)
    axes[1].set_ylim(0.10, 0.34)
    axes[1].legend(loc="lower left", frameon=True, edgecolor=GRID)
    save(fig, "ijcnn_style_model_performance.pdf")


def economic_summary() -> None:
    frame = pd.read_csv(ECONOMIC)
    keep = {"exp1_holdout_mcc_f1": "MCC/F1 fitness", "exp2_holdout_accuracy": "Accuracy fitness"}
    frame = frame[frame["experiment"].isin(keep)].copy()
    frame["protocol"] = frame["experiment"].map(keep)
    fig, axes = plt.subplots(1, 2, figsize=(6.25, 3.05), gridspec_kw={"wspace": 0.44})
    protocols = ["MCC/F1 fitness", "Accuracy fitness"]
    colours = ["#4A5568", "#9AA5B1"]
    x = np.arange(len(MODELS))
    width = 0.35
    for ax, metric, ylabel, scale in [
        (axes[0], "total_profit_mean", "Mean total profit (points)", 1.0),
        (axes[1], "max_drawdown_mean", "Mean maximum drawdown (points)", 1.0),
    ]:
        for offset, protocol, colour in [(-width / 2, protocols[0], colours[0]), (width / 2, protocols[1], colours[1])]:
            values = frame[frame["protocol"] == protocol].set_index("model").reindex(MODELS)[metric] * scale
            ax.bar(x + offset, values, width=width, color=colour, edgecolor=INK, linewidth=0.45, label=protocol)
        ax.axhline(0, color=INK, lw=0.65)
        ax.set_xticks(x, [SHORT_MODELS[m] for m in MODELS])
        ax.set_ylabel(ylabel, weight="bold")
        ax.grid(axis="y", color=GRID, lw=0.75)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_title("Economic result", weight="bold", pad=6)
    axes[1].set_title("Downside risk", weight="bold", pad=6)
    axes[1].legend(loc="lower left", frameon=True, edgecolor=GRID)
    save(fig, "ijcnn_style_economic_summary.pdf")


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    style()
    records = read_best_records()
    workflow()
    temporal_partition()
    for model in MODELS:
        model_convergence(model)
    model_performance(records)
    economic_summary()
    print("Generated IJCNN-style article figures in", FIGURES)


if __name__ == "__main__":
    main()
