# 2020_a_comprehensive_evaluation_of_ensemble_learning_for_stock_market_prediction

**Source File**: `article\references\nca_search\papers\02_financial_prediction_optimization\2020_a_comprehensive_evaluation_of_ensemble_learning_for_stock_market_prediction.pdf`
**Total Pages**: 40

---

<!-- Page 1 -->
## Page 1

A comprehensive evaluation of ensemble 
learning for stock‑market prediction
Isaac Kofi Nti1,2*  , Adebayo Felix Adekoya1   and Benjamin Asubam Weyori1 
Introduction
The stock market is considered to be a stochastic and challenging real-world envi-
ronment, where the stock-price movements are affected by a considerable number of 
factors [1, 2]. Billions of structured and unstructured data are generated daily from 
the stock market around the globe, increasing the “volume”, “velocity”, “variety” and 
Abstract 
Stock-market prediction using machine-learning technique aims at developing 
effective and efficient models that can provide a better and higher rate of prediction 
accuracy. Numerous ensemble regressors and classifiers have been applied in stock 
market predictions, using different combination techniques. However, three precari-
ous issues come in mind when constructing ensemble classifiers and regressors. The 
first concerns with the choice of base regressor or classifier technique adopted. The 
second concerns the combination techniques used to assemble multiple regressors 
or classifiers and the third concerns with the quantum of regressors or classifiers to be 
ensembled. Subsequently, the number of relevant studies scrutinising these previously 
mentioned concerns are limited. In this study, we performed an extensive comparative 
analysis of ensemble techniques such as boosting, bagging, blending and super learn-
ers (stacking). Using Decision Trees (DT), Support Vector Machine (SVM) and Neural 
Network (NN), we constructed twenty-five (25) different ensembled regressors and 
classifiers. We compared their execution times, accuracy, and error metrics over stock-
data from Ghana Stock Exchange (GSE), Johannesburg Stock Exchange (JSE), Bombay 
Stock Exchange (BSE-SENSEX) and New York Stock Exchange (NYSE), from January 2012 
to December 2018. The study outcome shows that stacking and blending ensemble 
techniques offer higher prediction accuracies (90–100%) and (85.7–100%) respectively, 
compared with that of bagging (53–97.78%) and boosting (52.7–96.32%). Furthermore, 
the root means square error (RMSE) recorded by stacking (0.0001–0.001) and blending 
(0.002–0.01) shows a better fit of ensemble classifiers and regressors based on these 
two techniques in market analyses compared with bagging (0.01–0.11) and boosting 
(0.01–0.443). Finally, the results undoubtedly suggest that an innovative study in the 
domain of stock market direction prediction ought to include ensemble techniques in 
their sets of algorithms.
Keywords:  Machine-learning, Ensemble-classifiers, Artificial intelligence, Predictions, 
Ensemble-regressors, Stacking, Blending
Open Access
© The Author(s) 2020. This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, 
adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and 
the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material 
in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material 
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the 
permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creat​iveco​
mmons​.org/licen​ses/by/4.0/.
RESEARCH
Nti et al. J Big Data            (2020) 7:20  
https://doi.org/10.1186/s40537-020-00299-5
*Correspondence:   
Ntious1@gmail.com 
1 Department of Computer 
Science and Informatics, 
University of Energy 
and Natural Resources, 
Sunyani, Ghana
Full list of author information 
is available at the end of the 
article


---

<!-- Page 2 -->
## Page 2

Page 2 of 40
Nti et al. J Big Data            (2020) 7:20 
“veracity” of stock market data, and making it complex to analyse [1, 3]. In analysing 
this “Big Data” from the stock market, two methods have generally been accepted, 
namely: fundamental analysis and technical analysis. The fundamental analysis 
focuses on the economic trends of local and international milieus, public sentiments, 
financial-statement and assets reported by companies, political conditions and com-
panies associations worldwide [1, 4]. The technical analysis is based on statistical 
analysis, using the historical movement of the stock-prices. Technical indicators such 
as moving-average, dead cross and golden-cross are employed for effective stock trad-
ing decisions. Despite the existence of these techniques, market analysis is still chal-
lenging and open [1].
To overcome the challenges in the stock market analysis, several computational 
models based on soft-computing and machine learning paradigms have been used in 
the stock-market analysis, prediction, and trading. Techniques like Support Vector 
Machine (SVM) [2, 5], DTs [6], neural networks [7], Naïve Bayes [8, 9] and artificial 
neural networks (ANN) [10, 11] were reported to have performed better in stock-
market prediction than conventional arithmetic methods like Logistic regression 
(LR), in respect of error prediction and accuracy. Nevertheless, ensemble learning 
(EL) based on a learning-paradigm that combines multiple learning algorithms, form-
ing committees to improve-predictions (stacking and blending) or decrease variance 
(bagging), and bias (boosting) is believed to perform better than single classifiers and 
regressors [12, 13].
Succinctly, EL techniques have been applied in serval sectors such as health [14], agri-
culture [15], energy [16], oil and gas [17], and finance [12, 18]. In all these applications, 
their reported accuracies support the argument that ensemble classifiers or regressors 
are often far more precise than the discrete classifiers or regressors. For this reason, the 
need for building a better-ensemble classification and regression models has become a 
critical and active research area in supervised learning, with boosting and bagging being 
the most common amalgamation methods used in the literature [16].
Despite numerous works revealing the dominance of ensemble classifier over single 
classifier, most of these studies only ensemble a specific type of classifier or regressor for 
stock-market prediction, such as NN [18–20], DT [21, 22] and SVM [12, 23]. Also, most 
previous studies [12, 19, 21, 22, 24–30], on ensemble methods for stock-market predic-
tions adopted the decrease variance approach (boosting or bagging) and experimented 
with data from one country. Furthermore, a comparison between bagging (BAG) and 
boosting (BOT) combination techniques by [12, 21] revealed that the BAG technique 
outperformed the BOT technique. However, the conclusion of these studies pointed out 
that the performance of ensemble classifiers using boosting or bagging in stock-market 
prediction is territory dependent. Thus, the authors foresee that some ensemble meth-
ods may perform better on data from some parts of the globe than other parts. This 
assumption calls for the application of different ensemble techniques to be benchmarked 
with stock-data from different continents, to ascertain their performance.
Besides, little is known on comparing ensemble classifiers and regressors using differ-
ent combination techniques with same or diverse base learners in predicting the stock 
market. Hence, in stock-market prediction, to the best of our knowledge, there is no 


---

<!-- Page 3 -->
## Page 3

Page 3 of 40
Nti et al. J Big Data            (2020) 7:20 
	
comprehensive comparative study to evaluate the performances of a good pool of diverse 
ensembles regressors and classifiers based on stock-data from three or more continents.
Therefore, this study seeks to perform a comprehensive comparative study of ensem-
ble learning methods for classification and regression machine learning tasks in stock 
market prediction. The following specific objectives aiding this study are as follows:
	 i.	 To bring together the theory of EL and appreciate the algorithms, which use this 
technique.
	ii.	 To review some of the recently published articles on ensemble techniques for clas-
sification and regression machine learning tasks in stock market prediction.
	iii.	 To set up ensemble classifiers and regressors with DTs, SVM and NN using stack-
ing, blending, bagging, and boosting combination techniques.
	iv.	 To examine and compare execution times, accuracy, and error metric of tech-
niques in (iii) over stock data from GSE, JSE, NYSE and BSE-SENSEX.
Hopefully, this paper brings more clarity on which ensembles techniques is best suita-
ble for machine learning tasks in stock market prediction. Again, offer help to beginners 
in the machine-learning field, to make an informed choice concerning ensemble meth-
ods that quickly offer best and accurate results in stock-market prediction. Furthermore, 
we probe the arguments made in [12, 21] about the consistency of ensemble learning 
superiority over stock data from different countries. Finally, this paper contributes to the 
literature in that it is, to the best of our knowledge, the first in stock market prediction to 
make such an extensive comparative analysis of ensemble techniques.
The remaining sections of the paper are organised as follows. “Related works evalu-
ation” section presents a review of related works. In “Procedure of proposed method” 
section, we present a quick dive-into basic and advanced ensemble methods and the 
study procedure. “Predictive models” section discusses the results of empirical stud-
ies. “Ensemble methods (EMs)” section concludes this study and describes avenues for 
future research.
Related works evaluation
Literature has shown that the applications of some powerful ML algorithms have sig-
nificantly improved the accuracy of stock prices classification and prediction [31, 32]. As 
such, ML has drawn the attention in stock market prediction, and several ensemble ML 
techniques have recorded high prediction accuracy in current studies.
Sohangir et al. [33] examined the ability of deep learning techniques such as LSTM 
and CNN to improve the prediction accuracy of the stock using public sentiments. The 
out of the study showed that deep learning technique (CNN) outperformed ML algo-
rithms like Logistic regression and Doc2vec. Their Simulation outcome demonstrated 
the attractiveness of their proposed ensemble method compared with auto-regressive 
integrated moving average, generalised autoregressive conditional heteroscedasticity. 
Likewise, Abe et al. [34] applied a deep neural network technique to predict stock price 
and reported that deep technique is more accurate than shallow neural networks.
An ensemble of state-of-the-art ML techniques, including deep neural networks, RF 
and gradient-boosted trees were proposed in [35], to predict the next day stock price 


---

<!-- Page 4 -->
## Page 4

Page 4 of 40
Nti et al. J Big Data            (2020) 7:20 
return on the S&P 500. Their experimental findings were hopeful, signifying that a sus-
tainable profit prospect in the short-run is exploitable through ML, even in the case of a 
developed-market. Qiu et al. [36] presented a stock prediction model based on ensemble 
ν-Support Vector Regression Model.
Similarly, an ensemble of Bayesian model averaging (BMA), weighted-average least 
squares (WALS), least absolute shrinkage and selection operator (LASSO) using Ada-
Bagging was proposed in [24] to predict stock price. Pasupulety et al. [37] proposed an 
ensemble of extra tree regressor and support vector regressor using stacking to predict 
the stock price based on public sentiment. Pulido et al. [38] ensembled NN with fuzzy 
incorporation (type-1 and type-2) for predicting the stock market [38], they achieved 
a high prediction accuracy by the proposed model compared with single NN classifier. 
An ensemble of trees in an RF using LSboost was carried out [25]; the study achieved 
reduced prediction error.
A Comparison of single, ensemble and integrated ensemble ML techniques to pre-
dict the stock market was carried out in [39]. The study showed that boosting ensem-
ble classifiers outperformed bagged classifiers. Sun et  al. [26] proposed an ensemble 
LSTM using AdaBoost for stock market prediction. Their results show that the pro-
posed AdaBoost-LSTM ensemble outperformed some other single forecasting mod-
els. A homogenous ensemble of time-series models including SVM, logistic regression, 
Lasso regression, polynomial regression, Naive forecast and more was proposed in [40] 
for predicting stock price movement. Likewise, Yang et al. [41] ensembled SVM, RF and 
AdaBoost using voting techniques to predict a buy or sell of stocks for intraday, weekly 
and monthly. The study shows that the ensemble technique outperformed single clas-
sifier in terms of accuracy. Gan et al. [42] proposed an ensemble of feedforward neural 
networks for predicting the stock closing price and reported a higher accuracy in predic-
tion as compared with single feedforward neural networks.
In another study, a 2-phase ensemble framework, including several non-classical dis-
integration models, namely, ensemble empirical mode decomposition, empirical mode 
decomposition, and complete ensemble empirical mode decomposition with adaptive 
noise, and ML models, namely, SVM and NN, was proposed for predicting stock-prices 
[43]. Implementation and evaluation of RF robustness in stocks selection strategy was 
carried out [31]. Using the fundamental and technical dataset, they concluded that in 
sound stocks investment, fundamental features, and long-term technical features are of 
importance to long-term profit. Mehta et al. [44] proposed a weighted ensemble model 
using weighted SVM, LSTM and multiple regression for predicting the stock market. 
Their results show that the ensemble learning technique attained maximum accuracy 
with lesser variance in stock prediction.
Similarly, Assis et  al. [45] proposed an NN ensemble for predicting stock price 
movement. A deep NN ensemble using bagging for stock market prediction was pro-
posed in [29]. The study revealed that assembling several neural networks to predict 
stock price movement is highly accurate than a single deep neural network. Jiang 
et  al. [27] implemented different state-of-the-art ML techniques, including a tree-
based and LSTM ensemble using stacking combination technique to predict stock 
price movement based on both information from the macroeconomic conditions and 


---

<!-- Page 5 -->
## Page 5

Page 5 of 40
Nti et al. J Big Data            (2020) 7:20 
	
historical transaction data. The authors recorded an accuracy of 60–70% on average. 
Kohli et al. [46] examined different ML algorithms (SVM, RF, Gradient Boosting and 
AdaBoost) performance in stock market price prediction. The study showed that Ada-
Boost outperformed Gradient Boosting in terms of predicting accuracy.
The work in [19] presents an ensemble classifier of NN using bagging. Their results 
revealed that the ensemble of NN performs much better than a single NN classifier. 
Equally, Wang et al. [4] proposed an RNN ensemble framework that combines trade-
based features deduced from historical trading records and characteristic features of 
the list companies to perceive stock-price manipulation activities effectively. Their 
experimental results reveal that the proposed RNN ensemble outperforms state-of-
the-art methods in distinguishing stock price manipulation by an average of 29.8% in 
terms of AUC value. Existing studies have shown that ensemble classifiers and regres-
sors are of higher predicting accuracy than a single classifier and regressor.
In the same way, Ballings et  al. [12] compared LR, NN, K-Nearest Neighbour 
(K-NN), and SVM ensembles using bagging and boosting. The study results revealed 
that bagging algorithm (random forest) outperformed boosting algorithm (Ada-
Boost). Nevertheless, the study concluded that the performance of ensemble methods 
is dependent on the domain of the dataset used for the study. Therefore, to obtain a 
generalisation of EL methods, a comprehensive comparison among ensemble meth-
ods using datasets from different continents are required.
Table 1 (Appendix A), present a summary of pertinent studies on stock market pre-
diction using EL based on different combination techniques. We categorised the rel-
evant literature based on (i) the base (weak) learner and the total number used. (ii) 
The type of machine learning task (classification or regression). (iii) The origin of the 
data used for the experimental analysis. (iv) The combination technique used and (v) 
evaluation metric used to contrast and compare the relative metamorphoses.
As observed in Table 1 (Appendix A), creating of ensemble classifiers and regres-
sors in the domain of stock-market predictions has become an area of interest in 
recent studies. However, most of these studies [12, 19, 21, 22, 24–30] were based on 
boosting (BOT) or bagging (BAG) combination method. Only a few [4, 18, 20, 37] 
examined ensemble classifiers or regressors based on stacking or blending combina-
tional technique.
Once more, as shown in Table  1 (Appendix A) most of the studies compared 
between ensemble classifiers [12, 18–20, 22, 23, 28] or regressors [21, 30] machine 
learning algorithms, but not both. On the other hand, literature shows that most 
machine learning algorithms can be used for classification and regression tasks. How-
ever, some are better for classification than regression, while others are vice versa [47, 
48]. Hence a good comparison among ensemble methods should cover both regres-
sion and classification tasks with same weaker learners.
Concerning combination techniques, Table 1 (Appendix A) affirms that a high per-
centage of existing literature used either BAG or BOT for classifier ensembles. Thus, 
only a few minorities examine the performance of different classifier using BAG and 
BOT and Stacking (STK).
Furthermore, the quantity of assembled classifiers in previous studies is diverse, 
whiles some used different numbers, other used fixed of say 10 for comparisons, and 


---

<!-- Page 6 -->
## Page 6

