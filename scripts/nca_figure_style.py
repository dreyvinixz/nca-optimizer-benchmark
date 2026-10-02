"""Shared visual tokens and export dimensions for the NCA manuscript figures."""

import matplotlib.pyplot as plt


FIGURE_WIDTH = 5.7
FIGURE_SINGLE = (FIGURE_WIDTH, 3.8)
FIGURE_MULTIPANEL = (FIGURE_WIDTH, 4.5)

OPTIMIZER_COLORS = {
    "random_search": "#0072B2",
    "ga": "#D55E00",
    "pso": "#009E73",
    "de": "#CC79A7",
    "gwo": "#E69F00",
}
OPTIMIZER_LINESTYLES = {
    "random_search": "-",
    "ga": (0, (5, 2)),
    "pso": (0, (3, 1, 1, 1)),
    "de": (0, (1, 1.5)),
    "gwo": (0, (7, 1.5, 1, 1.5)),
}
OPTIMIZER_MARKERS = {"random_search": "o", "ga": "s", "pso": "^", "de": "D", "gwo": "P"}
MODEL_COLORS = {
    "rf": "#0072B2",
    "svm": "#E69F00",
    "mlp": "#009E73",
    "cnn": "#CC79A7",
}
MODEL_LABELS = {"rf": "RF", "svm": "SVM", "mlp": "MLP", "cnn": "1D-CNN"}

RC_PARAMS = {
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9.5,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.linewidth": 0.75,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": "#E4E8ED",
    "grid.linewidth": 0.6,
    "grid.alpha": 0.9,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
}


def apply_publication_style() -> None:
    plt.rcParams.update(RC_PARAMS)
