"""File-driven paper trading simulator.

This is a bridge between offline research and a real-time data feed. It does
not send orders. It reads a CSV containing candles plus model signals, updates a
paper ledger, and writes theoretical trades.

Expected input columns:
datetime, open, high, low, close, y_pred, y_proba

Optional columns:
model, optimizer, experiment, seed

A signal at row i is executed on row i+1 open. If the next candle is not yet
available, the signal remains pending for the next run.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "professor_presentation" / "live_simulation" / "paper_trading"
REQUIRED_COLUMNS = ["datetime", "open", "high", "low", "close", "y_pred", "y_proba"]


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


def load_signals(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    missing = sorted(set(REQUIRED_COLUMNS) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns in {path}: {missing}")
    df = df.copy()
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime").reset_index(drop=True)
    df["signal_id"] = np.arange(len(df))
    for col, default in [
        ("model", "unknown"),
        ("optimizer", "unknown"),
        ("experiment", "paper"),
        ("seed", "paper"),
    ]:
        if col not in df.columns:
            df[col] = default
    return df


def load_ledger(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    ledger = pd.read_csv(path)
    for col in ["signal_datetime", "entry_datetime"]:
        if col in ledger.columns:
            ledger[col] = pd.to_datetime(ledger[col])
    return ledger


def summarize(ledger: pd.DataFrame) -> dict[str, Any]:
    closed = ledger[ledger["status"] == "closed"].copy() if not ledger.empty else pd.DataFrame()
    if closed.empty:
        return {
            "closed_trades": 0,
            "pending_signals": int((ledger["status"] == "pending").sum()) if not ledger.empty else 0,
            "total_profit_points": 0.0,
            "win_rate": 0.0,
            "profit_factor": 0.0,
            "max_drawdown_points": 0.0,
            "sharpe_ratio_annualized": 0.0,
        }
    returns = closed["net_points"].astype(float)
    equity = returns.cumsum()
    gross_profit = float(returns[returns > 0].sum())
    gross_loss = float(abs(returns[returns < 0].sum()))
    drawdown = equity - equity.cummax()
    daily = closed.groupby(closed["entry_datetime"].dt.date)["net_points"].sum()
    sharpe = 0.0
    if len(daily) > 1 and daily.std(ddof=1) > 0:
        sharpe = float((daily.mean() / daily.std(ddof=1)) * math.sqrt(252))
    return {
        "closed_trades": int(len(closed)),
        "pending_signals": int((ledger["status"] == "pending").sum()),
        "total_profit_points": float(returns.sum()),
        "win_rate": float((returns > 0).mean()),
        "profit_factor": float(gross_profit / gross_loss) if gross_loss > 0 else float("inf"),
        "max_drawdown_points": float(drawdown.min()),
        "sharpe_ratio_annualized": sharpe,
    }


def update_ledger(args: argparse.Namespace) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    signals = load_signals(Path(args.input_csv))
    ledger_path = Path(args.ledger) if args.ledger else OUT_DIR / "paper_trading_ledger.csv"
    summary_path = OUT_DIR / "paper_trading_summary.json"
    ledger = load_ledger(ledger_path)

    processed_ids = set()
    if not ledger.empty and "signal_id" in ledger.columns:
        processed_ids = set(ledger["signal_id"].astype(int).tolist())

    new_rows: list[dict[str, Any]] = []
    for i, row in signals.iterrows():
        signal_id = int(row["signal_id"])
        if signal_id in processed_ids:
            continue
        confidence = max(float(row["y_proba"]), 1.0 - float(row["y_proba"]))
        if confidence < args.min_confidence:
            continue

        if i + 1 >= len(signals):
            new_rows.append(
                {
                    "status": "pending",
                    "signal_id": signal_id,
                    "signal_datetime": row["datetime"],
                    "entry_datetime": pd.NaT,
                    "model": row["model"],
                    "optimizer": row["optimizer"],
                    "experiment": row["experiment"],
                    "seed": row["seed"],
                    "direction": "long" if int(row["y_pred"]) == 1 else "short",
                    "y_pred": int(row["y_pred"]),
                    "y_proba": float(row["y_proba"]),
                    "confidence": confidence,
                    "entry_price": np.nan,
                    "exit_price": np.nan,
                    "gross_points": np.nan,
                    "cost_points": args.cost_points,
                    "net_points": np.nan,
                    "exit_reason": "waiting_next_candle",
                }
            )
            continue

        nxt = signals.iloc[i + 1]
        direction = 1 if int(row["y_pred"]) == 1 else -1
        gross, exit_reason, exit_price = resolve_trade(
            direction,
            float(nxt["open"]),
            float(nxt["high"]),
            float(nxt["low"]),
            float(nxt["close"]),
            args.stop_points,
            args.target_points,
            args.ambiguous_policy,
        )
        new_rows.append(
            {
                "status": "closed",
                "signal_id": signal_id,
                "signal_datetime": row["datetime"],
                "entry_datetime": nxt["datetime"],
                "model": row["model"],
                "optimizer": row["optimizer"],
                "experiment": row["experiment"],
                "seed": row["seed"],
                "direction": "long" if direction == 1 else "short",
                "y_pred": int(row["y_pred"]),
                "y_proba": float(row["y_proba"]),
                "confidence": confidence,
                "entry_price": float(nxt["open"]),
                "exit_price": float(exit_price),
                "gross_points": float(gross),
                "cost_points": float(args.cost_points),
                "net_points": float(gross - args.cost_points),
                "exit_reason": exit_reason,
            }
        )

    if new_rows:
        ledger = pd.concat([ledger, pd.DataFrame(new_rows)], ignore_index=True)
        # If a signal was pending in a previous run and now has a next candle,
        # rebuild from scratch to keep the ledger deterministic.
        if (ledger["status"] == "pending").any() and len(signals) > 1:
            ledger_path.unlink(missing_ok=True)
            args_rebuild = argparse.Namespace(**vars(args))
            args_rebuild.ledger = str(ledger_path)
            # Prevent infinite recursion by writing only closed rows from the
            # current complete input; the final row may remain pending.
            ledger = pd.DataFrame()
            processed_ids = set()
            rebuilt_rows = []
            for i, row in signals.iterrows():
                signal_id = int(row["signal_id"])
                confidence = max(float(row["y_proba"]), 1.0 - float(row["y_proba"]))
                if confidence < args.min_confidence:
                    continue
                if i + 1 >= len(signals):
                    status_row = {
                        "status": "pending",
                        "signal_id": signal_id,
                        "signal_datetime": row["datetime"],
                        "entry_datetime": pd.NaT,
                        "model": row["model"],
                        "optimizer": row["optimizer"],
                        "experiment": row["experiment"],
                        "seed": row["seed"],
                        "direction": "long" if int(row["y_pred"]) == 1 else "short",
                        "y_pred": int(row["y_pred"]),
                        "y_proba": float(row["y_proba"]),
                        "confidence": confidence,
                        "entry_price": np.nan,
                        "exit_price": np.nan,
                        "gross_points": np.nan,
                        "cost_points": args.cost_points,
                        "net_points": np.nan,
                        "exit_reason": "waiting_next_candle",
                    }
                else:
                    nxt = signals.iloc[i + 1]
                    direction = 1 if int(row["y_pred"]) == 1 else -1
                    gross, exit_reason, exit_price = resolve_trade(
                        direction,
                        float(nxt["open"]),
                        float(nxt["high"]),
                        float(nxt["low"]),
                        float(nxt["close"]),
                        args.stop_points,
                        args.target_points,
                        args.ambiguous_policy,
                    )
                    status_row = {
                        "status": "closed",
                        "signal_id": signal_id,
                        "signal_datetime": row["datetime"],
                        "entry_datetime": nxt["datetime"],
                        "model": row["model"],
                        "optimizer": row["optimizer"],
                        "experiment": row["experiment"],
                        "seed": row["seed"],
                        "direction": "long" if direction == 1 else "short",
                        "y_pred": int(row["y_pred"]),
                        "y_proba": float(row["y_proba"]),
                        "confidence": confidence,
                        "entry_price": float(nxt["open"]),
                        "exit_price": float(exit_price),
                        "gross_points": float(gross),
                        "cost_points": float(args.cost_points),
                        "net_points": float(gross - args.cost_points),
                        "exit_reason": exit_reason,
                    }
                rebuilt_rows.append(status_row)
            ledger = pd.DataFrame(rebuilt_rows)

    if not ledger.empty:
        closed = ledger["status"] == "closed"
        ledger.loc[closed, "equity_points"] = ledger.loc[closed, "net_points"].astype(float).cumsum()
    ledger.to_csv(ledger_path, index=False)
    summary = summarize(ledger)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("Paper trading file simulation updated")
    print(f"Ledger: {ledger_path}")
    print(f"Summary: {summary_path}")
    print(json.dumps(summary, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Paper trading simulator from a candle/signal CSV.")
    parser.add_argument("--input-csv", required=True, help="CSV with datetime, OHLC, y_pred, y_proba.")
    parser.add_argument("--ledger", default=None, help="Optional ledger CSV path.")
    parser.add_argument("--cost-points", type=float, default=5.0)
    parser.add_argument("--min-confidence", type=float, default=0.0)
    parser.add_argument("--stop-points", type=float, default=None)
    parser.add_argument("--target-points", type=float, default=None)
    parser.add_argument("--ambiguous-policy", choices=["stop_first", "target_first"], default="stop_first")
    return parser


if __name__ == "__main__":
    update_ledger(build_parser().parse_args())
