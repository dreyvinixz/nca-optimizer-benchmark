# Deep overfitting assessment

## Verdict

The evidence shows a modest, consistent in-sample fit gap, so some overfitting is possible. It does not show a severe generalization collapse: frozen validation performance is maintained on the later final test, chronological development folds are reasonably stable, and no negative-MCC test session occurred for the three primary candidate models. This is evidence against severe overfitting in this sample, not proof that overfitting is absent.

The final test was not loaded by the train-versus-validation fitting diagnostic. This report reads its already-saved one-pass prediction artifact only to summarize the fixed test by session; it does not fit a model, select a model, or tune a threshold.

## Apparent training fit versus chronological validation

A separate CPU diagnostic reproduced the frozen model settings and seeds and fit each model once on the frozen training partition. Train metrics are in-sample and optimistically biased by construction. A positive MCC gap is train MCC minus validation MCC; positive Brier/log-loss degradation is validation minus train.

| Model | Target | Train MCC | Validation MCC | MCC gap | Train macro-F1 | Validation macro-F1 | Validation minus train Brier | Validation minus train log loss |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| hist_gradient_boosting | trend_10m | 0.478 | 0.441 | 0.037 | 0.739 | 0.720 | 0.010 | 0.025 |
| hist_gradient_boosting | trend_15m | 0.476 | 0.436 | 0.041 | 0.738 | 0.718 | 0.012 | 0.030 |
| hist_gradient_boosting | trend_5m | 0.513 | 0.487 | 0.026 | 0.756 | 0.743 | 0.007 | 0.017 |
| independent_mlp | trend_10m | 0.466 | 0.440 | 0.026 | 0.733 | 0.720 | 0.006 | 0.016 |
| independent_mlp | trend_15m | 0.461 | 0.427 | 0.035 | 0.728 | 0.707 | 0.012 | 0.030 |
| independent_mlp | trend_5m | 0.504 | 0.480 | 0.024 | 0.752 | 0.740 | 0.005 | 0.011 |
| logistic_regression | trend_10m | 0.462 | 0.437 | 0.025 | 0.731 | 0.718 | 0.008 | 0.019 |
| logistic_regression | trend_15m | 0.461 | 0.437 | 0.024 | 0.730 | 0.718 | 0.010 | 0.023 |
| logistic_regression | trend_5m | 0.501 | 0.481 | 0.019 | 0.750 | 0.740 | 0.007 | 0.015 |
| shared_multitask_mlp | trend_10m | 0.463 | 0.433 | 0.030 | 0.731 | 0.715 | 0.007 | 0.018 |
| shared_multitask_mlp | trend_15m | 0.459 | 0.428 | 0.031 | 0.728 | 0.711 | 0.010 | 0.024 |
| shared_multitask_mlp | trend_5m | 0.503 | 0.481 | 0.022 | 0.751 | 0.739 | 0.006 | 0.014 |

Across the nine MLP target/head comparisons, the apparent MCC gap is 0.022–0.035 and the macro-F1 gap is about 0.012–0.021. The CPU HistGradientBoosting gaps are 0.026–0.041 MCC. Logistic regression also has a smaller 0.019–0.025 MCC gap. All models score better on train than on later validation, which is expected; the size is noticeable but not a collapse.

## Chronological MLP cross-validation

Four expanding folds use successive validation periods. Their training windows overlap, so the standard deviation is descriptive rather than an independent confidence interval.

| Target | Fold mean MCC | Fold SD | Fold range |
|---|---:|---:|---:|
| majority | 0.464 | 0.027 | 0.439–0.500 |
| trend_10m | 0.447 | 0.031 | 0.421–0.489 |
| trend_15m | 0.442 | 0.024 | 0.417–0.471 |
| trend_5m | 0.487 | 0.012 | 0.475–0.505 |

## Frozen validation versus one-pass final test

The validation/test MCC change is test minus validation. A negative value would indicate deterioration on the later test period.

