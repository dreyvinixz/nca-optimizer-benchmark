# Stock price forecasting through symbolic dynamics and state transition graphs with a convolutional recurrent neural network architecture

**Year**: 2025 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-025-11325-z

---

## Page 1
ORIGINAL ARTICLE
Stock price forecasting through symbolic dynamics
and state transition graphs with a convolutional
recurrent neural network architecture
Fuat Kaan Mirza1
• O¨ nder Pekcan1 • Mustafa Hekimog˘lu1 • Tunçer Baykas¸1
Received: 28 December 2024 / Accepted: 2 May 2025 / Published online: 31 May 2025
 The Author(s) 2025
Abstract
Accurate stock price forecasting remains a critical challenge in ﬁnancial analytics due to volatile market con-
ditions, non-stationary dynamics, and abrupt regime shifts that often defy traditional modeling techniques. This
study proposes a comprehensive framework for stock price forecasting that integrates symbolic dynamics, graph-
based state representations, and deep learning. By converting continuous-valued stock prices into discrete
symbolic states representing amplitude and trend information, the method constructs transition matrices capturing
probabilistic relationships within ﬁnancial time series. These transition matrices are then processed by a con-
volutional recurrent neural network (CRNN), in which convolutional layers isolate local spatial dependencies in
the symbolic-state domain, while recurrent LSTM layers capture multi-scale temporal dynamics extending across
multiple time horizons. Experimental evaluations are conducted over prediction horizons of 1 day, 10 days, and
100 days, spanning pre-COVID, COVID, and post-COVID market regimes. The results indicate that while longer
prediction horizons naturally incur greater forecasting uncertainty due to compounding variability, the integration
of symbolic-state preprocessing with deep temporal modeling demonstrates signiﬁcant robustness in handling
non-stationary ﬁnancial environments. During the stable pre-COVID period, the proposed methodology achieves
reductions in mean squared error (MSE) of up to 98% relative to the volatile COVID phase, highlighting its
capability to effectively leverage well-deﬁned market patterns in stable economic conditions. Furthermore, the
model consistently delivers competitive forecasting performance across all prediction horizons and market
regimes. Collectively, these ﬁndings emphasize the potential of symbolic-state-based deep learning architectures
as a viable pathway to address the complexity and volatility characteristic of modern ﬁnancial markets.
Keywords Symbolic dynamics  Stock price forecasting  Graph signal processing  Convolutional recurrent
neural network  Non-stationary time series
1 Introduction
Forecasting stock prices is a central objective in ﬁnancial analytics, underpinning decisions in risk management,
policy formation, and strategic investment. The inherent complexity of ﬁnancial time series, characterized by high
volatility, non-stationary, and strong nonlinear dependencies, presents a continuous challenge to researchers and
practitioners. Early methods for ﬁnancial time series modeling provided structured statistical frameworks that
offered a degree of interpretability and analytical rigor [1–6]. However, these classical models assume relatively
stable market conditions and linear or near-linear relationships, limiting their capability to adapt to the complex,
Neural Computing and Applications (2025) 37:15855–15890
https://doi.org/10.1007/s00521-025-11325-z
123
Neural Computing and Applications (2025) 37:15855–15890

---

## Page 2
evolving patterns that characterize modern ﬁnancial environments. In response, researchers have increasingly
turned to more ﬂexible methodologies that can handle richer dynamics. Modern machine learning (ML) and deep
learning (DL) approaches, including long short-term memory (LSTM) networks and convolutional neural net-
works (CNNs), have demonstrated considerable promise in modeling complex time series. Despite these
advances, these methods often rely on extensive feature engineering, encounter difﬁculties in interpreting their
internal representations, and may not fully exploit the underlying qualitative patterns that drive price movements.
A supplementary approach to comprehending non-stationary ﬁnancial time series is offered by symbolic
dynamics, a paradigm that has its origins in nonlinear dynamics and chaos theory. By transforming continuous-
valued signals into sequences of discrete symbols, symbolic dynamics highlights structural characteristics and
reduces noise, enabling researchers to focus on meaningful qualitative behaviors rather than raw numerical
ﬂuctuations. This symbolic representation aligns naturally with graph-theoretic approaches, allowing complex
temporal interactions to be visualized and analyzed as state transition networks. Such integration between
symbolic encodings and graph-based modeling has the potential to enhance interpretability, reveal hidden market
regimes, and better guide the choice of predictive models.
To fully capitalize on the structured information provided by symbolic dynamics and its associated graph-
based abstractions, it is imperative to integrate these representations seamlessly with state-of-the-art predictive
modeling frameworks. By encoding raw ﬁnancial time series into discrete symbolic states that preserve essential
amplitude and directional characteristics, the process obviates the need for extensive domain-dependent feature
engineering. Subsequently, representing state transitions as weighted graphs provides a mathematically rigorous
substrate, akin to Markov transition matrices, from which complex temporal dependencies can be systematically
extracted. Advanced machine learning and deep learning architectures, particularly those equipped with recurrent
units, can then operate directly on these state-space representations to identify latent patterns, long-range cor-
relations, and regime-switching behaviors that remain obscured in conventional continuous-valued signals. In
doing so, symbolic encodings not only offer a dimensionality-reduced and noise-ﬁltered input domain but also
facilitate informed architectural decisions, hyperparameter tuning, and the selection of learning objectives,
thereby enhancing the stability and adaptability of predictive models under non-stationary and rapidly evolving
market conditions.
This study enhances the accuracy and robustness of stock price forecasting by combining the interpretive
strength of symbolic dynamics with the modeling capabilities of graph-based state representations and advanced
deep learning architectures. The proposed pipeline begins by symbolically encoding amplitude and directional
information from raw ﬁnancial time series, thereby distilling noisy price data into discrete states emphasizing
meaningful temporal patterns. Unlike purely data-driven models that rely on raw numerical sequences, this
symbolic transformation reduces overﬁtting by ﬁltering out stochastic ﬂuctuations while preserving essential
structural patterns. State transition matrices are constructed from these symbolic encodings, capturing the
probabilistic relationships that govern market dynamics. These matrices serve as a compact and inter-
pretable representation of ﬁnancial trends, facilitating the extraction of key transition probabilities that encode
short-term ﬂuctuations and long-range dependencies. These transition matrices are fed into a convolutional
recurrent neural network (CRNN). This hybrid architecture harnesses convolutional layers to extract local spatial
features and recurrent layers to capture long-term temporal dependencies. Employing convolutional ﬁlters, the
model effectively identiﬁes prominent structural motifs in transition matrices, while the recurrent layers ensure
the retention of historical dependencies crucial for robust predictions. Departing from traditional deep learning
models that treat ﬁnancial time series as raw numerical inputs, this approach structures data into symbolic
sequences and transition matrices, enabling the extraction of latent regime shifts and nonlinear dependencies that
remain hidden in conventional forecasting methods. This methodological shift enhances predictive stability under
market turbulence. It provides a degree of interpretability, as transitions between symbolic states can be analyzed
to understand regime-switching behaviors and volatility clustering. By synergizing the principled abstraction of
symbolic states with the adaptive learning capabilities of deep neural networks, the proposed framework delivers
more resilient, context-aware forecasts that retain scalability. Additionally, this hybrid formulation facilitates
123
Neural Computing and Applications (2025) 37:15855–15890
15856
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 3
generalization across multiple assets and market conditions, reducing sensitivity to overﬁtting while maintaining
adaptability to non-stationary ﬁnancial environments. By integrating symbolic encodings and CRNN-based
learning,
the
proposed framework
effectively
captures
hierarchical
temporal
structures,
allowing
for
microstructural pattern recognition and broader trend forecasting across varying time horizons.
The contributions of this work are threefold. First, an integrated symbolic-dynamics-to-CRNN pipeline is
introduced, extending beyond conventional feature engineering to provide a more principled approach for
highlighting essential temporal structures. This integration bridges the gap between purely statistical approaches
and deep learning methods, offering a structured yet data-driven representation that retains interpretability while
improving predictive accuracy. Second, the proposed method is empirically evaluated across multiple prediction
horizons (1-day, 10-day, and 100-day) and distinct market regimes (pre-COVID, COVID, and post-COVID),
demonstrating adaptability and resilience under shifting conditions. Through this extensive evaluation, the study
systematically examines how different market structures inﬂuence transition probabilities and neural network
performance, shedding light on the robustness of symbolic-state representations under varying volatility regimes.
Unlike traditional econometric approaches that struggle with capturing nonlinear dependencies or deep learning
models that lack interpretability, this approach provides both probabilistic insights and scalable learning capa-
bilities, offering a balanced perspective for theoretical advancements and practical applications in ﬁnancial
forecasting.
The following sections begin with a review of relevant literature, tracing developments from traditional
econometric approaches to advanced machine learning and deep learning architectures, followed by an intro-
duction to symbolic dynamics methodologies. Next, the theoretical foundations of symbolic dynamics are out-
lined, along with a detailed explanation of data preprocessing and model construction steps. The empirical results
are then analyzed, emphasizing the potential of symbolic-state-based modeling and CRNN architectures as a
promising framework for developing more robust and scalable ﬁnancial forecasting models.
2 Literature review
The ﬁeld of stock price forecasting encompasses a wide spectrum of approaches, each designed to capture distinct
facets of ﬁnancial time series complexity. The ﬁrst subsection examines foundational econometric models such as
ARIMA and GARCH and their extensions via machine learning and fuzzy logic frameworks. These methods
combine the statistical rigor of traditional econometrics with the ﬂexibility of data-driven feature engineering and
linguistic rule encoding. The second subsection focuses on deep learning techniques, including RNNs, LSTMs,
and CNNs, which alleviate the dependence on predeﬁned features by learning relevant representations directly
from raw data. Recent enhancements, such as attention mechanisms and hybrid architectures, further improve
robustness in non-stationary market environments. Finally, the third subsection introduces symbolic dynamics
and graph-based methodologies, emphasizing their ability to capture underlying nonlinear structures, identify
market regimes, and enhance transparency of collective trends. In synthesizing these three complementary
threads, this literature review outlines the progression toward more adaptive, explainable, and high-performing
stock price forecasting models.
2.1 Machine learning, statistical learning, and fuzzy logic-based stock price forecasting
Machine learning (ML) and statistical learning methodologies have long been a focal point of ﬁnancial time series
forecasting, with a substantial body of literature exploring their application to stock price prediction. Traditional
approaches rooted in statistical econometrics, such as ARIMA and GARCH models, rely on well-deﬁned sta-
tistical assumptions to characterize time-dependent structures and volatility patterns [4, 7–10]. These classical
models are often employed as baseline predictors due to their mathematical rigor, interpretability, and well-
understood theoretical properties [4–6, 8].
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15857

---

