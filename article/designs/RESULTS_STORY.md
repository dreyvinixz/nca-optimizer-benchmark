# RESULTS STORY — Findings Narrative Arc
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/designs/RESULTS_STORY.md`  

---

## 1. Findings Narrative Arc

Before drafting Section 5 (Results), every finding is structured as a complete narrative arc: `Finding` $\rightarrow$ `Evidence` $\rightarrow$ `Statistical Support` $\rightarrow$ `Interpretation` $\rightarrow$ `Reviewer Question` $\rightarrow$ `Answer`.

---

### Finding 1: Metaheuristic Superiority Over Random Search
- **Evidence**: Table 2 (`optimizer_comparison_metrics.csv`). GA achieves $\text{MCC} = 0.231 \pm 0.012$ vs. Random Search $\text{MCC} = 0.185 \pm 0.021$.
- **Statistical Support**: Wilcoxon-Holm $p = 0.0021$, Cohen's $d = 1.241$ (Large effect size).
- **Interpretation**: Guided metaheuristics extract real search efficiency beyond unguided stochastic sampling.
- **Reviewer Question**: *Could this improvement be a random artifact of seed sampling?*
- **Answer**: No. Confirmed by Friedman omnibus test ($\chi^2 = 38.42, p = 9.2 \times 10^{-8}$) and Wilcoxon post-hoc test across 20 independent seeds.

---

### Finding 2: Recombination Reconciles Late-Stage Exploration (GA vs GWO)
- **Evidence**: Figure 2 (Convergence Curves) and Table 2. GA ($\text{MCC} = 0.231$) and DE ($\text{MCC} = 0.228$) outperform GWO ($\text{MCC} = 0.208$).
- **Statistical Support**: Wilcoxon-Holm $p = 0.0142$, Cohen's $d = 0.815$ (GA vs GWO).
- **Interpretation**: GWO's leadership hierarchy causes early trajectory flattening, whereas GA's uniform crossover and DE's vector differencing maintain population variance.
- **Reviewer Question**: *Why did GWO plateau early despite rapid initial convergence?*
- **Answer**: Wolf leadership attraction ($\alpha, \beta, \delta$) rapidly reduces population diversity, trapping the pack in local sub-optima in noisy non-convex search spaces.

---

### Finding 3: Predictive MCC Improvements Yield Positive Net Financial Returns
- **Evidence**: Table 4 (`financial_backtest_results.csv`). GA trading strategy yields $+18.4\%$ Net Return and Sharpe ratio $1.42$ under $0.01\%$ fees.
- **Statistical Support**: Out-of-sample backtest over 3,012 test bars across 3 fee tiers ($0.00\%, 0.01\%, 0.02\%$).
- **Interpretation**: Optimizing compound MCC ($0.60\text{MCC} + 0.40F_1$) produces models with strong directionality that survive brokerage and slippage costs.
- **Reviewer Question**: *Does the model remain profitable under realistic transaction fees?*
- **Answer**: Yes. Net return remains positive ($+12.0\%$, Sharpe $0.98$) even under severe $0.02\%$ slippage friction.
