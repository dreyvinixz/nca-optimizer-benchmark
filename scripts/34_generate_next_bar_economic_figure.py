"""Regenerate the manuscript economic comparison with next-bar execution."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from nca_figure_style import FIGURE_SINGLE, MODEL_LABELS, apply_publication_style


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "outputs" / "article_next_bar_economic_audit"
FIGURES = ROOT / "article" / "manuscript" / "merged_parallel_working" / "figures"
MODELS = ["rf", "svm", "mlp", "cnn"]
EXPERIMENTS = ["exp1_holdout_mcc_f1", "exp2_holdout_accuracy"]
LABELS = {
    "exp1_holdout_mcc_f1": "MCC/$F_1$ fitness",
    "exp2_holdout_accuracy": "Weighted-accuracy fitness",
}
COLORS = {"exp1_holdout_mcc_f1": "#2166AC", "exp2_holdout_accuracy": "#D97706"}


def main() -> None:
    apply_publication_style()
    FIGURES.mkdir(parents=True, exist_ok=True)
    by_seed = pd.read_csv(AUDIT / "next_bar_summary_by_seed.csv")
    by_model = pd.read_csv(AUDIT / "next_bar_summary_by_model.csv")
    by_seed = by_seed[by_seed["experiment"].isin(EXPERIMENTS)]
    by_model = by_model[by_model["experiment"].isin(EXPERIMENTS)]

    fig, axes = plt.subplots(1, 2, figsize=FIGURE_SINGLE, gridspec_kw={"wspace": 0.48})
    ax = axes[0]
    y = np.arange(len(MODELS))
    for offset, experiment in zip([-0.14, 0.14], EXPERIMENTS):
        part = by_seed[by_seed["experiment"] == experiment]
        means = part.groupby("model")["total_profit_points"].mean().reindex(MODELS)
        stds = part.groupby("model")["total_profit_points"].std().reindex(MODELS)
        for i, model in enumerate(MODELS):
            points = part.loc[part["model"] == model, "total_profit_points"].to_numpy()
            jitter = np.linspace(-0.045, 0.045, len(points))
            ax.scatter(points, np.full(len(points), y[i] + offset) + jitter,
                       color=COLORS[experiment], alpha=0.24, s=9, zorder=1)
        ax.errorbar(means, y + offset, xerr=stds, fmt="o", color=COLORS[experiment],
                    capsize=2.5, lw=1.2, ms=4.6, label=LABELS[experiment], zorder=3)
    ax.axvline(0, color="#52616B", lw=0.7)
    ax.set_yticks(y, [MODEL_LABELS[m] for m in MODELS])
    ax.invert_yaxis()
    ax.set_xlabel("Net profit (points)", weight="bold")
    ax.set_title("Next-bar profit", weight="bold", fontsize=9.5, pad=7)
    ax.grid(axis="x")
    ax.set_axisbelow(True)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)

    ax = axes[1]
    for experiment in EXPERIMENTS:
        part = by_model[by_model["experiment"] == experiment].set_index("model").reindex(MODELS)
        ax.scatter(part["max_drawdown_mean"], part["total_profit_mean"],
                   color=COLORS[experiment], s=43, edgecolors="white", linewidths=0.6,
                   label=LABELS[experiment], zorder=3)
        for model, row in part.iterrows():
            ax.annotate(MODEL_LABELS[model], (row["max_drawdown_mean"], row["total_profit_mean"]),
                        xytext=(4, 4), textcoords="offset points", fontsize=6.5)
    ax.axhline(0, color="#52616B", lw=0.7)
    ax.axvline(0, color="#52616B", lw=0.7)
    ax.set_xlabel("Mean maximum drawdown (points)", weight="bold")
    ax.set_ylabel("Mean net profit (points)", weight="bold")
    ax.set_title("Return--risk profile", weight="bold", fontsize=9.5, pad=7)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.015),
               ncol=2, frameon=False, fontsize=7)
    fig.subplots_adjust(bottom=0.24, top=0.91)

    fig.savefig(FIGURES / "economic_return_drawdown.pdf", format="pdf", bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    print(FIGURES / "economic_return_drawdown.pdf")


if __name__ == "__main__":
    main()