| Model | Target | Validation MCC | Test MCC | Change | Validation Brier | Test Brier |
|---|---|---:|---:|---:|---:|---:|
| independent_mlp | trend_5m | 0.480 | 0.492 | +0.012 | 0.165 | 0.164 |
| independent_mlp | trend_10m | 0.440 | 0.442 | +0.003 | 0.180 | 0.180 |
| independent_mlp | trend_15m | 0.426 | 0.429 | +0.003 | 0.189 | 0.187 |
| shared_multitask_mlp | trend_5m | 0.481 | 0.487 | +0.007 | 0.168 | 0.166 |
| shared_multitask_mlp | trend_10m | 0.433 | 0.439 | +0.006 | 0.182 | 0.181 |
| shared_multitask_mlp | trend_15m | 0.428 | 0.429 | +0.001 | 0.187 | 0.187 |
| hist_gradient_boosting | trend_5m | 0.487 | 0.490 | +0.003 | 0.164 | 0.163 |
| hist_gradient_boosting | trend_10m | 0.441 | 0.451 | +0.011 | 0.179 | 0.178 |
| hist_gradient_boosting | trend_15m | 0.436 | 0.445 | +0.009 | 0.183 | 0.181 |

All nine validation-to-test MCC changes are nonnegative (range +0.001 to +0.012). The later sample therefore does not display the usual test-period performance drop associated with severe overfitting. This comparison uses the original frozen GPU-run validation and test predictions; small numerical differences from the separate CPU diagnostic above are expected. Because this is one time split, it cannot prove performance on future market periods.

## Test stability across independent sessions

Daily MCC uses each pregão as one unit. Every one of the 25 final-test sessions contains both classes for these summaries; sessions are temporally dependent and are not treated as 25 independent draws here.

| Model | Target | Sessions | Mean daily MCC | SD | 10th–90th percentile | Negative-MCC sessions |
|---|---|---:|---:|---:|---:|---:|
| hist_gradient_boosting | trend_10m | 25 | 0.447 | 0.062 | 0.370–0.546 | 0 |
| hist_gradient_boosting | trend_15m | 25 | 0.436 | 0.062 | 0.345–0.495 | 0 |
| hist_gradient_boosting | trend_5m | 25 | 0.488 | 0.042 | 0.442–0.540 | 0 |
| independent_mlp | trend_10m | 25 | 0.438 | 0.059 | 0.369–0.522 | 0 |
| independent_mlp | trend_15m | 25 | 0.422 | 0.061 | 0.350–0.477 | 0 |
| independent_mlp | trend_5m | 25 | 0.490 | 0.049 | 0.433–0.547 | 0 |
| shared_multitask_mlp | trend_10m | 25 | 0.435 | 0.060 | 0.353–0.508 | 0 |
| shared_multitask_mlp | trend_15m | 25 | 0.422 | 0.062 | 0.336–0.474 | 0 |
| shared_multitask_mlp | trend_5m | 25 | 0.486 | 0.046 | 0.442–0.531 | 0 |

## Regime, root, and contract checks

Across the three fixed test blocks, MCC is fairly stable for 5m and 10m. For 15m, all displayed models improve in block 3 relative to blocks 1–2, consistent with time variation rather than a test collapse. By root, WIN and IND scores are broadly similar. Contract rows show lower counts for WINV26 (n=149); conclusions for that contract are especially uncertain and should not be read as evidence of model fit or failure. Full contract scores are in [`final_test_contract_metrics.csv`](final_test_contract_metrics.csv).

The leakage audit passed checks for date-pure splits, ordered expanding folds, completed-candle features, reset state at gaps/contracts/sessions, and in-session label endpoints. This lowers the risk of implementation leakage. It does not make B0 labels causal: B0 is retrospective, and the reported task is reproducing those labels.

## Conclusion and limits

Assessment: **some overfitting is possible, with a modest apparent train–validation gap; no evidence of severe overfitting or a validation-to-test collapse was found in this snapshot.** The strongest warning is the 15m train–validation gap (up to 0.041 MCC for HistGradientBoosting and 0.035 for independent MLP), while test scores remain close to or above validation. Small, single-period data and only 25 test sessions limit certainty.

No model settings, decision threshold, or model choice were changed from this diagnostic, and no model was fit on test data. Test-session summaries are descriptive only; no new test-based model comparison or threshold selection was performed. A stronger prospective claim requires a later untouched date range or a new rolling-origin study; do not turn these findings into a claim of profitability or true market-state prediction.

Artifacts: [`overfitting_train_validation.csv`](overfitting_train_validation.csv), [`overfitting_session_metrics.csv`](overfitting_session_metrics.csv), [`mlp_cv_summary.csv`](mlp_cv_summary.csv), [`final_test_metrics.csv`](final_test_metrics.csv), [`final_test_contract_metrics.csv`](final_test_contract_metrics.csv), and [`leakage_audit.md`](leakage_audit.md).
