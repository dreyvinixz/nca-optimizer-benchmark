# Final test evaluation

Pre-registered models were fit on the fixed training dates. Validation and final test were scored once; no hyperparameters were changed after opening the test.

- Final test sessions: 25 (2026-05-26–2026-06-30); rows with complete features: 20,488.
- Device: /GPU:0; runtime 686.08 s; peak RSS 1,796,448 KiB.
- The complete table contains pooled test metrics and all three pre-fixed test blocks by model, target, and root.
- Main contrast uses the common sample with all three targets observed. Bootstrap resamples five-session blocks; test p-values are not reported.
- Probability scores estimate reproduction of retrospective B0 labels only. They are not independently validated market probabilities; there is no profitability claim.

## Primary paired contrast: pooled MCC and session-block bootstrap

| Target | Common n | Independent MCC | Shared MCC | Observed difference | Bootstrap 95% CI |
|---|---:|---:|---:|---:|---|
| trend_5m | 20332 | 0.4934 | 0.4882 | 0.0052 | [-0.0002, 0.0102] |
| trend_10m | 20332 | 0.4436 | 0.4403 | 0.0033 | [-0.0057, 0.0121] |
| trend_15m | 20332 | 0.4306 | 0.4306 | -0.0000 | [-0.0052, 0.0051] |

The confidence intervals include zero for all three paired differences. Independent and shared MLPs therefore show no clear separation on this test sample.

## Pooled test metrics (both roots)

| Model | Target | n | MCC | Balanced accuracy | Macro F1 | Brier | Log loss | MAE | MSE |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| majority_constant | majority | 20332 | 0.0000 | 0.5000 | 0.3263 | 0.5157 | 8.3127 | — | — |
| majority_mlp | majority | 20332 | 0.4624 | 0.7311 | 0.7302 | 0.1741 | 0.5173 | — | — |
| soft_score_mlp | mean_score | 20332 | — | — | — | — | — | 0.2837 | 0.1210 |
| soft_score_training_mean | mean_score | 20332 | — | — | — | — | — | 0.4119 | 0.1918 |
| causal_5m_momentum | trend_10m | 20395 | 0.4323 | 0.7163 | 0.7160 | — | — | — | — |
| hist_gradient_boosting | trend_10m | 20395 | 0.4513 | 0.7258 | 0.7252 | 0.1781 | 0.5270 | — | — |
| independent_mlp | trend_10m | 20395 | 0.4423 | 0.7212 | 0.7206 | 0.1795 | 0.5312 | — | — |
| logistic_regression | trend_10m | 20395 | 0.4426 | 0.7214 | 0.7206 | 0.1867 | 0.5562 | — | — |
| majority_constant | trend_10m | 20395 | 0.0000 | 0.5000 | 0.3254 | 0.5177 | 8.3439 | — | — |
| shared_multitask_mlp | trend_10m | 20395 | 0.4389 | 0.7192 | 0.7178 | 0.1811 | 0.5344 | — | — |
| causal_5m_momentum | trend_15m | 20397 | 0.3799 | 0.6902 | 0.6896 | — | — | — | — |
| hist_gradient_boosting | trend_15m | 20397 | 0.4448 | 0.7226 | 0.7217 | 0.1806 | 0.5349 | — | — |
| independent_mlp | trend_15m | 20397 | 0.4293 | 0.7132 | 0.7091 | 0.1874 | 0.5511 | — | — |
| logistic_regression | trend_15m | 20397 | 0.4340 | 0.7172 | 0.7160 | 0.1897 | 0.5651 | — | — |
| majority_constant | trend_15m | 20397 | 0.0000 | 0.5000 | 0.3223 | 0.5244 | 8.4530 | — | — |
| shared_multitask_mlp | trend_15m | 20397 | 0.4294 | 0.7140 | 0.7111 | 0.1867 | 0.5496 | — | — |
| causal_5m_momentum | trend_5m | 20444 | 0.4565 | 0.7283 | 0.7281 | — | — | — | — |
| hist_gradient_boosting | trend_5m | 20444 | 0.4896 | 0.7449 | 0.7444 | 0.1626 | 0.4861 | — | — |
| independent_mlp | trend_5m | 20444 | 0.4925 | 0.7463 | 0.7459 | 0.1636 | 0.4872 | — | — |
| logistic_regression | trend_5m | 20444 | 0.4891 | 0.7445 | 0.7438 | 0.1733 | 0.5194 | — | — |
| majority_constant | trend_5m | 20444 | 0.0000 | 0.5000 | 0.3267 | 0.5147 | 8.2964 | — | — |
| shared_multitask_mlp | trend_5m | 20444 | 0.4873 | 0.7434 | 0.7425 | 0.1659 | 0.4935 | — | — |

