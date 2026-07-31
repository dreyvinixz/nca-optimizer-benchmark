"""Build a model-ready 5-minute dataset from Quantbase 1-second candles.

The Quantbase backend stores new market data as daily Parquet files under
`worker/data_lake/gold/candles_1s`. This script converts those files into the
same broad column family used by `data/raw/merged_output.csv`, so the 2026 data
can be used as an out-of-time replay/validation sample.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


DEFAULT_QUANTBASE_ROOT = Path(
    r"C:\mysystems\services\quantbase-projectmain-repositories\quantbase-backend"
)
DEFAULT_CANDLES_DIR = DEFAULT_QUANTBASE_ROOT / "worker" / "data_lake" / "gold" / "candles_1s"
DEFAULT_OUTPUT = ROOT / "data" / "external" / "quantbase_2026_5m_model_ready.csv"


@dataclass(frozen=True)
class DailySelection:
    file: str
    date: str
    selected_symbol: str
    rows_1s: int
    volume_1s: float
    candles_5m: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aggregate Quantbase 1-second candles into a 5-minute model-ready CSV."
    )
    parser.add_argument("--candles-dir", type=Path, default=DEFAULT_CANDLES_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--metadata-output", type=Path, default=None)
    parser.add_argument("--start-date", default="2026-01-01", help="Inclusive YYYY-MM-DD.")
    parser.add_argument("--end-date", default="2026-12-31", help="Inclusive YYYY-MM-DD.")
    parser.add_argument(
        "--symbol",
        default=None,
        help="Exact contract/symbol, e.g. WINQ26. If omitted, choose the top-volume symbol per day.",
    )
    parser.add_argument(
        "--symbol-regex",
        default=r"^WIN[A-Z]\d{2}$",
        help="Regex used before top-volume selection. Default selects mini-index futures contracts.",
    )
    parser.add_argument("--bar-frequency", default="5min")
    parser.add_argument("--target-horizon", type=int, default=1)
    parser.add_argument("--drop-flat-targets", action="store_true")
    return parser.parse_args()


def parquet_files(candles_dir: Path, start: pd.Timestamp, end: pd.Timestamp) -> Iterable[Path]:
    if not candles_dir.exists():
        raise FileNotFoundError(f"Quantbase candles directory not found: {candles_dir}")

    for path in sorted(candles_dir.glob("Trades_*.parquet")):
        match = re.search(r"Trades_(\d{4}-\d{2}-\d{2})\.parquet$", path.name)
        if not match:
            continue
        file_date = pd.Timestamp(match.group(1))
        if start <= file_date <= end:
            yield path


def choose_symbol(day: pd.DataFrame, exact_symbol: str | None, symbol_regex: str) -> tuple[str, pd.DataFrame]:
    if exact_symbol:
        selected = day[day["symbol"].astype(str) == exact_symbol].copy()
        if selected.empty:
            return exact_symbol, selected
        return exact_symbol, selected

    mask = day["symbol"].astype(str).str.match(symbol_regex, na=False)
    candidates = day[mask].copy()
    if candidates.empty:
        return "", candidates

    volume_by_symbol = candidates.groupby("symbol", observed=True)["volume"].sum()
    selected_symbol = str(volume_by_symbol.sort_values(ascending=False).index[0])
    return selected_symbol, candidates[candidates["symbol"] == selected_symbol].copy()


def aggregate_5m(day: pd.DataFrame, frequency: str) -> pd.DataFrame:
    day = day.sort_values("datetime").copy()
    day["bar_time"] = day["datetime"].dt.floor(frequency)
    day["price_x_volume"] = day["close"].astype(float) * day["volume"].astype(float)

    grouped = day.groupby("bar_time", sort=True)
    candles = grouped.agg(
        datetime=("bar_time", "first"),
        symbol=("symbol", "first"),
        open=("open", "first"),
        high=("high", "max"),
        low=("low", "min"),
        close=("close", "last"),
        amount_stock=("volume", "sum"),
        business=("trades_count", "sum"),
        price_x_volume=("price_x_volume", "sum"),
    ).reset_index(drop=True)
    candles["average"] = np.where(
        candles["amount_stock"] > 0,
        candles["price_x_volume"] / candles["amount_stock"],
        candles["close"],
    )
    candles["volume"] = candles["price_x_volume"]
    candles = candles.drop(columns=["price_x_volume"])
    return candles[
        ["datetime", "symbol", "open", "high", "low", "average", "volume", "close", "business", "amount_stock"]
    ]


def add_indicators(frame: pd.DataFrame, target_horizon: int, drop_flat_targets: bool) -> pd.DataFrame:
    out = frame.sort_values("datetime").reset_index(drop=True).copy()
    for window in (3, 5, 7, 9):
        out[f"SMA_{window}"] = out["close"].rolling(window=window, min_periods=window).mean()
        out[f"EMA_{window}"] = out["close"].ewm(span=window, adjust=False).mean()
        out[f"std_close{window}"] = out["close"].rolling(window=window, min_periods=window).std(ddof=0)
        out[f"std_open{window}"] = out["open"].rolling(window=window, min_periods=window).std(ddof=0)

    for larger, smaller in ((5, 3), (7, 3), (7, 5), (9, 3), (9, 5), (9, 7)):
        out[f"SMA_{larger}-{smaller}"] = out[f"SMA_{larger}"] - out[f"SMA_{smaller}"]
        out[f"EMA_{larger}-{smaller}"] = out[f"EMA_{larger}"] - out[f"EMA_{smaller}"]

    price_range = out["high"] - out["low"]
    out["valid_range"] = price_range > 0
    safe_range = price_range.where(out["valid_range"])

    normalized_sources = [
        "SMA_3",
        "EMA_3",
        "SMA_5",
        "EMA_5",
        "SMA_7",
        "EMA_7",
        "SMA_9",
        "EMA_9",
        "open",
        "close",
        "SMA_5-3",
        "SMA_7-3",
        "SMA_7-5",
        "SMA_9-3",
        "SMA_9-5",
        "SMA_9-7",
        "EMA_5-3",
        "EMA_7-3",
        "EMA_7-5",
        "EMA_9-3",
        "EMA_9-5",
        "EMA_9-7",
        "std_close3",
        "std_close5",
        "std_close7",
        "std_close9",
        "std_open3",
        "std_open5",
        "std_open7",
        "std_open9",
    ]
    for column in normalized_sources:
        if column in {"open", "close", "SMA_3", "EMA_3", "SMA_5", "EMA_5", "SMA_7", "EMA_7", "SMA_9", "EMA_9"}:
            raw = out[column] - out["open"]
        else:
            raw = out[column]
        out[f"{column}_normalized"] = (raw / safe_range).replace([np.inf, -np.inf], np.nan).fillna(0.0)

    future_close = out["close"].shift(-1 * int(target_horizon))
    delta = future_close - out["close"]
    out["trend"] = np.where(delta > 0, "uptrend", "downtrend")
    if drop_flat_targets:
        out = out[delta != 0].copy()
    out = out[future_close.notna()].copy()
    out["id_ticker"] = pd.factorize(out["symbol"])[0] + 1
    return out


def build_dataset(args: argparse.Namespace) -> tuple[pd.DataFrame, list[DailySelection]]:
    start = pd.Timestamp(args.start_date)
    end = pd.Timestamp(args.end_date)
    frames: list[pd.DataFrame] = []
    selections: list[DailySelection] = []

    for path in parquet_files(args.candles_dir, start, end):
        day = pd.read_parquet(path, columns=["datetime", "symbol", "open", "high", "low", "close", "volume", "trades_count"])
        day["datetime"] = pd.to_datetime(day["datetime"])
        selected_symbol, selected = choose_symbol(day, args.symbol, args.symbol_regex)
        if selected.empty:
            continue
        candles = aggregate_5m(selected, args.bar_frequency)
        frames.append(candles)
        selections.append(
            DailySelection(
                file=path.name,
                date=str(pd.Timestamp(selected["datetime"].iloc[0]).date()),
                selected_symbol=selected_symbol,
                rows_1s=int(len(selected)),
                volume_1s=float(selected["volume"].sum()),
                candles_5m=int(len(candles)),
            )
        )

    if not frames:
        raise ValueError(
            "No Quantbase rows matched the requested range/symbol filters. "
            f"candles_dir={args.candles_dir}, symbol={args.symbol}, regex={args.symbol_regex}"
        )

    aggregated = pd.concat(frames, ignore_index=True).sort_values("datetime").reset_index(drop=True)
    return add_indicators(aggregated, args.target_horizon, args.drop_flat_targets), selections


def main() -> None:
    args = parse_args()
    dataset, selections = build_dataset(args)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(args.output, index=False)

    metadata_output = args.metadata_output
    if metadata_output is None:
        metadata_output = args.output.with_suffix(".metadata.json")
    metadata_output.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "source": str(args.candles_dir),
        "output": str(args.output),
        "start_date": args.start_date,
        "end_date": args.end_date,
        "symbol": args.symbol,
        "symbol_regex": args.symbol_regex,
        "bar_frequency": args.bar_frequency,
        "target_horizon": args.target_horizon,
        "rows": int(len(dataset)),
        "columns": list(dataset.columns),
        "daily_selection": [asdict(item) for item in selections],
    }
    metadata_output.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(f"Saved {len(dataset):,} rows to {args.output}")
    print(f"Saved metadata to {metadata_output}")
    print("Daily symbol selections:")
    for item in selections[:10]:
        print(f"  {item.date}: {item.selected_symbol} ({item.rows_1s:,} 1s rows -> {item.candles_5m:,} bars)")
    if len(selections) > 10:
        print(f"  ... {len(selections) - 10} more days")


if __name__ == "__main__":
    main()
