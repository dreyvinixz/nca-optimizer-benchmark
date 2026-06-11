"""Compare MCC/F1 and Accuracy-CV fitness modes on the blind X_test split."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
MCC_DIR = ROOT / "outputs" / "article_official" / "metrics"
ACC_DIR = ROOT / "outputs" / "article_official_accuracy" / "metrics"
OUT_DIR = ROOT / "outputs" / "comparative_analysis"

OUT_DIR.mkdir(parents=True, exist_ok=True)

MODELS = ["mlp", "rf", "svm", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]
MODE_LABELS = {
    "mcc_f1": "MCC/F1",
    "accuracy_cv": "Accuracy-CV",
}
PRIMARY_METRICS = ["accuracy_test", "mcc_test"]
ALL_METRICS = [
    "accuracy_test",
    "balanced_accuracy_test",
    "mcc_test",
    "f1_test",
    "auc_roc_test",
    "auc_pr_test",
    "best_validation_fitness",
]


def load_data(dir_path: Path, mode_name: str) -> pd.DataFrame:
    dfs = []
    for model in MODELS:
        for optimizer in OPTIMIZERS:
            file = dir_path / f"{model}_{optimizer}_best_by_seed.csv"
            if not file.exists():
                print(f"Missing file: {file.relative_to(ROOT)}")
                continue
            df = pd.read_csv(file)
            df["source_file"] = str(file.relative_to(ROOT))
            df["model_type"] = model
            df["optimizer"] = optimizer
            df["fitness_mode"] = mode_name
            df["fitness_mode_label"] = MODE_LABELS[mode_name]
            dfs.append(df)
    if not dfs:
        return pd.DataFrame()
    return pd.concat(dfs, ignore_index=True)


def keep_common_seeds(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only model/optimizer/seed tuples available in both fitness modes."""
    common_keys = (
        df.groupby(["model_type", "optimizer", "seed"])["fitness_mode"]
        .nunique()
        .reset_index(name="mode_count")
    )
    common_keys = common_keys[common_keys["mode_count"] == 2][["model_type", "optimizer", "seed"]]
    fair_df = df.merge(common_keys, on=["model_type", "optimizer", "seed"], how="inner")
    return fair_df.sort_values(["model_type", "optimizer", "seed", "fitness_mode"]).reset_index(drop=True)


def build_summary(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    grouped = (
        df.groupby(["model_type", "optimizer", "fitness_mode"])[ALL_METRICS]
        .agg(["mean", "std"])
        .reset_index()
    )
    grouped.columns = [
        "_".join(part for part in col if part).rstrip("_")
        if isinstance(col, tuple)
        else col
        for col in grouped.columns
    ]

    wide_parts = []
    for mode in MODE_LABELS:
        mode_df = grouped[grouped["fitness_mode"] == mode].copy()
        mode_df = mode_df.drop(columns=["fitness_mode"])
        rename = {
            col: f"{mode}_{col}"
            for col in mode_df.columns
            if col not in {"model_type", "optimizer"}
        }
        wide_parts.append(mode_df.rename(columns=rename))

    wide = wide_parts[0]
    for part in wide_parts[1:]:
        wide = wide.merge(part, on=["model_type", "optimizer"], how="outer")

    for metric in ALL_METRICS:
        wide[f"delta_accuracy_cv_minus_mcc_f1_{metric}_mean"] = (
            wide[f"accuracy_cv_{metric}_mean"] - wide[f"mcc_f1_{metric}_mean"]
        )
        wide[f"winner_{metric}"] = wide.apply(
            lambda row: (
                "Accuracy-CV"
                if row[f"delta_accuracy_cv_minus_mcc_f1_{metric}_mean"] > 0
                else "MCC/F1"
                if row[f"delta_accuracy_cv_minus_mcc_f1_{metric}_mean"] < 0
                else "Tie"
            ),
            axis=1,
        )

    ordered_cols = ["model_type", "optimizer"]
    for metric in ALL_METRICS:
        ordered_cols.extend(
            [
                f"mcc_f1_{metric}_mean",
                f"mcc_f1_{metric}_std",
                f"accuracy_cv_{metric}_mean",
                f"accuracy_cv_{metric}_std",
                f"delta_accuracy_cv_minus_mcc_f1_{metric}_mean",
                f"winner_{metric}",
            ]
        )

    wide = wide[ordered_cols].sort_values(["model_type", "optimizer"]).reset_index(drop=True)
    return grouped, wide


def write_markdown_table(summary_wide: pd.DataFrame) -> Path:
    article_cols = [
        "model_type",
        "optimizer",
        "mcc_f1_accuracy_test_mean",
        "accuracy_cv_accuracy_test_mean",
        "delta_accuracy_cv_minus_mcc_f1_accuracy_test_mean",
        "winner_accuracy_test",
        "mcc_f1_mcc_test_mean",
        "accuracy_cv_mcc_test_mean",
        "delta_accuracy_cv_minus_mcc_f1_mcc_test_mean",
        "winner_mcc_test",
    ]
    table = summary_wide[article_cols].copy()
    numeric_cols = table.select_dtypes(include="number").columns
    table[numeric_cols] = table[numeric_cols].round(6)
    path = OUT_DIR / "fitness_modes_model_optimizer_summary.md"
    path.write_text(table.to_markdown(index=False), encoding="utf-8")
    return path


def plot_metric_by_model_optimizer(df: pd.DataFrame, metric: str) -> list[Path]:
    metric_label = {
        "accuracy_test": "Accuracy on X_test",
        "mcc_test": "MCC on X_test",
    }.get(metric, metric)

    plot_df = df.copy()
    plot_df["model_label"] = plot_df["model_type"].str.upper()
    plot_df["optimizer_label"] = plot_df["optimizer"].str.upper().str.replace("_", " ", regex=False)

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.05)
    fig, axes = plt.subplots(2, 2, figsize=(15, 9.5), sharey=True)
    axes = axes.ravel()

    for ax, model in zip(axes, MODELS):
        model_df = plot_df[plot_df["model_type"] == model]
        sns.barplot(
            data=model_df,
            x="optimizer_label",
            y=metric,
            hue="fitness_mode_label",
            order=[opt.upper().replace("_", " ") for opt in OPTIMIZERS],
            hue_order=["MCC/F1", "Accuracy-CV"],
            errorbar="sd",
            capsize=0.08,
            palette={"MCC/F1": "#2364aa", "Accuracy-CV": "#f28e2b"},
            ax=ax,
        )
        ax.set_title(model.upper())
        ax.set_xlabel("")
        ax.set_ylabel(metric_label if ax in (axes[0], axes[2]) else "")
        ax.tick_params(axis="x", rotation=25)
        ax.grid(axis="y", alpha=0.35)
        if ax.legend_:
            ax.legend_.remove()

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, title="Fitness mode", loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.955))
    fig.suptitle(f"{metric_label} by model, optimizer, and fitness mode", y=0.995, fontsize=14)
    fig.tight_layout(rect=(0, 0, 1, 0.89))

    stem = "mcc_test_by_model_optimizer" if metric == "mcc_test" else "accuracy_test_by_model_optimizer"
    outputs = [OUT_DIR / f"{stem}.png", OUT_DIR / f"{stem}.pdf"]
    for path in outputs:
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return outputs


