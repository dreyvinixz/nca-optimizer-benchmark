# Short-term load forecasting: cascade intuitionistic fuzzy time series—univariate and bivariate models

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-10280-5

---

## Page 1
ORIGINAL ARTICLE
Short-term load forecasting: cascade intuitionistic fuzzy time series—
univariate and bivariate models
Ozge Cagcag Yolcu1
• Hak-Keung Lam2 • Ufuk Yolcu1
Received: 23 March 2023 / Accepted: 29 July 2024 / Published online: 11 August 2024
 The Author(s) 2024
Abstract
Short-term load forecasting (STLF) is essential for developing reliable and sustainable economic and operational strategies
for power systems. This study presents a forecasting model combining cascade forward neural network (CFNN) and
intuitionistic fuzzy time series (IFTS) models for STLF. The proposed cascading intuitionistic fuzzy time series forecasting
model (C-IFTS-FM) offers the advantage of CFNN using the links of both linear and nonlinear to model fuzzy relations
between inputs and outputs. Moreover, it offers a more reliable and realistic approach to uncertainty, taking notice of also
the degree of hesitation. C-IFTS-FM works in univariate structure when it uses only hourly load data, and in bivariate
structure when it uses hourly load data and hourly temperature time series together. The conversion of time series into IFTS
is realized with intuitionistic fuzzy c-means (IFCM). Thus, the membership and non-membership values for each data point
are produced. In modelling process, membership and non-membership values, in addition to actual lagged observations, are
used as input of the CFNNs. The effectiveness of C-IFTS-FM on test sets for both structures was discussed comparatively
via different error criteria, in addition, the convergence time was examined, and also the ﬁt of forecasts and observations
was presented with different illustrations. Among different combinations of hyperparameters, in the best case, approxi-
mately 86% better accuracy is achieved than the best of the others, while even in the case of the worst of hyperparameters
combination, the accuracy was improved by over 20% for the PSJM data sets. For HEXING, CHENGNAN, and EUNITE
data sets, these progress rates reached approximately 90% in the best case.
Keywords Short-term load forecasting  Cascade forward neural network  Intuitionistic fuzzy time series 
Univariate and bivariate time series forecasting
Abbreviations
STLF
Short-term load forecasting
CFNN
Cascade forward neural network
IFTS
Intuitionistic fuzzy time series
C-IFTS-FM
Cascading intuitionistic fuzzy time series
forecasting model
IFCM
Intuitionistic fuzzy C-means
ARIMA
Auto-regressive
integrated
moving
average
SARIMA
Seasonal
auto-regressive
integrated
moving average
ANN
Artiﬁcial neural network
BNN
Bayesian neural network
LSTM
Long short-term memory
FTS
Fuzzy time series
CNN
Convolutional neural network
LightGBM
Light gradient-boosting machine
FB-Prophet
Facebook prophet
IFSs
Intuitionistic fuzzy sets
UC-IFTS-FM
Univariate cascading intuitionistic fuzzy
time series forecasting model
BC-IFTS-FM
Bivariate cascading intuitionistic fuzzy
time series forecasting model
CFSs
Classical fuzzy sets
IFE
Intuitionistic fuzzy entropy
HLU
Hidden layer unit
& Ozge Cagcag Yolcu
ozge.cagcag@marmara.edu.tr
Hak-Keung Lam
hak-keung.lam@kcl.ac.uk
Ufuk Yolcu
ufuk.yolcu@marmara.edu.tr
1
Department of Statistics, Marmara University, Istanbul,
Turkey
2
Department of Engineering, King’s College London, London,
UK
123
Neural Computing and Applications (2024) 36:20167–20192
https://doi.org/10.1007/s00521-024-10280-5
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
OLU
Output layer unit
ILU
Input layer unit
PSJM
Power Supply Johor in Malaysia
T-MEP
Tu¨rkiye’s monthly electricity production
EXIST
Energy exchange Istanbul
TP
Total production
NG
Electricity is produced from natural gas
HYD
Electricity is produced from hydro
COAL
Electricity is produced from coal
WIND
Electricity is produced from wind
FO
Electricity is produced from fuel oil
BIO
Electricity is produced from bioenergy
GEO
Electricity is produced from geothermal
MAPE
Mean absolute percentage error
RMSE
Root mean square error
MdRAE
Median relative absolute error
PWFTS
Probabilistic weighted fuzzy time series
WFTS
Weighted fuzzy time series
IWFTS
Integrated weighted fuzzy time series
FTS-CNN
Combined
method
for
convolutional
neural network and fuzzy time series
CI
Conﬁdence interval
GEP
Gene expression programming
GEP-LS
Gene expression programming based on
least square
GEP-KLS
Gene expression programming based on
K-means and least square
QCLF
Quantitative
combination
load
forecasting
PLLR
Pattern-based local linear regression
BPNN
Back-propagation neural network
HW Add.
Holt–Winters exponential smoothing—
additive
HW Mult.
Holt–Winters exponential smoothing—
multiplicative
ETS
State
space
models
(error–trend–
seasonality)
TBATS
Trigonometric
seasonality,
box–cox
transformation,
ARMA
errors,
trend
components,
seasonal
components
models
STL-SARIMA
Hybrid model of seasonal trend loess
decomposition and SARIMA
STL-HW Add.
Hybrid model of seasonal trend loess
decomposition and Holt–Winters expo-
nential smoothing—additive
STL-HW
Mult.
Hybrid model of seasonal trend loess
decomposition and Holt–Winters expo-
nential smoothing—multiplicative
STL-ETS
Hybrid model of seasonal trend loess
decomposition and state space models
(error–trend–seasonality)
ANN
Artiﬁcial neural network
STL-ANN
Hybrid model of seasonal trend loess
decomposition
and
artiﬁcial
neural
network
STL-LSTM
Hybrid model of seasonal trend loess
decomposition
and
long
short-term
memory
STL-CNN
Hybrid model of seasonal trend loess
decomposition and convolutional neural
network
MV-ANN
Multivariate
artiﬁcial
neural
network
model
MV-LSTM
Multivariate
long
short-term
memory
model
MV-CNN
Multivariate convolutional neural net-
work model
ARDL
Auto-regressive distributed lag model
1 Introduction
1.1 General information and literature review
Load forecasting is an issue having a vital effect on making
today’s and future plans more sustainable and reliable to
render the safe and efﬁcient operation of power systems.
Considering the variety of external impact factors, high
levels of uncertainties that belong to these factors are
obviously seen. So, obtaining an accurate load estimation is
directly associated with power system management, hence
the economy, and has a considerable effect on them. The
more forecasting errors are reduced, the lower the operat-
ing cost will be. On the other hand, inaccurate forecasting
results may cause huge losses for electric power companies
by resulting in extra cost production and insufﬁcient elec-
tricity supply. Therefore, an accurate and reliable STLF is a
signiﬁcant achievement for most energy companies. This
goal motivates scientists and researchers to develop models
to obtain accurate and practical methods. Over the years, to
be able to improve the forecasting performance for the load
demands, different methods have been developed. These
are referred to under two main groups. The ﬁrst one,
probabilistic methods, includes statistical-based approa-
ches. The second, non-probabilistic methods, is classiﬁed
as computation-based and fuzzy-based methods [1].
As statistical-based models, linear regression, Kalman
ﬁltering, auto-regressive integrated moving average models
(ARIMA), seasonal auto-regressive integrated moving
average models (SARIMA), and stochastic process models
were the most preferred models for the short-term load
20168
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 3
forecasting literature. In the early stage of load forecasting,
to be able to describe the developed forecasting system for
the Imatra Power Company, Va¨ha¨kyla et al. [2] proposed a
forecasting model which uses the ARIMA model for STLF.
While Tafreshi and Farhadi [3] performed the linear
regression method, Kalman ﬁltering was used in Zheng
et al. [4] study. Auto-regressive integrated moving average
was used by Hippert et al. [5]. On the other hand, Weron
[6] and Taylor and McSharry [7] proposed studies based on
statistical forecasting models for the load forecasting
problems.
But just like the other statistical-based methods, these
models have some deﬁciencies. Although they are effective
in dealing with linear structures, some strict assumptions
need to be satisﬁed to be able to work with these models.
Moreover, when dealing with nonlinear or complex struc-
tures, again statistical-based methods are not effective. In
these conditions, to handle some of these problems artiﬁ-
cial neural network-based models have been started and
frequently used for the STLF see, for example, [8–12].
Artiﬁcial neural networks (ANNs) have become drastically
popular models thanks to some properties such as fault
tolerance, powerful capability in pattern recognition, and
distributed associative memory[8]. With the aim of mod-
elling electricity demand for Canada, Zahidi et al. [13]
used an adaptive neural network by ﬁltering the inputs with
Pearson correlation. Ghofrani et al. [14] presented a hybrid
model which includes Bayesian neural network (BNN) and
a wavelet transform, in order to obtain load characteristics
for BNN training with detail.
Apart from ANN-based models, deep learning models
were also the preferred methods for the load forecasting
studies. Khan et al. [15] proposed a hybrid method that
combines the random forest and recursive feature elimi-
nation methods with a deep neural network to forecast
loads for a week. To be able to forecast the effect of the
power load consumption Atef and Eltawil preferred to use
long short-term memory (LSTM) and bidirectional LSTM
networks [16]. Kumar et al. [17] introduced a forecasting
model in order to handle the nonlinearity and seasonality
problem in power load data forecasting. It is also obvious
that all these models may fail to model the data accurately
if the data sets contain ambiguous and linguistic terms.
Given the fact that almost all of the daily lifetime series
data sets contain vagueness, the interest in fuzzy time
series methods for the STLF is also inevitable. Fuzzy time
series (FTS) models, with their distinguished advantages,
have started to be preferred in short-term forecasts as well
as in many areas. A new weighted FTS model was
designed by Yu [18] to be able to forecast the stock market.
Also, for stock price forecasting, Cagcag Yolcu and
Alpaslan [19], Trierweiler Ribeiro et al. [20], and Ren et al.
[21] proposed hybrid models. A hybrid model which
combines harmony search algorithm with weighted FTS
was introduced by Sadaei et al. [22] for load data sets. On
the other hand, in a different study, a combined seasonal
auto-regressive fractional moving average model with FTS
was proposed by Sadaei et al. [23] for STLF. Moreover, in
some other studies, FTS models have been used as a
forecasting tool for STLF [24–26]. Apart from these,
Sadaei et al. presented a hybrid study which integrated the
convolutional neural network (CNN) and FTS for short-
term load forecasting [27]. Wang et al. recommended using
a deep autoencoder for STLF [28], while Zhao et al. used a
global prediction method based on pre-trained autoencoder
and deep LSTM model [29]. Berahmand et al., in their
studies, discussed autoencoders and their applications in
machine learning in detail [30, 31]. In electric power sys-
tem sector, a hybrid wavelet stacking ensemble model was
proposed to forecast insulators contamination [32]. Shakeel
et al. developed a hybrid model for district heating load
forecasting based on the LightGBM and FB-Prophet [33].
A novel hybrid model based on multivariate empirical
mode decomposition and support vector regression with
hyperparameters optimized by particle swarm optimization
was introduced for heat load [34]. Additionally, some
studies emphasize that accurate short-term load forecasts
should include temperature information to ensure the reli-
able and efﬁcient operation of power systems [35–37]. In
this context, this study introduces not only a univariate
forecasting model but also a bivariate model that includes
hourly temperature time series as an explanatory variable.
Considering that all these fuzzy-based and computa-
tional-based models are investigated in detail, some sig-
niﬁcant deﬁciencies can be mentioned. First of all,
computation-based models do not offer an approach to the
uncertainty contained in time series in forecasting prob-
lems such as STLF and focus only on prediction accuracy.
However, it is inevitable that time series, including energy
data sets, contain uncertainty by their nature. To address
uncertainty, more complex and sophisticated approaches,
such as models incorporating fuzzy logic, are required. In
this context, while fuzzy-based and hybrid models have
been proposed for STLF [24, 25, 27], they also have fun-
damental problems. The ﬁrst problem is that in almost all
of these studies, fuzzy set indices are taken into account
instead of membership values, and relationships are created
on these, which causes a loss of information that will
negatively affect forecasting performance. Secondarily, in
all these fuzzy-based models, the neutrality degree of time
series has not been taken into account. This means that
characterizing the uncertainty of the data which belongs to
non-membership degrees and the neutrality degrees of time
series has not been considered in a comprehensive manner.
Also, in the decision-making process, hesitations always
exist. Since there are always some factors that affect the
Neural Computing and Applications (2024) 36:20167–20192
20169
123

