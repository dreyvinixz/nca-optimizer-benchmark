# Accelerating hybrid ANN–ODE frameworks using surrogate machine learning and metaheuristic optimization for predicting recurrent venous thromboembolism

**Year**: 2026 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-026-12047-6

---

## Page 1
ORIGINAL ARTICLE
Neural Computing and Applications (2026) 38:285
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Accelerating hybrid ANN–ODE frameworks using 
surrogate machine learning and metaheuristic 
optimization for predicting recurrent venous 
thromboembolism
Mohamad Al Bannoud  · Tiago Dias Martins · Silmara Aparecida de Lima Montalvão · 
Joyce Maria Annichino-Bizzacchi · Rubens Maciel Filho · Maria Regina Wolf Maciel
Received: 12 October 2025 / Accepted: 25 February 2026 / Published online: 13 April 2026
© The Author(s) 2026
Abstract
Accurate and computationally efficient modeling of complex biological processes remains a major challenge in 
personalized medicine. This study introduces a hybrid framework that replaces the computationally intensive 
ordinary differential equation (ODE) system in hybrid artificial neural network–ODE (ANN–ODE) models 
with machine learning (ML) surrogate models. Using clinical and hematological data, the framework estimates 
patient-specific kinetic parameters of the coagulation cascade and predicts the endogenous thrombin potential 
(ETP), which serves as a discriminative threshold for classifying recurrent venous thromboembolism (RVTE) 
risk. Fourteen ML algorithms and eight metaheuristic optimization algorithms (MOAs) were systematically 
evaluated to identify optimal model–optimizer combinations. Among all candidates, the artificial neural net­
work (ANN) acts as the best surrogate, yielding a root mean squared error (RMSE) below 0.3 for both the 
training and test sets. The ANN coupled with the Grey Wolf Optimizer (ANN–GWO) achieved the best per­
formance, maintaining a relative accuracy of 97.97% compared with full ODE simulations, while reducing 
optimization time by over 99%. Particle swarm optimization (PSO) also exhibited competitive performance, 
confirming the robustness of swarm-based search strategies. These results demonstrate that replacing mechanis­
tic ODE systems with machine-learning surrogates can substantially reduce computational complexity without 
sacrificing predictive accuracy. The proposed ANN–GWO and ANN–PSO models provide efficient, accurate, 
and scalable computational tools for RVTE prediction and personalized medicine. The findings support the 
use of ANNs as surrogate models and highlight GWO and PSO as robust and reliable optimizers for RVTE 
prediction within the tested hybrid framework. This guidance is particularly relevant for further extensions and 
improvements of the hybrid framework that require low computational cost without compromising accuracy, 
such as backward and forward selection of clinical features and kinetic parameters.
Keywords  Recurrent venous thromboembolism · Surrogate machine learning · Blood coagulation cascade · 
Metaheuristic optimization
1 3

---

## Page 2
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Abbreviations
ABC	
Artificial Bee Colony
ACC	
Accuracy
ACO	
Ant Colony Optimization
Adam	
Adaptive Moment Estimation
ANN	
Artificial Neural Network
ANOVA	
Analysis of Variance
AT-III	
Antithrombin III
AUC	
Area Under the Curve
BA	
Bat Algorithm
BDF	
Backward Differentiation Formula
BR	
Bayesian Ridge Regression
CatBoost	
Categorical Boosting
CI	
Confidence Interval
CTESN	
Continuous-Time Echo State Networks
DCA	
Decision Curve Analysis
DMP	
Discriminant Margin Potential
DT	
Decision Tree
DVT	
Deep Vein Thrombosis
ETP	
Endogenous Thrombin Potential
EN	
ElasticNet Regression
FA	
Firefly Algorithm
GA	
Genetic Algorithm
GB	
Gradient Boosting
GWO	
Grey Wolf Optimizer
KNN	
K-Nearest Neighbors
LightGBM	
Light Gradient Boosting Machine
Lasso	
Lasso Regression
LR	
Linear Regression
MAD	
Mean Absolute Deviation
MAE	
Mean Absolute Error
ML	
Machine Learning
MLP	
Multilayer Perceptron
MOA	
Metaheuristic Optimization Algorithm
ODE	
Ordinary Differential Equation
PE	
Pulmonary Embolism
PSO	
Particle Swarm Optimization
QSP	
Quantitative Systems Pharmacology
RBC	
Red Blood Cell
RF	
Random Forest
RMSE	
Root Mean Squared Error
RMSProp	
Root Mean Square Propagation
ROC	
Receiver Operating Characteristic
RR	
Ridge Regression
RVTE	
Recurrent Venous Thromboembolism
SGD	
Stochastic Gradient Descent
SM	
Supplementary Material
1 3
285 
Page 2 of 49

---

## Page 3
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
SVR	
Support Vector Regression
TNR	
True Negative Rate
TPR	
True Positive Rate
VTE	
Venous Thromboembolism
WBC	
White Blood Cell
WOA	
Whale Optimization Algorithm
XGBoost	
eXtreme Gradient Boosting
1  Introduction
Thrombosis is characterized by the formation of abnormal blood clots within blood vessels, potentially obstruct­
ing normal blood flow. This pathological process underlies several severe conditions, including deep vein throm­
bosis (DVT), pulmonary embolism (PE), myocardial infarction, and ischemic stroke [1]. Thrombosis and its 
complications represent a primary global health concern, contributing to significant morbidity, mortality, and 
socioeconomic burden [2, 3]. Following an initial thrombotic event, a primary clinical concern is recurrence, 
influenced by factors such as inadequate anticoagulant therapy, malignancy, prothrombotic disorders, and poor 
treatment adherence [4, 5]. Accurate prediction of recurrent thrombosis is thus essential for guiding clinical deci­
sions, individualizing therapy, and improving long-term outcomes.
Various clinical risk scores have been developed and are routinely used in medical practice to predict venous 
thromboembolism (VTE), including the Khorana [6], Caprini [7], and Wells [8, 9] scores. For recurrent venous 
thromboembolism (RVTE), scores such as the Ottawa [10], DASH [11], and Vienna [12] have been proposed. 
Despite widespread use, these tools present several limitations: reliance on a restricted set of variables, limited 
adaptability to complex clinical scenarios, low specificity, and reduced applicability across diverse populations 
[13–15]. As an alternative, data-driven models, particularly those based on machine learning (ML), offer several 
advantages. These include the ability to incorporate a broader range of clinical, laboratory, and demographic vari­
ables, improved predictive accuracy, and the capacity to identify complex, nonlinear, and high-dimensional pat­
terns that often elude traditional statistical approaches [16–18]. Such models show strong potential for enhanced 
risk stratification and personalization of care in RVTE [19] and other complex conditions [20, 21].
A key barrier to clinical adoption of ML-based models for RVTE prediction is their black-box nature, which 
limits interpretability and hinders trust among healthcare professionals [22]. To address this, our group has pro­
posed a hybrid framework that integrates data-driven techniques with the mechanistic component of the blood 
coagulation process [23]. In this framework, clinical and hematological patient data are used to estimate personal­
ized kinetic parameters of the coagulation cascade, which vary substantially among models reported in the litera­
ture [24]. These parameters are then used to solve a system of ordinary differential equations (ODEs) modeling 
the coagulation cascade. From the resulting thrombin generation curve, the endogenous thrombin potential (ETP) 
is calculated and used, via a predefined optimal threshold, to classify patients as high or low risk for RVTE. This 
hybrid model poses its challenges. It combines a multilayer perceptron (MLP) to map clinical variables to kinetic 
parameters with a mechanistic ODE-based computation of ETP. Because the whole system is non-differentiable, 
traditional gradient-based optimization is not feasible, necessitating the use of gradient-free optimizers, such as 
metaheuristic algorithms, which do not require differentiability but typically require many function evaluations 
[25].
Despite their advantages, hybrid mechanistic–ML models face computational challenges, particularly due to 
the repeated solution of stiff ODE systems required during parameter estimation and optimization. Several strat­
egies have been explored in prior work to accelerate these computations, including surrogate modeling of stiff 
ODEs and advection–dispersion equations [26–28], quantitative systems pharmacology (QSP) model emulation 
[29], continuous-time echo state networks (CTESN) [30], neural ODEs [31, 32], and hybrid mechanistic–ML 
1 3
3
Page 3 of 49 
285

---

## Page 4
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
frameworks [23, 33, 34]. These approaches suggest that ML-based surrogates can faithfully approximate ODE 
outputs while reducing computational cost.
Building on this body of work, the present study focuses on a large-scale empirical evaluation of surrogate 
modeling within a clinically grounded hybrid framework for RVTE prediction. Rather than introducing the sur­
rogate concept, we investigate the application-specific performance of replacing a mechanistic blood coagulation 
model with ML surrogates that directly map patient-specific kinetic parameters to ETP. Therefore, it is necessary 
to rigorously assess the trade-offs among surrogate fidelity, computational throughput, and downstream diag­
nostic performance when embedded in a hybrid optimization pipeline to identify the best surrogate models and 
optimizer algorithms.
To this end, we present a comprehensive benchmark of 14 distinct ML algorithms acting as surrogates for a 
high-dimensional, stiff coagulation ODE system. We evaluate their integration with various metaheuristic opti­
mizers under a unified experimental protocol. By jointly analyzing optimization trajectory behavior, surrogate 
approximation error, and final RVTE classification accuracy, this work provides evidence-based guidance for 
selecting surrogate–optimizer pairs. The primary contribution of this study lies in the RVTE-specific integration 
of surrogate modeling into a hybrid mechanistic–ML framework and in the breadth of the empirical evaluation. 
By systematically benchmarking surrogate–optimizer combinations, this work provides practical, application-
driven guidance for designing and optimizing hybrid data-driven and mechanistic modeling pipelines for hema­
tological diseases, particularly those involving blood clot formation and growth.
2  Materials and methods
Figure 1 summarizes the workflow pipeline used in this study. The main steps are: (i) generate an input matrix 
by varying the values of kinetic parameters of a blood coagulation cascade represented by a system of ODEs, (ii) 
compute the target variable (ETP), (iii) train 14 ML models to predict ETP from kinetic parameters, (iv) replace 
the ODE solver with surrogate models in a hybrid framework linking clinical and hematological data to kinetic 
parameters, ETP, and clinical outcome (RVTE or non-RVTE), (v) optimize the hybrid model using eight meta­
heuristic algorithms, and (vi) evaluate surrogate model performance in accuracy and optimization acceleration. 
Further details are provided in the following subsections.
2.1  Dataset generation
The dataset used for surrogate model training was generated from a mechanistic ODE system describing the 
blood coagulation cascade. The underlying model of the extrinsic pathway, initially proposed by Zhu [35], cap­
tures the dynamic interactions among 27 biochemical species via 41 kinetic reactions and has been used in previ­
ous studies [23, 36]. Baseline kinetic parameters, including catalytic rate constants, Michaelis-Menten constants, 
and other rate constants, along with species’ initial concentrations and mathematical equations, are detailed in the 
Supplementary Material (SM).
A Sobol quasi-random sampling method was employed to generate 100,000 parameter sets by varying each 
baseline kinetic parameter between 50% and 300% of its nominal value, ensuring uniform coverage of the high-
dimensional input space. The choice of sampling kinetic parameters within 50–300% of their nominal values was 
motivated by the recognition that coagulation kinetics exhibit substantial interindividual variability and are influ­
enced by demographic, clinical, and experimental factors [23, 34]. Although many mechanistic coagulation mod­
els assume fixed kinetic constants, prior studies have demonstrated that these parameters can vary widely across 
experimental conditions and model formulations, with some kinetic parameters differing by orders of magnitude 
across published models [24]. Previous analyses have explored kinetic parameter ranges spanning 50–150% 
[37] and even 10–1000% [38] around nominal values. In this context, the selected 50–300% sampling range 
1 3
4285 
Page 4 of 49

---

## Page 5
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
represents a defensible compromise that captures biologically plausible variability while maintaining numerical 
stability and interpretability.
Each sampled parameter set was used to numerically solve the ODE system over a 10-minute interval with a 
time step of 0.0001 min, using the backward differentiation formula (BDF) method for stiff systems. The output 
of interest, thrombin concentration, was integrated over time via the trapezoidal method to compute the ETP, a 
widely used measure of thrombin generation capacity.
The final dataset comprised 100,000 samples, each with 41 input features (kinetic parameters) and one target 
variable (ETP, computed via the BDF solver). The dataset was randomly split into training (70%) and testing 
(30%) subsets. To prevent data leakage, all preprocessing steps, including normalization, model training, and 
hyperparameter tuning, were conducted exclusively on the training set. The test set was reserved solely for evalu­
ating model performance on unseen data.
2.2  Machine learning models training and evaluation
To develop surrogate models for predicting ETP, we evaluated 14 ML algorithms: Linear Regression (LR), Ridge 
Regression (RR), Lasso Regression (Lasso), ElasticNet Regression (EN), Bayesian Ridge Regression (BR), Sup­
port Vector Regression (SVR), K-Nearest Neighbors (KNN), Decision Tree (DT), Random Forest (RF), Gradient 
Fig. 1  Overview of the 
computational workflow 
for surrogate modeling and 
hybrid optimization
 
1 3
5
Page 5 of 49 
285

---

## Page 6
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Boosting (GB), eXtreme Gradient Boosting (XGBoost), Light Gradient Boosting Machine (LightGBM), Cate­
gorical Boosting (CatBoost), and Artificial Neural Network (ANN). Input features were normalized using Z-score 
normalization, computed as z = (x −µ)/σ, where µ and σ are the mean and standard deviation of the training 
data, respectively. The target variable (ETP) was also normalized using the same Z-score method to improve 
numerical stability and model convergence.
Each surrogate model was trained using normalized input features derived exclusively from the training set. 
Model development employed 5-fold cross-validation within the training data, and performance metrics were 
computed on the corresponding validation folds to guide hyperparameter selection. This procedure ensured 
robust model tuning while preventing information leakage from the independent test set.
After hyperparameter optimization, the final model configuration for each algorithm was retrained on the full 
training set and subsequently evaluated on the held-out test set, which was not used at any stage during training or 
model selection. Model predictions were inverse-transformed back to the original ETP scale prior to performance 
evaluation, ensuring that all reported error metrics were expressed in clinically interpretable units (nM·min).
Predictive performance was quantified using the root mean squared error (RMSE) and the coefficient of deter­
mination (R²), defined in Eqs. (1) and (2), respectively. Those metrics were calculated for both training and test­
ing sets.
For each algorithm, a comprehensive grid-based hyperparameter search was performed over a predefined 
parameter space. All possible combinations of hyperparameter values were systematically evaluated, and each 
candidate model was trained and validated using the cross-validation framework described above. The complete 
hyperparameter grids explored for each algorithm are reported in Table 1.
Figure 2 provides a schematic representation of the experimental workflow, highlighting the strict separation 
between training and testing partitions to prevent data leakage during feature scaling and hyperparameter optimi­
zation. This pipeline ensures that the independent test set remains isolated until the final performance assessment.
All computations were implemented in MATLAB version R2021, and Python v3.12.7, using the following 
libraries and versions: NumPy v1.26.4, Pandas v2.2.2, scikit-learn v1.5.1, XGBoost v2.1.2, LightGBM v4.5.0, 
CatBoost v1.2.7, and joblib v1.4.2. These libraries were used for data preprocessing, model implementation, 
training, and evaluation. All computational tasks were executed on a system with an AMD Ryzen 7900X pro­
cessor, an NVIDIA RTX 4090 GPU, and 32 GB of DDR5 RAM, running Windows 11. When feasible, parallel 
computing was used.
	
RMSE =



 1
n
n

i=1
(yi −yi)2
(1)
	
R2 = 1 −
n
i=1 (yi −yi)2
n
i=1

yi−
−y
2 
(2)
Here, RMSE is the RMSE, R2 is the R², n is the number of data points, yi is the actual value, yi is the predicted 
value, and 
−y is the mean of the actual values.
2.3  Hybrid ANN-surrogate modeling
The model used in this study to relate patient clinical data, kinetic parameters, ETP, and clinical outcome (RVTE) 
was based on the framework established in our previous study [23]. This study utilized clinical and hematological 
data from 235 patients who were monitored following a confirmed VTE event. Among these, 49 patients expe­
rienced a RVTE episode after discontinuing anticoagulant therapy. Details of the clinical variables are available 
in prior publications [23, 36, 39]. For model development, stratified patient data splitting was applied, allocating 
70% of the patients to the training set and the remaining 30% to the test set.
1 3
6285 
Page 6 of 49

---

## Page 7
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
In this study, we aimed to replace the computationally intensive ODE system with surrogate models, as 
illustrated in Fig. 3. To achieve this, various combinations of model configurations and hyperparameters were 
explored, as summarized in Table 2. The primary goal was to optimize the weights and biases of the ANN, which 
maps patient-specific clinical and hematological data to kinetic parameters, as formalized in Eq. 3.
	
K = satlins [W 2 · tansig (W 1 · X + b1) + b2]
(3)
In this formulation, W 1 ∈Rnn×nf and W 2 ∈Rnk×nn are the weight matrices of the first and second layers, 
respectively. b1 ∈Rnn and b2 ∈Rnk are the corresponding bias vectors. The input feature vector X passes 
through a two-layer feedforward ANN, where the hidden layer uses, in this study, a hyperbolic tangent sigmoid 
activation function (tansig), and the output layer applies a symmetric saturating linear function (satlins) to con­
strain values to the range [− 1, 1]. The network output is subsequently linearly scaled to represent kinetic parame­
ters within 50% to 300% of their nominal baseline values, resulting in the final transformed output Kr ∈Rnk×no. 
Here, nf, no, nn, and nk correspond to the numbers of input features, observations, hidden-layer neurons, and 
kinetic parameters, respectively.
Table 1  Hyperparameter search spaces for grid search optimization of machine learning regression models
Model
Hyperparameters
Search space
Linear Regression 
(LR)
fit_intercept, positive
fit_intercept: [True, False]; positive: [True, False]
Ridge Regression 
(RR)
alpha, solver, fit_intercept
alpha: logspace(-4, 3, 100); solver: [‘auto’, ‘svd’, ‘cholesky’, ‘lsqr’, ‘sparse_cg’, 
‘sag’, ‘saga’]; fit_intercept: [True, False]
Lasso Regression 
(Lasso)
alpha, max_iter, fit_intercept, 
selection
alpha: concat of four linspace ranges (0.0001–10); max_iter: [10000, 20000, 30000]; 
fit_intercept: [True, False]; selection: [‘cyclic’, ‘random’]
ElasticNet Regres­
sion (EN)
alpha, l1_ratio, max_iter, 
fit_intercept
alpha: concat of four linspace ranges (0.0001–10); l1_ratio: linspace(0, 1, 11); max_
iter: [10000, 20000, 30000]; fit_intercept: [True, False]
Bayesian Ridge 
Regression (BR)
n_iter, alpha_1, alpha_2, 
lambda_1, lambda_2
n_iter: [100, 200, 300, 400, 500]; alpha_1: [1e-6, 1e-5, 1e-4, 1e-3]; alpha_2: [1e-6, 
1e-5, 1e-4, 1e-3]; lambda_1: [1e-6, 1e-5, 1e-4, 1e-3]; lambda_2: [1e-6, 1e-5, 1e-4, 
1e-3]
Support Vector 
Regression (SVR)
C, epsilon, kernel, gamma, degree
C: logspace(-3, 3, 25); epsilon: linspace(0.001, 0.5, 25); kernel: [‘linear’, ‘rbf’, 
‘poly’]; gamma: logspace(-4, 0, 20) — for ‘rbf’ and ‘poly’; degree: [2, 3, 4, 5] — 
only if kernel=’poly’
K-Nearest Neigh­
bors (KNN)
n_neighbors, weights, p, 
algorithm, leaf_size, metric, 
metric_params
n_neighbors: [1–50]; weights: [‘uniform’, ‘distance’]; p: [1, 2, 3]; algorithm: [‘auto’, 
‘ball_tree’, ‘kd_tree’, ‘brute’]; leaf_size: [10, 15, 20, 25, 30, 35, 40, 45, 50]; metric: 
[‘minkowski’, ‘euclidean’, ‘manhattan’, ‘chebyshev’]; metric_params: [None]
Decision Tree (DT)
max_depth, min_samples_split, 
min_samples_leaf, max_features
max_depth: [1–30]; min_samples_split: [2–20]; min_samples_leaf: [1–20]; max_
features: [None, ‘auto’, ‘sqrt’, ‘log2’]
Random Forest 
(RF)
n_estimators, max_depth, min_
samples_split, min_samples_leaf, 
max_features, bootstrap
n_estimators: [50, 100, 150, 200, 250, 300]; max_depth: [None, 5, 10, 15, 20, 25, 
30]; min_samples_split: [2–10]; min_samples_leaf: [1–10]; max_features: [None, 
‘sqrt’, ‘log2’]; bootstrap: [True, False]
Gradient Boosting 
(GB)
n_estimators, learning_rate, 
max_depth, min_samples_split, 
min_samples_leaf, max_features, 
subsample
n_estimators: [50, 100, 150, 200, 250, 300]; learning_rate: [0.01, 0.05, 0.1, 0.2]; 
max_depth: [3–15]; min_samples_split: [2–10]; min_samples_leaf: [1–10]; max_
features: [None, ‘sqrt’, ‘log2’]; subsample: [0.5, 0.7, 0.8, 1.0]
eXtreme Gradi­
ent Boosting 
(XGBoost)
n_estimators, learning_rate, 
max_depth, subsample, col­
sample_bytree, gamma, reg_alpha, 
reg_lambda
n_estimators: [50, 100, 150, 200, 250, 300]; learning_rate: [0.01, 0.05, 0.1, 0.2]; 
max_depth: [3–10]; subsample: [0.5, 0.7, 0.8, 1.0]; colsample_bytree: [0.5, 0.7, 0.8, 
1.0]; gamma: [0, 0.1, 0.2, 0.3]; reg_alpha: [0, 0.01, 0.1, 1]; reg_lambda: [0.5, 1, 1.5, 
2]
Light Gradient 
Boosting Machine 
(LightGBM)
n_estimators, learning_rate, max_
depth, num_leaves, subsample, 
colsample_bytree, reg_alpha, 
reg_lambda
n_estimators: [50, 100, 150, 200, 250, 300]; learning_rate: [0.01, 0.05, 0.1, 0.2]; 
max_depth: [-1, 0, 1, 2, …, 10] (-1 = no limit); num_leaves: [20, 30, 40, …, 150]; 
subsample: [0.5, 0.7, 0.8, 1.0]; colsample_bytree: [0.5, 0.7, 0.8, 1.0]; reg_alpha: [0, 
0.01, 0.1, 1]; reg_lambda: [0.5, 1, 1.5, 2]
Categorical Boost­
ing (CatBoost)
iterations, learning_rate, depth, 
l2_leaf_reg, bagging_temperature, 
border_count
iterations: [50, 100, 150, 200, 250, 300]; learning_rate: [0.01, 0.05, 0.1, 0.2]; depth: 
[3–10]; l2_leaf_reg: [1, 3, 5, 7, 9]; bagging_temperature: [0, 0.5, 1, 2]; border_
count: [32, 64, 128, 254]
Artificial Neural 
Network (ANN)
hidden_layers, neurons_per_layer, 
activation, solver
hidden_layers: [1, 2]; neurons_per_layer: [2–30]; activation: [‘tansig’, ‘logsig’, 
‘purelin’, ‘satlins’]; solver: ‘Levenberg-Marquardt’
1 3
7
Page 7 of 49 
285

