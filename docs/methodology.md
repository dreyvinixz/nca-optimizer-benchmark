# Methodology

This project follows the methodological spirit of a recent Neural Computing and
Applications optimizer benchmark in solar PV forecasting, adapted to Brazilian
futures trend classification.

The central question is which optimizer family is more suitable for tuning an
MLP under realistic financial time-series constraints.

## Model

The first benchmark uses a compact MLP:

```text
Input
Dense(hidden_neurons, tanh, L2)
Dropout(dropout_rate)
Dense(1, sigmoid)
```

The intended neural optimizer is RMSprop with binary cross-entropy. When
TensorFlow is unavailable, the implementation uses an sklearn MLP fallback so
the benchmark pipeline remains executable and reproducible.

## Metrics

The benchmark reports accuracy, balanced accuracy, precision, recall, F1, MCC,
AUC-ROC, AUC-PR, confusion matrix, and runtime.

MCC and F1 are central because accuracy alone is weak for financial
classification and can hide class-imbalance behavior.

## Reproducibility

All scripts are config-driven and save CSV outputs. Figures and summaries are
generated from saved CSV files, not manually typed values.
