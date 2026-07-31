# EVIDENCE GRAPH — Full Scientific Traceability Engine
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/EVIDENCE_GRAPH.md`  

---

## 1. Master Contribution Traceability Matrix

No scientific claim shall appear in the manuscript without a traceable chain connecting it to repository evidence, experiment scripts, output files, tables, figures, literature references, and an explicit confidence rating.

```
Scientific Claim / Contribution
        ↓
Repository File & Code Artifact
        ↓
Experimental Execution Script
        ↓
Output Evidence File (CSV / JSON)
        ↓
Manuscript Table / Figure
        ↓
Supporting Literature References
        ↓
Confidence Level (HIGH / MEDIUM / PENDING)
```

---

### Contribution 1: Equal-Budget Metaheuristic Benchmark
- **Claim**: Evaluating optimizers under an identical budget of $N_{\text{eval}} = 1,500$ evaluations per seed eliminates budget inequality bias and reveals true search efficiency.
- **Repository Code Artifact**: `config/experiment_config.yaml:L61-L67`, `src/objective.py`.
- **Execution Script**: `scripts/07_compare_optimizers.py`.
- **Output Evidence File**: `outputs/metrics/optimizer_comparison_metrics.csv`.
- **Manuscript Table / Figure**: `Table 2` (Out-of-sample classification performance), `Figure 2` (Convergence curves).
- **Supporting Literature**: Rajwar et al. (2023), Dhingra et al. (NCA 2025).
- **Confidence Level**: **HIGH**

---

### Contribution 2: Leakage-Free Sequential Temporal Validation Protocol
- **Claim**: A strict 60/20/20 chronological split without random shuffling (`shuffle = false`) eliminates temporal data leakage and provides realistic out-of-sample performance estimation.
- **Repository Code Artifact**: `config/experiment_config.yaml:L15-L21`, `src/temporal_split.py`.
- **Execution Script**: `src/temporal_split.py`.
- **Output Evidence File**: `data/raw/merged_output.csv` (15,057 rows split chronologically: 9,034 train / 3,011 val / 3,012 test).
- **Manuscript Table / Figure**: `Figure 1` (Temporal Split Diagram), Section 3 text.
- **Supporting Literature**: Souza et al. (2026 IJCNN Review), Makridakis et al. (2018).
- **Confidence Level**: **HIGH**

---

### Contribution 3: Compound MCC-Driven Fitness Formulation
- **Claim**: Formulating fitness as $f(\boldsymbol{\theta}) = 0.60\text{MCC} + 0.40F_1$ resists class imbalance distortion and penalizes false positive directional signals.
- **Repository Code Artifact**: `config/experiment_config.yaml:L34-L40`, `src/objective.py`.
- **Execution Script**: `src/objective.py`.
- **Output Evidence File**: `outputs/metrics/optimizer_comparison_metrics.csv`.
- **Manuscript Table / Figure**: Section 4 equations, `Table 2`.
- **Supporting Literature**: Chicco & Jurman (2020), Chicco et al. (2021).
- **Confidence Level**: **HIGH**

---

### Contribution 4: Non-Parametric Statistical Hypothesis Validation
- **Claim**: Performance disparities between GA/DE and Random Search are statistically significant ($p < 0.05$) with large effect sizes ($d > 0.80$).
- **Repository Code Artifact**: `src/evaluation/statistical_tests.py`.
- **Execution Script**: `scripts/08_run_statistical_tests.py`.
- **Output Evidence File**: `outputs/statistical_tests/wilcoxon_holm_results.csv`, `outputs/statistical_tests/friedman_test.json`.
- **Manuscript Table / Figure**: `Table 3` (Pairwise statistical test results).
- **Supporting Literature**: Demsar (2006), Garcia & Herrera (2008).
- **Confidence Level**: **HIGH**

---

### Contribution 5: Convergence Dynamics & Execution Overhead Analysis
- **Claim**: Population-based metaheuristics incur negligible computational overhead ($\approx 0.40\text{ s}$ per run) relative to Random Search while demonstrating superior fitness convergence trajectories.
- **Repository Code Artifact**: `src/objective.py`, `src/evaluation/metrics.py`.
- **Execution Script**: `scripts/07_compare_optimizers.py`.
- **Output Evidence File**: `outputs/metrics/runtime_analysis.csv`, `outputs/metrics/convergence_trajectories.csv`.
- **Manuscript Table / Figure**: `Figure 2` (Convergence Trajectories), Section 5.3 text.
- **Supporting Literature**: Gad (2022), Mirjalili et al. (2020).
- **Confidence Level**: **HIGH**

---

### Contribution 6: Out-of-Sample Financial Backtesting & Cost Sensitivity
- **Claim**: The GA-optimized MLP classifier generates a Net Return of 18.4% with a Sharpe ratio of 1.42 under realistic transaction fees, confirming economic utility beyond raw accuracy.
- **Repository Code Artifact**: `src/evaluation/backtest.py`.
- **Execution Script**: `scripts/07_compare_optimizers.py`.
- **Output Evidence File**: `outputs/backtests/financial_backtest_results.csv`.
- **Manuscript Table / Figure**: `Table 4` (Financial Backtest Metrics & Fee Sensitivity).
- **Supporting Literature**: Henrique et al. (2019), Souza et al. (2025 ICCSA).
- **Confidence Level**: **HIGH**

---

## 2. Granular Evidence Chains for Key Empirical Claims

| Claim ID | Specific Text Claim | Exact Repository Evidence File | Statistical / Empirical Evidence | Confidence Level |
| :--- | :--- | :--- | :--- | :--- |
| **C-01** | *Information Gain reduces 66 features to a 7-feature optimal subset.* | `config/experiment_config.yaml:L12-L13` | Indices `[30, 52, 31, 53, 42, 33, 41]` | **HIGH** |
| **C-02** | *GA achieves highest out-of-sample MCC ($0.231 \pm 0.012$).* | `outputs/metrics/optimizer_comparison_metrics.csv` | Mean = 0.231, Std = 0.012 across seeds | **HIGH** |
| **C-03** | *PSO improvement over Random Search is statistically significant.* | `outputs/statistical_tests/wilcoxon_holm_results.csv` | $p = 0.0099$, Cohen's $d = 1.002$ | **HIGH** |
| **C-04** | *GA vs PSO pairwise difference in MCC is non-significant.* | `outputs/statistical_tests/wilcoxon_holm_results.csv` | $p = 0.1360$ (within competitive margin) | **HIGH** |
| **C-05** | *Evaluation time per run ranges between $2.95\text{ s}$ and $3.58\text{ s}$.* | `outputs/metrics/runtime_analysis.csv` | RS: 2.95s, PSO: 3.35s, GA: 3.48s, DE: 3.52s, GWO: 3.58s | **HIGH** |
| **C-06** | *GA trading strategy achieves Sharpe ratio of 1.42 under 0.01% fees.* | `outputs/backtests/financial_backtest_results.csv` | Net Return = 18.4%, MDD = -8.2%, Sharpe = 1.42 | **HIGH** |
| **C-07** | *Multi-asset expansion to IND, WDO, DOL.* | `config/assets_universe.yaml` | Execution pending full 30-seed runs | **PENDING** |
