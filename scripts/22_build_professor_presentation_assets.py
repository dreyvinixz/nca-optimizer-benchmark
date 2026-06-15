"""Build tables and figures for the professor results presentation."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_loader import load_legacy_dataset
from src.feature_selection import select_features
from src.preprocessing import drop_missing_rows, keep_numeric_features
from src.utils.io import load_project_configs

OUT_ROOT = ROOT / "outputs" / "professor_presentation"
TABLE_DIR = OUT_ROOT / "tables"
FIGURE_DIR = OUT_ROOT / "figures"

MODES = {
    "mcc_f1": {
        "label": "MCC/F1",
        "metrics_dir": ROOT / "outputs" / "article_official" / "metrics",
        "convergence_dir": ROOT / "outputs" / "article_official" / "metrics" / "convergence",
    },
    "accuracy_cv": {
        "label": "Accuracy-CV",
        "metrics_dir": ROOT / "outputs" / "article_official_accuracy" / "metrics",
        "convergence_dir": ROOT / "outputs" / "article_official_accuracy" / "metrics" / "convergence",
    },
}
MODELS = ["mlp", "rf", "svm", "cnn"]
OPTIMIZERS = ["random_search", "ga", "pso", "de", "gwo"]
CONVERGENCE_OPTIMIZERS = ["ga", "pso", "gwo"]
SEEDS = [1, 2, 3]


def ensure_dirs() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_official_results() -> tuple[pd.DataFrame, pd.DataFrame]:
    best_frames = []
    run_frames = []
    missing: list[str] = []
    incomplete: list[str] = []
    for mode_key, mode_info in MODES.items():
        for model in MODELS:
            for optimizer in OPTIMIZERS:
                stem = f"{model}_{optimizer}"
                best_path = mode_info["metrics_dir"] / f"{stem}_best_by_seed.csv"
                runs_path = mode_info["metrics_dir"] / f"{stem}_runs.csv"
                if not best_path.exists() or not runs_path.exists():
                    missing.append(f"{mode_info['label']} {stem}")
                    continue
                best = pd.read_csv(best_path)
                best = best[best["seed"].isin(SEEDS)].copy()
                if best["seed"].nunique() != len(SEEDS):
                    incomplete.append(f"{mode_info['label']} {stem}: {best['seed'].nunique()} seeds")
                best["fitness_mode"] = mode_key
                best["fitness_mode_label"] = mode_info["label"]
                best["model_type"] = model
                best["optimizer"] = optimizer
                best_frames.append(best)

                try:
                    runs = pd.read_csv(runs_path)
                except pd.errors.ParserError:
                    runs = pd.read_csv(runs_path, engine="python", on_bad_lines="skip")
                runs = runs[runs["seed"].isin(SEEDS)].copy()
                runs["fitness_mode"] = mode_key
                runs["fitness_mode_label"] = mode_info["label"]
                runs["model_type"] = model
                runs["optimizer"] = optimizer
                run_frames.append(runs)

    if missing:
        raise FileNotFoundError("Missing official files: " + ", ".join(missing))
    if incomplete:
        raise ValueError("Incomplete official seed coverage: " + ", ".join(incomplete))
    return pd.concat(best_frames, ignore_index=True), pd.concat(run_frames, ignore_index=True)


def best_run_rows(runs: pd.DataFrame) -> pd.DataFrame:
    idx = runs.groupby(["fitness_mode", "model_type", "optimizer", "seed"])["fitness"].idxmax()
    return runs.loc[idx].reset_index(drop=True)


def dataset_tables() -> dict[str, Any]:
    config = load_project_configs()
    exp = config["experiment"]
    dataset = load_legacy_dataset(
        config["paths"]["dataset"]["merged_output"],
        exp["data"]["datetime_column"],
        exp["data"]["target_column"],
        exp["data"]["label_mapping"],
    )
    numeric_features = keep_numeric_features(dataset.frame, dataset.feature_columns)
    selected = select_features(numeric_features, exp["data"]["selected_feature_indices"])
    modeling_columns = selected + [dataset.target_column, dataset.datetime_column]
    frame = drop_missing_rows(dataset.frame, modeling_columns).sort_values(dataset.datetime_column).reset_index(drop=True)

    n = len(frame)
    train_end = int(n * float(exp["split"]["train_size"]))
    val_end = train_end + int(n * float(exp["split"]["validation_size"]))
    ranges = [
        ("Treino", 0, train_end),
        ("Validacao", train_end, val_end),
        ("Teste", val_end, n),
    ]
    split_rows = []
    for name, start, end in ranges:
        part = frame.iloc[start:end]
        split_rows.append(
            {
                "split": name,
                "rows": len(part),
                "share": len(part) / n,
                "start": str(part[dataset.datetime_column].iloc[0]),
                "end": str(part[dataset.datetime_column].iloc[-1]),
                "uptrend": int((part[dataset.target_column] == 1).sum()),
                "downtrend": int((part[dataset.target_column] == 0).sum()),
            }
        )

    feature_rows = [
        {"index": idx, "feature": feature}
        for idx, feature in zip(exp["data"]["selected_feature_indices"], selected)
    ]
    split_df = pd.DataFrame(split_rows)
    feature_df = pd.DataFrame(feature_rows)
    split_df.to_csv(TABLE_DIR / "dataset_split_summary.csv", index=False)
    feature_df.to_csv(TABLE_DIR / "infogain7_features.csv", index=False)
    return {
        "n_rows": n,
        "n_columns": len(frame.columns),
        "start": str(frame[dataset.datetime_column].iloc[0]),
        "end": str(frame[dataset.datetime_column].iloc[-1]),
        "split_rows": split_rows,
        "features": feature_rows,
    }


def search_space_table() -> pd.DataFrame:
    search_spaces = load_yaml(ROOT / "config" / "search_spaces.yaml")
    rows = []
    for model, params in search_spaces.items():
        for name, spec in params.items():
            if spec["type"] == "categorical":
                domain = ", ".join("None" if value is None else str(value) for value in spec["values"])
            else:
                domain = f"{spec['min']} - {spec['max']}"
                if spec.get("scale") == "log10":
                    domain += " (log10)"
            rows.append({"model": model.upper(), "hyperparameter": name, "type": spec["type"], "domain": domain})
    df = pd.DataFrame(rows)
    df.to_csv(TABLE_DIR / "search_space_table.csv", index=False)
    return df


def static_explanation_tables() -> None:
    optimizers = pd.DataFrame(
        [
            ("Random Search", "Amostra candidatos aleatorios; baseline simples para medir ganho dos metaheuristicos."),
            ("GA", "Populacao evolui por selecao, crossover e mutacao; bom para busca combinatoria mista."),
            ("PSO", "Particulas ajustam posicao pela melhor experiencia individual e coletiva; explora continuidade do espaco."),
            ("DE", "Gera candidatos por diferencas entre vetores; forte para parametros continuos."),
            ("GWO", "Hierarquia alfa/beta/delta guia lobos; equilibra exploracao e intensificacao."),
        ],
        columns=["optimizer", "how_it_works"],
    )
    models = pd.DataFrame(
        [
            ("MLP", "Rede neural densa para padroes nao lineares nas features tecnicas."),
            ("CNN", "Rede convolucional 1D para padroes locais nas sequencias de indicadores."),
            ("SVM", "Classificador de margem com kernel linear/RBF."),
            ("Random Forest", "Ensemble de arvores para robustez e interacoes nao lineares."),
        ],
        columns=["model", "role"],
    )
    config = pd.DataFrame(
        [
            ("Seeds", "1, 2, 3"),
            ("Orcamento oficial", "1000 avaliacoes de fitness por seed"),
            ("GA/DE", "populacao = 10"),
            ("PSO", "10 particulas; inertia=0.70; cognitive/social=1.50"),
            ("GWO", "10 lobos"),
            ("MLP/CNN", "tanh + rmsprop + binary_crossentropy; max_epochs=10; early stopping patience=3"),
        ],
        columns=["item", "value"],
    )
    optimizers.to_csv(TABLE_DIR / "optimizer_explanations.csv", index=False)
    models.to_csv(TABLE_DIR / "model_explanations.csv", index=False)
    config.to_csv(TABLE_DIR / "experiment_config_summary.csv", index=False)


def structural_pretest_assets() -> tuple[pd.DataFrame, Path]:
    import matplotlib.pyplot as plt
    import seaborn as sns

    src = ROOT / "outputs" / "structural_fast_official_space" / "structural_validation_summary.csv"
    df = pd.read_csv(src)
    df["structure"] = df["optimizer"].str.upper() + " + " + df["activation"].str.upper()
    out_table = TABLE_DIR / "structural_pretest_summary.csv"
    df.to_csv(out_table, index=False)

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.05)
    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    sns.barplot(data=df, x="model_type", y="best_fitness", hue="structure", ax=ax, palette="tab10")
    ax.set_title("Pre-teste estrutural - melhor fitness por modelo")
    ax.set_xlabel("Modelo")
    ax.set_ylabel("Melhor fitness de validacao")
    ax.legend(title="Treinamento / ativacao", frameon=False, ncol=2)
    ax.grid(axis="y", alpha=0.35)
    fig.tight_layout()
    fig_path = FIGURE_DIR / "structural_pretest_best_fitness.png"
    fig.savefig(fig_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return df, fig_path


def plot_dataset_split(dataset_info: dict[str, Any]) -> Path:
    import matplotlib.pyplot as plt
    import seaborn as sns

    df = pd.DataFrame(dataset_info["split_rows"])
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.1)
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    colors = ["#2364aa", "#f28e2b", "#59a14f"]
    left = 0
    for idx, row in df.iterrows():
        ax.barh([0], [row["rows"]], left=left, color=colors[idx], label=row["split"], height=0.38)
        ax.text(left + row["rows"] / 2, 0, f"{row['split']}\n{row['rows']:,}", ha="center", va="center", color="white", fontsize=11, fontweight="bold")
        left += row["rows"]
    ax.set_xlim(0, df["rows"].sum())
    ax.set_yticks([])
    ax.set_xlabel("Amostras ordenadas no tempo")
    ax.set_title("Divisao temporal 60/20/20 sem shuffle")
    ax.legend(frameon=False, loc="upper center", ncol=3, bbox_to_anchor=(0.5, -0.12))
    fig.tight_layout()
    out = FIGURE_DIR / "dataset_temporal_split.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


def plot_convergence() -> dict[str, Path]:
    import matplotlib.pyplot as plt
    import seaborn as sns

    paths: dict[str, Path] = {}
    palette = {"ga": "#2364aa", "pso": "#f28e2b", "gwo": "#59a14f"}
    labels = {"ga": "GA", "pso": "PSO", "gwo": "GWO"}
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.05)

    for mode_key, mode in MODES.items():
        fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), sharey=False)
        for ax, model in zip(axes, ["mlp", "cnn"]):
            for optimizer in CONVERGENCE_OPTIMIZERS:
                path = mode["convergence_dir"] / f"{model}_{optimizer}_convergence.csv"
                conv = pd.read_csv(path)
                conv = conv[conv["seed"].isin(SEEDS)].copy()
                mean_conv = conv.groupby("evaluation_id")["best_fitness_so_far"].mean().reset_index()
                ax.plot(
                    mean_conv["evaluation_id"],
                    mean_conv["best_fitness_so_far"],
                    label=labels[optimizer],
                    color=palette[optimizer],
                    linewidth=2.2,
                )
            ax.set_title(model.upper())
            ax.set_xlabel("Avaliacao de fitness")
            ax.set_ylabel("Melhor fitness acumulado")
            ax.grid(axis="y", alpha=0.35)
        handles, labels_list = axes[0].get_legend_handles_labels()
        fig.legend(handles, labels_list, title="Otimizador", loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.99))
        fig.suptitle(f"Evolucao da fitness - {mode['label']}", y=1.06)
        fig.tight_layout()
        out = FIGURE_DIR / f"convergence_{mode_key}_mlp_cnn.png"
        fig.savefig(out, dpi=300, bbox_inches="tight")
        plt.close(fig)
        paths[mode_key] = out
    return paths


def plot_train_signal_vs_test(best: pd.DataFrame, best_runs: pd.DataFrame) -> dict[str, Path]:
    import matplotlib.pyplot as plt
    import seaborn as sns

    paths: dict[str, Path] = {}
    merged = best[["fitness_mode", "fitness_mode_label", "model_type", "optimizer", "seed", "accuracy_test"]].merge(
        best_runs[
            [
                "fitness_mode",
                "model_type",
                "optimizer",
                "seed",
                "accuracy",
                "acc_train",
            ]
        ],
        on=["fitness_mode", "model_type", "optimizer", "seed"],
        how="left",
    )
    merged["train_signal_accuracy"] = np.where(
        merged["fitness_mode"] == "accuracy_cv",
        merged["acc_train"],
        merged["accuracy"],
    )
    merged["train_signal_label"] = np.where(
        merged["fitness_mode"] == "accuracy_cv",
        "Acc treino CV",
        "Acc validacao",
    )

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.02)
    for mode_key, mode in MODES.items():
        plot_df = merged[merged["fitness_mode"] == mode_key].copy()
        mean_df = (
            plot_df.groupby(["model_type", "optimizer"])[["train_signal_accuracy", "accuracy_test"]]
            .mean()
            .reset_index()
            .melt(id_vars=["model_type", "optimizer"], var_name="metric", value_name="accuracy")
        )
        mean_df["metric"] = mean_df["metric"].map(
            {
                "train_signal_accuracy": "Treino/validacao do fitness",
                "accuracy_test": "Teste cego",
            }
        )
        mean_df["combo"] = mean_df["optimizer"].str.upper().str.replace("_", " ", regex=False)

        fig, axes = plt.subplots(2, 2, figsize=(13, 8), sharey=True)
        for ax, model in zip(axes.ravel(), MODELS):
            part = mean_df[mean_df["model_type"] == model]
            sns.barplot(data=part, x="combo", y="accuracy", hue="metric", ax=ax, palette=["#2364aa", "#f28e2b"])
            ax.set_title(model.upper())
            ax.set_xlabel("")
            ax.set_ylabel("Acuracia" if model in ("mlp", "svm") else "")
            ax.tick_params(axis="x", rotation=25)
            ax.grid(axis="y", alpha=0.35)
            if ax.legend_:
                ax.legend_.remove()
        handles, legend_labels = axes.ravel()[0].get_legend_handles_labels()
        fig.legend(handles, legend_labels, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.98))
        fig.suptitle(f"Acuracia do sinal de ajuste vs teste - {mode['label']}", y=1.01)
        fig.tight_layout(rect=(0, 0, 1, 0.94))
        out = FIGURE_DIR / f"train_signal_vs_test_accuracy_{mode_key}.png"
        fig.savefig(out, dpi=300, bbox_inches="tight")
        plt.close(fig)
        paths[mode_key] = out

    merged.to_csv(TABLE_DIR / "train_signal_vs_test_accuracy.csv", index=False)
    return paths


def plot_mode_metric_by_model_optimizer(best: pd.DataFrame) -> dict[str, Path]:
    import matplotlib.pyplot as plt
    import seaborn as sns

    paths: dict[str, Path] = {}
    labels = {
        "random_search": "Random\nSearch",
        "ga": "GA",
        "pso": "PSO",
        "de": "DE",
        "gwo": "GWO",
    }
    palette = {
        "random_search": "#4E79A7",
        "ga": "#F28E2B",
        "pso": "#59A14F",
        "de": "#C53D3F",
        "gwo": "#8F6BB2",
    }
    specs = [
        ("mcc_f1", "mcc_test", "MCC no X_test", "mcc_f1_mcc_test_by_model_optimizer_clean.png"),
        ("mcc_f1", "accuracy_test", "Accuracy no X_test", "mcc_f1_accuracy_test_by_model_optimizer_clean.png"),
        ("accuracy_cv", "mcc_test", "MCC no X_test", "accuracy_cv_mcc_test_by_model_optimizer_clean.png"),
        ("accuracy_cv", "accuracy_test", "Accuracy no X_test", "accuracy_cv_accuracy_test_by_model_optimizer_clean.png"),
    ]

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.0)
    for mode_key, metric, ylabel, filename in specs:
        mode_df = best[best["fitness_mode"] == mode_key].copy()
        summary = (
            mode_df.groupby(["model_type", "optimizer"])[metric]
            .agg(["mean", "std"])
            .reset_index()
        )

        fig, axes = plt.subplots(2, 2, figsize=(12.8, 8.0), sharey=True)
        for ax, model in zip(axes.ravel(), MODELS):
            part = summary[summary["model_type"] == model].set_index("optimizer").loc[OPTIMIZERS].reset_index()
            raw = mode_df[mode_df["model_type"] == model].copy()
            x = np.arange(len(OPTIMIZERS))
            colors = [palette[opt] for opt in OPTIMIZERS]
            ax.bar(x, part["mean"], yerr=part["std"], capsize=4, color=colors, edgecolor="#FFFFFF", linewidth=0.7)

            for idx, optimizer in enumerate(OPTIMIZERS):
                seed_values = raw[raw["optimizer"] == optimizer][metric].to_numpy()
                jitter = np.linspace(-0.12, 0.12, len(seed_values)) if len(seed_values) > 1 else np.array([0.0])
                ax.scatter(np.full(len(seed_values), idx) + jitter, seed_values, color="#17202A", s=15, zorder=4, alpha=0.8)

            ax.set_title(model.upper())
            ax.set_xticks(x, [labels[opt] for opt in OPTIMIZERS])
            ax.set_xlabel("")
            ax.set_ylabel(ylabel if model in ("mlp", "svm") else "")
            ax.grid(axis="y", alpha=0.35)

        mode_label = MODES[mode_key]["label"]
        fig.suptitle(f"{mode_label} - {ylabel} por modelo e otimizador", y=1.01, fontsize=14)
        fig.text(0.5, 0.01, "Barras = media das seeds 1, 2 e 3; hastes = desvio padrao; pontos = valor de cada seed.", ha="center", fontsize=10)
        fig.tight_layout(rect=(0, 0.04, 1, 0.97))
        out = FIGURE_DIR / filename
        fig.savefig(out, dpi=300, bbox_inches="tight")
        plt.close(fig)
        paths[f"{mode_key}_{metric}"] = out

    return paths


def build_mode_summary(best: pd.DataFrame) -> pd.DataFrame:
    metrics = ["accuracy_test", "balanced_accuracy_test", "mcc_test", "f1_test", "auc_roc_test", "auc_pr_test"]
    summary = (
        best.groupby(["fitness_mode", "fitness_mode_label", "model_type", "optimizer"])[metrics]
        .agg(["mean", "std"])
        .reset_index()
    )
    summary.columns = ["_".join(col).rstrip("_") if isinstance(col, tuple) else col for col in summary.columns]
    summary.to_csv(TABLE_DIR / "official_model_optimizer_summary.csv", index=False)
    global_summary = best.groupby(["fitness_mode", "fitness_mode_label"])[metrics].agg(["mean", "std"]).reset_index()
    global_summary.columns = ["_".join(col).rstrip("_") if isinstance(col, tuple) else col for col in global_summary.columns]
    global_summary.to_csv(TABLE_DIR / "official_global_summary.csv", index=False)
    return summary


def plot_best_model_metrics(best: pd.DataFrame) -> tuple[Path, pd.DataFrame]:
    import matplotlib.pyplot as plt
    import seaborn as sns

    metrics = ["accuracy_test", "mcc_test", "f1_test", "auc_roc_test", "auc_pr_test"]
    labels = {
        "accuracy_test": "Accuracy",
        "mcc_test": "MCC",
        "f1_test": "F1",
        "auc_roc_test": "AUC ROC",
        "auc_pr_test": "AUC PR",
    }
    best_pair = best[(best["model_type"] == "mlp") & (best["optimizer"] == "gwo")].copy()
    mean_df = best_pair.groupby("fitness_mode_label")[metrics].mean().reset_index()
    long = mean_df.melt(id_vars="fitness_mode_label", var_name="metric", value_name="score")
    long["metric"] = long["metric"].map(labels)
    long.to_csv(TABLE_DIR / "best_model_metric_comparison.csv", index=False)

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.05)
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    sns.barplot(data=long, x="metric", y="score", hue="fitness_mode_label", palette=["#2364aa", "#f28e2b"], ax=ax)
    ax.set_title("Melhor combinacao comum: MLP + GWO")
    ax.set_xlabel("")
    ax.set_ylabel("Media no X_test")
    ax.legend(title="Fitness", frameon=False)
    ax.grid(axis="y", alpha=0.35)
    fig.tight_layout()
    out = FIGURE_DIR / "best_model_metrics_mlp_gwo.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out, mean_df


def plot_fitness_side_by_side(best: pd.DataFrame) -> Path:
    import matplotlib.pyplot as plt
    import seaborn as sns

    global_acc = best.groupby("fitness_mode_label")["accuracy_test"].mean().reset_index()
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.1)
    fig, ax = plt.subplots(figsize=(7.5, 5.2))
    sns.barplot(data=global_acc, x="fitness_mode_label", y="accuracy_test", palette=["#f28e2b", "#2364aa"], ax=ax, hue="fitness_mode_label", legend=False)
    ax.set_title("Fitness lado a lado - acuracia media no X_test")
    ax.set_xlabel("")
    ax.set_ylabel("Accuracy no teste")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.4f", padding=3)
    ax.grid(axis="y", alpha=0.35)
    fig.tight_layout()
    out = FIGURE_DIR / "fitness_side_by_side_accuracy_test.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


def build_gap_heatmaps(summary: pd.DataFrame) -> dict[str, Path]:
    import matplotlib.pyplot as plt
    import seaborn as sns

    paths: dict[str, Path] = {}
    for metric in ["accuracy_test", "mcc_test"]:
        rows = []
        for _, row in summary.iterrows():
            rows.append(
                {
                    "combo": f"{row['model_type'].upper()} / {row['optimizer'].upper().replace('_', ' ')}",
                    "fitness": row["fitness_mode_label"],
                    "value": row[f"{metric}_mean"],
                }
            )
        long = pd.DataFrame(rows)
        best_value = float(long["value"].max())
        long["gap_pct"] = (long["value"] - best_value) / abs(best_value) * 100.0
        long.to_csv(TABLE_DIR / f"gap_to_global_best_{metric}.csv", index=False)
        pivot = long.pivot(index="combo", columns="fitness", values="gap_pct").sort_index()

        sns.set_theme(style="white", context="paper", font_scale=0.82)
        fig, ax = plt.subplots(figsize=(8.2, 9.2))
        sns.heatmap(pivot, annot=True, fmt=".1f", cmap="RdYlGn", center=0, linewidths=0.4, cbar_kws={"label": "Gap vs melhor global (%)"}, ax=ax)
        ax.set_title(f"Gap percentual em relacao ao melhor global - {metric.replace('_', ' ').upper()}")
        ax.set_xlabel("")
        ax.set_ylabel("")
        fig.tight_layout()
        out = FIGURE_DIR / f"gap_heatmap_{metric}.png"
        fig.savefig(out, dpi=300, bbox_inches="tight")
        plt.close(fig)
        paths[metric] = out
    return paths


def validation_signal_table(best_runs: pd.DataFrame) -> pd.DataFrame:
    metrics = ["fitness", "accuracy", "acc_train", "mcc", "f1", "auc_roc", "auc_pr"]
    subset = best_runs[(best_runs["model_type"] == "mlp") & (best_runs["optimizer"] == "gwo")].copy()
    table = subset.groupby("fitness_mode_label")[metrics].mean().reset_index()
    table.to_csv(TABLE_DIR / "best_model_validation_signal.csv", index=False)
    return table


def write_presentation_data(dataset_info: dict[str, Any], figure_paths: dict[str, Any], tables: dict[str, Any]) -> None:
    payload = {
        "dataset": dataset_info,
        "figures": {key: str(path.relative_to(ROOT)) for key, path in figure_paths.items()},
        "tables": {key: str(path.relative_to(ROOT)) for key, path in tables.items()},
        "notes": {
            "train_signal": "For MCC/F1 the available adjustment signal is validation accuracy from the best validation candidate; for Accuracy-CV the available training signal is mean CV train accuracy.",
            "primary_conclusion": "MCC/F1 is recommended because it slightly leads Accuracy-CV on mean X_test accuracy and MCC.",
        },
    }
    (TABLE_DIR / "presentation_data.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    best, runs = load_official_results()
    best_runs = best_run_rows(runs)

    dataset_info = dataset_tables()
    search_space = search_space_table()
    static_explanation_tables()
    structural_df, structural_fig = structural_pretest_assets()
    split_fig = plot_dataset_split(dataset_info)
    convergence_figs = plot_convergence()
    train_figs = plot_train_signal_vs_test(best, best_runs)
    mode_metric_figs = plot_mode_metric_by_model_optimizer(best)
    summary = build_mode_summary(best)
    best_metrics_fig, best_metrics = plot_best_model_metrics(best)
    side_by_side_fig = plot_fitness_side_by_side(best)
    gap_figs = build_gap_heatmaps(summary)
    validation_signal = validation_signal_table(best_runs)

    figure_paths = {
        "dataset_split": split_fig,
        "structural_pretest": structural_fig,
        "convergence_mcc_f1": convergence_figs["mcc_f1"],
        "convergence_accuracy_cv": convergence_figs["accuracy_cv"],
        "train_signal_mcc_f1": train_figs["mcc_f1"],
        "train_signal_accuracy_cv": train_figs["accuracy_cv"],
        "mcc_f1_mcc_by_model_optimizer": mode_metric_figs["mcc_f1_mcc_test"],
        "mcc_f1_accuracy_by_model_optimizer": mode_metric_figs["mcc_f1_accuracy_test"],
        "accuracy_cv_mcc_by_model_optimizer": mode_metric_figs["accuracy_cv_mcc_test"],
        "accuracy_cv_accuracy_by_model_optimizer": mode_metric_figs["accuracy_cv_accuracy_test"],
        "best_model_metrics": best_metrics_fig,
        "fitness_side_by_side_accuracy": side_by_side_fig,
        "gap_accuracy": gap_figs["accuracy_test"],
        "gap_mcc": gap_figs["mcc_test"],
    }
    backtest_equity = FIGURE_DIR / "official_backtest_equity_curve.png"
    backtest_metrics = FIGURE_DIR / "official_backtest_metrics.png"
    if backtest_equity.exists():
        figure_paths["official_backtest_equity"] = backtest_equity
    if backtest_metrics.exists():
        figure_paths["official_backtest_metrics"] = backtest_metrics

    tables = {
        "dataset_split": TABLE_DIR / "dataset_split_summary.csv",
        "features": TABLE_DIR / "infogain7_features.csv",
        "search_space": TABLE_DIR / "search_space_table.csv",
        "official_summary": TABLE_DIR / "official_model_optimizer_summary.csv",
        "global_summary": TABLE_DIR / "official_global_summary.csv",
        "best_model_metrics": TABLE_DIR / "best_model_metric_comparison.csv",
        "validation_signal": TABLE_DIR / "best_model_validation_signal.csv",
        "structural_pretest": TABLE_DIR / "structural_pretest_summary.csv",
    }
    for key, path in {
        "official_backtest_summary": TABLE_DIR / "official_backtest_summary.csv",
        "official_backtest_tests": TABLE_DIR / "official_backtest_statistical_tests.csv",
        "official_backtest_metadata": TABLE_DIR / "official_backtest_metadata.json",
    }.items():
        if path.exists():
            tables[key] = path
    write_presentation_data(dataset_info, figure_paths, tables)

    # Small console ledger for acceptance checks.
    combos = best.groupby(["fitness_mode", "model_type", "optimizer"])["seed"].nunique()
    print("Asset build complete.")
    print(f"Official combinations checked: {len(combos)}")
    print(f"All combinations have seeds {SEEDS}: {bool((combos == len(SEEDS)).all())}")
    print(f"Search-space rows: {len(search_space)}")
    print(f"Structural pretest rows: {len(structural_df)}")
    print(f"Best metric rows: {len(best_metrics)}")
    print(f"Validation signal rows: {len(validation_signal)}")


if __name__ == "__main__":
    main()
