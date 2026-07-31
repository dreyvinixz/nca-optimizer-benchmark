# Project Onboarding — NCA Optimizer Benchmark

This document provides a comprehensive onboarding guide for developers and AI agents working on the `nca-optimizer-benchmark` repository.

---

## 1. Project Overview

- **Goal**: Publish a benchmark paper in **Neural Computing and Applications (NCA)** evaluating 5 evolutionary and swarm intelligence optimizers for intraday trend classification using a Multilayer Perceptron (MLP).
- **Target Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, ISSN: 0941-0643).
- **Asset / Dataset**: Intraday 5-minute Mini-Index Futures (WIN) from B3 (Brazilian Stock Exchange), covering contracts WING24, WINJ24, WINM24, and WINQ24 (15,057 total instances).
- **Optimizers Evaluated**:
  1. Random Search (RS) — Baseline stochastic sampler.
  2. Genetic Algorithm (GA) — Evolutionary recombination & mutation.
  3. Particle Swarm Optimization (PSO) — Velocity & social/cognitive memory.
  4. Differential Evolution (DE) — Vector mutation & crossover.
  5. Grey Wolf Optimizer (GWO) — Alpha, beta, delta leadership hierarchy.

---

## 2. Directory Architecture

```
nca-optimizer-benchmark/
├── .agents/                        # Agent workspace rules, onboarding, handoff, and skills
│   ├── AGENTS.md                   # Workspace rules & standards
│   ├── ONBOARDING.md               # Onboarding & architecture overview
│   ├── HANDOFF.md                  # Session state & handoff checklist
│   └── skills/                     # Workspace custom skills
│       ├── nca-paper-authoring/    # Skill for LaTeX writing & NCA guidelines
│       ├── nca-literature-analysis/# Skill for literature querying & synthesis
│       └── metaheuristic-optimizer-benchmark/ # Skill for optimizer experiments
├── article/                        # Article manuscript and templates
│   ├── manuscript/                 # TeX source files (main.tex, titlepage.tex, sections/)
│   ├── templates/                  # Official Springer Nature templates & Overleaf ZIPs
│   └── references/                 # 90+ Markdown reference papers and search results
├── outputs/                        # Experimental tables, figures, and trade logs
└── scripts/                        # Python scripts for data processing, experiments, and LaTeX build
```

---

## 3. How to Compile the Paper

Run PowerShell commands from the workspace root:
```powershell
Set-Location 'article\manuscript'
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode titlepage.tex
```
Output PDFs:
- `article/manuscript/main.pdf` (13 pages, anonymized main text)
- `article/manuscript/titlepage.pdf` (2 pages, author metadata & ORCIDs)
