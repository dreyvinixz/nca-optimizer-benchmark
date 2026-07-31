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
