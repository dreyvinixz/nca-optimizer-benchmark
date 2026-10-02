"""Read-only audit of future-label dependencies at temporal split boundaries.

Uses the saved article CSV, experiment configuration, price database, and the
read-only historical label reproducer. Reports (i) next-target rows that cross
the train/validation cutoff, and (ii) whether labels before each cutoff change
when the exact pivot-label routine is run only on price data available by that
cutoff. No files or databases are modified.
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

import pandas as pd
import yaml

from audit_reproduce_historical_labels_readonly import recreate_for_ticker


def ro_connect(path: Path) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=root / "data/raw/merged_output.csv")
    parser.add_argument("--config", type=Path, default=root / "config/experiment_config.yaml")
    parser.add_argument("--prices", type=Path, default=Path(r"D:\database\Database_define.db"))
    parser.add_argument("--labels", type=Path, default=Path(r"D:\database\rotulos_price5.db"))
    args = parser.parse_args()

    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    data_cfg, split_cfg = cfg["data"], cfg["split"]
    frame = pd.read_csv(args.dataset, parse_dates=[data_cfg["datetime_column"]])
    target = data_cfg["target_column"]
    datetime_column = data_cfg["datetime_column"]
    frame = frame[frame[target].isin(data_cfg["label_mapping"])].copy()
    frame[target] = frame[target].map(data_cfg["label_mapping"]).astype(int)

    feature_columns = [
        col for col in frame.select_dtypes(include=["number"]).columns
        if col not in {datetime_column, target, "id_ticker"}
    ]
    selected = [feature_columns[index] for index in data_cfg["selected_feature_indices"]]
    frame = frame.dropna(subset=selected + [target, datetime_column])
    frame = frame.sort_values(datetime_column).reset_index(drop=True)
    frame["date"] = frame[datetime_column].dt.strftime("%Y-%m-%d")
    frame["time"] = frame[datetime_column].dt.strftime("%H:%M:%S")
    frame["next_id"] = frame.groupby("id_ticker")["id_ticker"].shift(-1)
    frame["next_date"] = frame.groupby("id_ticker")["date"].shift(-1)
    frame["next_time"] = frame.groupby("id_ticker")["time"].shift(-1)

    n_rows = len(frame)
    train_end = int(n_rows * float(split_cfg["train_size"]))
    val_end = train_end + int(n_rows * float(split_cfg["validation_size"]))
    boundaries = {
        "train": (frame.iloc[train_end - 1][datetime_column], frame.iloc[:train_end]),
        "validation": (frame.iloc[val_end - 1][datetime_column], frame.iloc[train_end:val_end]),
    }
    print(f"prepared rows={n_rows}; train/validation/test={train_end}/{val_end-train_end}/{n_rows-val_end}")

    with ro_connect(args.prices) as source, ro_connect(args.labels) as saved:
        source_by_id: dict[int, pd.DataFrame] = {}
        full_by_id: dict[int, dict[str, int]] = {}
        for ticker_id in sorted(frame["id_ticker"].unique()):
            ticker_id = int(ticker_id)
            prices = pd.read_sql_query(
                "SELECT date,time,open,close,high,low,volume FROM price5 WHERE id_ticker=? ORDER BY date,time",
                source,
                params=(ticker_id,),
            )
            source_by_id[ticker_id] = prices
            labels = pd.read_sql_query(
                "SELECT date,time,uptrend FROM Rotule_price5 WHERE id_ticker=?",
                saved,
                params=(ticker_id,),
            )
            labels["key"] = labels["date"].astype(str) + " " + labels["time"].astype(str)
            full_by_id[ticker_id] = dict(zip(labels["key"], labels["uptrend"].astype(int)))

        for split_name, (cutoff, rows) in boundaries.items():
            successor_date = pd.to_datetime(rows["next_date"] + " " + rows["next_time"])
            same_ticker_successor = rows["next_id"].eq(rows["id_ticker"])
            crosses = rows[same_ticker_successor & successor_date.gt(cutoff)]
            terminal = rows[~same_ticker_successor]

            truncated_by_id: dict[int, dict[str, int]] = {}
            cutoff_key = cutoff.strftime("%Y-%m-%d %H:%M:%S")
            for ticker_id, prices in source_by_id.items():
                keys = prices["date"].astype(str) + " " + prices["time"].astype(str)
                truncated_prices = prices[keys <= cutoff_key]
                generated = recreate_for_ticker(truncated_prices)
                generated["key"] = generated["date"].astype(str) + " " + generated["time"].astype(str)
                truncated_by_id[ticker_id] = dict(zip(generated["key"], generated["up_gen"].astype(int)))

            stable_checked = 0
            changed: list[tuple[int, str, int, int]] = []
            unavailable: list[tuple[int, str]] = []
            eligible = rows[same_ticker_successor & successor_date.le(cutoff)]
            for row in eligible.itertuples(index=False):
                ticker_id = int(row.id_ticker)
                key = row.next_date + " " + row.next_time
                full = full_by_id[ticker_id].get(key)
                truncated = truncated_by_id[ticker_id].get(key)
                if full is None or truncated is None:
                    unavailable.append((ticker_id, key))
                    continue
                stable_checked += 1
                if int(full) != int(truncated):
                    changed.append((ticker_id, key, int(full), int(truncated)))

            print(
                f"{split_name}: cutoff={cutoff}; rows={len(rows)}; "
                f"next-targets crossing cutoff={len(crosses)}; terminal rows without same-ticker successor={len(terminal)}; "
                f"pre-cut labels checked against cutoff-only reproduction={stable_checked}; "
                f"changed={len(changed)}; unavailable={len(unavailable)}"
            )
            if len(crosses):
                print(
                    "  crossing examples:",
                    rows.loc[crosses.index, ["id_ticker", datetime_column, "next_date", "next_time"]]
                    .to_dict("records"),
                )
            if changed:
                print("  changed label examples:", changed[:10])
            if unavailable:
                print("  unavailable label examples:", unavailable[:10])

    # The four final per-ticker rows have no target successor in the dataset.
    endings = frame.groupby("id_ticker", sort=False).tail(1)
    print("final per-ticker observations:")
    print(endings[["id_ticker", datetime_column, target]].to_string(index=False))


if __name__ == "__main__":
    main()
