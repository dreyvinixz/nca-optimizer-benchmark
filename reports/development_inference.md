# Development generalization and paired inference

Exploratory analysis of the 40 out-of-fold validation sessions only. The final test dates are absent. The daily session is the inference unit; candle counts are never used as independent sample size.

The primary paired contrast is independent MLP minus shared multi-task MLP on per-session MCC, restricted to the common three-target intersection. Two-sided Wilcoxon signed-rank p-values are Holm-adjusted across the three targets. Confidence intervals use a 5-session circular moving-block bootstrap (10,000 replicates). These CV comparisons remain developmental and do not replace the fixed final test.

| Target | Sessions | Both classes present | Mean MCC diff | 95% block-bootstrap CI | Wilcoxon p | Holm p | Independent/shared Brier | Independent/shared log loss |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| trend_5m | 40 | 40 | 0.0002 | [-0.0071, 0.0069] | 0.5101 | 1 | 0.1644 / 0.1654 | 0.4891 / 0.4925 |
| trend_10m | 40 | 40 | -0.0005 | [-0.0038, 0.0029] | 0.9893 | 1 | 0.1786 / 0.1783 | 0.5271 / 0.5268 |
| trend_15m | 40 | 40 | -0.0031 | [-0.0096, 0.0031] | 0.3934 | 1 | 0.1821 / 0.1815 | 0.5382 / 0.5367 |

## Root summary

| Root | Target | Sessions | Independent mean BAcc | Shared mean BAcc |
|---|---|---:|---:|---:|
| IND | trend_10m | 40 | 0.7087 | 0.7146 |
| IND | trend_15m | 40 | 0.7208 | 0.7143 |
| IND | trend_5m | 40 | 0.7404 | 0.7323 |
| WIN | trend_10m | 40 | 0.7204 | 0.7210 |
| WIN | trend_15m | 40 | 0.7185 | 0.7202 |
| WIN | trend_5m | 40 | 0.7465 | 0.7466 |

Brier and log loss describe probability forecasts of reproducing the retrospective B0 labels. Calibration against these labels is not independent truth. The report is not a profitability analysis.
