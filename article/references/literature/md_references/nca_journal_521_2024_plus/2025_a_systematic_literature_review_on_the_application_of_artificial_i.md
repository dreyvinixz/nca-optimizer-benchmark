# A systematic literature review on the application of artificial intelligence techniques for rock strength estimation

**Year**: 2025 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-025-11517-7

---

## Page 1
REVIEW
A systematic literature review on the application
of artificial intelligence techniques for rock strength
estimation
Stephen Akosah1
• Ivan Gratchev1
• Solomon S. R. Gidigasu2
Received: 7 October 2024 / Accepted: 9 July 2025 / Published online: 31 July 2025
 The Author(s) 2025
Abstract
This paper presents a systematic literature review on the prediction of unconﬁned compressive strength (UCS)
and elastic modulus (E) with artiﬁcial intelligence (AI) models. The study categorises three essential parts: (1) a
combination of physical and mechanical properties, (2) mechanical properties, and (3) physical properties as input
parameters for AI models in estimating UCS and E. The review selection was based on search keywords using
title-abstract, full-text, and keywords from Scopus and Web of Science online database libraries. A total of 131
peer-reviewed research articles published from 2014 to 2024 were critically reviewed to provide answers to
research-related questions related to current advancements in the prediction of UCS and E with AI models.
Among the AI technologies analysed, artiﬁcial neural networks (ANN) and ANN-based models stand out as the
most used AI algorithms; other algorithms, including ANFIS, RF, SVM, and XGBoost model, have been used at
signiﬁcant levels in predicting UCS and E with high prediction accuracy of R2 greater 0.90 with minimum mean
error margins. The ANN (24.7%), ANFIS (11.7%), and RF (7.6%) have been essentially employed in many
research studies to predict rock strength. The study combined mechanical and physical properties with AI models
at approximately 59%, and after that, mechanical properties at 23.6%. The efﬁciency of AI algorithms and their
application is associated with the usage of data and input parameters. This review recommends future study gaps
and places emphasis on integrating rock mechanics, physical laws (Mohr–Coulomb and Hoek–Brown failure
criteria) and adaptive AI techniques to advance the adaptability and reliability in predicting rock strength and
deformation characteristics.
Keywords Compressive strength  Artiﬁcial intelligence  Rocks  Elastic modulus  Physical–mechanical
properties  Prediction
Abbreviations
AI
Artiﬁcial intelligence
ANFIS
Adaptive neural fuzzy inference system
ANN
Artiﬁcial neural network
ML
Machine learning
DL
Deep learning
UCS
Unconﬁned compressive strength
UCT
Unconﬁned compressive test
RF
Random forest
SVM
Support vector machine
Neural Computing and Applications (2025) 37:20721–20753
https://doi.org/10.1007/s00521-025-11517-7
123
Neural Computing and Applications (2025) 37:20721–20753

---

## Page 2
ICA
Imperialist competitive algorithm
XGBoost
Extreme gradient boost
FIS
Fuzzy inference system
ELM
Extreme learning machine
CNN
Convolutional neural network
DNN
Deep neural network
RNN
Recurrent neural network
MLP
Multi-layer perceptron
GEP
Gene expression programming
LSSVM
Least square support vector machine
CART
Classiﬁcation and regression tree
KNN
K-nearest neighbours
MLR
Multiple linear regression
COA
Cuckoo optimisation algorithm
GP
Gaussian process
MPMR
Minimax probability machine regression
BPNN
Back propagation neural network
SANN
Subtree-based attention neural network
GA
Genetic algorithm
RMSE
Root mean square error
MSE
Mean square error
CFNN
Cascaded forward neural network
AAPE
Average absolute percentage error
LMA
Levenberg–Marquardt algorithm
BPNN
Back propagation neural network
LOG
Laplacian of Gaussian
MELM
Multi-layer extreme learning machine
COA
Cuckoo optimisation algorithm
TS
Tensile strength
BTI
Brazilian tensile index
BPI
Block punch index
PSO
Particle swarm optimisation
SLR
Systematic literature review
E
Elastic modulus
GFFN
Generalised feedforward network
MAPE
Mean average percentage error
GPR
Gaussian process regression
GBDT
Gradient boost decision tree
OB
Bayesian optimisation
SCM
Subtractive clustering method
MAPE
Mean absolute percentage error
M5T
Tree-based machine learning
GWO
Grey Wolf optimiser
KELM
Kernal extreme learning machine
SSA
Singular spectrum analysis
RVM
Relevance vector machine
MVRA
Multivariable regression analysis
VAF
Variance account for
123
Neural Computing and Applications (2025) 37:20721–20753
20722
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 3
MAE
Mean average error
List of symbols
Vp
P-wave velocity
Rn
Schmidt hammer rebound number
Is(50)
Point load index
BPI
Block punch index
qd
Dry density
n
Porosity
Qtz
Quartz
Plg
Plagioclase
q
Density
e
Poisson ratio
mc
Moisture content
Ab
Water absorption
md
Dynamic poisson ratio
Vs
S-wave velocity
qs
Saturates density
b
Serpentinisation percentage
cd
Dry unit weight
cs
Saturated unit weight
Ed
Dynamic Young’s modulus
ne
Effective porosity
ld
Dynamic Poisson ratio
Fr
Feldspar
Fg
Fragments
nt
Total porosity
Ct
Compression time
St
Shear time
Kpr
Alkali feldspar
Chl
Chlorite
c
Dry unit weight
1 Introduction
Rock strength prediction is vital in many industries for optimising operations, ensuring stability and safety, and
reducing project costs. The application of rock strength ranges from civil and mining engineering to energy
production and environmental management [1, 2]. The accurate unconﬁned compressive strength (UCS) and
elastic modulus (E) of rock data offer information for decision-making in designing efﬁcient and safe projects to
minimise risk to human life and the environment. By integrating more advanced prediction techniques, such as
artiﬁcial intelligence (AI) models, into rock strength assessment, it is possible to enhance the prediction accuracy
and reliability of rock strength properties, including UCS and E, proﬁting from a vast range of real-world
applications.
The rock strength parameter, such as UCS, is a signiﬁcant parameter for design and stability analysis, espe-
cially when rocks are under compressive stresses [3], and it can be obtained through a series of laboratory tests
[4, 5]. The most common laboratory test is the unconﬁned compression test, UCT, which provides rock strength
characteristics like uniaxial compressive strength, UCS, and elastic modulus, E. The UCT is a straightforward
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20723

---

## Page 4
method used to evaluate the UCS of rocks. Nonetheless, some challenges exist in determining UCS and E with
UCT. For instance, acquiring a high-quality rock core is a challenge, notably for highly weathered and frag-
mented rock masses [6]. Additionally, UCT has several disadvantages, such as being expensive and time-
consuming [7]. Therefore, several empirical models have been developed based on simple and multiple regression
methods with different rock strength properties from direct and indirect test results to estimate UCS and E.
An indirect and direct measurement approach including P-wave velocity (Vp), density, Schmidt hammer
rebound number (Rn), and point load index (Is(50)) has been used due to the high cost of UCT equipment for
predicting rock strength is more favourable and appropriate as these tests are economical and easy to carry out [8].
Is(50) [9, 10], Rn [11, 12], and Vp [13, 14] are widely utilised to predict UCS and E using simple and multiple
regressions. The indirect and direct estimation techniques of UCS and E have been considered in the literature and
developed several empirical models using linear simple regression analysis [7, 15], multiple regression methods
[16, 17], and nonlinear regression analysis [18, 19] with a meaningful relationship between UCS and E. In the
other studies by [20, 21], the correlation of indirect test parameters did not provide reliable values for UCS and E.
For example, Mohamad et al. [22] studied the correlation between Is(50) and UCS, classifying the Penang Island
granitic rock from weak (24.76 MPa) to very strong (156.82 MPa). Through simple and multiple regression
methods, Minaeian and Ahangari [23] investigated UCS with indirect methods, including Vp and Rn to estimate
the relationship of UCS. Using RMSE and VAF, they noticed 94.34 and 1.56 regarding Vp and UCS and 94.39
and 1.6 between UCS and Rn through a simple regression model. Meanwhile, through multiple regression
analysis for UCS, 97.24 and 1.34 were achieved. However, different empirical models have been reported on
estimating UCS and E; there is no conclusive generalised empirical equation for rocks [24]. The empirical models
from most of the studies are site-speciﬁc and applicable to a particular area [25], with low accuracy [24], and
empirical rock techniques involve experience, observation, and personal judgement [26]. In order to deal with
these shortcomings of empirical techniques, AI methods are introduced for predicting UCS and E using direct and
indirect test results.
In the past decade, many scholars have proposed AI algorithms capable of predicting UCS and E of rocks
[7, 27, 28]. The AI algorithms commonly used in predicting UCS include ANN [29–31], ANFIS [32–36], RF
[35, 36], XGBoost [37], and SVM [38]. Among the AI algorithms, ANN is the most widely used technique to
predict rock UCS and E. For example, some scholars have used hybrid optimised algorithms, including ICA-
ANN and PSO-ANN, to estimate UCS and E [15, 39, 40]. In addition, ANFIS and ANFIS-based subtractive
clustering methods (ANFIS-SCM) have also been utilised to predict the UCS and E [32, 41, 42]. The above AI
models were reported to demonstrate accurate predictions of UCS and E. Also, the AI models were noticed to
perform better than the empirical models. The call for the use of AI models in predicting UCS and E of rock relies
on the AI model’s ability to deal with nonlinear, complex, and multidimensional data. AI models provide rapid
and more accurate predictions, are cost-effective and adapt to new data. Additionally, AI models provide sig-
niﬁcant advantages in terms of scalability, ﬂexibility, and efﬁciency, making AI techniques gain currency in
geotechnical engineering and rock mechanics compared to traditional empirical methods.
Besides the AI algorithms mentioned above, numerous effective AI models have been adopted to forecast UCS
and E, including XGBoost, SVM, and CNN. Liu et al. [43] estimated the UCS of sandstone, exploring the
framework of boost trees, XGBoost, AdaBoostM, and CGBoost. Also, Sun et al. [44] innovatively used CNN and
X-ray computer tomography methods to estimate rock UCS. Cao et al. [37] developed an algorithm based on
XGBoost with ﬁreﬂy algorithm (XGBoost-FA) to sumise UCS and E, comparing the XGBoost-FA with RBFN
XGBoost and SVM the proposed XGBoost-FA algorithm achieving R2 of 0.99. To investigate the UCS, non-
destructive tests like Vp, ne, and Rn were used by Skentou et al. [28] with ANN-PSO, ANN-LM, and ANN-ICA
algorithms and noticed R2 of 0.96 for ANN-LM compared to the other algorithms. Jahed et al. [32] used the
ANFIS algorithm to estimate UCS and E of Pahang-Selangor granitic rock from Malaysia adopting Vp, density,
plagioclase, and quartz. They used Vp, density, plagioclase, and quartz as the input parameters for the ANFIS
algorithm, reporting R2 of about 0.99 and 1.0 for UCS and E, respectively.
123
Neural Computing and Applications (2025) 37:20721–20753
20724
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 5
There are a sizable number of the literature on estimations of rocks UCS and E applying AI techniques, both
traditional and hybrid algorithms, including ANN, FIS, ELM, RF, BO, ANN-TLBO, PSO–LSSVM, and ANN-
PSO [45–49]. Although AI methods have considerable advantages and promising features in rock mechanics and
engineering, there are still limitations. A signiﬁcant research gap exists in applying advanced and adaptive AI
models in rock mechanics. Recent studies predominantly depend on long-established AI methods, with limited
studies on promising deep and reinforcement AI algorithms, potentially improving modelling reliability and
predictability. Additionally, there is a signiﬁcant need to integrate AI algorithms with physical theories to enhance
consistency and pragmatical understanding. Enhancing the robustness of AI-driven rock mechanics and engi-
neering solutions can be achieved by addressing the gaps.
This paper conducts a systematic literature review (SLR) to thoroughly explore the usage of AI techniques in
rock engineering solutions. This review covers relevant peer-reviewed research articles published from 2014 to
2024. The objective of this review is to provide answers to the questions presented in Table 1. The SLR will
provide further research based on the usage of AI methods in calculating UCS and E. AI applications in
estimating UCS and E will highlight the potentials, available methods, and challenges. The SLR will also ﬁll an
essential gap in the literature. Additionally, the SLR will identify key areas for future research prospects.
2 Material and methods
2.1 Synopsis of SLR procedures
The protocol of this SLR adhered to three categories: (1) planning stage, (2) execution, and (3) discussion stages,
as illustrated in Fig. 1. The SLR approach offers a synopsis of a primary study on a speciﬁc research subject that
scientiﬁcally identiﬁes, to choose from, assesses, and synthesises all quality evidence pertinent to that research
theme or topic [50]. The PRISMA standard protocols [51, 52] were followed to develop this SLR. PRISMA
guidelines are a universally accepted method that provides a checklist that is strictly applied in this work. This
technique enhanced the quality assurance of the revision process and ensured its replication.
3 Research article search
The systematic search of articles was conducted across two databases, speciﬁcally the most widely known
libraries, Scopus and Web of Science (WoS) online library databases, as in Table 2. Table 2 summarises the
keywords employed to search the articles from the two databases relevant to the research topic by applying the
‘‘Boolean operators.’’ The keyword combination in the table was applied using the two databases through Grifﬁth
University’s online library system. The keywords used helped to facilitate the identiﬁcation of high-quality
literature from WoS and Scopus, which was screened using the PRISMA protocol. In addition, the PRISMA
Table 1 Quality assessment criteria for initial articles search
Research objective
Number
Questions
Research problems for the planning review
Main
Which AI algorithms have been used in the literature to predict UCS and E?
Sub-questions
1
What techniques are included in AI?
2
What are the features of available AI techniques?
3
How can AI techniques be used to predict UCS and E?
4
What are the projections and future research trends?
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20725

---

