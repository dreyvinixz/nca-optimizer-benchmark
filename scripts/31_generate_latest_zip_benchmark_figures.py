"""Regenerate benchmark figures for the latest ZIP-based NCA manuscript.

The manuscript source is extracted to article/manuscript/latest_zip_revision.
Raw experiment outputs remain in outputs/article_official and
outputs/article_official_accuracy_holdout. Only the three common seeds
(1, 2, 3) documented in the manuscript are included.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter, StrMethodFormatter
from nca_figure_style import (
    FIGURE_MULTIPANEL, FIGURE_SINGLE, MODEL_COLORS, MODEL_LABELS,
    OPTIMIZER_COLORS, OPTIMIZER_LINESTYLES, OPTIMIZER_MARKERS,
    apply_publication_style,
)


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "article" / "manuscript" / "latest_zip_revision" / "figures"
SEEDS = (1, 2, 3)
MODELS = ("rf", "svm", "mlp", "cnn")
OPTIMIZERS = ("random_search", "ga", "pso", "de", "gwo")
OPT_LABELS = {
    "random_search": "RS",
    "ga": "GA",
    "pso": "PSO",
    "de": "DE",
    "gwo": "GWO",
}
MODE_CONFIG = {
    "mcc_f1": {
        "label": "MCC/$F_1$ fitness",
        "data": ROOT / "outputs" / "article_official",
        "metric": "mcc_test",
        "metric_label": "Locked-test MCC",
        "y_title": "MCC/$F_1$ fitness",
        "convergence_suffix": "mccf1",
        "heatmap_file": "heatmap_mccf1_mcc_test.pdf",
    },
    "accuracy": {
        "label": "Weighted-accuracy fitness",
        "data": ROOT / "outputs" / "article_official_accuracy_holdout",
        "metric": "accuracy_test",
        "metric_label": "Locked-test accuracy",
        "y_title": "Weighted-accuracy fitness",
        "convergence_suffix": "accuracy",
        "heatmap_file": "heatmap_accuracy_accuracy_test.pdf",
    },
}

apply_publication_style()
OPT_COLORS = OPTIMIZER_COLORS
OPT_LINESTYLES = OPTIMIZER_LINESTYLES
OPT_MARKERS = OPTIMIZER_MARKERS

ECONOMIC_CSV = ROOT / "outputs" / "professor_presentation" / "statistical_economic_model_selection" / "economic_by_model_experiment.csv"


def read_run_csv(path: Path) -> pd.DataFrame:
    """Read a candidate log, ignoring any fields beyond its declared header.

    Two SVM/GWO logs contain an extra trailing field on some records. It is
    outside the CSV header schema, so the declared columns are retained and
    the undeclared tail is ignored.
    """
    with path.open("r", newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.reader(stream))
    header = rows[0]
    data = []
    for line_number, row in enumerate(rows[1:], start=2):
        if len(row) < len(header):
            raise ValueError(f"{path}:{line_number}: fewer fields than header")
        data.append(row[: len(header)])
    return pd.DataFrame(data, columns=header)


def load_protocol(mode: str) -> dict[str, pd.DataFrame]:
    config = MODE_CONFIG[mode]
    metrics_dir = config["data"] / "metrics"
    conv_dir = metrics_dir / "convergence"
    conv_files = sorted(conv_dir.glob("*_convergence.csv"))
    run_files = sorted(metrics_dir.glob("*_runs.csv"))
    best_files = sorted(metrics_dir.glob("*_best_by_seed.csv"))
    if not (len(conv_files) == len(run_files) == len(best_files) == 20):
        raise ValueError(f"{mode}: expected 20 model-optimizer files per output type")

    conv = pd.concat((pd.read_csv(path) for path in conv_files), ignore_index=True)
    runs = pd.concat((read_run_csv(path) for path in run_files), ignore_index=True)
    best = pd.concat((pd.read_csv(path) for path in best_files), ignore_index=True)

    for frame in (conv, runs, best):
        frame["model_type"] = frame["model_type"].astype(str).str.lower()
        frame["optimizer"] = frame["optimizer"].astype(str).str.lower()
        frame["seed"] = pd.to_numeric(frame["seed"], errors="raise").astype(int)
        frame.drop(frame.index[~frame["seed"].isin(SEEDS)], inplace=True)

    conv["evaluation_id"] = pd.to_numeric(conv["evaluation_id"], errors="raise").astype(int)
    conv["best_fitness_so_far"] = pd.to_numeric(conv["best_fitness_so_far"], errors="raise")
    runs["train_time_seconds"] = pd.to_numeric(runs["train_time_seconds"], errors="raise")
    cache_values = runs["cache_hit"].astype(str).str.lower()
    runs["cache_hit"] = cache_values.eq("true")
    for metric in ("accuracy_test", "mcc_test", "f1_test"):
        best[metric] = pd.to_numeric(best[metric], errors="raise")

    expected = {
        (model, optimizer, seed)
        for model in MODELS
        for optimizer in OPTIMIZERS
        for seed in SEEDS
    }
    for frame, name in ((conv, "convergence"), (runs, "candidate runs"), (best, "best-by-seed")):
        observed = set(map(tuple, frame[["model_type", "optimizer", "seed"]].drop_duplicates().to_numpy()))
        if observed != expected:
            raise ValueError(f"{mode} {name}: expected 60 common model/optimizer/seed cells")

    conv_counts = conv.groupby(["model_type", "optimizer", "seed"]).size()
    if not conv_counts.eq(1000).all():
        raise ValueError(f"{mode}: convergence data do not contain 1,000 evaluations per seed")
    eval_counts = conv.groupby(["model_type", "optimizer", "seed"])["evaluation_id"].nunique()
    if not eval_counts.eq(1000).all():
        raise ValueError(f"{mode}: a convergence series has repeated or missing evaluation IDs")
    run_counts = runs.groupby(["model_type", "optimizer", "seed"]).size()
    if not run_counts.eq(1000).all():
        raise ValueError(f"{mode}: candidate run logs do not match the 1,000-evaluation budget")
    best_counts = best.groupby(["model_type", "optimizer"]).size()
    if not best_counts.eq(3).all():
        raise ValueError(f"{mode}: best-by-seed metrics do not contain exactly three common seeds")

    runs["uncached_fit_seconds"] = runs["train_time_seconds"].where(~runs["cache_hit"], 0.0)
    fit_time = (
        runs.groupby(["model_type", "optimizer", "seed"], as_index=False)["uncached_fit_seconds"]
        .sum()
        .rename(columns={"uncached_fit_seconds": "candidate_fit_seconds"})
    )
    best["mode"] = mode
    conv["mode"] = mode
    return {"convergence": conv, "runs": runs, "best": best, "fit_time": fit_time}


def save_pdf(fig: plt.Figure, filename: str) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / filename, format="pdf", bbox_inches="tight", metadata={"Creator": "Matplotlib"})
    plt.close(fig)


def plot_convergence(data: dict[str, pd.DataFrame], mode: str) -> None:
    config = MODE_CONFIG[mode]
    conv = data["convergence"]
    summary = (
        conv.groupby(["model_type", "optimizer", "evaluation_id"])["best_fitness_so_far"]
        .mean()
        .reset_index(name="mean")
    )
    for model in MODELS:
        model_summary = summary[summary.model_type == model]
        observed_min = float(model_summary["mean"].min())
        observed_max = float(model_summary["mean"].max())
        observed_span = observed_max - observed_min
        ypadding = max(observed_span * 0.05, 0.0001)

        fig, ax = plt.subplots(figsize=FIGURE_SINGLE)
        for optimizer in OPTIMIZERS:
            curve = summary[(summary.model_type == model) & (summary.optimizer == optimizer)]
            x = curve.evaluation_id.to_numpy()
            mean = curve["mean"].to_numpy()
            ax.plot(
                x,
                mean,
                color=OPT_COLORS[optimizer],
                linewidth=1.05,
                linestyle=OPT_LINESTYLES[optimizer],
                label=OPT_LABELS[optimizer],
                zorder=3,
            )
        ax.set_xlim(1, 1000)
        ax.set_ylim(observed_min - ypadding, observed_max + ypadding)
        ax.set_xticks((1, 250, 500, 750, 1000))
        ax.set_xlabel("Objective-function evaluations")
        ax.set_ylabel("Best validation fitness")
        ax.set_title(f"{MODEL_LABELS[model]} | {config['label']}", pad=8, weight="bold")
        ax.yaxis.set_major_formatter(FormatStrFormatter("%.3f"))
        ax.grid(axis="y")
        ax.grid(axis="x", visible=False)
        ax.spines["left"].set_color("#66717D")
        ax.spines["bottom"].set_color("#66717D")

        # The main panel uses tight limits from this model's observed mean
        # trajectories. A line-only inset magnifies the final 250 evaluations.
        axins = ax.inset_axes([0.55, 0.055, 0.42, 0.35])
        for optimizer in OPTIMIZERS:
            curve = summary[
                (summary.model_type == model)
                & (summary.optimizer == optimizer)
                & (summary.evaluation_id >= 751)
            ]
            axins.plot(
                curve.evaluation_id,
                curve["mean"],
                color=OPT_COLORS[optimizer],
                linewidth=1.0,
                linestyle=OPT_LINESTYLES[optimizer],
            )
        terminal = summary[(summary.model_type == model) & (summary.evaluation_id >= 751)]
        zmin, zmax = float(terminal["mean"].min()), float(terminal["mean"].max())
        zpadding = max((zmax - zmin) * 0.12, observed_span * 0.002, 0.0001)
        axins.set_xlim(751, 1000)
        axins.set_ylim(zmin - zpadding, zmax + zpadding)
        axins.set_xticks((751, 875, 1000))
        axins.yaxis.set_major_formatter(FormatStrFormatter("%.3f"))
        axins.tick_params(axis="both", labelsize=6.5, length=2, pad=1.5)
        axins.set_title("Final 250 evaluations", fontsize=7.2, pad=2.5)
        axins.grid(axis="y", linewidth=0.45, alpha=0.75)
        axins.grid(axis="x", visible=False)
        axins.spines["top"].set_visible(True)
        axins.spines["right"].set_visible(True)
        axins.spines["top"].set_color("#87919B")
        axins.spines["right"].set_color("#87919B")
        axins.set_facecolor("white")
        fig.legend(
            loc="upper center",
            bbox_to_anchor=(0.5, 0.94),
            ncol=5,
            frameon=False,
            handlelength=2.0,
            columnspacing=1.15,
            fontsize=8,
        )
        fig.subplots_adjust(left=0.105, right=0.98, bottom=0.15, top=0.80)
        filename = f"{model}_convergence_{config['convergence_suffix']}.pdf"
        save_pdf(fig, filename)


def plot_heatmap(data: dict[str, pd.DataFrame], mode: str) -> None:
    config = MODE_CONFIG[mode]
    metric = config["metric"]
    summary = data["best"].groupby(["model_type", "optimizer"])[metric].agg(["mean", "std"])
    mean = summary["mean"].unstack("optimizer").reindex(index=MODELS, columns=OPTIMIZERS)
    std = summary["std"].unstack("optimizer").reindex(index=MODELS, columns=OPTIMIZERS)
    values = mean.to_numpy()
    low = float(np.nanmin(values))
    high = float(np.nanmax(values))
    pad = max((high - low) * 0.09, 0.003)
    vmin, vmax = low - pad, high + pad

    fig, ax = plt.subplots(figsize=FIGURE_SINGLE)
    mesh = ax.pcolormesh(
        np.arange(len(OPTIMIZERS) + 1),
        np.arange(len(MODELS) + 1),
        values,
        cmap="YlGnBu",
        vmin=vmin,
        vmax=vmax,
        shading="flat",
        edgecolors="white",
        linewidth=1.4,
    )
    ax.set_xlim(0, len(OPTIMIZERS))
    ax.set_ylim(len(MODELS), 0)
    ax.set_xticks(np.arange(len(OPTIMIZERS)) + 0.5, [OPT_LABELS[o] for o in OPTIMIZERS])
    ax.set_yticks(np.arange(len(MODELS)) + 0.5, [MODEL_LABELS[m] for m in MODELS])
    ax.set_xlabel("Optimizer")
    ax.set_ylabel("Model family")
    ax.set_title(f"{config['label']}: {config['metric_label']}", weight="bold", pad=11)
    for i, model in enumerate(MODELS):
        for j, optimizer in enumerate(OPTIMIZERS):
            value = mean.loc[model, optimizer]
            sd = std.loc[model, optimizer]
            normalized = (value - vmin) / (vmax - vmin)
            color = "white" if normalized > 0.57 else "#1D2730"
            ax.text(j + 0.5, i + 0.5, f"{value:.3f}\n$\\pm$ {sd:.3f}", ha="center", va="center", fontsize=8.5, color=color)
    cbar = fig.colorbar(mesh, ax=ax, pad=0.025, fraction=0.045)
    cbar.set_label(f"Mean {metric}", rotation=90, labelpad=9)
    if cbar.solids is not None:
        cbar.solids.set_rasterized(False)
    ax.grid(False)
    fig.tight_layout(pad=1.1)
    save_pdf(fig, config["heatmap_file"])


def plot_seed_distribution(all_best: pd.DataFrame) -> None:
    """Show the three observed seed outcomes directly; avoid box summaries at n=3."""
    fig, axes = plt.subplots(2, 2, figsize=FIGURE_MULTIPANEL, sharey=True, sharex=True)
    mode_colors = {"mcc_f1": "#2878A5", "accuracy": "#D58B22"}
    mode_offsets = {"mcc_f1": -0.18, "accuracy": 0.18}
    seed_jitter = {1: -0.035, 2: 0.0, 3: 0.035}
    for ax, model in zip(axes.flat, MODELS):
        subset = all_best[all_best.model_type == model]
        for i, optimizer in enumerate(OPTIMIZERS, start=1):
            for mode in MODE_CONFIG:
                values = subset[(subset.optimizer == optimizer) & (subset["mode"] == mode)].sort_values("seed")
                position = i + mode_offsets[mode]
                color = mode_colors[mode]
                ax.scatter(
                    [position + seed_jitter[int(seed)] for seed in values.seed],
                    values.mcc_test,
                    s=24,
                    color=color,
                    alpha=0.78,
                    edgecolor="white",
                    linewidth=0.5,
                    zorder=3,
                )
                mean = float(values.mcc_test.mean())
                sd = float(values.mcc_test.std(ddof=1))
                ax.errorbar(
                    position,
                    mean,
                    yerr=sd,
                    fmt="D",
                    color=color,
                    markerfacecolor="white",
                    markeredgecolor=color,
                    markeredgewidth=1.0,
                    markersize=4.5,
                    capsize=2.2,
                    elinewidth=0.9,
                    zorder=4,
                )
        ax.set_title(MODEL_LABELS[model], weight="bold", pad=5)
        ax.set_xticks(range(1, len(OPTIMIZERS) + 1), [OPT_LABELS[o] for o in OPTIMIZERS])
        ax.set_xlim(0.55, len(OPTIMIZERS) + 0.45)
        ax.grid(axis="y")
        ax.grid(axis="x", visible=False)
    for ax in axes[:, 0]:
        ax.set_ylabel("Locked-test MCC")
        ax.yaxis.set_major_formatter(FormatStrFormatter("%.3f"))
    for ax in axes[1, :]:
        ax.set_xlabel("Optimizer")
    handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=mode_colors[mode],
               markeredgecolor="white", label=MODE_CONFIG[mode]["label"], markersize=5.5)
        for mode in MODE_CONFIG
    ]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 1.01), ncol=2, frameon=False)
    fig.subplots_adjust(left=0.10, right=0.99, bottom=0.11, top=0.89, hspace=0.34, wspace=0.18)
    save_pdf(fig, "test_mcc_seed_points.pdf")


def plot_optimizer_ranks(all_best: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=FIGURE_SINGLE, sharex=True)
    for ax, mode in zip(axes, MODE_CONFIG):
        metric = MODE_CONFIG[mode]["metric"]
        d = all_best[all_best["mode"] == mode]
        d = d.copy()
        d["rank"] = d.groupby(["model_type", "seed"])[metric].rank(ascending=False, method="average")
        stats = d.groupby("optimizer")["rank"].agg(["mean", "std"]).reindex(OPTIMIZERS)
        y = np.arange(len(OPTIMIZERS))
        for i, optimizer in enumerate(OPTIMIZERS):
            ax.errorbar(
                stats.loc[optimizer, "mean"],
                i,
                xerr=stats.loc[optimizer, "std"],
                fmt="D",
                color=OPT_COLORS[optimizer],
                markeredgecolor="white",
                markeredgewidth=0.6,
                markersize=6,
                capsize=2.5,
                elinewidth=1.0,
                zorder=3,
            )
        ax.set_yticks(y, [OPT_LABELS[o] for o in OPTIMIZERS])
        ax.invert_yaxis()
        ax.set_title(f"{MODE_CONFIG[mode]['label']}\nranked by {metric}", weight="bold", pad=8)
        ax.set_xlim(0.8, 5.2)
        ax.set_xticks((1, 2, 3, 4, 5))
        ax.set_xlabel("Average rank (lower is better)")
        ax.grid(axis="x")
        ax.grid(axis="y", visible=False)
        ax.axvline(1, color="#66717D", linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
    fig.subplots_adjust(left=0.12, right=0.99, bottom=0.16, top=0.82, wspace=0.30)
    save_pdf(fig, "optimizer_average_ranks.pdf")


def plot_performance_cost(all_best: pd.DataFrame, all_fit_time: pd.DataFrame) -> None:
    data = all_best.merge(all_fit_time, on=["mode", "model_type", "optimizer", "seed"], validate="one_to_one")
    model_order = MODELS
    for mode, cfg in MODE_CONFIG.items():
        fig, axes = plt.subplots(2, 2, figsize=FIGURE_MULTIPANEL, sharex=True, sharey=True)
        d = data[data["mode"] == mode]
        stats = d.groupby(["model_type", "optimizer"]).agg(
            score_mean=(cfg["metric"], "mean"),
            score_sd=(cfg["metric"], "std"),
            cost_mean=("candidate_fit_seconds", "mean"),
            cost_sd=("candidate_fit_seconds", "std"),
        )
        cost_low = (stats.cost_mean - stats.cost_sd).clip(lower=stats.cost_mean * 0.25).min()
        cost_high = (stats.cost_mean + stats.cost_sd).max()
        log_span = np.log10(cost_high) - np.log10(cost_low)
        xlim = (10 ** (np.log10(cost_low) - 0.06 * log_span), 10 ** (np.log10(cost_high) + 0.06 * log_span))
        score_low = (stats.score_mean - stats.score_sd).min()
        score_high = (stats.score_mean + stats.score_sd).max()
        score_pad = max((score_high - score_low) * 0.08, 0.004)
        for ax, model in zip(axes.flat, model_order):
            model_stats = stats.loc[model]
            for optimizer in OPTIMIZERS:
                row = model_stats.loc[optimizer]
                ax.errorbar(
                    row.cost_mean,
                    row.score_mean,
                    yerr=row.score_sd,
                    fmt=OPT_MARKERS[optimizer],
                    color=OPT_COLORS[optimizer],
                    markerfacecolor=OPT_COLORS[optimizer],
                    markeredgecolor="white",
                    markeredgewidth=0.7,
                    markersize=5.0,
                    capsize=2.2,
                    elinewidth=0.9,
                    zorder=3,
                )
            ax.set_xscale("log")
            ax.set_xlim(xlim)
            ax.set_ylim(score_low - score_pad, score_high + score_pad)
            ax.set_title(MODEL_LABELS[model], weight="bold", pad=5)
            ax.grid(axis="both", which="major")
            ax.grid(axis="x", which="minor", alpha=0.25, linewidth=0.45)
            ax.set_axisbelow(True)
        for ax in axes[:, 0]:
            ax.set_ylabel(cfg["metric_label"])
        for ax in axes.flat:
            ax.yaxis.set_major_formatter(FormatStrFormatter("%.3f"))
        for ax in axes[1, :]:
            ax.set_xlabel("Fit time (s; log scale)")
        optimizer_handles = [
            Line2D([0], [0], marker=OPT_MARKERS[o], color=OPT_COLORS[o], linestyle="none",
                   label=OPT_LABELS[o], markersize=5)
            for o in OPTIMIZERS
        ]
        fig.legend(handles=optimizer_handles, loc="upper center", bbox_to_anchor=(0.5, 0.99),
                   ncol=5, frameon=False, columnspacing=1.2)
        fig.suptitle(f"{cfg['label']}: performance--effort by backbone", y=1.045, weight="bold", fontsize=10)
        fig.subplots_adjust(left=0.11, right=0.98, bottom=0.11, top=0.86, hspace=0.35, wspace=0.22)
        suffix = "mccf1" if mode == "mcc_f1" else "accuracy"
        save_pdf(fig, f"performance_vs_fit_time_{suffix}.pdf")


def plot_radar_overview(all_best: pd.DataFrame, all_fit_time: pd.DataFrame) -> None:
    data = all_best.merge(all_fit_time, on=["mode", "model_type", "optimizer", "seed"], validate="one_to_one")
    metrics = data.groupby(["mode", "model_type"]).agg(
        mcc=("mcc_test", "mean"),
        accuracy=("accuracy_test", "mean"),
        f1=("f1_test", "mean"),
        fit_time=("candidate_fit_seconds", "mean"),
    ).reset_index()
    metrics["log_fit_time"] = np.log10(metrics.fit_time.clip(lower=1e-6))
    axes_metrics = ("mcc", "accuracy", "f1", "log_fit_time")
    for col in axes_metrics:
        low = float(metrics[col].min())
        high = float(metrics[col].max())
        metrics[f"norm_{col}"] = 0.5 if np.isclose(low, high) else (metrics[col] - low) / (high - low)
    metrics["norm_inverse_fit_time"] = 1.0 - metrics["norm_log_fit_time"]
    labels = ("Test MCC", "Test accuracy", "Test F1", "Inverse\nfit time")
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    closed_angles = angles + angles[:1]

    fig, axes = plt.subplots(1, 2, figsize=FIGURE_MULTIPANEL, subplot_kw={"projection": "polar"})
    for ax, mode in zip(axes, MODE_CONFIG):
        for model in MODELS:
            row = metrics[(metrics["mode"] == mode) & (metrics.model_type == model)].iloc[0]
            values = [row.norm_mcc, row.norm_accuracy, row.norm_f1, row.norm_inverse_fit_time]
            closed_values = values + values[:1]
            ax.plot(closed_angles, closed_values, color=MODEL_COLORS[model], linewidth=1.6, marker="o", markersize=3.7, label=MODEL_LABELS[model])
            ax.fill(closed_angles, closed_values, color=MODEL_COLORS[model], alpha=0.075)
        ax.set_xticks(angles, labels)
        ax.tick_params(axis="x", labelsize=8, pad=9)
        ax.set_ylim(0, 1)
        ax.set_yticks((0.25, 0.5, 0.75, 1.0))
        ax.set_yticklabels(("0.25", "0.50", "0.75", "1.00"), fontsize=6.5, color="#66717D")
        ax.set_rlabel_position(22)
        ax.grid(color="#D7DDE3", linewidth=0.65)
        ax.spines["polar"].set_color("#9AA4AE")
        ax.set_title(MODE_CONFIG[mode]["label"], y=1.13, weight="bold", fontsize=9.5)
    handles = [Line2D([0], [0], color=MODEL_COLORS[m], marker="o", linewidth=1.6, label=MODEL_LABELS[m], markersize=4) for m in MODELS]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.015), ncol=4, frameon=False)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.84, bottom=0.16, wspace=0.30)
    save_pdf(fig, "radar_overview_normalized.pdf")


def plot_model_comparison(all_best: pd.DataFrame) -> None:
    """Protocol-by-metric comparison with one persistent color per backbone."""
    fig, axes = plt.subplots(2, 2, figsize=FIGURE_MULTIPANEL, sharex="col", sharey="col")
    metric_specs = (("accuracy_test", "Locked-test accuracy"), ("mcc_test", "Locked-test MCC"))
    labels = [m.upper() if m != "cnn" else "1D-CNN" for m in MODELS]
    for row, mode in enumerate(MODE_CONFIG):
        subset = all_best[all_best["mode"] == mode]
        for col, (metric, ylabel) in enumerate(metric_specs):
            ax = axes[row, col]
            values = subset.groupby("model_type")[metric].agg(["mean", "std"]).reindex(MODELS)
            for pos, model in enumerate(MODELS):
                ax.errorbar(pos, values.loc[model, "mean"], yerr=values.loc[model, "std"],
                            fmt="o", color=MODEL_COLORS[model], markeredgecolor="white",
                            markeredgewidth=0.7, markersize=5.5, capsize=2.3,
                            elinewidth=0.9, zorder=3)
            ax.set_xticks(range(len(MODELS)), labels, rotation=18, ha="right")
            ax.set_ylabel("")
            ax.yaxis.set_major_formatter(FormatStrFormatter("%.3f"))
            ax.grid(axis="y")
            ax.grid(axis="x", visible=False)
            ax.set_axisbelow(True)
            if row == 0:
                ax.set_title(ylabel, weight="bold", pad=5)
    for col, (metric, _ylabel) in enumerate(metric_specs):
        pooled = all_best.groupby("model_type")[metric].agg(["mean", "std"]).reindex(MODELS)
        lo = float((pooled["mean"] - pooled["std"]).min())
        hi = float((pooled["mean"] + pooled["std"]).max())
        margin = max((hi - lo) * 0.08, 0.004)
        axes[0, col].set_ylim(lo - margin, hi + margin)
    fig.text(0.03, 0.70, "MCC/$F_1$ fitness", rotation=90, ha="center", va="center", fontsize=8, weight="bold")
    fig.text(0.03, 0.29, "Weighted-accuracy fitness", rotation=90, ha="center", va="center", fontsize=8, weight="bold")
    fig.text(0.11, 0.50, "Locked-test metric", rotation=90, ha="center", va="center", fontsize=8)
    fig.subplots_adjust(left=0.19, right=0.98, bottom=0.15, top=0.91, hspace=0.38, wspace=0.28)
    save_pdf(fig, "model_comparison_protocols.pdf")


def plot_economic_comparison() -> None:
    """Return--drawdown scatter, with model colors shared by all model figures."""
    frame = pd.read_csv(ECONOMIC_CSV)
    frame = frame[frame["experiment"].isin(("exp1_holdout_mcc_f1", "exp2_holdout_accuracy"))].copy()
    protocol_order = ("exp1_holdout_mcc_f1", "exp2_holdout_accuracy")
    titles = ("MCC/$F_1$ fitness", "Weighted-accuracy fitness")
    fig, axes = plt.subplots(1, 2, figsize=FIGURE_SINGLE, sharex=True, sharey=True)
    for ax, protocol, title in zip(axes, protocol_order, titles):
        part = frame[frame.experiment == protocol].set_index("model").reindex(MODELS)
        for model in MODELS:
            row = part.loc[model]
            ax.scatter(row.total_profit_mean, row.max_drawdown_mean, s=42,
                       color=MODEL_COLORS[model], edgecolor="white", linewidth=0.7,
                       label=MODEL_LABELS[model], zorder=3)
        ax.set_title(title, weight="bold", pad=6)
        ax.grid(axis="both")
        ax.set_axisbelow(True)
        ax.set_xlabel("Mean net profit (points)")
        ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
        ax.yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    axes[0].set_ylabel("Mean maximum drawdown (points)")
    handles = [Line2D([0], [0], marker="o", color="none", markerfacecolor=MODEL_COLORS[m],
                      markeredgecolor="white", label=MODEL_LABELS[m], markersize=5.5) for m in MODELS]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.55, 1.03), ncol=4, frameon=False)
    fig.subplots_adjust(left=0.19, right=0.98, bottom=0.19, top=0.82, wspace=0.25)
    save_pdf(fig, "economic_return_drawdown.pdf")


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    protocol_data = {mode: load_protocol(mode) for mode in MODE_CONFIG}
    all_best = pd.concat((protocol_data[mode]["best"] for mode in MODE_CONFIG), ignore_index=True)
    all_fit_time = pd.concat(
        [data["fit_time"].assign(mode=mode) for mode, data in protocol_data.items()],
        ignore_index=True,
    )

    for mode, data in protocol_data.items():
        plot_convergence(data, mode)
        plot_heatmap(data, mode)
    plot_seed_distribution(all_best)
    plot_optimizer_ranks(all_best)
    plot_performance_cost(all_best, all_fit_time)
    plot_radar_overview(all_best, all_fit_time)
    plot_model_comparison(all_best)
    plot_economic_comparison()

    expected_figures = 17
    actual_figures = len(list(FIG_DIR.glob("*_convergence_*.pdf"))) + 9
    if actual_figures != expected_figures:
        raise RuntimeError(f"Expected {expected_figures} vector figures, found {actual_figures}")
    print(f"Generated {expected_figures} vector PDF figures in {FIG_DIR}")
    print("Validated 20 model-optimizer cells, 3 common seeds, and 1,000 evaluations per run for each protocol.")


if __name__ == "__main__":
    main()
