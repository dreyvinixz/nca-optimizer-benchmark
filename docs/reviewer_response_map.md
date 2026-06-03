# Reviewer Response Map

This document maps the IJCNN reviewer concerns to the new NCA benchmark design.

| IJCNN concern | NCA response |
|---|---|
| Limited novelty | Reframe as controlled optimizer benchmark, not single GA extension |
| Lack of optimizer comparison | Compare Random Search, GA, and PSO first; expand to DE and GWO later |
| Weak baselines | Include Random Search as a mandatory baseline |
| Insufficient temporal validation | Use chronological train/validation/test split without shuffle |
| Potential leakage | Fit scaler only on training data and keep test untouched during search |
| Accuracy-heavy evaluation | Add balanced accuracy, F1, MCC, AUC-ROC, AUC-PR, confusion matrix |
| No convergence analysis | Save convergence by fitness evaluation for every optimizer |
| No statistical tests | Placeholder retained for final Friedman/Wilcoxon-Holm stage |
| No economic evaluation | Placeholder retained for final financial backtesting stage |
| Limited reproducibility | Use YAML configs, thin scripts, central objective, and CSV outputs |
