# Various optimized machine learning techniques to predict agricultural commodity prices

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-09679-x

---

## Page 1
ORIGINAL ARTICLE
Various optimized machine learning techniques to predict agricultural
commodity prices
Murat Sari1 • Serbay Duran2 • Huseyin Kutlu3 • Bulent Guloglu4 • Zehra Atik4
Received: 16 August 2023 / Accepted: 25 March 2024 / Published online: 16 April 2024
 The Author(s) 2024
Abstract
Recent increases in global food demand have made this research and, therefore, the prediction of agricultural commodity
prices, almost imperative. The aim of this paper is to build efﬁcient artiﬁcial intelligence methods to effectively forecast
commodity prices in light of these global events. Using three separate, well-structured models, the commodity prices of
eleven major agricultural commodities that have recently caused crises around the world have been predicted. In achieving
its objective, this paper proposes a novel forecasting model for agricultural commodity prices using the extreme learning
machine technique optimized with the genetic algorithm. In predicting the eleven commodities, the proposed model, the
extreme learning machine with the genetic algorithm, outperforms the model formed by the combination of long short-term
memory with the genetic algorithm and the autoregressive integrated moving average model. Despite the ﬂuctuations and
changes in agricultural commodity prices in 2022, the extreme learning machine with the genetic algorithm model
described in this study successfully predicts both qualitative and quantitative behavior in such a large number of com-
modities and over such a long period of time for the ﬁrst time. It is expected that these predictions will provide beneﬁts for
the effective management, direction and, if necessary, restructuring of agricultural policies by providing food requirements
that adapt to the dynamic structure of the countries.
Keywords Prediction  Commodity prices  Artiﬁcial neural network  Extreme Learning Machine  Long short-term
memory  Genetic algorithm  Autoregressive integrated moving average
1 Introduction
Nowadays, the recovery process of countries continues
after the economic shock caused by the COVID-19 epi-
demic. The prospect of economic normality and the
decreasing impact of the pandemic globally have been
fueling consumer demand, which has been driving price
hikes. While price increases have caused inﬂation in almost
every country today, the rise in food prices stands out as
one of the primary causes of inﬂation. Furthermore, the
world has currently been facing a food security crisis as
well as supply chain tensions. Prices for agricultural
commodities have already been signiﬁcantly impacted by
global climate change, and price swings will unavoidably
be inﬂuenced by factors such localized ﬂoods and droughts
[1]. On the other hand, this inﬂationary climate has been
made worse by the huge rises in the price of electricity and
fertilizer. The cost of farming rises, which raises the price
of agricultural commodities. This is because agricultural
machinery, vehicles, and buildings use more energy during
the agricultural production process. In addition to upsetting
food supply systems, COVID-19 is reducing food reserves
and increasing food demand. As a result, the cost of food
and agricultural commodities is increasing and reaching
new highs. The Russia–Ukraine war additionally com-
pound the threat to the global food supply chain by
& Murat Sari
muratsari@itu.edu.tr
1
Department of Mathematical Engineering, Faculty of Science
and Letters, Istanbul Technical University, 34469 Istanbul,
Turkey
2
Department of Mathematics and Science Education, Faculty
of Education, Adiyaman University, Adiyaman, Turkey
3
Department of Computer Technologies, Besni Vocational
School, Adiyaman University, Adiyaman, Turkey
4
Economics Department, Faculty of Management, Istanbul
Technical University, 34367 Istanbul, Turkey
123
Neural Computing and Applications (2024) 36:11439–11459
https://doi.org/10.1007/s00521-024-09679-x
(0123456789().,-volV)(0123456789().,-volV)

---

## Page 2
disrupting production, planting, harvesting, and shipping,
in addition to climate disasters, pandemics, and rising
production costs [2, 3]. This supply shock has an imme-
diate effect on agricultural commodity prices, sending
them to all-time highs. Food import and export restrictions
also raise the overall price of food and its volatility [4]. As
a result, between April 2020 and March 2022, food prices
increased by 84 percent, which was the highest increase
since 2008 [5]. Agricultural commodity price spikes that
are excessively over forecasted levels are referred to as
crises, and they lead to signiﬁcant economic and societal
issues. The strategies of political leaders may be in doubt if
the price of a highly desired agricultural product increases
dramatically, as happened when onion prices in India
affected election outcomes [6] or when food prices in
Algeria drove people onto the streets in 2011 [7]. When the
price crises of various agricultural items, which ﬁrst
appeared in 1966, are analyzed, it is discovered that they
have evolved in response to changing economic and
political circumstances, such as the shift from agriculture
to urban regions [8]. Furthermore, it has been determined
that the incidence of localized crises has a limited world-
wide inﬂuence. Production and trade disruptions caused
worldwide agricultural commodity price crises in the 1970s
[9]. Concerns about the volatility of agricultural com-
modity prices are now linked to the concept of food
security. Factors such as the availability of agricultural
products, economic and physical access to these products,
and the consumption of agricultural products generate price
changes and major issues in their supply [10]. With the
recent addition of the Ukraine-Russia war, the difﬁculties
experienced in physical access to many agricultural items
as a result of global conﬂicts have had a substantial impact
on agricultural commodity prices. Agricultural commodity
prices are directly related to many factors such as weather
conditions [11], climate changes [12], supply and demand
factors [13] and international crises [14]. These factors play
an important role in determining agricultural commodity
prices. Many sectors such as investors, food companies and
consumers wish to predict agricultural commodity prices.
Therefore, it is believed that forecasting agricultural com-
modity prices will help those operating in this sector to
make strategic planning and will play an important role in
issues such as food security and economic stability. Fore-
casting is difﬁcult due to the combination of many vari-
ables affecting agricultural commodity prices, many of
which are based on uncontrollable natural factors. As a
result, forecasting agricultural commodity prices emerges
as a process characterized by inherent uncertainties, and
achieving precision in forecasts proves to be a considerable
challenge. Despite these challenges, applying accurate
prediction models without considering the causal relation-
ship between variables can help those operating in the
sector make more informed decisions and be prepared for
possible risks. As a result, it is a fact that forecasting the
behavior and trends of agricultural commodity prices
would enable the establishment of appropriate policies to
address potential local or global problems that may arise.
Many ways have been proposed in the literature to carry
out this prediction [15, 16]. Many artiﬁcial intelligence
models have lately been applied to anticipate the behavior
and trends of agricultural commodity prices. With the
application of these models, studies aimed at estimating
agricultural commodity prices by considering variables
such as product quality levels [17], previous prices [18],
agricultural illnesses [19], seasonal factors [20] and climate
change [21] come to the fore. Although many different
models have yielded successful results, policymakers are
concerned that the expected contributions may remain at
relatively low levels due to the short-term nature of these
predictions. In this study, three different models have been
proposed with the help of artiﬁcial intelligence techniques
to predict the price change behavior of eleven different
agricultural items, including crops like wheat, corn, and
soybeans, which have increased in price in recent years.
Sugar, rice, oat, cotton, coffee, cocoa, soybean oil, and
lumber came to the fore in this context in the grain corridor
constructed in Turkey under the UN coordination amid the
current global supply crisis. The ﬁrst of the three models is
the autoregressive integrated moving
average (Auto-
ARIMA) [22], which is a standard method for estimating
agricultural commodity prices. One of the remaining two
proposed models is the long short-term memory with
genetic algorithm (GA-LSTM) model, which is created by
merging genetic algorithm (GA) and long short-term
memory (LSTM) [23]. In predicting long-term variations
and trends in agricultural product commodity prices, the
third proposed model, a hybrid of the genetic algorithm and
the extreme learning machine (GA-ELM), is seen to out-
perform both the Auto-ARIMA and GA-LSTM models.
Some important mathematical abbreviations used in this
paper are listed in Table 1.
Several recent researches have focused on the con-
struction and optimization of various machine learning
models to forecast economic behaviors/processes in several
food categories, including agricultural commodity pricing.
These studies lead to the notion that anticipating agricul-
tural commodity futures prices and behavior will reduce
the uncertainty and risks associated with the existing crop
of agricultural markets [24]. In the ﬁrst step, machine
learning models were used to approximate the price of
agricultural commodities so that insurance algorithms
could identify pricing and trend behaviors with accuracy.
The static or non-stationary complicated behavior of input
data can be captured by machine learning models [25–27].
A non-stationary characteristic of agricultural commodity
11440
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 3
futures prices is that they change signiﬁcantly over time as
a result of several issues that we currently face or may
encounter in the worldwide community. The ARIMA
approach, like most methods, is more effective at modeling
linear processes than nonlinear phenomena. Despite this
limitation, the ARIMA may be expected to produce accu-
rate forecasts when some agricultural products are less
affected by the numerous challenges faced in the global-
izing world, thus when reducing the factors that may affect
the modeling results. The merits and shortcomings of the
ARIMA have been discussed in many studies and from
time to time comparatively discussed in many studies
presented in the literature. Although it is seen that the
ARIMA approach has been successfully applied in ﬁelds
that appeal to a wide range of ﬁelds, it is seen that it
performs effectively and successfully when it takes the
stage in estimating some agricultural commodity prices,
sometimes in effective combinations, and sometimes either
on its own or comparatively [28–36]. Due to the nature of
the data, ARIMA-based methods were seen to be relatively
slow in providing the desired contribution in capturing
long-term trends and short-term ﬂuctuations in several
ﬁelds of research in the following years [35]. However, it
should not be overlooked that many of the recent artiﬁcial
neural network models have their roots in more conven-
tional techniques like the Auto-ARIMA [36]. With the
advancement of computer and engineering technologies
over time, current approaches such as LSTM, also known
as soft computing methods, have recently come to the fore
[23, 37]. The LSTM introduced by Hochreiter and Sch-
midhuber [38] has the advantage of processing long-term
and non-stationary data and is widely employed in
numerous disciplines of science such as ﬁnance [39],
meteorological forecasts [40], energy markets [41] and
transportation [42]. The GA-LSTM, which is introduced
here for the long-term determination of agricultural com-
modity prices, is motivated by the goal of predicting
ﬁnancial data and outperforms the Auto-ARIMA in pre-
dicting commodity prices of some agricultural items.
The positive justiﬁcations, which are much more
prominent in the historical development above, have
revealed the necessity of including these two methods
comparatively in the important methodological stages of
this study. Like any algorithm, both conventional algo-
rithms like the Auto-ARIMA and contemporary algorithms
like the LSTM offer advantages and disadvantages. The
drawback of the Auto-ARIMA is that it produces inaccu-
rate long-term forecasts. Both the Auto-ARIMA and
LSTM algorithms need a lot of training time.
The literature tells us that the ELM was introduced by
Huang et al. [43, 44] to minimize these disadvantages and
to combine some advantages such as regression, classiﬁ-
cation, clustering, feature learning and sparse approach.
One of the most important features of the ELM is that it
adds a randomness feature to the ELM due to the random
assignment of input weights and biases, which improves its
universality and efﬁciency performance over other stan-
dard models [45, 46]. Due to their advantages, the major
goal of this study is to develop a new and effective model
combining the GA and ELM for the prediction of agri-
cultural commodity prices. The proposed methodology
improves the ability to accurately predict agricultural
commodity prices of eleven different products, including
agricultural products that cause food inﬂation increases that
affect many countries in the world, such as the USA and
European countries, which we have encountered recently.
In this study, the prediction capabilities of ELM are
increased by automatically adjusting features such as the
number of hidden nodes, layer weights, and number of lags
by the GA. Thus, the superiority of the GA-ELM approach
in predicting the prices of several agricultural commodities
has been tested and compared with the popular and very
effective Auto-ARIMA and GA-LSTM models. Further-
more, it has been found that the GA-ELM takes less time
than the Auto-ARIMA and GA-LSTM models.
Table 1 A list of some key
mathematical abbreviations
used in this paper
Abbreviations
Descriptions
GA
Genetic algorithm
ELM
Extreme Learning Machine
LSTM
Long short-term memory
Auto-ARIMA
Autoregressive integrated moving average
GA-ELM
Extreme learning machine with the genetic algorithm
GA-LSTM
Long short-term memory with the genetic algorithm
RNN
Recurrent neural network
CBOT
Chicago Board of Trade
RMSE
Root-mean-square error
MAPE
Mean absolute percentage error
MAE
Mean absolute error
Neural Computing and Applications (2024) 36:11439–11459
11441
123

