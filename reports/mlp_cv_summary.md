# Compact MLP cross-validation (development data only)

Four expanding folds; Parquet read filters out all test dates. Scaler fit only on each fold's training rows.

- Device: `/GPU:0`; visible GPU(s): /physical_device:GPU:0; total runtime 131.57 s; peak RSS 1,933,892 KiB.
- Architecture 11–32–16–1, dropout 0.10, batch 256, five epochs, no row shuffle. Mean epoch time 1.3651 s.
- Metrics are mean ± standard deviation across folds; this is descriptive because expanding training folds overlap.
- B0 target labels remain retrospective; these validation scores do not establish causal state accuracy or trading performance.

| Target | MCC | Balanced accuracy | Macro F1 |
|---|---:|---:|---:|
| majority | 0.464 ± 0.027 | 0.732 ± 0.013 | 0.732 ± 0.013 |
| trend_10m | 0.447 ± 0.031 | 0.723 ± 0.016 | 0.722 ± 0.017 |
| trend_15m | 0.442 ± 0.024 | 0.721 ± 0.011 | 0.719 ± 0.012 |
| trend_5m | 0.487 ± 0.012 | 0.744 ± 0.006 | 0.743 ± 0.006 |
