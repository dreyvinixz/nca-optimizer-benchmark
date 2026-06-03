# PROJECT CONTEXT — NCA Optimizer Benchmark

## 1. Project Identity

This repository contains the research and implementation pipeline for a journal article targeted at **Neural Computing and Applications**.

The current working title is:

**A benchmark study of evolutionary and swarm intelligence optimizers for neural intraday trend classification in Brazilian futures markets under real-world constraints**

The project investigates how different optimization algorithms perform when tuning neural models for short-horizon intraday financial trend classification. The main target is not simply to improve one classifier, but to build a rigorous and reproducible benchmark comparing optimization strategies under the same experimental conditions.

The project is a continuation and substantial extension of previous conference work on Brazilian futures market prediction.

---

## 2. Research Lineage

This project follows a three-stage research trajectory.

### Stage 1 — ICCSA Accepted Paper

The first accepted conference paper studied feature selection for short-term prediction of Brazilian mini-index futures.

The core experiment used:

* Brazilian Mini-Index futures data;
* 5-minute intraday records;
* technical indicators;
* feature selection methods;
* Random Forest classifier;
* comparison between full feature set and reduced feature subsets.

The main finding was that using a reduced feature subset selected by Information Gain improved generalization compared to using all available features. The Information Gain method selected 7 features from the original 66-feature space and improved test performance by reducing overfitting.

This paper is stored in:

```text
article/references/_ICSSA_Document_2025___Andrey__Predictive_analysis_with_technical_indicators_and_features_selection_for_futures_contracts_trading (1).pdf
```

This file should be treated as the historical baseline for the feature-selection stage.

---

### Stage 2 — IJCNN Rejected Extension

The second paper was an extension of the ICCSA work and was submitted to IJCNN. It extended the previous feature-selection pipeline by adding Genetic Algorithm hyperparameter optimization.

The core experiment used:

* the same general Mini-Index futures prediction setting;
* the 7 Information Gain features selected in the ICCSA study;
* Genetic Algorithm optimization;
* Random Forest, Support Vector Machine, and Multilayer Perceptron classifiers.

The strongest result came from the MLP optimized by GA, reaching approximately:

```text
MLP + GA + RMSprop
Test Accuracy: ~65.85%
AUC-ROC: ~0.7032
AUC-PR: ~0.7029
```

The IJCNN review criticized the work for:

* limited novelty;
* lack of optimizer comparison;
* insufficiently strong baselines;
* insufficient temporal validation;
* possible data leakage concerns;
* limited economic/financial evaluation;
* lack of ablation studies;
* lack of statistical testing;
* excessive reliance on accuracy and F1-score;
* insufficient connection to recent research directions.

This rejected paper is stored in:

```text
article/references/_ICCSA_2026___Andrey_____Combining_Technical_Indicators_and_Genetic_Algorithms_for_Short_Term_Machine_Learning_Prediction_of_Mini_Index_Futures (1).pdf
```

Despite the rejection, this file is important because it provides:

* the GA-based MLP baseline;
* historical hyperparameter search space;
* baseline figures and metrics;
* the transition from feature selection to model optimization.

This file should be treated as a previous extension, not as the final methodology for the journal paper.

---

### Stage 3 — Current Journal Article for Neural Computing and Applications

The current project must not be framed as merely “adding PSO to the previous GA paper.”

The new contribution must be reframed as a **controlled benchmark of optimizers**.

The core research question is:

> Which families of optimization algorithms are more suitable for tuning neural models in short-horizon intraday trend classification under real-world financial constraints?

The new article must compare optimization algorithms under a common experimental budget, using the same model, same dataset, same features, same validation protocol, same fitness function, and same evaluation metrics.

The initial optimizer benchmark should include:

```text
Random Search
Genetic Algorithm
Particle Swarm Optimization
Differential Evolution
Grey Wolf Optimizer
```

The minimum first implementation should start with:

```text
Random Search vs GA vs PSO
```

Then expand to:

```text
Random Search vs GA vs PSO vs DE vs GWO
```

---

## 3. Springer Benchmark Reference Paper

A key methodological reference for the target journal is:

```text
article/references/s00521-025-11546-2.pdf
```

This article is titled:

**A benchmark study of optimizers for short-term solar PV power forecasting using neural networks under real-world constraints**

This paper is important because it demonstrates that **Neural Computing and Applications** accepts benchmark-style articles when they are rigorous, reproducible, and evaluated under realistic constraints.

The reference paper compares neural optimizers for short-term forecasting and evaluates:

* model accuracy;
* convergence behavior;
* training stability;
* robustness under real-world constraints;
* different datasets and experimental scenarios.