---

## Page 8
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
The predicted kinetic parameters for each patient (Kr) were then input into the trained surrogate models to 
estimate ETP values. These ETP predictions were used to classify patients as RVTE-positive (ETP above the 
threshold) or non-RVTE (ETP below the threshold). The ETP threshold was determined by maximizing Youden’s 
J index on the receiver operating characteristic (ROC) curve. In addition to ROC analysis, several standard clas­
sification metrics were calculated to assess model performance, including area under the curve (AUC), accuracy 
(ACC), true positive rate (TPR), true negative rate (TNR), and F1-Score, as defined in Eqs. 4–7, respectively.
Fig. 2  Schematic of the data partitioning, preprocessing, and model optimization pipeline of surrogate models
 
1 3
8285 
Page 8 of 49

---

## Page 9
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
	
ACC =
TP + TN
TP + TN + FP + FN 
(4)
	
TPR =
TP
TP + FN 
(5)
	
TNR =
TN
TN + FP 
(6)
	
F1Score =
2TP
2TP + FP + FN 
(7)
Here, TP is the true positives, TN is the true negatives, FP is the false positives, and FN is the false negatives.
2.4  Optimization
The primary objective is to optimize the neural network’s weights and biases (Eq. 3) such that patients with 
RVTE exhibit higher predicted ETP values, while those without RVTE exhibit lower values. To achieve this, 
the training process aims to maximize the discriminant margin potential (DMP), which quantifies the separation 
between the two patient groups based on their ETP values. This function is formally defined in Eq. 8.
Table 2  Summary of model configuration options explored for hybrid ANN-Surrogate framework optimization
Configuration option
Description
Evaluated settings
Patient input data 
normalization 
scheme
Technique applied to preprocess and 
scale input variables.
- MinMax: Rescales inputs to the interval [− 1, 1].
- Standard: Centers data to zero mean and unit variance (Z-score).
Dimensionality 
reduction strategy
Determines whether all features or a 
reduced set are used as model inputs.
- All Features: Incorporates the complete clinical dataset [39].
- PCA-Based: Utilizes Principal Component Analysis to reduce dimensional­
ity [39].
Model target scope
Defines the extent of kinetic parameters 
that the model is trained to predict.
- Comprehensive: Outputs the complete set of kinetic parameters.
- Selective: Outputs a subset identified as most influential through sensitivity 
analysis [23].
Neural network 
width
Specifies the number of units in the hid­
den layer, impacting model flexibility.
{20, 30, 40, 50}
Initial state 
specification
Approach for Assigning Starting Bio­
chemical Conditions in Simulations.
- Uniform: All subjects begin with the same predefined initial values [35, 36].
- Personalized: Initial conditions are tailored to individual patient data [36].
Optimization 
criterion
Maximize an objective function using 
metaheuristic optimization algorithms.
- Margin-Only: Uses Discriminant Margin Potential (DMP) alone.
- Sparse: Combines DMP with L1 regularization.
- Full Regularization: Combines DMP with both L1 and L2 penalties.
Fig. 3  Hybrid ANN-Surrogate modeling framework for predicting RVTE risk based on patient-specific clinical data and 
coagulation kinetics
 
1 3
9
Page 9 of 49 
285

---

## Page 10
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
	
DMP =


i∈P
Y output,i
 •
nn
max (1, np) −


i∈N
Y output,i

(8)
Here, Y output ∈Rno represent the vector of predicted ETPs for all patients, and Y target ∈{−1, +1}no 
denote the corresponding binary class labels, where + 1 indicates an RVTE-positive patient and − 1 indicates 
a non-RVTE patient. Define the index sets of positive and negative samples as P = {i|Y target,i = +1} and 
N = {i|Y target,i = −1}, respectively, with cardinalities np = |P| and nn = |N|. In Eq. 8, the first term reflects 
the aggregated predicted thrombin potential among RVTE-positive patients, weighted by the ratio of class sizes 
to mitigate class imbalance. The second term represents the corresponding aggregation for non-RVTE patients. 
The objective is to maximize this margin, thereby enhancing the model’s discriminative capability between the 
two clinical outcomes.
To control model complexity and improve generalization, two regularized variants of the objective function 
were also considered. Let W 1 ∈Rnn×nf and W 2 ∈Rnk×nn denote the weight matrices of the hidden and output 
layers, respectively. The three objective functions to be maximized in the pipeline are:
	
FDMP = DMP
(9)
	
FDMP,L1 = DMP −1
no
[∑
(|W 1|) +
∑
(|W 2|)
]

(10)
	
FDMP,L1+L2 = DMP −
1
np + nn
[∑
(|W 1|) +
∑
(|W 2|)
]
−
1
np + nn
[∑
(W 1 ⊙W 1) +
∑
(W 2 ⊙W 2)
]
(11)
Here, ∥·∥1 and ∥·∥2 denote denote the ℓ₁ and ℓ₂ norms, respectively. The ℓ₁ penalty promotes sparsity in network 
weights, while the combined ℓ₁ + ℓ₂ formulation balances sparsity with smoothness and weight shrinkage.
Because the DMP-based objectives are non-differentiable due to the model’s underlying ODE system, gradi­
ent-based optimization is not applicable. Consequently, all objective functions were maximized using population-
based metaheuristic optimization algorithms (MOAs), as detailed in Sect. 2.6.
This study used eight MOAs: Genetic algorithm (GA) [40], particle swarm optimization (PSO) [41], grey wolf 
optimizer (GWO) [42], ant colony optimizer (ACO) [43], firefly algorithm (FA) [44], bat algorithm (BA) [45], 
artificial bee colony (ABC) [46], and whale optimizer algorithm (WOA) [47]. Additional implementation details, 
including pseudocode and hyperparameter configurations for each algorithm, are provided in the SM. In all cases, 
100 individuals and 300 generations were used.
2.5  Metrics for performance evaluation of surrogate models
The substitution of the ODE system with ML-based surrogate models within the hybrid framework was evaluated 
by comparing their outputs against reference values obtained using the original ANN–ODE approach, using the 
same optimized adjustable parameters, which involved numerical integration of the ODEs via the BDF method 
with a time step of 0.0001 min over a 10-minute simulation horizon. To assess the accuracy of the surrogate mod­
els, several performance metrics were computed, as summarized in Table 3. A radar plot was also constructed to 
facilitate the visualization of the performance across ML models and MOAs.
2.6  Improved analysis on the best surrogate model
After identifying the best-performing ML surrogate to replace the ODE system, additional analyses were con­
ducted to better characterize its optimization behavior and robustness across the full framework.
1 3
10
285 
Page 10 of 49

---

## Page 11
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Table 3  Quantitative metrics for assessing accuracy and efficiency of surrogate models within the hybrid ANN–ODE frame­
work
Type
Metric
Mathematical Equation
Notation
Equa­
tion #
Normalized 
per ML
ML-normalized true 
performance (%)
∼
P
ML
i,j
=
Pi,j
max
j
Pi,j
× 100
Pi,j: Performance of ML model with MOAj; 
max across MOAs for fixed ML
(12)
Normalized 
per MOA
MOA-normalized 
true performance (%)
∼
P
MOA
i,j
=
Pi,j
max
i
Pi,j
× 100
Pi,j: Performance of ML model with MOAj; 
max across MLs for fixed MOA
(13)
–
Relative accuracy (%) RAi,j = 100 −

DMP sur
i,j −DMP true
i,j
DMP true
i,j
 × 100 Relative Accuracy (RA) measures the percent­
age agreement between the Discriminant Mar­
gin Potential (DMP) from the surrogate model 
and the full ODE-based model for the -th ML 
model andj-th MOA. Higher values indicate 
closer alignment.
(14)
Normalized 
per MOA
MOA-normalized 
relative accuracy (%)
∼
RA
MOA
i,j
=
RAi,j
max
i
RAi,j
× 100
Normalized across MLs for each MOA
(15)
–
Model time reduction 
(%)
TRi,j =
(
1 −
T sur
i,j
T true
j
)
× 100
T sur
i,j : Computational time with surrogate of 
ML model with MOAj.T true
j
: Computational 
time for full ODE on MOAj
(16)
Normalized 
per MOA
MOA-normalized 
time reduction (%)
∼
TR
MOA
i,j
=
T Ri,j
max
i
T Ri,j
× 100
Normalized across MLs for each MOA
(17)
–
Convergence effi­
ciency (%)
CEi,j =
(
1 −
G90
i,j
Gtotal
i,j
)
× 100
G90
i,j: generation reaching 90% of the best fit­
ness.Gtotal
i,j
: total generations
(18)
–
Relative accuracy 
AUC (%)
RAAUC
i,j
= 100 −

AUCsur
i,j −AUCtrue
i,j
AUCtrue
i,j
 × 100 Measures the percentage agreement between 
the Area Under the Curve (AUC) predicted by 
the surrogate model and the full ODE model for 
the i-th ML model and j-th MOA. Higher values 
indicate closer alignment.
(19)
–
Relative accuracy 
ACC (%)
RAACC
i,j
= 100 −

ACCsur
i,j −ACCtrue
i,j
ACCtrue
i,j
 × 100 Quantifies agreement between surrogate and 
true accuracy (ACC). Values closer to 100% 
reflect better surrogate fidelity
(20)
–
Relative accuracy 
TPR (%)
RAT P R
i,j
= 100 −

T P Rsur
i,j −T P Rtrue
i,j
T P Rtrue
i,j
 × 100 Represents the agreement in true-positive rates 
between the surrogate and full models. Higher 
scores denote better match.
(21)
–
Relative accuracy 
TNR (%)
RAT NR
i,j
= 100 −

T NRsur
i,j −T NRtrue
i,j
T NRtrue
i,j
 × 100 Assesses the agreement in true negative rates 
between surrogate and full ODE predic­
tions. Higher percentages indicate stronger 
concordance.
(22)
–
Relative accuracy 
F1-score (%)
RAF 1
i,j = 100 −

F 1sur
i,j −F 1true
i,j
F 1true
i,j
 × 100
Evaluates the similarity of F1-scores from 
surrogate and true models, with higher values 
reflecting better accuracy.
(23)
Normalized 
per MOA
MOA-normalized RA 
AUC (%)
∼
RA
AUC
i,j
=
RAAUC
i,j
max
i
RAAUC
i,j
× 100
Best AUC-aligned ML model per MOA scores 
100%.
(24)
Normalized 
per MOA
MOA-normalized RA 
ACC (%)
∼
RA
ACC
i,j
=
RAACC
i,j
max
i
RAACC
i,j
× 100
Normalized accuracy agreement.
(25)
Normalized 
per MOA
MOA-normalized RA 
TPR (%)
∼
RA
T P R
i,j
=
RAT P R
i,j
max
i
RAT P R
i,j
× 100
Normalized TPR agreement.
(26)
Normalized 
per MOA
MOA-normalized RA 
TNR (%)
∼
RA
T NR
i,j
=
RAT NR
i,j
max
i
RAT NR
i,j
× 100
Normalized TNR agreement.
(27)
Normalized 
per MOA
MOA-normalized RA 
F1-score (%)
∼
RA
F 1
i,j =
RAF 1
i,j
max
i
RAF 1
i,j
× 100
Normalized F1-score agreement.
(28)
1 3
11
Page 11 of 49 
285

---

## Page 12
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
2.6.1  Comparison with gradient-based optimizer algorithms
Once a differentiable surrogate replaced the ODE system, the optimization pipeline became end-to-end differ­
entiable. Therefore, in addition to the previously employed metaheuristic algorithms, three widely used gradi­
ent-based optimizers were implemented as baselines: stochastic gradient descent (SGD) [48], root mean square 
propagation (RMSProp) [49], and adaptive moment estimation (Adam) [50]. All optimizers were tasked with 
maximizing the same fitness function used in the metaheuristic experiments, thereby ensuring a fair comparison.
Adam optimization was implemented with a learning rate of 10− 3, first- and second-moment decay parameters 
1 = 0.9 and 2 = 0.999, and numerical stabilization constant  = 10−8. RMSProp used the same learning rate, a decay 
factor of 0.9 for the running average of squared gradients, and  = 10−8. SGD was implemented with a higher 
learning rate and Xavier initialization to mitigate vanishing gradients in early iterations. In preliminary analyses, 
gradient-based optimizers exhibited substantially lower per-iteration computational cost, with average runtimes 
approximately three times faster than those of MOAs. To ensure a fair comparison under comparable computa­
tional budgets, all gradient-based optimizers were therefore executed for a fixed number of 900 iterations, cor­
responding to three times the iteration count used for MOAs, resulting in similar overall wall-clock optimization 
times across methods.
Gradient-based optimizers were compared with MOAs in terms of convergence speed, optimization stability, 
computational time, and predictive performance.
2.6.2  Improvements in the binary classifier
To quantify the impact of replacing the mechanistic ODE–based objective with a surrogate model on downstream 
RVTE prediction, we conducted a systematic comparative evaluation using the top-performing ML surrogate and 
the original ODE simulator.
To quantify predictive uncertainty, non-parametric bootstrap resampling (10,000 iterations) was applied to both 
training and test sets independently. For each resample, standard classification metrics were computed, including 
the AUC, ACC, TPR, TNR, and F1-score. Final estimates are reported as bootstrap means with 95% confidence 
intervals (CIs) defined by the 2.5th and 97.5th percentiles. Differences in performance between surrogate-driven 
and ODE-driven optimization pipelines were interpreted as a direct measure of surrogate-induced uncertainty 
propagation to the RVTE classification task.
To formally assess differences in discriminative performance across optimization strategies, pairwise com­
parisons between GWO and alternative optimizers were performed using DeLong’s test, which accounts for the 
correlation between models evaluated on the same patient samples. Mean AUC differences (ΔAUC), 95% confi­
dence intervals, and two-sided p-values were reported, with statistical significance defined at α = 0.05.
Model performance was further evaluated using complementary calibration, clinical utility, and threshold anal­
yses. Ground-truth outcomes were defined by the binary variable true. For calibration and decision curve analyses, 
continuous model outputs were min–max normalized to the [0,1] interval to represent predicted RVTE risk. In 
contrast, threshold analyses were conducted exclusively on the original ETP values (nM·min) to preserve clinical 
interpretability.
Calibration was assessed using quantile-based binning with five equally populated bins. For each bin, the mean 
predicted risk was compared with the observed event rate. Uncertainty in calibration estimates was quantified via 
non-parametric bootstrapping (10,000 resamples), and 95% CIs were constructed for observed proportions. The 
45° identity line represented perfect calibration.
Clinical usefulness was evaluated using decision curve analysis (DCA). The net benefit was computed across 
threshold probabilities ranging from 0.05 to 0.60 and compared with default strategies of treating all patients or 
none. This analysis quantified the trade-off between true positives and false positives while explicitly incorporat­
ing the relative harm of unnecessary treatment.
1 3
12
285 
Page 12 of 49

---

## Page 13
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Finally, decision thresholds were explored using Youden’s index (sensitivity + specificity − 1) evaluated over 
a dense grid of candidate ETP thresholds. Rather than selecting the single maximum Youden value, percentile-
based criteria (85th–99th percentiles, model-specific) were applied to favor robust and conservative threshold 
selection. For each model, the lowest ETP threshold achieving the selected percentile was retained, and the cor­
responding sensitivity and specificity were reported.
2.6.3  Impact of pipeline design choices on RVTE prediction performance
To quantify the influence of pipeline configuration choices on RVTE prediction performance, we conducted a 
structured sensitivity analysis focusing on test-set discrimination, measured by the AUC. For each metaheuristic 
optimizer, results from all evaluated configurations were aggregated into a single dataset comprising framework-
level settings, including data normalization strategy, initial condition model, feature selection approach, kinetic 
parameter subset, fitness score definition, and network size (number of hidden neurons).
A multivariable linear model was fitted with test-set AUC as the dependent variable, and all framework settings 
entered simultaneously as predictors. Categorical settings were modeled as factors, while the number of hidden 
neurons was treated as a continuous variable. Statistical significance of each setting was assessed using analysis 
of variance (ANOVA), with a significance threshold of p < 0.05.
To quantify the relative importance of each framework component, effect sizes were estimated using a drop-
one partial R² approach. For each setting, a reduced model excluding that factor was fitted, and partial R² was 
computed as the proportion of variance explained by the omitted factor relative to the unexplained variance. This 
metric reflects the contribution of each pipeline component to predictive performance independently of other 
settings.
For statistically significant factors, the direction and magnitude of their impact were further characterized 
by computing the mean test-set AUC across all levels of the setting. The best-performing configuration was 
identified as the level with the highest mean AUC, and performance dispersion was summarized using ΔAUC, 
the difference between the highest and lowest mean AUC across levels. Only statistically significant framework 
components were reported in the final analysis.
2.6.4  Ablations on clinical input features and kinetic parameter subsets
To investigate the relationship between clinical input variables and learned kinetic parameters, Spearman rank 
correlation coefficients () were calculated using pairwise complete observations. This approach allowed for the 
quantification of monotonic associations while minimizing the influence of potential outliers.
Initial associations were estimated across the full patient cohort to establish a global association landscape. 
Statistical uncertainty and significance were assessed using a non-parametric bootstrap framework with 10,000 
iterations. For each iteration, samples of the same size as the original dataset were drawn with replacement. From 
the resulting bootstrap distribution, percentile-based 95% CIs were derived. An association was deemed statisti­
cally significant if its 95% CI did not encompass zero.
To evaluate the impact of clinical outcomes on these associations, a stratified analysis was performed based on 
RVTE status (RVTE − and RVTE+). Correlation coefficients and 95% CIs were estimated independently within 
each stratum using the resampling strategy described above, with bootstrap sampling restricted to individuals 
within the respective subgroup.
Differential correlation analysis was subsequently performed to identify shifts in the association structure 
between groups. The metric Δ was defined as the absolute difference between the subgroup-specific Spearman 
coefficients (RVTE+ − RVTE−). To determine the statistical significance of these differences, 95% CIs for Δ were gen­
erated by independently resampling observations from both subgroups at each bootstrap iteration. A Δ was con­
sidered significant if the resulting interval excluded zero, indicating a statistically robust shift in the relationship 
1 3
13
Page 13 of 49 
285

---

