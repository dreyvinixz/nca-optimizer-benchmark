# SCIENTIFIC AUDIT REPORT — Pre-Flight Core Audit (Data, Methodology, Results)
**Mission ID**: MISSION 11  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/designs/SCIENTIFIC_AUDIT_REPORT.md`  

---

## 1. Executive Summary & Objective

This audit performs a self-critical examination of the manuscript's core technical sections—**Section 3 (Data)**, **Section 4 (Methodology)**, and **Section 5 (Results)**. The goal is to identify and resolve any structural inconsistencies, unhedged absolute statements, notational ambiguities, or statistical vulnerabilities before drafting subsequent sections.

---

## 2. Audit 1: Structural & Notational Consistency

- **Variable Definitions**:
  - *Finding*: Search space vector $\boldsymbol{\theta} = [N_{L1}, N_{L2}, \eta, \alpha, p_{\text{drop}}, B]$ is defined in Section 4.1 prior to use in fitness functions. Verified.
  - *Fix Needed*: Ensure time index notation ($k$ for 5-min bars, $t$ for optimizer evaluation steps) is strictly distinct across Sections 3, 4, and 5.
- **Equation Sequencing**: All equations (\ref{eq:target}) through (\ref{eq:backtest}) appear in sequential order before being referenced in Results. Verified.
- **Table & Figure Cross-References**:
  - *Finding*: Table 2, Table 3, Table 4, Figure 1, and Figure 2 are all explicitly cited and discussed in text. Verified.
- **Metric Definitions**:
  - *Finding*: Accuracy, $F_1$, MCC, AUC-ROC, AUC-PR, Net Return, Sharpe Ratio, and MDD are defined in Sections 4.2, 4.5, and 4.6 prior to reporting in Section 5 tables. Verified.
- **Acronym Expansion**:
  - *Finding*: MLP (Multilayer Perceptron), RS (Random Search), GA (Genetic Algorithm), PSO (Particle Swarm Optimization), DE (Differential Evolution), GWO (Grey Wolf Optimizer), MCC (Matthews Correlation Coefficient), MDD (Maximum Drawdown) are expanded on first usage. Verified.

---

## 3. Audit 2: Evidence Traceability & Epistemic Hedging (Removal of Absolutes)

- **Issue Identified**: Several sentences contained overly strong "absolute" phrasing (e.g., *"100% data leakage elimination"*, *"absolute guarantee"*).
- **Required Revisions**:
  - *Old Phrase*: *"To guarantee zero temporal data leakage..."*
  - *Scholarly Replacement*: *"To prevent temporal look-ahead leakage within the adopted experimental design..."*
  - *Old Phrase*: *"eliminates 100% of temporal data leakage..."*
  - *Scholarly Replacement*: *"is designed to preclude temporal data leakage under the sequential chronological split..."*
  - *Old Phrase*: *"absolute proof of superiority..."*
  - *Scholarly Replacement*: *"provides statistically significant evidence under the evaluated $N_{\text{eval}}=1,500$ budget constraint..."*

---

## 4. Audit 3: Statistical Rigor & Interpretation Audit

- **Omnibus Testing**: Friedman test ($\chi^2 = 38.42, p = 9.2 \times 10^{-8}$) precedes pairwise comparisons. Verified.
- **Family-Wise Error Rate**: Holm-Bonferroni correction applied to all pairwise Wilcoxon $p$-values. Verified.
- **Effect Size Interpretation**: Cohen's $d$ correctly interpreted alongside $p$-values (differentiating large effects $d > 0.80$ from medium effects $d > 0.50$). Verified.
- **Confidence Intervals**: Shaded $\pm 1$ standard deviation confidence intervals included in Figure 2 convergence trajectories. Verified.

---

## 5. Audit 4: Narrative Necessity Test (Paragraph-by-Paragraph Elimination Audit)

- **Test**: Does removing any paragraph degrade the core scientific argument?
  - *Section 3 (Data)*: 3 subsections (Dataset, InfoGain, Temporal Split). All 3 are essential; removing any breaks data leakage proof.
  - *Section 4 (Methodology)*: 6 subsections (Search Space, Fitness, Budget, Optimizers, Stats, Backtest). All 6 are essential; removing any breaks reproducibility.
  - *Section 5 (Results)*: 5 subsections (Predictive, Convergence, Runtime, Stats, Backtest). All 5 are essential; removing any leaves a gap in evidence.
- **Verdict**: Zero redundant paragraphs identified. Narrative density is optimal.

---

## 6. Action Plan for Refinement

1. Apply epistemic hedging replacements across `sections/data.tex`, `sections/methodology.tex`, and `sections/results.tex`.
2. Ensure notation ($k$ for bar index vs. $t$ for optimizer step) is 100% uniform.
3. Recompile `main.pdf` and verify clean build.
