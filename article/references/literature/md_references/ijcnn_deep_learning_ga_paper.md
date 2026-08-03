# _IJCNN_2026___Andrey__Deep_learning_in_financial_time_series_using_GA
**Original PDF**: `article\references\_IJCNN_2026___Andrey__Deep_learning_in_financial_time_series_using_GA.pdf`
**Page Count**: 6

---

<!-- Page 1 -->
## Page 1

Combining Technical Indicators and Genetic
Algorithms for Short-Term Machine Learning
Prediction of Mini-Index Futures
Abstract—This article investigates short-term trend forecasting
in the mini-index futures market using a hybrid framework
that integrates technical analysis, feature selection, and evolu-
tionary hyperparameter optimization. Five-minute intraday data
obtained from the BovDBV2 database are used to construct a set
of technical indicators that capture short-term price dynamics.
To address the redundancy and noise commonly found in high-
dimensional financial data, a feature selection method is applied
to reduce the original feature space to a compact and informative
subset. Genetic algorithms are then employed to optimize the
hyperparameters of three supervised learning models: Random
Forest, Support Vector Machine, and Multilayer Perceptron.
Experimental results indicate that genetic algorithm optimiza-
tion consistently improves model performance when compared to
a baseline Random Forest model without hyperparameter tuning,
which achieved an accuracy of approximately 61.63%. Within the
proposed framework, the optimized Support Vector Machine and
Multilayer Perceptron models reach test accuracies of 65.61%
and 65.85%, respectively, while maintaining balanced F1−scores
across uptrend and downtrend classes. These results demonstrate
the effectiveness of combining feature selection with evolutionary
hyperparameter optimization for short-term financial time series
forecasting in derivatives markets.
Index Terms—Neural Network, Machine Learning, Genetic
Algorithm, Intraday Trading, Mini Index
I. INTRODUCTION
The financial market is the arena for investing in various
capital instruments traded to achieve economic returns and
manage risk. One of the most sought-after assets by investors
is futures contracts, noted for their high liquidity; they are
widely used for both hedging against price fluctuations and
speculative strategies. These contracts establish the purchase
or sale of an underlying asset at a predetermined price, with
settlement on a future date, making them particularly sensitive
to market expectations and short-term dynamics [1].
Data generated from trading on stock exchanges world-
wide enables the development of assets with both short- and
long-term horizons to identify return patterns that support
investment strategies. However, many of these patterns tend to
dissipate as the market exploits them, reinforcing the dynamic
and uncertain nature of financial series.
In Brazil, the Brazilian Stock Exchange (B31) stands out as
the main regulated trading environment in the country. Among
them, the Mini Index (WIN) futures contract, referenced to
the Ibovespa, has high liquidity and is widely used in short-
term strategies and intraday operations, making it a particularly
1https://www.b3.com.br/
relevant source of data for computational studies of financial
time-series forecasting.
Early attempts to standardize patterns and identify trends
used static, linear models, such as traditional time-series
methods As finance and computing converged (Stock Market
Prediction) [2], more sophisticated models, such as machine
learning (ML) algorithms, gained popularity for market fore-
casting. Recently, deep learning architectures such as Multi-
layer Perceptrons (MLPs) and recurrent neural networks have
expanded these techniques, enabling the learning of complex
patterns from historical data.
A key part of data-driven methods involves technical anal-
ysis using indicators such as moving averages and volatility,
which capture market trends for machine learning [3]. How-
ever, the high dimensionality and redundancy of raw indicators
challenge model training, making feature selection vital to find
the most useful ones. Model performance also relies on proper
hyperparameter tuning, where meta-heuristic techniques like
Genetic Algorithms (GA) [4] effectively explore complex set-
tings and avoid local optima, unlike gradient-based methods.
The objective of this article is to investigate how evolu-
tionary optimization strategies scale with more expressive and
sensitive learning models for intraday financial forecasting.
While feature selection with a Random Forest (RF) baseline
has proven effective, these methods do not always generalize
to classifiers with greater representational power and risk of
overfitting. Here, we extend prior research by jointly optimiz-
ing feature subsets and hyperparameters for Support Vector
Machines (SVM) and Multilayer Perceptrons using a unified
genetic framework, systematically evaluating robustness and
generalization in financial time series forecasting.
The structure of this article is as follows: Section
II
presents related works. Section III describes the methodology
adopted in this study. Section
IV presents and discusses
the experimental results. Finally, Section
V presents the
conclusions and directions for future research.
II. RELATED WORK
With the advancements in artificial intelligence and the
widespread use of concepts such as machine learning and
deep learning in the literature, various sectors—both academic
and industrial—have sought to apply these techniques to their
respective domains. One of these areas is the financial market
[5], where the ability to predict future market values has
attracted considerable attention.


