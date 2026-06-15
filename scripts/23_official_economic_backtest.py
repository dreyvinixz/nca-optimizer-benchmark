"""Official economic backtest for the two fitness regimes.

The legacy phase2 backtest is kept as historical context. This script uses the
official MLP+GWO predictions from the two final fitness experiments and aligns
them by row_id against the same chronological X_test block reconstructed from
the benchmark pipeline.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_loader import load_legacy_dataset
from src.feature_selection import select_features
from src.preprocessing import drop_missing_rows, keep_numeric_features
from src.utils.io import load_project_configs

OUT_ROOT = ROOT / "outputs" / "professor_presentation"
TABLE_DIR = OUT_ROOT / "tables"
FIGURE_DIR = OUT_ROOT / "figures"

PREDICTION_FILES = {
    "MCC/F1": ROOT / "outputs" / "article_official" / "predictions" / "mlp_gwo_predictions.csv",
    "Accuracy-CV": ROOT / "outputs" / "article_official_accuracy" / "predictions" / "mlp_gwo_predictions.csv",
}
SEEDS = [1, 2, 3]
TRANSACTION_COST_POINTS = 5.0


def ensure_dirs() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def calculate_max_drawdown(equity_curve: pd.Series) -> float:
    rolling_max = equity_curve.cummax()
    drawdown = equity_curve - rolling_max
    return float(drawdown.min())


def load_test_market_frame() -> pd.DataFrame:
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
    frame = drop_missing_rows(dataset.frame, modeling_columns)
    ordered = frame.sort_values(dataset.datetime_column).reset_index(drop=True)

    split_cfg = exp["split"]
    train_end = int(len(ordered) * float(split_cfg["train_size"]))
    val_end = train_end + int(len(ordered) * float(split_cfg["validation_size"]))
    test = ordered.iloc[val_end:].copy().reset_index(drop=True)
    required = [dataset.datetime_column, "open", "close", dataset.target_column]
    missing = sorted(set(required) - set(test.columns))
    if missing:
        raise ValueError(f"Missing required market columns for backtest: {missing}")

    test = test[required].copy()
    test["row_id"] = np.arange(len(test))
    test = test.rename(columns={dataset.datetime_column: "datetime", dataset.target_column: "trend"})
    test["datetime"] = pd.to_datetime(test["datetime"])
    return test


def summarize_returns(mode: str, seed: int | str, returns: pd.Series, datetimes: pd.Series) -> dict[str, Any]:
    equity = returns.cumsum()
    gross_profit = float(returns[returns > 0].sum())
    gross_loss = float(abs(returns[returns < 0].sum()))
    daily_returns = returns.groupby(pd.to_datetime(datetimes).dt.date).sum()
    sharpe = 0.0
    if len(daily_returns) > 1 and daily_returns.std(ddof=1) > 0:
        sharpe = float((daily_returns.mean() / daily_returns.std(ddof=1)) * math.sqrt(252))
    return {
        "fitness_mode": mode,
        "seed": seed,
        "total_trades": int(len(returns)),
        "total_profit_points": float(returns.sum()),
        "win_rate": float((returns > 0).mean()),
        "profit_factor": float(gross_profit / gross_loss) if gross_loss > 0 else float("inf"),
        "max_drawdown_points": calculate_max_drawdown(equity),
        "sharpe_ratio_annualized": sharpe,
    }


def build_mode_trades(mode: str, predictions_path: Path, market_test: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    if not predictions_path.exists():
        raise FileNotFoundError(f"Missing official predictions: {predictions_path}")

    predictions = pd.read_csv(predictions_path)
    predictions = predictions[predictions["seed"].isin(SEEDS)].copy()
    summaries: list[dict[str, Any]] = []
    trade_frames = []

    for seed in SEEDS:
        pred = predictions[predictions["seed"] == seed].sort_values("row_id").copy()
        if len(pred) != len(market_test):
            raise ValueError(
                f"{mode} seed {seed} has {len(pred)} predictions, expected {len(market_test)} test rows."
            )

        merged = market_test.merge(pred[["row_id", "seed", "y_true", "y_pred", "y_proba"]], on="row_id", how="left")
        if merged[["y_pred", "y_proba"]].isna().any().any():
            raise ValueError(f"{mode} seed {seed} produced missing predictions after row_id alignment.")

        merged["fitness_mode"] = mode
        merged["seed"] = seed
        merged["long_return_points"] = merged["close"] - merged["open"]
        merged["short_return_points"] = merged["open"] - merged["close"]
        merged["gross_return_points"] = np.where(
            merged["y_pred"].astype(int) == 1,
            merged["long_return_points"],
            merged["short_return_points"],
        )
        merged["net_return_points"] = merged["gross_return_points"] - TRANSACTION_COST_POINTS
        merged["equity_points"] = merged["net_return_points"].cumsum()
        trade_frames.append(merged)
        summaries.append(summarize_returns(mode, seed, merged["net_return_points"], merged["datetime"]))

    return pd.concat(trade_frames, ignore_index=True), summaries


def build_baseline(market_test: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    baseline = market_test.copy()
    baseline["fitness_mode"] = "Long-only baseline"
    baseline["seed"] = "baseline"
    baseline["y_pred"] = 1
    baseline["y_proba"] = 1.0
    baseline["gross_return_points"] = baseline["close"] - baseline["open"]
    baseline["net_return_points"] = baseline["gross_return_points"] - TRANSACTION_COST_POINTS
    baseline["equity_points"] = baseline["net_return_points"].cumsum()
    return baseline, summarize_returns(
        "Long-only baseline",
        "baseline",
        baseline["net_return_points"],
        baseline["datetime"],
    )


def bootstrap_mean_ci(values: np.ndarray, n_bootstrap: int = 20000, seed: int = 123) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    if len(values) == 0:
        return float("nan"), float("nan")
    samples = rng.choice(values, size=(n_bootstrap, len(values)), replace=True).mean(axis=1)
    low, high = np.quantile(samples, [0.025, 0.975])
    return float(low), float(high)


def sign_test_p_value(values: np.ndarray) -> float:
    values = values[values != 0]
    n = len(values)
    if n == 0:
        return 1.0
    positives = int((values > 0).sum())
    k = min(positives, n - positives)
    # Two-sided exact binomial test with p=0.5.
    prob = sum(math.comb(n, i) for i in range(k + 1)) / (2**n)
    return float(min(1.0, 2.0 * prob))


def statistical_tests(trades: pd.DataFrame) -> pd.DataFrame:
    daily = (
        trades[trades["fitness_mode"].isin(["MCC/F1", "Accuracy-CV"])]
        .groupby(["fitness_mode", "seed", trades["datetime"].dt.date])["net_return_points"]
        .sum()
        .reset_index(name="daily_return_points")
        .rename(columns={"datetime": "date"})
    )
    mode_daily = daily.groupby(["fitness_mode", "date"])["daily_return_points"].mean().unstack("fitness_mode")
    mode_daily = mode_daily.dropna(subset=["MCC/F1", "Accuracy-CV"])
    diff = (mode_daily["MCC/F1"] - mode_daily["Accuracy-CV"]).to_numpy()
    ci_low, ci_high = bootstrap_mean_ci(diff)
    row = {
        "comparison": "MCC/F1 minus Accuracy-CV",
        "n_days": int(len(diff)),
        "mean_daily_difference_points": float(np.mean(diff)) if len(diff) else float("nan"),
        "bootstrap_ci95_low": ci_low,
        "bootstrap_ci95_high": ci_high,
        "sign_test_p_value": sign_test_p_value(diff),
        "wilcoxon_p_value": float("nan"),
        "wilcoxon_note": "scipy not available",
    }
    try:
        from scipy.stats import wilcoxon

        row["wilcoxon_p_value"] = float(wilcoxon(diff, zero_method="wilcox").pvalue)
        row["wilcoxon_note"] = "two-sided Wilcoxon signed-rank test"
    except Exception:
        pass
    return pd.DataFrame([row])


def aggregate_summary(summary_by_seed: pd.DataFrame) -> pd.DataFrame:
    metric_cols = [
        "total_trades",
        "total_profit_points",
        "win_rate",
        "profit_factor",
        "max_drawdown_points",
        "sharpe_ratio_annualized",
    ]
    agg = summary_by_seed.groupby("fitness_mode")[metric_cols].agg(["mean", "std"]).reset_index()
    agg.columns = ["_".join(col).rstrip("_") if isinstance(col, tuple) else col for col in agg.columns]
    return agg


def plot_equity(trades: pd.DataFrame) -> Path:
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.1)
    fig, ax = plt.subplots(figsize=(11, 5.8))

    mean_equity = (
        trades.groupby(["fitness_mode", "row_id"])["equity_points"]
        .mean()
        .reset_index()
    )
    palette = {"MCC/F1": "#2364aa", "Accuracy-CV": "#f28e2b", "Long-only baseline": "#767676"}
    for mode, part in mean_equity.groupby("fitness_mode"):
        ax.plot(part["row_id"], part["equity_points"], label=mode, linewidth=2.4, color=palette.get(mode))

    ax.axhline(0, color="#222222", linewidth=0.8, alpha=0.5)
    ax.set_title("Backtest oficial - curva media de equity no X_test")
    ax.set_xlabel("Trade no periodo de teste")
    ax.set_ylabel("Pontos acumulados liquidos")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.35)
    fig.tight_layout()
    out = FIGURE_DIR / "official_backtest_equity_curve.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


def plot_metrics(summary_agg: pd.DataFrame) -> Path:
    import matplotlib.pyplot as plt
    import seaborn as sns

    metrics = [
        ("total_profit_points_mean", "Lucro liquido (pts)"),
        ("profit_factor_mean", "Profit factor"),
        ("sharpe_ratio_annualized_mean", "Sharpe anualizado"),
        ("max_drawdown_points_mean", "Max drawdown (pts)"),
    ]
    plot_df = summary_agg[summary_agg["fitness_mode"].isin(["MCC/F1", "Accuracy-CV", "Long-only baseline"])].copy()
    long = []
    for col, label in metrics:
        for _, row in plot_df.iterrows():
            long.append({"fitness_mode": row["fitness_mode"], "metric": label, "value": row[col]})
    long_df = pd.DataFrame(long)

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.05)
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.2))
    palette = {"MCC/F1": "#2364aa", "Accuracy-CV": "#f28e2b", "Long-only baseline": "#767676"}
    for ax, (_, label) in zip(axes.ravel(), metrics):
        part = long_df[long_df["metric"] == label]
        sns.barplot(data=part, x="fitness_mode", y="value", palette=palette, ax=ax, hue="fitness_mode", legend=False)
        ax.set_title(label)
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.tick_params(axis="x", rotation=15)
        ax.grid(axis="y", alpha=0.35)
    fig.suptitle("Backtest oficial - metricas economicas no periodo de teste", y=0.995)
    fig.tight_layout()
    out = FIGURE_DIR / "official_backtest_metrics.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    ensure_dirs()
    market_test = load_test_market_frame()

    trade_frames = []
    summary_rows: list[dict[str, Any]] = []
    for mode, path in PREDICTION_FILES.items():
        trades, summaries = build_mode_trades(mode, path, market_test)
        trade_frames.append(trades)
        summary_rows.extend(summaries)

    baseline_trades, baseline_summary = build_baseline(market_test)
    trade_frames.append(baseline_trades)
    summary_rows.append(baseline_summary)

    trades_all = pd.concat(trade_frames, ignore_index=True)
    summary_by_seed = pd.DataFrame(summary_rows)
    summary_agg = aggregate_summary(summary_by_seed)
    tests = statistical_tests(trades_all)

    trades_path = TABLE_DIR / "official_backtest_trades.csv"
    summary_seed_path = TABLE_DIR / "official_backtest_summary_by_seed.csv"
    summary_path = TABLE_DIR / "official_backtest_summary.csv"
    tests_path = TABLE_DIR / "official_backtest_statistical_tests.csv"
    metadata_path = TABLE_DIR / "official_backtest_metadata.json"

    trades_all.to_csv(trades_path, index=False)
    summary_by_seed.to_csv(summary_seed_path, index=False)
    summary_agg.to_csv(summary_path, index=False)
    tests.to_csv(tests_path, index=False)

    equity_path = plot_equity(trades_all)
    metrics_path = plot_metrics(summary_agg)

    metadata = {
        "model": "MLP",
        "optimizer": "GWO",
        "seeds": SEEDS,
        "transaction_cost_points": TRANSACTION_COST_POINTS,
        "alignment": "predictions row_id aligned to reconstructed chronological X_test frame",
        "rows_per_seed": int(len(market_test)),
        "test_start": str(market_test["datetime"].min()),
        "test_end": str(market_test["datetime"].max()),
        "outputs": {
            "trades": str(trades_path.relative_to(ROOT)),
            "summary_by_seed": str(summary_seed_path.relative_to(ROOT)),
            "summary": str(summary_path.relative_to(ROOT)),
            "statistical_tests": str(tests_path.relative_to(ROOT)),
            "equity_curve": str(equity_path.relative_to(ROOT)),
            "metrics": str(metrics_path.relative_to(ROOT)),
        },
    }
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print("Official economic backtest complete:")
    print(summary_agg.to_string(index=False))
    print(f"Saved: {summary_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
