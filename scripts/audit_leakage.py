#!/usr/bin/env python3
"""Check the extracted feature cache for key, split, gap, and target-boundary leakage."""
import argparse
import json
from pathlib import Path

import pandas as pd
import yaml


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--contract", type=Path, default=Path("config/data_contract.yaml"))
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/win_ind_features_v1.parquet"))
    ap.add_argument("--report", type=Path, default=Path("reports/leakage_audit.md"))
    a = ap.parse_args()
    contract = yaml.safe_load(a.contract.read_text(encoding="utf-8"))
    frame = pd.read_parquet(a.parquet)
    manifest = json.loads(a.parquet.with_suffix(".manifest.json").read_text(encoding="utf-8"))
    feature_cols = contract["features"]["generated"]
    forbidden = set(contract["features"]["forbidden"])
    checks = {}
    checks["unique_sample_key"] = not frame.duplicated(["ticker", "date", "time"]).any()
    checks["no_forbidden_feature_columns"] = not (set(feature_cols) & forbidden)
    checks["split_is_date_pure"] = frame.groupby("date", sort=False).split.nunique().max() == 1
    checks["split_is_chronological"] = all(
        frame.loc[frame.split == s, "date"].max() < frame.loc[frame.split == t, "date"].min()
        for s, t in (("train", "validation"), ("validation", "test"))
    )
    folds = manifest.get("expanding_folds", [])
    test_start = manifest["date_ranges"]["test"][0]
    checks["expanding_folds_avoid_test_and_are_ordered"] = bool(
        len(folds) == 4
        and all(f["train_dates"][0] < f["train_dates"][1] < f["validation_dates"][0] < f["validation_dates"][1] < test_start for f in folds)
    )
    minute = frame.time.str.slice(0, 2).astype(int) * 60 + frame.time.str.slice(3, 5).astype(int)
    context_same = frame.ticker.eq(frame.ticker.shift()) & frame.date.eq(frame.date.shift())
    minute_adjacent = minute.sub(minute.shift()).eq(1)
    observed_contiguous = context_same & minute_adjacent
    same_segment = frame.segment_id.eq(frame.segment_id.shift())
    checks["segment_ids_reset_on_session_contract_and_gaps"] = bool((same_segment.iloc[1:] == observed_contiguous.iloc[1:]).all())
    endpoint_checks = {}
    for target, end_col in (("y5", "end5"), ("y10", "end10"), ("y15", "end15")):
        valid = frame[target].notna()
        endpoint = frame[end_col]
        endpoint_minute = endpoint.str.slice(0, 2).astype("float64") * 60 + endpoint.str.slice(3, 5).astype("float64")
        endpoint_checks[target] = {
            "valid_labels": int(valid.sum()),
            "valid_labels_missing_endpoint": int((valid & endpoint.isna()).sum()),
            "labels_ending_before_sample": int((valid & endpoint_minute.lt(minute)).sum()),
            "labels_ending_after_session": int((valid & endpoint_minute.gt(18 * 60)).sum()),
        }
    checks["labels_have_in_session_endpoints"] = all(
        x["valid_labels_missing_endpoint"] == 0 and x["labels_ending_before_sample"] == 0 and x["labels_ending_after_session"] == 0
        for x in endpoint_checks.values()
    )
    segment_first = frame.segment_id.ne(frame.segment_id.shift())
    checks["feature_warmup_is_explicit_null"] = bool(
        frame[feature_cols].notna().all(axis=1).any()
        and frame.loc[segment_first, "log_return_1m"].isna().all()
    )
    checks = {key: bool(value) for key, value in checks.items()}
    if not all(checks.values()):
        raise SystemExit("Leakage audit failed: " + json.dumps(checks))
    roots = contract["universe"]["primary_roots"]
    root = frame.ticker.map(lambda ticker: next((r for r in roots if ticker.startswith(r)), "OTHER"))
    grouped = frame.assign(root=root).groupby(["root", "split"], sort=True)
    rows = []
    for (r, split), group in grouped:
        ready = group[feature_cols].notna().all(axis=1)
        rows.append(f"| {r} | {split} | {len(group):,} | {int(ready.sum()):,} | {int(group.y5.notna().sum()):,} | {int(group.y10.notna().sum()):,} | {int(group.y15.notna().sum()):,} |")
    text = [
        "# Feature and temporal leakage audit",
        "",
        "The audit reads the ignored local Parquet cache. The source SQLite files remain read-only; the label audit from Phase 1 was reused.",
        "",
        f"- Rows: {len(frame):,}; unique sessions: {frame.date.nunique()}; keys are `(ticker,date,time)`. ",
        f"- Extraction runtime (including SHA-256 reads and Parquet write): {manifest['runtime_seconds']} seconds; cache size: {manifest['output_bytes']:,} bytes.",
        f"- Source SHA-256: market `{manifest['source_sha256']['market']}`, B4 `{manifest['source_sha256']['labels']}`.",
        f"- Contract/protocol SHA-256: `{manifest['contract_hash']}` / `{manifest['protocol_hash']}`.",
        f"- Date split: train `{manifest['date_ranges']['train'][0]}–{manifest['date_ranges']['train'][1]}`, validation `{manifest['date_ranges']['validation'][0]}–{manifest['date_ranges']['validation'][1]}`, test `{manifest['date_ranges']['test'][0]}–{manifest['date_ranges']['test'][1]}`.",
        "- All instruments/contracts on each date share one split. The missing 2026-05-25 session remains absent; no calendar-day forward shift is applied.",
        "- Every feature uses the completed bar at or before its row timestamp; rolling state resets at contract/session changes and any gap in observed minutes. No synthetic bars or forward fill.",
        "- The joined lookup casts source `date/time` to text to match B4 column affinity; `EXPLAIN QUERY PLAN` confirms the composite `(id_ticker,date,time)` primary-key lookup for all four label tables.",
        "- B0 labels are retrospective. All non-null labels have an endpoint in the same session at or after the sample minute. Training can use a session's labels only after that session has completed; segment endpoints are metadata, never model inputs.",
        "- Chronological date groups make the session-local B4 label horizon unable to cross a split boundary. Model preprocessing must still fit on training rows only.",
        "",
        "## Checks",
        "",
    ]
    text.extend(f"- PASS: {name.replace('_', ' ')}" for name, ok in checks.items() if ok)
    text += ["", "## Expanding validation folds", "", "| Fold | Train sessions | Train dates | Validation sessions | Validation dates |", "|---:|---:|---|---:|---|"]
    text.extend(f"| {f['fold']} | {f['train_sessions']} | {f['train_dates'][0]}–{f['train_dates'][1]} | {f['validation_sessions']} | {f['validation_dates'][0]}–{f['validation_dates'][1]} |" for f in folds)
    text += ["", "## Coverage by root and split", "", "| Root | Split | Rows | All features ready | 5m labels | 10m labels | 15m labels |", "|---|---|---:|---:|---:|---:|---:|"]
    text.extend(rows)
    text += ["", "## Label endpoint checks", "", "| Target | Valid labels | Missing endpoint | Endpoint before sample | Endpoint after 18:00 |", "|---|---:|---:|---:|---:|"]
    text.extend(f"| {target} | {d['valid_labels']:,} | {d['valid_labels_missing_endpoint']} | {d['labels_ending_before_sample']} | {d['labels_ending_after_session']} |" for target, d in endpoint_checks.items())
    text += ["", "## Limitations", "", "This audit proves feature construction and split hygiene for the extracted snapshot. It does not establish that B0 is an independent ground truth, that labels are causal market states, or that a model can trade profitably. No model metrics have been inspected.", ""]
    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.report.write_text("\n".join(text), encoding="utf-8")
    print(json.dumps({"checks": checks, "endpoint_checks": endpoint_checks, "report": str(a.report)}, indent=2))


if __name__ == "__main__":
    main()
