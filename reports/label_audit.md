# Auditoria de rótulos B4 (somente leitura)

Reproduzível por `scripts/audit_labels.py`; bancos SQLite abertos com `mode=ro`.

## Integridade e proveniência

- B4 `data\bovdb-labels-B4-v1.sqlite`: 743989248 bytes; SHA-256 `2d8c18c8d1a46be788ee2810a9caba043c2413102e4ee4f5c9927646037ce4c8`; `quick_check=ok` verificado na Fase 0.
- Fonte `data\bovdb-v3.1-internal.2.sqlite`: 428638208 bytes; SHA-256 `32cadf06387ae172edc804804fe762ef26f9f0928424ee83ce9e37a848389eab`; confere com `label_run.source_sha256`: True.
- Manifesto `C:\mysystems\services\bovdb\bovdb-pipeline\rotulos\data\bovdb-labels-B4-v1.manifest.json`: SHA-256 `977ef4f0448d66c129e8fa2b3caccd20fb5071658fd402e41fc93270d2ed1061`; hash/tamanho do artefato conferem com o B4 local: True.
- Configuração de universo `C:\mysystems\services\bovdb\bovdb-pipeline\config\v3_1_universe.yaml`: SHA-256 `2b08914d5eed3a93245d02d234b8e79e323dada159571bfe5b054424c0ed920b`; raízes futuras: WIN, IND, EURF, WEUF, CCMF, SJCF, BGIG.
- B4 `B4-v1` gerado por `B4-unsuppressed-B0+SIDEWAYS-features-v1`; período 2026-01-02–2026-06-30; 41 tickers e 119 pregões.
- `price1` tem 1255202 linhas; `label_run.source_candle_rows`=1255202; os hashes da fonte são idênticos.

## Cobertura e prevalência global

| Tabela | Linhas | Válidas | Nulas | Classe 0 | Classe 1 | Cobertura | Prevalência classe 1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| trend_5m | 1255202 | 1243932 | 11270 | 641113 | 602819 | 99.1021% | 48.4608% |
| trend_10m | 1255202 | 1239800 | 15402 | 637708 | 602092 | 98.7729% | 48.5636% |
| trend_15m | 1255202 | 1234614 | 20588 | 632931 | 601683 | 98.3598% | 48.7345% |
| trend_mean | 1255202 | 1230077 | 25125 | 632677 | 597400 | 97.9983% | 48.5661% |

## Concordância global

- Chaves alinhadas nas quatro tabelas: 1255202.

| Medida | Casos | Concordância/resultado |
|---|---:|---:|
| Três alvos válidos | 1230077 | — |
| Três classes iguais | 1230077 | 74.2297% |
| `trend_mean` igual ao voto majoritário | 1230077 | 100.0000%; divergências/nulos 0 |
| `mean_score` igual à média dos três rótulos | 1230077 | divergências/nulos 0 |
| 5m × 10m | 1237583 | 83.5960% |
| 5m × 15m | 1232219 | 78.2338% |
| 10m × 15m | 1231428 | 86.6315% |

## Universo de contratos futuros

| Raiz | Contrato | Pregões | Período | Candles | Cobertura 5m | Cobertura 10m | Cobertura 15m |
|---|---|---:|---|---:|---:|---:|---:|
| BGIG | BGIG26 | 39 | 2026-01-02–2026-02-27 | 7690 | 97.3082% | 96.3979% | 95.4616% |
| BGIG | BGIG27 | 13 | 2026-05-19–2026-06-30 | 29 | 34.4828% | 24.1379% | 24.1379% |
| CCMF | CCMF26 | 10 | 2026-01-02–2026-01-15 | 1774 | 98.4216% | 97.1251% | 97.9707% |
| CCMF | CCMF27 | 106 | 2026-01-02–2026-06-30 | 3902 | 92.1579% | 89.0313% | 91.1584% |
| EURF | EURF26 | 4 | 2026-01-06–2026-01-16 | 4 | 0.0000% | 0.0000% | 0.0000% |
| IND | INDG26 | 32 | 2026-01-02–2026-02-18 | 16262 | 99.7294% | 99.2559% | 99.2313% |
| IND | INDJ26 | 55 | 2026-01-13–2026-04-15 | 21083 | 99.5636% | 99.1889% | 99.1699% |
| IND | INDM26 | 45 | 2026-04-06–2026-06-17 | 19471 | 99.2913% | 99.0601% | 98.6801% |
| IND | INDQ26 | 19 | 2026-02-23–2026-06-30 | 5566 | 99.3173% | 99.1556% | 99.0478% |
| IND | INDV26 | 3 | 2026-02-09–2026-06-18 | 5 | 40.0000% | 40.0000% | 20.0000% |
| IND | INDZ26 | 3 | 2026-06-12–2026-06-16 | 6 | 16.6667% | 16.6667% | 16.6667% |
| SJCF | SJCF27 | 13 | 2026-05-11–2026-06-30 | 23 | 39.1304% | 39.1304% | 34.7826% |
| WEUF | WEUF26 | 4 | 2026-01-05–2026-01-14 | 4 | 0.0000% | 0.0000% | 0.0000% |
| WIN | WING26 | 32 | 2026-01-02–2026-02-18 | 16836 | 99.7387% | 99.3942% | 99.3348% |
| WIN | WINJ26 | 71 | 2026-01-02–2026-04-15 | 34766 | 99.6951% | 99.4564% | 99.2349% |
| WIN | WINM26 | 110 | 2026-01-02–2026-06-17 | 40673 | 99.3214% | 99.0706% | 98.9969% |
| WIN | WINQ26 | 88 | 2026-02-13–2026-06-30 | 23029 | 98.7190% | 98.6886% | 98.7755% |
| WIN | WINV26 | 49 | 2026-04-15–2026-06-30 | 4192 | 96.2786% | 96.8511% | 96.8511% |
| WIN | WINZ26 | 30 | 2026-05-12–2026-06-30 | 377 | 77.4536% | 85.1459% | 82.4934% |

