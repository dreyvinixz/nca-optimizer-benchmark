# CPU baseline cross-validation (development data only)

Four expanding folds on pre-test dates. The final test period was excluded by the Parquet reader and has no metrics in this report.

- Run time: 17.15 s; peak RSS: 482,008 KiB.
- Eligible pre-test rows: 87,448; feature rows with incomplete warm-up are excluded, no imputation is fitted.
- Input date cutoff: before `2026-05-26`. Scalers are inside the logistic regression Pipeline, fitted only on each fold's training rows.
- Hashes: contract `36d1603d84dc661bc9fcb353a281bd942519f8ab47ea7b880ff6bc915a494aa3`, protocol `8310b1249c717eececc8ffb1e31cc108bfedd2108537b31e5cddbe3c0d503111`, market `32cadf06387ae172edc804804fe762ef26f9f0928424ee83ce9e37a848389eab`, B4 `2d8c18c8d1a46be788ee2810a9caba043c2413102e4ee4f5c9927646037ce4c8`.
- Metrics are mean ± standard deviation across four chronological validation blocks. Folds have expanding, overlapping training periods, so this spread is descriptive, not an independent confidence interval.
- B0 labels are retrospective. These scores measure prediction of that label construction, not causal market-state accuracy or trading performance.
- Persistence of the previous B0 label is omitted: B4 does not store the confirmation time proving that label was available at the next minute.

## Pooled roots

| Target | Model | MCC | Balanced accuracy | Macro F1 | Mean validation rows | Mean fit + predict seconds |
|---|---|---:|---:|---:|---:|---:|
| majority | causal_5m_momentum | 0.441 ± 0.019 | 0.721 ± 0.009 | 0.720 ± 0.010 | 9,054 | 0.000 |
| majority | hist_gradient_boosting | 0.468 ± 0.030 | 0.734 ± 0.015 | 0.734 ± 0.015 | 9,054 | 0.175 |
| majority | logistic_regression | 0.466 ± 0.030 | 0.733 ± 0.015 | 0.732 ± 0.015 | 9,054 | 0.630 |
| majority | majority | 0.000 ± 0.000 | 0.500 ± 0.000 | 0.329 ± 0.014 | 9,054 | 0.001 |
| trend_10m | causal_5m_momentum | 0.424 ± 0.019 | 0.712 ± 0.009 | 0.712 ± 0.010 | 9,086 | 0.000 |
| trend_10m | hist_gradient_boosting | 0.448 ± 0.031 | 0.724 ± 0.015 | 0.724 ± 0.015 | 9,086 | 0.161 |
| trend_10m | logistic_regression | 0.444 ± 0.034 | 0.722 ± 0.017 | 0.721 ± 0.017 | 9,086 | 0.544 |
| trend_10m | majority | 0.000 ± 0.000 | 0.500 ± 0.000 | 0.328 ± 0.012 | 9,086 | 0.001 |
| trend_15m | causal_5m_momentum | 0.394 ± 0.016 | 0.697 ± 0.008 | 0.696 ± 0.008 | 9,061 | 0.000 |
| trend_15m | hist_gradient_boosting | 0.442 ± 0.023 | 0.721 ± 0.011 | 0.720 ± 0.011 | 9,061 | 0.178 |
| trend_15m | logistic_regression | 0.448 ± 0.030 | 0.724 ± 0.014 | 0.723 ± 0.015 | 9,061 | 0.768 |
| trend_15m | majority | 0.000 ± 0.000 | 0.500 ± 0.000 | 0.330 ± 0.021 | 9,061 | 0.001 |
| trend_5m | causal_5m_momentum | 0.444 ± 0.020 | 0.722 ± 0.010 | 0.722 ± 0.010 | 9,100 | 0.000 |
| trend_5m | hist_gradient_boosting | 0.488 ± 0.011 | 0.744 ± 0.005 | 0.744 ± 0.006 | 9,100 | 0.221 |
| trend_5m | logistic_regression | 0.487 ± 0.018 | 0.744 ± 0.009 | 0.743 ± 0.009 | 9,100 | 0.831 |
| trend_5m | majority | 0.000 ± 0.000 | 0.500 ± 0.000 | 0.328 ± 0.010 | 9,100 | 0.002 |

## Logistic regression by root

| Target | Root | MCC | Balanced accuracy | Macro F1 |
|---|---|---:|---:|---:|
| majority | IND | 0.471 ± 0.041 | 0.735 ± 0.020 | 0.735 ± 0.020 |
| majority | WIN | 0.464 ± 0.025 | 0.732 ± 0.012 | 0.731 ± 0.013 |
| trend_10m | IND | 0.447 ± 0.040 | 0.724 ± 0.020 | 0.723 ± 0.020 |
| trend_10m | WIN | 0.443 ± 0.032 | 0.722 ± 0.016 | 0.721 ± 0.017 |
| trend_15m | IND | 0.465 ± 0.030 | 0.732 ± 0.015 | 0.732 ± 0.015 |
| trend_15m | WIN | 0.442 ± 0.030 | 0.721 ± 0.014 | 0.719 ± 0.015 |
| trend_5m | IND | 0.480 ± 0.028 | 0.740 ± 0.014 | 0.739 ± 0.014 |
| trend_5m | WIN | 0.490 ± 0.015 | 0.745 ± 0.007 | 0.744 ± 0.008 |

Full fold, class prevalence, confusion matrices, and per-root outputs are in `baseline_cv_summary.csv`. No hyperparameter search was performed.