Page 6 of 40
Nti et al. J Big Data            (2020) 7:20 
to the best of our knowledge, previous studies did not compare ensembles classifiers 
and regressor with same single classifiers using same combinational methods.
Considering the above discussions presented in Table  1 (Appendix) carefully it 
leaves a gap for conducting a comprehensive comparison study of ensemble classifiers 
and regressors of the same or a different number of base learners using different com-
bination methods for stock-market prediction.
Procedure of proposed method
This section presents the details of Machine Learning (ML) algorithms adopted in this 
study and their implementation for predicting the stock market.
Predictive models
Like many other studies [18, 19, 21, 23, 49], this study adopts three bases line ML algo-
rithms, namely DT, SVM and NN, based on their superiority for ensemble learning in 
financial analysis.
Decision tree (DT)
DT is a flow-chart-like tree structure that uses a branching technique to clarify every 
single likely result of a decision. The interpretability and simplicity of DT, its low-slung 
computational cost and the ability to represent them graphically have contributed to the 
increase in its use for classification task [50]. An information gain approach was used to 
decide the appropriate property for each node of a generated tree. The test attributes of 
each current node are selected based on the attribute that has the maximum informa-
tion. The operation of a DT on a dataset (DS) is expressed in [51] as follows:
1.	 Estimate the entropy E (S) value of the DS as expressed in Eq. (1). 
where E(S) = entropy of a collection of DS, m = represents the number of classes in 
the system and pi = represents the number of instances proportion that belongs to 
class i.
2.	 Calculate the information gain for an attribute K, in a collection S, as expressed in 
Eq. (2). where E(S) represents the entropy of the entire collection and Su = the set of 
instances that have value u for attribute K. 
Support vector machine (SVM)
SVM is a supervised machine learning tool used for regression and classification tasks 
[52]. SVM serves as the linear separator sandwiched between two data nodes to detect 
(1)
E(S) =
m

i=1
−pi log2pi
(2)
G(S, K) = E(S) −

u∈values(K)
Su
S E(Su).


---

<!-- Page 7 -->
## Page 7

Page 7 of 40
Nti et al. J Big Data            (2020) 7:20 
	
two different classes in the multidimensional environs. The following steps show the 
implementation of SVM.
Let DS be the training dataset, DS =

xi, yi, . . . ,

xn, yn

∈X.R
where i =
(1, 2, 3, . . . , n). The SVM represents DS as points in an N-dimensional space and then 
tries to develop a hyperplane that will split the space into specific class labels with a right 
margin of error [51]. Equations (3) and (4) shows the formula used in the algorithm for 
the SVM optimisation.
The function θ of vectors xi (DS) are mapped in space dimension of higher space. In 
this dimension, the SVM finds a linear separating hyperplane with the best margin. The 
kernel function can be formulated as K(xi, xj) ≡θ(xi)Tθ

xj

. The Radial Basis Function 
(RBF) kernel expressed in Eq. (5) was adopted for this study.
where 

xi −xj

 is the Euclidian distance between two data point.
Neural networks (NN)
NN is a network of interrelated components that accepts input, actuates, and then for-
wards it to the next layer. The NN can be connected in several ways, but in this paper, 
the Multilayer Perceptron (MLP) for the neural network was adopted. The MLP is a 
supervised ML algorithm that studies a function f (.) : RD →Ro, by training on a dataset 
(DS), where (D) represents the dimension of the input DS, and o represents the num-
ber of dimensions of expected output. Given X set of features, and a target y , where 
X = {x1, x2, x3, . . . , xD} , the MLP can learn a non-linear function approximator for 
both regression and classification. MLP trains using Adam, Limited- Memory Broyden-
Fletcher-Goldfarb-Shanno (LBFGS) or Stochastic Gradient Descent. However, for this 
study, the Tikhonov regulariser [53], and Adam (Adaptive Moment Estimation) opti-
miser were adopted. The logistic sigmoid activation function (Eq. 7) was adopted as an 
activation function in each layer. The mapping-functions for individual layer l, are given 
as expressed in Eq. (6). The backpropagation algorithm was used in training the MLP in 
this study.
where W [l] and b[l] represents the weight matrix and bias respectively x is the sum of the 
weighted inputs.
(3)
min
d,bω,
1
2W TW + C
n

i=1
ωi
(4)
subject to yi

W Tθ(xi + b) ≥1 −ωi

,
ωi> 0
(5)
RBF: K

xi, xj

= exp

−y||xi −xj||2
,
y > 0
(6)
Z1 = W [l]T × a[l−1] + b[l]
(7)
g(x) =
1
1 + e−x


---

<!-- Page 8 -->
## Page 8

Page 8 of 40
Nti et al. J Big Data            (2020) 7:20 
Ensemble methods (EMs)
Ensemble methods are prevalent in machine learning and statistics. EMs offers techniques 
to merge multiple single classifiers or predictors to form a committee, to achieve amassed 
decision for better and accurate results than any of the single or base predictors [54, 55]. 
Thus, EMs highlights the strong point and watered-down the feebleness of the single classi-
fiers [54, 55]. Two types of ensemble methods are defined by Opitz and Maclin [55], namely: 
cooperative and competitive ensemble classifiers. Ensemble involves training diverse single 
classifiers independently with the same or different dataset, but not with the same param-
eters. Then, the final prediction (expected output) is obtained by finding an average of all 
individual single or base classifier output (or other similarities). Whiles the cooperative 
ensemble is a divide and conquers based approach. The prediction task is subdivided into 
two or more tasks, where each subtask is sent to the appropriate single classifier based on 
the characteristics and nature of the subtasks, and the final prediction output is obtained 
by the sum of all distinct single or base classifiers. In the creation of ensemble classifier and 
regresses models, three factors need careful consideration. (1) The availability of numer-
ous classification and regression methods makes it difficult to identify which one of them 
is suitable for the application domain. (2) The number of single classifiers or regressors to 
assembled for better and higher accuracy. (3) The amalgamation techniques are suitable for 
combining the outcomes (outputs) of the various single classifiers and regressor to obtain 
the final prediction or output. We present a brief discussion of some basic and advanced 
combination techniques for EL in the subsequent section.
Basic ensemble techniques
In this section, we discuss 3 basic but powerful ensemble methods, namely: (i) Weighted 
averaging (WA) (ii) Max voting (MV) (iii) Averaging.
Max voting (MV)
The primary application of MV is for a classification task. In the MV technique, several 
single classifier models are employed to decide on every data-point. The output of every 
individual or single classifier is taken as a ‘vote’, the final output (decision) is based on the 
majority’s answer. Let ­M1, ­M1 and ­M3 represent single different classifier models, and x_
train and y_train be training datasets, independent and dependent variables respectively. 
While x_test and y_test be independent variables and target variables of the testing data-
set, respectively. Let ­M1, ­M2 and ­M3 be trained separately with the same training dataset, 
thus, M1.ﬁt

xtrain, ytrain

, M2.ﬁt

xtrain, ytrain

 and M3.ﬁt

xtrain, ytrain

 , respectively. Let 

ym1, 
ym2 and 
ym3, represent the predicted output of the respective models. Then, the final 
prediction (Fp) is a simple majority vote among the predicted output.
Averaging
The averaging technique is very similar to the MV technique; however, an average of the 
outputs of all individual or single classifiers represents the final output (decision). However, 
unlike the MV, the averaging technique can be used for both regression and classification 
machine learning task. With models {M1, ­M2 and ­M3} separately trained and tested with 
the same dataset, final prediction (Fp) is the average of individual models, as expressed in 
Eq. (8). where y1, y2, . . . , yn are the predicted output of individual models.


---

<!-- Page 9 -->
## Page 9

Page 9 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Weighted average (WA)
The WA is an extension of the averaging techniques. In WA technique, different 
weights are assigned to every model signifying the prominence of an individual model 
for prediction. However, with WA, ­M1, ­M1 and ­M3 are assigned with different weights 
of say (0.5, 0.2 and 0.7) respectively, then, the final prediction (Fp) given as Eq. (9).
Advanced EL techniques
The following section discusses three advanced combination techniques in brief.
Stacking (STK)
Stacking is an EL technique that makes use of predictions from several models 
(m1, m2, . . . , mn) to construct a new model, where the new model is employed for 
making predictions on the test dataset. STK seeks to increase the predictive power of 
a classifier [16]. The basic idea of STK is to “stack” the predictions of (m1, m2, . . . , mn) 
by a linear combination of weights aj, . . . , (i = 1, . . . , n) as expressed in Eq. (10) [16]. 
The mlens library [56] was used to implement the stacked EL technique in this study.
where the weight vector “a” is learned by a meta-learner.
Blending (BLD)
The blending ensemble approach is like stacking technique. The only difference is 
that, while stacking uses test dataset for prediction blending uses a holdout (valida-
tion) dataset from the training dataset to make predictions. That is predictions take 
place on only the validation dataset from the training dataset. The outcome of the 
predicted dataset and validation dataset is used for building the final model for pre-
dictions on the test dataset.
Bagging (BAG)
Bagging also called bootstrap aggregating involves combining the outcome of several 
models (for instance, N number of K-NNs) to acquire a generalised outcome. Bagging 
employs bootstrapping-sampling techniques to create numerous subsets (bags) of the 
original train dataset with replacement. The bags created by the bagging techniques 
severs as an avenue for the bagging technique to obtain a non-discriminatory idea 
of the sharing (complete set) [48]. The bags’ sizes are lesser than the original dataset. 
Some machine learning algorithms that use the bagging techniques are bagging meta-
estimator and random forest. BAG seeks to decrease the variance of models.
(8)
Fp =
n

i=1
 y1 + y2, .., yn
n

(9)
Fp =

0.5 × y1

+

0.2 × y2

+, . . . , +

0.7 × yn

(10)
fSTK(x) =
n

i=1
aifi(x)


---

<!-- Page 10 -->
## Page 10

Page 10 of 40
Nti et al. J Big Data            (2020) 7:20 
Boosting (BOT)
Boosting also called “meta-algorithm” is a chronological or sequential process, where 
each successive model tries to remedy or correct the errors of the preceding model. 
Here, every successive model depends on the preceding model [57]. A BOT algorithm 
seeks to decrease the model’s bias. Hence, the boosting techniques lump together 
several weak-learners to form a strong leaner. However, the single models might not 
achieve better accuracy of the entire dataset; they perform well for some fragment of 
the dataset. Therefore, each of the single models substantially improves (boosts) the 
performance of the ensemble. Some commonly boosting algorithms are AdaBoost, 
GBM, XGBM, Light GBM and CatBoost.
Study framework
Figure 1 shows the study framework. We adopted STK, BLD, BAG, and BOT combination 
methods and used DTs, SVM and NNs algorithms as discussed above. To build ‘homogene-
ous’ and ‘heterogeneous’ ensemble classifiers and regressor for predicting stock price and 
compare their accuracy and error metrics. The study process, as shown in Fig. 1, is grouped 
into three-phase, namely: (1) Data preprocessing phase. (2) The building of homogenous 
Stacking 
Blending 
Bagging
Boosting
Stock 
Data
Data 
Pre-processing 
DT j
SVM 1
DT 1
NN 1
SVM k
NN i
……….
Accuracy 
Error Metric
Evaluation Metrics
Test Dataset
Train Dataset
Combination Methods
Homogenous Ensembles  
Heterogeneous Ensemble   
Regresses 
Classifiers 
ML Tasks
NN 1
NN 2
NN 3
NN k
….
NN 4
NN 5
SVM 1
SVM 2
SVM 3
SVM k
….
SVM 4
SVM 5
DT 1
DT 2
DT 3
DT k
….
DT 4
DT 5
Fig. 1  Study Framework


---

<!-- Page 11 -->
## Page 11

Page 11 of 40
Nti et al. J Big Data            (2020) 7:20 
	
and heterogeneous ensemble classifiers and regressor models. (3) Comparing the accuracy 
and error metrics of models. We discuss in detail each phase in the following section.
Research data
Market indices were downloaded from the Ghana stock exchange (GSE), the Johan-
nesburg stock exchange (JSE), the New York Stock Exchange (NYSE) and Bombay Stock 
Exchange (BSE-SENSEX) from January 2012 to December 2018, to test ensemble methods 
with datasets from different continents. By doing so, we can verify works that pointed out 
that some ensemble methods might underperform on datasets from some continents [12, 
47]. The datasets consist of daily stock information (year high, year low, previous closing 
price, opening price, closing price, price change, closing bid price, closing offer). To pro-
duce a generalisation of this study, five (5) well-known technical indicators, namely: simple-
moving average (SMA), exponential moving average (EMA), Moving average convergence/
divergence rules (MACD), relative-strength index (RSI), On-balance-volume (OBV), dis-
cussed in [1, 27, 58] were selected and added to some feature from the various dataset. All 
indicators were calculated from 5 fundamental quantities (opening-price, the highest-price, 
the lowest-price, closing price, and trading volume). We aimed at predicting a 30-day-ahead 
closing price and price movement for regression and classification, respectively. The down-
loaded datasets were preprocessed by going through 2 primary stages, namely: (i) data 
cleaning, (ii) data transformation.
Data cleaning
The complexity and stochastic nature of stock data make it always prone to noise, which 
might disturb the ML algorithm from studying the structure and trends in data. The wave-
let transform (WT) expressed in Eq. (11) was applied to free the dataset from noise and 
data inconsistency. We transformed the data Xω, using WT as follows, remove coeffi-
cients (a, b) with values more than standard deviation (STD). Now we inverse transformed 
the new coefficients to get our new data free from noise. The WT was used based on its 
reported ability to adopt and developed the localisation-principle of the short-time Fourier-
transform technique, as-well-as features of good-time frequency characteristics and multi-
resolution [59].
Data transformation
Machine learning algorithms offer higher accuracy and better error metrics when the 
input data is scaled within the same range [60]. The min–max normalisation techniques 
expressed in Eq. (12) guarantees all features will have the same scale [0, 1] as compared with 
other techniques [61], hence adopted for this study.
(11)
Xω(a, b) =
1
√a
∞

−∞
x(t)ϕ
t −b
a

dt
(12)
b′ =
b −bmin
bmax −bmin


---

<!-- Page 12 -->
## Page 12

Page 12 of 40
Nti et al. J Big Data            (2020) 7:20 
where b is the original data value, b′ is the value of b after normalisation, b(max)andb(min) 
are the maximum and minimum values of the input data.
Empirical analysis and discussion
In our quest to achieve a comprehensive comparative study among ensemble tech-
niques, four (4) different stock-datasets were downloaded from Ghana, South Africa, 
United States, and India. Each data had a different number of selected independent vari-
ables (features), as shown in Table 2 (Appendix 1). 10-fold cross-validation (10-CV) was 
adopted and applied in this study to attain an enhanced valuation of training accuracy. 
With the (10-CV) method, the training set was subdivided into ten subsets of training 
data, and nine out the ten were used in training each model. Whiles the remaining one 
(1) was used as test data. This process was repeated ten times, representing the number 
of folds (10-CV). 80% of each dataset was used for training, whiles the remaining 20% 
was for testing.
Figure 2 shows the variation between the open and close stock price of the Bombay 
stock exchange dataset. The graph shows a close range between the opening and closing 
stock price. We observed that the price of the stock went up in January 2018 as com-
pared with all other years during the period of this study. Figure 3 shows a graph of the 
open and close stock price of the NYSE dataset. The graph shows little marginal changes 
between open and closing stock price.
A graph of the open and close price of the GSE data is as shown in Fig. 4. A very close 
variation between open and close is observed in the dataset. Figure 5 shows a plot of the 
JSE dataset. A graph shows some variation in open and close price. 
0
50
100
150
200
250
01-Jan-15
01-Jan-16
01-Jan-17
01-Jan-18
Open Price
Close Price
Fig. 2  Bombay stock exchange dataset overview
0.00
5,000.00
10,000.00
15,000.00
Dec 31, 2018
Sep 25, 2018
Jun 21, 2018
Mar 19, 2018
Dec 11, 2017
Sep 07, 2017
Jun 05, 2017
Mar 01, 2017
Nov 22, 2016
Aug 19, 2016
May 17, 2016
Feb 11, 2016
Nov 05, 2015
Aug 04, 2015
Apr 30, 2015
Jan 26, 2015
Oct 20, 2014
Jul 17, 2014
Apr 11, 2014
Jan 07, 2014
Oct 02, 2013
Jun 28, 2013
Mar 26, 2013
Dec 18, 2012
Sep 12, 2012
Jun 08, 2012
Mar 06, 2012
Close Price
Open Price
Fig. 3  NYSE dataset overview


---

<!-- Page 13 -->
## Page 13