## Page 4
Building on the limitations of traditional econometric frameworks, researchers have increasingly embraced
advanced ML techniques for more adaptive forecasting solutions. Concurrently, advanced ML algorithms,
ranging from margin-based classiﬁers like SVMs [11, 12] to ensemble methods such as random forests [13] and
gradient boosting machines [14, 15], have gained traction by leveraging high-dimensional feature spaces and
ﬂexible function approximators. These approaches integrate sophisticated feature engineering techniques (e.g.,
technical indicators, sentiment metrics, and regime-switching markers) to model linear and nonlinear dynamics in
complex ﬁnancial environments. They are frequently augmented by hyperparameter optimization strategies and
cross-validation protocols to enhance generalization performance and mitigate overﬁtting, thus often outper-
forming classical models in short-term forecasting horizons [16–18]. As the literature attests, these machine
learning methodologies effectively address short-horizon volatility, laying the groundwork for specialized hybrid
systems that incorporate deep learning architectures and domain-speciﬁc heuristics.
In parallel with these theoretical and methodological developments, a growing number of empirical studies
highlight the practical efﬁcacy of advanced machine learning approaches in various ﬁnancial contexts. Gu et al.
[15] proposed a hybrid forecasting model combining empirical wavelet transform and gradient boosting decision
trees to predict the settlement prices of London Metal Exchange Nickel, demonstrating its superiority over
traditional EMD-based methods. Andrade and Cunha [16] proposed an XGBoost-based method for disaggregated
retail demand forecasting, addressing inventory inaccuracies, promotional impacts, and structural changes. Using
a large real-world dataset, their model outperformed the Base-Lift benchmark, improving forecasting accuracy by
26.72% and reducing stockouts and excess inventory, offering a scalable and automated solution for retail
operations. These empirical advancements emphasize not only the enhanced performance of modern ML models
but also the necessity of exploring alternative paradigms that can adapt to evolving market conditions.
As the complexity of ﬁnancial markets continues to challenge conventional modeling paradigms, fuzzy logic-
based frameworks emerge as a compelling alternative to purely quantitative approaches. Fuzzy logic-based
approaches provide an alternative way that incorporates linguistic variables and membership functions, thereby
accommodating uncertainty, ambiguity, and imprecision inherent in ﬁnancial markets [19–21]. Such systems can
codify human expert knowledge into interpretable rule sets, particularly important in volatile and rapidly shifting
market conditions, while preserving robustness against noisy and partially observed data. Nevertheless, although
these methods have demonstrated promise in capturing short-term patterns and rapidly evolving market
microstructures, the literature consistently notes challenges in modeling long-term dependencies and adapting to
structural changes in ﬁnancial time series. Researchers continue to explore hybrid architectures, transfer learning
approaches, and deep representation learning techniques aimed at overcoming these limitations and achieving
more stable, reliable, and interpretable long-term forecasting performance [19–21]. In this vein, new lines of
inquiry revolve around the synergy of fuzzy logic systems with other sophisticated machine learning and deep
learning models, paving a route toward more adaptive and explainable predictive frameworks.
Empirical work further consolidates the role of fuzzy logic and hybrid modeling, presenting evidence-based
improvements in forecasting accuracy and decision support capabilities. Jiang et al. [22] demonstrated the
superior performance of machine learning algorithms, particularly deep learning, in predicting stock price crash
risks by leveraging ﬁrm-speciﬁc characteristics, with a focus on proﬁtability and value versus growth features,
offering nuanced economic interpretations and highlighting signiﬁcant applications within state-owned enter-
prises and low economic policy uncertainty periods in the Chinese stock market. Chen et al. [21] proposed a
fuzzy time-series model incorporating the Fibonacci sequence to improve stock price forecasting accuracy. Using
TSMC and TAIEX stock data, the model outperformed existing fuzzy models by leveraging a ﬂuctuation-
weighted method, spread-center defuzziﬁcation, and Fibonacci-based forecasting adjustments, achieving signif-
icantly lower prediction errors. Hadavandi et al. [20] proposed a hybrid model combining genetic fuzzy systems
(GFS) and self-organizing map (SOM) neural networks for stock price forecasting. The approach uses stepwise
regression for feature selection, SOM for clustering, and GFS for rule extraction and database tuning. Applied to
stock price data from IT and airline sectors, the model achieved superior forecasting accuracy compared to
existing methods, as measured by mean absolute percentage error. Chang et al. [19] proposed a hybrid model
123
Neural Computing and Applications (2025) 37:15855–15890
15858
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 5
combining a Takagi–Sugeno fuzzy rule-based system and support vector regression (SVR) for stock trading
forecasting. The approach dynamically identiﬁes buy-sell trading thresholds using fuzzy sub-models trained on
historical technical indicators. By utilizing piecewise linear representation for segmenting stock prices and SVR
for forecasting trading signals, the model demonstrated superior proﬁtability and stability compared to traditional
regression and neural network-based methods in experiments. Kao et al. [23] introduced a hybrid stock price
forecasting model integrating nonlinear independent component analysis (NLICA) for feature extraction and SVR
for prediction. Using datasets from the Shanghai Stock Exchange Composite and Nikkei 225 indices, the
approach demonstrated improved accuracy compared to models combining principal component analysis (PCA)
or linear ICA with SVR. By extracting independent components to uncover hidden data patterns, the NLICA-
SVR method effectively enhanced prediction performance, highlighting its potential for ﬁnancial time series
forecasting. Taken together, these studies highlight the tangible beneﬁts of combining fuzzy logic principles with
advanced ML techniques, reinforcing the notion that integrated approaches can yield more robust and context-
aware forecasting tools.
In light of these diverse modeling strategies, ranging from classical econometric approaches to sophisticated
ML and fuzzy logic frameworks, it becomes clear that no single method uniformly outperforms others across all
market regimes and forecasting horizons. Each technique and combination thereof has inherent trade-offs in terms
of complexity, computational burden, and capacity to capture nonlinearity and structural changes in ﬁnancial time
series. Importantly, interpretability remains a critical factor in ﬁnancial decision making, as stakeholders must
understand the rationale behind model predictions to ensure trust, compliance with regulatory standards, and
alignment with institutional knowledge [24–27]. While deep learning architectures and hybrid models frequently
deliver superior predictive performance, they often do so at the expense of interpretability, motivating continued
research into explainable AI methods and transparent fuzzy rule extraction processes.
2.2 Deep learning-based stock price forecasting
Deep learning has revolutionized stock price forecasting by enabling end-to-end learning from raw data, elim-
inating the need for extensive feature engineering. Architectures such as recurrent neural networks (RNNs), long
short-term memory (LSTM) networks, and convolutional neural networks (CNNs) excel at capturing temporal
and spatial dependencies in ﬁnancial time series. Recent advancements include hybrid models that integrate deep
learning with attention mechanisms, reinforcement learning, and symbolic representations, enhancing their
robustness in handling non-stationarity and complex market dynamics.
Empirical investigations further emphasize the practical beneﬁts of deep learning. Jayanth Balaji et al. [28]
conducted an empirical study on the applicability of various deep learning models, including LSTM, GRU, CNN,
and ELM, for forecasting stock prices using the S&P BSE-BANKEX index data. Fourteen models were designed
to generate one-day-ahead and four-day-ahead forecasts, evaluated on metrics like RMSE, median absolute
percentage error, and directional accuracy. Results showed that GRU-based models excelled in short-term
forecasts, while ELM models performed better for longer-term horizons. In a complementary line of research, Yu
et al. [29] proposed a stock price forecasting model integrating locally linear embedding (LLE) for nonlinear
dimensionality reduction with a backpropagation (BP) neural network. The study demonstrated that the LLE
algorithm effectively reduces the dimensionality of high-dimensional, nonlinear ﬁnancial data, improving pre-
diction accuracy. Using stock data, the LLE-BP model was compared against BP, PCA-BP, and ARIMA models,
showing superior performance in terms of RMSE and MAE. This method highlights its practical applicability for
predicting stock prices in nonlinear and high-dimensional contexts.
Focusing on attribute selection and application-speciﬁc modeling, Laboissiere et al. [30] proposed a
methodology using artiﬁcial neural networks (ANNs) to forecast the maximum and minimum daily stock prices
of Brazilian power distribution companies traded on the Sao Paulo Stock Exchange. The approach combined
attribute selection based on correlation analysis with ANNs to improve prediction accuracy. Key attributes,
including historical prices, market indexes, and American dollar quotes, were used as inputs. The methodology
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15859

---

## Page 6
achieved low MAPE for maximum (below 0.9%) and minimum (below 2.1%) price predictions, demonstrating its
effectiveness in guiding investment decisions in the electricity sector. Li et al. [31] introduced a novel framework,
Chart GCN, which employs graph convolutional networks (GCNs) to analyze stock price movements by
transforming technical charts into graphs, outperforming traditional technical analysis and baseline deep learning
models with prediction accuracies of 69.26% on SZ-50 and 68.62% on CSI-300 datasets, while achieving the
highest net trading values in simulations. Long et al. [32] developed a multi-ﬁlters neural network (MFNN)
combining convolutional and recurrent units for ﬁnancial time series feature extraction, achieving higher pre-
diction accuracy compared to traditional machine learning and statistical models. Md et al. [33] proposed a novel
approach for stock price forecasting using a multilayer sequential (MLS) LSTM model. The model uses nor-
malized time-series data to capture long-term dependencies and overcome challenges like the vanishing gradient
problem. Tested on Samsung stock data, the MLS-LSTM achieved 95.9% accuracy on training data and 98.1%
accuracy on testing data, outperforming other machine learning and deep learning methods. With a mean MAPE
of 2.18%, the method demonstrated highly accurate predictions, showcasing its potential as a practical tool for
stock price forecasting. Tian et al. [34] presented a hybrid model combining a bidirectional LSTM network and
Bayesian-optimized LightGBM for stock price prediction. Utilizing Pearson’s correlation coefﬁcient for feature
selection, the model integrates LSTM for sequence learning and LightGBM for regression, with Bayesian
optimization reﬁning LightGBM parameters. Testing on ten stocks, including ES = F and YM = F, showed the
hybrid model consistently outperforming alternatives such as single LSTM and RNN models, with improved
RMSE, MAE, accuracy, and F1-score. The study demonstrates the model’s superior approximation and gener-
alization abilities for forecasting stock price ﬂuctuations.
Compared to earlier statistical and machine learning methods that often depend on handcrafted features and
explicit modeling assumptions, deep learning frameworks can learn complex patterns directly from raw data,
thereby reducing the need for extensive expert-driven variable selection. The evolution from traditional econo-
metric and ML methodologies to deep learning-based approaches marks a shift toward end-to-end learning,
adaptability, and automatic feature extraction. While deep learning has yet to achieve the full interpretability and
expert knowledge encoding capabilities seen in fuzzy logic systems and statistical learning approaches and often
involves more complex and computationally expensive training processes, continued research into explainable
deep learning, attention mechanisms, and hybrid frameworks promises to yield forecasting solutions that are both
powerful and contextually meaningful.
2.3 Symbolic dynamics in time series analysis for stock price forecasting
Symbolic dynamics, originally developed in the ﬁelds of nonlinear dynamics and chaos theory, provides a
framework for transforming continuous time series into discrete symbol sequences that preserve essential
structural and dynamical characteristics [35, 36]. This emphasis on nonlinear phenomena makes it particularly
suitable for analyzing the often nonlinear and chaotic behavior of stock price changes [1–3]. The symbolic
dynamics approach allows complex, non-stationary signals, such as stock prices, to be analyzed through patterns
of symbols rather than raw numerical values, thus offering a way to reduce noise and highlight underlying
regimes of behavior. By mapping continuous data to a ﬁnite alphabet and analyzing the resulting symbolic
sequences, researchers can detect shifts in market volatility, identify recurrent patterns, and characterize long-term
dependencies that may not be easily discernible using classical methods or direct numerical processing [35, 37].
Building upon the foundation laid by symbolic dynamics, graph-based approaches in nonlinear signal pro-
cessing further enhance our ability to characterize and interpret complex time series data [38]. By representing
symbolic sequences as networks, where symbols correspond to nodes and transitions between them form edges,
these methods translate temporal patterns into topological structures that can be examined using tools from graph
theory. Notably, these graph-based techniques have found applications across a wide range of natural and
engineered systems, including vibration analysis in mechanical structures [37], biomedical signal processing [39],
and other domains where uncovering hidden patterns is crucial. Networks generated from symbolized ﬁnancial
123
Neural Computing and Applications (2025) 37:15855–15890
15860
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 7
time series, for example, can capture transitions between volatility regimes that might indicate impending market
shifts, reveal community structures corresponding to various market states, and offer a glimpse into the resilience
and robustness of price dynamics.
Wang et al. [40] review graph-based methods for stock price prediction, focusing on graph construction and
learning. They discuss the importance of incorporating relational information and external factors, such as
economic indicators and social media, into stock market models. The study emphasizes constructing explicit and
implicit stock-to-stock relationships and explores specialized graph types like heterogeneous graphs, hyper-
graphs, and subgraphs. Additionally, feature extraction methods, including graph embeddings and neural net-
works, are highlighted. The review underscores the potential of graph learning to improve stock market
predictions by effectively modeling the complex relationships and dynamics within ﬁnancial markets. Jafari and
Haratizadeh [41] introduced GCNET, a graph-based framework for predicting stock price movements. GCNET
models the relationships among stocks using an inﬂuence network and employs graph convolutional networks
(GCNs) in a semi-supervised learning approach. It assigns initial labels to a subset of stocks using history-based
predictors and reﬁnes predictions by leveraging information from graph structures. Experiments on NASDAQ
stocks demonstrated GCNET’s superior performance compared to state-of-the-art methods, highlighting its ability
to model complex inter-stock relationships and improve prediction accuracy. Song et al. [42] introduced the
MGAR model to improve stock return ranking predictions by leveraging dynamic and multi-relational graphs. It
incorporates a price similarity relation graph alongside industry and Wiki relation graphs to capture evolving
stock interactions. Using a multi-relational graph attention mechanism and LSTM-based feature extraction,
MGAR effectively combines temporal and relational embeddings for accurate predictions. Experiments on
NASDAQ and NYSE datasets show MGAR achieves superior returns and ranking accuracy compared to
advanced methods, demonstrating its robustness in modeling complex stock relationships. Long et al. [43]
proposed the Deep Stock-trend Prediction Neural Network (DSPNN), integrating trading records and public
market data to predict stock price trends in the Chinese stock market. By leveraging knowledge graphs to identify
correlations between stocks, clustering investors to analyze trading patterns, and combining convolutional neural
networks with attention-based BiLSTMs, the model achieves enhanced accuracy for predicting short-term stock
movements and trends. Experimental results demonstrate the robustness and effectiveness of the approach, with
accuracies exceeding 70% for predicting trends over multiple trading days. Wang et al. [44] proposed a novel
model integrating knowledge graph (KG), GCN, and community detection for large-scale stock price prediction.
The authors construct a stock KG to capture explicit and implicit relationships between stocks and incorporate a
GCN-based community detection approach to reﬁne clusters of similar stocks. These clusters serve as input
features for time-series models (LSTM and GRU), enabling improved trend prediction. Evaluated on a dataset of
762 stocks from China’s A-share market (2013–2019), the model achieves superior accuracy, precision, and
stability compared to state-of-the-art methods, addressing challenges like dataset bias and prediction instability in
large-scale settings. Wu et al. [45] introduced a novel stock prediction framework leveraging complex network
theory by transforming time series data into price graphs to address challenges such as long-term dependencies
and chaotic properties in ﬁnancial time series. Using structural information extracted from graph embeddings and
node weights, their framework effectively captures both short- and long-term dependencies. Enhanced by
attention mechanisms, this approach outperformed state-of-the-art deep learning models on real-world stock
market data, demonstrating superior accuracy and proﬁtability in trading simulations.
Graph-based methods present captivating paths to improve stock price forecasting, particularly when paired
with symbolic dynamics and powerful feature extraction techniques. These techniques capture complex inter-
dependencies and changing market structures that are difﬁcult for traditional forecasting tools to handle by
converting time series data into network representations. These techniques offer a more comprehensive under-
standing of ﬁnancial markets, whether via community detection techniques, speciﬁc graph embeddings, transition
sequences, or probabilities. It is anticipated that further research combining symbolic analysis and graph theory
will lead to deeper understanding of the fundamental dynamics inﬂuencing market behavior as well as increased
predictive accuracy, which will ultimately help the ﬁnancial industry make better decisions.
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15861

---

