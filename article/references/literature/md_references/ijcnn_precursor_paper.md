# _ICCSA_2026___Andrey_____Combining_Technical_Indicators_and_Genetic_Algorithms_for_Short_Term_Machine_Learning_Prediction_of_Mini_Index_Futures (1)
**Original PDF**: `article\references\_ICCSA_2026___Andrey_____Combining_Technical_Indicators_and_Genetic_Algorithms_for_Short_Term_Machine_Learning_Prediction_of_Mini_Index_Futures (1).pdf`
**Page Count**: 15

---

<!-- Page 1 -->
## Page 1

Combining Technical Indicators and Genetic
Algorithms for Short-Term Machine Learning
Prediction of Mini-Index Futures
Andrey V.S Souza1[0009−0006−4177−758X], Bruno L.
Dalmazo1[0000−0002−6996−7602], Viviane Leite Dias de
Mattos1[0000−0002−3512−6290], Richard F. Pinto1[0009−0007−0176−3383], Diego
Renan Bruno2[0009−0008−1806−0278], Eduardo N. Borges1[0000−0003−1595−7676],
Giancarlo Lucca3[0000−0002−3776−0260], Fabian C. Cardoso4[0000−0002−2842−0387],
and Rafael A. Berri1[0000−0002−3812−4186]
1 Federal University of Rio Grande (FURG), Rio Grande, Brazil
{andreyvinicius, dalmazo, vivianemattos, richard_pinto, eduardoborges,
giancarlo.lucca, rafaelberri}@furg.br
2 Universidade Estadual Paulista (UNESP), São José do Rio Preto, Brazil
diego.bruno@unesp.br
3 University of Rio Verde (UniRV), Rio Verde, Brazil
fabian@unirv.edu.br
Abstract. This article investigates short-term trend forecasting in the
mini-index futures market using a hybrid framework that integrates tech-
nical analysis, feature selection, and evolutionary hyperparameter opti-
mization. Five-minute intraday data obtained from the BovDBV2 database
are used to construct a set of technical indicators that capture short-term
price dynamics. To address the redundancy and noise commonly found
in high-dimensional financial data, a feature selection method is applied
to reduce the original feature space to a compact and informative subset.
Genetic algorithms are then employed to optimize the hyperparameters
of three supervised learning models: Random Forest, Support Vector Ma-
chine, and Multilayer Perceptron. Experimental results indicate that ge-
netic algorithm optimization consistently improves model performance
when compared to a baseline Random Forest model without hyperpa-
rameter tuning, which achieved an accuracy of approximately 61.63%.
Within the proposed framework, the optimized Support Vector Machine
and Multilayer Perceptron models reach test accuracies of 65.61% and
65.85%, respectively, while maintaining balanced F1 −scores across up-
trend and downtrend classes. These results demonstrate the effectiveness
of combining feature selection with evolutionary hyperparameter opti-
mization for short-term financial time series forecasting in derivatives
markets.
Keywords: Neural Networks · Machine Learning · Genetic Algorithm ·
Intraday Trading · Financial Forecasting.


---

<!-- Page 2 -->
## Page 2

