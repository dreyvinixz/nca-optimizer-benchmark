# CatGrass: a feature engineering framework to forecast the seismic response of low-rise RC frames using CatBoost algorithm integrated with grasshopper optimization

**Year**: 2025 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-025-11387-z

---

## Page 1
ORIGINAL ARTICLE
CatGrass: a feature engineering framework to forecast
the seismic response of low-rise RC frames using
CatBoost algorithm integrated with grasshopper
optimization
Ahmet Demir1
• Selçuk Demir1
• Emrehan Kutlug Sahin1
Received: 29 January 2025 / Accepted: 20 May 2025 / Published online: 17 June 2025
 The Author(s) 2025
Abstract
Predicting the maximum drift ratio (MDR) of reinforced concrete frames is a critical parameter in the design,
evaluation, and rehabilitation of reinforced concrete structures. This study aims to investigate the prediction of the
MDR of regular and irregular low-rise reinforced concrete frames using the grasshopper optimization algorithm
(GOA) optimized CatBoost algorithm (i.e., CatGrass). For this purpose, a total of 2,300 ground motion records
were utilized, and the dataset includes 20 different intensity measures (IMs), spectral acceleration values at the
ﬁrst mode period Sa(T1), as well as the results of nonlinear time history analyses for each record. Also, several
feature engineering techniques (advanced ML pipeline) were applied including outlier detection using the
multivariate outlier detection and replacement method (i.e., outForest), missing data imputation with the remove
missing values function (i.e., na.omit), data transformation using the Box-Cox method, and feature selection via
the Chi-square method. To evaluate model performance, ﬁve statistical evaluation metrics, namely R2, RMSE,
MSE, MAE, and MAPE were employed. For comparison, the prediction results of the CatGrass models were
evaluated against those of the raw CatBoost model (benchmark ML pipeline) and some popular ML algorithms,
which do not use any feature engineering techniques. The results demonstrated that the proposed CatGrass model
achieved a higher R2 value (exceeding 0.99) and lower MSE, RMSE, MAE, and MAPE values compared to the
raw CatBoost model and the other ML models in predicting the MDR. This study conﬁrms the effectiveness of
the proposed novel CatGrass model, establishing it as a computationally efﬁcient, time-saving, and reliable tool
for seismic design and assessment of RC frames.
Keywords CatBoost  Feature engineering  Grasshopper optimization  Machine learning  Maximum drift ratio 
RC frames
1 Introduction
Earthquakes are one of the most important natural disasters, causing both casualties and damage to structures.
Every year, numerous major earthquakes occur worldwide, leading to serious socio-economic losses. The extent
of casualties and damage to structures that result from an earthquake depend on factors such as the building stock,
the seismic behavior of the structures, and the properties of the ground shaking. For these reasons, the seismic
assessment of the structures is of the utmost importance in earthquake engineering. Seismic assessment of low-
Neural Computing and Applications (2025) 37:18425–18447
https://doi.org/10.1007/s00521-025-11387-z
123
Neural Computing and Applications (2025) 37:18425–18447

---

## Page 2
and mid-rise reinforced concrete (RC) frame structures is particularly crucial because they build approximately
75% of the total building stock in Tu¨rkiye and are generally built for residential and school purposes. Addi-
tionally, the ratio of low- to mid-rise such as residential and school buildings to all buildings is also high
worldwide [9, 55, 69].
In recent decades, for the seismic design, evaluation, and rehabilitation of low- and mid-rise buildings, the
analysis method of nonlinear time history analysis (NTA) of structures has become a common analysis method
due to advances in the processing power of computers and the availability of ground motion (GM) records from
the database [1, 2]. With NTAs, target response parameters of the structures such as maximum and interstory
displacement, residual displacement, and rotation of the structure’s members can be found more realistic (Pri-
estley 2007; [64]). Different seismic codes such as EUROCODE-8 (EC8)[26], ASCE 07–16 [6], and TBEC [78]
contain relatively similar conditions for performing NTAs. In these codes, artiﬁcial, synthetic, and real GMs
downloaded from the database can be used. In addition, the mean of the structural response parameter can be used
for design and/or evaluation of structures if more than seven GM records are used. It should be noted that the
selection of the GM records can signiﬁcantly affect the target response parameters of the buildings. Therefore, the
selection of the GM records for NTA is a crucial step for the design and/or evaluation of the buildings.
It is also worth noting that the GM intensity measures (IMs) are important parameters for estimating target
response parameters. Previous studies have shown a strong correlation between target response parameters and
IMs [45, 18, 61, ]). For example, Kostinakis et al. [45] investigated the correlation between mid-rise RC buildings
and nineteen widely used IMs. In their study, four different RC buildings were considered and 64 bidirectional
ground motions using for NTA. The analysis results indicated that the spectral acceleration at the fundamental
period Sa(T1) of the buildings has the strongest correlation with the buildings damage. Conversely, there is a
medium or poor correlation between the majority of IMs and overall building damage index. Meral [55]
investigated the correlation between IMs and energy demands for low-rise RC buildings such as 4- and 7-story
residential buildings without shear walls. The study used 20 different IMs and 44 strong GM records. IMs
parameters related to velocity and acceleration showed stronger correlations than those related to frequency and
displacement.
It should be noted that the NTAs of buildings provides a more comprehensive and accurate assessment of
target response parameters. However, this analysis method is more complex and time-consuming especially for
two- or three-dimensional analysis of buildings [18, 32, 36]. Therefore, researchers have needed simpler and less
time-consuming computational tools for seismic assessment of the buildings. Eventually, machine learning (ML)
algorithms have been applied widely in recent years for seismic assessment of the buildings. In addition, ML
algorithm was used also in different areas of civil and earthquake engineering areas. For example, there is
extensive research on the use of ML algorithms in civil and earthquakes engineering areas such as seismic
damage and performance assessment of buildings ([19, 22, 39, 44, 46, 59]), liquefaction potential [20, 71],
damage classiﬁcation [52, 66], compressive strength of concrete material [63, 83], and prediction of the ﬁrst
periods of buildings [56, 80]. Finally, many researchers have also provided state-of-the-art reviews on structural
design, performance assessment, classiﬁcation, and other aspects of structural engineering [3, 38, 76].
Several studies in literature have investigated predicting the seismic target response of the structures using ML
algorithms [7, 8, 19, 22, 24, 34, 42, 60]. For instance, Asgarkhani et al. [7] investigated the prediction of
maximum interstory drift, maximum residual interstory drift, and maximum roof interstory drift demands using
stacked ML algorithm. NTAs and incremental dynamic analysis (IDAs) were performed for 2- to 12-story
buckling-restrained brace frames. Additionally, 78 far-ﬁeld GMs were used for analysis. The study considered
various ML models, including random forest (RF) [49], bagging regressor (BR) [13], extra-trees regressor (ETR)
[31], artiﬁcial neural networks (ANNs) [79], recurrent neural networks (RNNs) [27], gradient boosting machine
(GBM) [29], extreme gradient boosting (XGBoost) [15], and the proposed stacked ML algorithm. The analysis
results indicated that the proposed ML method could predict seismic response parameters with high accuracy.
Recently, Noureldin et al. [60] predicted the seismic performance of low- to mid-rise frame buildings, taking into
account soil-structure interaction (SSI). The methodology used in the study considers different ML techniques to
123
Neural Computing and Applications (2025) 37:18425–18447
18426
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 3
achieve highest prediction accuracy for seismic demands. In addition, the framework also considered two dif-
ferent types of structural irregularities: mass and stiffness. Another study conducted by [19, 22], utilized advanced
tree-based ML methods to predict the structural response (i.e., maximum drift ratio) of mid-rise RC frames with
structural irregularities. The study employed different data preprocessing techniques such as missing data
imputation using RF and feature selection using Hill Climbing [70]. According to analysis results, RF constantly
performed better than other ML models for all RC frames.
Recently, ML has been evolving at an incredible development, leading to signiﬁcant theoretical advancements
and various applications across various domains [77]. One of the key areas of focus in this ﬁeld is optimization,
which has become a major point of interest for researchers. Optimization plays a crucial role in ﬁne-tuning ML
models, and their importance is efforts to develop more effective and efﬁcient methods. As is known, some ML
algorithms such as tree-based ML algorithms contain many hyperparameters that strongly affect the model’s
prediction accuracy [28]. Hence, employing an optimization algorithm to properly adjust these hyperparameters is
an important task [11, 21, 35]. Various optimization algorithms have been proposed for this purpose, including
particle swarm optimization (PSO) [43], genetic algorithm (GA) [30], grasshopper optimization algorithm (GOA)
[73], differential evolution (DE) [75], wolf-bird optimizer (WBO) [10], symbiotic organisms search (SOS) [16],
whale optimization algorithm (WOA) [57], and so on. Azizi and Zhou [11] investigated an optimized ML
approach for predicting structural seismic response using WBO. In the study, GA, PSO, SOS, and WOA were
utilized for comparison. According to analysis results, the WBO algorithm provided higher accuracy prediction
than other metaheuristic approach. Another study was conducted by Demir and Sahin [21] employed the PSO
algorithm for hyperparameter optimization of the gradient boosting models, speciﬁcally PSO-XGBoost, PSO-
LightGBM, and PSO-CatBoost. In this study, the analysis results with the PSO optimized models were compared
to other models which used default parameters. The results indicated that the PSO algorithm achieved higher
prediction accuracy with optimized models compared to those using default parameters models. In addition to the
above studies, GOA presented by Saremi et al. [73] was also used to feature selection problems in the literature
for the different areas of sciences [4, 40, 41, 51]. Ibrahim et al. [40] studied support vector machines (SVM) by
using several optimization algorithms, such as multiverse optimizer (MVO) [58], GOA, the ﬁreﬂy algorithm (FF)
[81], GA, and PSO to compare the analysis results. According to analysis results, GOA-SVM showed the higher
performance compared to other algorithms. Another study conducted by Kamel and Yaghoubzadeh [41], pro-
posed the feature selection method using GOA for the increase the accuracy of the results. The analysis results
indicated that using GOA for feature selection resulted in greater efﬁciency and increased the SVM algorithm’s
accuracy by 97.14%.
Despite signiﬁcant progress in using ML techniques to predict seismic demands for RC frames, the application
of these methods, particularly the CatBoost algorithm, remains relatively underexplored [33, 67, 80]. There is a
notable gap in the literature regarding the use of the CatBoost algorithm for forecasting maximum drift ratio
(MDR) speciﬁcally for low-rise RC frames. This study seeks to address this gap by conducting an initial
investigation into the effectiveness of data-driven ML techniques for predicting MDR responses in low-rise RC
frames, which have 3-story with regular (R3) and vertically irregular (IR3) frames were studied. The main
innovations of the paper can be summarized as follows:
•
Investigating the relatively unexplored application of the CatBoost algorithm to predict MDR for R3 and IR3
RC frames.
•
Introducing and applying a GOA-based optimization framework for CatBoost (CatGrass) to enhance its
predictive performance.
•
Employing an advanced feature engineering framework to optimize the CatBoost model and to improve its
predictive capabilities.
•
Enhancing the robustness and reliability of MDR predictions by reducing uncertainties in seismic demand
forecasting for RC frames.
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18427