---

## Page 4
This study utilizes advantages of data-driven models
[47–49] by using nearly two decades of price data for
eleven different agricultural commodities as input, without
analyzing
the
cause-effect
relationships
of
variables
affecting agricultural commodity prices. The ability of
these models to predict agricultural commodity prices over
sixty-day intervals is the main focus. While several models
have achieved successful results, policymakers are con-
cerned that the expected contributions may be limited
because these forecasts are for a limited number of com-
modities and are short-term in nature. This study comprises
eleven major agricultural commodities that have increased
in price in recent years, such as wheat, corn, and soybeans.
The proposed model outperforms many studies in the lit-
erature in terms of accuracy and spotting trends of sixty-
day forecasts more effectively, making it a formidable rival
for real-time agricultural commodity price forecasting
applications. It is thought that the study will make impor-
tant practical contributions to stakeholders and policy-
makers in the agricultural sector due to its capacity to
reveal trends in both the number of products and sixty-day
forecasts.
2 Material and methods
The dataset of the current models consists of two main
parts as seen in Fig. 1. The ﬁrst part has employed 80% of
the daily data from the start date of eleven distinct agri-
cultural commodities goods to 11.03.2022 as training data
and 20% as testing data. In the second part, the models
have been trained with daily data from the start date of
eleven agricultural commodities to 11.03.2022. Based on
this information, the prices of all agricultural products are
forecasted for sixty days after 11.03.2022. The data after
this date have been considered as out of sample and used in
this study for the purpose of controlling the predictions.
Sustainable, smart, and precision agriculture policies are
clearly
crucial
for
countries
today.
Therefore,
it
is
undoubtedly simpler to understand the signiﬁcance of such
forecasts for wheat, corn, sugar, soybean, rice, oat, cotton,
coffee, cocoa, soybean oil, and lumber products, in the long
term, both qualitatively and quantitatively, in the current
time period, where prices vary widely, and inﬂation is a
major factor in determining agricultural policies.
This section summarizes some background information
needed to understand the GA-ELM, GA-LSTM hybrid
methods and Auto-ARIMA approach used in this study.
2.1 Extreme learning machines (ELM)
The ELM suggested by Huang et al. [50] is a single hidden
layer feed-forward neural network with a fast-learning
speed and a generalization feature [44, 45, 51]. This
enables the ELM to function effectively on data other than
training data. More clearly, the ELM that incorporates
nonlinear activation functions is successful in simulating
nonlinear issues resulting from numerous external and
environmental causes. The biases and weights of the hid-
den layer nodes are chosen at random in this method,
which reduces the amount of time required for backprop-
agation and hyper-tuning. The weights of the output layer
can be calculated analytically using the Moore–Penrose
inverse [52]. Figure 2 depicts the organizational structure
of the ELM model.
The following equation represents the output function of
the ELM with L hidden nodes
Fig. 1 Schematic diagram of the paper
11442
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 5
fL x
ð Þ ¼
X
L
i¼1
bihi x
ð Þ ¼
X
L
i¼1
bih xj  wi þ bi


;
j ¼ 1; :::; N:
ð1Þ
Here, N is the length of the training data vector. The
weight of the i-th hidden layer is wi and the bias is bi. Here,
xj, h and bi represent the element of the input vector j, the
activation function and the weight value i between the
hidden layer and the output layer, respectively.
Equation (1) can be re-expressed as
T ¼ Hb;
ð2Þ
where
H ¼
ðx1  w1 þ b1Þ
. . .
ðx1  wL þ bLÞ
..
.
..
.
..
.
ðxN  w1 þ b1Þ
. . .
ðxN  wL þ bLÞ
2
64
3
75;
ð3Þ
b ¼
bT
1
...
bT
L
2
64
3
75;
ð4Þ
T ¼
TT
1
...
TT
N
2
64
3
75:
ð5Þ
The matrices H; Tand eb represent the hidden layer
output matrix, the training data vector and the least-squares
solution of the linear system Hb ¼ T, respectively: The
matrices Hy and T stand for the Moore–Penrose general-
ized inverse of H and the training data vector, respectively.
Then,
~b ¼ HyT:
ð6Þ
To make predictions with testing data or out of sample
data (O), it can be written as:
FðOÞ ¼ ebHðOÞ:
ð7Þ
When it comes to time series forecasting, the ELM
algorithm can be an effective tool [53]. Statistical time
series forecasting models (ARIMA, for example) are
algorithms designed for stationary time series. These
algorithms frequently fail to detect seasonality in time data.
Because they contain activation functions, ANN models
have universal approximation capabilities. They can over-
come the difﬁculties of capturing environmental and
external impacts, i.e. nonlinear circumstances, in this
manner. Aside from this beneﬁt, ELMs have extraordi-
narily quick learning rates, good generalization perfor-
mance, and require little human involvement [46]. The
ELM algorithm combines the beneﬁts of traditional back
propagation neural network algorithms with the elimina-
tion of some of the disadvantages of ANN, such as over-
ﬁtting and slow learning speed.
The ELM method may perform less accurately than
ideal due to stochasticity. The amount of lag, type of
activation function, number of hidden nodes, and other
hyperparameters must be properly conﬁgured in order to
prevent this issue. Meta-heuristic optimization algorithms
like GAs and Bayesian Optimization can be used for this
tuning.
2.1.1 Genetic algorithm-based extreme learning machine
Because the weights and bias of the input layer are created
at random in the ELM, the system may exhibit unsteady
behavior. Because the weights and biases of the ELM input
layer are randomly generated, there may be too many
Fig. 2 The structure of the
ELM algorithm
Neural Computing and Applications (2024) 36:11439–11459
11443
123