2
Andrey V.S Souza et al.
1
Introduction
Futures contracts are financial instruments with high trading volume in the
intraday market, due to their combination of high liquidity and direct exposure
to price fluctuations. They define agreements for the purchase or sale of an
underlying asset at a predetermined price, with settlement on a future date [13].
In Brazil, the futures contract such as Mini Index (WIN), listed on the B3
(Brazilian Stock Exchange)4, concentrates a significant portion of the daily in-
traday volume, drawing attention as a particularly relevant instrument for short-
term forecasting research. These instruments are heavily traded in day trading;
however, identifying reliable patterns for forecasting over such short periods has
been a challenge due to the inherent volatility and dynamic behavior of the time
series. This complexity motivates researchers and professionals to develop more
robust and adaptable modeling approaches.
One of the early approaches to predicting financial time series was the use
of static models like ARIMA [22]; however, because these models assume simple
linearity and temporal dependence, they do not fit well with the highly complex
and dynamic structure of the current financial market. More recently, with the
growing intersection between computing and finance and the increasing avail-
ability of data, methods such as Machine Learning (ML) [14] and Recurrent
Neural Networks (RNN) [10] have emerged, which impose fewer distributional
constraints and can capture non-linear relationships directly from price series.
The best-known ways to "feed" the input to these models is by using math-
ematical values, such as historical price information, market data, and technical
analysis indicators like moving averages, volatility measures, and others. By
using this data with advanced models, we can try to predict market fluctua-
tions [17]. However, to increase the accuracy of the prediction, one of the most
critical steps in building more robust machine learning models is feature selec-
tion, which involves identifying and retaining only the most relevant attributes.
Since not all attributes contribute equally to predictive performance, techniques
such as filtering, encapsulation, or embedding are essential to minimize overfit-
ting and improve model generalization.
Technical indicators derived from price series — moving averages, volatility
measures, among others — serve as input variables in data-driven forecasting
models [17]. Including a large number of them, however, tends to introduce re-
dundancy, which can destabilize model training. Feature selection addresses this
by restricting the input space to the most informative variables. That said, a
reduced feature set does not compensate for poorly chosen hyperparameters.
Genetic Algorithms (GA) [6] have been used in this context to search for con-
figurations that improve generalization beyond what manual tuning typically
achieves.
In parallel, hyperparameter optimization plays a critical role in improving
model performance, particularly in flexible models such as Random Forest (RF)
and Multilayer Perceptron (MLP). Evolutionary approaches, such as Genetic Al-
4 https://www.b3.com.br/


---

<!-- Page 3 -->
## Page 3

Title Suppressed Due to Excessive Length
3
gorithms (GA), are well suited for this task due to their ability to explore complex
and non-convex search spaces [9] and avoid local optima, unlike gradient-based
methods [6].
The main objective of this article is to investigate how the combined ap-
plication of feature selection and evolutionary optimization strategies adapts to
more expressive and sensitive learning models for intraday financial forecasting.
By comparing models that applied these techniques with a Random Forest (RF)
baseline model, we aim to demonstrate that these methods aid in generaliza-
tion to classifiers with greater representational power and exhibit a lower risk of
overfitting. Here, we expand on previous research by jointly optimizing feature
subsets and hyperparameters for Support Vector Machines (SVMs) and Mul-
tilayer Perceptrons (MLPs) using a unified genetic framework, systematically
evaluating robustness and generalization in forecasting financial time series.
The remainder of this article is organized as follows: Section 2 presents the
theoretical background. Section 3 reviews related work. Section 4 describes the
methodology. Section 5 presents and discusses the results. Section 6 concludes
and outlines future directions.
2
Theoretical Concepts
In this section, we aim to contextualize our research by presenting the tech-
nical analysis indicators that are used as input to the models, followed by an
exploration of the feature selection techniques employed.
2.1
Technical Analysis Indicators
Technical analysis indicators are quantitative tools derived from historical as-
set data that are used to predict future market movements. These indicators
help traders identify trends, momentum, and potential reversal points, offering
a systematic approach to interpreting market fluctuations.
Moving Average The moving average is a fundamental statistical technique
used to smooth the volatility inherent in time series data [12]. Different forms
of Moving Averages, such as the Simple Moving Average (SMA) and the Expo-
nential Moving Average (EMA), provide varying degrees of sensitivity to recent
price changes [4]. The use of moving averages in technical analysis helps traders
to filter out the ’noise’ in market data, making it easier to identify support and
resistance levels and to confirm trend directions.
Standard Deviation Standard deviation is a statistical metric that quantifies
price volatility by measuring how much an asset’s price deviates from its mean
over a specific period [1]. In technical analysis, it is calculated by first determining
the moving average (mean) of closing prices and then calculating the squared
differences between each price and that average. The average of these squared
differences produces the variance, and the square root of the variance produces
the standard deviation.