## Page 6
technique provides an avenue to describe article collections and sorting, as in Table 2. It should be noted that only
peer-reviewed journal articles published from 2014 to 2024 were selected for this paper.
3.1 Screening, exclusion, and inclusion criteria
A total of 3263 records were obtained from WoS and Scopus online library databases. In the initial screening
processes, 750 duplicates were removed utilising the EndNote-21 reference manager tool. Next, 2513 documents
were assessed in the EndNote-21 considering the title and abstract. Two hundred three (200) articles were
recognised as hypothetically qualiﬁed after excluding 3063, as they fall outside the search criteria. The 200
articles (full text) were downloaded using the EndNote reference manager for further screening in Covidence
software version 2.0.
Two reviewers independently screened each research article using Covidence software version 2.0, and the
outcomes were assessed to conﬁrm the impartiality of the review procedure using all criteria in Table 3. It was
then followed by a thorough elimination of articles that did not have academic relevance and were unrelated to AI
models in predicting UCS and E. After the covidence full-text screening, 97 full-text articles were excluded, as
they fell out of the exclusion and inclusion criteria. Finally, 103 full-text articles were considered eligible for
content analysis. The study excluded conference proceedings, book chapters, and grey literature, including
(nonofﬁcially published articles by a journal) as described in Sect. 2.5. The literature search included research
Fig. 1 The research process of this SLR
Table 2 Keywords, controllers, and early search outcomes from Scopus and WoS databases online library
Database
Search keys and strainers utilised
Search
outcomes
Scopus
TITLE-ABS-KEY ((rock OR UCS OR AI OR ML OR DL) AND (SVM OR elastic modulus OR UCS OR ANN)
AND (rock OR CNN OR UCS)
Reﬁned By: Area of Study: Engineering: Publication Year: All Language: English
1763
WoS
AB = ((rock OR UCS OR AI OR ML OR DL) AND (SVM OR elastic modulus OR UCS OR ANN) AND (rock OR
CNN OR UCS)
Reﬁned By: Area of Study: Engineering: Publication Year: All Language: English
1503
WoS web of science
123
Neural Computing and Applications (2025) 37:20721–20753
20726
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 7
articles published only in English to ease translation and avoid confusion. In addition, the English language is
widely used in academic research, with a considerable number of published scholarly research articles and other
relevant documents.
Further, 28 more records were included, which were obtained from reference lists in some of the articles
included in this study. Ultimately, the full texts of 131 articles were studied. The assessment criteria and the SLR
approaches were adopted to ensure neutrality and fairness during the literature selection. Figure 2 summarises the
study procedure in the PRISMA ﬂow chart. A SLR protocol was developed to outline the criteria for research
article selection, record search plan, data retrieving, and analysis procedures, which are shown in Fig. 2. The
search only included peer-reviewed literature to ensure scientiﬁc rigour. Grey literature, reviews, conference
papers, and book chapters were intentionally excluded with the assumption that they were indirectly captured and
expanded upon in scientiﬁc texts.
Table 3 Quality evaluation criteria
Number
Criteria
Inclusion/eligibility criteria
Exclusion criteria
1
Timeline
2014–2024
Before 2014
2
Literature type
Full research articles retrieved
The research articles that are not fully accessed
3
Topic
The topic relevant to the UCS, E and AI models
The topic that is not related to AI models, UCS and E
4
Peer-reviewed
Peer-reviewed scientiﬁc articles
Not peer-reviewed
5
Clear research
content
Articles with explicit research titles, abstracts and
keywords
Articles with no explicit research titles, abstracts and
keywords
6
Rock type
Studies based on natural rocks only
Studies conducted on concrete blocks and rock-like
material
7
Language
Articles in English language
Articles not in English language
Databases (n = 2)
Web of Science, WoS (n = 1763)
Scopus (n = 1503)
Screening of 2,513 through title,
abstract and full text
750 duplicates
removed
Articles excluded (n = 2,390)
Non-peer-reviewed,
review articles,
not accessible or
English language
103 potentially eligible
papers were
considered
131
sudies were included
in quanlitative
synthesis
28 additional study included
from reference lists
Identification
Screening
Eligibility
Inclusion
Search included all fields:
geomechanics, rock mechanics,
geotechnical and mining
Scopus and Web of Science field search
labelled 'Topic' included title, abstract, full
text, authors keywords and keywords plus
Fig. 2 Summary of SLR
process: visualisation of
adopted process from
Prisma [53]
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20727

---

## Page 8
3.2 Data extraction
The 131 research articles after full-text screening in the Covidence software version 2.0 were extracted into
Microsoft Excel 365, which includes the author(s) name, year of publication, keywords, and other relevant
information on prediction UCS and E with AI algorithms, physical, and mechanical properties of natural rocks
from direct and indirect tests results and the relevant model accuracy metrics in these studies. A meta-analysis
was conducted based on the information acquired from the publications retrieved in this study. Each paper
comprehensively reviewed the rock types and important AI model input parameters.
3.3 Studies limitations
The primary limits of this study are (1) articles published in the English language that vetoed the inclusion of
articles published in another language on the topic, the selection of English language only was to avoid trans-
lation, misinterpretation, misrepresentation of articles not in the English language, (2) the choice of a speciﬁc
database skewed the search outcomes, and (3) the ﬁltered keywords search approach may disregard some vital
keywords. The restrictions may limit the realm of this review. However, efforts were put in place to alleviate
possible preferences and guarantee the vigour of the outcomes via the adopted methodology. Furthermore, the
SLR technique facilitates an utter check of the existing research articles, giving beneﬁcial comprehension into AI,
UCS, and E.
4 Results and discussion
4.1 Publication information and geographical context
Between the years of 2014 and 2024, all studies (n = 131) were peer-reviewed and published. Approximately
34% of research was produced from 2014 to 2019, after which most research (n = 85) was published in the last
5 years, as illustrated in Fig. 3(a). The most research articles (n = 22) were published in the 2022 ﬁscal year. As
exhibited in Fig. 3(b), the majority of the studies were conducted in China (n = 36), Iran (n = 31), India and
Turkey (n = 12 each), Malaysia (n = 11), Saudi Arabia and Greece (n = 6 and 3) each, 14 countries (n = 1 and
2014
2016
2018
2020
2022
2024
2
4
6
8
10
12
14
16
18
20
22
24
Sundan
UAE
Pakistan
Nigeria
Ghana
Russia
Kenya
Chile
Canada
Tunisia
Jordan
Vietnam
France
Iraq
Greece
Saudi Arabia
Malaysia
Turkey
India
Iran
China
0
5
10
15
20
25
30
35
40
Number of studies
Country
(a)
(b)
Year
Studies
Fig. 3 a Growth of scien-
tiﬁc production of research
articles per year on rock
UCS and AI; b geographi-
cal distribution of research
articles’ primary authors
123
Neural Computing and Applications (2025) 37:20721–20753
20728
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 9
2) articles each. Several studies conducted in some parts of the world are constrained. The column graph indicates
that substantial efforts must be considered in diverse parts across the globe to institute the utilisation of AI
algorithms in rock mechanics and engineering. It should be noted that many research articles were retrieved from
2023 to 2024 on studies involving the prediction of rock strength properties with AI models. However, per the
research objectives and focus, only a few articles meet the criteria set for this study, and this is the reason there is
a decrease in articles produced after 2022.
5 Keywords co-occurrence analysis
Figure 4 illustrates the co-occurrence of research keywords comprising computational methods with an AI
algorithms skeleton for the last decade (2014–2024), including a total of 233 individual keywords, using
VOSviewer software version 1.6.20. VOSviewer constructs a network and visualises bibliometrics based on the
co-occurrence of keywords in the form of linked clusters and generates a cluster map. Each node in Fig. 4
corresponds to a keyword, with the node size implying occurrence frequency. The keyword size demonstrates the
centrality and establishes the track of recognition in a research subject. Conspicuously, the crucial keywords in
Fig. 4 are the adaptive neuro-fuzzy inference system, artiﬁcial neural networks, uniaxial compressive strength,
rocks, rock properties, and elastic modulus. The linking lines joining the keywords imply the correlations, with
the thick lines demonstrating the rate of occurrence.
By analysing the rate of keywords within the research domain, VOSviewer performed some statistical analysis
to examine all the keywords listed in Table 4. The 10 keywords comprise the core ideas and associations in the
domain of this review. Logically, the prevailing term is ‘‘artiﬁcial neural network.’’ Additionally, keywords like
‘‘uniaxial compressive strength,’’ ‘‘granite,’’ and ‘‘elastic modulus’’ indicate the deep focus on advances in AI
algorithms and prediction models’ performance in recent studies on rocks. The existence of the ‘‘machine
learning’’ keyword highlights the already extensive exploitation of machine learning technologies. Simultane-
ously, the presence of ‘‘nondestructive testing’’ and particle swarm optimisation keywords also highlights the use
of indirect physical and mechanical properties in predicting UCS and E. The particle swarm optimisation
demonstrates the exploration of hybrid AI algorithms to determine rock strength.
Fig. 4 Keywords and co-
occurrence diagram
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20729

---

## Page 10
The illustrated cluster net map of computational mechanisms in AI frameworks is profound and satisfying,
with discerning coherent connections of linking themes. The incorporation of AI models, like adaptive neuro-
fuzzy inference systems, fuzzy inference systems, and hybrid particle swarm optimisation into the orthodox scope
of rock mechanics, has advanced the prediction and evaluation of rock strength and deformation characteristics.
6 Synopsis of used AI methods
AI is a general canopy beneath which machine (ML) and deep (DL) learning fall. The overarching concept of AI
encompasses creating machines capable of mimicking tasks typical of human intelligence. ML and DL provide
advanced tools, including neural networks and their architecture, to enhance and execute complicated tasks.
Numerous traditional learning models are available in the literature, for example, ANN, ANFIS, CNN, DNN, RF,
SVR, SVM, BP, FIS, MLP, RNN, and LSTM. Among the AI models mentioned in the previous sections, ANN
and ANN-based models are the most commonly used by researchers in the ﬁelds of rock mechanics and
engineering and geotechnical engineering. An artiﬁcial neural network (ANN) effectively links input geotechnical
and geometrical parameters, such as uniaxial compressive strength (UCS), density, porosity, Schmidt rebound
hardness, Brazilian tensile strength, point load index, and P- and S-wave velocities to the desired output by
learning from the training data.
The AI algorithms present unique features that make them appropriate for various applications in science and
engineering. Table 5 summarises the advantages and limitations of some commonly used AI algorithms in the
literature. Understanding each algorithm’s advantages and limitations is essential for selecting an appropriate
learning algorithm when facing a particular research task. Additionally, hybrid algorithms and ensemble learning
approaches can be utilised effectively, integrating diverse learning algorithms for complex tasks to achieve robust
accuracy. Furthermore, an integrated approach is especially beneﬁcial for tackling complex problems that need
multi-step solutions and involve diverse data types. However, using a combination of AI algorithms can achieve
more effective results.
The employment of selecting suitable AI algorithms requires performance metrics and validation methods,
which enable rigour accuracy assessment of efﬁcient performance. Efﬁcient and resource-efﬁcient integration of
AI algorithms in predicting UCS and E requires careful optimisation and adjustments due to limited resources and
computational power. AI algorithm’s effectiveness is typically evaluated using RMSE, accuracy, F1-score,
precision, and recall metrics, as presented in the equations below [58]. The methods validate AI model reliability
by testing them on diverse datasets, ensuring smooth integration into geotechnical engineering challenges through
optimisation and adjustments.
Table 4 Catalogue of
occurrences and keywords
obtained from 233 distinct
themes
Keyword
Occurrence
Artiﬁcial neural network
26
Uniaxial compressive strength
25
Adaptive neuro-fuzzy inference system
11
Machine learning
8
Granite
5
Modulus of elasticity
5
Fuzzy inference system
4
Multiple regression
4
Nondestructive testing
3
Particle swarm optimisation
3
123
Neural Computing and Applications (2025) 37:20721–20753
20730
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 11
Accuracy ¼
TP þ TN
TP þ TN þ FP þ FN
ð1Þ
Pr ecision ¼
TP
TP þ FP
ð2Þ
Recall ¼
TP
TP þ FN
ð3Þ
F1  score ¼ 2 
P  R
P þ R


ð4Þ
RMSE ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
n
X
n
i¼1
yn  yp

2
s
ð5Þ
where TP: true positive, TN: true negative, FP: force positive, FN: force negative, P: precision, R: recall, yn: is the
measured value, yp: is the mean of the measured value, and n is the absolute number of data.
7 Application of AI models in predicting UCS and E of rock
This section explores AI algorithms’ application in predicting UCS and E using physical and mechanical
properties as documented in the literature. The ﬁrst section presents the breakdown of subdomains typically used
as input parameters and a brief statistical analysis of AI algorithms available in the literature on estimating UCS
Table 5 Advantages and limitations of some developed AI models
AI
algorithm
Advantages
Limitations
References
ANN
Capable of predicting UCS with microfabric images, mainly
from weak and highly stratiﬁed fractured rock
The problem is the opaqueness of the underlying
relationship between inputs and outputs, often called
the ‘‘black box.’’
Ali et al.
[54]
ANFIS
Best prediction with random sets of data
It requires broad ideas to establish relationships between
different parameters and depends on membership
functions
Umrao
et al. [55]
RF
Minimal inﬂuence by hyperparameters, fast convergence
speed, resistance to overﬁtting and noise insensitive to
data, as well as best predictability
The predictive model is complex to explain physically
and cannot reveal the mechanisms of the inﬂuence of
input parameters on UCS
Wang et al.
[36]
SVM
Provide sufﬁcient accuracy for predicting intact rock UCS
Unsuitable for extensive data when faced with data noise
and not capable of using a probabilistic explanation
Cemiloglu
et al. [38]
DNN
Predict UCS and E with high accuracy
The algorithm is prone to overﬁtting due to the different
number of parameters learned during the model
building
Azarafza
et al. [56]
FIS
It emerges as a competent model because of its efﬁciency in
dealing with impreciseness and handling uncertainties in
test data with high accuracy
It depends on membership function variables and fuzzy
‘‘if–then’’ rules involving user interference
Heidari
et al. [57]
CNN
Shows superior performance for predicting UCS of rock
with CT-scanned image datasets
It requires data from high-resolution X-ray scanning to
calculate UCS
Sun et al.
[44]
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20731

---

## Page 12
and E. The three primary domains identiﬁed are (a) physical–mechanical properties, (b) mechanical properties,
and (c) physical properties.
7.1 Breakdown of input parameters typically used for predicting UCS and E
Figure 5(a) provides the breakdown of the subdomain identiﬁed. Geotechnical materials like rocks have
mechanical properties, including BTS, Is(50), Vp, BPI, modulus, and Rn, and physical properties such as density,
porosity, quartz content, plagioclase, and particle size. It is clear from the ﬁgure that the majority of studies
involve a combination of physical–mechanical properties as model input parameters (n = 75), followed by
mechanical properties (n = 33) and then physical properties (n = 23) for predicting UCS and E. Fig-
ure 5(b) presents the percentage distribution of different physical and mechanical properties and the combination
of physical and mechanical properties used as input parameters with AI algorithms in estimating UCS and E. As
observed in Fig. 5(b), most studies utilised the combination of physical–mechanical parameters in predicting
UCS and E, representing 57.3%. The reason could be that the incorporation of the combination of physical and
mechanical properties of rock with AI models allows for better accuracy, holistic, and generalisation in the
prediction of UCS and E. The combination of the two properties can help to capture the complex nature of the
multi-facet of rock, which leads to enhanced performance in estimating the UCS and E of different rocks under
various geological and environmental conditions and in diverse rock mechanics and geotechnical engineering
applications. Additionally, the combination of physical and mechanical properties helps reduce the risk of AI
models overﬁtting.
The combination of physical and mechanical properties amounts to 23.6%. The mechanical properties are
directly related to rock strength behaviour, and data from mechanical properties provide high prediction accuracy.
However, the physical properties of the enormous quantity of rock samples may sometimes be practicable, as AI
models require extensive data. The mechanical properties were observed to be used as input parameters for AI
models, provide better performance, reduce data complexity, and enhance models’ interpretability in situations
where there are limited datasets. Physical properties as input represent 17.3% of the research articles reviewed.
The physical properties are easily determined and interpreted, and they are cost-effective in terms of resources
and time compared to the mechanical testing of rock. They have a strong correlation in predicting UCS and E, but
(a)
(b)
Physical
properties
Mechanical
properties
Physical-mechanical
properties
0
10
20
30
40
50
60
70
80
Number of studies
Key areas of research in predicting UCS and E
57.3%
25.2%
17.6%
Physical properties
Mechanical properties
Physical-mechanical properties
Total :
131
Fig. 5 Distribution of physical and mechanical properties and AI across subdomains in estimating UCS and E: a number of
studies utilising AI, direct, and indirect rock properties in different key areas, b percentage distribution of rock properties
employed as input parameters with AI models
123
Neural Computing and Applications (2025) 37:20721–20753
20732
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 13
some physical properties, including density and porosity, provide variability, which may inﬂuence the accurate
prediction of UCS and E.
It should be noted that due to the large data requirement for AI models, most of the studies combined physical
properties, mechanical properties, and a combination of physical–mechanical properties data from different
sedimentary and igneous rocks from the same or different geological environments as input parameters for
predicting UCS and E. The combination of different rock data from various sources was found more in the studies
involved in the physical–mechanical properties compared to the physical and mechanical properties.
7.2 Statistical analysis of available AI algorithms
Several AI algorithms have been progressed over the past ten years, from 2014 to 2024. Figure 6 presents the
distributions of various AI algorithms and a breakdown of all the AI techniques utilised in rock mechanics for
estimating UCS and E. The most predominant are ANN-based algorithms (23.4%), ANFIS-based (11.3%), and
RF (8.4%) algorithms employed in evaluating or predicting UCS and E with mechanical and physical properties,
as displayed in Fig. 6(a). It can observed from Fig. 6(b) that the use of ANN and ANFIS models has been
adopted in predicting UCS and E from the 2014 ﬁscal year to date. The application of the RF model has also
drawn attention from 2018 to date among researchers in the ﬁeld of rock mechanics to estimate UCS, and E.
Recent studies have also used models, such as XGBoost, RVM, and BP models due to their capability of
predicting UCS and E. It is worth noting that in the stack column graph in Fig. 6(b), a single research article can
utilise multiple AI models, resulting in some AI models used more than the number of papers reviewed in this
study.
From the statistical point of view, ANN, ANFIS, SVM, RF, FIS, GEP, and XGBoost hold signiﬁcant
prominence in predicting UCS and E using rock mechanical and physical properties. Traditional ANN and ANN-
based algorithms have been used especially due to their capability and robust adaptability in dealing with
nonlinearities [7, 37, 39, 59, 60]. For instance, Ali et al. [54] predicted the UCS of amphibolite using microfabric
properties, including grain size, quartz content, and shape factor. The study employed multivariate regression
(MR), fuzzy inference system (FIS), and artiﬁcial neural network (ANN) and compared their predictive
2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024
0
5
10
15
20
25
30
35
40
45
50
Number of studies
Year of research article publication
ANN
GEP
XGBoost
KNN
MLR
LSSVM
SVR
ELM
BP
MLP
RVM
RF
ANFIS
SVM
FIS
LSTM
Others
(a)
(b)
AI models
2.5% 2.9%
2.5%
3.3%
4.2%
8.4%
3.3%
3.3%
2.5%
11.3%
4.6%
2.1%
4.6%
2.1%
23.4%
1.3%
17.6%
Fig. 6 Breakdown of vari-
ous AI techniques in the
literature for predicting
UCS and E: a distribution
of AI algorithms adopted in
the literature. b the research
trends of various AI models
utilised from 2014 to 2024
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20733

---

## Page 14
capabilities. After the evaluation of models according to performance indices like R2, RMSE, and VAF, all the
models showed reasonable predictions. However, the ANN outperformed the other models with R2 of 0.95,
RMSE of 3.42, and VAF of 97.9%. Aghda et al. [42] also estimate the UCS and E of Asmari limestone with
ANFIS and MR models utilising Brazilian tensile strength (BTS), porosity (n), and density (q) as inputs. The
research uses 655 rock datasets, with 436 of the data used for model construction, and veriﬁes the model with
219. The ANFIS after model construction and veriﬁcation demonstrated high prediction accuracy compared to
MR models, with VAF and RMSE values ranging from 90 to 95% and 6.86–8.94, respectively, demonstrating an
excellent prediction of UCS and E compared to multiple regression methods.
Gowida et al. [33] explore the ANN, SVM, and ANFIS models to estimate UCS of rocks in real time during
drilling operations using real-time drilling mechanical properties, such as standpipe pressure, penetration rate,
rotary speed per minute, bit weight, mud pumping rate as models input parameters. Their studies demonstrated
that the ANN model has the advantage over SVM and ANFIS models in predicting UCS in real time with high
prediction accuracy with R2 of 0.99 and AAPE of 3.5%. Using SVM and physical and mechanical properties of
Maragheh limestone, Cemiloglu et al. [38] predicted the UCS of the rock with a high accuracy of 0.91, precision
of 0.86, R2 of 0.97, and a low error rate (MAE = 0.45, RMSE = 0.41 and MSE = 0.44) compared to the
traditional ﬁtting curves. The researchers suggested that the SVM model used is not suitable for large datasets and
also not valid for probabilistic explanations for classiﬁcation (SVM classiﬁer). Matin et al. [35] explore the
utilisation of the RF algorithm in predicting the UCS and E of travertine rock, focusing on selecting important
variables used as the model input parameter (n, Vp, Is(50), and Rn). They concluded that the RF model can predict
UCS and E with R2 of 0.91 and 0.93, respectively. The Vp was found to be the most important variable in
predicting UCS and E.
Heidari et al. [57] focus on developing predictive models to estimate the UCS of sedimentary rocks using
multiple regression (MLR) and a Sugeno-type fuzzy inference system (FIS). The block punch index (BPI), Vp,
Is(50), and Rn were used as model parameters. It was noted from the study that both FIS and MLR perform well in
predicting UCS of the sedimentary rocks, with VAF of 90% for both models and RMSE of 10.80 and 12.82 for
FIS and MLR, respectively. The GEP has been used successfully to estimate the UCS of sandstone with input
indices such as n, BTS, and slake durability. The GEP was compared with linear multiple regression (LMR), and
it was found to be superior to LMR with an R2 of 0.965 [61]. Currently, an explainable artiﬁcial intelligence
(XAI) such as XGBoost, AdaBoost, and CATBoost models and Is(50), Rn, porosity, and Vp were utilised to
estimate the UCS of rock. The XGBoost among the three models identiﬁed as the best-performing model
achieved an R2 of 0.99 for training and 0.96 for testing, with Is(50) being a signiﬁcant inﬂuence on prediction
sandstone UCS [43].
In conclusion, AI technologies, with their exceptional capabilities and attributes, have a promising future in
estimating the strength properties of rocks. However, AI algorithms have their peculiar limitations associated with
them. For example, the ANN-based models have been identiﬁed as the best AI models for predicting the UCS and
E of rocks due to their high accuracy. Despite their high performance, there are limitations, particularly data
dependency, overﬁtting, and lack of interpretability, that need to be addressed to enhance real-time application
and reliability in real-time prediction of UCS and E. Similar to ANN, all the tree-based models, such as XGBoost,
AdaBoost, are data-dependent, complex in computation, require signiﬁcant processing time, and do not generalise
well to different types of rocks and geological conditions not represented in the training and testing data.
7.3 Physical and mechanical properties and AI models
Materials involved in rock mechanics and engineering are mainly rocks, which show a series of substantial
physical–mechanical features, such as porosity, density, speciﬁc gravity, unconﬁned compressive strength (UCS),
elastic modulus (E), Schmidt rebound hardness, point load, and block punch indexes. They collectively constitute
rocks’ physical and mechanical properties and serve as the core parameters for assessing rock strength and safety.
The properties are usually determined from standard laboratory tests, including uniaxial compression, Brazilian
123
Neural Computing and Applications (2025) 37:20721–20753
20734
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 15
tensile, and point load tests [6, 54, 61, 62]. The UCS and E are essential for designing underground space, tunnel
excavation, and dam sites [32, 41, 61, 63]. It is signiﬁcant to note that rock materials are anisotropic and
heterogeneous, and their physical and mechanical properties are inﬂuenced by temperature, stress path, and
moisture or saturation. Determining the UCS and E directly from the unconﬁned compression tests is costly and
laborious [33, 64]. Also, it is not easy to acquire quality rock cores from soft or highly fractured rocks [49].
Therefore, AI algorithms and indirect test results from the point load index (Is(50)), Schmidt rebound hardness
index (Rn), P-wave velocity (Vp), porosity (n), density (q), and block punch index (BPI) have been exploited to
estimate UCS and E.
Figure 7 illustrates the research statistics on AI in predicting UCS and E with physical–mechanical properties.
In recent years, signiﬁcant increment in the research studies using AI models is to evaluate UCS and E with both
the physical and mechanical properties of rocks, demonstrating the growing interest in the utilisation of AI in the
ﬁeld of rock mechanics and engineering. The primary use of AI models is ANN, ANFIS, and RF, representing
26.3%, 12.5%, and 10% of studies, respectively, from 2014 to 2024, underscoring the growing interest in the use
of AI techniques for predicting rock strength.
Comprehensive strength and elastic modulus jointly establish the mechanical strength of rocks, which serves as
part of the primary parameters for estimating rock strength, safety, and stability. Recently, AI models have
demonstrated their efﬁciency in analysing and predicting the strength of different rocks, especially elastic
modulus and compressive strength, considering different rock strength properties. The success of AI is due to its
efﬁcacy in processing and analysis of experimental datasets. Table 6 presents the usage of AI models in
estimating the UCS and E of rock using physical–mechanical properties. In Table 6, the MAE, MAPE, RMSE,
VAF, and R2 are the AI model performance metrics to validate the accuracy of the various models used in the
prediction of UCS and E. The AI model is efﬁcient when MAE, MAPE, and RMSE are smaller and approaching
0. The increase in VAF and R2 to 100 and 1, respectively, demonstrates the model’s accuracy of the model data.
For example, Jahed et al. [32] used the ANFIS model to forecast the UCS and E of granite with nondistractive
parameters (i.e. qd, Vp, Qtz, and Plg) as inputs. After comparing the model to MRA and ANN models, the ANFIS
model demonstrated a prediction accuracy with a higher R2 of 0.985, RMSE of 6.224, and VAF of 98.46% for
UCS and R2 of 0.99, RMSE of 3.503, and VAF of 98.97% for E.
2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024
0
2
4
6
8
10
12
14
16
18
20
Number of studies
Year of research article publication
ANN
RF
XGBoost
GPR
GEP
GP
PSO-BP
M5P
LSSVM
PSO-ANN
ANFIS
Others
AI models
2.5%
3.8%
3.8%
5%
6.3%
5%
10%
26.3%
12.5%
20%
(a)
(b)
Fig. 7 Breakdown of vari-
ous AI techniques in the
literature for forecasting
UCS and E: a distribution
of intelligence learning
models adopted in the lit-
erature. b the research
trends of various AI models
utilised from 2014 to 2024
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20735

---

## Page 16
Table 6 AI algorithms for estimate of the UCS and E of rock applying physical–mechanical properties
Rock type
Sample
size
Algorithms
Input
parameter
Output
MSE
RMSE
MAE
VAF
R2
References
Granite
45
ANFIS
qd, Vp,
Qtz,
Plg
UCS,
E
–
6.22, 3.50
–
98.50%,
98.97%
0.98,
0.99
Jahed et al. [32]
Limestone
105
ANN
n, q, Vp
UCS,
E
–
7.10, 5.00
–
–
0.95,
0.76
Torabi-Kaveh
et al. [63]
Limestone,
granite
66
PSO-ANN
Is(50), Rn,
Vp, qd
UCS
0.004
–
–
97.24%
0.97
Momeni et al.
[6]
Carbonate
54
M5P
Rn, Vp,
SDI, qd
UCS,
E
–
10.47,
4.32
8.83,3.40
70.17,
89.82
0.89,
0.84
Ghasemi et al.
[71]
Carbonate
163
ANN
n, Vp, e,
Is(50),
qd
UCS,
E
–
3.80, 6.60
–
–
0.97,
0.96
Madhubabu
et al. [72]
Sandstone
228
PSO-BP
qd, Vp,
Is(50),
mc
UCS
0.017–0.099
–
–
–
0.99
Mohamad et al.
[73]
13-rock types
94
ANFIS
Vp, SDI,
q
UCS
–
6.29
–
97.66%
0.98
Sharma et al.
[74]
Basalt
80
ANFIS
Vp, q, n
UCS
–
0.51–3.23
–
76–98%
0.99
Singh et al. [75]
Limestone,
sandstone,
marlstone,
conglomerate
196
ANN
qd, Vp, n,
Ab
UCS,
E
–
0.094,
0.89
0.074,
0.071
–
0.93,
0.92
Abdi et al. [76]
Limestone
115
COA-ANN
md, q, Vp,
n
UCS,
E
1.93, 2.85
–
–
85.21%,
74.48%
0.98
Mokhtari et al.
[69]
Travertine
93
ANN-
committee
Vp, n, Rn,
Is(50)
UCS
–
3.98
3.23
–
0.89
Barzegar et al.
[77]
Granite
71
GP
n, Vp, Rn,
Is(50)
UCS
–
0.0691
–
84.29%
0.84
Fang et al. [78]
Pyroclastic
50
GEP-I
qd, Vp, n,
qs, Is(50)
UCS
–
3.81
–
–
0.93
I˙nce et al. [79]
Marlstone
39
AdaBoost–
NNE
Vp, q, Vs,
BTS,
Is(50)
UCS,
E
–
–
–
–
0.98,
0.92
Salehin et al.
[80]
Sandstone
60
PSO-ANN
Vp, q, Rn
UCS
–
0.086
–
97.50%
0.97
Abdi et al. [40]
Basalt
56
ANN
qd, Vp,
Rn,
Is(50),
BTS
UCS
–
1.54
–
–
0.99
Barham et al.
[81]
Dasitic,
andesitic, tuff,
basalt
47
MPMR
n, BPI
UCS
–
0.059
–
98.12%
0.96
Ceryan et al.
[82]
Granite
88
GMDH
Rn, Is(50),
n, Vp
E
–
7.19
–
95.07%
0.96
Armaghani et al.
[83]
Travertine
32
ANN-PSO
q, Vp,
BTS, Vs
UCS
–
1.37
–
85%
0.91
Ebdali et al. [62]
Shale, Iron pan
40
RVR-HS
Is(50),
BTS,
qb, Vp
UCS
0.0031
–
–
–
0.99
Fattahi [84]
Shale
175
MLP-ANN,
LSSVM-
CSA
GR, DT,
qd, RT,
n
UCS
–
0.174,
0.019
–
–
0.94–1.0
Miah et al. [70]
Travertine
29
ANN
Vp, n
UCS
0.054
–
–
–
0.66
Saldan˜a et al.
[85]
Granite
182
BPNN
Vp, n
UCS
–
10.69
–
–
0.97
Armaghani et al.
[60]
123
Neural Computing and Applications (2025) 37:20721–20753
20736
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 17
In another study, Koken [34] employed CART, ANN, GEP, MARS, and ANFIS models with qd, n, and Vp as
input parameters to estimate the UCS of pyroclastic rock. The researchers concluded that the models performed
better with R2 ranging from 0.82 to 0.88, demonstrating the model’s reliability in predicting the UCS of
pyroclastic rocks. In addition, they suggested that the models used in the study were limited to pyroclastic rocks
only. Heidarian et al. [65] also applied the ANFIS model to predict the UCS of rock, considering the porosity (n),
depth (Dp), and P-wave velocity (Vp). After training, testing, and validation of 655 samples, the ANFIS model
proved to be effective in the prediction of the UCS. Asheghi et al. [66] pioneered a hybrid AI algorithm, a
generalised feedforward network (GFFN) with ICA, for an accurate estimate of the UCS of quarry rocks. They
concluded that the ICA-GFFN model shows better performance in predicting UCS, indicating the model’s
capability after comparing it with standard AI models like GFFN, RBF, and MLP.
Additionally, among the input parameters such as n, Vp, Is(50), and water absorption, the Vp was identiﬁed as the
signiﬁcant input factor in predicting UCS according to sensitivity analysis. Li and Tan [67] employed the LSSVM
Table 6 (continued)
Rock type
Sample
size
Algorithms
Input
parameter
Output
MSE
RMSE
MAE
VAF
R2
References
Granite, schist,
sandstone,
claystone,
slate, marl,
dolomite,
travertine
170
GPR
n, Rn, Vp,
Is(50)
UCS
–
0.522
–
–
0.99
Mahmoodzadeh
et al. [86]
Serpentinites
32
BPNN
b, cd, cs,
Ab, Rn,
Vp,
Is(50), Vs
UCS
0.008
–
–
–
0.94
Moussas and
Diamantis [87]
Travertine
30
XGBoost
n, Rn, Vp,
Is(50)
UCS,
E
–
0.647,
0.037
–
–
0.99
Nasiri et al. [88]
Limestone,
dolomite,
onyx
30
ANN,
ALPS-GP
n, Vp,
Is(50)
UCS
2.11, 1.64
2.50, 2.11
–
98.43%,
97.86%
0.98
O¨ zdemir [89]
Sedimentary
rocks
106
XGBoost
qw, qd,
BTS
UCS
0.00
0.001
0.0054
–
0.99
Shahani et al.
[90]
Igneous,
sedimentary,
metamorphic
60
RF
Rn, n,
BPI,
Is(50),
Gs
UCS
–
–
8.86
–
0.94
Dadhich et al.
[92]
Carbonate
94
SANN
c, Rn
UCS
–
24.15
17.91
–
0.99
Hassan and
Arman [93]
10 different
rocks
147
ANN
ne, qd,
Vp,
UCS
UCS
–
3.87
–
94.09
0.94
Ko¨ken and Koca
[94]
38 different
rocks
93
ANFIS-GA
n, q, Rn
UCS,
E
192.20
–
9.60
97.29
0.98
Rezaei and
Asadizadeh
[95]
Granite
71
ICA-ANN
n, Rn, Vp,
Is(50)
UCS
–
2.91
–
92.94
0.92
Armaghani et al.
[9]
qd dry density; Vp P-wave velocity; Qtz quartz; Plg plagioclase; n porosity; q density; Is(50) point load index; Rn Schmidt rebound hardness; SDI
slake durability index; n porosity; Dp depth; e Poisson ratio; BPI block punch index; R2 coefﬁcient of determination; mc moisture content; Ab water
absorption; md dynamic Poisson ratio; qs saturates density; Vs S-wave velocity; BTS Brazilian tensile strength; Vs S-wave velocity; qb bulk density;
GR gamma ray; DT sonic tensile time; RT true resistivity; b serpentinisation percentage; cd dry unit weight; cs saturated unit weight; Gs speciﬁc
gravity; c dry unit weight; T temperature; Ed dynamic Young’s modulus; ne effective porosity; UCS unconﬁned compressive strength
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20737

---

## Page 18
model to assess the UCS of different rocks. They researched 40 samples and found LSSVM effective in
predicting UCS with n, SDI, Vp, and Is(50) as model inputs. Khan et al. [68] exploited RFR, ANN, KNN, and
MLR models to forecast UCS and E, using T, Vp, n, q, and Ed as input parameters. After analysing 60 samples of
calcite and dolomite, the RFR model emerged as a suitable model for calculating UCS and E with R2 of 0.97.
However, the proposed model is suitable for estimating the UCS and E of high-temperature treated rock. Other
studies have explored the ANN model and observed that it performs more advantageously than the multivariable
regression model. The hybrid optimisation of ANN and other algorithms, including COA-ANN, PSO-ANN,
MLP-ANN, PSO–LSSVM, and ICA-ANN, have also been reported in the studies of [40, 48, 69, 70].
The Is(50), Rn, density (q), speciﬁc gravity (Gs), and water absorption (Ab) for predicting UCS and E. For
example, this study summarises some of the AI algorithms and physical–mechanical properties in Table 7,
including model accuracy measurement metrics and limitations. Asare et al. [96] estimated UCS with the
AutoNN-MARS model, where the model integrates the AutoNN to extract feature and dimensionality reduction
with MARS for regression analysis using Rn, Is(50), qb, and BTS as input variables. They compared the model with
four different existing AI models: RF, BPNN, and GRNN. The researchers concluded that the AutoNN-MARS
model outperforms all the other models with high precision accuracy, demonstrating an r-value of 0.99, RMSE of
0.39, and Pi of 0.31. Koopialipoor et al. [97] developed a stack-tree-KNN-RF-MLP model using different MLs to
estimate E. The model had excellent accuracy results with R2 of 0.83, RMSE of 15, MSE of 227, and MAE of 12.
However, the model can only be used with the input parameter range employed in their research.
Gene expression programme (GEP) generates an interpretable structural algorithm and is applicable to predict
rock strength, excelling in handling uncertainties and nonlinearities of rock data. For instance, Xue [98] devel-
oped GEP based on 44 rock datasets and evaluated it with four traditional regression models, including the ANN
model. The comparison results of the study indicated that GEP performance was better than that of the other
models, with the lowest RMSE of 10.22 and R2 of 0.98 in predicting UCS. The results demonstrate the GEP
model’s potential in predicting rock strength by utilising BPI, Rn, Is(50), and Vp as model input. Malkawi et al. [30]
predicted UCS of travertine rock using rock indices, including Rn, Leeb rebound hardness, Is(50), absorption, pulse
velocity, porosity, and density as input parameters. They used 61 data with ML models such as M5T, ANN, and
KNN. Among the models, the M5T outperformed ANN and KNN in predicting UCS with MAPE of 0.034,
RMSE of 0.045, and Spearman’s rho of 0.96. In order to estimate the UCS of rock, Lei et al. [99] use six hybrid
AI models integrated with a back-propagation (BP) neural network and ﬁve input parameters (E, n, Rn, Is(50), and
Vp). The study reported that among the six models, the ﬁreﬂy algorithm-BP (FA-BP) hybrid model demonstrated
the best prediction accuracy of R2 of 0.985, RMSE of 4.88, MAPE of 0.063, and 10-index of about 0.967.
Additionally, the sensitivity analysis of input parameters revealed that Is(50) is the most important parameter for
estimating UCS.
Xu et al. [100] developed an AI model based on a sparrow search algorithm (SSA) optimised with XGBoost.
The SSA-XGBoost model integrates SSA to optimise the hyperparameters of the XGBoost model to improve the
model predictive accuracy using Rn, Is(50), and Vp and n as model inputs. Their model was evaluated against six
different AI models. According to the evaluation measurement performance metrics, the SSA-XGBoost out-
performed the other models with R2 of 0.96, RMSE of 0.36, MAPE of 11.89%, MAE of 7.06, RMSE of 9.42, and
VAF of 95.97%, indicating the high performance of the model in predicting UCS. Despite the model prediction
performance, the model is limited to careful hyperparameter tuning, potential generalisation problems with
different data and complexity of model computation. Wu et al. [101] proposed optimised kernel ridge regression
(KRR) and Gaussian process regression (GPR) models based on the grid-search method for estimating UCS and
E. The KRR demonstrates exemplary performance in predicting UCS with an average error of 4.9%, and the GPR
model demonstrates better prediction of E with a relative average error of 1.10% using meso-mechanical prop-
erties as model input parameters.
By using physical–mechanical properties from direct and indirect test results as input parameters, including Rn,
dry density, block punch index, BTI, water absorption, porosity, and Is(50), AI algorithms can capture a complex
nonlinear relationship and accurately estimate E and UCS of rocks. The estimation outcomes help rock engineers
123
Neural Computing and Applications (2025) 37:20721–20753
20738
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 19
Table 7 AI algorithms for the forecast of the UCS and E of rock utilising mechanical properties
Model
Samples
Inputs
Output
R2
MSE
RMSE
MAE/
MAPE
VAF
(%)
Limitation
References
Stack-
tree-
KNN-
RF-
MLP
92
n, Is(50),
Rn, Vp
E
0.83
277
15
12
–
The model can only be used with the
input parameter range employed in
this research
Koopialipoor
et al. [97]
ANN-
ICA
367
ne, Rn, Vp
UCS
0.98
–
11.94
0.1196
95.10
The model is limited to the input
parameters used, and any value
outside the minimum and
maximum values cannot provide a
reliable prediction
Le et al. [102]
KELM-
GWO
271
n, Rn, Vp,
Is(50),
UCS
0.92
–
14.73
11.43
91.52
The prediction performance is
limited by parameter diversity
Li et al. [103]
TSO-RF
226
n, Rn, Vp,
Is(50), qd
UCS
0.97
–
6.60
–
–
The model is limited to speciﬁc rock
types adopted by the researchers
and may not be considered a
general model for other rocks
Li et al. [104]
SVR
115
Vp, n, q,
ld
UCS,
E
0.70,
0.76
22.15,
0.29
–
–
The model is limited to carbonate
rocks, and it should be used with
quadratic kernel and cubic kernel
functions
Mokhtari
[105]
WOA-
ELM
734
Rn, Vp,
Is(50)
UCS
0.86
17.61
4.20
–
91
The model has local minima
trapping issues
Qiu et al.
[106]
ANN-
LM
274
ne, Rn, Vp
UCS
0.96
–
14.83
0.11
94.30
Potential variations of input
parameters could inﬂuence the
model. For example, Vp is limited
between 1000 to 3000 m/s
Skentou et al.
[28]
PSO-
SVR
131
L, D,
grain
size,
strain
rate, qb,
SCS, Vp
UCS
0.99
–
4.95,
4.72
–
Increasing input parameters like
bulk density and strain rate
increases UCS
Yang et al.
[47]
GA–SEL
161
BPI, Rn,
Is(50), Vp
UCS
0.92
–
13.45
–
91.01%
Limited dataset and does not cover
all types of rock
Zhang et al.
[107]
fB-GPR
71
n, Rn, Vp,
Is(50)
UCS
0.90
–
13.24
–
–
The model has a large magnitude of
measurement errors
Zhao et al.
[108]
XGBoost
1771
Vp, ne, q
UCS
0.91
–
439
17.22
–
The model is limited to carbonate
rock. Parameters like grain size
and mineral composition were not
considered
Abdelhedi
et al. [64]
SVM
50
RAI,
AIV,
LAAV,
Rn, Is(50)
UCS
0.90
–
1.16
0.76
–
Limited rock samples restrict the
ability of the model
Afolagboye
et al. [109]
ANFIS
45
Is(50),
BTS,
BPI
UCS
0.99
–
0.36
0.28
99.92
The model is valid for limestone,
travertine, sandstone and
conglomerate only
Khajevand
[110]
LSO-RF
386
Vp, n,
Is(50), Rn
UCS
0.92
–
13.75
–
92
The initialisation of a random
population tends to trap it into
local minima optimisation
Li et al. [111]
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20739

---

## Page 20
understand and determine the rock UCS and E at numerous conditions and augment model and testing methods,
therefore enhancing efﬁcacy. In addition, the utilisation of AI algorithms is not restricted to experimental data
handling in predicting rock mechanical properties. The models can be extended to predict and monitor real-time
ﬁeld conditions. The application of AI models in rock engineering ensures that the predictions of rock strength
properties are consistent and accurate with different complex geoenvironmental and loading conditions. However,
some of the AI models developed in the literature are case-speciﬁc and may not be applicable to predict UCS and
E of different rocks with different geological conditions. Therefore, in selecting an AI model from the literature,
careful analysis must be performed to determine the model’s capability and reliability in performing the task.
7.4 Mechanical properties and AI models
Rock exhibits a range of critical rock mechanical properties such as UCS, e, TS, Is(50), Rn, BTI, Vp, and E. These
mechanical properties not only inﬂuence the stability of rock engineering structures but also play a critical role in
the design and construction of geomechanics projects. These mechanical properties have been widely used to
predict UCS and E [35, 91, 113–115]. Figure 8 shows statistical data on research involving AI models in
predicting UCS and E with mechanical properties of rocks from 2014 to 2024. As depicted in the ﬁgure, common
AI models include ANN (31.4%), ANFIS (25.7%), and SVR (8.6%).
AI models have shown the potential to predict UCS and E with rock mechanical properties. Kaithola et al.
[113] exploited the ANFIS model and linear regression with Vp to estimate the UCS and other rock properties
from the Himalayan. The ANFIS model outperforms the traditional linear regression models in predicting UCS,
indicating higher accuracy and reliability. Mohammadi et al. [116] utilised hybrid ANFIS-PSO and ANFIS-GA to
predict UCS and E. They noticed a successful prediction of UCS and E of dolomite and carbonate rocks, but the
model was less accurate in predicting the Poisson ratio and internal friction angle. The ANFIS-PSO model
demonstrates high prediction accuracy with a low RMSE of 1.14 and R2 of 0.90 than the ANFIS-GA model,
considering weight on the drill bit (WOB), drill string rotation speed (RPM), rate of penetration (ROP), and
torque (Trq) as model input parameters. A similar study by Davoodi et al. [117] explored the least square support
vector machine (LSSVM) and multi-layer extreme learning machine (MELM) algorithm amalgam with COA,
PSO, and GA to forecast UCS using depth (L), ROP, RPM, WOB, Trq, bit wear rate (CT), and ﬂow rate (FLR) as
model input. After the construction, training and testing of 3042 datasets from two wells, the MELM-COA model
achieved high prediction accuracy in estimated UCS with R2 of 0.99 and RMSE of 4.69. The L, ROP, RPM,
WOB, and Trq were found to inﬂuence the prediction of UCS signiﬁcantly.
Gamal et al. [118] developed AI models RF based on Principal Component Analysis (PCA) and Function
Network (FN). The drilling data include WOB, drill string rotating speed (RS), drilling torque (T), stand-pipe
pressure (SPP), mud pumping rate (Q), and ROP as model input parameters to predict real-time UCS of rock. The
RF-PCA model surpassed the RF-FN model, achieving an R2 of 0.99 and an average absolute percentage error
(AAPE) of 4.3%. In comparison, the FN model had an R2 of 0.97 and an AAPE of 8.5%. Validation results were
Table 7 (continued)
Model
Samples
Inputs
Output
R2
MSE
RMSE
MAE/
MAPE
VAF
(%)
Limitation
References
SSA-RF
126
Vp, n,
Is(50), Rn
UCS
0.96
–
9.42
7.06,
11.89
Low-quality data size
Wang et al.
[112]
ne effective porosity; Rn Schmidt hammer rebound number; Vp P-wave velocity; n porosity; ld dynamic Poisson ratio; BPI block punch index; R2
coefﬁcient of determination; SCS static compressive strength; Em elastic modulus; qd dry density; Is(50) point load index; q density; L length;
D diameter; SCS static compressive strength; Vp P-wave velocity; ne effective porosity; q density; RAI rock aggregate index; AIV aggregate impact
value; LAAV Loss Angeles aggregate value; BTS Brazilian tensile test; qd dry density; Ab water absorption; r correlation coefﬁcient; Pi performance
index
123
Neural Computing and Applications (2025) 37:20721–20753
20740
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 21
consistent, with the RF model demonstrating higher accuracy. Siddig et al. [119] also used three AI models:
ANFIS, RF, and FN with WOB, drill pipe torque, and ROP to estimate static elastic modulus (Es). The models
showed high accuracy, with R2 ranging from 0.92 to 0.99 and AAPE below 13%. The results indicate that using
drilling data and AI techniques to predict Es is promising. This approach is a cost-effective and efﬁcient
alternative to traditional methods, providing continuous proﬁles of rock mechanical properties crucial for
applications like fracturing design and wellbore stability.
In addition, Hiba et al. [120] predicted UCS with ANN using input parameters similar to [118, 119]. The ANN
model demonstrated high accuracy, with AAPE of 0.28% during training and 0.59% during testing, effectively
predicting UCS in real time. This AI-based approach provides a fast, reliable, and continuous method for
predicting rock strength parameters, offering signiﬁcant advantages over traditional laboratory-based methods.
Daniel et al. [121] developed models using GBDT, XGBoost, LightGBM, RF, and ET hybridise with Bayesian
Optimisation (OB) for predicting the UCS of metamorphic, magnetic, and sedimentary rocks, utilising input
parameters such as Rn, Vp, and Is(50). Notably, after analysing 729 datasets, the BO-ET optimisation algorithm
outperformed the other ﬁve models with R2 of 0.99, VAF of 99%, MAE of 3.97, and RMSE of 4.82. Also, a
graphic user interface (GUI) system was developed based on the BO-ET model and validated in tunnel boring
machine excavated tunnel. Khatti and Grover [122] introduced the MD21 model, including a PSO-optimised
relevance vector machine (RVM) model implemented by Laplacian ? polynomial for predicting UCS with
nondestructive mechanical properties.
After training and testing 734 rock datasets, the MD21 model demonstrates an optimal performance in
validation and testing with R2 of 0.998 and RMSE of 1.93 compared to the traditional models. The MD21 model
offers a highly accurate and reliable method for estimating UCS. It provides valuable insights for geotechnical
engineering applications. Despite the performance of the M21 model, there exists a limitation: using a hybrid
learning model to determine the optimal structure, which will be utilised in numerous analyses. Table 8 details the
application of speciﬁc AI models in assessing the UCS and E of rock with mechanical properties. From two ML
models, step-wise regression (SWR) and simple linear regression (SLR) for predicting UCS of Charnockite rock,
Kochukrishnan et al. [115] used indirect test results (Rn, BTS, Vp, and Is(50)) as input parameters and SWR
2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024
0
1
2
3
4
5
6
7
8
9
10
Number of studies
Year of research article publication
ANN
SWR
LSSVM
M21
BO-ET
ELM
SVM
MLPNN
MRA
GMDH
SVR
FIS
ANFIS
(a)
(b)
AI models
5.7%
2.9%
2.9%
2.9%
31.4%
8.6%
5.7%
25.7%
Fig. 8 Breakdown of AI
algorithms in forecasting
UCS and E with physical–
mechanical properties:
a distribution of different
algorithms employed in
estimating rock UCS and E,
and b trends and number of
studies involving different
AI models in using physi-
cal–mechanical properties
from 2014 to 2024
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20741

---

## Page 22
outperformed the SLR achieved a low MAE of 1.71 and R2 of 0.99. In the ranking of the signiﬁcance of the input
parameters, the Vp has a signiﬁcant inﬂuence on estimating the UCS of the Charnockite rock.
ANN, ANFIS, and other algorithms have substantial advantages in predicting UCS and E. Research by Jan
et al. [133] demonstrated that the UCS of marble rocks could be predicted with AI models: ANN, RF, XGBoost,
SVM, Elastic net (EN), Ridge, and Lasso model using mechanical properties as input parameters. The result
indicates that the ANN model had the highest prediction accuracy with R2 of 0.99, RMSE of 0.26, MSE of 0.069,
and MAE of 0.164 compared to other models. However, the XGBoost model also showed a close performance in
predicting UCS as the ANN. The models were trained and tested using limited rock data and three features, which
might not be able to capture signiﬁcant information in predicting UCS accurately. Also, since the study used only
marble rock, the models may be ﬁne-tuning when applying it to other rock types.
In predicting E, the RMSE of the ANFIS was 0.0025 for coal rock, 0.127 for ANN with sandstone, and 0.82
for SVR with limestone [27, 124, 127]. These results indicated that ANN and ANFIS offer high predictive
accuracy and efﬁciency in dealing with large datasets and complex nonlinear relationships in real-time rock data.
The ANN and ANFIS excel at capturing the UCS and E of rocks and their inﬂuencing factors. SVR also performs
better with small and linear data, but it faces challenges with nonlinear and enormous datasets, which makes SVR
less tractable than ANN algorithms. However, their estimated error can sometimes be less than those of other AI
algorithms. The SVR model has shown its effectiveness and suitability for predicting UCS due to a higher
computational advantage [124]. Overall, ANN and ANFIS outperform the SVR in efﬁciency, accuracy, and
adaptability. Nonetheless, future studies should emphasise the strength of these algorithms in developing efﬁcient
and hybrid algorithms.
Table 8 AI algorithms for evaluation of the UCS and E of rock employing mechanical properties
Rock type
Sample
size
Algorithms
Input parameter
Output
R2
RMSE
References
Limestone, schist,
quartzite, slate
597
ANFIS
Vp
UCS
0.91–0.97
–
Kainthola et al. [113]
Granite, schist, sandstone
44
FIS, ANN,
ANFIS
BPI, Is(50), Rn, Vp
UCS
0.92–0.98
9.54–16.90
Mishra et al. [123]
Sandstone
96
ANN
Is(50), Rn, Vp
E
0.81
0.127
Bejarbaneh et al. [27]
Sandstone
108
ICA-ANN
Rn, Vp, Is(50)
UCS
0.95
3.25
Armaghani et al. [15]
Limestone
482
SVR
Ed, md
UCS,
E
0.92, 0.93
1.31, 0.82
Aboutaleb et al. [124]
Basalt, metabasalt
47
ANFIS-SCM
Rn
UCS
0.93
0.198
Fattahi [41]
Calcareous mudstones
80
ANFIS
BPI, Is(50), CPI
UCS,
E
0.96, 0.79
–
Mahdiabadi and Khanlari
[125]
Migmatite
120
ANN
CPI, BPI, BTS,
Is(50), VP
UCS,
E
0.90, 0.93
–
Saedi et al. [126]
Coal
69
ANFIS
CS, TS, SS, Vp
E
0.98
0.0025
Roy et al. [127]
Granite
96
SFS-ANFIS
Rn, Vp, Is(50),
UCS
0.98
6.65
Jing et al. [128]
Granite
100
GMDH
Rn, Vp, qd
UCS
0.86
0.089
Li et al. [29]
Different rocks
93
MRA
Rn, BTS, SH, Is(50),
Vp
UCS
0.91
–
Teymen et al. [129]
Granite, schist, sandstone
44
GA-LSSVM
BPI, Rn, Vp
UCS
0.98
6.68
Xue and Wei [130]
Basalt, dolostone,
limestone
30
MLPNN
SH, BTS, Vp
UCS
0.99
1.34
Gu¨l et al. [131]
12 different rocks
37
ANN
Vp
UCS
–
–
Rahman and Sarkar [132]
Vp P-wave velocity; BPI block punch index; Is(50) point load index; Rn Schmidt rebound hardness; R2 coefﬁcient of determination; Ed dynamic
Young’s modulus; UCS unconﬁned compressive strength; CPI cylinder punch index; md dynamic Poisson ratio; CS compressive strength; TS
tensile strength; SS shear strength; BTS Brazilian tensile strength; SH shore hardness; E elastic modulus; SCM subtractive clustering method
123
Neural Computing and Applications (2025) 37:20721–20753
20742
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 23
In recent decades, AI algorithms such as ANN, RF, and SVM have demonstrated remarkable success in
predicting UCS and E of different rock types. Several studies have shown that the combination of these algo-
rithms with optimisation algorithms offers signiﬁcant beneﬁts in terms of forecasting UCS and E of rocks, for
example, the optimisation of ANN with ICA and marine predator algorithms (MPA). In addition, Jing et al. [128]
combined hybrid models such as particle swarm optimisation (PSO), subtractive clustering method (SCM),
genetic algorithm (GA), stochastic fractal search (SFS), and differential evolution (DE) with ANFIS for pre-
dicting UCS of rock using Vp, Rn, and Is(50). They concluded that the SFS-ANFIS model had high accuracy in
predicting UCS with R2 of 0.98, MAE of 4.44, and MAPE of 4.82 compared with the other hybrid models.
Furthermore, for the UCS forecast, the ANN algorithms surpassed the performance of MVRA, and fusion
optimisation models, with ICA-ANN and PSO-ANN, further boosted the algorithm’s performance [32, 73, 134].
Table 9 shows a comparison of hybrid models developed in the literature. From the table, it is clear that the hybrid
models provide an excellent tool for predicting the UCS and E of rocks, but the generalisation of these models is
still at the primary stage, because the same rock with different model input parameters may present different
model outcomes (i.e. UCS and E) when using the same AI model.
In summary, AI techniques have demonstrated signiﬁcant potential in predicting UCS and E with rock
mechanical properties. The AI algorithms for predicting UCS and E include extensive experimental data, like
point load index, unconﬁned compressive, Brazilian tensile, block punch, Schmidt hammer rebound, and P-wave
and S-wave velocity tests. The datasets from these tests, AI models can be constructed, trained, and tested to
capture nonlinear relations, predict real-time UCS and E, and provide accurate prediction results. It should be
noted that most of the AI models discussed cannot be generalised for predicting UCS and E due to different
model input parameters used, which may require a signiﬁcant modiﬁcation. It has also been found that limited
datasets can impact the AI model’s performance in predicting UCS and E. As presented in Table 8, the AI model
shows excellent performance in predicting UCS and E. However, caution must be considered when selecting an
AI model to perform any predictions in terms of rock strength. Most of the studies combined datasets from
different rock types, which makes it challenging to interpret and identify the particular rock type.
Table 9 Current AI hybrid
models in literature for
predicting UCS and E of
rocks
AI hybrid model
Output
Performance (R2)
References
ICA-GFNN
UCS
0.98
Asheghi et al. [66]
PSO-ANFIS
GA-ANFIS
DE-ANFIS
SFS-ANFIS
UCS
0.96
0.94
0.95
0.98
Jin et al. [128]
ANFIS-SCM
SVR-ABC
UCS
0.93
0.97
Fattahi [41]
ICA-ANN
UCS
0.95
Armaghani et al. [15]
XGBoost-FA
UCS, E
0.99, 0.97
Cao et al. [37]
ANN-PSO
UCS
0.97
Momeni et al. [6]
ANN-PSO
UCS
0.97
Mohamad et al. [39]
ANN-PSO
ANN-TLBO
UCS
0.99
0.93
Sabri et al. [49]
WOA-ELM
UCS
0.86
Qiu et al. [106]
MELM-COA
UCS
0.99
Davoodi et al. [117]
GA-SEL
UCS
0.92
Zhang et al. [107]
COA-ANN
UCS
0.97
Mokhtari and Behnai [69]
PSO-LSSVM
UCS
0.95–0.99
Wen et al. [48]
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20743

---

## Page 24
7.5 Physical properties and AI models
The physical properties of rocks signiﬁcantly inﬂuence the engineering characteristics of rocks, including bulk
density [135], quartz [37, 136], CT images [44], discontinuity density [137], and porosity [82], among others.
As presented in Fig. 9, AI techniques are widely used in estimating the UCS and E of rock with physical
properties. However, not many studies have focused only on the physical properties of rocks in determining
UCS and E, as in Fig. 9(a). The percentage ratios of the AI algorithms used with physical properties in
predicting UCS and E are shown in Fig. 9(b). It is evident from Fig. 9(b) that AI models: ANN, RF, ANFIS,
and SVM models have seen growing interest in predicting UCS and E utilising rock’s physical properties as
the model input parameters.
Sun et al. [36] proposed an innovative technique for reconstructing 2D fracture characteristics and mineral
distribution of mudstone from X-ray CT images processed with the LOG algorithm. The study introduced the
CNN algorithm with stochastic pooling technique and applied the model to LOG images to predict the UCS of the
rock. The study revealed that the CNN model can predict the UCS of the mudstone with CT slices with a mean
error of 2.19%. However, the proposed method used depends on signiﬁcant data for high-resolution X-ray
scanning. Overall, this proposed model supports the performance of UCS prediction.
Wu et al. [138] also employed X-ray CT images of limestone with porosity, dry density, P-wave velocity, and
other derived parameters as input to predict UCS. They utilised SVM, RF, and BPNN-based models embedded
with genetic algorithms (GA) to optimise the input parameters and effectively predict the UCS. Among other
models, the BPNN-base algorithm performed excellently with R2 of 0.92, MAPE of 14.81, RMSE of 8.68, and
MAE of 6.85. Through AI methods, researchers can automatically acquire and analyse rock strength with mineral
content [24, 139], rock quality designation [137], high–low-frequency ratio, and amplitude attenuation coefﬁcient
[140]. These are indicators forming the fundamentals for analysing UCS and E with some physical properties.
The AI technology also enables the reconstruction of 2D images and provides a quick and accurate way of
acquiring parameters. The technology provides solid grounds for research prospects and the use of AI algorithms
in rock engineering.
(a)
(b)
1
1
2
1
3
1
2
4
3
1
3
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023
2024
8.3%
4.2%
8.3%
12.5%
12.5%
4.2%
29.2%
12.5%
4.2%
CFNN-LMA
RF
GP
RVM
SVM
ELM
CNN
XGBoost
ANFIS
ANN
Fig. 9 Breakdown of AI algorithms in predicting UCS and E with mechanical properties: a distribution of various
algorithms employed in estimating rock UCS and E and b trends and number of studies involving various AI models in
using mechanical properties from 2014 to 2024
123
Neural Computing and Applications (2025) 37:20721–20753
20744
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 25
Elkatatny et al. [135] conducted a pioneering study using learning models such as ANFIS, SVM, and ANN to
predict E using bulk density (qb), compression time (Ct), and shear time (St) as input parameters. Among these
models, the ANN algorithm shows the best prediction accuracy of R2 of 0.96 and AAPE of 6.2%. In a similar
study, Wang et al. [141] applied dry density (qd), quartz, mica, and plagioclase as input, and the XGBT model
attained an R-value of 0.99 and MAE of 0.11 in predicting UCS. Hasanipanah et al. [137] successfully optimised
CFNN with LMA to predict the deformation modulus of rock using depth, RQD, discontinuity orientation
adjustment, groundwater conditions, and discontinuity density as model input.
Feldspar, fragments, and quartz minerals were employed as model input parameters by Fang et al. [136] to
predict UCS and E with the ANFIS algorithm (R2 = 0.99). The SVM provides excellent results in predicting
compressive strength. Utilising parameters including amplitude attenuation coefﬁcient and high–low-frequency
ratio, the R2 reaches 0.99, and MAE and RMSE were 0.092 and 0.10, respectively [140]. Hybrid intelligence
systems, such as artiﬁcial neural networks with particle size optimisation (ANN-PSO) and teaching learning-
based optimisation (ANN-TLBO) using unit weight and petrographic analysis, result in higher R2 and low
Theil’s inequality coefﬁcient (TIC) [49]. Table 10 summarises some of the studies involving physical
properties.
In summary, AI techniques demonstrate promising potential in predicting UCS and E of various rocks with
physical properties, including density, mineral contents, X-ray CT, and petrographic images as input parameters.
The input data can be acquired from CT scans and other laboratory tests, and by training these data, the AI
algorithms can capture both complex nonlinear and linear relationships to predict the UCS and deformation
characteristics of rocks. AI technology can provide accurate predictions for rock discontinuities (fragments or
fractures), water saturation, P-durability index, and neutron porosity. The application of AI extends to real-time
monitoring, ensuring that predictions of rock strength with physical properties are dependable considering
different complex geological terrains and stress conditions.
Table 10 Summary of some studies on AI algorithms for evaluating the UCS and E with physical properties
Rock type
Sample
size
Algorithms
Input parameter
Output
R2
References
Carbonate
120
ANFIS
qb, Ct, St
UCS,
E
0.94, 0.88
Tariq et al. [142]
Granite
45
XGBoost-
FA
Vp, Qtz, Kpr, Plg, Chl,
Mica, qd
UCS,
E
0.99, 0.97
Cao et al. [37]
Carbonate
2600
RF
qb, GR, DTC, DTS, np
UCS
0.99
Ibrahim et al. [143]
Shale
5000
GP
n, Ws, qb
UCS
0.96
Koolivand-Salooki
et al. [144]
Sandstone
64
ANFIS
Qtz, Fr, Fg, Vp
UCS,
E
0.99
Fang et al. [125]
Granite
45
XGBT
qd, Qtz, Vp, mica, Plg
UCS
0.99
Wang et al. [141]
Dasitic, andesitic, turffs
and basalt
10
RVM
n, PDI
UCS
0.85
Ceryan [82]
Carbonate
54
ELM
MC, qs, cd, nt, ne
UCS
0.79
Liu et al. [24]
Granite
54
ANN-PSO
cd, PA, MC
UCS
0.99
Sabri et al. [49]
Mudstone
15
CNN
150 CT images
UCS
CT-value % range from
0.94 to 0.96
Sun et al. [44]
Granite
40
SSA-
XGBoost
Vp
UCS
0.94
Xie et al. [145]
qb bulk density; Ct compression time; St shear time; Qtz quartz; Kpr alkali feldspar; Plg plagioclase; Chl chlorite; qd dry density; Vp P-wave
velocity; GR gamma ray; DTC sonic time compression; DTS shear time; np neutron porosity; n porosity; Ws water saturation; Fr feldspar; Fg
fragments; PDI P-durability index; MC mineral content; qs speciﬁc density; cd dry unit weight; ne effective porosity; nt total porosity
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20745

---

## Page 26
8 Limitations and challenges
The primary challenge of AI algorithms is the reliability of large datasets, which is the critical component for the
training and testing of AI algorithms. Data quality is crucial for the efﬁciency and strength of AI algorithms, as it
signiﬁcantly impacts their performance. In addition, the simpliﬁcation of AI algorithms necessitates evaluation
and authentication. Moreover, the interpretation and explanation of AI algorithms are essential. Comprehending
how to explain AI model expectations is signiﬁcant for extending conﬁdence and warranting realistic application
in rock engineering. The challenge lies in ensuring the precision and reliability of AI algorithms in reasonable
applications, thereby positively impacting rock mechanics and engineering.
AI algorithms signiﬁcantly enhanced the computation capabilities of processing data and recognised forms. AI
algorithms face considerable difﬁculties in accommodating complex rock mechanics scenarios and varying
geological terrains. With data scarcity, AI algorithms sometimes face challenges in providing accurate and
credible evaluations of rock strength. This is because the AI algorithms mainly depend on data-driven methods,
not integrating physical concepts, which sometimes weakens the algorithm’s interpretability and reliability in
predicting complex rock strength characteristics and other geological conditions. These AI algorithms are often
used to train data on speciﬁc rocks from different complexities of real-world geological formation environments
that may not adequately epitomise the diversity or to generalise and stipulate accurate forecasting with diverse
rock mass characteristics that can be co-operated.
9 Future research directions
AI algorithms offer signiﬁcant opportunities due to their exceptional analytical capabilities to assist in evaluating
complex and nonlinear relationships to rock engineering, hence offering crucial evidence that standard modelling
techniques sometimes miscue. AI technologies ease the integration and examination of diverse data from the
mechanical and physical properties of rocks, ranging from diverse laboratory tests to the promotion of an all-
inclusive, multi-scale elucidation of rock strength characteristics, which allows for the optimisation of test designs
and methods. The future research directions may include:
1.
Many studies have combined physical–mechanical properties in predicting UCS and E as input parameters.
On the other hand, few studies focused on the use of physical and mechanical properties with AI algorithms in
estimating UCS and E. It is recommended that more studies are conducted on physical and mechanical
properties only, especially physical properties since they are easy to determine. Additionally, the inﬂuence of
individual parameters of both physical and mechanical properties is used as model input in predicting rock
UCS, and E should be investigated to supplement the literature.
2.
By combining adaptive learning strategies and the physical concept of rock behaviour into computational
methods by integrating deep learning and fundamentals of rock mechanics principles, deep learning AI
algorithms can obey physical rules and theories, such as Drucker–Prager model, Bieniawski’s RMR, and
Hoek–Brown’s criterion as well as incorporation of stress–strain relationship to create synthetic features (e.g.
mineralogy, texture, porosity, hardness, and lithology) that estimate UCS based on other rock properties for
training and testing stages.
3.
Most studies used a combination of datasets from different rocks, including granite, sandstone, limestone,
mudstone, marble, and shale, to predict UCS and E. The combination of data from different rocks makes it a
challenge for the AI models to identify which speciﬁc rock UCS and E have been predicted. Therefore, it is
suggested that more work should based on a particular rock type.
123
Neural Computing and Applications (2025) 37:20721–20753
20746
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 27
10 Conclusions
This systematic literature review evaluates the position of AI algorithms in enhancing computation and predic-
tions of rock strength and deformation in engineering rock mechanics, emphasising their importance and capa-
bilities in dealing with the complicated behaviour of rock. Additionally, the review gives a thorough assessment
of different AI methods utilised in the realms of rock engineering. The main summary emerges regarding the
recent status and scope of AI models in rock mechanics:
1.
The review demonstrated that AI models can predict UCS and E with high accuracy and minimum errors.
Additionally, the study reveals that the ANN and ANN-based algorithms were noticed to be the most widely
used in predicting UCS and E. Other AI algorithms, such as RF, SVM, ANFIS, and XGBoost, have likewise
proven their potential in forecasting UCS and E of rocks.
2.
ANN, ANFIS, and RF-based algorithms per the study collectively constitute substantial proportions of 23.4%,
11.3%, and 8.4%, respectively, for the past decades, demonstrating their usefulness in predicting UCS and E.
AI models are used to forecast UCS and E, with a reliability rate of 57.3%, demonstrating robustness in data
handling and competence.
3.
This systematic literature review catalogues the usage of AI algorithms in predicting UCS strength and E into
three different themes: studies that (1) combined physical and mechanical properties, (2) mechanical, and (3)
physical properties with AI models. It is observed that a combination of physical and mechanical properties as
an input parameter is the most utilised for predicting UCS and E, followed by mechanical and physical
properties.
4.
High-quality data are essential for accurate AI learning, assessment, and prediction. Prioritising data
generation, curation, and management, especially for practical rock engineering tasks, is crucial for the precise
application of AI algorithms in predicting UCS and E of rock.
5.
In general, AI algorithms show promising potential in estimating the UCS and E of rocks. However, AI
models are also associated with some limitations. Therefore, care must be taken when selecting a model from
the literature to perform a particular task.
Acknowledgements The research was supported by the Grifﬁth University Postgraduate Research Scholarship (GUPRS).
Author contributions Stephen Akosah helped in conceptualisation, writing—original draft, writing—review and editing.
Ivan Gratchev contributed to conceptualisation, writing—original draft, supervision, writing—review and editing. Solomon
S. R. Gidigasu helped in writing—review and editing.
Funding Open Access funding enabled and organized by CAUL and its Member Institutions. This paper received no
funding.
Data availability All the research articles used in this paper were obtained from the databases described in this systematic
literature review.
Declarations
Conflict of interest The authors declare that they have no conflict of interest.
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20747

---

## Page 28
References
1. Kainthola A, Singh PK, Singh TN (2014) Stability investigation of road cut slope in basaltic rock mass. Maha-
baleshwar India Geosci Front 6(6):837–845
2. Singh VP, Kotiyal YC (2013) Prediction of compressive strength using artiﬁcial neural network. Int J Civil Struct
Constr Archit Eng 7(12):640–644
3. Yilmaz I (2009) A new testing method for indirect determination of the unconﬁned compressive strength of rocks. Int J
Rock Mech Min Sci 46(8):1349–1357
4. Bieniawski ZT (1974) Estimating the strength of rock materials. J South Afr Inst Min Metall 74(8):312–320
5. Rezaei M, Majdi A, Monjezi M (2014) An intelligent approach to predict unconﬁned compressive strength of rock
surrounding access tunnels in longwall coal mining. Neural Comput Appl 24:233–241
6. Momeni E, Armaghani DJ, Hajihassani M, Amin MFM (2015) Prediction of uniaxial compressive strength of rock
samples using hybrid particle swarm optimization-based artiﬁcial neural networks. Measurement 60:50–63
7. Armaghani DJ, Tonnizam Mohamad E, Momeni E, Monjezi M, Sundaram Narayanasamy M (2016) Prediction of the
strength and elasticity modulus of granite through an expert artiﬁcial neural network. Arab J Geosci 9(48):1–16
8. Mishra DA, Basu A (2012) Use of the block punch test to predict the compressive and tensile strengths of rocks. Int J
Rock Mech Min Sci 51:119–127
9. Basu A, Aydin A (2006) Predicting uniaxial compressive strength by point load test: signiﬁcance of cone penetration.
Rock Mech Rock Eng 39:483–490
10. Tandon RS, Gupta V (2015) Estimation of strength characteristics of different Himalayan rocks from Schmidt hammer
rebound, point load index, and compressional wave velocity. Bull Eng Geol Env 74(2):521–533
11. Nazir R, Momeni E, Armaghani DJ, Amin MM (2013) Prediction of unconﬁned compressive strength of limestone
rock samples using L-type Schmidt hammer. Electron J Geotech Eng 18:1767–1775
12. Karaman K, Kesimal A (2015) A comparative study of Schmidt hammer test methods for estimating the uniaxial
compressive strength of rocks. Bull Eng Geol Env 74:507–520
13. Kahraman SAI˙R (2001) Evaluation of simple methods for assessing the uniaxial compressive strength of rock. Int J
Rock Mech Min Sci 38(7):981–994
14. Çobanog˘lu I˙, Çelik SB (2008) Estimation of uniaxial compressive strength from point load strength, Schmidt hardness
and P-wave velocity. Bull Eng Geol Env 67:491–498
15. Armaghani DJ, Amin MFM, Yagiz S, Faradonbeh RS, Abdullah RA (2016) Prediction of the uniaxial compressive
strength of sandstone using various modeling techniques. Int J Rock Mech Min Sci 85:174–186
16. Yilmaz I, Yuksek G (2009) Prediction of the strength and elasticity modulus of gypsum using multiple regression,
ANN, and ANFIS models. Int J Rock Mech Min Sci 46(4):803–810
17. Winn K (2018) A fuzzy model to predict the unconﬁned compressive strength of Singapore’s sedimentary rocks in
comparison with multi-regression analysis. In ISRM International Symposium-Asian Rock Mechanics Symposium (pp.
ISRM-ARMS10). ISRM
18. Chau KT, Wong RHC (1996) Uniaxial compressive strength and point load strength of rocks. Int J Rock Mech Min Sci
Geomech Abstr 33(2):183–188
19. Fener M, Kahraman S, Bilgil A, Gunaydin O (2005) A comparative evaluation of indirect methods to estimate the
compressive strength of rocks. Rock Mech Rock Eng 38(4):329–343
20. Beiki M, Majdi A, Givshad AD (2013) Application of genetic programming to predict the uniaxial compressive
strength and elastic modulus of carbonate rocks. Int J Rock Mech Min Sci 63:159–169
21. Dehghan S, Sattari GH, Chelgani SC, Aliabadi MA (2010) Prediction of uniaxial compressive strength and modulus of
elasticity for Travertine samples using regression and artiﬁcial neural networks. Min Sci Technol (China) 20(1):41–46
22. Mohamad JD, Hasbollah DA, Taib AM, Dan MF, Jusoh SN, Said KM (2022) Correlation between uniaxial com-
pressive strength and point load strength of Penang island granites. IOP Conf Ser Earth Environ Sci 971(1):012025
23. Minaeian B, Ahangari K (2013) Estimation of uniaxial compressive strength based on P-wave and Schmidt hammer
rebound using statistical method. Arab J Geosci 6:1925–1931
24. Liu Z, Shao J, Xu W, Wu Q (2015) Indirect estimation of unconﬁned compressive strength of carbonate rocks using
extreme learning machine. Acta Geotech 10:651–663
25. Pappalardo G (2015) Correlation between P-wave velocity and physical-mechanical properties of intensely jointed
dolostones, Peloritani mounts, NE Sicily. Rock Mech Rock Eng 48:1711–1721
26. Niu G, He X, Xu H, Dai S (2024) Development of rock classiﬁcation systems: a comprehensive review with emphasis
on artiﬁcial intelligence techniques. Eng 5(1):217–245
27. Bejarbaneh BY, Bejarbaneh EY, Amin MFM, Fahimifar A, Jahed Armaghani D, Majid MZA (2018) Intelligent
modelling of sandstone deformation behaviour using fuzzy logic and neural network systems. Bull Eng Geol Env
77:345–361
123
Neural Computing and Applications (2025) 37:20721–20753
20748
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 29
28. Skentou AD, Bardhan A, Mamou A, Lemonis ME, Kumar G, Samui P, Armaghani DJ, Asteris PG (2023) Closed-form
equation for estimating unconﬁned compressive strength of granite from three non-destructive tests using soft com-
puting models. Rock Mech Rock Eng 56(1):487–514
29. Li D, Armaghani DJ, Zhou J, Lai SH, Hasanipanah M (2020) A GMDH predictive model to predict rock material
strength using three non-destructive tests. J Nondestr Eval 39:1–14
30. Malkawi DA, Rabab’ah SR, Sharo AA, Aldeeky H, Al-Souliman GK, Saleh HO (2023) Enhancing of uniaxial
compressive strength of travertine rock prediction through machine learning and multivariate analysis. Res Eng
20:101593
31. Asteris PG, Karoglou M, Skentou AD, Vasconcelos G, He M, Bakolas A, Zhou J, Armaghani DJ (2024) Predicting
uniaxial compressive strength of rocks using ANN models: incorporating porosity, compressional wave velocity, and
Schmidt hammer data. Ultrasonics 141:107347
32. Jahed Armaghani D, Tonnizam Mohamad E, Momeni E, Narayanasamy MS, Mohd Amin MF (2015) An adaptive
neuro-fuzzy inference system for predicting unconﬁned compressive strength and Young’s modulus: a study on main
range granite. Bull Eng Geol Env 74:1301–1319
33. Gowida A, Elkatatny S, Gamal H (2021) Unconﬁned compressive strength (UCS) prediction in real-time while drilling
using artiﬁcial intelligence tools. Neural Comput Appl 33(13):8043–8054
34. Koken E (2024) Estimating uniaxial compressive strength of pyroclastic rocks using soft computing techniques. J Min
Environ 15(3):977–990
35. Martin SS, Farahzadi L, Makaremi S, Chelgani SC, Sattari GH (2018) Variable selection and prediction of uniaxial
compressive strength and modulus of elasticity by random forest. Appl Soft Comput 70:980–987
36. Wang M, Wan W, Zhao Y (2020) Prediction of the uniaxial compressive strength of rocks from simple index tests
using a random forest predictive model. Comptes Rendus Me´c 348(1):3–32
37. Cao J, Gao J, Nikafshan Rad H, Mohammed AS, Hasanipanah M, Zhou J (2022) A novel systematic and evolved
approach based on XGBoost-ﬁreﬂy algorithm to predict Young’s modulus and unconﬁned compressive strength of
rock. Eng Comput 38(Suppl 5):3829–3845
38. Cemiloglu A, Zhu L, Arslan S, Xu J, Yuan X, Azarafza M, Derakhshani R (2023) Support vector chine (SVM)
application for uniaxial compression strength (UCS) prediction: a case study for Maragheh limestone. Appl Sci
13(4):2217
39. Mohamad ET, Jahed Armaghani D, Momeni E, Abad ANK (2015) Prediction of the unconﬁned compressive strength
of soft rocks: a PSO-based ANN approach. Bull Eng Geol Environ 74:745–757
40. Abdi Y, Momeni E, Khabir RR (2020) A reliable PSO-based ANN approach for predicting unconﬁned compressive
strength of sandstones. Open Construct Build Technol J 14(1):237–249
41. Fattahi H (2017) Applying soft computing methods to predict the uniaxial compressive strength of rocks from schmidt
hammer rebound values. Comput Geosci 21(4):665–681
42. Aghda SF, Kianpour M, Mohammadi M (2018) Estimation of uniaxial compressive strength and modulus of
deformability of the Asmari limestone, using neuro-fuzzy system. Iran J Sci Techn Trans A Sci 42:2005–2020
43. Liu Z, Armaghani DJ, Fakharian P, Li D, Ulrikh DV, Orekhova NN, Khedher KM (2022) Rock strength estimation
using several tree-based ML techniques. CMES-Comput Model Eng Sci 13(3)
44. Sun H, Du W, Liu C (2021) Uniaxial compressive strength determination of rocks using X-ray computed tomography
and convolutional neural networks. Rock Mech Rock Eng 54(8):4225–4237
45. Mu HQ, Yuen KV (2020) Bayesian learning-based data analysis of uniaxial compressive strength of rock: relevance
feature selection and prediction reliability assessment. ASCE-ASME J Risk Uncertain Eng Syst Part A Civil Eng
6(1):04019018
46. Sakız U, Kaya GU, Yaralı O (2021) Prediction of drilling rate index from rock strength and cerchar abrasivity index
properties using fuzzy inference system. Arab J Geosci 1(5):354
47. Yang Z, Wu Y, Zhou Y, Tang H, Fu S (2022) Assessment of machine learning models for the prediction of rate-
dependent compressive strength of rocks. Minerals 12(6):731
48. Wen T, Li D, Wang Y, Hu M, Tang R (2024) Machine learning methods for predicting the uniaxial compressive
strength of the rocks: a comparative study. Front Earth Sci 18(2):1–12
49. Sabri MS, Jaiswal A, Verma AK, Singh TN (2024) Advanced machine learning approaches for uniaxial compressive
strength prediction of Indian rocks using petrographic properties. Multiscale Multidiscip Model Exp Des 7(6):1–22
50. Read GJ, Cox JA, Hulme A, Naweed A, Salmon PM (2021) What factors inﬂuence risk at rail level crossings? A
systematic review and synthesis of ﬁndings using systems thinking. Saf Sci 138:105207
51. Liberati A, Altman DG, Tetzlaff J, Mulrow C, Gøtzsche PC, Ioannidis JP, Clarke M, Devereaux PJ, Kleijnen J, Moher
D (2009) The PRISMA statement for reporting systematic reviews and meta-analyses of studies that evaluate health
care interventions: explanation and elaboration. Annals Intern Med 151(4):W-65
52. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, Shamseer L, Tetzlaff JM, Moher D
(2021) Updating guidance for reporting systematic reviews: development of the PRISMA 2020 statement. J Clin
Epidemiol 134:103–112
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20749

---

## Page 30
53. Moher D, Liberati A, Tetzlaff J, Altman DG (2010) Preferred reporting items for systematic reviews and meta-
analyses: the PRISMA statement. Int J Surg 8(5):336–341
54. Ali E, Guang W, Ibrahim A (2014) Empirical relations between compressive strength and microfabric properties of
amphibolites using multivariate regression, fuzzy inference and neural networks: a comparative study. Eng Geol
183:230–240
55. Umrao RK, Sharma LK, Singh R, Singh TN (2018) Determination of strength and modulus of elasticity of hetero-
geneous sedimentary rocks: an ANFIS predictive technique. Measurement 126:194–201
56. Azarafza M, Hajialilue Bonab M, Derakhshani R (2022) A deep learning method for the prediction of the index
mechanical properties and strength parameters of marlstone. Materials 15(19):6899
57. Heidari M, Mohseni H, Jalali SH (2018) Prediction of uniaxial compressive strength of some sedimentary rocks by
fuzzy and regression models. Geotech Geol Eng 36:401–412
58. Aggarwal CC (2018) Neural Networks and Deep Learning, 2nd edn. Yorktown Heights, New York
59. Wei X, Shahani NM, Zheng X (2023) Predictive modeling of the uniaxial compressive strength of rocks using an
artiﬁcial neural network approach. Mathematics 11(7):1650
60. Armaghani DJ, Mamou A, Maraveas C, Roussis PC, Siorikis VG, Skentou AD, Asteris PG (2021) Predicting the
unconﬁned compressive strength of granite using only two non-destructive test indexes. Geomech Eng 25(4):317–330
61. Jahed Armaghani D, Safari V, Fahimifar A, Mohd Amin MF, Monjezi M, Mohammadi MA (2018) Uniaxial com-
pressive strength prediction through a new technique based on gene expression programming. Neural Comput Appl
30:3523–3532
62. Ebdali M, Khorasani E, Salehin S (2020) A comparative study of various hybrid neural networks and regression
analysis to predict unconﬁned compressive strength of travertine. Innov Infrastruct Solut 5:1–14
63. Torabi-Kaveh M, Naseri F, Saneie S, Sarshari B (2015) Application of artiﬁcial neural networks and multivariate
statistics to predict UCS and E using physical properties of Asmari limestones. Arab J Geosci 8:2889–2897
64. Abdelhedi M, Jabbar R, Said AB, Fetais N, Abbes C (2023) Machine learning for prediction of the uniaxial com-
pressive strength within carbonate rocks. Earth Sci Inf 16(2):1473–1487
65. Heidarian M, Jalalifar H, Rafati F (2016) Prediction of rock strength parameters for an Iranian oil ﬁeld using neuro-
fuzzy method. J AI Data Min 4(2):229–234
66. Asheghi R, Abbaszadeh Shahri A, Khorsand Zak M (2019) Prediction of uniaxial compressive strength of different
quarried rocks using metaheuristic algorithm. Arab J Sci Eng 44:8645–8659
67. Li W, Tan Z (2017) Research on rock strength prediction based on least squares support vector machine. Geotech Geol
Eng 35:385–393
68. Khan NM, Cao K, Yuan Q, Bin Mohd Hashim MH, Rehman H, Hussain S, Shah KS, Khan S (2022) Application of
machine learning and multivariate statistics to predict uniaxial compressive strength and static Young’s modulus using
physical properties under different thermal conditions. Sustainability 14(16):9901
69. Mokhtari M, Behnia M (2019) Comparison of LLNF, ANN, and COA-ANN techniques in modeling the uniaxial
compressive strength and static Young’s modulus of limestone of the Dalan formation. Nat Resour Res 28:223–239
70. Miah MI, Ahmed S, Zendehboudi S, Butt S (2020) Machine learning approach to model rock strength: prediction and
variable selection with aid of log data. Rock Mech Rock Eng 53:4691–4715
71. Ghasemi E, Kalhori H, Bagherpour R, Yagiz S (2018) Model tree approach for predicting uniaxial compressive
strength and Young’s modulus of carbonate rocks. Bull Eng Geol Env 77:331–343
72. Madhubabu N, Singh PK, Kainthola A, Mahanta B, Tripathy A, Singh TN (2016) Prediction of compressive strength
and elastic modulus of carbonate rocks. Measurement 88:202–213
73. Mohamad ET, Armaghani DJ, Momeni E, Yazdavar AH, Ebrahimi M (2018) Rock strength estimation: a PSO-based
BP approach. Neural Comput Appl 30:1635–1646
74. Sharma LK, Vishal V, Singh TN (2017) Developing novel models using neural networks and fuzzy systems for the
prediction of strength of rocks from key geomechanical properties. Measurement 102:158–169
75. Singh R, Umrao RK, Ahmad M, Ansari MK, Sharma LK, Singh TN (2017) Prediction of geomechanical parameters
using soft computing and multiple regression approach. Measurement 99:108–119
76. Abdi Y, Garavand AT, Sahamieh RZ (2018) Prediction of strength parameters of sedimentary rocks using artiﬁcial
neural networks and regression analysis. Arab J Geosci 11:1–11
77. Barzegar R, Sattarpour M, Deo R, Fijani E, Adamowski J (2020) An ensemble tree-based machine learning model for
predicting the uniaxial compressive strength of travertine rocks. Neural Comput Appl 32:9065–9080
78. Fang Q, Yazdani Bejarbaneh B, Vatandoust M, Jahed Armaghani D, Ramesh Murlidhar B, Tonnizam Mohamad E
(2021) Strength evaluation of granite block samples with different predictive models. Eng Comput 37:891–908
79. I˙nce I˙, Bozdag˘ A, Fener M, Kahraman S (2019) Estimation of uniaxial compressive strength of pyroclastic rocks
(Cappadocia, Turkey) by gene expression programming. Arab J Geosci 12:1–13
80. Salehin S, Hadavandi E, Chelgani SC (2020) Exploring relationships between mechanical properties of marl core
samples by a coupling of mutual information and predictive ensemble model. Model Earth Syst Environ 6:575–583
81. Barham WS, Rabab’ah SR, Aldeeky HH, Al Hattamleh OH (2020) Mechanical and physical based artiﬁcial neural
network models for the prediction of the unconﬁned compressive strength of rock. Geotech Geol Eng 38:4779–4792
123
Neural Computing and Applications (2025) 37:20721–20753
20750
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 31
82. Ceryan N, Samui P (2020) Application of soft computing methods in predicting uniaxial compressive strength of the
volcanic rocks with different weathering degree. Arab J Geosci 13(7):288
83. Armaghani DJ, Momeni E, Asteris PG (2020) Application of group method of data handling technique in assessing
deformation of rock mass. Metaheur Comput Appl 1(1):1–18
84. Fattahi H (2020) A new method for forecasting uniaxial compressive strength of weak rocks. J Min Environ
11(2):505–515
85. Saldan˜a M, Gonza´lez J, Pe´rez-Rey I, Jeldres M, Toro N (2020) Applying statistical analysis and machine learning for
modeling the UCS from P-wave velocity, density and porosity on dry travertine. Appl Sci 10(13):4565
86. Mahmoodzadeh A, Mohammadi M, Ibrahim HH, Abdulhamid SN, Salim SG, Ali HFH, Majeed MK (2021) Artiﬁcial
intelligence forecasting models of uniaxial compressive strength. Transp Geotech 27:100499
87. Moussas VC, Diamantis K (2021) Predicting uniaxial compressive strength of serpentinites through physical, dynamic
and mechanical properties using neural networks. J Rock Mech Geotech Eng 13(1):167–175
88. Nasiri H, Homafar A, Chelgani SC (2021) Prediction of uniaxial compressive strength and modulus of elasticity for
Travertine samples using an explainable artiﬁcial intelligence. Res Geophys Sci 8:100034
89. O¨ zdemir E (2022) A new predictive model for uniaxial compressive strength of rock using machine learning method:
artiﬁcial intelligence-based age-layered population structure genetic programming (ALPS-GP). Arab J Sci Eng
47(1):629–639
90. Shahani NM, Kamran M, Zheng X, Liu C, Guo X (2021) Application of gradient boosting machine learning algorithms
to predict uniaxial compressive strength of soft sedimentary rocks at Thar Coalﬁeld. Adv Civil Eng 1:2565488
91. Yesiloglu-Gultekin N, Gokceoglu C (2022) A comparison among some nonlinear prediction tools on indirect deter-
mination of uniaxial compressive strength and modulus of elasticity of basalt. J Nondestr Eval 41(1):10
92. Dadhich S, Sharma JK, Madhira M (2022) Prediction of uniaxial compressive strength of rock using machine learning.
J Instit Eng (India) Ser A; 103(4): 1209–1224
93. Hassan MY, Arman H (2022) Several machine learning techniques comparison for the prediction of the uniaxial
compressive strength of carbonate rocks. Sci Rep 12(1):20969
94. Ko¨ken E, Kadakçı Koca T (2022) Evaluation of soft computing methods for estimating tangential young modulus of
intact rock based on statistical performance indices. Geotech Geol Eng 40(7):3619–3631
95. Rezaei M, Asadizadeh M (2020) Predicting unconﬁned compressive strength of intact rock using new hybrid intelligent
models. J Min Environ 11(1):231–246
96. Asare EN, Affam M, Ziggah YY (2023) A hybrid intelligent prediction model of autoencoder neural network and
multivariate adaptive regression spline for uniaxial compressive strength of rocks. Model Earth Syst Environ
9(3):3579–3595
97. Koopialipoor M, Asteris PG, Mohammed AS, Alexakis DE, Mamou A, Armaghani DJ (2022) Introducing stacking
machine learning approaches for the prediction of rock deformation. Transp Geotech 34:100756
98. Xue X (2022) A novel model for prediction of uniaxial compressive strength of rocks. Comptes Rendus Me´c
350(G1):159–170
99. Lei Y, Zhou S, Luo X, Niu S, Jiang N (2022) A comparative study of six hybrid prediction models for uniaxial
compressive strength of rock based on swarm intelligence optimization algorithms. Front Earth Sci 10:930130
100. Xu B, Tan Y, Sun W, Ma T, Liu H, Wang D (2023) Study on the prediction of the uniaxial compressive strength of
rock based on the SSA-XGBoost model. Sustainability 15(6):5201
101. Wu Z, Wu Y, Weng L, Li M, Wang Z, Chu Z (2024) Machine learning approach to predicting the macro-mechanical
properties of rock from the meso-mechanical parameters. Comput Geotech 166:105933
102. Le TT, Skentou AD, Mamou A, Asteris PG (2022) Correlating the unconﬁned compressive strength of rock with the
compressional wave velocity effective porosity and schmidt hammer rebound number using artiﬁcial neural networks.
Rock Mech Rock Eng 55(11):6805–6840
103. Li C, Zhou J, Dias D, Gui Y (2022) A kernel extreme learning machine-grey wolf optimizer (KELM-GWO) model to
predict uniaxial compressive strength of rock. Appl Sci 12(17):8468
104. Li J, Li C, Zhang S (2022) Application of six metaheuristic optimization algorithms and random forest in the uniaxial
compressive strength of rock prediction. Appl Soft Comput 131:109729
105. Mokhtari M (2022) Predicting the Young’s modulus and uniaxial compressive strength of a typical limestone using the
principal component regression and particle swarm optimization. J Eng Geol 16(1):95
106. Qiu J, Yin X, Pan Y, Wang X, Zhang M (2022) Prediction of uniaxial compressive strength in rocks based on extreme
learning machine improved with metaheuristic algorithm. Mathematics 10(19):3490
107. Zhang H, Wu S, Zhang Z (2022) Prediction of uniaxial compressive strength of rock via genetic algorithm—selective
ensemble learning. Nat Resour Res 31(3):1721–1737
108. Zhao T, Song C, Lu S, Xu L (2022) Prediction of uniaxial compressive strength using fully Bayesian Gaussian process
regression (fB-GPR) with model class selection. Rock Mech Rock Eng 55(10):6301–6319
109. Afolagboye LO, Ajayi DE, Afolabi IO (2023) Machine learning models for predicting unconﬁned compressive
strength: a case study for Precambrian basement complex rocks from Ado-Ekiti. Southwest Niger Sci Afr 20:e01715
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20751

---

## Page 32
110. Khajevand R (2023) Prediction of the uniaxial compressive strength of rocks by soft computing approaches. Geotech
Geol Eng 41(6):3549–3574
111. Li C, Zhou J, Dias D, Du K, Khandelwal M (2023) Comparative evaluation of empirical approaches and artiﬁcial
intelligence techniques for predicting uniaxial compressive strength of rock. Geosciences 13(10):294
112. Wang H, Zhang C, Zhou B, Xue S, Jia P, Zhu X (2023) Prediction of triaxial mechanical properties of rocks based on
mesoscopic ﬁnite element numerical simulation and multi-objective machine learning. J King Saud Univ Sci
35(7):102846
113. Kainthola A, Singh PK, Verma D, Singh R, Sarkar K, Singh TN (2015) Prediction of strength parameters of Himalayan
rocks: a statistical and ANFIS approach. Geotech Geol Eng 33:1255–1278
114. Yu Z, Zhou J, Hu L (2023) Prediction of compressive strength of granite: use of machine learning techniques and
intelligent system. Earth Sci Inf 16(4):4113–4129
115. Kochukrishnan S, Krishnamurthy P, Kaliappan N (2024) Comprehensive study on the Python-based regression
machine learning models for prediction of uniaxial compressive strength using multiple parameters in Charnockite
rocks. Sci Rep 14(1):7360
116. Mohammadi BM, Ramezanzadeh A, Tokhmechi B, Mehrad M, Davoodi S (2023) Estimation of geomechanical rock
characteristics from speciﬁc energy data using combination of wavelet transform with ANFIS-PSO algorithm. J Petrol
Explor Prod Technol 13(8):1715–1740
117. Davoodi S, Mehrad M, Wood DA, Rukavishnikov VS, Bajolvand M (2023) Predicting uniaxial compressive strength
from drilling variables aided by hybrid machine learning. Int J Rock Mech Min Sci 170:105546
118. Gamal H, Alsaihati A, Elkatatny S, Haidary S, Abdulraheem A (2021) Rock strength prediction in real-time while
drilling employing random forest and functional network techniques. J Energy Resour Technol Trans ASME
143(9):093004
119. Siddig OM, Al-Afnan SF, Elkatatny SM, Abdulraheem A (2022) Drilling data-based approach to build a continuous
static elastic moduli proﬁle utilising artiﬁcial intelligence techniques. J Energy Resour Technol Trans ASME
144(2):023001
120. Hiba M, Ibrahim AF, Elkatatny S (2022) Real-time prediction of tensile and uniaxial compressive strength from
artiﬁcial intelligence-based correlations. Arabian J Geosci 15(19):1546
121. Daniel C, Yin X, Huang X, Busari JA, Daniel AI, Yu H, Pan Y (2024) Bayesian optimization-enhanced ensemble
learning for the uniaxial compressive strength prediction of natural rock and its application. Geohazard Mech. https://
doi.org/10.1016/j.ghm.2024.05.002
122. Khatti J, Grover KS (2024) Prediction of uniaxial strength of rocks using relevance vector machine improved with dual
kernels and metaheuristic algorithms. Rock Mech Rock Eng 57:1–32
123. Mishra DA, Srigyan M, Basu A, Rokade PJ (2015) Soft computing methods for estimating the uniaxial compressive
strength of intact rock from index tests. Int J Rock Mech Min Sci 80:418–424
124. Aboutaleb S, Behnia M, Bagherpour R, Bluekian B (2018) Using non-destructive tests for estimating uniaxial com-
pressive strength and static Young’s modulus of carbonate rocks via some modeling techniques. Bull Eng Geol Env
77:1717–1728
125. Mahdiabadi N, Khanlari G (2019) Prediction of uniaxial compressive strength and modulus of elasticity in calcareous
mudstones using neural networks, fuzzy systems, and regression analysis. Period Polytech Civil Eng 63(1):104–114
126. Saedi B, Mohammadi SD, Shahbazi H (2018) Prediction of uniaxial compressive strength and elastic modulus of
migmatites using various modeling techniques. Arab J Geosci 11:1–14
127. Roy DG, Singh TN (2020) Predicting deformational properties of Indian coal: soft computing and regression analysis
approach. Measurement 149:106975
128. Jing H, Nikafshan Rad H, Hasanipanah M, Jahed Armaghani D, Qasem SN (2021) Design and implementation of a
new tuned hybrid intelligent model to predict the uniaxial compressive strength of the rock using SFS-ANFIS. Eng
Comput 37:2717–2734
129. Teymen A, Mengu¨ç EC (2020) Comparative evaluation of different statistical tools for the prediction of uniaxial
compressive strength of rocks. Int J Min Sci Technol 30(6):785–797
130. Xue X, Wei Y (2020) A hybrid modelling approach for prediction of UCS of rock materials. Comptes Rendus Me´c
348(3):235–243
131. Gu¨l E, Ozdemir E, Sarıcı DE (2021) Modeling uniaxial compressive strength of some rocks from Turkey using soft
computing techniques. Measurement 171:108781
132. Rahman T, Sarkar K (2021) Lithological control on the estimation of uniaxial compressive strength by the P-wave
velocity using supervised and unsupervised learning. Rock Mech Rock Eng 54(6):3175–3191
133. Jan MS, Hussain S, Zahra R, Emad MZ, Khan NM, Rehman ZU, Cao K, AlariﬁSS, Raza S, Sherin S, Salman M
(2023) Appraisal of different artiﬁcial intelligence techniques for the prediction of marble strength. Sustainability
15(11):8835
134. Tian H, Shu J, Han L (2019) The effect of ICA and PSO on ANN results in approximating elasticity modulus of rock
material. Eng Comput 35:305–314
123
Neural Computing and Applications (2025) 37:20721–20753
20752
https://doi.org/10.1007/s00521-025-11517-7

---

## Page 33
135. Elkatatny S, Tariq Z, Mahmoud M, Mohamed AA (2019) An integrated approach for estimating static Young’s
modulus using artiﬁcial intelligence tools. Neural Comput Appl 31:4123–4135
136. Fang Z, Qajar J, Safari K, Hosseini S, Khajehzadeh M, Nehdi ML (2023) Application of non-destructive test results to
estimate rock mechanical characteristics—a case study. Minerals 13(4):472
137. Hasanipanah M, Jamei M, Mohammed AS, Amar MN, Hocine O, Khedher KM (2022) Intelligent prediction of rock
mass deformation modulus through three optimized cascaded forward neural network models. Earth Sci Inf
15(3):1659–1669
138. Wu K, Meng Q, Li R, Luo L, Ke Q, Wang C, Ma C (2024) A machine learning-based strategy for predicting the
mechanical strength of coral reef limestone using X-ray computed tomography. J Rock Mech Geotech Eng
16(7):2790–2800
139. Luo T, Wang J, Chen L, Sun C, Liu Q, Wang F (2024) Quantitative characterization of the brittleness of deep shales by
integrating mineral content, elastic parameters, in situ stress conditions and logging analysis. Int J Coal Sci Technol
11(1):10
140. Ren Q, Wang G, Li M, Han S (2019) Prediction of rock compressive strength using machine learning algorithms based
on spectrum analysis of geological hammer. Geotech Geol Eng 37:475–489
141. Wang Y, Hasanipanah M, Rashid ASA, Le BN, Ulrikh DV (2023) Advanced tree-based techniques for predicting
unconﬁned compressive strength of rock material employing non-destructive and petrographic tests. Materials
16(10):3731
142. Tariq Z, Abdulraheem A, Mahmoud M, Elkatatny S, Ali AZ, Al-Shehri D, Belayneh MW (2019) A new look into the
prediction of static Young’s modulus and unconﬁned compressive strength of carbonate using artiﬁcial intelligence
tools. Pet Geosci 25(4):389–399
143. Ibrahim AF, Hiba M, Elkatatny S, Ali A (2024) Estimation of tensile and uniaxial compressive strength of carbonate
rocks from well-logging data: artiﬁcial intelligence approach. J Petrol Explor Prod Technol 14(1):317–329
144. Koolivand-Salooki M, Esfandyari M, Rabbani E, Koulivand M, Azarmehr A (2017) Application of genetic programing
technique for predicting uniaxial compressive strength using reservoir formation properties. J Petrol Sci Eng 159:35–48
145. Xie H, Lin P, Kang J, Zhai C, Du Y (2024) Prediction method of rock uniaxial compressive strength based on feature
optimization and SSA-XGBoost. Sustainability 16(19):8460
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.
Authors and Afﬁliations
Stephen Akosah1
• Ivan Gratchev1
• Solomon S. R. Gidigasu2
& Ivan Gratchev
i.gratchev@grifﬁth.edu.au
Stephen Akosah
stephen.akosah@grifﬁthuni.edu.au
Solomon S. R. Gidigasu
ssrgidigasu.coe@knust.edu.gh
1
School of Engineering and Built Environment, Grifﬁth University, Parklands Drive, Gold Coast,
QLD 4222, Australia
2
Department of Geological Engineering, Kwame Nkrumah University of Science and Technology, Kumasi,
Ghana
Neural Computing and Applications (2025) 37:20721–20753
123
https://doi.org/10.1007/s00521-025-11517-7
20753

---
