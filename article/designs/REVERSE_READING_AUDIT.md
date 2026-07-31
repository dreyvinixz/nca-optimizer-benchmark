# REVERSE READING AUDIT — Manuscript Narrative Continuity Report
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/designs/REVERSE_READING_AUDIT.md`  

---

## 1. Executive Summary & Methodology

The **Reverse Reading Technique** audits narrative continuity and eliminates logical discrepancies by evaluating manuscript sections in strict reverse sequence:

```
Abstract
   │
   ▼
Conclusion (Section 7)
   │
   ▼
Discussion (Section 6)
   │
   ▼
Results (Section 5)
   │
   ▼
Methodology (Section 4)
   │
   ▼
Data & Protocol (Section 3)
   │
   ▼
Related Work (Section 2)
   │
   ▼
Introduction (Section 1)
```

---

## 2. Reverse Sequence Traceability Audit

### Step 1: Abstract $\longleftarrow$ Conclusion (Section 7)
- **Audit Focus**: Does the Abstract accurately summarize the Conclusion without adding extraneous claims?
- **Findings**:
  - Abstract states: GA $\text{MCC} = 0.231 \pm 0.012$, Net Return $18.4\%$, Sharpe $1.42$, equal-budget benchmark necessity.
  - Conclusion states: Identical 3 quantitative conclusions and 3 future directions.
- **Traceability Status**: **100% MATCH**

---

### Step 2: Conclusion (Section 7) $\longleftarrow$ Discussion (Section 6)
- **Audit Focus**: Do the 3 conclusion points directly reflect the interpretations in Discussion?
- **Findings**:
  - Conclusion Point 1 (Metaheuristics > Random Search) $\longleftarrow$ Discussion 6.1 & 6.3.
  - Conclusion Point 2 (Recombination vs Leadership) $\longleftarrow$ Discussion 6.2.
  - Conclusion Point 3 (Trading Profitability under Fees) $\longleftarrow$ Discussion 6.3 & 6.4.
- **Traceability Status**: **100% MATCH**

---

### Step 3: Discussion (Section 6) $\longleftarrow$ Results (Section 5)
- **Audit Focus**: Are all interpretations in Discussion anchored in empirical Results without overreaching?
- **Findings**:
  - Discussion 6.1 & 6.2 interpret GA/DE diversification vs GWO plateauing $\longleftarrow$ Results 5.1, 5.2, 5.4 (Table 2, Figure 2, Table 3).
  - Discussion 6.3 interprets compound MCC fee resilience $\longleftarrow$ Results 5.5 (Table 4).
  - Discussion 6.4 analyzes $0.40\text{ s}$ runtime overhead $\longleftarrow$ Results 5.3.
- **Traceability Status**: **100% MATCH**

---

### Step 4: Results (Section 5) $\longleftarrow$ Methodology (Section 4) & Data (Section 3)
- **Audit Focus**: Are all reported metrics, tables, and algorithms defined in Methodology and Data prior to Results?
- **Findings**:
  - Table 2 (Predictive Metrics) $\longleftarrow$ Defined in Sec 4.1, 4.2, 4.3.
  - Table 3 (Wilcoxon-Holm & Cohen's $d$) $\longleftarrow$ Defined in Sec 4.5.
  - Table 4 (Backtest Metrics & Fees) $\longleftarrow$ Defined in Sec 4.6.
  - Figure 1 (Temporal Split) $\longleftarrow$ Defined in Sec 3.3.
  - Figure 2 (Convergence Curves) $\longleftarrow$ Defined in Sec 4.3.
- **Traceability Status**: **100% MATCH**

---

### Step 5: Methodology (Section 4) & Data (Section 3) $\longleftarrow$ Related Work (Section 2)
- **Audit Focus**: Are all methodological choices contextualized by the hypothesis-driven gaps in Related Work?
- **Findings**:
  - Equal budget cap $N_{\text{eval}}=1,500 \longleftarrow$ Hypothesis 1 (Sec 2.2).
  - Sequential split 60/20/20 $\longleftarrow$ Hypothesis 2 (Sec 2.3).
  - Compound MCC objective & backtest $\longleftarrow$ Hypothesis 3 (Sec 2.4).
- **Traceability Status**: **100% MATCH**

---

### Step 6: Related Work (Section 2) $\longleftarrow$ Introduction (Section 1)
- **Audit Focus**: Does the Introduction promise ONLY what was contextualized in Related Work and delivered in Sections 3–7?
- **Findings**:
  - CARS Move 4 (Literature Flaws) matches 3 Hypotheses in Sec 2.
  - 6 Bulleted Contributions match verified contributions in Sec 3–7.
- **Traceability Status**: **100% MATCH**

---

## 3. Final Reverse Reading Verdict

### **VERDICT: MANUSCRIPT NARRATIVE IS 100% CONTINUOUS & CONTRADICTION-FREE**

Reverse reading confirms zero logical gaps, zero unhedged overclaiming, zero uncited variables, and total narrative alignment across all 7 sections.
