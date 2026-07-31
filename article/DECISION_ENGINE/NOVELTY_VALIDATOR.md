# NOVELTY VALIDATOR — Novelty Grading & Anti-Overclaiming Matrix
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/DECISION_ENGINE/NOVELTY_VALIDATOR.md`  

---

## 1. The 5 Novelty Levels

To enforce total scientific honesty and prevent overclaiming, every technical innovation in the project is assigned a Novelty Level between 0 and 4.

```
Level 0: Not Novel (Standard baseline usage / pre-existing tool)
Level 1: Incremental (Minor tuning or slight parameter adjustment)
Level 2: Methodological (New evaluation protocol, fitness formulation, or benchmark setup)
Level 3: Experimental / Domain Protocol (First controlled application to a specific high-frequency asset dataset)
Level 4: Conceptual (Groundbreaking new mathematical algorithm or fundamental theoretical paradigm)
```

---

## 2. Novelty Classification Matrix for Project Innovations

| Innovation Aspect | Claimed Feature | Novelty Level | Can We Claim Novelty? | Permitted Phrasing in Manuscript |
| :--- | :--- | :---: | :---: | :--- |
| **Multilayer Perceptron (MLP)** | Base neural classifier model. | **Level 0** | **NO** | *"We employ a standard Multilayer Perceptron as the universal function approximator..."* |
| **Information Gain Selection** | 7-feature subset (`InfoGain_[7]`). | **Level 0** | **NO** | *"Building on prior accepted work (Souza et al., 2025), we utilize the Information Gain feature subset..."* |
| **Individual Optimizers (GA, PSO, DE, GWO)** | Basic algorithm implementations. | **Level 0** | **NO** | *"We evaluate five established metaheuristic and stochastic optimizer families..."* |
| **Equal-Budget Multi-Optimizer Protocol** | $N_{\text{eval}} = 1,500$ cap across 5 optimizers. | **Level 2** | **YES** | *"We introduce a controlled equal-budget benchmark framework evaluating five optimizer families under an identical evaluation budget..."* |
| **Leakage-Free 60/20/20 Temporal Split** | Sequential split with `shuffle = false` on 5-min WIN futures. | **Level 3** | **YES** | *"We establish a strict leakage-free sequential temporal validation protocol over 15,057 intraday instances of B3 Mini-Index futures..."* |
| **Compound MCC-Driven Fitness** | $f(\boldsymbol{\theta}) = 0.60\text{MCC} + 0.40F_1$. | **Level 2** | **YES** | *"We formulate a compound MCC-driven objective function designed to resist class imbalance distortion..."* |
| **Out-of-Sample Financial Backtest** | Trading simulation under 0.01% fee tiers. | **Level 3** | **YES** | *"We evaluate out-of-sample financial performance under realistic transaction fee structures..."* |

---

## 3. Anti-Overclaiming Rules

1. **Rule of Level 0 Honesty**: Never present Level 0 elements (MLP, standard GA, Information Gain) as new contributions. Always attribute them to baseline literature.
2. **Rule of Level 4 Prohibition**: Do NOT claim Level 4 conceptual novelty (e.g., claiming to have invented a new fundamental optimization theory). Our contributions are Level 2 (Methodological) and Level 3 (Experimental/Domain Protocol).
3. **Rule of Conditional Permission**: Any sentence asserting novelty must explicitly state the Level 2/3 boundary conditions (*"for intraday trend classification in Brazilian futures markets"*).