## Page 8
Unlike traditional deep learning approaches that operate on Euclidean data, graph neural networks (GNNs) are
well suited for capturing non-Euclidean relationships, such as co-movements of stock prices, sectoral depen-
dencies, and investor behavior patterns. Cheng et al. [46] proposed a multi-modality graph neural network for
ﬁnancial time series forecasting, incorporating historical prices, media news, and knowledge graph-based rela-
tional data to model lead–lag effects between equities. Their method outperformed state-of-the-art baselines,
achieving a micro-F1-score of 0.4838, a macro-F1-score of 0.46, and a weighted-F1-score of 0.48. Xu et al. [47]
proposed a hierarchical graph neural network to classify price-limit-hitting stocks into two types, those that close
at the daily price limit (Type I) and those that do not (Type II), by modeling hierarchical market states from the
stock, industry, and market levels. Their method outperformed ALSTM, GCN, and GAT, achieving at least a
3.54% improvement in classiﬁcation accuracy, with an average return ratio increase of 18.57% in the Shanghai
Stock Exchange and 8.75% in the Shenzhen Stock Exchange. Chen et al. [48] proposed a graph convolutional
feature-based convolutional neural network (GC–CNN) for stock trend prediction, integrating both individual
stock information and market-wide relationships through an improved graph convolutional network and a Dual-
CNN. Experimental evaluations on six Chinese stocks demonstrate that the GC–CNN model outperforms several
traditional and deep learning-based methods, yielding more stable and higher returns, with annualized returns
exceeding 20% for most stocks tested. Shi et al. [49] developed an integrated GCN-LSTM model for stock price
movement prediction, incorporating four types of knowledge-based graphs (industry, region, concept, and
volatility) to extract stock embeddings via GCN before passing them into an LSTM for temporal modeling. Their
experiments on major Chinese stock indexes demonstrated the effectiveness of the proposed approach, achieving
a peak accuracy of 57.81%. Yin et al. [50] developed a high-frequency trading system using graph attention
LSTM (GALSTM) to model stock correlations and predict prices. Their approach achieved 44.71% annualized
returns by integrating a multi-dimensional Hawkes process with an attention-based LSTM for dynamic portfolio
management.
While GNN-based methods show signiﬁcant promise in capturing structural dependencies in ﬁnancial markets,
several challenges remain in fully leveraging their potential for stock price forecasting. One limitation is the need
for well-deﬁned and meaningful graph structures, as ﬁnancial relationships are often dynamic, latent, and non-
stationary. However, adjacency-based approaches offer a computationally efﬁcient way to integrate graph
structures into deep learning models while mitigating some of these challenges. By representing stock rela-
tionships through sparse adjacency matrices, these methods allow for efﬁcient message passing and structured
feature extraction without requiring the full graph to be explicitly stored in memory. Techniques such as
approximate nearest neighbor graphs, thresholded correlation networks, and knowledge-driven adjacency matrix
construction help deﬁne relevant connections while avoiding excessive computational overhead.
Adjacency matrix-based relation extraction approaches have utilized several studies highlighting the impor-
tance of network analysis in stock market data. Khoojinea and Han [51] proposed a Stock Price Network
Autoregressive Model (SPNAR) to analyze the behavior of the Chinese stock market during the 2015–2016
turbulence period by constructing an adjacency matrix-based ﬁnancial network. Their approach deﬁned stock
relationships using an information-theoretic distance threshold to build sparse, interpretable adjacency matrices,
which allowed for efﬁcient estimation of market dependencies while maintaining computational feasibility
compared to traditional vector autoregressive models. Zhao et al. [52] utilized a temporal network framework to
analyze stock market evolution, emphasizing the role of adjacency matrices in capturing the dynamic depen-
dencies among stocks. By constructing a supra-adjacency matrix that integrated time-evolving correlation-based
networks, their approach preserved crucial temporal structures, allowing for improved portfolio selection and risk
management, particularly through the identiﬁcation of peripheral stocks.
In summary, symbolic dynamics and graph-based methods enable the extraction of structured patterns from
ﬁnancial time series, enhancing interpretability and predictive accuracy. Adjacency matrix-based techniques
further optimize these approaches by efﬁciently capturing dynamic dependencies, facilitating scalable and robust
ﬁnancial modeling.
123
Neural Computing and Applications (2025) 37:15855–15890
15862
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 9
3 Symbolic dynamics for nonlinear financial time series analysis
Symbolic dynamics offers a powerful framework for analyzing complex time series by converting continuous-
valued data into sequences of discrete symbols, thereby emphasizing qualitative patterns rather than precise
numerical values. This transformation helps researchers capture essential structural and dynamical characteristics
hidden in the data, making it especially suitable for studying inherently volatile and nonlinear domains like
ﬁnancial markets.
In the subsections that follow, the theoretical underpinnings of symbolic dynamics and their relevance to
ﬁnancial time series are ﬁrst discussed, illustrating how these concepts can uncover meaningful patterns in non-
stationary and chaotic market environments. The procedures for normalizing and discretizing continuous price
signals into symbolic states are then described, with particular emphasis on how the choice of alphabet size and
discretization methodology can inﬂuence both the resolution and transparency of the extracted patterns. Finally,
the construction and analysis of state transition matrices from these symbolic sequences are introduced,
demonstrating how graph-theoretic measures can be applied to represent and scrutinize the resulting networks,
and utilized as inputs for deep learning models.
3.1 Exploration of temporal trends in stock price data
Financial time series, such as stock prices and trading volumes, are inherently noisy and exhibit highly non-
stationary, nonlinear behavior, making traditional analytical methods challenging. Such time series data are
characterized by persistent trends, cyclical ﬂuctuations, and sudden regime shifts, often driven by external factors
such as macroeconomic events, policy changes, or market sentiment.
Understanding the dynamics of stock price movements requires the decomposition of their behavior into clear,
transparent temporal components. Trends, which signify sustained upward or downward movements, often reﬂect
the long-term growth trajectories or structural declines of a company or sector. Cycles, on the other hand, capture
recurring, periodic patterns over a deﬁned period, such as quarterly earnings announcements or seasonal ﬂuc-
tuations. The presence of abrupt changes, such as price jumps or crashes, is typically attributed to unforeseen,
high-impact shocks like geopolitical crises or earnings surprises.
One of the key challenges in analyzing ﬁnancial data is distinguishing between meaningful trends and random
ﬂuctuations. Financial time series are often modeled as a combination of deterministic components and stochastic
noise. The stochastic noise arises from factors such as market microstructure effects, investor sentiment, and high-
frequency trading, which introduce short-term volatility and transient anomalies that may obscure the underlying
patterns.
The dataset used in this study, sourced from Yahoo Finance, encompasses a diverse set of ﬁnancial assets
spanning multiple sectors and types, as summarized in Table 1. By drawing on publicly available historical data,
these time series reﬂect real-market conditions and incorporate complexities inherent to ﬁnancial environments.
The primary focus is on corporate stocks, with target variables derived from the Close prices of assets in the
Technology (e.g., AAPL, MSFT, NVDA), Healthcare (e.g., PFE, JNJ), Energy (e.g., XOM), Consumer Dis-
cretionary (e.g., AMZN), and Airlines (e.g., UAL) sectors. These target variables correspond to prediction
horizons (e.g., 1-day, 10-day, 100-day) and are calculated as the percentage changes in future Close values
relative to their current levels.
In addition to the Close prices, other key features used in the analysis include Volume (to capture trading
activity) and High-Low Difference (to reﬂect daily price volatility). The dataset also incorporates data from non-
target assets, including ﬁnancial stocks (e.g., JPM, GS), commodities (e.g., GC = F for gold, CL = F for crude
oil), and the EUR/USD exchange rate. These non-target assets provide additional contextual information for
capturing broader market trends, improving the predictive power of the models.
Figure 1 illustrates the temporal evolution of stock prices across multiple corporate assets, covering a multi-
year period and highlighting the segmentation of the dataset into training and testing sets, with a 50–50 split. In
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15863

---

## Page 10
this study, the chosen timeframe ensures that the training phase captures a historically rich and relatively
stable market environment, while the test phase encompasses a variety of emerging trends and increased
volatility, including the aftermath of global economic disruptions. Unlike traditional machine learning tasks
where cross-validation is a widely accepted evaluation technique, its direct applicability to stock price forecasting
is limited due to the strong temporal dependencies and the non-stationary nature of ﬁnancial markets.
Standard k-fold cross-validation, commonly used in machine learning, assumes that data points are inde-
pendent and identically distributed, an assumption that is fundamentally violated in time series forecasting. When
applied to ﬁnancial time series, k-fold cross-validation randomly partitions the dataset into folds, training on some
subsets while validating on others [53, 54]. This introduces an unrealistic setting where later periods in time may
Table 1 Financial Assets
Utilized in this Study
Asset
Sector/Type
Used as Target
AAPL
Technology
Yes
MSFT
Technology
Yes
NVDA
Technology
Yes
GOOGL
Technology
Yes
AMZN
Consumer Discretionary
Yes
IBM
Technology
Yes
XOM
Energy
Yes
PFE
Healthcare
Yes
JNJ
Healthcare
Yes
UAL
Airlines
Yes
JPM
Financials
No
GS
Financials
No
GC = F
Commodity (Precious Metal)
No
SI = F
Commodity (Precious Metal)
No
HG = F
Commodity (Industrial Metal)
No
CL = F
Commodity (Energy)
No
NG = F
Commodity (Energy)
No
ZW = F
Commodity (Agriculture)
No
EUR/USD
Currency
No
Fig. 1 Temporal Evolution of Close Values for Selected Stocks with Train and Test Splits Highlighted
123
Neural Computing and Applications (2025) 37:15855–15890
15864
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 11
appear in the training data before earlier periods, leading to data leakage and inﬂated performance metrics that do
not generalize to real-world forecasting tasks.
An alternative approach, rolling-origin cross-validation (also known as expanding window validation),
maintains temporal consistency by incrementally expanding the training set while progressively validating on
subsequent periods [18]. However, this method often results in models trained on earlier historical data, which
may not fully capture the evolving market structures observed in the latter portions of the dataset. Moreover,
rolling-origin validation tends to overweight earlier periods, which may not be representative of the structural
changes and regime shifts occurring in ﬁnancial markets.
Another common approach, sliding window validation, mitigates this issue by maintaining a ﬁxed-length
training window that shifts forward over time [18]. While this ensures that the model is continuously trained on
the most recent data, it discards older information entirely, potentially losing valuable long-term dependencies
crucial for robust market forecasting. Additionally, models trained using sliding window validation may struggle
with abrupt market shifts, as the limited lookback period constrains their ability to recognize long-range trends.
To address these challenges, a simple but effective solution is the 50–50 temporal split adopted in this study.
This division ensures that the model is trained on the initial half of the data, capturing historical trends and
patterns, while the remaining half serves as an out-of-sample test set to evaluate predictive performance. By
deliberately withholding more recent data until the testing stage, realistic forecasting conditions are simulated in
which future market states are inherently uncertain and must be extrapolated from previously observed behaviors.
This temporally consistent partitioning strategy enhances the robustness of performance evaluation, ensuring that
the model is assessed under conditions that reﬂect its practical deployment in live trading scenarios. Furthermore,
the equal division of the dataset avoids potential biases that arise when the training period is disproportionately
larger or smaller than the test period, ensuring a balanced assessment of predictive stability across different
market regimes.
The training phase, marked by the light blue region, provides the model with sufﬁcient data to learn long-term
sectoral trends, inter-market dependencies, and the evolution of cross-asset correlations. The testing phase,
represented by the green region, covers more recent data and includes signiﬁcant market ﬂuctuations, such as the
sharp price movements observed in the post-2020 period. This phase allows for an evaluation of the model’s
adaptability to regime shifts, external shocks, and structural breaks in ﬁnancial markets. This period encapsulates
several distinct market regimes, from initial recovery phases to periods of heightened investor uncertainty,
spanning high-volatility events, macroeconomic disruptions, and changes in monetary policy frameworks,
reﬂecting the shifting risk proﬁles and sentiment-driven behaviors characteristic of modern ﬁnancial markets. By
structuring the dataset to include both relatively stable and highly volatile conditions, the robustness of the model
in varying market environments can be systematically assessed.
The Close values shown for each asset reﬂect the diversity of behaviors across sectors. Technology stocks,
such as AAPL, MSFT, and NVDA, exhibit steady growth over time, punctuated by sharp upward trends, often
synchronized with major product releases, breakthroughs in semiconductor technology, and shifts in investor
sentiment toward high-growth assets. These price movements align with broader macroeconomic tailwinds,
including increased digitalization and expansionary ﬁscal policies favoring innovation-driven sectors. Healthcare
stocks, like PFE and JNJ, maintain more stable trajectories, with occasional volatility linked to industry-speciﬁc
developments such as regulatory approvals, patent expirations, mergers and acquisitions, or global health crises
that reshape demand for pharmaceutical and biotech products. Energy sector stocks, such as XOM, are inﬂuenced
by commodity price ﬂuctuations, which are, in turn, driven by geopolitical tensions, supply chain disruptions, and
changes in global demand for crude oil and natural gas. These ﬂuctuations introduce periodic boom-and-bust
cycles, with price reversals occurring in response to macroeconomic indicators such as inﬂationary pressures and
shifts in energy policy. These observed patterns reinforce that stock price dynamics are not uniform but strongly
inﬂuenced by the intrinsic characteristics and external pressures unique to each sector. The heterogeneity of these
patterns underscores the necessity of a modeling approach that captures both short-term dependencies and long-
term structural shifts, making sector-aware forecasting frameworks particularly valuable.
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15865

---

## Page 12
To further ensure that the dataset division captures a realistic market representation, the selection of the training
and testing periods was carefully designed to encompass diverse economic conditions. The training phase spans a
period characterized by relative market stability, allowing the model to learn fundamental sectoral trends, cross-
asset dependencies, and macroeconomic inﬂuences that deﬁne long-term ﬁnancial dynamics. Meanwhile, the
testing phase is deliberately structured to include time frames of heightened market turbulence, such as the
COVID-19 pandemic and post-pandemic recovery, ensuring that the model’s predictive capability is evaluated
under extreme volatility and regime shifts.
This diverse economic landscape necessitates a modeling approach that not only learns from historical patterns
but also accounts for the broader market context in which ﬁnancial assets operate. To comprehensively capture
the interconnected nature of ﬁnancial markets, the modeling framework does not solely rely on the historical
behavior of each individual target asset in isolation. Instead, for each target asset, features derived from all other
target assets, as well as relevant non-target assets, are incorporated into the predictive process. This design choice
acknowledges the interdependence of ﬁnancial instruments, where price movements and volatility in one sector
may propagate across others due to macroeconomic factors, investor sentiment shifts, or structural market
relationships. By integrating sector-wide information, the model leverages cross-asset correlations to reﬁne its
forecasts, improving robustness against unpredictable market ﬂuctuations. Additionally, the inclusion of non-
target assets such as ﬁnancial stocks and commodities enhances contextual awareness by incorporating signals
that reﬂect broader market conditions.
3.2 Symbolization and state transition graph constructing methodology
Symbolization, a cornerstone of symbolic dynamics, transforms continuous-valued time series data into
sequences of discrete symbols, thereby highlighting dynamic patterns and reducing complexity to a manageable,
interpretable form. The implementation analyzes segments of length 100 timesteps, considering each window
from time t down to t  99, forwarding the sectioning window by 1 timestep at each iteration. This approach
ensures that each symbolic representation and subsequent analysis is based on a consistent temporal context of
100 consecutive observations. By maintaining a ﬁxed window size, the framework ensures stationarity within
local segments while preserving the sequential dependencies necessary for capturing market dynamics.
The analyze begins with the scaling the all time series ﬁrst, then normalization of the windowed time series
performed, ensuring scale invariance and facilitating uniform analysis across multiple datasets. This is achieved
by mapping the series xt to the interval [0,1] using:
xnormalized
t
¼
xt  minðxÞ
max x
ð Þ  minðxÞ
ð1Þ
Following normalization, the signal is partitioned into a ﬁnite number of amplitude states, deﬁned by an
alphabet of size n. These amplitude states
a0; a1; . . .; an1
f
g are determined by dividing the normalized range
[0,1] into equal intervals for n ¼ 10. This symbolic representation retains critical information about the signal’s
magnitude while discarding ﬁner numerical details. The discretization ensures a compact representation of the
signal while balancing the trade-off between resolution and computational efﬁciency. Let
a0; a1; . . .; an1
f
g
represent a ﬁnite alphabet of amplitude states, where each state corresponds to a uniform partitioning of the
interval [0,1]:
ai ¼
i
n ; i þ 1
n


