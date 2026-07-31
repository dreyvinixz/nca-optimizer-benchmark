# Guia de Referência Principal — Formato e Redação NCA

Este guia consolida as diretrizes textuais e de estruturação derivadas diretamente dos dois artigos de referência do projeto (convertidos para Markdown em `article/references/md_references/`).

---

## 1. Referências Principais do Projeto

| Papel no Projeto | Artigo de Referência | Arquivo Markdown |
|---|---|---|
| **Estrutura Principal & Formatação do NCA** | Dhingra et al. (2025) — *A benchmark study of optimizers for short-term solar PV power forecasting using neural networks under real-world constraints*. Neural Computing and Applications (NCA). | [`s00521_2025_11546_2_nca_benchmark.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/references/md_references/s00521_2025_11546_2_nca_benchmark.md) |
| **Escrita Textual & Revisão de Literatura** | Gad (2022) — *Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review*. Archives of Computational Methods in Engineering. | [`2022_pso_systematic_review.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/references/md_references/2022_pso_systematic_review.md) |

---

## 2. Estrutura do Artigo Segundo o Padrão NCA (Dhingra et al., 2025)

### 2.1 Estrutura da Introdução

O artigo do NCA segue um padrão rigoroso de 6 passos na Introdução:

1. **Contexto amplo**: Importância da aplicação prática (no nosso caso: previsão de tendências intraday em mercados futuros).
2. **Importância dos Otimizadores**: Explicar por que a escolha e ajuste do otimizador é tão crítica quanto a arquitetura da rede neural.
3. **Lacuna da Literatura (The Research Gap)**: A maioria dos trabalhos usa apenas 1 otimizador padrão (como Adam ou GA) sem comparação sistemática controlada sob orçamento computacional idêntico (*equal evaluation budget*).
4. **Tabela de Literatura de Referência com Lacunas (Table 1)**: Uma tabela que sintetiza os principais trabalhos anteriores e aponta explicitamente a limitação de cada um.
5. **Lista de Questões Abertas (Open Issues)**: Síntese em lista numerada de 4 a 5 lacunas não resolvidas na literatura.
6. **Principais Contribuições (Main Contributions)**: Lista numerada de 5 a 6 contribuições claras do trabalho.

### Modelo de Contribuições (adaptado para o nosso trabalho):
```latex
The main contributions of this work are:
1. We conduct a controlled benchmark of five metaheuristic optimization algorithms (Random Search, Genetic Algorithm, Particle Swarm Optimization, Differential Evolution, and Grey Wolf Optimizer) for tuning Multilayer Perceptron (MLP) neural networks.
2. We enforce an equal fitness evaluation budget across all optimizers to guarantee a fair performance comparison.
3. We evaluate performance under a strict temporal split protocol (60/20/20 train/val/test) on high-frequency intraday data (WIN mini-index futures) to prevent financial data leakage.
4. We evaluate model performance across classification metrics (MCC, F1-score, Balanced Accuracy, AUC-PR) and perform non-parametric statistical significance testing (Friedman test with Wilcoxon-Holm post-hoc analysis).
5. We analyze optimization dynamics, comparing convergence speed, stability across random seeds, and computational runtime.
6. We conduct a financial evaluation (Sharpe ratio, Maximum Drawdown, Profit Factor, transaction cost sensitivity) to measure the practical economic value of each optimizer.
```

---

## 3. Guia de Tabelas no Padrão NCA (Springer Nature)

### 3.1 Tabela de Síntese da Literatura (Table 1 na Introdução / Related Work)

Estrutura exata extraída de Dhingra et al. (2025):

```latex
\begin{table}[htbp]
\caption{Representative literature on metaheuristic optimizer benchmarks for neural networks and their reported limitations}
\label{tab:lit_comparison}
\begin{tabular}{lllll}
\toprule
Study & Model & Optimizer(s) & Domain / Data & Reported limitation / gap \\
\midrule
Author et al. [X] & MLP & GA & Financial time series & Single optimizer; no equal budget protocol \\
Author et al. [Y] & RF / MLP & GA & Mini-Index futures & No comparison with swarm algorithms (PSO, GWO) \\
Author et al. [Z] & LSTM & PSO & Stock forecasting & Accuracy-only evaluation; lacks convergence & stability analysis \\
... & ... & ... & ... & ... \\
\textbf{Present work} & \textbf{MLP} & \textbf{RS, GA, PSO, DE, GWO} & \textbf{WIN futures (5-min)} & \textbf{Addressed: Controlled benchmark, equal budget, statistical tests, financial backtest} \\
\bottomrule
\end{tabular}
\end{table}
```

