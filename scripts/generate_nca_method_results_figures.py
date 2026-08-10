"""Generate publication-ready vector figures for the methodology-results extract.

The performance and inferential values are transcribed from the currently
reported manuscript tables.  They are visual summaries only: they do not
recompute statistical tests or fabricate seed-level observations.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "article" / "manuscript" / "figures"

# Color-blind-safe, print-friendly palette.  Optimizer colours remain stable
# across every results figure.
INK = "#1F2933"
GRID = "#D9E2EC"
GA = "#0072B2"
DE = "#009E73"
PSO = "#E69F00"
GWO = "#8E6BBE"
RS = "#6B7280"
TRAIN = "#3B82A0"
VALIDATION = "#D69E2E"
TEST = "#B95454"


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.facecolor": "white",
        }
    )


def save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(FIGURES / filename, format="pdf", bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)


def rounded_box(ax, xy, width, height, title, subtitle, color) -> None:
    x, y = xy
    patch = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.018,rounding_size=0.06",
        facecolor=color,
        edgecolor=INK,
        linewidth=0.8,
    )
    ax.add_patch(patch)
    ax.text(x + width / 2, y + height * 0.73, title, ha="center", va="center", color="white", weight="bold", fontsize=9)
    ax.text(x + width / 2, y + height * 0.32, subtitle, ha="center", va="center", color="white", fontsize=7.5, linespacing=1.25)


def arrow(ax, start, end) -> None:
    ax.annotate(
        "", xy=end, xytext=start,
        arrowprops={"arrowstyle": "-|>", "color": INK, "lw": 1.0, "shrinkA": 0, "shrinkB": 0},
    )


def workflow_overview() -> None:
    # Match the printable manuscript width so embedded typography remains
    # at journal-readable size after LaTeX placement.
    fig, ax = plt.subplots(figsize=(5.8, 5.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    stages = [
        ("Data acquisition", "5-minute WIN futures\nN = 15,057 bars", "#2F6690"),
        ("Feature representation", "Technical indicators\nInformation Gain: 7 features", "#2A7F78"),
        ("Chronological protocol", "60% train | 20% validation | 20% test\nNo shuffling", "#52616B"),
        ("Equal-budget search", "1,500 evaluations per seed\nRS, GA, PSO, DE, GWO", "#8A6D3B"),
        ("Validation selection", "Candidate ranking on validation data\n0.60 MCC + 0.40 F1", "#6A5C9E"),
        ("Locked evaluation", "Held-out test: MCC and accuracy\nStatistical and financial assessment", "#A23E48"),
    ]
    box_height = 1.15
    y_positions = [8.55, 7.00, 5.45, 3.90, 2.35, 0.80]
    for (title, subtitle, color), y in zip(stages, y_positions):
        rounded_box(ax, (1.1, y), 7.8, box_height, title, subtitle, color)
    for current_y, next_y in zip(y_positions, y_positions[1:]):
        arrow(ax, (5.0, current_y), (5.0, next_y + box_height))

    ax.text(0.15, 5.2, "DATA\nPREPARATION", rotation=90, ha="center", va="center", fontsize=7, weight="bold", color="#52616B")
    ax.text(9.84, 3.0, "MODEL\nSELECTION", rotation=90, ha="center", va="center", fontsize=7, weight="bold", color="#52616B")
    save(fig, "methodology_overview.pdf")


def temporal_split() -> None:
    fig, ax = plt.subplots(figsize=(5.8, 2.8))
    total = 15057
    segments = [
        (0, 9034, TRAIN, "Training set", "60% | 9,034 bars", "Model fitting"),
        (9034, 3011, VALIDATION, "Validation set", "20% | 3,011 bars", "Selection"),
        (12045, 3012, TEST, "Locked test set", "20% | 3,012 bars", "Held-out test"),
    ]
    for start, width, color, title, count, purpose in segments:
        ax.add_patch(Rectangle((start, 0.58), width, 0.36, facecolor=color, edgecolor="white", linewidth=1.3))
        display_title = "Test set" if title == "Locked test set" else title
        ax.text(start + width / 2, 0.76, display_title, ha="center", va="center", color="white", weight="bold", fontsize=7.2)
        ax.text(start + width / 2, 0.25, count.replace(" | ", "\n"), ha="center", va="center", color=INK, weight="bold", fontsize=7.0, linespacing=1.15)
        ax.text(start + width / 2, 0.04, purpose, ha="center", va="center", color="#52616B", fontsize=6.5)

    for x in (9034, 12045):
        ax.axvline(x, ymin=0.42, ymax=0.93, color=INK, lw=0.7, ls=(0, (3, 3)))
    ax.annotate("chronological order", xy=(total, 1.17), xytext=(0, 1.17), ha="center", va="center", fontsize=8, weight="bold", color=INK,
                arrowprops={"arrowstyle": "-|>", "lw": 0.9, "color": INK})
    ax.text(13551, 1.00, "Never used for\nmodel selection", ha="center", va="bottom", fontsize=7.2, color=TEST, weight="bold")

    ax.set_xlim(0, total)
    ax.set_ylim(-0.15, 1.38)
    ax.set_xticks([0, 3000, 6000, 9034, 12045, 15057])
    ax.set_xlabel("Chronological 5-minute bar index (N = 15,057)", weight="bold")
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "temporal_split.pdf")


def metric_plot(filename: str, ylabel: str, values: list[float], errors: list[float], fmt: str, xlim: tuple[float, float]) -> None:
    labels = ["Random search", "GWO", "PSO", "DE", "GA"]
    colors = [RS, GWO, PSO, DE, GA]
    y = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(6.0, 3.5))
    ax.errorbar(values, y, xerr=errors, fmt="none", ecolor="#9AA5B1", elinewidth=1.5, capsize=3, zorder=1)
    ax.scatter(values, y, c=colors, s=56, zorder=2, edgecolors="white", linewidths=0.8)
    for yy, value, error in zip(y, values, errors):
        ax.text(xlim[1] - (xlim[1] - xlim[0]) * 0.01, yy, f"{value:{fmt}} +/- {error:{fmt}}", ha="right", va="center", fontsize=8, color=INK)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(*xlim)
    ax.set_xlabel(ylabel + " (mean +/- SD)", weight="bold")
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    save(fig, filename)


def statistical_evidence() -> None:
    # Values are the reported Holm-adjusted Wilcoxon results in Table 2.
    # Keep the complete comparison set visible in the compact manuscript rather
    # than compressing it into a narrow, hard-to-read table.
    labels = [
        "GA vs RS", "DE vs RS", "PSO vs RS", "GWO vs RS",
        "GA vs GWO", "PSO vs GWO", "DE vs GWO",
        "GA vs PSO", "GA vs DE", "PSO vs DE",
    ]
    effects = np.array([1.241, 1.182, 1.105, 0.742, 0.815, 0.621, 0.667, 0.261, 0.115, 0.132])
    p_values = np.array([0.0021, 0.0032, 0.0045, 0.0215, 0.0142, 0.0380, 0.0285, 0.1360, 0.4520, 0.5200])
    colors = [GA, DE, PSO, GWO, GA, PSO, DE, GA, GA, PSO]
    y = np.arange(len(labels))
    fig, axes = plt.subplots(1, 2, figsize=(6.0, 5.15), sharey=True, gridspec_kw={"wspace": 0.18})

    axes[0].barh(y, effects, color=colors, height=0.52)
    axes[0].axvline(0.8, color="#52616B", lw=0.9, ls=(0, (3, 3)))
    axes[0].set_xlabel("Standardized effect (Cohen's d)", weight="bold")
    axes[0].set_yticks(y, labels)
    axes[0].invert_yaxis()
    axes[0].set_xlim(0, 1.45)
    axes[0].grid(axis="x", color=GRID, linewidth=0.8)

    evidence = -np.log10(p_values)
    axes[1].barh(y, evidence, color=colors, height=0.52)
    axes[1].axvline(-np.log10(0.05), color="#52616B", lw=0.9, ls=(0, (3, 3)))
    axes[1].set_xlabel("-log10(Holm-adjusted p-value)", weight="bold")
    axes[1].grid(axis="x", color=GRID, linewidth=0.8)
    for ax in axes:
        ax.axhline(3.5, color=GRID, lw=1.0)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="y", length=0)
        ax.set_axisbelow(True)
    save(fig, "statistical_evidence_mcc.pdf")


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    setup_style()
    workflow_overview()
    temporal_split()
    metric_plot("mcc_performance.pdf", "Matthews correlation coefficient (MCC)", [0.185, 0.208, 0.225, 0.228, 0.231], [0.021, 0.016, 0.011, 0.014, 0.012], ".3f", (0.155, 0.270))
    metric_plot("accuracy_performance.pdf", "Accuracy (%)", [58.12, 59.85, 60.98, 61.20, 61.45], [1.45, 1.12, 0.88, 0.95, 0.92], ".2f", (55.0, 65.0))
    statistical_evidence()
    print(f"Generated vector figures in {FIGURES}")


if __name__ == "__main__":
    main()