---

<!-- Page 4 -->
## Page 4

4
Andrey V.S Souza et al.
2.2
Machine Learning for Price Prediction
Three supervised learning algorithms are evaluated. Random Forest constructs
multiple decision trees and aggregates their outputs, which provides some ro-
bustness to noise and allows nonlinear relationships to be captured [3]. Support
Vector Machines identify a separating boundary in the feature space, extended
to nonlinear cases through kernel functions. Multilayer Perceptrons are feed-
forward neural networks capable of approximating complex functions through
compositions of linear transformations and nonlinear activations [2, 8]. Since
model performance is sensitive to hyperparameter configuration, evolutionary
optimization is applied to all three classifiers to improve generalization on un-
seen data.
3
Related Work
Machine learning methods have been widely applied to financial forecasting, of-
ten showing better results than traditional econometric models [10]. Ballings et
al. [2], in a study involving data from thousands of European companies, eval-
uated several classifiers and found that Random Forests and SVMs performed
better than logistic regression across most of the tested scenarios [4]. These re-
sults pointed to the relevance of nonlinear methods for capturing patterns in
financial return data, where linear assumptions tend to hold poorly.
M. Ballings et al. [2] evaluated several classifiers using data from European
companies and found that Random Forests and SVMs performed better than
logistic regression across most tested scenarios. The study focused on longer-
term return prediction rather than intraday forecasting. In the present work,
the same classifiers are evaluated, but applied to 5-minute WIN futures data,
where the noise level and pattern persistence differ considerably from the setting
studied by Ballings et al.
F. Ecer [8] investigated how network structure and training configuration
affect MLP performance on financial time series, finding that task-specific adap-
tations produced better out-of-sample results than default settings. The study
did not combine architectural search with feature selection. Here, both aspects
are addressed jointly through a genetic algorithm applied to the same optimiza-
tion process.
Naik and Mohan [18] applied the Boruta algorithm to filter technical indi-
cators before training an ANN on NSE data, reducing prediction error by 12%
compared to the full feature set. Their work treated feature selection as an iso-
lated step, independent of model configuration. The present work extends this
idea by combining feature selection with hyperparameter optimization in a uni-
fied pipeline.
Ding et al. [7] combined back-propagation with a genetic algorithm and re-
ported better generalization compared to standard gradient-based training on
complex datasets. The study focused on the optimization of neural network
weights rather than hyperparameters. In contrast, this work uses GA to search


---

<!-- Page 5 -->
## Page 5

