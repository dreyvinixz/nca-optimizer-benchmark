# TABLE PLANNER — Tabular Structure & Formatting Engine
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/DECISION_ENGINE/TABLE_PLANNER.md`  

---

## 1. Master Table Inventory & Necessity Audit

Tables serve as the quantitative core of an academic manuscript. To avoid redundancy with text or figures, every table must pass the Tabular Necessity Audit.

```
Table Candidate
    ↓
What Quantitative Question Does it Answer?
    ↓
Source Data File (CSV / JSON)
    ↓
Bolding & Formatting Rules (\toprule, \midrule, \bottomrule)
    ↓
Width Scaling (\resizebox{\linewidth}{!}{...})
```

---

## 2. Planned Table Specifications

### TABLE 1: Representative Literature & Unmet Limitations Matrix
- **Quantitative Question Answered**: *What are the specific methodological limitations of prior published studies?*
- **Necessity Rating**: **ESSENTIAL** (Foundation of literature gap in Section 2).
- **Columns**: `Study (Author, Year)` | `Target Model & Domain` | `Optimization Approach` | `Unmet Limitations / Research Gaps`.
- **Formatting Rules**: `booktabs` package (`\toprule`, `\midrule`, `\bottomrule`). No vertical lines.

---

### TABLE 2: Out-of-Sample Predictive Classification Performance
- **Quantitative Question Answered**: *How do the 5 optimizers compare across standard predictive classification metrics over 20 stochastic seeds?*
- **Necessity Rating**: **ESSENTIAL** (Primary empirical results table in Section 5.1).
- **Source Data**: `outputs/metrics/optimizer_comparison_metrics.csv`.
- **Columns**: `Optimizer` | `Accuracy` | `F1-Score` | `MCC` | `AUC-ROC` | `AUC-PR` | `Runtime (s)`.
- **Formatting Rules**: All metrics reported as $\text{Mean} \pm \text{Std}$. The highest mean score in each column MUST be highlighted in **boldface**.

---

### TABLE 3: Non-Parametric Statistical Hypothesis Testing Results
- **Quantitative Question Answered**: *Are pairwise metric differences between optimizers statistically significant, and what is their effect size?*
- **Necessity Rating**: **ESSENTIAL** (Statistical significance proof in Section 5.4).
- **Source Data**: `outputs/statistical_tests/wilcoxon_holm_results.csv`.
- **Columns**: `Pairwise Comparison` | `Target Metric` | `Mean Diff.` | `p-value (Wilcoxon-Holm)` | `Cohen's d` | `Statistical Interpretation`.
- **Formatting Rules**: $p$-values $< 0.05$ highlighted in **bold**. Large effect sizes ($|d| > 0.80$) explicitly annotated.

---

### TABLE 4: Out-of-Sample Financial Backtest Performance & Fee Sensitivity
- **Quantitative Question Answered**: *How do predictive gains translate into net trading return, Sharpe ratio, and drawdown under transaction costs?*
- **Necessity Rating**: **ESSENTIAL** (Financial utility validation in Section 5.5).
- **Source Data**: `outputs/backtests/financial_backtest_results.csv`.
- **Columns**: `Optimizer Strategy` | `Net Return (%)` | `Sharpe Ratio` | `Max Drawdown (%)` | `Profit Factor` | `Win Rate (%)` | `Total Trades`.
- **Formatting Rules**: Multi-tier cost breakdown (0.00%, 0.01%, 0.02% per trade). Best financial metrics highlighted in **boldface**.

---

## 3. Formatting Rules (NCA LaTeX Standards)

1. **Booktabs Package**: Use only `\toprule`, `\midrule`, and `\bottomrule`. Never use vertical lines (`|`).
2. **Width Scaling**: Every table must be wrapped in `\resizebox{\linewidth}{!}{...}` to prevent margin overflow (`overfull \hbox`).
3. **Bolding Criteria**: Bold ONLY the top mean value per column. Never bold multiple values unless they are mathematically tied.
