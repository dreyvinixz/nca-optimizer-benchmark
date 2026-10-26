#!/usr/bin/env python3
"""Build causal, session-local features joined to the existing B4 targets."""
import argparse
import hashlib
import json
import sqlite3
import time
from pathlib import Path

import numpy as np
import pandas as pd
import yaml


def ro(path: Path):
    return sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)


def sha256(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_rows(market_db: Path, labels_db: Path, roots, explain_only=False):
    src = ro(market_db)
    try:
        src.execute("PRAGMA query_only=ON")
        # Cache hot SQLite pages in memory and filter ticker IDs before touching
        # the large minute tables. This avoids repeated full price1 scans.
        src.execute("PRAGMA cache_size=-131072")  # 128 MiB
        src.execute("PRAGMA temp_store=MEMORY")
        root_sql = " OR ".join("ticker LIKE ?" for _ in roots)
        params = [f"{r}%" for r in roots]
        query = f"""WITH selected_tickers AS MATERIALIZED (
            SELECT DISTINCT id_ticker,ticker FROM ticker WHERE ({root_sql})
          ), selected AS (
            SELECT p.id_ticker,t.ticker,p.date,p.time,p.open,p.high,p.low,p.close,
                   p.volume,p.business,p.amount_stock
            FROM selected_tickers t JOIN price1 p ON p.id_ticker=t.id_ticker
            WHERE p.time BETWEEN '09:00:00' AND '18:00:00'
          )
          SELECT p.id_ticker,p.ticker,p.date,p.time,
            p.open,p.high,p.low,p.close,p.volume,p.business,p.amount_stock,
            a.trend_label,b.trend_label,c.trend_label,m.trend_label,m.mean_score,
            a.segment_end_time,b.segment_end_time,c.segment_end_time
          FROM selected p
          LEFT JOIN labels.trend_5m a ON a.id_ticker=p.id_ticker AND a.date=CAST(p.date AS TEXT) AND a.time=CAST(p.time AS TEXT)
          LEFT JOIN labels.trend_10m b ON b.id_ticker=p.id_ticker AND b.date=CAST(p.date AS TEXT) AND b.time=CAST(p.time AS TEXT)
          LEFT JOIN labels.trend_15m c ON c.id_ticker=p.id_ticker AND c.date=CAST(p.date AS TEXT) AND c.time=CAST(p.time AS TEXT)
          LEFT JOIN labels.trend_mean m ON m.id_ticker=p.id_ticker AND m.date=CAST(p.date AS TEXT) AND m.time=CAST(p.time AS TEXT)
          ORDER BY p.ticker,p.date,p.time"""
        # Label DB has no ticker catalog; attach the read-only B4 database.
        src.execute("ATTACH DATABASE ? AS labels", (labels_db.resolve().as_uri() + "?mode=ro",))
        src.execute("PRAGMA labels.cache_size=-262144")  # 256 MiB
        if explain_only:
            for row in src.execute("EXPLAIN QUERY PLAN " + query, params):
                print(" | ".join(str(value) for value in row))
            return None
        rows = pd.read_sql_query(query, src, params=params)
    finally:
        src.close()
    names = ["id_ticker","ticker","date","time","open","high","low","close","volume","business","amount_stock","y5","y10","y15","y_majority","y_soft","end5","end10","end15"]
    rows.columns = names
    return rows


def add_features(df):
    if df.duplicated(["ticker", "date", "time"]).any():
        raise ValueError("Duplicate (ticker,date,time) source keys")
    df["minute"] = df.time.str.slice(0, 2).astype(int) * 60 + df.time.str.slice(3, 5).astype(int)
    df = df.sort_values(["ticker", "date", "time"]).reset_index(drop=True)
    same_series = df.ticker.eq(df.ticker.shift()) & df.date.eq(df.date.shift())
    gap = df.minute.sub(df.minute.shift()).ne(1)
    df["segment"] = (~same_series | gap).cumsum()
    log_close = np.log(pd.to_numeric(df.close, errors="coerce").astype(float))
    close = pd.to_numeric(df.close, errors="coerce").astype(float)
    for lag, name in ((1, "log_return_1m"), (5, "log_return_5m"), (15, "log_return_15m")):
        prior_log = log_close.shift(lag)
        same_segment = df.segment.eq(df.segment.shift(lag))
        df[name] = (log_close - prior_log).where(same_segment)
    close = close.replace(0, np.nan)
    op = pd.to_numeric(df.open, errors="coerce").astype(float)
    hi = pd.to_numeric(df.high, errors="coerce").astype(float)
    lo = pd.to_numeric(df.low, errors="coerce").astype(float)
    df["candle_body_fraction"] = (close - op) / close
    df["candle_range_fraction"] = (hi - lo) / close
    for win in (5, 15, 30):
        vol = df.log_return_1m.rolling(win, min_periods=win).std(ddof=0)
        within = df.segment.eq(df.segment.shift(win - 1))
        df[f"realized_volatility_{win}m"] = vol.where(within)
    for col, name in (("volume", "log_volume"), ("business", "log_business"), ("amount_stock", "log_amount_stock")):
        df[name] = np.log1p(pd.to_numeric(df[col], errors="coerce").clip(lower=0))
    df["date"] = pd.to_datetime(df.date).dt.strftime("%Y-%m-%d")
    return df


def main():
    started = time.perf_counter()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--protocol", type=Path, default=Path("config/experiment_protocol.yaml"))
    ap.add_argument("--market-db", type=Path, default=Path("data/bovdb-v3.1-internal.2.sqlite"))
    ap.add_argument("--labels-db", type=Path, default=Path("data/bovdb-labels-B4-v1.sqlite"))
    ap.add_argument("--output", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--explain", action="store_true", help="print SQLite query plan without reading rows")
    a = ap.parse_args()
    contract, protocol = yaml.safe_load(a.contract.read_text()), yaml.safe_load(a.protocol.read_text())
    roots = contract["universe"]["primary_roots"]
    if a.explain:
        load_rows(a.market_db, a.labels_db, roots, explain_only=True)
        return
    df = add_features(load_rows(a.market_db, a.labels_db, roots))
    if df.empty:
        raise ValueError("No matching rows; check data paths and ticker joins")
    feature_names = contract["features"]["generated"]
    if set(feature_names) - set(df.columns):
        raise ValueError("Feature contract and implementation differ")
    # Every non-null B4 label must carry an in-session segment end; this is
    # retained to support training-label maturity/purge checks.
    for y, end in (("y5", "end5"), ("y10", "end10"), ("y15", "end15")):
        bad = df[y].notna() & df[end].isna()
        if bad.any():
            raise ValueError(f"{int(bad.sum())} {y} labels lack segment endpoints")
    dates = sorted(df.date.unique())
    train_share, val_share, _ = protocol["temporal_validation"]["proportions"]
    n_train = int(len(dates) * train_share)
    n_val = int(len(dates) * val_share)
    cuts = {d: "train" if i < n_train else "validation" if i < n_train + n_val else "test" for i, d in enumerate(dates)}
    fold_cfg = protocol["temporal_validation"]["expanding_folds"]
    folds = []
    for fold_no in range(fold_cfg["count"]):
        val_start = fold_cfg["minimum_initial_training_sessions"] + fold_no * fold_cfg["validation_block_sessions"]
        val_end = val_start + fold_cfg["validation_block_sessions"]
        if val_end > n_train + n_val:
            break
        folds.append({"fold": fold_no + 1, "train_dates": [dates[0], dates[val_start - 1]], "validation_dates": [dates[val_start], dates[val_end - 1]], "train_sessions": val_start, "validation_sessions": val_end - val_start})
    df["split"] = df.date.map(cuts)
    df["segment_id"] = df.segment.astype("int32")
    df["contract_hash"] = hashlib.sha256(a.contract.read_bytes()).hexdigest()
    df["protocol_hash"] = hashlib.sha256(a.protocol.read_bytes()).hexdigest()
    keep = ["id_ticker", "ticker", "date", "time", "split", "segment_id", *feature_names, "y5", "y10", "y15", "y_majority", "y_soft", "end5", "end10", "end15", "contract_hash", "protocol_hash"]
    a.output.parent.mkdir(parents=True, exist_ok=True)
    df[keep].to_parquet(a.output, index=False, compression="zstd")
    source_hashes = {"market": sha256(a.market_db), "labels": sha256(a.labels_db)}
    summary = {"rows": len(df), "dates": len(dates), "roots": roots, "date_ranges": {s: [min(d for d in dates if cuts[d] == s), max(d for d in dates if cuts[d] == s)] for s in ("train", "validation", "test")}, "expanding_folds": folds, "target_coverage": {y: int(df[y].notna().sum()) for y in ("y5", "y10", "y15")}, "feature_rows_ready": int(df[feature_names].notna().all(axis=1).sum()), "output": str(a.output), "output_bytes": a.output.stat().st_size, "runtime_seconds": round(time.perf_counter() - started, 2), "source_sha256": source_hashes, "contract_hash": df.contract_hash.iloc[0], "protocol_hash": df.protocol_hash.iloc[0]}
    a.output.with_suffix(".manifest.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