## Cobertura e transições por raiz e escala

| Raiz | Escala | Pregões-raiz | Candles | Cobertura | Prev. classe 1 | Mudanças/1.000 transições | Duração média do segmento (candles) | Minutos ausentes |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| WIN | 5m | 119 | 119873 | 99.1975% | 49.9945% | 101.404 | 6.097 | 66648 |
| IND | 5m | 117 | 62393 | 99.4871% | 50.0894% | 100.991 | 6.641 | 9545 |
| EURF | 5m | 4 | 4 | 0.0000% | n/a | n/a | n/a | 0 |
| WEUF | 5m | 4 | 4 | 0.0000% | n/a | n/a | n/a | 0 |
| CCMF | 5m | 109 | 5676 | 94.1156% | 47.2295% | 131.995 | 1.614 | 35311 |
| SJCF | 5m | 13 | 23 | 39.1304% | 0.0000% | n/a | 1.000 | 762 |
| BGIG | 5m | 52 | 7719 | 97.0722% | 50.5805% | 122.093 | 2.194 | 10346 |
| WIN | 10m | 119 | 119873 | 99.0331% | 49.6597% | 50.117 | 8.539 | 66648 |
| IND | 10m | 117 | 62393 | 99.1505% | 50.2821% | 51.162 | 9.677 | 9545 |
| EURF | 10m | 4 | 4 | 0.0000% | n/a | n/a | n/a | 0 |
| WEUF | 10m | 4 | 4 | 0.0000% | n/a | n/a | n/a | 0 |
| CCMF | 10m | 109 | 5676 | 91.5610% | 46.9694% | 83.665 | 1.662 | 35311 |
| SJCF | 10m | 13 | 23 | 39.1304% | 0.0000% | n/a | 1.000 | 762 |
| BGIG | 10m | 52 | 7719 | 96.1264% | 52.7493% | 71.554 | 2.326 | 10346 |
| WIN | 15m | 119 | 119873 | 98.9439% | 49.5123% | 33.013 | 9.846 | 66648 |
| IND | 15m | 117 | 62393 | 99.0079% | 49.6681% | 33.041 | 11.675 | 9545 |
| EURF | 15m | 4 | 4 | 0.0000% | n/a | n/a | n/a | 0 |
| WEUF | 15m | 4 | 4 | 0.0000% | n/a | n/a | n/a | 0 |
| CCMF | 15m | 109 | 5676 | 93.2875% | 45.8357% | 69.114 | 1.686 | 35311 |
| SJCF | 15m | 13 | 23 | 34.7826% | 0.0000% | n/a | 1.000 | 762 |
| BGIG | 15m | 52 | 7719 | 95.1937% | 53.6609% | 49.734 | 2.395 | 10346 |

O CSV `label_audit_by_root_session.csv` contém as métricas por raiz, pregão e escala. Mudanças/segmentos usam pares de rótulos válidos em candles consecutivos separados por um minuto; lacunas interrompem segmentos.

## Limites

- A classificação por raiz usa `future_roots` da configuração BovDB aprovada; contratos da mesma raiz não são aqui emendados/ajustados numa série contínua.
- A chave primária garante unicidade dentro das tabelas, e hash/contagem confirmam a mesma fotografia de origem; não foi feito anti-join candle a candle entre bases por custo de leitura.
- A auditoria descreve os alvos B0 e não seleciona indicadores nem treina modelos. A decisão sobre vencimentos/rolagem segue pendente da Fase 2.
- Prevalência é ponderada por candle; para inferência, pregões/blocos continuam sendo as unidades de incerteza.