---

## Page 4
•
Contributing to seismic design methodologies by integrating ML with optimization techniques to offer a more
precise and dependable approach to seismic demand assessment.
Moreover, the study considers the following contributions which are typically ignored in research studying
problems using ML algorithms in structural engineering domain.
•
Prediction performance of the CatGrass model was systematically compared with some popular ML
algorithms, such as RF, SVM, and XGBoost to make a more comprehensive evaluation.
•
A SHAP (SHapley Additive exPlanations) based feature importance analysis was applied to evaluate and
measure the relative importance of input features.
•
Computation costs of the CatGrass model and other ML models were evaluated to observe the trade-off
between accuracy and computational efﬁciency.
•
A statistical signiﬁcance test was employed to determine whether there is a statistical signiﬁcance between the
actual and predicted values.
2 Methodology
In this study, an advanced ML pipeline called CatGrass was employed to predict the structural response of regular
and vertically irregular 3-story RC frames. The CatBoost algorithm optimized by GOA was utilized for gener-
ation ML models using several features. These features consisted of 21 input parameters, comprising 20 different
IMs and Sa(T1), along with a target feature represented by Dmax/H (i.e., MDR). This framework incorporated an
extensive pipeline, involving data preprocessing techniques such as multivariate outlier detection and replacement
(outForest) analysis for outlier detection, remove missing values (na.omit) function for cleaning rows containing
any null entries, feature transformation with Box-Cox transformation, and feature selection through the Chi-
square method. Figure 1 presents the ML pipelines for the generated models, providing a visual summary of the
processes. The performance measurements (i.e., R2, MSE, RMSE, MAE, and MAPE) were utilized to evaluate
each ML model. Also, a benchmark ML pipeline was built using CatBoost algorithm using no feature engineering
process. The main reason for the implementation of two different ML pipelines is to observe the extent to which
feature engineering applications affect model prediction performance. It is worth noting that the conﬁguration of
the computational power executed for this study is listed in Table 1.
Fig. 1 The framework of [A] and [B] employed for model development and performance evaluation
123
Neural Computing and Applications (2025) 37:18425–18447
18428
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 5
2.1 Details of structure properties and the dataset
2.1.1 Analysis models of low-rise RC frames
The buildings stock in Tu¨rkiye and the world mostly consists of low- and medium-rise buildings. Therefore, it is
important to obtain the seismic response of these buildings for future earthquakes. In this study, low-rise RC
frames of R3 and IR3 were studied. Figure 2 shows these frames which were designed by Hatzigeorgiou and
Liolios [36]. Low-rise frames consist of the beam columns. As can be seen from Hatzigeorgiou and Liolios [36],
all frames were assumed to be designed on local soil classes B according to EC8.
Figure 2 also presents the geometrical and reinforcement properties of both beams and columns. The ﬂoor
height is 3.0 m for both low-rise frames. Dimensions of the columns and beams are 30/30 cm and 30/40 cm for
both R3 and IR3 frames, respectively. The accepted values for the concrete strength and the strength of rein-
forcements are 20 MPa and 500 MPa, respectively. Dead and live loads are equal to 20 kN/m and 10 kN/m
loading on the beams, respectively. It should be noted that self-weight of beams is not included in dead load.
Using the loading (dead, live, and self-weight), reinforcing details, and cross-sectional dimensions, all frames
were nonlinear modeled with SAP2000 [72]. Mander model [53] was used for conﬁned and unconﬁned concrete
and stress–strain models with strain hardening for steel. The lumped plastic hinges are considered, and the hinges
are assigned ends of the frame’s members at the half of the members section height for considered direction. The
ﬁrst mod period of the R3 and IR3 is found to be 0.611 s and 0.470 s.
Capacity curves were obtained using pushover analysis. In this analysis, ﬁrst mode shape is considered for
lateral load patterns and second-order effects which are known as P-D effect are also considered to obtain
capacity curves. The other details, such as assumptions of nonlinear modeling and information about capacity
curves, can be found in Demir [18]. The ratio of the base shear to calculated seismic weight of the frames which
also known as ‘‘lateral strength ratio, Fy/W’’ is calculated for both R3 and IR3 frames as 40% and 59%,
respectively.
Table 1 Conﬁguration of
the computational power
executed during the devel-
opment of the ML models
Components
Details
RAM
64 GB
Processor
4.0 GHz AMD Ryzen 9 3950X CPU
Operating system
Windows 10
Fig. 2 Properties of the RC frames for R3 and IR3 buildings
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18429

---

