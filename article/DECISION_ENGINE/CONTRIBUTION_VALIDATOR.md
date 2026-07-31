# CONTRIBUTION VALIDATOR — Anti-Artificial Contribution Matrix
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/DECISION_ENGINE/CONTRIBUTION_VALIDATOR.md`  

---

## 1. Deconstruction of Proposed Contributions

To prevent artificial, padded, or weak contribution lists, every bullet point in Section 1 must be validated through the 6-tier deconstruction matrix.

```
Contribution
    ↓
Problem Solved
    ↓
Why Unsolved by Prior Work?
    ↓
Repository Evidence
    ↓
Literature Evidence
    ↓
Reviewer Criticism Addressed
    ↓
Strength of Novelty (Methodological / Experimental)
```

---

## 2. 6-Tier Contribution Validation Matrix

### Contribution 1: Equal-Budget Metaheuristic Benchmark
- **Problem Solved**: Eliminates computational budget inequality bias in evolutionary neural tuning.
- **Why Unsolved by Prior Work**: Prior papers compare algorithms under unequal iteration counts, masking whether gains stem from search mechanics or excessive sampling.
- **Repository Evidence**: `config/experiment_config.yaml:L61-L67` ($N_{\text{eval}} = 1,500$ cap across all 5 algorithms).
- **Literature Evidence**: Rajwar et al. (2023), Dhingra et al. (NCA 2025).
- **Reviewer Criticism Addressed**: IJCNN Reviewer 1 & 2 ("Lack of fair optimizer budget comparison").
- **Novelty Strength**: **Methodological (Level 2)**

---

### Contribution 2: Leakage-Free Sequential Temporal Validation Protocol
- **Problem Solved**: Eliminates temporal data leakage caused by random cross-validation on time series.
- **Why Unsolved by Prior Work**: Published studies apply randomized $K$-fold splits, leaking future price information into training sets.
- **Repository Evidence**: `src/temporal_split.py`, `config/experiment_config.yaml:L15-L21` (`shuffle = false`, 60/20/20 split).
- **Literature Evidence**: Souza et al. (2026 IJCNN Review), Makridakis et al. (2018).
- **Reviewer Criticism Addressed**: IJCNN Reviewer 3 ("Data leakage and temporal validation concerns").
- **Novelty Strength**: **Experimental / Protocol (Level 3)**

---

### Contribution 3: Compound MCC-Driven Objective Formulation
- **Problem Solved**: Resists class imbalance distortion and penalizes false directional signals.
- **Why Unsolved by Prior Work**: Prior work relies on raw accuracy or cross-entropy loss, which fail under minor class imbalance.
- **Repository Evidence**: `src/objective.py` ($f(\boldsymbol{\theta}) = 0.60\text{MCC} + 0.40F_1$).
- **Literature Evidence**: Chicco & Jurman (2020).
- **Reviewer Criticism Addressed**: IJCNN Reviewer 4 ("Excessive reliance on raw accuracy").
- **Novelty Strength**: **Methodological (Level 2)**

---

### Contribution 4: Non-Parametric Statistical Hypothesis Validation
- **Problem Solved**: Provides statistical rigor confirming performance differences are non-random.
- **Why Unsolved by Prior Work**: Most papers report simple point metrics without hypothesis testing or effect sizes.
- **Repository Evidence**: `scripts/08_run_statistical_tests.py`, `outputs/statistical_tests/`.
- **Literature Evidence**: Demsar (2006), Garcia & Herrera (2008).
- **Reviewer Criticism Addressed**: IJCNN Reviewer 2 ("Absence of statistical significance testing").
- **Novelty Strength**: **Methodological (Level 2)**

---

### Contribution 5: Convergence Dynamics & Execution Overhead Analysis
- **Problem Solved**: Quantifies the real-world trade-off between search efficiency gains and computational execution time.
- **Why Unsolved by Prior Work**: Prior work ignores execution runtime overhead.
- **Repository Evidence**: `outputs/metrics/runtime_analysis.csv` ($3.35\text{ s}$ to $3.58\text{ s}$ per run).
- **Literature Evidence**: Gad (2022), Mirjalili et al. (2020).
- **Reviewer Criticism Addressed**: NCA Reviewer Profile ("Runtime and convergence efficiency").
- **Novelty Strength**: **Experimental (Level 3)**

---

### Contribution 6: Out-of-Sample Financial Backtesting & Cost Sensitivity
- **Problem Solved**: Bridges machine learning classification metrics with real-world trading profitability.
- **Why Unsolved by Prior Work**: Published studies stop at classification metrics without financial evaluation under transaction fees.
- **Repository Evidence**: `src/evaluation/backtest.py`, `outputs/backtests/financial_backtest_results.csv` (18.4% Net Return, Sharpe 1.42).
- **Literature Evidence**: Henrique et al. (2019), Souza et al. (2025 ICCSA).
- **Reviewer Criticism Addressed**: IJCNN Reviewer 1 ("Lack of financial/economic evaluation").
- **Novelty Strength**: **Experimental / Domain (Level 3)**
