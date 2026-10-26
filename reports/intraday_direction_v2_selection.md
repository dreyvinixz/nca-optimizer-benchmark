# Baseline direcional intradiária v2 — resultados de desenvolvimento

Validação rolling-origin. Todas as datas disponíveis são desenvolvimento; o teste histórico já aberto não é teste independente desta hipótese. Nenhuma conclusão de rentabilidade é avaliada.

- Indicadores: 101; folds executados: 5; métricas por modelo/fold: 2700.
- Ranking de features: intraday_direction_v2_selection_rankings.csv; estabilidade: intraday_direction_v2_selection_stability.csv; correlações Spearman: intraday_direction_v2_selection_rank_correlations.csv.
- Ranking de permutação usa somente o bloco temporal interno do treino. Cada bloco externo permanece fora da seleção. Métricas por WIN/IND usam previsões do modelo conjunto.

## Melhores combinações por horizonte/faixa/raiz (MCC médio; apenas resumo exploratório)

| Horizonte | Faixa | Raiz | Seletor | K | Modelo | MCC ± DP | Balanced accuracy | Macro-F1 | ROC-AUC | PR-AUC |
|---:|---|---|---|---:|---|---:|---:|---:|---:|---:|
| 5m | early | ALL | mutual_information | 10 | logistic_regression | 0.027 ± 0.058 | 0.511 | 0.484 | 0.508 | 0.480 |
| 5m | early | IND | mutual_information | 10 | hist_gradient_boosting | 0.034 ± 0.039 | 0.517 | 0.512 | 0.517 | 0.495 |
| 5m | early | WIN | mutual_information | 10 | logistic_regression | 0.032 ± 0.057 | 0.514 | 0.486 | 0.506 | 0.479 |
| 5m | late | ALL | inner_temporal_permutation | all | hist_gradient_boosting | 0.024 ± 0.036 | 0.512 | 0.511 | 0.514 | 0.482 |
| 5m | late | IND | inner_temporal_permutation | 20 | logistic_regression | 0.076 ± 0.107 | 0.534 | 0.505 | 0.537 | 0.515 |
| 5m | late | WIN | inner_temporal_permutation | all | hist_gradient_boosting | 0.026 ± 0.038 | 0.513 | 0.512 | 0.516 | 0.485 |
| 5m | middle | ALL | mutual_information | 10 | logistic_regression | 0.049 ± 0.056 | 0.524 | 0.499 | 0.531 | 0.507 |
| 5m | middle | IND | inner_temporal_permutation | all | hist_gradient_boosting | 0.089 ± 0.071 | 0.545 | 0.539 | 0.544 | 0.532 |
| 5m | middle | WIN | mutual_information | 10 | logistic_regression | 0.050 ± 0.052 | 0.524 | 0.495 | 0.534 | 0.509 |
| 15m | early | ALL | mutual_information | all | logistic_regression | 0.016 ± 0.051 | 0.508 | 0.506 | 0.501 | 0.494 |
| 15m | early | IND | mutual_information | all | logistic_regression | 0.029 ± 0.091 | 0.514 | 0.513 | 0.503 | 0.522 |
| 15m | early | WIN | mutual_information | 10 | logistic_regression | 0.020 ± 0.072 | 0.508 | 0.490 | 0.505 | 0.488 |
| 15m | late | ALL | l1_logistic | 10 | hist_gradient_boosting | 0.018 ± 0.081 | 0.510 | 0.496 | 0.511 | 0.481 |
| 15m | late | IND | inner_temporal_permutation | all | hist_gradient_boosting | 0.001 ± 0.167 | 0.498 | 0.416 | 0.476 | 0.427 |
| 15m | late | WIN | l1_logistic | 10 | hist_gradient_boosting | 0.024 ± 0.079 | 0.512 | 0.499 | 0.516 | 0.487 |
| 15m | middle | ALL | mutual_information | 10 | logistic_regression | 0.054 ± 0.045 | 0.524 | 0.480 | 0.526 | 0.494 |
| 15m | middle | IND | mutual_information | 10 | logistic_regression | 0.195 ± 0.156 | 0.602 | 0.545 | 0.569 | 0.527 |
| 15m | middle | WIN | mutual_information | 10 | logistic_regression | 0.046 ± 0.046 | 0.520 | 0.471 | 0.525 | 0.492 |
| 30m | early | ALL | inner_temporal_permutation | 20 | logistic_regression | 0.043 ± 0.033 | 0.521 | 0.513 | 0.510 | 0.498 |
| 30m | early | IND | inner_temporal_permutation | all | logistic_regression | 0.043 ± 0.163 | 0.520 | 0.518 | 0.510 | 0.517 |
| 30m | early | WIN | inner_temporal_permutation | 10 | logistic_regression | 0.051 ± 0.060 | 0.526 | 0.517 | 0.507 | 0.495 |
| 30m | late | ALL | mutual_information | 10 | logistic_regression | 0.055 ± 0.086 | 0.525 | 0.498 | 0.497 | 0.423 |
| 30m | late | IND | l1_logistic | 10 | logistic_regression | 0.174 ± 0.241 | 0.391 | 0.312 | 0.657 | 0.649 |
| 30m | late | WIN | mutual_information | 10 | logistic_regression | 0.060 ± 0.089 | 0.527 | 0.500 | 0.500 | 0.426 |
| 30m | middle | ALL | mutual_information | 10 | logistic_regression | 0.025 ± 0.074 | 0.515 | 0.469 | 0.522 | 0.492 |
| 30m | middle | IND | inner_temporal_permutation | 20 | hist_gradient_boosting | 0.187 ± 0.158 | 0.589 | 0.545 | 0.584 | 0.512 |
| 30m | middle | WIN | mutual_information | 10 | logistic_regression | 0.033 ± 0.075 | 0.518 | 0.470 | 0.524 | 0.495 |