## Page 14
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
between clinical inputs and kinetic parameters. Correlation matrices were visualized using heatmaps, with statis­
tically significant associations indicated by overlaid black-filled circle markers.
2.6.5  Permutation-importance analysis
To quantify the relative contribution and global sensitivity of individual input features to the prediction of kinetic 
parameters, a permutation-importance analysis was conducted. This analysis was specifically applied to the top-
performing surrogate-MOA models identified in the previous evaluation stages.
The permutation procedure involved independently shuffling each input feature within each sample while 
keeping all other variables at their baseline values. This process disrupts the specific association between a given 
feature and the output without altering its marginal distribution. For each feature, 500 independent permutations 
were performed to ensure statistical stability. Following each shuffling event, the ANN forward pass was recom­
puted, and the predicted kinetic parameters were compared against the original baseline predictions. Feature 
impact was quantified as the mean absolute deviation (MAD) between the permuted and baseline kinetic param­
eters, averaged across the entire dataset.
To facilitate comparison across kinetic parameters with varying absolute scales, importance values were nor­
malized within each parameter. This was achieved by dividing each importance score by the maximum importance 
value observed across all input features for that specific parameter. The resulting normalized permutation-impor­
tance matrix represents the relative influence of each clinical input on the prediction of each kinetic parameter, 
where a value of 1.0 denotes the most influential feature. Finally, the importance landscape was visualized using 
heatmaps to identify global sensitivities and parameter-specific dependencies within the learned surrogate models.
2.6.6  Performance variability across independent runs
To account for the stochastic variability inherent to the framework, each algorithm was executed over 30 inde­
pendent optimization runs using the best-performing configuration identified during the preliminary screening 
phase. Across runs, all algorithmic settings were held constant, including population size, stopping criterion, fit­
ness function, surrogate model, and data preprocessing pipeline. Runs differed only in their random initialization, 
implemented via distinct random seeds.
For each run, we recorded (i) the final DMP value, (ii) convergence efficiency, and (iii) classification perfor­
mance. Convergence efficiency was defined as 100% minus the percentage of generations required to reach 90% 
of the final fitness attained in that run, providing a normalized measure of optimization speed independent of 
absolute fitness scale. Predictive performance was evaluated using bootstrap-resampled AUC, computed sepa­
rately on training and test sets using 10,000 nonparametric bootstrap iterations.
To summarize robustness and stability across runs, worst-case, mean, best-case, and standard deviation sta­
tistics were computed for each metric and each algorithm. To formally assess statistically significant differences 
among optimization algorithms across repeated runs, nonparametric rank-based statistical tests were employed, 
as described below. This multiple-run evaluation framework enabled a comprehensive assessment of optimiza­
tion consistency, convergence behavior, and generalization performance under stochastic variability.
To compare the performance of the optimization algorithms across multiple independent runs, the Friedman 
test was employed [51, 52]. This nonparametric statistical test is widely used in algorithm benchmarking and is 
particularly well suited for repeated-measures designs, in which the same set of algorithms is evaluated across 
identical and independent runs, problems, or datasets [53–55]. Based on the DMP values, algorithms were ranked 
within each independent run, with higher-performing algorithms assigned better ranks. The Friedman test was 
then used to determine whether statistically significant differences existed among the algorithms’ average ranks 
across runs.
When the Friedman test indicated a significant overall effect, pairwise post-hoc comparisons were conducted 
using the Nemenyi test. The Nemenyi procedure evaluates all pairwise differences in average ranks while 
1 3
14
285 
Page 14 of 49

---

## Page 15
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
controlling the family-wise error rate, making it appropriate for multiple-algorithm comparisons under a com­
mon experimental protocol. Two-sided p-values were reported, with statistical significance defined at α = 0.05.
3  Results
3.1  Comparative performance benchmarking of machine learning surrogates
The Sobol sequence generated 100,000 parameter sets, which were simulated using the ODE–based coagulation 
model to compute ETP, expressed in nM·min. The resulting ETP distribution had a mean of 768.7 nM·min (95% 
CI: 766.8–770.6), a median of 673.6 nM·min, and an interquartile range of 411.9 nM·min (Q1: 525.7 nM·min, 
Q3: 937.6 nM·min). The minimum and maximum observed values were 394.0 nM·min and 2212.1 nM·min, 
respectively. The literature describes ETP values covering a wide physiological spectrum, generally ranging from 
554 to 1952 nM·min, depending on demographic and clinical factors such as age and comorbidities [56–60]. The 
ETP values generated by our simulations fall within and extend this reported range, consistent with the physi­
ological range reported in the literature.
Table 4 summarizes the performance of the evaluated regression models on both the training and testing sets. 
LR, RR, Lasso, EN, and BR exhibited similar performance, with RMSE around 110 on both datasets, indicating 
moderate predictive accuracy without overfitting. SVR achieved slightly lower performance (RMSE ≈ 114). KNN 
severely overfitted the training set and performed poorly on the test set. Tree-based ensemble methods (DT, RF, 
GB, XGBoost, LightGBM, CatBoost) and the ANN achieved very high predictive accuracy, with R2 > 0.998 
and very low RMSE values, maintaining excellent generalization to the test data. Among them, ANN attained 
the highest performance, with R2 = 0.999 and RMSE < 0.3 on both sets. The top-performing ANN has a structure 
with two hidden layers, tansig-logsig-purelin activation functions, and 41-7-10-1 neurons.
To further characterize surrogate model behavior beyond global goodness-of-fit metrics, residual-based analy­
ses and formal statistical tests were conducted under two complementary evaluation settings: (i) an independent 
held-out test set spanning the full Sobol-sampled parameter space (50–300% of nominal kinetic values), and (ii) 
a constrained Sobol-sampled parameter set covering 95–105% of the nominal kinetic values, representing a clini­
cally plausible local neighborhood around the baseline coagulation cascade model.
For each surrogate, predictive accuracy was quantified using the RMSE and mean absolute error (MAE). Sys­
tematic prediction bias was assessed using the mean residual (mean error). Statistical evidence of bias was evalu­
ated exclusively using non-parametric methods: a sign test, which assesses whether residuals are symmetrically 
Model
R² (Train)
R² (Test)
RMSE (Train)
RMSE (Test)
Linear
0.873
0.872
109.549
110.278
Ridge
0.873
0.872
109.549
110.278
Lasso
0.873
0.872
109.558
110.243
ElasticNet
0.873
0.872
109.553
110.255
Bayesian Ridge
0.873
0.872
109.549
110.278
Support Vector Regression
0.864
0.863
113.135
113.984
K Nearest Neighbors
0.999
0.615
0.001
190.798
Decision Tree
0.999
0.998
6.989
12.180
Random Forest
0.999
0.999
3.104
6.144
Gradient Boosting
0.999
0.999
0.939
3.373
XGBoost
0.999
0.999
2.831
3.701
LightGBM
0.999
0.999
2.831
4.175
CatBoost
0.999
0.999
3.088
3.439
ANN
0.999
0.999
0.286
0.264
Table 4  Performance 
metrics of machine learning 
regression models on train­
ing and testing sets
The best-performing model is 
highlighted in bold
 
1 3
15
Page 15 of 49 
285

---

## Page 16
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
distributed around zero, and the Wilcoxon signed-rank test, which additionally accounts for the magnitude of 
deviations while remaining robust to non-normal residual distributions.
Parity plots, residuals versus predicted values, and residual spread distributions are shown in Figs. 4 and 5 for 
the test and constrained sets, respectively. On the full test set (50–300%), DT and RF models exhibited the largest 
residual dispersion (DT MAE = 7.41; RF MAE = 3.52), with clear heteroscedasticity characterized by increasing 
Fig. 4  Residual diagnostics 
of surrogate models on the 
independent test set sampled 
over the full Sobol parameter 
space (50–300% of nominal 
kinetic values)
 
1 3
16
285 
Page 16 of 49

---

## Page 17
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Fig. 5  Residual diagnostics of 
surrogate models evaluated on 
a constrained physiological 
parameter domain (95–105% of 
nominal kinetic values)
 
1 3
17
Page 17 of 49 
285

---

## Page 18
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
residual variance at higher ETP values. Similar heteroscedastic patterns were observed for Gradient Boosting, 
XGBoost, LightGBM, and CatBoost, although these ensemble boosting methods substantially reduced error 
magnitude compared with single-tree and bagging approaches.
Among all evaluated surrogates, the ANN demonstrated superior performance, achieving the lowest residual 
errors (RMSE = 0.264, MAE = 0.184) and exhibiting homoscedastic residuals across the full ETP range. Impor­
tantly, no statistically significant systematic bias was detected in the ANN on the test set (sign test, p = 0.885; 
Wilcoxon, p = 0.133), indicating symmetric residuals centered on zero.
These findings were further reinforced in the constrained physiological parameter set (95–105%), where per­
formance differences became more pronounced. The ANN again outperformed all alternatives (RMSE = 0.116, 
Table 5  Comparative analysis of surrogate-based optimization versus true ODE simulation using the decision tree model
MOA
Optimal DMP 
(Surrogate)
True DMP (Full 
ODE)
Relative Accuracy
Surrogate average Simu­
lation Time (min)
Time Reduction 
(%)
Conver­
gence 
effi­
ciency
GA
145,873.39
129,043.06
86.96
5.59
99.41
53.00
PSO
225,716.37
209,133.48
92.07
5.58
99.70
65.00
GWO
228,392.24
250,110.55
91.32
5.51
99.41
45.00
ACO
80,218.55
78,394.15
97.67
5.80
99.39
78.00
FA
102,416.23
98,649.79
96.18
5.94
99.38
72.33
BA
199,976.94
210,642.69
94.94
5.80
99.39
68.67
ABC
164,248.32
181,892.29
90.30
12.40
99.35
67.00
WOA
102,416.23
58,021.55
23.46
5.28
99.45
99.33
Table 6  Comparative analysis of surrogate-based optimization versus true ODE simulation using the random forest model
MOA
Optimal DMP 
(Surrogate)
True DMP (Full 
ODE)
Relative Accuracy 
(%)
Surrogate average 
Simulation Time (min)
Time Reduction 
(%)
Conver­
gence 
efficiency 
(%)
GA
123,081.79
102,212.49
79.58
327.78
65.48
58.67
PSO
237,265.31
253,091.02
93.75
323.89
82.64
40.33
GWO
238,781.78
273,844.50
87.20
325.06
65.39
47.02
ACO
86,848.91
86,217.74
99.27
322.65
65.80
31.33
FA
99,506.60
97,973.44
98.44
312.43
67.37
65.67
BA
198,671.81
213,758.18
92.94
316.02
66.52
37.67
ABC
156,879.52
162,294.17
96.66
640.82
66.24
55.33
WOA
87,780.41
75,764.70
85.91
320.60
66.85
92.67
Table 7  Comparative analysis of surrogate-based optimization versus true ODE simulation using the gradient boosting 
model
MOA
Optimal DMP 
(Surrogate)
True DMP (Full 
ODE)
Relative Accuracy 
(%)
Surrogate average Simu­
lation Time (min)
Time Reduction 
(%)
Conver­
gence 
efficiency 
(%)
GA
140,828.43
142,155.66
99.07
8.87
99.07
49.00
PSO
255,059.75
275,770.43
92.49
8.65
99.54
49.67
GWO
248,256.99
266,827.88
93.04
8.97
99.04
37.00
ACO
78,896.91
80,462.11
98.05
8.54
99.10
99.67
FA
97,303.50
96,633.60
99.31
8.42
99.12
78.00
BA
203,277.77
211,079.46
96.30
8.33
99.12
53.33
ABC
159,359.54
160,944.92
99.01
16.41
99.14
66.67
WOA
85,749.06
73,810.01
83.82
8.19
99.15
99.67
1 3
18
285 
Page 18 of 49

---

## Page 19
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
MAE = 0.094), whereas the second-best model (LightGBM) showed substantially higher errors (RMSE = 5.25, 
MAE = 4.28). Residual spread plots in this local neighborhood demonstrate the markedly tighter error distribution 
of the ANN compared with that of tree-based ensembles.
Although boosting-based models such as LightGBM and CatBoost may be considered worse than ANN, their 
residual biases remained small in absolute terms. For example, mean absolute bias values for LightGBM (≈ 2.63) 
and CatBoost (≈ 2.29) correspond to approximately 0.34% of the mean true ETP value, suggesting limited practi­
cal impact.
The residual analyses and non-parametric bias tests consistently indicate that the ANN provides the most accu­
rate and unbiased surrogate across both the global synthetic parameter space and the clinically constrained physi­
ological domain, supporting its suitability for patient-specific coagulation modeling. Boosting models, although 
Table 8  Comparative analysis of surrogate-based optimization versus true ODE simulation using the XGBoost model
MOA
Optimal DMP 
(Surrogate)
True DMP (Full 
ODE)
Relative Accuracy 
(%)
Surrogate average Simu­
lation Time (min)
Time Reduction 
(%)
Conver­
gence 
efficiency 
(%)
GA
132,163.82
120,584.88
90.40
9.97
98.95
75.67
PSO
248,642.43
260,831.49
95.33
10.00
99.46
55.33
GWO
240,565.51
265,926.60
90.46
9.79
98.96
36.67
ACO
79,890.59
71,443.70
88.18
10.20
98.92
99.67
FA
99,276.32
94,890.80
95.38
10.18
98.94
28.00
BA
200,343.25
199,987.94
99.82
10.07
98.93
16.67
ABC
164,303.78
179,937.42
91.31
19.83
98.96
48.00
WOA
87,843.61
78,593.91
88.23
10.13
98.95
99.67
Table 9  Comparative analysis of surrogate-based optimization versus true ODE simulation using the lightGBM model
MOA
Optimal DMP 
(Surrogate)
True DMP (Full 
ODE)
Relative Accuracy 
(%)
Surrogate average Simu­
lation Time (min)
Time Reduction 
(%)
Conver­
gence 
efficiency 
(%)
GA
136,669.38
130,454.01
95.24
7.88
99.17
64.67
PSO
258,027.76
258,823.10
99.69
7.79
99.58
40.33
GWO
260,583.74
278,388.31
93.60
8.38
99.11
31.67
ACO
80,949.25
80,056.92
98.89
7.02
99.26
99.33
FA
100,117.57
101,118.28
99.01
7.10
99.26
65.00
BA
202,503.21
210,327.42
96.28
6.39
99.32
49.00
ABC
176,629.61
187,564.46
94.17
13.69
99.28
18.33
WOA
85,308.19
69,134.20
76.58
6.57
99.32
99.33
Table 10  Comparative analysis of surrogate-based optimization versus true ODE simulation using the CatBoost model
MOA
Optimal DMP 
(Surrogate)
True DMP (Full 
ODE)
Relative Accuracy 
(%)
Surrogate average Simu­
lation Time (min)
Time Reduction 
(%)
Conver­
gence 
efficiency 
(%)
GA
165,160.00
160,875.62
97.41
6.31
99.34
67.33
PSO
243,024.01
250,098.07
97.09
6.04
99.68
39.00
GWO
264,267.71
276,729.70
95.29
6.55
99.30
36.33
ACO
80,567.76
80,462.11
99.87
5.91
99.37
99.67
FA
96,713.00
90,084.13
93.15
6.35
99.34
66.00
BA
209,966.45
207,170.14
98.67
6.52
99.31
33.67
ABC
169,621.07
180,415.22
93.64
12.65
99.33
71.33
WOA
78,512.16
53,243.13
67.84
6.02
99.38
99.33
1 3
19
Page 19 of 49 
285

---

## Page 20
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
presenting limitations, remain viable due to their low bias magnitude and were also considered in the following 
analyses.
Tables 5, 6, 7, 8, 9, 10 and 11 present the comparative performance of surrogate-based optimization using 
different ML models against the true ODE simulations across multiple MOAs. Across all surrogates, the simula­
tion time was drastically reduced, with time savings exceeding 98% in most cases and reaching over 99% for 
DT, GB, LightGBM, CatBoost, and ANN models. Relative accuracy varied across models and MOAs, with the 
highest values (> 99%) observed for ACO and FA across several surrogates, while WOA consistently exhibited 
lower accuracy (as low as 23.46% for the DT model). The RF model, despite maintaining competitive accu­
racy, incurred substantially higher average simulation times (> 300 min) than other surrogates, due to the greater 
complexity and size of the model (many trees). Among the MOAs analyzed, GWO and PSO achieved the high­
est DMP values in both surrogate and true ODE predictions, consistently across ML models. The ANN–GWO 
combination attained the highest objective function value during hybrid model optimization. Although ACO and 
WOA demonstrated high convergence efficiency, their low DMP values suggest that these MOAs were unable to 
Table 11  Comparative analysis of surrogate-based optimization versus true ODE simulation using the ANN model
MOA
Optimal DMP 
(Surrogate)
True DMP (Full 
ODE)
Relative Accuracy 
(%)
Surrogate average Simu­
lation Time (min)
Time Reduction 
(%)
Conver­
gence 
efficiency 
(%)
GA
138,085.53
116,416.98
84.32
8.35
99.12
72.67
PSO
275,547.26
254,905.28
92.51
8.32
99.55
57.00
GWO
291,759.95
285,828.28
97.97
8.31
99.12
28.33
ACO
82,271.26
71,443.70
86.85
8.10
99.14
99.67
FA
99,395.68
97,140.56
97.73
8.30
99.13
50.67
BA
209,004.03
188,181.20
90.06
8.00
99.15
73.33
ABC
206,077.54
206,147.72
99.97
16.02
99.16
37.33
WOA
79,058.68
53,243.13
67.30
8.24
99.15
99.33
Fig. 6  Performance evaluation of surrogate models across multiple metaheuristic optimization algorithms and machine 
learning techniques
 
1 3
20
285 
Page 20 of 49

---

## Page 21
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
ML
MOA
Settings*
AUC Train
ACC Train
TPR Train
TNR Train
F1score Train
AUC Test
ACC Test
TPR Test
TNR Test
F1Score Test
DT
GA
S-U-40-A-S-M
0.80658
0.83030
0.82353
0.83206
0.66667
0.59091
0.68571
0.73333
0.67273
0.50000
DT
PSO
S-U-30-P-S-M
0.92782
0.92121
0.94118
0.91603
0.83117
0.82182
0.87143
0.93333
0.85455
0.75676
DT
GWO
S-U-30-P-C-M
0.85631
0.84242
0.91176
0.82443
0.70455
0.84788
0.87143
0.93333
0.85455
0.75676
DT
ACO
S-U-50-A-S-M
0.53065
0.63030
0.73529
0.60305
0.45045
0.49697
0.60000
0.73333
0.56364
0.44000
DT
FA
S-U-50-A-S-S
0.68321
0.67273
0.70588
0.66412
0.47059
0.71515
0.65714
0.86667
0.60000
0.52000
DT
BA
S-U-30-A-C-F
0.84677
0.81818
0.88235
0.80153
0.66667
0.88303
0.77143
1.00000
0.70909
0.65217
DT
ABC
N-U-50-P-C-F
0.74405
0.83636
0.73529
0.86260
0.64935
0.72485
0.80000
0.66667
0.83636
0.58824
DT
WOA
S-U-50-A-S-S
0.68321
0.67273
0.70588
0.66412
0.47059
0.71515
0.65714
0.86667
0.60000
0.52000
RF
GA
S-U-30-A-S-M
0.74181
0.71515
0.82353
0.68702
0.54369
0.73515
0.68571
0.80000
0.65455
0.52174
RF
PSO
S-U-40-P-C-M
0.90952
0.93333
0.88235
0.94656
0.84507
0.90667
0.88571
0.86667
0.89091
0.76471
RF
GWO
S-U-40-A-C-S
0.92075
0.93939
0.88235
0.95420
0.85714
0.88242
0.84286
0.93333
0.81818
0.71795
RF
ACO
S-U-50-A-C-M
0.68949
0.66667
0.70588
0.65649
0.46602
0.65939
0.68571
0.66667
0.69091
0.47619
RF
FA
S-U-50-P-S-S
0.69275
0.63030
0.82353
0.58015
0.47863
0.76485
0.61429
0.80000
0.56364
0.47059
RF
BA
S-U-20-A-C-S
0.90144
0.86667
0.88235
0.86260
0.73171
0.79879
0.85714
0.80000
0.87273
0.70588
RF
ABC
M-U-50-P-S-F
0.79625
0.82424
0.82353
0.82443
0.65882
0.68727
0.82857
0.66667
0.87273
0.62500
RF
WOA
M-U-50-A-S-M
0.65043
0.67273
0.64706
0.67939
0.44485
0.72848
0.71429
0.80000
0.69091
0.54545
GB
GA
S-U-40-A-C-S
0.79838
0.76364
0.79412
0.75573
0.58065
0.68364
0.62857
0.73333
0.60000
0.45833
GB
PSO
S-U-50-P-C-M
0.95195
0.93333
0.97059
0.92366
0.85714
0.86788
0.85714
0.86667
0.85455
0.72222
GB
GWO
S-U-30-A-C-M
0.93444
0.89697
0.91176
0.89313
0.78481
0.90182
0.85714
0.93333
0.83636
0.73684
GB
ACO
S-U-30-P-C-F
0.66637
0.63636
0.73529
0.61069
0.45455
0.65455
0.61429
0.53333
0.63636
0.30476
GB
FA
S-U-50-A-S-F
0.71778
0.66061
0.82353
0.61832
0.50000
0.63636
0.55714
0.73333
0.50909
0.41509
GB
BA
S-U-20-P-C-F
0.90031
0.86061
0.94118
0.83969
0.73563
0.72000
0.72857
0.80000
0.70909
0.55814
GB
ABC
S-U-50-P-S-F
0.79255
0.71515
0.91176
0.66412
0.56881
0.80121
0.70000
1.00000
0.61818
0.58824
GB
WOA
S-U-40-P-C-F
0.74405
0.64242
0.82353
0.59542
0.48696
0.62424
0.57143
0.66667
0.54545
0.38095
XGBoost
GA
S-U-40-A-S-F
0.72149
0.79394
0.73529
0.80916
0.59524
0.81576
0.74286
0.86667
0.70909
0.59091
XGBoost
PSO
S-U-20-P-C-M
0.93309
0.93939
0.91176
0.94656
0.86111
0.91636
0.88571
0.80000
0.90909
0.75000
XGBoost
GWO
S-U-50-A-C-M
0.93714
0.92727
0.91176
0.93130
0.83784
0.92364
0.88571
0.93333
0.87273
0.77778
XGBoost
ACO
S-U-30-A-S-M
0.70914
0.73333
0.70588
0.74046
0.52174
0.64970
0.64286
0.66667
0.63636
0.44444
XGBoost
FA
S-U-30-P-S-F
0.69533
0.66061
0.76471
0.63359
0.48148
0.63333
0.60000
0.66667
0.58182
0.40404
XGBoost
BA
M-U-30-A-C-M
0.86013
0.84242
0.88235
0.83206
0.69767
0.86061
0.81429
0.93333
0.78182
0.68293
XGBoost
ABC
S-U-30-P-C-F
0.86080
0.83030
0.79412
0.83969
0.65854
0.73697
0.85714
0.53333
0.94545
0.61538
XGBoost
WOA
S-U-50-P-S-S
0.65413
0.69091
0.70588
0.68702
0.48485
0.70970
0.61429
0.66667
0.60000
0.41667
LightGBM
GA
S-U-40-A-C-M
0.80108
0.79394
0.76471
0.80153
0.60465
0.74182
0.65714
0.66667
0.65455
0.45455
LightGBM
PSO
S-U-40-A-C-M
0.95442
0.93333
0.94118
0.93130
0.85333
0.91515
0.87143
0.86667
0.87273
0.74286
LightGBM
GWO
S-U-40-A-C-S
0.91311
0.91515
0.91176
0.91603
0.81579
0.92485
0.87143
0.93333
0.85455
0.75676
LightGBM
ACO
S-U-40-P-S-S
0.68040
0.74545
0.61765
0.77863
0.50000
0.49576
0.58571
0.33333
0.65455
0.13889
LightGBM
FA
S-U-40-A-S-M
0.72654
0.66667
0.79412
0.63359
0.49541
0.60182
0.55714
0.73333
0.50909
0.41509
LightGBM
BA
S-U-40-A-C-F
0.89313
0.87273
0.88235
0.87023
0.74074
0.80606
0.80000
0.93333
0.76364
0.66667
LightGBM
ABC
N-U-40-P-C-F
0.83330
0.84848
0.76471
0.87023
0.67532
0.78000
0.80000
0.80000
0.80000
0.63158
LightGBM
WOA
S-U-30-P-S-F
0.69241
0.69091
0.76471
0.67176
0.50485
0.60000
0.55714
0.46667
0.58182
0.21778
Table 12  Binary classification performance of the ANN-Surrogate framework across ML algorithms and optimization methods
1 3
21
Page 21 of 49 
285

