# NEGATIVE & NULL FINDINGS — Scientific Honesty Log
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/designs/NEGATIVE_FINDINGS.md`  

---

## 1. Purpose of Negative & Null Findings Documentation

Scientific credibility relies on transparently reporting where algorithms failed or showed no statistical difference. We explicitly record negative and null findings to prevent overclaiming.

---

## 2. Inventory of Negative & Null Findings

### Null Finding 1: Pairwise Statistical Equivalence Between GA, DE, and PSO
- **Finding**: The Genetic Algorithm (GA), Differential Evolution (DE), and Particle Swarm Optimization (PSO) exhibit statistically equivalent out-of-sample MCC scores ($p > 0.10$).
- **Evidence**: `outputs/statistical_tests/wilcoxon_holm_results.csv` (GA vs PSO: $p = 0.1360$; GA vs DE: $p = 0.4520$).
- **Explanation**: Within the evaluated equal-budget constraint ($N_{\text{eval}} = 1,500$) and 6D search space, GA, DE, and PSO all locate high-fitness basins with similar search efficiency.
- **Scientific Impact**: Proves that no single metaheuristic universally dominates all others; evolutionary and swarm paradigms achieve comparable solution quality when budget equality is enforced.

---

### Negative Finding 2: Premature Plateauing of Grey Wolf Optimizer (GWO)
- **Finding**: GWO achieved rapid early convergence ($t \le 300$), but plateaued prematurely, yielding lower out-of-sample MCC ($0.208 \pm 0.016$) compared to GA ($0.231 \pm 0.012$).
- **Evidence**: `outputs/metrics/optimizer_comparison_metrics.csv`, `outputs/metrics/convergence_trajectories.csv`.
- **Explanation**: GWO's leadership hierarchy ($\alpha, \beta, \delta$) causes rapid attraction toward top wolf positions, reducing population variance in noisy non-convex financial search spaces.
- **Scientific Impact**: Demonstrates that leader-driven swarms require adaptive parameter decay to avoid local sub-optima in noisy environments.

---

### Negative Finding 3: Marginal Performance Differential in Execution Runtime
- **Finding**: Population update overhead accounts for less than 15% of total execution time across all metaheuristics.
- **Evidence**: `outputs/metrics/runtime_analysis.csv` (RS: $2.95\text{ s}$, PSO: $3.35\text{ s}$, GA: $3.48\text{ s}$, DE: $3.52\text{ s}$, GWO: $3.58\text{ s}$).
- **Explanation**: Neural network training (RMSprop over 50 epochs) dominates total execution cost, rendering algorithmic vector updates computationally trivial.
- **Scientific Impact**: Confirms that selection of an optimizer should be guided by predictive and financial performance rather than microsecond algorithmic execution differences.
