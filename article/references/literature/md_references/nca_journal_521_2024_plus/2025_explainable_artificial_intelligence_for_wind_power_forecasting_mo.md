# Explainable artificial intelligence for wind power forecasting model based on long short-term memory

**Year**: 2025 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-025-11230-5

---

## Page 1
ORIGINAL ARTICLE
Explainable artificial intelligence for wind power
forecasting model based on long short-term memory
Mona Ahmed Yassen1,2 • El-Sayed M. El-Kenawy3,4,5,6 • Mohamed Gamal Abdel-Fattah2 •
Islam Ismail2 • Hossam El-Deen Salah Mostafa2
Received: 10 January 2025 / Accepted: 26 March 2025 / Published online: 14 May 2025
 The Author(s) 2025
Abstract
Expanding the world’s economy leads to higher requirements for energy storage. Traditional energy resources
decline at the same time that environmental contamination levels increase in the world. Wind power is the most
potential energy resource supported by its status as a signiﬁcant renewable energy system. Wind power gener-
ation has become a popular and exciting method among nations worldwide for generating renewable energy.
High wind power generation unpredictability results in unavoidable errors throughout the wind power prediction
process, creating substantial difﬁculties in the optimal management of power systems. Wind power prediction
errors remain unavoidable, but appropriate wind power uncertainty models help power system operators reduce
their adverse impact on operational decision-making performance. In this paper, developed an appropriate
machine learning model that efﬁciently forecasted wind power data through time series analysis. The long Short-
Term Memory (LSTM), Gated Reference Unit (GRU), and Autoregressive Integrated Moving Average (ARIMA)
are the machine algorithms used in this investigation. This paper proposed an X-double LSTM, which integrates
explainable artiﬁcial intelligence (XAI) and long short-term memory (LSTM). The XAI-Shapley Additive
Explanations (SHAP) model is modiﬁed to pinpoint the crucial elements affecting the power generation fore-
casting model’s accuracy in cutting-edge solar systems. Nine metrics are used to assess the efﬁcacy of the
proposed X-double LSTM model: root mean square error, mean bias error, correlation coefﬁcient, relative root
mean square error, Nash–Sutcliffe efﬁciency, mean square error, mean absolute deviation, coefﬁcient of multiple
determination, and Willmott index of agreement. For MSE, RMSE, MAE, MBE, r, R2, RRMSE, NSE, and WI,
the suggested model improves by 0.000 11, 0.011, 0.008, 0.008, 0.99, 0.98, 2.5, 0.98, and 0.98, respectively.
Other machine learning methods, including the Transformer model, single-layer LSTM networks, Autoregressive
Moving Average (ARMA) models, Gated Recurrent Unit (GRU) networks, and Bidirectional (Bi-LSTM) net-
works, are compared to the performance of double LSTM. The twin LSTM model was demonstrated to perform
better. The simulations and experimental ﬁndings show that the suggested model can precisely estimate wind
power. Within the Google Collab environment, the suggested model uses TensorFlow and Keras.
Keywords Wind power  Forecasting  Renewable energy  Deep learning  Optimization
1 Introduction
According to data from the International Energy Agency, renewable energy usage standards have increased to
19.3%, while its power generation level is 24.5%. Renewable energy will remain vital to upcoming power
consumption patterns as data from the energy sector proves its importance in achieving fossil fuel elimination.
Neural Computing and Applications (2025) 37:14589–14611
https://doi.org/10.1007/s00521-025-11230-5
123
Neural Computing and Applications (2025) 37:14589–14611

---

## Page 2
The rise of sustainable power sources such as solar, wind, hydro, and geothermal energy further bolsters this shift,
offering a viable alternative to traditional energy systems. Renewable energy systems are suitable fossil fuel
alternatives because they function reliably and exist widely throughout the planet. The falling prices to generate
and distribute renewable energy enable various countries to adopt it as a sustainable power source that simul-
taneously protects the environment. The power grid faces obstacles when implementing renewable energy
systems mainly because wind energy can be periodic. Predicting wind speeds is vital in maximizing wind energy
production and maintaining steady power grid operations. Improvements in wind energy production speed
depend directly on ﬂow speed, so better wind speed forecasting algorithms will lead to signiﬁcant economic and
technical developments. Renewable energy development wins, farm layouts, and power transmission require-
ments heavily depend on applying sophisticated forecasting technologies. Developing methods to forecast wind
speed and power generation has consumed considerable research. The forecasting methods are divided into three
sections: turbine control in the short-term and monthly and yearly trend prediction in the long term, with
dispatching power functions in the mid-term. This research focuses on the third category, proposing a novel
forecasting technique for predicting daily mean wind speed over a year. The global wind power capacity has
grown substantially, reaching 906 GW as of 2022 (see Fig. 1), reﬂecting the increasing reliance on renewable
energy sources.
Despite these advancements, wind energy forecasting remains challenging due to wind’s stochastic nature.
Researchers have employed advanced methodologies, including Long Short-Term Memory (LSTM) networks
[1], which leverage historical data for precise predictions. Time series forecasting has proven crucial for
improving wind energy reliability as it helps decrease fossil fuel use and sustain energy development. The
combination of real-time statistical and climate forecasting models increases prediction accuracy according to [2].
However, forecasting remains an ongoing research challenge requiring continuous reﬁnement of methods to
improve reliability and stability. This study employs historical time series data analysis to examine wind energy
production and utilization [3]. Artiﬁcial intelligence (AI), particularly ensemble learning methods, has signiﬁ-
cantly improved over traditional approaches. Hybrid AI models enhance forecasting accuracy, as demonstrated in
Kao et al. [4], where the XGBoost algorithm and a causal sliding window method optimized predictions.
However, model interpretability remains critical in machine learning-based forecasting, especially as complex AI
models are more challenging to interpret. The problem of AI decision transparency receives its solution through
Explainable Artiﬁcial Intelligence (XAI) according to [5]. Implementing XAI improves deep learning model
performance levels by adding necessary interpretability features that researchers and industry stakeholders need to
understand AI-produced predictions. This research integrates LSTM neural networks with XAI tools to improve
Fig. 1 Wind power capac-
ity over a year
123
Neural Computing and Applications (2025) 37:14589–14611
14590
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 3
energy forecasting efﬁciency. LSTM models effectively capture temporal dependencies in data but introduce high
complexity. By incorporating XAI, we aim to create a transparent framework that clariﬁes how LSTM processes
and generates predictions. Enhancing model interpretability builds user conﬁdence and trust in AI-driven fore-
casting systems. The main contributions of this work include:
•
Utilizing LSTM to explore the search space, preventing suboptimal solutions effectively.
•
Employing SHAP, an XAI technique, to explain model performance and improve interpretability.
•
Identifying key environmental factors inﬂuencing wind energy forecasting results.
•
Developing an X-double LSTM model that enhances prediction accuracy across diverse environmental
scenarios, mitigating wind power unpredictability and improving grid integration.
•
The proposed method requires statistical testing to show how it outperforms current methods.
The rest of this research paper follows this structure: Section 2 reviews existing literature through a summary
of previous work. Section 3 describes the framework theory and necessary research methods. Section 4 presents
the experimental procedures through which LSTM worked with XAI for energy forecasting assessment. Section 5
shows and interprets the ﬁndings through a series of results and analyses. The paper ends by offering a summary
of essential discoveries and suggesting new paths for renewable energy forecasting research in Section 6.
2 Related works
This section presents papers that compare wind power prediction models and highlight various methods and
developments in the subﬁeld. The studies presented and discussed here in detail explore the various approaches
adopted to enhance the efﬁciency of the conventional techniques employed in wind power prediction. Tian et al
[6]. proposed an original WPF system composed of two stages of attention mechanisms, allowing the model to
address relevant data points and improve the prediction quality effectively. This establishment in deep learning
algorithms forms the basis of the feature and performance inspection. Likewise, New et al. [7] proposed a similar
data-driven WPF model that explored high-level deep learning techniques. Their model fared even better than
existing models to show a substantial enhancement in performance indicators like Mean Absolute Error (MAE),
Mean Absolute Percentage Error (MAPE), and Mean Squared Error(MSE) to vouch for the capability of their
model in precise wind power forecasting. The problem of working with a small amount of historical data in new
wind farms was discussed in Dong et al. [8]. Suggested transfer learning in corrupted power curve estimation for
wind farms using a small data set was proposed. This method improves the efﬁciency of few-shot learning by a
large margin and can help avoid the problem of a small number of training cases in wind power forecasting. At
the same time, He et al [9]. introduced the incorporation of the LSTM models with the Convolutional Neural
Networks (CNNs) to enhance short-term WPF performance. When used for a wind farm in northwest China, their
work showed LSTM and CNN superior to other sophisticated machine learning algorithms. The scholars Al-
Kasabi et al. [10] used variables like wind direction and velocity to improve wind energy forecasting using
machine learning. Their model was tested in several sites, particularly France and Turkey, and was found to give
reasonable estimates of wind energy production. Shahid et al [11]. used a set of neural networks on genetic
programming and an auxiliary predictor. According to a double t-test of their results, the authors pointed out that
their model yielded a better prognosis than other methods utilized before. Ban et al [12]. introduced a spa-
tiotemporal graph convolutional network for accurate short-term wind power forecasts. Their model outper-
formed ﬁve conventional forecasting methods based on MAE and RMSE across different forecasting horizons.
Residual correction and ensemble reinforcement learning models were developed with the help of Yin and Hui
[13], alongside an outlier correction method. Another promising approach, based on Q-learning, is presented as
an effective means of forecasting wind power. Peiris et al. [14] used ANN in accurately predicting the wind
energy production of the Pawan Danawi wind farm in Sri Lanka at an 85% validation level. On the other hand,
Delgado and Fahim [15] employed LSTM networks since, as claimed by the model’s authors, LSTM networks
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14591

