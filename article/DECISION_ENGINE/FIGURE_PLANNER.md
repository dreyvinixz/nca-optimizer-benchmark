# FIGURE PLANNER — Graphic Necessity & Design Engine
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/DECISION_ENGINE/FIGURE_PLANNER.md`  

---

## 1. Master Figure Inventory & Necessity Audit

To maintain high visual quality and prevent unnecessary chart clutter, every figure in the manuscript must pass the Graphic Necessity Audit.

```
Figure Candidate
    ↓
What Scientific Question Does it Answer?
    ↓
Can the Data be Presented in a Table Instead?
    ↓
Source Data File (CSV)
    ↓
Generation Script
    ↓
Graphic Resolution & Color Palette (300 DPI / HSL / Vector)
```

---

## 2. Planned Figure Specifications

### FIGURE 1: Sequential Temporal Split Protocol Diagram
- **Scientific Question Answered**: *How does the 60/20/20 sequential split preserve chronological order and eliminate data leakage?*
- **Necessity Rating**: **ESSENTIAL** (Visual proof of zero temporal data leakage).
- **Source Data**: `config/experiment_config.yaml:L15-L21` (9,034 Train / 3,011 Val / 3,012 Test).
- **Generation Script**: `scripts/09_generate_paper_figures.py`.
- **Target Section**: Section 3 (Data & Problem Formulation).
- **Format**: Vector EPS / High-Res PNG (1200 DPI). Clean HSL palette (Train: Blue, Val: Amber, Test: Green).

---

### FIGURE 2: Convergence Dynamics across 5 Optimizers
- **Scientific Question Answered**: *How rapidly do RS, GA, PSO, DE, and GWO converge over the $N_{\text{eval}} = 1,500$ evaluation budget?*
- **Necessity Rating**: **ESSENTIAL** (Core visual evidence of search efficiency and exploration vs. exploitation dynamics).
- **Source Data**: `outputs/metrics/convergence_trajectories.csv`.
- **Generation Script**: `scripts/09_generate_paper_figures.py`.
- **Target Section**: Section 5.2 (Convergence Dynamics).
- **Format**: Line plot with $N_{\text{eval}}$ on x-axis, mean validation fitness ($0.60\text{MCC} + 0.40F_1$) on y-axis, shaded standard deviation confidence intervals across 20 seeds. 300 DPI PNG / EPS.

---

### FIGURE 3: Financial Backtest Cumulative Equity Curves
- **Scientific Question Answered**: *How do the genetically/metaheuristically tuned models perform economically over out-of-sample trading days under transaction fees?*
- **Necessity Rating**: **RECOMMENDED** (Visual proof of trading utility and drawdown recovery).
- **Source Data**: `outputs/backtests/equity_curves.csv`.
- **Generation Script**: `scripts/09_generate_paper_figures.py`.
- **Target Section**: Section 5.5 (Financial Backtest).
- **Format**: Cumulative net return % curve over test time steps, comparing GA, PSO, DE, GWO, RS, and Buy & Hold baseline.

---

## 3. Graphic Quality Rules (NCA Standards)

1. **Resolution Cap**: Minimum 300 DPI for halftone figures, 1200 DPI for vector diagrams.
2. **Color Palette**: Use distinct, publication-grade, colorblind-friendly HSL palettes. Never use default bright primaries (red/green/blue).
3. **Typography**: All axis labels, titles, and legends must use clean sans-serif fonts (Helvetica or Arial) matching LaTeX font sizes (8pt–10pt).

---

## 4. Current Curated Figure Plan — 2026-08-12

This section supersedes the numerical assumptions in the preliminary plan above. The current paper uses a common locked temporal test block, **three common seeds** in every model--optimizer cell, **1,000 candidate evaluations per seed**, and two separate validation protocols: compound MCC/$F_1$ fitness and weighted training/validation accuracy fitness. No figure may imply 20 seeds, a 1,500-evaluation budget, or a cross-protocol inferential test.

### 4.1 Figures currently included in `main.pdf`

| Current figure | Purpose | Evidence basis | Retain / revision |
|---|---|---|---|
| Workflow with two validation objectives | Makes the chronological split, equal budget, and separation of MCC/$F_1$ and accuracy fitness explicit. | Protocol specification and final experiment outputs. | **Retain.** Add a compact equal-budget search-cycle inset only if it remains legible. |
| Chronological 60/20/20 partition | Demonstrates that the locked test block is not accessed during feature selection or search. | 15,057 records: 9,034 training, 3,011 validation, 3,012 test. | **Retain.** |
| Four optimizer-convergence panels | Shows best-so-far search trajectories for RF, SVM, MLP, and 1D-CNN, each with both validation objectives. | Per-optimizer convergence records, common seeds 1--3. | **Retain.** Objective scales must remain separate. |
| Predictive model comparison | Reports held-out accuracy and MCC by model family under each protocol. | Fifteen optimizer--seed blocks per model and protocol. | **Replace or complement** with the outcome-distribution and heatmap figures below. |
| Economic summary | Reports mean total profit and maximum drawdown by model family under each protocol. | Economic summaries from the common locked test block. | **Replace or complement** with the predictive--economic association map below. |

### 4.2 Priority additions for the main manuscript

| Priority | Proposed figure | Section | Scientific question | Available evidence | Design decision |
|---:|---|---|---|---|---|
| 1 | **Input representation and model-family architectures** | Methodology | How do the seven retained features enter tabular models and the 1D-CNN? | Information-Gain-7 feature list and documented search spaces. | Redraw as one clean vector schematic: shared seven-feature input; RF/SVM/MLP as tabular branch; 1D-CNN as a $7\times1$ sequence branch. Do not reuse legacy CUDA-labelled diagrams. |
| 2 | **Held-out performance heatmaps by optimizer and protocol** | Results | Which model--optimizer cells perform well under each objective? | `predictive_by_combo.csv` and per-seed result files. | Four aligned panels: MCC/$F_1$ protocol accuracy/MCC and accuracy protocol accuracy/MCC. Rows: models; columns: RS, GA, PSO, DE, GWO. Show means only; raw-seed variation belongs in the next figure. |
| 3 | **Distribution of locked-test outcomes and statistical contrasts** | Results | How variable are the results across matched optimizer--seed blocks? | Three common seeds; 15 blocks per model within protocol; Friedman and Holm-adjusted Wilcoxon results. | Use raw points plus median and interval, not violin/KDE plots. Present inferential annotations strictly within each protocol. |
| 4 | **Predictive--economic association map** | Results | Does stronger predictive performance correspond to higher profit or lower downside risk? | `predictive_by_combo.csv` and `economic_by_combo.csv`. | Two panels: test MCC versus total profit; test accuracy versus maximum drawdown. Color: model; marker: optimizer; facet: validation protocol. |
| 5 | **Information-Gain feature-selection profile** | Methodology | Which descriptors were retained, and how is feature selection made auditable? | Existing retained-feature ranking: EMA$_{5-3}$, normalized EMA$_{5-3}$, EMA$_{7-3}$, normalized EMA$_{7-3}$, normalized SMA$_9$, EMA$_{9-3}$, normalized EMA$_7$. | Recompute Information-Gain values on the training block only before publication; then display a sorted horizontal bar chart. |
| 6 | **Temporal stability on the locked test set** | Results / supplement candidate | Do model outcomes remain stable across the chronology of the held-out period? | Timestamped predictions over 3,012 locked-test records. | Rolling-window accuracy or MCC over time, separately by protocol. Use a predeclared window size and report it in the caption. This is valuable but requires a new analysis step. |
| 7 | **Anytime search-efficiency map** | Results / supplement candidate | Which optimizers achieve useful fitness earlier under the same evaluation budget? | Per-model, per-optimizer convergence trajectories. | Heatmap of normalized area under each best-so-far fitness curve; rows: model; columns: optimizer; one panel per protocol. This supplements, not replaces, the trajectories. |

### 4.3 Optional supplementary figures

| Figure | Rationale | Constraint |
|---|---|---|
| ROC curves for all matched model--optimizer blocks | Uses available probability outputs and can document discrimination beyond one threshold. | Never show only a post-hoc winning configuration; aggregate or present every comparable block. |
| Confusion-matrix summary | Gives an intuitive error-type view for uptrend/downtrend classification. | Aggregate consistently across matched blocks and keep it supplementary to MCC/$F_1$. |
| Representative price and trading-signal episode | Offers an operational illustration of the economic simulation. | Clearly label it illustrative; it cannot substitute for the full locked-test economic analysis. |
| Cumulative equity curves | Makes the path of return and drawdown concrete. | Use the full common test period and identify transaction-cost assumptions. |

### 4.4 Literature inspirations that informed the plan

The project Markdown library was searched for `Fig.` and `Figure` occurrences across 90 article records. The useful conceptual precedents are adapted, not reproduced:

- **Data-to-model architecture diagrams**: symbolic-dynamics/CRNN workflow and recurrent-network schematics motivate the input-and-architecture figure.
- **Equal-budget convergence and distribution plots**: NCA benchmark and metaheuristic papers motivate trajectories, search-efficiency summaries, raw-point distributions, and boxplot-style comparisons.
- **Feature-importance bars**: metaheuristic-tuned model papers motivate an auditable Information-Gain profile.
- **Scatter/risk-yield figures**: financial forecasting and portfolio-optimization papers motivate the predictive--economic association map.
- **Chronological forecast and signal plots**: financial prediction papers motivate a temporal-stability analysis, rather than a single hand-picked trading example.

### 4.5 Explicit exclusions from the main paper

| Excluded visual form | Why it is excluded |
|---|---|
| Radar plots | They obscure absolute magnitudes and uncertainty; heatmaps and raw-point plots are more defensible. |
| Cumulative distributions of Markovianity tests | The paper does not test a Markovianity hypothesis. |
| PINN, symbolic-regression, island-GP, or generic evolutionary-operator diagrams | These are outside the implemented method and would falsely broaden the contribution. |
| Taxonomies of PSO/GA/metaheuristics | General review material; it does not answer an empirical question of this benchmark. |
| A ROC curve only for a selected winner | It would look post-hoc and would not represent all comparable model--optimizer blocks. |
| Violin/KDE outcome plots | Three seeds are too few to support a smooth density claim. |
| Numerous buy/sell price charts | They consume space without adding benchmark-level evidence; at most one predeclared illustrative example belongs in the supplement. |

### 4.6 Production and review rules

1. Every graphic must be generated from the final audited outputs, not manually edited values.
2. Use publication-grade, colorblind-safe colors and preserve the same model and optimizer encoding across all figures.
3. Use vector PDF for diagrams and plots; raster assets, if ever required, must be at least 300 DPI.
4. Captions must state aggregation level, seed count, protocol, and whether the panel uses locked-test data.
5. The main text must report values and statistical interpretation in the Results section only; the Introduction may state the design but must not preannounce empirical rankings or values.
