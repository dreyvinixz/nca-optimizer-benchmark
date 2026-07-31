# SECTION DESIGN — Section 2: Related Work & Literature Gap Matrix
**Mission ID**: MISSION 14A  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/designs/related_work_design.md`  

---

## 1. Hypothesis-Driven Structure

Rather than listing literature chronologically, Section 2 is organized into three thematic hypothesis-driven subsections, each contrasting current literature against our contribution and synthesizing recent 2024–2026 NCA papers.

---

### Subsection 2.1: Technical Analysis & Machine Learning in Intraday Forecasting
- **Thematic Focus**: Financial time series complexity and neural network feature representations.
- **Current Literature**: Machine learning models (MLPs, LSTMs, CNNs) process technical indicators to detect market signals (Billah et al., NCA 2024; Cardoso et al., 2022; Souza et al., 2025 ICCSA).
- **Unmet Gap**: Published studies often rely on high-dimensional raw indicator spaces without information-theoretic feature selection, exacerbating model complexity.

---

### Subsection 2.2: Metaheuristic Tuning & The Budget Inequality Hypothesis
- **Hypothesis 1 (Budget Inequality)**: *Reported superiority among metaheuristic optimizers is heavily distorted when algorithms are evaluated under unequal candidate solution evaluation counts.*
- **Current Evidence**: Prior studies compare GA using 100 generations against PSO using 20 iterations, obscuring whether gains stem from search operators or unequal sampling (Dhingra et al., NCA 2025; Rajwar et al., 2023; Ecer et al., 2020).
- **Our Contribution**: Enforces an identical budget cap of $N_{\text{eval}} = 1,500$ evaluations per seed across all 5 optimizer families.

---

### Subsection 2.3: Validation Protocols & The Temporal Data Leakage Hypothesis
- **Hypothesis 2 (Temporal Data Leakage)**: *Randomized K-fold cross-validation on intraday financial time series introduces look-ahead data leakage, yielding artificially inflated validation performance.*
- **Current Evidence**: Financial ML literature routinely applies random cross-validation or shuffled sampling, destroying time-series chronology (Souza et al., 2026 IJCNN Review; Makridakis et al., 2018).
- **Our Contribution**: Establishes a strict 60/20/20 sequential chronological split with `shuffle = false` over 15,057 5-minute bars.

---

### Subsection 2.4: Evaluation Objectives & The Classification-Economic Disconnect Hypothesis
- **Hypothesis 3 (Classification-Economic Disconnect)**: *Optimizing models purely on raw accuracy fails to guarantee positive out-of-sample trading returns under realistic transaction costs.*
- **Current Evidence**: Literature overwhelmingly tunes hyperparameters via accuracy or cross-entropy loss, ignoring class imbalance distortion and brokerage fees (Chicco & Jurman, 2020; Henrique et al., 2019).
- **Our Contribution**: Formulates a compound MCC-driven objective ($0.60\text{MCC} + 0.40F_1$) and validates trading performance across 3 fee tiers ($0.00\%, 0.01\%, 0.02\%$).

---

### Table 1: Representative Literature & Unmet Limitations Matrix
- **Columns**: `Study` | `Model & Asset Domain` | `Optimization Paradigm` | `Unmet Limitations / Research Gap`.
- **References Included**: Billah et al. (NCA 2024), Dhingra et al. (NCA 2025), Ecer et al. (2020), Rajwar et al. (2023), Souza et al. (2025 ICCSA), Gad (2022).
