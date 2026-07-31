# MANUSCRIPT BLUEPRINT — Paragraph-by-Paragraph Blueprint
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/MANUSCRIPT_BLUEPRINT.md`  

---

## 1. Master Section & Paragraph Blueprint

This blueprint defines the paragraph-by-paragraph objective and required evidence sources for every section of the manuscript.

---

### SECTION 4: METHODOLOGY & BENCHMARK FRAMEWORK (Writing Order Step 1)

- **P1 Goal**: Formalize the 6D discrete-continuous hyperparameter search space $\boldsymbol{\theta}$.
  - *Evidence*: `config/search_spaces.yaml`, Table 2 (Search space bounds).
- **P2 Goal**: Formulate the compound MCC-driven objective function $f(\boldsymbol{\theta}) = 0.60\text{MCC} + 0.40F_1$.
  - *Evidence*: `config/experiment_config.yaml:L34-L40`, `src/objective.py`, Chicco & Jurman (2020).
- **P3 Goal**: Detail the equal evaluation budget constraint ($N_{\text{eval}} = 1,500$).
  - *Evidence*: `config/experiment_config.yaml:L61-L67`, Rajwar et al. (2023).
- **P4 Goal**: Mathematically formulate Random Search (RS) baseline mechanics.
  - *Evidence*: `src/optimizers/random_search.py`.
- **P5 Goal**: Mathematically formulate Genetic Algorithm (GA) recombination and mutation operators.
  - *Evidence*: `config/experiment_config.yaml:L68-L74`, Goldberg (1989), Holland (1992).
- **P6 Goal**: Mathematically formulate Particle Swarm Optimization (PSO) velocity and position updates.
  - *Evidence*: `config/experiment_config.yaml:L75-L78`, Kennedy & Eberhart (1995).
- **P7 Goal**: Mathematically formulate Differential Evolution (DE) `best/1/bin` mutation and crossover.
  - *Evidence*: `config/experiment_config.yaml:L79-L83`, Storn & Price (1997).
- **P8 Goal**: Mathematically formulate Grey Wolf Optimizer (GWO) alpha, beta, delta leadership hierarchy.
  - *Evidence*: `config/experiment_config.yaml:L84-L86`, Mirjalili et al. (2014).
- **P9 Goal**: Define non-parametric statistical hypothesis testing protocol (Friedman, Wilcoxon-Holm, Cohen's $d$).
  - *Evidence*: `src/evaluation/statistical_tests.py`, Demsar (2006).
- **P10 Goal**: Define out-of-sample trading backtest simulator and fee sensitivity framework.
  - *Evidence*: `src/evaluation/backtest.py`, Henrique et al. (2019).

---

### SECTION 5: EXPERIMENTAL RESULTS (Writing Order Step 2)

- **P1 Goal**: Present out-of-sample predictive classification performance across all 5 optimizers.
  - *Evidence*: `outputs/metrics/optimizer_comparison_metrics.csv`, Table 2 ($\text{Mean} \pm \text{Std}$).
- **P2 Goal**: Analyze convergence dynamics and fitness trajectories over $N_{\text{eval}} = 1,500$.
  - *Evidence*: `outputs/metrics/convergence_trajectories.csv`, Figure 2.
- **P3 Goal**: Analyze computational runtime overhead and execution efficiency.
  - *Evidence*: `outputs/metrics/runtime_analysis.csv` ($3.35\text{ s}$ to $3.58\text{ s}$).
- **P4 Goal**: Report non-parametric statistical hypothesis tests and effect sizes.
  - *Evidence*: `outputs/statistical_tests/wilcoxon_holm_results.csv`, Table 3 ($p$-values and Cohen's $d$).
- **P5 Goal**: Present out-of-sample financial backtesting and transaction cost sensitivity.
  - *Evidence*: `outputs/backtests/financial_backtest_results.csv`, Table 4 (Net Return, Sharpe, MDD).

---

### SECTION 6: DISCUSSION (Writing Order Step 3)

- **P1 Goal**: Interpret empirical performance gains through search space mechanics (GA/DE diversification vs. GWO exploitation).
  - *Evidence*: Results from Section 5, Gad (2022).
- **P2 Goal**: Discuss the trade-off between computational execution overhead and predictive/financial return.
  - *Evidence*: Section 5.3 runtime vs. Section 5.5 return.
- **P3 Goal**: Discuss robustness under intraday financial microstructure noise.
  - *Evidence*: `outputs/metrics/optimizer_comparison_metrics.csv` (Standard deviation across seeds).
- **P4 Goal**: Provide explicit recommendations for quantitative trading practitioners.
  - *Evidence*: Decision Engine recommendations.

---

### SECTION 1: INTRODUCTION (Writing Order Step 4)

- **P1 Goal**: High-frequency intraday domain motivation and market non-stationarity challenges.
  - *Evidence*: Billah et al. (NCA 2024), Cardoso et al. (2022).
- **P2 Goal**: Multilayer Perceptrons and non-convex hyperparameter search space complexity.
  - *Evidence*: Ecer et al. (2020), Chung et al. (2018).
- **P3 Goal**: Metaheuristic optimization algorithms as global search paradigms.
  - *Evidence*: Goldberg (1989), Mirjalili (2014).
- **P4 Goal**: Literature gap & articulation of 3 systemic flaws (budget inequality, data leakage, classification disconnect).
  - *Evidence*: Dhingra et al. (NCA 2025), Rajwar et al. (2023).
- **P5 Goal**: Proposed benchmark framework solution.
  - *Evidence*: `PROJECT_MEMORY.md`.
- **P6 Goal**: Deconstruction of 6 bulleted contributions in bold.
  - *Evidence*: `CONTRIBUTION_VALIDATOR.md`.
- **P7 Goal**: Structural section outline mapping Sections 2–7.
  - *Evidence*: Manuscript structure.

---

### ABSTRACT & CONCLUSION (Writing Order Steps 5 & 6)

- **Abstract Goal**: 150–250 word synthesis of Context $\rightarrow$ Problem $\rightarrow$ Method $\rightarrow$ Results $\rightarrow$ Conclusion.
- **Conclusion P1 Goal**: Synthesis of core 3 benchmark discoveries.
- **Conclusion P2 Goal**: 3 explicit future research directions.
