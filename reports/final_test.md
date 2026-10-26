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

## Primary overall metrics (both roots)

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

## Supplementary classification metrics

These metrics were computed from the saved one-pass predictions after the primary evaluation. They were not used to refit models, choose models, or tune thresholds. Binary classification metrics use the frozen 0.5 threshold. ROC-AUC uses continuous saved scores; PR-AUC is reported as average precision (AP). ECE uses 10 fixed-width probability bins.

| Model | Target | n | Accuracy | Precision (class 1) | Recall (class 1) | F1 macro | ROC-AUC | PR-AUC (AP) | Specificity | Cohen kappa | ECE |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| majority_constant | majority | 20332 | 0.4843 | 0.4843 | 1.0000 | 0.3263 | 0.5000 | 0.4843 | 0.0000 | 0.0000 | 0.5157 |
| majority_mlp | majority | 20332 | 0.7302 | 0.7059 | 0.7593 | 0.7302 | 0.8187 | 0.8096 | 0.7029 | 0.4612 | 0.0239 |
| soft_score_mlp | mean_score | 20332 | — | — | — | — | — | — | — | — | — |
| soft_score_training_mean | mean_score | 20332 | — | — | — | — | — | — | — | — | — |
| causal_5m_momentum | trend_10m | 20395 | 0.7161 | 0.6990 | 0.7224 | 0.7160 | — | — | 0.7102 | 0.4321 | — |
| hist_gradient_boosting | trend_10m | 20395 | 0.7252 | 0.7046 | 0.7409 | 0.7252 | 0.8093 | 0.8001 | 0.7106 | 0.4507 | 0.0191 |
| independent_mlp | trend_10m | 20395 | 0.7206 | 0.6992 | 0.7385 | 0.7206 | 0.8067 | 0.7976 | 0.7039 | 0.4416 | 0.0231 |
| logistic_regression | trend_10m | 20395 | 0.7206 | 0.6977 | 0.7425 | 0.7206 | 0.7945 | 0.7753 | 0.7002 | 0.4418 | 0.0418 |
| majority_constant | trend_10m | 20395 | 0.4823 | 0.4823 | 1.0000 | 0.3254 | 0.5000 | 0.4823 | 0.0000 | 0.0000 | 0.5177 |
| shared_multitask_mlp | trend_10m | 20395 | 0.7178 | 0.6887 | 0.7571 | 0.7178 | 0.8054 | 0.7973 | 0.6812 | 0.4368 | 0.0370 |
| causal_5m_momentum | trend_15m | 20397 | 0.6898 | 0.6661 | 0.6973 | 0.6896 | — | — | 0.6830 | 0.3795 | — |
| hist_gradient_boosting | trend_15m | 20397 | 0.7218 | 0.6947 | 0.7404 | 0.7217 | 0.8050 | 0.7866 | 0.7049 | 0.4439 | 0.0288 |
| independent_mlp | trend_15m | 20397 | 0.7096 | 0.6642 | 0.7872 | 0.7091 | 0.7983 | 0.7838 | 0.6392 | 0.4227 | 0.0650 |
| logistic_regression | trend_15m | 20397 | 0.7160 | 0.6863 | 0.7418 | 0.7160 | 0.7887 | 0.7660 | 0.6926 | 0.4327 | 0.0438 |
| majority_constant | trend_15m | 20397 | 0.4756 | 0.4756 | 1.0000 | 0.3223 | 0.5000 | 0.4756 | 0.0000 | 0.0000 | 0.5244 |
| shared_multitask_mlp | trend_15m | 20397 | 0.7112 | 0.6709 | 0.7709 | 0.7111 | 0.7973 | 0.7821 | 0.6571 | 0.4251 | 0.0559 |
| causal_5m_momentum | trend_5m | 20444 | 0.7282 | 0.7142 | 0.7334 | 0.7281 | — | — | 0.7233 | 0.4563 | — |
| hist_gradient_boosting | trend_5m | 20444 | 0.7444 | 0.7259 | 0.7606 | 0.7444 | 0.8403 | 0.8358 | 0.7292 | 0.4891 | 0.0234 |
| independent_mlp | trend_5m | 20444 | 0.7459 | 0.7280 | 0.7605 | 0.7459 | 0.8388 | 0.8348 | 0.7321 | 0.4920 | 0.0215 |
| logistic_regression | trend_5m | 20444 | 0.7438 | 0.7213 | 0.7693 | 0.7438 | 0.8235 | 0.8129 | 0.7198 | 0.4881 | 0.0375 |
| majority_constant | trend_5m | 20444 | 0.4853 | 0.4853 | 1.0000 | 0.3267 | 0.5000 | 0.4853 | 0.0000 | 0.0000 | 0.5147 |
| shared_multitask_mlp | trend_5m | 20444 | 0.7425 | 0.7172 | 0.7749 | 0.7425 | 0.8355 | 0.8308 | 0.7120 | 0.4858 | 0.0275 |

## Existing and regression metrics

The complete CSV also retains MCC, balanced accuracy, class-wise precision/recall/F1, prevalence, all four confusion-matrix cells, Brier score, log loss, ECE, MAE, and MSE. MAE/MSE apply to the continuous `mean_score` target; threshold-based classification and AUC metrics do not apply to it.

## Confusion matrices for primary models

Each cell is shown as `actual 0/1 × predicted 0/1`: TN, FP, FN, TP.

| Target | Model | TN | FP | FN | TP |
|---|---|---:|---:|---:|---:|
| trend_10m | hist_gradient_boosting | 7503 | 3055 | 2549 | 7288 |
| trend_10m | independent_mlp | 7432 | 3126 | 2572 | 7265 |
| trend_10m | shared_multitask_mlp | 7192 | 3366 | 2389 | 7448 |
| trend_15m | hist_gradient_boosting | 7540 | 3157 | 2518 | 7182 |
| trend_15m | independent_mlp | 6837 | 3860 | 2064 | 7636 |
| trend_15m | shared_multitask_mlp | 7029 | 3668 | 2222 | 7478 |
| trend_5m | hist_gradient_boosting | 7673 | 2850 | 2375 | 7546 |
| trend_5m | independent_mlp | 7704 | 2819 | 2376 | 7545 |
| trend_5m | shared_multitask_mlp | 7492 | 3031 | 2233 | 7688 |

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