## Primary models by root

| Target | Root | Model | n | MCC | Balanced accuracy | Macro F1 |
|---|---|---|---:|---:|---:|---:|
| trend_10m | IND | hist_gradient_boosting | 4185 | 0.4523 | 0.7262 | 0.7257 |
| trend_10m | IND | independent_mlp | 4185 | 0.4466 | 0.7232 | 0.7223 |
| trend_10m | IND | shared_multitask_mlp | 4185 | 0.4359 | 0.7178 | 0.7168 |
| trend_10m | WIN | hist_gradient_boosting | 16210 | 0.4510 | 0.7256 | 0.7251 |
| trend_10m | WIN | independent_mlp | 16210 | 0.4411 | 0.7207 | 0.7201 |
| trend_10m | WIN | shared_multitask_mlp | 16210 | 0.4397 | 0.7195 | 0.7180 |
| trend_15m | IND | hist_gradient_boosting | 4185 | 0.4522 | 0.7260 | 0.7257 |
| trend_15m | IND | independent_mlp | 4185 | 0.4419 | 0.7205 | 0.7198 |
| trend_15m | IND | shared_multitask_mlp | 4185 | 0.4420 | 0.7206 | 0.7201 |
| trend_15m | WIN | hist_gradient_boosting | 16212 | 0.4428 | 0.7218 | 0.7206 |
| trend_15m | WIN | independent_mlp | 16212 | 0.4271 | 0.7117 | 0.7064 |
| trend_15m | WIN | shared_multitask_mlp | 16212 | 0.4267 | 0.7126 | 0.7088 |
| trend_5m | IND | hist_gradient_boosting | 4185 | 0.4828 | 0.7415 | 0.7407 |
| trend_5m | IND | independent_mlp | 4185 | 0.4877 | 0.7440 | 0.7435 |
| trend_5m | IND | shared_multitask_mlp | 4185 | 0.4892 | 0.7441 | 0.7423 |
| trend_5m | WIN | hist_gradient_boosting | 16259 | 0.4914 | 0.7458 | 0.7454 |
| trend_5m | WIN | independent_mlp | 16259 | 0.4937 | 0.7469 | 0.7465 |
| trend_5m | WIN | shared_multitask_mlp | 16259 | 0.4869 | 0.7433 | 0.7425 |

## Primary models by fixed time block

