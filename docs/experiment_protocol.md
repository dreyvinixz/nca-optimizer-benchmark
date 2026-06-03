# Experiment Protocol

The first clean benchmark compares Random Search, GA, and PSO under a common
evaluation budget.

## Data

- Source: `data/raw/merged_output.csv`
- Target: `trend`
- Mapping: `downtrend -> 0`, `uptrend -> 1`
- Features: historical `InfoGain_[7] = [30, 52, 31, 53, 42, 33, 41]`

The feature indices are resolved over modeling columns after excluding
`datetime` and `trend`.

## Split

The primary protocol is chronological:

```text
60% train
20% validation
20% test
```

No shuffle is used. The test split is untouched during optimization.

## Objective

All optimizers call `src/objective.py::evaluate_candidate`.

```text
fitness = 0.60 * MCC + 0.40 * F1
```

The scaler is fit only on the training split inside model training.

## Optimizer Budget

All optimizers use 100 fitness evaluations per seed:

- Random Search: 100 sampled candidates
- GA: 10 population members x 10 generations
- PSO: 10 particles x 10 iterations

Convergence plots use `fitness evaluations` on the x-axis.