---

<!-- Page 2 -->
## Page 2

In research by Ballings [6], various machine learning tech-
niques were tested for stock market prediction using financial
data from 5,767 European companies. Experimental results
identified SVM as the most accurate model, followed by
Random Forest, Kernel Factory, AdaBoost, and Logistic Re-
gression. These findings highlight the adaptability of machine
learning for financial forecasting and show that model perfor-
mance depends strongly on input feature selection, hyperpa-
rameter tuning, and learning strategies.
In this scenario, the MLP has become a widely used
deep learning architecture in financial forecasting, primarily
because it can capture complex nonlinear relationships among
economic variables. F. Ecer [7] proposed an optimized MLP
architecture for financial time-series forecasting, evaluating
various network topologies and activation functions.
Recent studies show technical analysis indicators are effec-
tive features for machine learning in stock prediction. Naik and
Mohan [8] used Boruta to select relevant indicators from 33
combinations, finding dimensionality reduction boosts short-
term prediction accuracy. Their ANN model cut prediction
error by 12% on NSE data, highlighting the value of selecting
informative features from high-dimensional sets.
Hyperparameter optimization is vital for neural network per-
formance in finance. Ding et al. [9] introduced a hybrid GA-
Back-Propagation (BP) approach to overcome BP networks’
limitations, combining GA’s global search with BP fine-tuning
for better generalization on UCI datasets.
Unlike previous studies that treat feature selection and
hyperparameter tuning separately, this work integrates both
within a unified evolutionary framework and evaluates their
effectiveness across distinct models for financial market time
series prediction.
III. METHOLOGY
This section presents the methodology adopted in this study.
Figure
1 presents an overview of the methodological flow
adopted in this study. The diagram highlights each step of the
process, illustrating the flow from data acquisition to model
optimization and evaluation.
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
Genetic Algorithm
Train Models
Evaluation Metrics
Fig. 1. Overview of the proposed methodology.
A. Input Data
The data used in this article were obtained from the
BovDbV2 [10] database, an extension of the original BovDb
[11] that provides publicly available, pre-processed infor-
mation from the B3 for research purposes, covering listed
companies from 1995 to 2024. This new version also includes
intraday records in 5-minute windows from January to June
2024, enabling a more detailed analysis of short-term market
dynamics.
From this intraday data, a subset of futures contracts
relevant to the objectives of this study was selected, with
emphasis on the WIN, chosen for its high liquidity and
suitability for short-term strategies. The contracts considered
were WING24 and WINJ24 (Jan.–Feb. 2024), WINJ24 and
WINM24 (Mar.–Apr. 2024), and WINM24 and WINQ24
(May–Jun. 2024), selected based on their high volumes and in-
tense trading activity, totaling approximately 38 to 40 business
days per period and more than 15,000 instances throughout the
analyzed set.
The technical analysis indicators used in this study were
computed from these intraday series and serve as the explana-
tory variables in the dataset. In addition, a binary market trend
column was defined, with 0 indicating a downtrend and 1
indicating an uptrend. These labels were derived from a top
and trough identification algorithm presented in previous work.
B. Generation of Technical Analysis Indicators
Technical indicators were built from the intraday dataset to
capture short-term price changes. Key metrics—Simple Mov-
ing Average (SMA), Exponential Moving Average (EMA),
and Standard Deviation—were calculated using short time
windows (3, 5, 7, and 9 periods) to enhance sensitivity to
rapid market shifts, where significant moves can happen in
minutes [12].
To capture changes in trend slope and momentum, attributes
derived from the differences between calculated moving av-
erages were also constructed. For example, the difference
between the 7-period SMA and the 3-period SMA is defined
in Eq. (1) as:
SMA7−3 = SMA7 −SMA3,
(1)
A central preprocessing step consisted of normalizing the
technical indicators [13], as well as the opening and closing
prices, in order to place all variables on a common numerical
scale. For each 5-minute intraday window, a min–max–type
scaling was applied, in which each feature was transformed
according to Eq. (2):
Featurenorm = Feature −Low
High −Low .
(2)
Where High and Low correspond to the maximum and
minimum prices observed within the same 5-minute interval,
and Feature denotes any technical indicator or price-based
variable being normalized. This transformation maps the fea-
tures predominantly to the interval [0, 1], while preserving
their relative positions within the intraday price range, thereby
reducing the impact of heterogeneous attribute scales and
facilitating the learning of machine learning models. This