## Page 6
2.1.2 Ground motion records and IMs
In EC8, three different GM selection criteria are given for nonlinear dynamic analysis: (1) At least three GMs
should be used; (2) the mean of spectral acceleration values of selected GM at the T = 0.0 s should be higher than
the corresponding target spectrum (T is fundamental period of the structure); and (3) the ratio of the mean of the
selected GM spectral acceleration values to the corresponding target spectrum should be higher than the 0.90 for
between the 0.2 T and 2.0 T. In addition, mean structural response is used if at least seven GM records are used in
the time history analysis. In this study, 2300 GM records were used for calculated MDR of the R3 and IR3
frames. All GM records are obtained from Demir [18]. These GM records were downloaded from PEER database
(Ancheta et al. [1]). The magnitude, epicentral distances, and shear wave velocity properties of the GM records
are Mw [5.0, 10\ R \60, and Vs,30 are between 360 and 800 m/s which compatible with EC8 local soil class B.
The period ranges for compatibility between the mean spectra of the selected GM records and corresponding
target spectra are assumed between 0.08 s-2.50 s. Finally, scaling GM records is an important task for the
nonlinear dynamic analysis [19, 22, 62]. In this study, scaling factors are considered between 0.25 and 4.00 for
scaling GMs. The individual spectrums of the 2300 selected GMs (in shadow area), target, mean spectra of
selected GMs, and mean  0.5xSD (standard deviation) are given in Fig. 3. It is seen that the compatibility
between the mean of the selected GMs and target spectra is high. Therefore, it can be said that the mean spectra of
selected GMs meet the GM selection criteria according to EC8 conditions.
In this study, 20 different IMs and Sa values at the ﬁrst mode periods Sa(T1) for each record were obtained.
Prediction of MDR for the R3 and IR3 frames based on these IMs and Sa(T1) was investigated via ML
approaches. It should be noted that there is much research about the relationship between the IMs and the seismic
response of the buildings [18, 45, 61]. According to these studies, there is a robust correlation between the
seismic demand and the IMs. For this study, all IMs are presented in Fig. 4.
IMs show the amplitude, duration, and frequency content of the GM records. In these IMs, six amplitude
content (peak ground acceleration (PGA), peak ground velocity (PGV), peak ground displacement (PGD),
sustained maximum acceleration (SMA), sustained maximum velocity (SMV), and effective design acceleration
(EDA)) and ﬁve different amplitude and frequency content (root mean square of acceleration (ARMS), root mean
square of velocity (VRMS), root mean square of displacement (DRMS), acceleration spectrum intensity (ASI), and
velocity spectrum intensity (VSI)) were used. Furthermore, some IMs describe amplitude, frequency, and/or
duration. These are Vmax/Amax, predominant period (PP), and signiﬁcant duration (SD). Lastly, the IMs with
amplitude, frequency, and duration contents, such as Arias intensity (AI), characteristic intensity (CI), speciﬁc
energy density (SED), cumulative absolute velocity (CAV), Housner Intensity (HI), and level of the acceleration
which contains up to 95% of the AI (A95) were also used in the study. Vmax/Amax and PP represent frequency of
the records. Sa(T1) values of R3 and IR3 frames are given in Fig. 5.
Fig. 3 Target and mean
spectra for 2300 ground
motion records
123
Neural Computing and Applications (2025) 37:18425–18447
18430
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 7
Fig. 4 IMs used in the study
Fig. 5 Spectral acceleration
values at the ﬁrst periods of
frames (Sa(T1))
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18431

---

## Page 8
Moreover, the statistical parameters of the IMs and Sa(T1) values, including mean, maximum and minimum
values, and CoV of R3 and IR3 frames are given in Table 2. It is seen that the CoV values of the IMs are generally
high and range between 0.489 and 4.841 for SD and SED, respectively.
2.1.3 Analysis results and data analysis
In this study, 4600 (2300 GM records for R3 and IR3 frames) NTH analyses were performed. As a result of the
NTH analysis, the maximum drift (Dmax) value was calculated for each GM record and both R3 and IR3 frames.
Then, the MDR (Dmax/H) was obtained by dividing the maximum drift value by the frame’s height (height is 9.0
m). Dmax/H values of each R3 and IR3 RC frames for 2300 GM records are given in Fig. 6. The maximum and
minimum Dmax/H values are computed as 10.40–0.037% and 8.43–0.03% for R3 and IR3, respectively. The mean
of the 2300 Dmax/H values are found to be 0.598% for R3 and 0.500% for IR3. In addition, the CoV(D/H) values are
calculated as 1.261 and 1.158 for R3 and IR3, respectively. Figure 6 shows that the dispersion of the Dmax/H
values is considerable high. This issue was not considered in the study when selecting the GM record and just the
Table 2 Statistical parame-
ters for 21 features used in
the study
Feature
Unit
Mean
Maximum
Minimum
CoV
PGA
g
0.277
2.391
0.017
0.890
PGV
cm/s
30.373
533.446
1.41
1.262
PGD
cm
15.571
736.47
0.311
2.411
Vmax/Amax
s
0.112
0.726
0.019
0.647
ARMS
g
0.035
0.29
0.002
0.879
VRMS
cm/s
5.268
92.678
0.161
1.296
DRMS
cm/s
3.731
195.402
0.032
2.491
AI
m/s
1.818
77.78
0.006
2.156
CI
m1.5/s2.5
0.059
1.21
0.001
1.403
SED
cm2/s
5226.463
772,988.803
4.784
4.841
CAV
cm/s
987.640
7285.611
64.035
0.989
ASI
gs
0.237
2.073
0.016
0.885
VSI
cm
109.954
1203.563
8.129
1.042
HI
cm
101.107
1306.043
7.55
1.097
SMA
g
0.205
1.573
0.015
0.852
SMV
cm/s
21.690
384.89
1.32
1.195
EDA
g
0.262
2.306
0.014
0.889
A95
g
0.273
2.361
0.016
0.892
PP
s
0.338
2.32
0.06
0.616
SD
s
16.083
56.77
1.19
0.489
Sa (R3)
g
0.486
3.638
0.014
1.147
Sa (IR3)
g
0.574
3.483
0.016
1.045
Fig. 6 Dmax/H values of RC
frames for 2300 ground
motion records
123
Neural Computing and Applications (2025) 37:18425–18447
18432
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 9
compatibility between the mean spectrum and the target spectra was checked. The compatibility between the
individual spectrum and the target spectrum was not considered in the study because of only EC8 GM record
selection considered. On the other hand, there is a strong correlation between the dispersion of individual
spectrum and dispersion of seismic response ([5], [23]). However, dispersion of seismic response was not
considered and also was not the purpose of this study.
2.2 Feature engineering framework
In this study, a specialized feature engineering framework (advanced ML pipeline) was employed on the studied
dataset to ensure the robustness and accuracy of the predictive models. The ﬁrst step involved outlier detection
using the outForest approach [9]. The implementation of the outlier forest in the R library was preferred for
identifying and removing anomalous data points from the dataset. outForest identiﬁes outliers by regressing each
numeric variable against all other variables using a random forest model. If the scaled absolute difference between
the observed value and the out-of-bag prediction from the random forest is unusually large, the value is ﬂagged as
an outlier [54]. After removing outliers in the dataset, it was cleaned of any missing values (removed outliers)
using the na.omit function, which systematically removes rows containing any null entries.
To address skewness in the distribution of features, the Box-Cox transformation was applied. The Box-Cox
transformation [12] is a powerful tool for normalizing non-normal data, thereby stabilizing variance and making
the data more amenable to predictive modeling. Mathematically, for a given feature y with skewed distribution,
the Box-Cox transformation is deﬁned as:
yk ¼
yk  1
k
ðk 6¼ 0Þ
log y
ðk ¼ 0Þ
8
<
:
ð1Þ
where k is the transformation parameter that optimizes normality. By applying the Box-Cox transformation, the
features are made more symmetric. An example of R3 and IR3 datasets in the case of before and after Box-Cox
transformation is given in Table 3. Upon evaluating the skewness of features in the raw data for R3 and IR3, it is
found that the skewness values for nearly all features, except PP and SD, exceed 1.0, indicating a high degree of
skewness in their distribution. However, after applying the Box-Cox transformation, it is observed that the
distributions of all features become symmetric.
Feature selection was conducted using the Chi-square test, a statistical method employed to evaluate the
independence between features and the target variable. The Chi-square test (Li et al. [48]) is a widely utilized
method for feature selection, and it is useful for identifying relevant features, reducing the dimensionality and
improving model performance. This statistical technique aims to identify features that exhibit signiﬁcant
dependency on the target variable. The Chi-square test assesses the relationship between two variables by
comparing observed and expected frequencies, thereby determining whether they are related or independent [74].
In cases where the variables are dependent, the observed frequencies will substantially deviate from the
expected frequencies, yielding a high Chi-square value. Conversely, if the variables are independent, the observed
frequencies will closely align with the expected frequencies, resulting in a low Chi-square value. A higher Chi-
square value indicates a stronger dependency between the variables, making the feature more suitable for
inclusion in model training. In contrast, a lower Chi-square value suggests independence, implying that the
feature may not contribute signiﬁcantly to the model and, therefore, may be excluded from further analysis.
Table 4 presents the features identiﬁed by the Chi-square feature selection method from each dataset. It is seen
that the features of Vmax/Amax, PP, SD, DRMS, PGD and Vmax/Amax, SD, DRMS were extracted from the dataset R3
and IR3, respectively.
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18433

---

## Page 10
Subsequently, the dataset was split into training and test sets in a 75–25% ratio. This step ensures that the
models are trained on a substantial portion of the data while reserving a sufﬁcient subset for validation purposes.
The choice of a 75–25% split balances the need for ample training data with the necessity of a robust testing
phase, thus mitigating overﬁtting.
The ﬁnal stage of the preprocessing pipeline involved integrating the selected features into a predictive model
built using the CatBoost algorithm, optimized through GOA. CatBoost, a gradient boosting algorithm that excels
in handling categorical data, was chosen for its ability to mitigate overﬁtting and deliver high accuracy [21]. The
integration of GOA into CatBoost enhances the model’s performance by optimizing hyperparameters such as
learning rate, depth, and iterations. GOA, inspired by the swarming behavior of grasshoppers, operates by
iteratively adjusting the hyperparameters to minimize the objective function, thereby improving the predictive
power of the model. Details of these algorithms are presented in the following section.
Table 3 Variation of skewness values and distribution types of the features after Box-Cox transformation
Feature
R3
IR3
RAW
Box-Cox
RAW
Box-Cox
SV
DT
SV
DT
SV
DT
SV
DT
PGA
1.66
Highly skewed
0.01
Symmetric
1.66
Highly skewed
0.00
Symmetric
PGV
4.27
Highly skewed
0.04
Symmetric
4.19
Highly skewed
0.06
Symmetric
PGD
5.07
Highly skewed
0.25
Symmetric
5.11
Highly skewed
0.29
Symmetric
Vmax/Amax
1.72
Highly skewed
0.09
Symmetric
1.69
Highly skewed
0.10
Symmetric
ARMS
1.45
Highly skewed
0.04
Symmetric
1.45
Highly skewed
0.05
Symmetric
VRMS
2.88
Highly skewed
0.00
Symmetric
3.03
Highly skewed
0.03
Symmetric
DRMS
5.08
Highly skewed
0.15
Symmetric
5.06
Highly skewed
0.19
Symmetric
AI
5.96
Highly skewed
- 0.23
Symmetric
5.86
Highly skewed
-0.22
Symmetric
CI
3.12
Highly skewed
- 0.27
Symmetric
3.15
Highly skewed
-0.26
Symmetric
SED
10.47
Highly skewed
0.19
Symmetric
9.55
Highly skewed
0.23
Symmetric
CAV
1.89
Highly skewed
- 0.06
Symmetric
2.06
Highly skewed
-0.03
Symmetric
ASI
1.40
Highly skewed
0.02
Symmetric
1.39
Highly skewed
0.01
Symmetric
VSI
3.16
Highly skewed
- 0.01
symmetric
3.16
Highly skewed
0.00
Symmetric
HI
3.46
Highly skewed
0.05
Symmetric
3.44
Highly skewed
0.06
Symmetric
SMA
1.38
Highly skewed
- 0.04
Symmetric
1.39
Highly skewed
-0.04
Symmetric
SMV
2.80
Highly skewed
0.04
Symmetric
2.96
Highly skewed
0.07
Symmetric
EDA
1.70
Highly skewed
0.03
Symmetric
1.70
Highly skewed
0.02
Symmetric
A95
1.66
Highly skewed
0.01
Symmetric
1.66
Highly skewed
0.00
Symmetric
PP
0.91
Moderately skewed
0.03
Symmetric
0.92
Moderately skewed
0.03
Symmetric
SD
0.61
Moderately skewed
- 0.08
Symmetric
0.62
Moderately skewed
-0.06
Symmetric
Sa
2.57
Highly skewed
- 0.11
Symmetric
2.01
Highly skewed
-0.11
Symmetric
*SV: skewness value [17], DT: distribution type
Table 4 Selected features after the Chi-square test
Dataset
Number of features
Features selected by Chi-square
R3
16
Sa, VSI, PGV, HI, SMV, AI, CI, EDA, SMA, PGA, ASI, A95, VRMS, ARMS, CAV, SED
IR3
18
Sa, VSI, PGV, HI, SMV, AI, CI, EDA, SMA, PGA, ASI, A95, VRMS, ARMS, CAV, SED, PGD, PP
123
Neural Computing and Applications (2025) 37:18425–18447
18434
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 11
2.3 Details of optimization and machine learning algorithms
2.3.1 Grasshopper optimization algorithm (GOA)
GOA is a highly effective population-based metaheuristic algorithm that expertly models the behavior of
grasshopper swarms in nature to solve optimization problems [73]. The algorithm operates by simulating both
repulsion and attraction forces among virtual grasshoppers within a search space. Repulsion forces enable
grasshoppers to explore widely across the search space, while attraction forces drive them toward promising areas
for exploitation [37]. This dual approach also makes the GOA effective in avoiding the problem of stagnation at
local optima, which is a common issue in optimization problems. In GOA, the grasshoppers collectively form a
network, creating a community where each individual’s position is synchronized with the others. This inter-
connected network allows for the direction of foraging to be determined based on the positions of other indi-
viduals in the group [25]. The following equation is the mathematical model used to conﬁdently simulate the
swarming behavior of grasshoppers:
Xi ¼ Si þ Gi þ Ai
ð2Þ
where Xi determines the position of the i-th grasshopper, Si and Gi are the social interaction between grasshoppers
and the gravity force on the i-th grasshopper, respectively, and Ai is the wind advection. Moreover, random
behavior can be written using random numbers with the following equation:
Xi ¼ r1Si þ r2Gi þ r3Ai
ð3Þ
where r1, r2, and r3 are the random numbers in the range [0–1]. The social interaction Si is deﬁned as follows:
Si ¼
X
N
j¼1;j6¼i
sðdijÞ ^dij
ð4Þ
In which, dij is the distance between the i-th and j-th grasshopper and can be determined as dij ¼ xj  xi

. ^dij is
the unit vector between the i-th and j-th grasshoppers represented by ^dij ¼ ðxjxiÞ
dij . The s function is the social
forces and can be determined in Eq. (5).
sðrÞ ¼ fer=l  er
ð5Þ
where f denotes the attraction intensity, l shows the attractive length scale, and r is the random number.
The Gi and Ai parameters given in Eq. (2) can be computed using the following equations:
Gi ¼ g^eg
ð6Þ
Ai ¼ u^ew
ð7Þ
The g, u, ^eg, and ^ew denote gravitational constant, constant drift, unity vector toward the center of the earth, and
unity vector toward the direction of wind, respectively.
Equation (2) can be generalized by substituting Si,Gi, and Ai as below:
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18435

---

## Page 12
Xd
i ¼ c
X
N
j¼1;j6¼i
c ubd  lbd
2
s
xd
j  xd
i



 xj  xi
dij
 
!
þ ^Td
ð8Þ
where N shows the grasshoppers’ number, ubd and lbd are the d-th dimension of upper boundary and lower
boundary, ^Td is the d-th dimension value in the best solution so far obtained, and c is a decreasing coefﬁcient
which is used to balances the entire swarm’s exploration and exploitation of the target according to the number of
iterations through the following equation:
c ¼ cmax  l cmax  cmin
L
ð9Þ
where the maximum and minimum values are represented by cmax and cmin, l corresponds to the current iteration,
and L denotes the highest iteration number.
2.3.2 Categorical boosting (CatBoost)
CatBoost is a kind of gradient boosting decision tree algorithm (GBDT) that stands out due to its superior
performance compared to the other publicly available boosting algorithms [65]. It is a useful algorithm for solving
problems in areas such as classiﬁcation, regression, and ranking. CatBoost has an innovative approach to dealing
with categorical variables. Unlike many other gradient boosting algorithms that require preprocessing such as
one-hot encoding or label encoding, CatBoost implements an algorithm known as ordered boosting. This tech-
nique allows CatBoost to process categorical features directly by sorting their values and creating splits based on
this sorted order during training [21]. CatBoost incorporates a unique feature known as a ‘‘prior term’’ which is
designed to augment the performance of greedy target statistics as given in Eq. 10. The introduction of this prior
term fundamentally alters the way the algorithm functions, enabling it to generate more accurate models. Fur-
thermore, this integration is not merely for enhancing performance, it plays a crucial role in mitigating the risk of
overﬁtting (Lui and Setiono [50] ).
xrp;k ¼
Pp1
j¼1 xrj;k ¼ xrp;k


Yrj þ a  P
Pp1
j¼1 xrj;k ¼ xrp;k


þ a
ð10Þ
where P represents the prior term and a indicates the weight coefﬁcient greater than 0.
2.4 Hyperparameter tuning and optimization
Hyperparameter tuning plays a pivotal role in optimizing the performance of ML models by directly inﬂuencing
the behavior of training algorithms [82]. Several common hyperparameter tuning approaches have limitations
such as increased search space complexity, high computational cost, and elevated variance [21]. GOA excels at
balancing exploration and exploitation, allowing it to efﬁciently converge toward globally optimal solutions in
high-dimensional search spaces. In this study, GOA was utilized to select the optimal hyperparameters for the
CatBoost algorithm (Table 5). GOA is governed by a set of control parameters, including ﬁtness criteria, type of
optimization (optimType), number of variables (numVar), maximum number of iterations (maxIter), population
size (numPopulation), and a matrix containing the range of variables (rangeVar). A full list of GOA parameters
and their default settings can be found in the GOA documentation [68]. Table 6 outlines the GOA control
parameters and tuned hyperparameters of the CatBoost algorithm.
The construction of the CatBoost model commenced with identifying optimal hyperparameters by applying the
GOA algorithm. The most critical and inﬂuential hyperparameters, depth, learning_rate, l2_leaf_reg,
123
Neural Computing and Applications (2025) 37:18425–18447
18436
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 13
random_strength, subsample, and model_shrink_rate were utilized for optimization by the algorithm. After
completion of the GOA optimization process, the optimal values for the selected hyperparameters were deter-
mined for the R3 and IR3 cases, given in Table 6.
2.5 Evaluation criteria for algorithm performance
Understanding and addressing errors is an essential aspect of evaluating the accuracy of an ML model. The
discrepancy or deviation that appears between the actual data (yi) and the predicted data (^yi) is referred to as the
‘‘error.’’ This error serves as a measure of the accuracy of the ML model’s predictions. If this error falls within
acceptable boundaries, it signiﬁes that the model is performing well and is ready to be put into use. However, if
the error exceeds the tolerable limits, it indicates that the model’s predictions are not accurate enough. There are
numerous methods available to estimate the accuracy of an ML model’s performance. Some of the most popular
and widely used methods include the mean squared error (MSE), root mean squared error (RMSE), mean absolute
error (MAE), mean absolute percentage error (MAPE), and coefﬁcient of determination (R2) (Table 7). Each of
these methods provides a different perspective on the model’s accuracy, allowing data scientists to gain a
comprehensive understanding of the model’s performance and make necessary adjustments. The metrics to be
used to evaluate the performance of the algorithms can be given as listed in Table 7 with n which represents test
sample size and yi shows mean value.
Table 5 CatBoost hyperparameters and their ranges
No
Hyperparameters
Explanation
Range
1
Depth
Depth of the tree
1.0–10
2
Learning_rate
Boosting learning rate
0.01–1.0
3
l2_leaf_reg
Coefﬁcient at the L2 regularization term of the cost function
2.0–10
4
Random_strength
The level of randomness
0.0–10
5
Subsample
Ratio of training instances
0.01–1.0
6
Model_shrink_rate
The constant used for determining the coefﬁcient to multiple the model on each iteration
0.0–1.0
Table 6 Hyperparameters
for the CatBoost algorithm
with GOA control
parameters
Model
Hyperparameters
Depth
Learning rate
l2_leaf_reg
Random_strength
Subsample
Model_shrink_rate
R3
7.110
0.672
6.862
0.485
0.428
0.0007
IR3
10.00
0.713
3.534
0.519
0.696
0.0002
Model
GOA control parameters
FC*
Maxiter
Rangevar
Numpopulation
NumVar
Optimtype
R3
RMSE
100
Matrix (2 9 6)
20
6
MIN
IR3
RMSE
500
Matrix (2 9 6)
40
6
MIN
*FC: ﬁtness criteria
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18437

---

## Page 14
3 Results and discussion
3.1 Evaluation of R3
In this paper, the test data are utilized to rigorously evaluate the performance of ML models through a range of
statistical metrics. Each of these metrics offers unique insights into the predictive capacity and accuracy of the
model. In particular, lower values of RMSE, MSE, and MAE signify enhanced model reliability and statistical
robustness, suggesting that the model’s predictions are more aligned with actual outcomes. Meanwhile, the R2
value, which varies between 0 and 1, measures the proportion of the variance in the dependent variable explained
by the independent variables. Generally, R2 values above 0.7 or 0.8 are regarded as indicative of a strong model
ﬁt, reﬂecting a higher level of explanatory power. Another critical metric in evaluating model performance is
MAPE, which provides an easily interpretable measure of prediction accuracy. MAPE expresses the average
deviation between predicted and actual values as a percentage, offering a more intuitive understanding of the
model’s performance. A MAPE value below 10% is generally classiﬁed as ‘‘highly accurate,’’ representing an
excellent model. Values between 10 and 20% are considered ‘‘good,’’ while those between 20 and 50% indicate
‘‘reasonable’’ predictive accuracy. However, a MAPE value exceeding 50% points to a model with ‘‘poor’’
performance, suggesting that its predictions deviate substantially from actual values and may not be reliable for
practical applications [47]. Table 8 summarizes the overall performance metric results for R3 using the CatGrass
framework. As can be seen from the table, all metrics have excellent scores, indicating a highly accurate
prediction performance. Moreover, Fig. 7 thoroughly illustrates the comparison between the actual and predicted
values of each test sample. The comparison between the actual and predicted values clearly shows a strong
alignment between them. An individual analysis of the test data reveals that 76% of the test data were predicted
with ‘‘highly accurate,’’ indicating a minimal percentage difference between the actual and predicted values.
Furthermore, 20% of the predictions were classiﬁed as ‘‘good’’ while the proportion deemed ‘‘reasonable’’
accounts for 3%. When averaged across the dataset, as indicated in Table 8, MAPE was calculated to be 7%,
indicating a highly effective prediction performance.
Table 7 Performance eval-
uation metrics for regres-
sion models
Name of evaluation metric
Equation
Mean squared error
MSE ¼ 1
n
P
n
i¼1
yi  ^yi
ð
Þ2
Root mean squared error
RMSE ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
n
P
n
i¼1
yi  ^yi
ð
Þ2
s
Mean absolute error
MAE ¼ 1
n
P
n
i¼1
yi  ^yi
j
j
Mean absolute percentage error
MAPE ¼ 100%
n
P
n
i¼1
yi ^yi
yi


Coefﬁcient of determination
R2 ¼ 1 
Pn
i¼1 yi ^yi
j
j2
Pn
i¼1 yiyi
j
j2
Table 8 Performance
results of the ML model for
R3
Evaluation metrics
R2
MSE
RMSE
MAE
MAPE (%)
0.9928
0.00002
0.0053
0.0028
7.0074
123
Neural Computing and Applications (2025) 37:18425–18447
18438
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 15
3.2 Evaluation of IR3
Table 9 indicates the performance metrics results for IR3. Similar to R3, IR3 results exhibited highly successful
performance outcomes. This clearly demonstrates the effectiveness and robustness of the applied CatGrass
approach, highlighting its ability to deliver reliable results in the context of the given analysis or experiment.
Furthermore, for IR3, a detailed comparison of the actual and predicted values for each test data is presented in
Fig. 8. The analysis reveals that 70% of the test data were predicted with ‘‘highly accurate.’’ Additionally, 21% of
the samples were classiﬁed as ‘‘good’’ predictions, 8% of the samples were predicted with ‘‘reasonable’’ accu-
racy, and ﬁnally, a small fraction of 2% were categorized as ‘‘poor’’ predictions, highlighting areas for potential
improvement. Although the results obtained for IR3 are somewhat behind compared to those achieved for R3,
both RC cases have still yielded exceptionally high MDR predictions. This indicates that despite some differences
in performance, the overall predictive accuracy for MDR remains notably strong across both scenarios.
3.3 Effectiveness of the CatGrass Model as compared to CatBoost Model
To assess the effectiveness of the CatGrass model, a benchmark model was built using the same dataset and the
results of this comparison are illustrated in Fig. 9. It should be noted that no feature engineering was applied to
the raw model, it was only optimized with GOA. It is clearly seen that the proposed CatGrass model signiﬁcantly
outperforms the benchmark model in terms of prediction performance. A detailed examination of the R2 values
reveals that CatBoost model yielded R2 values of 0.86 and 0.89 for R3 and IR3, respectively. However, by
employing the novel framework to CatBoost (i.e., CatGrass), an improvement of 11% to 15% was observed in R2
values, reaching up to 0.99. This substantial enhancement underscores the superiority of the proposed method.
Fig. 7 Comparison of
actual and predicted Dmax/H
values with percentage
error for R3
Table 9 Performance
results of the ML model for
IR3
Evaluation metrics
R2
MSE
RMSE
MAE
MAPE (%)
0.9922
0.00001
0.0036
0.0024
9.6924
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18439

---

## Page 16
Moreover, notable improvements were also observed in other key metrics, including RMSE, MSE, MAE, and
MAPE, all of which experienced signiﬁcant decreases. The substantial improvements in all metrics afﬁrm that the
CatGrass approach proposed in this study offers a robust and reliable MDR prediction model for low-rise RC
frames. These ﬁndings clearly demonstrate the effectiveness of the integrated feature engineering techniques and
optimization strategy, contributing to the development of more accurate and efﬁcient predictive models in
structural engineering applications.
Fig. 8 Comparison of
actual and predicted Dmax/H
values with percentage
error for IR3
Fig. 9 Performance metric
results of the CatBoost and
CatGrass models
123
Neural Computing and Applications (2025) 37:18425–18447
18440
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 17
3.4 Effectiveness of the CatGrass model as compared to popular ML algorithms
Table 10 compares the prediction results of CatGrass and other popular ML algorithms in terms of R2, RMSE,
MSE, MAE, MAPE, and computational time (s), with the best values highlighted in bold. Table 10 shows that the
proposed CatGrass model demonstrates superior predictive performance compared to the other ML models,
namely CatBoost, XGBoost, RF, and SVM both for R3 and IR3. CatGrass exhibits the highest R2 values (0.9928
for R3 and 0.9922 for IR3), and the lowest RMSE, MSE, and MAE values, signifying its superior accuracy in
predictive modeling. However, while CatGrass achieves relatively low MAPE values, it is important to highlight
that RF for R3 and XGBoost for IR3 outperform CatGrass in this metric. Moreover, it is also evident that
CatGrass incurs a signiﬁcantly higher computational cost compared to the other models. The computational time
required for CatGrass is 188.98 seconds for R3 and 190.68 seconds for IR3, which is substantially longer than
that of SVM, the most computationally efﬁcient model, with processing times of only 3.06 seconds for R3 and
2.36 seconds for IR3. This observation suggests a trade-off between accuracy and computational efﬁciency,
which must be carefully considered when selecting an optimal model for real-world applications.
3.5 SHAP-based feature importance analysis
The XGBoost algorithm combined with SHAP (SHapley Additive exPlanations) was applied to evaluate and
measure the relative importance of input features, as illustrated in Fig. 10. The ﬁgure depicts the distribution of
SHAP values across individual data points, revealing how different input variables inﬂuence the results of
prediction algorithms. Dots positioned to the right of the zero line indicate an increasing contribution to the
model’s prediction, while dots on the left side suggest a decreasing effect. Within the color-coded representation,
the red data points demonstrate high feature values compared to their blue counterparts (low feature values). The
SHAP summary plots for R3 (a) and IR3 (b) reveal that Sa is the most inﬂuential feature in both cases, exhibiting
the highest SHAP value. The distribution of SHAP values for Sa in R3 indicates that both high and low values
contribute to both positive and negative model outputs without a clear separation. Conversely, high values of Sa
are more aligned with positive SHAP values, suggesting a stronger positive impact on the prediction results for
Table 10 Comparison of
performance results of the
CatGrass model and the
other ML models
R3
CatGrass
CatBoost
XGBoost
RF
SVM
R2
0.9928
0.8882
0.9629
0.9461
0.7924
RMSE
0.0053
0.0131
0.0105
0.0126
0.0252
MSE
0.0000
0.0001
0.0001
0.0001
0.0006
MAE
0.0028
0.0046
0.0048
0.0048
0.0084
MAPE (%)
7.007
22.115
8.3708
6.7137
21.153
Computational time (s)
188.98
104.76
128.76
158.22
3.06
IR3
CatGrass
CatBoost
XGBoost
RF
SVM
R2
0.9922
0.8602
0.9150
0.9495
0.6133
RMSE
0.0035
0.0130
0.0152
0.0118
0.0331
MSE
0.0000
0.0001
0.0002
0.0001
0.0011
MAE
0.0024
0.0033
0.0044
0.0040
0.0083
MAPE (%)
9.6923
21.350
6.8376
6.8447
19.214
Computational time (s)
190.68
99.71
122.04
153.88
2.36
*Best values highlighted in bold
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18441

---

## Page 18
IR3. Besides Sa, features such as VSI, PGV, and HI also play signiﬁcant roles in R3, whereas A95 gains more
importance while HI becomes less inﬂuential in IR3. These differences indicate that while Sa remains the
dominant feature in both cases, the relative contributions of secondary features vary, inﬂuencing the model’s
predictions differently across R3 and IR3.
3.6 Statistical significance analysis
In the evaluation of regression-based ML models, assessing the statistical signiﬁcance of the relationship between
actual and predicted values is crucial for determining model performance. In this section, it was aimed to
determine the strength and statistical signiﬁcance of the linear relationship between actual and predicted values in
each dataset. Therefore, the Pearson correlation technique was used to assess the statistical signiﬁcance of the
relationship between predicted and actual values. The Pearson correlation coefﬁcient (denoted as r) is a widely
used statistic that measures the strength and direction of a linear relationship between two continuous variables. It
ranges from - 1 to ? 1, where r = ? 1 indicates a perfect positive linear correlation, meaning that as one
variable increases, the other increases proportionally, r = - 1 signiﬁes a perfect negative linear correlation,
whereas one variable increases, the other decreases proportionally, and r = 0 denotes no linear correlation
between the variables. Besides the correlation coefﬁcient, the p-value is a critical output of the Pearson correlation
test. A low p-value (typically below a signiﬁcance level of 0.05) suggests that the observed correlation is
statistically signiﬁcant and unlikely to have occurred by random chance.
Based on the prediction results of CatGrass, R3 yielded a Pearson correlation coefﬁcient of r = 0.979. This
exceptionally high positive value indicates a very strong positive linear relationship between the actual and
predicted values. Furthermore, the associated p-value was found to be p \0.001. This extremely low p-value is
far below the conventional signiﬁcance level of 0.05. For IR3, the Pearson correlation analysis resulted in a
correlation coefﬁcient of r = 0.947. While slightly lower than that observed for R3, this value still signiﬁes a very
strong positive linear relationship between the actual and predicted values. The p-value associated with this
correlation was also found to be p \ 0.001. Statistical signiﬁcance analysis strongly suggests that the predicted
values are statistically signiﬁcantly related to the actual values. The extremely low p-values across all tests
indicate that these results are highly unlikely to have occurred by random chance if there were no true relationship
between the actual and predicted values. This suggests that the CatGrass model is performing well in predicting
the actual values.
Fig. 10 SHAP importance values of features for R3 (a) and IR3 (b) cases
123
Neural Computing and Applications (2025) 37:18425–18447
18442
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 19
4 Conclusions
In this study, an advanced feature engineering pipeline with GOA-optimized CatBoost model was employed to
predict the maximum drift ratio of regular and irregular low-rise RC frames. Two distinct RC frames were
considered for this purpose: a 3-story regular RC frame (R3) and a vertically irregular RC frame (IR3). 20
different intensity measures (IMs), spectral acceleration (Sa) values at the ﬁrst mode periods Sa(T1), and nonlinear
time history analyses results for each record are considered as a dataset. The framework used in the study
incorporated an extensive workﬂow, including the data preprocessing techniques such as outForest analysis for
outlier detection, na.omit function for cleaning rows containing any null entries, feature transformation with Box-
Cox transformation, and feature selection through the Chi-square method. The hyperparameters of the ML models
were optimized using GOA. For comparison, the predictive performance of the GOA-optimized CatGrass models
(i.e., CatGrass) was assessed against that of the raw CatBoost model. The ﬁndings of this study can be sum-
marized as follows:
•
A total of 16 out of 21 features were identiﬁed for R3, and 18 features were selected IR3 using the Chi-square
feature selection method. Additionally, the features Vmax/Amax, PP, SD, DRMS, and PGD were eliminated from
the R3 dataset, while Vmax/Amax, SD, DRMS were extracted from the IR3 dataset.
•
The novel CatGrass model demonstrated exceptionally high performance in predicting MDR of low-rise RC
frames. The model achieved an R2 of 0.99, RMSE of 0.0053, a MSE of 0.00002, MAE of 0.0028, and MAPE
of 7% for R3. Similarly, the model also reached an R2 of 0.99, with an RMSE of 0.0036, an MSE of 0.0001, an
MAE of 0.0024, and an MAPE of 9.7% for IR3. This study approved the effectiveness of the proposed
CatGrass model. It can be considered an efﬁcient tool for seismic design and assessment of RC frames.
•
To better demonstrate the effectiveness of the CatGrass model, a benchmark model based on the CatBoost
algorithm was created, and the results were compared. Indeed, the comparison showed an improvement of
11% to 15% in R2 values when using the CatGrass model. This increase in R2 values highlights the enhanced
predictive accuracy achieved through the novel feature engineering framework and GOA optimization.
Additionally, signiﬁcant reductions were observed in other performance metrics. These improvements
collectively demonstrate the superiority of the CatGrass approach in providing more accurate and reliable
predictions, particularly in the context of seismic response for low-rise RC frames.
•
CatGrass also outperformed some popular ML algorithms (i.e., RF, SVM, and XGBoost) in terms of
performance metrics; however, it fell behind as compared to the other ML algorithms based on computational
time.
•
Features such as Sa, VSI and PGV were found to be the strongest inﬂuences on the seismic response of both
R3 and IR3 frames.
In this study, low-rise RC frames were considered and proposed CatGrass ML model is used for predicting of
MDR. This situation can be considered a limitation of the study. However, future research could extend these
ﬁndings by analyzing the effects of varying seismic scenarios and different structural conﬁgurations on the overall
performance. A more in-depth exploration of different lateral strength ratios and periods would help reﬁne the
understanding of their inﬂuence on the nonlinear response. Furthermore, conducting comparative studies using
alternative ML methods could complement the ﬁndings and broaden the scope of seismic risk assessment
techniques.
Acknowledgements Not applicable.
Author contributions AD: Conceptualization, Writing – review & editing, Writing – original draft, Investigation, Visual-
ization. SD: Conceptualization, Writing – review & editing, Writing – original draft, Investigation, Visualization. EKS:
Conceptualization, Writing – review & editing, Writing – original draft, Investigation, Visualization.
Funding Open access funding provided by the Scientiﬁc and Technological Research Council of Tu¨rkiye (TU¨ BI˙TAK). No
funding was received for conducting this study.
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18443

---

## Page 20
Data availability Data will be made available on request.
Declarations
Competing interests The authors declare that they have no known competing financial interests or personal relationships
that could have appeared to influence the work reported in this paper.
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
1. Ancheta TD, Darragh RB, Stewart JP, Seyhan E, Silva WJ, Chiou BSJ et al (2014) NGAWest2 database. Earthq Spectra
30(3):989–1005. https://doi.org/10.1193/070913EQS197M
2. Ambraseys NN, Douglas J, Rinaldis D, Berge CT, Suhadolc P, Costa G, Sigbjornsson R, Smit P (2004) Dissemination
of European strong-motion data, vol. 2. CD-ROM Collection. Engineering and Physical Sciences Research Council,
Swindon.
3. Amezquita-Sanchez J, Valtierra-Rodriguez M, Adeli H (2020) Machine learning in structural engineering. Sci Iran, Civ
Eng Trans 27(6):2645–2656. https://doi.org/10.24200/sci.2020.22091
4. Aljarah I, Al-Zoubi AM, Faris H et al (2018) Simultaneous feature selection and support vector machine optimization
using the grasshopper optimization algorithm. Cogn Comput 10:478–495. https://doi.org/10.1007/s12559-017-9542-9
5. Arau´jo M, Macedo L, Marques M, Castro JM (2016) Code-based record selection methods for seismic performance
assessment of buildings. Earthq Eng Struct Dyn 45(1):129–148. https://doi.org/10.1002/eqe.2620
6. ASCE 7–16 (2016) Minimum design loads for buildings and other structures. American Society of Civil Engineers,
Reston.
7. Asgarkhani N, Kazemi F, Jakubczyk-Gałczynska A, Mohebi B, Jankowski R (2024) Seismic response and performance
prediction of steel buckling-restrained braced frames using machine-learning methods. Eng Appl Artif Intell
128:107388. https://doi.org/10.1016/j.engappai.2023.107388
8. Asteris PG, Repapis CC, Repapi EV, Cavaleri L (2017) Fundamental period of inﬁlled reinforced concrete frame
structures. Struct Infrastruct Eng 13(7):929–941. https://doi.org/10.1080/15732479.2016.1227341
9. Ay O¨ B, Erberik MA (2008) Vulnerability of Turkish low-rise and mid-rise reinforced concrete frame structures. J Earthq
Eng 12(2):2–11. https://doi.org/10.1080/13632460802012687
10. Azizi M, Shishehgarkhaneh MB, Basiri M, Moehler RC, Fang Y, Chan M (2023) Wolf-Bird optimizer (WBO): a novel
metaheuristic algorithm for building information modeling-based resource tradeoff. J Eng Res. https://doi.org/10.1016/j.
jer.2023.11.024
11. Azizi M, Zhou A (2024) Optimized machine learning approach for structural response prediction using wolf-bird
optimizer. Structures 65:106691. https://doi.org/10.1016/j.istruc.2024.106691
12. Box GE, Cox DR (1969) An analysis of transformations. J Roy Stat Soc: Ser B (Methodol) 26:211–243
13. Breiman L (1996) Bagging predictors. Mach Learn 24:123–140. https://doi.org/10.1007/BF00058655
14. Chandola V, Banerjee A, Kumar V (2009) Anomaly detection: a survey. ACM Comput Surv 41:1–58. https://doi.org/
10.1145/1541880.1541882
15. Chen T, Guestrin C (2016) XGBoost: A scalable tree boosting system. 22nd Acm Sigkdd International Conference on
Knowledge Discovery and Data Mining 785–794. https://doi.org/10.1145/2939672.2939785.
16. Cheng MY, Prayogo D (2014) Symbiotic organisms Search: a new metaheuristic optimization algorithm. Comput Struct
139:98–112. https://doi.org/10.1016/j.compstruc.2014.03.007
17. Cramer H (1946) Mathematical methods of statistics. Princeton Univ, Princeton, NJ
18. Demir A (2022) Investigation of the effect of real ground motion record number on seismic response of regular and
vertically irregular RC frames. Structures 39:1074–1091. https://doi.org/10.1016/j.istruc.2022.03.091
19. Demir A, Sahin EK, Demir S (2024) Advanced tree-based machine learning methods for predicting the seismic response
of regular and irregular RC frames. Structures 64:106524. https://doi.org/10.1016/j.istruc.2024.106524
123
Neural Computing and Applications (2025) 37:18425–18447
18444
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 21
20. Demir S, Sahin EK (2022) Comparison of tree-based machine learning algorithms for predicting liquefaction potential
using canonical correlation forest, rotation forest, and random forest based on CPT data. Soil Dyn Earthq Eng
154:107130. https://doi.org/10.1016/j.soildyn.2021.107130
21. Demir S, Sahin EK (2023) Predicting occurrence of liquefaction-induced lateral spreading using gradient boosting
algorithms integrated with particle swarm optimization: PSO-XGBoost, PSO-LightGBM, and PSO-CatBoost. Acta
Geotech 18:3403–3419. https://doi.org/10.1007/s11440-022-01777-1
22. Demir A, Palanci M, Kayhan AH (2024) Evaluation the effect of amplitude scaling of real ground motions on seismic
demands accounting different structural characteristics and soil classes. Bull Earthquake Eng 22:365–393. https://doi.
org/10.1007/s10518-023-01780-1
23. Demir A, Kayhan AH, Palanci M (2023) Response- and probability-based evaluation of spectrally matched ground
motion selection strategies for bi-directional dynamic analysis of low-to mid-rise RC buildings. Structures 58:105533.
https://doi.org/10.1016/j.istruc.2023.105533
24. Demertzis K, Kostinakis K, Morﬁdis K, Iliadis L (2023) An interpretable machine learning method for the prediction of
R/C buildings’ seismic response. J Build Eng 63:105493. https://doi.org/10.1016/j.jobe.2022.105493
25. Dong J, Zeng W, Lei G, Wu L, Chen H, Wu J, Srivastava AK (2022) Simulation of dew point temperature in different
time scales based on grasshopper algorithm optimized extreme gradient boosting. J Hydrol 606: 127452 https://doi.org/
10.1016/j.jhydrol.2022.127452.
26. EUROCODE-8 (2004) Design provisions for earthquake resistance of structures, Part 1: General rules, seismic actions
and rules for buildings. European Committee for Standardization, Brussels.
27. Fausett LW (1994) Fundamentals of Neural Networks: Architectures. Prentice-Hall, Algorithms and Applications
28. Feurer M, Hutter F (2019) Hyperparameter Optimization. In: Hutter F, Kotthoff L, Vanschoren J (eds) Automated
Machine Learning. The Springer Series on Challenges in Machine Learning. Springer, Cham
29. Friedman JH (2001) Greedy function approximation: A gradient boosting machine. Ann Stat 29:1189–232. https://www.
jstor.org/stable/2699986.
30. Goldberg DE (1989) Genetic Algorithms in Search. Optimization, and Machine Learning, 1st edn. Addison Wesley Pub,
Boston, Massachusetts, USA
31. Geurts P, Ernst D, Wehenkel L (2006) Extremely randomized trees. Mach Learn 63:3–42. https://doi.org/10.1007/
s10994-006-6226-1
32. Giordano N, De Luca F, Sextos A (2021) Analytical fragility curves for masonry school building portfolios in Nepal.
Bull Earthq Eng 19:1121–1150. https://doi.org/10.1007/s10518-020-00989-8
33. Hamidia M, Kaboodkhani M, Bayesteh H (2024) Vision-oriented machine learning-assisted seismic energy dissipation
estimation for damaged RC beam-column connections. Eng Struct 301:117345. https://doi.org/10.1016/j.engstruct.2023.
117345
34. Harirchian E, Lahmer T, Kumari V, Jadhav K (2020) Application of support vector machine modeling for the rapid
seismic hazard safety evaluation of existing buildings. Energies 13(13):3340. https://doi.org/10.3390/en13133340
35. HariﬁS, Khalilian M, Mohammadzadeh J, Ebrahimnejad S (2020) Optimizing a neuro-fuzzy system based on nature-
inspired emperor penguins colony optimization algorithm. IEEE Trans Fuzzy Syst 28(6):1110–1124. https://doi.org/10.
1109/TFUZZ.2020.2984201
36. Hatzigeorgiou GD, Liolios AA (2010) Nonlinear behaviour of RC frames under repeated strong ground motions. Soil
Dyn Earthq Eng 30(10):1010–1025. https://doi.org/10.1016/j.soildyn.2010.04.013
37. Hekimog˘lu B, Ekinci S (2018) Grasshopper optimization algorithm for automatic voltage regulator system. In: 5th
international conference on electrical and electronic engineering (5th ICEEE) 152–156. IEEE.
38. Huu-Tai T (2022) Machine learning for structural engineering: a state-of-the-art review. Structures 38:448–491. https://
doi.org/10.1016/j.istruc.2022.02.003
39. Hwang SH, Mangalathu S, Shin J, Jeon JS (2021) Machine learning-based approaches for seismic demand and collapse
of ductile reinforced concrete building frames. J Build Eng 34:101905. https://doi.org/10.1016/j.jobe.2020.101905
40. Ibrahim HT, Mazher WJ, Ucan ON et al (2019) A grasshopper optimizer approach for feature selection and optimizing
SVM parameters utilizing real biomedical data sets. Neural Comput Appl 31:5965–5974. https://doi.org/10.1007/
s00521-018-3414-4
41. Kamel SR, Yaghoubzadeh R (2021) Feature selection using grasshopper optimization algorithm in diagnosis of diabetes
disease. Inform Med Unlocked 26:100707. https://doi.org/10.1016/j.imu.2021.100707
42. Kazemi F, Asgarkhani N, Jankowski R (2023) Machine learning-based seismic response and performance assessment of
reinforced concrete buildings. Arch Civ Mech Eng 23:94. https://doi.org/10.1007/s43452-023-00631-9
43. Kennedy J, Eberhart R (1995) Particle swarm optimization. IEEE International Conference on Neural Networks,
Piscataway, NJ.
44. Kiani J, Camp C, Pezeshk S (2019) On the application of machine learning techniques to derive seismic fragility curves.
Comput Struct 218:108–122. https://doi.org/10.1016/j.compstruc.2019.03.004
45. Kostinakis K, Athanatopoulou A, Morﬁdis K (2015) Correlation between ground motion intensity measures and seismic
damage of 3D R/C buildings. Eng Struct 82:151–167. https://doi.org/10.1016/j.engstruct.2014.10.035
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18445

---

## Page 22
46. Lazaridis PC, Kavvadias IE, Demertzis K, Iliadis L, Vasiliadis LK (2022) Structural damage prediction of a reinforced
concrete frame under single and multiple seismic events using machine learning algorithms. Appl Sci 12(8):3845.
https://doi.org/10.3390/app12083845
47. Lewis C (1982) International and Business Forecasting Methods Butterworths: London.
48. Li K, Xie X, Zhou B, Huang C, Lin W, Zhou Y, Wang C (2024) Thickness regression for backﬁll grouting of shield
tunnels based on GPR data and CatBoost & BO-TPE: a full-scale model test study. Undergr Space 17:100–119. https://
doi.org/10.1016/j.undsp.2023.10.003
49. Liaw A, Wiener M (2002) Classiﬁcation and regression by randomForest. R News 2(3):18–22
50. Liu H, Setiono R (1995) Chi2: Feature selection and discretization of numeric attributes. In: Proceedings of the
International Conference on Tools with Artiﬁcial Intelligence (7th IEEE) 388–391.
51. Mafarja M, Aljarah I, Faris H, Hammouri AI, Al-Zoubi A, Mirjalili S (2019) Binary grasshopper optimisation algorithm
approaches for feature selection problems. Expert Syst Appl 117:267–286. https://doi.org/10.1016/j.eswa.2018.09.015
52. Mangalathu S, Hwang SH, Choi E, Jeon JS (2019) Rapid seismic damage evaluation of bridge portfolios using machine
learning techniques. Eng Struct 201:109785. https://doi.org/10.1016/j.engstruct.2019.109785
53. Mander JB (1983) Seismic design of bridge piers. research report 84–2, Department of Civil Engineering, University of
Canterbury, Christchurch.
54. Mayer M (2023) outForest: Multivariate Outlier Detection and Replacement, R package version 1.0.1. https://CRAN.
Rproject.org/package=outForest/. [accessed 13 March 2024].
55. Meral E (2024) Relationships between ground motion parameters and energy demands for regular low-rise RC frame
buildings. Bull Earthquake Eng 22:2829–2865. https://doi.org/10.1007/s10518-024-01885-1
56. Mirrashid M, Naderpour H (2022) Computational intelligence-based models for estimating the fundamental period of
inﬁlled reinforced concrete frames. J Build Eng 46:103456. https://doi.org/10.1016/j.jobe.2021.103456
57. Mirjalili S, Lewis A (2016) The whale optimization algorithm. Adv Eng Softw 95:51–67. https://doi.org/10.1016/j.
advengsoft.2016.01.008
58. Mirjalili S, Jangir P, Mirjalili SZ, Saremi S, Trivedi IN (2017) Optimization of problems with multiple objectives using
the multi-verse optimization algorithm. Knowl Based Syst 134:50–71. https://doi.org/10.1016/j.knosys.2017.07.018
59. Morﬁdis K, Kostinakis K (2023) Seismic parameters’ combinations for the optimum prediction of the damage state of
R/C buildings using neural networks. Adv Eng Softw 106:1–16. https://doi.org/10.1016/j.advengsoft.2017.01.001
60. Noureldin M, Ali T, Kim J (2023) Machine Learning-based seismic assessment of framed structures with soil-structure
interaction. Front Struct Civ Eng 17:205–223. https://doi.org/10.1007/s11709-022-0909-y
61. Palanci M, Senel SM (2019) Correlation of earthquake intensity measures and spectral displacement demands in
building type structures. Soil Dyn Earthq Eng 121:306–326. https://doi.org/10.1016/j.soildyn.2019.03.023
62. Palanci M, Demir A, Kayhan AH (2023) Quantifying the effect of amplitude scaling of real ground motions based on
structural responses of vertically irregular and regular RC frames. Struct 51:105–123. https://doi.org/10.1016/j.istruc.
2023.03.040
63. Paudel S, Pudasaini A, Shrestha RK, Kharel E (2023) Compressive strength of concrete material using machine learning
techniques. Clean Eng Technol 15:100661. https://doi.org/10.1016/J.CLET.2023.100661
64. Priestley MJN, Calvi GM, Kowalsky MJ (2007) Displacement-Based Seismic Design of Structures. IUSS Press, Pavia,
Italy
65. Prokhorenkova L, Gusev G, Vorobev A, Dorogush AV, Gulin A (2018) CatBoost: unbiased boosting with categorical
features. In: Proceedings of the 32nd International Conference on Neural Information Processing Systems, 6639–49.
66. Raﬁei MH, Adeli H (2017) A novel machine learning-based algorithm to detect damage in high-rise building structures.
Struct Des Tall Build 26(18):e1400. https://doi.org/10.1002/tal.1400
67. Rahman T, Hasan MH, Momin MF, Zheng P (2024) Data-driven approach to predict the fundamental period of steel-
braced RC frames using stacked generalization machine learning models. Asian J Civ Eng 25(3):2379–2397. https://doi.
org/10.1007/s42107-023-00914-9
68. Riza LS, Nugroho EP, Prabowo MBA, Junaeti E, Abdullah AG (2019) Metaheuristicopt: Metaheuristic for optimization.
R package version 2.0. 0. https://doi.org/10.32614/CRAN.package.metaheuristicOpt.
69. Rodrigues H, Furtado A, Vila-Pouca N, Varum H, Barbosa AR (2018) Seismic assessment of a school building in Nepal
and analysis of retroﬁtting solutions. Int J Civ Eng 16:1573–1589. https://doi.org/10.1007/s40999-018-0297-9
70. Russell SJ, Norvig P (2009) Artiﬁcial Intelligence: A Modern Approach. 3rd, edition. Pearson, Upper Saddle River
71. Sahin EK, Demir S (2023) Greedy-AutoML: a novel greedy-based stacking ensemble learning framework for assessing
soil liquefaction potential. Eng Appl Artif Intell 119:105732. https://doi.org/10.1016/j.engappai.2022.105732
72. SAP2000 (2009) Integrated solution for structural analysis and design. Computers and Structures, Berkeley.
73. Saremi S, Mirjalili S, Lewis A (2017) Grasshopper optimisation algorithm: Theory and application. Adv Eng Softw
105:30–47. https://doi.org/10.1016/j.advengsoft.2017.01.004
74. Sreehari E, Babu LD (2024) Critical factor analysis for prediction of diabetes mellitus using an inclusive feature
selection strategy. Appl Artif Intell 38(1):2331919. https://doi.org/10.1080/08839514.2024.2331919
75. Storn R, Price K (1997) Differential evolution – a simple and efﬁcient heuristic for global optimization over continuous
spaces. J Global Optim 11:341–359. https://doi.org/10.1023/A:1008202821328
123
Neural Computing and Applications (2025) 37:18425–18447
18446
https://doi.org/10.1007/s00521-025-11387-z

---

## Page 23
76. Sun H, Burton HV, Huang H (2021) Machine learning applications for building structural design and performance
assessment: state-of-the-art review. J Build Eng 33:101816. https://doi.org/10.1016/j.jobe.2020.101816
77. Sun S, Cao Z, Zhu H, Zhao J (2019) A survey of optimization methods from a machine learning perspective. IEEE Trans
Cybern 50(8):3668–3681. https://doi.org/10.48550/arXiv.1906.06821
78. TBEC (2018). Turkish building earthquake code. Disaster and Emergency Management Presidency, Ankara.
79. Wang SC (2003) Artiﬁcial Neural Network. In: Interdisciplinary Computing in Java Programming. The Springer
International Series in Engineering and Computer Science. 743. Springer, Boston, 81–100 https://doi.org/10.1007/978-
1-4615-0377-4_5.
80. Yahiaoui A, Dorbani S, Yahiaoui L (2023) Machine learning techniques to predict the fundamental period of inﬁlled
reinforced concrete frame buildings. Structures 54:918–927. https://doi.org/10.1016/j.istruc.2023.05.052
81. Yang XS, He X (2013) Fireﬂy algorithm: recent advances and applications. Int J Swarm Intell 1(1):36–50. https://doi.
org/10.1504/IJSI.2013.055801
82. Yang L, Shami A (2020) On hyperparameter optimization of machine learning algorithms: theory and practice. Neu-
rocomputing 415:295–316. https://doi.org/10.1016/j.neucom.2020.07.061
83. Yu Y, Li W, Li J, Nguyen TN (2018) A novel optimised self-learning method for compressive strength prediction of
high performance concrete. Constr Build Mater 184:229–247. https://doi.org/10.1016/j.conbuildmat.2018.06.219
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.
Authors and Afﬁliations
Ahmet Demir1
• Selçuk Demir1
• Emrehan Kutlug Sahin1
& Ahmet Demir
ahmetdemir@ibu.edu.tr
Selçuk Demir
selcukdemir@ibu.edu.tr
Emrehan Kutlug Sahin
emrehansahin@ibu.edu.tr
1
Department of Civil Engineering, Bolu Abant Izzet Baysal University, 14030 Bolu, Tu¨rkiye
Neural Computing and Applications (2025) 37:18425–18447
123
https://doi.org/10.1007/s00521-025-11387-z
18447

---