## Top 10 por método e tarefa

| Horizonte | Faixa | Método | Features (ordem média) |
|---:|---|---|---|
| 5m | early | inner_temporal_permutation | upside_semivolatility_15m, ema_distance_10m, realized_volatility_5m, log_return_1m, candle_body_fraction, session_log_cumulative_quantity, upper_wick_fraction, atr_fraction_30m, upside_semivolatility_20m, log_return_2m |
| 5m | early | l1_logistic | sma_distance_30m, sma_distance_15m, quantity_robust_surprise_15m, log_volume, upside_semivolatility_30m, donchian_width_30m, session_log_cumulative_trades, stochastic_k_14m, donchian_position_10m, session_return_so_far |
| 5m | early | mutual_information | session_range_so_far, downside_semivolatility_15m, downside_semivolatility_30m, downside_semivolatility_20m, downside_semivolatility_10m, upside_semivolatility_30m, downside_semivolatility_5m, upside_semivolatility_15m, upside_semivolatility_10m, upside_semivolatility_20m |
| 5m | late | inner_temporal_permutation | adx_28m, sma_distance_10m, log_return_5m, session_log_cumulative_trades, sma_distance_5m, downside_semivolatility_5m, downside_semivolatility_20m, plus_di_14m, candle_range_fraction, log_return_1m |
| 5m | late | l1_logistic | sma_distance_10m, bollinger_percent_b_20m, trades_zscore_30m, upside_semivolatility_20m, realized_volatility_5m, plus_di_28m, upside_semivolatility_5m, realized_volatility_30m, stochastic_k_28m, atr_fraction_5m |
| 5m | late | mutual_information | donchian_width_30m, donchian_width_20m, session_range_so_far, downside_semivolatility_10m, donchian_width_10m, downside_semivolatility_30m, downside_semivolatility_20m, downside_semivolatility_5m, upside_semivolatility_10m, upside_semivolatility_20m |
| 5m | middle | inner_temporal_permutation | minus_di_28m, close_location_in_range, upside_semivolatility_20m, plus_di_28m, bollinger_width_30m, sma_distance_5m, stochastic_k_28m, session_log_cumulative_volume, donchian_position_30m, macd_histogram_fraction |
| 5m | middle | l1_logistic | rsi_28m, atr_fraction_14m, minus_di_28m, trades_surprise_5m, sma_distance_5m, plus_di_28m, upside_semivolatility_20m, stochastic_k_28m, trades_robust_surprise_5m, downside_semivolatility_30m |
| 5m | middle | mutual_information | session_range_so_far, donchian_width_30m, downside_semivolatility_10m, downside_semivolatility_5m, donchian_width_20m, upside_semivolatility_10m, downside_semivolatility_20m, downside_semivolatility_30m, downside_semivolatility_15m, upside_semivolatility_20m |
| 15m | early | inner_temporal_permutation | minus_di_28m, realized_volatility_30m, upside_semivolatility_5m, log_return_1m, ema_distance_30m, log_return_2m, rsi_28m, log_return_10m, candle_body_fraction, candle_range_fraction |
| 15m | early | l1_logistic | donchian_position_20m, bollinger_percent_b_20m, bollinger_width_30m, log_volume, session_log_cumulative_trades, quantity_robust_surprise_15m, sma_distance_30m, stochastic_d_28m, sma_distance_10m, plus_di_28m |
| 15m | early | mutual_information | session_range_so_far, downside_semivolatility_15m, downside_semivolatility_20m, downside_semivolatility_5m, downside_semivolatility_10m, downside_semivolatility_30m, upside_semivolatility_20m, upside_semivolatility_10m, upside_semivolatility_30m, donchian_width_30m |
| 15m | late | inner_temporal_permutation | time_of_day_sin, candle_body_fraction, sma_distance_5m, session_log_cumulative_quantity, donchian_width_10m, log_return_3m, upside_semivolatility_15m, donchian_position_30m, downside_semivolatility_15m, log_return_2m |
| 15m | late | l1_logistic | donchian_width_30m, realized_volatility_30m, upside_semivolatility_15m, macd_histogram_fraction, plus_di_28m, minus_di_28m, sma_distance_15m, bollinger_width_20m, realized_volatility_15m, downside_semivolatility_15m |
| 15m | late | mutual_information | session_range_so_far, donchian_width_30m, donchian_width_20m, downside_semivolatility_20m, upside_semivolatility_20m, downside_semivolatility_10m, downside_semivolatility_30m, upside_semivolatility_15m, upside_semivolatility_30m, downside_semivolatility_15m |
| 15m | middle | inner_temporal_permutation | downside_semivolatility_20m, log_return_15m, donchian_width_20m, log_return_30m, macd_histogram_fraction, minus_di_14m, rsi_28m, donchian_width_10m, bollinger_width_30m, upside_semivolatility_30m |
| 15m | middle | l1_logistic | rsi_28m, atr_fraction_14m, donchian_width_10m, minus_di_14m, plus_di_28m, minus_di_28m, stochastic_k_14m, session_log_cumulative_trades, session_range_so_far, donchian_position_20m |
| 15m | middle | mutual_information | session_range_so_far, donchian_width_30m, downside_semivolatility_30m, downside_semivolatility_20m, downside_semivolatility_10m, downside_semivolatility_15m, upside_semivolatility_20m, downside_semivolatility_5m, donchian_width_20m, upside_semivolatility_10m |
| 30m | early | inner_temporal_permutation | session_return_so_far, minus_di_28m, adx_28m, session_log_cumulative_quantity, rsi_28m, downside_semivolatility_20m, downside_semivolatility_15m, donchian_width_30m, atr_fraction_30m, plus_di_28m |
| 30m | early | l1_logistic | log_volume, session_log_cumulative_trades, downside_semivolatility_30m, realized_volatility_30m, donchian_position_30m, bollinger_percent_b_30m, realized_volatility_15m, rsi_28m, rsi_14m, session_return_so_far |
| 30m | early | mutual_information | session_range_so_far, upside_semivolatility_20m, downside_semivolatility_30m, downside_semivolatility_10m, downside_semivolatility_15m, downside_semivolatility_5m, upside_semivolatility_10m, upside_semivolatility_30m, downside_semivolatility_20m, donchian_width_30m |
| 30m | late | inner_temporal_permutation | plus_di_14m, log_return_30m, session_log_cumulative_trades, session_range_so_far, session_log_cumulative_quantity, log_return_1m, macd_signal_9_fraction, bollinger_width_20m, log_return_2m, log_return_3m |
| 30m | late | l1_logistic | downside_semivolatility_30m, donchian_width_20m, bollinger_width_20m, minus_di_28m, adx_28m, bollinger_percent_b_20m, donchian_width_30m, plus_di_28m, downside_semivolatility_15m, log_return_15m |
| 30m | late | mutual_information | session_range_so_far, donchian_width_30m, donchian_width_20m, downside_semivolatility_30m, downside_semivolatility_5m, downside_semivolatility_20m, downside_semivolatility_15m, downside_semivolatility_10m, upside_semivolatility_15m, donchian_width_10m |
| 30m | middle | inner_temporal_permutation | log_return_10m, log_return_1m, session_return_so_far, log_return_2m, donchian_width_20m, candle_body_fraction, candle_range_fraction, minus_di_28m, ema_distance_30m, upper_wick_fraction |
| 30m | middle | l1_logistic | atr_fraction_30m, log_volume, trades_zscore_30m, trades_robust_surprise_15m, trades_zscore_15m, upside_semivolatility_30m, minus_di_14m, session_range_so_far, time_of_day_cos, volume_robust_surprise_15m |
| 30m | middle | mutual_information | session_range_so_far, donchian_width_30m, donchian_width_20m, downside_semivolatility_30m, downside_semivolatility_15m, downside_semivolatility_20m, downside_semivolatility_5m, upside_semivolatility_20m, upside_semivolatility_10m, downside_semivolatility_10m |