; i ¼ 0,1; . . .; n  1
ð2Þ
For each xnorm
t
, the amplitude symbol is assigned as:
123
Neural Computing and Applications (2025) 37:15855–15890
15866
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 13
At ¼ ai if xnorm
t
2 ai
ð3Þ
To capture directional changes, a trend state, Tt, is assigned based on the ﬁrst-order difference:
Dxt ¼ xt  xt1
ð4Þ
The trend state, slope, is then categorized into three discrete states:
Tt ¼
d;
if Dxt \0 ðDecreasingÞ
s;
if Dxt ¼ 0 ðstableÞ
i;
if Dxt [ 0 ðIncreasingÞ
8
<
:
ð5Þ
The combination of amplitude and trend states allows for the characterization of not only magnitude-based
ﬂuctuations but also the directional evolution of the ﬁnancial time series, providing a richer representation of the
underlying dynamics. By combining the amplitude and trend states, each timestep is assigned a composite
symbolic representation:
St ¼ ðAt; TtÞ
ð6Þ
where St results in a sequence of symbolic states that describe both magnitude and directional dynamics.
Given the sequence of symbolic states St
f gN
t¼1, the transition matrix T 2 Rnn is constructed that quantiﬁes the
transitions between symbolic states and is deﬁned as for m ¼ n  3 total number of unique symbolic states
(amplitude-slope combinations). Each element in the matrix is computed as:
Ti;j ¼
PN1
t¼1 1ðSt ¼ i; Stþ1 ¼ jÞ
PN1
t¼1 1ðSt ¼ iÞ
ð7Þ
where 1ðÞ is an indicator function that returns 1 if the condition is met and 0 otherwise. This ensures that:
X
m
j¼1
Ti;j ¼ 1; 8i
ð8Þ
conﬁrming that each row of T represents a valid probability distribution.
The state transition matrix can be visualized as a graph, G ¼ ðV; EÞ, where V consists of m nodes, each
corresponding to a unique state, and E consists of directed edges weighted by the transition counts for this
purpose. This approach reveals temporal structures and facilitates graph-theoretic analysis of complexity and
cyclic behavior. Figure 2 illustrates this using Apple Inc.’s stock price data: Part (a) shows the normalized time
series with symbolic states representing discretized amplitude and trends, while part (b) depicts the state transition
graph, with edge weights showing number of transitions between those nodes.
The transition matrix is mathematically analogous to a Markov transition matrix, capturing ﬁrst-order
dependencies in the symbolic sequence. This methodology facilitates the comparison of time series across assets
and timeframes, providing a robust framework for understanding the qualitative dynamics of ﬁnancial markets.
By encoding both amplitude and directional information, the symbolic representation emphasizes signiﬁcant
qualitative features while reducing noise and preserving essential characteristics of the signal.
To rigorously assess whether the transition matrices satisfy the Markov property, several statistical tests
grounded in matrix analysis, information theory, and statistical inference were employed. The Markov property
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15867

---

## Page 14
states that a stochastic process Xt is Markovian if the probability of transitioning to the next state depends only on
the present state, and not on the sequence of past states:
P Xtþ1
ð
jXt; Xt1; . . .; X0Þ ¼ P Xtþ1
ð
jXtÞ
ð9Þ
To examine this assumption, the empirical second-step transition matrix, Pð2Þ
empirical, is computed and compared
to the theoretical second-step transition matrix derived from the Chapman–Kolmogorov equation [55–57]:
Fig. 2 a Symbolic Dynamics Visualization of AAPL Close Values for the First 100 Timesteps, Highlighting Assigned
States; b Corresponding State Transition Graph Representing the Temporal Dynamics of Symbolic States
123
Neural Computing and Applications (2025) 37:15855–15890
15868
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 15
Pð2Þ
theoretical ¼ P1  P1 ¼ P2
ð10Þ
where P1 is the one-step transition matrix. The following statistical measures were used to evaluate the dis-
crepancy between these matrices:
•
Frobenius Norm Difference: The Frobenius norm measures the Euclidean difference between the empirical
and theoretical second-step transition matrices [58, 59]:
dF ¼ kPð2Þ
empirical  Pð2Þ
theoreticalkF
ð11Þ
where the Frobenius norm is deﬁned as:
kAkF ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
X
i;j
aij

2
s
ð12Þ
A low Frobenius norm indicates that the observed transition structure closely follows the Markovian
assumption.
•
Kullback–Leibler (KL) Divergence: The KL divergence quantiﬁes how much information is lost when using
the theoretical transition matrix instead of the empirical one [60, 61]:
DKLðP 2
ð Þ
empiricalj P 2
ð Þ
theoretical


¼
X
i;j
P 2
ð Þ
empirical i; j
ð
Þlog
P 2
ð Þ
empiricalði; jÞ
P 2
ð Þ
theoreticalði; jÞ
ð13Þ
A low KL divergence suggests that the empirical transition probabilities follow the theoretical Markovian
expectations.
•
Pearson Correlation Coefﬁcient: The Pearson correlation coefﬁcient measures the linear relationship between
the ﬂattened empirical and theoretical transition matrices [62, 63]:
q P 2
ð Þ
empirical; P 2
ð Þ
theoretical


¼
PðXi  XÞðYi  YÞ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
P ðXi  XÞ
2
q
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
P ðYi  YÞ
2
q
ð14Þ
where X and Y are vectorized forms of the empirical and theoretical matrices, respectively. A high correlation
indicates strong agreement between observed and expected Markovian transitions.
•
Likelihood Ratio Test (LRT): To formally test the ﬁrst-order Markov assumption against a second-order
model, which can be compared in terms of the log-likelihoods of the ﬁrst-order transition model and the
second-order empirical transition model [64–66]:
k ¼ 2 logL P 1
ð Þ


 logL P 2
ð Þ




ð15Þ
where LðPÞ is the likelihood of observing the given transitions under the respective model. Under the null
hypothesis of ﬁrst-order Markovianity, k follows a chi-square distribution [67, 68]:
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15869

---

## Page 16
k  x2ðkÞ
ð16Þ
with k degrees of freedom determined by the number of free parameters in the transition matrices. A statistically
signiﬁcant likelihood ratio suggests that higher-order dependencies may be present.
These tests collectively provide a rigorous mathematical framework to assess the validity of the ﬁrst-order
Markov assumption in the ﬁnancial time series. This multi-faceted evaluation captures local deviations in tran-
sition probabilities and broader structural inconsistencies in state dynamics by leveraging complementary sta-
tistical and information-theoretic measures. Signiﬁcant deviations from the expected Markov structure may
indicate hidden dependencies, long-range correlations, or structural non-stationarities, suggesting that additional
higher-order memory effects or regime shifts inﬂuence market behavior. Such deviations could emerge from
latent exogenous factors, behavioral biases, or autocorrelated volatility patterns that are not fully captured within
the ﬁrst-order Markovian framework.
Figure 3 presents the cumulative distributions of four Markovianity test metrics—Frobenius norm difference,
KL divergence, Pearson correlation, and likelihood ratio—comparing the train and test periods to assess the
stability of ﬁrst-order dependencies in transition matrices. These results provide empirical evidence on whether
transition structures remain consistent over time or undergo structural breaks. The ﬁndings from these tests
contribute to a deeper understanding of how well symbolic-state-based models capture the underlying proba-
bilistic structure of ﬁnancial markets.
Fig. 3 Cumulative Distribution of Markovianity Tests; a Frobenius Norm Difference; b KL Divergence; c Pearson
Correlation; and d Likelihood Ratio
123
Neural Computing and Applications (2025) 37:15855–15890
15870
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 17
The cumulative distributions of the Markovianity test results provide insights into the validity of the ﬁrst-order
Markov assumption across training and test periods. The Frobenius norm difference distribution is around 1.5,
indicating a systematic deviation between empirical and theoretical second-step transition matrices. Both periods
exhibit similar distributions, suggesting that the transition structure remains relatively stable, with no abrupt shifts
in dependency patterns. Minor variations between the train and test periods suggest some non-stationarity but do
not indicate a fundamental change in the underlying Markovian behavior.
The KL divergence distributions exhibit a sharp peak near zero, with a long-tailed spread. This indicates that
while many transition matrices remain close to their theoretical counterparts, some cases deviate, especially in the
test period. The extended tail in the test period suggests increased uncertainty or structural shifts in the temporal
dependencies of the ﬁnancial time series. This ﬁnding implies that while ﬁrst-order dependencies are dominant,
occasional deviations from strict Markovianity occur.
The Pearson correlation values are predominantly near 0.85–1.0, reﬂecting a strong agreement between
empirical and theoretical transition matrices. This supports the assumption that the ﬁrst-order Markov model
captures short-term dependencies well in most cases. However, the slight spread in the test period suggests
increased variability in temporal dynamics, indicating that certain dataset segments may exhibit higher-order
dependencies. Despite this, the overall consistency between periods supports the robustness of the Markov-based
modeling approach.
The likelihood ratio test results are heavily centered around zero, indicating that the ﬁrst-order Markov
assumption is often not ﬁrmly rejected. The similarity between train and test period distributions suggests that
dependencies between states remain stable over time, although minor ﬂuctuations may signal evolving market
conditions. These ﬁndings provide evidence that symbolic dynamics-based transition matrices effectively capture
short-term dependencies.
Although ﬁnancial time series are modeled as transition graphs and corresponding transition matrices, their
representation within neural network architectures requires a structured temporal encoding. To achieve this,
transition matrices are stacked with a temporal dimension, where each sample consists of a sequence of ﬁve
consecutive matrices, incorporating the previous four matrices as observations for the current step. This approach
allows the network to capture temporal dependencies beyond a single-step transition, effectively embedding
historical dynamics into the learning process. By structuring the input in this way, the neural network can exploit
both short-term Markovian transitions and potential deviations from strict ﬁrst-order assumptions.
4 Convolutional recurrent neural network and forecasting strategy
Forecasting time series data, particularly in the context of ﬁnancial markets, requires a methodology that can
handle complex temporal dependencies, non-stationary, and multivariate interactions. This section details the
end-to-end pipeline, highlighting how symbolic transformations, tensor construction, and hybrid neural archi-
tectures are combined to provide a robust and scalable forecasting strategy. Figure 4 illustrates the complete
pipeline for transforming time series data into structured inputs for a CRNN and the corresponding architecture
used for predictive modeling. This pipeline encompasses four key stages: symbolic dynamics-based prepro-
cessing, transition matrix calculation and normalization, temporal stacking into tensors, and the design of a neural
network that integrates convolutional and recurrent layers for robust time series forecasting.
4.1 Construction temporally stacked transition matrices as tensors
To extend the temporal dynamics captured by state transition matrices, temporally stacked tensors are constructed
that aggregate sequential information over multiple time windows. This approach enables recurrent neural net-
work (RNN)-based models to process transition matrices in a temporally structured format, capturing depen-
dencies not just within individual windows but also across successive windows. Given that transition matrices T
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15871

---

## Page 18
are computed for each timestep t over the interval [t, t-99], the input tensors incorporate transition matrices from
multiple consecutive steps, speciﬁcally t  4tot for each transition matrix in timestep t, forming a temporally
structured sequence. This approach enables recurrent neural network (RNN)-based models to process transition
matrices in a time-aware manner, capturing dependencies not just within individual observation windows but also
across successive transitions.
Each stacked tensor Xt
tensor is thus deﬁned as:
Xt
tensor ¼ ½Tt4; Tt3; Tt2; Tt1; Tt
ð17Þ
The entire tensor Xt
tensor encapsulates the sequential evolution of transition probabilities across recent market
states, which have the shape of:
Xt
tensor 2 R 5;m;m;f
ð
Þ
ð18Þ
where
•
5 is the temporal dimension, representing the stacked tensors,
•
m is the number of symbolic states (e.g., 30 symbolic states in the discretization process), and
•
f is the number of time series features utilized, which is 57 coming from 19 assets.
The temporally stacked tensor encodes both short-term and long-term dynamics, making it an ideal input for
RNN-based models, such as long short-term memory (LSTM) neural networks [54, 69, 70]. The inclusion of
multiple temporal windows enables these models to leverage sequential patterns across time, enhancing their
ability to predict future dynamics. Speciﬁcally, the CRNN architecture utilizes convolutional layers to capture
spatial correlations within the transition matrices, followed by recurrent layers that process the temporal
Fig. 4 Overview of Input Tensor Generation and Convolutional Recurrent Neural Network Architecture
123
Neural Computing and Applications (2025) 37:15855–15890
15872
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 19
dependencies encoded in the stacked tensor. This hybrid architecture ensures that both the intra-window and
inter-window patterns are effectively captured, providing a comprehensive understanding of the temporal
dynamics underlying the time series.
Furthermore, the temporal stacking framework aligns with the concept of capturing hierarchical temporal
structures, where shorter temporal windows capture high-frequency transitions and longer sequences allow the
model to learn low-frequency trends. This hierarchical processing facilitates robust forecasting, particularly in
scenarios where ﬁnancial time series exhibit complex, multi-scale temporal dependencies.
4.2 Model architecture and the role of convolutional layers
The proposed CRNN architecture is designed to effectively process temporally stacked tensors that encode
symbolic-state transitions across consecutive time windows. In our approach, each temporal segment is repre-
sented by a series of transition matrices that reﬂect evolving state dynamics over time, providing a structured view
of the underlying temporal patterns. Each tensor slice consists of 5 transition matrices, corresponding to con-
secutive segments of the time series, ensuring that the network receives a coherent block of historical information
at each step. A notable characteristic of these transition matrices is their inherent sparsity, as many transitions
between states may not occur frequently, leading to zero or near-zero entries. This sparsity presents a unique
computational and modeling challenge that necessitates specialized preprocessing layers.
To address this, convolutional layers are applied to each transition matrix individually within the temporally
stacked tensor. By processing each matrix separately, the network can isolate local spatial correlations without
interference from adjacent matrices, ultimately reducing the risk of blending together unrelated patterns. This
independent processing ensures that the spatial correlations within each matrix are preserved and allows the
network to capture patterns speciﬁc to individual temporal windows. The convolutional blocks serve multiple
purposes: They extract local spatial patterns from the transition matrices, reduce the impact of noise due to
sparsity, and identify meaningful state transitions that contribute to the temporal dynamics. Each convolutional
block is composed of Conv2D layers, followed by max-pooling layers to down sample and highlight the most
prominent spatial features. By accentuating key structural dependencies and suppressing superﬂuous detail, these
operations help create a more compact and informative representation of the data, laying a strong foundation for
subsequent temporal modeling.
The processed features are subsequently passed to recurrent layers, speciﬁcally LSTM units, which are
designed to model the temporal dependencies across the stacked windows [34, 54, 70, 71]. LSTMs excel at
retaining and updating information over extended sequences, making them well suited for capturing the evolution
of state transitions as the time series unfolds. This sequential modeling allows the network to capture both short-
term and long-term dynamics in the time series, leveraging the rich spatial features extracted by the convolutional
layers. In essence, the CRNN design combines the complementary strengths of convolutional and recurrent
architectures, and convolutions handle the spatial intricacies of the transition matrices, while LSTMs contextu-
alize these ﬁndings within a temporal narrative, resulting in a more robust and adaptive forecasting framework.
4.3 Target variables and final forecast predictions
In this modeling framework, the target variables represent the ratio of change between the current and future
values of the Close prices, normalized to fall within the range [- 1,1]. This transformation ensures numerical
stability during training and aligns the target variable with the output activation function of the neural network.
The ratio of change for each asset is computed as:
yt ¼ Closetþh  Closet
Closet
ð19Þ
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15873

---

## Page 20
where yt is the target variable at time t, Closet is the current Close price, and Closetþh is the Close price at a future
horizon h. This representation captures the relative change in the asset price over the prediction horizon, enabling
the model to focus on the proportional dynamics rather than absolute values.
During the inference phase, the model outputs predictions for yt, the ratio of change, based on the processed
temporal and spatial features from the input tensors. To derive the ﬁnal forecasted Close price, these ratio
predictions are transformed back into the original scale of the time series using the current Close price. The
forecasted value is calculated as:
d
Closetþh ¼ Closet  ð1 þ bytÞ
ð20Þ
where
d
Closetþh is the forecasted future Close price and bytÞ is the model’s predicted ratio of change.
This formulation ensures that the model predictions remain consistent with the original scale of the ﬁnancial
time series while preserving the coherence of the ratio predictions. By expressing the target variable as a ratio, the
model can generalize across assets with different price ranges. This standardization ensures that the loss function
treats all assets equally, avoiding bias toward high-value stocks. Ratio-based targets capture relative changes,
making the model more robust to non-stationary behavior in the time series, such as price trends or volatility
shifts.
5 Results and discussion
This section examines the outcomes and implications of the forecasting strategy, evaluating its effectiveness
across three different forecast horizons. The forecasting results for 1-day, 10-day, and 100-day prediction
horizons demonstrate the model’s ability to adapt to varying temporal dynamics across different market condi-
tions. As illustrated in Figs. 5, 6, 7, the predictions are analyzed within three distinct time intervals: pre-COVID,
COVID, and post-COVID. Each interval exhibits unique patterns and levels of volatility and distinct market
dynamics that inﬂuence investment strategies and risk assessment. The pre-COVID period is characterized by
stable economic conditions, gradual trends, and predictable market behavior, providing a relatively low-risk
environment where the model achieves high forecasting accuracy. The COVID period, in contrast, reﬂects
extreme volatility and rapid shifts driven by global uncertainty, making it a highly challenging period for accurate
predictions. This interval is crucial for robust forecasting models to support decisions in crisis scenarios, where
market shocks demand rapid adaptations. Finally, the post-COVID period signiﬁes a recovery phase with
emerging stability, allowing for more reliable forecasting and strategic planning.
The model’s performance is quantitatively assessed using two widely adopted metrics: mean absolute error
(MAE) and mean squared error (MSE). These metrics provide complementary perspectives on the accuracy of
predictions. Mathematically, MAE is deﬁned as:
MAE ¼ 1
n
X
n
i¼1
yi  byi
j
j
ð21Þ
where yi represents the actual value, byi is the predicted value, and n is the total number of predictions. MAE
captures the average magnitude of prediction errors, treating all deviations equally regardless of their direction,
making it intuitive for understanding the typical size of errors.
On the other hand, MSE is deﬁned as:
123
Neural Computing and Applications (2025) 37:15855–15890
15874
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 21
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15875

---

## Page 22
MSE ¼ 1
n
X
n
i¼1
yi  byi
ð
Þ2
ð22Þ
MSE takes the squared differences between actual and predicted values. By squaring the errors, MSE penalizes
larger deviations more heavily than smaller ones, providing sensitivity to signiﬁcant outliers in the predictions.
For shorter prediction horizons, such as the 1-day forecast, the model consistently achieves lower values for
both MAE and MSE, reﬂecting a high degree of accuracy in short-term predictions. Notably, during the
stable pre-COVID period, the reduced market volatility results in a lower variance of prediction errors, enabling
the model to perform particularly well. This stability minimizes the inﬂuence of noise and confounding factors,
leading to more reliable and precise predictions during this interval. The explicit focus on short-term dynamics
and the low noise levels in pre-COVID data further enhance the performance metrics in this context.
During the COVID interval, characterized by heightened volatility and abrupt market ﬂuctuations, the model’s
predictive performance becomes more asset- and sector-dependent. Technology stocks, such as AAPL and
MSFT, exhibit higher errors due to the pronounced price jumps and sharp trends. In contrast, healthcare stocks
like PFE and JNJ maintain relatively stable performance, highlighting sector-speciﬁc resilience even amid global
uncertainty. Post-COVID, the model demonstrates improved predictive capability for most stocks, capturing
recovery trends and sector-speciﬁc growth patterns, particularly for energy stocks like XOM, which beneﬁt from
cyclic rebounds in commodity markets.
For longer horizons (e.g., 10-day and 100-day predictions), errors understandably rise as uncertainty com-
pounds over time. However, the temporal stacking of transition matrices, coupled with the CRNN architecture,
allows the model to retain meaningful sequential information, yielding competitive performance even during
challenging periods. These results emphasize the importance of integrating symbolic dynamics and deep recurrent
structures to capture the intricate, long-range dependencies inherent in ﬁnancial time series. Longer-term horizons
offer perspectives on more general market trends at the expense of greater uncertainty, while short-term horizons
provide higher precision but may lack broader strategic insights.
The quantitative analysis of the forecasting results across pre-COVID, COVID, and post-COVID intervals
reveals signiﬁcant variations inﬂuenced by market conditions and prediction horizons. During the pre-COVID
period, marked by relatively stable market dynamics, the model exhibited superior accuracy, achieving the lowest
errors across all horizons. For instance, AAPL’s 1-day horizon MSE and MAE were 0.54 and 0.52, respectively,
while NVDA showed exceptional precision with an MSE of 0.01 and MAE of 0.08 for the same horizon.
However, as the prediction horizon extended to 10 days and 100 days, the errors naturally increased due to the
compounding uncertainties, though the pre-COVID errors remained signiﬁcantly lower than in the volatile
COVID period.
The COVID interval, characterized by heightened volatility and market disruptions, posed considerable
challenges for the model. For instance, MSFT’s MSE rose sharply to 26.24 for the 1-day horizon and 189.01 for
the 10-day horizon, reﬂecting the difﬁculty in capturing abrupt market shifts. Longer horizons, such as the
100-day forecast, showed even more pronounced errors, with AMZN’s MSE reaching 1489.84. Similarly,
GOOGL experienced a surge in MSE from 4.87 in the pre-COVID period to 36.00 during COVID for the 10-day
horizon. The increased errors highlight the need for robust modeling approaches to adapt to extreme market
conditions.
In the post-COVID phase, while market conditions began stabilizing, residual volatility remained, leading to
moderate improvements in forecasting accuracy compared to the COVID interval. For instance, XOM’s MSE for
the 1-day horizon reduced from 2.65 during COVID to 3.02 post-COVID, and AAPL’s 100-day horizon MSE
dropped from 642.19 during COVID to 604.76 post-COVID. However, the errors remained higher than in the
bFig. 5 Forecast Results for 1-Day Prediction Horizon
123
Neural Computing and Applications (2025) 37:15855–15890
15876
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 23
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15877

---

## Page 24
pre-COVID period, reﬂecting the ongoing challenges in modeling long-term forecasts in dynamic post-pandemic
markets.
Table 2 presents forecasting metrics (MSE and MAE) for a range of assets—AAPL, MSFT, NVDA, GOOGL,
AMZN, IBM, XOM, PFE, JNJ, and UAL—across three forecast horizons (1-day, 10-day, and 100-day) and three
market regimes (pre-COVID, COVID, and post-COVID).
Figure 8 quantitatively evaluates the percentage changes in MSE and MAE across three prediction horizons (1
day, 10 days, and 100 days) for multiple assets during the transitions between pre-COVID, COVID, and post-
COVID periods. As depicted in the ﬁgure, medium-term (10 days) and long-term (100 days) horizons demon-
strate a persistent pattern of volatility; however, the percentage increases in MSE generally decline for most
assets, reﬂecting reduced sensitivity to COVID-related disruptions over longer timeframes. Conversely, short-
term predictions (1 Day) exhibit pronounced spikes in MSE, particularly during the transition from pre-COVID to
COVID, indicating that these horizons are more vulnerable to abrupt market ﬂuctuations induced by the
pandemic.
The technology sector demonstrates pronounced increases in prediction errors, particularly during the transi-
tion from pre-COVID to COVID. For instance, NVDA shows extreme increases in MSE, reaching approximately
3500% for the 1-day horizon, indicating a signiﬁcant challenge in capturing the volatility of technology stocks
during the early pandemic phase. Similarly, MSFT exhibits a 1500% increase in 1-day MSE and a sustained rise
of over 1000% for longer horizons (10 days and 100 days). AAPL and GOOGL, while exhibiting more moderate
increases (below 1000%), still reﬂect elevated modeling challenges due to increased market uncertainty.
In contrast, IBM, as a more stable technology stock, shows relatively smaller error increases, with MSE
changes remaining below 500% across all horizons. These ﬁndings suggest that technology sector stocks, par-
ticularly high-growth and volatile ones like NVDA and MSFT, posed signiﬁcant modeling challenges during the
pandemic, requiring adaptive strategies to manage sudden shifts in market dynamics.
AMZN, representing the consumer discretionary sector, exhibits a different trend compared to technology
stocks. The pre-COVID-to-COVID MSE increases are moderate, with less than 500% across all prediction
horizons. Interestingly, the COVID-to-post-COVID transitions reveal declines in MAE, particularly for the
100-day horizon, where AMZN shows a nearly 20% reduction in prediction errors. This behavior suggests that
consumer discretionary stocks like AMZN beneﬁted from relatively higher predictability during the recovery
phase, potentially driven by increased demand for e-commerce services.
XOM, representing the energy sector, shows modest increases in prediction errors compared to technology
stocks. For the 1-day horizon, MSE increases are below 500%, and for longer horizons, the increases are even
smaller. This sector’s resilience in modeling may be attributed to its dependence on macroeconomic factors like
oil prices, which exhibited more predictable recovery trends during the post-COVID phase.
Healthcare stocks such as PFE and JNJ exhibit relatively lower increases in MSE and MAE across all horizons.
For example, PFE shows less than 200% MSE increases for the 1-day horizon, and JNJ reﬂects similar trends.
These modest error changes highlight the relative stability of healthcare stocks during the pandemic, likely due to
sustained demand and the sector’s role in vaccine and treatment development.
UAL, representing the airlines sector, stands out due to its unique behavior. The 1-day and 10-day horizons
show modest increases in prediction errors, with MSE changes remaining below 500%. However, the 100-day
horizon reveals a more signiﬁcant rise in MSE, reﬂecting the long-term uncertainty surrounding the sector’s
recovery. Airlines faced signiﬁcant disruptions during the pandemic, including travel restrictions and demand
collapse, making accurate long-term modeling particularly challenging.
bFig. 6 Forecast Results for 10-Day Prediction Horizon
123
Neural Computing and Applications (2025) 37:15855–15890
15878
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 25
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15879

---

## Page 26
5.1 Statistical analysis of forecast errors across market regimes
To quantitatively assess the impact of market conditions on forecasting accuracy, a statistical analysis was
conducted to compare forecast error distributions across the pre-COVID, COVID, and post-COVID periods. This
analysis employs the Kolmogorov–Smirnov (KS) test to detect distributional shifts and Levene’s test to examine
changes in variance, to analyze how forecast errors evolved under different market conditions.
The Kolmogorov–Smirnov (KS) test is a nonparametric test used to compare two empirical distributions.
Given two cumulative distribution functions, F1ðxÞ and F2ðxÞ, the KS test statistic is deﬁned as [72–74]:
D ¼ sup
x
F1 x
ð Þ  F2ðxÞ
j
j
ð23Þ
where D represents the maximum absolute difference between the two distributions. A small p value ðp\0:05Þ
suggests that the two distributions are signiﬁcantly different.
The Levene’s test is used to assess the equality of variances between two or more groups. Given a dataset split
into k groups, the test statistics are computed as [75–77]:
bFig. 7 Forecast Results for 100-Day Prediction Horizon
Table 2 Forecasting Performance Metrics (MSE and MAE) Across Pre-COVID, COVID, and Post-COVID Periods for
Different Prediction Horizons
Asset
Error
Pre-COVID
COVID
Post-COVID
Overall
1
Day
10
Days
100
Days
1
Day
10
Days
100
Days
1
Day
10
Days
100
Days
1
Day
10
Days
100
Days
AAPL
MSE:
0.54
5.72
67.36
8.75
69.18
642.19
8.81
90.33
604.76
5.28
46.79
372.32
MAE:
0.52
1.82
5.61
2.22
6.76
18.60
2.21
7.71
21.69
1.50
4.86
13.23
MSFT
MSE:
2.18
11.15
81.96
26.24
189.01
1782.98
30.71
277.72
1855.17
17.04
132.77
1017.99
MAE:
1.06
2.53
6.72
3.85
11.17
34.87
4.25
13.40
34.85
2.76
7.98
21.99
NVDA
MSE:
0.01
0.14
1.68
0.38
3.68
50.15
7.01
63.76
966.40
1.72
15.49
196.27
MAE:
0.08
0.27
1.10
0.43
1.38
5.82
1.71
5.64
26.14
0.57
1.85
7.39
GOOGL
MSE:
0.65
4.87
32.86
4.81
36.00
411.64
7.02
68.11
381.29
3.54
29.60
232.76
MAE:
0.57
1.69
4.61
1.61
4.77
17,46
1.91
6.40
16.59
1.24
3.82
11.42
AMZN
MSE:
1.78
14.45
148.42
11.81
112.28
1489.84
9.37
75.56
348.12
7.01
62.39
666.42
MAE:
0.89
2.68
9.15
2.59
8.38
33.58
2.30
6.66
15.56
1.81
5.57
19.09
IBM
MSE:
3.62
34.29
231.59
5.77
51.62
164.36
5.56
67.44
793.50
4.81
47.73
310.68
MAE:
1.34
4.45
12.37
1.67
5.37
10.14
1.57
6.24
22.19
1.51
5.17
13.38
XOM
MSE:
1.14
8.82
84.51
2.65
24.68
211.32
3.02
23.57
72.84
2.09
17.67
127.87
MAE:
0.83
2.27
6.27
1.23
3.75
11.83
1.34
3.84
7.27
1.08
3.14
8.45
PFE
MSE:
0.19
1.70
15.42
0.66
6.92
39.56
0.26
2.89
31.47
0.37
3.80
27.03
MAE:
0.32
0.96
3.03
0.59
2.05
4.86
0.38
1.33
4.58
0.43
1.42
3.97
JNJ
MSE:
2.02
17.83
117.89
4.36
34.15
145.18
2.65
29.50
178.23
2.98
26.16
138.77
MAE:
0.96
3.10
8.94
1.48
4.46
9.67
1.17
4.45
11.29
1.19
3.88
9.64
UAL
MSE:
2.99
24.53
373.97
3.59
44.12
238.35
2.15
20.98
200.17
3.01
30.63
293.39
MAE:
1.27
3.89
12.42
1.36
4.55
11.13
1.07
3.48
10.05
1.26
4.03
11.52
123
Neural Computing and Applications (2025) 37:15855–15890
15880
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 27
W ¼ ðN  kÞ
ðk  1Þ
Pk
i¼1NiðZi  ZÞ
2
Pk
i¼1
PNi
j¼1ðZij  ZiÞ
2
ð24Þ
where N is the total number of observations, Ni is the sample size of group i, Zi;j represents transformed absolute
deviations, and Zi and Zare the group-wise and overall means, respectively. A signiﬁcant p value ðp\0:05Þ
indicates that at least one group exhibits a different variance from the others. Table 3 presents the detailed
statistical results supporting these conclusions. It summarizes the outcomes of Kolmogorov–Smirnov and
Levene’s tests across different market regimes. Levene’s test results further support these ﬁndings by showing
substantial changes in variance across market regimes.
Applying these tests to forecast errors across market regimes reveals critical insights into how prediction
uncertainty evolved. The KS test results indicate signiﬁcant distributional shifts from pre-COVID to COVID for
all assets ðp\0:05Þ, conﬁrming that forecasting errors followed a markedly different distribution during the high-
Fig. 8 Comparison of Per-
centage Changes in Predic-
tion Errors (MSE and
MAE) Across COVID
Periods
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15881

---

## Page 28
volatility pandemic period. The largest discrepancies were observed in technology stocks, such as GOOGL
ðp ¼ 7:66  106Þ and XOM ðp ¼ 1:42  1011Þ, reﬂecting the extreme ﬂuctuations in market conditions. In
contrast, comparisons between COVID and post-COVID periods yielded mixed results. While some assets, such
as MSFT and NVDA, showed no signiﬁcant difference ðp [ 0:05Þ, others (GOOGL and XOM) continued to
exhibit statistically distinct error distributions, suggesting that forecasting challenges persisted beyond the
pandemic.
The transition from pre-COVID to COVID resulted in a statistically signiﬁcant increase in forecasting error
variance for all assets ðp\0:05Þ , with particularly extreme effects in NEXT_XOM ðp ¼ 5:54  1049Þ and
NEXT_GOOGLEðp ¼ 8:56  1018Þ, indicating heightened uncertainty and error magniﬁcation during market
shocks. While some assets showed a partial return to pre-pandemic variance levels in the post-COVID period,
others (PFE, XOM, GOOGL) retained signiﬁcantly higher variances, suggesting that forecasting uncertainty
remained elevated even as markets stabilized.
5.2 Computational considerations, symbolization trade-offs, and model sensitivity analysis
The proposed methodology, which combines symbolic dynamics and graph-theoretic approaches, offers a
structured and interpretable framework for analyzing nonlinear ﬁnancial time series. However, its complexity and
inherent limitations present challenges that require consideration.
An important consideration in the computational efﬁciency of the symbolization process is its OðNÞ com-
plexity, where N is the length of the time series. The transformation from raw numerical values to symbolic states
involves three primary steps: normalization, discretization into amplitude symbols, and trend state assignment.
Each of these operations is applied sequentially to the time series, requiring only a single pass through the data,
ensuring that the computational cost scales linearly with the dataset size. The transition matrix construction,
which follows symbolization, operates by iterating through N  w overlapping windows of length w to capture
state transitions, resulting in a computational cost of OðN  wÞ  OðNÞ for large datasets where w is signiﬁcantly
smaller than N. Compared to traditional feature extraction methods that rely on high-dimensional technical
indicators or complex handcrafted representations, symbolization remains a highly efﬁcient alternative, pre-
serving structural information while mitigating computational overhead.
Symbolization involves normalizing time series data and discretizing it into symbolic states. The choice of
alphabet size and window length directly inﬂuences the granularity and accuracy of the symbolic representation.
A comparison of these choices for the 1-day prediction horizon is presented in Table 4. A small alphabet (e.g.,
Table 3 Statistical Analysis of Forecast Error Distributions Across Market Regimes
Asset
KS Test Pre-
COVID vs
COVID
KS Test COVID
vs Post-COVID
KS Test Pre-COVID
vs Post-COVID
Levene Test Pre-
COVID vs COVID
Levene Test COVID
vs Post-COVID
Levene Test Pre-
COVID vs Post-
COVID
AAPL
2.55E-04
9.69 E-04
8.27 E-01
4.01E-15
7.57E-13
4.06 E-01
MSFT
3.43 E-04
8.49 E-02
2.37 E-01
4.05E-18
6.62 E-08
1.93 E-02
NVDA
1.14 E-03
6.66 E-02
6.82 E-03
9.30 E-09
2.43 E-02
5.11 E-03
GOOGL
7.67 E-06
1.26 E-03
3.04 E-04
8.56E-18
1.20 E-02
9.21 E-08
AMZN
5.31 E-06
1.27 E-01
2.59 E-02
1.83 E-16
8.61 E-04
2.36 E-05
IBM
2.34 E-03
2.29 E-03
5.55 E-02
1.52 E-10
9.06 E-08
7.69 E-01
XOM
1.42 E-11
4.76 E-04
2.58 E-02
5.55E-49
2.69 E-17
6.44 E-08
PFE
2.19 E-05
6.34 E-02
0.00E ? 00
6.35E-25
2.13 E-04
1.10 E-09
JNJ
5.57 E-03
7.65 E-02
1.25 E-01
1.31 E-06
2.65 E-04
6.01 E-01
UAL
1.59 E-06
2.50 E-05
5.85 E-04
5.74E-31
1.53 E-09
4.00 E-07
123
Neural Computing and Applications (2025) 37:15855–15890
15882
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 29
3–5 symbols) leads to information loss, whereas a large alphabet (e.g., more than 10 symbols) increases noise
sensitivity and computational cost. The results indicate that an alphabet size of 10 consistently outperforms
smaller alternatives across multiple assets, including AAPL (4.53 MSE), MSFT (14.94 MSE), and AMZN (7.15
MSE) when using a 100-timestep window. These ﬁndings suggest that an alphabet size of 10 balances granularity
and robustness, capturing essential signal variations while avoiding excessive noise ampliﬁcation.
Similarly, window size plays a crucial role in capturing the temporal dependencies of ﬁnancial time series. A
key aspect of the amplitude symbolization process is normalizing time series data before symbol assignments.
Each windowed segment of length w undergoes min–max normalization, ensuring that the transformed values lie
within a ﬁxed range [0,1]. This transformation effectively reduces the impact of extreme outliers, preventing high-
magnitude ﬂuctuations from dominating the symbolic representation. However, the effectiveness of normalization
is inherently dependent on window size. A shorter window (e.g., 50 timesteps) may fail to capture broader trends
and remain susceptible to local spikes. In contrast, an excessively long window (e.g., 250 timesteps) may lead to
over-smoothing, suppressing meaningful variations, and distorting high-frequency components essential for
short-term predictions.
Furthermore, the total MSE values across all assets conﬁrm the superiority of this conﬁguration. The
100-timestep window with 10 symbols yields the lowest total MSE (47.85), signiﬁcantly outperforming the
50-timestep (64.63) and 250-timestep (64.64) alternatives. This highlights that a 100-timestep window effectively
balances short-term and long-term dependencies, enabling the model to achieve accuracy and computational
efﬁciency. The increased errors in the 50-timestep window indicate that shorter contexts fail to encode sufﬁcient
information. At the same time, the degradation in performance at 250 timesteps suggests that an overly extended
context reduces the model’s sensitivity to critical short-term ﬂuctuations.
The construction of state transition matrices offers a potent probabilistic framework for capturing temporal
dynamics, providing a valuable understanding of the underlying structure of ﬁnancial time series. While it
primarily assumes ﬁrst-order Markov properties, this approach effectively models short-term dependencies and
can be extended to incorporate higher-order transitions to capture more complex patterns. However, the efﬁcacy
of these transition matrices in deep learning models heavily relies on robust preprocessing layers that ensure
consistency, noise reduction, and enhanced feature extraction before being fed into neural architectures.
To assess the impact of different architectural choices, an absence study is conducted by systematically
removing key components and measuring their effect on forecasting performance. The following inferences are
obtained:
Table 4 Impact of Window
Size and Amplitude
Alphabet Size on Forecast-
ing Performance (MSE)
Across Different Assets
Window Size:
50 timesteps
100 timesteps
250 timesteps
Amplitude Alphabet Size:
4
8
10
4
8
10
4
8
10
Asset
MSE
MSE
MSE
MSE
MSE
MSE
MSE
MSE
MSE
AAPL
5.39
5.27
4.53
5.23
5.14
5.28
5.45
5.31
5.22
MSFT
16.63
15.25
14.94
19.94
14.47
17.04
16.99
19.81
17.21
NVDA
1.84
1.76
1.82
1.82
8.68
1.72
2.06
2.01
2.01
GOOGL
3.79
3.68
3.59
3.77
3.55
3.54
4.15
10.56
10.21
AMZN
7.56
7.16
7.15
7.55
12.90
7.01
7.98
7.87
8.45
IBM
3.58
3.46
3.24
3.74
3.44
4.81
3.39
14.26
3.44
XOM
2.39
2.75
1.36
1.34
1.53
2.09
1.68
3.12
3.12
PFE
0.27
0.25
0.25
2.92
0.25
0.37
0.27
0.25
0.28
JNJ
2.93
2.41
24.68
2.60
2.46
2.98
11.42
2.57
11.27
UAL
3.57
7.23
3.07
3.25
2.78
3.01
3.32
3.20
3.43
TOTAL
47.95
49.22
64.63
52.16
55.2
47.85
56.71
68.96
64.64
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15883

---

## Page 30
•
The inclusion of Conv2D layers signiﬁcantly enhanced short-term predictions by capturing localized symbolic
dependencies in state transition matrices. The removal of these layers led to a notable increase in error
variance, indicating that spatial patterns in symbolic sequences are crucial for precise forecasting.
•
While LSTMs demonstrated superior stability and predictive accuracy in most cases, GRUs performed
comparably for certain assets, XOM and PFE, as indicated by their lower MSE values in Table 5.
•
The proposed combination, incorporating both Conv2D and LSTM layers, yielded the most consistent
accuracy across assets, reinforcing the importance of capturing both local patterns and long-range
dependencies in ﬁnancial time series through transition matrices.
The comparison results, summarized in Table 5, highlight the inﬂuence of each architectural component on
forecasting performance. These ﬁndings emphasize the necessity of Conv2D layers for capturing local features,
LSTM layers for maintaining long-range dependencies.
While the proposed approach provides a computationally efﬁcient alternative to direct deep learning-based
methods, certain trade-offs must be acknowledged. The computational complexity of symbolization and transition
matrix construction is OðNÞ, making it scalable for large datasets, yet the additional storage and processing of
symbolic states add complexity compared to traditional continuous-valued time series models. The hierarchical
stacking of transition matrices ensures that both short- and long-range temporal dependencies are captured, but
this also introduces potential sensitivity to the choice of symbolic parameters, including alphabet size and window
length. Moreover, while the proposed approach simpliﬁes feature extraction and enhances interpretability, it
requires careful tuning to optimize performance across different market conditions.
5.3 Rolling expanding window cross-validation
While the 50–50 temporal split serves as the primary validation strategy in this study, rolling expanding window cross-
validation is applied on 1-day prediction horizon model as a complementary method to assess how forecasting
performance varies across different temporal segments. This approach not only supports the validity of the 50–50 split
but also offers insights into the stability and adaptability of the models when exposed to gradually increasing training
periods [78, 79]. This method progressively expands the training window while shifting the test set forward in time.
The rolling window cross-validation approach is implemented using a ﬁxed window size for training and testing:
•
The training set starts with 10% of the data.
•
Test set is the next 10% of the data immediately following the training set.
•
The training set expands by incorporating the previous test set, while the test set moves forward by another
10%.
•
This process is repeated until the entire dataset is covered, leading to multiple validation splits.
Table 5 Systematic Ablation Studies on the Individual Contributions of Architectural Components
Condition:
Without Conv2D Layers
Without LSTM Layer
LSTM Replaced with GRU Layer
Proposed Combination
Asset
MSE
MSE
MSE
MSE
AAPL
88.72
5.14
119.52
5.28
MSFT
20.12
16.12
15.00
17.04
NVDA
8.08
1.78
5.59
1.72
GOOGL
8.73
3.60
10.57
3.54
AMZN
11.90
7.40
12.32
7.01
IBM
8.76
3.68
13.32
4.81
XOM
1.32
1.40
1.47
2.09
PFE
0.67
0.26
0.35
0.37
JNJ
18.18
15.17
12.37
2.98
UAL
5.06
2.88
3.06
3.01
123
Neural Computing and Applications (2025) 37:15855–15890
15884
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 31
This ensures that each model is trained only on past data while forecasting the subsequent period, making it a realistic
evaluation method for ﬁnancial time series forecasting. This progressive training expansion allows us to evaluate:
The effectiveness of different training period lengths in capturing essential patterns for forecasting.
The impact of temporal variations on model performance, particularly in response to structural changes in the data.
Potential performance trends that may emerge when the model is exposed to longer training histories.
By implementing this cross-validation scheme, ﬂuctuations in forecasting accuracy across different temporal
splits are analyzed. This examination is crucial in ﬁnancial markets, where abrupt shifts in market conditions can
inﬂuence model reliability. Table 6 presents the mean squared error (MSE) results for the rolling expanding
window cross-validation across different train–test splits for multiple assets. Several key observations emerge:
•
Early-stage models (10–50% training windows) exhibit relatively stable forecasting performance, indicating
that short-term historical data are sufﬁcient for certain assets but may be insufﬁcient for others.
•
Performance variations in later windows (60–100%) suggest that some assets experience greater volatility or
non-stationary effects that impact forecasting accuracy.
•
Longer training periods (e.g., 50–100%) do not universally guarantee better results, indicating that optimal
training window selection remains asset-dependent.
These ﬁndings reinforce the rationale for the 50–50 split as a robust validation approach while also high-
lighting the nuances of forecasting performance across different temporal horizons.
6 Conclusion
This study advances the theoretical and empirical understanding of ﬁnancial time series forecasting by integrating
symbolic dynamics with a convolutional recurrent neural network (CRNN) architecture. Symbolic dynamics
provides a powerful preprocessing framework that transforms continuous-valued stock price data into sequences
of discrete symbols, preserving essential structural patterns and emphasizing qualitative behaviors. Discretizing
the data into amplitude and trend states, followed by the construction of state transition matrices, enables the
representation of the probabilistic structure of market movements. The methodology uniquely focuses on time
series data derived exclusively from economic factors, such as stock prices, trading volumes, and volatility,
without incorporating external political or social variables. This self-contained framework highlights the strength
of symbolic dynamics in capturing inherent market ﬂuctuations while ﬁltering out noise. By discretizing time
series data into symbolic states based on amplitude and trend, and representing their transitions probabilistically,
Table 6 Rolling Expanding Window Cross-Validation Results
Train Period (%)
Test Period (%)
AAPL
MSFT
NVDA
GOOGL
AMZN
IBM
XOM
PFE
JNJ
UAL
MSE
MSE
MSE
MSE
MSE
MSE
MSE
MSE
MSE
MSE
0–10
10–20
0.01
0.11
0.00
0.05
0.02
0.74
0.28
0.02
110.43
0.42
0–20
20–30
0.06
0.12
0.00
0.07
0.07
1.97
0.49
0.02
0.20
0.49
0–30
30–40
7.65
0.21
0.00
0.13
0.10
1.89
0.30
0.04
0.31
0.84
0–40
40–50
0.20
0.51
0.00
0.29
0.22
1.83
0.60
0.07
357.56
2.62
0–50
50–60
0.19
0.45
0.01
0.22
0.29
1.43
0.33
0.06
899.50
1.94
0–60
60–70
0.77
6.28
0.22
12.19
3.25
2.38
0.60
0.16
15.19
3.93
0–70
70–80
6.57
20.63
0.13
3.23
10.01
5.28
1.23
0.32
4.55
5.80
0–80
80–90
10.74
31.85
0.72
7.75
14.92
3.09
3.01
0.71
3.15
2.10
0–90
90–100
9.00
31.36
9.61
7.78
11.65
7.40
2.33
0.20
2.15
2.32
0–50
50–100
5.28
17.04
1.72
3.54
7.01
4.81
2.09
0.37
2.98
3.01
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15885

---

## Page 32
the methodology emphasizes structural and qualitative patterns that are crucial for analyzing nonlinear and
volatile ﬁnancial domains.
From a theoretical standpoint, the combination of symbolic dynamics with CRNN-based forecasting aligns
with principles from ergodic theory, information theory, and Markovian dynamics. Representing complex
temporal dependencies in a compact, state-based manner reduces the problem’s dimensionality while preserving
its nonlinear characteristics. The symbolic-state transitions are then encapsulated in tensors suitable for deep
learning models, where convolutional layers focus on extracting spatial patterns within transition matrices and
recurrent layers capture temporal dependencies spanning multiple time windows.
Empirically, the results underscore the model’s adaptability across varying market regimes and forecasting
horizons. During the stable pre-COVID period, the CRNN achieved relatively low error metrics, with MSE and
MAE values as low as 0.01 and 0.08 for NVDA’s 1-day horizon. The reduced volatility in this phase allowed the
symbolization and neural architecture to exploit well-deﬁned market patterns. However, as market uncertainty
intensiﬁed during the COVID period, both short- and long-term forecasts became more challenging, reﬂected in
increased errors, e.g., MSFT’s 1-day horizon MSE surged to 26.24, and AMZN’s 100-day horizon MSE reached
1489.84. These results highlight the intrinsic difﬁculty of forecasting in crisis conditions and reinforce the value
of symbolization as a robust baseline technique, even when facing abrupt regime changes.
Post-COVID, moderate improvements in predictive accuracy emerged as markets began stabilizing, though
they remained more volatile than pre-COVID conditions. For instance, AAPL’s 100-day horizon MSE decreased
from 642.19 during COVID to 604.76 post-COVID. These changes emphasize the necessity of adaptive models
that not only learn from historical stable regimes but also accommodate and recalibrate as new structural patterns
emerge.
The multi-horizon forecasting experiments demonstrate a trade-off between forecast length and accuracy.
While 1-day predictions often achieved high precision, longer-term horizons ampliﬁed cumulative uncertainties.
Nevertheless, the use of symbolic dynamics, normalized transition matrices, and CRNN architectures enabled the
retention of meaningful information, yielding competitive performance even for extended horizons like 100 days.
While the 50–50 temporal split was adopted as the primary validation strategy to ensure a stable and unbiased
assessment of forecasting accuracy, the rolling expanding window cross-validation provided further acuities into
the variations in model performance across different time horizons. The observed ﬂuctuations in error metrics,
MSE, across expanding windows emphasize the importance of selecting an appropriate training horizon that
balances historical representativeness and adaptability to structural changes. The results conﬁrm that while a ﬁxed
validation split offers a reliable benchmark, additional cross-validation approaches can help reveal forecasting
sensitivities to different market conditions.
Despite its promising results, the methodology’s exclusive reliance on time series data from economic factors
represents both a strength and a limitation. On the one hand, this focus ensures scalability and independence from
external, less predictable factors like political or social events. On the other hand, it overlooks potentially valuable
contextual information from other domains that could enhance forecasting performance. For instance, incorpo-
rating macroeconomic indicators, geopolitical developments, or consumer sentiment data through data fusion
approaches could provide a more comprehensive understanding of market dynamics and improve the model’s
responsiveness to external shocks.
The growing adoption of graph-theoretic approaches in ﬁnancial forecasting has further highlighted the need to
model complex interdependencies among ﬁnancial assets. Traditional time series models often overlook structural
relationships between market entities, whereas graph neural networks (GNNs) provide a robust framework for
capturing dynamic interactions, sectoral dependencies, and global market inﬂuences [40–42, 45–50]. Recent
advancements in GNN-based forecasting have demonstrated superior performance in modeling stock co-move-
ments, leveraging adjacency matrix representations and message-passing architectures to uncover latent structural
patterns in ﬁnancial networks [46, 48, 50]. By integrating graph-based methodologies with symbolic transition
matrices, future research can further enhance interpretability, exploit higher-order relationships, and develop more
adaptive forecasting models that effectively respond to evolving market dynamics.
123
Neural Computing and Applications (2025) 37:15855–15890
15886
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 33
As a ﬁnal note, while the proposed framework demonstrates robustness and adaptability across diverse
ﬁnancial scenarios, future research can build upon these ﬁndings by integrating symbolic dynamics with data
fusion techniques. By incorporating complementary information from political, social, and economic domains, as
well as reﬁning symbolization schemes and enhancing neural architectures with attention mechanisms or
explainable AI frameworks, the methodology can be further strengthened. Such advancements will not only
improve forecasting accuracy in volatile and complex environments but also provide a more holistic approach to
understanding ﬁnancial market behaviors, ultimately guiding better investment decisions and risk management
strategies.
Author contributions Fuat Kaan Mirza designed the study, performed the analysis, and wrote the manuscript. O¨ nder Pekcan
contributed to construction of methodology and the interpretation of the results. Mustafa Hekimog˘lu provided critical
feedback and edited the manuscript. Tunçer Baykas¸ oversaw the research process and approved the ﬁnal manuscript. All
authors reviewed and approved the ﬁnal version.
Funding Open access funding provided by the Scientiﬁc and Technological Research Council of Tu¨rkiye (TU¨ BI˙TAK). This
research received no speciﬁc grant from any funding agency in the public, commercial, or not-for-proﬁt sectors.
Data availability The data used in this study were sourced from Yahoo Finance, a publicly accessible platform for historical
and real-time ﬁnancial data. All datasets utilized in the analysis, including stock price data and related market indicators, are
openly available through the Yahoo Finance website (https://ﬁnance.yahoo.com). Researchers can access the same datasets
by retrieving historical data for the relevant assets and time periods through the platform’s data export feature.
Declarations
Conflict of interest The authors declare that they have no competing interests.
Ethical approval The submitted work is original and has not been published elsewhere in any form or language. The
results/data/figures in this manuscript have not been published elsewhere, nor are they under consideration (from you or one
of your contributing authors) by another publisher.
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
1. Spelta A, Pecora N, Pagnottoni P (2022) Chaos based portfolio selection: a nonlinear dynamics approach. Expert Syst
Appl 188:116055. https://doi.org/10.1016/j.eswa.2021.116055
2. Mandelbrot BB (1997) The variation of certain speculative prices. In: Mandelbrot BB (ed) Fractals and scaling in
ﬁnance. Springer New York, New York, pp 371–418. https://doi.org/10.1007/978-1-4757-2763-0_14
3. Shively PA (2003) The nonlinear dynamics of stock prices. Quarterly Rev Econ Finance 43:505–517. https://doi.org/10.
1016/S1062-9769(02)00190-4
4. Pai P-F, Lin C-S (2005) A hybrid ARIMA and support vector machines model in stock price forecasting. Omega
(Westport) 33:497–505. https://doi.org/10.1016/j.omega.2004.07.024
5. Kobiela D, Krefta D, Kro´l W, Weichbroth P (2022) ARIMA vs LSTM on NASDAQ stock exchange data. Proced
Comput Sci 207:3836–3845. https://doi.org/10.1016/j.procs.2022.09.445
6. Verma S, Prakash Sahu S, Prasad Sahu T. 2022 Ensemble approach for stock market forecasting using ARIMA and
LSTM model. In: Pandian AP, Palanisamy R, Narayanan M, Senjyu T, editors. In: Proceedings of third international
conference on intelligent computing, information and control systems, Singapore: Springer Nature Singapore, p. 65–80.
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15887

---

## Page 34
7. Bollerslev T (1986) Generalized autoregressive conditional heteroskedasticity. J Econom 31:307–327. https://doi.org/10.
1016/0304-4076(86)90063-1
8. Kim HY, Won CH (2018) Forecasting the volatility of stock price index: A hybrid model integrating LSTM with
multiple GARCH-type models. Expert Syst Appl 103:25–37. https://doi.org/10.1016/j.eswa.2018.03.002
9. Wang L, Ma F, Liu J, Yang L (2020) Forecasting stock price volatility: new evidence from the GARCH-MIDAS model.
Int J Forecast 36:684–694. https://doi.org/10.1016/j.ijforecast.2019.08.005
10. Zhao C, Wu M, Liu J, Duan Z, Li J, Shen L et al (2023) Progress and prospects of data-driven stock price forecasting
research. In J Cognit Comput Eng 4:100–108. https://doi.org/10.1016/j.ijcce.2023.03.001
11. Lahmiri S (2018) Minute-ahead stock price forecasting based on singular spectrum analysis and support vector
regression. Appl Math Comput 320:444–451. https://doi.org/10.1016/j.amc.2017.09.049
12. Xiao C, Xia W, Jiang J (2020) Stock price forecast based on combined model of ARI-MA-LS-SVM. Neural Comput
Appl 32:5379–5388. https://doi.org/10.1007/s00521-019-04698-5
13. Park HJ, Kim Y, Kim HY (2022) Stock market forecasting using a multi-task approach integrating long short-term
memory and the random forest framework. Appl Soft Comput 114:108106. https://doi.org/10.1016/j.asoc.2021.108106
14. Zhou F, Zhang Q, Sornette D, Jiang L (2019) Cascading logistic regression onto gradient boosted decision trees for
forecasting and trading stock indices. Appl Soft Comput 84:105747. https://doi.org/10.1016/j.asoc.2019.105747
15. Gu Q, Chang Y, Xiong N, Chen L (2021) Forecasting Nickel futures price based on the empirical wavelet transform and
gradient boosting decision trees. Appl Soft Comput 109:107472. https://doi.org/10.1016/j.asoc.2021.107472
16 Andrade LACG, Cunha CB (2023) Disaggregated retail forecasting: a gradient boosting approach. Appl Soft Comput
141:110283. https://doi.org/10.1016/j.asoc.2023.110283
17. Jerez T, Kristjanpoller W (2020) Effects of the validation set on stock returns forecasting. Expert Syst Appl 150:113271.
https://doi.org/10.1016/j.eswa.2020.113271
18 Bergmeir C, Costantini M, Benı´tez JM (2014) On the usefulness of cross-validation for directional forecast evaluation.
Comput Stat Data Anal 76:132–143. https://doi.org/10.1016/j.csda.2014.02.001
19. Chang P-C, Wu J-L, Lin J-J (2016) A Takagi-Sugeno fuzzy model combined with a support vector regression for stock
trading forecasting. Appl Soft Comput 38:831–842. https://doi.org/10.1016/j.asoc.2015.10.030
20 Hadavandi E, Shavandi H, Ghanbari A (2010) Integration of genetic fuzzy systems and artiﬁcial neural networks for
stock price forecasting. Knowl Based Syst 23:800–808. https://doi.org/10.1016/j.knosys.2010.05.004
21. Chen T-L, Cheng C-H, Jong TH (2007) Fuzzy time-series based on Fibonacci sequence for stock price forecasting. Phys
A: Stat Mech Appl 380:377–390. https://doi.org/10.1016/j.physa.2007.02.084
22. Jiang F, Ma T, Zhu F (2024) Fundamental characteristics, machine learning, and stock price crash risk. J Financial Mark
69:100908. https://doi.org/10.1016/j.ﬁnmar.2024.100908
23. Kao L-J, Chiu C-C, Lu C-J, Yang J-L (2013) Integration of nonlinear independent component analysis and support
vector regression for stock price forecasting. Neurocomputing 99:534–542. https://doi.org/10.1016/j.neucom.2012.06.
037
24. Chen Y, Calabrese R, Martin-Barragan B (2024) Interpretable machine learning for imbalanced credit scoring datasets.
Eur J Oper Res 312:357–372. https://doi.org/10.1016/j.ejor.2023.06.036
25. Mirza FK, Ogrenci AS (2023) Using Hybrid Approaches for Credit Application Scoring. In: 2023 IEEE 23rd Inter-
national symposium on computational intelligence and informatics (CINTI), p. 111–6. https://doi.org/10.1109/
CINTI59972.2023.10382025.
26. Rajab S, Sharma V (2019) An interpretable neuro-fuzzy approach to stock price forecasting. Soft Comput 23:921–936.
https://doi.org/10.1007/s00500-017-2800-7
27. Yun KK, Yoon SW, Won D (2023) Interpretable stock price forecasting model using genetic algorithm-machine
learning regressions and best feature subset selection. Expert Syst Appl 213:118803. https://doi.org/10.1016/j.eswa.
2022.118803
28. JayanthBalaji A, Harish Ram DS, Nair BB (2018) Applicability of deep learning models for stock price forecasting an
empirical study on BANKEX data. Proced Comput Sci 143:947–953. https://doi.org/10.1016/j.procs.2018.10.340
29. Yu Z, Qin L, Chen Y, Parmar MD (2020) Stock price forecasting based on LLE-BP neural network model. Phys A: Stat
Mech Appl 553:124197. https://doi.org/10.1016/j.physa.2020.124197
30. Laboissiere LA, Fernandes RAS, Lage GG (2015) Maximum and minimum stock price forecasting of Brazilian power
distribution companies based on artiﬁcial neural networks. Appl Soft Comput 35:66–74. https://doi.org/10.1016/j.asoc.
2015.06.005
31 Li S, Wu J, Jiang X, Xu K (2022) Chart GCN: learning chart information with a graph convolutional network for stock
movement prediction. Knowl Based Syst 248:108842. https://doi.org/10.1016/j.knosys.2022.108842
32. Long W, Lu Z, Cui L (2019) Deep learning-based feature engineering for stock price movement prediction. Knowl
Based Syst 164:163–173. https://doi.org/10.1016/j.knosys.2018.10.034
33. Abdul Quadir Md, Kapoor S, Chris Junni AV, Sivaraman AK, Tee KF, Sabireen H, Janakiraman N (2023) Novel
optimization approach for stock price forecasting using multi-layered sequential LSTM. Appl Soft Comput 134:109830.
https://doi.org/10.1016/j.asoc.2022.109830
123
Neural Computing and Applications (2025) 37:15855–15890
15888
https://doi.org/10.1007/s00521-025-11325-z

---

## Page 35
34. Tian L, Feng L, Yang L, Guo Y (2022) Stock price prediction based on LSTM and LightGBM hybrid model.
J Supercomput 78:11768–11793. https://doi.org/10.1007/s11227-022-04326-5
35 Osipenko G (2007) Symbolic image. In: Osipenko G (ed) Dynamical Systems Graphs, and Algorithms. Springer, Berlin,
pp 15–25
36. Hao B-L, Zheng W-M. 1998 Applied symbolic dynamics and chaos. Vol. 7. WORLD SCIENTIFIC. https://doi.org/10.
1142/3830.
37. Mirza FK, O¨ z U, Hekimog˘lu M, Pural YE, Aydemir MT, Baykas¸ T, et al (2024) A novel multiscale graph signal
processing and network dynamics approach to vibration analysis for stone size discrimination via nonlinear manifold
embeddings and a convolutional self-attention model. SSRN.
38. Dong X, Thanou D, Toni L, Bronstein M, Frossard P (2020) Graph signal processing for machine learning: a review and
new perspectives. IEEE Signal Process Mag 37:117–127. https://doi.org/10.1109/MSP.2020.3014591
39. Mirza FK, Baykas¸ T, Hekimog˘lu M, Pekcan O¨ (2024) Interpretable multi-model EEG signal classiﬁcation employing
Modwt and nonlinear dynamics quantiﬁers with state transitional statistics. SSRN. https://doi.org/10.2139/ssrn.4931753.
40. Wang Y, Qu Y, Chen Z (2022) Review of graph construction and graph learning in stock price prediction. Proced
Comput Sci 214:771–778. https://doi.org/10.1016/j.procs.2022.11.240
41 Jafari A, Haratizadeh S (2022) GCNET: Graph-based prediction of stock price movement using graph convolutional
network. Eng Appl Artif Intell 116:105452. https://doi.org/10.1016/j.engappai.2022.105452
42. Song G, Zhao T, Wang S, Wang H, Li X (2023) Stock ranking prediction using a graph aggregation network based on
stock price and stock relationship information. Inf Sci 643:119236. https://doi.org/10.1016/j.ins.2023.119236
43 Long J, Chen Z, He W, Wu T, Ren J (2020) An integrated framework of deep learning and knowledge graph for
prediction of stock price trend: an application in Chinese stock exchange market. Appl Soft Comput 91:106205. https://
doi.org/10.1016/j.asoc.2020.106205
44 Wang T, Guo J, Shan Y, Zhang Y, Peng B, Wu Z (2023) A knowledge graph–GCN–community detection integrated
model for large-scale stock price prediction. Appl Soft Comput 145:110595. https://doi.org/10.1016/j.asoc.2023.110595
45 Wu J, Xu K, Chen X, Li S, Zhao J (2022) Price graphs: utilizing the structural information of ﬁnancial time series for
stock prediction. Inf Sci 588:405–424. https://doi.org/10.1016/j.ins.2021.12.089
46. Cheng D, Yang F, Xiang S, Liu J (2022) Financial time series forecasting with multi-modality graph neural network.
Pattern Recognit 121:108218. https://doi.org/10.1016/j.patcog.2021.108218
47 Xu C, Huang H, Ying X, Gao J, Li Z, Zhang P et al (2022) HGNN: hierarchical graph neural network for predicting the
classiﬁcation of price-limit-hitting stocks. Inf Sci 607:783–798. https://doi.org/10.1016/j.ins.2022.06.010
48. Chen W, Jiang M, Zhang W-G, Chen Z (2021) A novel graph convolutional feature based convolutional neural network
for stock trend prediction. Inf Sci 556:67–94. https://doi.org/10.1016/j.ins.2020.12.068
49. Shi Y, Wang Y, Qu Y, Chen Z (2024) Integrated GCN-LSTM stock prices movement prediction based on knowledge-
incorporated graphs construction. Int J Mach Learn Cybern 15:161–176. https://doi.org/10.1007/s13042-023-01817-6
50 Yin T, Liu C, Ding F, Feng Z, Yuan B, Zhang N (2022) Graph-based stock correlation and prediction for high-frequency
trading systems. Pattern Recognit 122:108209. https://doi.org/10.1016/j.patcog.2021.108209
51. Khoojine AS, Han D (2020) Stock price network autoregressive model with application to stock market turbulence. Eur
Phys J B 93:133. https://doi.org/10.1140/epjb/e2020-100419-9
52. Zhao L, Wang G-J, Wang M, Bao W, Li W, Stanley HE (2018) Stock market as temporal network. Phys A: Stat Mech
Appl 506:1104–1112. https://doi.org/10.1016/j.physa.2018.05.039
53. Anguita D, Ghelardoni L, Ghio A, Oneto L, Ridella S (2012) The ‘‘K’’ in K-fold cross validation. ESANN.
54. Mirza FK, Gu¨rsoy AF, Baykas¸ T, Hekimog˘lu M, Pekcan O¨ (2023) Residual LSTM neural network for time dependent
consecutive pitch string recognition from spectrograms: a study on Turkish classical music makams. Multimed Tools
Appl. https://doi.org/10.1007/s11042-023-17105-y
55 Belhadj M, Aldemir T (1995) The cell to cell mapping technique and chapman-kolmogorov representation of system
dynamics. J Sound Vib 181:687–707. https://doi.org/10.1006/jsvi.1995.0166
56. Barendregt NW, Josic´ K, Kilpatrick ZP (2019) Analyzing dynamic decision-making models using Chapman-Kol-
mogorov equations. J Comput Neurosci 47:205–222. https://doi.org/10.1007/s10827-019-00733-5
57. Breuer H-P, Petruccione F (1995) Stochastic dynamics of open quantum systems: derivation of the differential Chap-
man-Kolmogorov equation. Phys Rev E 51:4041–4054. https://doi.org/10.1103/PhysRevE.51.4041
58. Powell MJD (2004) Least Frobenius norm updating of quadratic models that satisfy interpolation conditions. Math
Program 100:183–215. https://doi.org/10.1007/s10107-003-0490-7
59 Bo¨ttcher A, Wenzel D (2008) The Frobenius norm and the commutator. Linear Algebra Appl 429:1864–1885. https://
doi.org/10.1016/j.laa.2008.05.020
60 Belov DI, Armstrong RD (2011) Distributions of the Kullback-Leibler divergence with applications. British J Math Stat
Psychol 64:291–309. https://doi.org/10.1348/000711010X522227
61. van Erven T, Harremos P (2014) Re´nyi divergence and Kullback-Leibler divergence. IEEE Trans Inf Theory
60:3797–3820. https://doi.org/10.1109/TIT.2014.2320500
62. Ahlgren P, Jarneving B, Rousseau R (2003) Requirements for a cocitation similarity measure, with special reference to
Pearson’s correlation coefﬁcient. J Am Soc Inform Sci Technol 54:550–560
Neural Computing and Applications (2025) 37:15855–15890
123
https://doi.org/10.1007/s00521-025-11325-z
15889

---

## Page 36
63 Hauke J, Kossowski T (2011) Comparison of values of pearson’s and spearman’s correlation coefﬁcients on the same
sets of data. Quaest Geogr 30:87–93. https://doi.org/10.2478/v10117-011-0021-1
64. Kent JT (1982) Robust properties of likelihood ratio tests. Biometrika 69:19–27. https://doi.org/10.1093/biomet/69.1.19
65 McLachlan GJ (1987) On bootstrapping the likelihood ratio test statistic for the number of components in a normal
mixture. J R Stat Soc Ser C Appl Stat 36:318–324. https://doi.org/10.2307/2347790
66. Protassov R, van Dyk DA, Connors A, Kashyap VL, Siemiginowska A (2002) Statistics, handle with care: detecting
multiple model components with the likelihood ratio test. Astrophys J 571:545. https://doi.org/10.1086/339856
67. Hiscott RN (1981) Chi-square tests for Markov chain analysis. J Int Assoc Math Geol 13:69–80. https://doi.org/10.1007/
BF01032010
68 Xuan Vinh N, Chetty M, Coppel R, Wangikar PP (2012) Gene regulatory network modeling via global optimization of
high-order dynamic Bayesian network. BMC Bioinf 13:131. https://doi.org/10.1186/1471-2105-13-131
69. Deng J, Schuller B, Eyben F, Schuller D, Zhang Z, Francois H et al (2020) Exploiting time-frequency patterns with
LSTM-RNNs for low-bitrate audio restoration. Neural Comput Appl 32:1095–1107. https://doi.org/10.1007/s00521-
019-04158-0
70 Mirza FK, Baykas¸ T, Hekimog˘lu M, Pekcan O¨ , Tunçay GP (2024) Decoding compositional complexity: Identifying
composers using a model fusion-based approach with nonlinear signal processing and chaotic dynamics. Chaos Solitons
Fractals 187:115450. https://doi.org/10.1016/j.chaos.2024.115450
71. Karim F, Majumdar S, Darabi H, Chen S (2018) LSTM fully convolutional networks for time series classiﬁcation. IEEE
Access 6:1662–1669. https://doi.org/10.1109/ACCESS.2017.2779939
72. Darling DA (1957) The Kolmogorov-Smirnov, Crame´r-von Mises tests. Ann Math Stat 28:823–838
73. Lilliefors HW (1967) On the Kolmogorov-Smirnov test for normality with mean and variance unknown. J Am Stat
Assoc 62:399–402. https://doi.org/10.1080/01621459.1967.10482916
74. Massey FJ Jr (1951) The Kolmogorov-Smirnov test for goodness of ﬁt. J Am Stat Assoc 46:68–78. https://doi.org/10.
1080/01621459.1951.10500769
75. Marozzi M (2011) Levene type tests for the ratio of two scales. J Stat Comput Simul 81:815–826. https://doi.org/10.
1080/00949650903499321
76 Wang Y, Tang M, Wang P, Liu B, Tian R (2022) The Levene test based-leakage assessment. Integration 87:182–193.
https://doi.org/10.1016/j.vlsi.2022.06.013
77 Carroll RJ, Schneider H (1985) A note on levene’s tests for equality of variances. Stat Probab Lett 3:191–194. https://doi.
org/10.1016/0167-7152(85)90016-1
78. Ersoy E, Li H, Schaffer ME, Szendrei T (2024) Stacking regression for time-series, with an application to forecasting
quarterly US GDP growth. In: Ngoc Thach N, Kreinovich V, Ha DT, Trung ND (eds) Optimal transport statistics for
economics and related topics. Springer Nature Switzerland, Cham, pp 131–149
79. Xu X, Zhang Y (2023) A Gaussian process regression machine learning model for forecasting retail property prices with
Bayesian optimizations and cross-validation. Decis Anal J 8:100267. https://doi.org/10.1016/j.dajour.2023.100267
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.
Authors and Afﬁliations
Fuat Kaan Mirza1
• O¨ nder Pekcan1 • Mustafa Hekimog˘lu1 • Tunçer Baykas¸1
& Fuat Kaan Mirza
kaan.mirza@khas.edu.tr
O¨ nder Pekcan
pekcan@khas.edu.tr
Mustafa Hekimog˘lu
mustafa.hekimoglu@khas.edu.tr
Tunçer Baykas¸
tbaykas@ieee.org
1
Faculty of Engineering and Natural Sciences, Kadir Has University, 34083 Cibali, Istanbul, Turkey
123
Neural Computing and Applications (2025) 37:15855–15890
15890
https://doi.org/10.1007/s00521-025-11325-z

---
