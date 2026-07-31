# Saida esperada para o professor

## Interpretacao do pedido

O pedido tem duas partes. A primeira e separar as metricas para nao comparar MCC com Accuracy no mesmo grafico. A segunda e adicionar uma leitura de complexidade empirica: quantos treinamentos/avaliacoes cada otimizador precisou para chegar a um bom resultado.

## Graficos gerados

- `00_visao_geral_experimentos_1_2_3.png`
- `01_experimento_1_mcc_only.png`
- `02_experimentos_1_2_holdout_accuracy.png`
- `03_experimento_3_cv_accuracy_only.png`
- `04_treinamentos_ate_bom_resultado_exp1_exp2_exp3.png`

## Como apresentar os experimentos

- Experimento 1: Holdout temporal com fitness MCC/F1. O grafico principal dele deve ser MCC no X_test.
- Experimento 1 tambem pode aparecer no grafico de holdout/acuracia, mas reportando Accuracy no X_test.
- Experimento 2: Holdout temporal com fitness Accuracy. Deve ser comparado com Exp. 1 apenas quando a metrica reportada for Accuracy.
- Experimento 3: Cross-validation temporal com fitness Accuracy. Deve aparecer sozinho como CV, sem ser chamado de Experimento 4.

## Melhores resultados medios nos graficos

- Exp. 1 MCC: MLP + GWO = MCC 0.3047, F1 0.6601, Accuracy 0.6525.
- Exp. 1 Holdout/Accuracy: MLP + GWO = Accuracy 0.6525.
- Exp. 2 Holdout/Accuracy: MLP + PSO = Accuracy 0.6523.
- Exp. 3 CV/Accuracy: MLP + GWO = Accuracy 0.6515.

## Contagem de treinamentos

Cada linha em `*_runs.csv` foi tratada como uma avaliacao da funcao objetivo, isto e, um treinamento/avaliacao de um candidato de hiperparametros. A saida de eficiencia usa `trainings_to_95pct_final_best`: a mediana de treinamentos necessarios para atingir 95% da melhora obtida pelo melhor fitness final daquela execucao.

- Experimento 1 - Holdout + MCC/F1: menor custo mediano = DE com 126 treinamentos.
- Experimento 2 - Holdout + Accuracy: menor custo mediano = GA com 44 treinamentos.
- Experimento 3 - Cross-validation + Accuracy: menor custo mediano = PSO com 42 treinamentos.

## Observacoes de qualidade dos dados

Algumas combinacoes nao tem as 3 repeticoes completas nos arquivos lidos:
- exp1_holdout_mcc_f1 / svm / gwo: best=3, runs=2
- exp2_holdout_accuracy / svm / gwo: best=3, runs=2
- exp3_cv_accuracy / svm / gwo: best=3, runs=2