---

<!-- Page 3 -->
## Page 3

normalization procedure, combined with historical information
on open, high, low, average, close, bid, ask, trade volume, and
number of shares, results in a total of 66 constructed features.
C. Feature Selection Method
The predictive pipeline incorporates a structured feature se-
lection stage based on technical analysis indicators. Following
the approach proposed in [10], multiple selection strategies
are evaluated to identify the most informative feature subsets,
thereby enhancing model discrimination while reducing redun-
dancy and noise inherent in high-dimensional financial data.
Based on the results presented, we evaluated several fea-
ture selection approaches using filters and wrappers. Among
the methods evaluated, the Information Gain Method [14]
demonstrated superior performance in terms of model stability
compared to all other methods tested, showing generalization
and training efficiency when applied to the intraday dataset.
This method identified a compact and informative subset,
selecting 7 features from the original 66.
The selected features, ranked by their Information Gain
scores, include the EMA-based differences 5−3 and 7−3,
their normalized counterparts, the normalized 9-period SMA,
the 9−3 EMA difference, and the normalized 7-period EMA.
This ranked subset was subsequently used as the optimized
input space for training the models using a GA-based hyperpa-
rameter optimization procedure. Limiting the learning space to
key indicators allowed the genetic algorithm’s optimization to
run more efficiently, finding parameters with better predictive
capacity and less variance [15].
D. Genetic Algorithm Parameters
Genetic Algorithms, grounded in the seminal works of
Holland [16] and Goldberg [17], constitute a class of evo-
lutionary optimization methods particularly suitable for high-
dimensional and multimodal search spaces. Their stochastic
nature enables efficient global exploration, mitigating the risk
of premature convergence that frequently affects gradient-
based or exhaustive search strategies. These characteristics are
especially relevant in financial time series modeling, where
nonlinearity, structural regimes, and noise produce highly
irregular loss surfaces.
A fixed configuration of GA parameters was used across
all experiments to ensure methodological consistency and
enable direct model-to-model comparison. The search pro-
ceeds through successive generations, with diversity enforced
via uniform crossover and gene-wise mutation, and selective
pressure maintained through tournament selection.
Evolutionary optimization was performed using a genetic
algorithm with a population of 10 individuals evolved over
1,000 generations. Uniform crossover was applied with a
probability of 0.80, and mutation was performed using a gene-
wise adaptive strategy with a probability of 0.05 per individual
and per gene. Parent selection was based on tournament
selection with a tournament size of three individuals. Model
fitness was evaluated using a parallel cross-validation strategy.
The optimized hyperparameters from this configuration were
then used to retrain the final predictive models.
IV. RESULTS
This section presents the experimental results and discusses
their implications for forecasting short-term movements in
Brazilian Mini Index Futures Contracts. The analysis has two
parts: the first describes the setup and evaluation protocol, and
the second compares the models’ predictive performance.
A. Experimental Setup and Data Partitioning
To ensure a fair and consistent comparison, all models
evaluated in this study were trained and tested under iden-
tical experimental conditions. Each model used the reduced
feature set from the feature selection stage, as described in
Section III-C, consisting of seven technical indicators selected
using the Information Gain criterion. In addition, all models
used the same Genetic Algorithm configuration for hyperpa-
rameter optimization, as detailed in Section III-D.
The dataset was split into training and test sets using a
balanced, reproducible strategy to address class imbalance and
temporal bias. From the intraday data, 1,500 “uptrend” and
1,500 “downtrend” instances were randomly sampled for the
training set, creating a balanced 3,000-instance subset. A fixed
seed ensured reproducibility. The remaining 12,057 instances
were reserved for testing.
To obtain reliable estimates and reduce variance, all models
used 5-fold cross-validation on the training set, splitting data
into five folds, training on four, validating on one, and aver-
aging accuracy. After optimization, models were retrained on
all training data and tested on the unseen set.
All experiments were conducted in the same computa-
tional environment to ensure comparable execution times and
performance metrics. The models were trained on a CPU-
based system with 12 processing cores and 16 GB of RAM.
In this configuration, the MLP required approximately 18
hours to complete optimization and training, while the SVM
required approximately 3 hours and the RF approximately 2
hours. These differences reflect the computational complexity
and search space associated with each genetically optimized
algorithm.
The following subsection presents a comparative analysis
of the predictive performance achieved by each model under
this unified experimental framework.
B. Performance of the Models
This subsection presents and discusses the results obtained
from training and evaluating the proposed models, with initial
emphasis on the performance of the Random Forest model
after hyperparameter optimization using the GA.
Table
I shows the search space defined for each hyper-
parameter, as well as the optimal values found at the end of
the evolutionary process. Each hyperparameter optimized by
the GA plays a distinct role in controlling the complexity and
generalization capacity of the RF model. The n estimators pa-
rameter defines the number of decision trees in the ensemble;
the max depth parameter limits the maximum depth of each
tree; the min samples split parameter specifies the minimum
number of samples required to split an internal node, acting


