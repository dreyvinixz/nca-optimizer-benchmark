# Multi-scale intraday label study

This branch contains the focused project plan for evaluating joint and separate
models of B0 intraday labels at 5, 10, and 15 minutes. The research scope,
data constraints, validation protocol, and phase exit criteria are in
[ROADMAP_ONE_MINUTE_LABELS.md](ROADMAP_ONE_MINUTE_LABELS.md).

The actionable phase and task checklist is in [task.md](task.md).

CPU baselines and a compact MLP have been evaluated on the four expanding
development folds; the final test dates have not been scored. The contracts and
first feature cache are defined. The cache is local/ignored, while its hash,
coverage, split dates, and leakage checks are recorded in the report manifest.
To rebuild and rerun the development baselines in the existing WSL environment:

```bash
source scripts/wsl_cuda_env.sh
.venv_wsl/bin/python scripts/build_features.py
.venv_wsl/bin/python scripts/audit_leakage.py
.venv_wsl/bin/python scripts/run_baseline_cv.py
.venv_wsl/bin/python scripts/run_mlp_cv.py
```

Keep source code, configuration, and small traceable summaries here; use the
external BovDB sources described in the roadmap without modifying them.
