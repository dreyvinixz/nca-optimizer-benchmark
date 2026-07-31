# Live Simulation / Paper Trading

Esta pasta guarda os testes para aproximar o benchmark de um uso operacional,
sem enviar ordens reais.

## 1. Replay offline

Script:

```bash
python scripts/29_replay_trading_simulator.py
```

O replay usa as predicoes ja salvas em `outputs/*/predictions`. A regra e:

```text
sinal no candle i -> entrada no candle i+1 na abertura -> saida no proprio candle i+1
```

Exemplo com filtro de confianca, horario e limite diario:

```bash
python scripts/29_replay_trading_simulator.py ^
  --cost-points 5 ^
  --min-confidence 0.55 ^
  --max-trades-per-day 20 ^
  --start-time 10:00 ^
  --end-time 17:00 ^
  --output-tag confidence_time_filter
```

Exemplo com stop e alvo:

```bash
python scripts/29_replay_trading_simulator.py ^
  --cost-points 5 ^
  --min-confidence 0.55 ^
  --max-trades-per-day 20 ^
  --start-time 10:00 ^
  --end-time 17:00 ^
  --stop-points 150 ^
  --target-points 200 ^
  --output-tag stop150_target200
```

Saidas:

```text
offline_replay/<cenario>/offline_replay_trades.csv
offline_replay/<cenario>/offline_replay_summary_by_seed.csv
offline_replay/<cenario>/offline_replay_summary_by_combo.csv
offline_replay/<cenario>/offline_replay_metadata.json
```

## 2. Paper trading por arquivo

Script:

```bash
python scripts/30_paper_trading_file_simulator.py --input-csv CAMINHO_DO_CSV
```

Formato esperado do CSV:

```text
datetime,open,high,low,close,y_pred,y_proba
```

Colunas opcionais:

```text
model,optimizer,experiment,seed
```

O script nao envia ordem real. Ele apenas atualiza um ledger teorico:

```text
paper_trading/paper_trading_ledger.csv
paper_trading/paper_trading_summary.json
```

Se o CSV ainda nao tiver o candle seguinte, o ultimo sinal fica como
`pending`. Na proxima execucao, quando houver um candle novo, a operacao e
fechada teoricamente.

## 3. Dados novos do Quantbase 2026

O backend Quantbase guarda candles de 1 segundo em:

```text
C:\mysystems\services\quantbase-projectmain-repositories\quantbase-backend\worker\data_lake\gold\candles_1s
```

Para transformar esses dados novos em um CSV de 5 minutos compativel com as
features do benchmark:

```bash
.\\.venv\\Scripts\\python.exe scripts/31_import_quantbase_2026_intraday.py ^
  --start-date 2026-06-22 ^
  --end-date 2026-06-24 ^
  --output data/external/quantbase_win_2026_06_22_24_5m_model_ready.csv
```

Por padrao o script procura contratos `WIN` e escolhe o simbolo de maior volume
em cada dia. No recorte validado, ele selecionou `WINQ26` nos dias 2026-06-22,
2026-06-23 e 2026-06-24.

Para treinar de novo no historico antigo e testar nesse periodo 2026:

```bash
.\\.venv\\Scripts\\python.exe scripts/32_score_quantbase_out_of_time.py ^
  --combos mlp:gwo rf:gwo cnn:de svm:gwo ^
  --new-dataset data/external/quantbase_win_2026_06_22_24_5m_model_ready.csv ^
  --output-dir outputs/professor_presentation/live_simulation/quantbase_2026_out_of_time_initial
```

Saidas principais:

```text
quantbase_2026_out_of_time_initial/predictive_by_seed.csv
quantbase_2026_out_of_time_initial/predictive_by_combo.csv
quantbase_2026_out_of_time_initial/economic_replay_by_seed.csv
quantbase_2026_out_of_time_initial/economic_replay_by_combo.csv
quantbase_2026_out_of_time_initial/economic_replay_trades.csv
```

## Observacao importante

Esses simuladores sao uma etapa antes do trading real. Antes de operar com
capital real, ainda precisamos validar fonte de dados, latencia, spread,
slippage, regras de risco e paper trading conectado a uma fonte ao vivo.