Page 13 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Empirical setup
We constructed twelve homogenous ensemble classifiers and regressors based on bag-
ging and boosting combination techniques and thirteen different classifiers, as seen in 
(Appendix A Table  4) and regressors using stacking, blending and maximum voting 
combination techniques, as seen in (Appendix A Table 5). Our base leaners parameters 
were set as follows: MLP three hidden layer (HL), HL1 and HL2 (with five (5) nodes), and 
HL3 (with ten (10) nodes), the maximum iteration was set to 5000, optimiser = Adam, 
activation = logistic. For SVM, the Radial Basis Function (RBF) kernel was used, and the 
regularisation (C) = 100. The DT setting were, criterion = entropy, max_depth = 4. In all, 
25 models were built in this study using the Scikit-learn Library, the mlens library [56] 
and Python. The number of base-leaners was set in a range of [1–200] for “homogene-
ous” ensemble experiments based on findings in [1] The parameter setting of the SVM 
and MLP were based on the findings of [12]. An Intel Core i5 64bit with 8 GB memory 
laptop was used for the implementation of all experiments.
Model evaluation
There are several evaluation metrics available for measuring the performance of classi-
fiers and regressors [1]. However, twelve (12) accuracy and closeness evaluation metrics 
were selected for evaluating the performance among adopted techniques in this study (see 
Fig. 4  GSE dataset overview
0.00
10,000.00
20,000.00
30,000.00
40,000.00
50,000.00
60,000.00
70,000.00
Dec 31, 2018
Jul 12, 2018
Jan 23, 2018
Aug 04, 2017
Feb 14, 2017
Aug 29, 2016
Mar 07, 2016
Sep 18, 2015
Mar 31, 2015
Oct 13, 2014
Apr 24, 2014
Nov 01, 2013
May 17, 2013
Nov 23, 2012
Jun 11, 2012
Close Price
Open Price
Fig. 5  JSE data


---

<!-- Page 14 -->
## Page 14

Page 14 of 40
Nti et al. J Big Data            (2020) 7:20 
Table 3, Appendix 1). These metrics were selected due to their appropriateness and effec-
tiveness for classification and regression ML tasks in stock market prediction [1, 27, 62].
Results and discussion
This section presents the results and discussions of our experimental.
Homogenous ensembled classifiers by BAG and BOT
The prediction accuracies of the ensemble classifiers over the GSE, BSE, NYSE, and JSE 
datasets are shown in Figs. 6, 7, 8, 9, respectively, where the x-axis represents the num-
ber of base-learners, and the y-axis represents the accuracy of prediction.
We observed that the DT ensemble classifiers by boosting (DTBotc) and bagging 
(DTBagc) obtain an accuracy of 99.98% with (10–200) estimators over the GSE, BSE, 
and NYSE dataset (Figs. 6, 7, 8, 9). The accuracy of the MLP ensemble by bagging 
Fig. 6  Bagging and boosting classifiers accuracy over the GSE dataset
Fig. 7  Bagging and boosting classifiers accuracy over the BSE dataset


---

<!-- Page 15 -->
## Page 15

Page 15 of 40
Nti et al. J Big Data            (2020) 7:20 
	
(MLPBagc) performed better with an accuracy of 100% over the NYSE dataset for 
estimators from (1 to 200), 94–98% over GSE and 92–100% over BSE, while 80–84% 
over JSE dataset. The SVM (SVMBagc) recorded 96–97% over NYSE, 53–60% over 
JSE dataset, 88–89% over GSE dataset.
On an average, the DT ensemble classifier by boosting (DTBotc) recorded an accu-
racy measure of 100% over NYSE, 95.09% over JSE, and 98.52% over GSE and 99.98 
over BSE as shown in Figs. 6, 7, 8 and 9 respectively. While DT ensemble classifier 
via bagging (DTBagc) obtained an accuracy measure of 100% over the NYSE, 79.95% 
over JSE, 98.78% over GSE, and 99.93 over BSE. The MLP ensemble classifier by bag-
ging (MLPBagc) obtained an accuracy of 100% over NYSE, 81.53% over JSE, 97.98% 
over GSE and 98.93 over BSE, while MLP ensemble classifier by boosting (MLP-
Botc) recorded 96.32% over NYSE, 62.45% over JSE dataset, 88.99% over GSE dataset 
and 96.45% over BSE dataset. The SVM ensemble classifier by bagging (SVMBagc) 
recorded an accuracy of 97.43% over NYSE, 54.98% over JSE, 88.87% over GSE and 
93.78 over BSE, while SVM ensemble classifier using boosting (SVMBotc) 52.7% over 
NYSE, 53.02% over JSE dataset, 62.74% over GSE dataset and 62% over BSE dataset.
Fig. 8  Bagging and boosting classifiers accuracy over the NYSE dataset
Fig. 9  Bagging and boosting classifiers accuracy over the JSE dataset


---

<!-- Page 16 -->
## Page 16

Page 16 of 40
Nti et al. J Big Data            (2020) 7:20 
Likewise, it was observed that the DT ensemble classifiers DTBotc and DTBagc per-
formed very-well over NYSE at 100% accuracy with (1–20) estimators as compared 
with the JSE, GSE, and BSE. The high accuracy level of the DT ensemble on NYSE 
might be the fact that the NYSE dataset is the largest (1760) with the highest feature 
(15) when compared with the rest of all the dataset. This outcome might imply that 
ensemble classifier performs best with the larger dataset. The MLP ensemble clas-
sifier through boosting and bagging did perform well over the NYSE and BSE data-
sets, as compared with JSE and GSE datasets. On the other hand, the SVM ensemble 
employing bagging performed very well over NYSE (97.43%), BSE (93.78%) and GSE 
(88.87%) but low accuracy on the JSE (54.98%). Overall, the SVM ensemble by boost-
ing recorded low accuracy on all datasets.
Furthermore, we observed that the performance of DT ensemble classifiers (DTBotc 
and DTBagc) increase with the increase in the number of estimators used. This outcome 
shows that for a higher and better accuracy measure, the number of estimators for DT 
ensemble should be high. On the other hand, the accuracy SVM ensemble via boosting 
and bagging was not directly proportional to the number of estimators. Thus, irrespec-
tive of the number of estimators, the accuracy of the SVM was stable. Although the per-
formance of SVM ensemble as compared with DT ensemble and MLP ensemble was 
low, the outcome obtained implies that when building an ensemble of SVM, the accu-
racy is independent of the number of estimators. The variation in accuracy by classifier 
ensembles over different dataset shows that the accuracy of ensemble methods in stock-
market prediction is dependent on the origin of the data being analysed, which affirms 
literature [12, 21].
Error metrics analysis of homogenous ensembled classifiers
Measuring the performance of classifiers and regressors models based on only the accu-
racy score is not enough for a truthfully [63]. Hence, we further calculated some known 
error metric. Tables 6, 7, 8, 9, 10, 11, 12 and 13 (Appendix A) shows the error metrics 
of DT, SVM, and MLP ensemble classifiers based on boosting and bagging over GSE, 
BSE, NYSE, and the JSE, respectively. The area-under-curve (AUC) of a DT ensemble 
classifier by boosting and bagging (DTBotc and DTBagc) falls within (0.920–1) for one 
estimator to 200 estimators over GSE, BSE and NYSE as shown in Tables 6, 7, 8, 10, 11 
and 12 (Appendix A). Hence, confirms the accuracy score obtained by the DT ensembles 
by boosting and bagging over these datasets shown in Figs. 6, 7, 8 and 9. This finding 
suggests some skill in the prediction by DT ensembles. On the other hand, AUC meas-
ure on JSE dataset falls within 0.5 for one estimator to 0.996 for 200 estimators. The 
F1-score values of the DT ensemble classifiers (DTBotc and DTBagc) shown in Tables 6, 
7, 8, 10, 11 and 12 (Appendix A), shows a balance between recall and precision of the DT 
ensemble classifiers. Again, the values of RMSE and MAE of DT ensembles by bagging 
and boosting (DTBagc and DTBotc respectively) are approximately 0.00 from 10 estima-
tors to 200 estimators, which again confirms that the accuracy of DT ensembles is highly 
dependent on the number of estimators used.
The MLP ensemble classifier by boosting (MLPBotc) recorded AUC values of (0.845–
0.847), (0.938–0.965), (0.934–0.938) and (0.523–0.626) over GSE, BSE, NYSE and JSE 


---

<!-- Page 17 -->
## Page 17

Page 17 of 40
Nti et al. J Big Data            (2020) 7:20 
	
datasets respectively (Appendix A, Tables 6, 7, 8 and 9). Whiles, MLP ensemble classifier 
by bagging (MLPBagc) recorded AUC values of (0.943–0.99) (1–1), (1–1), (0.810–0.811) 
over GSE, BSE, NYSE and JSE datasets respectively for estimators within 1–200 (Appen-
dix A, Tables 10, 11, 12 and 13). The results show that MLP ensemble (MLPBagc) out-
performed (MLPBotc) over GSE, BSE, NYSE and JSE datasets. This implies that an MLP 
ensemble classifier with bagging outperforms MLP ensemble classifier with boosting for 
stock-market prediction.
Though the overall performance of SVM ensemble by boosting and bagging is low 
as compared to DT and MLP ensembles by same combination methods, the AUC, 
RMSE MAE and recall values of SVM ensemble classifier were more moderate over 
the BSE dataset with smaller size of 984 than the GSE, BSE and NYSE datasets, as 
shown in Tables 6, 7, 8, 9, 10, 11, 12 and 13 (Appendix A). This result shows that the 
classical SVM classifier in its natural form is not suitable for the larger dataset. Except 
it is enhanced with techniques such as dimensionality reduction.
Homogenous ensembled regressors by BAG and BOT
In other to ascertain the superiority of same machine learning algorithm as an 
ensemble classifier and regressor, the selected machine learning algorithm DT, MLP 
and SVM were homogeneously ensemble as regressors using bagging and boosting. 
Table 14, 15, 16 and 17 (Appendix A) shows the error metrics obtained by the DT, 
MLP and SVM ensemble regressors over GSE, BSE, NYSE and JSE datasets.
We observed that MLP ensemble regressor by boosting (MLPBotr) and bagging 
(MLPBagr) offered better accuracy of prediction done DT ensemble regressor by bag-
ging (DTBagr) and bossing (DTBotr) over all datasets. This finding shows that MLP as 
ensemble regressor is suitable than DT ensemble regressor by bagging and boosting. 
Again, no significant difference was seen between MLP ensemble by boosting (MLP-
Botr), and that of bagging (MLPBagr) as far as the results of this study is a concern as 
shown in Tables 14, 15, 16 and 17.
The SVM bagged ensemble regressor (SVMBagr) recorded RMSE values of (0.0685–
0.0431), (0.0463–0.0465), (0.11–0.071) and (0.010–0.010) over JSE, NYSE, BSE and 
GSE datasets as shown in Tables 14, 15, 16 and 17 (Appendix A) respectively. While 
the boosted SVM ensemble regressor (SVMBotr) recorded RMSE values of (0.0681–
0.443), (0.0457–0.0455), (0.081–0.056) and (0.010–0.010) over JSE, NYSE, BSE and 
GSE datasets as shown in (Appendix A, Tables 14, 15, 16 and 17) respectively.
Despite the below-average performance of the SVM ensemble classifier on all data-
sets, the results of the SVM ensemble regressor by bagging (SVMBagr) and boosting 
(SVMBotr) obtained better error metrics, which signifies better accuracy levels. The 
outcome suggests that the SVM is suitable for regression than classification when the 
dataset is small. Furthermore, the RMSLE and ­R2 values of (SVMBotr) compared with 
(SVMBagr) values as in Tables 14, 15, 16 and 17 (Appendix A), reveals that boosting is 
more suitable and accurate for SVM ensemble regressors. Subsequently, we observed 
that the SVM ensemble regressor over GSE outperforms NYSE, BSE and JSE datasets. 
Once more, this confirms that ensemble techniques, performance is dependents on 


---

<!-- Page 18 -->
## Page 18

Page 18 of 40
Nti et al. J Big Data            (2020) 7:20 
the origin of the dataset. However, in some cases, the ­(R2) of the SVM was negative, 
indicating that SVM at this case is worse than predicting the mean.
Furthermore, the training and testing time of bagged and boosted regressors are 
higher compared with their counterparts (classifiers). On average, the MLP ensemble 
(regressor and classifier) requires more time for training and testing as the number of 
estimators and dataset size increases.
Heterogeneous ensembled classifier by STK and BLD
The section discusses the empirical results of the heterogeneous selected machine 
learning algorithms (DTs, SVM and NN (MLP)) using stacking, blending and maxi-
mum voting combination techniques.
Accuracy measure of heterogeneous ensembled classifier by STK and BLD
Figure  10 shows the accuracy measure of stacked and blended classifier ensemble 
with DT, NN for (MLP) and SVM classifiers. The stacking ensemble was clustered in 
three models STK_DSN_C (where DT and SVM were the base learners respectively, 
and MLP the meta-learner), STK_SND_C (where SVM and MLP were the base learn-
ers respectively, and DT the meta-learner), and STK_DNS_C (where DT and MLP 
were the base learners respectively and SVM the meta-learner). On the same way, the 
blending ensembles were three, namely: BLD_DSN_C (where DT and SVM were the 
base learners respectively, and MLP the meta-learner), BLD_SND_C (where SVM and 
MLP were the base learners respectively, and DT the meta-learner) and BLD_DNS_C 
(where DT and MLP were the base learners respectively and SVM the meta-learner). 
The maximum voting technique was also used to ensemble DT, SVM and MLP with 
the name vote (DSN).
The results (Fig. 10) Shows an average accuracy of 100% over BSE and NYSE data-
sets, 90% and 98% over JSE and GSE dataset by all stacking ensemble classifiers. How-
ever, all blending ensemble classifiers recorded an average of 100% accuracy over BSE 
and NYSE datasets, but 85.7% and 93.14% over JSE and GSE datasets.
The finding reveals that stacking ensemble classifiers outperforms bagging and 
boosting ensemble classifier over all datasets and blending over GSE dataset. Despite 
only two base classifiers and one meta-classifier as compared to 200 base learners for 
bagging and boosting, stacking, and blending offered higher accuracy. However, the 
GSE
BSE
NYSE
JSE
0.0%
50.0%
100.0%
Datasets
Accuracy (%)
Classifier Ensembles
GSE
BSE
NYSE
JSE
Fig. 10  Heterogeneous ensembles by stacking and blending


---

<!-- Page 19 -->
## Page 19

Page 19 of 40
Nti et al. J Big Data            (2020) 7:20 
	
training time and testing time are far lesser than boosting and bagging of 100–200 
estimators that achieved 100% accuracy.
On the other hand, the accuracy obtained by STK_SND_C (100% and 91.5%), 
STK_DNS_C (100% and 91.5%) and STK_DSN_C (93.4% and 86.3%) over GSE and 
JSE respectively, has a massive implication on building stacked and blended ensemble. 
That is, in building stacking and blending ensemble, the choice of base-learners and 
meta-learner, and how the base learners are position is a significant determinant of 
the accuracy level of the classifier. This outcome also implies for blending ensemble 
classifier, as it is evident in Table 18, 19, 20 and 21 (Appendix A) for (BLD_SND_C).
The higher accuracy obtained by stacking and blending ensemble over BSE and 
NYSE as compared to the JSE and GS shows that ensemble techniques might not per-
form well on all datasets. Though the maximum voting is a simple ensemble tech-
nique Vote (DSN), it showed its ability with better accuracy measure of 97.1%, 100%, 
100% and 87.9% over GSE, BSE, NYSE and JSE respectively.
Error metrics analysis of heterogeneous ensembled classifier by STK and BLD
Table 18, 19, 20 and 21 (Appendix A) shows the error metrics of stacking and blend-
ing ensemble classifier over BSE, GSE, NYSE and JSE, respectively. The average val-
ues 0.9936 (mean), 0.0071 (STD), 0 (RMSE), 0 (MAE) 1 ­(R2), 1 (Precision), 1 (Recall) 
and 1 (AUC) over BSE and NYSE. These values of ­R2 reveal that blending and stack-
ing ensemble classifier is good as compared with the naive mean model and are well 
optimised.
We also observed that the training and testing times of blending classifier ensem-
bles as compared with stacking ensemble classifier overall all datasets were high. 
However, the accuracy of stacking was higher than blending. The study reveals that 
the accuracy of ensemble classifiers is not dependent on the time used by the classi-
fier to learn or predict. Again, the cost-efficient of building blended ensemble is high 
due to higher training and predicting time.
Furthermore, the NYSE dataset was of higher dimension (1760) than the JSE dataset 
(1749). Nonetheless, the training and predicting the time of blending ensemble clas-
sifier over JSE was higher than the NYSE. This result might be due to the noise in the 
JSE dataset, as shown in Fig. 5.
Tables 22, 23, 24 and 25 (Appendix A), shows the error metrics of ensemble regres-
sors by stacking and blending over BSE, GSE, NYSE and JSE, respectively. The blend-
ing and stacking jointly perform well over the NYSE dataset, as shown in Table 24. 
Oddly, stacking ensemble regressor (STK_DSN_R) outperformed all regressors by 
stacking and blending over all datasets. Again, this indicates that the selection and 
position of base learners and the meta-learner is a necessity when building predictive 
ensemble model by stacking or blending. The training and prediction time of ensem-
ble classifiers and regressors by stacking and blending were quite higher, compared 
with ensemble classifiers and regressors through other combination techniques.
To sum-up, stacking combination technique outperformed all other combination 
techniques for ensemble classifier and regressor. However, the DT ensemble with (10–
200) estimators by boosting and bagging did offer good accuracy measure. Though DT 


