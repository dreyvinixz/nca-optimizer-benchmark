# Processo de Revisão Linguística e Estilística Comparativa (Escrita Humana vs. Manuscrito)

Este documento documenta o **processo explícito de revisão comparativa**, contrastando os trechos do nosso manuscrito (`sections/introduction.tex`) diretamente contra a sintaxe e retórica de autores humanos publicados em artigos de alto impacto do **Neural Computing and Applications (NCA)**, **PLoS ONE** e **Springer**.

---

## Parágrafo 1: Abertura e Motivação do Domínio

### Texto Original (Antes da Revisão):
> *"Financial asset price forecasting in high-frequency intraday environments represents one of the most challenging applications of computational intelligence [Ref]. Modern derivatives markets, such as the Mini-Index futures contract (WIN)... exhibit extreme trading velocity... However, the dynamic adaptation of market dynamics rapidly dissipates predictive patterns, posing severe obstacles to standard econometric methods."*

### Crítica de Escrita Humana (Diagnóstico):
1. **Redundância Tautológica**: *"dynamic adaptation of market dynamics"* é um vício de repetição artificial não encontrado em textos humanos.
2. **Falta de Especificidade Econômica**: Autores humanos no NCA (como Billah et al. 2024 e Makridakis et al. 2018) explicam a decadência de padrões usando termos do mercado (*arbitrage*, *microstructure noise*, *decaying temporal dependencies*).

### Padrão Extraído dos Autores Humanos:
- **Dhingra et al. (NCA 2025)**: *"However, the inherent intermittency and variability... pose substantial challenges to reliable grid integration..."*
- **Makridakis et al. (2018)**: *"Scant empirical evidence is available about... as competitive pressures alter series behavior across short horizons."*

### Texto Humano Reescrito (Final em `sections/introduction.tex`):
> *"Financial asset price forecasting in high-frequency intraday environments represents one of the most challenging applications of computational intelligence \cite{billah2024nca_moving_average}. Modern derivatives markets, such as the Mini-Index futures contract (WIN) listed on the Brazilian Stock Exchange (B3), exhibit extreme trading velocity, severe non-stationarity, rapid regime transitions, and low signal-to-noise ratios \cite{cardoso2022bovdb, souza2025iccsa}. Market participants operating within sub-hourly execution horizons (e.g., 5-minute intervals) require automated models capable of extracting persistent directional signals amidst market microstructure noise \cite{henrique2019stock_review}. However, continuous arbitrage and adaptive trading behavior rapidly erode short-term price inefficiencies, causing temporal dependencies to decay quickly over short execution horizons and rendering static econometric models ineffective."*

---

## Parágrafo 2: Transição para a Rede Neural e Complexidade dos Hiperparâmetros

### Padrão Extraído dos Autores Humanos:
- **Dhingra et al. (NCA 2025)**: *"While these neural networks inherently possess the architecture needed... their performance is significantly influenced by the optimization algorithms used during the training phase. Optimizers are critical components that control weight updates..."*
- **Bischl et al. (WIREs 2023)**: *"Because loss surfaces over hyperparameter spaces are non-convex, discontinuous, and noisy, gradient-based methods cannot be applied..."*

### Texto Humano Reescrito:
> *"To capture these intricate non-linear price behaviors, machine learning models—particularly Multilayer Perceptrons (MLPs)—have been widely adopted due to their universal function approximation capabilities \cite{ecer2020mlp_ga_pso}. Although gradient-based backpropagation effectively optimizes internal network weights during training, overall generalization hinges on identifying an optimal hyperparameter configuration \cite{chung2018ga_lstm}. Parameters such as layer depth, neuron counts, learning rates, regularizers, and dropout probabilities jointly define a high-dimensional, mixed discrete-continuous search space. Because the resulting loss surface is non-convex, discontinuous, and contaminated by financial noise, traditional gradient methods cannot be applied to hyperparameter selection, while exhaustive grid search quickly becomes computationally prohibitive \cite{gad2022pso_comprehensive, rajwar2023exhaustive_review}."*

---

## Parágrafo 4 & Lista: Formatação das Lacunas (*Research Gaps*) e Contribuições

### Padrão Extraído dos Autores Humanos:
- **Makridakis et al. (2018)**: *"Published claims are characterized by the following three major limitations: 1... 2... 3..."*
- **Dhingra et al. (NCA 2025)**: *"Table 1 offers a structured synopsis... explicitly flagging the specific limitations... A synthesis of the studies reveals five open issues... Addressing these gaps, we focus on..."*

### Texto Humano Reescrito (Lista de Lacunas):
> *"Despite widespread interest in evolutionary machine learning, a critical methodological limitation persists in the literature: most existing financial studies evaluate a single, arbitrarily selected optimizer—typically a standard GA or basic PSO—without conducting controlled benchmarks against alternative metaheuristic paradigms \cite{dhingra2025solar}. Furthermore, published evaluations frequently suffer from three pervasive flaws:
> 1. Evaluation Budget Inequality...
> 2. Temporal Data Leakage...
> 3. Classification and Economic Disconnect..."*

---

## Resumo dos Critérios de Excelência da Escrita Humana Aplicados

1. **Eliminação Total de Tautologias**: Remoção de termos repetidos em um mesmo período.
2. **Precisão Terminológica**: Emprego de termos consolidados em computação quantitativa (*exploration-exploitation trade-off*, *non-convex loss surface*, *microstructure noise*, *arbitrage erosion*).
3. **Fluidez dos Conectivos**: Uso de conectivos formais (*"Crucially"*, *"Addressing these open issues"*, *"Despite widespread interest"*, *"Although gradient-based backpropagation..."*).