---

## Page 4
are excellent in capturing nonlinear dynamics to improve the prediction of the performance of wind turbines.
Lo´pez and Arboleya [16], and Sun and Jin [17] also stressed that PCC was widely used for input selection in
LSTM and DNNs. Their studies focused on the features that should be utilized to increase the model performance
indicators. Xiong et al. [18], advancing the data selection explicitly focused on reconstruction, employed an
approach whereby input variables are ranked. A few recent literatures proposed integrated models, where Yu
et al. [19] used wavelet decomposition on wind speed data. They divided the data into subseries, which improved
the effectiveness of the forecast models, including the Recurrent Neural Networks (RNN), Long Short-Term
Memories (LSTM) and Gated Temporal Units (GTU). Subsequently, Shang et al. [20] went a step further and
utilized a computational technique known as Complementary Ensemble Empirical Mode Decomposition, which
lends enhanced characterization of historical wind speed data and then used a model selection technique known as
the Self Organizing Map Clustering for efﬁcient categorization. However, Praveena and Dhanalakshmi [21] went
in a different direction, characterizing the days by similar wind conditions with the help of Fuzzy K-means
Clustering. They realized that this technique was proper precisely because it allowed them to look for changes in
the wind speed over a twenty-four-hour cycle, which gave a handy forecast. Clustering of climatology tem-
perature and humidity parameters of the region was the scope of Ghanbarzadeh et al. [22]. They wanted to design
an ANN model for predicting wind speeds. It also had higher levels of prediction accuracy than the other
forecasting models employed by the companies. Abdoos et al [23]. proposed an advanced wind power forecasting
model using Variational Mode Decomposition (VMD) and Extreme Learning Machine (ELM), integrating the
Monte Carlo method for probabilistic forecasts, further enhancing accuracy and reliability. Zhao et al [23].
developed a model combining the LightGBM algorithm and the neural prophet technique, optimizing parameter
tuning through grid search, which improved efﬁciency and reduced computation time. Finally, Mei and Ma’s
prediction model [24] combined CNN, an attention mechanism, and a bidirectional LSTM network to capture
linear and nonlinear relationships in wind power time series. In another research, F.Shahid et al. [25] used a
genetic algorithm application for LSTM window size and neuron number optimization to improve the accuracy of
wind power prediction compared to existing methods. National Renewable Energy Laboratory’s wind power
forecasting was enhanced by Azimi et al [26]. integrating the traditional K-means clustering approach with the
discrete wavelet transform and the multilayer perceptron neural network. Shi et al [27]. used variational mode
decomposition and LSTM to predict hourly wind power for a Chinese wind farm with an accurate day-ahead
forecast. A.Lahouar et al [28]. improved a wind power forecasting model based on random forest (RF) and
showed that it was more accurate by adding average wind speed and wind direction as the input features.
However, adding these features sometimes degrades the results signiﬁcantly. In another research, Velazquez et al
[29]. suggested the impact of wind speed, wind power density, and power output on the performance of ANN
models. Using wind direction as an input can reduce forecasting errors. In the present study, Su et al [30]. used
wind power prediction analysis to decompose the wind speed data into four low-frequency and four high-
frequency. Then, the four high-frequency components were extracted into 60 intrinsic mode functions (IMFs) by
ensemble empirical mode decomposition (EEMD). These components were then incorporated into individual
LSTM models with yaw error and rotor speed input. The power prediction results of the proposed approach were
signiﬁcantly improved in accuracy. Nevertheless, the role of the direct application of the wind power dataset for
prediction still needs to be examined. Zu et al. [31] employed the WPD method to disintegrate wind power times
series into three levels. The gained subseries were given to a gated recurrent unit (GRU), and the predictions were
reconstructed to get the results. Experimental analysis revealed that the proposed WPD-GRU-SELU model is
more accurate for prediction than existing RNN models. In another research, Mujeeb et al. [32] used Wavelet
Packet Transform (WPT) with Deep convolutional neural network (DCNN) to forecast the day-ahead hourly wind
power of ISO New England’s wind farm; nevertheless, the authors failed to forecast the subseries using different
independent models. Besides wind power prediction, other wavelet transform methods have recently been
employed in the wind power prediction domain. However, they identiﬁed the need for improved model inter-
pretability. Therefore, this paper has provided an exhaustive chronology of the wind power forecasting techniques
developed in chronological succession, advanced neural networks, hybrid wind power forecasting models, and
123
Neural Computing and Applications (2025) 37:14589–14611
14592
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 5
methods of the scarcity of data and predictive accuracy. Again, these works indicate that work is ongoing to
enhance the precision of wind power forecasts since such enhancements are critical in handling wind power
systems. Last, Table 1 revisits the considered investigations and identiﬁes their impact on developing forecasting
methodologies for wind power systems.
3 Materials and methods
These are the methodologies employed in the preprocessing and modeling stage from the research highlighted in
this study. The data was cleaned adequately before analyzing the collected data to ensure datasets were correctly
compiled for analysis. Regression analysis procedures, such as imputation and removal of outliers, were applied
to improve the data quality. The main objective focused on maintaining a comprehensive feature collection
alongside optimizing model operational speed. Our team used an amin-max scaler because this method provides
speciﬁc value ranges from 0 to 1 for data interpretation and comparison in wind power generation forecasting
tasks. After getting the data in shape, we laid out the outcomes with various prediction plots for selected cases.
Table 1 Summary of Wind Power Forecasting (WPF) Studies
Authors
Technique
Results
Limitations
Tian et al. [6]
Two-stage attention mecha- nism in deep
learning
Superior accuracy and perfor-
mance
Limited validation across dif-
ferent locations
New et al. [7]
Data-driven deep learning model
Reduced MAE, MAPE, and MSE
Performance may degrade with
imbalanced data
Dong et al. [8]
Transfer learning for data scarcity
Improved few-shot learning
accuracy
Highly dependent on avail- able
small datasets
He et al. [9]
LSTM and CNN combina- tion for short-
term WPF
Outperformedtraditional models
Sensitive to noisy data
Al-Kasabi et al. [10]
Ensemble models with wind direction and
speed
Effective
Turkey
in
France
and
Requires extensive meteoro-
logical data
Shahid et al. [11]
Neural networks with ge- netic
programming
Better than existing tech- niques
Limited generalization due to
dataset speciﬁcity
Ban et al. [12]
Spatiotemporal graph convo- lutional
network
Improved MAE and RMSE
High dependency on spatial data
availability
Yin & Hui [13]
Residual correction and rein- forcement
learning
Signiﬁcant improvement in
Q-learning-based forecast- ing
High computational cost
Peiris et al. [14]
ANN for wind energy predic- tion
85% accuracy in Sri Lanka
Results may not generalize well
Delgado & Fahim [15]
LSTM for turbine perfor- mance
Captured nonlinear depen-
dencies
Requires large datasets
Lo´pez & Arboleya [16]
PCC analysis for LSTM and DNN
Identiﬁed relevant input vari-
ables
PCC may not always be opti- mal
Yu et al. [19]
Wavelet method for wind data
Improved hybrid model per-
formance
Sensitive to sudden changes
Shang et al. [20]
Ensemble empirical mode decomposition
Categorized data efﬁciently
High computational cost
Praveena &
Dhanalakshmi [21]
Fuzzy K-means clustering
Improved daily pattern fore-
casting
Struggles with dynamic wind
patterns
Ghanbarzadeh et al. [22]
ANN using meteorological variables
High wind speed prediction
accuracy
Sensitive to climate varia- tions
Abdoos et al. [23]
VMD and ELM with Monte Carlo
Accurate probabilistic fore- casts
Computationally intensive
Zhao et al. [23]
LightGBMandNeural- Prophet combination
Improved interpretability
Parameter tuning is time-
consuming
Mei & Ma [24]
CNN, attention mechanism, and
bidirectional LSTM
Captured linear and nonlin- ear
relationships
Complexity time
use
hinders
real-
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14593

