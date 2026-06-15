# Protocolo Experimental 2 x 2

Este documento registra o protocolo solicitado pelo professor e separa o que ja foi executado do que ainda precisa ser implementado caso o protocolo seja confirmado.

## Ideia Central

O professor pediu comparar duas funcoes de fitness em dois protocolos de validacao:

| Protocolo de validacao | Fitness MCC/F1 | Fitness Accuracy |
|---|---:|---:|
| Holdout temporal 60/20/20 | Experimento 1 | Experimento 2 |
| Cross-validation temporal | Experimento 3 | Experimento 4 |

Em todos os experimentos, o criterio final deve ser sempre o mesmo:

- avaliar no mesmo `X_test` cego;
- usar as mesmas seeds `1, 2, 3`;
- usar o mesmo budget de otimizacao;
- comparar modelos e otimizadores pelas metricas finais no teste, nao pelo valor bruto de fitness.

## Dataset E Split Principal

Dataset:

- arquivo: `data/raw/merged_output.csv`
- amostras apos pipeline de modelagem: `15.057`
- ativo/frequencia: WIN, 5 minutos
- periodo usado pelo pipeline: `2024-01-02 09:40:00` ate `2024-06-28 17:50:00`

Split principal atual:

| Bloco | Percentual | Amostras | Papel |
|---|---:|---:|---|
| Treino | 60% | 9.034 | ajuste dos modelos no holdout |
| Validacao | 20% | 3.011 | validacao fixa no protocolo holdout |
| Teste cego | 20% | 3.012 | avaliacao final comum a todos |

Regra importante:

> O `X_test` cego nao deve ser usado durante a otimizacao. Ele entra apenas no final, para comparar os experimentos.

## Fitness 1: MCC/F1

Formula base:

```text
fitness = 0.6 * MCC + 0.4 * F1
```

Interpretacao:

- MCC mede qualidade da classificacao considerando os quatro termos da matriz de confusao;
- F1 equilibra precisao e recall;
- a combinacao favorece modelos menos enganados por desbalanceamento e por acuracia artificial.

## Fitness 2: Accuracy

O professor pediu manter a formula:

```text
fitness = 0.4 * Acc_train + 0.6 * Acc_val
```

Interpretacao:

- `Acc_train` entra com peso 40%;
- `Acc_val` entra com peso 60%;
- a validacao tem peso maior porque representa melhor a capacidade de generalizacao.

## Experimento 1: Holdout + MCC/F1

Status: **ja executado / praticamente pronto**.

Fonte atual:

- `outputs/article_official/metrics/`
- fitness atual configurada como `mcc_f1`

Protocolo:

```text
Treino 60% -> ajusta o modelo
Validacao 20% -> calcula MCC_val e F1_val
Teste 20% -> avaliacao final cega
```

Fitness:

```text
fitness = 0.6 * MCC_val + 0.4 * F1_val
```

Resultado principal ja observado:

- melhor par medio: `MLP + GWO`
- `accuracy_test = 0.652501`
- `mcc_test = 0.304668`

Observacao:

- este experimento representa o regime principal recomendado ate agora para o artigo.

## Experimento 2: Holdout + Accuracy

Status: **implementado, ainda nao rodado**.

Protocolo desejado:

```text
Treino 60% -> ajusta o modelo e calcula Acc_train
Validacao 20% -> calcula Acc_val
Teste 20% -> avaliacao final cega
```

Fitness:

```text
fitness = 0.4 * Acc_train + 0.6 * Acc_val
```

Implementacao preparada:

- modo de fitness: `accuracy_holdout`;
- usar o split fixo 60/20/20;
- nao usar `TimeSeriesSplit` nesse experimento;
- salvar resultados em pasta separada:

```text
outputs/article_official_accuracy_holdout/
```

## Experimento 3: Cross-Validation + MCC/F1

Status: **implementado, ainda nao rodado**.

Protocolo desejado:

```text
Treino + validacao -> dividido em folds temporais internos
Fold 1 -> calcula MCC_val_fold e F1_val_fold
Fold 2 -> calcula MCC_val_fold e F1_val_fold
Fold 3 -> calcula MCC_val_fold e F1_val_fold
Teste 20% -> avaliacao final cega
```

Fitness:

```text
fitness = media_dos_folds(0.6 * MCC_val_fold + 0.4 * F1_val_fold)
```

Implementacao preparada:

- modo de fitness: `mcc_f1_cv`;
- usar `TimeSeriesSplit(n_splits=3)`;
- manter o `X_test` final fora dos folds;
- salvar resultados em pasta separada:

```text
outputs/article_official_mcc_f1_cv/
```

## Experimento 4: Cross-Validation + Accuracy