---

<!-- Page 20 -->
## Page 20

Page 20 of 40
Nti et al. J Big Data            (2020) 7:20 
ensemble by boosting and bagging offered higher accuracy for stock market prediction, 
the selection of estimators requires careful assessment. The selection of the base-learner 
and meta-learner for stacking and boosting ensemble needs careful consideration since 
the wrong choice can profoundly affect model performance in stock-market prediction.
Furthermore, despite the higher accuracy by DT ensembles by boosting and bag-
ging as compared with MLP and SVM ensembles same combination techniques, the 
MLP and SVM ensembles were more stable than DT ensembles. Thus, the number of 
estimators less affected MLP and SVM ensembles. Notwithstanding the number of 
estimators required by the DT ensemble to offer better accuracy as compared to MLP 
and SVM ensemble, for stacking and blending ensemble, the computational cost of 
the DT ensemble is lower. The reason is that the design of MLP, SVM, stacking, and 
blending ensemble is sophisticated, requiring much time in design.
Conclusion
This paper sought to perform an extensive comparative analysis of ensemble methods 
such as bagging, boosting, stacking, and blending for stock-market prediction, using 
stock market indices (dataset) from four countries. Since the performance of ensemble 
regressors and classifiers based on these techniques for stock market prediction have not 
wholly been scrutinised in literature. This study attempts to provide answers to the fol-
lowing questions:
1.	 Which of these amalgamation techniques (as bagging, boosting, stacking, and blend-
ing) is best suitable for regression and classification tasks in stock market prediction?
2.	 Is the performance of ensemble techniques in stock market prediction associated 
with the origin of stock data?
3.	 Again, in building ensemble classifiers and regressors, what is the appropriate num-
ber of estimators required in building a homogenous ensemble?
To obtain answers to these questions, three well-used machine-learning algorithms, 
namely; decision trees (DTs), support vector machine (SVM) and a multilayer percep-
tron (MLP) neural networks, were employed. Using boosting, bagging, stacking, blending 
and simple maximum voting combination techniques, we, constructed twenty-five (25) 
different ensemble regressors and classifiers using DT, MLP and SVM for stock market 
prediction. We experimented our models on four available public stock-data from GSE, 
BSE, NYSE and JSE, and compared their accuracy and error metrics. The obtained result 
revealed that the combination technique (stacking) for building an ensemble classifier or 
regressor outperformed all other combination techniques like boosting, bagging, blend-
ing and simple maximum in stock market prediction. They are followed by blending 
classifier and regressor ensembles and DT ensembles by boosting and bagging. Again, 
it was found that stacking and blending though offered high accuracy; they are compu-
tationally expensive as compared with DT by boosting and bagging, due to their high 
training and testing time. For that reason, DT ensemble of 50–100 estimators by boost-
ing can be taken as a classifier baseline for low-cost computation. However, where higher 
and better accuracy is of vital interest, stacking should be preferred, followed by blend-
ing. To the best of our knowledge, this study is the first to carry out a comprehensive 


---

<!-- Page 21 -->
## Page 21

Page 21 of 40
Nti et al. J Big Data            (2020) 7:20 
	
evaluation of ensemble techniques (bagging, boosting, stacking, and blending) in a stock 
market prediction.
Though the SVM ensemble by boosting and bagging was stable, it suffered some defi-
ciencies concerning input variables (input features) and dataset sizes. This defect was 
overcome when DT and MLP were used as base-learner respectively, and SVM as meta-
learner for stacking and blending ensemble. Thus, the classical SVM algorithm assumes 
that all the features of samples give the same contribution to the target value, which 
is not always accurate in several real problems as pointed out by Chen and Hao [58]. 
Therefore, the practicality of SVM is impacted, due to the problems of choosing suitable 
parameters of SVM (C, σ and ε)..
Hence, in future work, some feature selection and SVM parameter optimisation meth-
ods such as genetic algorithm (GA), principal component analysis (PCA) can be adapted 
to assess the effect of carrying-out feature-selection and SVM parameter setting of the 
classical SVM. Furthermore, we focus on predicting stock market indices, hence we 
used market indices dataset, where underperforming stocks usually are pulled out from 
top-line indices and replaced by outperforming stocks to offer market stability. Another 
focus can be predicting the exact stock prices using ensemble techniques.
Abbreviations
DT: Decision trees; SVM: Support vector machine; NN: Neural network; GSE: Ghana stock exchange; JSE: Johannesburg 
stock exchange; NYSE: York stock exchange; BSE-SENSEX: Bombay stock exchange; ML: Machine learning; EL: Ensemble 
learning; BAG: Bagging; BOT: Boosting; K-NN: K-nearest neighbour; STK: Stacking; EMs: Ensemble methods; WA: Weighted 
averaging; MV: Max voting; BLD: BLD; SMA: Simple-moving average; EMA: Exponential moving average; MACD: Moving 
average convergence/divergence rules; RSI: Relative-strength index; OBV: On-balance-volume; WT: Wavelet transform; 
STD: standard deviation; MLP: Multi-layer perceptron; LBFGS: Broyden–Fletcher–Goldfarb–Shanno; AUC​: Area-under-
curve; LR: Logistic regression; RMSE: Root mean squared error; MAE: Mean absolute error; RMSLE: Root mean squared 
logarithmic error; MedAE: Median absolute error; EVS: Explained variance score; DTBotc: DT ensembles classifier by 
boosting; SVMBotc: SVM ensembles classifier by boosting; MLPBotc: MLP ensembles classifier by boosting; DTBotc: DT 
ensembles classifier by bagging; SVMBagc: SVM ensembles classifier by bagging; MLPBagc: MLP ensembles classifier 
by bagging; DTBotr: DT ensembles regressor by boosting; SVMBotr: SVM ensembles regressor by boosting; MLPBotr: 
MLP ensembles regressor classifier by boosting; DTBotr: DT ensembles regressor by bagging; SVMBagr: SVM ensembles 
regressor by bagging; MLPBagr: MLP ensembles regressor by bagging; PCA: principal component analysis; GA: Genetic 
algorithm; BMA: Bayesian model averaging; WALS: Weighted-average least squares; LASSO: Least absolute shrinkage and 
selection operator; BSE: Bombay stock exchange.
Acknowledgements
Not applicable.
Authors’ contributions
IKN obtained the datasets for the research and explored different methods discussed. AFA and BAW contributed to 
the modification of study objectives and framework. Their rich experience was instrumental in improving our work. All 
authors contributed to the editing and proofreading. All authors read and approved the final manuscript.
Funding
Authors did not receive any funding for this study.
Availability of data and materials
The datasets used and/or analysed during the current study are publicly available.
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Competing interests
The authors declare that they have no competing interests.
Author details
1 Department of Computer Science and Informatics, University of Energy and Natural Resources, Sunyani, Ghana. 
2 Department of Computer Science, Sunyani Technical University, Sunyani, Ghana. 


---

<!-- Page 22 -->
## Page 22

Page 22 of 40
Nti et al. J Big Data            (2020) 7:20 
Appendix A
See Tables 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 and 25.   
Table 1  Comparison of related studies
CV cross-validation, RNN recurrent neural networks, CLF classification, MV majority voting, REG regression, MAPE mean 
absolute percentage error, MLP multi-layer perceptron, RMSE root mean square error
Articles
Base learner
Number 
of weak 
learners
Ensemble 
algorithms 
(combination 
method)
Datasets
Machine 
learning 
task
Evaluation 
methods
Source
Type
CLF
REG
[19]
MLP
BAG
Tokyo stock 
exchange
Stock
√
[18]
SVM and NN
Not stated
STK
S&P 500 index
Stock
√
Cross-validation
[20]
RNN
Not stated
STK
American 
Association 
of Individual 
Investors
Stock
√
Accuracy
[12]
LR, NN, K-NN 
and SVM
BAG, BOT
Amadeus 
database
Stock
√
Operating 
characteristic 
curve (AUC)
[23]
SVM
10
MV
Sao Paulo 
Stock 
Exchange 
Index
Stock
√
10-fold CV
[21]
DT, RF and 
ANN
Not stated
BAG, BOT
U.S stock (S&P 
500)
Stock
√
MAPE, RMSE, ­R2
[30]
RF
200
BAG
NASDAQ
Stock
√
CV, MAPE, RMSE
[22]
RF
30
BAG
NASDAQ
√
Accuracy, preci-
sion
Recall and 
specificity
[24]
BMA WALS and 
LASSO
BOT-BAG
Not stated
stock
√
Out-of-sample 
­R2
[28]
NN
1–5
BAG
Mexican stock 
exchange
Stock
√
[37]
SVM and extra 
tress
1–250
STK
Not stated
Stock
√
RMSE
[25]
Tress
Not stated
BOT
Not stated
Stock
√
RMSE, MAPE 
and MSE
[26]
LSTM
10–50
BOT
S&P 500
Stock
√
MAPE
[41]
SVM, RF
Not stated
Voting
BSE SENSEX
Stock
√
Accuracy
[42]
NN
2–5
Not stated
CIMB stock 
market
Stock
√
MSE, Accuracy
[44]
SVM, LSTM 
and Multiple 
Regression
Not stated
Not stated
Yahoo stock 
data
Stock
√
Accuracy
[45]
NN
30
Not stated
Brazilian stock 
market
Stock
√
Precision and 
recall
[29]
NN
Not stated
BAG
Chinese stock 
market
Stock
√
Accuracy
[27]
Tress and LSTM 50–150
BOT, STK
S&P500 and 
Nasdaq
Stock
√
F-score, AUC 
and accuracy
[4]
RNN
Not stated
STK
Stock
√
AUC, accuracy


---

<!-- Page 23 -->
## Page 23

Page 23 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Table 2  Details of dataset
a  GSE: https​://www.gse.com.gh
b, c  NYSE: https​://www.inves​ting.com
d  BSE: https​://www.bsein​dia.com
Data source
Data size
Period
No. of features
GSEa [Ghana]
1100
January 2012 to December 2017
9
NYSEb [United State]
1760
January 03, 2012 to December 2018
15
JSEc
1749
January 2012 to December 2018
7
BSEd [India]
984
January 2015 to December 2018
12
Table 3  Used evaluation metrics
Where yi is the predicted value produced by the model, ti is the actual value and n = total number of test-dataset. Also, TP 
number of true positive values, TN number of true negative values, FP number of false-positive values, FN number of false-
negative values
Acronym
Full name
Formula
RMSE
Root mean squared error
RMSE =