---

## Page 22
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
ML
MOA
Settings*
AUC Train
ACC Train
TPR Train
TNR Train
F1score Train
AUC Test
ACC Test
TPR Test
TNR Test
F1Score Test
CatBoost
GA
S-U-40-A-C-S
0.82196
0.86667
0.70588
0.90840
0.68571
0.73091
0.81429
0.60000
0.87273
0.58065
CatBoost
PSO
S-U-30-P-C-M
0.91154
0.85455
0.97059
0.82443
0.73333
0.90061
0.84286
0.93333
0.81818
0.71795
CatBoost
GWO
S-U-40-P-C-M
0.92187
0.89091
0.97059
0.87023
0.78571
0.97091
0.91429
1.00000
0.89091
0.83333
CatBoost
ACO
S-U-30-P-C-F
0.68006
0.63636
0.73529
0.61069
0.45455
0.67030
0.65714
0.66667
0.65455
0.45455
CatBoost
FA
S-U-40-P-S-M
0.71082
0.67879
0.73529
0.66412
0.48544
0.62970
0.57143
0.73333
0.52727
0.42308
CatBoost
BA
S-U-20-A-C-F
0.82914
0.88485
0.76471
0.91603
0.73239
0.88485
0.87143
0.80000
0.89091
0.72727
CatBoost
ABC
S-U-20-P-C-F
0.87057
0.76364
0.94118
0.71756
0.62136
0.81212
0.71429
0.86667
0.67273
0.56522
CatBoost
WOA
N-U-20-A-S-F
0.65963
0.73333
0.61765
0.76336
0.48837
0.72364
0.68571
0.66667
0.69091
0.47619
ANN
GA
S-U-40-P-S-M
0.78682
0.72121
0.94118
0.66412
0.58182
0.76727
0.62857
0.80000
0.58182
0.48000
ANN
PSO
S-U-20-P-C-M
0.87315
0.92121
0.88235
0.93130
0.82192
0.93939
0.88571
0.93333
0.87273
0.77778
ANN
GWO
S-U-40-P-C-M
0.96677
0.94545
0.94118
0.94656
0.87671
0.91636
0.90000
0.93333
0.89091
0.80000
ANN
ACO
S-U-30-A-S-M
0.69903
0.70303
0.73529
0.69466
0.50505
0.67152
0.61429
0.66667
0.60000
0.41667
ANN
FA
S-U-20-P-C-F
0.67041
0.71515
0.70588
0.71756
0.50526
0.85212
0.74286
0.73333
0.74545
0.55000
ANN
BA
S-U-20-A-C-F
0.89672
0.87879
0.82353
0.89313
0.73684
0.84970
0.82857
0.86667
0.81818
0.68421
ANN
ABC
N-U-40-P-C-F
0.84564
0.78788
0.88235
0.76336
0.63158
0.82303
0.71429
0.86667
0.67273
0.56522
ANN
WOA
N-U-20-A-S-F
0.65065
0.73333
0.61765
0.76336
0.48837
0.69576
0.68571
0.66667
0.69091
0.47619
*Model specifications (see Table 2) are abbreviated in the format α - β - γ - δ - ε – ζ, where: α represents the patient input data normalization scheme (“S” = standard; “M” = MinMax). β 
represents the initial state specification (“P” = personalized; “U” = uniform). γ represents the neural network width (20, 30, 40, or 50 neurons in the hidden layer). δ represents the dimen­
sionality reduction strategy (“A” = all features; “P” = PCA-based variables). ε represents the model target scope (“S” = selective, use a subset identified as most influential through sensitivity 
analysis; “C” = comprehensive, use the complete set of kinetic parameters). ζ represents optimization criterion (“M” = margin-only, use only DMP; “S” = Sparse, combines DMP with L1 
regularization; “F” = Full regularization, combines DMP with both L1 and L2 penalties)
Table 12  (continued)
 
1 3
22
285 
Page 22 of 49

---

## Page 23
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
improve the model, indicating limited optimization capability under these conditions. In contrast, PSO and GWO 
exhibited moderate convergence efficiency but achieved higher DMP values, indicating a more effective balance 
between exploitation and exploration.
Figure 6 graphically illustrates the performance differences among the ML–MOA combinations. PSO and 
GWO outperformed all other optimizers across the seven top ML models. BA and ABC achieved intermediate 
results, while GA, ACO, FA, and WOA showed comparatively lower performance. Among all configurations, 
ANN–GWO achieved the highest DMP value, closely followed by ANN–PSO, reinforcing the strong compat­
ibility between these optimizers and the ANN architecture.
The comparative analysis of Tables 12 and 13 highlights evident performance disparities among the evaluated 
MOAs. Across both the surrogate and true ANN–ODE frameworks, ACO and WOA frequently ranked among the 
lowest-performing optimizers, with lower AUC, ACC, and F1-score values across most ML algorithms, indicat­
ing limited capacity to effectively fine-tune model parameters. In contrast, GWO and PSO demonstrated remark­
able efficiency on the test set, achieving superior predictive accuracy and robustness, particularly when coupled 
with boosting-based ML models (GB, XGBoost, LightGBM, and CatBoost) and ANN. These combinations not 
only yielded the highest AUC values, frequently exceeding 0.90, but also maintained balanced sensitivity and 
specificity, reflecting strong generalization and stability. Notably, the ANN models optimized by GWO achieved 
peak test performance, indicating strong compatibility between GWO optimization and the ANN architecture.
Regarding model configurations, Most top-ranked configurations employed standardized (Z-score) inputs, with 
most top-ranked models using Zhu’s [35] baseline blood concentrations. The network widths varied across ML–
MOA combinations, indicating no consistent preference for a specific hidden-layer size. Notably, the ANN-based 
hybrids with GWO and PSO achieved superior predictive performance when paired with PCA-based dimension­
ality reduction and patient-specific kinetic parameter calibration, with optimization restricted to the DMP-only 
objective. Configurations optimized using the DMP-only objective frequently demonstrated higher test perfor­
mance than sparsity- or fully regularized schemes. Across other ML families (DT, RF, GB, XGBoost, LightGBM, 
and CatBoost), no single configuration dominated. However, models employing PCA-reduced features and com­
prehensive adjustments to kinetic parameters tended to outperform those trained on all raw variables. In particu­
lar, PSO- and GWO-driven surrogates repeatedly ranked among the highest in AUC and ACC, suggesting that 
swarm-based search strategies were more effective in navigating adjustable parameter space. Conversely, ACO, 
FA, and WOA configurations showed weaker stability across both ML and ANN surrogates, with performance 
sensitive to feature selection and regularization strategy. Overall, these results highlight the importance of both 
dimensionality reduction and objective function design in tailoring surrogate model efficiency, with ANN-PSO 
and ANN-GWO emerging as the most robust patient-specific predictors.
To evaluate the discriminatory performance of different MOA-ML models in separating patients with RVTE 
from those without RVTE, we computed the mean ETP for each clinical group. For each model, the separation 
between RVTE and non-RVTE patients was defined as the difference between the mean ETP of the two groups. 
The reference model, ANN-GWO, was compared to each alternative MOA-ML model by calculating the dif­
ference in separation (ANN-GWO minus the comparative model). Statistical significance and uncertainty were 
assessed using a bootstrap-based one-sided Wilcoxon signed-rank approach. Specifically, RVTE and non-RVTE 
ETP values from the reference model were resampled with replacement 10,000 times to generate a distribution 
of bootstrap separation estimates. For each bootstrap sample, the difference between the reference separation 
and the comparative model’s separation was calculated, yielding a bootstrap distribution of differences. The one-
sided p-value was computed as the proportion of bootstrap differences less than or equal to zero, reflecting the 
probability that the reference model is not superior. The 95% CI for the median difference was estimated as the 
2.5th and 97.5th percentiles of the bootstrap distribution. Positive median differences indicate superior discrimi­
nation by ANN-GWO, and statistical significance was defined as p < 0.05. This nonparametric bootstrap approach 
allows robust inference without assuming normality and provides a reliable assessment of differences in model 
performance.
1 3
23
Page 23 of 49 
285

---

## Page 24
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
ML
MOA
AUC 
Train
ACC 
Train
TPR 
Train
TNR 
Train
F1score 
Train
AUC Test ACC Test TPR Test
TNR Test
F1Score 
Test
DT
GA
0.79277
0.83030
0.82353
0.83206
0.66667
0.65091
0.68571
0.73333
0.67273
0.50000
DT
PSO
0.91693
0.92121
0.94118
0.91603
0.83117
0.86788
0.87143
0.93333
0.85455
0.75676
DT
GWO
0.82645
0.84242
0.91176
0.82443
0.70455
0.88848
0.87143
0.93333
0.85455
0.75676
DT
ACO
0.65739
0.59394
0.82353
0.53435
0.45528
0.62909
0.51429
0.80000
0.43636
0.41379
DT
FA
0.68321
0.67273
0.70588
0.66412
0.47059
0.69576
0.65714
0.86667
0.60000
0.52000
DT
BA
0.86439
0.85455
0.82353
0.86260
0.70000
0.87394
0.78571
0.93333
0.74545
0.65116
DT
ABC
0.77930
0.83636
0.73529
0.86260
0.64935
0.78667
0.80000
0.66667
0.83636
0.58824
DT
WOA
0.70117
0.73333
0.67647
0.74809
0.51111
0.45576
0.57143
0.40000
0.61818
0.17778
RF
GA
0.73664
0.71515
0.82353
0.68702
0.54369
0.62182
0.68571
0.80000
0.65455
0.52174
RF
PSO
0.89717
0.92121
0.88235
0.93130
0.82192
0.88727
0.87143
0.86667
0.87273
0.74286
RF
GWO
0.93534
0.93939
0.88235
0.95420
0.85714
0.85939
0.82857
0.86667
0.81818
0.68421
RF
ACO
0.69511
0.66061
0.70588
0.64885
0.46154
0.64121
0.67143
0.60000
0.69091
0.41538
RF
FA
0.71599
0.63030
0.82353
0.58015
0.47863
0.69333
0.61429
0.80000
0.56364
0.47059
RF
BA
0.89021
0.87273
0.88235
0.87023
0.74074
0.79152
0.84286
0.73333
0.87273
0.66667
RF
ABC
0.76134
0.81818
0.82353
0.81679
0.65116
0.72364
0.80000
0.66667
0.83636
0.58824
RF
WOA
0.63247
0.67273
0.64706
0.67939
0.44485
0.76121
0.71429
0.80000
0.69091
0.54545
GB
GA
0.79300
0.85455
0.61765
0.91603
0.63636
0.70667
0.71429
0.53333
0.76364
0.40635
GB
PSO
0.94612
0.91515
1.00000
0.89313
0.82927
0.85212
0.85714
0.86667
0.85455
0.72222
GB
GWO
0.90840
0.87879
0.94118
0.86260
0.76190
0.90303
0.81429
0.93333
0.78182
0.68293
GB
ACO
0.67894
0.66061
0.70588
0.64885
0.46154
0.66424
0.62857
0.53333
0.65455
0.31605
GB
FA
0.70566
0.63030
0.82353
0.58015
0.47863
0.67030
0.58571
0.80000
0.52727
0.45283
GB
BA
0.87741
0.84848
0.94118
0.82443
0.71910
0.71758
0.72857
0.80000
0.70909
0.55814
GB
ABC
0.80624
0.72727
0.91176
0.67939
0.57944
0.78909
0.70000
0.80000
0.67273
0.53333
GB
WOA
0.74225
0.64242
0.82353
0.59542
0.48696
0.57333
0.57143
0.66667
0.54545
0.38095
XGBoost
GA
0.72474
0.79394
0.73529
0.80916
0.59524
0.72000
0.74286
0.86667
0.70909
0.59091
XGBoost
PSO
0.91491
0.93333
0.91176
0.93893
0.84932
0.87758
0.87143
0.73333
0.90909
0.70968
XGBoost
GWO
0.91109
0.91515
0.91176
0.91603
0.81579
0.87515
0.85714
0.93333
0.83636
0.73684
XGBoost
ACO
0.74091
0.69697
0.73529
0.68702
0.50000
0.54545
0.58571
0.66667
0.56364
0.39216
XGBoost
FA
0.64212
0.65455
0.79412
0.61832
0.48649
0.58182
0.54286
0.66667
0.50909
0.36036
XGBoost
BA
0.86866
0.82424
0.91176
0.80153
0.68132
0.84242
0.75714
0.93333
0.70909
0.62222
XGBoost
ABC
0.86080
0.78182
0.85294
0.76336
0.61702
0.74182
0.74286
0.73333
0.74545
0.55000
XGBoost
WOA
0.65447
0.69091
0.70588
0.68702
0.48485
0.68727
0.61429
0.66667
0.60000
0.41667
LightGBM
GA
0.80736
0.84848
0.76471
0.87023
0.67532
0.71515
0.72857
0.60000
0.76364
0.48649
LightGBM
PSO
0.93983
0.92121
0.97059
0.90840
0.83544
0.88485
0.85714
0.86667
0.85455
0.72222
LightGBM
GWO
0.90391
0.91515
0.91176
0.91603
0.81579
0.90788
0.87143
0.93333
0.85455
0.75676
LightGBM
ACO
0.66300
0.66061
0.70588
0.64885
0.46154
0.52485
0.57143
0.66667
0.54545
0.38095
LightGBM
FA
0.71711
0.69697
0.76471
0.67939
0.50980
0.63030
0.61429
0.66667
0.60000
0.41667
LightGBM
BA
0.88258
0.81212
0.91176
0.78626
0.66667
0.81091
0.75714
0.93333
0.70909
0.62222
LightGBM
ABC
0.82869
0.83636
0.76471
0.85496
0.65823
0.79152
0.78571
0.73333
0.80000
0.59459
LightGBM
WOA
0.67423
0.65455
0.82353
0.61069
0.49558
0.62545
0.55714
0.66667
0.52727
0.37037
CatBoost
GA
0.82645
0.88485
0.67647
0.93893
0.70769
0.73333
0.77143
0.46667
0.85455
0.43556
CatBoost
PSO
0.87427
0.86061
0.94118
0.83969
0.73563
0.85697
0.82857
0.86667
0.81818
0.68421
CatBoost
GWO
0.92995
0.88485
0.97059
0.86260
0.77647
0.91879
0.88571
1.00000
0.85455
0.78947
CatBoost
ACO
0.67894
0.66061
0.70588
0.64885
0.46154
0.66424
0.62857
0.53333
0.65455
0.31605
CatBoost
FA
0.69578
0.67879
0.73529
0.66412
0.48544
0.56121
0.57143
0.73333
0.52727
0.42308
CatBoost
BA
0.82600
0.83030
0.79412
0.83969
0.65854
0.87394
0.82857
0.80000
0.83636
0.66667
CatBoost
ABC
0.88348
0.75758
0.94118
0.70992
0.61538
0.81091
0.68571
0.86667
0.63636
0.54167
CatBoost
WOA
0.63583
0.73333
0.61765
0.76336
0.48837
0.64727
0.68571
0.66667
0.69091
0.47619
ANN
GA
0.76134
0.72121
0.94118
0.66412
0.58182
0.67879
0.62857
0.80000
0.58182
0.48000
ANN
PSO
0.84890
0.91515
0.88235
0.92366
0.81081
0.92364
0.82857
0.86667
0.81818
0.68421
ANN
GWO
0.93534
0.94545
0.94118
0.94656
0.87671
0.89455
0.90000
0.93333
0.89091
0.80000
ANN
ACO
0.74091
0.69697
0.73529
0.68702
0.50000
0.54545
0.58571
0.66667
0.56364
0.39216
Table 13  Binary classification performance of the true ANN–ODE framework using the adjustable parameters optimized via 
the ANN-Surrogate framework across ML models and MOAs
1 3
24
285 
Page 24 of 49

---

## Page 25
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
As shown in Table 14, ANN-GWO consistently achieved greater mean ETP separation than most competing 
ML–MOA combinations, with statistically significant superiority (p < 0.05) in the majority of pairwise compari­
sons, particularly against GA-, ACO-, FA-, BA-, ABC-, and WOA-based models. In statistically significant com­
parisons, confidence intervals were largely positive, supporting the stability of the observed differences. Overall, 
ANN-GWO demonstrated strong discrimination between RVTE and non-RVTE patients. While ANN-GWO 
attained the highest DMP among surrogate models, its advantage over other ML surrogates with GWO was not 
statistically significant. Nonetheless, pairing GWO with boosting-based surrogates yielded competitive results, 
except for RF. RF-based surrogates, although competitive in discrimination, were previously shown to offer only 
a limited computational advantage over ANN and boosting models. The similar performance trends observed for 
GWO and PSO suggest that both MOAs are highly effective optimizers within this hybrid framework.
Figure 7 shows the ROC curves for the test set, where predictions were generated using the ANN in place of the 
ODE component of the hybrid framework. Among the optimizers, PSO (AUC = 0.939) and GWO (AUC = 0.916) 
exhibited the highest discriminatory power, markedly outperforming the others. In contrast, ACO (AUC = 0.672) 
and WOA (AUC = 0.696) demonstrated substantially lower performance. Figure  8 presents the ROC curves 
obtained with the optimally tuned parameters in the hybrid framework with ODE, showing similar trends but 
slightly lower AUC values. These findings indicate that PSO and GWO consistently maintain superior perfor­
mance, even within the computationally efficient surrogate framework, demonstrating stable performance across 
surrogate and ODE-based implementations.
Figure 9 presents radar plots summarizing the performance metrics of different MOAs across the seven best 
ML models (DT, RF, GB, XGBoost, LightGBM, CatBoost, and ANN). Across most models, PSO and GWO con­
sistently exhibit superior performance, achieving high relative accuracy, AUC, TPR, TNR, and F1-scores, while 
also maintaining strong convergence efficiency and time reduction. GA and BA perform competitively in certain 
ML frameworks, yet they generally lag behind PSO and GWO. In contrast, ABC and WOA demonstrate lower 
normalized true performance and relative accuracy across multiple metrics, particularly in models such as DT and 
GB. Optimizers like ACO achieve moderate accuracy and discriminatory power, but with comparatively lower 
convergence efficiency. These trends highlight that PSO and GWO provide a balanced combination of predictive 
performance and computational efficiency across ML frameworks, whereas other MOAs often trade off accuracy 
for speed or vice versa. The impact of ML integration is most evident in computational time, with notable reduc­
tions across most methods. However, RF exhibited comparatively smaller time savings. In terms of predictive 
relative accuracy, binary classification metrics remained close to 100% for PSO- and GWO-based models, and 
were consistently high for BA and FA. By contrast, other MOAs showed greater variability and larger errors 
across ML algorithms, including WOA with DT, GA with GB, ABC with XGBoost, and ACO with LightGBM.
Figure 10 presents radar plots of normalized performance metrics across different ML models under various 
MOAs. Overall, the plots reveal distinct performance patterns for each MOA. GWO- and PSO-based models 
consistently exhibit high normalized true performance and relative accuracy across all metrics, particularly excel­
ling in relative aaccuracies of AUC, ACC, and F1-score for ANN and boosting models. Conversely, ABC- and 
WOA-based models generally demonstrate lower overall performance, with WOA showing notable reductions 
in normalized relative accuracy for TPR and F1-score. Intermediate behavior is observed for GA, ACO, FA, and 
BA, with some metrics approaching peak values while others lag. ANN and GB models maintain robust per­
formance across most MOAs, highlighting their effectiveness when coupled with high-performing optimizers. 
ML
MOA
AUC 
Train
ACC 
Train
TPR 
Train
TNR 
Train
F1score 
Train
AUC Test ACC Test TPR Test
TNR Test
F1Score 
Test
ANN
FA
0.68635
0.70909
0.70588
0.70992
0.50000
0.83030
0.75714
0.80000
0.74545
0.58537
ANN
BA
0.88617
0.84242
0.85294
0.83969
0.69048
0.84848
0.72857
0.93333
0.67273
0.59574
ANN
ABC
0.83767
0.78182
0.88235
0.75573
0.62500
0.81697
0.71429
0.86667
0.67273
0.56522
ANN
WOA
0.63583
0.73333
0.61765
0.76336
0.48837
0.64727
0.68571
0.66667
0.69091
0.47619
Table 13  (continued)
 