---

## Page 4
decision process, in this study, a model based on intu-
itionistic fuzzy sets introduced by Atanassov [38], which
incorporates all relevant information, is proposed. In this
way, using information about both membership and non-
membership degrees will provide more realistic and pow-
erful forecasting results. With the introduction of IFSs,
these problems have been relatively eliminated. There is no
introduced study that uses IFSs in the STLF literature.
Furthermore, while some studies on STLF propose linear
models [3, 4], others identify relationships using nonlinear
models [8, 9, 11, 27]. However, data sets can contain both
linear and nonlinear relationships, together. This study
addresses this issue by employing a cascaded forward
neural network to uncover and identify the relationships.
In this study, we aim to achieve more effective fore-
casting results in the STLF problem by incorporating both
the hesitation degree and the inherent uncertainty in the
data through an intuitionistic fuzzy sets-based approach.
Considering the STLF literature, this study is notable for
being the ﬁrst to utilize IFSs in the ﬁeld of STLF. On the
other hand, to be able to reveal both and identify linear and
nonlinear relationships between inputs and outputs, we
leverage a cascade neural network with such capability.
Therefore, we called the proposed forecasting model the
cascade intuitionistic fuzzy time series forecasting model.
C-IFTS-FM is capable of operating in both univariate and
bivariate structures. In a univariate structure, C-IFTS-FM
uses only hourly load data to model the load and to obtain
the short-term forecasts of load (UC-IFTS-FM). In the
bivariate structure, C-IFTS-FM also uses hourly tempera-
ture time series besides the hourly load data (BC-IFTS-
FM). Additionally, Tu¨rkiye’s monthly electricity produc-
tion data from January 2012 to May 2022 were analysed
using the proposed univariate model to demonstrate its
performance.
C-IFTS-FM converts these time series with the real
observations into IFTS by performing the IFCM algorithm.
Besides the real observations of hourly load and tempera-
ture time series, both the non-membership and the mem-
bership values obtained in this way are also used in the
forecasting process.
1.2 Motivation and contributions
STLF plays a signiﬁcant role for the power system in terms
of determining economic formulations, providing reliable
and secure operating strategies. The main purpose of the
STLF function can be summarized with titles Gross and
Galiana [39].
•
To provide load estimates for basic production schedul-
ing functions
•
To evaluate the power system security at any time
•
To provide information relevant to timely dispatch
Apart from these important purposes, STLF has a huge
usage area. STLF applications are crucial for hydro
scheduling, as they help determine optimal reservoir
releases and powerhouse generation levels. Moreover,
STLF is necessary to determine hourly minimum-cost
strategies for commissioning and shutting down units in
thermal systems. Also, STLF is used to schedule the hourly
operation of various resources and minimize production
costs for mixed hydro and thermal systems. On the other
hand, STLF plays an active role in ensuring power system
security. System load forecasting is essential for detecting
future conditions where the power system might be vul-
nerable. One of the other application areas of STLF is also
providing system dispatchers with timely information,
which helps them to operate the system economically and
reliably by taking advantage of the latest weather fore-
casting and random behaviour.
When evaluating all these areas of use, the signiﬁcance
of STLF becomes evident. Therefore, developing an STLF
model that offers high reliability, accuracy, and validity is
crucial. However, obtaining accurate load forecasts is
challenging, as various external factors inﬂuence loads. In
this study, we aim to address this challenge by proposing a
model that combines intuitionistic fuzzy clustering with
cascade neural networks to achieve high accuracy. Fore-
casting tools based on artiﬁcial intelligence and fuzzy logic
have been widely used to support smart energy manage-
ment in recent years. The proposed model leverages the
fundamental advantages of neural networks and the
uncertainty-handling capabilities of IFSs. Intuitionistic
fuzzy sets incorporate membership degrees, non-member-
ship degrees, and hesitation degrees, providing a richer and
more comprehensive representation of uncertainty. These
additional components of information can result in more
accurate modelling of complex systems. Studies have
shown that incorporating both membership and non-
membership degrees as inputs in the models can enhance
forecasting performance. By leveraging detailed informa-
tion about the degree of membership and non-membership
of observations, proposed models can make more informed
forecasts. Moreover, what makes the proposed forecasting
model superior and distinct from other models is its ability
to simultaneously model both linear and nonlinear rela-
tionships between inputs and outputs, thanks to its cas-
caded analysis structure. The C-IFTS-FM offers several
contributions, fundamental features, and advantages com-
pared to current models aimed at STLF.
C-IFTS-FM offers a more realistic approach by mod-
elling the uncertainty included in the time series, taking
into account the degree of hesitation (to compare fuzzy-
based models).
20170
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 5
C-IFTS-FM uses both membership and non-membership
values determined for time series (to compare fuzzy-
based models).
C-IFTS-FM does not need to convert the data to an
image and therefore does not include any loss of
information due to conversion (to compare CNN-based
models).
C-IFTS-FM has the ability of modelling both types of
relationships between inputs and outputs (linear and
nonlinear), thanks to its cascading structure (when
compared with fuzzy-based and neural network-based
models).
C-IFTS-FM is capable of operating in both univariate
and bivariate structures, and thus, it can turn into a more
effective forecasting tool by taking into account other
variables that may have an effect on the load.
With these features, the proposed C-IFTS-FM shows
superior performance in terms of different evaluation
metrics and aspects as well for STLF.
2 Background
The background on which the proposed forecasting models
are based can be given by mentioning some points. To
determine the membership and non-membership degrees,
the used clustering algorithm is presented in general terms.
Moreover, in this section, brief information is given about
the cascaded neural networks that enable the proposed
forecasting models to determine linear and nonlinear
relationships together, that is, their cascading structure is
explained.
2.1 IFCM
IFSs establish a mathematical framework based on FSs to
bring out and characterize vagueness and uncertainty
existing inner of the data. IFSs have some distinct advan-
tages over classical fuzzy sets (CFSs). CFSs [40] only take
notice of the membership function, l x
ð Þ. However, IFSs
deal with non-membership v x
ð Þ and membership functions
together.
When X is a universe of discourse, an IFS can be
deﬁned as in Eq. (1)
A ¼ x; lA x
ð Þ; vA x
ð Þ=x 2 X
f
g
ð1Þ
Here, for an element xX, while lA x
ð Þ ! d0,1e depicts
the membership degree, lA x
ð Þ ! d0,1e represents the non-
membership degree under the condition given by Eq. (2).
0  lA x
ð Þ þ vA x
ð Þ  1
ð2Þ
As another speciﬁc measure of uncertainty, pA x
ð Þ, the
degree of hesitation represents the lack of knowledge in
deﬁning membership and non-membership degrees and is
deﬁned as:
pA x
ð Þ ¼ 1  lA x
ð Þ  vA x
ð Þ
ð3Þ
It is clear from Eq. (3) that 0  pA x
ð Þ  1. For all xX, if
lA x
ð Þ ¼ vA x
ð Þ ¼ 0, the IFS is said to be purely intuition-
istic. On the other hand, for all xX, if pA x
ð Þ ¼ 0, the IFS
transforms into a CFS.
The objective function to be optimized in IFCM [41],
given in Eq. 4, consists of two components. The ﬁrst is the
modiﬁed objective function of FCM using IFS. The second
is the intuitionistic fuzzy entropy (IFE).
JIFCM ¼
Xc
i¼1
Xn
k¼1um
ik d2
ik þ
Xc
i¼1p
i exp 1  p
i


ð4Þ
Here, c and n represent the number of clusters and the
number of data set points, respectively. In JIFCM, u
ik
depicts the intuitionistic fuzzy membership and calculated
by Eq. (5)
u
ik ¼ uik þ pik
ð5Þ
Also, uik is equivalent to the membership for CFS of the
k th observation set in i th set. Consequently, the degree of
hesitation, pik, can be given as follows:
pik ¼ 1  uik  1  ua
ik