## Concordância média dos rankings

| Horizonte | Faixa | Método A | Método B | Spearman |
|---:|---|---|---|---:|
| 5m | early | l1_logistic | inner_temporal_permutation | -0.014 |
| 5m | early | mutual_information | inner_temporal_permutation | 0.018 |
| 5m | early | mutual_information | l1_logistic | 0.289 |
| 5m | late | l1_logistic | inner_temporal_permutation | 0.047 |
| 5m | late | mutual_information | inner_temporal_permutation | 0.032 |
| 5m | late | mutual_information | l1_logistic | 0.188 |
| 5m | middle | l1_logistic | inner_temporal_permutation | 0.109 |
| 5m | middle | mutual_information | inner_temporal_permutation | 0.031 |
| 5m | middle | mutual_information | l1_logistic | 0.355 |
| 15m | early | l1_logistic | inner_temporal_permutation | -0.004 |
| 15m | early | mutual_information | inner_temporal_permutation | 0.020 |
| 15m | early | mutual_information | l1_logistic | 0.109 |
| 15m | late | l1_logistic | inner_temporal_permutation | 0.076 |
| 15m | late | mutual_information | inner_temporal_permutation | 0.121 |
| 15m | late | mutual_information | l1_logistic | 0.327 |
| 15m | middle | l1_logistic | inner_temporal_permutation | 0.096 |
| 15m | middle | mutual_information | inner_temporal_permutation | 0.205 |
| 15m | middle | mutual_information | l1_logistic | 0.210 |
| 30m | early | l1_logistic | inner_temporal_permutation | 0.105 |
| 30m | early | mutual_information | inner_temporal_permutation | 0.272 |
| 30m | early | mutual_information | l1_logistic | 0.289 |
| 30m | late | l1_logistic | inner_temporal_permutation | 0.115 |
| 30m | late | mutual_information | inner_temporal_permutation | 0.235 |
| 30m | late | mutual_information | l1_logistic | 0.279 |
| 30m | middle | l1_logistic | inner_temporal_permutation | -0.048 |
| 30m | middle | mutual_information | inner_temporal_permutation | 0.090 |
| 30m | middle | mutual_information | l1_logistic | 0.111 |

