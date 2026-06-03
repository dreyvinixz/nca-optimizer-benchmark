# TASKS.md - NCA Optimizer Benchmark

Status: active
Last update: 2026-06-03

## Tasks

| ID | Status | Objective |
|---|---|---|
| NCA-001 | DONE | Define project context, scientific framing, and target journal |
| NCA-002 | DONE | Create repository structure for `article`, `config`, `data`, `src`, `scripts`, and `outputs` |
| NCA-003 | DONE | Move benchmark dataset to `data/raw/merged_output.csv` |
| NCA-004 | DONE | Configure paths, experiment protocol, and MLP search space |
| NCA-005 | DONE | Implement data loading, preprocessing, feature selection, and temporal split |
| NCA-006 | DONE | Implement central objective function with MCC/F1 fitness |
| NCA-007 | DONE | Implement Random Search baseline |
| NCA-008 | DONE | Implement GA with equal evaluation budget |
| NCA-009 | DONE | Implement PSO with equal evaluation budget |
| NCA-010 | DONE | Generate optimizer comparison tables, convergence figure, metric figure, and summary |
| NCA-011 | DONE | Add ICCSA and IJCNN baseline reference scripts |
| NCA-012 | IN PROGRESS | Audit first benchmark outputs and decide whether TensorFlow training should replace NumPy fallback |
| NCA-013 | BACKLOG | Add DE after Random Search, GA, and PSO are validated |
| NCA-014 | BACKLOG | Add GWO after Random Search, GA, and PSO are validated |
| NCA-015 | BACKLOG | Expand statistical tests with Friedman, Holm correction, and effect sizes |
| NCA-016 | BACKLOG | Add financial backtesting and transaction-cost sensitivity |
| NCA-017 | BACKLOG | Prepare anonymous manuscript and separate title page |

## Immediate Next Actions

1. Review `outputs/tables/optimizer_comparison.csv`.
2. Decide whether to install TensorFlow for the final neural training backend.
3. Increase seeds only after the first pipeline is scientifically audited.
