# Multi-scale intraday label study

This branch contains the focused project plan for evaluating joint and separate
models of B0 intraday labels at 5, 10, and 15 minutes. The research scope,
data constraints, validation protocol, and phase exit criteria are in
[ROADMAP_ONE_MINUTE_LABELS.md](ROADMAP_ONE_MINUTE_LABELS.md).

The actionable phase and task checklist is in [task.md](task.md).

The training study has not started. The contracts and first feature cache are
now defined. The cache is local/ignored, while its hash, coverage, split dates,
and leakage checks are recorded in the report manifest. To rebuild it in the
existing WSL environment:

```bash
source scripts/wsl_cuda_env.sh
.venv_wsl/bin/python scripts/build_features.py
.venv_wsl/bin/python scripts/audit_leakage.py
```

Keep source code, configuration, and small traceable summaries here; use the
external BovDB sources described in the roadmap without modifying them.
