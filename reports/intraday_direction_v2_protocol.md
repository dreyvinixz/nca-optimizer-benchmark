# Protocolo da baseline direcional intradiária v2

## Pergunta e unidade de previsão

Depois do fechamento do candle de um minuto no instante `t`, estimar se o fechamento estará acima do fechamento atual após 5, 15 ou 30 barras consecutivas observadas. O rótulo é `1` para retorno logarítmico positivo e `0` para retorno zero/negativo. A observação só é elegível quando os candles intermediários existem e permanecem no mesmo ticker, pregão e trecho contínuo. A primeira versão não usa banda neutra.

Os resultados de janeiro a junho de 2026 são desenvolvimento. O teste histórico do estudo B0 já foi consultado e não serve como teste final desta hipótese. A avaliação expanding por pregões estima estabilidade temporal interna; um período futuro intocado ainda será necessário para confirmação.

## Indicadores candidatos

Todos os indicadores usam o candle atual já fechado e observações anteriores da mesma série. A série reinicia por contrato, pregão e gap. Não há preenchimento de lacunas. Janelas incompletas ficam ausentes e não são imputadas.

| Família | Cálculo e janelas | Quantidade |
|---|---|---:|
| Retorno/momentum | Retorno logarítmico do fechamento em 1, 2, 3, 5, 10, 15 e 30 minutos observados | 7 |
| Forma do candle | Corpo, amplitude, pavio superior, pavio inferior e posição do fechamento na amplitude, normalizados pelo preço/amplitude | 5 |
| Médias e MACD | Distância log do fechamento à SMA e EMA em 5, 10, 15, 20 e 30; MACD 12/26, sinal 9 e histograma normalizados pelo fechamento | 13 |
| RSI e estocástico | RSI 7/14/28; %K e %D estocásticos em 14/28 | 7 |
| Amplitude e direção | ATR fracionário 5/14/30; +DI, -DI e ADX em 14/28 | 9 |
| Volatilidade | Desvio-padrão populacional dos retornos e semivolatilidade positiva/negativa em 5/10/15/20/30 | 15 |
| Bandas e canais | %B e largura de Bollinger em 20/30; posição e largura de Donchian em 10/20/30 | 10 |
| Atividade | Volume, negócios e quantidade em log; surpresa contra média/mediana em 5/15/30 e z-score em 15/30 | 27 |
| Acumulados do pregão | Retorno e amplitude desde o primeiro candle observado; log dos acumulados de volume, negócios e quantidade | 5 |
| Hora do dia | Fração da janela 09:00–18:00 e codificações seno/cosseno | 3 |
| **Total candidato** | Valores exatos registrados no manifesto após a geração | **101** |

As faixas 09:00–12:00, 12:00–15:00 e 15:00–18:00 são cortes de pesquisa dentro da janela local observada, não uma afirmação sobre horários oficiais da bolsa. Cada tarefa ajusta e avalia modelos apenas na faixa em que a previsão é emitida; o horizonte futuro pode avançar para outra faixa, mas nunca para outro pregão/contrato/trecho.

## Seleção e ranking

Em cada fold externo e tarefa `(horizonte, faixa)`, três métodos ranqueiam as mesmas colunas:

1. **Informação mútua:** filtro univariado calculado exclusivamente nos pregões da parte de ajuste interna.
2. **Regressão logística L1:** magnitude dos coeficientes após padronização ajustada na parte de ajuste interna.
3. **Importância por permutação:** queda de balanced accuracy ao permutar uma coluna, usando HistGradientBoosting ajustado na parte de ajuste e avaliado nos 10 pregões seguintes do bloco interno, com 3 permutações por coluna e amostra de até 2.000 observações para limitar custo.

Os 10 pregões internos ficam dentro do treino externo; não incluem qualquer observação do bloco externo. Após ordenar, a avaliação usa top 10, top 20 e todas as colunas, com regressão logística e HistGradientBoosting reajustados nos dados completos de treino externo. A estabilidade será descrita pela posição média, frequência no top 10/20 e correlação Spearman entre rankings.

## Cortes e métricas

São usados cinco folds expanding, com 69 pregões iniciais e blocos externos de 10 pregões. Os folds são dependentes e suas variações são descritivas, não intervalos de confiança independentes. Comparadores sem seleção: previsão pela prevalência do treino e momentum causal pelo retorno de 5 minutos já observado.

Métricas: MCC, balanced accuracy e macro-F1 como principais; acurácia, precisão/recall de cada classe, ROC-AUC, PR-AUC, Brier, log-loss, prevalência e matriz de confusão como complementares. Resultados são reportados no conjunto WIN+IND e desagregados por WIN e IND com as mesmas previsões do modelo conjunto. A comparação de muitos seletores, horizontes, faixas e tamanhos de subconjunto é exploratória. Nenhum melhor resultado interno será chamado de vencedor confirmatório. Não há alegação de lucro sem simulação executável com custos.

## Artefatos

- Configuração: `config/intraday_direction_v2.yaml`
- Geração de OHLCV e alvos: `scripts/build_intraday_direction_v2.py`
- Ranking, folds e avaliação: `scripts/run_intraday_direction_v2_selection.py`
- Parquet e manifesto: ignorados pelo Git sob `data/derived/`
- Métricas, ranks, estabilidade e resumo: `reports/intraday_direction_v2_selection*`