---

<!-- Page 4 -->
## Page 4

as a regularization mechanism that prevents overly specific
decision rules. Similarly, min samples leaf determines the
minimum number of samples required in a leaf node, resulting
in smoother decision boundaries and increased robustness
against noise.
TABLE I
RANDOM FOREST HYPERPARAMETERS OPTIMIZED BY THE GENETIC
ALGORITHM
Hyperparameter
Search Space
Optimal Value
n estimators
[50, 500]
200
max depth
[5, 50]
15
min samples split
[2, 20]
4
min samples leaf
[1, 20]
1
Figure 2 shows the fitness evolution, measured as average
accuracy from 5-fold cross-validation, across the GA genera-
tions for the Random Forest. It quickly converges initially and
then stabilizes, indicating efficient hyperparameter exploration.
Fig. 2.
Evolution of the fitness function during the Genetic Algorithm
optimization of the Random Forest model, where the x-axis denotes the
generation number and the y-axis represents the average cross-validation
accuracy.
The best individual found by the Hall of Fame (HOF)
showed an average cross-validation accuracy of 0.7739.
In the test set, the model showed a final accuracy of 0.6331.
RF analysis indicates a relatively balanced performance be-
tween the uptrend and downtrend classes, with comparable
levels of recall and accuracy in both categories. Despite this
balance, a non-negligible number of misclassifications occur
in both directions. The resulting F1 values were 0.6169 for the
downtrend class and 0.6479 for the uptrend class, reflecting
moderate but consistent predictive performance.
The SVM classifier, optimized using a Genetic Algorithm,
was configured with a Radial Basis Function (RBF) Kernel,
particularly suitable for capturing nonlinear decision bound-
aries in high-dimensional feature spaces.
Figure 3 shows the fitness function’s evolution during the
genetic algorithm’s optimization of the SVM model. It im-
proves quickly at first, then stabilizes, signifying convergence
to a robust hyperparameter configuration.
The best individual preserved by the HOF achieved a mean
cross-validation accuracy of 0.6517, reflecting stable perfor-
mance across folds and indicating adequate generalization
during training.
Fig. 3.
Evolution of the fitness function during the Genetic Algorithm
optimization of the SVM model (RBF kernel), where the x-axis denotes
the generation number and the y-axis represents the average cross-validation
accuracy.
TABLE II
SVM HYPERPARAMETERS AND SEARCH SPACE OPTIMIZED BY THE
GENETIC ALGORITHM
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
Table II illustrates that the C and gamma hyperparameters
shape the SVM’s behavior; C balances margin maximization
and error minimization, with higher values favoring correct
classification and complexity. gamma determines the local
influence radius, with smaller values smoothing boundaries
and larger ones fitting localized patterns. Their combination af-
fects the SVM’s flexibility and generalization. On a test set of
12,057 unseen instances, the model achieved 0.6561 accuracy,
outperforming the Random Forest. Like the Random Forest,
the SVM achieved balanced performance across trend classes,
with higher effectiveness for uptrend detection, resulting in
F1-scores of 0.6308 and 0.6781 for downtrend and uptrend.
Following our approach, the Multilayer Perceptron classifier
was optimized using a GA. The MLP represents a nonlinear
parametric model capable of approximating complex decision
boundaries through layered compositions of affine transforma-
tions and nonlinear activation functions, making it particularly
suitable for financial time series classification problems.
The Genetic Algorithm was employed to optimize the archi-
tectural and training hyperparameters of the MLP, including
the number of neurons in the hidden layer, the learning rate,
the L2 regularization coefficient, the dropout rate, the batch
size, the activation function, and the optimizer.
Figure 4 shows the fitness evolution over 1,000 generations
of the GA. The best individual’s curve improves gradually
and stabilizes, indicating convergence to a local optimum.
The average fitness varies more, reflecting the exploration and
diversity of solutions.
The best individual identified by the HOF achieved a
mean cross-validation accuracy of approximately 0.6540, with
observed fitness values ranging from 0.6499 to 0.6540 across
generations. The optimal hyperparameter configuration ob-
tained for the MLP model is summarized in Table III.
The number of neurons in the hidden layer affects the
MLP’s capacity. The Genetic Algorithm selected a moderate


