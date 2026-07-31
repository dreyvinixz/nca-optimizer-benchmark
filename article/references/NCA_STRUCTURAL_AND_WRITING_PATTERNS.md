# Manual de Padrões Estruturais, Metodológicos e de Redação — Journal NCA (Springer Nature)

Este documento constitui o **guia mestre de referência e treinamento de escrita** para submissão ao journal **Neural Computing and Applications (NCA)** (Springer Nature, Journal ID 521, ISSN: 0941-0643).

Toda a redação e estrutura do nosso artigo deve obedecer rigorosamente às diretrizes e padrões aqui estabelecidos.

---

## Módulo 1: Requisitos Formais de Formato & Submissão (Springer Nature / NCA)

### 1.1. Extensão e Número de Páginas
- **Layout de Submissão (Coluna Única em LaTeX `sn-jnl.cls`)**:
  - Tamanho recomendado: **12 a 25 páginas** (aproximadamente 6.000 a 10.000 palavras no corpo principal, excluindo referências).
- **Layout Final Publicado pela Editora (Coluna Dupla/Simples Diagramada)**:
  - Média observada na amostra de 40 artigos do NCA: **29.6 páginas** (variando de 14 a 54 páginas).

### 1.2. Protocolo de Anonimização (*Double-Blind Peer Review*)
- **Manuscrito Principal (`main.tex` e pasta `sections/`)**:
  - **100% Anônimo**. Proibida qualquer menção a nomes de autores, e-mails, universidades, cidades de origem do grupo ou códigos de projetos de órgãos de fomento.
  - Citações de trabalhos anteriores do próprio grupo devem ser feitas na terceira pessoa (ex: *"In prior work, Souza et al. [21] evaluated feature selection..."*).
- **Folha de Rosto Separada (`titlepage.tex`)**:
  - Enviada separadamente no sistema de submissão (*Editorial Manager*).
  - Contém: Título completo, lista dos 9 autores com ORCIDs de 16 dígitos, afiliações institucionais completas, e-mail dos autores correspondentes e declaração formal de apoio financeiro (*Acknowledgments* para FAPERGS, CNPq, UniRV).

### 1.3. Abstract & Keywords
- **Abstract**: **150 a 250 palavras** em parágrafo único sem citações nem abreviações não definidas. Estruturado na sequência: *Contexto do Problema $\rightarrow$ Lacuna $\rightarrow$ Metodologia do Benchmark $\rightarrow$ Resultados Quantitativos Principais $\rightarrow$ Conclusão/Impacto*.
- **Keywords**: **4 a 6 palavras-chave** separadas por ponto central (`\cdot`), cobrindo: *Neural Networks, Machine Learning, Metaheuristic Optimization, Financial Forecasting, Intraday Trading, Benchmark*.

---

## Módulo 2: Macro-Estrutura Padrão dos Artigos do NCA

A estrutura de seções exigida pelo NCA para artigos de benchmark e inteligência computacional segue rigorosamente o seguinte encadeamento:

```text
Title: A Benchmark Study of Evolutionary and Swarm Intelligence Optimizers for Neural Intraday Trend Classification in Brazilian Futures Markets

Abstract & Keywords

1. Introduction
   1.1 Domain Motivation & High-Frequency Intraday Challenges
   1.2 Neural Networks & Hyperparameter Optimization Complexity
   1.3 Metaheuristic Optimizers as the Focus of Inquiry
   1.4 Literature Gaps & Synthesis of Open Issues (Table 1)
   1.5 Main Contributions (6 Bullet Points in Bold)
   1.6 Paper Organization

2. Related Work & Theoretical Background
   2.1 Technical Analysis Indicators & Financial Features
   2.2 Machine Learning in Financial Time-Series Forecasting
   2.3 Evolutionary and Swarm Intelligence Metaheuristics
   2.4 Representative Literature & Unmet Gaps (Table 1)

3. Data & Problem Formulation
   3.1 B3 Mini-Index Futures Dataset (5-min WIN)
   3.2 Information Gain Feature Selection
   3.3 Leakage-Free Sequential Temporal Split (60/20/20 Protocol)

4. Proposed Optimizer Benchmark Framework
   4.1 Multilayer Perceptron (MLP) Search Space Formulation (6D Space)
   4.2 Compound MCC-Driven Fitness Objective
   4.3 Equal Evaluation Budget Protocol (N_eval = 1,500)
   4.4 Formulations of Evaluated Optimizers (RS, GA, PSO, DE, GWO)
   4.5 Non-Parametric Statistical Significance Protocol

5. Experimental Results & Performance Benchmark
   5.1 Out-of-Sample Classification Metrics (Table 2: Mean ± Std, Bold for Best)
   5.2 Convergence Dynamics & Fitness Trajectories (Figure 2)
   5.3 Execution Time & Computational Efficiency Analysis
   5.4 Non-Parametric Hypothesis Testing (Table 3: p-values & Cohen's d)
   5.5 Financial Backtest & Transaction Cost Sensitivity (Table 4)

6. Discussion & Practical Implications
   6.1 Trade-off Analysis: Accuracy vs. Computational Overhead
   6.2 Robustness under Financial Noise & Regime Shifts
   6.3 Practical Guidelines for Algorithmic Trading Systems

7. Conclusion & Future Work
   7.1 Summary of Core Findings (3 Key Takeaways)
   7.2 Limitations & Future Research Directions (3 Future Avenues)

Declarations
   - Funding
   - Conflict of Interest / Competing Interests
   - Ethics Approval
   - Data and Code Availability
```