---

## Page 6
These visualizations demonstrate how well our modeling approach forecasts wind power generation, so they are
not merely for show. We will also give you a thorough assessment of the study performance, which will help you
understand how accurate and dependable our model is. Our fundamental objective is simple: we use several
sophisticated deep learning techniques, such as the Transformer model, single-layer LSTM networks, and double
layer
LSTM networks, Autoregressive Moving Average (ARMA) models, Gated Recurrent Unit (GRU) networks,
and Bidirectional (Bi-LSTM) networks, to forecast wind power generation. We’re not limiting ourselves. We’re
rigorously testing the performance of a diverse range of models, including the Transformer model, single-layer
LSTM networks, double layer LSTM networks, Autoregressive Moving Average (ARMA) models, Gated
Recurrent Unit (GRU) networks, and Bidirectional (Bi-LSTM) networks. This paper evaluates these analytical
methods to determine their predictive potential and ability to represent wind power generation intricacies. The
team pursues quantitative analysis and qualitative evaluation to study our research process thoroughly. Our
analysis begins with investigations of the dataset to understand the patterns alongside visualization studies. Data
collection proceeds through partitioning into training data and testing data to build reliable models during
development. Five distinct models go through training as part of this process to provide independent deep
learning methods. We apply the reserved data set to evaluate our trained models during testing. A deep learning
model’s performance evaluation determines the optimal solution. Figure 2 displays a complete diagram of the
proposed wind forecasting technique that covers the entire process, starting with data preparation and ending with
model assessment.
3.1 Dataset
We got our hands on a publicly available wind dataset from Kaggle, packed with essential information for
studying and analyzing the factors and features. This data was pulled from four major German energy companies:
50Hertz, Amprion, TenneT TSO, and TransnetBW. It shows non-normalized power generation ﬁgures recorded
every 15 minutes, giving us 96 daily data points. The dataset covers the period from August 23, 2019, to
September 22, 2020, and offers a thorough foundation for examining swings in wind energy output over a little
more than a year. Figure 3 shows the complex interrelationships among these critical factors and how each affects
Fig. 2 Block schematic of the suggested methodology
123
Neural Computing and Applications (2025) 37:14589–14611
14594
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 7
the total amount of wind energy produced. This visualization can help guide future energy policies and improve
comprehension of dynamics involved in wind energy production.
Research variables produce distinct relationships and patterns from the data, which helps us understand their
interdependent behavior. High numbers of interdependencies within wind energy forecasting prove why devel-
oping an accurate prediction model is essential. A credible model proving essential for forecasting becomes
essential because of the pressing need to improve our energy management approaches and policy and strategic
decision- making. Developing such a forecasting model will not only enhance our understanding of the given data
set and its forecast but also advance our analysis of the patterns of renewable energy production. From our
detailed study, these insights are unique and crucial for any stakeholders in wind energy to engage in sound
planning and action to maximize energy yield and incorporate wind energy into the overall power network.
Figure 8 showcases the elaborate relationships between the four German transmission system operators TenneT
TSO, 50Hertz, TransnetBW, and Amprion using heat mappings. Visual representation of operator correlation
values between 0 and 1 makes the heatmap reveal signiﬁcant data relations that keep operators relevant. Lighter
shades of red indicate weaker associations, while darker shades represent stronger correlations. For instance,
TenneT TSO and 50Hertz show a high degree of similarity with a correlation of 0.87, while 50Hertz and
TransnetBW have a moderate connection with a correlation of 0.61. Overall, the heatmap reveals signiﬁcant
relationships between the operators that could be harnessed for collaborative efforts to enhance energy man-
agement and grid stability (Figs. 4 and 5).
Fig. 3 Graphical representation of the histogram for every feature in the energy efﬁciency dataset
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14595

---

