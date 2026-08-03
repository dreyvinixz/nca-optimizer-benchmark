# Complete Anatomical Blueprint — Al Bannoud et al. (NCA 2026)
**Reference Paper**: *Accelerating hybrid ANN–ODE frameworks using surrogate machine learning and metaheuristic optimization for predicting recurrent venous thromboembolism*  
**Journal**: Neural Computing and Applications (Springer Nature, Journal ID 521, Vol 38:285, 2026)  
**DOI**: `10.1007/s00521-026-12047-6` | **Length**: 49 Pages

---

## 🏛️ 1. Complete Section & Subsection Structure

```text
Neural Computing and Applications (2026) 38:285
ORIGINAL ARTICLE

Title: Accelerating hybrid ANN–ODE frameworks using surrogate machine learning...
Authors: Mohamad Al Bannoud, Tiago Dias Martins, Silmara Aparecida de Lima Montalvão, et al.
Received / Accepted / Published online dates
Abstract & Keywords (Page 1)
Abbreviations List (Page 2)

1 Introduction (Pages 3–4)
  • Clinical motivation, VTE risk scores, hybrid ML–ODE motivation, stiff ODE bottleneck, research gap & 4 main contributions.

2 Materials and methods (Pages 4–14)
  2.1 Dataset generation (Pages 4–5)
      • Sobol sampling over 41 kinetic parameters (50–300% nominal range), 100,000 parameter sets, BDF stiff solver.
  2.2 Machine learning models training and evaluation (Pages 5–6)
      • 14 ML models (LR, RR, Lasso, EN, BR, SVR, KNN, DT, RF, GB, XGBoost, LightGBM, CatBoost, ANN).
      • Z-score scaling, 5-fold CV on training set (70%), held-out test set (30%), RMSE & R² equations.
  2.3 Hybrid ANN-surrogate modeling (Pages 6–8)
      • Patient data (N=235), MLP surrogate mapping clinical data to kinetic parameters, satlins & tansig activations.
  2.4 Optimization (Pages 9–10)
      • Metaheuristic search engines (GWO, PSO, GA, ABC, ACO, BA, FA, WOA) maximizing Discriminant Margin Potential (DMP).
  2.5 Metrics for performance evaluation of surrogate models (Page 10)
      • Accuracy (ACC), True Positive Rate (TPR/Sensitivity), True Negative Rate (TNR/Specificity), F1-Score, AUC.
  2.6 Improved analysis on the best surrogate model (Pages 10–14)
      2.6.1 Comparison with gradient-based optimizer algorithms (SGD, Adam, RMSProp)
      2.6.2 Improvements in the binary classifier (Youden's J index threshold optimization)
      2.6.3 Impact of pipeline design choices on RVTE prediction performance (PCA vs full features, normalization)
      2.6.4 Ablations on clinical input features and kinetic parameter subsets (Comprehensive vs Selective parameters)
      2.6.5 Permutation-importance analysis (Feature contribution ranking)
      2.6.6 Performance variability across independent runs (Bootstrap medians and 95% CIs)

3 Results (Pages 15–40)
  3.1 Comparative performance benchmarking of machine learning surrogates (Pages 15–20)
      • Regression performance across 14 surrogates (Table 4, Figs 4–5).
      • Model-by-model surrogate vs true ODE optimization comparisons (Tables 5–11).
      • Master binary classification matrix across 14 models × 8 optimizers (Table 12, Fig 6).
      • True ANN-ODE framework benchmark (Table 13) and discrimination comparison (Table 14).
  3.2 Detailed evaluation of the best-performing ANN surrogate (Pages 20–40)
      • Gradient-based vs metaheuristic strategy comparisons (Table 15, Figs 7–8).
      • Bootstrap median and 95% CIs across runs (Table 16 for ANN surrogate, Table 17 for ODE reference).
      • Pipeline configuration sensitivity ablation (Table 18).
      • Pairwise DeLong test comparisons of AUCs across optimizers (Table 19).
      • Robustness, convergence efficiency, and statistical rankings (Table 20, Figs 9–10).

4 Discussion (Pages 40–44)
  4.1 Mechanistic interpretation and clinical trade-offs
  4.2 Scalability to complex parameter spaces
  4.3 Local trapping risks in metaheuristic algorithms
  4.4 Methodological boundaries and future outlook

5 Conclusion (Page 44)
Declarations (Page 45)
References (Pages 45–49)
```

---

## 📊 2. Inventory of All 20 Tables (Purpose, Placement, and Structure)