1 3
25
Page 25 of 49 
285

---

## Page 26
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
MOA
ML model
Median difference (ETP)1
p-value2
95% CI Lower3
95% CI Upper3
GA
DT
961.53
< 0.0001
621.45
1193.7
GA
RF
1034.7
< 0.0001
702.64
1264.5
GA
GB
918.41
< 0.0001
590.12
1150.0
GA
XGBoost
820.54
< 0.0001
478.24
1054.4
GA
LightGBM
1041.5
< 0.0001
713.27
1278.1
GA
CatBoost
832.85
< 0.0001
498.62
1068.3
GA
ANN
975.56
< 0.0001
644.63
1212.8
PSO
DT
403.72
0.0112
63.506
640.65
PSO
RF
201.17
0.1066
− 130.55
433.40
PSO
GB
147.95
0.1758
− 191.74
374.54
PSO
XGBoost
161.61
0.1613
− 180.1
396.48
PSO
LightGBM
202.79
0.1059
− 130.29
432.63
PSO
CatBoost
172.16
0.1428
− 162.15
399.79
PSO
ANN
34.347
0.4082
− 300.7
265.92
GWO
DT
-0.72527
0.5023
-337.8
234.20
GWO
RF
96.585
0.2691
-239.16
328.06
GWO
GB
79.407
0.2995
-253.18
311.22
GWO
XGBoost
96.002
0.2729
-240.36
326.09
GWO
LightGBM
19.73
0.4460
-312.92
247.86
GWO
CatBoost
-66.102
0.6851
-399.07
168.39
ACO
DT
1024.5
< 0.0001
684.73
1254.0
ACO
RF
999.55
< 0.0001
664.1
1233.6
ACO
GB
1042.8
< 0.0001
705.91
1275.1
ACO
XGBoost
1315
< 0.0001
986.4
1545.1
ACO
LightGBM
1128.4
< 0.0001
787.06
1359.6
ACO
CatBoost
1043.5
< 0.0001
718.56
1275.6
ACO
ANN
1315.9
< 0.0001
972.88
1545.3
FA
DT
844.66
0.0001
512.87
1081.3
FA
RF
934.97
< 0.0001
593.66
1168.2
FA
GB
996.42
< 0.0001
656.59
1227.4
FA
XGBoost
1023.2
< 0.0001
681.59
1255.1
FA
LightGBM
1066.8
< 0.0001
732.25
1302.1
FA
CatBoost
1064.2
< 0.0001
726.04
1295.2
FA
ANN
728.67
0.0001
395.53
967.99
BA
DT
313.92
0.0324
-18.459
545.12
BA
RF
504.11
0.0025
169.46
738.09
BA
GB
583.82
0.0009
242.58
818.87
BA
XGBoost
370.33
0.0196
24.148
604.98
BA
LightGBM
404.07
0.0099
67.231
637.63
BA
CatBoost
243.91
0.0721
-95.938
475.04
BA
ANN
487.85
0.0040
148.01
723.09
ABC
DT
449.28
0.0048
114.37
682.88
ABC
RF
655.00
0.0004
322.24
884.80
ABC
GB
562.66
0.0009
231.6
789.81
ABC
XGBoost
621.29
0.0003
283.42
856.89
ABC
LightGBM
570.12
0.0012
237.87
802.33
ABC
CatBoost
594.32
0.0008
260.09
828.41
ABC
ANN
298.87
0.0354
-30.815
530.01
WOA
DT
1455.6
< 0.0001
1121.4
1688.2
WOA
RF
855.41
< 0.0001
512.43
1093.7
WOA
GB
1250.2
< 0.0001
918.44
1483.5
WOA
XGBoost
1067.5
< 0.0001
736.39
1299.2
WOA
LightGBM
1190.2
< 0.0001
853.88
1419.8
Table 14  Comparative performance of ANN-GWO and alternative ML-MOA models in discriminating RVTE from non-
RVTE patients using endogenous thrombin potential
1 3
26
285 
Page 26 of 49

---

## Page 27
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
These results underscore the influence of MOA selection on ML model performance and demonstrate that GWO 
and PSO are particularly efficient for both classical and ensemble ML approaches.
Together with previous analyses, these visual summaries further support the consistent superiority of swarm-
based optimizers (PSO and GWO) in achieving stable, high-accuracy, and computationally efficient hybrid mod­
els, particularly when coupled with the ANN surrogate.
3.2  Detailed evaluation of the best-performing ANN surrogate
Based on the previously presented comparative results, the ANN emerged as the most accurate surrogate model. 
This subsection provides a deeper evaluation of ANN-based models optimized using all MOAs, with particular 
emphasis on GWO and PSO, which demonstrated the strongest optimization performance.
Following the replacement of the ODE-based kinetic model with a fully differentiable ANN surrogate, gradi­
ent-based optimizers became applicable in theory. Accordingly, Adam, RMSProp, and SGD were implemented as 
baseline optimizers and directly compared with PSO and GWO in terms of convergence behavior, computational 
efficiency, and predictive fidelity.
Figure 11 illustrates convergence trajectories under both surrogate-based and true ODE evaluations. Because 
gradient-based methods were approximately three times faster per iteration than MOAs, their iteration budget 
was increased to 900 (versus 300 for MOAs) to ensure comparable total runtime. Although SGD converged rap­
idly, it reached substantially lower DMP values, indicating convergence to a local optimum. Adam and RMSProp 
Fig. 7  ROC curves for the test set of the hybrid model with 
ANN–Surrogate replacing the ODE system, optimized by 
different MOAs
 
MOA
ML model
Median difference (ETP)1
p-value2
95% CI Lower3
95% CI Upper3
WOA
CatBoost
1145.4
< 0.0001
811.34
1378.2
WOA
ANN
1148
< 0.0001
811.44
1382.1
1Median difference: Difference in mean ETP separation between RVTE and non-RVTE patients (ANN-GWO minus comparative model)
2p-value: One-sided Wilcoxon signed-rank test assessing whether ANN-GWO separation is significantly greater than the comparative model. 
P-values < 0.05 denote statistically significant superiority of ANN-GWO
395% CI: Percentile-based bootstrap confidence interval of the median difference (10,000 resamples). Positive values indicate that ANN-GWO 
provides superior discrimination
Bold values indicate non-signifi cant p-values
Table 14  (continued)
 
1 3
27
Page 27 of 49 
285

---

## Page 28
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
exhibited smoother convergence behavior but showed marked discrepancies between surrogate and true ODE 
evaluations. In contrast, PSO and GWO consistently achieved higher DMP values and demonstrated strong 
agreement between surrogate and true evaluations.
Table 15 summarizes the quantitative comparison. While gradient-based optimizers achieved substantial reduc­
tions in optimization time (≈ 99.8%), this improvement was accompanied by lower objective quality. Adam and 
RMSProp yielded relative accuracies of approximately 66–67%, whereas PSO and GWO maintained accuracies 
Fig. 9  Radar plots of performance metrics (see Table 3) comparing MOAs across ML models. Metrics include: 
∼
P
ML
i,j , RAi,j, 
TRi,j, CEi,j, RAAUC
i,j
, RAACC
i,j
, RAT P R
i,j
, RAT NR
i,j
, RAF 1
i,j  for MOAs j ∊ {GA, PSO, GWO, ACO, FA, BA, ABC, WOA} 
under ML models. (a) DT, (b) RF, (c) GB, (d) XGBoost, (e) LightGBM, (f) CatBoost, and (g) ANN
 
Fig. 8  ROC curves for the test of the true hybrid ANN–ODE 
model using adjustable parameters optimized via ANN–Sur­
rogate across different MOAs
 
1 3
28
285 
Page 28 of 49

---

## Page 29
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
above 92%, with GWO approaching 98%. Although SGD achieved high relative accuracy (99.83%), this reflects 
strong surrogate–ODE agreement at a low-quality solution, rather than identification of a globally competitive 
optimum.
Collectively, these findings suggest that, despite differentiability, the ANN-based objective landscape remains 
highly nonconvex and challenging to optimize. Gradient-based methods appear sensitive to initialization and 
may converge prematurely, whereas metaheuristic algorithms provide more robust global search and consistently 
identify higher-quality optima. Therefore, metaheuristic optimization remains advantageous within this hybrid 
modeling framework.
Table 16 summarizes the predictive performance of ANN surrogate models optimized using different meta­
heuristic and gradient-based algorithms, while Table 17 reports the corresponding results obtained using the 
original ODE-based model. Overall, ANN surrogates consistently matched or outperformed the ODE-based 
counterparts across most metrics and optimization strategies, particularly on the independent test set.
Among all optimization algorithms, the GWO achieved the strongest and most stable performance for the 
ANN surrogate, yielding the highest test AUC (0.916, 95% CI: 0.840–0.974), along with balanced sensitivity 
(TPR = 0.933) and specificity (TNR = 0.891). PSO ranked second, demonstrating excellent generalization with a 
test AUC of 0.939 (95% CI: 0.876–0.985) and high accuracy (0.886), confirming its robustness as an alternative 
optimizer.
In contrast, gradient-based optimizers (Adam, RMSProp, SGD) showed competitive training performance but 
substantial degradation on the test set, particularly in sensitivity and F1-score, indicating overfitting and reduced 
Fig. 10  Radar plots of performance metrics (see Table  3) comparing ML models across MOAs. Met­
rics include: 
∼
P
MOA
i,j
, 
∼
RA
MOA
i,j
, 
∼
TR
MOA
i,j
, 
∼
RA
AUC
i,j
, 
∼
RA
ACC
i,j
, 
∼
RA
T P R
i,j
, 
∼
RA
T NR
i,j
, 
∼
RA
F 1
i,j  for ML models i ∊ 
{DT, RF, GB, XGBoost, LightGBM, CatBoost, ANN} under MOAs. (a) GA, (b) PSO, (c) GWO, (d) ACO, (e) FA, 
(f) BA, (g) ABC, and (h) WOA
 
1 3
29
Page 29 of 49 
285

---

## Page 30
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
generalization. Across nearly all optimization algorithms, ANN-based surrogates achieved test AUCs equal to 
or higher than those of their ODE-based counterparts. These findings identify the ANN–PSO and ANN–GWO 
configurations as the most reliable and generalizable modeling strategies, with minimal performance loss upon 
replacing the ODE model with the ANN surrogate.
Framework sensitivity analysis identified a small subset of design choices with statistically significant and 
practically meaningful effects on RVTE prediction performance (Table 18). Across metaheuristic optimizers, 
the normalization strategy consistently emerged as the dominant determinant of test-set AUC, explaining up to 
28.9% of the explainable variance and yielding absolute performance gains of up to 0.075. This effect was par­
ticularly pronounced for GWO and PSO, which also achieved the highest mean test AUCs under standardized 
normalization. The feature selection strategy showed a smaller but reproducible influence, with full or PCA-
based representations providing modest improvements, depending on the optimizer. Model capacity, reflected by 
the number of hidden neurons, contributed a secondary yet significant effect in selected algorithms. In contrast, 
neither the initial condition model nor the kinetic parameter configuration exerted a consistent or substantial 
Table 15  Performance comparison of gradient-based and metaheuristic optimization strategies
MOA
Optimal DMP 
(Surrogate)
True DMP (Full 
ODE)
Relative Accuracy 
(%)
Surrogate average 
Simulation Time (min)
Time Reduction 
(%)
Conver­
gence 
efficiency 
(%)
PSO
275,547.26
254,905.28
92.51
8.32
99.55
57.00
GWO
291,759.95
285,828.28
97.97
8.31
99.12
28.33
Adam
213,409.55
141,536.55
66.32
2.80
99.80
65.33
RMSProp
219,946.57
148,127.41
67.35
2.74
99.89
50.44
SGD
68,722.41
68,606.05
99.83
2.75
99.88
99.78
Fig. 11  Convergence behavior of gradient-based and metaheuristic optimizers using ANN surrogate and true ODE evaluations
 
1 3
30
285 
Page 30 of 49

---

## Page 31
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Table 16  Performance of ANN surrogate models optimized by metaheuristic and gradient-based algorithms (bootstrap median and 95% CIs for training and testing 
metrics)
MOA
AUC Train
ACC Train
TPR Train
TNR Train
F1score Train
AUC Test
ACC Test
TPR Test
TNR Test
F1Score Test
GA
0.7868 (0.7022, 
0.8614)
0.7215 (0.6545, 
0.7879)
0.9415 (0.8485, 
1.0000)
0.6642 (0.5809, 
0.7441)
0.5806 (0.4660, 
0.6863)
0.7681 (0.6341, 
0.8824)
0.6284 (0.5143, 
0.7429)
0.8008 (0.5714, 
1.0000)
0.5816 
(0.4483, 
0.7091)
0.4684 
(0.2405, 
0.6415)
PSO
0.8732 (0.7695, 
0.9595)
0.9210 (0.8788, 
0.9576)
0.8824 (0.7619, 
0.9737)
0.9310 (0.8842, 
0.9704)
0.8195 (0.7143, 
0.9091)
0.9394 (0.8763, 
0.9845)
0.8861 (0.8000, 
0.9571)
0.9341 (0.7857, 
1.0000)
0.8731 
(0.7778, 
0.9592)
0.7736 
(0.6000, 
0.9130)
GWO
0.9673 (0.9172, 
0.9961)
0.9456 (0.9091, 
0.9758)
0.9419 (0.8495, 
1.0000)
0.9466 (0.9051, 
0.9841)
0.8753 (0.7838, 
0.9493)
0.9164 (0.8400, 
0.9740)
0.9001 (0.8286, 
0.9571)
0.9327 (0.7778, 
1.0000)
0.8912 
(0.8036, 
0.9643)
0.7954 
(0.6286, 
0.9268)
ACO
0.6997 (0.5978, 
0.7939)
0.7034 (0.6364, 
0.7697)
0.7359 (0.5806, 
0.8750)
0.6950 (0.6169, 
0.7727)
0.4991 (0.3378, 
0.6195)
0.6715 (0.4834, 
0.8438)
0.6137 (0.5000, 
0.7286)
0.6670 (0.4118, 
0.9000)
0.5990 
(0.4667, 
0.7288)
0.3942 
(0.1429, 
0.5882)
FA
0.6701 (0.5605, 
0.7740)
0.7154 (0.6485, 
0.7818)
0.7059 (0.5455, 
0.8571)
0.7180 (0.6412, 
0.7923)
0.4977 (0.3162, 
0.6226)
0.8527 (0.7308, 
0.9526)
0.7433 (0.6429, 
0.8429)
0.7353 (0.5000, 
0.9412)
0.7455 
(0.6271, 
0.8547)
0.5384 
(0.2727, 
0.7222)
BA
0.8968 (0.8209, 
0.9565)
0.8784 (0.8242, 
0.9273)
0.8227 (0.6818, 
0.9412)
0.8930 (0.8372, 
0.9440)
0.7338 (0.6111, 
0.8387)
0.8502 (0.7490, 
0.9350)
0.8295 (0.7429, 
0.9143)
0.8681 (0.6667, 
1.0000)
0.8189 
(0.7119, 
0.9138)
0.6795 
(0.4848, 
0.8372)
ABC
0.8456 (0.7821, 
0.9020)
0.7880 (0.7273, 
0.8485)
0.8816 (0.7619, 
0.9730)
0.7636 (0.6889, 
0.8346)
0.6297 (0.5106, 
0.7368)
0.8237 (0.7181, 
0.9133)
0.7153 (0.6143, 
0.8143)
0.8673 (0.6667, 
1.0000)
0.6738 
(0.5472, 
0.7963)
0.5608 
(0.3636, 
0.7234)
WOA
0.6503 (0.5327, 
0.7597)
0.7332 (0.6667, 
0.8000)
0.6169 (0.4483, 
0.7813)
0.7635 (0.6899, 
0.8333)
0.4689 (0.2645, 
0.6139)
0.6952 (0.5395, 
0.8367)
0.6851 (0.5714, 
0.7857)
0.6668 (0.4000, 
0.9091)
0.6900 
(0.5660, 
0.8103)
0.4500 
(0.1736, 
0.6500)
Adam
0.9260 (0.8722, 
0.9699)
0.9272 (0.8848, 
0.9636)
0.7649 (0.6129, 
0.9000)
0.9694 (0.9375, 
0.9926)
0.8102 (0.6939, 
0.9057)
0.6519 (0.4494, 
0.8407)
0.8865 (0.8000, 
0.9571)
0.4705 (0.2143, 
0.7333)
1.0000 
(1.0000, 
1.0000)
0.6286 
(0.3529, 
0.8462)
RMSProp
0.9226 (0.8655, 
0.9693)
0.9275 (0.8848, 
0.9636)
0.7362 (0.5806, 
0.8788)
0.9771 (0.9480, 
1.0000)
0.8044 (0.6866, 
0.9041)
0.6840 (0.8419, 
0.9143)
0.8288 (0.7429, 
0.9143)
0.4000 (0.1429, 
0.6667)
0.9454 
(0.8776, 
1.0000)
0.4677 
(0.1111, 
0.7200)
SGD
0.5960 (0.4876, 
0.7026)
0.5214 (0.4424, 
0.6000)
0.7656 (0.6133, 
0.9032)
0.4581 (0.3731, 
0.5455)
0.3868 (0.2384, 
0.5000)
0.6420 (0.4790, 
0.7928)
0.5429 (0.4286, 
0.6571)
0.7994 (0.5714, 
1.0000)
0.4727 
(0.3396, 
0.6034)
0.4164 
(0.2042, 
0.5806)
1 3
31
Page 31 of 49 
285

---

## Page 32
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
impact on test-set performance, indicating that baseline initialization and default kinetic formulations were suf­
ficient for RVTE discrimination. Collectively, these results demonstrate that framework-level preprocessing and 
representation choices, rather than mechanistic parameter variations, are the primary drivers of performance dif­
ferences across optimization strategies.
The bootstrap DeLong analysis confirmed significant differences in discriminatory performance among opti­
mization strategies (Table 19). The GWO achieved a mean AUC of 0.917 (95% CI: 0.841–0.973), serving as 
the reference method. Although PSO produced a numerically higher mean AUC (0.940; 95% CI: 0.880–0.984), 
the difference relative to GWO was not statistically significant (ΔAUC = 0.023, p = 0.554), indicating compa­
rable discriminative performance. In contrast, GWO significantly outperformed several metaheuristic optimizers, 
including the GA (p = 0.0168), ACO (p = 0.0178), and WOA (p = 0.0080). GWO also demonstrated clear statisti­
cal superiority over gradient-based optimizers: Adam (p = 0.0076), RMSProp (p = 0.0100), and SGD (p = 0.0022). 
All gradient-based optimizers showed substantially lower AUCs. Differences between GWO and the FA and BA 
were not statistically significant, while ABC approached but did not reach significance (p = 0.0528). Overall, 
these results identify GWO and PSO as the top-performing optimizers in terms of AUC, with GWO exhibiting 
the most consistent and statistically robust discrimination.
The evaluated optimization models displayed distinct and complementary performance profiles regarding cali­
bration, clinical utility, and threshold stability (Fig. 12). In the calibration analysis (Fig. 12A), the GWO- and 
PSO-optimized frameworks demonstrated the highest fidelity, with predicted risks showing strong agreement 
with observed event rates across the entire risk spectrum. The calibration curves for these methods tracked the 
ideal reference line more closely than those of competing metaheuristics and exhibited narrower bootstrap CIs, 
suggesting enhanced model stability and reduced predictive uncertainty.
The clinical impact was further quantified using DCA (Fig. 12B), underscoring the utility of GWO and PSO. 
Across a broad range of clinically relevant threshold probabilities, both methods consistently achieved a higher 
net benefit than alternative optimizers or “treat-all/treat-none” strategies. Notably, GWO maintained the peak net 
benefit across most thresholds, representing an optimal trade-off between sensitivity for RVTE events and mini­
mizing unnecessary clinical interventions.
Finally, threshold stability was assessed using Youden’s index plateaus on the ETP scale (Fig. 12C). GWO 
and PSO yielded balanced sensitivity and specificity without relying on extreme or unstable cutoffs. The broad 
plateau observed for these optimizers, as opposed to the sharp, localized peaks seen in other methods, suggests a 
robust decision-making zone. This threshold behavior is particularly critical for clinical translation, as it ensures 
that the model remains reliable even under slight variations in population-specific cutoffs. Collectively, these 
findings position GWO and PSO as the most robust candidates for threshold-based clinical decision support in 
RVTE risk stratification.
To investigate how systemic clinical profiles relate to localized biochemical mechanisms and how these rela­
tionships vary with recurrence status, we performed a stratified Spearman correlation analysis using the optimal 
ANN–GWO and ANN–PSO surrogate frameworks. Results are summarized in Figs. 13, 14, 15 and 16, and pro­
vide complementary insight into both stable and RVTE-specific clinical–mechanistic couplings.
The stratified rank correlation maps for RVTE − and RVTE+ patients (Figs. 13 and 15) reveal a heterogeneous 
pattern of predominantly weak-to-moderate associations across kinetic parameters and clinical variables. This 
diffuse structure indicates that coagulation kinetics are governed by nonlinear, multifactorial interactions rather 
than by a single dominant clinical driver.
Despite this complexity, several hematological indices exhibited consistent and recurrent associations across 
both recurrence strata and both optimization frameworks. In particular, red blood cell (RBC) count, hemoglobin, 
and hematocrit showed the most robust and spatially coherent correlations with multiple kinetic parameters, sug­
gesting a stable link between erythrocyte-related properties and coagulation dynamics. White blood cell (WBC) 
count and antithrombin III (AT-III) emerged as secondary but statistically significant modulators, consistent with 
the contribution of inflammatory and anticoagulant pathways to thrombin generation.
1 3
32
285 
Page 32 of 49