## Page 8
4 Deep learning (DL) models
4.1 Long short-term memory (LSTM)
To effectively manage and reduce the signiﬁcant correlations that often afﬂict nonlinear regression tasks, LSTM
models are sophisticated neural network designs. Sequential data regression applications, like time series analysis,
are incredibly remarkable because of this. Unlike traditional statistical methods that mainly focus on predicting
outcomes based on the immediate past of a stochastic process, LSTM models have the remarkable ability to
Fig. 4 Total daily wind power generation over time
Fig. 5 Heatmap graph for
dataset attributes related to
wind energy efﬁciency
123
Neural Computing and Applications (2025) 37:14589–14611
14596
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 9
remember and integrate information about events that occurred way back, even long before the query was made.
This distinctive feature enhances their ability to estimate the probability of future occurrences, making LSTM a
great powerhouse tool for predicting scenarios. Based on the work [33], this ability is efﬁcient for time series
regression forecasts as it allows the model to inﬂuence predictions by previously observed time points, signiﬁ-
cantly improving the quality of the results. One study reveals that original classical LSTM methods perform better
than other regression task approaches. This is particularly the case in ﬁnancial modeling, trafﬁc prognostication
and meteorology. This paper underscores the effectiveness of LSTMs, especially in regression problems with the
time series [34] data and speciﬁc implications of optimum strategies and design changes for its implementation.
In addition, what makes LSTM unique is the hidden layer in its structure. The LSTM network consists of a
memory cell (cell state), forget gate, input gate, and output gate [35]. The formula [36] for the LSTM component
is as follows:
at ¼ rðWa½qt1; zt þ baÞ
ð1Þ
st ¼ rðWs½qt1; zt þ bsÞ
ð2Þ
^Ct ¼ ReLUðWc½qt1; zt þ bcÞ
ð3Þ
Ct ¼ at  Ct1 þ it  ^Ct
ð4Þ
ot ¼ rðWo½qt1; zt þ boÞ
ð5Þ
qt ¼ ot  ReLUðCtÞ
ð6Þ
ReLU : fðzÞ ¼ maxð0; zÞ;
ð7Þ
where at is the forget gate, st is the input gate, Ct is the newly added value to the cell gate, Ct is the cell state, ot is
the output gate, and qt is the output value at time t. The activation functions used are r (sigmoid) and ReLU. Here,
Ws, Wc, and Wo represent the weight matrices for the respective gates. qt-1 is the output value at time t - 1, Ct-1
is the cell state at time t - 1, xt is the input value at time t, and ba, bs, bc, bo are the bias values for the respective
gates.
4.2 Bidirectional (Bi-LSTM)
Recent advancements in RNNs’ have enhanced the development of models capable of processing forward and
backward data. Predictability of more than 90 percent was obtained by tri-training the authors’ models of bi-
LSTMs and bidirectional Gated Recurrent Units (Bi-GRUs), respectively; these architectures are particularly
suitable for time series forecasting [37, 38]. They improve their capacity to sort data into categories and foretell
based on past and future data. Bidirectional Long and Short-Term Memory Networks (bi-LSTMs) are also
bidirectional gated recurring units (bi-GRUs) used in natural language processing since their inception in 1997.
Due to their ﬂexibility, they can efﬁciently perform tasks as simple as classiﬁcation or sorting of text. Here,
sentiment analysis is all about analyzing the sentiment projected to a text, while language translation is about
translating content from one language to another. The application efﬁciency of such models increases their
signiﬁcance and performance in managing real-life sequential data [39]. In bidirectional LSTM, the working of
the forward layer is the same as that of the standard LSTM, which traverses from time t = 1 to T. However, in the
case of the backward layer, the input sequence is fed from t = T to 1. Therefore, a mathematical representation of
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14597

---

## Page 10
the LSTM cell in the forward layer will remain the same. In contrast, mathematical expressions of the LSTM cell
in the backward layer denoted by the leftward arrow (/) at time t can be written as [40]:
F~ ¼ rðWfX~t þ WfR~t þ iÞ;
ð8Þ
I~¼ rðWiX~t þ WiR~t þ iÞ;
ð9Þ
O~ ¼ rðWoX~t þ WoR~t þ iÞ;
ð10Þ
G~ ¼ tanhðWgX~t þ WgR~t þ iÞ;
ð11Þ
C~t ¼ F~  C~t  1 þ I~ G~;
ð12Þ
R~t ¼ O~  tanhðC~tÞ:
ð13Þ
At each time step of bidirectional LSTM, two outputs will be generated, one by forwarding the LSTM layer
(Rt) and one by the backward LSTM layer (Rt ?). These two outputs will be merged to get the output. Final
output Y will be expressed as combining the outputs generated by individual LSTM layers.
Yt ¼ Rt þ R~t;
ð14Þ
Y ¼ yt1 þ yt þ ytþ1:
ð15Þ
4.3 Gated recurrent unit (GRU)
The Gated Recurrent Unit, like the LSTM, is a Recurrent Neural Network. It, however, has a less complex
architecture than LSTM–RNN. Further, in 2014 [41], proposed an improved architecture of RNNs in Gated
Recurrent Units (GRUs), which were further enhanced over the standard LSTM networks. They can handle
streams of identical input sequences of any length, the same as LSTMs, and hold the state containing historical
info. Yet, to control the ﬂow of information, there is only a single update gate to determine which data to let
through and which to reject and a reset gate to decide when to forget the past and start anew. This is not the same
as the LSTMs, which work with several gates and an internal memory cell. For this reason, GRUs are less
complex than LSTMs and can be trained much more straightforwardly but are equally effective when used in
different tasks [37]. As postulated by [37], GRUs have better performance compared to LSTMs in language
modeling than that of Penn Treebank. Indeed, in an NLP model comparison, GRUs again performed better than
CNNs and LSTMs in several qualities, ensuring the domination of GRUs. However, GRUs can outperform
ordinary RNNs in identifying the long dependency in sequential data patterns. Even though GRUs control current
data differently based on the current input and network state, their update and reset gates selectively enable the
reminiscence or forgetfulness of earlier information. Among the types of RNNs used for tasks, where it is
necessary to store and use a lot of information within the sequences, the so-called GRU is the best choice for you.
GRU has fewer gates than LSTM, which contributes to its high efﬁciency. The transition functions of GRU are
formulated as follows:
123
Neural Computing and Applications (2025) 37:14589–14611
14598
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 11
rt ¼ rðxtWr þ ht1Wr þ brÞ;
ð16Þ
zt ¼ rðxtWz þ ht1Wz þ bzÞ;
ð17Þ
~ht ¼ tanhðxtWx þ ðrt  ht1ÞWh þ bÞ;
ð18Þ
ht ¼ ð1  ztÞ  ht1 þ zt  ~ht:
ð19Þ
4.4 Autoregressive integrated moving average (ARIMA)
ARIMA, which stands for AutoRegressive Integrated Moving Average [42], is a robust statistical model com-
monly used for time series analysis. This model is designed to analyze data collected at regular intervals, allowing
for a consistent approach to forecasting. By leveraging historical data, ARIMA aims to predict future values based
on observed patterns and trends. The model focuses on two primary variables: the predicted characteristics, such
as sales, temperature, or stock prices, and the time these predictions are made. ARIMA consists of two essential
components: the autoregressive (AR) part, which uses the relationship between an observation and several lagged
observations (past values), and the moving average (MA) part, which models the interaction between an
observation and a residual error from a moving average model. To effectively implement an ARIMA model, three
critical hyperparameters must be identiﬁed and ﬁne-tuned: The number of autoregressive lags (p): This parameter
identiﬁes the amount of previous stale observations regarding integration into the model. Choosing a proper p
value lets us describe the current value’s dependency on its historical counterparts. The order of differencing (d):
This parameter refers to the number of times the data has to be differenced to become stationary. As it can be
recalled, one of the primary assumptions or conditions in using the ARIMA models is stationarity to guarantee
that the properties of the series are stable over space. The number of moving average terms (q): Out-of-home
moving expenses. This parameter determines the number of lagged forecast error terms in the forecast equation.
This is much easier said than done, and q must be appropriately determined to accommodate the noise in the data.
If well chosen, these hyperparameters allow practitioners to obtain an improved ARIMA model for better
forecasts based on historical time series data. In this context, the next step remains to identify the ARIMA model
(p, d, q) to ﬁt the situation under consideration. The long-standing time meaning that the esteem of a variable
could be a straight mixture of past values and past errors, which is shown in the ARIMA model as follows:
Xt ¼ u1Xt1 þ u2Xt2 þ    þ upXtp þ mt  h1mt1  h2mt2      hqmtk;
where Xt is the actual value, mt is a random error at time t, u1, u2,...,up are the coefﬁcients of the autoregressive
(AR) model, and h1, h2,...,hq are the coefﬁcients of the moving average (MA) model. The parameters p and q are
integers representing the orders of the autoregressive and moving average components, respectively.
4.5 Proposed model based on XAI
During training, a parametrized machine learning algorithm processes artiﬁcial data to optimize the minimization
of objective functions through adjustable parameters. This phase constitutes the LSTM’s data supply method
through batch distribution. The LSTM parameters receive their deﬁnitions and then proceed with evaluation in the
next operation phase. The illustration in Fig. 6 presents the LSTM Architecture. By applying the SHAP tool,
users can obtain an understandable model that is interpretable to neighborhoods after completing the training
process. Current AI systems generate user concerns through black-box models by showing prediction outputs,
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14599

