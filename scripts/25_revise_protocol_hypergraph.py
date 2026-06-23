"""Build revised protocol figures from the professor feedback.

The old protocol_hypergraph figure mixed MCC/F1 and accuracy readings in a
single visual scale. This version separates the reported metric by protocol:

- Exp 1: holdout validation with MCC/F1 fitness, reported as MCC on X_test.
- Exp 1: the same MCC/F1 fitness run, reported as accuracy on X_test.
- Exp 2: holdout validation with accuracy fitness, reported as accuracy on X_test.
- Exp 3: cross-validation with accuracy fitness, reported as accuracy on X_test.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "professor_presentation" / "figures" / "protocol_revised"
DOWNLOADS_DIR = Path.home() / "Downloads"

MODELS = ["cnn", "mlp", "rf", "svm"]
OPTIMIZERS = ["de", "ga", "gwo", "pso", "random_search"]
OPTIMIZER_LABELS = {
    "de": "DE",
    "ga": "GA",
    "gwo": "GWO",
    "pso": "PSO",
    "random_search": "RS",
}
MODEL_LABELS = {
    "cnn": "CNN",
    "mlp": "MLP",
    "rf": "RF",
    "svm": "SVM",
}
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
    title: str
    metrics_dir: Path
    metric: str
    ylabel: str
    ylim: tuple[float, float]


EXPERIMENTS = [
    Experiment(
        key="exp1_mcc",
        title="Exp 1 (Holdout + MCC/F1) - MCC on X_test",
        metrics_dir=ROOT / "outputs" / "article_official" / "metrics",
        metric="mcc_test",
        ylabel="Test MCC",
        ylim=(0.0, 0.36),
    ),
    Experiment(
        key="exp1_mcc_accuracy",
        title="Exp 1 (Holdout + MCC/F1) - Accuracy on X_test",
        metrics_dir=ROOT / "outputs" / "article_official" / "metrics",
        metric="accuracy_test",
        ylabel="Test Accuracy",
        ylim=(0.0, 0.80),
    ),
    Experiment(
        key="exp2_holdout_accuracy",
        title="Exp 2 (Holdout + Accuracy) - Accuracy on X_test",
        metrics_dir=ROOT / "outputs" / "article_official_accuracy_holdout" / "metrics",
        metric="accuracy_test",
        ylabel="Test Accuracy",
        ylim=(0.0, 0.80),
    ),
    Experiment(
        key="exp3_cv_accuracy",
        title="Exp 3 (CV + Accuracy) - Accuracy on X_test",
        metrics_dir=ROOT / "outputs" / "article_official_accuracy" / "metrics",
        metric="accuracy_test",
        ylabel="Test Accuracy",
        ylim=(0.0, 0.80),
    ),
]


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except pd.errors.ParserError:
        return pd.read_csv(path, engine="python", on_bad_lines="skip")


def summarize_experiment(exp: Experiment) -> pd.DataFrame:
    rows: list[dict[str, float | str]] = []
    for model in MODELS:
        for optimizer in OPTIMIZERS:
            stem = f"{model}_{optimizer}"
            best_path = exp.metrics_dir / f"{stem}_best_by_seed.csv"
            runs_path = exp.metrics_dir / f"{stem}_runs.csv"
            if not best_path.exists():
                raise FileNotFoundError(best_path)
            if not runs_path.exists():
                raise FileNotFoundError(runs_path)

            best = read_csv(best_path)
            best = best[best["seed"].isin([1, 2, 3])].copy()
            runs = read_csv(runs_path)
            runs = runs[runs["seed"].isin([1, 2, 3])].copy()

            rows.append(
                {
                    "experiment": exp.key,
                    "model": model,
                    "optimizer": optimizer,
                    "value": float(best[exp.metric].mean()),
                    "mcc_test": float(best["mcc_test"].mean()) if "mcc_test" in best else float("nan"),
                    "f1_test": float(best["f1_test"].mean()) if "f1_test" in best else float("nan"),
                    "accuracy_test": float(best["accuracy_test"].mean()) if "accuracy_test" in best else float("nan"),
                    "runtime_minutes": float(runs["train_time_seconds"].sum() / 60.0),
                }
            )
    return pd.DataFrame(rows)


def annotate_bars(ax: plt.Axes, part: pd.DataFrame, exp: Experiment) -> None:
    best_value = part["value"].max()
    fastest_runtime = part["runtime_minutes"].min()
    y0, y1 = exp.ylim
    value_offset = (y1 - y0) * 0.012
    time_offset = (y1 - y0) * 0.075

    for i, row in enumerate(part.itertuples(index=False)):
        is_best = abs(row.value - best_value) < 1e-12
        is_fastest = abs(row.runtime_minutes - fastest_runtime) < 1e-12
        value_color = "#B22222" if is_best else "#222222"
        time_color = "#137333" if is_fastest else "#1E40FF"
        ax.text(
            i,
            row.value + value_offset,
            f"{row.value:.4f}",
            ha="center",
            va="bottom",
            fontsize=7.5,
            color=value_color,
            fontweight="bold" if is_best else "normal",
        )
        ax.text(
            i,
            row.value + time_offset,
            f"{row.runtime_minutes:.1f}m",
            ha="center",
            va="bottom",
            fontsize=7.5,
            color=time_color,
            fontweight="bold" if is_fastest else "normal",
        )


def plot_experiment(df: pd.DataFrame, exp: Experiment, out_path: Path) -> Path:
    fig, axes = plt.subplots(1, len(MODELS), figsize=(16, 4.6), sharey=True)
    fig.suptitle(exp.title, fontsize=16, fontweight="bold", y=1.02)

    for ax, model in zip(axes, MODELS):
        part = df[df["model"] == model].set_index("optimizer").loc[OPTIMIZERS].reset_index()
        ax.bar(
            range(len(part)),
            part["value"],
            color=[COLORS[optimizer] for optimizer in part["optimizer"]],
            width=0.78,
            alpha=0.9,
        )
        annotate_bars(ax, part, exp)
        ax.set_title(MODEL_LABELS[model], fontsize=11, fontweight="bold")
        ax.set_xticks(range(len(part)))
        ax.set_xticklabels([OPTIMIZER_LABELS[optimizer] for optimizer in part["optimizer"]], fontsize=9)
        ax.set_ylim(*exp.ylim)
        ax.grid(axis="y", color="#d0d0d0", linewidth=0.8, alpha=0.8)
        ax.set_axisbelow(True)
        if ax is axes[0]:
            ax.set_ylabel(exp.ylabel, fontsize=10)

    fig.text(0.5, -0.02, "Red value = best score in model panel; green time = fastest optimizer in model panel.", ha="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_combined(summaries: dict[str, pd.DataFrame], out_path: Path) -> Path:
    fig, axes = plt.subplots(len(EXPERIMENTS), len(MODELS), figsize=(19, 12), sharex=False)
    fig.set_size_inches(19, 15)
    fig.suptitle("Benchmark Results by Protocol: MCC and Accuracy Reported Separately", fontsize=18, fontweight="bold", y=0.995)

    for row_idx, exp in enumerate(EXPERIMENTS):
        df = summaries[exp.key]
        for col_idx, model in enumerate(MODELS):
            ax = axes[row_idx, col_idx]
            part = df[df["model"] == model].set_index("optimizer").loc[OPTIMIZERS].reset_index()
            ax.bar(
                range(len(part)),
                part["value"],
                color=[COLORS[optimizer] for optimizer in part["optimizer"]],
                width=0.78,
                alpha=0.9,
            )
            annotate_bars(ax, part, exp)
            ax.set_title(f"{exp.title} | {MODEL_LABELS[model]}", fontsize=10.5, fontweight="bold")
            ax.set_xticks(range(len(part)))
            ax.set_xticklabels([OPTIMIZER_LABELS[optimizer] for optimizer in part["optimizer"]], fontsize=8.5)
            ax.set_ylim(*exp.ylim)
            ax.grid(axis="y", color="#d0d0d0", linewidth=0.8, alpha=0.8)
            ax.set_axisbelow(True)
            if col_idx == 0:
                ax.set_ylabel(exp.ylabel, fontsize=9.5)

    fig.text(0.5, 0.012, "Red value = best score in model panel; green time = fastest optimizer in model panel.", ha="center", fontsize=9)
    fig.tight_layout(rect=[0, 0.02, 1, 0.97])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_exp1_mcc_and_accuracy(summaries: dict[str, pd.DataFrame], out_path: Path) -> Path:
    exps = [EXPERIMENTS[0], EXPERIMENTS[1]]
    fig, axes = plt.subplots(len(exps), len(MODELS), figsize=(19, 7.8), sharex=False)
    fig.suptitle("Exp 1 (Holdout + MCC/F1): MCC and Accuracy on X_test", fontsize=18, fontweight="bold", y=0.995)

    for row_idx, exp in enumerate(exps):
        df = summaries[exp.key]
        for col_idx, model in enumerate(MODELS):
            ax = axes[row_idx, col_idx]
            part = df[df["model"] == model].set_index("optimizer").loc[OPTIMIZERS].reset_index()
            ax.bar(
                range(len(part)),
                part["value"],
                color=[COLORS[optimizer] for optimizer in part["optimizer"]],
                width=0.78,
                alpha=0.9,
            )
            annotate_bars(ax, part, exp)
            ax.set_title(f"{exp.ylabel} | {MODEL_LABELS[model]}", fontsize=10.5, fontweight="bold")
            ax.set_xticks(range(len(part)))
            ax.set_xticklabels([OPTIMIZER_LABELS[optimizer] for optimizer in part["optimizer"]], fontsize=8.5)
            ax.set_ylim(*exp.ylim)
            ax.grid(axis="y", color="#d0d0d0", linewidth=0.8, alpha=0.8)
            ax.set_axisbelow(True)
            if col_idx == 0:
                ax.set_ylabel(exp.ylabel, fontsize=9.5)

    fig.text(0.5, 0.012, "Red value = best score in model panel; green time = fastest optimizer in model panel.", ha="center", fontsize=9)
    fig.tight_layout(rect=[0, 0.02, 1, 0.955])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summaries = {exp.key: summarize_experiment(exp) for exp in EXPERIMENTS}
    pd.concat(summaries.values(), ignore_index=True).to_csv(OUT_DIR / "protocol_revised_summary.csv", index=False)

    outputs = [
        plot_experiment(summaries["exp1_mcc"], EXPERIMENTS[0], OUT_DIR / "protocol_exp1_mcc_only.png"),
        plot_experiment(summaries["exp1_mcc_accuracy"], EXPERIMENTS[1], OUT_DIR / "protocol_exp1_accuracy_from_mcc_f1.png"),
        plot_exp1_mcc_and_accuracy(summaries, OUT_DIR / "protocol_exp1_mcc_and_accuracy.png"),
        plot_experiment(summaries["exp2_holdout_accuracy"], EXPERIMENTS[2], OUT_DIR / "protocol_exp2_holdout_accuracy.png"),
        plot_experiment(summaries["exp3_cv_accuracy"], EXPERIMENTS[3], OUT_DIR / "protocol_exp3_cv_accuracy.png"),
        plot_combined(summaries, OUT_DIR / "protocol_hypergraph_revised.png"),
    ]

    for path in outputs:
        shutil.copy2(path, DOWNLOADS_DIR / path.name)

    print("Saved revised protocol figures:")
    for path in outputs:
        print(path)
        print(DOWNLOADS_DIR / path.name)


if __name__ == "__main__":
    main()
