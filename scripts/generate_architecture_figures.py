"""Generate article-ready neural architecture diagrams for MLP and CNN."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUTPUT_DIR = Path("outputs/article_figures/architecture")


COLORS = {
    "input": "#E7F0FA",
    "layer": "#EAF6EA",
    "regularization": "#FFF4D8",
    "output": "#F3EAF7",
    "training": "#FDE9E7",
    "edge": "#2F3A45",
    "muted": "#5A6673",
}


def setup_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.linewidth": 0.0,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def box(ax, x, y, w, h, title, body, fill, fontsize=9.5):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.018,rounding_size=0.045",
        linewidth=1.3,
        edgecolor=COLORS["edge"],
        facecolor=fill,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h * 0.68,
        title,
        ha="center",
        va="center",
        fontsize=fontsize + 0.7,
        fontweight="bold",
        color="#1E2933",
    )
    ax.text(
        x + w / 2,
        y + h * 0.36,
        body,
        ha="center",
        va="center",
        fontsize=fontsize,
        color="#26323D",
        linespacing=1.18,
    )
    return patch


def arrow(ax, start, end, rad=0.0, lw=1.5, color=None):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=lw,
            color=color or COLORS["edge"],
            connectionstyle=f"arc3,rad={rad}",
            shrinkA=5,
            shrinkB=5,
        )
    )


def annotate_band(ax, text):
    ax.text(
        0.5,
        0.895,
        text,
        ha="center",
        va="center",
        fontsize=9.8,
        color=COLORS["muted"],
    )


def finish(ax, title, out_stem):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(
        0.5,
        0.965,
        title,
        ha="center",
        va="top",
        fontsize=14.5,
        fontweight="bold",
        color="#17212B",
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "svg", "pdf"):
        path = OUTPUT_DIR / f"{out_stem}.{ext}"
        ax.figure.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(ax.figure)


def draw_training_loop(ax, loss_x=0.50, opt_x=0.70):
    loss = box(
        ax,
        loss_x - 0.105,
        0.075,
        0.21,
        0.16,
        "Training Objective",
        "Binary cross-entropy\n+ L2 regularization\nEarly stopping: val_loss",
        COLORS["training"],
        fontsize=8.1,
    )
    opt = box(
        ax,
        opt_x - 0.095,
        0.075,
        0.19,
        0.16,
        "Optimizer",
        "RMSProp\nlearning rate optimized\n1e-8 to 1e-2",
        COLORS["regularization"],
        fontsize=8.1,
    )
    arrow(ax, (loss_x + 0.105, 0.155), (opt_x - 0.095, 0.155), lw=1.3)
    arrow(ax, (opt_x, 0.235), (0.43, 0.355), rad=-0.23, lw=1.2, color="#57606A")
    ax.text(
        0.49,
        0.275,
        "updates trainable weights",
        ha="center",
        va="center",
        fontsize=8.3,
        color=COLORS["muted"],
    )
    return loss, opt


def draw_mlp():
    fig, ax = plt.subplots(figsize=(13.2, 5.15))
    annotate_band(
        ax,
        "CUDA MLP used in the NCA optimizer benchmark; structural validation selected RMSProp + Tanh.",
    )

    y = 0.56
    h = 0.20
    w = 0.145
    xs = [0.035, 0.225, 0.415, 0.605, 0.795]

    boxes = [
        box(
            ax,
            xs[0],
            y,
            w,
            h,
            "Input",
            "InfoGain-7 features\nstandardized tabular\nintraday indicators",
            COLORS["input"],
        ),
        box(
            ax,
            xs[1],
            y,
            w,
            h,
            "Dense Hidden",
            "H neurons\noptimized: 5 to 500\nactivation: Tanh",
            COLORS["layer"],
        ),
        box(
            ax,
            xs[2],
            y,
            w,
            h,
            "Dropout",
            "p optimized\n0.00 to 0.10\ntraining only",
            COLORS["regularization"],
        ),
        box(
            ax,
            xs[3],
            y,
            w,
            h,
            "Output Layer",
            "Dense(1)\nsigmoid activation\nthreshold: 0.50",
            COLORS["layer"],
        ),
        box(
            ax,
            xs[4],
            y,
            w,
            h,
            "Prediction",
            "P(uptrend)\nclass label:\ndowntrend / uptrend",
            COLORS["output"],
        ),
    ]

    for left, right in zip(boxes, boxes[1:]):
        arrow(
            ax,
            (left.get_x() + left.get_width(), y + h / 2),
            (right.get_x(), y + h / 2),
        )

    box(
        ax,
        0.225,
        0.345,
        0.335,
        0.09,
        "Regularized Parameters",
        "Hidden Dense kernel uses L2 alpha optimized from 1e-8 to 1e-2",
        "#F8FAFC",
        fontsize=8.2,
    )
    arrow(ax, (0.392, 0.435), (0.298, 0.56), rad=0.1, lw=1.0, color="#6B7280")

    draw_training_loop(ax, loss_x=0.50, opt_x=0.72)
    finish(ax, "MLP Architecture and Training Flow", "mlp_architecture")


def draw_cnn():
    fig, ax = plt.subplots(figsize=(14.2, 5.25))
    annotate_band(
        ax,
        "CUDA 1D-CNN over ordered InfoGain-7 features; structural validation selected RMSProp + Tanh.",
    )

    y = 0.56
    h = 0.20
    w = 0.13
    xs = [0.025, 0.185, 0.345, 0.505, 0.665, 0.825]

    boxes = [
        box(
            ax,
            xs[0],
            y,
            w,
            h,
            "Input",
            "InfoGain-7 features\nreshaped as\n7 x 1 sequence",
            COLORS["input"],
        ),
        box(
            ax,
            xs[1],
            y,
            w,
            h,
            "Conv1D",
            "filters: 8 to 128\nkernel: 2 to 5\npadding: same\nactivation: Tanh",
            COLORS["layer"],
            fontsize=8.7,
        ),
        box(
            ax,
            xs[2],
            y,
            w,
            h,
            "Global Max Pool",
            "selects strongest\nlocal feature response\nper filter",
            COLORS["layer"],
            fontsize=8.8,
        ),
        box(
            ax,
            xs[3],
            y,
            w,
            h,
            "Dense Hidden",
            "D neurons\noptimized: 16 to 256\nactivation: Tanh",
            COLORS["layer"],
            fontsize=8.8,
        ),
        box(
            ax,
            xs[4],
            y,
            w,
            h,
            "Dropout",
            "p optimized\n0.00 to 0.10\ntraining only",
            COLORS["regularization"],
            fontsize=8.8,
        ),
        box(
            ax,
            xs[5],
            y,
            w,
            h,
            "Prediction",
            "Dense(1) + sigmoid\nP(uptrend)\nthreshold: 0.50",
            COLORS["output"],
            fontsize=8.8,
        ),
    ]

    for left, right in zip(boxes, boxes[1:]):
        arrow(
            ax,
            (left.get_x() + left.get_width(), y + h / 2),
            (right.get_x(), y + h / 2),
        )

    box(
        ax,
        0.195,
        0.345,
        0.39,
        0.09,
        "Regularized Parameters",
        "Conv1D and Dense hidden kernels use L2 alpha optimized from 1e-8 to 1e-2",
        "#F8FAFC",
        fontsize=8.2,
    )
    arrow(ax, (0.29, 0.435), (0.25, 0.56), rad=0.08, lw=1.0, color="#6B7280")
    arrow(ax, (0.49, 0.435), (0.57, 0.56), rad=-0.08, lw=1.0, color="#6B7280")

    draw_training_loop(ax, loss_x=0.50, opt_x=0.72)
    finish(ax, "1D-CNN Architecture and Training Flow", "cnn_architecture")


def main() -> None:
    setup_style()
    draw_mlp()
    draw_cnn()
    print(f"Wrote architecture figures to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
