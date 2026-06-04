"""Compare CPU and CUDA MLP benchmark timings.

Reads:
    outputs/phase2/metrics/mlp_ga_runs.csv
    outputs/phase2/gpu_test/mlp_ga_gpu_runs.csv

Writes:
    outputs/phase2/gpu_test/gpu_vs_cpu_comparison.csv
    outputs/phase2/gpu_test/gpu_vs_cpu_speedup_report.md
    outputs/phase2/gpu_test/gpu_vs_cpu_comparison.png
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    HAS_MPL = True
except ImportError:
    HAS_MPL = False


def load_data(root: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load CPU and GPU run CSVs."""
    cpu_path = root / "outputs" / "phase2" / "metrics" / "mlp_ga_runs.csv"
    gpu_path = root / "outputs" / "phase2" / "gpu_test" / "mlp_ga_gpu_runs.csv"

    if not cpu_path.exists():
        raise FileNotFoundError(f"CPU results not found: {cpu_path}")
    if not gpu_path.exists():
        raise FileNotFoundError(f"GPU results not found: {gpu_path}")

    return pd.read_csv(cpu_path), pd.read_csv(gpu_path)


def _backend_label(df: pd.DataFrame, fallback: str) -> str:
    if "model_backend" not in df.columns or df.empty:
        return fallback
    values = sorted(str(v) for v in df["model_backend"].dropna().unique())
    return f"{fallback} ({', '.join(values)})" if values else fallback


def _gpu_total_wall_seconds(df_gpu: pd.DataFrame) -> float:
    if {"seed", "generation", "batch_total_time"}.issubset(df_gpu.columns):
        return float(df_gpu.drop_duplicates(["seed", "generation"])["batch_total_time"].sum())
    if "wall_time_per_eval" in df_gpu.columns:
        return float(df_gpu["wall_time_per_eval"].sum())
    return float(df_gpu["train_time_seconds"].sum())


def _stats(df: pd.DataFrame, backend: str, time_values: pd.Series, total_time: float) -> dict[str, float | int | str]:
    return {
        "Backend": backend,
        "Evaluations": int(len(df)),
        "Avg wall/eval (s)": float(time_values.mean()),
        "Min wall/eval (s)": float(time_values.min()),
        "Max wall/eval (s)": float(time_values.max()),
        "Total wall time (s)": float(total_time),
        "Best fitness": float(df["fitness"].max()),
        "Avg fitness": float(df["fitness"].mean()),
        "Best MCC": float(df["mcc"].max()),
        "Best F1": float(df["f1"].max()),
    }


def compare(df_cpu: pd.DataFrame, df_gpu: pd.DataFrame) -> tuple[pd.DataFrame, float]:
    """Build comparison summary table and speedup value."""
    n_gpu = len(df_gpu)
    if n_gpu == 0:
        raise ValueError("GPU results are empty")

    df_cpu_matched = df_cpu.head(n_gpu)
    cpu_times = df_cpu_matched["train_time_seconds"].astype(float)
    gpu_times = (
        df_gpu["wall_time_per_eval"].astype(float)
        if "wall_time_per_eval" in df_gpu.columns
        else df_gpu["train_time_seconds"].astype(float)
    )

    cpu_stats = _stats(
        df_cpu_matched,
        _backend_label(df_cpu_matched, "CPU"),
        cpu_times,
        float(cpu_times.sum()),
    )
    gpu_stats = _stats(
        df_gpu,
        _backend_label(df_gpu, "GPU"),
        gpu_times,
        _gpu_total_wall_seconds(df_gpu),
    )

    if "cuda_kernel_time" in df_gpu.columns:
        gpu_stats["Avg CUDA kernel/eval (s)"] = float(df_gpu["cuda_kernel_time"].mean())

    summary = pd.DataFrame([cpu_stats, gpu_stats])
    speedup = cpu_stats["Avg wall/eval (s)"] / max(gpu_stats["Avg wall/eval (s)"], 1e-9)
    return summary, float(speedup)