---

## Page 6
nodes in the hidden layer, causing overﬁtting during the
training process. The GA can choose to optimize the
weights and bias of the input layer of the ELM, thus
improving the stability of the model and the prediction
accuracy.
The GA offered by Holland as a solution to the opti-
mization problems of complicated nonlinear systems [54]
seeks the best solution in an adaptive manner. It may
automatically collect information about the search area.
The citation above contains more information about the
procedure.
In this study, the GA is used to optimize the number of
input lags, the type of activation function, and the number
of hidden nodes parameters, in addition to the input
weights and biases in the ELM algorithm. The GA-ELM
technique for commodity price forecasting is depicted in
Fig. 3. The data preparation and selection of hyperparam-
eters to be optimized in the methodological development of
the GA-ELM are shown in Table 2 and Fig. 3. The
implementation
of
optimization
and
iterative
model
parameter generation are shown in Fig. 3 together with the
random generation of learning parameters. The literature
[55–59] contains structural information on the hyperpa-
rameters utilized in this study, including the lag size,
number
of
hidden
nodes,
input
weights/biases,
and
activation function of the ELM. It should be noted that the
selection strategy used in this study was roulette and the
GA was constructed using two-point crossover and Gaus-
sian mutation as suggested by Immanuel and Chakraborty
[60].
2.2 Long short-term memory (LSTM)
The LSTM is an artiﬁcial recurrent neural network (RNN)
used in deep learning [61]. The LSTM was presented by
Hochreiter and Schmidhuber to access constant error car-
ouse units and problem of gradient disappearance [38]. The
LSTM is a deep learning model that has recently been
widely used in time series forecasting and is speciﬁcally
designed to solve problems such as gradient bursting that
arise when working with long sequence data
[62]. The
Fig. 3 The GA-ELM architecture
Table 2 Selection of hyperparameters to be optimized
Variable
Type
Lower bound
Upper bound
Number of input lags
Integer
1
200
Number of hidden nodes
Integer
1
500
Input weights
Double
- 5
5
Input biases
Double
- 5
5
Type of activation function
Integer
1
4
11444
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 7
main concept of LSTM is based on cell state and gate
structures. It can be seen that these structures allow the
model to learn long-term dependencies more effectively
and produce more consistent results [63]. In the ﬁrst ver-
sion of the LSTM block, the cells include input and output
gates. The LSTM has feedback connections as opposed to
conventional feed-forward neural networks. The fact that it
can analyze data arrays in addition to instant data is a
signiﬁcant advantage. When dealing with estimate of
nonlinear and time series problems, the LSTM model with
memory capabilities can provide signiﬁcant advantages
[64]. To remember prior information, an LSTM memory
cell structure is added, and three gate structures are intro-
duced to manage the transfer of historical knowledge: input
gate, output gate, and forget gate. The cell stores values in
variable-length time periods, and these three gates control
and regulate the ﬂow of information entering and leaving
the cell. The structure of the LSTM algorithm at time step
t is depicted in Fig. 4.
Assuming the network input is x1; x2; :::; xt and the
hidden-layer state is h1; h2; :::; ht, the computations of each
unit and gate at time t are presented as follows.
The LSTM cell has three gates that play an important
role in controlling the ﬂow of information through the
neural network. Three gates on the LSTM cell are crucial
in regulating how information moves through the neural
network. Input, output, and forget gates are the names of
these gates. The input gate it
ð Þ, which controls how much
input data is current state stored in the unit state, is the ﬁrst
of them and
it ¼ r wi: ht1; xt
½
 þ bi
ð
Þ;
ð8Þ
where ht1; wi and bi represent the output values of the
previous cell, the weight matrices of the input gate and the
bias of the input gate, respectively.
The second of these is the forget gate
ft
ð Þ and is cal-
culated as follows:
ft ¼ r wf: ht1; xt
½
 þ bf
ð
Þ;
ð9Þ
where wf and bf indicate the weight matrices of the forget
gate and the bias of the forget gate, respectively.
The most important step in creating an LSTM network is
to determine how much information is retained in the
current cell state of ct, from the state of ct1 from the
previous moment. In other words, it is the determination of
the information that is not necessary and will be removed
from the cell:
ct ¼ ft  ct1 þ it  ~ct;
ð10Þ
~ct ¼ tanh wc: ht1; xt
½
 þ bc
ð
Þ;
ð11Þ
where ct and ~ct stand for the current input and current
moment unit state, respectively.
The third gate ot
ð Þ is the output gate and is calculated as:
ot ¼ r wo: ht1; xt
½
 þ bo
ð
Þ;
ð12Þ
ht ¼ ot  tanh ct
ð Þ;
ð13Þ
where wo and bo indicate the weight matrices of the output
gate and the bias of the output gate, respectively.
The notations r :ð Þ and tanh :ð Þ indicate transfer func-
tions;: and  represent the inner product and element-wise
multiplication, respectively.
2.2.1 Genetic algorithm-based LSTM (GA-LSTM)
In order to increase the performance of deep neural networks,
hyperparameters are usually determined by trial-and-error
method. This method is time consuming as well as data
dependent. In this study, the GA has been used to optimize
the LSTM architectural parameters for each of the eleven
products. Optimal lag size and number of units parameters of
LSTM architecture are optimized by genetic algorithm. The
architecture used in the study is shown in Fig. 5.
2.3 Autoregressive integrated moving average
(ARIMA)
ARIMA models are stable which implies stationarity.
ARIMA model can be applied to non-stationary series after
differencing them up to stationary. One of the most
important features of this model is that it is based on a
linear function between past observations and random
errors. The ARIMA model is a combination of AR and MA
models. p and q describe the order of AR and MA models,
respectively, while d is the degree of difference [65]. Then,
dt ¼
X
p
i¼1
/idti
X
q
j¼0
ujetj:
ð14Þ
Fig. 4 The structure of the LSTM algorithm
Neural Computing and Applications (2024) 36:11439–11459
11445
123

---