1
n
n
i=1
(ti −yi)
MAE
Mean absolute error
MAE = 1
n
n
i=1
(ti −yi)
R2
The F1-score
R2 = 2×PR×RR
PR+RR
RMSLE
Root mean squared logarithmic error
RMSLE = √
MSE(log(yn + 1), log(ˆyn + 1

)
ACC​
Accuracy
Acc =
TN+TP
FP+TP+TN+FN
REC
Recall
REC =
TP
TP+FN
PRE
Precision
PRE =
TP
TP+FP
AUC​
Area under ROC curve
AUC =
1
∫
0
TP
(TP+FN)d
FP
(FP+TN =
1
∫
0
TP
P d FP
N
MedAE
Median absolute error
MedAE

y, ˆy

= median
y1 −ˆy1
, . . . ,
yn −ˆyn

EVS
Explained variance score
Mean
Mean
STD
Standard deviation
Table 4  Homogeneous ensemble classifiers and regressors
Base leaner
Machine learning tasks
No. of estimators
Classification
Regression
BAG
BOT
BAG
BOT
Homogeneous ensembles
 DT ensembles
√
√
√
√
1–200
 SVM ensembles
√
√
√
√
1–200
 MLP ensembles
√
√
√
√
1–200
Table 5  Heterogeneous ensembles classifiers and regressors
Base estimators
Meta estimator
Name
Combination 
techniques
Classification
Regression
STK
BLD
MV
DT and SVM
NN
DSN
√
√
√
√
SVM and MLP
DT
SND
√
√
√
√
DT and MLP
SVM
DNS
√
√
√
√
DT, MLP and SVM
Vote (DNS)
√
√


---

<!-- Page 24 -->
## Page 24

Page 24 of 40
Nti et al. J Big Data            (2020) 7:20 
Table 6  Boosting Ensemble Classifiers training time, prediction time and error metrics result on GSE Dataset
Models
No. estimators
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
DTBotc
1
0.863
0.031
0.274
0.075
0.673
0.946
0.925
0.920
0.052
0.005
SVMBotc
1
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
0.313
0.009
MLPBotc
1
0.829
0.073
0.356
0.127
0.450
0.868
0.873
0.845
0.046
0.003
DTBotc
5
0.859
0.027
0.166
0.027
0.881
0.964
0.973
0.964
0.249
0.015
SVMBotc
5
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
1.413
0.020
MLPBotc
5
0.826
0.075
0.375
0.140
0.390
0.880
0.860
0.842
0.130
0.025
DTBotc
10
0.873
0.024
0.000
0.000
1.000
1.000
1.000
1.000
0.670
0.041
SVMBotc
10
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
1.358
0.017
MLPBotc
10
0.857
0.041
0.321
0.103
0.554
0.894
0.897
0.876
0.298
0.023
DTBotc
15
0.873
0.024
0.000
0.000
1.000
1.000
1.000
1.000
0.670
0.041
SVMBotc
15
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
1.358
0.017
MLPBotc
15
0.857
0.041
0.321
0.103
0.554
0.894
0.897
0.876
0.298
0.023
DTBotc
20
0.891
0.027
0.000
0.000
1.000
1.000
1.000
1.000
0.810
0.079
SVMBotc
20
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
1.333
0.019
MLPBotc
20
0.853
0.054
0.336
0.113
0.509
0.881
0.887
0.862
0.262
0.008
DTBotc
50
0.891
0.016
0.000
0.000
1.000
1.000
1.000
1.000
1.918
0.153
SVMBotc
50
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
1.369
0.028
MLPBotc
50
0.851
0.019
0.351
0.123
0.465
0.865
0.877
0.845
0.224
0.013
DTBotc
100
0.895
0.020
0.000
0.000
1.000
1.000
1.000
1.000
5.138
0.344
SVMBotc
100
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
1.628
0.021
MLPBotc
100
0.860
0.035
0.370
0.137
0.405
0.911
0.863
0.860
0.352
0.012
DTBotc
150
0.894
0.022
0.000
0.000
1.000
1.000
1.000
1.000
7.222
0.614
SVMBotc
150
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
1.724
0.022
MLPBotc
150
0.842
0.043
0.356
0.127
0.450
0.871
0.873
0.847
0.435
0.014
DTBotc
200
0.895
0.026
0.000
0.000
1.000
1.000
1.000
1.000
9.392
0.731
SVMBotc
200
0.613
0.037
0.600
0.360
− 0.561
0.640
0.640
0.500
1.636
0.021
MLPBotc
200
0.835
0.028
0.375
0.140
0.390
0.876
0.860
0.840
0.376
0.023


---

<!-- Page 25 -->
## Page 25

Page 25 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Table 7  Boosting ensemble classifiers training time, prediction time and error metrics result on bse dataset
Models
No. estimators
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
DTBotc
1
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.053
0.004
SVMBotc
1
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
0.333
0.013
MLPBotc
1
0.914
0.055
0.233
0.054
0.770
0.953
0.946
0.938
0.041
0.003
DTBotc
5
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.070
0.010
SVMBotc
5
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
1.157
0.104
MLPBotc
5
0.930
0.041
0.193
0.037
0.842
0.964
0.963
0.958
0.231
0.050
DTBotc
10
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.070
0.010
SVMBotc
10
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
1.157
0.104
MLPBotc
10
0.930
0.041
0.193
0.037
0.842
0.964
0.963
0.958
2.310
0.050
DTBotc
15
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.070
0.004
SVMBotc
15
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
1.546
0.058
MLPBotc
15
0.946
0.048
0.202
0.041
0.828
0.932
0.959
0.960
4.020
0.525
DTBotc
20
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.077
0.003
SVMBotc
20
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
1.694
0.058
MLPBotc
20
0.948
0.034
0.130
0.017
0.928
0.991
0.983
0.980
6.680
0.720
DTBotc
50
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.060
0.004
SVMBotc
50
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
2.839
0.037
MLPBotc
50
0.955
0.033
0.184
0.034
0.857
0.964
0.966
0.962
13.050
0.800
DTBotc
100
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.069
0.004
SVMBotc
100
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
5.775
0.058
MLPBotc
100
0.952
0.026
0.175
0.031
0.871
0.956
0.969
0.969
50.200
4.300
DTBotc
150
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.092
0.004
SVMBotc
150
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
8.751
0.049
MLPBotc
150
0.135
0.036
0.193
0.037
0.842
0.947
0.963
0.961
84.300
20.250
DTBotc
200
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.099
0.004
SVMBotc
200
0.596
0.063
0.619
0.383
− 0.621
0.000
0.617
0.500
11.799
0.049
MLPBotc
200
0.946
0.023
0.175
0.031
0.871
0.973
0.969
0.965
75.400
6.600


---

<!-- Page 26 -->
## Page 26

Page 26 of 40
Nti et al. J Big Data            (2020) 7:20 
Table 8  Boosting ensemble classifiers accuracy and error metrics result on NYSE dataset
Models
No. estimators
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
DTBotc
1.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.051
0.003
SVMBotc
1.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
0.966
0.021
MLPBotc
1.000
0.953
0.040
0.257
0.066
0.734
0.952
0.934
0.934
1.500
0.051
DTBotc
5.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.053
0.003
SVMBotc
5.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
2.898
0.129
MLPBotc
5.000
0.976
0.016
0.062
0.004
0.985
1.000
0.996
0.996
3.100
0.200
DTBotc
10.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.058
0.004
SVMBotc
10.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
4.050
0.022
MLPBotc
10.000
0.977
0.032
0.222
0.049
0.802
0.988
0.951
0.953
2.660
0.150
DTBotc
15.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.058
0.005
SVMBotc
15.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
4.850
0.013
MLPBotc
15.000
0.977
0.032
0.222
0.049
0.802
0.988
0.951
0.953
3.990
0.225
DTBotc
20.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.057
0.003
SVMBotc
20.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
3.667
0.109
MLPBotc
20.000
0.965
0.061
0.163
0.027
0.894
0.955
0.973
0.972
5.440
0.260
DTBotc
50.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.057
0.004
SVMBotc
50.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
3.697
0.112
MLPBotc
50.000
0.975
0.032
0.199
0.040
0.840
0.971
0.960
0.961
17.800
1.100
DTBotc
100.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.060
0.144
SVMBotc
100.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
4.592
0.112
MLPBotc
100.000
0.976
0.032
0.250
0.063
0.749
0.955
0.938
0.938
21.100
0.500
DTBotc
150.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.059
0.004
SVMBotc
150.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
4.213
0.115
MLPBotc
150.000
0.989
0.010
0.151
0.023
0.909
0.962
0.977
0.976
57.000
1.350
DTBotc
200.000
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.000
0.075
0.006
SVMBotc
200.000
0.531
0.035
0.688
0.473
− 0.899
0.527
0.527
0.500
4.466
0.212
MLPBotc
200.000
0.984
0.016
0.107
0.011
0.954
0.979
0.989
0.988
54.800
5.400


---

<!-- Page 27 -->
## Page 27

Page 27 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Table 9  Boosting ensemble classifiers training time, prediction time and error metrics result on JSE dataset
Models
No. estimators
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
DTBotc
1
0.587
0.029
0.660
0.436
− 0.752
0.549
0.564
0.535
0.161
0.006
SVMBotc
1
0.527
0.035
0.685
0.469
− 0.882
0.531
0.531
0.500
3.298
0.023
MLPBotc
1
0.573
0.051
0.673
0.453
− 0.821
0.544
0.547
0.523
3.300
0.035
DTBotc
5
0.608
0.036
0.653
0.427
− 0.713
0.555
0.573
0.545
0.472
0.020
SVMBotc
5
0.527
0.035
0.685
0.469
− 0.882
0.531
0.531
0.500
5.110
0.062
MLPBotc
5
0.644
0.092
0.524
0.274
− 0.101
0.919
0.726
0.739
5.350
0.650
DTBotc
10
0.642
0.036
0.512
0.262
− 0.084
0.664
0.718
0.703
1.122
0.086
SVMBotc
10
0.517
0.034
0.675
0.459
− 0.872
0.521
0.521
0.500
4.560
0.103
MLPBotc
10
0.659
0.078
0.628
0.398
− 0.627
0.556
0.582
0.555
8.950
0.400
DTBotc
15
0.652
0.037
0.522
0.272
− 0.094
0.674
0.728
0.713
1.222
0.096
SVMBotc
15
0.527
0.035
0.685
0.469
− 0.882
0.531
0.531
0.500
4.660
0.203
MLPBotc
15
0.669
0.079
0.638
0.408
− 0.637
0.566
0.592
0.565
13.950
0.450
DTBotc
20
0.638
0.042
0.434
0.189
0.243
0.749
0.811
0.801
1.825
0.092
SVMBotc
20
0.527
0.035
0.685
0.469
− 0.882
0.531
0.531
0.500
4.570
0.078
MLPBotc
20
0.705
0.110
0.511
0.261
− 0.048
0.832
0.739
0.746
12.500
0.900
DTBotc
50
0.679
0.032
0.360
0.130
0.480
0.825
0.870
0.864
4.360
0.214
SVMBotc
50
0.527
0.035
0.685
0.469
− 0.882
0.531
0.531
0.500
6.520
0.061
MLPBotc
50
0.697
0.101
0.690
0.476
− 0.912
0.577
0.524
0.533
8.100
0.300
DTBotc
100
0.707
0.032
0.200
0.040
0.839
0.961
0.960
0.960
8.420
0.580
SVMBotc
100
0.527
0.035
0.685
0.469
− 0.882
0.531
0.531
0.500
5.732
0.077
MLPBotc
100
0.736
0.089
0.554
0.307
− 0.232
0.673
0.693
0.685
13.250
0.117
DTBotc
150
0.735
0.034
0.157
0.025
0.901
0.982
0.975
0.976
15.799
0.884
SVMBotc
150
0.527
0.035
0.685
0.469
− 0.882
0.531
0.531
0.500
5.153
0.085
MLPBotc
150
0.688
0.057
0.653
0.427
− 0.713
0.558
0.573
0.549
27.500
1.020
DTBotc
200
0.738
0.035
0.062
0.004
0.985
0.996
0.996
0.996
17.407
0.996
SVMBotc
200
0.527
0.035
0.685
0.469
− 0.882
0.531
0.531
0.500
7.020
0.531
MLPBotc
200
0.706
0.091
0.597
0.356
− 0.430
0.611
0.644
0.626
31.600
0.644


---

<!-- Page 28 -->
## Page 28

Page 28 of 40
Nti et al. J Big Data            (2020) 7:20 
Table 10  Bagging ensemble classifiers training time, predicting time and error metrics result on GSE dataset
Models
No. estimators
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Training time
Testing time
DTBagc:
1
0.857
0.035
0.255
0.065
0.717
0.938
0.935
0.924
0.084
0.009
SVMBagc:
1
0.862
0.039
0.321
0.103
0.554
0.879
0.897
0.868
0.106
0.004
MLPBagc:
1
0.957
0.036
0.227
0.051
0.777
0.957
0.949
0.943
2.080
0.116
DTBagc:
5
0.881
0.020
0.166
0.027
0.881
0.969
0.973
0.966
0.202
0.024
SVMBagc:
5
0.859
0.036
0.346
0.120
0.480
0.862
0.880
0.846
0.412
0.016
MLPBagc:
5
0.972
0.019
0.203
0.041
0.822
0.953
0.959
0.949
12.505
0.652
DTBagc:
10
0.882
0.016
0.131
0.017
0.926
0.979
0.983
0.978
0.404
0.045
SVMBagc:
10
0.862
0.034
0.321
0.103
0.554
0.876
0.897
0.865
0.804
0.048
MLPBagc:
10
0.978
0.020
0.131
0.017
0.926
0.979
0.983
0.978
22.697
1.823
DTBagc:
15
0.878
0.025
0.117
0.014
0.941
0.984
0.986
0.983
0.537
0.050
SVMBagc:
15
0.863
0.034
0.331
0.110
0.524
0.867
0.890
0.856
1.132
0.043
MLPBagc:
15
0.984
0.017
0.117
0.014
0.941
0.989
0.986
0.985
37.923
2.578
DTBagc:
20
0.881
0.020
0.083
0.007
0.970
0.995
0.993
0.993
0.789
0.087
SVMBagc:
20
0.863
0.035
0.336
0.113
0.509
0.867
0.887
0.853
1.872
0.059
MLPBagc:
20
0.982
0.018
0.143
0.021
0.911
0.979
0.979
0.976
55.596
3.145
DTBagc:
50
0.897
0.011
0.000
0.000
1.000
1.000
1.000
1.000
1.927
0.139
SVMBagc:
50
0.863
0.038
0.336
0.113
0.509
0.860
0.887
0.849
3.913
0.143
MLPBagc:
50
0.971
0.022
0.117
0.014
0.941
0.984
0.986
0.983
144.367
7.525
DTBagc:
100
0.893
0.016
0.000
0.000
1.000
1.000
1.000
1.000
3.267
0.240
SVMBagc:
100
0.862
0.035
0.331
0.110
0.524
0.860
0.890
0.852
10.105
0.367
MLPBagc:
100
0.976
0.016
0.083
0.007
0.970
0.995
0.993
0.993
308.796
16.173
DTBagc:
150
0.894
0.014
0.000
0.000
1.000
1.000
1.000
1.000
5.475
0.378
SVMBagc:
150
0.860
0.034
0.331
0.110
0.524
0.864
0.890
0.854
15.336
0.461
MLPBagc:
150
0.975
0.016
0.101
0.010
0.955
0.989
0.990
0.988
430.847
23.734
DTBagc:
200
0.888
0.017
0.000
0.000
1.000
1.000
1.000
1.000
6.641
0.495
SVMBagc:
200
0.862
0.037
0.336
0.113
0.509
0.863
0.887
0.851
18.557
0.688
MLPBagc:
200
0.969
0.022
0.083
0.007
0.970
0.989
0.993
0.990
536.433
34.095


---

<!-- Page 29 -->
## Page 29

Page 29 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Table 11  Bagging ensemble classifiers training time, predicting time and error metrics result on BSE dataset
Models
No. estimators
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
train time
Test time
DTBagc:
1
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.095
0.011
SVMBagc:
1
0.907
0.044
0.291
0.085
0.641
0.968
0.915
0.89
0.096
0.011
MLPBagc:
1
0.977
0.021
0.285
0.081
0.656
0.845
0.919
0.93
0.939
0.045
DTBagc:
5
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.283
0.024
SVMBagc:
5
0.911
0.035
0.254
0.064
0.727
0.980
0.936
0.92
0.449
0.056
MLPBagc:
5
0.987
0.014
0.101
0.010
0.957
0.982
0.990
0.99
3.929
0.256
DTBagc:
10
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.303
0.068
SVMBagc:
10
0.911
0.028
0.279
0.078
0.670
0.989
0.922
0.90
0.751
0.135
MLPBagc:
10
0.993
0.012
0.058
0.003
0.986
0.991
0.997
1.00
9.663
0.739
DTBagc:
15
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.550
0.036
SVMBagc:
15
0.911
0.028
0.279
0.078
0.670
0.989
0.922
0.90
1.516
0.230
MLPBagc:
15
0.991
0.012
0.000
0.000
1.000
1.000
1.000
1.00
12.232
0.855
DTBagc:
20
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
2.511
0.060
SVMBagc:
20
0.962
0.024
0.154
0.024
0.900
0.991
0.976
0.97
5.048
0.225
MLPBagc:
20
0.996
0.007
0.000
0.000
1.000
1.000
1.000
1.00
103.208
1.127
DTBagc:
50
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
1.254
0.124
SVMBagc:
50
0.917
0.029
0.154
0.024
0.900
0.991
0.976
0.97
4.245
0.525
MLPBagc:
50
0.993
0.010
0.000
0.000
1.000
1.000
1.000
1.00
58.650
3.288
DTBagc:
100
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
2.509
0.234
SVMBagc:
100
0.916
0.031
0.273
0.075
0.684
0.989
0.925
0.90
9.770
1.066
MLPBagc:
100
0.994
0.010
0.000
0.000
1.000
1.000
1.000
1.00
107.326
7.407
DTBagc:
150
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
3.794
0.395
SVMBagc:
150
0.914
0.032
0.285
0.081
0.656
0.989
0.919
0.90
14.122
1.345
MLPBagc:
150
0.994
0.010
0.000
0.000
1.000
1.000
1.000
1.00
0.010
9.248
DTBagc:
200
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
4.628
0.554
SVMBagc:
200
0.913
0.033
0.285
0.081
0.656
1.000
0.919
0.89
16.874
1.963
MLPBagc:
200
0.994
0.010
0.000
0.000
1.000
1.000
1.000
1.00
248.903
15.745


---

<!-- Page 30 -->
## Page 30

Page 30 of 40
Nti et al. J Big Data            (2020) 7:20 
Table 12  Bagging ensemble classifiers accuracy and error metrics result on NYSE dataset
Models
No. of estimators
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
DTBagc:
1
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.095
0.009
SVMBagc:
1
0.980
0.015
0.179
0.032
0.871
0.982
0.968
0.97
0.112
0.006
MLPBagc:
1
0.997
0.005
0.000
0.000
1.000
1.000
1.000
1.00
0.567
0.060
DTBagc:
5
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.243
0.023
SVMBagc:
5
0.983
0.013
0.115
0.013
0.947
0.986
0.987
0.99
0.470
0.018
MLPBagc:
5
0.999
0.002
0.000
0.000
1.000
1.000
1.000
1.00
2.293
0.266
DTBagc:
10
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.299
0.035
SVMBagc:
10
0.986
0.010
0.151
0.023
0.909
0.972
0.977
0.98
0.968
0.036
MLPBagc:
10
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
6.361
0.579
DTBagc:
15
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.404
0.075
SVMBagc:
15
0.986
0.008
0.163
0.027
0.894
0.965
0.973
0.97
1.732
0.061
MLPBagc:
15
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
11.362
0.678
DTBagc:
20
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
0.597
0.104
SVMBagc:
20
0.987
0.009
0.157
0.025
0.901
0.972
0.975
0.98
1.762
0.111
MLPBagc:
20
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
11.613
1.274
DTBagc:
50
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
2.997
1.037
SVMBagc:
50
0.987
0.009
0.163
0.027
0.894
0.968
0.973
0.97
10.942
0.487
MLPBagc:
50
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
85.596
8.087
DTBagc:
100
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
9.973
0.798
SVMBagc:
100
0.989
0.007
0.163
0.027
0.894
0.968
0.973
0.97
32.817
1.042
MLPBagc:
100
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
207.098
17.046
DTBagc:
150
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
13.123
1.343
SVMBagc:
150
0.988
0.010
0.169
0.028
0.886
0.968
0.972
0.97
46.707
3.002
MLPBagc:
150
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
300.789
34.477
DTBagc:
200
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
18.437
1.691
SVMBagc:
200
0.988
0.010
0.174
0.030
0.878
0.965
0.970
0.97
66.954
3.035
MLPBagc:
200
1.000
0.000
0.000
0.000
1.000
1.000
1.000
1.00
442.953
30.594


---

<!-- Page 31 -->
## Page 31

Page 31 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Table 13  Bagging ensemble classifiers training time, predicting time and error metrics result on JSE dataset
Models
No. of estimators
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Training time
Test time
DTBagc:
1
0.698
0.040
0.412
0.170
0.319
0.835
0.830
0.829
0.366
0.012
SVMBagc:
1
0.555
0.033
0.683
0.467
− 0.874
0.532
0.533
0.502
0.335
0.013
MLPBagc:
1
0.809
0.057
0.436
0.190
0.235
0.786
0.810
0.805
2.280
0.187
DTBagc:
5
0.736
0.032
0.185
0.034
0.862
0.964
0.966
0.965
0.490
0.028
SVMBagc:
5
0.585
0.062
0.683
0.467
− 0.874
0.532
0.533
0.502
1.551
0.039
MLPBagc:
5
0.864
0.017
0.436
0.190
0.235
0.790
0.810
0.805
11.782
1.043
DTBagc:
10
0.751
0.034
0.145
0.021
0.916
0.993
0.979
0.980
0.763
0.053
SVMBagc:
10
0.586
0.069
0.669
0.448
− 0.798
0.575
0.552
0.549
2.840
0.066
MLPBagc:
10
0.863
0.022
0.432
0.187
0.250
0.801
0.813
0.810
23.923
1.489
DTBagc:
15
0.772
0.027
0.107
0.011
0.954
0.989
0.989
0.989
0.978
0.107
SVMBagc:
15
0.568
0.047
0.650
0.423
− 0.698
0.564
0.577
0.556
4.869
0.124
MLPBagc:
15
0.867
0.022
0.428
0.183
0.266
0.802
0.817
0.814
39.900
3.282
DTBagc:
20
0.760
0.032
0.123
0.015
0.939
0.989
0.985
0.985
1.502
0.245
SVMBagc:
20
0.563
0.049
0.626
0.392
− 0.576
0.586
0.608
0.589
5.280
0.236
MLPBagc:
20
0.867
0.024
0.434
0.189
0.243
0.802
0.811
0.808
39.325
2.625
DTBagc:
50
0.767
0.038
0.044
0.002
0.992
0.996
0.998
0.998
3.109
0.188
SVMBagc:
50
0.569
0.059
0.683
0.467
− 0.874
0.532
0.533
0.502
18.013
0.362
MLPBagc:
50
0.869
0.021
0.432
0.187
0.250
0.803
0.813
0.810
132.852
10.885
DTBagc:
100
0.770
0.034
0.000
0.000
1.000
1.000
1.000
1.000
8.923
0.432
SVMBagc:
100
0.568
0.059
0.679
0.461
− 0.851
0.536
0.539
0.508
39.565
0.802
MLPBagc:
100
0.868
0.022
0.434
0.189
0.243
0.802
0.811
0.808
270.825
22.026
DTBagc:
150
0.770
0.031
0.000
0.000
1.000
1.000
1.000
1.000
11.446
0.432
SVMBagc:
150
0.565
0.056
0.679
0.461
− 0.851
0.536
0.539
0.508
58.771
0.802
MLPBagc:
150
0.868
0.020
0.434
0.189
0.243
0.802
0.811
0.808
395.453
22.026
DTBagc:
200
0.771
0.034
0.000
0.000
1.000
1.000
1.000
1.000
13.760
0.772
SVMBagc:
200
0.563
0.056
0.683
0.467
− 0.874
0.532
0.533
0.502
63.858
1.388
MLPBagc:
200
0.870
0.023
0.434
0.189
0.243
0.798
0.811
0.808
548.328
33.102


---

<!-- Page 32 -->
## Page 32

Page 32 of 40
Nti et al. J Big Data            (2020) 7:20 
Table 14  Bagging and boosting ensemble regressors error metrics result over JSE dataset
Models
No. 
of estimators
RMSE
MAE
R2
EVS
MedAE
RMSLE
Train time
Test time
DTBagr
1
0.2043
0.1426
0.9153
0.9154
0.0932
0.0372
0.005
0.0010
SVMBagr
1
0.0685
0.0641
0.9905
0.9983
0.0691
0.0121
0.008
0.0020
MLPBagr
1
0.0363
0.0277
0.9973
0.9973
0.0218
0.0061
0.338
0.0010
DTBotr
1
0.2344
0.1974
0.8885
0.8886
0.1882
0.0423
0.004
0.0010
SVMBotr
1
0.0681
0.0636
0.9906
0.9982
0.0676
0.0121
0.018
0.0010
MLPBotr
1
0.0339
0.0257
0.9977
0.9977
0.0192
0.0057
1.449
0.0010
DTBagr
5
0.0984
0.0809
0.9803
0.9803
0.0721
0.0175
0.015
0.0020
SVMBagr
5
0.0574
0.0526
0.9933
0.9982
0.0562
0.0101
0.018
0.0010
MLPBagr
5
0.0313
0.0240
0.9980
0.9980
0.0196
0.0053
3.025
0.0030
DTBotr
5
0.1554
0.1175
0.9510
0.9511
0.0827
0.0305
0.014
0.0020
SVMBotr
5
0.0610
0.0559
0.9925
0.9981
0.0590
0.0108
0.043
0.0010
MLPBotr
5
0.0324
0.0249
0.9979
0.9979
0.0195
0.0054
1.467
0.0030
DTBagr
15
0.1076
0.0904
0.9765
0.9765
0.0800
0.0194
0.031
0.0020
SVMBagr
15
0.0460
0.0406
0.9957
0.9981
0.0417
0.0077
0.054
0.0050
MLPBagr
15
0.0292
0.0221
0.9983
0.9983
0.0191
0.0049
7.054
0.0070
DTBotr
15
0.0820
0.0667
0.9864
0.9864
0.0591
0.0141
0.042
0.0040
SVMBotr
15
0.0389
0.0325
0.9969
0.9979
0.0300
0.0064
0.170
0.0080
MLPBotr
15
0.0321
0.0247
0.9979
0.9980
0.0199
0.0054
7.174
0.0060
DTBagr
20
0.1030
0.0877
0.9785
0.9785
0.0802
0.0184
0.030
0.0030
SVMBagr
20
0.0482
0.0430
0.9953
0.9982
0.0444
0.0081
0.061
0.0060
MLPBagr
20
0.0294
0.0223
0.9983
0.9983
0.0189
0.0049
9.403
0.0190
DTBotr
20
0.0746
0.0592
0.9887
0.9887
0.0500
0.0125
0.071
0.0060
SVMBotr
20
0.0443
0.0384
0.9960
0.9981
0.0382
0.0073
0.202
0.0110
MLPBotr
20
0.0319
0.0247
0.9979
0.9980
0.0203
0.0054
10.910
0.0270
DTBagr
50
0.0989
0.0811
0.9801
0.9801
0.0727
0.0174
0.117
0.0100
SVMBagr
50
0.0449
0.0391
0.9959
0.9980
0.0387
0.0074
0.235
0.0190
MLPBagr
50
0.0305
0.0232
0.9981
0.9981
0.0189
0.0051
27.088
0.0210
DTBotr
50
0.0568
0.0444
0.9934
0.9935
0.0368
0.0095
0.133
0.0150
SVMBotr
50
0.0443
0.0384
0.9960
0.9981
0.0382
0.0073
0.357
0.0140
MLPBotr
50
0.0322
0.0258
0.9979
0.9981
0.0229
0.0054
33.004
0.0290
DTBagr
100
0.0988
0.0840
0.9802
0.9802
0.0836
0.0173
0.537
0.0860
SVMBagr
100
0.0442
0.0382
0.9960
0.9980
0.0369
0.0073
1.220
0.0340
MLPBagr
100
0.0303
0.0230
0.9981
0.9981
0.0188
0.0051
52.394
0.0530
DTBotr
100
0.0557
0.0449
0.9937
0.9938
0.0399
0.0093
0.248
0.0150
SVMBotr
100
0.0443
0.0384
0.9960
0.9981
0.0382
0.0073
0.388
0.0150
MLPBotr
100
0.0327
0.0265
0.9978
0.9981
0.0239
0.0055
40.600
0.0400
DTBagr
150
0.1023
0.0871
0.9788
0.9788
0.0868
0.0176
0.320
0.0420
SVMBagr
150
0.0427
0.0365
0.9963
0.9979
0.0344
0.0070
1.923
0.0480
MLPBagr
150
0.0307
0.0233
0.9981
0.9981
0.0189
0.0051
69.295
0.2220
DTBotr
150
0.0525
0.0431
0.9944
0.9945
0.0393
0.0089
0.442
0.0300
SVMBotr
150
0.0443
0.0384
0.9960
0.9981
0.0382
0.0073
1.448
0.0300
MLPBotr
150
0.0327
0.0265
0.9978
0.9981
0.0239
0.0055
36.989
0.0310
DTBagr
200
0.1054
0.0897
0.9775
0.9775
0.0896
0.0180
0.366
0.0420
SVMBagr
200
0.0431
0.0370
0.9962
0.9980
0.0349
0.0071
0.574
0.0470
MLPBagr
200
0.0309
0.0235
0.9981
0.9981
0.0191
0.0052
91.345
0.1000
DTBotr
200
0.0519
0.0431
0.9945
0.9947
0.0398
0.0088
0.540
0.0380
SVMBotr
200
0.0443
0.0384
0.9960
0.9981
0.0382
0.0073
0.262
0.0090
MLPBotr
200
0.0327
0.0265
0.9978
0.9981
0.0239
0.0055
42.799
0.0450


---

<!-- Page 33 -->
## Page 33

Page 33 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Table 15  Bagging and  boosting ensemble regressors error metrics result over  NYSE 
dataset
Models
No. 
of estimators
RMSE
MAE
R2
EVS
MedAE
RMSLE
Train time
Test time
DTBagr
1
0.0438
0.0327
0.9024
0.9024
0.0244
0.0218
0.004
0.002
SVMBagr
1
0.0463
0.0358
0.8908
0.8918
0.0258
0.0228
0.004
0.002
MLPBagr
1
0.0135
0.0115
0.9907
0.9948
0.0111
0.0066
0.131
0.003
DTBotr
1
0.0457
0.0369
0.8937
0.8937
0.0320
0.0227
0.004
0.001
SVMBotr
1
0.0463
0.0358
0.8908
0.8918
0.0258
0.0228
0.004
0.001
MLPBotr
1
0.0089
0.0064
0.9959
0.9965
0.0048
0.0043
0.152
0.001
DTBagr
5
0.0283
0.0233
0.9591
0.9593
0.0201
0.0142
0.011
0.002
SVMBagr
5
0.0456
0.0354
0.8940
0.8959
0.0249
0.0224
0.010
0.001
MLPBagr
5
0.0083
0.0062
0.9965
0.9981
0.0048
0.0041
2.160
0.002
DTBotr
5
0.0193
0.0145
0.9810
0.9811
0.0114
0.0093
0.012
0.002
SVMBotr
5
0.0465
0.0361
0.8901
0.8918
0.0253
0.0228
0.018
0.002
MLPBotr
5
0.0070
0.0047
0.9975
0.9981
0.0032
0.0034
0.491
0.002
DTBagr
15
0.0295
0.0250
0.9555
0.9556
0.0233
0.0149
0.029
0.007
SVMBagr
15
0.0465
0.0361
0.8899
0.8922
0.0256
0.0228
0.025
0.009
MLPBagr
15
0.0088
0.0068
0.9960
0.9984
0.0055
0.0043
3.590
0.020
DTBotr
15
0.0193
0.0153
0.9810
0.9811
0.0127
0.0093
0.093
0.009
SVMBotr
15
0.0455
0.0354
0.8947
0.8970
0.0252
0.0223
0.145
0.029
MLPBotr
15
0.0075
0.0055
0.9971
0.9984
0.0042
0.0037
2.557
0.007
DTBagr
20
0.0268
0.0235
0.9634
0.9635
0.0224
0.0134
0.036
0.006
SVMBagr
20
0.0465
0.0361
0.8900
0.8920
0.0253
0.0228
0.033
0.007
MLPBagr
20
0.0091
0.0072
0.9958
0.9984
0.0057
0.0044
3.767
0.011
DTBotr
20
0.0179
0.0139
0.9837
0.9837
0.0116
0.0085
0.041
0.005
SVMBotr
20
0.0455
0.0354
0.8947
0.8970
0.0252
0.0223
0.045
0.005
MLPBotr
20
0.0076
0.0055
0.9971
0.9984
0.0041
0.0037
3.305
0.009
DTBagr
50
0.0223
0.0189
0.9747
0.9747
0.0175
0.0110
0.084
0.009
SVMBagr
50
0.0465
0.0361
0.8900
0.8924
0.0256
0.0228
0.078
0.023
MLPBagr
50
0.0094
0.0076
0.9955
0.9983
0.0065
0.0046
8.237
0.022
DTBotr
50
0.0167
0.0138
0.9858
0.9858
0.0123
0.0081
0.111
0.010
SVMBotr
50
0.0455
0.0354
0.8947
0.8970
0.0252
0.0223
0.148
0.013
MLPBotr
50
0.0079
0.0058
0.9968
0.9982
0.0044
0.0039
6.851
0.014
DTBagr
100
0.0217
0.0187
0.9759
0.9759
0.0180
0.0108
0.150
0.016
SVMBagr
100
0.0465
0.0361
0.8900
0.8924
0.0255
0.0228
0.155
0.023
MLPBagr
100
0.0094
0.0076
0.9955
0.9984
0.0063
0.0046
19.791
0.058
DTBotr
100
0.0127
0.0107
0.9918
0.9918
0.0100
0.0062
0.424
0.026
SVMBotr
100
0.0455
0.0354
0.8947
0.8970
0.0252
0.0223
0.291
0.069
MLPBotr
100
0.0079
0.0058
0.9968
0.9982
0.0044
0.0039
6.788
0.015
DTBagr
150
0.0214
0.0188
0.9767
0.9767
0.0183
0.0105
0.271
0.058
SVMBagr
150
0.0464
0.0361
0.8903
0.8926
0.0255
0.0227
0.169
0.035
MLPBagr
150
0.0095
0.0077
0.9954
0.9983
0.0064
0.0046
24.502
0.071
DTBotr
150
0.0118
0.0098
0.9929
0.9929
0.0087
0.0057
0.502
0.044
SVMBotr
150
0.0455
0.0354
0.8947
0.8970
0.0252
0.0223
1.018
0.174
MLPBotr
150
0.0079
0.0058
0.9968
0.9982
0.0044
0.0039
6.617
0.015
DTBagr
200
0.0222
0.0195
0.9750
0.9750
0.0188
0.0108
0.860
0.378
SVMBagr
200
0.0465
0.0361
0.8900
0.8925
0.0257
0.0227
1.091
0.064
MLPBagr
200
0.0095
0.0076
0.9954
0.9983
0.0063
0.0046
35.916
0.092
DTBotr
200
0.0109
0.0090
0.9939
0.9939
0.0080
0.0053
0.521
0.063
SVMBotr
200
0.0455
0.0354
0.8947
0.8970
0.0252
0.0223
0.545
0.042
MLPBotr
200
0.0079
0.0058
0.9968
0.9982
0.0044
0.0039
4.847
0.068


---

<!-- Page 34 -->
## Page 34

Page 34 of 40
Nti et al. J Big Data            (2020) 7:20 
Table 16  Bagging and boosting ensemble regressors error metrics result over BSE dataset
Models
No. 
of estimators
RMSE
MAE
R2
EVS
MedAE
RMSLE
Train time
Test time
DTBagr
1
0.266
0.213
0.449
0.451
0.210
0.129
0.014
0.004
SVMBagr
1
0.110
0.069
0.906
0.908
0.051
0.051
0.007
0.001
MLPBagr
1
0.061
0.034
0.971
0.972
0.021
0.028
0.141
0.002
DTBotr
1
0.104
0.073
0.916
0.917
0.052
0.046
0.004
0.000
SVMBotr
1
0.081
0.057
0.949
0.949
0.048
0.040
0.005
0.001
MLPBotr
1
0.036
0.026
0.990
0.991
0.023
0.019
0.187
0.001
DTBagr
5
0.091
0.069
0.935
0.935
0.056
0.041
0.015
0.002
SVMBagr
5
0.081
0.057
0.949
0.949
0.046
0.039
0.013
0.003
MLPBagr
5
0.026
0.014
0.995
0.995
0.008
0.013
0.678
0.003
DTBotr
5
0.080
0.060
0.950
0.951
0.047
0.036
0.014
0.001
SVMBotr
5
0.060
0.049
0.972
0.973
0.046
0.030
0.021
0.004
MLPBotr
5
0.027
0.017
0.994
0.995
0.013
0.013
0.799
0.003
DTBagr
15
0.083
0.069
0.946
0.946
0.063
0.039
0.038
0.004
SVMBagr
15
0.076
0.056
0.956
0.956
0.047
0.037
0.034
0.011
MLPBagr
15
0.021
0.014
0.996
0.997
0.010
0.010
3.829
0.006
DTBotr
15
0.069
0.054
0.963
0.963
0.044
0.032
0.096
0.012
SVMBotr
15
0.057
0.047
0.975
0.975
0.043
0.029
0.224
0.039
MLPBotr
15
0.016
0.011
0.998
0.998
0.008
0.007
4.987
0.023
DTBagr
20
0.089
0.075
0.939
0.939
0.072
0.042
0.068
0.006
SVMBagr
20
0.075
0.055
0.956
0.956
0.044
0.037
0.040
0.013
MLPBagr
20
0.021
0.014
0.996
0.997
0.010
0.010
4.038
0.021
DTBotr
20
0.077
0.057
0.954
0.955
0.044
0.033
0.058
0.006
SVMBotr
20
0.057
0.047
0.975
0.976
0.043
0.028
0.089
0.020
MLPBotr
20
0.014
0.010
0.999
0.999
0.008
0.006
4.824
0.009
DTBagr
50
0.078
0.064
0.953
0.953
0.057
0.037
0.114
0.010
SVMBagr
50
0.072
0.054
0.960
0.960
0.044
0.036
0.226
0.056
MLPBagr
50
0.014
0.010
0.999
0.999
0.007
0.007
13.967
0.021
DTBotr
50
0.047
0.038
0.983
0.983
0.033
0.023
0.211
0.010
SVMBotr
50
0.056
0.047
0.975
0.976
0.044
0.028
0.186
0.039
MLPBotr
50
0.013
0.009
0.999
0.999
0.006
0.006
22.515
0.019
DTBagr
100
0.075
0.061
0.956
0.956
0.055
0.036
0.325
0.045
SVMBagr
100
0.073
0.054
0.959
0.959
0.045
0.036
0.559
0.127
MLPBagr
100
0.014
0.010
0.999
0.999
0.008
0.007
34.135
0.053
DTBotr
100
0.039
0.032
0.988
0.988
0.029
0.020
0.315
0.021
SVMBotr
100
0.056
0.047
0.975
0.976
0.044
0.028
0.787
0.357
MLPBotr
100
0.011
0.008
0.999
0.999
0.006
0.005
28.182
0.039
DTBagr
150
0.073
0.059
0.959
0.959
0.053
0.035
0.339
0.042
SVMBagr
150
0.072
0.054
0.960
0.960
0.045
0.036
0.401
0.119
MLPBagr
150
0.013
0.010
0.999
0.999
0.008
0.007
30.237
0.082
DTBotr
150
0.038
0.031
0.989
0.990
0.028
0.019
0.345
0.024
SVMBotr
150
0.056
0.047
0.975
0.976
0.044
0.028
0.115
0.019
MLPBotr
150
0.011
0.008
0.999
0.999
0.006
0.005
24.404
0.187
DTBagr
200
0.073
0.060
0.958
0.958
0.055
0.035
0.786
0.043
SVMBagr
200
0.071
0.054
0.960
0.961
0.044
0.035
0.487
0.100
MLPBagr
200
0.013
0.010
0.999
0.999
0.008
0.007
38.432
0.091
DTBotr
200
0.035
0.028
0.990
0.991
0.024
0.018
0.453
0.027
SVMBotr
200
0.056
0.047
0.975
0.976
0.044
0.028
0.126
0.021
MLPBotr
200
0.011
0.008
0.999
0.999
0.006
0.005
24.178
0.039


---

<!-- Page 35 -->
## Page 35

Page 35 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Table 17  Bagging and boosting ensemble regressors error metrics result over GSE dataset
Models
No. 
of estimators
RMSE
MAE
R2
EVS
MedAE
RMSLE
Train time
Test time
DTBagr
1
0.002
0.001
0.961
0.961
0.001
0.002
0.006
0.002
SVMBagr
1
0.010
0.008
− 0.217
0.000
0.009
0.009
0.005
0.001
MLPBagr
1
0.011
0.009
− 0.713
− 0.669
0.009
0.011
0.242
0.014
DTBotr
1
0.003
0.002
0.882
0.882
0.002
0.003
0.004
0.001
SVMBotr
1
0.010
0.008
− 0.217
0.000
0.009
0.009
0.005
0.001
MLPBotr
1
0.010
0.008
− 0.323
− 0.323
0.006
0.010
0.156
0.001
DTBagr
5
0.001
0.001
0.973
0.973
0.001
0.001
0.019
0.002
SVMBagr
5
0.010
0.008
− 0.217
0.000
0.009
0.009
0.022
0.002
MLPBagr
5
0.004
0.003
0.742
0.755
0.003
0.004
0.526
0.003
DTBotr
5
0.002
0.002
0.931
0.931
0.001
0.002
0.013
0.001
SVMBotr
5
0.010
0.008
− 0.217
0.000
0.009
0.009
0.144
0.011
MLPBotr
5
0.007
0.004
0.407
0.408
0.003
0.006
1.919
0.003
DTBagr
15
0.002
0.001
0.970
0.970
0.001
0.001
0.047
0.005
SVMBagr
15
0.010
0.008
− 0.216
0.000
0.009
0.009
0.045
0.005
MLPBagr
15
0.003
0.002
0.887
0.895
0.002
0.003
1.531
0.008
DTBotr
15
0.001
0.001
0.980
0.980
0.001
0.001
0.075
0.022
SVMBotr
15
0.010
0.008
− 0.217
0.000
0.009
0.009
0.171
0.013
MLPBotr
15
0.004
0.003
0.825
0.829
0.002
0.004
2.223
0.005
DTBagr
20
0.001
0.001
0.975
0.975
0.975
0.001
0.041
0.004
SVMBagr
20
0.010
0.008
− 0.220
0.000
0.220
0.009
0.029
0.005
MLPBagr
20
0.002
0.001
0.963
0.977
0.963
0.002
2.427
0.008
DTBotr
20
0.001
0.001
0.980
0.980
0.980
0.001
0.048
0.004
SVMBotr
20
0.010
0.008
− 0.217
0.000
0.217
0.009
0.046
0.005
MLPBotr
20
0.003
0.002
0.861
0.870
0.861
0.003
2.921
0.040
DTBagr
50
0.001
0.001
0.977
0.977
0.001
0.001
0.317
0.076
SVMBagr
50
0.010
0.008
− 0.216
0.000
0.009
0.009
0.376
0.171
MLPBagr
50
0.001
0.001
0.982
0.990
0.001
0.001
8.220
0.029
DTBotr
50
0.001
0.001
0.987
0.987
0.001
0.001
0.106
0.009
SVMBotr
50
0.010
0.008
− 0.217
0.000
0.009
0.009
0.098
0.015
MLPBotr
50
0.002
0.001
0.958
0.965
0.001
0.002
7.231
0.023
DTBagr
100
0.001
0.001
0.975
0.975
0.001
0.001
0.182
0.028
SVMBagr
100
0.010
0.008
− 0.215
0.000
0.009
0.009
0.251
0.039
MLPBagr
100
0.001
0.001
0.991
0.994
0.001
0.001
15.411
0.054
DTBotr
100
0.001
0.001
0.991
0.991
0.001
0.001
0.644
0.025
SVMBotr
100
0.010
0.008
− 0.217
0.000
0.009
0.009
0.214
0.092
MLPBotr
100
0.001
0.001
0.983
0.987
0.001
0.001
14.632
0.045
DTBagr
150
0.001
0.001
0.976
0.976
0.001
0.001
0.266
0.027
SVMBagr
150
0.010
0.008
− 0.212
0.000
0.009
0.009
0.181
0.073
MLPBagr
150
0.001
0.001
0.994
0.997
0.001
0.001
20.029
0.206
DTBotr
150
0.001
0.001
0.994
0.994
0.000
0.001
0.381
0.023
SVMBotr
150
0.010
0.008
− 0.217
0.000
0.009
0.009
0.249
0.032
MLPBotr
150
0.001
0.001
0.985
0.989
0.001
0.001
19.393
0.042
DTBagr
200
0.001
0.001
0.974
0.974
0.001
0.001
0.393
0.032
SVMBagr
200
0.010
0.008
− 0.213
0.000
0.009
0.009
0.256
0.048
MLPBagr
200
0.001
0.001
0.995
0.996
0.001
0.001
28.065
0.238
DTBotr
200
0.001
0.001
0.995
0.995
0.000
0.001
0.786
0.024
SVMBotr
200
0.010
0.008
− 0.217
0.000
0.009
0.009
0.474
0.038
MLPBotr
200
0.001
0.001
0.985
0.989
0.001
0.001
26.815
0.048


---

<!-- Page 36 -->
## Page 36

Page 36 of 40
Nti et al. J Big Data            (2020) 7:20 
Table 18  Stacking and blending ensemble classifiers error metrics result over BSE dataset
Model
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
STK_DSN_C
1.000
0.000
0
0
1
1
1
1
1.044
0.028
STK_SND_C
0.989
0.013
0
0
1
1
1
1
1.922
0.109
STK_DNS_C
0.995
0.009
0
0
1
1
1
1
1.009
0.073
Vote(DSN)
0.992
0.011
0
0
1
1
1
1
1.634
0.058
BLD_DSN_C
1.000
0.000
0
0
1
1
1
1
5.408
0.389
BLD_SND_C
0.980
0.016
0
0
1
1
1
1
7.323
0.388
BLD_DNS_C
1.000
0.000
0
0
1
1
1
1
6.882
1.341
Table 19  Stacking and blending ensemble classifiers error metrics result over GSE dataset
Model
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
STK_DSN_C
0.896
0.022
0.257
0.066
0.7255
0.939
0.934
0.930
2.443
0.131
STK_SND_C
0.960
0.019
0.000
0.000
1.0000
1.000
1.000
1.000
9.966
0.837
STK_DNS_C
0.960
0.019
0.000
0.000
1.0000
1.000
1.000
1.000
7.615
0.188
Vote(DSN)
0.918
0.032
0.170
0.029
0.8799
0.966
0.971
0.967
9.285
0.223
BLD_DSN_C
0.849
0.048
0.363
0.132
0.4509
0.856
0.868
0.851
23.455
2.783
BLD_SND_C
0.942
0.024
0.272
0.074
0.6911
1.000
0.926
0.938
20.041
0.771
BLD_DNS_C
0.959
0.018
0.000
0.000
1.0000
1.000
1.000
1.000
19.658
1.102
Table 20  Stacking and blending ensemble classifiers error metrics result on NYSE dataset
Model
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
STK_DSN_C
1
0
0
0
1
1
1
1
1.232
0.034
STK_SND_C
1
0
0
0
1
1
1
1
2.28
0.062
STK_DNS_C
1
0
0
0
1
1
1
1
1.373
0.045
Vote(DSN)
1
0
0
0
1
1
1
1
3.182
0.077
BLD_DSN_C
1
0
0
0
1
1
1
1
6.17
0.293
BLD_SND_C
1
0
0
0
1
1
1
1
7.377
0.373
BLD_DNS_C
1
0
0
0
1
1
1
1
8.157
0.383
Table 21  Stacking and blending ensemble classifiers error metrics result on JSE dataset
Model
Mean
STD
RMSE
MAE
R2
Precision
Recall
AUC​
Train time
Test time
STK_DSN_C
0.828
0.032
0.371
0.137
0.449
0.828
0.863
0.86
5.04
0.10
STK_SND_C
0.818
0.027
0.291
0.085
0.660
0.911
0.915
0.91
267.23
10.58
STK_DNS_C
0.818
0.027
0.291
0.085
0.660
0.911
0.915
0.91
269.21
9.17
Vote(DSN)
0.827
0.028
0.348
0.121
0.513
0.838
0.879
0.87
314.04
10.51
BLD_DSN_C
0.799
0.112
0.403
0.162
0.348
0.816
0.838
0.83
21.97
2.74
BLD_SND_C
0.817
0.034
0.412
0.169
0.320
0.786
0.831
0.82
480.04
14.78
BLD_DNS_C
0.822
0.029
0.314
0.098
0.605
0.876
0.902
0.90
477.11
14.78


---

<!-- Page 37 -->
## Page 37

Page 37 of 40
Nti et al. J Big Data            (2020) 7:20 
	
Received: 22 October 2019   Accepted: 26 February 2020
References
	1.	
Nti IK, Adekoya AF, Weyori BA. A systematic review of fundamental and technical analysis of stock market predic-
tions. Artif Intell Rev. 2019. https​://doi.org/10.1007/s1046​2-019-09754​-z.
Table 22  Stacking and blending ensemble regressors error metrics result on BSE dataset
Model
RMSE
MAE
R2
EVS
MedAE
RMSLE
Train time
Test time
STK_DSN_R
0.053
0.036
0.978
0.978
0.028
0.025
0.284
0.002
STK_SND_R
0.111
0.081
0.904
0.904
0.056
0.051
2.360
0.001
STK_DNS_R
0.063
0.056
0.970
0.979
0.056
0.034
0.984
0.001
BLD_DSN_R
0.211
0.197
0.653
0.928
0.213
0.108
0.302
0.288
BLD_SND_R
0.132
0.108
0.864
0.864
0.098
0.070
0.661
0.519
BLD_DNS_R
0.055
0.039
0.977
0.977
0.030
0.024
1.142
0.287
Table 23  Stacking and blending ensemble regressors error metrics result on GSE dataset
Model
RMSE
MAE
R2
EVS
MedAE
RMSLE
Train time
Test time
STK_DSN_R
0.074
0.061
0.993
0.993
0.057
0.014
0.279
0.004
STK_SND_R
0.210
0.157
0.942
0.942
0.128
0.042
5.945
0.001
STK_DNS_R
0.055
0.050
0.996
0.998
0.051
0.011
4.480
0.001
BLD_DSN_R
0.574
0.521
0.570
0.917
0.450
0.105
0.338
0.343
BLD_SND_R
0.275
0.194
0.901
0.902
0.136
0.064
2.503
0.400
BLD_DNS_R
0.067
0.054
0.994
0.994
0.047
0.013
1.224
0.339
Table 24  Stacking and blending ensemble regressors error metrics result on NYSE dataset
Model
RMSE
MAE
R2
EVS
MedAE
RMSLE
Train time
Test time
STK_DSN_R
0.015
0.011
0.989
0.989
0.009
0.007
0.192
0.001
STK_SND_R
0.023
0.018
0.973
0.973
0.016
0.011
2.618
0.000
STK_DNS_R
0.045
0.035
0.895
0.897
0.025
0.022
2.307
0.002
BLD_DSN_R
0.051
0.041
0.867
0.889
0.035
0.026
0.578
0.334
BLD_SND_R
0.073
0.059
0.725
0.734
0.055
0.036
1.378
0.389
BLD_DNS_R
0.043
0.034
0.908
0.911
0.027
0.021
0.519
0.319
Table 25  Stacking and blending ensemble regressors error metrics result on JSE dataset
Model
RMSE
MAE
EVS
MedAE
RMSLE
R2
Train time
Test time
STK_DSN_R
0.068
0.055
0.991
0.048
0.012
0.991
0.283
0.001
STK_SND_R
0.125
0.094
0.968
0.074
0.023
0.968
5.757
0.002
STK_DNS_R
0.041
0.035
0.997
0.033
0.007
0.997
5.338
0.001
BLD_DSN_R
0.210
0.179
0.961
0.163
0.036
0.911
0.314
0.424
BLD_SND_R
0.379
0.268
0.709
0.175
0.065
0.709
2.134
0.503
BLD_DNS_R
0.047
0.037
0.996
0.031
0.008
0.996
1.179
0.585


---

<!-- Page 38 -->
## Page 38

Page 38 of 40
Nti et al. J Big Data            (2020) 7:20 
	2.	
Bousono-Calzon C, Bustarviejo-Munoz J, Aceituno-Aceituno P, Escudero-Garzas JJ. On the economic significance 
of stock market prediction and the no free lunch theorem. IEEE Access. 2019;7:75177–88. https​://doi.org/10.1109/
ACCES​S.2019.29210​92.
	3.	
Nti IK, Adekoya AF, Weyori BA. Random forest based feature selection of macroeconomic variables for stock 
market prediction. Am J Appl Sci. 2019;16:200–12. https​://doi.org/10.3844/ajass​p.2019.200.212.
	4.	
Wang Q, Xu W, Huang X, Yang K. Enhancing intraday stock price manipulation detection by leveraging recurrent 
neural networks with ensemble learning. Neurocomputing. 2019;347:46–58. https​://doi.org/10.1016/j.neuco​
m.2019.03.006.
	5.	
Liu L, Wu J, Li P, Li Q. A social-media-based approach to predicting stock comovement. Expert Syst Appl. 
2015;42:3893–901. https​://doi.org/10.1016/j.eswa.2014.12.049.
	6.	
Gupta K. Oil price shocks, competition, and oil and gas stock returns—global evidence. Energy Econ. 
2016;57:140–53. https​://doi.org/10.1016/j.eneco​.2016.04.019.
	7.	
Billah M, Waheed S, Hanifa A. Stock market prediction using an improved training algorithm of neural network. 
In: 2016 2nd international conference on electrical, computer and telecommunication engineering. IEEE; 2016. 
pp. 1–4. http://doi.org/10.1109/ICECT​E.2016.78796​11.
	8.	
Kraus M, Feuerriegel S. Decision support from financial disclosures with deep neural networks and transfer 
learning. Decis Supp Syst. 2017;104:38–48. https​://doi.org/10.1016/j.dss.2017.10.001.
	9.	
Pimprikar R, Ramachadran S, Senthilkumar K. Use of machine learning algorithms and twitter sentiment analysis 
for stock market prediction. Int J Pure Appl Math. 2017;115:521–6.
	10.	 Göçken M, Özçalici M, Boru A, Dosdoʇru AT. Integrating metaheuristics and artificial neural networks for 
improved stock price prediction. Expert Syst Appl. 2016;44:320–31. https​://doi.org/10.1016/j.eswa.2015.09.029.
	11.	 Dosdoğru AT, Boru A, Göçken M, Özçalici M, Göçken T. Assessment of hybrid artificial neural networks and 
metaheuristics for stock market forecasting Ç.Ü. Sos Bilim Enstitüsü Derg. 2018;24:63–78.
	12.	 Ballings M, Van den Poel D, Hespeels N, Gryp R. Evaluating multiple classifiers for stock price direction predic-
tion. Expert Syst Appl. 2015;42:7046–56. https​://doi.org/10.1016/j.eswa.2015.05.013.
	13.	 Akyuz AO, Uysal M, Bulbul BA, Uysal MO. Ensemble approach for time series analysis in demand forecasting: 
Ensemble learning. In: 2017 IEEE international conference on innovations in intelligent systems and applica-
tions. IEEE; 2017. pp. 7–12. https​://doi.org/10.1109/inist​a.2017.80011​23.
	14.	 Bergquist SL, Brooks GA, Keating NL, Landrum MB, Rose S. Classifying lung cancer severity with ensemble 
machine learning in health care claims data. In: 2nd machine learning for healthcare conference. 2017. pp. 
25–38.
	15.	 Priya P, Muthaiah U, Balamurugan M. Predicting yield of the crop using machine learning algorithm. Int J Eng Sci 
Res Technol. 2018;7:1–7.
	16.	 Khairalla MA, Ning X, AL-Jallad NT, El-Faroug MO. Short-term forecasting for energy consumption through stack-
ing heterogeneous ensemble learning model. Energies. 2018;11:1–21. https​://doi.org/10.3390/en110​61605​.
	17.	 Zhao Y, Li J, Yu L. A deep learning ensemble approach for crude oil price forecasting. Energy Econ. 2017;66:9–16. 
https​://doi.org/10.1016/j.eneco​.2017.05.023.
	18.	 Macchiarulo A. Predicting and beating the stock market with machine learning and technical analysis. J Intern 
Bank Commer. 2018;23:1–22.
	19.	 Mabu S, Obayashi M, Kuremoto T. Ensemble learning of rule-based evolutionary algorithm using multi-layer 
perceptron for supporting decisions in stock trading problems. Appl Soft Comput. 2015;36:357–67. https​://doi.
org/10.1016/j.asoc.2015.07.020.
	20.	 Maknickiene N, Lapinskaite I, Maknickas A. Application of ensemble of recurrent neural networks for forecasting 
of stock market sentiments. Equilib Q J Econ Econ Policy. 2018;13:7–27. https​://doi.org/10.24136​/eq.2018.001.
	21.	 Weng B. Application of machine learning techniques for stock market prediction. Auburn: Auburn University; 
2017.
	22.	 Khaidem L, Saha S, Dey SR. Predicting the direction of stock market prices using random forest. Appl Math 
Financ. 2016;2016:1–20.
	23.	 Gonzalez TR, Padilha AC, Couto AD. Ensemble system based on genetic algorithm for stock market forecasting. 
In: 2015 IEEE congress on evolutionary computation. 2015. pp. 3102–8.
	24.	 Jacobsen B, Jiang F, Zhang H. Ensemble machine learning and stock return predictability. SSRN Electron J. 2018. 
https​://doi.org/10.2139/ssrn.33102​89.
	25.	 Sharma N, Juneja A. Combining of random forest estimates using LSboost for stock market index prediction. In: 
2017 2nd international conference for convergence in technology I2CT 2017. 2017. pp. 1199–202. https​://doi.
org/10.1109/i2ct.2017.82263​16.
	26.	 Sun S, Wei Y, Wang S. AdaBoost-LSTM ensemble learning for financial time series forecasting, lecturer notes 
computer science (including subseries lecturer notes in artificial intelligence and lecture notes in bioinformat-
ics). 10862 LNCS; 2018. pp. 590–7. https​://doi.org/10.1007/978-3-319-93713​-7_55.
	27.	 Jiang M, Liu J, Zhang L, Liu C. An improved Stacking framework for stock index prediction by leveraging tree-
based ensemble models and deep learning algorithms. Phys Stat Mech Appl. 2019. https​://doi.org/10.1016/j.physa​
.2019.12227​2.
	28.	 Pulido M, Melin P, Castillo O. Particle swarm optimization of ensemble neural networks with fuzzy aggrega-
tion for time series prediction of the Mexican Stock Exchange. Inf Sci (Ny). 2014;342:317–29. https​://doi.
org/10.1007/978-3-319-32229​-2_23.
	29.	 Yang B, Gong ZJ, Yang W. Stock market index prediction using deep neural network ensemble, in: 2017 36th 
Chinese control conferrence. IEEE; 2017. pp. 3882–7. https​://doi.org/10.23919​/chicc​.2017.80279​64.
	30.	 Booth A, Gerding E, Mcgroarty F. Automated trading with performance weighted random forests and seasonal-
ity. Expert Syst Appl. 2014;41:3651–61. https​://doi.org/10.1016/j.eswa.2013.12.009.
	31.	 Tan Z, Yan Z, Zhu G. Stock selection with random forest: an exploitation of excess return in the Chinese stock 
market. Heliyon. 2019;5:e02310. https​://doi.org/10.1016/j.heliy​on.2019.e0231​0.


---

<!-- Page 39 -->
## Page 39

Page 39 of 40
Nti et al. J Big Data            (2020) 7:20 
	
	32.	 Mathur R, Pathak V, Bandil D. Stock market price prediction using LSTM RNN. Singapore: Springer; 2019. https​://
doi.org/10.1007/978-981-13-2285-3.
	33.	 Sohangir S, Wang D, Pomeranets A, Khoshgoftaar TM. Big Data: deep learning for financial sentiment analysis. J 
Big Data. 2018;5:3. https​://doi.org/10.1186/s4053​7-017-0111-6.
	34.	 Abe M, Nakayama H. Deep learning for forecasting stock returns in the cross-section. In: Phung D, Tseng V, Webb 
G, Ho B, Ganji M, Rashidi L, editors. Advanced techniques in knowledge discovery and data mining. PAKDD 2018 
lecture notes in computer science. Cham: Springer; 2018. p. 273–84. https​://doi.org/10.1007/978-3-319-93034​
-3_22.
	35.	 Krauss C, Do XA, Huck N. Deep neural networks, gradient-boosted trees, random forests: statistical arbitrage on 
the S&P 500. Eur J Oper Res. 2017;259:689–702. https​://doi.org/10.1016/j.ejor.2016.10.031.
	36.	 Qiu X, Zhu H, Suganthan PN, Amaratunga GAJ. Stock price forecasting with empirical mode decomposition 
based ensemble v-support vector regression model. In: Mandal J, Dutta P, Mukhopadhyay S, editors. Compu-
tational intelligence, communications, and business analytics CICBA 2017. Communications in computer and 
information science. Singapore: Springer; 2017. p. 22–34. https​://doi.org/10.1007/978-981-10-6427-2_2.
	37.	 Pasupulety U, Abdullah Anees A, Anmol S, Mohan BR. Predicting stock prices using ensemble learning and 
sentiment analysis. In: Proceedings of IEEE 2nd international conference on artificial intelligence and knowledge 
engineering. AIKE; 2019. pp. 215–22. https​://doi.org/10.1109/aike.2019.00045​.
	38.	 Pulido M, Melin P. Optimization of ensemble neural networks with type-1 and type-2 fuzzy integration 
for prediction of the Taiwan stock exchange. Stud Fuzziness Soft Comput. 2018;361:151–64. https​://doi.
org/10.1007/978-3-319-75408​-6_13.
	39.	 Zhu Y, Xie C, Wang GJ, Yan XG. Comparison of individual, ensemble and integrated ensemble machine learning 
methods to predict China’s SME credit risk in supply chain finance. Neural Comput Appl. 2017;28:41–50. https​://
doi.org/10.1007/s0052​1-016-2304-x.
	40.	 Yadav S, Sharma N. Homogenous ensemble of time-series models for indian stock market. Springer. 2018. https​
://doi.org/10.1007/978-3-030-04780​-1_7.
	41.	 Yang J, Rao R, Hong P, Ding P. Ensemble model for stock price movement trend prediction on different investing 
periods. In: Proceedings of 12th international conference on computational intelligence in security. CIS 2016. 
2017. pp. 358–61. https​://doi.org/10.1109/cis.2016.86.
	42.	 K.S. Gan, K.O. Chin, P. Anthony, S.V. Chang, Homogeneous ensemble feedforward neural network in CIMB stock 
price forecasting In: Proceedings of international conference on artificial intelligence in engineering and tech-
nology IICAIET 2018. 2019, pp. 111–6. https​://doi.org/10.1109/iicai​et.2018.86384​52.
	43.	 Jothimani D, Yadav SS. Stock trading decisions using ensemble-based forecasting models: a study of the Indian 
stock market. J Bank Financ Technol. 2019. https​://doi.org/10.1007/s4278​6-019-00009​-7.
	44.	 Mehta S, Rana P, Singh S, Sharma A, Agarwal P. Ensemble learning approach for enhanced stock prediction. 
In: 2019 12th international conference on contemporary computing IC3 2019. 2019, pp. 1–5. https​://doi.
org/10.1109/ic3.2019.88448​91.
	45.	 Assis JDM, Pereira ACM, Silva RCE. Designing financial strategies based on artificial neural networks ensembles 
for stock markets. In: Proceedings of international joint conference neural networks. 2018, pp. 1–8. https​://doi.
org/10.1109/ijcnn​.2018.84896​88.
	46.	 Kohli PPS, Zargar S, Arora S, Gupta P. Stock prediction using machine learning algorithms. In: Malik H, 
Srivastava S, Sood YR, Ahmad A, editors. Applications of artificial intelligence technology and engineer-
ing advances in intelligent systems and computing. Singapore: Springer; 2019. p. 405–14. https​://doi.
org/10.1007/978-981-13-1819-1_38.
	47.	 Kumar M, Thenmozhi M. Forecasting stock index movement: a comparison of support vector machines and 
random forest. In: 9th Capital Mark Conference Paper, Indian Institute of Capital Mark. 2006, pp. 1–16.
	48.	 Tsai CF, Hsu YF, Yen DC. A comparative study of classifier ensembles for bankruptcy prediction. Appl Soft Com-
put J. 2014;24:977–84. https​://doi.org/10.1016/j.asoc.2014.08.047.
	49.	 Usmani M, Ebrahim M, Adil SH, Raza K. Predicting market performance with hybrid model. in: 2018 3rd interna-
tional conference emergency of trends engineering science and technology. IEEE; 2018. pp. 1–4. https​://doi.
org/10.1109/icees​t.2018.86433​27.
	50.	 Ghosh S, Sadhu S, Biswas S, Sarkar D, Sarkar PP. A comparison between different classifiers for tennis match 
result. Malays J Comput Sci. 2019;32:97–111.
	51.	 Akanbi OA, Amiri IS, Fazeldehkordi E. A machine-learning approach to phishing detection and defense. Syn-
gress. 2014. https​://doi.org/10.1016/c2014​-0-03762​-8.
	52.	 Agarwal P, Bajpai S, Pathak A, Angira R. Stock market price trend forecasting using. Int J Res Appl Sci Eng Tech-
nol. 2017;5:1673–6.
	53.	 Golub GH, Christian PER, Leary DPO. Tikhonov regularization and total least squares. SIAM J Matrix Anal Appl. 
1999;21:185–94.
	54.	 Guzman E, El-halaby M, Bruegge B. Ensemble methods for app review classification : an approach for software 
evolution. In: 30th IEEE/ACM international conference on software engineering. 2015, pp. 771–6. https​://doi.
org/10.1109/ase.2015.88.
	55.	 Ren Y, Suganthan PN, Srikanth N. Ensemble methods for wind and solar power forecasting—a state-of-the-art 
review. Renew Sustain Energy Rev. 2015;50:82–91. https​://doi.org/10.1016/j.rser.2015.04.081.
	56.	 Flennerhag S. ML-Ensemble. 2017.
	57.	 Mayr A, Binder H, Gefeller O, Schmid M. The evolution of boosting algorithms from machine learning to statisti-
cal modelling. Methods Inf Med. 2014;53:419–27.
	58.	 Chen Y, Hao Y. A feature weighted support vector machine and K-nearest neighbor algorithm for stock market 
indices prediction. Expert Syst Appl. 2017;80:340–55. https​://doi.org/10.1016/j.eswa.2017.02.044.
	59.	 Shobana T, Umamakeswari A. A review on prediction of stock market using various methods in the field of data 
mining. Indian J Sci Technol. 2016;9:9–14. https​://doi.org/10.17485​/ijst/2016/v9i48​/10798​5.


---

<!-- Page 40 -->
## Page 40

Page 40 of 40
Nti et al. J Big Data            (2020) 7:20 
	60.	 Chong E, Han C, Park FC. Deep learning networks for stock market analysis and prediction: methodol-
ogy, data representations, and case studies. Expert Syst Appl. 2017;83:187–205. https​://doi.org/10.1016/j.
eswa.2017.04.030.
	61.	 Academy C. Normalization. 2019. https​://www.codec​ademy​.com/artic​les/norma​lizat​ion. Accessed 1 Dec 2019.
	62.	 Kamel SR, Yaghoubzadeh R, Kheirabadi M. Improving the performance of support-vector machine by selecting the 
best features by Gray Wolf algorithm to increase the accuracy of diagnosis of breast cancer. J Big Data. 2019. https​://
doi.org/10.1186/s4053​7-019-0247-7.
	63.	 Mishra A. Metrics to evaluate your machine learning algorithm. 2018. https​://towar​dsdat​ascie​nce.com/metri​cs-to-
evalu​ate-your-machi​ne-learn​ing-algor​ithm-f10ba​6e382​34.
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


---