Os melhores valores foram usados para descrição dos folds de desenvolvimento. Como várias tarefas/configurações foram comparadas, não são estimativas confirmatórias nem justificam escolher um vencedor sem avaliação futura bloqueada.

## Leitura dos resultados

- Para os resultados agrupados WIN+IND, o desempenho médio fica próximo da referência de prevalência: MCC médio dos candidatos fica em torno de zero, balanced accuracy perto de 0,50 e ROC-AUC perto de 0,50. O momentum causal de 5 minutos foi negativo nos três horizontes. Não aparece ganho consistente de top-10/top-20 sobre o conjunto completo.
- O maior MCC médio observado entre as combinações pooled foi 0,055 (30m, faixa late, informação mútua top-10 com regressão logística), com desvio-padrão de 0,086 entre folds; ROC-AUC 0,497 e PR-AUC 0,423. Esse resultado é fraco, inconsistente entre métricas e foi escolhido entre muitas combinações.
- A concordância média dos rankings entre folds/tarefas foi baixa: informação mútua vs. L1 = 0,240; informação mútua vs. permutação = 0,114; L1 vs. permutação = 0,054. Informação mútua ranqueou repetidamente amplitude acumulada e semivolatilidade entre as primeiras posições, mas a baixa concordância impede tratar um ranking como consenso.
- A regressão logística emitiu avisos de não convergência no limite de 400 iterações em alguns ajustes. Os resultados lineares são provisórios até repetir esses ajustes com um limite maior e registrar convergência por fold. HistGradientBoosting também não apresenta evidência consistente de desempenho acima da referência.
- As métricas separadas por raiz são previsões do modelo conjunto, não validação de modelos treinados independentemente em WIN e IND. As oscilações por raiz/bloco devem ser lidas junto de `mcc_sd`, cobertura, matriz de confusão e prevalência nos CSVs.

**Conclusão desta baseline:** o conjunto mais amplo e os três métodos foram implementados e comparados, mas os dados de desenvolvimento não sustentam, por enquanto, uma vantagem preditiva estável nem um subconjunto universal de indicadores. Corrigir a convergência da regressão logística e obter um período futuro intocado são pré-requisitos para a etapa confirmatória.
