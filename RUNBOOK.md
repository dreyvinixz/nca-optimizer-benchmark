# RUNBOOK.md — NCA Optimizer Benchmark

Status: draft
Last update: 2026-06-03
Target journal: Neural Computing and Applications
Project: nca-optimizer-benchmark

---

## 1. Purpose

This runbook defines the operational workflow for implementing, running, validating, and documenting the optimizer benchmark experiments for the Neural Computing and Applications article.

The project investigates evolutionary and swarm intelligence optimizers for neural intraday trend classification in Brazilian futures markets.

The repository must remain reproducible, modular, and journal-ready.

---

## 2. Core Workflow

Keep requirements, configurations, code, evidence, drafts, and final exports separated.

Suggested cycle:

```text
context → requirements → implementation → experiment → evidence → analysis → paper figures → manuscript → review → submission
```

Operational cycle:

```text
PROJECT_CONTEXT.md
        ↓
SKILLS.md
        ↓
config/
        ↓
src/
        ↓
scripts/
        ↓
outputs/
        ↓
article/
```

---

## 3. Main Scientific Objective

The current journal article must not be treated as a simple extension that only adds PSO to the previous GA-based model.

The central contribution is:

```text
A controlled benchmark of evolutionary and swarm intelligence optimizers for neural intraday trend classification under real-world financial constraints.
```

Initial benchmark:

```text
Random Search vs GA vs PSO
```

Final benchmark:

```text
Random Search vs GA vs PSO vs DE vs GWO
```

---

## 4. Repository Areas

### `PROJECT_CONTEXT.md`

Explains the scientific context, research lineage, target journal, previous papers, and project motivation.

Use this file when an AI assistant or collaborator needs to understand the project before coding.

### `SKILLS.md`

Defines how work should be done in this repository.

It includes rules for:

```text
implementation
optimizer fairness
temporal validation
metrics
outputs
figures
statistical tests
financial evaluation
```

### `config/`

Stores all experiment definitions.

Expected files:

```text
config/paths.yaml
config/experiment_config.yaml
config/search_spaces.yaml
config/assets_universe.yaml
```

Do not hardcode paths or experiment parameters inside `src/`.

### `src/`

Contains reusable implementation.

Expected modules:

```text
src/data_loader.py
src/preprocessing.py
src/feature_engineering.py
src/feature_selection.py
src/temporal_split.py
src/objective.py
src/models/mlp.py
src/optimizers/random_search.py
src/optimizers/ga.py
src/optimizers/pso.py
src/optimizers/de.py
src/optimizers/gwo.py
src/evaluation/metrics.py
src/evaluation/backtest.py
src/evaluation/statistical_tests.py
src/utils/seeds.py
src/utils/io.py
src/utils/logger.py
```

### `scripts/`

Contains executable experiment scripts.

Scripts should be thin wrappers around `src/`.

Expected scripts:

```text
scripts/00_reproduce_iccsa_baseline.py
scripts/01_reproduce_ijcnn_baseline.py
scripts/02_run_random_search.py
scripts/03_run_ga.py
scripts/04_run_pso.py
scripts/05_run_de.py
scripts/06_run_gwo.py
scripts/07_compare_optimizers.py
scripts/08_run_statistical_tests.py
scripts/09_generate_paper_figures.py
```

### `experiments/train_model/`

Legacy folder containing previous IJCNN experimental material.

Use it only for:

```text
reproducing previous results
checking historical parameters
recovering old figures
recovering old checkpoints
understanding the prior GA/MLP implementation
```

Do not build the new journal pipeline inside this folder.

### `outputs/`

Stores generated experimental evidence.

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

### `article/`

Stores paper-related files.

Expected subfolders:

```text
article/manuscript/
article/figures/
article/tables/
article/references/
article/templates/
article/cover_letter/
article/overleaf_zips/
```

---

## 5. Initial Setup

### 5.1 Create virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 5.2 Install dependencies

```bash
pip install -r requirements.txt
```

### 5.3 Confirm project structure

Run:

```bash
python generate_project_map.py
```

Expected output:

```text
project_map.md
```

Check that the following folders exist:

```text
config/
src/
scripts/
outputs/
article/
experiments/train_model/
```

---

## 6. Configuration Order

Before running experiments, fill these files:

```text
config/paths.yaml
config/experiment_config.yaml
config/search_spaces.yaml
```

Recommended order:

```text
1. paths.yaml
2. experiment_config.yaml
3. search_spaces.yaml
```

### 6.1 `paths.yaml`

Must define:

```text
legacy dataset path
outputs paths
checkpoint paths
logs paths
```

The legacy IJCNN dataset should initially point to:

```text
data/raw/merged_output.csv
```

### 6.2 `experiment_config.yaml`

