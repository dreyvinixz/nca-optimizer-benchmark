# Article Inventory — NCA Optimizer Benchmark

This inventory tracks all assets available for the manuscript.

## Manuscript Files

| File | Description | Status |
|---|---|---|
| `manuscript/main.tex` | Anonymous manuscript (sn-jnl.cls) | Skeleton |
| `manuscript/titlepage.tex` | Separate title page (double-blind) | Skeleton |
| `manuscript/references.bib` | BibTeX database | 15 entries |
| `manuscript/sections/introduction.tex` | Section 1 | Skeleton |
| `manuscript/sections/related_work.tex` | Section 2 | Skeleton |
| `manuscript/sections/data.tex` | Section 3 | Skeleton |
| `manuscript/sections/methodology.tex` | Section 4 | Skeleton |
| `manuscript/sections/results.tex` | Section 5 | Skeleton |
| `manuscript/sections/discussion.tex` | Section 6 | Skeleton |
| `manuscript/sections/limitations.tex` | Section 7 | Skeleton |
| `manuscript/sections/conclusion.tex` | Section 8 | Skeleton |
| `manuscript/sections/declarations.tex` | Declarations | Skeleton |

## Reference PDFs

### Research Lineage (in `references/`)
| File | Description |
|---|---|
| `_ICSSA_Document_2025_*.pdf` | ICCSA accepted paper (feature selection) |
| `_ICCSA_2026_*.pdf` | IJCNN extension (GA optimization) |
| `review_ijcnn.pdf` | IJCNN reviewer feedback |
| `s00521-025-11546-2.pdf` | NCA benchmark reference (solar PV) |

### Literature Reviews (in `references/literature/`)
| File | Description |
|---|---|
| `2022_particle_swarm_optimization_a_comprehensive_survey.pdf` | PSO comprehensive survey |
| `2022_particle_swarm_optimization_algorithm_and_its_applications_a_systematic_review.pdf` | PSO systematic review |
| `2023_an_exhaustive_review_of_the_metaheuristic_algorithms_*.pdf` | Metaheuristics exhaustive review |
| `2023_recent_advances_in_grey_wolf_optimizer_*.pdf` | GWO review |
| `2023_a_survey_on_evolutionary_neural_architecture_search.pdf` | Evolutionary NAS survey |

## Figures Available

| Source | Description | Location |
|---|---|---|
| Convergence curves | Best fitness vs evaluations (RS, GA, PSO) | `outputs/figures/` |
| Metric comparison | Bar/box plots per optimizer | `outputs/figures/` |
| Confusion matrices | Per optimizer, per seed | `outputs/figures/` |

## Tables Available

| Source | Description | Location |
|---|---|---|
| Optimizer comparison | Mean ± std metrics per optimizer | `outputs/tables/` |
| Hyperparameter summary | Best hyperparameters per optimizer | `outputs/tables/` |

## Missing Items

- [ ] Template files (sn-jnl.cls, sn-mathphys-num.bst) — need download
- [ ] NCA search results — need to run `scripts/search_nca_papers.py`
- [ ] DE and GWO experiment results — pending implementation
- [ ] Statistical test outputs — pending implementation
- [ ] Financial backtest outputs — pending implementation
- [ ] Cover letter — not yet drafted
- [ ] Final figures in EPS/TIFF format
