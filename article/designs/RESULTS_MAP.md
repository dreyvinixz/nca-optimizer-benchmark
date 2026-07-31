# RESULTS MAP — Findings & Evidence Hierarchy
**Mission ID**: MISSION 10 (Phase A & B)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/designs/RESULTS_MAP.md`  

---

## 1. Scientific Risk Assessment (Pre-Draft)

- **Methodological Risk**: **LOW** (Identical budget $N_{\text{eval}}=1,500$ cap & 60/20/20 sequential split).
- **Statistical Risk**: **LOW** (Friedman omnibus $\chi^2 = 38.42, p < 0.001$, Wilcoxon-Holm $p$-values, Cohen's $d$).
- **Evidence Coverage**: **COMPLETE** (CSV data verified across `outputs/metrics/`, `outputs/statistical_tests/`, `outputs/backtests/`).
- **Novelty Risk**: **MEDIUM** (Methodological benchmark novelty, not claiming new optimizer invention).
- **Reviewer Concern**: **LOW** (Null findings transparently reported).
- **Repository Traceability**: **COMPLETE** (Every metric mapped to output CSVs).

---

## 2. Findings Hierarchy (Ordered from Strongest to Weakest Evidence)

### Finding 1: Statistically Significant Superiority of Metaheuristics Over Unguided Random Search
- **Main Question**: *Do guided metaheuristics achieve superior out-of-sample classification balance compared to unguided stochastic sampling under budget equality?*
- **Repository Evidence**: `outputs/metrics/optimizer_comparison_metrics.csv` (Table 2). GA $\text{MCC} = 0.231 \pm 0.012$, DE $\text{MCC} = 0.228 \pm 0.014$, PSO $\text{MCC} = 0.225 \pm 0.011$ vs. Random Search $\text{MCC} = 0.185 \pm 0.021$.
- **Statistical Support**: Friedman test ($\chi^2 = 38.42, p = 9.2 \times 10^{-8}$). Wilcoxon-Holm GA vs RS ($p = 0.0021, d = 1.241$), DE vs RS ($p = 0.0032, d = 1.182$), PSO vs RS ($p = 0.0045, d = 1.105$).
- **Practical Impact**: +24.8% relative MCC improvement for GA over Random Search.
- **Discussion Preview**: Demonstrates that guided recombination and particle swarm dynamics extract real search efficiency.

---

### Finding 2: Direct Translation of Classification MCC Gains into Net Financial Returns
- **Main Question**: *Do predictive MCC gains translate into net intraday trading profitability under realistic transaction fees?*
- **Repository Evidence**: `outputs/backtests/financial_backtest_results.csv` (Table 4). GA Strategy yields $+18.4\%$ Net Return, Sharpe $1.42$, MDD $-8.2\%$ under $0.01\%$ fees vs Random Search ($+4.2\%$, Sharpe $0.48$) and Buy \& Hold ($-2.5\%$).
- **Statistical Support**: Empirical backtest over 3,012 out-of-sample bars across 3 fee tiers ($0.00\%, 0.01\%, 0.02\%$).
- **Practical Impact**: Confirms that compound MCC optimization produces models that remain profitable even under $0.02\%$ slippage friction.
- **Discussion Preview**: Bridges the gap between ML metrics and quantitative finance utility.

---

### Finding 3: Recombination-Driven Diversification Prevents Premature Local Trapping
- **Main Question**: *How do evolutionary recombination mechanisms (GA/DE) compare against swarm leadership dynamics (GWO/PSO) over execution iterations?*
- **Repository Evidence**: `outputs/metrics/convergence_trajectories.csv` (Figure 2). GA and DE sustain steady fitness escalation beyond $t \ge 800$, outperforming GWO ($\text{MCC} = 0.208 \pm 0.016$).
- **Statistical Support**: Wilcoxon-Holm GA vs GWO ($p = 0.0142, d = 0.815$).
- **Practical Impact**: Population recombination (crossover and vector differencing) maintains diversity in non-convex search spaces.
- **Discussion Preview**: GWO's leadership hierarchy causes early attraction to sub-optimal local basins.

---

### Finding 4 (Null Finding): Competitive Parity Between Top Evolutionary and Swarm Paradigms
- **Main Question**: *Is there a statistically significant performance difference between GA, DE, and PSO?*
- **Repository Evidence**: `outputs/statistical_tests/wilcoxon_holm_results.csv` (Table 3). GA vs PSO ($p = 0.1360, d = 0.261$), GA vs DE ($p = 0.4520, d = 0.115$).
- **Statistical Support**: Adjusted $p > 0.10$ for pairwise comparisons among GA, DE, and PSO.
- **Practical Impact**: Transparently acknowledges that GA, DE, and PSO achieve comparable solution quality under budget equality.
- **Discussion Preview**: Prevents overclaiming universal dominance for a single algorithm.

---

## 3. Unsupported Interpretations (Excluded from Results Text)

The following hypotheses were considered but are **EXCLUDED from the Results section** due to insufficient repository evidence (saved for Future Work discussion):
1. *Claiming GA is universally superior across all global financial markets*: **EXCLUDED** (Only B3 Mini-Index futures evaluated).
2. *Claiming GWO is incapable of optimizing neural networks*: **EXCLUDED** (GWO succeeded relative to Random Search, but plateaued relative to GA).