| Target | Block | Model | n | MCC | Balanced accuracy | Macro F1 |
|---|---:|---|---:|---:|---:|---:|
| trend_10m | 1 | hist_gradient_boosting | 5845 | 0.4537 | 0.7291 | 0.7250 |
| trend_10m | 1 | independent_mlp | 5845 | 0.4487 | 0.7266 | 0.7225 |
| trend_10m | 1 | shared_multitask_mlp | 5845 | 0.4343 | 0.7195 | 0.7137 |
| trend_10m | 2 | hist_gradient_boosting | 8211 | 0.4427 | 0.7214 | 0.7213 |
| trend_10m | 2 | independent_mlp | 8211 | 0.4356 | 0.7178 | 0.7177 |
| trend_10m | 2 | shared_multitask_mlp | 8211 | 0.4312 | 0.7154 | 0.7150 |
| trend_10m | 3 | hist_gradient_boosting | 6339 | 0.4544 | 0.7265 | 0.7268 |
| trend_10m | 3 | independent_mlp | 6339 | 0.4389 | 0.7186 | 0.7189 |
| trend_10m | 3 | shared_multitask_mlp | 6339 | 0.4462 | 0.7208 | 0.7210 |
| trend_15m | 1 | hist_gradient_boosting | 5846 | 0.4290 | 0.7174 | 0.7121 |
| trend_15m | 1 | independent_mlp | 5846 | 0.4062 | 0.7057 | 0.6931 |
| trend_15m | 1 | shared_multitask_mlp | 5846 | 0.4104 | 0.7082 | 0.6984 |
| trend_15m | 2 | hist_gradient_boosting | 8209 | 0.4285 | 0.7143 | 0.7142 |
| trend_15m | 2 | independent_mlp | 8209 | 0.4152 | 0.7067 | 0.7050 |
| trend_15m | 2 | shared_multitask_mlp | 8209 | 0.4098 | 0.7045 | 0.7034 |
| trend_15m | 3 | hist_gradient_boosting | 6342 | 0.4731 | 0.7355 | 0.7358 |
| trend_15m | 3 | independent_mlp | 6342 | 0.4630 | 0.7258 | 0.7248 |
| trend_15m | 3 | shared_multitask_mlp | 6342 | 0.4650 | 0.7284 | 0.7280 |
| trend_5m | 1 | hist_gradient_boosting | 5867 | 0.5034 | 0.7525 | 0.7513 |
| trend_5m | 1 | independent_mlp | 5867 | 0.5037 | 0.7526 | 0.7514 |
| trend_5m | 1 | shared_multitask_mlp | 5867 | 0.5023 | 0.7521 | 0.7500 |
| trend_5m | 2 | hist_gradient_boosting | 8230 | 0.4836 | 0.7418 | 0.7418 |
| trend_5m | 2 | independent_mlp | 8230 | 0.4897 | 0.7449 | 0.7448 |
| trend_5m | 2 | shared_multitask_mlp | 8230 | 0.4794 | 0.7395 | 0.7394 |
| trend_5m | 3 | hist_gradient_boosting | 6347 | 0.4834 | 0.7409 | 0.7402 |
| trend_5m | 3 | independent_mlp | 6347 | 0.4840 | 0.7415 | 0.7409 |
| trend_5m | 3 | shared_multitask_mlp | 6347 | 0.4824 | 0.7395 | 0.7381 |

## Contract-level sensitivity (descriptive)

Performance is also retained per ticker/contract in `final_test_contract_metrics.csv`; the contracts remain separate, with no continuous-series stitching. These small-contract summaries are descriptive and are not used for model selection or inferential claims.


## Interpretation

The independent and shared MLPs are effectively tied: all three paired confidence intervals include zero. On the 5-minute target, the independent MLP is close to logistic regression and HistGradientBoosting; on 10- and 15-minute targets, HistGradientBoosting has the highest pooled MCC among the listed models. Root-level results are broadly similar, while the 15-minute scores increase in the final time block for all three displayed models.
The soft-score MLP improves over the training-mean constant by 31.1% in MAE and 36.9% in MSE. This measures reproduction of the B0 vote fraction only.

These are predictions of retrospective B0 labels, not independent market truth. The analysis covers only WIN/IND in January–June 2026, has no executable trading or profitability evaluation, and does not establish an edge. B1/B2/Fuzzy coverage is insufficient for an independent-label comparison.

Reproduction: run the committed one-pass model evaluator only before opening the final test, then run `scripts/summarize_final_test.py` to derive pooled and subgroup tables from its saved predictions. The supplement script does not fit models or rerun test scoring. The final test was already opened for this study; do not use it for further model or hyperparameter selection.
