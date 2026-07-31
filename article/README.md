# Directory Guide — Article Manuscript & References (`article/`)

Welcome to the `article/` directory of the **NCA Optimizer Benchmark** project (`nca-optimizer-benchmark`). 

This directory contains the complete academic production pipeline, including LaTeX TeX sources, official Springer Nature templates, raw PDF literature files, and a repository of **90+ full-text Markdown converted academic reference papers** targeting publication in **Neural Computing and Applications (NCA)** (Springer Nature, Journal ID 521, ISSN: 0941-0643).

---

## 1. Project Goal & Scientific Context

- **Objective**: Author a benchmark paper for **Neural Computing and Applications (NCA)** evaluating five metaheuristic and stochastic optimizers for intraday trend classification using Multilayer Perceptrons (MLPs).
- **Application Domain**: High-frequency 5-minute Mini-Index Futures (WIN) traded on the Brazilian Stock Exchange (B3).
- **Core Methodological Pillars**:
  1. **Controlled Equal-Budget Benchmark**: All 5 optimizers (Random Search, Genetic Algorithm, Particle Swarm Optimization, Differential Evolution, Grey Wolf Optimizer) evaluated under an identical budget of $N_{\text{eval}} = 1,500$ fitness evaluations per seed.
  2. **Leakage-Free Sequential Temporal Protocol**: Strict 60/20/20 chronological split (train/validation/test) over 15,057 intraday instances, eliminating temporal data leakage.
  3. **Compound MCC-Driven Fitness Function**: $f(\boldsymbol{\theta}) = 0.60 \times \text{MCC} + 0.40 \times F_1$ to resist class imbalance distortion.
  4. **Non-Parametric Statistical Testing**: Friedman test + paired Wilcoxon signed-rank tests with Holm-Bonferroni correction and Cohen's $d$ effect sizes.
  5. **Out-of-Sample Financial Backtesting**: Simulation of real-world trading utility measuring Net Return %, Sharpe Ratio, Maximum Drawdown (MDD), and transaction cost sensitivity.

---

## 2. Exhaustive Directory Map & File Inventory

Below is the complete audit of all directories, raw PDF files (93 total), and Markdown reference files (99 total):

