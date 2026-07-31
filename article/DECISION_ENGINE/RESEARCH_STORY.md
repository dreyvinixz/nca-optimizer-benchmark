# RESEARCH STORY — The Scientific Narrative Arc
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/DECISION_ENGINE/RESEARCH_STORY.md`  

---

## 1. The Core Scientific Storyline

Before any section of the manuscript is written, the underlying research story must be articulated. Academic writing does not merely report technical details; it materializes a cohesive scientific narrative.

```
1. Current Literature Paradigm
        ↓
2. Underlying Systemic Problem
        ↓
3. The Methodological Gap
        ↓
4. Why the Gap Matters (High Stakes)
        ↓
5. Central Research Hypothesis
        ↓
6. Proposed Methodological Framework
        ↓
7. Empirical Evidence
        ↓
8. Rigorous Validation & Statistical Proof
        ↓
9. Practical & Economic Implications
        ↓
10. Transparent Boundaries & Limitations
        ↓
11. Future Research Trajectory
```

---

## 2. Deconstruction of the 11 Story Arc Nodes

### Node 1: Current Literature Paradigm
- **Story Element**: Machine learning models, particularly Multilayer Perceptrons (MLPs), are increasingly applied to high-frequency intraday trend classification (e.g., 5-minute B3 Mini-Index futures) due to their universal function approximation capabilities.
- **Evidence**: [`PROJECT_MEMORY.md:Sec 1-3`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/PROJECT_MEMORY.md), Souza et al. (2025 ICCSA), Ecer et al. (2020).

### Node 2: Underlying Systemic Problem
- **Story Element**: Internal neural weight training via backpropagation is insufficient if hyperparameter selection is sub-optimal. Hyperparameter tuning defines a high-dimensional, non-convex, non-differentiable 6D search space where gradient descent breaks down and grid search becomes computationally intractable.
- **Evidence**: [`config/search_spaces.yaml`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/search_spaces.yaml), Gad (2022), Rajwar et al. (2023).

### Node 3: The Methodological Gap
- **Story Element**: Existing financial ML literature relies almost exclusively on single, default optimizers (e.g., standard GA or basic PSO) without conducting controlled multi-optimizer benchmarks under an identical evaluation budget. Published studies suffer from budget inequality, temporal data leakage, and a disconnect from financial metrics.
- **Evidence**: [`PROJECT_CONTEXT.md:Sec 2`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md), IJCNN 2026 reviewer critiques, Dhingra et al. (NCA 2025).

### Node 4: Why the Gap Matters (High Stakes)
- **Story Element**: Without equal-budget evaluation and leakage-free temporal splits, reported performance gains may be artificial artifacts of data leakage or excessive solution sampling. Deploying such unvalidated models in live trading leads to severe financial drawdown under real-world transaction fees.
- **Evidence**: [`article/references/ijcnn_rejection_analysis_and_nca_fixes.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/references/ijcnn_rejection_analysis_and_nca_fixes.md).

### Node 5: Central Research Hypothesis
- **Story Element**: *Hypothesis*: Evaluating evolutionary and swarm optimizers under an identical budget cap ($N_{\text{eval}} = 1,500$) within a leakage-free sequential temporal split (60/20/20) and a compound MCC-driven objective ($0.60\text{MCC} + 0.40F_1$) will reveal statistically significant disparities in search efficiency, predictive balance, and out-of-sample trading profitability.
- **Evidence**: [`config/experiment_config.yaml`](file:///c:/mysystems/projects/nca-optimizer-benchmark/config/experiment_config.yaml).

### Node 6: Proposed Methodological Framework
- **Story Element**: A controlled multi-optimizer benchmark framework systematically comparing 5 optimizer families (Random Search, GA, PSO, DE, GWO) tuning a 6D MLP search space over 15,057 intraday bars of B3 Mini-Index futures.
- **Evidence**: [`article/manuscript/sections/methodology.tex`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/manuscript/sections/methodology.tex).

### Node 7: Empirical Evidence
- **Story Element**: GA and DE achieve superior out-of-sample classification balance ($\text{MCC} = 0.231 \pm 0.012$ and $0.228 \pm 0.014$), significantly outperforming unguided Random Search ($\text{MCC} = 0.185 \pm 0.021$).
- **Evidence**: `outputs/metrics/optimizer_comparison_metrics.csv`.

### Node 8: Rigorous Validation & Statistical Proof
- **Story Element**: Non-parametric Friedman test confirms non-random performance differences ($p < 0.05$). Paired Wilcoxon-Holm tests confirm GA/DE superiority over Random Search with large effect sizes ($d > 0.80$).
- **Evidence**: `outputs/statistical_tests/wilcoxon_holm_results.csv`.

### Node 9: Practical & Economic Implications
- **Story Element**: In an out-of-sample financial backtest with transaction costs (0.01% fee per trade), the GA-tuned MLP generates a Net Return of 18.4% with an annualized Sharpe ratio of 1.42 and a Maximum Drawdown of -8.2%.
- **Evidence**: `outputs/backtests/financial_backtest_results.csv`.

### Node 10: Transparent Boundaries & Limitations
- **Story Element**: Conclusions are explicitly bounded by the evaluated $N_{\text{eval}} = 1,500$ evaluation cap, 5-minute execution horizon, 6D MLP space, and B3 Mini-Index futures domain (WIN).
- **Evidence**: [`article/EDITORIAL_MEMORY.md:DECISION 002`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/EDITORIAL_MEMORY.md).

### Node 11: Future Research Trajectory
- **Story Element**: Future extensions will evaluate multi-asset universes (WDO, DOL, IND), sub-minute tick execution, and multi-objective Pareto optimization.
- **Evidence**: [`PROJECT_CONTEXT.md:Sec 11`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md).