## Page 8
Here, dt denotes the actual value of the time series at
time t. dti and etj represent different observation values
and
error
terms,
respectively.
The
coefﬁcients
/i i ¼ 1; 2; :::; p
ð
Þ and uj j ¼ 1; 2; . . .; q
ð
Þ are the parameters
of the AR and MA models, respectively. Details of the
ARIMA modeling procedure, for instance, can be found in
the work of Box and Jenkins [65]. Also note, by the way,
that the Auto ARIMA method returns the best ARIMA
pattern based on the AIC, AICc, or BIC value. The method
performs a search on the possible model within the pro-
vided ordering constraints and ﬁnds the ARIMA model
with the best parameters.
3 Experiments and analysis
3.1 Data processing and analysis
This paper has analyzed eleven different data groupings,
including daily data for wheat, corn, sugar, soybeans, rice,
oat, cotton, coffee, cocoa, soybean oil, and lumber agri-
cultural items in Table 3. The Chicago Board of Trade
(CBOT) provides data on wheat, corn, soybean, rice, oat,
and soybean oil agricultural products, while the Immigra-
tion and Customs Enforcement (ICE-US) provides data on
sugar, cotton, coffee, and cocoa agricultural products for
daily sales prices. All agricultural commodity unit prices
are expressed in US dollars. Furthermore, there are gaps in
the data utilized on some days owing to holidays or tech-
nical issues, which are not included in this study.
The use of data from reputable sources such as CBOT
and ICE-US enhances the reliability of this paper. In terms
of data pre-processing, the dataset has carefully been
curated and cleaned to ensure accuracy and consistency.
However, it is important to recognize that some limitations
and biases may remain despite rigorous pre-processing
efforts. Notably, the study addresses potential gaps in data
due to holidays or technical issues on certain days, and
such cases are excluded from the analysis to maintain data
integrity. However, it is imperative to recognize that
inherent biases or limitations in the original data sources
may affect the results of the study. This article provides a
comprehensive understanding of the quality and limitations
of the dataset, as well as transparency about the source of
the data, pre-processing steps, and potential biases.
Based on literature reviews [66, 67], prediction periods
used in machine learning models are generally categorized
as short, medium and long term. However, the limitation
that the meanings of these terms may vary from context to
context should be noted. In this study, we classify sixty-day
forecast periods as long-term, and forecasts shorter than
two weeks as short-term. A medium-term time period was
Fig. 5 The architecture of the GA-LSTM algorithm
11446
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 9
not taken into account in this study. However, it is
imperative to recognize that time constraints may affect the
results of the study.
3.2 Performance metrics
Our forecasting performance relies on several key metrics:
root-mean-square error (RMSE), mean absolute percentage
error (MAPE), and mean absolute error (MAE) [68]. The
RMSE is calculated as the square root of the average
squared differences between the actual values (yi) and the
forecasted values ð^yiÞ, summed over all observations (N).
Speciﬁcally, the RMSE, MAPE and MAE are given by:
RMSE ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
N
X
N
i¼1
yi  ^yi
ð
Þ2
v
u
u
t
;
ð15Þ
where yi, ^yi and N stand for the actual data, the forecasted
data, and the overall number of days that the forecasting
was done for. Also
MAPE ¼ 100
N
X
N
i¼1
yi  ^yi
yi

;
ð16Þ
MAE ¼ 1
N
X
N
i¼1
yi  ^yi
j
j:
ð17Þ
4 Application of the models
The data are separated into two categories: training data
and test data. 80% of the data according to the start date has
been employed in the training time of the GA-LSTM and
GA-ELM models proposed with the Auto-ARIMA. The
remaining 20% has been used for testing in all models.
Future data for eleven different agricultural product prices
have been predicted using three different models as shown
in Figure 6.
Forecast performance is measured by using root-mean-
square error (RMSE), mean absolute error (MAE) and
mean absolute percentage error (MAPE) as seen in
Table 4.
4.1 Approaches for forecasting agricultural
commodity prices over the next sixty days
This section determines the data in agricultural commodity
prices before to 12.03.2022, which is the second key theme
of the study, and presents forecasts for the following sixty
days. The prediction results, which can be regarded very
long, have been determined on a daily basis for all items
from the start date of 13.03.2022 to the ﬁnish date of
05.06.2022. Because weekend data are not available
between these periods, it has been examined over a sixty
days period. Furthermore, projections are not produced on
the days when real data are unavailable.
In Fig. 7, it can be observed that the GA-ELM model for
wheat, which is one of the products most affected by the
food crisis caused by global conﬂicts, generates very suc-
cessful behavioral predictions when compared to the GA-
LSTM and Auto-ARIMA models. Although known to be
quite successful overall, the Auto-ARIMA lagged undeni-
ably behind the GA-ELM. It has been found that GA-
LSTM could not consistently approach real data, both in
terms of quality and quantity, depending on the structure of
the data.
In comparison to the GA-LSTM in Fig. 8, it can be
shown that the GA-ELM and Auto-ARIMA models for
corn, which is included in cereal products, both generate
very accurate quantitative predictions. The GA-ELM
model is shown to come to the fore both qualitatively and
quantitatively according to the Auto-ARIMA, especially
when looking at the long-term forecasts made after May
22. It is worth noting that the GA-ELM successfully
Table 3 Descriptive statistics
on agricultural commodity
products
Time period
Number of record
Mean
St. Dev
Min
Max
Wheat
01.01.2000–29.07.2022
5899
523.70
189.98
233.5
1425.25
Corn
03.01.2000–29.07.2022
5732
393.69
160.71
174.75
831.25
Sugar
03.01.2000–29.07.2022
5730
14.26
5.81
4.65
35.31
Soybean
03.01.2000–29.07.2022
5846
967.26
334.47
418
1769
Rice
19.01.2007–29.07.2022
3904
13.19
2.39
9.12
24.46
Oat
15.07.2008–29.07.2022
3481
318.91
114.31
158.50
807
Cotton
14.10.2009–29.07.2022
3288
83.09
24.92
48.85
213.84
Coffee
03.01.2000–29.07.2022
5721
126.81
50.20
41.50
304.90
Cocoa
03.01.2000–29.07.2022
5677
2208.14
670.01
674
3774
Soybean oil
03.01.2000–29.07.2022
5745
35.04
14.09
14.38
90.60
Lumber
03.01.2000–29.07.2022
5686
351.92
193.65
138.10
1686
Neural Computing and Applications (2024) 36:11439–11459
11447
123

---

## Page 10
captures the behavioral tendencies of real data, even when
global crises directly boost agricultural commodity prices.
Furthermore, the GA-LSTM model is slower than the other
two models in capturing long-term forecasts.
Considering the changes in sugar prices in the last
twenty-two years, the change in prices is low since it has a
homogeneous
structure
compared
to
many
other
agricultural commodities. Therefore, depending on the
nature of the data, all three models appear to be successful
in the ﬁrst ﬁve-day forecasts (short-term) in Fig. 9. Despite
the fact that prices in real data exhibit relatively very little
ﬂuctuations beyond ﬁve days, the GA-ELM model is more
sensitive than the other two models in capturing these
trends.
Fig. 6 Forecasting results of the GA-ELM, GA-LSTM and Auto-ARIMA models
Table 4 Forecasting results for
agricultural commodity futures
GA-ELM
GA-LSTM
Auto-ARIMA
RMSE
MAE
MAPE
RMSE
MAE
MAPE
RMSE
MAE
MAPE
Wheat
10.27
7.82
1.39
43.52
25.45
4.42
10.91
8.36
1.48
Corn
8.36
5.15
1.14
32.38
20.75
4.58
8.96
5.49
1.22
Sugar
0.25
0.19
1.37
0.90
0.69
5.5
0.26
0.20
1.46
Soybean
14.18
9.99
0.93
47.04
35.12
3.24
16.47
11.31
1.05
Rice
0.30
0.15
1.09
1.07
0.60
1.10
0.31
0.15
1.14
Oat
11.82
7.32
1.72
38.28
27.04
6.63
11.91
7.41
1.81
Cotton
1.53
1.05
1.37
5.17
3.98
4.90
1.55
1.15
1.43
Coffee
2.94
2.11
1.64
9.89
7.12
5.64
3.10
2.23
1.73
Cocoa
50.60
36.78
1.52
161.59
122.22
5.10
54.07
39.46
1.63
Soybean oil
0.71
0.46
1.11
2.96
1.86
4.37
0.75
0.49
1.19
Lumber
28.17
16.67
2.62
112.62
73.10
11.10
30.09
16.46
2.79
11448
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 11
Fig. 7 Forecasts of the models for wheat for the next 60 days
Fig. 8 Forecasts of the models for corn for the next 60 days
Fig. 9 Forecasts of the models for sugar for the next 60 days
Neural Computing and Applications (2024) 36:11439–11459
11449
123

---