Must define:

```text
experiment name
target column
datetime column
selected features
split protocol
model settings
objective function
benchmark settings
seeds
evaluation budget
```

### 6.3 `search_spaces.yaml`

Must define MLP search space:

```text
hidden neurons
learning rate
L2 regularization
dropout rate
batch size
```

---

## 7. Implementation Order

Follow this order strictly.

### Step 1 — Utilities

Implement:

```text
src/utils/seeds.py
src/utils/io.py
src/utils/logger.py
```

Purpose:

```text
reproducibility
YAML loading
directory creation
CSV saving
logging
```

### Step 2 — Data pipeline

Implement:

```text
src/data_loader.py
src/preprocessing.py
src/feature_selection.py
src/temporal_split.py
```

Purpose:

```text
load merged_output.csv
map target labels
select InfoGain_[7] features
create temporal train/validation/test split
avoid shuffle in main protocol
```

### Step 3 — Model and metrics

Implement:

```text
src/models/mlp.py
src/evaluation/metrics.py
```

Purpose:

```text
build MLP
train MLP
compute accuracy, balanced accuracy, precision, recall, F1, MCC, AUC-ROC, AUC-PR
```

### Step 4 — Objective function

Implement:

```text
src/objective.py
```

This is the central file.

All optimizers must call the same objective function:

```python
evaluate_candidate(candidate, X_train, y_train, X_val, y_val, config)
```

### Step 5 — Random Search baseline

Implement:

```text
src/optimizers/random_search.py
scripts/02_run_random_search.py
```

Run Random Search before GA and PSO.

### Step 6 — GA and PSO

Implement:

```text
src/optimizers/ga.py
src/optimizers/pso.py
scripts/03_run_ga.py
scripts/04_run_pso.py
```

### Step 7 — Comparison script

Implement:

```text
scripts/07_compare_optimizers.py
```

It must read saved CSV files from `outputs/metrics/`, not manually typed values.

### Step 8 — Expand benchmark

After Random Search, GA, and PSO work, implement:

```text
src/optimizers/de.py
src/optimizers/gwo.py
scripts/05_run_de.py
scripts/06_run_gwo.py
```

---

## 8. Execution Order

### 8.1 Reproduce previous results

Optional but recommended:

```bash
python scripts/00_reproduce_iccsa_baseline.py
python scripts/01_reproduce_ijcnn_baseline.py
```

Purpose:

```text
confirm historical baselines
document continuity from ICCSA and IJCNN
```

### 8.2 Run first clean baseline

```bash
python scripts/02_run_random_search.py
```

Expected outputs:

```text
outputs/metrics/random_search_runs.csv
outputs/metrics/random_search_best_by_seed.csv
outputs/predictions/random_search_predictions.csv
outputs/metrics/convergence/random_search_convergence.csv
```

### 8.3 Run GA

```bash
python scripts/03_run_ga.py
```

Expected outputs:

```text
outputs/metrics/ga_runs.csv
outputs/metrics/ga_best_by_seed.csv
outputs/predictions/ga_predictions.csv
outputs/metrics/convergence/ga_convergence.csv
```

### 8.4 Run PSO

```bash
python scripts/04_run_pso.py
```

Expected outputs:

```text
outputs/metrics/pso_runs.csv
outputs/metrics/pso_best_by_seed.csv
outputs/predictions/pso_predictions.csv
outputs/metrics/convergence/pso_convergence.csv
```

### 8.5 Compare initial benchmark

```bash
python scripts/07_compare_optimizers.py
```

Expected outputs:

```text
outputs/tables/optimizer_comparison.csv
outputs/figures/optimizer_convergence.png
outputs/figures/optimizer_metrics_comparison.png
outputs/reports/optimizer_benchmark_summary.md
```

---

## 9. Minimum First Benchmark

The first clean benchmark must use:

```text
Dataset: data/raw/merged_output.csv
Features: InfoGain_[7]
Model: MLP
Split: temporal holdout
Optimizers: Random Search, GA, PSO
Seeds: 5
Evaluations per seed: 100
Fitness: 0.60 * MCC + 0.40 * F1
```

Required metrics:

```text
Accuracy
Balanced Accuracy
Precision
Recall
F1-score
MCC
AUC-ROC
AUC-PR
Runtime
```

Required analysis:

```text
best validation fitness
test metrics
runtime
convergence curve
best hyperparameters
```

---

## 10. Final Journal-Level Benchmark

The final version should use:

```text
Optimizers: Random Search, GA, PSO, DE, GWO
Seeds: 20–30
Equal evaluation budget across optimizers
Temporal or walk-forward validation
Predictive metrics
Financial metrics
Statistical tests
Runtime analysis
Convergence analysis
```