---

## Page 33
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Table 17  Performance of ODE-based reference models optimized by metaheuristic and gradient-based algorithms (bootstrap median and 95% CIs for training and 
testing metrics)
MOA
AUC Train
ACC Train
TPR Train
TNR Train
F1score Train
AUC Test
ACC Test
TPR Test
TNR Test
F1Score Test
GA
0.7619 (0.6841, 
0.8343)
0.7216 (0.6545, 
0.7879)
0.9419 (0.8529, 
1.0000)
0.6645 (0.5814, 
0.7443)
0.5801 (0.4632, 
0.6838)
0.6801 (0.5463, 
0.8023)
0.6300 (0.5143, 
0.7429)
0.7985 (0.5714, 
1.0000)
0.5838 
(0.4528, 
0.7143)
0.4699 
(0.2424, 
0.6414)
PSO
0.8486 (0.7433, 
0.9357)
0.9152 (0.8727, 
0.9576)
0.8820 (0.7586, 
0.9730)
0.9239 (0.8769, 
0.9645)
0.8086 (0.6984, 
0.8986)
0.9239 (0.8551, 
0.9769)
0.8285 (0.7429, 
0.9143)
0.8660 (0.6667, 
1.0000)
0.8182 
(0.7143, 
0.9138)
0.6776 
(0.4848, 
0.8372)
GWO
0.9354 (0.8711, 
0.9843)
0.9455 (0.9091, 
0.9758)
0.9413 (0.8485, 
1.0000)
0.9466 (0.9051, 
0.9837)
0.8749 (0.7813, 
0.9500)
0.8942 (0.8071, 
0.9636)
0.8999 (0.8286, 
0.9571)
0.9343 (0.7778, 
1.0000)
0.8905 
(0.8000, 
0.9643)
0.7953 
(0.6250, 
0.9231)
ACO
0.7408 (0.6487, 
0.8274)
0.6971 (0.6242, 
0.7636)
0.7351 (0.5833, 
0.8788)
0.6872 (0.6064, 
0.7647)
0.4931 (0.3279, 
0.6111)
0.5461 (0.3850, 
0.7043)
0.5863 (0.4714, 
0.7000)
0.6661 (0.4000, 
0.9000)
0.5643 
(0.4333, 
0.6923)
0.3768 
(0.1326, 
0.5714)
FA
0.6855 (0.5776, 
0.7927)
0.7087 (0.6364, 
0.7758)
0.7049 (0.5484, 
0.8571)
0.7098 (0.6290, 
0.7865)
0.4907 (0.3210, 
0.6154)
0.8308 (0.7060, 
0.9350)
0.7580 (0.6571, 
0.8571)
0.8009 (0.5714, 
1.0000)
0.7462 
(0.6250, 
0.8571)
0.5780 
(0.3429, 
0.7500)
BA
0.8858 (0.8085, 
0.9469)
0.8420 (0.7818, 
0.8970)
0.8522 (0.7222, 
0.9667)
0.8393 (0.7731, 
0.9008)
0.6874 (0.5641, 
0.7957)
0.8486 (0.7492, 
0.9349)
0.7288 (0.6143, 
0.8286)
0.9340 (0.7778, 
1.0000)
0.6730 
(0.5472, 
0.7931)
0.5907 
(0.4087, 
0.7500)
ABC
0.8374 (0.7748, 
0.8940)
0.7815 (0.7212, 
0.8424)
0.8825 (0.7586, 
0.9737)
0.7553 (0.6818, 
0.8277)
0.6221 (0.5000, 
0.7306)
0.8176
(0.7149, 0.9085)
0.7151 (0.6000, 
0.8143)
0.8677 (0.6667, 
1.0000)
0.6732 
(0.5470, 
0.7925)
0.5604 
(0.3615, 
0.7200)
WOA
0.6369
(0.5224, 0.7469)
0.7337 (0.6667, 
0.8000)
0.6188 (0.4483, 
0.7826)
0.7635 (0.6884, 
0.8333)
0.4693 (0.2608, 
0.6108)
0.6484 (0.4984, 
0.7895)
0.6870 (0.5714, 
0.7857)
0.6670 (0.4167, 
0.9091)
0.6925 
(0.5636, 
0.8077)
0.4523 
(0.1832, 
0.6512)
Adam
0.9049 (0.8443, 
0.9543)
0.8181 (0.7576, 
0.8727)
0.8826 (0.7647, 
0.9730)
0.8014 (0.7308, 
0.8682)
0.6641 (0.5430, 
0.7692)
0.6145 (0.4112, 
0.8057)
0.7568 (0.6571, 
0.8571)
0.4643 (0.2000, 
0.7273)
0.8367 
(0.7347, 
0.9273)
0.3955 
(0.0833, 
0.6471)
RMSProp
0.8991 (0.8358, 
0.9520)
0.8061 (0.7455, 
0.9520)
0.8829 (0.7619, 
0.9730)
0.7861 (0.7132, 
0.8538)
0.6498 (0.5263, 
0.7600)
0.6382 (0.4570, 
0.8053)
0.7145 (0.6000, 
0.8143)
0.4649 (0.2000, 
0.7273)
0.7826 
(0.6667, 
0.8868)
0.3456 
(0.0672, 
0.6087)
SGD
0.5949 (0.4884, 
0.6963)
0.5390 (0.4606, 
0.6121)
0.7352 (0.5806, 
0.8800)
0.4881 (0.4015, 
0.5736)
0.3816 (0.2286, 
0.5000)
0.6188 (0.4406, 
0.7845)
0.5570 (0.4429, 
0.6714)
0.7339 (0.5000, 
0.9375)
0.5088 
(0.3750, 
0.6364)
0.3938 
(0.1645, 
0.5714)
1 3
33
Page 33 of 49 
285

---

## Page 34
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Significant correlations were sparsely distributed, reinforcing that no single clinical variable uniformly gov­
erns the mechanistic landscape. Instead, the observed associations reflect distributed sensitivity across multiple 
physiological domains.
To explicitly quantify recurrence-dependent shifts in clinical–mechanistic coupling, we computed Δρ maps 
(Figs. 14 and 16), defined as the difference in Spearman correlation coefficients between the RVTE + and RVTE− 
groups. While the majority of Δρ values clustered near zero, indicating broadly conserved association patterns, a 
subset of kinetic parameters exhibited statistically significant deviations, highlighting RVTE-specific modulation.
Positive Δρ values were most frequently associated with erythrocyte-related indices (RBC count, hemoglobin, 
and hematocrit), indicating that, in RVTE+ patients, variations in these variables exert a disproportionately stron­
ger influence on kinetic rates than in the non-recurrent group. This pattern may reflect altered blood rheology, 
erythrocyte–leukocyte interactions, or potential alterations in erythrocyte-mediated microenvironmental effects 
in patients prone to recurrence.
A pronounced and consistent finding across both frameworks was the age-dependent amplification of associa­
tions with Kcat47 and Kcat14, corresponding to the activation of coagulation factors X and V, respectively. These 
parameters are central components of the prothrombinase complex, and their age-sensitive modulation in RVTE+ 
patients suggests selective sensitization of key amplification pathways within the coagulation cascade.
In addition, the duration of anticoagulation therapy showed positive Δρ values across several kinetic param­
eters, suggesting that long-term treatment may not only suppress coagulation activity but also be associated 
with altered coupling patterns, particularly in patients with recurrent disease. WBC count and AT-III also dem­
onstrated localized but significant Δρ shifts, consistent with recurrence-specific inflammatory and anticoagulant 
adaptations.
Importantly, these RVTE-associated changes were distributed across multiple clinical domains rather than 
driven by a single factor, underscoring the multifactorial architecture of recurrence risk.
Comparison of the GWO- and PSO-optimized surrogates demonstrates strong concordance in the overall 
topology of the stratified correlation and Δρ maps. Both optimizers consistently identified the dominance of the 
erythrocyte-related triad (RBC, hemoglobin, hematocrit) and the age-dependent sensitivity of factor X and factor 
V activation, supporting the biological robustness of these findings.
Subtle differences in sensitivity were observed. The PSO-derived Δρ maps (Fig. 16) exhibited slightly enhanced 
detection of significant shifts involving AT-III and WBC count, suggesting increased sensitivity to lower-magni­
tude inflammatory or anticoagulant effects. In contrast, the GWO framework yielded a marginally stronger and 
more spatially coherent signal for age-related modulation of kinetic parameters. Nevertheless, these differences 
were quantitative rather than qualitative.
The convergence of two distinct heuristic optimization strategies on the same core biological signatures pro­
vides internal validation of the surrogate modeling framework. It supports the interpretation that the observed 
associations reflect intrinsic properties of the patient cohorts rather than optimizer-specific artifacts.
The transition from an RVTE − to an RVTE+ phenotype is characterized by a distributed reweighting of 
clinical influence on coagulation kinetics rather than by wholesale reorganization of the association structure. 
Age-dependent modulation of factor X and V activation and the amplified role of hematological indices in recur­
rent patients define a distinct biochemical signature of recurrence. These findings support a mechanistically 
grounded, multifactorial view of RVTE risk and highlight the potential of clinical–mechanistic coupling analyses 
for improved, personalized risk stratification in VTE. It is important to note that these associations should be 
interpreted with caution. Although the observed relationships are internally consistent, they arise from a pseudo-
supervised model-derived surrogate framework rather than from direct experimental supervision. Consequently, 
external validation and complementary experimental approaches—such as integration with thrombin genera­
tion assays—are necessary to strengthen the robustness, biological plausibility, and scientific credibility of the 
reported associations.
The normalized permutation-importance matrices were visualized as heatmaps (Figs. 17 and 18), providing a 
global, parameter-specific view of clinical feature sensitivity within the learned surrogate models. This analysis 
1 3
34
285 
Page 34 of 49

---

## Page 35
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
quantifies how perturbations in individual clinical inputs propagate through the ANN to influence distinct kinetic 
parameters of the coagulation cascade.
Permutation analysis of the ANN–GWO model (Fig. 17) revealed pronounced heterogeneity in feature impor­
tance across kinetic parameters, indicating that distinct subsets of clinical variables govern different biochemical 
reactions. No single input emerged as a universal driver; instead, importance patterns were highly structured and 
parameter-specific, consistent with the multifactorial nature of coagulation kinetics.
Across kinetic parameters, hematologic variables dominated the importance landscape. Red blood cell–related 
indices, such as RBC count, hemoglobin, and hematocrit, formed a coherent cluster of high importance and acted 
as primary drivers for multiple activation and saturation parameters, including Kcat9, Kcat12, Kcat14, Km15, and 
K50. This finding supports a central role for erythrocyte-related properties in shaping reaction rates and effective 
enzyme–substrate interactions within the coagulation system.
WBC count emerged as the single most influential feature on average in the GWO-optimized model, exhibit­
ing moderate-to-high importance across a broad set of kinetic parameters. This diffuse influence suggests that 
Table 18  Sensitivity of RVTE prediction performance to framework configuration across metaheuristic optimizers
Metaheuristic 
Optimizer
Framework Component
Best-Performing 
Configuration
ΔAUC (Best − Worst) Partial R² (Drop-One)
p-value
Best 
Mean 
Test 
AUC
GA
Normalization
Standardized
0.058
0.182
< 0.001
0.703
Selected Features
All features
0.033
0.070
< 0.001
0.691
PSO
Normalization
Standardized
0.060
0.163
< 0.001
0.841
Kinetic Parameters
Full parameter set
0.032
0.052
0.002
0.827
GWO
Normalization
Standardized
0.075
0.289
< 0.001
0.829
Hidden Neurons
50
0.045
0.064
< 0.001
0.808
Selected Features
All features
0.019
0.027
0.025
0.801
ACO
Selected Features
PCA-based
0.040
0.074
< 0.001
0.612
FA
Normalization
Standardized
0.028
0.037
0.009
0.653
Selected Features
PCA-based
0.027
0.035
0.010
0.652
BA
Normalization
Standardized
0.052
0.158
< 0.001
0.791
ABC
Fitness Score
DMP-L2 (full 
regularization)
0.052
0.096
< 0.001
0.750
Normalization
Standardized
0.029
0.046
0.003
0.737
Selected Features
PCA-based
0.021
0.026
0.028
0.733
WOA
Hidden Neurons
50
0.033
0.022
0.045
0.630
Notes: ΔAUC represents the difference between the highest and lowest mean test AUC observed across levels of each framework component. 
Partial R² was computed using a drop-one model strategy and reflects the proportion of variance explained by each setting relative to the unex­
plained variance. Only statistically significant factors (p < 0.05) are reported. Reported AUC values correspond to the mean performance across 
configurations that share the specified setting and do not necessarily reflect the single globally optimal model
Table 19  Pairwise DeLong comparison of AUCs across optimization algorithms for RVTE prediction
Optimizer
Mean AUC
95% CI (Lower)
95% CI (Upper)
ΔAUC vs. GWO
Z-Statistic
p-Value
GWO
0.9168
0.8406
0.9733
-
-
-
GA
0.7677
0.6378
0.8800
− 0.1491
2.1199
0.0168
PSO
0.9397
0.8804
0.9842
0.0230
− 0.4870
0.5540
ACO
0.6722
0.4788
0.8462
− 0.2446
2.3591
0.0178
FA
0.8523
0.7327
0.9492
− 0.0645
0.9382
0.3074
BA
0.8500
0.7512
0.9350
− 0.0668
1.0724
0.2410
ABC
0.8240
0.7207
0.9109
− 0.0928
1.6329
0.0528
WOA
0.6950
0.5397
0.8364
− 0.2218
2.5304
0.0080
Adam
0.6510
0.4481
0.8358
− 0.2658
2.6266
0.0076
RMSProp
0.6842
0.5100
0.8434
− 0.2326
2.4092
0.0100
SGD
0.6432
0.4791
0.7942
− 0.2735
3.1421
0.0022
1 3
35
Page 35 of 49 
285

---

## Page 36
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
inflammatory or immune-related processes act as global modulators rather than targeting a single reaction step, 
consistent with the known crosstalk between leukocytes and thrombin generation.
Age also displayed strong and selective importance, particularly for activation constants such as Kcat10, Kcat11, 
and Kcat13, as well as downstream parameters including K49. These patterns reinforce the role of age as a modula­
tor of amplification dynamics rather than baseline reaction rates.
In contrast, lipid-related variables and metabolic markers generally showed lower and more localized impor­
tance, with HDL cholesterol and glucose exerting sparse but non-negligible influence on specific parameters such 
as K17 and K53. Collectively, these results underscore that the ANN–GWO model’s predictive capacity arises 
from integrating multiple clinical domains rather than relying on a narrow subset of inputs.
Fig. 12  Comparative 
evaluation of (A) calibration 
curves, (B) clinical utility, 
and (C) decision stabil­
ity across MOAs. THR: 
Threshold. Se: sensivity. Sp: 
Specificity
 
1 3
36
285 
Page 36 of 49

---

## Page 37
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Entropy-based analysis further demonstrated that feature importance in the GWO model was relatively con­
centrated (mean entropy = 3.84), indicating sharper reliance on dominant hematologic and inflammatory features.
Permutation analysis of the ANN–PSO model (Fig. 18) revealed a broadly consistent yet quantitatively distinct 
importance structure. While hematologic variables remained influential, the PSO-optimized network distributed 
importance more evenly across clinical inputs.
Age emerged as the most influential feature overall in the PSO model, followed closely by thrombosis side, 
total cholesterol, and LDL cholesterol, indicating a stronger integration of demographic and metabolic informa­
tion compared with the GWO surrogate. Several kinetic parameters, including K50 and K51, consistently retained 
sensitivity to red blood cell indices across both optimizers, suggesting robust erythrocyte-driven effects indepen­
dent of the training heuristic.
Notably, Protein C ranked among the top contributors in both GWO and PSO frameworks, highlighting its 
stable mechanistic relevance. Protein S exerted a selective effect on K18 in both models, further supporting bio­
logical plausibility.
Compared with GWO, PSO exhibited a significantly higher entropy of importance (mean entropy = 5.30), 
indicating a more diffuse sensitivity profile. This redistribution is consistent with broader integration of the mul­
tidimensional input space during PSO optimization, reducing dominance by individual features.
Direct comparison of permutation-importance matrices revealed minimal global agreement between GWO 
and PSO at the individual-entry level (Spearman’s ρ = 0.03, p = 0.42), indicating that local feature–parameter sen­
sitivities differ substantially between optimization strategies. However, this apparent discrepancy masks strong 
agreement at a higher structural level.
Fig. 13  Stratified association analysis of clinical inputs and mechanistic kinetic parameters. Heatmaps display Spearman 
rank correlation coefficients (ρ) for the RVTE − and RVTE+ subgroups, generated using the optimal ANN-GWO framework. 
Significant associations, defined as those where the 95% bootstrap CI (10,000 iterations) excludes zero, are indicated by 
black markers
 
1 3
37
Page 37 of 49 
285

---

## Page 38
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Both optimizers consistently identified hematologic indices and age as dominant drivers, with age and protein 
C emerging as shared top-ranked features. Moreover, several kinetic parameters, particularly Kcat14, Kcat15, 
Kcat47, Km9, Km12, and K43, exhibited large optimizer-dependent shifts in sensitivity, suggesting that these reac­
tions are especially responsive to alternative parameterizations of the surrogate model.
Overall, the permutation analysis demonstrates that while GWO and PSO differ in how they distribute impor­
tance across inputs, they converge on the same core biological domains. GWO yields a more concentrated, 
feature-selective importance structure, whereas PSO promotes broader, more balanced integration of clinical 
information.
To evaluate robustness to stochastic variability, each metaheuristic was executed over 30 independent runs 
using fixed algorithmic settings from the top-performing models and distinct random initializations. Summary 
statistics of final fitness, convergence efficiency, and predictive performance are reported in Table 20.
Across repeated runs, GWO and PSO consistently emerged as the two best-performing algorithms, clearly out­
performing the remaining metaheuristics in terms of optimization quality and discriminative performance. Both 
methods achieved nearly identical mean final fitness values (PSO: 238,477; GWO: 236,845) and comparable 
best-case solutions exceeding 132,800, indicating a similar capacity to explore and exploit high-quality regions 
of the search space. In contrast, GA, FA, ABC, BA, ACO, and WOA exhibited markedly lower fitness values and 
greater variability, reflecting reduced robustness to stochastic initialization.
While the final optimization outcomes of GWO and PSO were highly comparable, differences were primarily 
observed in convergence dynamics rather than solution quality. PSO reached 90% of its final fitness on average 
earlier (61.5% of the optimization horizon) than GWO (42.2%), suggesting faster convergence. However, GWO 
demonstrated competitive convergence behavior with acceptable variability across runs, indicating stable albeit 
slower optimization trajectories.
In terms of predictive performance, both GWO and PSO achieved the highest bootstrap AUC values on the 
training and test sets, with only marginal differences between them (PSO: 0.881 train, 0.849 test; GWO: 0.875 
train, 0.821 test). These small performance gaps were accompanied by overlapping variability ranges, support­
ing the conclusion that both algorithms offer comparable generalization capability. The remaining metaheuristics 
produced substantially lower AUC values and higher dispersion, particularly on the test set, highlighting inferior 
stability under stochastic perturbations.
Statistical analysis corroborated these observations. The Friedman test ranked GWO and PSO as the top-
performing methods. Subsequent Nemenyi post-hoc comparisons revealed no statistically significant difference 
between GWO and PSO. GWO significantly outperformed all remaining algorithms, whereas PSO significantly 
Fig. 14  Δρ analysis of clinical inputs and mechanistic kinetic 
parameters, generated using the optimal ANN-GWO frame­
work. Visualization of the change in correlation strength 
between RVTE + and RVTE− strata. Significant associations, 
defined as those where the 95% bootstrap CI (10,000 itera­
tions) excludes zero, are indicated by black markers
 
1 3
38
285 
Page 38 of 49

---

