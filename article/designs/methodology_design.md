# SECTION DESIGN — Section 4: Methodology & Benchmark Framework
**Mission ID**: MISSION 08A  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/designs/methodology_design.md`  

---

## 1. Section Metadata & Scope

- **Section Title**: Proposed Optimizer Benchmark Framework (`\section{Proposed Optimizer Benchmark Framework}`)
- **Scientific Objective**: Formalize the 6D MLP hyperparameter search space, the compound MCC-driven objective function, the equal evaluation budget protocol ($N_{\text{eval}}=1,500$), the update equations for 5 optimizers, non-parametric statistical tests, and the financial backtest simulator.
- **Peer-Review Goal**: Satisfy Reviewer 1 (Methodological Rigorist) and Reviewer 2 (Statistician) by establishing absolute mathematical clarity, zero evaluation budget bias, and full reproducibility.

---

## 2. Subsection Breakdown & Structural Plan

### Subsection 4.1: Multilayer Perceptron Search Space Formulation (`sec:search_space`)
- **Objective**: Define the 6-dimensional mixed discrete-continuous search space $\boldsymbol{\Theta} \subset \mathbb{R}^6$ for the MLP classifier.
- **Repository Evidence**: [`config/search_spaces.yaml:L1-L7`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/search_spaces.yaml#L1-L7), [`config/experiment_config.yaml:L22-L33`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L22-L33).
- **Equations**:
  - Search Space Vector: $\boldsymbol{\theta} = [N_{L1}, N_{L2}, \eta, \alpha, p_{\text{drop}}, B]$.
  - Bounds: $N_{L1} \in [16, 256]$, $N_{L2} \in [0, 128]$, $\eta \in [10^{-4}, 10^{-1}]$ ($\log_{10}$), $\alpha \in [10^{-6}, 10^{-2}]$ ($\log_{10}$), $p_{\text{drop}} \in [0.0, 0.50]$, $B \in \{32, 64, 128, 256\}$.
- **Tables**: Table of hyperparameter search space boundaries.
- **References**: Ecer et al. (2020), Chung et al. (2018).
- **Reviewer Concerns Solved**: Clarifies search boundaries and parameter types (discrete vs. continuous).

---

### Subsection 4.2: Compound MCC-Driven Fitness Formulation (`sec:fitness`)
- **Objective**: Formulate the compound objective function $f(\boldsymbol{\theta}) = 0.60\text{MCC} + 0.40F_1$.
- **Repository Evidence**: [`config/experiment_config.yaml:L34-L40`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L34-L40), [`src/objective.py`](file:///c:/mysystems/projects/nca-optimizer-benchmark/src/objective.py).
- **Equations**:
  - Fitness: $f(\boldsymbol{\theta}) = 0.60 \times \text{MCC}(\boldsymbol{\theta}) + 0.40 \times F_1(\boldsymbol{\theta})$.
  - MCC: $\text{MCC} = \frac{TP \times TN - FP \times FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$.
- **References**: Chicco & Jurman (2020), Chicco et al. (2021).
- **Reviewer Concerns Solved**: Explains why accuracy is inadequate under intraday class imbalance and how MCC penalizes false positives.

---

### Subsection 4.3: Equal Evaluation Budget Protocol (`sec:budget`)
- **Objective**: Formalize the budget cap constraint ($N_{\text{eval}} = 1,500$) across 20 stochastic seeds.
- **Repository Evidence**: [`config/experiment_config.yaml:L61-L67`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L61-L67), [`article/EDITORIAL_MEMORY.md:DECISION 004`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/EDITORIAL_MEMORY.md).
- **Equations**:
  - Budget Unit: $N_{\text{eval}} = N_{\text{pop}} \times T = 15 \times 100 = 1,500$.
- **References**: Rajwar et al. (2023), Dhingra et al. (NCA 2025).
- **Reviewer Concerns Solved**: Eliminates budget inequality bias (Reviewer 1 key concern).

---

### Subsection 4.4: Mathematical Formulations of Evaluated Optimizers (`sec:optimizers`)
- **Objective**: Provide explicit mathematical update equations for Random Search (RS), GA, PSO, DE, and GWO.
- **Repository Evidence**: [`config/experiment_config.yaml:L68-L86`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L68-L86).
- **Equations**:
  - RS: $\boldsymbol{\theta}_t \sim \mathcal{U}(\boldsymbol{\Theta}_{\text{min}}, \boldsymbol{\Theta}_{\text{max}})$.
  - GA: Uniform crossover $\boldsymbol{x}_i^{t+1} = \gamma \boldsymbol{x}_{\text{p1}}^t + (1-\gamma)\boldsymbol{x}_{\text{p2}}^t$, Gaussian mutation $\mathcal{N}(0, \sigma^2)$.
  - PSO: Velocity $\boldsymbol{v}_i^{t+1} = w\boldsymbol{v}_i^t + c_1 r_1 (\boldsymbol{p}_i - \boldsymbol{x}_i^t) + c_2 r_2 (\boldsymbol{g} - \boldsymbol{x}_i^t)$.
  - DE: Mutation $\boldsymbol{v}_i^t = \boldsymbol{x}_{\text{best}}^t + F(\boldsymbol{x}_{r1}^t - \boldsymbol{x}_{r2}^t)$, binomial crossover.
  - GWO: Leadership vector $\boldsymbol{x}_i^{t+1} = \frac{\boldsymbol{x}_1 + \boldsymbol{x}_2 + \boldsymbol{x}_3}{3}$.
- **References**: Goldberg (1989), Kennedy & Eberhart (1995), Storn & Price (1997), Mirjalili et al. (2014), Bergstra & Bengio (2012).
- **Reviewer Concerns Solved**: Demonstrates complete mathematical transparency for all 5 optimizers.

---

### Subsection 4.5: Statistical Hypothesis Testing Protocol (`sec:stats_protocol`)
- **Objective**: Define non-parametric Friedman test, post-hoc Wilcoxon signed-rank test with Holm-Bonferroni correction, and Cohen's $d$ effect sizes.
- **Repository Evidence**: `src/evaluation/statistical_tests.py`.
- **Equations**:
  - Cohen's $d$: $d = \frac{\bar{x}_1 - \bar{x}_2}{s_{\text{pooled}}}$.
- **References**: Demsar (2006), Garcia & Herrera (2008).
- **Reviewer Concerns Solved**: Satisfies Reviewer 2 (Statistician) requirements.

---

### Subsection 4.6: Financial Backtest Simulator & Cost Sensitivity (`sec:backtest_protocol`)
- **Objective**: Define trading signal generation, net period return, brokerage fees, and transaction cost sensitivity tiers ($0.00\%, 0.01\%, 0.02\%$).
- **Repository Evidence**: `src/evaluation/backtest.py`.
- **Equations**:
  - Signal: $S_k = +1$ if $\hat{p}_k \ge 0.50$ else $-1$.
  - Net Return: $R_{\text{net}, k} = S_k \cdot r_k - |S_k - S_{k-1}| \cdot c_{\text{fee}}$.
- **References**: Henrique et al. (2019), Souza et al. (2025 ICCSA).
- **Reviewer Concerns Solved**: Satisfies Reviewer 3 (Financial Specialist) requirements.

---

## 3. Verification & Approval Status

- [x] All claims verified against `PROJECT_MEMORY.md` and `EVIDENCE_GRAPH.md`.
- [x] All 5 optimizers mathematically formulated.
- [x] Search space 6D parameters bounded and explicit.
- [x] Zero unhedged SOTA claims.
- **DESIGN APPROVED FOR WRITING MISSION 08B**.
