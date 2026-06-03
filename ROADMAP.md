# ROADMAP.md - NCA Optimizer Benchmark

Status: active
Last update: 2026-06-03
Target journal: Neural Computing and Applications

## Goal

Build a reproducible journal-grade benchmark of evolutionary and swarm
intelligence optimizers for MLP-based intraday trend classification in Brazilian
futures markets.

## Phases

| Phase | Status | Objective |
|---|---|---|
| 0. Context and structure | DONE | Define research lineage, folders, runbook, and benchmark framing |
| 1. Data migration | DONE | Move the benchmark dataset from legacy `experiments/` into `data/raw/` |
| 2. Minimum benchmark | DONE | Implement Random Search vs GA vs PSO with temporal split and equal budget |
| 3. Evidence generation | DONE | Save metrics, predictions, convergence curves, figures, and summary report |
| 4. Reproduction baselines | IN PROGRESS | Keep ICCSA and IJCNN baseline references reproducible and documented |
| 5. Optimizer expansion | BACKLOG | Add DE and GWO after the first benchmark is validated |
| 6. Statistical analysis | BACKLOG | Add Friedman, Wilcoxon-Holm, and effect sizes with more seeds |
| 7. Financial evaluation | BACKLOG | Add simple trading/backtesting metrics and transaction-cost sensitivity |
| 8. Manuscript | BACKLOG | Prepare anonymous Springer Nature manuscript and separate title page |

## Current Executable Target

```powershell
python scripts\02_run_random_search.py
python scripts\03_run_ga.py
python scripts\04_run_pso.py
python scripts\07_compare_optimizers.py
```

## Data Policy

The clean benchmark pipeline uses:

```text
data/raw/merged_output.csv
```

The `experiments/` folder is legacy material and should not be required by the
current implementation.
