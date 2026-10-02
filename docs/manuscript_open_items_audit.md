# Manuscript audit: remaining methodological items

Updated: 2026-10-02. Scope: current active manuscript in `article/manuscript/merged_parallel_working/` and supporting experiment artifacts available in this repository.

## Addressed in the current manuscript revision

- **Target alignment and execution timing:** documents five-minute features, labels generated from retrospective hourly pivot regimes, `y[t] = r[t+1]` for 15,053 rows with successors, next-bar trade entry, 196 session-final rows whose successor is next session, and four terminal exceptions. It explicitly states that a one-row shift does not make retrospective pivots causal.
- **Partition crossings:** documents the one train-to-validation and two validation-to-test shifted-target crossings, the four terminal source-label exceptions, and the cutoff-only replay result (9,032 training and 3,008 validation records unchanged). It no longer calls the test fully isolated or locked.
- **Fitness protocols:** equations and prose identify the MCC/`F_1` validation-only objective, weighted-accuracy objective using 0.4 training plus 0.6 validation accuracy, and the analogous three-fold temporal CV objective. The comparison is explicitly described as between complete protocols, since both metric and data composition differ.
- **RQ2:** revised to ask about behavior under a common chronologically subsequent test interval with temporal model selection. The old randomized-CV-versus-chronological comparison is not claimed as an experiment. The current RQ is answerable descriptively by the reported experiments, subject to boundary-label caveats.
- **Statistical inference:** says the 15 optimizer-seed blocks share the same market interval; ranks/p-values are exploratory and conditional on that interval, not independent market replications.
- **Computational complexity and practical cost:** adds asymptotic optimizer-overhead analysis, separates it from model-fit cost, and adds a grouped bar figure based on uncached candidate-model fits. The prose states the conditional pattern for RS and does not assert universal inferiority.
- **Figure 21 label collision:** shortened radar labels remain separated and were visually rechecked in the final PDF.
- **CNN diagram semantics:** changed “Time steps” and temporal-convolution wording to “Feature index” and convolution across the ordered feature axis, matching the implemented input shape `(7,1)`.
- **Literature review label:** changed from “Systematic Literature Review”/PRISMA implication to structured literature comparison/narrative synthesis.
- **Model implementation detail:** documents MLP and CNN layout, seven-feature CNN axis, optimizer/loss, epoch cap, early stopping, non-shuffled fit, and seed handling based on source code.
- **Economic interpretation:** methods define daily Sharpe and next-bar execution with the fixed five-point round-trip cost; discussion keeps the economic backtest diagnostic and discloses omitted execution effects.
- **Final PDF:** recompiled the current manuscript and inspected all 45 rendered pages, with enlarged review of changed Methods, cost figure/table, and limitations pages. No overfull box, undefined reference, duplicated label, clipped object, or caption collision was found.

## Still open; needs a new experiment or archived artifact

1. **Purged rerun.** Purge the three direct partition-crossing target rows and the four terminal exceptions, and purge each temporal-CV fold boundary; rerun selection, test metrics, economic results, inferential summaries, convergence/cost plots, tables, and abstract/conclusion claims. Existing results remain exploratory until this is done. The cutoff-only label replay does not replace a purged benchmark.
2. **Retrospective target availability.** The hourly pivot generator is reproduced exactly against 23,181 archived rows, but the pivot labels use later confirmation information. Retain pivot-detection and confirmation timestamps in a future causal target design; the present target cannot support a fully live-available forecast claim.
3. **WEKA artifact.** The author recalls that Information Gain was run only on the January–March chronological training segment and that April–June test observations were excluded. The seven-feature list and split are present, but the original WEKA project, output, and settings are unavailable. This history is now transparently qualified; independent replay is impossible without the artifact or a new feature-selection rerun.
4. **Common absolute quality-versus-compute curve.** Current 95%-of-own-gain statistic compares relative within-run progress, not fits to a common fitness threshold. A fair common-threshold curve requires a prespecified threshold per model/protocol, or full fitness-versus-fit curves with a declared aggregation rule; it must not be inferred from the current bar chart.
5. **End-to-end wall-clock cost.** Candidate-level training seconds are archived and feed the manuscript’s normalized overview, but controlled total search wall-clock (including optimizer bookkeeping and orchestration) and energy are not measured. A timed rerun under documented hardware/software is needed for those claims.
6. **No-tuning references.** No-tuning baselines are missing for SVM, MLP, and 1D-CNN. Add them if the paper claims the measured gain comes from optimization rather than merely comparing tuned cells.
7. **Software environment.** The exact TensorFlow and scikit-learn versions for official runs are not archived. `requirements.txt` has lower bounds, not an exact lock file; bitwise reproduction is therefore not guaranteed.
8. **Statistical replication.** Three seeds and one test period do not establish cross-regime generalization. A stronger confirmatory study requires multiple non-overlapping market periods crossed with seeds and optimizers; merely adding seeds on the same interval is insufficient.
9. **Protocol interpretation.** The two holdout objectives differ in metric and in whether training accuracy contributes. Text now acknowledges this; the effect of metric alone remains unidentified unless a validation-only accuracy experiment is run.


## Decision boundary

The text and figure can close documentation and presentation issues, but they cannot convert the current non-purged results into strict test-isolated estimates. Do not present submission readiness as fully closed until item 1 is either completed or the study is explicitly submitted with the boundary leakage limitation accepted and all claims correspondingly narrowed.
