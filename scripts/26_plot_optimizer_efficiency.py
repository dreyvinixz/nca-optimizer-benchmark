"""Plot optimizer computational-efficiency figures from saved run logs.

The figures use the recorded objective-function evaluations in *_runs.csv.
Each row is treated as one fitness evaluation, which usually corresponds to
training/evaluating one model candidate.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "professor_presentation" / "figures" / "optimizer_efficiency"
DOWNLOADS_DIR = Path.home() / "Downloads"

SEEDS = [1, 2, 3]
MODELS = ["cnn", "mlp", "rf", "svm"]
OPTIMIZERS = ["de", "ga", "gwo", "pso", "random_search"]
BUDGETS = [50, 100, 250, 500, 1000]

MODEL_LABELS = {"cnn": "CNN", "mlp": "MLP", "rf": "RF", "svm": "SVM"}
OPTIMIZER_LABELS = {"de": "DE", "ga": "GA", "gwo": "GWO", "pso": "PSO", "random_search": "RS"}
COLORS = {
    "de": "#4C72B0",
    "ga": "#DD8452",
    "gwo": "#55A868",
    "pso": "#C44E52",
    "random_search": "#8172B2",
}


@dataclass(frozen=True)
class Experiment:
    key: str
    label: str
    metrics_dir: Path


EXPERIMENTS = [
    Experiment("exp1_mcc_f1", "Exp 1 - Holdout + MCC/F1", ROOT / "outputs" / "article_official" / "metrics"),
    Experiment(
        "exp2_holdout_accuracy",
        "Exp 2 - Holdout + Accuracy",
        ROOT / "outputs" / "article_official_accuracy_holdout" / "metrics",
    ),
    Experiment("exp3_cv_accuracy", "Exp 3 - CV + Accuracy", ROOT / "outputs" / "article_official_accuracy" / "metrics"),
]


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except pd.errors.ParserError:
        return pd.read_csv(path, engine="python", on_bad_lines="skip")


def load_runs() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    missing: list[Path] = []
    for exp in EXPERIMENTS:
        for model in MODELS:
            for optimizer in OPTIMIZERS:
                path = exp.metrics_dir / f"{model}_{optimizer}_runs.csv"
                if not path.exists():
                    missing.append(path)
                    continue
                df = read_csv(path)
                df = df[df["seed"].isin(SEEDS)].copy()
                df["experiment"] = exp.key
                df["experiment_label"] = exp.label
                df["model"] = model
                df["optimizer"] = optimizer
                frames.append(df)
    if missing:
        raise FileNotFoundError("Missing run logs:\n" + "\n".join(str(path) for path in missing))
    data = pd.concat(frames, ignore_index=True)
    data["train_time_seconds"] = pd.to_numeric(data["train_time_seconds"], errors="coerce").fillna(0.0)
    data["fitness"] = pd.to_numeric(data["fitness"], errors="coerce")
    data = data.dropna(subset=["fitness"]).copy()
    data = data.sort_values(["experiment", "model", "optimizer", "seed", "candidate_id"]).reset_index(drop=True)
    grouped = data.groupby(["experiment", "model", "optimizer", "seed"], sort=False)
    data["evaluation"] = grouped.cumcount() + 1
    data["best_so_far"] = grouped["fitness"].cummax()
    data["runtime_minutes_so_far"] = grouped["train_time_seconds"].cumsum() / 60.0
    return data


def progress_frame(runs: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    run_summaries = []
    budget_rows = []
    for keys, group in runs.groupby(["experiment", "experiment_label", "model", "optimizer", "seed"], sort=False):
        exp_key, exp_label, model, optimizer, seed = keys
        group = group.sort_values("evaluation").copy()
        first_best = float(group["best_so_far"].iloc[0])
        final_best = float(group["best_so_far"].iloc[-1])
        total_evaluations = int(group["evaluation"].iloc[-1])
        total_runtime = float(group["runtime_minutes_so_far"].iloc[-1])
        denominator = final_best - first_best
        if abs(denominator) < 1e-12:
            progress = np.ones(len(group))
        else:
            progress = ((group["best_so_far"].to_numpy() - first_best) / denominator).clip(0.0, 1.0)
        group["progress_to_final"] = progress

        target = final_best if abs(denominator) < 1e-12 else first_best + 0.95 * denominator
        reached = group[group["best_so_far"] >= target]
        if reached.empty:
            eval_to_95 = total_evaluations
            time_to_95 = total_runtime
        else:
            eval_to_95 = int(reached["evaluation"].iloc[0])
            time_to_95 = float(reached["runtime_minutes_so_far"].iloc[0])

        auc_progress = float(np.trapezoid(group["progress_to_final"], group["evaluation"]) / max(total_evaluations - 1, 1))
        run_summaries.append(
            {
                "experiment": exp_key,
                "experiment_label": exp_label,
                "model": model,
                "optimizer": optimizer,
                "seed": seed,
                "first_fitness": first_best,
                "best_fitness": final_best,
                "total_evaluations": total_evaluations,
                "total_runtime_minutes": total_runtime,
                "eval_to_95pct_final": eval_to_95,
                "time_to_95pct_final_minutes": time_to_95,
                "auc_progress": auc_progress,
            }
        )

        for budget in BUDGETS:
            at_budget = group[group["evaluation"] <= budget]
            if at_budget.empty:
                row = group.iloc[0]
            else:
                row = at_budget.iloc[-1]
            budget_rows.append(
                {
                    "experiment": exp_key,
                    "experiment_label": exp_label,
                    "model": model,
                    "optimizer": optimizer,
                    "seed": seed,
                    "budget": budget,
                    "best_fitness_at_budget": float(row["best_so_far"]),
                    "progress_to_final_at_budget": float(row["progress_to_final"]),
                    "runtime_minutes_at_budget": float(row["runtime_minutes_so_far"]),
                }
            )
    return pd.DataFrame(run_summaries), pd.DataFrame(budget_rows)


def plot_convergence(runs: pd.DataFrame, out_path: Path) -> Path:
    fig, axes = plt.subplots(1, len(EXPERIMENTS), figsize=(17, 4.8), sharex=True)
    fig.suptitle("Optimizer Convergence: Best Fitness So Far vs Fitness Evaluations", fontsize=16, fontweight="bold")

    for ax, exp in zip(axes, EXPERIMENTS):
        part = runs[runs["experiment"] == exp.key]
        for optimizer in OPTIMIZERS:
            opt = part[part["optimizer"] == optimizer]
            curve = opt.groupby("evaluation")["best_so_far"].mean().reset_index()
            ax.plot(
                curve["evaluation"],
                curve["best_so_far"],
                label=OPTIMIZER_LABELS[optimizer],
                color=COLORS[optimizer],
                linewidth=2.0,
            )
        ax.set_title(exp.label, fontsize=11, fontweight="bold")
        ax.set_xlabel("Fitness evaluations")
        ax.grid(True, alpha=0.28)
        if ax is axes[0]:
            ax.set_ylabel("Mean best fitness so far")
    axes[-1].legend(title="Optimizer", bbox_to_anchor=(1.02, 1.0), loc="upper left")
    fig.tight_layout(rect=[0, 0, 0.95, 0.92])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_fixed_budget_heatmap(budgets: pd.DataFrame, out_path: Path) -> Path:
    fig, axes = plt.subplots(1, len(EXPERIMENTS), figsize=(17, 4.8), sharey=True)
    fig.suptitle("Fraction of Final Improvement Reached at Fixed Evaluation Budgets", fontsize=16, fontweight="bold")
    for ax, exp in zip(axes, EXPERIMENTS):
        part = budgets[budgets["experiment"] == exp.key]
        pivot = (
            part.groupby(["optimizer", "budget"])["progress_to_final_at_budget"]
            .mean()
            .unstack("budget")
            .loc[OPTIMIZERS, BUDGETS]
        )
        image = ax.imshow(pivot.to_numpy(), vmin=0, vmax=1, cmap="YlGnBu", aspect="auto")
        ax.set_title(exp.label, fontsize=11, fontweight="bold")
        ax.set_xticks(range(len(BUDGETS)))
        ax.set_xticklabels(BUDGETS)
        ax.set_yticks(range(len(OPTIMIZERS)))
        ax.set_yticklabels([OPTIMIZER_LABELS[optimizer] for optimizer in OPTIMIZERS])
        ax.set_xlabel("Evaluation budget")
        for i in range(len(OPTIMIZERS)):
            for j in range(len(BUDGETS)):
                value = pivot.to_numpy()[i, j]
                ax.text(j, i, f"{value:.2f}", ha="center", va="center", fontsize=8, color="#111111")
    fig.colorbar(image, ax=axes, shrink=0.82, label="Mean progress to final best")
    fig.tight_layout(rect=[0, 0, 0.93, 0.92])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_metric_by_model(summary: pd.DataFrame, metric: str, ylabel: str, title: str, out_path: Path) -> Path:
    fig, axes = plt.subplots(len(EXPERIMENTS), len(MODELS), figsize=(18, 10), sharey=False)
    fig.suptitle(title, fontsize=16, fontweight="bold")
    for row_idx, exp in enumerate(EXPERIMENTS):
        for col_idx, model in enumerate(MODELS):
            ax = axes[row_idx, col_idx]
            part = summary[(summary["experiment"] == exp.key) & (summary["model"] == model)]
            values = part.groupby("optimizer")[metric].median().reindex(OPTIMIZERS)
            ax.bar(
                range(len(OPTIMIZERS)),
                values.to_numpy(),
                color=[COLORS[optimizer] for optimizer in OPTIMIZERS],
                alpha=0.9,
            )
            best_idx = int(np.nanargmin(values.to_numpy()))
            for idx, value in enumerate(values.to_numpy()):
                color = "#B22222" if idx == best_idx else "#222222"
                ax.text(idx, value, f"{value:.1f}", ha="center", va="bottom", fontsize=7.5, color=color, fontweight="bold" if idx == best_idx else "normal")
            ax.set_title(f"{exp.label} | {MODEL_LABELS[model]}", fontsize=9.5, fontweight="bold")
            ax.set_xticks(range(len(OPTIMIZERS)))
            ax.set_xticklabels([OPTIMIZER_LABELS[optimizer] for optimizer in OPTIMIZERS], fontsize=8)
            ax.grid(axis="y", alpha=0.28)
            if col_idx == 0:
                ax.set_ylabel(ylabel, fontsize=9)
    fig.text(0.5, 0.01, "Red value = lowest median cost to reach 95% of the final best fitness.", ha="center", fontsize=9)
    fig.tight_layout(rect=[0, 0.025, 1, 0.94])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_optimizer_summary(summary: pd.DataFrame, out_path: Path) -> Path:
    agg = (
        summary.groupby(["experiment", "experiment_label", "optimizer"])
        .agg(
            eval_to_95=("eval_to_95pct_final", "median"),
            time_to_95=("time_to_95pct_final_minutes", "median"),
            auc_progress=("auc_progress", "mean"),
            total_runtime=("total_runtime_minutes", "median"),
        )
        .reset_index()
    )
    fig, axes = plt.subplots(len(EXPERIMENTS), 3, figsize=(16, 10))
    fig.suptitle("Optimizer Efficiency Summary", fontsize=16, fontweight="bold")
    metrics = [
        ("eval_to_95", "Evaluations to 95% final best", "lower"),
        ("time_to_95", "Minutes to 95% final best", "lower"),
        ("auc_progress", "AUC of convergence progress", "higher"),
    ]
    for row_idx, exp in enumerate(EXPERIMENTS):
        part = agg[agg["experiment"] == exp.key].set_index("optimizer").loc[OPTIMIZERS].reset_index()
        for col_idx, (metric, title, direction) in enumerate(metrics):
            ax = axes[row_idx, col_idx]
            values = part[metric].to_numpy()
            ax.bar(
                range(len(OPTIMIZERS)),
                values,
                color=[COLORS[optimizer] for optimizer in OPTIMIZERS],
                alpha=0.9,
            )
            best_idx = int(np.nanargmin(values) if direction == "lower" else np.nanargmax(values))
            for idx, value in enumerate(values):
                color = "#B22222" if idx == best_idx else "#222222"
                ax.text(idx, value, f"{value:.2f}" if metric == "auc_progress" else f"{value:.1f}", ha="center", va="bottom", fontsize=8, color=color, fontweight="bold" if idx == best_idx else "normal")
            ax.set_title(f"{exp.label}\n{title}", fontsize=9.5, fontweight="bold")
            ax.set_xticks(range(len(OPTIMIZERS)))
            ax.set_xticklabels([OPTIMIZER_LABELS[optimizer] for optimizer in OPTIMIZERS], fontsize=8)
            ax.grid(axis="y", alpha=0.28)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def write_tables(summary: pd.DataFrame, budgets: pd.DataFrame) -> None:
    summary.to_csv(OUT_DIR / "optimizer_efficiency_by_run.csv", index=False)
    budgets.to_csv(OUT_DIR / "optimizer_efficiency_fixed_budgets.csv", index=False)
    optimizer_summary = (
        summary.groupby(["experiment", "experiment_label", "optimizer"])
        .agg(
            eval_to_95_median=("eval_to_95pct_final", "median"),
            time_to_95_median=("time_to_95pct_final_minutes", "median"),
            auc_progress_mean=("auc_progress", "mean"),
            total_evaluations_median=("total_evaluations", "median"),
            total_runtime_median=("total_runtime_minutes", "median"),
            best_fitness_mean=("best_fitness", "mean"),
        )
        .reset_index()
    )
    optimizer_summary.to_csv(OUT_DIR / "optimizer_efficiency_summary.csv", index=False)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    runs = load_runs()
    summary, budgets = progress_frame(runs)
    write_tables(summary, budgets)

    outputs = [
        plot_convergence(runs, OUT_DIR / "efficiency_convergence_best_so_far.png"),
        plot_fixed_budget_heatmap(budgets, OUT_DIR / "efficiency_fixed_budget_progress.png"),
        plot_metric_by_model(
            summary,
            "eval_to_95pct_final",
            "Evaluations",
            "Evaluations Needed to Reach 95% of Final Best Fitness",
            OUT_DIR / "efficiency_evaluations_to_95_by_model.png",
        ),
        plot_metric_by_model(
            summary,
            "time_to_95pct_final_minutes",
            "Minutes",
            "Runtime Needed to Reach 95% of Final Best Fitness",
            OUT_DIR / "efficiency_runtime_to_95_by_model.png",
        ),
        plot_optimizer_summary(summary, OUT_DIR / "efficiency_optimizer_summary.png"),
    ]

    for path in outputs:
        shutil.copy2(path, DOWNLOADS_DIR / path.name)

    print("Saved optimizer-efficiency figures:")
    for path in outputs:
        print(path)
        print(DOWNLOADS_DIR / path.name)


if __name__ == "__main__":
    main()
