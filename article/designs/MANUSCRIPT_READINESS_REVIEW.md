# MANUSCRIPT READINESS REVIEW — Current Pre-Submission Audit

**Journal target:** Neural Computing and Applications (NCA)
**Scope:** `article/manuscript/main.tex` and the official benchmark artifacts
**Status:** Current as of the three-seed, two-holdout-protocol benchmark

| Dimension | Current assessment | Evidence |
| :--- | :--- | :--- |
| Design | Chronological 60/20/20 split; 15,057 five-minute WIN bars; locked test block. | `config/experiment_config.yaml`, `sections/nca_methods.tex` |
| Budget parity | 1,000 candidate evaluations per optimizer and seed; population methods use 10 candidates for 100 iterations/generations. | `config/protocol_experiments.yaml`, `scripts/run_article_official_benchmark.py` |
| Replication | Three common seeds per model--optimizer cell. Fitness comparisons are descriptive; model tests are exploratory. | `outputs/article_official/`, `outputs/article_official_accuracy_holdout/`, `sections/nca_results.tex` |
| Reproducibility | Search-space bounds, optimizer controls, scaling procedure, test refit, and economic execution rule are specified. | `config/search_spaces.yaml`, `config/experiment_config.yaml`, `sections/nca_methods.tex` |
| Double blind | Funding, contributions, dataset self-citation, and precursor citation are anonymized in the main manuscript. Author metadata remain only in `titlepage.tex`. | `sections/declarations.tex`, `references.bib` |
| Reporting limits | One instrument and one chronological test period; no confirmatory claim about either fitness function or deployable trading performance. | `sections/nca_discussion.tex`, `sections/nca_results.tex` |

## Determination

The manuscript is suitable for a further editorial and statistical review, but not yet a final submission package. The main remaining scientific limitation is the three-seed, single-test-period design. A preregistered multi-period study with at least 20 common seeds is required for confirmatory claims; it is not required to describe the present study as exploratory.
