# NCA Optimizer Benchmark

This repository supports a journal article targeted at **Neural Computing and
Applications**.

The scientific contribution is not a simple extension of a previous GA model.
The project reframes the work as a controlled benchmark of evolutionary and
swarm intelligence optimizers for neural intraday trend classification under
real-world financial constraints.

## Research Lineage

- ICCSA accepted paper: feature selection for Brazilian mini-index futures with
  Random Forest models.
- IJCNN extension: GA hyperparameter optimization for RF, SVM, and MLP.
- Current NCA project: controlled optimizer benchmark with temporal validation,
  equal evaluation budgets, multiple seeds, convergence analysis, and richer
  metrics.

## First Benchmark

The initial executable benchmark compares:

```text
Random Search vs GA vs PSO
```

Protocol:

```text
Dataset: data/raw/merged_output.csv
Features: InfoGain_[7]
Model: MLP
Split: temporal 60/20/20, no shuffle
Fitness: 0.60 * MCC + 0.40 * F1
Seeds: 5
Evaluations per seed: 100
```

## Installation

To run the official benchmark experiments, you must install the required dependencies (including TensorFlow/Keras). Run:

```powershell
pip install tensorflow scikit-learn pandas numpy pyyaml matplotlib
```

## Commands

```powershell
.\.venv\Scripts\python.exe scripts\02_run_random_search.py
.\.venv\Scripts\python.exe scripts\03_run_ga.py
.\.venv\Scripts\python.exe scripts\04_run_pso.py
.\.venv\Scripts\python.exe scripts\07_compare_optimizers.py
```

Outputs are saved under `outputs/metrics`, `outputs/predictions`,
`outputs/figures`, `outputs/tables`, and `outputs/reports`.

## Legacy Material

`experiments/train_model/` contains historical IJCNN code, checkpoints, logs,
and figures. It is reference material only and is not required by the clean
benchmark pipeline. The dataset used by the current pipeline lives in
`data/raw/merged_output.csv`.