---

<!-- Page 5 -->
## Page 5

Fig. 4.
Evolution of the fitness function during the Genetic Algorithm
optimization of the MLP model, where the x-axis denotes the generation
number and the y-axis represents the average cross-validation accuracy.
TABLE III
MLP HYPERPARAMETERS OPTIMIZED BY THE GENETIC ALGORITHM
Hyperparameter
Search Space
Optimal Value
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
size to balance expressiveness and overfitting. An optimized
logarithmic learning rate ensures efficient, stable convergence.
Small L2 regularization penalizes large weights, producing
smoother solutions. Dropout deactivates neurons during train-
ing, improving generalization by reducing co-adaptation.
The final evaluation across the test suite resulted in an
overall accuracy of 0.6585, comparable to the SVM model
and superior to the Random Forest model under identical
experimental conditions, for the model using the Hyperbolic
Tagent Activation Function and RMSprop optimizer.
According to the ranking report, MLP achieved an F1
score of 0.6397 for the downtrend class and 0.6753 for the
uptrend class. These results indicate slightly higher sensitivity
to upward market movements, which is particularly relevant
in financial forecasting contexts, where accurate identification
of positive trends can yield greater practical utility.
To evaluate the sensitivity of the Multilayer Perceptron to
the optimization strategy, a second model test experiment was
conducted using the same search space configuration shown in
the previous test, as per Table III, with the only modification
being the optimization algorithm employed during training,
which was Adam.
The best individual found by the GA in this configuration
specified a hidden layer with 89 neurons, a learning rate of
1.94×10−3, an L2 regularization coefficient of approximately
8.71 × 10−8, a dropout rate of 0.01 and a batch size of 112,
while keeping the hyperbolic tangent activation function as the
nonlinear transformation in the hidden layer.
Table IV compares two MLP models optimized with RM-
Sprop and Adam, focusing on min/max GA fitness, final test
accuracy, and metrics like AUC-ROC and AUC-PR.
TABLE IV
COMPARISON OF MLP PERFORMANCE USING DIFFERENT OPTIMIZERS
OPTIMIZED BY THE GENETIC ALGORITHM
Metric
MLP + RMSprop
MLP + Adam
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
Table IV shows both optimizers have similar probabilistic
performance, with nearly identical AUC-ROC and AUC-PR
values. The RMSprop-based MLP has slightly higher cross-
validation fitness and test accuracy, while Adam yields a
marginally higher F1-score, indicating the optimizer mainly
influences the precision-recall trade-off rather than causing
significant performance differences in the GA search space.
Fig. 5. Comparison of training and test accuracy of all models.
To place these results in a broader context, Figure 5 sum-
marizes the cross-validation and test accuracies obtained by
all models evaluated in this study, namely Random Forest,
SVM, MLP with RMSprop and MLP with Adam. The image
shows that, despite the Random Forest achieving the highest
cross-validation accuracy, its performance deteriorates more
sharply on the test set, whereas SVM and both MLP variants
exhibit more consistent behavior between validation and test,
with MLP (RMSprop) and SVM obtaining the best overall test
accuracies among the compared approaches.
V. CONCLUSION
This work extends the findings of [18], which investi-
gated feature selection strategies for machine learning models
applied to the Brazilian derivatives market. In that study,
technical indicators extracted from intraday Mini-Index futures
data were used to construct a reduced feature space, improving
generalization and reducing computational cost. However, the
Random Forest classifier, trained without hyperparameter op-
timization, achieved a test accuracy of approximately 61.63%,
indicating that feature selection alone is insufficient to fully
address the complexity of intraday financial dynamics.