def plot_comparison(df_cpu: pd.DataFrame, df_gpu: pd.DataFrame, output_path: Path) -> None:
    """Generate comparison bar chart."""
    if not HAS_MPL:
        print("matplotlib not available, skipping plot")
        return

    n_gpu = len(df_gpu)
    df_cpu_matched = df_cpu.head(n_gpu)
    cpu_time = float(df_cpu_matched["train_time_seconds"].mean())
    gpu_time = float(
        df_gpu["wall_time_per_eval"].mean()
        if "wall_time_per_eval" in df_gpu.columns
        else df_gpu["train_time_seconds"].mean()
    )
    cpu_total = float(df_cpu_matched["train_time_seconds"].sum())
    gpu_total = _gpu_total_wall_seconds(df_gpu)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("GPU CUDA vs CPU TensorFlow - MLP Training", fontsize=14, fontweight="bold")

    colors = ["#d95f02", "#1b9e77"]
    panels = [
        ("Avg Wall Time per Evaluation", "Seconds", [cpu_time, gpu_time], ".2f"),
        (f"Total Wall Time ({n_gpu} evals)", "Seconds", [cpu_total, gpu_total], ".1f"),
        ("Best Fitness Achieved", "Fitness", [df_cpu_matched["fitness"].max(), df_gpu["fitness"].max()], ".4f"),
    ]

    for ax, (title, ylabel, values, fmt) in zip(axes, panels):
        bars = ax.bar(["CPU", "GPU"], values, color=colors, edgecolor="black", linewidth=0.5)
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                format(float(value), fmt),
                ha="center",
                va="bottom",
                fontweight="bold",
            )

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Chart saved to {output_path}")


def write_report(
    summary: pd.DataFrame,
    speedup: float,
    df_cpu: pd.DataFrame,
    df_gpu: pd.DataFrame,
    output_path: Path,
) -> None:
    """Write a short Markdown speedup report."""
    n_gpu = len(df_gpu)
    cpu_avg = float(df_cpu.head(n_gpu)["train_time_seconds"].mean())
    gpu_avg = float(
        df_gpu["wall_time_per_eval"].mean()
        if "wall_time_per_eval" in df_gpu.columns
        else df_gpu["train_time_seconds"].mean()
    )
    official_evals = 5 * 1000 * 5
    try:
        summary_table = summary.to_markdown(index=False)
    except ImportError:
        summary_table = "```\n" + summary.to_string(index=False) + "\n```"

    lines = [
        "# GPU vs CPU Speedup Report",
        "",
        f"- Matched evaluations: {n_gpu}",
        f"- CPU average wall time/eval: {cpu_avg:.4f}s",
        f"- GPU average wall time/eval: {gpu_avg:.4f}s",
        f"- Observed speedup: {speedup:.2f}x",
        f"- Projected CPU time for {official_evals:,} evals: {cpu_avg * official_evals / 3600:.2f} hours",
        f"- Projected GPU time for {official_evals:,} evals: {gpu_avg * official_evals / 3600:.2f} hours",
        "",
        "## Summary Table",
        "",
        summary_table,
        "",
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report saved to {output_path}")


def main() -> None:
    df_cpu, df_gpu = load_data(ROOT)
    summary, speedup = compare(df_cpu, df_gpu)

    print()
    print("=" * 70)
    print("  GPU vs CPU - Benchmark Comparison")
    print("=" * 70)
    print()
    print(summary.to_string(index=False))
    print()
    print(f"  Speedup: {speedup:.2f}x")
    print("=" * 70)

    output_dir = ROOT / "outputs" / "phase2" / "gpu_test"
    output_dir.mkdir(parents=True, exist_ok=True)
    summary.to_csv(output_dir / "gpu_vs_cpu_comparison.csv", index=False)
    write_report(summary, speedup, df_cpu, df_gpu, output_dir / "gpu_vs_cpu_speedup_report.md")
    plot_comparison(df_cpu, df_gpu, output_dir / "gpu_vs_cpu_comparison.png")


if __name__ == "__main__":
    main()