## Page 12
When we look at the price ﬂuctuations of soybean prices
over the previous twenty-two years, we see that the price
range is fairly wide since it has a heterogeneous structure
compared to other agricultural commodities. The GA-ELM
model is quantitatively successful in the long-term fore-
casts shown in Fig. 10. Furthermore, when the 5846-day
data are examined, it is apparent that GA-ELM caught this
upward trend in the long run on 09.06.2022, when soybean
prices were at their highest. Although the Auto-ARIMA
has shown an upward trend in long-term forecasts, it has
not shown the predicted performance quantitatively. Con-
trary to the Auto-ARIMA, the GA-LSTM was expected to
have a downward trend in soybean prices in the long run.
Since rice has a uniform structure in comparison to other
agricultural commodities, price ranges are rather minimal
when looking at price movements over the past twenty-two
years. The long-term forecasts in Fig. 11 demonstrate the
effectiveness of the GA-ELM model. In addition, it is seen
that the GA-ELM and Auto-ARIMA models are faster than
the GA-LSTM in catching up and down trends in prices.
Russia is one of the top producers of oat in the world. In
light of the recent disputes between Russia and Ukraine,
the price of oat appears to have peaked on April 12, 2022,
when looking back over the previous ﬁfteen years. It is
crucial that the GA-ELM model being applied captures the
upward trend shown in Fig. 12 and takes values that are
very close to the largest value it has ever taken on this date.
The abrupt uptrends and downtrends that happen in
unforeseen situations and in capturing them, like with other
agricultural commodities, make the GA-ELM stand out
visibly. Although it is a little slow, GA-LSTM has been
seen to play a signiﬁcant role in capturing the changing
trends of oat prices. Although the Auto-ARIMA is not as
good as expected at capturing the ups and downs in real
data, depending on the structure of the data, it has been
noted that it can quantitatively capture values close to real
data in long-term forecasts.
The GA-ELM model outperforms the rival models in
terms of quality and quantity during the short term (ﬁrst
ﬁfteen days), despite the anticipated values for cotton being
less accurate than those for other agricultural products.
According to Fig. 13, the GA-ELM model performs better
than the other two models in capturing real values, and it is
seen that it can slow down even though it maintains its
superiority compared to other models even in projections
longer than ﬁfteen days.
In long-term forecasts covering sixty days, the GA-ELM
model outperforms the other two models in coffee prices,
which are less affected by global disputes than other
agricultural products. Figure 14 illustrates how the GA-
LSTM model has been slow to detect long-term up and
down trends after May 8 even if it has been qualitatively
good in forecasting up to that point. Additionally, after
May 8th, the Auto-ARIMA has been seen to outperform
the GA-LSTM model in terms of quality and quantity in
long-term projections.
The GA-ELM model is extremely successful in captur-
ing both the short-term and long-term ranges of variation
for the cocoa product in Fig. 15. Despite the fact that the
GA-LSTM model can be seen to be getting close to the
trends of real data in some time intervals, it still behind the
GA-ELM overall. As can be seen in Fig. 15, the Auto-
ARIMA has not been successful in predicting cocoa prices.
The fact that the range of changes in cocoa prices over time
is so wide is one of the most signiﬁcant elements gener-
ating this situation.
Soybean oil is one of the products most affected by the
recent global problems in the world. As can be seen in
Fig. 16, soybean oil reached its peak value on April 28,
2022. The sixty-day projections (long-term) covering this
Fig. 10 Forecasts of the models for soybean for the next 60 days
11450
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 13
Fig. 11 Forecasts of the models for rice for the next 60 days
Fig. 12 Forecasts of the models for oat for the next 60 days
Fig. 13 Forecasts of the models for cotton for the next 60 days
Neural Computing and Applications (2024) 36:11439–11459
11451
123

---

## Page 14
Fig. 14 Forecasts of the models for coffee for the next 60 days
Fig. 15 Forecasts of the models for cocoa for the next 60 days
Fig. 16 Forecasts of the models for soybean oil for the next 60 days
11452
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 15
date show that GA-LSTM has particularly well captured
this increasing trend. But when looking at a longer time
period, it is clear that the GA-ELM model excels at iden-
tifying these trends. The Auto-ARIMA is seen to be suc-
cessful in forecasting till May 22 while being very slow to
identify rapid changes.
The GA-ELM model for lumber prices is quite suc-
cessful in both the long and short terms, as can be observed
in Fig. 17. Additionally, even though the GA-LSTM is
effective in the near term, it is noticed that it was slow to
reach the expected performance between April 21 and May
11. The GA-LSTM seems to show a downward trend in
performance after May 11. Compared to both competing
models, the Auto-ARIMA has been slow to achieve
expected performance, both qualitatively and numerically,
as shown in Fig. 17.
As demonstrated in Table 5, the GA-ELM model per-
forms better and has a higher sensitivity when compared to
the Auto-ARIMA and GA-LSTM models for all agricul-
tural commodity items when the long-term forecast results
covering sixty days are analyzed. The Auto-ARIMA
appears to be the second efﬁcient model after the GA-ELM
for wheat, corn, rice, cotton, coffee and soybean oil prod-
ucts. Apart from these products, the GA-LSTM model
stands out as the second model after GA-ELM in the
agricultural products (sugar, soybeans, oat, cocoa and
lumber). Although the Auto-ARIMA and GA-LSTM
models are very slow in reaching the accurate results
achieved by the GA-ELM due to some ranges and data
types, the qualitative and quantitative predictions produced
by these two models should not be perceived as useless.
Figure 18 presents a violin plot of the RMSE values of
the three methods for sixty-day forecasts of sugar, rice,
Fig. 17 Forecasts of the models for lumber for the next 60 days
Table 5 The GA-ELM, GA-
LSTM and ARIMA test results
for 60 days forecasts of
agricultural commodity prices
GA-ELM
GA-LSTM
Auto-ARIMA
RMSE
MAE
MAPE
RMSE
MAE
MAPE
RMSE
MAE
MAPE
Wheat
65.94
53.43
5.13
191.84
152.12
13.41
74.30
53.24
4.74
Corn
21.98
17.73
2.26
69.82
61.99
7.90
29.10
22.60
2.95
Sugar
0.68
0.56
2.95
0.80
0.66
3.43
1.32
1.09
5.67
Soybean
37.43
29.91
1.73
117.34
97.42
5.68
120.70
102.60
6.12
Rice
0.46
0.38
2.33
1.80
1.72
10.51
0.88
0.68
4.05
Oat
33.86
27.39
3.98
37.44
28.94
4.08
114.86
103.190
14.36
Cotton
5.56
4.23
2.79
18.92
17.07
12.47
17.53
16.20
11.46
Coffee
8.52
6.93
2.98
13.86
12.57
5.71
10.35
7.71
3.53
Cocoa
70.07
53.65
2.16
91.58
77.46
3.17
295.93
267.67
10.54
Soybean oil
5.49
4.72
5.98
10.38
8.43
10.34
5.64
5.02
6.48
Lumber
138.54
111.09
19.40
208.30
183.87
19.40
592.30
533.78
66.54
Neural Computing and Applications (2024) 36:11439–11459
11453
123

---