Title Suppressed Due to Excessive Length
5
over the hyperparameter space of three distinct classifiers applied to intraday
financial data.
Taken together, these studies address feature selection and hyperparameter
optimization as separate problems. This work evaluates their combined effect
on intraday trend prediction using WIN futures data from the Brazilian mar-
ket, comparing Random Forest, SVM and MLP under the same experimental
conditions.
4
Methodology
This section presents the methodological steps adopted in the study. Figure 1
summarizes the experimental flow, including data acquisition, feature construc-
tion, feature selection, and model evaluation.
Input Data
Generate
Technical
Indicators
Normalized
Technical
Indicators
Approaches
Adopted
Feature Selection
Method
Genetic Al-
gorithm
Train Models
Evaluation
Metrics
Fig. 1. Overview of the proposed methodology.
4.1
Input Data
The data used in this study were obtained from the BovDbV2 database [20],
an updated version of BovDB [5]. For this work, we used the 5-minute intraday
records available from January to June 2024. This time interval was adopted
because it allows the analysis of short-term price variation while avoiding the
higher noise level usually found in tick-by-tick data.
The study focused on the Mini Index futures contract (WIN), since it is one
of the most actively traded derivatives on B3 and is frequently used in short-
term trading. To keep the analysis aligned with the most liquid contracts in each
period, three rollover intervals were considered: WING24 to WINJ24 (January–
February), WINJ24 to WINM24 (March–April), and WINM24 to WINQ24 (May–


---

<!-- Page 6 -->
## Page 6

6
Andrey V.S Souza et al.
June). After preprocessing, this selection resulted in approximately 120 trading
days and more than 15,000 instances.
The target variable was defined as a binary label indicating the direction of
the next relevant price movement. To obtain this label, we applied the peak-
and-trough detection procedure described in [21] to identify local extrema in the
series. Each instance received label 1 when the following movement was classified
as an uptrend and label 0 when it was classified as a downtrend. This definition
allowed the task to be treated as a binary classification problem.
4.2
Generation of Technical Analysis Indicators
Technical indicators were computed directly from the 5-minute price series. Since
the objective was to capture short intraday movements, only short windows
were considered. The adopted periods were 3, 5, 7, and 9 intervals. Based on
these windows, three types of indicators were generated: Simple Moving Average
(SMA), Exponential Moving Average (EMA), and Standard Deviation (STD).
To capture changes in trend dynamics, we calculated the differences between
the moving averages calculated over different time periods. For example, the
difference between the 7-period SMA and the 3-period SMA is represented in
Eq. (1):
SMA7−3 = SMA7 −SMA3,
(1)
Normalization scales features to a common range (typically [0, 1]) to improve
model adaptability [19]. For every 5-minute interval, we applied a min-max scal-
ing, formulated in Eq. (2):
Featurenorm = Feature −Low
High −Low .
(2)
Here, High and Low define the price limits within each 5-minute window.
After these normalization steps, and combining them with standard daily pricing
features—open, high, low, average, close, buy price, sell price, trading volume,
and number of shares—the resulting dataset totals 66 features.
4.3
Feature Selection Method
This section will discuss how the feature selection step was performed. Since the
complete dataset contained 66 features, a feature selection step was introduced to
reduce redundancy and simplify the search space explored during model fitting.
Among the methods evaluated, Information Gain produced the most stable
results across all training partitions and was therefore adopted for model train-
ing. This criterion estimates how much each feature reduces the uncertainty
about the target class by identifying a compact and informative subset [16],
selecting 7 features from the original 66.
The retained subset includes the 5−3 and 7−3 EMA differences, their nor-
malized counterparts, the normalized 9-period SMA, the 9−3 EMA difference,
and the normalized 7-period EMA.


---

<!-- Page 7 -->
## Page 7

Title Suppressed Due to Excessive Length
7
This reduced subset was then adopted as the fixed input space for the Genetic
Algorithm optimization stage. With fewer input variables, the training process
becomes less affected by irrelevant information, and the search becomes easier
to manage [15]. In practice, this also makes the fitness evaluation more stable
across generations.
4.4
Genetic Algorithm Parameters
Genetic Algorithms (GAs) are evolutionary optimization methods based on se-
lection, crossover, and mutation [9, 11]. In this study, they were used because
hyperparameter tuning involves a discrete and nonlinear search space. By evalu-
ating different candidate solutions over successive generations, GA can gradually
retain the best configurations found during the search.
The GA optimization cycle comprises population initialization, fitness eval-
uation, parent selection, crossover, mutation, and elitist preservation of the best
solution. To ensure methodological consistency and allow a direct comparison
across experiments, the same GA configuration was adopted for all models.
Parent selection was performed using tournament selection with size 3, while
crossover and mutation were applied with fixed probabilities throughout the
optimization process. The adopted configuration is summarized in Table 1.
Table 1. Genetic Algorithm parameters adopted in this study.
Parameter
Value
Number of generations (Ngen) 1000
Population size (Npop)
10
Crossover probability (pc)
0.80
Mutation probability (pm)
0.50
Per-gene mutation probability
0.05
Tournament size
3
Elitism (Hall-of-Fame size)
1
Random seed
42
The fitness of each individual was computed exclusively on the training par-
tition using stratified cross-validation, whereas the test partition was reserved
for the final out-of-sample evaluation. For the Random Forest and Multilayer
Perceptron models, fitness was defined as a weighted combination of training
and validation accuracy in order to promote generalization while discouraging
severe underfitting. The fitness function is given by:
Fitness = 0.4 · Acctrain + 0.6 · Accval,
(3)
The final fitness corresponds to the average value across all folds. After the
optimization stage, the best hyperparameter configuration found by the GA was
used to retrain each model on the full training set before the final evaluation on
the test set.


