---
name: metaheuristic-optimizer-benchmark
description: Guidelines for benchmarking, configuring, running, and statistically analyzing evolutionary and swarm intelligence optimizers (RS, GA, PSO, DE, GWO) under equal evaluation budgets.
---

# Metaheuristic Optimizer Benchmark Skill

Use this skill when modifying, running, or analyzing hyperparameter optimization experiments for neural network intraday classifiers.

## 1. Controlled Experimental Design

- **Optimizers**: Random Search (RS), Genetic Algorithm (GA), Particle Swarm Optimization (PSO), Differential Evolution (DE), Grey Wolf Optimizer (GWO).
- **Equal Evaluation Budget**: Enforce $N_{eval} = 1,500$ fitness evaluations per optimizer seed.
- **MLP Search Space**:
  - Hidden Layer 1: $[16, 256]$
  - Hidden Layer 2: $[0, 128]$
  - Learning Rate ($lr$): $[10^{-4}, 10^{-1}]$ (log scale)
  - Batch Size: $\{32, 64, 128, 256\}$
  - Dropout Rate: $[0.0, 0.5]$
  - L2 Regularization ($\alpha$): $[10^{-6}, 10^{-2}]$ (log scale)
- **Objective Function**: $f(\boldsymbol{\theta}) = 0.60 \times \text{MCC} + 0.40 \times F_1$.

## 2. Statistical & Economic Analysis Protocol

1. **Hypothesis Testing**: Apply non-parametric Friedman test followed by paired Wilcoxon signed-rank tests with Holm-Bonferroni correction ($p < 0.05$).
2. **Effect Size**: Calculate Cohen's $d$ ($|d| > 0.8$ for large effect).
3. **Financial Backtest**: Evaluate Sharpe ratio, Net Return %, Max Drawdown (MDD), Profit Factor, and trade frequency under realistic brokerage/slippage fees.
