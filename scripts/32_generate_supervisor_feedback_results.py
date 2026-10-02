"""Create the three supervisor-requested manuscript figures and effort summary.

Uses the three common seeds in the manuscript. Effort is reported both as
objective calls and as uncached candidate fits (multiplied by the number of
temporal folds for the cross-validation experiment).
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

from nca_figure_style import (
    FIGURE_MULTIPANEL, MODEL_COLORS, MODEL_LABELS, OPTIMIZER_COLORS,
    OPTIMIZER_MARKERS, apply_publication_style,
)

ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "article/manuscript/latest_zip_revision/figures"
SEEDS = (1, 2, 3)
MODELS = ("rf", "svm", "mlp", "cnn")
OPTIMIZERS = ("random_search", "ga", "pso", "de", "gwo")
OPT_LABEL = dict(zip(OPTIMIZERS, ("RS", "GA", "PSO", "DE", "GWO")))
EXPERIMENTS = {
    "exp1_mcc_f1_holdout": (ROOT / "outputs/article_official", 1, "MCC/$F_1$ holdout"),
    "exp2_accuracy_holdout": (ROOT / "outputs/article_official_accuracy_holdout", 1, "Weighted-accuracy holdout"),
    "exp3_accuracy_temporal_cv": (ROOT / "outputs/article_official_accuracy", 3, "Temporal cross-validation"),
}

apply_publication_style()
plt.rcParams.update({"legend.frameon": False, "axes.titleweight": "bold"})


def read_run(path: Path) -> pd.DataFrame:
    # Some legacy SVM/GWO logs have undeclared trailing CSV fields.
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    return pd.DataFrame([r[:len(rows[0])] for r in rows[1:]], columns=rows[0])


def load_best_and_effort():
    best_rows, effort_rows = [], []
    for exp, (root, folds, _) in EXPERIMENTS.items():
        metrics = root / "metrics"
        best = pd.concat([pd.read_csv(p) for p in metrics.glob("*_best_by_seed.csv")], ignore_index=True)
        best["model_type"] = best.model_type.str.lower()
        best["optimizer"] = best.optimizer.str.lower()
        best["seed"] = pd.to_numeric(best.seed).astype(int)
        best = best[best.seed.isin(SEEDS)].copy()
        best["experiment"] = exp
        best_rows.append(best)

        logs = pd.concat([read_run(p) for p in metrics.glob("*_runs.csv")], ignore_index=True)
        logs["model_type"] = logs.model_type.str.lower()
        logs["optimizer"] = logs.optimizer.str.lower()
        logs["seed"] = pd.to_numeric(logs.seed).astype(int)
        logs["candidate_id"] = pd.to_numeric(logs.candidate_id).astype(int)
        logs["fitness"] = pd.to_numeric(logs.fitness)
        logs["cache_hit"] = logs.cache_hit.astype(str).str.lower().eq("true")
        logs = logs[logs.seed.isin(SEEDS)]
        for (model, optimizer, seed), run in logs.groupby(["model_type", "optimizer", "seed"]):
            run = run.sort_values("candidate_id")
            best_so_far = run.fitness.cummax().to_numpy()
            first, final = float(best_so_far[0]), float(best_so_far[-1])
            threshold = first + .95 * (final - first)
            idx = int(np.flatnonzero(best_so_far >= threshold)[0])
            through = run.iloc[:idx + 1]
            calls = int(through.candidate_id.iloc[-1])
            fits = int((~through.cache_hit).sum()) * folds
            effort_rows.append({"experiment": exp, "folds_per_candidate": folds,
                                "model_type": model, "optimizer": optimizer, "seed": seed,
                                "objective_evaluations_to_95pct_gain": calls,
                                "actual_model_fits_to_95pct_gain": fits,
                                "threshold_validation_fitness": threshold,
                                "initial_best_fitness": first, "final_best_fitness": final})
    return pd.concat(best_rows, ignore_index=True), pd.DataFrame(effort_rows)


def save(fig, name):
    fig.savefig(FIG_DIR / name, format="pdf", bbox_inches="tight", metadata={"Creator": "Matplotlib"})
    plt.close(fig)


def plot_exp1_mcc(best):
    data = best[best.experiment.eq("exp1_mcc_f1_holdout")]
    fig, axs = plt.subplots(2, 2, figsize=(FIGURE_MULTIPANEL[0], 5.0), sharey=True)
    for ax, model in zip(axs.flat, MODELS):
        d = data[data.model_type.eq(model)]
        for x, opt in enumerate(OPTIMIZERS):
            v = d[d.optimizer.eq(opt)].mcc_test.to_numpy(float)
            ax.errorbar(x, v.mean(), yerr=v.std(ddof=1), marker=OPTIMIZER_MARKERS[opt],
                        color=OPTIMIZER_COLORS[opt], capsize=2.5, linewidth=1.0, markersize=5)
        ax.set_title(MODEL_LABELS[model])
        ax.set_xticks(range(5), [OPT_LABEL[o] for o in OPTIMIZERS])
        ax.grid(axis="x", visible=False)
    axs[0, 0].set_ylabel("Locked-test MCC")
    axs[1, 0].set_ylabel("Locked-test MCC")
    fig.suptitle("Experiment 1 | MCC/$F_1$ holdout", y=1.01, fontsize=9.5, fontweight="bold")
    fig.supxlabel("Optimizer")
    fig.subplots_adjust(top=.89, bottom=.13, hspace=.48, wspace=.12)
    save(fig, "exp1_holdout_mcc_by_optimizer.pdf")


def plot_holdout_accuracy(best):
    data = best[best.experiment.isin(("exp1_mcc_f1_holdout", "exp2_accuracy_holdout"))]
    fig, axs = plt.subplots(1, 2, figsize=(FIGURE_MULTIPANEL[0], 4.8), sharey=True)
    model_offsets = np.linspace(-.24, .24, 4)
    for ax, exp, title in zip(axs, ("exp1_mcc_f1_holdout", "exp2_accuracy_holdout"),
                              ("Exp. 1 | MCC/$F_1$ fitness", "Exp. 2 | weighted-accuracy fitness")):
        d = data[data.experiment.eq(exp)]
        for mi, model in enumerate(MODELS):
            for oi, opt in enumerate(OPTIMIZERS):
                v = d[(d.model_type.eq(model)) & (d.optimizer.eq(opt))].accuracy_test.to_numpy(float)
                x = oi + model_offsets[mi]
                ax.errorbar(x, v.mean(), yerr=v.std(ddof=1), marker=OPTIMIZER_MARKERS[opt],
                            color=MODEL_COLORS[model], capsize=2, linewidth=.9, markersize=4.5)
        ax.set_title(title)
        ax.set_xticks(range(5), [OPT_LABEL[o] for o in OPTIMIZERS])
        ax.grid(axis="x", visible=False)
    axs[0].set_ylabel("Locked-test accuracy")
    fig.supxlabel("Optimizer (model encoded by color)", y=.07)
    handles = [Line2D([0], [0], color=MODEL_COLORS[m], marker="o", linestyle="none", label=MODEL_LABELS[m]) for m in MODELS]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(.5, 1.0), ncol=4)
    fig.subplots_adjust(top=.78, bottom=.20, wspace=.12)
    save(fig, "exp1_exp2_holdout_accuracy.pdf")


def plot_exp3_accuracy(best):
    data = best[best.experiment.eq("exp3_accuracy_temporal_cv")]
    fig, axs = plt.subplots(2, 2, figsize=(FIGURE_MULTIPANEL[0], 5.0), sharey=True)
    for ax, model in zip(axs.flat, MODELS):
        d = data[data.model_type.eq(model)]
        for x, opt in enumerate(OPTIMIZERS):
            v = d[d.optimizer.eq(opt)].accuracy_test.to_numpy(float)
            ax.errorbar(x, v.mean(), yerr=v.std(ddof=1), marker=OPTIMIZER_MARKERS[opt],
                        color=OPTIMIZER_COLORS[opt], capsize=2.5, linewidth=1.0, markersize=5)
        ax.set_title(MODEL_LABELS[model])
        ax.set_xticks(range(5), [OPT_LABEL[o] for o in OPTIMIZERS])
        ax.grid(axis="x", visible=False)
    axs[0, 0].set_ylabel("Locked-test accuracy")
    axs[1, 0].set_ylabel("Locked-test accuracy")
    fig.suptitle("Experiment 3 | temporal cross-validation accuracy objective", y=.99, fontsize=9.5, fontweight="bold")
    fig.supxlabel("Optimizer")
    handles = [Line2D([0], [0], color=OPTIMIZER_COLORS[o], marker=OPTIMIZER_MARKERS[o], linewidth=1, label=OPT_LABEL[o]) for o in OPTIMIZERS]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(.5, .925), ncol=5)
    fig.subplots_adjust(top=.83, bottom=.13, hspace=.48, wspace=.12)
    save(fig, "exp3_temporal_cv_accuracy_by_optimizer.pdf")


def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    best, effort = load_best_and_effort()
    effort.to_csv(ROOT / "article/manuscript/latest_zip_revision/tmp/effort_to_95_validation_gain_by_seed.csv", index=False)
    summary = (effort.groupby(["experiment", "model_type", "optimizer"])
               [["objective_evaluations_to_95pct_gain", "actual_model_fits_to_95pct_gain"]]
               .median().reset_index())
    summary.to_csv(ROOT / "article/manuscript/latest_zip_revision/tmp/effort_to_95_validation_gain_summary.csv", index=False)
    plot_exp1_mcc(best)
    plot_holdout_accuracy(best)
    plot_exp3_accuracy(best)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
