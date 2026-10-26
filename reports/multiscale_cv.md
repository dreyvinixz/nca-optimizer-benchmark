# Multi-scale model comparison (pre-test folds)

Four expanding validation folds; the final test period was excluded. Full fold/root metrics are in `multiscale_cv_summary.csv`; the row-level prediction cache is local in ignored `tmp/`.

- Device `/GPU:0`, runtime 203.13 s, peak RSS 2,251,012 KiB, temporary prediction cache 1,676,438 bytes.
- Independent and shared models use identical folds and the common three-label intersection for paired headline scores. Fold mean ± SD is descriptive because expanding training windows overlap.
- Selective acceptance requires unanimous predictions from the model's three heads; coverage is listed with performance. The rule uses model predictions, not future target values.
- Reference unanimous/discordant target strata are descriptive and unavailable at prediction time; do not use them as an operational filter.
- `mean_score` remains a deterministic vote fraction. Its regression errors do not make it a calibrated or independently validated probability.
- Labels remain retrospective B0 references; results do not establish causal market-state accuracy or trading performance. No test metrics were opened.

## Paired independent vs shared-head scores

| Architecture | Target | Sample | MCC | Balanced accuracy | Macro F1 | Coverage |
|---|---|---|---:|---:|---:|---:|
| independent | trend_10m | common_intersection | 0.446 ± 0.028 | 0.723 ± 0.014 | 0.722 ± 0.014 | 1.000 |
| independent | trend_10m | selective_unanimous_predictions | 0.534 ± 0.033 | 0.767 ± 0.017 | 0.767 ± 0.017 | 0.800 |
| independent | trend_15m | common_intersection | 0.442 ± 0.034 | 0.721 ± 0.016 | 0.719 ± 0.018 | 1.000 |
| independent | trend_15m | selective_unanimous_predictions | 0.517 ± 0.022 | 0.759 ± 0.010 | 0.758 ± 0.011 | 0.800 |
| independent | trend_5m | common_intersection | 0.489 ± 0.013 | 0.745 ± 0.006 | 0.744 ± 0.006 | 1.000 |
| independent | trend_5m | selective_unanimous_predictions | 0.556 ± 0.028 | 0.778 ± 0.014 | 0.778 ± 0.014 | 0.800 |
| shared_multitask | trend_10m | common_intersection | 0.446 ± 0.031 | 0.723 ± 0.015 | 0.723 ± 0.015 | 1.000 |
| shared_multitask | trend_10m | selective_unanimous_predictions | 0.525 ± 0.038 | 0.762 ± 0.019 | 0.762 ± 0.019 | 0.820 |
| shared_multitask | trend_15m | common_intersection | 0.443 ± 0.029 | 0.722 ± 0.014 | 0.721 ± 0.014 | 1.000 |
| shared_multitask | trend_15m | selective_unanimous_predictions | 0.508 ± 0.029 | 0.754 ± 0.014 | 0.753 ± 0.014 | 0.820 |
| shared_multitask | trend_5m | common_intersection | 0.488 ± 0.015 | 0.744 ± 0.007 | 0.744 ± 0.007 | 1.000 |
| shared_multitask | trend_5m | selective_unanimous_predictions | 0.547 ± 0.032 | 0.773 ± 0.016 | 0.773 ± 0.016 | 0.820 |

## Hard majority and soft-score models

- Majority MLP on the common intersection: MCC 0.466 ± 0.030, balanced accuracy 0.733 ± 0.015, macro-F1 0.733 ± 0.015.
- Mean-score regression on the common intersection: MAE 0.290 ± 0.007, MSE 0.126 ± 0.004; the training-mean constant baseline gives MAE 0.421 ± 0.004, MSE 0.198 ± 0.003.

## Independent and shared scores by root

| Architecture | Target | Root | MCC | Balanced accuracy | Coverage |
|---|---|---|---:|---:|---:|
| independent | trend_10m | IND | 0.447 ± 0.038 | 0.723 ± 0.019 | 1.000 |
| independent | trend_10m | WIN | 0.447 ± 0.025 | 0.723 ± 0.013 | 1.000 |
| independent | trend_15m | IND | 0.456 ± 0.029 | 0.728 ± 0.014 | 1.000 |
| independent | trend_15m | WIN | 0.437 ± 0.035 | 0.719 ± 0.016 | 1.000 |
| independent | trend_5m | IND | 0.478 ± 0.023 | 0.739 ± 0.011 | 1.000 |
| independent | trend_5m | WIN | 0.493 ± 0.010 | 0.747 ± 0.005 | 1.000 |
| shared_multitask | trend_10m | IND | 0.449 ± 0.039 | 0.724 ± 0.020 | 1.000 |
| shared_multitask | trend_10m | WIN | 0.446 ± 0.028 | 0.723 ± 0.014 | 1.000 |
| shared_multitask | trend_15m | IND | 0.454 ± 0.032 | 0.727 ± 0.016 | 1.000 |
| shared_multitask | trend_15m | WIN | 0.439 ± 0.028 | 0.720 ± 0.013 | 1.000 |
| shared_multitask | trend_5m | IND | 0.476 ± 0.025 | 0.738 ± 0.012 | 1.000 |
| shared_multitask | trend_5m | WIN | 0.494 ± 0.011 | 0.747 ± 0.006 | 1.000 |

## Provenance

- Contract/protocol SHA-256: `36d1603d84dc661bc9fcb353a281bd942519f8ab47ea7b880ff6bc915a494aa3` / `8310b1249c717eececc8ffb1e31cc108bfedd2108537b31e5cddbe3c0d503111`.
- Market/B4 SHA-256: `32cadf06387ae172edc804804fe762ef26f9f0928424ee83ce9e37a848389eab` / `2d8c18c8d1a46be788ee2810a9caba043c2413102e4ee4f5c9927646037ce4c8`.
- The previous-label persistence model remains omitted because B4 has no confirmation timestamp proving that a prior label was observable.
