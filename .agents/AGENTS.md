# Workspace Rules & Guidelines — NCA Optimizer Benchmark

Welcome to the `nca-optimizer-benchmark` project. This workspace contains the complete experimental code, outputs, and LaTeX manuscript targeting **Neural Computing and Applications (NCA)** (Springer Nature, Journal ID 521, ISSN: 0941-0643).

---

## Key Workspace Rules & Authoring Standards

1. **Master Structural & Writing Guide**:
   - Every text edit, section drafting, or revision MUST strictly adhere to the master guide **[NCA_STRUCTURAL_AND_WRITING_PATTERNS.md](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/references/NCA_STRUCTURAL_AND_WRITING_PATTERNS.md)**.

2. **Academic Rigor & Peer Review Compliance**:
   - Double-Blind Peer Review: All files under `article/manuscript/sections/` and `article/manuscript/main.tex` MUST remain strictly anonymized (no author names, affiliations, or explicit grant numbers in the main text).
   - Author metadata, ORCIDs, and grant numbers belong exclusively in `article/manuscript/titlepage.tex`.

3. **LaTeX Manuscript & Compilation**:
   - Class File: Always use `sn-jnl.cls` with option `sn-mathphys-num`.
   - Table Scaling: Every table must use `\resizebox{\linewidth}{!}{...}` to prevent margin overflows (`overfull \hbox`).
   - Compilation: Compile using MiKTeX `pdflatex` and `bibtex` from working directory `article/manuscript/`.

4. **Data Leakage & Evaluation Budget**:
   - Temporal Protocol: Always maintain strict 60/20/20 sequential chronological split without random shuffling.
   - Equal Evaluation Budget: All 5 optimizers (RS, GA, PSO, DE, GWO) must be evaluated under an identical $N_{eval} = 1,500$ fitness evaluation budget per seed.
   - Fitness Function: Compound MCC-driven objective $f(\boldsymbol{\theta}) = 0.60 \times \text{MCC} + 0.40 \times F_1$.

5. **Literature & Reference Integration**:
   - Always reference the 90+ Markdown files under `article/references/md_references/` for citations and stylistic alignment with recent 2024–2026 NCA papers.
