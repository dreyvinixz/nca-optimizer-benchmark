# Liquidez dos futuros na base intradiária (somente leitura)

Fonte: `price1` do BovDB v3.1-internal.2; sessão por data, agregando contratos da mesma raiz. A métrica primária é `amount_stock` (quantidade negociada de contratos); `business` (negócios) é secundária. `volume` é financeiro em BRL e aparece como contexto, pois o notional/multiplicador varia por produto. Medianas são calculadas entre pregões com linhas presentes.

- Janela da fonte: 2026-01-02 a 2026-06-30.
- Raízes aprovadas na configuração atual: WIN, IND, EURF, WEUF, CCMF, SJCF, BGIG; `WDO`, `WSP` e `ISP` foram incluídos como candidatos explícitos à checagem.

| Ordem por mediana | Raiz | Contratos presentes | Pregões observados | Mediana contratos/dia | Mediana negócios/dia | Mediana volume financeiro BRL/dia | Mediana minutos com negócio/dia |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | WIN | WING26, WINJ26, WINM26, WINQ26, WINV26, WINZ26 | 119 | 17,606,946 | 5,375,827 | 3,247,963,744,390.00 | 1,024 |
| 2 | IND | INDG26, INDJ26, INDM26, INDQ26, INDV26, INDZ26 | 117 | 51,900 | 8,661 | 9,529,452,900.00 | 525 |
| 3 | BGIG | BGIG26, BGIG27 | 52 | 1,844 | 1,216 | 610,384.25 | 172 |
| 4 | CCMF | CCMF26, CCMF27 | 109 | 312 | 155 | 23,025.64 | 38 |
| 5 | EURF | EURF26 | 4 | 42 | 1 | 267,150.00 | 1 |
| 6 | WEUF | WEUF26 | 4 | 26 | 1 | 164,810.25 | 1 |
| 7 | SJCF | SJCF27 | 13 | 1 | 1 | 26.89 | 1 |
| — | WDO | — | 0 | n/a | n/a | n/a | 0 |
| — | WSP | — | 0 | n/a | n/a | n/a | 0 |
| — | ISP | — | 0 | n/a | n/a | n/a | 0 |

## Verificação de disponibilidade dos candidatos

| Raiz | Registros no cadastro de tickers | Linhas price1 | Linhas B4 5m | Linhas B4 10m | Linhas B4 15m |
|---|---:|---:|---:|---:|---:|
| WDO | 67 | 0 | 0 | 0 | 0 |
| WSP | 0 | 0 | 0 | 0 | 0 |
| ISP | 0 | 0 | 0 | 0 | 0 |

## Leitura e limite

- Na amostra atualmente disponível, WIN e IND lideram claramente em quantidade de contratos e negócios. WDO, WSP e ISP sem candles/labels locais não podem ser ranqueados.
- Os registros são a cobertura local da fonte BovDB, não uma auditoria independente de completude de mercado. Ausência local não significa que o produto não foi negociado no período.
- A seleção do universo deve usar a liquidez pré-treino; a auditoria de rótulos B4 já realizada continua válida para as linhas existentes. Reexecutá-la só será necessário para símbolos novos se a fonte for ampliada.
- As somas por raiz agregam contratos sobrepostos no mesmo dia; as janelas de features ainda devem manter a identidade do contrato e não atravessar rolagens.
