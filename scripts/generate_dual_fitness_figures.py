"""Build audited, publication-ready figures for the two-fitness comparison.

Only paired seeds 1--3 that are present for every model/optimizer cell in
both holdout protocols are used.  The output is deliberately descriptive:
three seeds per cell are not represented as confirmatory hypothesis tests.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "article" / "manuscript" / "figures"
SEEDS = [1, 2, 3]
MODELS = ["mlp", "rf", "svm", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]
MODELS_LABEL = {"mlp": "MLP", "rf": "RF", "svm": "SVM", "cnn": "1D-CNN"}
OPT_LABELS = {"random_search": "RS", "ga": "GA", "pso": "PSO", "de": "DE", "gwo": "GWO"}

INK = "#1F2933"
GRID = "#D9E2EC"
MCC_MODE = "#2166AC"
ACC_MODE = "#D97706"
MODEL_COLORS = {"mlp": "#0072B2", "rf": "#009E73", "svm": "#8E6BBE", "cnn": "#C65D7B"}
OPT_COLORS = {"random_search": "#6B7280", "ga": "#0072B2", "pso": "#E69F00", "de": "#009E73", "gwo": "#8E6BBE"}
PROTOCOLS = {
    "MCC/F1 fitness": ROOT / "outputs" / "article_official" / "metrics",
    "Accuracy fitness": ROOT / "outputs" / "article_official_accuracy_holdout" / "metrics",
}


def style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 8.5, "axes.labelsize": 8.5,
        "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7,
        "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.facecolor": "white",
    })


def save(fig: plt.Figure, name: str) -> None:
    fig.savefig(FIGURES / name, format="pdf", bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)


def load_records() -> pd.DataFrame:
    rows = []
    for protocol, directory in PROTOCOLS.items():
        for model in MODELS:
            for optimizer in OPTIMIZERS:
                path = directory / f"{model}_{optimizer}_best_by_seed.csv"
                frame = pd.read_csv(path)
                available = sorted(frame["seed"].unique().tolist())
                if not set(SEEDS).issubset(available):
                    raise RuntimeError(f"Missing paired seeds in {path}: {available}")
                part = frame[frame["seed"].isin(SEEDS)].copy()
                part["protocol"] = protocol
                part["model"] = model
                part["optimizer"] = optimizer
                rows.append(part)
    return pd.concat(rows, ignore_index=True)


def box(ax, xy, w, h, title, text, color) -> None:
    x, y = xy
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.018,rounding_size=0.06",
                                facecolor=color, edgecolor=INK, linewidth=0.8))
    ax.text(x + w / 2, y + h * 0.69, title, ha="center", va="center", color="white", weight="bold", fontsize=8.5)
    ax.text(x + w / 2, y + h * 0.30, text, ha="center", va="center", color="white", fontsize=7.1, linespacing=1.2)


def arrow(ax, start, end) -> None:
    ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "-|>", "color": INK, "lw": 1.0})


def dual_protocol_overview() -> None:
    fig, ax = plt.subplots(figsize=(6.1, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    box(ax, (1.0, 8.55), 8.0, 0.95, "Shared data and features", "WIN 5-minute futures | 15,057 bars | Information Gain: 7 features", "#2F6690")
    box(ax, (1.0, 7.05), 8.0, 0.95, "Shared temporal protocol", "60% training | 20% validation | 20% locked test | no shuffling", "#52616B")
    box(ax, (1.0, 5.55), 8.0, 0.95, "Shared search control", "RS, GA, PSO, DE, GWO | four backbones | 1,500 evaluations per seed", "#8A6D3B")
    box(ax, (0.55, 3.55), 4.0, 1.10, "Protocol A: MCC/F1 fitness", "Validation objective\n0.60 MCC + 0.40 F1", MCC_MODE)
    box(ax, (5.45, 3.55), 4.0, 1.10, "Protocol B: accuracy fitness", "Validation objective\nAccuracy", ACC_MODE)
    box(ax, (1.0, 1.20), 8.0, 1.05, "Common locked evaluation", "Test MCC, F1, and accuracy reported after selection\nNo test-set feedback during search", "#A23E48")
    arrow(ax, (5.0, 8.55), (5.0, 8.00))
    arrow(ax, (5.0, 7.05), (5.0, 6.50))
    arrow(ax, (3.3, 5.55), (2.65, 4.65))
    arrow(ax, (6.7, 5.55), (7.35, 4.65))
    arrow(ax, (2.55, 3.55), (4.0, 2.25))
    arrow(ax, (7.45, 3.55), (6.0, 2.25))
    ax.text(0.15, 5.9, "CONTROLLED\nCONDITIONS", rotation=90, ha="center", va="center", fontsize=7, weight="bold", color="#52616B")
    ax.text(9.85, 3.95, "OBJECTIVE\nVARIES", rotation=90, ha="center", va="center", fontsize=7, weight="bold", color="#52616B")
    save(fig, "dual_fitness_protocol_overview.pdf")


def temporal_split() -> None:
    fig, ax = plt.subplots(figsize=(5.8, 2.8))
    total = 15057
    segments = [(0, 9034, "#3B82A0", "Training", "60% | 9,034 bars", "Model fitting"),
                (9034, 3011, "#D69E2E", "Validation", "20% | 3,011 bars", "Fitness evaluation"),
                (12045, 3012, "#B95454", "Locked test", "20% | 3,012 bars", "Final reporting")]
    for start, width, color, title, count, role in segments:
        ax.add_patch(Rectangle((start, 0.58), width, 0.36, facecolor=color, edgecolor="white", linewidth=1.3))
        ax.text(start + width / 2, 0.76, title, ha="center", va="center", color="white", weight="bold", fontsize=7.3)
        ax.text(start + width / 2, 0.25, count.replace(" | ", "\n"), ha="center", va="center", color=INK, weight="bold", fontsize=7)
        ax.text(start + width / 2, 0.04, role, ha="center", va="center", color="#52616B", fontsize=6.5)
    for x in (9034, 12045):
        ax.axvline(x, ymin=0.42, ymax=0.93, color=INK, lw=0.7, ls=(0, (3, 3)))
    ax.annotate("chronological order", xy=(total, 1.17), xytext=(0, 1.17), ha="center", va="center", fontsize=8, weight="bold", color=INK,
                arrowprops={"arrowstyle": "-|>", "lw": 0.9, "color": INK})
    ax.text(13551, 1.00, "Never used for\nfitness selection", ha="center", va="bottom", fontsize=7.1, color="#B95454", weight="bold")
    ax.set(xlim=(0, total), ylim=(-0.15, 1.38), yticks=[])
    ax.set_xticks([0, 3000, 6000, 9034, 12045, 15057])
    ax.set_xlabel("Chronological 5-minute bar index (N = 15,057)", weight="bold")
    for spine in ax.spines.values(): spine.set_visible(False)
    save(fig, "dual_fitness_temporal_split.pdf")


def paired_outcomes(records: pd.DataFrame) -> None:
    means = records.groupby(["protocol", "model", "optimizer"], as_index=False)[["accuracy_test", "mcc_test"]].mean()
    fig, axes = plt.subplots(1, 2, figsize=(6.25, 4.6), gridspec_kw={"wspace": 0.36})
    for ax, metric, title, fmt in zip(axes, ["accuracy_test", "mcc_test"], ["Test accuracy", "Test MCC"], [".3f", ".3f"]):
        wide = means.pivot(index=["model", "optimizer"], columns="protocol", values=metric)
        for (model, optimizer), values in wide.iterrows():
            ax.plot([0, 1], values[["MCC/F1 fitness", "Accuracy fitness"]], color="#BAC5D1", lw=0.8, zorder=1)
            marker = {"random_search": "o", "ga": "s", "pso": "^", "de": "D", "gwo": "P"}[optimizer]
            ax.scatter(0, values["MCC/F1 fitness"], s=28, color=MODEL_COLORS[model], marker=marker, edgecolor="white", linewidth=0.45, zorder=2)
            ax.scatter(1, values["Accuracy fitness"], s=28, color=MODEL_COLORS[model], marker=marker, edgecolor="white", linewidth=0.45, zorder=2)
        aggregate = means.groupby("protocol")[metric].mean()
        ax.hlines(aggregate["MCC/F1 fitness"], -0.12, 0.12, color=MCC_MODE, lw=2.0)
        ax.hlines(aggregate["Accuracy fitness"], 0.88, 1.12, color=ACC_MODE, lw=2.0)
        ax.text(-0.15, aggregate["MCC/F1 fitness"], f"{aggregate['MCC/F1 fitness']:{fmt}}", ha="right", va="center", fontsize=7, color=MCC_MODE, weight="bold")
        ax.text(1.15, aggregate["Accuracy fitness"], f"{aggregate['Accuracy fitness']:{fmt}}", ha="left", va="center", fontsize=7, color=ACC_MODE, weight="bold")
        ax.set_title(title, weight="bold", pad=8)
        ax.set_xticks([0, 1], ["MCC/F1\nfitness", "Accuracy\nfitness"])
        ax.grid(axis="y", color=GRID, lw=0.8)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Held-out test score", weight="bold")
    handles = [Line2D([0], [0], marker="o", color="none", label=MODELS_LABEL[m], markerfacecolor=MODEL_COLORS[m], markeredgecolor="white", markersize=6) for m in MODELS]
    fig.legend(handles=handles, title="Backbone colour", loc="lower center", bbox_to_anchor=(0.5, -0.02), ncol=4, frameon=False)
    save(fig, "dual_fitness_paired_outcomes.pdf")


def delta_heatmaps(records: pd.DataFrame) -> None:
    means = records.groupby(["protocol", "model", "optimizer"], as_index=False)[["accuracy_test", "mcc_test"]].mean()
    fig, axes = plt.subplots(1, 2, figsize=(6.3, 3.45), gridspec_kw={"wspace": 0.42})
    maps = [("accuracy_test", "Delta test accuracy (percentage points)", 100), ("mcc_test", "Delta test MCC", 1)]
    for ax, (metric, title, scale) in zip(axes, maps):
        wide = means.pivot(index=["model", "optimizer"], columns="protocol", values=metric)
        delta = (wide["Accuracy fitness"] - wide["MCC/F1 fitness"]).mul(scale).unstack("optimizer").reindex(index=MODELS, columns=OPTIMIZERS)
        limit = max(abs(delta.to_numpy()).max(), 0.01)
        im = ax.imshow(delta, cmap="RdBu_r", norm=TwoSlopeNorm(vcenter=0, vmin=-limit, vmax=limit), aspect="auto")
        for i in range(len(MODELS)):
            for j in range(len(OPTIMIZERS)):
                value = delta.iloc[i, j]
                ax.text(j, i, f"{value:+.1f}" if scale == 100 else f"{value:+.3f}", ha="center", va="center", fontsize=6.7,
                        color="white" if abs(value) > limit * 0.55 else INK, weight="bold")
        ax.set_title(title, weight="bold", fontsize=8.4, pad=7)
        ax.set_xticks(range(len(OPTIMIZERS)), [OPT_LABELS[x] for x in OPTIMIZERS])
        ax.set_yticks(range(len(MODELS)), [MODELS_LABEL[x] for x in MODELS])
        ax.tick_params(length=0)
        for spine in ax.spines.values(): spine.set_visible(False)
        bar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        bar.ax.tick_params(labelsize=6.5)
    fig.text(0.5, 0.01, "Delta = accuracy-fitness protocol minus MCC/F1-fitness protocol; positive values favour accuracy fitness.", ha="center", fontsize=7, color="#52616B")
    save(fig, "dual_fitness_delta_heatmaps.pdf")


def convergence() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(6.25, 3.2), gridspec_kw={"wspace": 0.32})
    settings = [("MCC/F1 fitness", "Composite validation fitness (0.60 MCC + 0.40 F1)", MCC_MODE),
                ("Accuracy fitness", "Validation accuracy", ACC_MODE)]
    for ax, (protocol, ylabel, accent) in zip(axes, settings):
        directory = PROTOCOLS[protocol] / "convergence"
        for optimizer in OPTIMIZERS:
            frame = pd.read_csv(directory / f"mlp_{optimizer}_convergence.csv")
            frame = frame[frame["seed"].isin(SEEDS)]
            grouped = frame.groupby("evaluation_id")["best_fitness_so_far"]
            mean, sd = grouped.mean(), grouped.std(ddof=1).fillna(0)
            x = mean.index.to_numpy()
            ax.plot(x, mean.to_numpy(), color=OPT_COLORS[optimizer], lw=1.35, label=OPT_LABELS[optimizer])
            ax.fill_between(x, (mean - sd).to_numpy(), (mean + sd).to_numpy(), color=OPT_COLORS[optimizer], alpha=0.10, linewidth=0)
        ax.set_title(protocol, weight="bold", color=accent, pad=7)
        ax.set_xlabel("Evaluation step (N_eval)", weight="bold")
        ax.set_ylabel(ylabel, weight="bold")
        ax.set_xlim(1, 1500)
        ax.grid(color=GRID, lw=0.8)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[1].legend(loc="lower right", frameon=True, edgecolor=GRID)
    save(fig, "dual_fitness_convergence.pdf")


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    style()
    records = load_records()
    dual_protocol_overview()
    temporal_split()
    paired_outcomes(records)
    delta_heatmaps(records)
    convergence()
    print("Generated audited dual-fitness figures in", FIGURES)


if __name__ == "__main__":
    main()