---

<!-- Page 6 -->
## Page 6

Building upon this foundation, this study advances the
analysis by using a Genetic Algorithm–based hyperparameter
optimization and evaluating more expressive learning mod-
els. Consistent performance gains across classifiers suggest a
highly nonconvex optimization landscape, favoring evolution-
ary strategies over manual or heuristic tuning. While Ran-
dom Forest led in cross-validation accuracy, Support Vector
Machines and Multilayer Perceptrons better balanced cross-
validation and out-of-sample performance.
This behavior shows that margin-based learning and deep
networks perform better at capturing the unpredictable nature
of high-frequency financial data. In particular, the Multilayer
Perceptron trained with RMSprop reached the highest test
accuracy, about 65.85%.
Overall, these findings reinforce the effectiveness of com-
bining feature selection with evolutionary hyperparameter op-
timization, especially when coupled with nonlinear models.
From a methodological perspective, this study supports the
use of hybrid evolutionary–machine learning frameworks as
a robust approach to short-term forecasting in derivatives
markets. It also provides insights that can be generalized to
other noise-dominated, nonstationary prediction tasks.
ACKNOWLEDGMENT
This information has been omitted to allow for blind review.
REFERENCES
[1] R. A. Jarrow and G. S. Oldfield, “Forward contracts and futures
contracts,” Journal of Financial Economics, vol. 9, no. 4, pp. 373–382,
1981.
[2] W. Jiang, “Applications of deep learning in stock market prediction:
recent progress,” Expert Systems with Applications, vol. 184, p. 115537,
2021.
[3] M. Nabipour, P. Nayyeri, H. Jabani, A. Mosavi et al., “Predicting stock
market trends using machine learning and deep learning algorithms via
continuous and binary data; a comparative analysis,” Ieee Access, vol. 8,
pp. 150 199–150 212, 2020.
[4] H. Chung and K.-s. Shin, “Genetic algorithm-optimized long short-term
memory network for stock market prediction,” Sustainability, vol. 10,
no. 10, p. 3765, 2018.
[5] J. B. Heaton, N. G. Polson, and J. H. Witte, “Deep learning for finance:
deep portfolios,” Applied Stochastic Models in Business and Industry,
vol. 33, no. 1, pp. 3–12, 2017.
[6] M. Ballings, D. Van den Poel, N. Hespeels, and R. Gryp, “Evaluating
multiple classifiers for stock price direction prediction,” Expert systems
with Applications, vol. 42, no. 20, pp. 7046–7056, 2015.
[7] F. Ecer, S. Ardabili, S. S. Band, and A. Mosavi, “Training multilayer
perceptron with genetic algorithms and particle swarm optimization for
modeling stock price index prediction,” Entropy, vol. 22, no. 11, p. 1239,
2020.
[8] N. Naik and B. R. Mohan, “Optimal feature selection of technical
indicator and stock prediction using machine learning technique,” in
International Conference on Emerging Technologies in Computer Engi-
neering.
Springer, 2019, pp. 261–268.
[9] S. Ding, C. Su, and J. Yu, “An optimizing bp neural network algorithm
based on genetic algorithm,” Artificial intelligence review, vol. 36, no. 2,
pp. 153–162, 2011.
[10] A. S. Souza, G. Lucca, E. N. Borges, F. C. Cardoso, B. L. Dalmazo,
and R. Berri, “Dataset for intraday analysis of b3 stock prices,” Dataset
for Intraday Analysis of B3 stock prices, 2024.
[11] F. C. Cardoso, J. A. V. Malska, P. J. Ramiro, G. Lucca, E. N. Borges,
V. L. D. de Mattos, and R. A. Berri, “Bovdb: a data set of stock prices
of all companies in b3 from 1995 to 2020,” Journal of Information and
Data Management, vol. 13, no. 1, 2022.
[12] J. S. Hunter, “The exponentially weighted moving average,” Journal of
quality technology, vol. 18, no. 4, pp. 203–210, 1986.
[13] D. Singh and B. Singh, “Feature wise normalization: An effective way
of normalizing data,” Pattern Recognition, vol. 122, p. 108307, 2022.
[14] S. Lei, “A feature selection method based on information gain and ge-
netic algorithm,” in 2012 international conference on computer science
and electronics engineering, vol. 2.
IEEE, 2012, pp. 355–358.
[15] V. Kumar and S. Minz, “Feature selection,” SmartCR, vol. 4, no. 3, pp.
211–229, 2014.
[16] J. H. Holland, “Genetic algorithms and adaptation,” in Adaptive control
of ill-defined systems.
Springer, 1984, pp. 317–333.
[17] D. E. Goldberg, “Genetic algorithm in search, optimization and machine
learning, addison,” W esley Publishing Company, R eading, MA, vol. 1,
no. 98, p. 9, 1989.
[18] A. V. Souza, R. F. Pinto, B. L. Dalmazo, E. N. Borges, G. Lucca, V. L. d.
Mattos, and R. A. Berri, “Predictive analysis with technical indicators
and features selection for futures contracts trading,” in International
Conference on Computational Science and Its Applications.
Springer,
2025, pp. 349–367.


---
