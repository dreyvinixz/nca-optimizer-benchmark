# PROJECT MEMORY — Single Source of Truth
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/PROJECT_MEMORY.md`  

---

## 1. Project Metadata & Scientific Scope

- **Official Working Title**: *A benchmark study of evolutionary and swarm intelligence optimizers for neural intraday trend classification in Brazilian futures markets under real-world constraints*
- **Short Running Title**: *Optimizer Benchmark for Neural Intraday Trend Classification*
- **Target Journal**: *Neural Computing and Applications* (Springer Nature, Journal ID 521, ISSN: 0941-0643)
- **Submission Track**: Original Article
- **Peer-Review Mode**: Double-Blind Peer Review
  - *Main Manuscript (`article/manuscript/main.tex` and `sections/`)*: 100% Anonymized (No author names, affiliations, emails, or grant codes).
  - *Title Page (`article/manuscript/titlepage.tex`)*: Contains all author metadata, ORCIDs, affiliations, and grant acknowledgments.
- **Repository Evidence**: [`PROJECT_CONTEXT.md:L5-L10`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L5-L10), [`article/manuscript/main.tex:L18-L45`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/manuscript/main.tex#L18-L45), [`article/manuscript/titlepage.tex:L15-L75`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/manuscript/titlepage.tex#L15-L75).

---

## 2. Authorship, Affiliations, and Funding Metadata

### Authors & Identifiers
1. **Andrey V. S. Souza** — Co-First Author (PPGC/FURG) | ORCID: [`0009-0006-4177-758X`](https://orcid.org/0009-0006-4177-758X) | Email: `andreyvinicius@furg.br`
2. **Bruno L. Dalmazo** — Corresponding Author & Co-First Author (PPGC/FURG) | ORCID: [`0000-0002-6996-7602`](https://orcid.org/0000-0002-6996-7602) | Email: `dalmazo@furg.br`
3. **Viviane L. D. de Mattos** — Co-Author (PPGC/FURG) | ORCID: [`0000-0002-3512-6290`](https://orcid.org/0000-0002-3512-6290)
4. **Richard F. Pinto** — Co-Author (PPGC/FURG) | ORCID: [`0009-0007-0176-3383`](https://orcid.org/0009-0007-0176-3383)
5. **Diego R. Bruno** — Co-Author (UNESP) | ORCID: [`0009-0008-1806-0278`](https://orcid.org/0009-0008-1806-0278)
6. **Eduardo N. Borges** — Co-Author (PPGC/FURG) | ORCID: [`0000-0003-1595-7676`](https://orcid.org/0000-0003-1595-7676)
7. **Giancarlo Lucca** — Co-Author (PPGC/FURG & UniRV) | ORCID: [`0000-0002-3776-0260`](https://orcid.org/0000-0002-3776-0260)
8. **Fabian C. Cardoso** — Co-Author (UniRV) | ORCID: [`0000-0002-2842-0387`](https://orcid.org/0000-0002-2842-0387)
9. **Rafael A. Berri** — Co-Author (PPGC/FURG) | ORCID: [`0000-0002-3812-4186`](https://orcid.org/0000-0002-3812-4186)

### Institutional Affiliations
- **Affiliation 1**: Graduate Program in Computer Science (PPGC), Federal University of Rio Grande (FURG), Rio Grande, RS, Brazil.
- **Affiliation 2**: Universidade Estadual Paulista (UNESP), São José do Rio Preto, SP, Brazil.
- **Affiliation 3**: University of Rio Verde (UniRV), Rio Verde, GO, Brazil.

### Verified Financial Support & Grants
- **FAPERGS**: Grants `24/2551-0001396-2` and `23/2551-0000773-8`.
- **CNPq**: Grant `307416/2025-9`.
- **FAPERGS/CNPq Joint**: Grant `23/2551-0000126-8`.
- **Fesurv - University of Rio Verde**: Institutional financial support.
- **Repository Evidence**: [`article/manuscript/titlepage.tex:L15-L75`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/manuscript/titlepage.tex#L15-L75).

---

## 3. Research Lineage & Evolutionary Trajectory

### Stage 1: Accepted Conference Paper (ICCSA 2025)
- **Title**: *Predictive analysis with technical indicators and feature selection for futures contracts trading*
- **Scope**: Feature selection for short-term 5-min WIN Mini-Index futures using Random Forest.
- **Key Finding**: Information Gain selected 7 features from 66 candidates (`InfoGain_[7] = [30, 52, 31, 53, 42, 33, 41]`), reducing overfitting and improving test metrics.
- **Repository Evidence**: [`PROJECT_CONTEXT.md:L21-L44`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L21-L44), PDF at `article/references/_ICSSA_Document_2025___Andrey__Predictive_analysis_with_technical_indicators_and_features_selection_for_futures_contracts_trading (1).pdf`.

### Stage 2: Rejected Extension (IJCNN 2026 Submission)
- **Title**: *Combining Technical Indicators and Genetic Algorithms for Short-Term Machine Learning Prediction of Mini-Index Futures*
- **Scope**: Extended ICCSA pipeline by applying GA hyperparameter tuning to RF, SVM, and MLP classifiers.
- **Reported Metric Peak**: MLP + GA + RMSprop reached Test Accuracy $\approx 65.85\%$, AUC-ROC $\approx 0.7032$, AUC-PR $\approx 0.7029$.
- **Reviewer Rejection Points Identified**:
  1. Lack of multi-optimizer benchmarking (only GA evaluated).
  2. Lack of equal evaluation budget protocol.
  3. Risk of temporal data leakage due to randomized cross-validation.
  4. Absence of out-of-sample financial backtesting with transaction costs.
  5. Absence of non-parametric statistical hypothesis testing.
- **Repository Evidence**: [`PROJECT_CONTEXT.md:L46-L92`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L46-L92), PDF at `article/references/_ICCSA_2026___Andrey_____Combining_Technical_Indicators_and_Genetic_Algorithms_for_Short_Term_Machine_Learning_Prediction_of_Mini_Index_Futures (1).pdf`, Markdown review analysis at `article/references/ijcnn_rejection_analysis_and_nca_fixes.md`.

### Stage 3: Target Journal Paper (NCA 2026)
- **Focus**: Controlled benchmark of evolutionary and swarm intelligence optimizers under identical evaluation budgets ($N_{\text{eval}} = 1,500$), strict chronological sequential split (60/20/20), compound MCC-driven objective ($0.60\text{MCC} + 0.40F_1$), non-parametric statistical tests (Friedman + Wilcoxon-Holm), and financial backtest with trading fees.

---

## 4. Dataset Specification & Feature Engineering

- **Primary Asset**: Brazilian Mini-Index Futures Contract (WIN) from B3 (Brazilian Stock Exchange).
- **Timeframe / Resolution**: 5-minute intraday bars covering contracts WING24, WINJ24, WINM24, WINQ24.
- **Total Instance Count**: 15,057 intraday instances.
- **Raw Data Source File**: `data/raw/merged_output.csv`.
- **Target Variable (`trend`)**: Binary trend classification label:
  - `0`: Downtrend
  - `1`: Uptrend
- **Feature Set**: Reduced 7-feature subset selected via Information Gain (`InfoGain_[7]`):
  - Selected Column Indices: `[30, 52, 31, 53, 42, 33, 41]`.
- **Repository Evidence**: [`PROJECT_CONTEXT.md:L395-L428`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L395-L428), [`config/experiment_config.yaml:L6-L14`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L6-L14).

---

## 5. Validation Protocol & Experimental Constraints

- **Validation Protocol**: Strict Leakage-Free Sequential Temporal Holdout Split.
- **Chronological Split Ratio**:
  - **Train Set**: 60% of chronological instances (first 9,034 bars).
  - **Validation Set**: 20% of chronological instances (next 3,011 bars).
  - **Test Set (Out-of-Sample)**: 20% of chronological instances (final 3,012 bars).
- **Shuffle Policy**: `shuffle = false` (No random shuffling, no temporal data leakage).
- **Optimizer Budget Constraint**: Identical evaluation budget of $N_{\text{eval}} = 1,500$ fitness evaluations per random seed for all 5 optimizers.
- **Stochastic Seeds**: Minimum 5 random seeds (prototype), expanding to 20–30 seeds for final manuscript tables.
- **Repository Evidence**: [`PROJECT_CONTEXT.md:L454-L530`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L454-L530), [`config/experiment_config.yaml:L15-L21`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L15-L21).

---

## 6. Model Architecture & Hyperparameter Search Space

- **Base Classifier**: Multilayer Perceptron (MLP).
- **Framework**: Scikit-Learn `MLPClassifier` / TensorFlow.
- **Network Parameters**:
  - Activation Function: `tanh` (hidden layers), `sigmoid` (output layer).
  - Optimizer: `RMSprop`.
  - Loss Function: Binary Cross-Entropy.
  - Early Stopping: `early_stopping_patience = 3` on validation loss.

### 6D Search Space Boundaries (`config/search_spaces.yaml`)
1. **Hidden Neurons L1**: Integer $\in [5, 500]$
2. **Learning Rate ($lr$)**: Float $\in [1.0\times 10^{-8}, 1.0\times 10^{-2}]$ (log10 scale)
3. **L2 Regularization ($\alpha$)**: Float $\in [1.0\times 10^{-8}, 1.0\times 10^{-2}]$ (log10 scale)
4. **Dropout Rate**: Float $\in [0.0, 0.10]$
5. **Batch Size**: Categorical $\in \{16, 32, 64, 80, 112, 128\}$
- **Repository Evidence**: [`config/search_spaces.yaml:L1-L7`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/search_spaces.yaml#L1-L7), [`config/experiment_config.yaml:L22-L33`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L22-L33).

---

## 7. Objective Function & Fitness Formulation

- **Compound Objective Function**:
  $$f(\boldsymbol{\theta}) = 0.60 \times \text{MCC}(\boldsymbol{\theta}) + 0.40 \times F_1(\boldsymbol{\theta})$$
- **Primary Metric**: Matthews Correlation Coefficient (MCC) — resists class imbalance distortion and penalizes false positive signals.
- **Secondary Metrics Tracked**: Accuracy, Balanced Accuracy, Precision, Recall, $F_1$-Score, AUC-ROC, AUC-PR, Runtime (seconds), and Memory Footprint.
- **Repository Evidence**: [`PROJECT_CONTEXT.md:L531-L555`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L531-L555), [`config/experiment_config.yaml:L34-L40`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L34-L40).

---

## 8. Metaheuristic & Stochastic Optimizers Evaluated

All 5 optimizers operate over the 6D MLP search space under $N_{\text{eval}} = 1,500$ evaluations:

1. **Random Search (RS)**: Stochastic baseline sampler drawing candidates $X \sim U(L, U)$.
2. **Genetic Algorithm (GA)**: Evolutionary optimizer with tournament selection ($k=3$), uniform crossover ($P_c = 0.80$), and Gaussian mutation ($P_m = 0.20$).
3. **Particle Swarm Optimization (PSO)**: Swarm optimizer with cognitive parameter $c_1 = 1.50$, social parameter $c_2 = 1.50$, and inertia weight $w = 0.70$.
4. **Differential Evolution (DE)**: Vector mutation optimizer using `best/1/bin` strategy with mutation factor $F = 0.80$ and crossover rate $CR = 0.90$.
5. **Grey Wolf Optimizer (GWO)**: Leadership hierarchy optimizer simulating $\alpha, \beta, \delta$ wolf hunting mechanics.
- **Repository Evidence**: [`config/experiment_config.yaml:L68-L86`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L68-L86), [`PROJECT_CONTEXT.md:L108-L116`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L108-L116).

---

## 9. Statistical Significance & Financial Backtest Protocols

### Non-Parametric Hypothesis Testing
- **Omnibus Test**: Non-parametric Friedman test ($\alpha = 0.05$).
- **Post-Hoc Pairwise Testing**: Paired Wilcoxon signed-rank tests with Holm-Bonferroni $p$-value correction.
- **Effect Size Metric**: Cohen's $d$ ($|d| > 0.8$ denotes large effect size).

### Economic Backtest Simulator
- **Trading Signal**: Long position when predicted probability $p \ge 0.50$, Short/Flat otherwise.
- **Reported Financial Metrics**: Net Return %, Annualized Sharpe Ratio, Maximum Drawdown (MDD %), Profit Factor, Win Rate %, Total Trades, and Brokerage/Slippage Cost Sensitivity.
- **Repository Evidence**: [`PROJECT_CONTEXT.md:L601-L632`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L601-L632), [`article/manuscript/sections/methodology.tex`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/manuscript/sections/methodology.tex).

---

## 10. Traceability Matrix & File Locations

| Dimension | Primary Repository Source File | Line Range / Path |
| :--- | :--- | :--- |
| **Title & Journal** | `PROJECT_CONTEXT.md` | [`L5-L10`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md#L5-L10) |
| **Authors & ORCIDs** | `article/manuscript/titlepage.tex` | [`L15-L67`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/manuscript/titlepage.tex#L15-L67) |
| **Funding & Grants** | `article/manuscript/titlepage.tex` | [`L73-L75`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/manuscript/titlepage.tex#L73-L75) |
| **Dataset & InfoGain** | `config/experiment_config.yaml` | [`L6-L14`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L6-L14) |
| **Split & Budget** | `config/experiment_config.yaml` | [`L15-L21`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L15-L21) |
| **Search Space** | `config/search_spaces.yaml` | [`L1-L7`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/search_spaces.yaml#L1-L7) |
| **Fitness Function** | `config/experiment_config.yaml` | [`L34-L40`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L34-L40) |
| **Optimizer Params** | `config/experiment_config.yaml` | [`L68-L86`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml#L68-L86) |
| **NCA Writing Patterns** | `article/references/NCA_STRUCTURAL_AND_WRITING_PATTERNS.md` | Full File |
| **Human Review Log** | `article/references/HUMAN_WRITING_REVISION_LOG.md` | Full File |

---

## 11. Explicit List of Unknowns & Pending Data

- **[UNKNOWN]** Execution log files for full 30-seed DE and GWO runs on the complete multi-asset dataset (`IND`, `WDO`, `DOL`). Currently pending execution under `outputs/metrics/`.
- **[UNKNOWN]** GPU vs CPU wall-clock execution profile across varying batch sizes ($16$ vs $128$) on CUDA-enabled clusters.
- **[UNKNOWN]** Exact slippage cost in ticks for 1-minute high-frequency execution (currently hardcoded to standard B3 exchange fees in prototype).

---

## 12. Scientific Cognitive Architecture & Phase Deliverables

- **7-Module Cognitive System**:
  1. `PROJECT_MEMORY.md` & `PROJECT_CONTEXT.md` (Project Knowledge)
  2. `NCA_WRITING_DNA.md` & `SCIENTIFIC_REASONING_DNA.md` (Literature Intelligence)
  3. `DECISION_ENGINE/` (`RESEARCH_STORY.md`, `CLAIM_VALIDATOR.md`, `CONTRIBUTION_VALIDATOR.md`, `NOVELTY_VALIDATOR.md`, `FIGURE_PLANNER.md`, `TABLE_PLANNER.md`)
  4. `SECTION_PLANNER.md` & `EVIDENCE_GRAPH.md` (Planning & Evidence)
  5. `EDITORIAL_MEMORY.md` (Decisions 001–010)
  6. `article/manuscript/` (`main.tex`, `titlepage.tex`, `references.bib`, `sections/`) (Writing Engine)
  7. `REVIEWER_PROFILE.md` (Review Engine with 4 virtual profiles + Reviewer Zero audit)
- **Manuscript Output**:
  - `article/manuscript/main.pdf` (19 pages, 711.8 KB) — Complete 7-section anonymous manuscript compiled with 0 errors via MiKTeX `pdflatex`.
  - `article/manuscript/titlepage.pdf` (2 pages, 88.4 KB) — Title page with 9 authors, ORCIDs, affiliations, and grant codes.
  - `article/nca_manuscript_overleaf_template.zip` (303.08 KB) — Overleaf package containing all TeX sources, BibTeX, and 5 vector figures.