## Page 16
cotton, coffee, and soybean oil prices RMSE\20
ð
Þ: It is
clear that the GA-ELM model provides the best distribu-
tion and ﬁt of the prediction. RMSE values are presented
comparatively for the three models. Upon close examina-
tion of Fig. 18, the Auto-ARIMA emerges as the second
most effective model for capturing changes over the sixty
days period following the GA-ELM.
Figure 19 presents a violin plot of the RMSE values of
the three methods for sixty-day forecasts of wheat, corn,
soybeans, oat, cocoa, and lumber prices RMSE  20
ð
Þ: It is
clear that the GA-ELM model provides the best distribu-
tion and ﬁt of the predicted RMSE values compared to the
competing models (GA-LSTM and Auto-ARIMA). Upon
closer inspection of Fig. 19, the GA-LSTM emerges as the
second most effective model in capturing changes over the
sixty-day period, following the Auto-ARIMA.
Determining acceptable limits of RMSE can be difﬁcult
when working on a variable and dynamic data set such as
agricultural commodity prices. In this study, the constraint
criterion for the RMSE value is deﬁned as 20 in order to
examine the effectiveness of three different methods in
more detail and to categorize agricultural commodity
products. As seen in Figs. 17 and 18, it can be seen that the
GA-ELM model is the model that most effectively captures
changes
in
two
different
agricultural
commodity
categories.
The RMSE values of the GA-ELM model for wheat,
corn, soybeans, oat, cocoa and lumber compared to other
agricultural products can be considered a successful level,
considering that the forecast period is sixty days. Also note
that when working on a variable and dynamic data set such
as agricultural commodity prices, it can be difﬁcult to
determine acceptable limits of RMSE. High RMSE values
may be caused by factors such as the complexity of the
model, the characteristics of the data set or the optimization
algorithms used [69]. At the same time, the fact that the
RMSE values of the GA-ELM model for eleven different
agricultural products are lower than the GA-LSTM and
ARIMA models shows that the GA-ELM model has a
superior performance. It should be noted that in addition to
the quantitative prediction of agricultural commodity pri-
ces, the proposed models also successfully capture quali-
tative ﬂuctuations, as shown in Figs. 7, 8, 9, 10, 11, 12, 13,
14, 15, 16 and 17.
5 Results and discussion
Although this study focuses on agricultural product price
forecasts, it should not be ignored that these results may be
slightly below the desired level of success from time to
time, seasonal and political considerations, as well as
model-based elements, can be effective in this. At least
intuitively, it can be stated that the ﬁndings achieved by
eliminating the inﬂuences of periodic and political factors,
as well as the effects of long-term data, can be carried to a
considerably higher degree of success.
This research has presented deep learning techniques to
produce predictive models of the long-term trends of
agricultural commodity prices, including those of products
Fig. 18 Violin plot for the three
proposed methods
RMSE\20
ð
Þ:
Fig. 19 Violin plot for the three
proposed methods
RMSE  20
ð
Þ:
11454
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 17
involved in the current food crisis. Despite the fact that a
variety of machine learning algorithms have been utilized
in the literature to estimate agricultural commodity prices,
to the best of the authors’ knowledge, sixty-day forecasts
have not yet been taken into account. One of the most
important reasons for this situation is that the success levels
of many models used decrease as the prediction time
increases. As a result, most agricultural commodity pricing
in the literature [70–72] have used daily or weekly fore-
casts. Although using many distinct models in short-term
predictions have yielded more successful results, the short-
term character of these predictions appears to be a factor
limiting conﬁdence in determining long-term strategy.
Recently, there has been a surge in the number of studies
that take into account a wide range of variables, including
product quality levels [17], past pricing [18], agricultural
illnesses [19], seasonal factors [20] and climate change
[21]. These studies all have the goal of making predictions
based on the causal relationship between the variables. The
ARIMA and machine learning-based models have been
preferred, regardless of whether there is causality between
the dependent and independent variables for the eleven
distinct agricultural products examined in this paper. This
paper has successfully forecasted commodity prices for
eleven distinct agricultural items over a two-month period
using three models: ARIMA, GA-LSTM, and GA-ELM.
Traditional computational algorithms like ARIMA and soft
computational techniques like LSTM have advantages and
limitations like any other algorithm. It is known that
ARIMA has the disadvantage of deviating from reality in
long-term projections. During the training stages, both the
ARIMA and LSTM algorithms need a signiﬁcant amount
of time. The ELM was developed by Huang et al. [43, 44]
to reduce these drawbacks and address issues with
regression, classiﬁcation, clustering, feature learning, and
sparse approximation. One of the most important features
of ELM is that it adds a randomness feature to the ELM
due to the random assignment of input weights and biases,
which improves its universality and efﬁciency performance
over other traditional models [45, 46]. A new ELM model
with genetic optimization (GA) method is proposed in this
paper for estimating agricultural commodities prices. The
proposed methodology improves their ability to forecast
agricultural commodity prices for eleven different prod-
ucts, including agricultural products that have recently
caused food shortages and price increases in many coun-
tries around the world, including the USA and European
countries. Prediction capabilities of the ELM are enhanced
by automatically adjusting features such as the number of
hidden nodes, layer weights, number of delays by the
genetic algorithm. The GA-ELM approach has outper-
formed the ARIMA and GA-LSTM models, which are
frequently faced in many disciplines to estimate the pricing
of various products. When RMSE, MAE, and MAPE val-
ues are computed, the ELM combined with genetic algo-
rithms appears to be quite successful in both short-term and
long-term price forecasts for all eleven distinct agricultural
products compared to two separate models (ARIMA and
GA-LSTM). In
addition,
the GA-ELM,
one
of
the
approaches proposed here, seems to be quite useful because
it requires less time in terms of speed factor compared to
the ARIMA and GA-LSTM. It has been shown that the
proposed model, unlike many studies in the literature,
performs better both in closeness to reality and in deter-
mining the trends of predictions covering sixty days,
making it a strong candidate for real-time agricultural
commodity price forecasting applications.
5.1 Advantages of the GA-ELM model
over the rival models:
•
The performance of GA-ELM has a distinct advantage
over other popular models, as reported in the literature
[73]. It tends to generalize better, especially on complex
and large data sets. In various tests, the accuracy rates
of GA-ELM have been found to be statistically signif-
icantly
higher
than
other
models
(in
terms
of
performance).
•
The GA-ELM has been successfully applied in ﬁelds
such as ﬁnancial forecasting [47], materials engineering
[48],
and
industrial
system
[74].
This
versatility
demonstrates ability of the GA-ELM to adapt to various
problems and its capacity to improve its performance
(in terms of application ﬂexibility).
•
Compared to the competing models, ability of the GA-
ELM to optimize the weights of the model using a
genetic algorithm stands out [68]. Traditional ELM
starts with random weights and optimizes these weights
during the training phase. The GA-ELM, on the other
hand, can ﬁnd the best weight combinations more
efﬁciently by using the genetic algorithm that increases
its generalization ability (in terms of uniqueness and
validity).
•
The GA-ELM may require less training data compared
to some other deep learning models [73]. This espe-
cially supports the preference of the GA-ELM in
limited data situations (in terms of usability).
•
The GA-ELM model has adaptive features managed by
genetic algorithm to ensure long-term sustainability
[75, 76]. In this way, it can successfully adapt to
changing conditions by performing effectively accord-
ing to the ELM model in terms of maintenance,
updating and adaptation to data sources (Long-Term
Sustainability).
Neural Computing and Applications (2024) 36:11439–11459
11455
123

---

