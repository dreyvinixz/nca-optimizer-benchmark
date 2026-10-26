# Feature and temporal leakage audit

The audit reads the ignored local Parquet cache. The source SQLite files remain read-only; the label audit from Phase 1 was reused.

- Rows: 182,266; unique sessions: 119; keys are `(ticker,date,time)`.
- Extraction runtime (including SHA-256 reads and Parquet write): 11.93 seconds; cache size: 12,619,028 bytes.
- Source SHA-256: market `32cadf06387ae172edc804804fe762ef26f9f0928424ee83ce9e37a848389eab`, B4 `2d8c18c8d1a46be788ee2810a9caba043c2413102e4ee4f5c9927646037ce4c8`.
- Contract/protocol SHA-256: `36d1603d84dc661bc9fcb353a281bd942519f8ab47ea7b880ff6bc915a494aa3` / `8310b1249c717eececc8ffb1e31cc108bfedd2108537b31e5cddbe3c0d503111`.
- Date split: train `2026-01-02–2026-04-15`, validation `2026-04-16–2026-05-22`, test `2026-05-26–2026-06-30`.
- All instruments/contracts on each date share one split. The missing 2026-05-25 session remains absent; no calendar-day forward shift is applied.
- Every feature uses the completed bar at or before its row timestamp; rolling state resets at contract/session changes and any gap in observed minutes. No synthetic bars or forward fill.
- The joined lookup casts source `date/time` to text to match B4 column affinity; `EXPLAIN QUERY PLAN` confirms the composite `(id_ticker,date,time)` primary-key lookup for all four label tables.
- B0 labels are retrospective. All non-null labels have an endpoint in the same session at or after the sample minute. Training can use a session's labels only after that session has completed; segment endpoints are metadata, never model inputs.
- Chronological date groups make the session-local B4 label horizon unable to cross a split boundary. Model preprocessing must still fit on training rows only.

## Checks

- PASS: unique sample key
- PASS: no forbidden feature columns
- PASS: split is date pure
- PASS: split is chronological
- PASS: expanding folds avoid test and are ordered
- PASS: segment ids reset on session contract and gaps
- PASS: labels have in session endpoints
- PASS: feature warmup is explicit null

## Expanding validation folds

| Fold | Train sessions | Train dates | Validation sessions | Validation dates |
|---:|---:|---|---:|---|
| 1 | 47 | 2026-01-02–2026-03-11 | 10 | 2026-03-12–2026-03-25 |
| 2 | 57 | 2026-01-02–2026-03-25 | 10 | 2026-03-26–2026-04-09 |
| 3 | 67 | 2026-01-02–2026-04-09 | 10 | 2026-04-10–2026-04-24 |
| 4 | 77 | 2026-01-02–2026-04-24 | 10 | 2026-04-27–2026-05-11 |

## Coverage by root and split

| Root | Split | Rows | All features ready | 5m labels | 10m labels | 15m labels |
|---|---|---:|---:|---:|---:|---:|
| IND | test | 12,588 | 4,185 | 12,494 | 12,461 | 12,422 |
| IND | train | 38,781 | 24,298 | 38,608 | 38,464 | 38,458 |
| IND | validation | 11,024 | 4,584 | 10,971 | 10,938 | 10,894 |
| WIN | test | 25,136 | 16,303 | 24,906 | 24,842 | 24,862 |
| WIN | train | 72,315 | 46,075 | 71,783 | 71,666 | 71,590 |
| WIN | validation | 22,422 | 12,491 | 22,222 | 22,206 | 22,155 |

## Label endpoint checks

| Target | Valid labels | Missing endpoint | Endpoint before sample | Endpoint after 18:00 |
|---|---:|---:|---:|---:|
| y5 | 180,984 | 0 | 0 | 0 |
| y10 | 180,577 | 0 | 0 | 0 |
| y15 | 180,381 | 0 | 0 | 0 |

## Limitations

This audit proves feature construction and split hygiene for the extracted snapshot. It does not establish that B0 is an independent ground truth, that labels are causal market states, or that a model can trade profitably. No model metrics have been inspected.