def plot_global_metric_comparison(df: pd.DataFrame) -> list[Path]:
    melted = df.melt(
        id_vars=["fitness_mode_label", "model_type", "optimizer", "seed"],
        value_vars=PRIMARY_METRICS,
        var_name="metric",
        value_name="value",
    )
    melted["metric"] = melted["metric"].map(
        {
            "accuracy_test": "Accuracy",
            "mcc_test": "MCC",
        }
    )

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.1)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    sns.barplot(
        data=melted,
        x="metric",
        y="value",
        hue="fitness_mode_label",
        hue_order=["MCC/F1", "Accuracy-CV"],
        errorbar="sd",
        capsize=0.08,
        palette={"MCC/F1": "#2364aa", "Accuracy-CV": "#f28e2b"},
        ax=ax,
    )
    ax.set_title("Global test performance by fitness mode")
    ax.set_xlabel("")
    ax.set_ylabel("Mean score across common seeds/model/optimizer runs")
    ax.legend(title="Fitness mode", frameon=False)
    ax.grid(axis="y", alpha=0.35)
    fig.tight_layout()

    outputs = [OUT_DIR / "global_mcc_accuracy_comparison.png", OUT_DIR / "global_mcc_accuracy_comparison.pdf"]
    for path in outputs:
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return outputs


def main() -> None:
    df_mcc = load_data(MCC_DIR, "mcc_f1")
    df_acc = load_data(ACC_DIR, "accuracy_cv")

    if df_mcc.empty or df_acc.empty:
        raise SystemExit("Missing data for comparison.")

    raw_df = pd.concat([df_mcc, df_acc], ignore_index=True)
    df = keep_common_seeds(raw_df)

    if df.empty:
        raise SystemExit("No common model/optimizer/seed tuples found between both fitness modes.")

    grouped, summary_wide = build_summary(df)

    per_seed_path = OUT_DIR / "fitness_modes_per_seed.csv"
    grouped_path = OUT_DIR / "fitness_modes_grouped_summary_long.csv"
    summary_path = OUT_DIR / "fitness_modes_model_optimizer_summary.csv"
    global_path = OUT_DIR / "fitness_modes_global_summary.csv"

    df.to_csv(per_seed_path, index=False)
    grouped.to_csv(grouped_path, index=False)
    summary_wide.to_csv(summary_path, index=False)
    markdown_path = write_markdown_table(summary_wide)

    global_summary = (
        df.groupby("fitness_mode_label")[ALL_METRICS]
        .agg(["mean", "std"])
        .sort_index()
    )
    global_summary.to_csv(global_path)

    figure_paths = []
    figure_paths.extend(plot_metric_by_model_optimizer(df, "mcc_test"))
    figure_paths.extend(plot_metric_by_model_optimizer(df, "accuracy_test"))
    figure_paths.extend(plot_global_metric_comparison(df))

    print("Saved comparison outputs:")
    for path in [per_seed_path, grouped_path, summary_path, markdown_path, global_path, *figure_paths]:
        print(f"- {path.relative_to(ROOT)}")

    print("\nGlobal means on X_test:")
    print(global_summary.to_string(float_format=lambda value: f"{value:.6f}"))

if __name__ == "__main__":
    main()