Our article should follow the same high-level methodological spirit, but in the financial domain:

```text
Solar PV forecasting benchmark
→ neural optimizers
→ real-world constraints
→ convergence and robustness

Brazilian futures trend classification benchmark
→ evolutionary and swarm optimizers
→ real-world financial constraints
→ convergence, stability, runtime, predictive metrics, and financial metrics
```

This paper should guide:

* article positioning;
* title style;
* benchmark framing;
* experimental rigor;
* results organization;
* discussion of optimizer-specific recommendations.

---

## 4. Target Journal

Target journal:

```text
Neural Computing and Applications
Springer Nature
```

The article should be prepared as an **Original Article**.

The journal uses double-blind peer review. Therefore, the final submission should include:

```text
1. Anonymous manuscript
2. Separate title page
```

The article should use the Springer Nature journal template, not the LNCS conference template.

The recommended LaTeX class is:

```latex
\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}
```

The project should eventually include:

```text
article/manuscript/
article/templates/
article/figures/
article/tables/
article/cover_letter/
article/references/
```

---

## 5. Project Goal

The goal is to produce a journal-level benchmark article that substantially extends the previous conference work.

The article must address the weaknesses identified in the IJCNN reviews by adding:

* multiple optimizer baselines;
* fair comparison by number of fitness evaluations;
* temporal validation;
* multiple random seeds;
* convergence curves;
* runtime analysis;
* stability analysis;
* statistical tests;
* ablation studies;
* financial performance metrics;
* transparent reproducible configuration files.

The new contribution is not:

```text
GA improves MLP.
```

The new contribution is:

```text
A controlled benchmark of evolutionary and swarm intelligence optimizers for neural intraday trend classification in Brazilian futures markets.
```

---

## 6. Current Repository Organization

The repository is organized as follows:

```text
nca-optimizer-benchmark/
├── article/
├── checkpoints/
├── config/
├── data/
├── docs/
├── experiments/
├── logs/
├── notebooks/
├── outputs/
├── scripts/
├── src/
├── README.md
├── ROADMAP.md
├── RUNBOOK.md
├── TASKS.md
├── PROJECT_CONTEXT.md
└── requirements.txt
```

### `article/`

Contains manuscript-related material.

Important subfolders:

```text
article/references/
article/manuscript/
article/figures/
article/tables/
article/templates/
article/cover_letter/
```

The `references/` folder contains the three key PDF files that define the research lineage and target-journal benchmark model.

### `experiments/train_model/`

Contains the historical IJCNN experimental files.

This folder should be treated as **legacy experimental material**.

It includes:

* old MLP-GA code;
* Random Forest GA code;
* previous checkpoints;
* figures used in the IJCNN version;
* previous logs;
* previous dataset file `merged_output.csv`;
* previous technical explanation file.

Do not build the new journal pipeline directly inside this folder. Use it only for reproduction and reference.

### `src/`

This is where the clean implementation for the journal article must live.

Main responsibilities:

```text
src/data_loader.py
src/preprocessing.py
src/feature_engineering.py
src/feature_selection.py
src/temporal_split.py
src/models/mlp.py
src/objective.py
src/optimizers/
src/evaluation/
src/utils/
```

### `scripts/`

This folder contains executable experiment scripts.

Planned scripts:

```text
00_reproduce_iccsa_baseline.py
01_reproduce_ijcnn_baseline.py
02_run_random_search.py
03_run_ga.py
04_run_pso.py
05_run_de.py
06_run_gwo.py
07_compare_optimizers.py
08_run_statistical_tests.py
09_generate_paper_figures.py
```

Scripts should be thin wrappers around reusable code in `src/`.

### `config/`

Configuration files should define paths, experiment parameters, and search spaces.

Expected files:

```text
assets_universe.yaml
experiment_config.yaml
paths.yaml
search_spaces.yaml
```

### `outputs/`

This folder stores all experiment outputs.

Expected subfolders:

```text
outputs/metrics/
outputs/predictions/
outputs/figures/
outputs/tables/
outputs/backtests/
outputs/statistical_tests/
outputs/reports/
```

### `checkpoints/`

Stores trained models and optimizer checkpoints.

Expected subfolders:

```text
checkpoints/ga/
checkpoints/pso/
checkpoints/de/
checkpoints/gwo/
checkpoints/final_models/
```

---

## 7. Data Context

The historical experiments use:

```text
data/raw/merged_output.csv
```

This file contains preprocessed 5-minute Mini-Index futures data with:

* datetime;
* OHLC prices;
* volume;
* trading-related fields;
* technical indicators;
* normalized indicators;
* trend labels.

The previous experiments used 66 features and a binary target:

```text
downtrend → 0
uptrend   → 1
```

The previous best feature subset came from Information Gain:

```text
InfoGain_[7] = [30, 52, 31, 53, 42, 33, 41]
```

The previous experiments converted these indices into feature names using the column order from the dataset.

For the first journal benchmark prototype, reuse the same 7 selected features to reduce changes and isolate the effect of the optimizer.

Later, extend the study to:

```text
WIN
IND
WDO
DOL
```

The broader goal is to evaluate Brazilian futures markets through mini and full contracts:

```text
Mini Index  → WIN
Full Index  → IND
Mini Dollar → WDO
Full Dollar → DOL
```

---

## 8. Methodological Rules for the New Journal Pipeline

The new journal pipeline must follow these rules.

### Rule 1 — Do not use random sampling across the whole period as the main protocol

The IJCNN experiment used balanced random sampling:

```text
1500 downtrend + 1500 uptrend for training
remaining samples for testing
```

This is useful as a historical baseline, but it weakens the temporal interpretation of financial forecasting.

For the journal paper, the main protocol must be temporal:

```text
train → validation → test
```

No shuffle should be used in the primary experiment.

### Rule 2 — Use one common objective function

All optimizers must call the same objective function.

The central function should be:

```python
evaluate_candidate(candidate, X_train, y_train, X_val, y_val, config)
```

This function should:

1. decode candidate hyperparameters;
2. train the MLP;
3. evaluate on validation data;
4. compute metrics;
5. return fitness and metric details.

### Rule 3 — Use the same computational budget

All optimizers must receive the same number of fitness evaluations.

Do not compare GA by number of generations and PSO by number of iterations directly.

The common comparison unit is:

```text
number of fitness evaluations
```

Example:

```text
Random Search: 100 sampled candidates
GA: 10 individuals × 10 generations = 100 evaluations
PSO: 10 particles × 10 iterations = 100 evaluations
DE: 10 individuals × 10 generations = 100 evaluations
GWO: 10 wolves × 10 iterations = 100 evaluations
```

### Rule 4 — Use multiple seeds

The old IJCNN experiment used limited stochastic replication.

The journal version must use multiple seeds.

Prototype:

```text
5 seeds
```

Final article:

```text
20–30 seeds
```

### Rule 5 — Do not rely only on accuracy

Accuracy alone is not sufficient for financial classification.

Use at least:

```text
Accuracy
Balanced Accuracy
Precision
Recall
F1-score
MCC
AUC-ROC
AUC-PR
```

MCC and F1-score should be central validation metrics.

Recommended initial fitness:

```text
fitness = 0.60 * MCC + 0.40 * F1
```

### Rule 6 — Save predictions and metrics

For every optimizer, seed, and evaluation, save:

```text
optimizer
seed
evaluation
candidate hyperparameters
validation metrics
fitness
runtime
```

For each best model, save:

```text
test predictions
test probabilities
test metrics
confusion matrix
runtime
selected hyperparameters
```

### Rule 7 — Include convergence analysis

For each optimizer, save and plot:

```text
best fitness by evaluation
mean fitness by evaluation
standard deviation across seeds
```

Figures should use:

```text
x-axis: fitness evaluations
y-axis: best validation fitness
```

Do not use only “generation” as the x-axis when comparing different optimizers.

### Rule 8 — Add statistical testing

The final benchmark should use:

```text
Friedman test
Wilcoxon signed-rank test
Holm correction
effect size
```

### Rule 9 — Add financial evaluation

The journal paper should include at least a simple trading evaluation:

```text
if prediction = uptrend → long
if prediction = downtrend → out or short
```

Report:

```text
cumulative return
Sharpe ratio
maximum drawdown
profit factor
number of trades
transaction cost sensitivity
```

This is necessary because IJCNN reviewers criticized the absence of economic evaluation.

---

## 9. Initial Implementation Order

The implementation should proceed in this order.

### Step 1 — Configuration

Create and populate:

```text
config/paths.yaml
config/experiment_config.yaml
config/search_spaces.yaml
```

### Step 2 — Core utilities

Implement:

```text
src/utils/seeds.py
src/utils/io.py
src/utils/logger.py
```

### Step 3 — Data pipeline

Implement:

```text
src/data_loader.py
src/preprocessing.py
src/feature_selection.py
src/temporal_split.py
```

### Step 4 — Model and metrics

Implement:

```text
src/models/mlp.py
src/evaluation/metrics.py
```

### Step 5 — Objective function