---

## Módulo 3: Padrões de Redação e Micro-Estrutura por Seção

### 1. Seção 1 — Introdução (*Introduction*)
- **Modelo Retórico CARS (5 Movimentos)**:
  - **Move 1 (Território)**: Iniciar direto na previsão de ativos de alta frequência (WIN 5-min) sem frases generalistas óbvias.
  - **Move 2 (Rede Neural)**: Explicar que a MLP aproxima funções complexas, mas que o ajuste de hiperparâmetros é um problema de otimização não-convexo e ruidoso.
  - **Move 3 (Meta-heurísticas)**: Apresentar os otimizadores estocásticos (evolutivos e enxames) como solução central.
  - **Move 4 (Lacuna e Open Issues)**: Apontar que a literatura usa apenas 1 otimizador fixo, não controla o orçamento ($N_{eval}$) e sofre de *data leakage*. Referenciar a **Table 1** e sintetizar 5 *open issues*.
  - **Move 5 (6 Contribuições)**: Apresentar a solução com 6 marcadores em negrito iniciando com verbos no presente (*"We conduct...", "We establish...", "We formulate...", "We apply...", "We analyze...", "We evaluate out-of-sample..."*).

### 2. Seção 2 — Trabalhos Relacionados (*Related Work*)
- **Construção da Tabela 1**: Obrigatoriamente incluir a **Table 1: Representative literature on optimizer-driven financial forecasting and their unmet limitations** com 4 colunas:
  - *Study (Author, Year)*
  - *Target Model & Domain*
  - *Optimization Technique*
  - *Unmet Limitations / Research Gaps*
- **Conexão com Periódicos do NCA**: Citar ativamente artigos recentes do NCA (2024–2026) para demonstrar alinhamento com a literatura do jornal.

### 3. Seção 3 — Dados e Protocolo Temporal (*Data & Temporal Protocol*)
- **Enfase na Isenção de Data Leakage**: Detalhar que os dados 5-min do WIN são divididos em ordem cronológica estrita **60% Treino / 20% Validação / 20% Teste**.
- Proibir categoricamente amostragem aleatória e *K-Fold Cross-Validation* em séries temporais.

### 4. Seção 4 — Metodologia e Otimizadores (*Methodology & Optimizers*)
- **Formulação Matemática Explicita**:
  - Descrever o espaço 6D do MLP: número de neurônios L1, L2, learning rate ($lr$), batch size, dropout e regularização L2 ($\alpha$).
  - Apresentar a equação da fitness composta:
    $$f(\boldsymbol{\theta}) = 0.60 \times \text{MCC}(\boldsymbol{\theta}) + 0.40 \times F_1(\boldsymbol{\theta})$$
  - Apresentar o pseudo-código e equações matemáticas dos 5 otimizadores (RS, GA, PSO, DE, GWO).
  - Definir o protocolo de orçamento idêntico: $N_{eval} = 1.500$ avaliações por seed.

### 5. Seção 5 — Resultados e Benchmark (*Results & Benchmark*)
- **Formatação de Tabelas**:
  - **Tabela 2 (Desempenho Preditivo)**: Colunas para Acurácia, F1-Score, MCC, AUC-ROC e Runtime. Linhas para os 5 otimizadores. Reportar $\text{Média} \pm \text{Desvio Padrão}$ e destacar a **melhor média em negrito**.
  - **Tabela 3 (Testes Estatísticos)**: Reportar valor da estatística de Wilcoxon, $p$-valor ajustado por Holm-Bonferroni e tamanho de efeito $d$ de Cohen.
  - **Tabela 4 (Backtest Financeiro)**: Retorno Líquido %, Índice Sharpe, Drawdown Máximo (MDD), Profit Factor e simulação de custos de corretagem/slippage.
- **Gráficos de Convergência**: Incluir gráfico de convergência temporal da fitness ao longo das avaliações para demonstrar o equilíbrio entre exploração e explotação.

### 6. Seção 6 e 7 — Discussão e Conclusão (*Discussion & Conclusion*)
- **Discussão**: Discutir o *trade-off* entre ganho preditivo/financeiro e custo de execução computacional.
- **Conclusão**: Sintetizar as 3 principais descobertas quantitativas e apontar 3 caminhos futuros claros.

---

## Módulo 4: Checklist de Validação do Artigo Antes da Submissão

- [ ] Manuscrito em `article/manuscript/main.tex` e `sections/` **100% anônimo**.
- [ ] Folha de rosto `titlepage.tex` completa com os 9 autores, ORCIDs, afiliações e agências de fomento.
- [ ] Classe LaTeX `sn-jnl.cls` com a opção `sn-mathphys-num`.
- [ ] Todas as tabelas utilizando `booktabs` e envoltas em `\resizebox{\linewidth}{!}{...}`.
- [ ] Resumo com 150 a 250 palavras e 4 a 6 palavras-chave.
- [ ] Tabela 1 de trabalhos relacionados e lacunas presente na Seção 2.
- [ ] Lista de 6 contribuições enumeradas em negrito presente na Seção 1.
- [ ] Orçamento idêntico $N_{eval} = 1.500$ e divisão 60/20/20 temporal estrita rigorosamente explicados.
- [ ] Compilação sem erros no MiKTeX gerando `main.pdf` e `titlepage.pdf`.