### 3.2 Tabela de Resultados Preditivos (Table 2 no Results)

Regras do NCA:
- **Linhas**: Otimizadores (RS, GA, PSO, DE, GWO).
- **Colunas**: Métricas de desempenho ($\text{Mean} \pm \text{Std}$).
- **Valores em Negrito**: O melhor valor em cada coluna deve ser destacado em `\textbf{}`.
- **Valores em Itálico / Sublinhado**: O segundo melhor valor.

```latex
\begin{table}[htbp]
\caption{Predictive performance across 20 random seeds on the test dataset (Mean $\pm$ Std). Best results in bold.}
\label{tab:predictive_results}
\begin{tabular}{lcccccc}
\toprule
Optimizer & Accuracy (\%) & Bal. Acc. (\%) & F1-Score & MCC & AUC-ROC & AUC-PR \\
\midrule
Random Search & 51.20 $\pm$ 0.85 & 50.80 $\pm$ 0.90 & 0.5115 $\pm$ 0.012 & 0.0210 $\pm$ 0.018 & 0.5180 $\pm$ 0.015 & 0.5140 $\pm$ 0.014 \\
GA            & 54.10 $\pm$ 0.65 & 53.95 $\pm$ 0.70 & 0.5402 $\pm$ 0.009 & 0.0815 $\pm$ 0.014 & 0.5520 $\pm$ 0.011 & 0.5480 $\pm$ 0.010 \\
PSO           & \textbf{55.80 $\pm$ 0.52} & \textbf{55.65 $\pm$ 0.55} & \textbf{0.5575 $\pm$ 0.008} & \textbf{0.1150 $\pm$ 0.011} & \textbf{0.5710 $\pm$ 0.009} & \textbf{0.5650 $\pm$ 0.008} \\
DE            & 54.90 $\pm$ 0.58 & 54.75 $\pm$ 0.60 & 0.5485 $\pm$ 0.009 & 0.0970 $\pm$ 0.012 & 0.5600 $\pm$ 0.010 & 0.5550 $\pm$ 0.009 \\
GWO           & 55.10 $\pm$ 0.61 & 54.95 $\pm$ 0.62 & 0.5505 $\pm$ 0.008 & 0.1010 $\pm$ 0.013 & 0.5630 $\pm$ 0.010 & 0.5580 $\pm$ 0.009 \\
\bottomrule
\end{tabular}
\end{table}
```

---

## 4. Guia de Figuras no Padrão NCA

1. **Curvas de Convergência (Fig 1)**:
   - Eixo X: Número de Avaliações de Fitness (0 a 1500).
   - Eixo Y: Melhor Fitness de Validação (MCC / Composite Fitness).
   - Linhas contínuas com faixa sombreada ($\text{Mean} \pm \text{Std}$) representando as seeds.
   - Legenda clara diferenciando as 5 curvas por cor e estilo de linha.

2. **Gráficos de Distribuição / Boxplots (Fig 2)**:
   - Boxplot comparando a distribuição do MCC no conjunto de teste entre os otimizadores.
   - Destacar dispersão e outliers para mostrar estabilidade (*stability across seeds*).

3. **Curva de Sensibilidade Financeira (Fig 3)**:
   - Eixo X: Custo de transação por contrato em pontos / BRL.
   - Eixo Y: Retorno acumulado (%) ou Índice Sharpe.
   - Demostrar a resiliência das estratégias otimizadas frente aos custos operacionais.

---

## 5. Guia Textual e Estilo de Redação (Gad, 2022)

### Vocabulário e Conectivos Acadêmicos Recomendados

| Objetivo Textual | Expressões Recomendadas |
|---|---|
| **Apresentar o gap** | *"While existing studies extensively focus on... little attention has been devoted to..."*, *"However, the comparative impact of different optimizers under equal evaluation budgets remains underexplored."* |
| **Comparar algoritmos** | *"Unlike evolutionary algorithms (EAs) that rely on selection and crossover, swarm-based approaches leverage collective particle dynamics..."*, *"While GA exhibits robust global exploration, PSO demonstrates faster early-stage convergence."* |
| **Discutir resultados** | *"Empirical results indicate a statistically significant advantage for..."*, *"As evidenced in Table X, PSO achieves a superior balance between exploration and exploitation, yielding..."* |
| **Reconhecer limitações** | *"Despite the promising performance of X, several boundary limitations warrant consideration, including..."* |