## Page 18
In this paper, we use the RMSE measure to evaluate the
robustness of the model. Agricultural commodity prices are
divided into randomly selected training and validation sets
in a ratio of 8:2 and various models are built and checked
using different training sets. Figure 6 shows the distribu-
tion of GA-ELM, GA-LSTM and Auto-ARIMA models for
eleven different agricultural commodities. Table 5 shows
that the GA-ELM model is more stable compared to the
GA-LSTM and Auto-ARIMA models considering the
RMSE distribution. In multiple experiments conducted for
the basic infrastructure of the study, the lowest RMSE and
ﬂuctuations have been observed in the GA-ELM model,
which is superior in terms of accuracy and robustness. It is
concluded that the predictive ability of the GA-ELM model
is consistently more accurate.
In this paper, when applied to eleven different agricul-
tural commodity prices using traditional algorithms such as
ARIMA and soft calculation algorithms such as the GA-
LSTM, the ARIMA stands out in some products and GA-
LSTM in others, after the GA-ELM. Although both
methods seem successful in short time periods, it is seen
that they are below the expected success in long-term
forecasts. A new model, according to the literature, is
necessary to produce more accurate predictions for both the
number of agricultural products and a long time period
such as sixty days. In order to predict such a wide range of
commodities over such a long period of time, a model
called GA-ELM has been suggested in the main emphasis
of this study by effectively combining the ELM and GA.
When compared to the ARIMA and GA-LSTM, this model
is quite successful at predicting all of the commodity val-
ues of eleven distinct agricultural products over both short
and long time periods. At the same time, it has been shown
that the difﬁculties associated with estimating agricultural
commodity prices can be overcome to some extent by the
ARIMA and GA-LSTM. In addition, the GA-ELM model
is also very successful in terms of training time compared
to the other two models. It has been demonstrated that the
suggested model is in the lead both qualitatively and
quantitatively, even when prices ﬂuctuate signiﬁcantly
owing to global difﬁculties in several months of 2022. The
fact that it contains daily pricing for agricultural com-
modity products from January 2000 to July 2022 demon-
strates that this analysis is more thorough and up-to-date
than earlier studies.
The proposed GA-ELM model provides higher accuracy
than the ARIMA and GA-LSTM models in determining
long-term price trends of agricultural products. This pri-
marily allows policymakers to predict future price ﬂuctu-
ations and develop appropriate strategies. Secondly, by
providing separate performance analyses for different
agricultural products, the study provides policymakers with
information on which products are more predictable. This
information enables the development of risk management
strategies. The model also predicts the future prices of
agricultural products and ﬁnally, it is thought that it can
contribute to managerial implications in inventory planning
and supply chain. This allows policymakers to use this
information effectively to maintain the balance of supply
and demand. This information, which can provide guidance
in dealing with price uncertainty and enable them to adapt
to market conditions more effectively, can offer a signiﬁ-
cant advantage to managerial implications.
6 Conclusions and recommendation
This paper has built efﬁcient artiﬁcial intelligence methods
for effectively forecasting commodities prices considering
worldwide
events.
The
commodity prices
of
eleven
important agricultural goods that have recently caused
crises around the world have been forecasted using three
independent, well-structured models. In addition to the
other two proposed models, this research has created a
novel model for commodity price forecasting by combin-
ing the extreme learning machine method and the genetic
algorithm. The GA-ELM model has been observed to
perform better at forecasting commodity prices than the
GA-LSTM and ARIMA models, thus enabling successful
estimation of the prices of these products, which may
naturally also be strategic in the future. Despite the unex-
pected changes in commodity prices caused by worldwide
conﬂicts in 2022, the GA-ELM model proposed in this
study accurately predicts both the qualitative and quanti-
tative behavior of such a large number of commodities over
such a long time period. As a natural consequence of the
war, it has been observed in test results and predicted
results that the prices of the goods produced by the warring
parties or their neighbors change the most quickly; as a
result, they are among the most signiﬁcant factors in
shaping international relations in the short and long term.
Furthermore, the richness of the number of agricultural
items treated here in comparison to the literature, as well as
the successful capture of commodity price trends over a
reasonably long period of time, can be viewed as a major
outcome of our work. The prediction that it will improve
the effective management, guidance and restructuring of
agricultural policies by meeting food needs that adapt to
the dynamic structure of countries can be considered as an
important ﬁnding of this study. However, future research
should consider the impact of various objective functions
in the optimization process with a genetic algorithm. This
is because the objective function is the key element that
drives the optimization process and therefore has a sig-
niﬁcant impact on model accuracy. It should also be noted
that a fair amount of data is needed for the process if both
11456
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 19
the model parameters and the selection of input variables
are estimated over different time periods. Although the
results produced by all three models are very promising, it
may be useful to discuss possible modiﬁcations to the
models to obtain more realistic results in the future.
Funding Open access funding provided by the Scientiﬁc and Tech-
nological Research Council of Tu¨rkiye (TU¨ BI˙TAK).
Data availability The datasets generated during and/or analyzed
during the current study are available from the corresponding author
on reasonable request.
Declarations
Conflict of interest The authors declare that they have no known
competing financial interests or personal relationships that could have
appeared to influence the work reported in this paper.
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
1. Lewis K, Witham C (2012) Agricultural commodities and climate
change. Clim Policy 12(sup01):S53–S61
2. Adekoya OB, Oliyide JA, Yaya OS, Al-Faryan MAS (2022) Does
oil connect differently with prominent assets during war? Anal-
ysis of intra-day data during the Russia–Ukraine saga. Resour
Policy 77:102728
3. McKinsey (2022) The rising risk of a global food crisis. https://
www.mckinsey.com/industries/agriculture/our-insights/the-rising-
risk-of-a-global-food-crisis
4. World Bank (2022) Food security update. https://thedocs.world
bank.org/en/doc/40ebbf38f5a6b68bfc11e5273e1405d4-0090012
022/original/Food-Security-Update-LXVII-July-29-2022.pdf
5. World Bank, Commodity Markets Outlook (2022). Impact of the
war in Ukraine on commodity markets. https://openknowledge.
worldbank.org/server/api/core/bitstreams/da0196b9-6f9c-5d28-
b77c-31a936d5098f/content
6. https://www.bloomberg.com/news/articles/2013-07-25/for-indias-
inﬂation-crisis-see-onion-prices
7. https://www.bbc.com/news/world-africa-12134307
8. Abel
W
(1966)
Agrarkrisen
und
Agrarkonjunktur
(Eine
Geschichte der Land- und Ernaˆhrungswis senschaft Mitteleuropas
seit dem hohen Mittelalter). Parey Verlag, Berlin
9. Valdes A (ed) (1981) Food security for developing countries.
Westview Press, Boulder
10. Tadasse G, Algieri B, Kalkuhl M, Braun JV (2016) Drivers and
triggers of international food price spikes and volatility. In:
Kalkuhl M, von Braun J, Torero M (eds) Food price volatility and
its implications for food security and policy. Springer, Cham,
p. 59–82
11. Zhang D, Dai X, Wang Q, Lau CKM (2023) Impacts of weather
conditions on the US commodity markets systemic interdepen-
dence across multi-timescales. Energy Econ 123:106732
12. Fujimori S, Wu W, Doelman J, Frank S, Hristov J, Kyle P,
Takahashi K (2022) Land-based climate change mitigation
measures can affect agricultural markets and food security. Nat
Food 3(2):110–121
13. Staugaitis AJ, Vaznonis B (2022) Financial speculation impact on
agricultural and other commodity return volatility: implications
for sustainable development and food security. Agriculture
12(11):1892
14. Arndt C, Diao X, Dorosh P, Pauw K, Thurlow J (2023) The
Ukraine war and rising commodity prices: implications for
developing countries. Glob Food Secur 36:100680
15. Haykin S (1999) Neural networks: a comprehensive foundation.
Prentice Hall, Upper Saddle River, New Jersey
16. Sari M, Yalcin IE, Taner M, Cosgun T, Ozyigit II (2023) Fore-
casting contamination in an ecosystem based on a network model.
Environ Monit Assess 195(5):536
17. Liu J, Dong C, Liu S, Rahman S, Sriboonchitta S (2020) Sources
of total-factor productivity and efﬁciency changes in China’s
agriculture. Agriculture 10(7):279
18. Xiong T, Li C, Bao Y (2018) Seasonal forecasting of agricultural
commodity price using a hybrid STL and ELM method: evidence
from
the
vegetable
market
in
China.
Neurocomputing
275:2831–2844
19. Mayuri A, Rashmi V, Das B, Mandal A, Neelakandan S (2023)
Artiﬁcial neural network (ANN) with Chan–Vese (CV) algo-
rithm-based plant disease detection and classiﬁcation. In: 2023
international conference on applied intelligence and sustainable
computing (ICAISC). IEEE, p. 1–6
20. Paul RK, Garai S (2021) Performance comparison of wavelets-
based machine learning technique for forecasting agricultural
commodity prices. Soft Comput 25(20):12857–12873
21. Cho W, Na MH, Park Y, Kim DH, Cho Y (2020) Prediction of
weights during growth stages of onion using agricultural data
analysis method. Appl Sci 10(6):2094
22. Wang M, Pan J, Li X, Li M, Liu Z, Zhao Q, Wang Y (2022)
ARIMA and ARIMA-ERNN models for prediction of pertussis
incidence in mainland China from 2004 to 2021. BMC Public
Health 22(1):1–11
23. Sari M, Ahmad AA (2019) Anemia modelling using the multiple
regression analysis. Int J Anal Appl 17(5):838–849
24. Wang D, Yue C, Wei S, Lv J (2017) Performance analysis of four
decomposition-ensemble models for one-day-ahead agricultural
commodity futures price forecasting. Algorithms 10(3):108
25. Zulauf C, Rettig N, Roberts M (2015) Do futures forecast the
future? Farmdoc Daily (4): 147
26. Glorot X, Bordes A, Bengio Y (2011) Deep sparse rectiﬁer neural
networks. In: Proceedings of the fourteenth international con-
ference on artiﬁcial intelligence and statistics. JMLR workshop
and conference proceedings, p. 315–323
27. Goodfellow I, Pouget-Abadie J, Mirza M, Xu B, Warde-Farley D,
Ozair S, Bengio Y (2014) Generative adversarial nets. Adv
Neural Inf Process Syst. https://doi.org/10.48550/arXiv.1406.
2661
Neural Computing and Applications (2024) 36:11439–11459
11457
123

---

