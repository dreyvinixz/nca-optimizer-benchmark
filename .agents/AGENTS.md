# Workspace Rules & Guidelines — NCA Optimizer Benchmark

Welcome to the `nca-optimizer-benchmark` project. This workspace contains the complete experimental code, outputs, and LaTeX manuscript targeting **Neural Computing and Applications (NCA)** (Springer Nature, Journal ID 521, ISSN: 0941-0643).

---

## 1. The 7-Module Scientific Cognitive Architecture

Every agent and developer operating in this workspace MUST navigate and obey the 7 permanent cognitive modules:

1. **Project Knowledge**:
   - [`article/PROJECT_MEMORY.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/PROJECT_MEMORY.md) — Single Source of Truth for verified project facts, metadata, and data bounds.
   - [`PROJECT_CONTEXT.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/PROJECT_CONTEXT.md) — Scientific scope, research lineage, and IJCNN review points.
2. **Literature Intelligence**:
   - [`article/NCA_WRITING_DNA.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/NCA_WRITING_DNA.md) — Reverse-engineered statistical writing patterns from 90 NCA papers.
   - [`article/SCIENTIFIC_REASONING_DNA.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/SCIENTIFIC_REASONING_DNA.md) — Epistemological argument construction & Toulmin model.
3. **Scientific Decision Engine**:
   - [`article/DECISION_ENGINE/RESEARCH_STORY.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/DECISION_ENGINE/RESEARCH_STORY.md) — The 11-node scientific narrative arc.
   - [`article/DECISION_ENGINE/CLAIM_VALIDATOR.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/DECISION_ENGINE/CLAIM_VALIDATOR.md) — 5-point verification gating engine for text claims.
   - [`article/DECISION_ENGINE/CONTRIBUTION_VALIDATOR.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/DECISION_ENGINE/CONTRIBUTION_VALIDATOR.md) — Deconstruction matrix for bulleted contributions.
   - [`article/DECISION_ENGINE/NOVELTY_VALIDATOR.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/DECISION_ENGINE/NOVELTY_VALIDATOR.md) — 5-level novelty classification & anti-overclaiming matrix.
   - [`article/DECISION_ENGINE/FIGURE_PLANNER.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/DECISION_ENGINE/FIGURE_PLANNER.md) — Graphic necessity audit & resolution specs.
   - [`article/DECISION_ENGINE/TABLE_PLANNER.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/DECISION_ENGINE/TABLE_PLANNER.md) — Tabular necessity audit & booktabs scaling specs.
4. **Planning & Evidence**:
   - [`article/SECTION_PLANNER.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/SECTION_PLANNER.md) — Pre-writing scientific blueprint for every section.
   - [`article/EVIDENCE_GRAPH.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/EVIDENCE_GRAPH.md) — Traceability matrix mapping claims to code, data, tables, and figures.
5. **Editorial Memory**:
   - [`article/EDITORIAL_MEMORY.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/EDITORIAL_MEMORY.md) — Binding scientific decisions (Decisions 001–010) to prevent AI drift.
6. **Writing Engine**:
   - `article/manuscript/` — Anonymous `main.tex`, `titlepage.tex`, `references.bib`, and `sections/`.
7. **Review Engine**:
   - [`article/REVIEWER_PROFILE.md`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/REVIEWER_PROFILE.md) — 4 virtual reviewer profiles and pre-flight audit matrix.

---

## 2. The 9-Step Scientific Iteration Cycle

No manuscript section shall be considered complete without progressing through the 9-step cycle:

```text
1. Planning (SECTION_PLANNER.md & RESEARCH_STORY.md)
        ↓
2. Decision & Claim Validation (DECISION_ENGINE/*.md)
        ↓
3. Evidence Verification (EVIDENCE_GRAPH.md)
        ↓
4. First Draft (sections/*.tex)
        ↓
5. Scientific Reasoning Review (SCIENTIFIC_REASONING_DNA.md)
        ↓
6. NCA Writing Review (NCA_WRITING_DNA.md)
        ↓
7. Technical Consistency Review (code & output CSV check)
        ↓
8. Editorial Consistency Review (EDITORIAL_MEMORY.md)
        ↓
9. Originality & Reviewer Simulation Review (REVIEWER_PROFILE.md)
```

---

## 3. Key Operational Rules & Standards

1. **Double-Blind Peer Review**: All files under `article/manuscript/sections/` and `article/manuscript/main.tex` MUST remain strictly anonymized. Author metadata, ORCIDs, and grant numbers belong exclusively in `article/manuscript/titlepage.tex`.
2. **LaTeX Manuscript & Compilation**: Always compile using MiKTeX `pdflatex` and `bibtex` from working directory `article/manuscript/` using class `sn-jnl.cls` with option `sn-mathphys-num`.
3. **Data Leakage & Evaluation Budget**: Maintain a strict 60/20/20 sequential chronological split (`shuffle = false`). Enforce an identical $N_{\text{eval}} = 1,500$ evaluation budget per seed across all 5 optimizers.
