# REVIEWER PROFILE — Peer-Review Simulation Engine
**Journal Target**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/REVIEWER_PROFILE.md`  

---

## 1. Virtual Reviewer Profiles (NCA Peer-Review Panel)

To ensure acceptance prior to formal submission, every drafted section must be audited against four specialized virtual peer-review profiles representing the editorial standards of *Neural Computing and Applications*.

---

### REVIEWER 1: The Methodological Rigorist
- **Primary Focus**: Experimental design, data leakage prevention, validation protocols, baseline choices, budget fairness.
- **Key Inspection Questions**:
  1. *Was the dataset split chronologically, or did the authors use random sampling that leaks future price data into the past?*
  2. *Are all optimizers evaluated under an identical computational budget ($N_{\text{eval}}$), or is GA given 100 generations while PSO gets 10 iterations?*
  3. *Is Random Search included as an essential stochastic baseline?*
- **Fatal Rejection Triggers**:
  - Use of randomized $K$-fold cross-validation on time series.
  - Comparing algorithms using different numbers of candidate evaluations.
  - Absence of a unguided Random Search baseline.
- **Verification Checklist for Reviewer 1**:
  - [ ] `shuffle = false` and 60/20/20 sequential split explicitly stated.
  - [ ] $N_{\text{eval}} = 1,500$ evaluation cap identical across all 5 algorithms.
  - [ ] Random Search included in all tables and figures as Baseline 1.

---

### REVIEWER 2: The Computational Statistician
- **Primary Focus**: Statistical hypothesis testing, seed variance, $p$-values, effect size measurements, Friedman/Wilcoxon tests.
- **Key Inspection Questions**:
  1. *Did the authors report standard deviations across multiple stochastic seeds, or just single-run point estimates?*
  2. *Was an omnibus test (Friedman) conducted before running post-hoc pairwise comparisons?*
  3. *Were $p$-values corrected for multiple comparisons (Holm-Bonferroni)?*
  4. *Is the practical magnitude of gains supported by Cohen's $d$ effect size?*
- **Fatal Rejection Triggers**:
  - Reporting only mean metrics without $\pm \text{Std}$.
  - Claiming "significant improvement" based solely on raw percentage differences without $p$-values.
  - Omission of effect size metrics.
- **Verification Checklist for Reviewer 2**:
  - [ ] All predictive metrics in Table 2 formatted as $\text{Mean} \pm \text{Std}$.
  - [ ] Friedman test reported in Section 5.4.
  - [ ] Table 3 includes exact Wilcoxon $p$-values and Holm-Bonferroni correction.
  - [ ] Cohen's $d$ values reported for all pairwise comparisons ($d > 0.80$ highlighted).

---

### REVIEWER 3: The Domain & Quantitative Finance Specialist
- **Primary Focus**: Financial market applicability, trading backtest simulation, transaction cost sensitivity, risk-adjusted returns (Sharpe, MDD).
- **Key Inspection Questions**:
  1. *Does a high classification metric (MCC/F1) actually yield positive financial returns after transaction fees?*
  2. *Are brokerage fees and slippage included in the trading simulation?*
  3. *Is risk evaluated via Maximum Drawdown (MDD) and Sharpe Ratio, or just total return?*
- **Fatal Rejection Triggers**:
  - Evaluating models purely on raw classification accuracy without economic metrics.
  - Assuming zero transaction costs or zero execution latency in 5-minute futures trading.
- **Verification Checklist for Reviewer 3**:
  - [ ] Table 4 includes Net Return %, Sharpe Ratio, MDD %, and Profit Factor.
  - [ ] Transaction cost sensitivity analysis included (0.00%, 0.01%, 0.02% fee tiers).
  - [ ] Matthews Correlation Coefficient (MCC) used as primary validation metric.

---

### REVIEWER 4: The Novelty & Literature Specialist
- **Primary Focus**: Literature gap articulation, alignment with recent NCA state of the art (2024–2026), Table 1 clarity, 6 bulleted contributions.
- **Key Inspection Questions**:
  1. *Does the introduction clearly articulate why this benchmark is needed beyond prior conference papers?*
  2. *Is Table 1 structured with an explicit "Unmet Limitations" column?*
  3. *Are recent 2024–2026 NCA papers cited and synthesized in Section 2?*
- **Fatal Rejection Triggers**:
  - Framing the paper as a incremental extension of a single previous paper.
  - Vague or missing bulleted contribution list in the Introduction.
  - Outdated reference list missing current journal literature.
- **Verification Checklist for Reviewer 4**:
  - [ ] Introduction contains 6 bold bulleted contributions starting with present-tense active verbs.
  - [ ] Table 1 present in Section 2 with 4 explicit columns.
  - [ ] At least 15 citations from 2024–2026 NCA papers included.

---

## 2. Pre-Flight Peer-Review Audit Matrix

Before any manuscript section is declared complete, it must pass the Pre-Flight Peer-Review Audit Matrix:

| Reviewer Profile | Audit Requirement | Section Responsible | Pass / Fail |
| :--- | :--- | :--- | :--- |
| **Reviewer 1** | Sequential temporal split (`shuffle = false`, 60/20/20). | Section 3 | **PASS** |
| **Reviewer 1** | Identical budget ($N_{\text{eval}} = 1,500$) for all 5 optimizers. | Section 4 | **PASS** |
| **Reviewer 2** | Predictive performance reported as $\text{Mean} \pm \text{Std}$. | Section 5 (Table 2) | **PASS** |
| **Reviewer 2** | Friedman + Wilcoxon-Holm $p$-values and Cohen's $d$. | Section 5 (Table 3) | **PASS** |
| **Reviewer 3** | Financial backtest (Sharpe, MDD, Net Return %, Costs). | Section 5 (Table 4) | **PASS** |
| **Reviewer 4** | Table 1 literature gap matrix present. | Section 2 | **PASS** |
| **Reviewer 4** | 6 bold bulleted contributions in Introduction. | Section 1 | **PASS** |