```
article/
├── README.md                           # Master guide for developers and AI agents
├── ARTICLE_GUIDE.md                    # Detailed manuscript roadmap & section guidelines
├── article_inventory.md                # Comprehensive file inventory
├── manuscript/                         # LaTeX TeX source files & compilation output
│   ├── main.tex                        # Anonymous main manuscript (for double-blind review)
│   ├── titlepage.tex                   # Separate title page (authors, ORCIDs, affiliations, funding)
│   ├── references.bib                  # BibTeX bibliography database (20+ references)
│   ├── sn-jnl.cls                      # Official Springer Nature LaTeX class file
│   ├── sn-mathphys-num.bst             # Official Springer Nature bibliography style
│   ├── main.pdf                        # Compiled manuscript PDF (5 pages - Introduction focus)
│   ├── titlepage.pdf                   # Compiled title page PDF (2 pages)
│   └── sections/                       # Individual LaTeX section TeX files
│       ├── introduction.tex            # Section 1: Introduction (CARS 5-move model + 6 contributions)
│       ├── related_work.tex            # Section 2: Related Work & Literature Gap (Table 1)
│       ├── data.tex                    # Section 3: Dataset & Temporal Validation Protocol
│       ├── methodology.tex             # Section 4: MLP Search Space & Optimizer Formulations
│       ├── results.tex                 # Section 5: Experimental Results & Statistical Benchmark
│       ├── discussion.tex              # Section 6: Trade-off Analysis & Practical Implications
│       ├── limitations.tex             # Section 7: Limitations
│       ├── conclusion.tex              # Section 8: Conclusion & Future Work
│       └── declarations.tex            # Declarations (Funding, Conflicts, Ethics, Data Availability)
├── templates/                          # Official & Overleaf LaTeX template packages
│   ├── springer_nature_official_latex_template.zip # Official Dec 2024 Springer Nature ZIP (901.8 KB)
│   └── nca_overleaf_template.zip       # Ready-to-import Overleaf ZIP of our manuscript (63.3 KB)
└── references/                         # Complete Literature & Guidelines Repository (93 PDFs, 99 MDs)
    ├── nca_submission_guidelines.md    # Official Springer Nature author guidelines (1,125 lines)
    ├── NCA_STRUCTURAL_AND_WRITING_PATTERNS.md # Master structural, rhetorical, and writing patterns
    ├── MASTER_INTRODUCTION_ANALYSIS.md # Comparative introduction analysis across 45 papers
    ├── HUMAN_WRITING_REVISION_LOG.md   # Step-by-step human writing review log & transformations
    ├── ijcnn_rejection_analysis_and_nca_fixes.md # Analysis of precursor paper flaws & NCA fixes
    ├── REFERENCE_BENCHMARK_GUIDE.md    # Technical guide for tables, equations, and vocabulary
    ├── [Root PDFs]                     # 6 Precursor & Reference PDFs (Dhingra 2025, ICCSA, IJCNN, Review)
    ├── literature/                     # 6 Raw PDF survey papers (Gad 2022, Rajwar 2023, Makridakis 2018)
    │   └── additional_key_pdfs/        # 1 Raw PDF (Makridakis et al. 2018)
    ├── nca_journal_521_pdfs/           # 40 Raw PDF papers published directly in NCA (2024–2026)
    ├── nca_search/                     # OpenAlex / Crossref search inventory (40 PDFs, top_papers.md, papers.csv)
    │   └── papers/                     # 40 Raw PDF search papers (categorized across 4 topic subfolders)
    └── md_references/                  # 90 Full Markdown converted academic papers (100% Converted)
        ├── nca_journal_521_2024_plus/  # 40 Converted MD papers from Journal 521 (2024–2026)
        ├── nca_search_all/             # 40 Converted MD search papers across 4 subcategories:
        │   ├── 01_metaheuristic_neural_optimization/   # 10 MD papers
        │   ├── 02_financial_prediction_optimization/   # 10 MD papers
        │   ├── 03_optimizer_comparison_benchmark/      # 10 MD papers
        │   └── 04_mlp_optimization/                    # 10 MD papers
        ├── literature_all/             # 5 Converted MD survey papers (Gad, Rajwar, etc.)
        ├── additional_key_papers/      # 1 Converted MD paper (Makridakis et al. 2018)
        ├── s00521_2025_11546_2_nca_benchmark.md # Anchor NCA benchmark paper (Dhingra 2025)
        ├── ijcnn_precursor_paper.md     # Group precursor 1 (Souza et al. 2025 ICCSA)
        └── ijcnn_deep_learning_ga_paper.md # Group precursor 2 (Souza et al. 2026 IJCNN)
```

---

## 3. Verified Reference Audit Status

- **Total PDF Files**: **93 PDFs** (40 in `nca_journal_521_pdfs/`, 40 in `nca_search/papers/`, 6 in `literature/`, 6 in `references/` root).
- **Total Markdown Files**: **99 MDs** (90 converted full-text papers + 9 structural & writing guides).
- **Conversion Audit**: **100% of all PDF literature files have been fully converted into clean Markdown (.md)** and indexed under `md_references/`.

---

## 4. Important Instructions for AI Agents & Collaborators

### A. Double-Blind Peer Review Compliance
- **Main Manuscript (`manuscript/main.tex` and `manuscript/sections/`)**: Must remain **100% anonymized**. Never include author names, affiliations, emails, or explicit grant numbers in `main.tex` or any file in `sections/`.
- **Title Page (`manuscript/titlepage.tex`)**: Contains all author metadata, ORCIDs, affiliations (FURG, UNESP, UniRV), corresponding author emails, and grant acknowledgments (FAPERGS, CNPq).

### B. Master Writing & Structural Guidelines
- Before writing or editing any section, you MUST consult **[NCA_STRUCTURAL_AND_WRITING_PATTERNS.md](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/references/NCA_STRUCTURAL_AND_WRITING_PATTERNS.md)**.
- Follow the 5 rhetorical moves (CARS Model) for the Introduction and list the **6 bulleted contributions in bold** using active present-tense verbs (*"We conduct..."*, *"We establish..."*).
- Table 1 in Section 2 must follow the *Representative Literature & Unmet Limitations* format.

### C. Compilation Commands (MiKTeX LaTeX)
To recompile the PDF outputs from PowerShell, run:
```powershell
Set-Location 'article\manuscript'
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode titlepage.tex
```

### D. Citation & Literature Integration
- Always query the 90 Markdown files in `article/references/md_references/` to cite recent 2024–2026 NCA papers and ground all methodological decisions in published literature.