1
a; a [ 0
ð6Þ
and is obtained via an intuitionistic fuzzy complement of
Yager:
N X
ð Þ ¼ 1  xa
ð
Þ
1
a; a [ 0
ð7Þ
The alpha-cut (a-cut) determines the set of elements
whose membership degree in A is at least a. Herewith, the
IFS becomes
AIFS
k
¼
x; lA x
ð Þ; 1  lA x
ð Þa
ð
Þ
1
a=x 2 X
n
o
ð8Þ
and
p
i ¼ 1
N
XN
k¼1pik; k 2 1; N
½

ð9Þ
IFE, the second component of the objective function,
indicates the amount of fuzziness or uncertainty in a set.
Thus, IFE as a measure of the degree of intuitionism can be
deﬁned as in Eq. (10).
Neural Computing and Applications (2024) 36:20167–20192
20171
123

---

## Page 6
IFE A
ð Þ ¼
XN
i¼1pA xi
ð Þexp 1  pA xi
ð Þ
ð
Þ; k 2 1; N
½

ð10Þ
also, the degree of hesitation
pA xi
ð Þ ¼ 1  lA xi
ð Þ  vA xi
ð Þ
ð11Þ
The cluster centres can be modiﬁed as in Eq. (12)
v
i ¼
Pn
k¼1u
ikxk
Pn
k¼1u
ik
ð12Þ
The maximum number of iterations can be taken as the
stopping criterion for the process, or it can be adjusted
according to the difference of the membership degrees in
successive iterations. In this case, the process is stopped
when the maximum number of iterations is reached or
when maxik unew
ik
 uprevious
ik

  e (e is pre-deﬁned value).
2.2 Cascade forward neural network
Cascade forward neural network was proposed by Demuth
[42] inspired by the cascade correlation approaches of
Fahlman [43], and Fahlman and Lebiere [44]. Like other
classical feed-forward multilayer neural networks, the
architecture of CFNN consists of input, output, and hidden
layer(s) [45]. However, the main feature that distinguishes
this network from existing networks is that each neuron
layer is associated with all previous neuron layers. How-
ever, the main distinguishing aspect of this network from
existing networks is that it accommodates the nonlinear
relationship between input and output by not eliminating
the linear relationship between the two. The sigmoid acti-
vation function used in the hidden layer and the linear
activation function used in the output layer provide this
feature. A simple CFNN architecture with two hidden
layers is given in Fig. 1.
3 The proposed methodology
3.1 C-IFTS-FM
Today,
considering
the
increasing
population
and
decreasing energy resources, national and global energy
management is really important in terms of the sustain-
ability of life. Load forecasting is one of the basic and most
important elements of energy management. At this point,
various forecasting tools act as a pioneer and guide for load
forecasting as in many other areas. Especially in recent
years, forecasting tools based on artiﬁcial intelligence and
fuzzy logic are widely used to provide a service for smart
energy management. In this study, a new forecasting
model/tool is proposed for short-term load forecasting. The
introduced model uses the basic advantages of neural net-
works and the uncertainty approach of IFSs. Moreover, the
aspect that makes the proposed forecasting model superior
and distinguishes it from other models is the ability of
accommodating the nonlinear relationship between input
and output by not eliminating the linear relationship
between the two, thanks to its cascade analysis structure.
The C-IFTS-FM is based on two deﬁnitions given in the
following text and introduced in this study.
3.2 UC-IFTS-FM
C-IFTS-FM can be considered a model combining intu-
itionistic fuzzy clustering and cascade neural networks. By
using IFCM clustering algorithm, the memberships and
non-memberships values are determined for time series
observations. And these membership and non-membership
values are used as inputs of cascade neural network besides
the lagged observations of crisp time series. The target
values are also composed of crisp time series observation at
t time. The structure of UC-IFTS-M can be given in Fig. 2.
UC-IFTS-FM, to determine the intuitionistic relation-
ships between inputs and outputs, uses a cascade neural
network composed of three layers as input, hidden, and
output layers. A linear activation function (f 2) is executed
in the output layer, while a nonlinear activation function
(f 1) is used in hidden layer units (HLUs). The unit in the
output layer (OLU) is fed directly with the inputs as well as
with the outputs generated by processing the inputs in the
hidden layer with a nonlinear activation function. Feeding
the output layer with direct inputs models the effect of
linear relationships, while feeding with the hidden layer
output determines the effect of nonlinear relationships on
the output.
Definition
5
(UC-IFTS-FM)
Let
IFt
be
an
IFTS,
I1; I2;    ; Ic are IFSs on the universal set, and lIl tð Þ, vIl tð Þ
are the degree of membership and non-membership values
Fig. 1 The architecture of C-IFTS-M designed for STLF
20172
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 7
of the tth observation in the lth IFS, respectively. The high-
order UC-IFTS-FM can be deﬁned as in Eq. (13).
In Eq. (13), while F and F1 symbolize the linear func-
tions, F2 symbolizes a nonlinear function obtained from an
estimation tool. In this step an artiﬁcial neural network has
been used to reveal the nonlinear relationships but different
estimation tools can be chosen as well. et represents the
error term. Thanks to the cascaded structure of the model,
both linear and nonlinear relationships can be modelled
synchronously at the same time.
Yt ¼ F F1 Yt1Yt2    ; Ytm; lI1 t  1
ð
Þ;


lI2 t  1
ð
Þ;    ; lIc t  1
ð
Þ; vI1 t  1
ð
Þ; vI2 t  1
ð
Þ;    ;
vIc t  1
ð
ÞÞ; F2 Yt1Yt2    ; Ytm; lI1 t  1
ð
Þ;

lI2 t  1
ð
Þ;    ; lIc t  1
ð
Þ; vI1 t  1
ð
Þ; vI2 t  1
ð
Þ;    ;
vIc t  1
ð
ÞÞÞ þ et
ð13Þ
where Yt1Yt2    ; Ytm are mth order lagged real valued
time
series
for
tth
time
point,
lI1 t  1
ð
Þ; lI2 t  1
ð
Þ;    ; lIc t  1
ð
Þ are the ﬁrst-order lag-
ged degrees of membership of the tth observation in each
intuitionistic
fuzzy
set
also
Fig. 2 The structure of UC-
IFTS-M designed for STLF
Neural Computing and Applications (2024) 36:20167–20192
20173
123

---

## Page 8
vI1 t  1
ð
Þ; vI2 t  1
ð
Þ;    ; vIc t  1
ð
Þ are the ﬁrst-order lag-
ged degrees of membership of the tth observation in each
intuitionistic fuzzy set.
In the structure given by Fig. 2;
lLc t  1
ð
Þ:
The membership input, associated with cth
IFS, for the data point at the t  1 time.
vLc t  1
ð
Þ:
The non-membership input, associated with
cth IFS, for the data point at the t  1 time.
ytj:
Real input related to jth lagged variable.
byt:
The output for the t time.
lwil
t :
For
membership
component,
the
weight
between lth input layer unit (ILU) and ith
HLU i ¼ 1; K; l ¼ 1; c


.
vwil
t :
For non-membership component, the weight
between
lth
ILU
and
ith
HLU i ¼ 1; K; l ¼ 1; c


.
wij
t :
For lagged variables with real values, the
weights
between
jth
ILU
and
ith
HLU i ¼ 1; K; j ¼ 1; m


.
bi
t:
The bias for ith HLU i ¼ 1; K


.
Hwi
t:
The
weight
between
ith
HLU
and
the
OLU i ¼ 1; K


.
IWt:
The vector of weights between ILUs and the
H IWt ¼ ½Iw1
t Iw2
t    Iw2lþm
t



.
bo
t :
The bias of OLU.
The outputs of HLU are obtained by Eq. (14).
oi ¼ f 1
Xc
l¼1lwil
t lLl t  1
ð
Þ


þ
Xc
l¼1vwil
t vLl t  1
ð
Þ



þ
Xm
j¼1wij
t ytj


þ bi
t

; i ¼ 1,2; . . .; K
ð14Þ
Here f 1 represents the sigmoid activation function and
f 1 x
ð Þ ¼
1
1þexp x
ð
Þ. The outputs of the system are obtained,
by using the weights between the hidden and output layers,
as in the formula given Eq. (15).
oCIFTSFM ¼ f 2
Xc
l¼1Hwi
toi



þ
Xc
l¼1IWtINPUTS tð Þ


þ bo
t

; i ¼ 1,2; . . .; K
ð15Þ
f 2, in Eq. (16), is the linear activation function and
INPUTS tð Þ is a vector which is composed of inputs for the t
time (lLl t  1
ð
Þ; vLl t  1
ð
Þ; ytj).
3.3 BC-IFTS-FM
In this study, until now, it has been focused on STLF,
which has a univariate structure. In this univariate struc-
ture, the intuitionistic fuzzy relationships between the
inputs consisting of the loads’ own lagged variables,
memberships, and non-memberships and the output are
modelled. However, based on the fact that the load is
particularly affected by the air temperature, an approach
can be put forward where the air temperature information is
also used in STLF. In this respect, for STLF, this study also
presents a C-IFTS-FM in which air temperatures are also
included in the model.
Definition 6
(BC-IFTS-FM) Let IFt be an intuitionistic
fuzzy time series, I1; I2;    ; Ic are IFSs on the universal
set, and lIl tð Þ, vIl tð Þ are the degree of membership and non-
membership values of the tth observation for both time
series (Yt and Zt) in the lth IFS, respectively. The high-
order BC-IFTS-FM model can be deﬁned as below:
Yt ¼ F F1 Yt1Yt2    ; Ytm; Zt1Zt2    ;
ð
ð
Ztm; lI1 t  1
ð
Þ; lI2 t  1
ð
Þ;    ; lIc t  1
ð
Þ; vI1 t  1
ð
Þ;
vI2 t  1
ð
Þ;    ; vIc t  1
ð
ÞÞ; F2 Yt1Yt2    ; Ytm;
ð
Zt1Zt2    ; Ztm; lI1 t  1
ð
Þ; lI2 t  1
ð
Þ;    ; lIc t  1
ð
Þ;
vI1 t  1
ð
Þ; vI2 t  1
ð
Þ;    ; vIc t  1
ð
ÞÞÞ þ et
ð16Þ
BC-IFTS-FM, via IFCM, generates the membership and
the non-membership by clustering load and air tempera-
tures together and also uses lagged variables of both load
and air temperature as input besides these memberships
and non-memberships. The basic structure of BC-IFTS-M
can be given in Fig. 3.
The list of process parameters is given below:
maxitr
Maximum number of iterations.
m
Number of lagged crisp variables of Load and
Temperature.
K
The number of HLU.
ttrain
Number of observations for the training set.
ttest
Number of observations for test set.
c
Number of IFSs.
T
Number of time series observations.
The pseudo-code is presented which deﬁnes as a step-
by-step description of the working principle of both
C-IFTS-FM algorithm.
20174
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 9
Algorithm: UC-IFTS-M / BC-IFTS-M.
4 Data and implementation scenarios
Short-term load data include complicated relations for
forecasting. These complicated relations can be in a
structure of linear or nonlinear. Moreover, most of the
time, it can consist of both of these structures. In this
context, the STLF problem has been chosen to validate and
demonstrate the performance of the forecasting model
proposed in this study on a forecasting problem with such
complex relationships. Moreover, as emphasized before,
for the power suppliers and managers, performing an
accurate and consistent STLF is crucial. By the objectives
of this study, ﬁrstly, the hourly load data of the power
supply company of the city of Johor in Malaysia (PSJM)
generated in 2009 and 2010 (see Fig. 4) were analysed.
Furthermore, as mentioned before, based on the fact that
the load is particularly affected by the air temperature, the
air temperature data sets (see Fig. 5) observed in the same
period were also used as auxiliary time series in STLF.
Secondly, as in Deng et.al. [46], the proposed UC-FITS-
FM was applied to three data sets (HEXING, CHENG-
NAN, and EUNITE). All experimental data sets were
downloaded
at
https://github.com/chenxiaoxin-102496/
DataSet.git given in [46]. HEXING and CHENGNAN data
sets consist of 251 (from 8/01/2019 to 04/07/2020) and 247
(from 08/05/2019 to 04/07/2020) observations, respec-
tively. EUNITE data set consists of 761 observations (from
01/01/1997 to 01/31/1999).
Finally, the proposed univariate model’s performance
was evaluated using Tu¨rkiye’s monthly electricity pro-
duction (T-MEP) data sets. The data sets were sourced
from Energy Exchange Istanbul (EXIST) (https://www.
epias.com.tr/en/) and reorganized into monthly periods,
comprising 125 observations from January 2012 to May
2022, just like in the study of Gulay et al. [47].
4.1 Data organization
The forecasting performance of the proposed UC-IFTS-FM
and BC-IFTS-FM was validated and evaluated by dividing
the data sets into two sets as training and test. For PSJM,
the details of the training and test sets created for the
hourly load data consisting of 8760 observations for each
year are given in Fig. 6.
Moreover,
for
the
HEXING,
CHENGNAN,
and
EUNITE data sets, the details of the training and test sets
are given in Fig. 7.
Finally, for the T-MEP data sets, the details of the
training, validation, and test sets are given in Fig. 8. In
these data sets, unlike the others, just like in the study of
Neural Computing and Applications (2024) 36:20167–20192
20175
123

---

## Page 10
Gulay et al. [47], a validation data set was used and the
optimal hyperparameters were determined according to the
performance of the trained models on the validation data
sets. Tu¨rkiye’s electricity production consists of various
components depending on the sources used for generation.
The proposed univariate model was used to forecast seven
components and the total production (TP) data sets. These
seven data sets show how much electricity is produced
from natural gas (NG), hydro (HYD), coal (COAL), wind
(WIND), fuel oil (FO), bioenergy (BIO), and geothermal
power (GEO).
4.2 Performance measures
The comparative performance evaluation of the models
was realized by using mean absolute percentage error
(MAPE) and root mean square error (RMSE) which are
given in Eqs. (17) and (18).
Fig. 3 The structure of BC-IFTS-M designed for STLF
20176
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 11
MAPE ¼ mean
Actualt  Forecastedt
Actualt

  100%


; t ¼ 1,2;    ; T
ð17Þ
RMSE ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
mean
Actualt  Forecastedt
ð
Þ2


r
; t ¼ 1,2;    ; T
ð18Þ
Moreover, the median relative absolute error (MdRAE),
a measure of relative error, is also used to compare with a
reference model. The MdRAE is calculated as in Eq. (20).
Here, rt is the relative error given in Eq. (19).
rt ¼ Actualt  Forecastedt
Actualt  Forecasted
t
; t ¼ 1,2;    ; T
ð19Þ
MdRAE ¼ Median rt
j j; t ¼ 1,2;    ; T
ð20Þ
Fig. 4 The hourly load data of
Malaysia of the years of 2009
and 2010
18
20
22
24
26
28
30
32
34
36
38
Temperaure (Celsius)
18
20
22
24
26
28
30
32
34
36
38
Temperaure (Celsius)
Fig. 5 The hourly air
temperature data of the years of
2009 and 2010
Neural Computing and Applications (2024) 36:20167–20192
20177
123

---

## Page 12
Forecasted
t
is the forecasted values produced by a
benchmark model chosen as the reference model. The
naive model was considered as a reference model, just like
most of the other studies in the literature. In the naive
model; Forecasted
t ¼ Actualt1.
4.3 Scenarios of implementations
This study basically presents two forecasting models as
UC-IFTS-FM and BC-IFTS-FM. Different implementa-
tions were designed by taking different parameters for the
analysis process in both forecasting models for STLF.
These parameters and their usage characteristics are
detailed in Table 1.
The results of 288 different applications were evaluated
using statistics such as average, minimum, and maximum.
In this evaluation, the worst designs in terms of perfor-
mance besides the best designs were also considered and
compared with the best performances of other models
available in the literature. In this way, the performance of
the proposed models for the forecasting problem was
investigated extensively as a whole.
4.4 Consistency/reliability and validity
of forecasts
As in all other forecasting problems, there are two
important concepts for forecasting models in STLF: Reli-
ability and validity. For a model, which is reliable, it is said
that it has internal consistency. Actually, reliability is a
principle with a degree. Therefore, one cannot mention
being completely reliable of any particular model. Since
chance and random effects are always present, it is quite
normal for analyses to differ in performance. However, for
a sufﬁcient and efﬁcient forecasting model, performance is
expected to vary within the narrow intervals from one
implementation to another.
Another important concept is validity which can be
considered as a measure of accuracy for a forecasting
model. An interaction between reliability and validity is
explicit, and this interaction can be illustrated in Fig. 9. On
the ﬁrst dartboard, the hits are far from the target and quite
messy. The mentioned model has a high margin of error
and its consistency cannot be relied upon. The second
dartboard represents an illustration of the reliable but not
valid hits. Illustrated model has fairly low variability, but
outputs/hits are off-target. The third one represents a case
where the outputs are neither reliable nor valid. The ﬁnal
illustration includes the case where the expected from a
satisfactory forecasting model. The outputs/hits, in this
case, are both consistently showing similar values and
fairly near to the targets of interest. In the light of all this
information, the two proposed models were run 30 times
over architectural structures that produced both the best
and the worst results to be detailed examination in terms of
validity and consistency.
5 Results and discussions
To demonstrate the effectiveness and forecasting ability of
the proposed models, the results have been evaluated from
different points of view.
PSJM
Fig. 6 Data organization for
PSJM data sets in STLF
20178
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 13
5.1 Evaluation of all implementations-PSJM data
sets
As it is emphasized before, for STLF, 288 different
implementations were designed. Table 2 shows some of the
statistics belonging to 3 error criteria obtained from 288
applications for the training and test sets of PSJM data sets.
From Table 2, the UC-IFTS-FM produced forecasts
with a minimum MAPE value of 0.3203% for the test set of
load data in the 2009 year. For the test set of load data in
the 2010 year, the forecasts produced by UC-IFTS-FM had
Fig. 7 Data organization for HEXING (a), CHENGNAN (b), and EUNITE (c) data sets
Fig. 8 Data organization for
T-MEP data sets
Neural Computing and Applications (2024) 36:20167–20192
20179
123

---

## Page 14
a minimum MAPE value of 0.3571%. Another remarkable
ﬁnding in Table 2 is that the model can produce forecasts
with a percentage error of approximately 2% (for 2009
load data test set: 2.6527% and for 2010 load data test set:
2.1681%) even for the cases where it shows the worst
performance in all 288 analysis. Moreover, for both the
2009 and 2010 years, load data sets, the average of the
MAPE values of the forecasts obtained from 288 imple-
mentations of UC-IFTS-FM was observed to be even less
than 1%. The reason why the evaluations made so far have
been made over the MAPE is that MAPE is a pure error
criterion independent of the scale of the data. According to
Table 2, parallel comments can also be made for RMSE
and MdRAE. All these ﬁndings and conclusions are also
valid for BC-IFTS-FM, which produces similar results. In
addition, when the results of UC-IFTS-FM and BC-IFTS-
FM are evaluated together; although these two models have
close forecasting performances, it can be said that BC-
IFTS-FM has a slightly better performance. Another result
that can be drawn from Table 2 is that the performances in
the training and test sets for load data for both 2009 and
2010 are close to each other. This can be seen as an indi-
cation that the proposed models are producing consistent
results, and they are also producing reliable forecasts for
out-of-sample data.
5.2 Comparison to the state-of-the-art models—
PSJM data sets
Among the 288 analyses, the models were run 30 times for
the two cases that produced the best and the worst results in
terms of RMSE values over the training set, and the
average statistics of the obtained MAPE, RMSE, and
MdRAE criteria values were calculated. As a traditional
time series forecasting method, seasonal auto-regressive
integrated moving average (SARIMA) was preferred to use
in comparison because the SARIMA model has the best
compatibility to the Malaysia load data sets in the years of
2009 and 2010 via their seasonal structure. The best models
were determined as SARIMA (1,0,3)(2,1,2) for load data
2009 and SARIMA(1,0,1)(1,1,2) for load data in 2010 [27].
Some of the other models used in the comparative evalu-
ation of performances are fuzzy-based models, while others
are forecasting models based on deep networks. These are:
•
Probabilistic weighted fuzzy time series (PWFTS)
•
Weighted fuzzy time series (WFTS)
•
Integrated weighted fuzzy time series (IWFTS)
•
Long short-term memory (LSTM)
•
Model 1 (168 former lags)
•
Model 2 (72 former lags)
•
Model 3 (48 former lags)
•
Model 4 (24 former lags)
•
The combined method (FTS-CNN)
These results are presented in Tables 3, 4 and 5 together
with the results obtained with other STLF methods. The
results of other STLF methods are taken from Sadaei et.al.
[27]. Considering Table 3, it is observed that the proposed
BC-IFTS-FM, which uses temperature data as auxiliary
time series in the analysis process, showed the best per-
formance for both the years 2009 (0.43%) and 2010
(0.41%) in the best case of it. Moreover, even in the worst
case of BC-IFTS-FM, it is seen that the proposed model
produced superior forecasts than the other models in the
STLF literature (2.33% for 2009 and 2.06% for 2010). In
addition, UC-IFTS-FM,
which
performs
a univariate
analysis process, produced better forecasts than the other
current models for both the best and worst cases of it. The
proposed
BC-IFTS-FM,
for its best cases, achieved
approximately 86% better accuracy than the FTS-CNN,
which ranked second in both 2009 and 2010. Compared to
the FTS-CNN, which ranked second even in the worst
cases of the proposed model, these rates are approximately
23% and 29% for 2009 and 2010, respectively. Similarly,
the proposed UC-IFTS-FM has approximately 85% better
forecasting performance than FTS-CNN, which ranked
second for both 2009 and 2010, in the case of the best
Table 1 The implementation designs
Changing
# of Lagged Variables
# of IFS
# of HLU
from
2
3
2
to
5
10
10
# of Implementation
288
Neither Valid
nor Reliable
Reliable
but not Valid
Fairly Valid
but not very Reliable
Valid &
Reliable
Fig. 9 The interaction between
reliability/consistency and
validity
20180
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 15
situation. Even in the worst cases of the proposed model,
these rates are approximately 25% and 28% for 2009 and
2010, respectively. At this point, it should be noted that the
selection of the best and the worst cases among the 288
implementations performed for the proposed models is
determined based on the performance of the models over
the training set. That is, the best case implementations
determined here can always be obtained without the need
for out-of-sample data points. The worst results are also
presented to emphasize the superior performance of the
proposed methods in each case.
Similar ﬁndings to those obtained for MAPE were also
obtained for RMSE. Both of the proposed models, for their
best cases, presented over 85% better accuracy than the
FTS-CNN, which ranked second in both 2009 and 2010. In
addition, in terms of the RMSE criterion, the proposed
models, even for their worst cases, performed over 30%
and 20% better accuracy than the FTS-CNN in 2009 and
2010, respectively.
Considering the MdRAE criterion, both of the proposed
models, for their best cases, presented over 80% better
performance than the FTS-CNN, which ranked second in
both 2009 and 2010. Moreover, for their worst cases
compared to FTS-CNN in 2009, the proposed BC-IFTS-
FM made progress with a ratio of 5%, while the proposed
UC-IFTS-FM made progress with a ratio of 10%. For 2010,
these progress levels are about 15% for both proposed
models.
5.3 The statistical evaluation of the errors—
PSJM data sets
By running the proposed models for STLF 30 times, it can
make a statistical evaluation over some statistics of the
errors. Table 6 presents these statistics for MdRAE error
criterion values produced by BC-IFTS-FM and UC-IFTS-
FM for test sets, their best cases. It is clear from Table 6
that both proposed models produce forecasts with quietly
low MdRAE values compared to other models, even for
repetition where forecasts are generated with a maximum
MdRAE. In addition, when the standard deviation is taken
into account, it is observed that the variation of the fore-
casting errors is pretty small and the very narrow conﬁ-
dence interval (CI) bounds also support this situation. In
addition, considering the kurtosis and skewness values of
the errors and the standard errors of these values, it was
determined that the MdRAE values showed a normal dis-
tribution
and
thus
the
error
probabilities
could
be
calculated.
The distribution of MdRAE values obtained from 30
repetitions of both models can be presented with the graphs
given in Figs. 10 and 11. The MdRAE values which have
such scattering can be evaluated in two different ways. One
of them is reliability. For a reliable forecasting model,
performance metrics are expected to vary within narrow
ranges from one implementation to the other, as mentioned
in previous sections. From Fig. 10, in the case of the best
situations, it is observed that the MdRAE values of fore-
casts produced by two proposed models are scattered
between 0.04 and 0.10 for the years 2009 and 2010. From
Fig. 11, in the case of the worst situations, it is seen that the
MdRAE values are scattered approximately between 0.20
Table 2 Some statistics on error criteria for 288 implementations
Model
Statistic
Data Set
MAPE
RMSE
MdRAE
2009
2010
2009
2010
2009
2010
UC-IFTS-FM (UNIVARIATE)
Min
Training
0.3317%
0.3766%
175.4178
211.01606
0.0463
0.0598
Test
0.3203%
0.3571%
159.5506
210.21613
0.0459
0.0578
Max
Training
2.5914%
2.5891%
1335.5160
1448.87486
0.4167
0.4201
Test
2.6527%
2.1681%
1277.0889
1427.48491
0.5372
0.4380
Average
Training
0.8819%
0.9868%
481.22116
538.73720
0.1442
0.1615
Test
0.8842%
0.8956%
444.65748
530.84009
0.1623
0.1659
BC-IFTS-FM (BIVARIATE)
Min
Training
0.3255%
0.3806%
175.0835
205.2821
0.0472
0.0576
Test
0.3246%
0.3444%
159.8204
210.8734
0.0522
0.0550
Max
Training
2.6800%
2.5818%
1455.4642
1494.2805
0.4220
0.4191
Test
2.6056%
2.3178%
1388.8959
1438.4058
0.4960
0.4014
Average
Training
0.8555%
0.9463%
463.5468
512.2697
0.1382
0.1531
Test
0.8673%
0.8537%
435.7309
497.9765
0.1578
0.1588
Neural Computing and Applications (2024) 36:20167–20192
20181
123

---

## Page 16
and 0.60 for both years. In both cases, it has been observed
that the MdRAE values are scattered within a fairly narrow
range, which is proof of the reliability of the proposed
models. Secondly, to focus on validity. Even in the worst
case, the proposed models revealed a very small MdRAE in
all repetitions. Among repetitions, the highest MdRAE
values have been found around 0.10 for the best cases and
0.60 for the worst case. These values are evidence that the
proposed models produce highly satisfactory predictive
results in all cases and are valid models.
5.4 The convergence time of the proposed
models—PSJM data sets
This subsection is aimed to prove that the proposed models
have a reasonable convergence time as another ﬁnding
proving their superiority over other existing models. For
this purpose, the average convergence times for 30 times
repeated implementations in the best and worst cases of the
two models were determined in seconds. The information
collected in this direction is summarized in Table 7. From
Table 7, it is seen that the convergence time is longer than
Table 3 Average MAPE (%) of
the models in STLF
Forecasting model
2009
2010
Average
Rank
Average
Rank
BC-IFTS-FM (The Proposed Model/Best)
0.43
1
0.41
1
BC-IFTS-FM (The Proposed Model/Worst)
2.33
4
2.06
3
UC-IFTS-FM (The Proposed Model/Best)
0.45
2
0.44
2
UC-IFTS-FM (The Proposed Model/Worst)
2.25
3
2.07
4
SARIMA
4.68
12
4.23
11
FTS-CNN
3.02
5
2.89
5
PWFTS model 1
3.86
7
4.00
8
PWFTS model 2
4.59
11
5.83
12
WFTS
5.33
14
9.09
14
IWFTS
5.32
13
7.69
13
LSTM model 1
3.71
6
3.45
6
LSTM model 2
4.55
10
4.21
9
LSTM model 3
4.11
9
4.23
10
LSTM model 4
3.93
8
3.88
7
Bold-Underline values represent the best-performing models
Bold values only represent the second-best-performing models
Table 4 Average RMSE of the
models in STLF
Forecasting model
2009
2010
Average
Rank
Average
Rank
BC-IFTS-FM (The Proposed Model/Best)
200.41
1
228.28
1
BC-IFTS-FM (The Proposed Model/Worst)
1214.03
4
1296.37
3
UC-IFTS-FM (The Proposed Model/Best)
213.98
2
251.30
2
UC-IFTS-FM (The Proposed Model/Worst)
1184.08
3
1340.95
4
SARIMA
2763.66
11
2501.25
11
FTS-CNN
1777.99
5
1702.70
5
PWFTS model 1
2230.91
7
2162.57
8
PWFTS model 2
2987.40
14
3797.35
12
WFTS
2930.36
12
4419.11
13
IWFTS
2961.17
13
4663.17
14
LSTM model 1
2194.19
6
2037.49
6
LSTM model 2
2689.42
10
2044.68
7
LSTM model 3
2413.60
9
2483.71
10
LSTM model 4
2317.88
8
2279.23
9
Bold-Underline values represent the best-performing models
Bold values only represent the second-best-performing models
20182
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 17
the others in cases the best results are produced. This is
because the architectures which produced the best perfor-
mances have more IFS and HLUs. Even for these cases, the
convergence time is on average between 1.5 and 2.5 min,
and such a convergence time is remarkably reasonable and
applicable. In the worst scenarios, the convergence speed is
much higher, with around 5 s or less. Given forecasts
having high accuracy obtained for these scenarios, it can be
Table 5 Average MdRAE of
the models in STLF
Forecasting model
2009
2010
Average
Rank
Average
Rank
BC-IFTS-FM (The Proposed Model/Best)
0.0707
1
0.0712
1
BC-IFTS-FM (The Proposed Model/Worst)
0.4621
4
0.3869
4
UC-IFTS-FM (The Proposed Model/Best)
0.0720
2
0.0756
2
UC-IFTS-FM (The Proposed Model/Worst)
0.4358
3
0.3853
3
SARIMA
0.7504
12
0.6655
10
FTS-CNN
0.4857
5
0.4537
5
PWFTS model 1
0.6107
8
0.6319
8
PWFTS model 2
0.5284
6
0.7638
12
WFTS
1.0838
14
2.1105
14
IWFTS
1.0780
13
1.2185
13
LSTM model 1
0.5981
7
0.5435
6
LSTM model 2
0.7313
11
0.6622
9
LSTM model 3
0.6610
10
0.6673
11
LSTM model 4
0.6273
9
0.5991
7
Bold-Underline values represent the best-performing models
Bold values only represent the second-best-performing models
Table 6 Some statistics on
MdRAE error criterion of test
sets for 30 times running
Model
Statistic
MdRAE
2009
2010
C-IFTS-FM (UNIVARIATE)
Min
0.0459
0.0500
Max
0.0912
0.1006
Standard Deviation
0.0146
0.0127
Mean
Lower Bound of %95 CI
0.0665
0.0709
Value
0.0720
0.0756
Standard Error
0.0027
0.0023
Upper Bound of %95 CI
0.0774
0.0804
Skewness
- 0.3442
0.2143
Standard Error
0.4268
0.4270
Kurtosis
- 1.3805
- 0.4560
Standard Error
0.8326
0.8330
BC-IFTS-FM (BIVARIATE)
Min
0.0471
0.0561
Max
0.0952
0.0858
Standard Deviation
0.0144
0.0079
Mean
Lower Bound of %95 CI
0.0653
0.0682
Value
0.0707
0.0712
Standard Error
0.0026
0.0014
Upper Bound of %95 CI
0.0761
0.0741
Skewness
0.1018
0.1379
Standard Error
0.4269
0.4270
Kurtosis
- 1.0479
- 0.7904
Std. Error
0.8327
0.8330
Neural Computing and Applications (2024) 36:20167–20192
20183
123

---

## Page 18
said
that
these
times
are
outstanding
for
STLF
practitioners.
5.5 The fit of forecasted and observed data
points—PSJM data sets
It has been proven from different points of view that both
models proposed for both data sets in all scenarios have
superior performance compared to other models until this
section. In this section, these ﬁndings are supported by
providing visual evidence showing the high ﬁtting between
the forecasts obtained for some scenarios and the observed
values. For this purpose, in the best situations of BC-IFTS-
FM, the graph of the forecasts and observations values is
shown in Figs. 12 and 13. The high synchronization of the
forecasts with the observed values is clearly observed in
these two graphs.
5.6 Comparison to the state-of-the-art models—
HEXING, CHENGNAN, and EUNITE data sets
For these data sets, the best results, in terms of RMSE
values over the training set, were compared with some
other methods used by Deng et.al. [46]. Other methods can
be listed as:
The comparative evaluation of performances are fuzzy-
based models, while others are forecasting models based on
deep networks. These are:
•
Gene expression programming (GEP)
•
Gene expression programming based on least square
(GEP-LS)
•
Gene expression programming based on K-means and
least square (GEP-KLS)
•
Quantitative combination load forecasting (QCLF)
Fig. 10 The distribution of
MdRAE values in the case of
the best situations
Fig. 11 The distribution of
MdRAE values in the case of
the worst situations
20184
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 19
•
LSTM
•
Pattern-based local linear regression (PLLR)
•
Back-propagation neural network (BPNN)
All results of other methods are from Deng et al. [46].
The comparative results, in terms of RMSE and MAPE
metrics, are presented in Tables 8 and 9.
Table 8 shows that the proposed UC-IFTS-FM produced
the best performance for all three data sets, even for the
worst case of the proposed model over other methods. For
the best case, the forecasts produced by the proposed UC-
IFTS-FM had RMSE values of 0.5747, 0.2907, and 1.4992,
respectively. These values were 8.12, 4.80, and 0.84, even
in the worst case. Even in the worst case, the proposed
model made progress by about 55% (HEXING), 70%
(CHENGNAN), and 39% (EUNITE), respectively, over the
best of the others. Also, in the best case, progress was
phenomenal, with 95%, 97%, and 86%, respectively, over
the best of the rest. To respecify, the best and the worst
cases for testing sets among all implementations performed
for the proposed model were determined based on the
performance of the models over the training set.
Similar results, for the MAPE, to the RMSE metric were
obtained. In HEXING forecasting, the proposed model, in
its best case, presented 93% better accuracy than BPNN
which was the best among the others. In CHENGNAN and
UENITE forecasting, the accuracy progress levels are 55%
and 37% over the GEP-KLS which was the best among the
others, respectively.
5.7 Comparison to the state-of-the-art models–
T-MEP data sets
The optimal hyperparameter combinations obtained from
the validation sets for the eight-time series that make up the
T-MEP data set are given in Table 10.
Tables 11 and 12 offer the MAPE and RMSE, along
with their ranks (R), as measures for assessing and com-
paring the forecasting performance of the models on out-
of-sampling time points. The loss function values of other
models used in the comparison were sourced from the
study by Gulay et al. [47]. The results produced by 19
different forecasting models in addition to the proposed
univariate model were presented to compare prediction
performances in Tables 16 and 17. However, since the
ARDL model has its own characteristics, the values cor-
responding to certain series are left blank, as in the study of
Gulay et al. [47]. The MAPE results presented in Table 11
Table 7 Convergence time (in seconds) of the proposed models
The Proposed Model
Year of Data
Case
# of Lagged Variables
# of IFS
# of HLU
Time in averagely second
BC-IFTS-FM
2009
Best
3
9
8
120.55
Worst
4
3
2
5.63
2010
Best
2
10
7
146.40
Worst
3
3
2
5.41
UC-IFTS-FM
2009
Best
2
10
10
88.91
Worst
3
3
2
3.91
2010
Best
2
10
9
94.28
Worst
4
3
2
3.83
Fig. 12 The harmony of forecasted and observed loads for BC-IFTS-FM in 2009
Neural Computing and Applications (2024) 36:20167–20192
20185
123

---

## Page 20
reveal that the proposed UC-IFTS-FM model, compared to
the others, demonstrates outstanding forecasting perfor-
mance for all time series. In addition, the improvements
made by the proposed model in prediction performance
compared to the best model among the other 19 models are
also given in Table 11 for each data set. According to these
results, in terms of the MAPE criterion, the proposed
model has improved forecasting performance for the
‘‘COAL’’ data set by over 80%. The progress levels,
exhibited by the proposed UC-IFTS-FM, for ‘‘HYD’’ and
‘‘WIND’’ data sets, were observed as 63.53 and 54.48%,
respectively. Moreover, the progress levels, shown by the
proposed UC-IFTS-FM, for ‘‘NG’’ and ‘‘GEO’’ data sets,
were seen as over 40 and 30%, respectively. Furthermore,
for the ‘‘TP’’, the progress level was over 20%. The RMSE
results summarized in Table 12 prove that the proposed
UC-IFTS-FM model, compared to the others, exhibits
again superior forecasting performance for all time series
except the ‘‘NG’’ data set. In terms of RMSE, the progress
levels,
provided
by
the
proposed
UC-IFTS-FM,
for
‘‘HYD’’ and ‘‘COAL’’ data sets, reached 70 and 90%
levels, respectively. Moreover, the compatibility of the
forecasts obtained for each T-MEP data set with the actual
observation values is visually presented in Fig. 14.
6 Conclusions
Two new forecasting models, UC-IFTS-FM and BC-IFTS-
FM, were proposed in this study with the aim of short-term
load forecasting. The proposed models are based on IFSs
and neural networks with the cascade structure. One of
these proposed models has been designed in a way that air
temperature information is also used in the STLF, based on
the fact that the load is particularly affected by the air
temperature. The proposed models have been performed in
different implementation scenarios. PSJM data sets were
forecasted in 288 different scenarios with both proposed
Fig. 13 The harmony of forecasted and observed loads for BC-IFTS-FM in 2010
Table 8 Performance
comparison between different
models for testing data sets—
RMSE
Forecasting Model
Data sets
HEXING
CHENGNAN
EUNITE
RMSE
Rank
RMSE
Rank
RMSE
Rank
The Proposed UC-IFTS-FM (Best)
0.5747
1
0.2907
1
1.4992
1
The Proposed UC-IFTS-FM (Worst)
5.6477
2
3.4904
2
6.7035
2
QCLF
12.9326
5
12.5342
4
13.9355
6
GEP-KLS
12.7206
4
11.5153
3
10.9587
3
GEP-LS
21.5100
9
22.5342
9
14.4026
8
GEP
12.9326
6
12.5342
5
13.9355
7
LSTM
18.7941
8
14.7829
8
11.9168
4
PLLR
15.7051
7
12.9215
6
15.8813
9
BPNN
12.5609
3
13.6523
7
13.7958
5
Bold-Underline values represent the best-performing models
Bold values only represent the second-best-performing models
20186
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 21
Table 9 Performance
comparison between different
models for testing data sets—
MAPE(%)
Forecasting Model
Data sets
HEXING
CHENGNAN
EUNITE
MAPE
Rank
MAPE
Rank
MAPE
Rank
The Proposed UC-IFTS-FM (Best)
0.90
1
0.33
1
0.18
1
The Proposed UC-IFTS-FM (Worst)
8.12
2
4.80
2
0.84
2
QCLF
13.90
4
13.55
5
1.83
6
GEP-KLS
13.99
6
11.23
3
1.33
3
GEP-LS
20.37
9
23.55
9
1.83
8
GEP
13.90
5
13.55
6
1.83
7
LSTM
18.38
8
12.55
4
1.56
4
PLLR
15.08
7
14.29
8
2.21
9
BPNN
12.93
3
14.17
7
1.72
5
Bold-Underline values represent the best-performing models
Bold values only represent the second-best-performing models
Table 10 Optimal
hyperparameter values for
T-MEP data sets
Hyperparameter
Data Sets
TP
NG
HYD
COAL
WIND
FO
GEO
BIO
# of Lagged Variables
2
2
2
2
2
2
3
2
# of IFS
8
10
10
10
4
6
5
3
# of HLU
3
2
7
5
6
5
8
7
Table 11 Performance comparison for T-MEP testing data sets—MAPE(%)
Methods
TP
R
NG
R
HYD
R
COAL
R
WIND
R
FO
R
GEO
R
BIO
R
SARIMA
2.26
6
10.68
6
10.40
4
11.13
11
14.01
11
161.23
8
2.18
3
2.80
7
HW Add
30.11
19
32.25
15
26.57
13
27.12
17
70.76
18
4573.98
17
88.67
19
88.69
19
HW Mult
30.11
20
32.27
16
26.21
12
25.97
16
65.56
17
4856.85
18
88.62
18
88.68
17
ETS
1.93
4
11.13
7
12.22
7
9.40
7
12.70
9
240.21
11
2.42
5
2.99
8
TBATS
2.27
7
12.87
8
11.82
6
10.14
8
12.64
8
124.30
7
3.67
9
3.34
12
STL-SARIMA
2.06
5
8.07
3
27.43
14
7.27
3
11.56
4
358.14
13
2.67
6
2.59
6
STL-HW Add
29.99
17
34.85
17
28.57
17
41.80
20
77.17
20
4001.27
16
87.69
16
88.58
16
STL-HW Mult
30.02
18
35.74
18
32.02
19
36.08
19
74.89
19
6990.74
19
88.14
17
88.69
18
STL-ETS
1.63
3
8.65
5
11.01
5
8.10
5
11.80
5
557.87
15
4.11
10
2.07
3
ANN
5.57
13
27.84
13
24.92
11
14.97
15
16.87
14
230.73
10
54.99
15
2.54
5
LSTM
3.91
9
17.16
10
21.20
10
10.29
9
15.81
12
76.33
6
3.07
7
3.17
11
CNN
6.93
16
30.16
14
27.56
15
13.15
13
16.20
13
166.88
9
3.60
8
2.32
4
STL-ANN
5.75
14
38.92
19
64.85
20
28.08
18
30.79
16
9909.66
20
46.85
14
3.10
10
STL-LSTM
1.63
2
4.71
2
9.13
2
7.51
4
10.42
3
50.61
5
2.09
2
3.05
9
STL-CNN
5.51
12
15.02
9
10.37
3
5.65
2
10.26
2
337.96
12
2.39
4
1.97
2
MV-ANN
5.24
10
8.14
4
12.62
8
10.61
10
13.69
10
25.63
2
9.78
13
8.76
14
MV-LSTM
5.43
11
22.65
11
29.14
18
9.12
6
12.26
7
26.60
3
5.55
11
4.41
13
MV-CNN
6.74
15
26.41
12
27.70
16
13.42
14
17.60
15
27.89
4
5.85
12
11.76
15
ARDL
3.09
8
–
–
16.54
9
12.91
12
11.90
6
403.62
14
–
–
–
UC-IFTS-FM
1.30
1
2.65
1
3.33
1
0.78
11
4.67
1
23.58
1
1.37
1
1.50
1
Progress Level
20.25%
43.74%
63.53%
86.19%
54.48%
8.00%
34.45%
23.86%
Bold-Italic values represent the progress levels
Bold-Underline values represent the best-performing models
Neural Computing and Applications (2024) 36:20167–20192
20187
123

---

## Page 22
Table 12 Performance comparison for T-MEP testing data sets—RMSE
Methods
TP
R
NG
R
HYD
R
COAL
R
WIND
R
FO
R
GEO
R
BIO
R
SARIMA
913,751
7
1,139,236
7
521,572
3
1,029,488
11
493,040
13
21,366
13
22,115
5
18,577
6
HW Add
8,208,756
19
2,375,007
13
1,881,202
16
2,578,660
18
2,000,264
18
204,925
17
669,103
19
488,318
18
HW Mult
8,209,099
20
2,378,611
14
1,885,108
17
2,492,407
17
1,883,016
17
226,518
18
668,737
18
488,314
17
ETS
685,158
4
1,076,002
6
731,128
7
823,965
6
396,434
8
28,695
14
21,670
2
19,234
8
TBATS
764,334
6
1,161,169
8
691,392
6
995,496
10
386,006
6
13,971
9
30,403
8
22,752
12
STL-SARIMA
745,460
5
867,286
4
1,485,190
10
736,196
4
333,149
4
16,426
10
22,959
6
15,310
4
STL-HW Add
8,183,556
17
2,514,487
17
2,143,232
18
3,568,360
19
2,150,919
20
191,952
16
661,969
16
487,804
16
STL-HW Mult
8,191,133
18
2,586,084
18
2,570,716
19
3,618,517
20
2,085,589
19
363,411
19
665,200
17
488,424
19
STL-ETS
675,535
3
882,909
5
638,401
4
750,137
5
341,218
5
29,168
15
34,102
9
13,104
2
ANN
1,927,761
13
2,079,753
11
1,683,690
14
1,233,064
15
509,480
14
9656
7
414,717
14
19,865
9
LSTM
1,510,685
9
1,864,405
10
1,500,310
12
875,692
8
456,276
11
4233
6
29,172
7
19,896
10
CNN
2,466,245
15
2,418,549
15
1,672,880
13
1,106,566
12
475,691
12
10,820
8
35,437
10
16,427
5
STL-ANN
1,900,929
12
3,330,084
19
2,984,626
20
2,466,662
16
873,603
16
503,645
20
434,638
15
21,385
11
STL-LSTM
658,631
2
529,115
1
450,056
2
692,133
3
328,497
3
2819
5
22,040
4
18,747
7
STL-CNN
1,707,045
10
1,276,826
9
668,990
5
587,653
2
304,432
2
20,128
11
21,767
3
13,591
3
MV-ANN
1,777,954
11
800,185
3
752,801
8
957,319
9
421,917
9
1737
3
90,018
13
57,790
14
MV-LSTM
2,052,424
14
2,236,366
12
1,485,294
11
867,887
7
422,323
10
1736
2
47,729
11
35,696
13
MV-CNN
2,575,040
16
2,448,352
16
1,710,791
15
1,176,451
14
520,575
15
1810
4
56,465
12
68,785
15
ARDL
966,049
8
–
–
934,517
9
1,161,092
13
390,786
7
20,421
12
–
–
–
–
UC-IFTS-FM
524,296
1
669,827
2
133,672
1
39,526
1
186,479
1
1323
1
14,763
1
12,560
1
Progress Level
20.40%
–-
70.30%
93.27%
38.75%
23.79%
31.87%
4.15%
Bold-Italic values represent the progress levels
Bold-Underline values represent the best-performing models
20188
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 23
(c) Produced from Hydro
(d) Produced from Coal
(e) Produced from Wind
(f)
Produced from Fuel Oil
(g) Produced from Geothermal
(h) Produced from Bioenergy
(a) Total Production
(b) Produced from Natural Gas
Fig. 14 The harmony of forecasted and observed values for UC-IFTS-FM
Neural Computing and Applications (2024) 36:20167–20192
20189
123

---

## Page 24
univariate and multivariate models, and superior perfor-
mance was observed compared to other models even in
scenarios where the worst results were produced. More-
over, the consistency and reliability of the forecasts were
proven by running the proposed models 30 times, and the
results were analysed statistically. In addition, HEXING,
CHENGNAN, and EUNITE data sets were analysed in 288
different scenarios with the proposed univariate model, and
it was observed that even in the worst-performing scenario,
the proposed model exhibited a signiﬁcantly superior pre-
diction performance compared to the current value models.
Moreover, the T-MEP data sets, consisting of 8 different
time series, were analysed with the proposed univariate
model. In T-MEP analysis, hyperparameter tuning was
performed and the best hyperparameter combination was
determined based on validation sets. The main conclusions
obtained at the end of the study can be summarized as
follows:
•
The proposed UC-IFTS-FM and BC-IFTS-FM pro-
duced superior and more accurate forecasts than current
models in STLF.
•
With close and successful performance demonstrated
for training and test data in different scenarios, it has
been proven that the proposed models do not contain
the problem of overﬁtting.
•
The proposed BC-IFTS-FM results proved the impor-
tance of info on temperature data to improve perfor-
mance in STLF.
•
IFS-based models also take into account the non-
memberships based on hesitation degrees. By this
means, IFS-based models produced more advantageous
results in STLF compared to fuzzy-based models.
•
The proposed models have improved the performance
in the STLF since they can simultaneously model the
linear and nonlinear relationships between inputs and
outputs, thanks to the cascade structure.
•
The proposed models do not experience any loss of
information as they do not need the time series to be
converted into an image and thus exhibit superior
performance.
•
The proposed models achieve superior forecasting
performance in all scenarios at extremely reasonable
convergence times.
All ﬁndings of this paper can serve as a foundation for
further studies. In particular, new approaches incorporating
fuzzy sets with different properties and neural networks
with various structures can build on these results. We
believe these ﬁndings can be applied to mid-term and long-
term time series forecasting problems in many scientiﬁc
and practical areas, in addition to enhancing short-term
load forecasting.
Author contributions Ozge Cagcag Yolcu contributed to conceptu-
alization, methodology, software, and writing—original draft prepa-
ration. Hak-Keung Lam contributed to software, data curation,
writing—reviewing and editing, and supervision. Ufuk Yolcu con-
tributed to visualization, investigation, software, and validation.
Funding Open access funding provided by the Scientiﬁc and Tech-
nological Research Council of Tu¨rkiye (TU¨ BI˙TAK).
Data availability The data sets used and/or analysed during the cur-
rent study available from the corresponding author on reasonable
request.
Declarations
Conflict of interest The authors declare that they have no known
competing financial interests or personal relationships that could have
appeared to influence the work reported in this paper. The authors
declare the following financial interests/personal relationships which
may be considered as potential competing interests.
Open Access
This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit http://creativecommons.
org/licenses/by/4.0/.
References
1. Yolcu OC, Egrioglu E, Bas E, Yolcu U (2022) Multivariate
intuitionistic fuzzy inference system for stock market prediction:
the cases of Istanbul and Taiwan. Appl Soft Comput. https://doi.
org/10.1016/j.asoc.2021.108363
2. Va¨ha¨kyla P, Hakonen E, Le´man P (1980) Short-term forecasting
of grid load using Box-Jenkins techniques. Int J Electr Power
Energy Syst. https://doi.org/10.1016/0142-0615(80)90004-6
3. Moghaddas-Tafreshi SM, Farhadi M (2008) A linear regression-
based study for temperature sensi.wity analysis of iran electrical
load. In: Proceedings of the IEEE international conference on
industrial technology
4. Zheng Z, Chen H, Luo X (2019) A Kalman ﬁlter-based bottom-
up approach for household short-term load forecast. Appl Energy.
https://doi.org/10.1016/j.apenergy.2019.05.102
5. Hippert HS, Pedreira CE, Souza RC (2000) Combining neural
networks and ARIMA models for hourly temperature forecast. In:
Proceedings of the international joint conference on neural
networks
6. Weron R (2006) Modeling and forecasting electricity loads and
prices: a statistical approach. Wiley, London. https://doi.org/10.
1002/9781118673362
7. Taylor JW, McSharry PE (2007) Short-term load forecasting
methods: an evaluation based on European data. IEEE Trans
Power Syst. https://doi.org/10.1109/TPWRS.2007.907583
20190
Neural Computing and Applications (2024) 36:20167–20192
123

---

## Page 25
8. Zhang R, Dong ZY, Xu Y et al (2013) Short-term load fore-
casting of Australian national electricity market by an ensemble
model of extreme learning machine. IET Gener Transm Distrib.
https://doi.org/10.1049/iet-gtd.2012.0541
9. Senjyu T, Takara H, Uezato K, Funabashi T (2002) One-hour-
ahead load forecasting using neural network. IEEE Trans Power
Syst. https://doi.org/10.1109/59.982201
10. Nowotarski J, Liu B, Weron R, Hong T (2016) Improving short
term load forecast accuracy via combining sister forecasts.
Energy. https://doi.org/10.1016/j.energy.2015.12.142
11. Li S, Wang P, Goel L (2016) A novel wavelet-based ensemble
method for short-term load forecasting with hybrid neural net-
works and feature selection. IEEE Trans Power Syst. https://doi.
org/10.1109/TPWRS.2015.2438322
12. Chaturvedi DK, Sinha AP, Malik OP (2015) Short term load
forecast using fuzzy logic and wavelet transform integrated
generalized neural network. Int J Electr Power Energy Syst.
https://doi.org/10.1016/j.ijepes.2014.11.027
13. Zahedi G, Azizi S, Bahadori A et al (2013) Electricity demand
estimation using an adaptive neuro-fuzzy network: a case study
from the Ontario province - Canada. Energy. https://doi.org/10.
1016/j.energy.2012.10.019
14. Ghofrani M, Ghayekhloo M, Arabali A, Ghayekhloo A (2015) A
hybrid short-term load forecasting with a new input selection
framework. Energy. https://doi.org/10.1016/j.energy.2015.01.028
15. Khan IU, Javaid N, Taylor CJ, et al (2020) Big data analytics based
short term load forecasting model for residential buildings in smart
grids. In: IEEE INFOCOM 2020 - IEEE conference on computer
communications workshops, INFOCOM WKSHPS 2020
16. Atef S, Eltawil AB (2020) Assessment of stacked unidirectional
and bidirectional long short-term memory networks for electricity
load forecasting. Electric Power Syst Res. https://doi.org/10.
1016/j.epsr.2020.106489
17. Kumar S, Hussain L, Banarjee S, Reza M (2018) Energy load
forecasting using deep learning approach-LSTM and GRU in
spark cluster. In: Proceedings of 5th international conference on
emerging applications of information technology, EAIT 2018
18. Yu HK (2005) Weighted fuzzy time series models for TAIEX
forecasting. Physica A Stat Mech Appl. https://doi.org/10.1016/j.
physa.2004.11.006
19. Cagcag Yolcu O, Alpaslan F (2018) Prediction of TAIEX based on
hybrid fuzzy time series model with single optimization process.
Appl Soft Comput J. https://doi.org/10.1016/j.asoc.2018.02.007
20. Trierweiler Ribeiro G, Alves Portela Santos A, Cocco Mariani V,
dos Santos CL (2021) Novel hybrid model based on echo state
neural network applied to the prediction of stock price return
volatility. Expert Syst Appl. https://doi.org/10.1016/j.eswa.2021.
115490
21. Ren S, Wang X, Zhou X, Zhou Y (2023) A novel hybrid model
for stock price forecasting integrating Encoder Forest and
Informer. Expert Syst Appl. https://doi.org/10.1016/j.eswa.2023.
121080
22. Sadaei HJ, Enayatifar R, Abdullah AH, Gani A (2014) Short-term
load forecasting using a hybrid model with a reﬁned exponen-
tially weighted fuzzy time series and an improved harmony
search. Int J Electr Power Energy Syst. https://doi.org/10.1016/j.
ijepes.2014.04.026
23. Sadaei HJ, Guimara˜es FG, Jose´ da Silva C et al (2017) Short-term
load forecasting method based on fuzzy time series, seasonality
and long memory process. Int J Approx Reason. https://doi.org/
10.1016/j.ijar.2017.01.006
24. Efendi R, Ismail Z, Deris MM (2015) A new linguistic out-
sample approach of fuzzy time series for daily forecasting of
Malaysian electricity load demand. Appl Soft Comput J. https://
doi.org/10.1016/j.asoc.2014.11.043
25. Enayatifar R, Sadaei HJ, Abdullah AH, Gani A (2013) Imperialist
competitive algorithm combined with reﬁned high-order weigh-
ted fuzzy time series (RHWFTS-ICA) for short term load fore-
casting.
Energy
Convers
Manag.
https://doi.org/10.1016/j.
enconman.2013.08.039
26. Lee WJ, Hong J (2015) A hybrid dynamic and fuzzy time series
model for mid-term power load forecasting. Int J Electr Power
Energy Syst. https://doi.org/10.1016/j.ijepes.2014.08.006
27. Sadaei HJ, de Lima e Silva PC, Guimara˜es FG, Lee MH (2019)
Short-term load forecasting by using a combined method of
convolutional neural networks and fuzzy time series. Energy.
https://doi.org/10.1016/j.energy.2019.03.081
28. Wang T, Lai CS, Ng WWY et al (2021) Deep autoencoder with
localized stochastic sensitivity for short-term load forecasting. Int
J Electr Power Energy Syst. https://doi.org/10.1016/j.ijepes.2021.
106954
29. Zhao W, Li T, Xu D, Wang Z (2022) A global forecasting method
of heterogeneous household short-term load based on pre-trained
autoencoder and deep-LSTM model. Ann Oper Res. https://doi.
org/10.1007/s10479-022-05070-y
30. Berahmand K, Daneshfar F, Salehi ES et al (2024) Autoencoders
and their applications in machine learning: a survey. Artif Intell
Rev. https://doi.org/10.1007/s10462-023-10662-6
31. Berahmand K, Li Y, Xu Y (2023) DAC-HPP: deep attributed
clustering with high-order proximity preserve. Neural Comput
Appl. https://doi.org/10.1007/s00521-023-09052-4
32. Stefenon SF, Ribeiro MHDM, Nied A et al (2021) Hybrid
wavelet stacking ensemble model for insulators contamination
forecasting.
IEEE
Access.
https://doi.org/10.1109/ACCESS.
2021.3076410
33. Shakeel A, Chong D, Wang J (2023) District heating load fore-
casting with a hybrid model based on LightGBM and FB-prophet.
J Clean Prod. https://doi.org/10.1016/j.jclepro.2023.137130
34. Li Y, Zhu N, Hou Y (2023) A novel hybrid model for building
heat load forecasting based on multivariate Empirical modal
decomposition. Build Environ. https://doi.org/10.1016/j.buildenv.
2023.110317
35. Nti IK, Teimeh M, Nyarko-Boateng O, Adekoya AF (2020)
Electricity load forecasting: a systematic review. J Electr Syst Inf
Technol. https://doi.org/10.1186/s43067-020-00021-8
36. Candela Esclapez A, Lo´pez Garcı´a M, Valero Verdu´ S, Senabre
Blanes C (2022) Automatic selection of temperature variables for
short-term load forecasting. Sustain (Switzerland). https://doi.org/
10.3390/su142013339
37. Akhtar S, Shahzad S, Zaheer A et al (2023) Short-term load
forecasting models: a review of challenges, progress, and the road
ahead. Energies (Basel). https://doi.org/10.3390/en16104060
38. Atanassov KT (1986) Intuitionistic fuzzy sets. Fuzzy Sets Syst.
https://doi.org/10.1016/S0165-0114(86)80034-3
39. Gross G, Galiana FD (1987) Short-term load forecasting. Proc
IEEE 75:1558–1573. https://doi.org/10.1109/PROC.1987.13927
40. Zadeh LA (1965) Fuzzy sets. Inf Control. https://doi.org/10.1016/
S0019-9958(65)90241-X
41. Chaira T (2011) A novel intuitionistic fuzzy C means clustering
algorithm and its application to medical images. Appl Soft
Comput J 11(2):1711–1717
42. Demuth H, Raele MH (2009) Neural network toolbox user’s
guide for use with MATLAB. The MathWorks
43. Fahlman SE, Lebiere C (1990) The cascade-correlation learning
architecture. In: Advances in neural information processing
44. Fahlman SE, Lebiere C (1997) The cascade-correlation learning
architecture scott. In: Proceedings of NIPS
45. Alkhasawneh MS (2019) Hybrid cascade forward neural network
with elman neural network for disease prediction. Arab J Sci Eng.
https://doi.org/10.1007/s13369-019-03829-3
Neural Computing and Applications (2024) 36:20167–20192
20191
123

---

## Page 26
46. Deng S, Chen F, Wu D et al (2022) Quantitative combination
load forecasting model based on forecasting error optimization.
Comput Electr Eng. https://doi.org/10.1016/j.compeleceng.2022.
108125
47. Gulay E, Sen M, Akgun OB (2024) Forecasting electricity pro-
duction from various energy sources in Tu¨rkiye: a predictive
analysis of time series, deep learning, and hybrid models. Energy.
https://doi.org/10.1016/j.energy.2023.129566
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
20192
Neural Computing and Applications (2024) 36:20167–20192

---
