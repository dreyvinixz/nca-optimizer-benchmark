# Validacao out-of-time com Quantbase 2026

Este teste usa dados novos do Quantbase, ainda fora do dataset original de
2024. O recorte processado foi de 2026-06-22 a 2026-06-24, com candles de 1
segundo agregados para 5 minutos. O contrato selecionado automaticamente foi o
`WINQ26`, por maior volume diario entre os contratos `WIN`.

## Protocolo

1. Treinar novamente no bloco antigo de treino+validacao do benchmark.
2. Usar os melhores hiperparametros ja encontrados pelos otimizadores.
3. Predizer o periodo novo de 2026 sem reotimizar hiperparametros.
4. Simular replay economico: sinal no candle `i`, entrada no candle `i+1`,
   custo de 5 pontos por operacao e filtro de confianca minima de 0.55.

## Resultado preditivo medio

| Modelo | Otimizador | Accuracy | MCC | F1 | AUC-ROC | Seeds |
|---|---|---:|---:|---:|---:|---:|
| RF | GWO | 0.542 | 0.084 | 0.599 | 0.520 | 5 |
| MLP | GWO | 0.535 | 0.068 | 0.586 | 0.538 | 5 |
| SVM | GWO | 0.530 | 0.060 | 0.591 | 0.543 | 3 |
| CNN | DE | 0.519 | 0.037 | 0.581 | 0.522 | 3 |

## Resultado economico medio

| Modelo | Otimizador | Trades | Lucro total | Media/trade | Win rate | Profit factor | Max drawdown |
|---|---|---:|---:|---:|---:|---:|---:|
| RF | GWO | 302.4 | 5394.0 pts | 17.83 pts | 0.524 | 1.380 | -2283.0 pts |
| MLP | GWO | 304.8 | 4586.0 pts | 15.05 pts | 0.515 | 1.316 | -2175.0 pts |
| SVM | GWO | 302.0 | 4525.0 pts | 15.00 pts | 0.518 | 1.309 | -2525.0 pts |
| CNN | DE | 127.0 | 1411.7 pts | 9.74 pts | 0.495 | 1.181 | -1370.0 pts |

## Leitura cautelosa

Neste recorte curto de tres dias, o `RF+GWO` foi o melhor em MCC, F1, lucro
medio por trade, profit factor e Sharpe. Ainda nao da para bater o martelo
como melhor modelo geral, porque o periodo e pequeno e as combinacoes nao tem
o mesmo numero de seeds disponiveis nos arquivos salvos. O resultado serve como
primeiro sinal de robustez fora da amostra e justifica rodar uma janela maior
de 2026 antes da conclusao final.
