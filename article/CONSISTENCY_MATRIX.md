# CONSISTENCY MATRIX — Cross-Section Traceability
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/CONSISTENCY_MATRIX.md`  

---

## 1. Cross-Section Contribution Consistency Matrix

Every contribution listed in Section 1 MUST be explicitly verified across all sections of the paper.

| Contribution | Intro (Sec 1) | RelWork (Sec 2) | Data (Sec 3) | Method (Sec 4) | Results (Sec 5) | Discuss (Sec 6) | Concl (Sec 7) | Consistency Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Equal-Budget Benchmark ($N_{\text{eval}}=1,500$)** | ✓ | ✓ | N/A | ✓ (Sec 4.3) | ✓ (Sec 5.1–5.2) | ✓ (Sec 6.1) | ✓ (Sec 7.1) | **VERIFIED** |
| **2. Leakage-Free Temporal Protocol (60/20/20)** | ✓ | ✓ | ✓ (Sec 3.3) | ✓ (Sec 4.3) | ✓ (Sec 5.1) | ✓ (Sec 6.2) | ✓ (Sec 7.1) | **VERIFIED** |
| **3. Compound MCC-Driven Fitness ($0.60\text{MCC}+0.40F_1$)** | ✓ | ✓ | N/A | ✓ (Sec 4.2) | ✓ (Sec 5.1) | ✓ (Sec 6.1) | ✓ (Sec 7.1) | **VERIFIED** |
| **4. Non-Parametric Statistical Validation** | ✓ | N/A | N/A | ✓ (Sec 4.5) | ✓ (Sec 5.4) | ✓ (Sec 6.1) | ✓ (Sec 7.1) | **VERIFIED** |
| **5. Convergence & Runtime Overhead Analysis** | ✓ | N/A | N/A | ✓ (Sec 4.3) | ✓ (Sec 5.2–5.3) | ✓ (Sec 6.2) | ✓ (Sec 7.1) | **VERIFIED** |
| **6. Out-of-Sample Financial Backtesting** | ✓ | ✓ | N/A | ✓ (Sec 4.5) | ✓ (Sec 5.5) | ✓ (Sec 6.3) | ✓ (Sec 7.1) | **VERIFIED** |

---

## 2. Table and Figure Verification Matrix

| Element | Mentioned in Text | Defined in TeX | Generated in Output | Cited in Captions | Consistency Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Table 1** (Literature Gap Matrix) | Sec 1.4, Sec 2.4 | `related_work.tex` | N/A (Textual) | `related_work.tex` | **VERIFIED** |
| **Table 2** (Predictive Metrics $\text{Mean}\pm\text{Std}$) | Sec 5.1 | `results.tex` | `optimizer_comparison_metrics.csv` | `results.tex` | **VERIFIED** |
| **Table 3** (Statistical Test $p$-values & Cohen's $d$) | Sec 5.4 | `results.tex` | `wilcoxon_holm_results.csv` | `results.tex` | **VERIFIED** |
| **Table 4** (Financial Backtest & Cost Sensitivity) | Sec 5.5 | `results.tex` | `financial_backtest_results.csv` | `results.tex` | **VERIFIED** |
| **Figure 1** (Temporal Split Diagram) | Sec 3.3 | `data.tex` | `figures/temporal_split.pdf` | `data.tex` | **VERIFIED** |
| **Figure 2** (Convergence Curves over $N_{\text{eval}}$) | Sec 5.2 | `results.tex` | `figures/convergence_curves.pdf` | `results.tex` | **VERIFIED** |
