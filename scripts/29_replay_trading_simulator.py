"""Offline candle-by-candle replay simulator for saved model predictions.

The simulator uses the already generated prediction files and reconstructs the
same chronological X_test market block. A prediction at row i opens a simulated
trade on row i+1, so the model never trades on the same candle used to produce
the signal.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import sys
from dataclasses import dataclass
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


OUT_DIR = ROOT / "outputs" / "professor_presentation" / "live_simulation" / "offline_replay"
SEEDS = [1, 2, 3]
MODELS = ["cnn", "mlp", "rf", "svm"]
OPTIMIZERS = ["de", "ga", "gwo", "pso", "random_search"]


@dataclass(frozen=True)
class Experiment:
    key: str
    label: str
    predictions_dir: Path


EXPERIMENTS = [
    Experiment("exp1_holdout_mcc_f1", "Exp. 1 - Holdout + MCC/F1", ROOT / "outputs" / "article_official" / "predictions"),
    Experiment(
        "exp2_holdout_accuracy",
        "Exp. 2 - Holdout + Accuracy",
        ROOT / "outputs" / "article_official_accuracy_holdout" / "predictions",
    ),
    Experiment("exp3_cv_accuracy", "Exp. 3 - CV + Accuracy", ROOT / "outputs" / "article_official_accuracy" / "predictions"),
]


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

    required = [dataset.datetime_column, "open", "high", "low", "close", dataset.target_column]
    missing = sorted(set(required) - set(test.columns))
    if missing:
        raise ValueError(f"Missing required market columns: {missing}")

    test = test[required].copy()
    test["row_id"] = np.arange(len(test))
    test = test.rename(columns={dataset.datetime_column: "datetime", dataset.target_column: "trend"})
    test["datetime"] = pd.to_datetime(test["datetime"])
    return test


def parse_time(value: str | None) -> tuple[int, int] | None:
    if not value:
        return None
    hour, minute = value.split(":")
    return int(hour), int(minute)


def time_allowed(ts: pd.Timestamp, start: tuple[int, int] | None, end: tuple[int, int] | None) -> bool:
    minutes = ts.hour * 60 + ts.minute
    if start:
        start_minutes = start[0] * 60 + start[1]
        if minutes < start_minutes:
            return False
    if end:
        end_minutes = end[0] * 60 + end[1]
        if minutes > end_minutes:
            return False
    return True


def resolve_trade(
    direction: int,
    entry_price: float,
    high: float,
    low: float,
    close: float,
    stop_points: float | None,
    target_points: float | None,
    ambiguous_policy: str,
) -> tuple[float, str, float]:
    """Return gross points, exit reason, and exit price for one-candle trade."""
    if direction == 1:
        stop_hit = stop_points is not None and low <= entry_price - stop_points
        target_hit = target_points is not None and high >= entry_price + target_points
        if stop_hit and target_hit:
            if ambiguous_policy == "target_first":
                return float(target_points), "target_ambiguous", entry_price + float(target_points)
            return -float(stop_points), "stop_ambiguous", entry_price - float(stop_points)
        if target_hit:
            return float(target_points), "target", entry_price + float(target_points)
        if stop_hit:
            return -float(stop_points), "stop", entry_price - float(stop_points)
        return close - entry_price, "close", close

    stop_hit = stop_points is not None and high >= entry_price + stop_points
    target_hit = target_points is not None and low <= entry_price - target_points
    if stop_hit and target_hit:
        if ambiguous_policy == "target_first":
            return float(target_points), "target_ambiguous", entry_price - float(target_points)
        return -float(stop_points), "stop_ambiguous", entry_price + float(stop_points)
    if target_hit:
        return float(target_points), "target", entry_price - float(target_points)
    if stop_hit:
        return -float(stop_points), "stop", entry_price + float(stop_points)
    return entry_price - close, "close", close


def summarize_trades(trades: pd.DataFrame) -> dict[str, Any]:
    if trades.empty:
        return {
            "total_trades": 0,
            "total_profit_points": 0.0,
            "mean_trade_points": 0.0,
            "win_rate": 0.0,
            "profit_factor": 0.0,
            "max_drawdown_points": 0.0,
            "sharpe_ratio_annualized": 0.0,
        }
    returns = trades["net_points"].astype(float)
    equity = returns.cumsum()
    gross_profit = float(returns[returns > 0].sum())
    gross_loss = float(abs(returns[returns < 0].sum()))
    rolling_max = equity.cummax()
    drawdown = equity - rolling_max
    daily = trades.groupby(trades["entry_datetime"].dt.date)["net_points"].sum()
    sharpe = 0.0
    if len(daily) > 1 and daily.std(ddof=1) > 0:
        sharpe = float((daily.mean() / daily.std(ddof=1)) * math.sqrt(252))
    return {
        "total_trades": int(len(trades)),
        "total_profit_points": float(returns.sum()),
        "mean_trade_points": float(returns.mean()),
        "win_rate": float((returns > 0).mean()),
        "profit_factor": float(gross_profit / gross_loss) if gross_loss > 0 else float("inf"),
        "max_drawdown_points": float(drawdown.min()),
        "sharpe_ratio_annualized": sharpe,
    }


def replay_predictions(
    predictions: pd.DataFrame,
    market: pd.DataFrame,
    *,
    experiment: Experiment,
    model: str,
    optimizer: str,
    seed: int,
    cost_points: float,
    min_confidence: float,
    stop_points: float | None,
    target_points: float | None,
    max_trades_per_day: int | None,
    start_time: tuple[int, int] | None,
    end_time: tuple[int, int] | None,
    ambiguous_policy: str,
) -> pd.DataFrame:
    pred = predictions[predictions["seed"] == seed].sort_values("row_id").copy()
    if pred.empty:
        return pd.DataFrame()

    merged = pred.merge(
        market[["row_id", "datetime", "open", "high", "low", "close", "trend"]],
        on="row_id",
        how="left",
        suffixes=("_signal", "_signal_market"),
    )
    execution = market[["row_id", "datetime", "open", "high", "low", "close", "trend"]].copy()
    execution["signal_row_id"] = execution["row_id"] - 1
    merged = merged.merge(
        execution,
        left_on="row_id",
        right_on="signal_row_id",
        how="left",
        suffixes=("_signal", "_entry"),
    )
    merged = merged.dropna(subset=["open_entry", "high_entry", "low_entry", "close_entry"]).copy()

    daily_counts: dict[Any, int] = {}
    rows: list[dict[str, Any]] = []
    for row in merged.itertuples(index=False):
        signal_dt = pd.Timestamp(row.datetime_signal)
        entry_dt = pd.Timestamp(row.datetime)
        if not time_allowed(entry_dt, start_time, end_time):
            continue
        confidence = max(float(row.y_proba), 1.0 - float(row.y_proba))
        if confidence < min_confidence:
            continue
        trade_day = entry_dt.date()
        if max_trades_per_day is not None and daily_counts.get(trade_day, 0) >= max_trades_per_day:
            continue

        direction = 1 if int(row.y_pred) == 1 else -1
        gross, exit_reason, exit_price = resolve_trade(
            direction,
            float(row.open_entry),
            float(row.high_entry),
            float(row.low_entry),
            float(row.close_entry),
            stop_points,
            target_points,
            ambiguous_policy,
        )
        net = gross - cost_points
        daily_counts[trade_day] = daily_counts.get(trade_day, 0) + 1
        rows.append(
            {
                "experiment": experiment.key,
                "experiment_label": experiment.label,
                "model": model,
                "optimizer": optimizer,
                "seed": seed,
                "signal_row_id": int(row.row_id_signal),
                "entry_row_id": int(row.row_id_entry),
                "signal_datetime": signal_dt,
                "entry_datetime": entry_dt,
                "direction": "long" if direction == 1 else "short",
                "y_true_signal": int(row.y_true),
                "y_pred": int(row.y_pred),
                "y_proba": float(row.y_proba),
                "confidence": confidence,
                "entry_price": float(row.open_entry),
                "exit_price": float(exit_price),
                "entry_high": float(row.high_entry),
                "entry_low": float(row.low_entry),
                "entry_close": float(row.close_entry),
                "gross_points": float(gross),
                "cost_points": float(cost_points),
                "net_points": float(net),
                "exit_reason": exit_reason,
            }
        )
    trades = pd.DataFrame(rows)
    if not trades.empty:
        trades["equity_points"] = trades["net_points"].cumsum()
    return trades


def run(args: argparse.Namespace) -> None:
    out_dir = OUT_DIR / args.output_tag if args.output_tag else OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    market = load_test_market_frame()
    start = parse_time(args.start_time)
    end = parse_time(args.end_time)

    experiments = [exp for exp in EXPERIMENTS if args.experiment == "all" or exp.key == args.experiment]
    models = MODELS if args.model == "all" else [args.model]
    optimizers = OPTIMIZERS if args.optimizer == "all" else [args.optimizer]
    seeds = SEEDS if args.seed == "all" else [int(args.seed)]

    all_trades: list[pd.DataFrame] = []
    summary_rows: list[dict[str, Any]] = []
    missing: list[Path] = []
    for exp in experiments:
        for model in models:
            for optimizer in optimizers:
                path = exp.predictions_dir / f"{model}_{optimizer}_predictions.csv"
                if not path.exists():
                    missing.append(path)
                    continue
                predictions = pd.read_csv(path)
                for seed in seeds:
                    trades = replay_predictions(
                        predictions,
                        market,
                        experiment=exp,
                        model=model,
                        optimizer=optimizer,
                        seed=seed,
                        cost_points=args.cost_points,
                        min_confidence=args.min_confidence,
                        stop_points=args.stop_points,
                        target_points=args.target_points,
                        max_trades_per_day=args.max_trades_per_day,
                        start_time=start,
                        end_time=end,
                        ambiguous_policy=args.ambiguous_policy,
                    )
                    if not trades.empty:
                        all_trades.append(trades)
                    summary_rows.append(
                        {
                            "experiment": exp.key,
                            "experiment_label": exp.label,
                            "model": model,
                            "optimizer": optimizer,
                            "seed": seed,
                            **summarize_trades(trades),
                        }
                    )

    trades_all = pd.concat(all_trades, ignore_index=True) if all_trades else pd.DataFrame()
    summary = pd.DataFrame(summary_rows)
    combo_summary = (
        summary.groupby(["experiment", "experiment_label", "model", "optimizer"])
        .agg(
            n=("seed", "nunique"),
            total_profit_mean=("total_profit_points", "mean"),
            total_profit_std=("total_profit_points", "std"),
            win_rate_mean=("win_rate", "mean"),
            profit_factor_mean=("profit_factor", "mean"),
            max_drawdown_mean=("max_drawdown_points", "mean"),
            sharpe_mean=("sharpe_ratio_annualized", "mean"),
            total_trades_mean=("total_trades", "mean"),
        )
        .reset_index()
        .sort_values("total_profit_mean", ascending=False)
    )

    trades_path = out_dir / "offline_replay_trades.csv"
    summary_path = out_dir / "offline_replay_summary_by_seed.csv"
    combo_path = out_dir / "offline_replay_summary_by_combo.csv"
    metadata_path = out_dir / "offline_replay_metadata.json"
    trades_all.to_csv(trades_path, index=False)
    summary.to_csv(summary_path, index=False)
    combo_summary.to_csv(combo_path, index=False)
    metadata_path.write_text(
        json.dumps(
            {
                "cost_points": args.cost_points,
                "min_confidence": args.min_confidence,
                "stop_points": args.stop_points,
                "target_points": args.target_points,
                "max_trades_per_day": args.max_trades_per_day,
                "start_time": args.start_time,
                "end_time": args.end_time,
                "ambiguous_policy": args.ambiguous_policy,
                "signal_execution_rule": "signal at row i enters on row i+1 open and exits on that candle",
                "missing_prediction_files": [str(path.relative_to(ROOT)) for path in missing],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    shutil.copy2(combo_path, Path.home() / "Downloads" / combo_path.name)
    print("Offline replay complete")
    print(f"Trades: {trades_path}")
    print(f"Summary: {combo_path}")
    print("Top 10 combinations:")
    print(combo_summary.head(10).round(4).to_string(index=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Offline replay trading simulator.")
    parser.add_argument("--experiment", default="all", choices=["all", *(exp.key for exp in EXPERIMENTS)])
    parser.add_argument("--model", default="all", choices=["all", *MODELS])
    parser.add_argument("--optimizer", default="all", choices=["all", *OPTIMIZERS])
    parser.add_argument("--seed", default="all")
    parser.add_argument("--cost-points", type=float, default=5.0)
    parser.add_argument("--min-confidence", type=float, default=0.0)
    parser.add_argument("--stop-points", type=float, default=None)
    parser.add_argument("--target-points", type=float, default=None)
    parser.add_argument("--max-trades-per-day", type=int, default=None)
    parser.add_argument("--start-time", default=None, help="Optional HH:MM entry start time.")
    parser.add_argument("--end-time", default=None, help="Optional HH:MM entry end time.")
    parser.add_argument("--ambiguous-policy", choices=["stop_first", "target_first"], default="stop_first")
    parser.add_argument("--output-tag", default=None, help="Optional subfolder name to keep scenarios separate.")
    return parser


if __name__ == "__main__":
    run(build_parser().parse_args())