---

<!-- Page 8 -->
## Page 8

8
Andrey V.S Souza et al.
5
Results
This section presents the results obtained in the experiments. For clarity, it
is divided into two parts. The first describes the experimental setup and data
partitioning procedure, and the second compares the predictive performance of
the evaluated models.
5.1
Experimental Setup and Data Partitioning
To ensure a fair comparison, all models were evaluated under the same experi-
mental conditions. Each algorithm used the same 7-feature input space selected
by the Information Gain criterion Section 4.3, and the same Genetic Algorithm
configuration described in Section 4.4.
Since the dataset presented class imbalance, a balanced sampling procedure
was adopted for the training stage. We selected 1,500 uptrend instances and
1,500 downtrend instances, resulting in a training set with 3,000 observations.
The remaining 12,057 instances were kept as an independent test set. A fixed
random seed was used to make the sampling reproducible.
During the GA optimization stage, model fitness was evaluated using 5-fold
cross-validation on the training set. After the best hyperparameter configuration
was found, each model was retrained on the full 3,000-instance training set and
then evaluated on the 12,057 test instances.
All experiments were executed on the same hardware platform, with a 12-core
CPU and 16 GB of RAM, to allow runtime comparison. Under these conditions,
the complete optimization and training procedure took about 2 hours for Ran-
dom Forest, 3 hours for SVM, and nearly 18 hours for MLP.
5.2
Performance of the Models
Figure 2 shows the evolution of the Random Forest fitness during the GA op-
timization. The cross-validation accuracy increases in the first generations and
then stabilizes, indicating convergence to a more stable region of the search
space and Table 2 presents the search space and the final configuration selected
for Random Forest.
Table 2. Search space optimized by GA for RF
Hyperparameter
Search Space Optimal Value
n_estimators
[50, 500]
200
max_depth
[5, 50]
15
min_samples_split
[2, 20]
4
min_samples_leaf
[1, 20]
1


---

<!-- Page 9 -->
## Page 9

Title Suppressed Due to Excessive Length
9
Fig. 2. Evolution of the fitness function during the Genetic Algorithm optimization of
the Random Forest model, where the x-axis denotes the generation number and the
y-axis represents the average cross-validation accuracy.
The optimized values for n_estimators, max_depth, min_samples_split,
and min_samples_leaf indicate that the GA favored a model with controlled
complexity. The best configuration in the Hall of Fame (HOF) achieved an av-
erage cross-validation accuracy of 0.7739. And in the test set, a final accuracy
of 0.6331. Performance by class remained relatively balanced, with F1 scores of
0.6169 for downtrends and 0.6479 for uptrends.
For the Support Vector Machine (SVM), we defined the kernel as a Radial
Basis Function (RBF), as it is faster to train compared to functions like Poly-
nomial (POLY) and captures trends more quickly.
Figure 3 shows the evolution of the SVM model’s performance throughout
the hyperparameter optimization process using Genetic Algorithm (GA). Com-
pared to Random Forest (RF), the SVM showed less tendency to overfit the
training data, which may be related to its greater generalization capacity in
high-dimensional spaces. The best fitness value obtained was 0.6517, indicating
stable behavior during the optimization process.
Table
3 presents the hyperparameters C and γ and the values obtained
from the search space optimization by GA. While C balances maximizing the
margin and minimizing the error, γ determines the local radius of influence. The
combination of these parameters affects the flexibility and generalization of the
SVM model.
For the test set of 12,057 unseen instances, the model achieved an accuracy
of 0.6561, outperforming the Random Forest. Like the Random Forest, the SVM
achieved balanced performance across trend classes, with greater effectiveness in
detecting uptrends, resulting in F1 scores of 0.6308 and 0.6781 for downtrends
and uptrends, respectively.


