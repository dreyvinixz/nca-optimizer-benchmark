# Análise Comparativa das Introduções — Referências & Periódicos NCA

Este documento reúne o estudo comparativo das introduções dos principais artigos de referência do projeto e sintetiza as **regras de ouro de escrita** para o journal **Neural Computing and Applications (NCA)**.

---

## 1. Síntese dos Padrões Encontrados por Dimensão Textual

### Dimensão A: Frases de Abertura (*The Opening Hook*)
- **O que funciona no NCA**:
  - Começar conectando a **complexidade matemática do problema** com a **necessidade prática do mundo real**.
  - Evitar generalidades históricas ou óbvias (ex: "O mercado financeiro é muito antigo...").
  - *Exemplo NCA Benchmark*: *"Financial asset price forecasting in high-frequency intraday environments represents one of the most challenging applications of computational intelligence, characterized by severe non-stationarity, regime switches, and low signal-to-noise ratios."*

### Dimensão B: Articulação da Lacuna de Pesquisa (*The Research Gap*)
- **O que funciona no NCA**:
  - Denunciar que a literatura atual foca quase exclusivamente na arquitetura neural (número de camadas/neurônios) e negligencia a **meta-heurística de otimização dos hiperparâmetros**.
  - Apontar que estudos anteriores usam apenas 1 otimizador padrão (como GA ou Grid Search) sem comparação pareada sob **orçamento idêntico de avaliações ($N_{eval}$)**.
  - Usar expressões de contraste técnico: *"While neural networks possess strong function approximation capabilities, their generalization relies heavily on hyperparameter configuration. However, prior studies overwhelmingly adopt single, default optimizers without comparative benchmarks under equal evaluation budgets..."*

### Dimensão C: Apresentação das Contribuições (*Main Contributions*)
- **O que funciona no NCA**:
  - Apresentar uma lista numerada explicita de 5 a 6 itens com marcadores em negrito.
  - Cada item deve começar com um verbo de ação no presente (*"We conduct...", "We establish...", "We evaluate...", "We perform...", "We provide..."*).
  - *Exemplo*:
    1. **Controlled Equal-Budget Benchmark**: Conducted a systematic evaluation across 5 optimizers under an identical $N_{eval} = 1,500$ budget.
    2. **Leakage-Free Temporal Protocol**: Enforced strict chronological 60/20/20 train/val/test splits without random shuffling.
    3. **MCC-Driven Fitness Optimization**: Formulated a compound fitness objective mitigating class imbalance.
    4. **Non-Parametric Statistical Testing**: Applied Friedman and paired Wilcoxon tests with Holm-Bonferroni correction and Cohen's $d$.
    5. **Convergence & Runtime Analysis**: Evaluated exploration-exploitation dynamics and computational overhead.
    6. **Out-of-Sample Financial Backtesting**: Demonstrated real-world economic utility under transaction costs.

---

## 2. Excertos Textuais Analisados dos Artigos de Referência

### 2.1. NCA Solar Benchmark (Dhingra et al., 2025)
> *"While these neural networks inherently possess the architecture needed to model complex time-series data, their performance is significantly influenced by the optimization algorithms used during the training phase. Optimizers are critical components that control the weight update process, directly affecting convergence speed, model stability, and predictive accuracy... However, the comparative impact of different optimizers on neural networks for PV power forecasting remains underexplored in current literature... Table 1 offers a structured synopsis of the key studies and explicitly flags the specific limitations or research gaps each one leaves unaddressed..."*

### 2.2. Precursor IJCNN 2026 (Souza et al., 2026)
> *"The financial market is the arena for investing in various capital instruments traded to achieve economic returns and manage risk... Early attempts to standardize patterns used static, linear models... As finance and computing converged, machine learning gained popularity... However, the high dimensionality and redundancy challenge model training, making feature selection vital..."*
> **Diagnóstico de Ajuste para o NCA**: Substituir a abertura genérica por uma frase direta sobre previsão intraday de alta frequência e transformar a menção ao GA em uma investigação comparativa de 5 otimizadores.

---

## 3. Diretrizes Finais de Redação para a Introdução no NCA

1. **Primeiro Parágrafo**: Contextualizar o Mini-Índice WIN em barras de 5 minutos como um ambiente de teste de alta volatilidade para modelos neurais.
2. **Segundo Parágrafo**: Explicar o papel da rede MLP e por que a superfície de perda em hiperparâmetros é não-convexa e ruidosa.
3. **Terceiro Parágrafo**: Transitar para as meta-heurísticas de otimização (algoritmos evolutivos vs. inteligência de enxame).
4. **Quarto Parágrafo & Tabela 1**: Apresentar o estado da arte e denunciar as lacunas (falta de orçamento igual, *data leakage* e falta de validação financeira).
5. **Quinto Parágrafo & Lista**: Enumerar as 6 contribuições principais.
6. **Sexto Parágrafo**: Mapeamento da estrutura do artigo (*Section II presents... Section III describes...*).
