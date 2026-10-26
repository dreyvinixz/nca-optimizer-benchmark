#!/usr/bin/env python3
"""Extract raw WIN/IND candles and build causal future-direction targets/features."""
import argparse
import hashlib
import json
import sqlite3
import time
from pathlib import Path

import numpy as np
import pandas as pd
import yaml


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_market(path, roots):
    conn = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        conn.execute("PRAGMA query_only=ON")
        conn.execute("PRAGMA cache_size=-131072")
        conn.execute("PRAGMA temp_store=MEMORY")
        clauses = " OR ".join("t.ticker LIKE ?" for _ in roots)
        sql = f"""
            SELECT p.id_ticker, t.ticker, p.date, p.time,
                   p.open, p.high, p.low, p.close, p.volume,
                   p.business, p.amount_stock
            FROM ticker t JOIN price1 p ON p.id_ticker=t.id_ticker
            WHERE ({clauses}) AND p.time >= '09:00:00' AND p.time < '18:00:00'
            ORDER BY t.ticker, p.date, p.time
        """
        data = pd.read_sql_query(sql, conn, params=[f"{r}%" for r in roots])
    finally:
        conn.close()
    if data.empty:
        raise ValueError("No intraday rows for the configured roots")
    data["date"] = pd.to_datetime(data.date).dt.strftime("%Y-%m-%d")
    data["time"] = data.time.astype(str)
    for col in ("open", "high", "low", "close", "volume", "business", "amount_stock"):
        data[col] = pd.to_numeric(data[col], errors="coerce").astype(float)
    if data.duplicated(["ticker", "date", "time"]).any():
        raise ValueError("Duplicate (ticker,date,time) keys in the selected market data")
    data["minute"] = data.time.str.slice(0, 2).astype(int) * 60 + data.time.str.slice(3, 5).astype(int)
    same = data.ticker.eq(data.ticker.shift()) & data.date.eq(data.date.shift()) & data.minute.sub(data.minute.shift()).eq(1)
    data["segment_id"] = (~same).cumsum().astype("int32")
    return data


def _safe_div(a, b):
    return a.div(b.replace(0, np.nan))


