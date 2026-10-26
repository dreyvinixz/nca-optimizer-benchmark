# Multi-scale intraday label study

This branch contains the focused project plan for evaluating joint and separate
models of B0 intraday labels at 5, 10, and 15 minutes. The research scope,
data constraints, validation protocol, and phase exit criteria are in
[ROADMAP_ONE_MINUTE_LABELS.md](ROADMAP_ONE_MINUTE_LABELS.md).

The actionable phase and task checklist is in [task.md](task.md).

Fases 0–6 are complete. The frozen final evaluation ran once over 25 test
sessions; the main paired independent-versus-shared MLP intervals include zero
at all three label scales. The conditional extension phase was closed without
an extension, and an internal manuscript draft is in `manuscript/`. The cache
and row-level predictions are local/ignored; compact summaries, source hashes,
coverage, splits, and leakage checks are recorded in `reports/`.

The test has already been opened. Do not rerun it for model or hyperparameter
selection. The original frozen run and the non-refitting summary command are
shown below for provenance:

```bash
source scripts/wsl_cuda_env.sh
.venv_wsl/bin/python scripts/build_features.py
.venv_wsl/bin/python scripts/audit_leakage.py
.venv_wsl/bin/python scripts/run_baseline_cv.py
.venv_wsl/bin/python scripts/run_mlp_cv.py
.venv_wsl/bin/python scripts/run_multiscale_cv.py
.venv_wsl/bin/python scripts/summarize_multiscale_cv.py
# Run only if reproducing the already completed final evaluation:
.venv_wsl/bin/python scripts/run_final_evaluation.py
.venv_wsl/bin/python scripts/summarize_final_test.py
```

The final model runner requires the committed pre-registration and the exact
committed runner source. `summarize_final_test.py` derives pooled, root, block,
and contract summaries from the saved one-pass predictions; it does not refit
models. See [the final report](reports/final_test.md), [the task checklist](task.md),
and [the manuscript draft](manuscript/multiscale_b0_label_prediction_draft.md).

Keep source code, configuration, and small traceable summaries here; use the
external BovDB sources described in the roadmap without modifying them.
