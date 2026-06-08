"""Generate neural-network style architecture figures for the article.

These figures are intentionally closer to textbook architecture diagrams:
nodes, connections, layer labels, and compact mathematical notation.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


OUT_DIR = Path("outputs/article_figures/architecture_network")
FEATURES = ["f30", "f52", "f31", "f53", "f42", "f33", "f41"]


def setup() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "mathtext.fontset": "dejavusans",
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.linewidth": 0,
        }
    )
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def save(fig: plt.Figure, stem: str) -> None:
    for ext in ("png", "svg", "pdf"):
        fig.savefig(OUT_DIR / f"{stem}.{ext}", dpi=350, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def line(ax, x1, y1, x2, y2, lw=0.8, alpha=0.72, color="#222222"):
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw, alpha=alpha, solid_capstyle="round")


def arrow(ax, start, end, lw=1.1, color="#222222", mutation_scale=11, alpha=0.9):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=mutation_scale,
            lw=lw,
            color=color,
            alpha=alpha,
            shrinkA=2,
            shrinkB=2,
        )
    )


def node(ax, x, y, r=0.024, text="", fc="white", ec="#111111", lw=1.15, fontsize=9):
    c = Circle((x, y), r, facecolor=fc, edgecolor=ec, lw=lw, zorder=3)
    ax.add_patch(c)
    if text:
        ax.text(x, y, text, ha="center", va="center", fontsize=fontsize, zorder=4)
    return c


def vertical_ellipsis(ax, x, y, fontsize=16):
    ax.text(x, y, r"$\vdots$", ha="center", va="center", fontsize=fontsize, color="#111111")


def layer_brace(ax, x0, x1, y, label):
    ax.plot([x0, x1], [y, y], color="#111111", lw=1.0)
    ax.plot([x0, x0], [y - 0.008, y + 0.008], color="#111111", lw=1.0)
    ax.plot([x1, x1], [y - 0.008, y + 0.008], color="#111111", lw=1.0)
    ax.text((x0 + x1) / 2, y - 0.035, label, ha="center", va="top", fontsize=10)


def draw_feature_selection(ax, x=0.04, y=0.80):
    ax.text(
        x,
        y,
        "Feature selection",
        ha="left",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color="#222222",
    )
    ax.text(
        x,
        y - 0.055,
        "Information Gain -> InfoGain-7",
        ha="left",
        va="center",
        fontsize=8.9,
        color="#222222",
    )


def training_box(ax, x, y, w, h, text):
    rect = Rectangle((x, y), w, h, facecolor="#F7F7F7", edgecolor="#222222", lw=0.9)
    ax.add_patch(rect)
    ax.text(
        x + w / 2,
        y + h * 0.78,
        "Training protocol",
        ha="center",
        va="center",
        fontsize=8.7,
        fontweight="bold",
    )
    ax.text(
        x + w / 2,
        y + h * 0.38,
        text,
        ha="center",
        va="center",
        fontsize=7.6,
        linespacing=1.18,
    )


def draw_mlp() -> None:
    fig, ax = plt.subplots(figsize=(12.0, 6.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.965, "CUDA MLP Architecture", ha="center", va="top", fontsize=17, fontweight="bold")
    ax.text(
        0.5,
        0.925,
        "InfoGain-7 input, fully connected hidden layer, Tanh activation, Sigmoid output, RMSProp optimization",
        ha="center",
        va="top",
        fontsize=10.5,
        color="#333333",
    )

    draw_feature_selection(ax, 0.035, 0.835)
    training_box(
        ax,
        0.705,
        0.715,
        0.245,
        0.135,
        "BCE + L2 regularization\nRMSProp, lr in [1e-8, 1e-2]\nEarly stopping on validation loss",
    )

    x_input, x_hidden, x_output, x_pred = 0.20, 0.48, 0.76, 0.91
    y_nodes = np.array([0.72, 0.63, 0.54, 0.45, 0.36, 0.27, 0.18])
    hidden_y = np.array([0.69, 0.58, 0.47, 0.36, 0.25])
    output_y = np.array([0.47])

    ax.text(0.085, 0.46, r"$\mathbf{x}=$", fontsize=15, ha="right", va="center")
    ax.plot([0.10, 0.10], [0.155, 0.745], color="#111111", lw=1.0)
    ax.plot([0.155, 0.155], [0.155, 0.745], color="#111111", lw=1.0)
    ax.plot([0.10, 0.115], [0.745, 0.745], color="#111111", lw=1.0)
    ax.plot([0.10, 0.115], [0.155, 0.155], color="#111111", lw=1.0)
    ax.plot([0.140, 0.155], [0.745, 0.745], color="#111111", lw=1.0)
    ax.plot([0.140, 0.155], [0.155, 0.155], color="#111111", lw=1.0)

    for i, (feat, y) in enumerate(zip(FEATURES, y_nodes), start=1):
        ax.text(0.128, y, rf"$x_{{{i}}}$", ha="center", va="center", fontsize=9)
        node(ax, x_input, y, r=0.010, fc="#111111")
        ax.text(x_input - 0.025, y + 0.017, feat, ha="right", va="center", fontsize=7.7, color="#444444")

    for j, y in enumerate(hidden_y, start=1):
        label = r"$\tanh$" if j in (1, 3, 5) else ""
        node(ax, x_hidden, y, r=0.028, text=label, fontsize=8.5)
        ax.text(x_hidden + 0.045, y + 0.006, rf"$h_{{{j}}}$", fontsize=9)
    vertical_ellipsis(ax, x_hidden, 0.305)
    ax.text(x_hidden, 0.185, r"$H \in [5,500]$", ha="center", fontsize=9.5)

    for y1 in y_nodes:
        for y2 in hidden_y:
            line(ax, x_input + 0.010, y1, x_hidden - 0.028, y2, lw=0.55, alpha=0.38)
    ax.text(0.335, 0.76, r"$W^{h}$", ha="center", fontsize=12)
    ax.text(0.335, 0.705, r"$z^{h}=\mathbf{x}W^{h}+b^{h}$", ha="center", fontsize=9)

    node(ax, x_output, output_y[0], r=0.032, text=r"$\sigma$", fontsize=12)
    ax.text(x_output + 0.055, output_y[0] + 0.005, r"$\hat{y}=P(\mathrm{uptrend})$", fontsize=10)
    for y2 in hidden_y:
        line(ax, x_hidden + 0.028, y2, x_output - 0.032, output_y[0], lw=0.75, alpha=0.65)
    ax.text(0.625, 0.66, r"$W^{y}$", ha="center", fontsize=12)
    ax.text(0.625, 0.61, r"$\hat{y}=\sigma(hW^{y}+b^{y})$", ha="center", fontsize=9)

    arrow(ax, (x_output + 0.035, output_y[0]), (x_pred - 0.02, output_y[0]), lw=1.2)
    ax.text(x_pred - 0.01, output_y[0] - 0.060, r"$\hat{c}=\mathbb{1}[\hat{y}\geq0.50]$", ha="left", va="center", fontsize=10)
    ax.text(x_pred - 0.01, output_y[0] - 0.115, "downtrend / uptrend", ha="left", va="center", fontsize=9)

    layer_brace(ax, x_input - 0.055, x_input + 0.055, 0.095, "Input layer")
    layer_brace(ax, x_hidden - 0.090, x_hidden + 0.090, 0.095, "Hidden layer")
    layer_brace(ax, x_output - 0.070, x_pred + 0.040, 0.095, "Output layer")

    save(fig, "mlp_network_architecture")


def feature_map(ax, x, y, w, h, offset=0.012, n=4, label=""):
    for i in reversed(range(n)):
        rect = Rectangle(
            (x + i * offset, y + i * offset),
            w,
            h,
            facecolor="white",
            edgecolor="#111111",
            lw=1.0,
            zorder=2 + i,
        )
        ax.add_patch(rect)
    if label:
        ax.text(x + w / 2 + offset * (n - 1) / 2, y + h + 0.045, label, ha="center", fontsize=9.5)


def draw_cnn() -> None:
    fig, ax = plt.subplots(figsize=(12.5, 7.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.965, "CUDA 1D-CNN Architecture", ha="center", va="top", fontsize=17, fontweight="bold")
    ax.text(
        0.5,
        0.925,
        "InfoGain-7 sequence, Conv1D with Tanh, Global Max Pooling, Dense Tanh layer, Sigmoid output, RMSProp optimization",
        ha="center",
        va="top",
        fontsize=10.2,
        color="#333333",
    )
    draw_feature_selection(ax, 0.035, 0.835)
    training_box(
        ax,
        0.755,
        0.765,
        0.210,
        0.105,
        "BCE + L2 regularization\nRMSProp, lr in [1e-8, 1e-2]\nEarly stopping on validation loss",
    )

    x0 = 0.17
    y0 = 0.18
    cell_h = 0.072
    cell_w = 0.075
    ax.text(x0 + cell_w / 2, 0.705, r"$\mathbf{x}\in\mathbb{R}^{7\times1}$", ha="center", fontsize=11)
    for i, feat in enumerate(FEATURES):
        y = y0 + (6 - i) * cell_h
        rect = Rectangle((x0, y), cell_w, cell_h * 0.82, facecolor="white", edgecolor="#111111", lw=1.0)
        ax.add_patch(rect)
        ax.text(x0 + cell_w / 2, y + cell_h * 0.41, rf"$x_{{{i+1}}}$ ({feat})", ha="center", va="center", fontsize=8)
    ax.text(x0 + cell_w / 2, 0.12, "standardized\nInfoGain-7", ha="center", fontsize=8.7)

    x_conv = 0.36
    feature_map(ax, x_conv, 0.33, 0.105, 0.265, offset=0.012, n=5, label="Conv1D feature maps")
    ax.text(
        x_conv + 0.07,
        0.275,
        r"$F\in[8,128]$ filters" "\n" r"$K\in[2,5]$, same padding" "\n" r"$a=\tanh(z)$",
        ha="center",
        va="top",
        fontsize=8.8,
    )
    arrow(ax, (x0 + cell_w + 0.015, 0.45), (x_conv - 0.010, 0.45), lw=1.2)
    ax.text(0.285, 0.505, r"$W^{c}$", ha="center", fontsize=12)

    x_pool = 0.56
    ax.text(x_pool + 0.03, 0.72, "Global max pooling", ha="center", fontsize=9.5)
    for i in range(5):
        y = 0.58 - i * 0.055
        node(ax, x_pool, y, r=0.012, fc="#111111")
    vertical_ellipsis(ax, x_pool, 0.37, fontsize=13)
    ax.text(x_pool, 0.295, r"$p_f=\max_t a_{t,f}^{c}$", ha="center", fontsize=9)
    arrow(ax, (x_conv + 0.165, 0.46), (x_pool - 0.018, 0.46), lw=1.2)

    x_dense = 0.73
    dense_y = np.array([0.61, 0.53, 0.45, 0.37])
    ax.text(x_dense, 0.72, "Dense hidden layer", ha="center", fontsize=9.5)
    for j, y in enumerate(dense_y, start=1):
        node(ax, x_dense, y, r=0.026, text=r"$\tanh$", fontsize=8.1)
        ax.text(x_dense + 0.042, y + 0.003, rf"$h_{{{j}}}$", fontsize=8.7)
    vertical_ellipsis(ax, x_dense, 0.315, fontsize=13)
    ax.text(x_dense, 0.255, r"$D\in[16,256]$", ha="center", fontsize=9.2)
    for yp in [0.58, 0.525, 0.47, 0.415, 0.36]:
        for yd in dense_y:
            line(ax, x_pool + 0.012, yp, x_dense - 0.026, yd, lw=0.58, alpha=0.42)
    ax.text(0.645, 0.64, r"$W^{d}$", ha="center", fontsize=12)

    x_out = 0.89
    node(ax, x_out, 0.47, r=0.032, text=r"$\sigma$", fontsize=12)
    for yd in dense_y:
        line(ax, x_dense + 0.026, yd, x_out - 0.032, 0.47, lw=0.75, alpha=0.65)
    ax.text(0.815, 0.64, r"$W^{y}$", ha="center", fontsize=12)
    ax.text(x_out + 0.045, 0.49, r"$\hat{y}=P(\mathrm{uptrend})$", ha="left", fontsize=9.5)
    ax.text(x_out + 0.045, 0.44, r"$\hat{c}=\mathbb{1}[\hat{y}\geq0.50]$", ha="left", fontsize=9.2)

    layer_brace(ax, x0 - 0.015, x0 + cell_w + 0.015, 0.075, "Input sequence")
    layer_brace(ax, x_conv - 0.015, x_conv + 0.175, 0.075, "Convolution")
    layer_brace(ax, x_pool - 0.050, x_pool + 0.050, 0.075, "Pooling")
    layer_brace(ax, x_dense - 0.070, x_dense + 0.070, 0.075, "Dense")
    layer_brace(ax, x_out - 0.045, x_out + 0.125, 0.075, "Output")

    save(fig, "cnn_network_architecture")


def main() -> None:
    setup()
    draw_mlp()
    draw_cnn()
    print(f"Wrote network-style architecture figures to {OUT_DIR}")


if __name__ == "__main__":
    main()