def features_for_segment(g):
    close = g.close
    op, high, low = g.open, g.high, g.low
    log_close = np.log(close.where(close > 0))
    ret1 = log_close.diff()
    out = pd.DataFrame(index=g.index)

    # Multi-lag returns and candle geometry.
    for lag in (1, 2, 3, 5, 10, 15, 30):
        out[f"log_return_{lag}m"] = log_close - log_close.shift(lag)
    out["candle_body_fraction"] = (close - op) / close
    out["candle_range_fraction"] = (high - low) / close
    out["upper_wick_fraction"] = (high - pd.concat([op, close], axis=1).max(axis=1)) / close
    out["lower_wick_fraction"] = (pd.concat([op, close], axis=1).min(axis=1) - low) / close
    out["close_location_in_range"] = _safe_div(close - low, high - low)

    # Moving-average distances, momentum and MACD.
    for span in (5, 10, 15, 20, 30):
        ema = close.ewm(span=span, min_periods=span, adjust=False).mean()
        sma = close.rolling(span, min_periods=span).mean()
        out[f"ema_distance_{span}m"] = np.log(_safe_div(close, ema))
        out[f"sma_distance_{span}m"] = np.log(_safe_div(close, sma))
    ema12 = close.ewm(span=12, min_periods=12, adjust=False).mean()
    ema26 = close.ewm(span=26, min_periods=26, adjust=False).mean()
    macd = ema12 - ema26
    macd_signal = macd.ewm(span=9, min_periods=9, adjust=False).mean()
    out["macd_12_26_fraction"] = macd / close
    out["macd_signal_9_fraction"] = macd_signal / close
    out["macd_histogram_fraction"] = (macd - macd_signal) / close

    # RSI, stochastic oscillator, ATR and directional movement.
    delta = close.diff()
    gain, loss = delta.clip(lower=0), -delta.clip(upper=0)
    for window in (7, 14, 28):
        avg_gain = gain.rolling(window, min_periods=window).mean()
        avg_loss = loss.rolling(window, min_periods=window).mean()
        rs = _safe_div(avg_gain, avg_loss)
        rsi = 100 - (100 / (1 + rs))
        rsi = rsi.mask((avg_loss == 0) & (avg_gain > 0), 100)
        rsi = rsi.mask((avg_loss == 0) & (avg_gain == 0), 50)
        out[f"rsi_{window}m"] = rsi / 100
    for window in (14, 28):
        roll_high = high.rolling(window, min_periods=window).max()
        roll_low = low.rolling(window, min_periods=window).min()
        stoch = _safe_div(close - roll_low, roll_high - roll_low)
        out[f"stochastic_k_{window}m"] = stoch
        out[f"stochastic_d_{window}m"] = stoch.rolling(3, min_periods=3).mean()

    previous_close = close.shift(1)
    true_range = pd.concat([high - low, (high - previous_close).abs(), (low - previous_close).abs()], axis=1).max(axis=1)
    for window in (5, 14, 30):
        atr = true_range.rolling(window, min_periods=window).mean()
        out[f"atr_fraction_{window}m"] = atr / close

    up_move = high.diff()
    down_move = -low.diff()
    plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0.0)
    minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0.0)
    for window in (14, 28):
        atr = true_range.rolling(window, min_periods=window).mean()
        plus_di = 100 * _safe_div(plus_dm.rolling(window, min_periods=window).mean(), atr)
        minus_di = 100 * _safe_div(minus_dm.rolling(window, min_periods=window).mean(), atr)
        dx = 100 * _safe_div((plus_di - minus_di).abs(), plus_di + minus_di)
        out[f"plus_di_{window}m"] = plus_di / 100
        out[f"minus_di_{window}m"] = minus_di / 100
        out[f"adx_{window}m"] = dx.rolling(window, min_periods=window).mean() / 100

    # Return distribution and volatility/semivolatility.
    for window in (5, 10, 15, 20, 30):
        rolling_ret = ret1.rolling(window, min_periods=window)
        out[f"realized_volatility_{window}m"] = rolling_ret.std(ddof=0)
        out[f"upside_semivolatility_{window}m"] = ret1.clip(lower=0).rolling(window, min_periods=window).std(ddof=0)
        out[f"downside_semivolatility_{window}m"] = ret1.clip(upper=0).rolling(window, min_periods=window).std(ddof=0)

    # Bollinger and Donchian position/width.
    for window in (20, 30):
        mean = close.rolling(window, min_periods=window).mean()
        std = close.rolling(window, min_periods=window).std(ddof=0)
        upper, lower = mean + 2 * std, mean - 2 * std
        out[f"bollinger_percent_b_{window}m"] = _safe_div(close - lower, upper - lower)
        out[f"bollinger_width_{window}m"] = _safe_div(upper - lower, mean)
    for window in (10, 20, 30):
        roll_high = high.rolling(window, min_periods=window).max()
        roll_low = low.rolling(window, min_periods=window).min()
        out[f"donchian_position_{window}m"] = _safe_div(close - roll_low, roll_high - roll_low)
        out[f"donchian_width_{window}m"] = _safe_div(roll_high - roll_low, close)

    # Volume, transaction count and traded quantity surprises.
    for raw, name in (("volume", "volume"), ("business", "trades"), ("amount_stock", "quantity")):
        logged = np.log1p(g[raw].clip(lower=0))
        out[f"log_{name}"] = logged
        for window in (5, 15, 30):
            mean = logged.rolling(window, min_periods=window).mean()
            std = logged.rolling(window, min_periods=window).std(ddof=0)
            median = logged.rolling(window, min_periods=window).median()
            out[f"{name}_surprise_{window}m"] = logged - mean
            out[f"{name}_robust_surprise_{window}m"] = logged - median
            if window in (15, 30):
                out[f"{name}_zscore_{window}m"] = _safe_div(logged - mean, std)

    # Time-of-day encoding for the fixed local observation window 09:00-18:00.
    minute = g.minute.astype(float)
    phase = (minute - 540.0) / 540.0
    out["time_of_day_fraction"] = phase.clip(0, 1)
    out["time_of_day_sin"] = np.sin(2 * np.pi * phase)
    out["time_of_day_cos"] = np.cos(2 * np.pi * phase)
    return out.replace([np.inf, -np.inf], np.nan)