---

<!-- Page 10 -->
## Page 10

10
Andrey V.S Souza et al.
Table 3. Search space optimized by the GA for SVM
Hyperparameter
Search Space
Optimal Value
C
log10(C) ∈[−3, 3]
9.75 × 102
γ
log10(γ) ∈[−5, 1]
1.28 × 10−5
Kernel
Fixed
RBF
Fig. 3. Evolution of the fitness function during the Genetic Algorithm optimization of
the SVM model (RBF kernel), where the x-axis denotes the generation number and
the y-axis represents the average cross-validation accuracy.
The Multilayer Perceptron classifier was optimized using GA, following our
methodology. This model is a type of artificial neural network composed of sev-
eral layers of interconnected neurons. It is widely used in machine learning tasks,
such as classification, regression, and pattern recognition, due to its ability to
learn non-linear relationships in data, making it particularly suitable for financial
time series classification problems.
For the MLP, the GA optimized both architectural and training hyperparam-
eters, including the number of hidden neurons, learning rate, L2 regularization,
dropout rate, batch size, activation function, and optimizer.
Figure 4 presents the evolution of MLP fitness over 1,000 generations. The
best individual’s fitness increases gradually and then stabilizes. The average
fitness shows greater variation across generations, which is expected during the
search process.
The GA optimization of the MLP produced fitness values in a relatively nar-
row interval, ranging from 0.6499 to 0.6540 over 1,000 generations. This limited
variation suggests that the search process converged to a stable region of the
hyperparameter space, without large oscillations in performance. The best con-
figuration reached a cross-validation accuracy of 0.6540. Table 4 summarizes the
optimized hyperparameters, their search ranges, and the final values selected by
the GA.


---

<!-- Page 11 -->
## Page 11

Title Suppressed Due to Excessive Length
11
Table 4. Search space optimized by the GA for MLP
Hyperparameter Search Space Optimal Value
Hidden neurons
[5, 500]
44
Learning rate
[10−8, 10−2]
4.70 × 10−3
L2 regularization
[10−8, 10−2]
4.48 × 10−6
Dropout rate
[0.00, 0.10]
0.07
Batch size
{16, . . . , 128}
80
Activation function
Fixed
Tanh
Optimizer
Fixed
RMSprop
Fig. 4. Evolution of the fitness function during the Genetic Algorithm optimization
of the MLP model, where the x-axis denotes the generation number and the y-axis
represents the average cross-validation accuracy.
The selected configuration kept the hidden layer at a moderate size, which is
consistent with the need to control model complexity when dealing with noisy
intraday financial data. The optimization also selected a small L2 regularization
term and a low learning rate, indicating that a more conservative training process
was beneficial for this problem.
With RMSprop and Hyperbolic Tangent activation, the MLP achieved a test
accuracy of 0.6585. This was the highest result among the evaluated models,
slightly exceeding the performance of the SVM and remaining clearly above
that of Random Forest. In the class-specific analysis, the model showed better
performance for uptrends, with an F1-score of 0.6753, compared with 0.6397 for
downtrends.
To evaluate the sensitivity of the Multilayer Perceptron to the optimization
strategy, a second model test experiment was conducted using the same search
space configuration shown in the previous test, as per Table 4, with the only


---

<!-- Page 12 -->
## Page 12