## Page 39
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
outperformed all others except BA, for which the difference did not reach statistical significance. Taken together, 
these findings indicate that GWO and PSO provide similarly robust optimization performance, with PSO offering 
faster convergence and GWO representing a competitive alternative with comparable final solution quality and 
generalization performance.
4  Discussion
The present study demonstrates that replacing a computationally intensive ODE-based coagulation model with 
an ANN surrogate enables substantial gains in efficiency without compromising predictive fidelity. Linear regres­
sion methods confirmed the highly nonlinear structure of the problem, as they yielded relatively high and com­
parable errors. In contrast, boosting algorithms and ANN achieved markedly improved fits, consistent with their 
established ability to model nonlinear interactions in different applications [61, 62]. The ANN achieved the low­
est prediction errors (RMSE < 0.3 in both the training and test sets), highlighting its suitability as a surrogate for 
complex biochemical dynamics.
The best-performing ANN comprised 385 adjustable parameters compared with 41 kinetic parameters in the 
mechanistic ODE system. Despite the larger parameter space, the ANN achieved a drastic computational advan­
tage, reducing runtime by more than 99% while maintaining high fidelity, with a relative accuracy of 97.97% 
under ANN-GWO optimization. A similar example of reducing an intensive optimization problem through model 
replacement with an ANN is reported in the literature [63], where substituting a computationally demanding 
ODE system with an ANN during multiple optimization steps (as in model predictive control) decreased the 
Fig. 15  Stratified association analysis of clinical inputs and mechanistic kinetic parameters. Heatmaps display Spearman 
rank correlation coefficients (ρ) for the RVTE − and RVTE+ subgroups, generated using the optimal ANN-PSO framework. 
Significant associations, defined as those where the 95% bootstrap CI (10,000 iterations) excludes zero, are indicated by 
black markers
 
1 3
39
Page 39 of 49 
285

---

## Page 40
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
computational cost by approximately three orders of magnitude (around 1000-fold). This efficiency gain is par­
ticularly critical in hybrid mechanistic–data-driven frameworks, where repeated model evaluations constitute the 
principal computational bottleneck.
Within the hybrid framework, z-score normalization consistently emerged as the most effective preprocessing 
strategy, suggesting its role as a practical default for similar applications. This pattern aligns with the findings of 
Fig. 17  Relative feature importance for clinical-to-kinetic 
parameter mapping. Heatmap of normalized permutation 
importance values, highlighting the dependence of the ANN-
GWO on specific hematologic, metabolic, and clinical inputs
 
Fig. 16  Δρ analysis of clini­
cal inputs and mechanistic 
kinetic parameters, gener­
ated using the optimal ANN-
PSO framework. Visual­
ization of the change in 
correlation strength between 
RVTE + and RVTE− strata. 
Significant associations, 
defined as those where the 
95% bootstrap CI (10,000 
iterations) excludes zero, are 
indicated by black markers
 
1 3
40
285 
Page 40 of 49

---

## Page 41
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
the study by Singh and Singh [64], which reported that the z-score normalization method achieved the best per­
formance across 20 medical datasets using ML. The optimal configuration also employed initial concentrations 
of coagulation species reported by Zhu [35], varying only the kinetic parameters during training. This strategy is 
clinically relevant, as molar concentrations of most coagulation factors are rarely available in practice. Addition­
ally, feature reduction via PCA was often beneficial, lowering data collection demands. However, this came at 
Table 20  Robustness, convergence efficiency, predictive performance, and statistical comparison of metaheuristic algo­
rithms over 30 independent runs with ANN surrogate
Metric
Statistics
GA
PSO
GWO
ACO
FA
BA
ABC
WOA
Final DMP
Worst
95,112.75
190,068.89
204,295.83
39,579.67
79,653.98
160,937.75
124,601.29
1,590.74
Mean
117,737.58
238,477.51
236,845.91
56,120.81
88,733.67
201,625.39
161,295.02
10,427.98
Best
139,147.39
265,960,50
265,197.45
68,258.74
99,489.55
236,029.11
203,229.47
47,628.35
SD
6,970.24
19,856.29
16,620.44
48,406.41
4,922.55
16,411.60
19,210.44
11,252.15
Convergence Effi­
ciency (%)
Worst
43.00
42.67
26.33
99.67
48.00
6.67
32.67
81.33
Mean
76.92
61.46
42.22
99.67
78.84
59.90
55.00
97.98
Best
95.00
77.00
74.67
99.67
95.33
89.33
82.33
99.67
SD
13.47
8.88
10.80
0.00
12.85
22.89
13.36
3.65
Bootstrap AUC (Train) Worst
0.6300
0.7973
0.8139
0.5418
0.5864
0.7417
0.6893
0.3266
Mean
0.7494
0.8811
0.8749
0.6355
0.6912
0.8542
0.7808
0.4726
Best
0.8227
0.9337
0.9310
0.7107
0.7498
0.9280
0.8699
0.6012
SD
0.0387
0.0335
0.0354
0.0424
0.0399
0.0494
0.0469
0.0572
Bootstrap AUC (Test)
Worst
0.5492
0.7045
0.6978
0.4214
0.4841
0.6477
0.5731
0.3180
Mean
0.6995
0.8487
0.8213
0.5770
0.6432
0.7955
0.7354
0.4852
Best
0.8163
0.9553
0.9250
0.7346
0.7850
0.9390
0.8622
0.5886
SD
0.0695
0.0622
0.0455
0.0774
0.0889
0.0632
0.0630
0.0716
Friedman test
Rank
5
2
1
7
6
3
4
8
Average Rank
5.00
1.77
1.23
6.83
6.17
3.20
3.80
8.00
Nemenyi post-hoc
p-value vs. 
GWO
< 0.001
0.991
-
< 0.001
< 0.001
0.039
0.001
< 0.001
Significance
Very 
significant
Not 
significant
-
Very 
significant
Very 
significant
Significant
Significant
Very 
significant
p-value vs. PSO < 0.001
-
0.991
< 0.001
< 0.001
0.312
0.029
< 0.001
Significance
Very 
significant
-
Not 
significant
Very 
significant
Very 
significant
Not 
significant
Significant
Very 
significant
Fig. 18  Relative feature importance for clinical-to-kinetic 
parameter mapping. Heatmap of normalized permutation 
importance values, highlighting the dependence of the ANN-
PSO on specific hematologic, metabolic, and clinical inputs
 
1 3
41
Page 41 of 49 
285

---

## Page 42
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
the cost of reduced interpretability, as dimensionality reduction can obscure the physiological role of individual 
variables in thrombin generation and RVTE prediction.
The ANN-GWO model achieved strong classification performance, with AUC = 0.89455, TPR = 0.933, and 
TNR = 0.89 on the independent test set. Reported AUC values in the literature vary widely, from moderate (AUC 
= 0.69 with DT [65]) to near-perfect (AUC = 0.9973 with ANN [23]). More recent ANN-based approaches 
typically report AUC values above 0.85 [23, 36], often supported by dimensionality reduction methods such as 
PCA or PLS. Although the ANN-GWO achieved a slightly lower AUC, it provided a balanced trade-off between 
sensitivity and specificity, in contrast to the inflated TPR = 1.0 commonly reported in prior studies [20, 23, 36], 
which may suggest overfitting or limited generalizability. Unlike purely data-driven models, the proposed frame­
work integrates mechanistic surrogate modeling with metaheuristic optimization, enhancing interpretability and 
translational relevance.
Beyond discrimination, calibration analysis, decision curve analysis, and threshold stability analyses collec­
tively demonstrated the clinical robustness of swarm-based optimizers. GWO and PSO showed superior agree­
ment between predicted and observed risks, consistently higher net benefit across clinically relevant thresholds, 
and broad Youden index plateaus on the ETP scale. This plateau behavior is particularly relevant for real-world 
deployment, as it reduces sensitivity to minor threshold perturbations and enhances decision stability. Competing 
optimizers exhibited narrower stability regions or reduced net benefit, limiting their clinical reliability.
Stratified correlation and Δρ analyses indicated that RVTE recurrence is characterized not by a structural 
reorganization of clinical–kinetic relationships, but rather by a selective reweighting of existing couplings. 
Erythrocyte-related indices (RBC count, hemoglobin, and hematocrit) consistently emerged as dominant modu­
lators across recurrence strata and optimization frameworks, reinforcing their systemic influence on coagulation 
dynamics. In addition, age-dependent amplification of factor X and factor V activation suggests sensitization of 
key nodes within the prothrombinase complex in recurrent patients. This age-related kinetic reinforcement is 
biologically plausible and consistent with established hemostatic changes observed in aging populations. Plasma 
concentrations of several coagulation factors—especially factors V and X—have been shown to increase with 
age, accompanied by enhanced thrombin generation and platelet activation, collectively contributing to a pro­
thrombotic phenotype [66, 67]. Moreover, population-based studies demonstrate that biomarkers reflecting fac­
tor Xa activity and prothrombin conversion, such as prothrombin fragment F1 + 2, rise progressively with age, 
indicating increased basal thrombin generation in older individuals [68]. The convergence between these clinical 
observations and the model-derived amplification of kinetic parameters for factors V and X supports the mecha­
nistic plausibility of our findings.
Permutation-importance analysis reinforced this interpretation. Although GWO and PSO distributed feature 
importance differently at the local level, both consistently identified hematologic variables, age, and Protein C as 
dominant biological drivers. GWO exhibited a more concentrated importance structure, whereas PSO distributed 
sensitivity more diffusely across clinical inputs. Despite low agreement at the entry level, both optimizers con­
verged on shared physiological domains.
Across all comparative experiments, GWO and PSO consistently achieved superior performance in final fit­
ness, discrimination, calibration, and robustness. Their superiority persisted across 30 independent stochastic runs, 
confirming that results were not attributable to favorable initialization. Friedman and Nemenyi tests demonstrated 
that both methods significantly outperformed most alternative metaheuristics, with no statistically significant 
difference between GWO and PSO. Although PSO converged more rapidly, both algorithms achieved statisti­
cally indistinguishable final solution quality and AUC values. These findings suggest that the surrogate objec­
tive landscape remains highly nonconvex and multimodal, favoring global search strategies. Notably, even after 
replacing the ODE system with a differentiable ANN surrogate, gradient-based optimizers (Adam, RMSProp, 
SGD) failed to match swarm-based performance. This underscores that differentiability alone does not guarantee 
effective optimization in complex biological systems characterized by rugged loss surfaces and multiple local 
minima. These observations are consistent with the recent literature, which shows that swarm-based metaheuris­
tic algorithms can outperform traditional gradient-based methods in training ANNs and other high-dimensional, 
1 3
42
285 
Page 42 of 49

---

## Page 43
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
nonlinear problems due to their enhanced capacity to avoid local minima and to explore rugged, multimodal 
search spaces through demographic and adaptive search mechanisms [69]. Additionally, systematic reviews of 
optimization methods in ML underscore that population-based, gradient-free strategies such as PSO and GWO 
are particularly effective in complex nonconvex landscapes where gradient descent techniques may struggle to 
escape local optima or to provide reliable global search direction [70, 71].
Direct comparison with alternative surrogate models confirmed the superiority of ANN-GWO over all MOA-
based approaches tested with GA, ACO, FA, BA, and WOA, except for CatBoost-BA. ANN-GWO also showed 
statistically comparable performance to surrogate models optimized with PSO, suggesting that GWO and PSO 
are particularly effective metaheuristics in this context. No statistically significant improvements were observed 
when comparing GWO to other ML algorithms. These findings provide practical guidance on the application of 
GWO and PSO as robust optimizers, and of ANN and boosting-based ML methods as efficient surrogates to ODE 
systems in hybrid frameworks.
The proposed approach offers substantial practical potential for advancing hybrid mechanistic–data-driven 
modeling in clinical settings. The original ANN–ODE framework [23] was limited by high computational costs, 
restricting the exploration of features and kinetic parameter selection. Replacing the ODE with ANN-GWO 
reduced computation time by over 99%, effectively removing this barrier. This efficiency gain enables the use of 
refined selection strategies, such as backward and forward elimination, to identify clinical features and kinetic 
parameters that maintain accuracy while reducing complexity and enhancing interpretability. Moreover, the 
framework facilitates investigation of how clinical variables (e.g., age, comorbidities, hemostatic biomarkers) 
qualitatively and quantitatively influence kinetic parameters, and how these, in turn, affect thrombin generation, 
ETP, and ultimately RVTE risk.
Several limitations should be acknowledged. First, only a single ODE-based coagulation model was examined. 
Given structural and kinetic differences across alternative coagulation models, such as models of Hockin et al. 
[72] and Jones and Mann [73], it remains uncertain whether surrogate replacement generalizes universally. Future 
work should evaluate robustness across multiple mechanistic frameworks.
Second, MOA hyperparameters were adopted from commonly used literature settings rather than systemati­
cally tuned. Because hyperparameter configurations strongly influence convergence dynamics and solution qual­
ity [74, 75], future studies should perform systematic sensitivity analyses to provide a more rigorous comparison 
of algorithmic robustness.
Third, the surrogate was designed to predict a single scalar summary of thrombin generation (ETP) rather than 
the full time-resolved thrombin concentration curve. ETP is clinically interpretable and mechanistically grounded 
as a global measure of thrombin-generating capacity. It reflects the integrated balance between pro- and anticoag­
ulant forces in plasma, distinguishes hypo- and hypercoagulable states in clinical populations [76], and has been 
associated with both initial and RVTE risk [77, 78]. These findings support the use of ETP as a clinically mean­
ingful surrogate marker of coagulation perturbation in both mechanistic modeling and risk stratification contexts.
However, reliance on this scalar endpoint inevitably discards temporal information embedded in the thrombin 
generation curve. Dynamic features such as peak thrombin, lag time, time-to-peak, post-peak decay behavior, 
and maximum thrombin generation rate represent distinct physiological phases of initiation, amplification, and 
inhibition within the coagulation cascade. Incorporating these time-dependent characteristics in future surrogate 
frameworks may provide complementary mechanistic insight and potentially enhance discrimination and bio­
logical interpretability beyond what can be achieved with ETP alone.
The focus on ETP in the present study was motivated by its strong clinical relevance and interpretability. 
Nevertheless, future investigations should directly compare scalar ETP-based surrogates with multi-output or 
time-series architectures. Potential extensions include (i) joint prediction of multiple curve-derived metrics (e.g., 
peak thrombin and lag time), (ii) vector-valued surrogate models that simultaneously approximate several kinetic 
summaries, or (iii) sequence-based neural architectures capable of reconstructing the full thrombin generation 
curve. Moreover, incorporating experimental thrombin generation assay data would strengthen the biological 
1 3
43
Page 43 of 49 
285

---

## Page 44
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
grounding of the framework by enabling training and validation against empirically observed full-curve dynam­
ics rather than relying solely on theoretical ODE-derived outputs.
Accordingly, the present findings demonstrate the feasibility and robustness of ANN surrogate modeling for 
scalar ETP prediction, while highlighting multi-output and full-curve modeling as important next steps toward 
enhanced mechanistic resolution and clinical translation.
Finally, the substantial computational acceleration achieved here enables a far greater number of exploratory 
and validation experiments within feasible time constraints. This makes iterative feature selection and kinetic 
parameter refinement strategies practically viable, increasing the potential to validate and refine the relationships 
among clinical features, kinetic parameters, ETP, and clinical outcomes. This enhanced experimental flexibility 
strengthens both methodological rigor and translational applicability of the proposed hybrid framework.
5  Conclusion
This study demonstrates that computationally intensive ODE-based coagulation models can be effectively 
replaced by ANN surrogates within hybrid optimization frameworks for RVTE prediction, yielding substantial 
efficiency gains without compromising predictive fidelity. Among the 14 ML algorithms evaluated, the ANN sur­
rogate provided the best balance between accuracy and computational speed, reducing runtime by more than 99% 
while maintaining a relative accuracy of 97.97% under GWO optimization. This acceleration removes a major 
practical barrier associated with repeated ODE evaluations in high-dimensional optimization settings.
Comparative analyses across ML models and MOAs revealed that swarm-based optimizers, particularly GWO 
and PSO, consistently achieved superior performance in terms of fitness, discrimination, calibration, and robust­
ness. Their effectiveness persisted across multiple stochastic runs and statistical comparisons, highlighting their 
suitability for navigating the highly nonconvex and multimodal objective landscape inherent to the hybrid frame­
work. While ANN-GWO was statistically superior to most alternative MOA combinations and comparable only 
to ANN-PSO, no significant performance differences were observed between ANN-GWO and boosting-based 
models optimized with GWO. Nonetheless, the ANN surrogate achieved markedly lower RMSE values (below 
0.3 in both training and testing sets) and lower residuals, confirming its strong approximation capacity relative to 
other ML approaches.
The optimal ANN architecture (41-7-10-1 neurons with tansig–logsig–purelin activation functions) provided 
a compact yet expressive representation of the underlying kinetic dynamics. Importantly, the synergy between 
ANN surrogate and swarm-based optimizers enabled reliable patient-specific risk stratification while preserving 
mechanistic interpretability through kinetic parameter analysis. Beyond predictive performance, the surrogate 
framework has the potential to facilitate deeper exploration of clinical–mechanistic relationships, sensitivity pat­
terns, and robustness under stochastic variability, analyses that would be computationally prohibitive with the 
original ODE solver.
Overall, the findings support a practical and scalable strategy for the proposed hybrid mechanistic–data-driven 
modeling: replace stiff ODE systems with high-fidelity ANN surrogates and perform optimization using robust 
swarm-based algorithms such as GWO or PSO. Although developed in the context of RVTE prediction, the pro­
posed surrogate-assisted optimization framework has broader applicability to other computationally intensive 
models. The approach can be extended to related hemostatic conditions, including broader VTE phenotypes and 
inherited bleeding disorders such as hemophilia, where dynamic coagulation modeling plays a central role.
Importantly, the substantial computational acceleration achieved in this study enables more intensive and 
systematic model development strategies. Iterative feedforward and feedback procedures for clinical feature 
selection and kinetic parameter refinement become computationally feasible, allowing deeper exploration of the 
relationships between clinical variables and kinetic parameters, as well as their joint influence on ETP and clini­
cal outcomes. This expanded modeling capacity enhances both mechanistic insight and translational potential, 
supporting more refined and clinically informative hybrid modeling frameworks.
1 3
44
285 
Page 44 of 49

---

## Page 45
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Supplementary Information  The online version contains supplementary material available at ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​0​0​
5​2​1​-​0​2​6​-​1​2​0​4​7​-​6.
Acknowledgements  We want to express our gratitude to the CNPq, FAPESP and CAPES. This study was supported by 
Conselho Nacional de Desenvolvimento Científico e Tecnológico (Brazilian National Council for Scientific and Techno­
logical Development, CNPq), grant #164134/2022-0, Fundação de Amparo à Pesquisa do Estado de São Paulo (São Paulo 
Research Foundation, FAPESP), grant #2016/14172-6 and #08/57860-3.
Author contributions  The first author contributed to model development, data analysis, the proposed methodology, and the 
initial draft. All authors provided feedback on earlier versions of the manuscript and contributed to the final text. The last 
three authors also provided supervision and funding. All authors read and approved the final manuscript.
Funding  The Article Processing Charge (APC) for the publication of this research was funded by the Coordenação de 
Aperfeiçoamento de Pessoal de Nível Superior - Brasil (CAPES) (ROR identifier: 00x0ma614). The research leading to 
these results received funding from CNPq grant #164134/2022-0, and FAPESP grants #2016/14172-6 and #08/57860-3.
Data availability  The data are not publicly available because they contain information that could compromise the privacy 
of research participants.
Declarations
Conflict of interest  The authors have no competing interests to declare that are relevant to the content of this article.
Ethical approval  Ethical approval of the patient data used in this work was obtained and approved by the Comitê de Ética 
da Universidade Federal de Campinas (Approval number: 88970218.0.0000.5404).
Open Access 
 This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, 
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The 
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your 
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly 
from the copyright holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​n​s​.​o​r​g​/​l​i​c​e​n​s​e​s​/​b​y​/​4​.​0​/.
References
	 1.	Lichota A, Szewczyk EM, Gwozdzinski K (2020) Factors affecting the formation and treatment of thrombosis by natural 
and synthetic compounds. Int J Mol Sci 21:7975
	 2.	Guanella R, Ducruet T, JohrI M et al (2011) Economic burden and cost determinants of deep vein thrombosis during 2 
years following diagnosis: a prospective evaluation. J Thromb Haemost 9:2397–2405. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​1​1​/​j​.​1​5​3​8​-​7​8​
3​6​.​2​0​1​1​.​0​4​5​1​6​.​x
	 3.	Oleksiuk-Bójko M, Lisowska A (2023) Venous thromboembolism: Why is it still a significant health problem? Adv Med 
Sci 68:10–20. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​a​d​v​m​s​.​2​0​2​2​.​1​0​.​0​0​2
	 4.	Streiff MB (2015) Predicting the risk of recurrent venous thromboembolism (VTE). J Thromb Thrombolysis 39:353–
366. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​1​2​3​9​-​0​1​5​-​1​1​8​8​-​4
	 5.	Kyrle PA, Rosendaal FR, Eichinger S (2010) Risk assessment for recurrent venous thrombosis. Lancet 376:2032–2039. ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​S​0​1​4​0​-​6​7​3​6​(​1​0​)​6​0​9​6​2​-​2
	 6.	Khorana AA, Kuderer NM, Culakova E et al (2008) Development and validation of a predictive model for chemotherapy-