Status: **ja executado parcialmente / pronto como Accuracy-CV atual**.

Fonte atual:

- `outputs/article_official_accuracy/metrics/`
- nome atual nos resultados: `Accuracy-CV`

Protocolo:

```text
Treino + validacao -> dividido em folds temporais internos
Fold 1 -> calcula Acc_train_fold e Acc_val_fold
Fold 2 -> calcula Acc_train_fold e Acc_val_fold
Fold 3 -> calcula Acc_train_fold e Acc_val_fold
Teste 20% -> avaliacao final cega
```

Fitness:

```text
fitness = media_dos_folds(0.4 * Acc_train_fold + 0.6 * Acc_val_fold)
```

Resultado principal ja observado:

- melhor par medio: `MLP + GWO`
- `accuracy_test = 0.651505`
- `mcc_test = 0.302763`

Observacao:

- este experimento corresponde ao que chamamos no deck de `Accuracy-CV`.

## Resumo Do Que Ja Temos

| Experimento | Protocolo | Fitness | Status | Pasta atual/proposta |
|---|---|---|---|---|
| Exp. 1 | Holdout 60/20/20 | MCC/F1 | ja executado | `outputs/article_official/` |
| Exp. 2 | Holdout 60/20/20 | Accuracy | implementado, ainda nao rodado | `outputs/article_official_accuracy_holdout/` |
| Exp. 3 | Cross-validation temporal | MCC/F1 | implementado, ainda nao rodado | `outputs/article_official_mcc_f1_cv/` |
| Exp. 4 | Cross-validation temporal | Accuracy | ja executado | `outputs/article_official_accuracy/` |

## Figura Do Protocolo

A figura esquematica ja foi gerada em:

```text
outputs/professor_presentation/figures/protocolo_holdout_cv_fitness.png
outputs/professor_presentation/figures/protocolo_holdout_cv_fitness.pdf
```

## O Que Implementar Quando O Professor Confirmar

1. Modos de fitness adicionados:

```text
accuracy_holdout
mcc_f1_cv
```

2. Quando o professor confirmar, rodar o benchmark oficial para os dois experimentos faltantes:

```text
Holdout + Accuracy
Cross-validation + MCC/F1
```

3. Manter constantes:

- modelos: `MLP`, `CNN`, `SVM`, `Random Forest`;
- otimizadores: `Random Search`, `GA`, `PSO`, `DE`, `GWO`;
- seeds: `1, 2, 3`;
- budget: `1000` avaliacoes por seed;
- `X_test` cego igual para todos.

4. Atualizar a apresentacao e tabelas finais para comparar:

```text
4 experimentos x 4 modelos x 5 otimizadores
```

5. Escolher a recomendacao final pelo desempenho medio no `X_test`:

- `accuracy_test`;
- `mcc_test`;
- `f1_test`;
- e, se mantido, backtest economico do melhor par.

## Observacao Para Apresentar Ao Professor

Uma frase curta para explicar:

> O protocolo final fica 2 x 2: duas estrategias de validacao, holdout temporal e cross-validation temporal, cruzadas com duas funcoes de fitness, MCC/F1 e Accuracy. A formula da Accuracy e mantida como `0.4 * Acc_train + 0.6 * Acc_val`; a diferenca e que no holdout ela usa treino e validacao fixos, enquanto no cross-validation ela e calculada em cada fold e depois fazemos a media.

## Comandos Preparados, Ainda Nao Executados

Experimento 2, holdout + Accuracy:

```powershell
.\.venv\Scripts\python.exe scripts\run_article_official_benchmark.py `
  --fitness-mode accuracy_holdout `
  --seeds 1 2 3 `
  --evaluations-per-seed 1000
```

Saida padrao:

```text
outputs/article_official_accuracy_holdout/
```

Acompanhar status:

```powershell
.\.venv\Scripts\python.exe scripts\check_article_official_status.py `
  --output-root outputs/article_official_accuracy_holdout
```

Experimento 3, cross-validation + MCC/F1:

```powershell
.\.venv\Scripts\python.exe scripts\run_article_official_benchmark.py `
  --fitness-mode mcc_f1_cv `
  --seeds 1 2 3 `
  --evaluations-per-seed 1000
```

Saida padrao:

```text
outputs/article_official_mcc_f1_cv/
```

Acompanhar status:

```powershell
.\.venv\Scripts\python.exe scripts\check_article_official_status.py `
  --output-root outputs/article_official_mcc_f1_cv
```

Observacao de implementacao:

> Para manter consistencia com o experimento 4 ja executado (`Accuracy-CV`), o modo cross-validation usa o bloco `treino + validacao` como area interna de folds temporais e deixa apenas o `X_test` cego totalmente fora da otimizacao.