12
Andrey V.S Souza et al.
modification being the optimization algorithm employed during training, which
was Adam.
The best individual found by the GA in this configuration specified a hidden
layer with 89 neurons, a learning rate of 1.94 × 10−3, an L2 regularization coef-
ficient of approximately 8.71 × 10−8, a dropout rate of 0.01 and a batch size of
112, while keeping the hyperbolic tangent activation function as the nonlinear
transformation in the hidden layer.
Table 5. Comparison of MLP performance using different optimizers optimized by the
Genetic Algorithm
Metric
MLP + RMSprop MLP + Adam
GA Fitness (min)
0.6499
0.6471
GA Fitness (max)
0.6540
0.6514
Test Accuracy
0.6585
0.6544
Precision
0.6755
0.6783
Recall
0.6789
0.6623
F1-score
0.6772
0.6702
AUC-ROC
0.7032
0.7023
AUC-PR
0.7029
0.7022
Fig. 5. Comparison between cross-validation and test accuracies obtained for the eval-
uated models.


---

<!-- Page 13 -->
## Page 13

Title Suppressed Due to Excessive Length
13
Table 5 compares two MLP models optimized with RMSprop and Adam,
focusing on min/max GA fitness, final test accuracy, and metrics like AUC-ROC
and AUC-PR.
Table 5 shows both optimizers have similar probabilistic performance, with
nearly identical AUC-ROC and AUC-PR values. The RMSprop-based MLP has
slightly higher cross-validation fitness and test accuracy, while Adam yields
a marginally higher F1-score, indicating the optimizer mainly influences the
precision-recall trade-off rather than causing significant performance differences
in the GA search space.
Figure 5 puts the performance of all three algorithms into perspective. Ran-
dom Forest showed the highest accuracy in cross-validation, but the difference
between validation and test results was greater. This is because tree-based algo-
rithms often suffer from overfitting to the noise inherent in market microstruc-
tures, leading to exactly this type of generalization failure. SVM and MLP based
on RMSprop showed closer results in these two stages; the difference in general-
ization between training and testing is not as large, indicating more consistent
generalization on unseen data. In this comparison, MLP (RMSprop) and SVM
obtained the best results in the tests.
6
Conclusion
Previous results in the Brazilian derivatives market [21] indicated that selecting
intraday Mini-Index technical indicators can reduce computational cost and im-
prove baseline generalization. However, feature selection alone was not sufficient
to obtain the best predictive performance. Without hyperparameter optimiza-
tion, the baseline Random Forest reached a test accuracy of 61.63%.
To improve these results, we introduced a Genetic Algorithm for hyperpa-
rameter optimization and evaluated classifiers with different model structures.
The optimized Random Forest achieved the highest cross-validation accuracy,
but its performance dropped more clearly on the test set. In contrast, SVM and
MLP showed more consistent generalization on unseen data.
These results indicate that, in this problem, the SVM and MLP models
handled noisy and nonlinear intraday patterns more effectively than Random
Forest. Among the evaluated models, the MLP with RMSprop achieved the
highest test accuracy, reaching 65.85%.
Overall, the results suggest that combining feature selection with hyperpa-
rameter optimization is more effective than using a default configuration after
feature reduction alone. Although this framework was applied here to short-term
index forecasting, the same strategy may also be useful in other predictive tasks
involving noisy and non-stationary data.
As a continuation of this study, future experiments may include additional
technical indicators, such as RSI, MACD, and volatility- or volume-based vari-
ables, in order to verify whether the predictive performance can be improved
with a broader representation of market behavior.


---

<!-- Page 14 -->
## Page 14

