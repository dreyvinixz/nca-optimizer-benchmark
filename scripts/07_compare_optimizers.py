from __future__ import annotations

import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
if VENV_PYTHON.exists() and Path(sys.executable).resolve() != VENV_PYTHON.resolve():
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), *sys.argv])
sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt
import pandas as pd

from src.utils.io import load_project_configs, project_path, write_text
from src.utils.logger import get_logger


OPTIMIZERS = ["random_search", "ga", "pso"]


def _load_existing(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required benchmark output not found: {path}")
    return pd.read_csv(path)


def main() -> None:
    logger = get_logger("compare_optimizers", "logs/experiments/compare_optimizers.log")
    config = load_project_configs()
    paths = config["paths"]["outputs"]

    best_frames = []
    convergence_frames = []
    for optimizer in OPTIMIZERS:
        best_frames.append(_load_existing(project_path(f"{paths['metrics']}/{optimizer}_best_by_seed.csv")))
        convergence_frames.append(_load_existing(project_path(f"{paths['convergence']}/{optimizer}_convergence.csv")))

    best = pd.concat(best_frames, ignore_index=True)
    convergence = pd.concat(convergence_frames, ignore_index=True)

    metric_columns = [
        "accuracy_test",
        "balanced_accuracy_test",
        "precision_test",
        "recall_test",
        "f1_test",
        "mcc_test",
        "auc_roc_test",
        "auc_pr_test",
        "runtime_seconds_test",
        "best_validation_fitness",
    ]
    comparison = (
        best.groupby("optimizer")[metric_columns]
        .agg(["mean", "std"])
        .reset_index()
    )
    comparison.columns = [
        column[0] if column[1] == "" else f"{column[0]}_{column[1]}"
        for column in comparison.columns.to_flat_index()
    ]
    comparison_path = project_path(f"{paths['tables']}/optimizer_comparison.csv")
    comparison_path.parent.mkdir(parents=True, exist_ok=True)
    comparison.to_csv(comparison_path, index=False)

    fig_path = project_path(f"{paths['figures']}/optimizer_convergence.png")
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(9, 5))
    grouped = (
        convergence.groupby(["optimizer", "evaluation_id"])["best_fitness_so_far"]
        .mean()
        .reset_index()
    )
    for optimizer in OPTIMIZERS:
        subset = grouped[grouped["optimizer"] == optimizer]
        plt.plot(subset["evaluation_id"], subset["best_fitness_so_far"], label=optimizer)
    plt.xlabel("fitness evaluations")
    plt.ylabel("best validation fitness")
    plt.title("Optimizer convergence")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=160)
    plt.close()

    metric_fig_path = project_path(f"{paths['figures']}/optimizer_metrics_comparison.png")
    metric_means = best.groupby("optimizer")[["f1_test", "mcc_test", "auc_roc_test", "auc_pr_test"]].mean()
    metric_means.plot(kind="bar", figsize=(9, 5))
    plt.ylabel("mean test metric")
    plt.title("Test metric comparison")
    plt.tight_layout()
    plt.savefig(metric_fig_path, dpi=160)
    plt.close()

    summary_lines = [
        "# Optimizer Benchmark Summary",
        "",
        "This report is generated from saved CSV outputs, not manually typed metrics.",
        "",
        "## Mean Test Metrics",
        "",
        "```text",
        metric_means.round(4).to_string(),
        "```",
        "",
        "## Protocol",
        "",
        "- Dataset: `data/raw/merged_output.csv`",
        "- Features: historical `InfoGain_[7]`",
        "- Split: temporal holdout, 60% train, 20% validation, 20% test",
        "- Fitness: `0.60 * MCC + 0.40 * F1`",
        "- X-axis for convergence: fitness evaluations",
        "",
        "## Official Experiment Status",
        "",
        f"- Model Backend: `{best['backend'].iloc[0] if 'backend' in best.columns else 'unknown'}`",
        f"- Official Experiment: `{bool(best['official_experiment'].iloc[0]) if 'official_experiment' in best.columns else False}`",
    ]
    write_text(f"{paths['reports']}/optimizer_benchmark_summary.md", "\n".join(summary_lines))
    logger.info("Optimizer comparison outputs saved")


if __name__ == "__main__":
    main()