def build_dataset(raw, horizons):
    feature_frames = []
    for _, segment in raw.groupby("segment_id", sort=False):
        feature_frames.append(features_for_segment(segment))
    feat = pd.concat(feature_frames).sort_index()
    out = pd.concat([raw, feat], axis=1)
    # Causal session-to-date summaries include the completed current candle.
    # They reset for each contract and date and never carry into another day.
    session = out.groupby(["ticker", "date"], sort=False)
    session_open = session.open.transform("first")
    session_high = session.high.cummax()
    session_low = session.low.cummin()
    out["session_return_so_far"] = np.log(_safe_div(out.close, session_open))
    out["session_range_so_far"] = _safe_div(session_high - session_low, out.close)
    for raw_col, name in (("volume", "volume"), ("business", "trades"), ("amount_stock", "quantity")):
        cumulative = session[raw_col].cumsum()
        out[f"session_log_cumulative_{name}"] = np.log1p(cumulative.clip(lower=0))
    raw_features = [c for c in out.columns if c not in {"id_ticker", "ticker", "date", "time", "minute", "segment_id", "open", "high", "low", "close", "volume", "business", "amount_stock"}]
    bands = np.select(
        [out.minute < 12 * 60, out.minute < 15 * 60],
        ["early", "middle"], default="late",
    )
    out["time_band"] = bands
    out["session_fraction"] = ((out.minute - 540) / 540).clip(0, 1)
    for horizon in horizons:
        future_close = out.groupby(["ticker", "date"], sort=False).close.shift(-horizon)
        future_minute = out.groupby(["ticker", "date"], sort=False).minute.shift(-horizon)
        future_segment = out.groupby(["ticker", "date"], sort=False).segment_id.shift(-horizon)
        valid = future_minute.sub(out.minute).eq(horizon) & future_segment.eq(out.segment_id)
        forward = np.log(future_close.where(future_close > 0)) - np.log(out.close.where(out.close > 0))
        valid &= forward.notna()
        out[f"forward_log_return_{horizon}m"] = forward.where(valid)
        out[f"target_up_{horizon}m"] = np.where(valid, (forward > 0).astype(float), np.nan)
    out["date"] = out.date.astype(str)
    return out, raw_features


def main():
    started = time.perf_counter()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", type=Path, default=Path("config/intraday_direction_v2.yaml"))
    ap.add_argument("--market-db", type=Path, default=Path("data/bovdb-v3.1-internal.2.sqlite"))
    ap.add_argument("--output", type=Path, default=Path("data/derived/intraday_direction_v2_features.parquet"))
    args = ap.parse_args()
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    raw = read_market(args.market_db, config["source"]["roots"])
    out, features = build_dataset(raw, config["forecast_target"]["horizons_observed_bars"])
    targets = [f"target_up_{h}m" for h in config["forecast_target"]["horizons_observed_bars"]]
    keys = ["id_ticker", "ticker", "date", "time", "minute", "segment_id", "time_band", "session_fraction"]
    keep = keys + ["open", "high", "low", "close", "volume", "business", "amount_stock"] + features + [f"forward_log_return_{h}m" for h in config["forecast_target"]["horizons_observed_bars"]] + targets
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out[keep].to_parquet(args.output, index=False, compression="zstd")
    target_summary = {}
    for horizon in config["forecast_target"]["horizons_observed_bars"]:
        label = f"target_up_{horizon}m"
        target_summary[str(horizon)] = {
            "valid": int(out[label].notna().sum()),
            "up_prevalence": float(out[label].dropna().mean()),
            "by_band": {
                band: {
                    "n": int(out.loc[(out.time_band == band) & out[label].notna(), label].size),
                    "up_prevalence": float(out.loc[(out.time_band == band) & out[label].notna(), label].mean()),
                } for band in ("early", "middle", "late")
            },
        }
    manifest = {
        "study": config["study"], "status": config["status"],
        "source_sha256": sha256(args.market_db), "rows": len(out),
        "dates": int(out.date.nunique()), "roots": config["source"]["roots"],
        "time_range": [out.time.min(), out.time.max()],
        "feature_count": len(features), "feature_columns": features,
        "feature_rows_complete": int(out[features].notna().all(axis=1).sum()),
        "target_summary": target_summary,
        "output": str(args.output), "output_bytes": args.output.stat().st_size,
        "runtime_seconds": round(time.perf_counter() - started, 2),
        "config_sha256": hashlib.sha256(args.config.read_bytes()).hexdigest(),
        "builder_sha256": sha256(Path(__file__)),
        "independent_final_test_available": False,
    }
    args.output.with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
