# Multi-scale intraday label study

This branch contains the focused project plan for evaluating joint and separate
models of B0 intraday labels at 5, 10, and 15 minutes. The research scope,
data constraints, validation protocol, and phase exit criteria are in
[ROADMAP_ONE_MINUTE_LABELS.md](ROADMAP_ONE_MINUTE_LABELS.md).

The actionable phase and task checklist is in [task.md](task.md).

CPU baselines and multi-scale MLP comparisons have been evaluated on the four
expanding development folds; the final test dates have not been scored. The
contracts and feature cache are defined. The cache and row predictions are
local/ignored, while hashes, coverage, splits, and leakage checks are recorded
in manifests/reports. In the existing WSL environment:

```bash
source scripts/wsl_cuda_env.sh
.venv_wsl/bin/python scripts/build_features.py
.venv_wsl/bin/python scripts/audit_leakage.py
.venv_wsl/bin/python scripts/run_baseline_cv.py
.venv_wsl/bin/python scripts/run_mlp_cv.py
.venv_wsl/bin/python scripts/run_multiscale_cv.py
.venv_wsl/bin/python scripts/summarize_multiscale_cv.py
```

Keep source code, configuration, and small traceable summaries here; use the
external BovDB sources described in the roadmap without modifying them.