## Page 20
28. Kohzadi N, Boyd MS, Kermanshahi B, Kaastra I (1996) A
comparison of artiﬁcial neural network and time series models for
forecasting commodity prices. Neurocomputing 10(2):169–181
29. Shahwan T, Odening M (2007) Forecasting agricultural com-
modity prices using hybrid neural networks. In: Chen S-H, Wang
P, Kuo T-W (eds) Computational intelligence in economics and
ﬁnance. Springer, Berlin, Heidelberg, p. 63–74
30. Li GQ, Xu SW, Li ZM (2010) Short-term price forecasting for
agro-products using artiﬁcial neural networks. Agric Agric Sci
Procedia 1:278–287
31. Burark SS, Sharma H (2012) Price forecasting of coriander:
methodological issues. Agric Econ Res Rev 25:530
32. Ticlavilca AM, Feuz DM, McKee M (2010) Forecasting agri-
cultural commodity prices using multivariate Bayesian machine
learning regression
33. Ly R, Traore F, Dia K (2021) Forecasting commodity prices
using long-short-term memory neural networks, vol 2000. Intl
Food Policy Res Inst. Washington DC, USA
34. Menhaj M, Kavoosi-Kalashami M (2022) Developing a hybrid
forecasting system for agricultural commodity prices (case study:
Thailand rice free on board price). Cieˆncia Rural 52:e20201128
35. Atsalakis GS, Valavanis KP (2010) Surveying stock market
forecasting techniques-part I: conventional methods. J Comput
Optim Econ Financ 2(1):45–92
36. Huang Y, Gao Y, Gan Y, Ye M (2021) A new ﬁnancial data
forecasting model using genetic algorithm and long short-term
memory network. Neurocomputing 425:207–218
37. Keller WJ, Keuning JW (2016). Protective asset allocation
(PAA): a simple momentum-based alternative for term deposits.
Available at SSRN 2759734
38. Hochreiter S, Schmidhuber J (1997) Long short-term memory.
Neural Comput 9(8):1735–1780
39. Lin SL, Huang HW (2020) Improving deep learning for fore-
casting accuracy in ﬁnancial data. Discrete Dyn Nat Soc. https://
doi.org/10.1155/2020/5803407
40. Dai Y, Lu Z, Zhang H, Zhan T (2018) Research on visibility
forecast based on LSTM neural network. In: International con-
ference on signal and information processing, networking and
computers. Springer, Singapore, p. 551–558
41. Zhang L, Wang J, Wang B (2020) Energy market prediction with
novel long short-term memory network: case study of energy
futures index volatility. Energy 211:118634
42. He J (2021) Application of deep learning model under improved
emd in railway transportation investment beneﬁts and national
economic attribute analysis. J Supercomput 77(8):8194–8208
43. Huang GB, Zhu QY, Siew CK (2004) Extreme learning machine:
a new learning scheme of feedforward neural networks. In: 2004
IEEE international joint conference on neural networks (IEEE
Cat. No. 04CH37541), vol 2. IEEE, p. 985–990
44. Huang GB, Zhu QY, Siew CK (2006) Extreme learning machine:
theory and applications. Neurocomputing 70(1–3):489–501
45. Huang GB, Zhou H, Ding X, Zhang R (2011) Extreme learning
machine for regression and multiclass classiﬁcation. IEEE Trans
Syst Man Cybern Part B (Cybern) 42(2):513–529
46. Chaudhuri KD, Alkan B (2022) A hybrid extreme learning
machine model with harris hawks optimisation algorithm: an
optimised model for product demand forecasting applications.
Appl Intell 52:11489–11505
47. Weng F, Chen Y, Wang Z, Hou M, Luo J, Tian Z (2020) Gold
price forecasting research based on an improved online extreme
learning machine algorithm. J Ambient Intell Humaniz Comput
11:4101–4111
48. Suo Y, Zhang C, Liu L, Qu H, Yang P, Xie G (2023) Proportion
optimization and strength prediction of CGS backﬁll materials
based on GA-ELM mode. Energy Sour Part A Recovery Util
Environ Eff 45(2):5173–5189
49. Berbic´ J, Ocvirk E, Gilja G (2022) Optimization of supervised
learning models for modeling of mean monthly ﬂows. Neural
Comput Appl 34(20):17877–17904
50. Huang GB, Chen YQ, Babri HA (2000) Classiﬁcation ability of
single hidden layer feedforward neural networks. IEEE Trans
Neural Netw 11(3):799–801
51. Huang GB, Chen L, Siew CK (2006) Universal approximation
using incremental constructive feedforward networks with ran-
dom hidden nodes. IEEE Trans Neural Netw 17(4):879–892
52. Courrieu P (2008) Fast computation of Moore–Penrose inverse
matrices. arXiv preprint arXiv:0804.4809
53. Miche Y, Sorjamaa A, Bas P, Simula O, Jutten C, Lendasse A
(2009) OP-ELM: optimally pruned extreme learning machine.
IEEE Trans Neural Netw 21(1):158–162
54. Holland JH (1970) Robust algorithms for adaptation set in a
general formal framework. In: 1970 IEEE symposium on adap-
tive processes (9th) decision and control. IEEE, p. 175–175
55. Ribeiro GH, Neto PSDM, Cavalcanti GD, Tsang R. (2011). Lag
selection for time series forecasting using particle swarm opti-
mization. In: The 2011 international joint conference on neural
networks. IEEE, p. 2437–2444
56. Eshtay M, Faris H, Obeid N (2019) Metaheuristic-based extreme
learning machines: a review of design formulations and appli-
cations. Int J Mach Learn Cybern 10(6):1543–1561
57. Han F, Yao HF, Ling QH (2013) An improved evolutionary
extreme learning machine based on particle swarm optimization.
Neurocomputing 116:87–93
58. Silva DN, Paciﬁco LD, Ludermir TB (2011) An evolutionary
extreme learning machine based on group search optimization.
In: 2011 IEEE congress of evolutionary computation (CEC).
IEEE, p. 574–580
59. Li B, Li Y, Rong X (2013) The extreme learning machine
learning algorithm with tunable activation function. Neural
Comput Appl 22(3):531–539
60. Immanuel SD, Chakraborty UK (2019). Genetic algorithm: an
approach on optimization. In: 2019 international conference on
communication
and
electronics
systems
(ICCES).
IEEE,
p. 701–708
61. Qian L, Zheng Y, Li L, Ma Y, Zhou C, Zhang D (2022) A new
method of inland water ship trajectory prediction based on long
short-term memory network optimized by genetic algorithm.
Appl Sci 12(8):4073
62. An W, Wang L, Zhang D (2023) Comprehensive commodity
price forecasting framework using text mining methods. J Fore-
cast 42:1865–1888
63. Mo J, Gao R, Liu J, Du L, Yuen KF (2022) Annual dilated
convolutional LSTM network for time charter rate forecasting.
Appl Soft Comput 126:109259
64. Zhao Z, Chen W, Wu X, Chen PC, Liu J (2017) LSTM network:
a deep learning approach for short-term trafﬁc forecast. IET Intel
Transp Syst 11(2):68–75
65. Box GE, Jenkins GM, Reinsel GC, Ljung GM (2015) Time series
analysis: forecasting and control. John Wiley & Sons
66. Mohammed NA, Al-Bazi A (2022) An adaptive backpropagation
algorithm for long-term electricity load forecasting. Neural
Comput Appl 34(1):477–491
11458
Neural Computing and Applications (2024) 36:11439–11459
123

---

## Page 21
67. Ertugrul OF, Tekin H, Tekin R (2021) A novel regression method
in forecasting short-term grid electricity load in buildings that
were connected to the smart grid. Electr Eng 103:717–728
68. Jamil M, Zeeshan M (2019) A comparative analysis of ANN and
chaotic approach-based wind speed prediction in India. Neural
Comput Appl 31:6807–6819
69. Sajja PS (2021) Examples and applications on hybrid computa-
tional
intelligence
systems.
Illus
Comput
Intell
Ex
Appl
931:191–225
70. Jiang F, He J, Zeng Z (2019) Pigeon-inspired optimization and
extreme learning machine via wavelet packet analysis for pre-
dicting bulk commodity futures prices. Sci China Inf Sci
62(7):1–19
71. Luo J, Klein T, Ji Q, Hou C (2022) Forecasting realized volatility
of agricultural commodity futures with inﬁnite Hidden Markov
HAR models. Int J Forecast 38(1):51–73
72. Ouyang H, Wei X, Wu Q (2019) Agricultural commodity futures
prices prediction via long-and short-term time series network.
J Appl Econ 22(1):468–483
73. Li B, Liao M, Yuan J, Zhang J (2023) Green consumption
behavior prediction based on fan-shaped search mechanism fruit
ﬂy algorithm optimized neural network. J Retail Consum Serv
75:103471
74. Guan X, Li W, Huang Q, Huang J (2022) Intelligent color
matching model for wood dyeing using genetic algorithm and
extreme learning machine. J Intell Fuzzy Syst 42(6):4907–4917
75. Ge L, Liu J, Wang B, Zhou Y, Yan J, Wang M (2021) Improved
adaptive gray wolf genetic algorithm for photovoltaic intelligent
edge
terminal
optimal
conﬁguration.
Comput
Electr
Eng
95:107394
76. Wang Q, Sun C, Li Y, Liu Y (2022) Numerical simulation of
erosion characteristics and residual life prediction of defective
pipelines
based
on
Extreme
Learning
Machine.
Energies
15(10):3750
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
Neural Computing and Applications (2024) 36:11439–11459
11459
123

---
