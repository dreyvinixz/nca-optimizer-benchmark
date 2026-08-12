"""Create the literature-synthesis figure used in Section 2 of the NCA paper.

The counts are derived from the 15 representative published studies in
Table 1 of article/manuscript/sections/literature_review.tex.  The present
work is deliberately excluded: the figure characterizes prior literature.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator


YEARS = np.array([2019, 2020, 2024, 2025, 2026])

# Each study is assigned once according to its optimizer-comparison scope.
# Totals by year are 1, 2, 3, 4, and 5, respectively (n = 15).
SERIES = {
    "No metaheuristic": np.array([1, 1, 2, 3, 2]),
    "Single optimizer": np.array([0, 0, 1, 1, 2]),
    "Multi-optimizer": np.array([0, 1, 0, 0, 1]),
}

COLORS = {
    "No metaheuristic": "#9AA5B1",  # neutral gray-blue
    "Single optimizer": "#E07A24",  # restrained orange
    "Multi-optimizer": "#2F6690",   # deep blue
}


def main() -> None:
    output = (
        Path(__file__).resolve().parents[1]
        / "article"
        / "manuscript"
        / "figures"
        / "literature_scope_by_year.pdf"
    )
    output.parent.mkdir(parents=True, exist_ok=True)

    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 8,
            "axes.labelweight": "normal",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    figure, axis = plt.subplots(figsize=(6.7, 3.35))
    x_positions = np.arange(len(YEARS))
    bar_width = 0.22
    offsets = (-bar_width, 0.0, bar_width)

    for (label, values), offset in zip(SERIES.items(), offsets):
        bars = axis.bar(
            x_positions + offset,
            values,
            width=bar_width,
            label=label,
            color=COLORS[label],
            edgecolor="#263238",
            linewidth=0.65,
        )
        for bar, value in zip(bars, values):
            if value:
                axis.text(
                    bar.get_x() + bar.get_width() / 2,
                    value + 0.10,
                    str(value),
                    ha="center",
                    va="bottom",
                    fontsize=6.5,
                    color="#263238",
                )

    axis.set_xlabel("Publication year", fontsize=7.5, labelpad=5)
    axis.set_ylabel("Representative studies", fontsize=7.5, labelpad=5)
    axis.set_xticks(x_positions, YEARS)
    axis.set_ylim(0, 3.8)
    axis.yaxis.set_major_locator(MaxNLocator(integer=True))
    axis.grid(axis="y", color="#CFD8DC", linewidth=0.65)
    axis.set_axisbelow(True)
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines[["left", "bottom"]].set_color("#37474F")
    axis.tick_params(color="#37474F", labelcolor="#263238", labelsize=7)

    legend = axis.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.24),
        ncol=3,
        frameon=False,
        columnspacing=1.6,
        handlelength=1.15,
        handletextpad=0.45,
        prop={"size": 7},
    )
    for text in legend.get_texts():
        text.set_color("#263238")

    figure.subplots_adjust(left=0.12, right=0.985, top=0.96, bottom=0.30)
    figure.savefig(output, bbox_inches="tight", pad_inches=0.02)
    plt.close(figure)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
