"""Plot MCC/F1 fitness benchmark performance by model and optimizer."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
METRICS_DIR = ROOT / "outputs" / "article_official" / "metrics"
OUT_DIR = ROOT / "outputs" / "comparative_analysis"

MODELS = ["mlp", "rf", "svm", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]
OPTIMIZER_LABELS = {
    "random_search": "Random Search",
    "ga": "GA",
    "pso": "PSO",
    "de": "DE",
    "gwo": "GWO",
}


def load_mcc_fitness_results() -> pd.DataFrame:
    frames = []
    for model in MODELS:
        for optimizer in OPTIMIZERS:
            path = METRICS_DIR / f"{model}_{optimizer}_best_by_seed.csv"
            if not path.exists():
                print(f"Missing file: {path.relative_to(ROOT)}")
                continue

            df = pd.read_csv(path)
            df = df[df["seed"].isin([1, 2, 3])].copy()
            df["model_label"] = model.upper()
            df["optimizer_label"] = OPTIMIZER_LABELS[optimizer]
            frames.append(df)

    if not frames:
        raise SystemExit("No MCC/F1 benchmark files found.")
    return pd.concat(frames, ignore_index=True)


def plot_metric(df: pd.DataFrame, metric: str, ylabel: str, stem: str) -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.15)
    fig, ax = plt.subplots(figsize=(12, 6.5))

    sns.barplot(
        data=df,
        x="model_label",
        y=metric,
        hue="optimizer_label",
        order=[model.upper() for model in MODELS],
        hue_order=[OPTIMIZER_LABELS[optimizer] for optimizer in OPTIMIZERS],
        errorbar="sd",
        capsize=0.08,
        palette="tab10",
        ax=ax,
    )

    ax.set_title(f"MCC/F1 fitness benchmark - {ylabel} by model and optimizer")
    ax.set_xlabel("Model")
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=0.35)
    ax.legend(title="Optimizer", frameon=False, ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.12))
    fig.tight_layout()

    outputs = [OUT_DIR / f"{stem}.png", OUT_DIR / f"{stem}.pdf"]
    for path in outputs:
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return outputs


def main() -> None:
    df = load_mcc_fitness_results()
    summary = (
        df.groupby(["model_label", "optimizer_label"])[["mcc_test", "accuracy_test"]]
        .agg(["mean", "std"])
        .reset_index()
    )
    summary.columns = ["_".join(col).rstrip("_") for col in summary.columns]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = OUT_DIR / "mcc_fitness_model_optimizer_summary.csv"
    summary.to_csv(summary_path, index=False)

    paths = [summary_path]
    paths.extend(plot_metric(df, "mcc_test", "MCC on X_test", "mcc_fitness_mcc_test_by_model_optimizer"))
    paths.extend(
        plot_metric(
            df,
            "accuracy_test",
            "Accuracy on X_test",
            "mcc_fitness_accuracy_test_by_model_optimizer",
        )
    )

    print("Saved MCC/F1 fitness plots:")
    for path in paths:
        print(f"- {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
