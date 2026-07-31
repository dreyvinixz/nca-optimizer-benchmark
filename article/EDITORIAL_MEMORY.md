# EDITORIAL MEMORY — Scientific Decision Log
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/EDITORIAL_MEMORY.md`  

---

## 1. Purpose of Editorial Memory

The Editorial Memory records all binding scientific, methodological, and terminology decisions established for the project. **No future AI agent or collaborator may alter these decisions without explicit user approval**, ensuring total manuscript consistency.

---

## 2. Binding Scientific & Editorial Decisions

### DECISION 001: Compound MCC-Driven Objective as Primary Validation Metric
- **Decision**: Use $f(\boldsymbol{\theta}) = 0.60 \times \text{MCC} + 0.40 \times F_1$ as the primary fitness objective.
- **Rationale**: Raw accuracy and cross-entropy loss are distorted by intraday class imbalances. Matthews Correlation Coefficient (MCC) treats true positives, true negatives, false positives, and false negatives symmetrically, providing a robust optimization target.
- **Enforcement**: Applied across `config/experiment_config.yaml`, `src/objective.py`, and all manuscript tables.

---

### DECISION 002: Strict Prohibition of Unhedged State-of-the-Art (SOTA) Claims
- **Decision**: Never claim "state-of-the-art performance" or "universal optimizer superiority".
- **Rationale**: Empirical evidence supports superiority only within the evaluated equal-budget constraint ($N_{\text{eval}} = 1,500$), 6D MLP search space, and 5-minute WIN futures dataset.
- **Enforcement**: All performance claims must include boundary qualifiers (*"under the evaluated equal-budget constraint..."*).

---

### DECISION 003: Random Search as the Mandatory Baseline Sampler
- **Decision**: Random Search (RS) must always be included as Baseline 1 in every table, figure, and comparative discussion.
- **Rationale**: Random Search proves whether guided metaheuristics (GA, PSO, DE, GWO) extract real search efficiency beyond unguided uniform sampling.
- **Enforcement**: `Random Search` must appear as column/row 1 in Tables 2, 3, 4 and Figure 2.

---

### DECISION 004: Equal Evaluation Budget as the Comparison Unit
- **Decision**: All five optimizers must be compared strictly under an identical number of fitness evaluations ($N_{\text{eval}} = 1,500$).
- **Rationale**: Comparing GA by generation count vs. PSO by iteration count is scientifically invalid. Fitness evaluation count is the single universal unit of computational effort.
- **Enforcement**: $N_{\text{eval}}$ is the x-axis for all convergence plots in Figure 2.

---

### DECISION 005: Absolute Double-Blind Anonymity Compliance
- **Decision**: All files under `article/manuscript/sections/` and `article/manuscript/main.tex` must remain 100% anonymized.
- **Rationale**: *Neural Computing and Applications* enforces double-blind peer review. Mentioning author names, e-mails, universities, or grant numbers in the main text causes immediate desk rejection.
- **Enforcement**: Author metadata, ORCIDs, and grant codes reside exclusively in `article/manuscript/titlepage.tex`.

---

### DECISION 006: Chronological 60/20/20 Sequential Temporal Split Protocol
- **Decision**: The main dataset must be split sequentially in chronological order (60% Train / 20% Validation / 20% Test) with `shuffle = false`.
- **Rationale**: Randomized K-fold cross-validation breaks time series ordering, leaking future price information into the past.
- **Enforcement**: Enforced in `config/experiment_config.yaml` and `src/temporal_split.py`.

---

### DECISION 007: Standardized Optimizer Nomenclature & Parameterization
- **Decision**: Optimizers must be named consistently as: `Random Search (RS)`, `Genetic Algorithm (GA)`, `Particle Swarm Optimization (PSO)`, `Differential Evolution (DE)`, and `Grey Wolf Optimizer (GWO)`.
- **Rationale**: Maintains terminology uniformity across text, code, tables, and figures.
- **Enforcement**: Validated against `NCA_WRITING_DNA.md`.

---

### DECISION 008: Dual Reporting of Statistical Significance and Effect Size
- **Decision**: Statistical testing must report both the inferential $p$-value (Wilcoxon-Holm) and the descriptive effect size (Cohen's $d$).
- **Rationale**: $p$-values alone do not quantify the practical magnitude of performance gains. Large effect sizes ($d > 0.80$) demonstrate real-world impact.
- **Enforcement**: Table 3 must report both $p$-value and Cohen's $d$ columns.

---

### DECISION 009: Integration of Financial Backtesting under Realistic Costs
- **Decision**: Every tuned model must be evaluated in an out-of-sample trading simulation measuring Net Return %, Sharpe Ratio, Maximum Drawdown (MDD %), and transaction fee sensitivity.
- **Rationale**: Addresses IJCNN reviewer rejection point regarding the disconnect between machine learning metrics and financial trading utility.
- **Enforcement**: Table 4 reports economic metrics under 0.00%, 0.01%, and 0.02% transaction fee tiers.

---

### DECISION 010: Adoption of the 9-Step Scientific Iteration Cycle
- **Decision**: All manuscript editing and drafting must proceed through the 9-step scientific iteration cycle:
  `1. Planning` $\rightarrow$ `2. Evidence Verification` $\rightarrow$ `3. First Draft` $\rightarrow$ `4. Reasoning Review` $\rightarrow$ `5. Writing Review` $\rightarrow$ `6. Technical Review` $\rightarrow$ `7. Editorial Review` $\rightarrow$ `8. Reviewer Simulation` $\rightarrow$ `9. Final Version`.
- **Rationale**: Ensures text generation is preceded by cognitive planning and followed by multi-layered quality control.
- **Enforcement**: Integrated into `.agents/AGENTS.md` and project workflow.