associated thrombosis. Blood 111:4902–4907. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​8​2​/​b​l​o​o​d​-​2​0​0​7​-​1​0​-​1​1​6​3​2​7
	 7.	Caprini JA (2005) Thrombosis risk assessment as a guide to quality patient care. Dis Mon 51:70–78
	 8.	Wells PS, Anderson DR, Bormanis J et al (1997) Value of assessment of pretest probability of deep-vein thrombosis in 
clinical management. Lancet 350:1795–1798
	 9.	Wells PS, Ginsberg JS, Anderson DR et al (1998) Use of a clinical model for safe management of patients with suspected 
pulmonary embolism. Ann Intern Med 129:997–1005. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​7​3​2​6​/​0​0​0​3​-​4​8​1​9​-​1​2​9​-​1​2​-​1​9​9​8​1​2​1​5​0​-​0​0​0​0​2
1 3
45
Page 45 of 49 
285

---

## Page 46
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
	10.	Louzada ML, Carrier M, Lazo-Langner A et al (2012) Development of a clinical prediction rule for risk stratification of 
recurrent venous thromboembolism in patients with cancer-associated venous thromboembolism. Circulation 126:448–
454
	11.	Tosetto A, Iorio A, Marcucci M et al (2012) Predicting disease recurrence in patients with previous unprovoked venous 
thromboembolism: a proposed prediction score (DASH). J Thromb Haemost 10:1019–1025. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​1​1​/​j​.​1​5​
3​8​-​7​8​3​6​.​2​0​1​2​.​0​4​7​3​5​.​x
	12.	Eichinger S, Heinze G, Jandeck LM, Kyrle PA (2010) Risk assessment of recurrence in patients with unprovoked deep 
vein thrombosis or pulmonary embolism: the Vienna prediction model. Circulation 121:1630–1636. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​
1​6​1​/​C​I​R​C​U​L​A​T​I​O​N​A​H​A​.​1​0​9​.​9​2​5​2​1​4
	13.	Kafeza M, Shalhoub J, Salooja N et al (2017) A systematic review of clinical prediction scores for deep vein thrombosis. 
Phlebology 32:516–531. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​7​7​/​0​2​6​8​3​5​5​5​1​6​6​7​8​7​2​9
	14.	Mulder FI, Candeloro M, Kamphuisen PW et al (2019) The Khorana score for prediction of venous thromboembolism in 
cancer patients: a systematic review and meta-analysis. Haematologica 104:1277–1287. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​2​4​/​h​a​e​m​a​t​
o​l​.​2​0​1​8​.​2​0​9​1​1​4
	15.	Stevens H, Peter K, Tran H, McFadyen J (2020) Predicting the Risk of Recurrent Venous Thromboembolism: Current 
Challenges and Future Opportunities. J Clin Med 9. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​j​c​m​9​0​5​1​5​8​2
	16.	Chen R, Petrazzini BO, Malick WA et al (2024) Prediction of Venous Thromboembolism in Diverse Populations Using 
Machine Learning and Structured Electronic Health Records. Arterioscler Thromb Vasc Biol 44:491–504. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​
g​/​1​0​.​1​1​6​1​/​A​T​V​B​A​H​A​.​1​2​3​.​3​2​0​3​3​1
	17.	Meng L, Wei T, Fan R et al (2022) Development and validation of a machine learning model to predict venous 
thromboembolism among hospitalized cancer patients. Asia-Pacific J Oncol Nurs 9:100128. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​a​p​
j​o​n​.​2​0​2​2​.​1​0​0​1​2​8
	18.	Danilatou Dimitrios, Kostoulas T, Douketis JVD (2024) Machine Learning-Based Predictive Models for Patients with 
Venous Thromboembolism: A Systematic Review. Thromb Haemost 124:1040–1052. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​5​5​/​a​-​2​2​9​9​-​4​7​
5​8
	19.	Martins TD, Annichino-Bizzacchi JM, Romano AVC, Maciel Filho R (2020) Artificial neural networks for prediction of 
recurrent venous thromboembolism. Int J Med Inf 141:104221. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​i​j​m​e​d​i​n​f​.​2​0​2​0​.​1​0​4​2​2​1
	20.	Martins TD, Martins SD, Montalvão S et al (2024) Combining artificial neural networks and hematological data to 
diagnose Covid-19 infection in Brazilian population. Neural Comput Appl 36:4387–4399. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​0​0​5​2​
1​-​0​2​3​-​0​9​3​1​2​-​3
	21.	Martins TD, Maciel-Filho R, Montalvão SAL et al (2024) Predicting mortality of cancer patients using artificial 
intelligence, patient data and blood tests. Neural Comput Appl. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​0​0​5​2​1​-​0​2​4​-​0​9​9​1​5​-​4
	22.	Rashidi HH, Bowers KA, Reyes Gil M (2023) Machine learning in the coagulation and hemostasis arena: an overview 
and evaluation of methods, review of literature, and future directions. J Thromb Haemost 21:728–743. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​
.​1​0​1​6​/​j​.​j​t​h​a​.​2​0​2​2​.​1​2​.​0​1​9
	23.	Al Bannoud M, Martins TD, de Lima Montalvão SA et al (2025) Determination of Patient-Specific Blood Coagulation 
Kinetic Parameters via Neural Networks: Toward Thrombosis Prediction in Personalized Medicine. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​
0​0​7​/​s​1​0​4​3​9​-​0​2​5​-​0​3​8​3​7​-​5. Ann Biomed Eng
	24.	Al Bannoud M, Martins TD, de Lima Montalvão SA et al (2024) Integrating biomarkers for hemostatic disorders into 
computational models of blood clot formation: A systematic review. Math Biosci Eng 21:7707–7739. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​
3​9​3​4​/​m​b​e​.​2​0​2​4​3​3​9
	25.	Bannoud M, da Al CAM, Martins TD (2024) Applications of metaheuristic optimization algorithms in model predictive 
control for chemical engineering processes: A systematic review. Annu Rev Control 58:100973. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​
j​.​a​r​c​o​n​t​r​o​l​.​2​0​2​4​.​1​0​0​9​7​3
	26.	Kircher T, Votsmeier M (2025) Machine Learning Surrogate Models for Mechanistic Kinetics: Embedding Atom Balance 
and Positivity. J Phys Chem Lett 16:4715–4723. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​2​1​/​a​c​s​.​j​p​c​l​e​t​t​.​5​c​0​0​6​0​2
	27.	Nguyen T-U, Suk H, Liang C-P et al (2025) Using Machine Learning to Develop a Surrogate Model for Simulating 
Multispecies Contaminant Transport in Groundwater. Hydrology 12:185
	28.	Kumar T, Kumar A, Pal P (2025) Phy-ChemNODE: an end-to-end physics-constrained autoencoder-NeuralODE 
framework for learning stiff chemical kinetics of hydrocarbon fuels. Front Therm Eng Volume 5:1594443
	29.	Pawłowski T, Bokota G, Lazarou G et al (2024) Emulation of Quantitative Systems Pharmacology models to accelerate 
virtual population inference in immuno-oncology. Methods 223:118–126. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​y​m​e​t​h​.​2​0​2​3​.​1​2​.​0​0​6
	30.	Roberts C, Lara JD, Henriquez-Auba R et al (2022) Continuous-time echo state networks for predicting power system 
dynamics. Electr Power Syst Res 212:108562. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​e​p​s​r​.​2​0​2​2​.​1​0​8​5​6​2
	31.	Losada IB, Terranova N (2024) Bridging pharmacology and neural networks: A deep dive into neural ordinary differential 
equations. CPT Pharmacometrics Syst Pharmacol 13:1289–1296. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​2​/​p​s​p​4​.​1​3​1​4​9
	32.	Bräm DS, Nahum U, Schropp J et al (2024) Low-dimensional neural ODEs and their application in pharmacokinetics. J 
Pharmacokinet Pharmacodyn 51:123–140. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​9​2​8​-​0​2​3​-​0​9​8​8​6​-​4
1 3
46
285 
Page 46 of 49

---

## Page 47
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
	33.	Murugesh V, Priyadharshini M, Sharma YK et al (2025) A novel hybrid framework for efficient higher order ODE solvers 
using neural networks and block methods. Sci Rep 15:8456. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​3​8​/​s​4​1​5​9​8​-​0​2​5​-​9​0​5​5​6​-​5
	34.	Bannoud M, Al, Martins TD, de Montalvão SA L, et al (2025) Artificial intelligence in computational modeling of 
thrombosis: Bridging mechanistic insights and clinical translation. J Thromb Thrombolysis. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​1​
2​3​9​-​0​2​5​-​0​3​2​2​2​-​y
	35.	Zhu D (2007) Mathematical modeling of blood coagulation cascade: kinetics of intrinsic and extrinsic pathways in 
normal and deficient conditions. Blood Coagul fibrinolysis Int J Haemost Thromb 18:637–646. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​9​7​/​
M​B​C​.​0​b​0​1​3​e​3​2​8​2​a​1​6​7​b​b
	36.	Al Bannoud M, Martins TD, de Lima Montalvão SA et al (2025) Prediction of recurrent venous thromboembolism using 
a spatiotemporal phenomenological model and artificial neural network. Neural Comput Appl. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​
0​0​5​2​1​-​0​2​5​-​1​1​0​7​0​-​3
	37.	Danforth CM, Orfeo T, Mann KG et al (2009) The impact of uncertainty in a blood coagulation model. Math Med Biol 
26:323–336. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​9​3​/​i​m​a​m​m​b​/​d​q​p​0​1​1
	38.	Link KG, Stobb MT, Di Paola J et al (2018) A local and global sensitivity analysis of a mathematical model of coagulation 
and platelet deposition under flow. PLoS ONE 13:e0200917
	39.	Martins TD, Annichino-Bizzacchi JM, Romano AVC, Filho RM (2019) Principal Component Analysis on Recurrent 
Venous Thromboembolism. Clin Appl Thromb 25. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​7​7​/​1​0​7​6​0​2​9​6​1​9​8​9​5​3​2​3
	40.	Holland JH (1992) Genetic algorithms. Sci Am 267:66–73
	41.	Fearn Tom (2010) Particle Swarm Optimisation. NIR news 25:27. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​2​5​5​/​n​i​r​n​.​1​4​2​1
	42.	Mirjalili S, Mirjalili SM, Lewis A (2014) Grey Wolf Optimizer. Adv Eng Softw 69:46–61. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​a​d​v​
e​n​g​s​o​f​t​.​2​0​1​3​.​1​2​.​0​0​7
	43.	Dorigo M, Maniezzo V, Colorni A (1996) Ant system: optimization by a colony of cooperating agents. IEEE Trans Syst 
Man Cybern Part B 26:29–41. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​3​4​7​7​.​4​8​4​4​3​6
	44.	Yang X-S (2010) Firefly algorithm, stochastic test functions and design optimisation. Int J bio-inspired Comput 2:78–84
	45.	Yang X-S (2010) In: González JR, Pelta DA, Cruz C et al (eds) A New Metaheuristic Bat-Inspired Algorithm BT - Nature 
Inspired Cooperative Strategies for Optimization (NICSO 2010). Springer Berlin Heidelberg, Berlin, Heidelberg, pp 
65–74
	46.	Akay B, Karaboga D (2012) Artificial bee colony algorithm for large-scale problems and engineering design optimization. 
J Intell Manuf 23:1001–1014. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​8​4​5​-​0​1​0​-​0​3​9​3​-​4
	47.	Mirjalili S, Lewis A (2016) The Whale Optimization Algorithm. Adv Eng Softw 95:51–67. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​a​d​v​
e​n​g​s​o​f​t​.​2​0​1​6​.​0​1​.​0​0​8
	48.	Robbins H, Monro S (1951) A stochastic approximation method. Ann Math Stat 22(3):400–407
	49.	Tieleman T, Hinton G (2012) Lecture 6.5-rmsprop: Divide the gradient by a running average of its recent magnitude. 
COURSERA Neural networks Mach Learn 4:26
	50.	Kingma DP (2014) Adam: A method for stochastic optimization. arXiv Prepr arXiv14126980. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​
a​r​X​i​v​.​1​4​1​2​.​6​9​8​0
	51.	Friedman M (1937) The Use of Ranks to Avoid the Assumption of Normality Implicit in the Analysis of Variance. J Am 
Stat Assoc 32:675–701. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​8​0​/​0​1​6​2​1​4​5​9​.​1​9​3​7​.​1​0​5​0​3​5​2​2
	52.	Friedman M (1940) A Comparison of Alternative Tests of Significance for the Problem of m Rankings. Ann Math Stat 
11:86–92
	53.	Veček N, Črepinšek M, Mernik M (2017) On the influence of the number of algorithms, problems, and independent runs 
in the comparison of evolutionary algorithms. Appl Soft Comput 54:23–45. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​a​s​o​c​.​2​0​1​7​.​0​1​.​0​1​1
	54.	Jia B-B, Liu J-Y, Zhang M-L (2025) Pairwise statistical comparisons of multiple algorithms. Front Comput Sci 19:1–3
	55.	Bannoud M, Al, Mendes JL, Sacay RS et al (2026) Machine Learning forecasting of dengue in São Paulo using virtual data 
augmentation and urban incident predictors: Addressing the exceptional surge of cases in 2024. Acta Trop 275:107992. ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​a​c​t​a​t​r​o​p​i​c​a​.​2​0​2​6​.​1​0​7​9​9​2
	56.	Marchetti M, Giaccherini C, Masci G et al (2020) Thrombin generation predicts early recurrence in breast cancer patients. 
J Thromb Haemost 18:2220–2231. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​1​1​/​j​t​h​.​1​4​8​9​1
	57.	Wang H, Rosendaal FR, Cushman M, van Hylckama Vlieg A (2021) D‐dimer, thrombin generation, and risk of a first 
venous thrombosis in the elderly. Res Pract Thromb Haemost 5:. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​2​/​r​t​h​2​.​1​2​5​3​6
	58.	van Hylckama Vlieg A, Baglin CA, Luddington R, et al (2015) The risk of a first and a recurrent venous thrombosis 
associated with an elevated D‐dimer level and an elevated thrombin potential: results of the THE‐VTE study. J Thromb 
Haemost 13:1642–1652. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​1​1​/​j​t​h​.​1​3​0​4​3
	59.	Lundbech M, Krag AE, Christensen TD, Hvas A-M (2020) Thrombin generation, thrombin-antithrombin complex, and 
prothrombin fragment F1 + 2 as biomarkers for hypercoagulability in cancer patients. Thromb Res 186:80–85. ​h​t​t​p​s​:​/​/​d​o​
i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​t​h​r​o​m​r​e​s​.​2​0​1​9​.​1​2​.​0​1​8
	60.	Luna-Záizar H, González-Moncada AI, Padilla-López EL et al (2015) Thrombin generation and international normalized 
ratio in inherited thrombophilia patients receiving thromboprophylactic therapy. Thromb Res 136:1291–1298. ​h​t​t​p​s​:​/​/​d​o​
i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​t​h​r​o​m​r​e​s​.​2​0​1​5​.​1​0​.​0​2​6
1 3
47
Page 47 of 49 
285

---

## Page 48
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
	61.	Tariq A, Uzun B, Deliktaş B, Yaylı MÖ (2024) An investigation on ensemble machine learning algorithms for nonlinear 
stability response of a two-dimensional FG nanobeam. J Brazilian Soc Mech Sci Eng 46:556. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​4​
0​4​3​0​-​0​2​4​-​0​5​0​9​3​-​5
	62.	Bannoud MA, Gomes BP, de Abdalla MC SP, et al (2024) Mathematical modeling of drying kinetics of ground Açaí 
(Euterpe oleracea) kernel using artificial neural networks. Chem Pap 78:1033–1054. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​1​6​9​6​-​0​2​
3​-​0​3​1​4​2​-​2
	63.	Bannoud M, Al, Ferreira PHN, de Andrade RR, da Silva CAM (2025) Control of an integrated first and second-generation 
continuous alcoholic fermentation process with cell recycling using model predictive control. Chem Eng Commun 
212:521–544. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​8​0​/​0​0​9​8​6​4​4​5​.​2​0​2​4​.​2​4​1​7​9​0​1
	64.	Singh N, Singh P (2021) Exploring the effect of normalization on medical data classification. In: 2021 International 
Conference on Artificial Intelligence and Machine Vision (AIMV). pp 1–5
	65.	Muñoz AJ, Souto JC, Lecumberri R et al (2023) Development of a predictive model of venous thromboembolism 
recurrence in anticoagulated cancer patients using machine learning. Thromb Res 228:181–188. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​
j​.​t​h​r​o​m​r​e​s​.​2​0​2​3​.​0​6​.​0​1​5
	66.	Favaloro EJ, Franchini M, Lippi G (2014) Aging hemostasis: changes to laboratory markers of hemostasis as we age - a 
narrative review. Semin Thromb Hemost 40:621–633. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​5​5​/​s​-​0​0​3​4​-​1​3​8​4​6​3​1
	67.	Akrivou D, Perlepe G, Kirgou P et al (2022) Pathophysiological Aspects of Aging in Venous Thromboembolism: An 
Update. Med (B Aires 58:1078
	68.	Bauer KA, Weiss LM, Sparrow D et al (1987) Aging-associated changes in indices of thrombin generation and protein C 
activation in humans. Normative Aging Study. J Clin Invest 80:1527–1534. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​7​2​/​J​C​I​1​1​3​2​3​8
	69.	Eker E, Kayri M, Ekinci S, Izci D (2023) Comparison of Swarm-based Metaheuristic and Gradient Descent-based 
Algorithms in Artificial Neural Network Training. ADCAIJ Adv Distrib Comput Artif Intell J 12:e29969. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​
/​1​0​.​1​4​2​0​1​/​a​d​c​a​i​j​.​2​9​9​6​9
	70.	Liu X, Qi H, Jia S et al (2025) Recent Advances in Optimization Methods for Machine Learning: A Systematic Review. 
Mathematics 13:2210
	71.	Shaikh MS, Raj S, Zheng G et al (2025) Applications, classifications, and challenges: a comprehensive evaluation of 
recently developed metaheuristics for search and analysis. Artif Intell Rev 58:390. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​4​6​2​-​0​2​5​-​1​
1​3​7​7​-​6
	72.	Hockin MF, Jones KC, Everse SJ, Mann KG (2002) A model for the stoichiometric regulation of blood coagulation. J 
Biol Chem 277:18322–18333. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​7​4​/​j​b​c​.​M​2​0​1​1​7​3​2​0​0
	73.	Jones KC, Mann KG (1994) A model for the tissue factor pathway to thrombin. II. A mathematical simulation. J Biol 
Chem 269:23367–23373
	74.	Lee D, Noh S, Kim J, Lee S (2025) Efficient Hyperparameter Optimization Using Metaheuristics for Machine Learning 
in Truss Steel Structure Cross-Section Prediction. Buildings 15:2791
	75.	Gu J, Zhang Y, Li C et al (2026) Hybrid Machine Learning with Metaheuristic Optimization for Predicting Peak Particle 
Velocity in Open-Pit Mines. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​4​2​4​6​1​-​0​2​5​-​0​1​3​5​9​-​1. Mining, Metall Explor
	76.	Chantarangkul V, Clerici M, Bressi C et al (2003) Thrombin generation assessed as endogenous thrombin potential in 
patients with hyper- or hypo-coagulability. Haematologica 88:547–554
	77.	Tripodi A, Martinelli I, Chantarangkul V et al (2007) The endogenous thrombin potential and the risk of venous 
thromboembolism. Thromb Res 121:353–359. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​t​h​r​o​m​r​e​s​.​2​0​0​7​.​0​4​.​0​1​2
	78.	Eichinger S, Hron G, Kollars M, Kyrle PA (2008) Prediction of Recurrent Venous Thromboembolism by Endogenous 
Thrombin Potential and D-Dimer. Clin Chem 54:2042–2048. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​3​7​3​/​c​l​i​n​c​h​e​m​.​2​0​0​8​.​1​1​2​2​4​3
Publisher’s note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional 
affiliations.
1 3
48
285 
Page 48 of 49

---

## Page 49
Neural Computing and Applications (2026) 38:285
https://doi.org/10.1007/s00521-026-12047-6
Authors and Affiliations
Mohamad Al Bannoud1,4  · Tiago Dias Martins2 · 
Silmara Aparecida de  Lima Montalvão3,4 · Joyce Maria Annichino-Bizzacchi3,4 · 
Rubens Maciel Filho1,4 · Maria Regina Wolf Maciel1
	
 Mohamad Al Bannoud
mohamad.bannoud@unifesp.br
1	
School of Chemical Engineering, Laboratory of Optimization, Design, and Advanced Control, Universidade 
Estadual de Campinas, Campinas, Campinas, São Paulo, Brazil
2	
Departamento de Engenharia Química, Instituto de Ciências Ambientais, Químicas e Farmacêuticas, Universidade 
Federal de São Paulo, Diadema, São Paulo, Brazil
3	
Hematology and Hemotherapy Center, University of Campinas/ Hemocentro-Unicamp, Instituto Nacional de 
Ciência e Tecnologia do Sangue, Campinas, São Paulo, Brazil
4	
Centro de Doenças Tromboembólicas (CCT), Centro de Hematologia e Hemoterapia (HEMOCENTRO), 
Universidade Estadual de Campinas, Campinas, São Paulo, Brazil
1 3
49
Page 49 of 49 
285

---
