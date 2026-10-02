r"""Read-only reproduction audit for the archived WIN trend labels.

This script mirrors the relevant behavior of:
  D:\bovdb\code\examples\candle_logic.py
  D:\bovdb\code\examples\rotulos_dabase_create.py

It reads the source price and label SQLite databases in read-only mode, writes
nothing, and compares generated flags with the saved Rotule_price5 rows. If the
article's merged CSV is present, it also checks the one-row forward alignment.
"""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

import pandas as pd


def connect_read_only(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def recreate_for_ticker(price: pd.DataFrame) -> pd.DataFrame:
    """Reproduce the source pivot detector and label state machine in memory."""
    # The original DataProcessor sets the datetime index on the input frame,
    # then rebinds its own self.df to a session-filtered frame. The labeling
    # script iterates its original df reference afterward, so labels are
    # emitted for all source rows while pivots are detected on 09:00--17:30.
    rows = price.copy()
    rows["datetime"] = pd.to_datetime(
        rows["date"].astype(str) + " " + rows["time"].astype(str),
        format="%Y-%m-%d %H:%M:%S",
    )
    rows = rows.set_index("datetime").sort_index()
    session = rows[
        (rows.index.time >= pd.Timestamp("09:00").time())
        & (rows.index.time <= pd.Timestamp("17:30").time())
    ]

    agg = {"open": "first", "close": "last", "high": "max", "low": "min", "volume": "sum"}
    hourly = session.resample("60min").agg(agg).dropna()
    five_minute = session.resample("5min").agg(agg).dropna()

    tops: list[tuple[pd.Timestamp, float]] = []
    bottoms: list[tuple[pd.Timestamp, float]] = []
    i = 0
    while i < len(hourly) - 1:
        candle = hourly.iloc[i]
        if candle["close"] > candle["open"]:
            run = [candle]
            while i + 1 < len(hourly) and hourly.iloc[i + 1]["close"] > hourly.iloc[i + 1]["open"]:
                i += 1
                run.append(hourly.iloc[i])
            peak = max(run, key=lambda x: x["close"])
            interval = five_minute[
                (five_minute.index >= peak.name)
                & (five_minute.index < peak.name + pd.Timedelta(minutes=60))
            ]
            if not interval.empty:
                extreme = interval["close"].max()
                pivot_time = interval[interval["close"] == extreme].index[0]
                tops.append((pivot_time, interval.loc[pivot_time, "close"]))
                if i + 1 < len(hourly):
                    following = hourly.iloc[i + 1]
                    next_interval = five_minute[
                        (five_minute.index >= following.name)
                        & (five_minute.index < following.name + pd.Timedelta(minutes=60))
                    ]
                    if not next_interval.empty and next_interval["close"].max() > extreme:
                        new_extreme = next_interval["close"].max()
                        new_time = next_interval[next_interval["close"] == new_extreme].index[0]
                        tops[-1] = (new_time, next_interval.loc[new_time, "close"])
        else:
            run = [candle]
            while i + 1 < len(hourly) and hourly.iloc[i + 1]["close"] < hourly.iloc[i + 1]["open"]:
                i += 1
                run.append(hourly.iloc[i])
            valley = min(run, key=lambda x: x["close"])
            interval = five_minute[
                (five_minute.index >= valley.name)
                & (five_minute.index < valley.name + pd.Timedelta(minutes=60))
            ]
            if not interval.empty:
                extreme = interval["close"].min()
                pivot_time = interval[interval["close"] == extreme].index[0]
                bottoms.append((pivot_time, interval.loc[pivot_time, "close"]))
                if i + 1 < len(hourly):
                    following = hourly.iloc[i + 1]
                    next_interval = five_minute[
                        (five_minute.index >= following.name)
                        & (five_minute.index < following.name + pd.Timedelta(minutes=60))
                    ]
                    if not next_interval.empty and next_interval["close"].min() < extreme:
                        new_extreme = next_interval["close"].min()
                        new_time = next_interval[next_interval["close"] == new_extreme].index[0]
                        bottoms[-1] = (new_time, next_interval.loc[new_time, "close"])
        i += 1

    output = []
    trend = None
    trend_start = None
    last_date = None
    for timestamp, row in rows.iterrows():
        down = up = top = bottom = 0
        if last_date != row["date"]:
            trend = None
            trend_start = None
            last_date = row["date"]
        if (timestamp, row["close"]) in tops:
            top = up = 1
            trend = "downtrend"
            trend_start = timestamp
        elif (timestamp, row["close"]) in bottoms:
            bottom = down = 1
            trend = "uptrend"
            trend_start = timestamp
        if trend == "uptrend" and trend_start is not None and timestamp > trend_start:
            up = 1
        elif trend == "downtrend" and trend_start is not None and timestamp > trend_start:
            down = 1
        output.append([row["date"], row["time"], down, up, top, bottom])

    # Preserve the source script's prefix retroactivity (one pass per ticker).
    for index, row in enumerate(output):
        if row[4] == 1:
            for prefix in range(index):
                output[prefix] = [output[prefix][0], output[prefix][1], 0, 1, 0, 0]
            break
        if row[5] == 1:
            for prefix in range(index):
                output[prefix] = [output[prefix][0], output[prefix][1], 1, 0, 0, 0]
            break
    return pd.DataFrame(output, columns=["date", "time", "down_gen", "up_gen", "top_gen", "bottom_gen"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prices", type=Path, default=Path(r"D:\database\Database_define.db"))
    parser.add_argument("--labels", type=Path, default=Path(r"D:\database\rotulos_price5.db"))
    parser.add_argument(
        "--article-csv",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data/raw/merged_output.csv",
    )
    args = parser.parse_args()

    with connect_read_only(args.prices) as source, connect_read_only(args.labels) as saved:
        ticker_ids = [row[0] for row in saved.execute("SELECT DISTINCT id_ticker FROM Rotule_price5 ORDER BY id_ticker")]
        total_match = total_common = 0
        saved_flags = ["downtrend", "uptrend", "top", "bottom"]
        generated_flags = ["down_gen", "up_gen", "top_gen", "bottom_gen"]
        for ticker_id in ticker_ids:
            price = pd.read_sql_query(
                "SELECT date,time,open,close,high,low,volume FROM price5 WHERE id_ticker=? ORDER BY date,time",
                source,
                params=(ticker_id,),
            )
            expected = pd.read_sql_query(
                "SELECT date,time,downtrend,uptrend,top,bottom FROM Rotule_price5 WHERE id_ticker=?",
                saved,
                params=(ticker_id,),
            )
            generated = recreate_for_ticker(price)
            common = expected.merge(generated, on=["date", "time"], how="inner", validate="one_to_one")
            equal = pd.Series(True, index=common.index)
            for saved_name, generated_name in zip(saved_flags, generated_flags):
                equal &= common[saved_name].astype(int).eq(common[generated_name].astype(int))
            total_match += int(equal.sum())
            total_common += len(common)
            print(
                f"ticker={ticker_id} price={len(price)} stored={len(expected)} "
                f"common={len(common)} exact={int(equal.sum())}/{len(common)}"
            )
        print(f"DATABASE TOTAL exact={total_match}/{total_common}")

        if args.article_csv.exists():
            article = pd.read_csv(args.article_csv, usecols=["datetime", "id_ticker", "trend"], parse_dates=["datetime"])
            article = article.sort_values(["id_ticker", "datetime"]).reset_index(drop=True)
            article["date"] = article["datetime"].dt.strftime("%Y-%m-%d")
            article["time"] = article["datetime"].dt.strftime("%H:%M:%S")
            article["session_last"] = article["datetime"].eq(
                article.groupby(["id_ticker", "date"])["datetime"].transform("max")
            )
            article["next_id"] = article.groupby("id_ticker")["id_ticker"].shift(-1)
            article["next_date"] = article.groupby("id_ticker")["date"].shift(-1)
            article["next_time"] = article.groupby("id_ticker")["time"].shift(-1)

            labels = pd.read_sql_query("SELECT id_ticker,date,time,uptrend FROM Rotule_price5", saved)
            current = labels.rename(columns={"uptrend": "current_uptrend"})
            joined = article.merge(current, on=["id_ticker", "date", "time"], how="left", validate="one_to_one")
            next_labels = labels.rename(
                columns={"id_ticker": "next_id", "date": "next_date", "time": "next_time", "uptrend": "next_uptrend"}
            )
            joined = joined.merge(next_labels, on=["next_id", "next_date", "next_time"], how="left")

            has_next = joined["next_uptrend"].notna()
            next_expected = joined.loc[has_next, "next_uptrend"].astype(int).map({1: "uptrend", 0: "downtrend"})
            next_match = joined.loc[has_next, "trend"].eq(next_expected)
            session_end = joined["session_last"]
            session_end_has_next = session_end & has_next
            session_end_next_match = joined.loc[session_end_has_next, "trend"].eq(
                joined.loc[session_end_has_next, "next_uptrend"].astype(int).map({1: "uptrend", 0: "downtrend"})
            )
            final_series = ~has_next
            final_same_row_match = joined.loc[final_series, "trend"].eq(
                joined.loc[final_series, "current_uptrend"].astype(int).map({1: "uptrend", 0: "downtrend"})
            )
            print(
                f"ARTICLE CSV rows={len(article)} next-same-ticker={int(next_match.sum())}/{len(next_match)}; "
                f"session-final rows with later same-ticker row={int(session_end_has_next.sum())}, "
                f"match={int(session_end_next_match.sum())}/{len(session_end_next_match)}; "
                f"final ticker rows={int(final_series.sum())}, "
                f"same-row raw-label agreement={int(final_same_row_match.sum())}/{len(final_same_row_match)}"
            )


if __name__ == "__main__":
    main()