Implement:

```text
src/objective.py
```

This is the central component of the project.

### Step 6 — First optimizer baseline

Implement:

```text
src/optimizers/random_search.py
scripts/02_run_random_search.py
```

The first test should run Random Search before GA or PSO.

### Step 7 — Add GA and PSO

Implement:

```text
src/optimizers/ga.py
src/optimizers/pso.py
scripts/03_run_ga.py
scripts/04_run_pso.py
```

### Step 8 — Compare

Implement:

```text
scripts/07_compare_optimizers.py
```

### Step 9 — Expand

Add:

```text
src/optimizers/de.py
src/optimizers/gwo.py
scripts/05_run_de.py
scripts/06_run_gwo.py
```

---

## 10. Expected First Benchmark

The first benchmark should be:

```text
Dataset: data/raw/merged_output.csv
Features: InfoGain_[7]
Model: MLP
Split: temporal holdout
Optimizers: Random Search, GA, PSO
Seeds: 5
Evaluations per seed: 100
Fitness: 0.60 * MCC + 0.40 * F1
Metrics: Accuracy, Balanced Accuracy, Precision, Recall, F1, MCC, AUC-ROC, AUC-PR
Outputs: metrics, predictions, convergence curves, runtime
```

This first benchmark is not the final paper result. It is the proof that the new pipeline works.

---

## 11. Expected Journal-Level Benchmark

The final benchmark should be:

```text
Dataset: Brazilian futures intraday data
Assets: WIN, IND, WDO, DOL
Frequency: initially 5-minute legacy data, later expandable to 1-minute data
Features: technical indicators and selected feature subsets
Model: MLP baseline
Optimizers: Random Search, GA, PSO, DE, GWO
Seeds: 20–30
Evaluation budget: fixed and equal across all optimizers
Validation: temporal / walk-forward
Metrics: predictive, optimization, statistical, and financial
```

Optional extension:

```text
Bayesian Optimization
CMA-ES
ABC
```

---

## 12. Writing Strategy

The article should not be written as:

```text
We improved a previous GA-based model by adding PSO.
```

It should be written as:

```text
We conduct a controlled benchmark of evolutionary and swarm intelligence optimizers for neural intraday trend classification under real-world financial constraints.
```

The connection to previous work should be transparent:

```text
A previous conference version investigated feature selection for Random Forest models using Brazilian mini-index futures. A subsequent extension explored GA-based hyperparameter optimization for RF, SVM, and MLP models. The present study substantially extends this line by shifting the focus from a single optimizer to a controlled benchmark of optimizer families, adding temporal validation, convergence analysis, statistical testing, and financial evaluation.
```

---

## 13. Non-Negotiable Scientific Requirements

Before submission to Neural Computing and Applications, the project must include:

```text
1. Clear research gap.
2. Strong related work with recent Neural Computing and Applications papers.
3. Temporal validation protocol.
4. No data leakage.
5. Equal optimizer budget.
6. Multiple seeds.
7. Random Search baseline.
8. GA and PSO at minimum.
9. DE and GWO for final benchmark.
10. MCC/F1/AUC metrics.
11. Convergence curves.
12. Runtime analysis.
13. Statistical tests.
14. Financial backtesting.
15. Reproducible configs.
16. Anonymous manuscript.
17. Separate title page.
18. Data/code availability statement.
```

---

## 14. Assistant Behavior for This Project

When assisting with this repository, follow these principles:

1. Prefer complete code files over fragments.
2. Keep code modular and reusable.
3. Do not duplicate experimental logic across optimizer scripts.
4. Centralize evaluation in `src/objective.py`.
5. Centralize metrics in `src/evaluation/metrics.py`.
6. Centralize data loading and splitting.
7. Avoid ad hoc notebooks for core results.
8. All experiments must save machine-readable outputs.
9. All random processes must accept explicit seeds.
10. All figures must be reproducible from saved CSV files.
11. Prioritize journal-level rigor over quick accuracy gains.
12. Treat the IJCNN rejection as a reviewer-guided roadmap.
13. Treat the ICCSA paper as the accepted baseline study.
14. Treat the Springer benchmark article as the methodological model for the new submission.

---

## 15. Current Immediate Goal

The immediate goal is to implement the first clean benchmark pipeline:

```text
Random Search vs GA vs PSO
```

using:

```text
MLP
InfoGain_[7]
temporal split
fixed evaluation budget
multiple seeds
MCC/F1-based fitness
saved metrics and convergence outputs
```

Only after this first benchmark works should the project expand to DE, GWO, financial backtesting, statistical tests, and multi-asset experiments.

