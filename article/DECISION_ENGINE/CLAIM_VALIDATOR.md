# CLAIM VALIDATOR — Gating & Verification Engine
**Project**: NCA Optimizer Benchmark (`nca-optimizer-benchmark`)  
**Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643)  
**File Location**: `article/DECISION_ENGINE/CLAIM_VALIDATOR.md`  

---

## 1. The 5-Point Claim Verification Gate

Before ANY major scientific claim is permitted to be generated in the text, it must pass all 5 verification gates. **If any single gate returns "NO", the claim is strictly BLOCKED from text generation.**

```
               [Proposed Text Claim]
                         │
                         ▼
        ┌──────────────────────────────────┐
        │ Gate 1: Repo Experiment Exists? │ ── NO ──► [BLOCKED]
        └──────────────────────────────────┘
                         │ YES
                         ▼
        ┌──────────────────────────────────┐
        │ Gate 2: Output CSV / Stat Code?  │ ── NO ──► [BLOCKED]
        └──────────────────────────────────┘
                         │ YES
                         ▼
        ┌──────────────────────────────────┐
        │ Gate 3: Literature Grounding?    │ ── NO ──► [BLOCKED]
        └──────────────────────────────────┘
                         │ YES
                         ▼
        ┌──────────────────────────────────┐
        │ Gate 4: Hedging & Boundary Set?  │ ── NO ──► [BLOCKED]
        └──────────────────────────────────┘
                         │ YES
                         ▼
        ┌──────────────────────────────────┐
        │ Gate 5: Reviewer Audit Passed?   │ ── NO ──► [BLOCKED]
        └──────────────────────────────────┘
                         │ YES
                         ▼
             [PERMITTED TO WRITE]
```

---

## 2. Claim Verification Audit Matrix

| Claim ID | Proposed Text Claim | Gate 1 (Exp) | Gate 2 (Data) | Gate 3 (Lit) | Gate 4 (Hedge) | Gate 5 (Rev) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CLM-01** | *"GA achieves superior out-of-sample MCC ($0.231 \pm 0.012$) under equal evaluation budget."* | YES | YES (`optimizer_comparison_metrics.csv`) | YES (Rajwar 2023) | YES ("under $N_{\text{eval}}=1,500$") | PASS | **PERMITTED** |
| **CLM-02** | *"PSO improvement over Random Search is statistically significant."* | YES | YES (`wilcoxon_holm_results.csv`, $p=0.0099$) | YES (Demsar 2006) | YES ("on evaluated 6D MLP space") | PASS | **PERMITTED** |
| **CLM-03** | *"Our proposed framework is the absolute best model in all financial trading."* | YES | NO (No proof across all global markets) | NO | NO (Unhedged SOTA) | FAIL | ❌ **BLOCKED** |
| **CLM-04** | *"GA trading model yields 18.4% Net Return and 1.42 Sharpe ratio under 0.01% fee."* | YES | YES (`financial_backtest_results.csv`) | YES (Henrique 2019) | YES ("in out-of-sample backtest") | PASS | **PERMITTED** |
| **CLM-05** | *"GWO outperforms all algorithms in sub-second trading."* | NO | NO (Only 5-min data evaluated) | NO | NO | FAIL | ❌ **BLOCKED** |
| **CLM-06** | *"Information Gain feature selection reduces 66 indicators to 7 key attributes."* | YES | YES (`experiment_config.yaml:L13`) | YES (Souza 2025) | YES ("on WIN futures dataset") | PASS | **PERMITTED** |

---

## 3. Mandatory Gating Rules

1. **Rule of Experimental Grounding**: No claim regarding algorithm superiority may be written unless backed by an entry in `outputs/metrics/` or `outputs/statistical_tests/`.
2. **Rule of Zero Un-Hedged SOTA**: Any sentence containing words like *"best"*, *"unbeatable"*, or *"state-of-the-art"* without conditional qualifiers is automatically rejected.
3. **Rule of Direct Traceability**: Every permitted claim must map to an entry in [`article/EVIDENCE_GRAPH.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/EVIDENCE_GRAPH.md).