---

## Page 12
while remaining completely opaque about variable-input relationships to output results. Interpretable models,
including linear regression, demonstrate superiority because they disclose the strength of variables to inﬂuence
prediction results. XAI provides a solution that enables people to understand the assessment processes behind AI
systems. The search for how features and model components affect each other occurs through black-box methods
in XAI during training periods. Domain experts in photovoltaic power generation beneﬁt from the solution
because it generates results that allow users to evaluate model rationality and follow variable interactions. SHAP
deﬁnes itself as the leading approach for delivering predictions from machine learning models through its
adaptable methodology. The explanation technique works with any model type because it lacks speciﬁc model
requirements, thus allowing its application across tree-based models, neu, real networks, and linear models.
SHAP derives its feature contribution calculations through the implementation of Shapley values. The distri-
bution of beneﬁts occurs through the Shapley value, which emerged from cooperative game theory to give equal
shares to coalition players. Researchers have observed signiﬁcant expansion in adopting this theory to create
machine learning explanation models throughout the past few years. The model explanation system displays both
variables as player characteristics through features and predictions as revenue outputs, while adopting principles
of Shapley value theory. The mathematical calculation for the Shapley value requires the following formula.
Mj ¼
X
SNn j
f g
Sj j! n  Sj j  1
ð
Þ!
n!
 x S [
j
f g
ð
Þ  x S
ð Þ
ð
Þ:
ð20Þ
where Mj is the contribution of the j-th variable; N is the set of all players (features) (1, 2, 3,..., j, . . . , n), which is
the complete set; S is a subset of N, in which the explained feature j is removed, with a total of 2n; v is the gain
function:
xðSÞ ¼ EA ^fðyÞjyS;
ð21Þ
Fig. 6 LSTM architecture
123
Neural Computing and Applications (2025) 37:14589–14611
14600
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 13
where A
ˆ is the empirical distribution of the training data; and f is the black-box model. SHAP assesses feature
signiﬁcance through global and local explanations, demonstrating both the general effects on model prediction
and the individual instance outcome impacts of each variable. SHAP has rapidly become popular within different
application domains, including LT care, image processing, and other areas. System transparency increases due to
understandable explanations regarding advanced machine learning models through the SHAP method, allowing
users greater conﬁdence in their predictions.
5 Experimental results
The evaluation of wind power generation prediction models was conducted using several key metrics: Mean
Square Error (MSE), Mean Absolute Deviation (MAD), Coefﬁcient of Multiple Determination (R2), Root Mean
Square Error (RMSE), Mean Bias Error (MBE), Correlation Coefﬁcient (r), Relative Root Mean Square Error
(RRMSE), Nash-Sutcliffe Efﬁciency (NSE), and Willmott Index of Agreement (WI). Table 2 presents the metrics
that evaluate the prediction models according to their efﬁciency and accuracy. The computational duration for
each model training was considered since it determines the practical implementation potential of this proposed
method. Since each model involves a unique computational cost and exhibits varying strengths and weaknesses in
terms of accuracy, the selection process is based on a trade-off between these characteristics. Tables 3 and 4
provide a comparative analysis of various machine learning models to highlight their advantages and limitations
in different conditions for wind power forecasting. Among these models, the Double Layer LSTM is the best
performer across all evaluation metrics. As shown in Tables 3 and 4, it achieves the lowest MSE (0.000113) and
RMSE (0.011021), indicating superior accuracy with minimal prediction errors. Furthermore, its correlation
coefﬁcient (r = 0.99996) supports an almost perfect prediction capability. The model displays robust properties
through NSE (0.98762) and WI (0.98465) values indicating reliability. The Double Layer LSTM reaches an
optimal rate of accuracy and efﬁcacy through its 9.35-second computation time. Competitively, the Single Layer
LSTM and GRU models achieve performance metrics slightly worse than the Double Layer LSTM results. The
single-layer LSTM achieves an MSE of 0.000199 along with an RMSE of 0.018743, and the GRU model
matches these results with an MSE of 0.000198 and an RMSE of 0.019056. Predictive accuracy remains
satisfactory for these models since they demonstrate correlation values that fall between 0.98 and 0.99. The
implementation time of the GRU exceeds the single-layer LSTM period, offering 14.39 seconds as opposed to
11.37 seconds. The bidirectional LSTM model demonstrates inferior performance in terms of prediction accuracy
Table 2 Equations for
evaluation metrics
Metric
Equation
Coefﬁcient of Determination
R2 ¼ 1 
Pn
j¼1
FjZj
ð
Þ
2
Pn
j¼1 FjF2
Mean Square Error
MSE = 1
n
Pn
j¼1 Fj  Zj

2
Mean Absolute Error
MAE = 1
n
Pn
j¼1 Fj  Zj
Root Mean Square Error
RMSE = 1
n
Pn
j¼1 Fj  zj

2
Correlation Coefﬁcient
r ¼
qPs
i¼1 fif
ð
Þ ^fi ^f
ð
Þ
Ps
i¼1
f if
ð
Þ
2PS
i¼1
^fi ^f
ð
Þ
2
Relative Root Mean Square Error
RRMSE =
1
s
Ps
i¼1
fi ^fi
ð
Þ
2
f
Nash–Sutcliffe Efﬁciency
NSE = 1 -
PS
i¼1
fi ^fi
ð
Þ
2
PS
i¼1
fif
ð
Þ
2
Willmott Index of Agreement
WI = 1 -
P
i¼1 fifi
ð
Þ
PS
i¼1 ^fifþfif
2
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14601

---

## Page 14
compared to the basic LSTM models. The prediction performance becomes less effective because the MSE
reaches 0.000162 and the RMSE reaches 0.021743 for this model. Although the MBE value is 0.033915, this
model may display an existing prediction bias. The Transformer ? LSTM hybrid model demonstrates limited
effectiveness for wind power generation prediction according to the data in Table 4. The hybrid model with
Transformer ? LSTM reaches 0.019594 MSE and 0.139978 RMSE but fails to match LSTM-only models. The
combination of Transformer with LSTM does not seem to function well for this particular task. This model needs
too much time, at 17.42 seconds, to function practically. ARIMA produces the least successful results among all
prediction models. It reports the highest error values, with an MSE of 0.024507, an RMSE of 0.156546, and a
lower correlation coefﬁcient (r = 0.9214), indicating a weaker relationship between predicted and actual values
than deep learning models. Although ARIMA exhibits relatively low MBE (0.04197) and moderate NSE
(0.95479) and WI (0.98155) values, its ability to capture wind power generation dynamics remains limited due to
its lack of adaptability to temporal patterns. Furthermore, its computation time of 24.46 seconds makes it the least
efﬁcient model in this study. Although the bidirectional LSTM model remains a standard tool in many appli-
cations, it displays room for enhancement by reducing its current error standards compared to basic LSTM
models. The results demonstrate an MSE of 0.000162 and an RMSE of 0.021743, while displaying an MBE value
of 0.033915, which indicates possible bias in prediction. Although incorporating two robust architectures, the
Transformer ? LSTM hybrid model performs less effectively than LSTM-only structures. It achieves an MSE of
0.019594 and an RMSE of 0.139978, but these values indicate a drop in predictive performance compared to
simpler LSTM variants. This suggests that the Transformer component may not integrate efﬁciently with LSTM
for this speciﬁc task. Furthermore, with a computation time of 17.42 seconds, this model is less efﬁcient than its
LSTM-only counterparts. The ARIMA model demonstrates the weakest predictive capabilities at the lower end of
the performance spectrum. It reports the highest error values, with an MSE of 0.024507 and RMSE of 0.156546.
The correlation coefﬁcient value (r = 0.9214) reveals that the predictive strength between actual and predicted
values is lower than deep learning models, thus indicating weaker predictive power. Although ARIMA exhibits
relatively low MBE (0.04197) and moderate NSE (0.95479) and WI (0.98155) values, its ability to capture wind
power generation dynamics remains limited due to its constraints in modeling temporal dependencies. Moreover,
its computational time of 24.46 seconds makes it the least efﬁcient model in this study. SHAP (Shapley Additive
exPlanations) values were employed further to analyze input features’ inﬂuence on model predictions, as shown
in Fig. 7. Each input feature is represented as a vertical bar, with its position indicating its Contribution to the
model’s predictions. The SHAP summary bar chart evaluates features through their mean absolute SHAP values
Table 3 Performance Met-
rics Depend on MSE,
RMSE, MAE, MBE, and r
Models
MSE
RMSE
MAE
MBE
r
Double Layer LSTM
0.00011
0.01102
0.00816
0.00843
0.99996
Single Layer LSTM
0.00020
0.01874
0.00962
0.01042
0.98998
GRU
0.00020
0.01906
0.01091
0.01068
0.97993
Bidirectional LSTM
0.00016
0.02174
0.00962
0.03392
0.96986
Transformer ? LSTM
0.01959
0.13998
0.09245
0.02912
0.93119
ARIMA
0.02451
0.15655
0.13731
0.01646
0.92137
Table 4 Performance Met-
rics Depend on RRMSE,
NSE, WI, and Fitted Time
Models
R2
RRMSE
NSE
WI
Fitted Time (s)
Double Layer LSTM
0.98860
2.57637
0.98762
0.98465
9.35368
Single Layer LSTM
0.98730
2.63750
0.97759
0.98276
11.37579
GRU
0.98460
2.70348
0.97756
0.98300
14.39658
Bidirectional LSTM
0.98730
2.80976
0.97641
0.98155
16.41367
Transformer ? LSTM
0.93460
2.76483
0.96756
0.98300
17.42966
ARIMA
0.92480
2.89890
0.95479
0.98155
24.46384
123
Neural Computing and Applications (2025) 37:14589–14611
14602
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 15
to present the most inﬂuential variables for forecasting purposes. The feature values align with the horizontal axis,
yet their priority levels are shown in the vertical bars. Through this analysis, researchers gain insights regarding
their present model execution and develop a framework for future model optimization to construct effective and
shallow models that retain accuracy levels. The data in Fig. 7 reveals that Feature_59 establishes itself as the most
inﬂuential variable with a score value of 0.76. The signiﬁcance score of Feature_58 comes in second to Fea-
ture_59, according to the summary results. The signiﬁcance levels start from Feature_57 at 0.88 before reaching a
moderate value for Feature_56, then continue declining for less signiﬁcant elements beginning with Feature_54.
This framework produces important results about which features have the most signiﬁcant impact on predictive
values, enabling a better selection of features and reduction methods. Excessive optimization of core variables
enables dimensional search space reduction, which might lead to effective shallow models with high accuracy
levels.
6 Discussion of satisical result analysis
The performance metrics in Fig. 8 are compared using a visual heatmap structure, which includes MSE, RMSE,
MAE, MBE, R-squared, NSE, and WI. The performance metrics in the heatmap reveal better results through dark
colors, thus enabling easy and rapid detection of the leading models. The proposed Double Layer LSTM
demonstrates exceptional performance, particularly in its superior predictive accuracy in almost every evaluation
metric. The visual representation exhibits the comparison between models and ultimately demonstrates the
Double- Layer LSTM’s impressive predictive accuracy, convincing the audience of its effectiveness. Figure 9
Fig. 7 Contribution of each
model attribute to the pre-
diction outcomes
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14603

---

## Page 16
presents a vertical bar chart showing different performance indicators dispersed across models to provide sig-
niﬁcant statistical data about their statistical matching with the available dataset. Error measures, including MSE,
RMSE and MAE, exhibit most of their values distributed in the lower parts of the scale. The model performance
shows good results through this concentration of data points that support its reliability through low error margins.
Multiple visualizations produce an extensive and comprehensive performance evaluation of the Double Layer
LSTM model, providing a wealth of knowledge in wind power forecasting scenarios. The Willmott Index (WI)
operates crucially for forecasting accuracy because its value stays at one, demonstrating high agreement between
Fig. 8 Heatmap of perfor-
mance metrics
Fig. 9 Stacked KDE of
different models
123
Neural Computing and Applications (2025) 37:14589–14611
14604
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 17
predicted and actual values. The index functions as a dependable method for evaluating the prediction capabilities
of developed models. Figure 9 contains vital points that reveal how different models perform based on their
metrics. The visual representation shows that measurement performance between models is comparable because
metrics values are distributed symmetrically at low density for errors and high density for WI metrics. This
Fig. 10 compares the performance of different models based on three main metrics. Their mean and standard
deviation have also been calculated and presented: MSE, RMSE, and MAE. Speciﬁc models, such as double layer
LSTM and bidirectional LSTM, outperformed other models by giving low errors compared to other models. On
the other hand, Transformer ? LSTM and other models, such as ARIMA, offered worse results, with notably
higher values. The same chart also reveals that LSTM-based models have a low standard deviation, denoting the
relative stability and reliability of these models. The plot in Fig. 11 is a comprehensive illustration of the
performance of various models across a set of evaluation metrics. The models include double layer LSTM, single-
layer LSTM, GRU, Bidirectional LSTM, Transformer ? LSTM, and ARIMA. Various performance indicators
(MSE, RMSE, MAE, and others) can be placed on the horizontal axis, and their values are plotted on the vertical
axis. This is evidenced by the fact that the lines are closely clustered for all the plots, except the x-axis, for such
measures as RMSE, R2, and WI. The measured model performances demonstrate shared similarities between
them. RRMSE and MSE assessment parameters show minor variations between the different regression models.
Each colored line in Fig. 9 shows different models performing their assessment. Among all models, ARIMA
exhibits speciﬁc characteristics speciﬁc to performance measurement parameters. This analysis conﬁrms the
overall identical performance of the models yet shows the necessity to focus on speciﬁc metrics for improving
model efﬁciency. The radar Fig. 12 is a comprehensive tool that provides a detailed overview of the model’s
performance across various tests and measurements. Each axis on the radar plot corresponds to a speciﬁc metric:
MSE, RMSE, MAE, and MBE, which are global measures of the error and bias of the problems. r, R2:
Quantitative data on regularity and correspondence: coefﬁcients of correlation and ﬁts. This comprehensive tool
equips the audience with a powerful means to evaluate model performance. RRMSE, NSE, WI: Measures that
give information about the performance of models in terms of their accuracy and the resources used in their
Fig. 10 Comparision of
models by mean and stan-
dard deviation
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14605

---

## Page 18
creation. The blue line shows the connection of values of each measured parameter, making it a polygonal line.
Higher values are located farther from the origin, making Employee metrics look better (if not error-based metrics
such as MSE or RMSE, where lower values indicate better performance). The horizontal blue line covers the
entire model performance area, also shaded in the Figure. Radar plots can also be used to ﬂag the strengths and
weaknesses of metrics together at a single glance. For example, a model might exhibit high R2 while, at the same
time, having high total error, as can be seen from the plot of the data. This Fig. 13 presents a visually engaging
tool for understanding how the MSE varies across different models using Cubic Spline Interpolation. Raw data
points are displayed in red dots, indicating the diagram’s MSE values for particular models. These MSE values
become accessible through the blue curved path that cubic spline interpolation produced. The independent
variable exists along the X-axis as different models, while the dependent variable stays on the Y-axis as MSE
Fig. 11 Plotting parallel coordinates
Fig. 12 Radar plot of
model performance metrics
123
Neural Computing and Applications (2025) 37:14589–14611
14606
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 19
Fig. 13 Spline interpola-
tion for MSE trend across
models
Fig. 14 Mixed Plot – Density ? KDE
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14607

---

## Page 20
values. Cubic spline interpolation offers a visually pleasing way to understand the overall pattern of the set
through its representation of error increases or decreases. For instance, we observe higher MSE for more
signiﬁcant model indices, indicating a change in model behavior. Figure 14 show cases nine images illustrating
the model prediction metrics through density plots and the Kernel Density Estimation technique. The KDE plot
helps observers understand how the model operates across all evaluated metrics. MSE, RMSE, MAE: These are
some of the ways most often used for evaluating the size of prediction errors. Mean Bias Error indicates that there
is bias in the predictive computation. A positive value indicates a tendency to over-predict, while a negative value
indicates under-predicting. r and R2: Employing such measures explains the relationship between the anticipated
and actual case incidences. The R2 part shows how much of the actual value variation can be attributed to the
internal model. Root Mean Squared Error then scales the prediction errors to the extent that they can be compared
more conveniently. Nash Sutcliffe Efﬁciency measures how well the model is. Such values signify that higher
values are associated with better accuracy. A comparison of the actual and predicted values can be made by
looking at the Willmott Index. Each plot has an area shaded in green to point at the metric values, and above the
KDE plot, there is a smooth blue curve to accentuate density ﬂuctuations. Performance ﬁgures are well conveyed
by this form of visualization. The current Fig. 15 displays the box plot with swarm overlay showing the
performance of the predictive models based on several evaluation metrics. This paper used MSE, RMSE, MAE
MAE, MBE, r, R2, RRMSE, NSE and WI to analyze the accuracy of the models. The box plot again helps to give
a view of the data distribution for each of the metrics and shows the median, the range between the ﬁrst and third
quartiles and any outliers. The swarm overlay is depicted in the form of individual dots in black to provide an
open for the spread and density of values as depicted by individual dots. However, the R2 and WI diagnostics
show a higher coefﬁcient, highlighting the model’s efﬁciency regarding variance explanation and comparing with
real-world data. Hence, the model is evaluated based on MSE, RMSE and MAE, which reveal comparatively
small ﬁgures indicating minimal prediction errors. In total, the graph of the outcoming metrics underlines the
stability of the predictive model, as such characteristics are stable regardless of the measure chosen. Thus, high
values of the correlation coefﬁcients (r and R2) along with low error measures support that the proposed model
performs the outcome prediction effectively. Moreover, it is possible to note that most distributions are compact,
indicating stable and relatively reliable performance in most tested conditions. Overall, this visualization does a
great job of revealing the strengths and weaknesses of the model and informs a general audience of the kind of
performance the model can deliver.
Fig. 15 Box Plot for per-
formance of predictive
models
123
Neural Computing and Applications (2025) 37:14589–14611
14608
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 21
7 Conclusion
Energy management system quality has emerged as a primary area of research in renewable energy because it
stands as an essential distribution method for electricity. Wind speed predictions constitute a fundamental
component of the system. The proposed method uses X-double LSTM technology to produce reliable wind speed
forecasting results under differing environmental situations. When utilized in the selected dataset, the statistical
model presented effectiveness in forecasting wind power. Multiple metrics, including MSE, RMSE, MAE, MBE,
r, R2, RRMSE, NSE, and WI, show that the model achieves accurate results. The results prove that the proposed
methodology effectively generates wind power forecasts. The implemented model uses an XAI-based shap
algorithm for result explanation to improve transparency alongside predictive output interpretability. This
algorithm identiﬁes the most critical wind power-generating features to measure output levels, resulting in
trustworthy model predictions. Combining X-double LSTM with an XAI-based shap enhances wind power
generation prediction accuracy through an improved explanation of prediction results. Results from this work
establish fundamental knowledge for deploying renewable energy technologies, especially wind power genera-
tion facilities. Further evaluation with extended datasets should occur to establish the proposed methodology’s
superior performance and enhanced prediction methods during future implementation.
Funding Open access funding provided by The Science, Technology & Innovation Funding Authority (STDF) in coop-
eration with The Egyptian Knowledge Bank (EKB). Not applicable.
Data availability The data that support the ﬁndings of this study are openly available at [https://www.kaggle.com/datasets/
jorgesandoval/wind-power-generation].
Declarations
Conflicts of interest The authors declare that they have no conflicts of interest to report regarding the present study.
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
1. Sherstinsky A (2020) Fundamentals of recurrent neural network (rnn) and long short-term memory (lstm) network. Phys
D: Nonlinear Phenom 404:132306
2. Qureshi S et al (2023) Short-term forecasting of wind power generation using artiﬁcial intelligence. Environ Challenges
11:100722. https://doi.org/10.1016/j.envc.2023.100722
3. Lin W, Wu D, Boulet B (2021) Spatial-temporal residential short-term load forecasting via graph neural networks. IEEE
Transactions on Smart Grid 12:5373–5384
4. Cao W, Liu Y, Mei H, Shang H, Yu Y (2023) Short-term district power load self-prediction based on improved xgboost
model. Eng Appl Artif Intell 126:106826
5. Long AW (2016) Learning to place one foot in front of the other: investigation of action and perception in human split-
belt walking. Ph.D. thesis, The Johns Hopkins University.
6. Tian C, Niu T, Wei W (2022) Developing a wind power forecasting system based on deep learning with attention
mechanism. Energy 257:124750
7. Niu D, Sun L, Yu M, Wang K (2022) Point and interval forecasting of ultra-short-term wind power based on a data-
driven method and hybrid deep learning model. Energy 254:124384
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14609

---

## Page 22
8. Dong X et al (2023) Transferable wind power probabilistic forecasting based on multi-domain adversarial networks.
Energy 285:129496
9. He B et al (2022) A combined model for short-term wind power forecasting based on the analysis of numerical weather
prediction data. Energy Rep 8:929–939
10. Li Y, Wang R, Li Y, Zhang M, Long C (2023) Wind power forecasting considering data privacy protection: A federated
deep reinforcement learning approach. Appl Energy 329:120291
11. Shahid F, Khan A, Zameer A, Arshad J, Safdar K (2020) Wind power prediction using a three stage genetic ensemble
and auxiliary predictor. Appl Soft Comput 90:106151
12. Pan X, Wang L, Wang Z, Huang C (2022) Short-term wind speed forecasting based on spatial-temporal graph trans-
former networks. Energy 253:124095
13. Yin S, Liu H (2022) Wind power prediction based on outlier correction, ensemble reinforcement learning, and residual
correction. Energy 250:123857
14. Peiris AT, Jayasinghe J, Rathnayake U (2021) Forecasting wind power generation using artiﬁcial neural net-
work:‘‘pawan danawi’’—a case study from sri lanka. J Electr Comput Eng 2021:5577547
15. Delgado I, Fahim M (2020) Wind turbine data analysis and lstm-based prediction in scada system. Energies 14:125
16. Lo´pez G, Arboleya P (2022) Short-term wind speed forecasting over complex terrain using linear regression models and
multivariable lstm and narx networks in the andes mountains, ecuador. Renew Energy 183:351–368. https://doi.org/10.
1016/j.renene.2021.10.070
17. Sun F, Jin T (2022) A hybrid approach to multi-step, short-term wind speed forecasting using correlated features.
Renewable Energy 186:742–754. https://doi.org/10.1016/j.renene.2022.01.041
18. Xiong B et al (2022) Short-term wind power forecasting based on attention mechanism and deep learning. Electr Power
Syst Res 206:107776. https://doi.org/10.1016/j.epsr.2022.107776
19. Yu C, Li Y, Bao Y, Tang H, Zhai G (2018) A novel framework for wind speed prediction based on recurrent neural
networks and support vector machine. Energy Convers Manag 178:137–145. https://doi.org/10.1016/j.apenergy.2019.
01.010
20. Shang Z, He Z, Chen Y, Chen Y, Xu M (2022) Short-term wind speed forecasting system based on multivariate time
series and multi-objective optimization. Energy 238:122024. https://doi.org/10.1016/j.energy.2021.122024
21. Praveena R, Dhanalakshmi K (2018) Wind power forecasting in short-term using fuzzy k-means clustering and neural
network. In: 2018 international conference on intelligent computing and communication for smart world (I2C2SW),
336–339, https://doi.org/10.1109/I2C2SW45816.2018.8997350 (IEEE, 2018).
22. Ghanbarzadeh A, Noghrehabadi A, Behrang MA, Assareh E (2009) Wind speed prediction based on simple meteo-
rological data using artiﬁcial neural network. In: 2009 7th IEEE international conference on industrial informatics,
664–667 (IEEE, 2009).
23. Abdoos AA, Abdoos H, Kazemitabar J, Mobashsher MM, Khaloo H (2023) An intelligent hybrid method based on
monte carlo simulation for short-term probabilistic wind power prediction. Energy 278:127914
24. Ma Z, Mei G (2022) A hybrid attention-based deep learning approach for wind power prediction. Appl Energy
323:119608
25. Shahid F, Zameer A, Muneeb M (2021) A novel genetic lstm model for wind power forecast. Energy 223:120069
26. Azimi R, Ghofrani M, Ghayekhloo M (2016) A hybrid wind power forecasting model based on data mining and
wavelets analysis. Energy Conv Manag 127:208–225
27. Shi X et al (2018) Hourly day-ahead wind power prediction using the hybrid model of variational model decomposi-
tion and long short-term memory. Energies 11:3227
28. Lahouar A, Slama JBH (2017) Hour-ahead wind power forecast based on random forests. Renew Energy 109:529–541
29. Vela´zquez S, Carta JA, Matı´as J (2011) Inﬂuence of the input layer signals of anns on wind power estimation for a target
site: A case study. Renew Sustain Energy Rev 15:1556–1566
30. Su Y. et al. (2019) A lstm based wind power forecasting method considering wind frequency components and the wind
turbine states. In: 2019 22nd International Conference on Electrical Machines and Systems (ICEMS), 1–6 (IEEE, 2019).
31. Zu X, Song R (2018) Short-term wind power prediction method based on wavelet packet decomposition and improved
gru. J Phys Conf Ser, vol. 1087, 022034 (IOP Publishing, 2018).
32. Mujeeb S et al (2019) Exploiting deep learning for wind power forecasting based on big data analytics. Appl Sci 9:4417
33. Hochreiter S (1997) Long short-term memory. Neural Comput MIT-Press. https://doi.org/10.1162/neco.1997.9.8.1735
34. Graves A, Mohamed A-r, Hinton G (2013) Speech recognition with deep recurrent neural networks. In: 2013 IEEE
international conference on acoustics, speech and signal processing, 6645–6649, https://doi.org/10.1109/icassp.
2013.6638947 (Ieee, 2013).
35. Zhang J et al (2023) Research on none-line-of-sight/line-of-sight identiﬁcation method based on convolutional neural
network-channel attention module. Sensors 23:8552
36. Sunjaya BA, Permai SD, Gunawan AAS (2023) Forecasting of covid-19 positive cases in indonesia using long short-
term memory (lstm). Procedia Comput Sci 216:177–185
123
Neural Computing and Applications (2025) 37:14589–14611
14610
https://doi.org/10.1007/s00521-025-11230-5

---

## Page 23
37. Yang S, Yu X, Zhou Y (2020) Lstm and gru neural network performance comparison study: Taking yelp review dataset
as an example. In: 2020 International workshop on electronic communication and artiﬁcial intelligence (IWECAI),
98–101 (IEEE, 2020).
38. Lai S, Ye C, Zhou HJH (2021) Chinese stock trend prediction based on multi-feature learning and model fusion. In:
2021 IEEE International Conference on Smart Data Services (SMDS), 18–23 (IEEE, 2021).
39. Boissonneault D, Hensen E (2024) Fake news detection with large language models on the liar dataset.
40. Subbiah SS, Paramasivan SK, Arockiasamy K, Senthivel S, Thangavel M (2023) Deep learning for wind speed
forecasting using bi-lstm with selected features. Intell Autom Soft Comput 35.
41. Chung J, Gulcehre C, Cho K, Bengio Y (2014) Empirical evaluation of gated recurrent neural networks on sequence
modeling. arXiv preprint arXiv:1412.3555
42. Li X, Sabas JF, Mende´z VD (2022) Wind energy forecasting using multiple arima models. In: 2022 IEEE 18th
International Conference on Automation Science and Engineering (CASE), 2034–2039 (IEEE, 2022).
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.
Authors and Afﬁliations
Mona Ahmed Yassen1,2 • El-Sayed M. El-Kenawy3,4,5,6 • Mohamed Gamal Abdel-Fattah2 •
Islam Ismail2 • Hossam El-Deen Salah Mostafa2
& Mona Ahmed Yassen
Monagaffer@std.mans.edu.eg
1
Faculty of Artiﬁcial Intelligence, Hours University, Damietta, Egypt
2
Department of Electronics and Communications Engineering, Faculty of Engineering, Mansoura
University, Mansoura 35516, Egypt
3
School of ICT, Faculty of Engineering, Design and Information&Communications Technology(EDICT),
Bahrain Polytechnic, PO Box 33349, Isa Town, Bahrain
4
Applied Science Research Center, Applied Science Private University, Amman, Jordan
5
Jadara University Research Center, Jadara University, Irbid, Jordan
6
Department of Communications and Electronics, Delta Higher Institute of Engineering and Technology,
Mansoura 35111, Egypt
Neural Computing and Applications (2025) 37:14589–14611
123
https://doi.org/10.1007/s00521-025-11230-5
14611

---