14
Andrey V.S Souza et al.
Acknowledgment
The authors would like to thank FAPERGS (24/2551-0001396-2, 23/2551-0000773-
8), CNPq (307416/2025-9), FAPERGS/CNPq (23/2551-0000126-8) and the Fesurv-
University of Rio Verde.
References
1. Altman, D.G., Bland, J.M.: Standard deviations and standard errors. Bmj
331(7521), 903 (2005)
2. Ballings, M., Van den Poel, D., Hespeels, N., Gryp, R.: Evaluating multiple classi-
fiers for stock price direction prediction. Expert systems with Applications 42(20),
7046–7056 (2015)
3. Biau, G., Scornet, E.: A random forest guided tour. Test 25(2), 197–227 (2016)
4. Billah, M.M., Sultana, A., Bhuiyan, F., Kaosar, M.G.: Stock price prediction: com-
parison of different moving average techniques using deep learning model. Neural
Computing and Applications 36(11), 5861–5871 (2024)
5. Cardoso, F.C., Malska, J.A.V., Ramiro, P.J., Lucca, G., Borges, E.N., de Mattos,
V.L.D., Berri, R.A.: Bovdb: a data set of stock prices of all companies in b3 from
1995 to 2020. Journal of Information and Data Management 13(1) (2022)
6. Chung, H., Shin, K.s.: Genetic algorithm-optimized long short-term memory net-
work for stock market prediction. Sustainability 10(10), 3765 (2018)
7. Ding, S., Su, C., Yu, J.: An optimizing bp neural network algorithm based on
genetic algorithm. Artificial intelligence review 36(2), 153–162 (2011)
8. Ecer, F., Ardabili, S., Band, S.S., Mosavi, A.: Training multilayer perceptron with
genetic algorithms and particle swarm optimization for modeling stock price index
prediction. Entropy 22(11), 1239 (2020)
9. Goldberg, D.E.: Genetic algorithm in search, optimization and machine learning,
addison. W esley Publishing Company, R eading, MA 1(98), 9 (1989)
10. Heaton, J.B., Polson, N.G., Witte, J.H.: Deep learning for finance: deep portfolios.
Applied Stochastic Models in Business and Industry 33(1), 3–12 (2017)
11. Holland, J.H.: Genetic algorithms and adaptation. In: Adaptive control of ill-
defined systems, pp. 317–333. Springer (1984)
12. Hoque, M.E., Billah, M., Kapar, B., Naeem, M.A.: Quantifying the volatility
spillover dynamics between financial stress and us financial sectors: Evidence from
qvar connectedness. International Review of Financial Analysis 95, 103434 (2024)
13. Jarrow, R.A., Oldfield, G.S.: Forward contracts and futures contracts. Journal of
Financial Economics 9(4), 373–382 (1981)
14. Jiang, W.: Applications of deep learning in stock market prediction: recent
progress. Expert Systems with Applications 184, 115537 (2021)
15. Kumar, V., Minz, S.: Feature selection. SmartCR 4(3), 211–229 (2014)
16. Lei, S.: A feature selection method based on information gain and genetic al-
gorithm. In: 2012 international conference on computer science and electronics
engineering. vol. 2, pp. 355–358. IEEE (2012)
17. Nabipour, M., Nayyeri, P., Jabani, H., Mosavi, A., et al.: Predicting stock market
trends using machine learning and deep learning algorithms via continuous and
binary data; a comparative analysis. Ieee Access 8, 150199–150212 (2020)
18. Naik, N., Mohan, B.R.: Optimal feature selection of technical indicator and
stock prediction using machine learning technique. In: International Conference
on Emerging Technologies in Computer Engineering. pp. 261–268. Springer (2019)


---

<!-- Page 15 -->
## Page 15

Title Suppressed Due to Excessive Length
15
19. Singh, D., Singh, B.: Feature wise normalization: An effective way of normalizing
data. Pattern Recognition 122, 108307 (2022)
20. Souza,
A.S.,
Lucca,
G.,
Borges,
E.N.,
Cardoso,
F.C.,
Dalmazo,
B.L.,
Berri,
R.:
Dataset
for
Intraday
Analysis
of
B3
stock
prices
(2024).
https://doi.org/10.7910/DVN/TMB4IG
21. Souza, A.V., Pinto, R.F., Dalmazo, B.L., Borges, E.N., Lucca, G., Mattos, V.L.d.,
Berri, R.A.: Predictive analysis with technical indicators and features selection for
futures contracts trading. In: International Conference on Computational Science
and Its Applications. pp. 349–367. Springer (2025)
22. Stellwagen, E., Tashman, L.: Arima: The models of box and jenkins. Foresight:
The International Journal of Applied Forecasting (30) (2013)


---
