# SECTION PLANNER — Scientific Planning Engine
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/SECTION_PLANNER.md`  

---

## 1. Master Section-by-Section Plan

This document defines the pre-writing blueprint for every section of the paper. **No text shall be drafted without first validating against this planner.**

---

### SECTION 1: INTRODUCTION

- **Scientific Objective**: Convince the reader and reviewers that hyperparameter selection for intraday financial classification is a non-convex global optimization problem that suffers from severe methodological flaws in existing literature, requiring an equal-budget benchmark.
- **Questions the Reader Has**:
  1. Why is 5-minute intraday futures prediction challenging?
  2. Why can't gradient descent or grid search solve hyperparameter selection for MLPs?
  3. Why are metaheuristics (GA, PSO, DE, GWO, RS) appropriate?
  4. What specific flaws exist in prior published papers?
  5. What does this paper do differently?
  6. What are the concrete, verifiable contributions?
- **Questions That Must Be Answered**:
  - How do market non-stationarity and microstructure noise erode price patterns?
  - What is the 6D search space over which optimizers operate?
  - What are the 3 major literature flaws (budget inequality, data leakage, classification-economic disconnect)?
  - How does our protocol eliminate these flaws?
- **Repository Evidence Required**:
  - `PROJECT_CONTEXT.md` (Research lineage, IJCNN reviewer rejection points).
  - `config/experiment_config.yaml` (Equal budget $N_{\text{eval}} = 1,500$, 60/20/20 temporal split).
  - `config/search_spaces.yaml` (6D MLP search space bounds).
- **Literature Evidence Required**:
  - Dhingra et al. (NCA 2025), Billah et al. (NCA 2024), Gad (2022), Rajwar et al. (2023), Chicco & Jurman (2020).
- **Figures Needed**: None (Introduction is textual).
- **Tables Needed**: None (Table 1 resides in Section 2).
- **Logical Dependencies**: Requires clarity on the 3 literature flaws and 6 bulleted contributions.
- **Expected Conclusion**: The reader agrees that an equal-budget, leakage-free benchmark is urgent and scientifically necessary.
- **Common Reviewer Criticisms**: Overclaiming novelty, lack of clear research gap, fuzzy contributions.
- **Acceptance Checklist**:
  - [ ] CARS 5-move model followed precisely.
  - [ ] 3 literature flaws explicitly articulated.
  - [ ] 6 bulleted contributions in bold starting with present-tense active verbs.
  - [ ] Zero citations inside the contributions list.
  - [ ] Section outline paragraph at the end.

---

### SECTION 2: RELATED WORK & THEORETICAL BACKGROUND

- **Scientific Objective**: Provide a rigorous synthesis of technical analysis, neural financial forecasting, and metaheuristics, culminating in Table 1 which exposes unmet limitations in published literature.
- **Questions the Reader Has**:
  1. What features are standard in high-frequency intraday prediction?
  2. How have neural networks and metaheuristics been combined previously?
  3. What are the exact limitations of prior studies?
- **Questions That Must Be Answered**:
  - Why is Information Gain effective for feature selection in 5-min WIN futures?
  - Which metaheuristic families (evolutionary vs. swarm) have been applied?
  - What gaps exist in the 40+ reference papers from NCA and financial ML?
- **Repository Evidence Required**:
  - `article/references/md_references/` (90 Markdown reference papers).
  - ICCSA 2025 paper (`InfoGain_[7] = [30, 52, 31, 53, 42, 33, 41]`).
- **Literature Evidence Required**:
  - 40 recent NCA papers (2024–2026), Faris et al. (2018), Mirjalili et al. (2020).
- **Figures Needed**: None.
- **Tables Needed**: **Table 1: Representative literature on optimizer-driven financial forecasting and their unmet limitations**.
- **Logical Dependencies**: Depends on literature survey in `md_references/`.
- **Expected Conclusion**: Prior work is fragmented and lacks equal-budget temporal validation.
- **Common Reviewer Criticisms**: Superficial literature review, missing recent 2024-2026 NCA citations, non-systematic table.
- **Acceptance Checklist**:
  - [ ] 3 thematic sub-sections (2.1 Technical Analysis, 2.2 Financial ML, 2.3 Metaheuristics).
  - [ ] Table 1 present with 4 columns (*Study, Model/Domain, Optimization, Unmet Limitations*).
  - [ ] At least 15 citations from 2024–2026 NCA papers included.

---

### SECTION 3: DATA & PROBLEM FORMULATION

- **Scientific Objective**: Establish complete transparency regarding dataset properties, Information Gain feature selection, and the leakage-free sequential temporal split protocol.
- **Questions the Reader Has**:
  1. What asset and timeframe are evaluated?
  2. How were the 15,057 bars divided?
  3. Is there any possibility of future information leaking into the past?
- **Questions That Must Be Answered**:
  - What are the properties of WIN contracts (WING24, WINJ24, WINM24, WINQ24)?
  - Why is `shuffle = false` mandatory?
  - How are train (60%), validation (20%), and test (20%) sets structured?
- **Repository Evidence Required**:
  - `data/raw/merged_output.csv` (15,057 rows).
  - `config/experiment_config.yaml` (`train_size: 0.60`, `validation_size: 0.20`, `test_size: 0.20`, `shuffle: false`).
- **Literature Evidence Required**:
  - Souza et al. (2025 ICCSA), Souza et al. (2026 IJCNN review).
- **Figures Needed**: **Figure 1: Chronological 60/20/20 sequential temporal split diagram**.
- **Tables Needed**: Summary table of dataset attributes and instance counts.
- **Logical Dependencies**: Requires dataset metrics from `data/raw/merged_output.csv`.
- **Expected Conclusion**: Data leakage is 100% eliminated by design.
- **Common Reviewer Criticisms**: Temporal leakage, random K-Fold cross-validation on time series, missing class balance statistics.
- **Acceptance Checklist**:
  - [ ] 15,057 total instances accounted for (9,034 train / 3,011 val / 3,012 test).
  - [ ] `shuffle = false` explicitly stated.
  - [ ] 7 Information Gain feature names and indices documented.

---

### SECTION 4: PROPOSED OPTIMIZER BENCHMARK FRAMEWORK

- **Scientific Objective**: Formulate the 6D MLP search space, compound MCC-driven fitness objective, mathematical equations of the 5 optimizers, non-parametric statistical protocol, and backtest simulator.
- **Questions the Reader Has**:
  1. What parameters define the search space $\boldsymbol{\theta}$?
  2. How is fitness calculated?
  3. How do RS, GA, PSO, DE, and GWO update candidate solutions?
  4. How is computational budget equality enforced?
- **Questions That Must Be Answered**:
  - What are the bounds of L1 neurons, $lr$, $\alpha$, dropout, batch size?
  - Why $f(\boldsymbol{\theta}) = 0.60\text{MCC} + 0.40F_1$?
  - What equations govern velocity in PSO, mutation in DE, and wolf vectors in GWO?
  - What formula calculates Sharpe ratio and Maximum Drawdown?
- **Repository Evidence Required**:
  - `config/search_spaces.yaml`.
  - `config/experiment_config.yaml` ($N_{\text{eval}} = 1,500$, GA/PSO/DE/GWO hyperparameters).
- **Literature Evidence Required**:
  - Goldberg (1989), Kennedy & Eberhart (1995), Storn & Price (1997), Mirjalili (2014), Chicco & Jurman (2020).
- **Figures Needed**: Architectural diagram of the optimizer-MLP evaluation loop.
- **Tables Needed**: Hyperparameter search space boundaries table.
- **Logical Dependencies**: Search space definitions in `config/search_spaces.yaml`.
- **Expected Conclusion**: The benchmark framework is 100% reproducible and fair.
- **Common Reviewer Criticisms**: Unequal evaluations per algorithm, missing mathematical equations, uncalibrated fitness.
- **Acceptance Checklist**:
  - [ ] 6D search space bounds explicitly tabulated.
  - [ ] Fitness formula $f(\boldsymbol{\theta}) = 0.60\text{MCC} + 0.40F_1$ mathematically defined.
  - [ ] Mathematical update equations provided for all 5 optimizers.
  - [ ] $N_{\text{eval}} = 1,500$ evaluation budget cap explicitly enforced.

---

### SECTION 5: EXPERIMENTAL RESULTS & PERFORMANCE BENCHMARK

- **Scientific Objective**: Present empirical out-of-sample predictive metrics, convergence dynamics, runtime analysis, statistical hypothesis tests, and financial backtest outcomes.
- **Questions the Reader Has**:
  1. Which optimizer achieved the highest out-of-sample MCC and F1 score?
  2. Are performance differences statistically significant?
  3. How fast do optimizers converge?
  4. Did predictive gains translate into net trading profits?
- **Questions That Must Be Answered**:
  - What are the $\text{Mean} \pm \text{Std}$ values for Accuracy, F1, MCC, AUC-ROC across seeds?
  - What are the $p$-values of Friedman and Wilcoxon-Holm tests?
  - What are the Cohen's $d$ effect sizes?
  - What Net Return %, Sharpe ratio, and MDD % did each optimizer achieve under transaction fees?
- **Repository Evidence Required**:
  - `outputs/metrics/`, `outputs/statistical_tests/`, `outputs/backtests/`.
- **Literature Evidence Required**:
  - Rajwar et al. (2023), Dhingra et al. (2025).
- **Figures Needed**: **Figure 2: Convergence trajectories (Fitness vs. $N_{\text{eval}}$)** across 5 optimizers.
- **Tables Needed**:
  - **Table 2: Out-of-sample predictive performance ($\text{Mean} \pm \text{Std}$)**.
  - **Table 3: Non-parametric statistical test results ($p$-values and Cohen's $d$)**.
  - **Table 4: Out-of-sample financial backtest metrics (Net Return, Sharpe, MDD)**.
- **Logical Dependencies**: Output CSV files in `outputs/`.
- **Expected Conclusion**: GA and DE achieve superior predictive balance and economic return with statistical significance over Random Search.
- **Common Reviewer Criticisms**: Missing standard deviations, lack of statistical tests, no financial metrics.
- **Acceptance Checklist**:
  - [ ] Table 2 presents $\text{Mean} \pm \text{Std}$ with best mean in **bold**.
  - [ ] Table 3 reports exact $p$-values and Cohen's $d$.
  - [ ] Table 4 reports Sharpe, MDD, Net Return %, and transaction fee impacts.

---

### SECTION 6: DISCUSSION & PRACTICAL IMPLICATIONS

- **Scientific Objective**: Interpret empirical findings through algorithmic search mechanics, analyze trade-offs between predictive gains and computational execution overhead, and provide practical deployment guidelines.
- **Questions the Reader Has**:
  1. Why did GA and DE outperform PSO and GWO on this specific search space?
  2. Is the extra execution runtime worth the predictive gain?
  3. How should practitioners select optimizers for quantitative trading?
- **Questions That Must Be Answered**:
  - How did crossover diversification prevent premature local convergence in GA/DE?
  - Why did GWO exhibit fast early convergence but plateau prematurely?
  - What is the computational overhead of metaheuristics vs. Random Search?
- **Repository Evidence Required**:
  - `outputs/metrics/runtime_analysis.csv`.
- **Literature Evidence Required**:
  - Gad (2022), Mirjalili et al. (2020).
- **Figures Needed**: Trade-off plot (MCC Gain vs. Runtime Overhead).
- **Tables Needed**: Summary recommendations matrix for practitioners.
- **Logical Dependencies**: Empirical results from Section 5.
- **Expected Conclusion**: Optimizer choice involves a structural trade-off between early convergence speed and long-term search space coverage.
- **Common Reviewer Criticisms**: Surface-level restatement of results without mechanical interpretation, overclaiming SOTA status.
- **Acceptance Checklist**:
  - [ ] Results interpreted via search mechanics (*exploration vs. exploitation*).
  - [ ] Runtime overhead analyzed ($3.35\text{ s}$ vs. $2.95\text{ s}$).
  - [ ] Zero un-hedged claims of universal superiority.

---

### SECTION 7: CONCLUSION & FUTURE WORK

- **Scientific Objective**: Provide a concise 2-to-3 paragraph synthesis of the 3 primary benchmark discoveries and outline 3 concrete future research directions.
- **Questions the Reader Has**:
  1. What are the key takeaways of this benchmark?
  2. What are the limitations of this study?
  3. Where should future research proceed?
- **Questions That Must Be Answered**:
  - What were the 3 core quantitative findings?
  - How can future work expand the benchmark (multi-asset, 1-min data, multi-objective Pareto optimization)?
- **Repository Evidence Required**:
  - Synthesis of Sections 1–6.
- **Literature Evidence Required**: None.
- **Figures Needed**: None.
- **Tables Needed**: None.
- **Logical Dependencies**: Completed manuscript.
- **Expected Conclusion**: The benchmark establishes a clean, reproducible foundation for evolutionary neural forecasting in financial markets.
- **Common Reviewer Criticisms**: Vague future work, repetition of introduction text verbatim.
- **Acceptance Checklist**:
  - [ ] Concise (300 to 450 words total).
  - [ ] 3 core quantitative takeaways synthesized.
  - [ ] 3 explicit future research directions outlined.