Possible assets:

```text
WIN
IND
WDO
DOL
```

---

## 11. Data Protocol

The main protocol must preserve time order.

Do not use random train/test splitting across the entire period as the primary journal experiment.

Allowed for historical reproduction:

```text
balanced random sampling
1500 downtrend + 1500 uptrend
```

Required for journal benchmark:

```text
chronological train/validation/test split
no shuffle
scaler fit only on training data
test set untouched during optimization
```

---

## 12. Objective Function Protocol

The objective function must:

1. receive candidate hyperparameters;
2. decode candidate;
3. build MLP;
4. fit scaler only on training data;
5. train the model;
6. predict validation data;
7. compute metrics;
8. compute fitness;
9. return complete logs.

Recommended first fitness:

```text
fitness = 0.60 * MCC + 0.40 * F1
```

Do not optimize directly on the test set.

---

## 13. Optimizer Fairness Protocol

All optimizers must use the same number of fitness evaluations.

Example:

```text
Random Search: 100 sampled candidates
GA: 10 individuals × 10 generations = 100 evaluations
PSO: 10 particles × 10 iterations = 100 evaluations
DE: 10 individuals × 10 generations = 100 evaluations
GWO: 10 wolves × 10 iterations = 100 evaluations
```

When comparing convergence, use:

```text
x-axis: fitness evaluations
y-axis: best validation fitness
```

---

## 14. Output Protocol

Each run must save:

```text
optimizer
seed
evaluation_id
candidate hyperparameters
validation metrics
fitness
runtime
```

Each best model must save:

```text
test predictions
test probabilities
test metrics
confusion matrix
best hyperparameters
runtime
```

Never rely only on console logs.

---

## 15. Figure Protocol

Figures must be generated from saved CSV files.

Do not hardcode metric values manually inside plotting scripts.

Expected figures:

```text
optimizer convergence curves
test metric comparison
runtime comparison
validation vs test comparison
confusion matrices
financial backtest curves
```

Save figures to:

```text
outputs/figures/
```

Copy paper-ready versions to:

```text
article/figures/
```

---

## 16. Statistical Testing Protocol

After all optimizer runs are complete:

```bash
python scripts/08_run_statistical_tests.py
```

Required tests:

```text
Friedman test
Wilcoxon signed-rank test
Holm correction
effect size
```

Outputs:

```text
outputs/statistical_tests/friedman_results.csv
outputs/statistical_tests/wilcoxon_holm_results.csv
outputs/statistical_tests/effect_sizes.csv
```

---

## 17. Financial Backtesting Protocol

The final paper must include simple economic evaluation.

Minimum rule:

```text
if prediction = uptrend → long
if prediction = downtrend → out or short
```

Required metrics:

```text
cumulative return
Sharpe ratio
maximum drawdown
profit factor
number of trades
transaction cost sensitivity
```

Save outputs to:

```text
outputs/backtests/
```

---

## 18. Manuscript Protocol

Paper files should be stored in:

```text
article/manuscript/
```

The target journal is double-blind, so prepare:

```text
anonymous manuscript
separate title page
```

Use Springer Nature journal template, not LNCS conference template.

Recommended class:

```latex
\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}
```

---

## 19. Pre-Submission Checklist

Before submission, confirm:

```text
[ ] Target journal requirements reviewed
[ ] Anonymous manuscript prepared
[ ] Separate title page prepared
[ ] Data availability statement written
[ ] Code availability statement written
[ ] Competing interests statement written
[ ] Funding statement written
[ ] Author contributions prepared
[ ] All figures exported in publication quality
[ ] All tables generated from output CSVs
[ ] All metrics reproducible
[ ] Multiple seeds used
[ ] Equal optimizer budget used
[ ] Temporal validation used
[ ] Statistical tests completed
[ ] Financial backtesting completed
[ ] Related work updated
[ ] Previous conference work cited transparently
```

---

## 20. Common Mistakes to Avoid

Avoid:

```text
using test data during optimization
using shuffle in main time-series split
manually typing figure values
comparing optimizers with different evaluation budgets
reporting only accuracy
running only one seed
using notebooks as the only source of results
building new code inside experiments/train_model/
```

Prefer:

```text
config-driven experiments
saved CSV evidence
central objective function
temporal split
multiple seeds
complete metrics
clear runtime logs
reproducible figures
```

---

## 21. Current Immediate Task

The immediate task is to implement and run:

```text
Random Search vs GA vs PSO
```

using:

```text
MLP
InfoGain_[7]
temporal split
MCC/F1 fitness
5 seeds
100 evaluations per seed
```

The first executable target is:

```bash
python scripts/02_run_random_search.py
```

Only after Random Search works should GA and PSO be implemented.

