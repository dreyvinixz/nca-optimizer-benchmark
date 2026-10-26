#!/usr/bin/env python3
"""Audit v2 feature cache keys, target alignment, and leakage-prone columns."""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parquet", type=Path, default=Path("data/derived/intraday_direction_v2_features.parquet"))
    ap.add_argument("--report", type=Path, default=Path("reports/intraday_direction_v2_data_audit.md"))
    a = ap.parse_args()
    manifest_path = a.parquet.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    frame = pd.read_parquet(a.parquet)
    features = manifest["feature_columns"]
    keys = ["ticker", "date", "time"]
    if frame.duplicated(keys).any():
        raise ValueError("Duplicate (ticker,date,time) records")
    forbidden = [c for c in features if any(tag in c.lower() for tag in (
        "target", "forward", "trend", "b4", "endpoint", "future", "segment_end",
    ))]
    if forbidden:
        raise ValueError(f"Leakage-prone columns in features: {forbidden}")
    feature_matrix = frame[features].to_numpy(dtype=np.float32)
    finite_by_row = np.isfinite(feature_matrix).all(axis=1)
    if int(finite_by_row.sum()) != int(manifest["feature_rows_complete"]):
        raise ValueError("Manifest complete-feature row count does not match Parquet")
    if not np.isfinite(feature_matrix[finite_by_row]).all():
        raise ValueError("Non-finite value in a supposedly complete feature row")

    frame["_minute"] = frame.time.str.slice(0, 2).astype(int) * 60 + frame.time.str.slice(3, 5).astype(int)
    grouped = frame.groupby(["ticker", "date"], sort=False)
    checks = []
    for horizon in (5, 15, 30):
        target_col = f"target_up_{horizon}m"
        return_col = f"forward_log_return_{horizon}m"
        future_close = grouped.close.shift(-horizon)
        future_minute = grouped["_minute"].shift(-horizon)
        future_segment = grouped.segment_id.shift(-horizon)
        expected_valid = future_minute.sub(frame._minute).eq(horizon) & future_segment.eq(frame.segment_id)
        expected_return = np.log(future_close.where(future_close > 0)) - np.log(frame.close.where(frame.close > 0))
        expected_valid &= expected_return.notna()
        observed_valid = frame[target_col].notna()
        if not observed_valid.equals(expected_valid):
            mismatch_count = int((observed_valid != expected_valid).sum())
            raise ValueError(f"{h}-bar target coverage/alignment differs on {mismatch_count} rows")
        if observed_valid.any():
            actual_return = frame.loc[observed_valid, return_col].to_numpy(dtype=float)
            expected = expected_return.loc[observed_valid].to_numpy(dtype=float)
            if not np.allclose(actual_return, expected, rtol=1e-8, atol=1e-12):
                raise ValueError(f"{h}-bar forward returns do not match the within-session shift")
            expected_target = (expected > 0).astype(float)
            actual_target = frame.loc[observed_valid, target_col].to_numpy(dtype=float)
            if not np.array_equal(actual_target, expected_target):
                raise ValueError(f"{h}-bar binary labels do not match the declared sign rule")
        if not bool(frame.loc[observed_valid, target_col].isin([0.0, 1.0]).all()):
            raise ValueError(f"{h}-bar target includes values outside {{0,1}}")
        summary = manifest["target_summary"][str(horizon)]
        if int(observed_valid.sum()) != int(summary["valid"]):
            raise ValueError(f"{h}-bar valid count differs from manifest")
        checks.append({"horizon": horizon, "valid_rows": int(observed_valid.sum()),
                       "up_prevalence": float(frame.loc[observed_valid, target_col].mean()),
                       "band_rows": {band: int((frame.time_band.eq(band) & observed_valid).sum())
                                     for band in ("early", "middle", "late")}})

    roots = {root: int(frame.ticker.str.startswith(root).sum()) for root in ("WIN", "IND")}
    report = [
        "# Auditoria do cache direcional intradiário v2", "",
        "**Resultado: aprovada.** Chaves, features completas e alvos foram comparados com deslocamentos dentro do mesmo ticker e pregão.", "",
        f"- Linhas: {len(frame):,}; pregões: {frame.date.nunique()}; features candidatas: {len(features)}.",
        f"- Linhas completas após aquecimento integral: {int(finite_by_row.sum()):,} ({finite_by_row.mean():.1%}).",
        f"- WIN: {roots['WIN']:,}; IND: {roots['IND']:,}.",
        f"- Janela observada: {frame.time.min()}–{frame.time.max()}.",
        "- Chave única `(ticker,date,time)`; nenhum nome de coluna de B4/rótulo/endpoint/futuro nas features.",
        "- Em todos os horizontes, o deslocamento corresponde exatamente a h minutos consecutivos observados e não cruza ticker, data ou segmento.", "",
        "| Horizonte | Alvos válidos | Prevalência de alta | Linhas early | Linhas middle | Linhas late |", "|---:|---:|---:|---:|---:|---:|",
    ]
    for c in checks:
        report.append(f"| {c['horizon']}m | {c['valid_rows']:,} | {c['up_prevalence']:.4f} | {c['band_rows']['early']:,} | {c['band_rows']['middle']:,} | {c['band_rows']['late']:,} |")
    report += ["", f"SHA-256 da origem SQLite: `{manifest['source_sha256']}`.",
               "O período inteiro permanece desenvolvimento; esta auditoria não abre nem valida um teste futuro independente.", ""]
    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.report.write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main()
