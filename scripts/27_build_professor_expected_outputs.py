"""Build the figures and summary requested in the professor feedback.

This script keeps MCC and accuracy on separate visual scales and reports the
optimizer effort as objective-function evaluations. In this project one row in
`*_runs.csv` is one candidate evaluation, usually one model training.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "professor_presentation" / "figures" / "professor_expected"
DOWNLOADS_DIR = Path.home() / "Downloads"

SEEDS = [1, 2, 3]
MODELS = ["cnn", "mlp", "rf", "svm"]
OPTIMIZERS = ["de", "ga", "gwo", "pso", "random_search"]

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
    short_label: str
    metrics_dir: Path
    protocol: str
    fitness: str


EXPERIMENTS = [
    Experiment(
        key="exp1_holdout_mcc_f1",
        label="Experimento 1 - Holdout + MCC/F1",
        short_label="Exp. 1",
        metrics_dir=ROOT / "outputs" / "article_official" / "metrics",
        protocol="Holdout temporal 60/20/20",
        fitness="0.6*MCC + 0.4*F1",
    ),
    Experiment(
        key="exp2_holdout_accuracy",
        label="Experimento 2 - Holdout + Accuracy",
        short_label="Exp. 2",
        metrics_dir=ROOT / "outputs" / "article_official_accuracy_holdout" / "metrics",
        protocol="Holdout temporal 60/20/20",
        fitness="0.4*Acc_train + 0.6*Acc_val",
    ),
    Experiment(
        key="exp3_cv_accuracy",
        label="Experimento 3 - Cross-validation + Accuracy",
        short_label="Exp. 3",
        metrics_dir=ROOT / "outputs" / "article_official_accuracy" / "metrics",
        protocol="Cross-validation temporal",
        fitness="mean(0.4*Acc_train_fold + 0.6*Acc_val_fold)",
    ),
]


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except pd.errors.ParserError:
        return pd.read_csv(path, engine="python", on_bad_lines="skip")


def load_best_metrics() -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for exp in EXPERIMENTS:
        for model in MODELS:
            for optimizer in OPTIMIZERS:
                path = exp.metrics_dir / f"{model}_{optimizer}_best_by_seed.csv"
                if not path.exists():
                    raise FileNotFoundError(path)
                df = read_csv(path)
                df = df[df["seed"].isin(SEEDS)].copy()
                rows.append(
                    {
                        "experiment": exp.key,
                        "experiment_label": exp.label,
                        "model": model,
                        "optimizer": optimizer,
                        "seed_count_best": int(df["seed"].nunique()),
                        "accuracy_test_mean": float(df["accuracy_test"].mean()),
                        "accuracy_test_std": float(df["accuracy_test"].std(ddof=1)),
                        "mcc_test_mean": float(df["mcc_test"].mean()),
                        "mcc_test_std": float(df["mcc_test"].std(ddof=1)),
                        "f1_test_mean": float(df["f1_test"].mean()),
                        "f1_test_std": float(df["f1_test"].std(ddof=1)),
                    }
                )
    return pd.DataFrame(rows)


def load_runs() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for exp in EXPERIMENTS:
        for model in MODELS:
            for optimizer in OPTIMIZERS:
                path = exp.metrics_dir / f"{model}_{optimizer}_runs.csv"
                if not path.exists():
                    raise FileNotFoundError(path)
                df = read_csv(path)
                df = df[df["seed"].isin(SEEDS)].copy()
                df["experiment"] = exp.key
                df["experiment_label"] = exp.label
                df["model"] = model
                df["optimizer"] = optimizer
                frames.append(df)

    runs = pd.concat(frames, ignore_index=True)
    runs["fitness"] = pd.to_numeric(runs["fitness"], errors="coerce")
    runs["train_time_seconds"] = pd.to_numeric(runs["train_time_seconds"], errors="coerce").fillna(0.0)
    runs = runs.dropna(subset=["fitness"]).copy()
    runs = runs.sort_values(["experiment", "model", "optimizer", "seed", "candidate_id"]).reset_index(drop=True)
    grouped = runs.groupby(["experiment", "model", "optimizer", "seed"], sort=False)
    runs["training_evaluation"] = grouped.cumcount() + 1
    runs["best_fitness_so_far"] = grouped["fitness"].cummax()
    runs["runtime_minutes_so_far"] = grouped["train_time_seconds"].cumsum() / 60.0
    return runs


def summarize_effort(runs: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for keys, group in runs.groupby(["experiment", "experiment_label", "model", "optimizer", "seed"], sort=False):
        exp_key, exp_label, model, optimizer, seed = keys
        group = group.sort_values("training_evaluation")
        first_best = float(group["best_fitness_so_far"].iloc[0])
        final_best = float(group["best_fitness_so_far"].iloc[-1])
        total_trainings = int(group["training_evaluation"].iloc[-1])
        total_runtime = float(group["runtime_minutes_so_far"].iloc[-1])

        delta = final_best - first_best
        target = final_best if abs(delta) < 1e-12 else first_best + 0.95 * delta
        reached = group[group["best_fitness_so_far"] >= target]
        if reached.empty:
            trainings_to_95 = total_trainings
            minutes_to_95 = total_runtime
        else:
            trainings_to_95 = int(reached["training_evaluation"].iloc[0])
            minutes_to_95 = float(reached["runtime_minutes_so_far"].iloc[0])

        rows.append(
            {
                "experiment": exp_key,
                "experiment_label": exp_label,
                "model": model,
                "optimizer": optimizer,
                "seed": int(seed),
                "total_trainings": total_trainings,
                "total_runtime_minutes": total_runtime,
                "best_fitness": final_best,
                "trainings_to_95pct_final_best": trainings_to_95,
                "minutes_to_95pct_final_best": minutes_to_95,
            }
        )
    return pd.DataFrame(rows)


def add_bar_labels(ax: plt.Axes, values: np.ndarray, fmt: str = "{:.4f}", best_high: bool = True) -> None:
    if len(values) == 0 or np.all(np.isnan(values)):
        return
    best_idx = int(np.nanargmax(values) if best_high else np.nanargmin(values))
    y_min, y_max = ax.get_ylim()
    offset = (y_max - y_min) * 0.012
    for idx, value in enumerate(values):
        color = "#B22222" if idx == best_idx else "#222222"
        ax.text(
            idx,
            value + offset,
            fmt.format(value),
            ha="center",
            va="bottom",
            fontsize=7.5,
            color=color,
            fontweight="bold" if idx == best_idx else "normal",
        )


def plot_exp1_mcc(best: pd.DataFrame, out_path: Path) -> Path:
    fig, axes = plt.subplots(1, len(MODELS), figsize=(16, 4.6), sharey=True)
    fig.suptitle("Experimento 1 - Holdout + MCC/F1: MCC no X_test", fontsize=16, fontweight="bold", y=1.02)
    exp_df = best[best["experiment"] == "exp1_holdout_mcc_f1"]
    for ax, model in zip(axes, MODELS):
        part = exp_df[exp_df["model"] == model].set_index("optimizer").loc[OPTIMIZERS].reset_index()
        values = part["mcc_test_mean"].to_numpy()
        ax.bar(range(len(OPTIMIZERS)), values, color=[COLORS[o] for o in OPTIMIZERS], width=0.78)
        ax.set_title(MODEL_LABELS[model], fontsize=11, fontweight="bold")
        ax.set_xticks(range(len(OPTIMIZERS)))
        ax.set_xticklabels([OPTIMIZER_LABELS[o] for o in OPTIMIZERS], fontsize=9)
        ax.set_ylim(0.0, 0.36)
        ax.grid(axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        if ax is axes[0]:
            ax.set_ylabel("MCC no teste cego", fontsize=10)
        add_bar_labels(ax, values)
    fig.text(0.5, -0.02, "Valor vermelho = maior MCC medio do painel. Seeds usadas: 1, 2 e 3.", ha="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_overview_1_2_3(best: pd.DataFrame, out_path: Path) -> Path:
    rows = [
        ("exp1_holdout_mcc_f1", "Experimento 1 - Holdout + MCC/F1", "mcc_test_mean", "MCC no X_test", (0.0, 0.36)),
        ("exp2_holdout_accuracy", "Experimento 2 - Holdout + Accuracy", "accuracy_test_mean", "Accuracy no X_test", (0.0, 0.80)),
        ("exp3_cv_accuracy", "Experimento 3 - Cross-validation + Accuracy", "accuracy_test_mean", "Accuracy no X_test", (0.0, 0.80)),
    ]
    fig, axes = plt.subplots(len(rows), len(MODELS), figsize=(19, 12), sharex=False)
    fig.suptitle("Experimentos 1, 2 e 3 - Metricas Separadas Conforme Feedback", fontsize=18, fontweight="bold", y=0.995)

    for row_idx, (exp_key, row_title, metric, ylabel, ylim) in enumerate(rows):
        exp_df = best[best["experiment"] == exp_key]
        for col_idx, model in enumerate(MODELS):
            ax = axes[row_idx, col_idx]
            part = exp_df[exp_df["model"] == model].set_index("optimizer").loc[OPTIMIZERS].reset_index()
            values = part[metric].to_numpy()
            ax.bar(range(len(OPTIMIZERS)), values, color=[COLORS[o] for o in OPTIMIZERS], width=0.78)
            ax.set_title(f"{row_title} | {MODEL_LABELS[model]}", fontsize=10, fontweight="bold")
            ax.set_xticks(range(len(OPTIMIZERS)))
            ax.set_xticklabels([OPTIMIZER_LABELS[o] for o in OPTIMIZERS], fontsize=8.5)
            ax.set_ylim(*ylim)
            ax.grid(axis="y", alpha=0.3)
            ax.set_axisbelow(True)
            if col_idx == 0:
                ax.set_ylabel(ylabel, fontsize=9.5)
            add_bar_labels(ax, values)

    fig.text(
        0.5,
        0.012,
        "Exp. 1 usa MCC; Exp. 2 e Exp. 3 usam Accuracy. A figura evita comparar MCC e Accuracy na mesma linha.",
        ha="center",
        fontsize=9,
    )
    fig.tight_layout(rect=[0, 0.025, 1, 0.965])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_holdout_accuracy(best: pd.DataFrame, out_path: Path) -> Path:
    exp_keys = ["exp1_holdout_mcc_f1", "exp2_holdout_accuracy"]
    titles = [
        "Exp. 1 - Holdout + MCC/F1\nreportado como Accuracy no X_test",
        "Exp. 2 - Holdout + Accuracy\nreportado como Accuracy no X_test",
    ]
    fig, axes = plt.subplots(len(exp_keys), len(MODELS), figsize=(18, 8), sharey=True)
    fig.suptitle("Holdout: Accuracy no X_test para Experimentos 1 e 2", fontsize=16, fontweight="bold", y=0.995)
    for row_idx, (exp_key, row_title) in enumerate(zip(exp_keys, titles)):
        exp_df = best[best["experiment"] == exp_key]
        for col_idx, model in enumerate(MODELS):
            ax = axes[row_idx, col_idx]
            part = exp_df[exp_df["model"] == model].set_index("optimizer").loc[OPTIMIZERS].reset_index()
            values = part["accuracy_test_mean"].to_numpy()
            ax.bar(range(len(OPTIMIZERS)), values, color=[COLORS[o] for o in OPTIMIZERS], width=0.78)
            title = f"{row_title} | {MODEL_LABELS[model]}"
            ax.set_title(title, fontsize=9.5, fontweight="bold")
            ax.set_xticks(range(len(OPTIMIZERS)))
            ax.set_xticklabels([OPTIMIZER_LABELS[o] for o in OPTIMIZERS], fontsize=8.5)
            ax.set_ylim(0.0, 0.80)
            ax.grid(axis="y", alpha=0.3)
            ax.set_axisbelow(True)
            if col_idx == 0:
                ax.set_ylabel("Accuracy no teste cego", fontsize=10)
            add_bar_labels(ax, values)
    fig.text(0.5, 0.01, "MCC e Accuracy nao foram misturados: aqui todos os valores sao Accuracy.", ha="center", fontsize=9)
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_exp3_cv_accuracy(best: pd.DataFrame, out_path: Path) -> Path:
    fig, axes = plt.subplots(1, len(MODELS), figsize=(16, 4.6), sharey=True)
    fig.suptitle("Experimento 3 - Cross-validation + Accuracy: Accuracy no X_test", fontsize=16, fontweight="bold", y=1.02)
    exp_df = best[best["experiment"] == "exp3_cv_accuracy"]
    for ax, model in zip(axes, MODELS):
        part = exp_df[exp_df["model"] == model].set_index("optimizer").loc[OPTIMIZERS].reset_index()
        values = part["accuracy_test_mean"].to_numpy()
        ax.bar(range(len(OPTIMIZERS)), values, color=[COLORS[o] for o in OPTIMIZERS], width=0.78)
        ax.set_title(MODEL_LABELS[model], fontsize=11, fontweight="bold")
        ax.set_xticks(range(len(OPTIMIZERS)))
        ax.set_xticklabels([OPTIMIZER_LABELS[o] for o in OPTIMIZERS], fontsize=9)
        ax.set_ylim(0.0, 0.80)
        ax.grid(axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        if ax is axes[0]:
            ax.set_ylabel("Accuracy no teste cego", fontsize=10)
        add_bar_labels(ax, values)
    fig.text(0.5, -0.02, "Este grafico substitui a nomenclatura antiga de 'Experimento 4' por 'Experimento 3'.", ha="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def plot_training_efficiency(effort: pd.DataFrame, out_path: Path) -> Path:
    agg = (
        effort.groupby(["experiment", "experiment_label", "optimizer"])
        .agg(
            trainings_to_95=("trainings_to_95pct_final_best", "median"),
            minutes_to_95=("minutes_to_95pct_final_best", "median"),
            total_trainings=("total_trainings", "median"),
        )
        .reset_index()
    )
    fig, axes = plt.subplots(1, len(EXPERIMENTS), figsize=(17, 4.8), sharey=True)
    fig.suptitle("Eficiencia dos Otimizadores: Treinamentos ate 95% do Melhor Fitness Final", fontsize=16, fontweight="bold")
    for ax, exp in zip(axes, EXPERIMENTS):
        part = agg[agg["experiment"] == exp.key].set_index("optimizer").loc[OPTIMIZERS].reset_index()
        values = part["trainings_to_95"].to_numpy()
        ax.bar(range(len(OPTIMIZERS)), values, color=[COLORS[o] for o in OPTIMIZERS], width=0.78)
        ax.set_title(exp.label, fontsize=10.5, fontweight="bold")
        ax.set_xticks(range(len(OPTIMIZERS)))
        ax.set_xticklabels([OPTIMIZER_LABELS[o] for o in OPTIMIZERS], fontsize=9)
        ax.grid(axis="y", alpha=0.3)
        ax.set_axisbelow(True)
        ax.set_xlabel("Otimizador")
        add_bar_labels(ax, values, "{:.0f}", best_high=False)
        if ax is axes[0]:
            ax.set_ylabel("Mediana de treinamentos", fontsize=10)
    fig.text(
        0.5,
        0.0,
        "Cada treinamento = uma linha em *_runs.csv = uma avaliacao da funcao objetivo. Menor valor e melhor.",
        ha="center",
        fontsize=9,
    )
    fig.tight_layout(rect=[0, 0.03, 1, 0.92])
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out_path


def build_expected_summary(best: pd.DataFrame, effort: pd.DataFrame) -> pd.DataFrame:
    effort_agg = (
        effort.groupby(["experiment", "model", "optimizer"])
        .agg(
            seed_count_runs=("seed", "nunique"),
            total_trainings_median=("total_trainings", "median"),
            total_runtime_minutes_median=("total_runtime_minutes", "median"),
            trainings_to_95pct_final_best_median=("trainings_to_95pct_final_best", "median"),
            minutes_to_95pct_final_best_median=("minutes_to_95pct_final_best", "median"),
            best_fitness_mean=("best_fitness", "mean"),
        )
        .reset_index()
    )
    return best.merge(effort_agg, on=["experiment", "model", "optimizer"], how="left")


def write_markdown(summary: pd.DataFrame, effort: pd.DataFrame, paths: list[Path]) -> Path:
    report_path = OUT_DIR / "saida_esperada_professor.md"

    best_mcc = summary[summary["experiment"] == "exp1_holdout_mcc_f1"].sort_values("mcc_test_mean", ascending=False).iloc[0]
    best_exp1_acc = summary[summary["experiment"] == "exp1_holdout_mcc_f1"].sort_values("accuracy_test_mean", ascending=False).iloc[0]
    best_exp2_acc = summary[summary["experiment"] == "exp2_holdout_accuracy"].sort_values("accuracy_test_mean", ascending=False).iloc[0]
    best_exp3_acc = summary[summary["experiment"] == "exp3_cv_accuracy"].sort_values("accuracy_test_mean", ascending=False).iloc[0]

    seed_gaps = summary[(summary["seed_count_best"] < len(SEEDS)) | (summary["seed_count_runs"] < len(SEEDS))]
    warnings = []
    if not seed_gaps.empty:
        examples = seed_gaps[["experiment", "model", "optimizer", "seed_count_best", "seed_count_runs"]].head(8)
        warnings.append("Algumas combinacoes nao tem as 3 repeticoes completas nos arquivos lidos:")
        warnings.extend(
            f"- {row.experiment} / {row.model} / {row.optimizer}: best={int(row.seed_count_best)}, runs={int(row.seed_count_runs)}"
            for row in examples.itertuples(index=False)
        )

    text = [
        "# Saida esperada para o professor",
        "",
        "## Interpretacao do pedido",
        "",
        "O pedido tem duas partes. A primeira e separar as metricas para nao comparar MCC com Accuracy no mesmo grafico. A segunda e adicionar uma leitura de complexidade empirica: quantos treinamentos/avaliacoes cada otimizador precisou para chegar a um bom resultado.",
        "",
        "## Graficos gerados",
        "",
    ]
    text.extend(f"- `{path.name}`" for path in paths)
    text.extend(
        [
            "",
            "## Como apresentar os experimentos",
            "",
            "- Experimento 1: Holdout temporal com fitness MCC/F1. O grafico principal dele deve ser MCC no X_test.",
            "- Experimento 1 tambem pode aparecer no grafico de holdout/acuracia, mas reportando Accuracy no X_test.",
            "- Experimento 2: Holdout temporal com fitness Accuracy. Deve ser comparado com Exp. 1 apenas quando a metrica reportada for Accuracy.",
            "- Experimento 3: Cross-validation temporal com fitness Accuracy. Deve aparecer sozinho como CV, sem ser chamado de Experimento 4.",
            "",
            "## Melhores resultados medios nos graficos",
            "",
            f"- Exp. 1 MCC: {MODEL_LABELS[best_mcc.model]} + {OPTIMIZER_LABELS[best_mcc.optimizer]} = MCC {best_mcc.mcc_test_mean:.4f}, F1 {best_mcc.f1_test_mean:.4f}, Accuracy {best_mcc.accuracy_test_mean:.4f}.",
            f"- Exp. 1 Holdout/Accuracy: {MODEL_LABELS[best_exp1_acc.model]} + {OPTIMIZER_LABELS[best_exp1_acc.optimizer]} = Accuracy {best_exp1_acc.accuracy_test_mean:.4f}.",
            f"- Exp. 2 Holdout/Accuracy: {MODEL_LABELS[best_exp2_acc.model]} + {OPTIMIZER_LABELS[best_exp2_acc.optimizer]} = Accuracy {best_exp2_acc.accuracy_test_mean:.4f}.",
            f"- Exp. 3 CV/Accuracy: {MODEL_LABELS[best_exp3_acc.model]} + {OPTIMIZER_LABELS[best_exp3_acc.optimizer]} = Accuracy {best_exp3_acc.accuracy_test_mean:.4f}.",
            "",
            "## Contagem de treinamentos",
            "",
            "Cada linha em `*_runs.csv` foi tratada como uma avaliacao da funcao objetivo, isto e, um treinamento/avaliacao de um candidato de hiperparametros. A saida de eficiencia usa `trainings_to_95pct_final_best`: a mediana de treinamentos necessarios para atingir 95% da melhora obtida pelo melhor fitness final daquela execucao.",
            "",
        ]
    )

    effort_best = (
        effort.groupby(["experiment_label", "optimizer"])["trainings_to_95pct_final_best"]
        .median()
        .reset_index()
        .sort_values(["experiment_label", "trainings_to_95pct_final_best"])
    )
    for exp_label, part in effort_best.groupby("experiment_label", sort=False):
        top = part.iloc[0]
        text.append(f"- {exp_label}: menor custo mediano = {OPTIMIZER_LABELS[top.optimizer]} com {top.trainings_to_95pct_final_best:.0f} treinamentos.")

    if warnings:
        text.extend(["", "## Observacoes de qualidade dos dados", ""])
        text.extend(warnings)

    report_path.write_text("\n".join(text) + "\n", encoding="utf-8")
    return report_path


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    best = load_best_metrics()
    runs = load_runs()
    effort = summarize_effort(runs)
    summary = build_expected_summary(best, effort)

    summary_path = OUT_DIR / "saida_esperada_professor_summary.csv"
    effort_path = OUT_DIR / "saida_esperada_professor_effort_by_run.csv"
    summary.to_csv(summary_path, index=False)
    effort.to_csv(effort_path, index=False)

    paths = [
        plot_overview_1_2_3(best, OUT_DIR / "00_visao_geral_experimentos_1_2_3.png"),
        plot_exp1_mcc(best, OUT_DIR / "01_experimento_1_mcc_only.png"),
        plot_holdout_accuracy(best, OUT_DIR / "02_experimentos_1_2_holdout_accuracy.png"),
        plot_exp3_cv_accuracy(best, OUT_DIR / "03_experimento_3_cv_accuracy_only.png"),
        plot_training_efficiency(effort, OUT_DIR / "04_treinamentos_ate_bom_resultado_exp1_exp2_exp3.png"),
    ]
    report_path = write_markdown(summary, effort, paths)
    paths.extend([summary_path, effort_path, report_path])

    for path in paths:
        if path.suffix.lower() == ".png":
            shutil.copy2(path, DOWNLOADS_DIR / path.name)

    print("Saved professor expected outputs:")
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
