# SKILLS.md — Implementation Skills and Research Rules

## 1. Purpose of this File

This file defines the technical and methodological skills required to work on this repository.

The project is a journal-level research implementation for a paper targeted at **Neural Computing and Applications**. The main goal is to build a reproducible benchmark of evolutionary and swarm intelligence optimizers for neural intraday trend classification in Brazilian futures markets.

All implementation must prioritize:

* scientific rigor;
* reproducibility;
* modularity;
* temporal validation;
* fair optimizer comparison;
* clean experiment outputs;
* journal-level methodological standards.

---

## 2. Core Research Objective

The project must not be treated as a simple code experiment.

The central research question is:

> Which optimizer families are more suitable for tuning neural models in short-horizon intraday financial trend classification under real-world market constraints?

The benchmark should compare, at minimum:

* Random Search;
* Genetic Algorithm;
* Particle Swarm Optimization;
* Differential Evolution;
* Grey Wolf Optimizer.

The first minimal benchmark should compare:

```text
Random Search vs GA vs PSO
```

Only after this works should the project expand to:

```text
Random Search vs GA vs PSO vs DE vs GWO
```

---

## 3. Historical Context

This project extends a previous research line.

### ICCSA Accepted Paper

The accepted ICCSA paper studied:

* technical indicators;
* feature selection;
* Random Forest;
* Brazilian Mini-Index futures;
* 5-minute intraday data;
* full feature set vs reduced feature subsets.

The main result was that **Information Gain with 7 selected features** improved test generalization compared to the full feature set.

### IJCNN Rejected Extension

The IJCNN extension added:

* Genetic Algorithm optimization;
* Random Forest;
* SVM;
* MLP;
* the same Information Gain feature subset.

The best result was obtained by:

```text
MLP + GA + RMSprop
```

with approximately:

```text
Test Accuracy ≈ 65.85%
AUC-ROC ≈ 0.7032
AUC-PR ≈ 0.7029
```

However, the IJCNN reviewers criticized:

* limited novelty;
* weak optimizer comparison;
* lack of temporal validation;
* potential data leakage;
* lack of economic evaluation;
* lack of statistical tests;
* lack of ablation studies;
* excessive reliance on accuracy and F1-score.

The new journal version must directly address these issues.

---

## 4. Implementation Philosophy

The repository must be organized as a clean research pipeline, not as isolated scripts.

Avoid:

```text
copy-paste experiments
hardcoded paths
hardcoded metrics
manual-only plotting
one-off notebooks
random sampling across the whole period as the main protocol
optimizer-specific objective functions
```

Prefer:

```text
modular src/ code
thin scripts/
YAML configuration
single objective function
centralized metrics
saved predictions
saved convergence data
saved runtime logs
reproducible figures
multiple seeds
temporal split
```

---

## 5. Repository Responsibilities

### `src/`

Contains reusable implementation.

Expected responsibilities:

```text
src/data_loader.py              Load datasets
src/preprocessing.py            Clean and prepare data
src/feature_engineering.py      Generate features
src/feature_selection.py        Select features
src/temporal_split.py           Create temporal splits
src/objective.py                Central candidate evaluation
src/models/mlp.py               MLP model definition
src/optimizers/                 Optimizer implementations
src/evaluation/                 Metrics, backtests, statistical tests
src/utils/                      Seeds, logging, IO helpers
```

### `scripts/`

Contains runnable experiment entrypoints.

Scripts must be thin. They should call functions from `src/`.

Expected scripts:

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

### `config/`

Contains experiment definitions.

Expected files:

```text
paths.yaml
experiment_config.yaml
search_spaces.yaml
assets_universe.yaml
```

### `outputs/`

Stores all generated results.

Expected folders:

```text
outputs/metrics/
outputs/predictions/
outputs/figures/
outputs/tables/
outputs/backtests/
outputs/statistical_tests/
outputs/reports/
```

### `experiments/train_model/`

Contains legacy IJCNN experiment files.

This folder is historical material. Do not build the new journal pipeline directly inside it.

Use this folder only to:

* reproduce previous results;
* inspect old GA/MLP implementation;
* compare historical results;
* recover previous checkpoints or figures.

---

## 6. Central Design Rule

All optimizers must call the same objective function.

The central function must be similar to:

```python
def evaluate_candidate(candidate, X_train, y_train, X_val, y_val, config):
    ...
```

It must:

1. decode candidate hyperparameters;
2. build the MLP;
3. train the model;
4. evaluate validation predictions;
5. compute metrics;
6. return fitness and detailed metric logs.

Do not implement separate metric logic inside each optimizer.

Wrong:

```text
GA has its own evaluation function
PSO has its own evaluation function
DE has its own evaluation function
```

Correct:

```text
GA  → evaluate_candidate()
PSO → evaluate_candidate()
DE  → evaluate_candidate()
GWO → evaluate_candidate()
Random Search → evaluate_candidate()
```

---

## 7. Temporal Validation Rule

This project deals with financial time series.

The main experiment must not use random train/test splitting across the whole period.

The preferred protocol is:

```text
train → validation → test
```

with chronological order preserved.

The first clean benchmark may use:

```text
60% train
20% validation
20% test
```

without shuffle.

Later, the project should move to:

```text
walk-forward validation
external test month
```

If balancing is needed, it should be performed only within the training set, never across the entire dataset.

---

## 8. Optimizer Fairness Rule

All optimizers must have the same number of fitness evaluations.

Do not compare by raw number of generations or iterations.

Correct comparison unit:

```text
fitness evaluations
```

Example:

```text
Random Search: 100 sampled candidates
GA: 10 individuals × 10 generations = 100 evaluations
PSO: 10 particles × 10 iterations = 100 evaluations
DE: 10 individuals × 10 generations = 100 evaluations
GWO: 10 wolves × 10 iterations = 100 evaluations
```

When plotting convergence, use:

```text
x-axis: fitness evaluations
y-axis: best validation fitness
```

---

## 9. Required Metrics

Accuracy alone is not enough.

Every experiment should report:

```text
Accuracy
Balanced Accuracy
Precision
Recall
F1-score
MCC
AUC-ROC
AUC-PR
Confusion Matrix
Runtime
```

The preferred initial fitness is:

```text
fitness = 0.60 * MCC + 0.40 * F1
```

Accuracy can be reported, but it should not be the only central metric.

---

## 10. Required Outputs Per Experiment

Each optimizer run must save machine-readable results.

For each candidate evaluation, save:

```text
experiment_name
optimizer
seed
evaluation_id
fitness
accuracy_val
balanced_accuracy_val
precision_val
recall_val
f1_val
mcc_val
auc_roc_val
auc_pr_val
runtime_seconds
neurons
learning_rate
l2_alpha
dropout_rate
batch_size
```

For each best model per seed, save:

```text
test predictions
test probabilities
test metrics
confusion matrix
best hyperparameters
runtime
```

For convergence analysis, save:

```text
optimizer
seed
evaluation_id
best_fitness_so_far
mean_fitness_so_far
```

---

## 11. Randomness and Reproducibility

Every stochastic process must accept an explicit seed.

This includes:

* NumPy;
* Python random;
* TensorFlow;
* optimizer initialization;
* candidate sampling;
* train/validation procedures.

Use a central seed utility in:

```text
src/utils/seeds.py
```

A function such as:

```python
def set_global_seed(seed: int) -> None:
    ...
```

should set all relevant random states.

---

## 12. Model Rules

The first benchmark should use a simple MLP.

The model should be defined in:

```text
src/models/mlp.py
```

Initial architecture:

```text
Input
Dense(hidden_neurons, activation=tanh)
Dropout(dropout_rate)
Dense(1, activation=sigmoid)
```

Initial tunable hyperparameters:

```text
hidden_neurons
learning_rate
l2_alpha
dropout_rate
batch_size
```

Initial fixed values:

```text
activation = tanh
optimizer = RMSprop
loss = binary_crossentropy
```

Do not add LSTM, CNN-LSTM, TCN, or Transformer before the optimizer benchmark is working.

---

## 13. Search Space Rules

The first benchmark should use the historical IJCNN-inspired search space:

```text
hidden_neurons: 5 to 500
learning_rate: 1e-8 to 1e-2
l2_alpha: 1e-8 to 1e-2
dropout_rate: 0.00 to 0.10
batch_size: [16, 32, 64, 80, 112, 128]
```

For continuous optimizers such as PSO and DE, learning rate and L2 must be optimized in log scale:

```text
log10_learning_rate
log10_l2_alpha
```

Then decoded as:

```python
learning_rate = 10 ** log10_learning_rate
l2_alpha = 10 ** log10_l2_alpha
```

---

## 14. Initial Features

For the first clean benchmark, use the historical Information Gain subset:

```text
InfoGain_[7] = [30, 52, 31, 53, 42, 33, 41]
```

These are feature indices from the historical dataset column order.

The code must convert these indices into feature names using the loaded dataset columns.

Later versions may test:

```text
full feature set
InfoGain selected features
optimizer-selected feature masks
```

But do not add feature-mask optimization before the basic optimizer benchmark is stable.

---

## 15. Financial Evaluation

The final journal version must include a simple financial evaluation.

Minimum strategy:

```text
if prediction = uptrend → long
if prediction = downtrend → out or short
```

Report at least:

```text
cumulative return
Sharpe ratio
maximum drawdown
profit factor
number of trades
transaction cost sensitivity
```

This is necessary because previous reviews criticized the absence of economic evaluation.

---

## 16. Statistical Testing

The final benchmark must include statistical tests.

Use:

```text
Friedman test
Wilcoxon signed-rank test
Holm correction
effect size
```

These should be implemented in:

```text
src/evaluation/statistical_tests.py
```

and executed by:

```text
scripts/08_run_statistical_tests.py
```

---

## 17. Figure Generation Rules

Figures must be generated from saved CSV files, not from manually typed values.

Expected figures:

```text
optimizer convergence curves
validation vs test performance
runtime comparison
MCC/F1/AUC comparison
confusion matrices
financial backtest curves
feature selection frequency, if applicable
```

Figures should be saved in:

```text
outputs/figures/
```

Paper-ready copies should be exported to:

```text
article/figures/
```

---

## 18. Article Writing Rules

The paper must not be framed as:

```text
We added PSO to a previous GA model.
```

It must be framed as:

```text
We conduct a controlled benchmark of evolutionary and swarm intelligence optimizers for neural intraday trend classification under real-world financial constraints.
```

The paper should transparently explain the relation to previous work:

```text
A previous conference version studied feature selection for Random Forest models in Brazilian mini-index futures. A later extension explored GA-based hyperparameter optimization for RF, SVM, and MLP models. The present work substantially extends this research line by shifting the focus from a single optimizer to a controlled optimizer benchmark, adding temporal validation, convergence analysis, statistical testing, and financial evaluation.
```

---

## 19. Coding Style

Use:

* clear function names;
* type hints where practical;
* docstrings for public functions;
* small modules with clear responsibility;
* no hardcoded Windows paths inside `src/`;
* YAML config for paths and experiment parameters;
* CSV outputs for all experiment results.

Avoid:

* large monolithic scripts;
* hidden global state;
* hardcoded experiment settings;
* manual metrics written into plotting scripts;
* non-reproducible random behavior;
* optimizer-specific training logic.

---

## 20. Immediate Implementation Priority

The immediate implementation order is:

```text
1. config/paths.yaml
2. config/experiment_config.yaml
3. config/search_spaces.yaml
4. src/utils/seeds.py
5. src/utils/io.py
6. src/data_loader.py
7. src/temporal_split.py
8. src/models/mlp.py
9. src/evaluation/metrics.py
10. src/objective.py
11. src/optimizers/random_search.py
12. scripts/02_run_random_search.py
```

After Random Search works:

```text
13. src/optimizers/ga.py
14. src/optimizers/pso.py
15. scripts/03_run_ga.py
16. scripts/04_run_pso.py
17. scripts/07_compare_optimizers.py
```

Only then expand to:

```text
DE
GWO
backtesting
statistical tests
multi-asset experiments
```

---

## 21. Final Scientific Standard

Before submitting to Neural Computing and Applications, the project must satisfy:

```text
temporal validation
no data leakage
equal optimizer budget
multiple seeds
strong baselines
predictive metrics
financial metrics
runtime analysis
convergence analysis
statistical tests
ablation studies
reproducible configuration
anonymous manuscript
separate title page
data availability statement
code availability statement
```

If an implementation decision improves short-term accuracy but weakens reproducibility, temporal validity, or scientific rigor, reject that decision.