| Table # | Page | Title / Subject | Structural Role & Content |
| :--- | :--- | :--- | :--- |
| **Table 1** | P. 7 | *Hyperparameter search spaces for grid search optimization of machine learning regression models* | Defines hyperparameter names, grid search spaces, and domain types for all 14 ML regression models. |
| **Table 2** | P. 9 | *Summary of model configuration options explored for hybrid ANN-Surrogate framework optimization* | Summarizes pipeline design choices: normalization (MinMax vs Standard), features (All vs PCA), scope (Selective vs Comprehensive), network width, and optimization criterion (DMP, Sparse, Full). |
| **Table 3** | P. 11 | *Quantitative metrics for assessing accuracy and efficiency of surrogate models within the hybrid ANN–ODE framework* | Defines mathematical formulas and descriptions for RMSE, R², ACC, TPR, TNR, F1-Score, AUC, and Runtime. |
| **Table 4** | P. 15 | *Performance comparison of machine learning surrogate models in predicting ETP* | Reports Training RMSE, Training R², Test RMSE, and Test R² across all 14 surrogate models. |
| **Table 5** | P. 18 | *Comparative analysis of surrogate-based optimization versus true ODE simulation using Decision Tree* | Compares DT surrogate vs true ODE across 8 optimizers (DMP, ETP separation, accuracy, time). |
| **Table 6** | P. 18 | *Comparative analysis of surrogate-based optimization versus true ODE simulation using Random Forest* | Compares RF surrogate vs true ODE across 8 optimizers. |
| **Table 7** | P. 18 | *Comparative analysis of surrogate-based optimization versus true ODE simulation using Gradient Boosting* | Compares GB surrogate vs true ODE across 8 optimizers. |
| **Table 8** | P. 19 | *Comparative analysis of surrogate-based optimization versus true ODE simulation using XGBoost* | Compares XGBoost surrogate vs true ODE across 8 optimizers. |
| **Table 9** | P. 19 | *Comparative analysis of surrogate-based optimization versus true ODE simulation using LightGBM* | Compares LightGBM surrogate vs true ODE across 8 optimizers. |
| **Table 10** | P. 19 | *Comparative analysis of surrogate-based optimization versus true ODE simulation using CatBoost* | Compares CatBoost surrogate vs true ODE across 8 optimizers. |
| **Table 11** | P. 20 | *Comparative analysis of surrogate-based optimization versus true ODE simulation using ANN* | Compares ANN surrogate vs true ODE across 8 optimizers (shows ANN achieves lowest RMSE). |
| **Table 12** | P. 21–25 | *Binary classification performance of the ANN-Surrogate framework across ML algorithms and optimization methods* | **Master 5-Page Matrix**: Reports AUC, ACC, TPR, TNR, F1, and Runtime for 14 ML models × 8 Metaheuristics. |
| **Table 13** | P. 26–30 | *Binary classification performance of the true ANN–ODE framework using parameters optimized via metaheuristics* | Reports true ODE performance using optimal parameters found by each surrogate-optimizer pair. |
| **Table 14** | P. 31–33 | *Comparative performance of ANN-GWO and alternative ML-MOA models in discriminating RVTE from non-RVTE* | Detailed clinical discrimination performance (ETP mean diff, p-values, sensitivity/specificity). |
| **Table 15** | P. 34 | *Performance comparison of gradient-based and metaheuristic optimization strategies* | Compares SGD, Adam, RMSProp vs GWO, PSO, GA, ABC, WOA, ACO, BA, FA. |
| **Table 16** | P. 35–37 | *Performance of ANN surrogate models optimized by metaheuristic and gradient-based algorithms (bootstrap medians & 95% CIs)* | Bootstrapped medians and 95% confidence intervals for training/testing ACC, AUC, F1 across runs. |
| **Table 17** | P. 38–40 | *Performance of ODE-based reference models optimized by metaheuristic and gradient-based algorithms (bootstrap medians & 95% CIs)* | Bootstrapped reference baseline performance. |
| **Table 18** | P. 41 | *Sensitivity of RVTE prediction performance to framework configuration across metaheuristic optimizers* | Ablation table evaluating impact of normalization (Standard vs MinMax), PCA, and parameter scope. |
| **Table 19** | P. 42 | *Pairwise DeLong comparison of AUCs across optimization algorithms for RVTE prediction* | Pairwise statistical significance matrix ($Z$-statistic and $p$-values) comparing ROC-AUC curves. |
| **Table 20** | P. 43 | *Robustness, convergence efficiency, predictive performance, and statistical comparison of metaheuristic algorithms* | Final ranking table summarizing robustness index, median evaluations to convergence, and overall rank. |

---

## 📈 3. Inventory of All 10 Figures (Purpose, Components, and Placement)

| Figure # | Page | Description / Content |
| :--- | :--- | :--- |
| **Fig. 1** | P. 5 | *Overview of computational workflow*: High-level system diagram showing ODE sampling, surrogate dataset assembly, 14 ML model training, hybrid ANN-ODE optimization, and binary risk classification. |
| **Fig. 2** | P. 8 | *Schematic of data partitioning, preprocessing, and model optimization pipeline*: Pipeline layout showing 70/30 split, Z-score normalization, grid search CV, and held-out test set isolation. |
| **Fig. 3** | P. 9 | *Hybrid ANN-Surrogate modeling framework*: Technical network diagram showing clinical inputs $X$, hidden layer weights $W^1$, output layer weights $W^2$, satlins/tansig activation, and kinetic output $K_r$. |
| **Fig. 4** | P. 16 | *Residual diagnostics for ML regression models (Part 1)*: Residual vs fitted plots and error distribution histograms for linear and tree-based surrogates. |
| **Fig. 5** | P. 17 | *Residual diagnostics for ML regression models (Part 2)*: Residual plots for boosting and ANN surrogate models. |
| **Fig. 6** | P. 20 | *Performance evaluation boxplots across metaheuristic algorithms*: Multi-panel boxplot comparing AUC, ACC, and runtime distributions across 8 metaheuristics. |
| **Fig. 7** | P. 34 | *ROC curves for the test set of hybrid models*: Receiver Operating Characteristic curves comparing GWO, PSO, GA, and gradient-based baselines. |
| **Fig. 8** | P. 34 | *Convergence trajectories of metaheuristic optimization algorithms*: Objective function fitness vs iteration count for GWO, PSO, GA, DE, ABC, ACO, BA, FA. |
| **Fig. 9** | P. 34 | *Radar plots comparing MOAs across ML models*: Multi-metric radar chart evaluating ACC, TPR, TNR, F1, AUC, and Speed across algorithms. |
| **Fig. 10** | P. 35 | *Radar plots comparing ML models across MOAs*: Multi-metric radar chart evaluating surrogate accuracy across ML model families. |
