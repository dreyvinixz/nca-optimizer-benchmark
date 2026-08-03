# Evaluating the performance of metaheuristic-tuned weight agnostic neural networks for crop yield prediction

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-09850-4

---

## Page 1
ORIGINAL ARTICLE
Evaluating the performance of metaheuristic-tuned weight agnostic
neural networks for crop yield prediction
Luka Jovanovic1 • Miodrag Zivkovic2 • Nebojsa Bacanin2,3,4 • Milos Dobrojevic1 • Vladimir Simic5,6,7 •
Kishor Kumar Sadasivuni8 • Erfan Babaee Tirkolaee9,10
Received: 31 October 2023 / Accepted: 12 April 2024 / Published online: 10 May 2024
 The Author(s) 2024
Abstract
This study explores crop yield forecasting through weight agnostic neural networks (WANN) optimized by a modiﬁed
metaheuristic. WANNs offer the potential for lighter networks with shared weights, utilizing a two-layer cooperative
framework to optimize network architecture and shared weights. The proposed metaheuristic is tested on real-world crop
datasets and benchmarked against state-of-the-art algorithms using standard regression metrics. While not claiming
WANN as the deﬁnitive solution, the model demonstrates signiﬁcant potential in crop forecasting with lightweight
architectures. The optimized WANN models achieve a mean absolute error (MAE) of 0.017698 and an R-squared (R2)
score of 0.886555, indicating promising forecasting performance. Statistical analysis and Simulator for Autonomy and
Generality Evaluation (SAGE) validate the improvement signiﬁcance and feature importance of the proposed approach.
Keywords Crop yield prediction  Reptile search algorithm  Weight agnostic neural networks  Metaheuristics
1 Introduction
Agriculture has always been based on mass labor and
intensive physical work, with the results heavily dependent
on weather and climate conditions [42]. Despite the
& Erfan Babaee Tirkolaee
erfan.babaee@istinye.edu.tr
Luka Jovanovic
luka.jovanovic.191@singimail.rs
Miodrag Zivkovic
mzivkovic@singidunum.ac.rs
Nebojsa Bacanin
nbacanin@singidunum.ac.rs
Milos Dobrojevic
mdobrojevic@singidunum.ac.rs
Vladimir Simic
vsima@sf.bg.ac.rs
Kishor Kumar Sadasivuni
kishorkumars@qu.edu.qa
1
Faculty of Technical Sciences, Singidunum University,
Danijelova 32, Belgrade 11000, Serbia
2
Faculty of Informatics and Computing, Singidunum
University, Danijelova 32, Belgrade 11000, Serbia
3
Department of Mathematics, Saveetha School of
Engineering, SIMATS, Thandalam,
Chennai 602105, Tamilnadu, India
4
MEU Research Unit, Middle East University, Amman,
Jordan
5
Faculty of Transport and Trafﬁc Engineering, University of
Belgrade, Vojvode Stepe 305, Belgrade 11010, Serbia
6
Department of Industrial Engineering and Management,
College of Engineering, Yuan Ze University, Yuandong Rd.,
Zhongli Dist., Taoyuan City 320315, Taiwan
7
Department of Computer Science and Engineering, College
of Informatics, Korea University, Seoul 02841, Republic of
Korea
8
Center for Advanced Materials, Qatar University,
P.O. Box 2713, Doha, Qatar
9
Department of Industrial Engineering, Istinye University,
34396 Istanbul, Turkey
10
Department of Industrial and Mechanical Engineering,
Lebanese American University, Byblos, Lebanon
123
Neural Computing and Applications (2024) 36:14727–14756
https://doi.org/10.1007/s00521-024-09850-4
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
everlasting uncertainty of crop yields, the increasing
demand for food due to rapid population growth, Fig. 1,
has provided farmers with a stable income and thus made
agriculture the largest workforce absorber. Even nowadays,
despite modern technology and automation of agricultural
production, a third of the world’s economically active
population derives its income from agriculture [22].
New technologies facilitated and mechanized work in
agriculture, reducing the number of required farmers [24].
In the second half of the twentieth century, a signiﬁcant
effort known as the Green Revolution [17] was made to
increase the production of high-yielding cereals, especially
wheat and rice, to suppress hunger and increase yield per
plant, Fig. 2. Food production transitioned from being of
the local character, i.e., farmers producing food for their
families or communities, to global food trade which has
made diets around the world more diverse and brought new
business opportunities to farmers and processing industries
[49]. This process was not interrupted even by major events
such as the 2007–2008 Global Financial Crisis (GFC), the
recent COVID-19 pandemic, or the ongoing conﬂict in
Ukraine.
It is necessary to emphasize the fact that the problem of
hunger in the world has not been solved yet. Many coun-
tries still have a signiﬁcant percentage of the population
that cannot meet their nutritional energy needs on a regular
basis [36].
Arable land comprises only a small part of the total area
of each country. According to currently available statistical
data,  15.83 million square kilometers (mkm2) are cul-
tivated on the global level [6], i.e., just under 11% of the
total land mass, and yet only 10 countries control more
than half of the globally available arable land, Fig. 3.
A simpliﬁed assessment of the extent to which the most
populous countries are currently effective in solving the
problem of food security can be evaluated based on the
comparison of the population to available arable land ratio
and cereal yield, both compared to the global average.
Comparing the ten most populous countries in the world,
Fig. 4, the US, Brazil, and Russia have the most favorable
population to available arable land ratio (\ 1), but yet only
the US and China achieve signiﬁcantly above-average
cereal
yields,
 200%
and
 150%,
respectively.
Countries with a prevalence of undernourishment, Fig. 5,
have a mostly unfavorable ratio of population to arable
land (ratio [ 2), and cereal yields signiﬁcantly below the
global average (  40%).
Although the evident increase in crop yield was
achieved, the nutritional quality failed to keep pace.
Modern cereals suffer from deﬁciencies such as low-
quality proteins, and the lack of essential amino acids,
vitamins, and minerals [53]. The so-called ancient grains
and heirloom varieties became popular in the early twenty-
ﬁrst century, but their lower yield per plant may present a
problem in resource–poor areas where crops used by the
producer to feed his own family and livestock in subsis-
tence agriculture (food crops) are being replaced by crops
grown for proﬁt (cash crops) [18].
Intensive farming with the use of synthetic fertilizers
and pesticides increased the productivity of crops but also
increased environmental pollution and its impact on the
quality of life, which people became aware of and revived
interest
in
organic,
regenerative,
and
sustainable
Fig. 1 Global population growth with key milestones, based on [48, 66]
14728
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 3
agriculture. The European Union was a pioneer in this ﬁeld
by introducing certiﬁcation of organic food in 1991 [20].
Research interest in alternative technologies was reestab-
lished, primarily in pest management, selective breeding,
and controlled environment agriculture [60].
Until recently, it was believed that the single means of
surviving in agriculture were to increase the holdings and
productivity, with the mandatory (mis)use of chemical
fertilizers and appropriate machinery, but as mentioned
before, this approach has brought a whole new set of
challenges. In research, the scenario of industrial agricul-
tural production is considered most often, while individual
households and small farms are classiﬁed as a recurrence of
the pre-industrial form of production [22]. However, during
the COVID-19 pandemic, a signiﬁcant number of urban
households classiﬁed themselves as food insecure due to
occasional food shortages caused by disruptions in supply
chains and began producing food for their own needs
through gardening, ﬁshing, backyard livestock, etc. [40].
Trends of exurbanization and counter-urbanization gained
in popularity, where part of urban population trade the city
life for life in smaller, but healthier environments. These
people are mostly digitally savvy, work remotely, and are
not interested in industrial agriculture but may produce
organic food for their needs [11].
Crop yield forecasting could help alleviate many
uncertainties associated with food production. However, as
many factors inﬂuence production, this is not a straight-
forward task. Fluctuations in several factors, unpre-
dictable disease outbreaks, natural disasters, and many
Fig. 2 Global cereal yield and
production versus population
and land used for production
[50]
Fig. 3 Total area versus arable land (left) and percentage of global arable land (right), based on [6, 65]
Neural Computing and Applications (2024) 36:14727–14756
14729
123

---

## Page 4
other factors can severely and unforeseeable impact yields.
To help tackle this ever-pressing challenge, robust tech-
niques are needed, capable of responding to an ever-
changing environment.
One possible approach comes from the application of
artiﬁcial intelligence (AI). These algorithms mathemati-
cally mimic behaviors observed in biological brains, and
given enough computational time and data can adjust their
behaviors to suit a speciﬁc problem without explicitly
being programmed to do so. By applying powerful AI
algorithms to the task of crop yield prediction, nonlinear
relations between various factors can be observed and
leveraged to cast more accurate forecasts. These can
become a valuable tool for both farmers and policy-makers
allowing preemptive measures to be taken to prevent crop
failure and even famine. Preceding works have explored
the potential of integrating powerful machine learning
(ML) techniques to incorporate emerging technologies into
Fig. 4 Arable land versus population versus cereal yield per country on a global scale, the most populated countries, based on [6, 64]
Fig. 5 Arable land versus population versus cereal yield per country on global scale, countries with prevalence of undernourishment (% of
population), based on [6, 36, 64]
14730
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 5
agriculture systems [10] as well as other difﬁcult chal-
lenges in computing [3, 47, 59].
A notably interesting emerging class of AI algorithms
inspired by evolution and cell structures in the brain, as
well as the processes of shaping these connections comes
from neuroevolutionary algorithms. While more traditional
algorithms rely on simulated predeﬁned structures divided
into layers and organized into a network, neuroevolution-
ary algorithms are capable of evolving the structure of the
network to better suit the speciﬁc problem. The process of
selection
is
similar
to
that
of
the
genetic
algo-
rithm (GA) [38] where each potential solution is assigned a
describing genome that is altered, mutated, and combined
with other solutions to attain an optimal. This can often
result in simpler and smaller networks, requiring less
computational power to execute. Furthermore, while tra-
ditional networks heavily depend on weights and biases,
the approach of using weight agnostic neural networks
(WANN) [19] simpliﬁes the process of selecting weights,
pushing the responsibility for addressing the problem
toward network architecture.
The motivation behind employing WANN in this
research lies in the intriguing concept that a network’s
architecture can be dynamically evolved to address speciﬁc
challenges, diverging from the conventional emphasis
solely on weights and biases. This relatively unexplored
avenue within computer science offers a novel approach to
problem-solving. Additionally, WANN’s distinct advan-
tage in mitigating the computational complexity associated
with traditional backpropagation methods serves as a key
motivation. By streamlining the network optimization
process during training, WANN provides an efﬁcient and
promising framework for enhancing crop yield forecasting
models, prompting further exploration and investigation
within the scope of this work.
The performance of AI algorithms is heavily connected
to parameter values that deﬁne behavior. Often referred to
as hyperparameters, these are usually deﬁned by default to
ensure a good general performance of the algorithm.
Additional tuning is often required for the algorithm to
address a speciﬁc problem effectively. This task was tra-
ditionally tackled via trial and error; however, with the
increasing number of hyperparameters present in newer
algorithms, automated processes are needed.
Hyperparameter tuning can often be considered an NP-
hard task. Therefore, to tackle it effectively, algorithms
capable of resolving NP-hard problems are required. One
notably interesting subgroup of algorithms known for the
ability to tackle NP-hard problems with reasonable com-
putational resources and within realistic time frames is
swarm intelligence algorithms. These algorithms simulate
cooperative
populations
usually
observed
in
nature,
through a set of simple rules. By following these rules,
individuals allow for complex behaviors to emerge on a
global scale, allowing for effective optimization to take
place.
To effectively tackle the pressing issue of crop yield
forecasting, several problems need to be addressed as well.
To efﬁciently apply WANN, adequate parameter selections
need to be made. Furthermore, adequate weight adjust-
ments need to be made to attain satisfying results when
applied to this speciﬁc problem.
This work proposes a two-layer cooperative framework
based on metaheuristics optimization algorithms. The ﬁrst
layer (L1) is tasked with optimizing the WANN hyperpa-
rameters to efﬁciently select the best possible network
architecture suited to crop yield forecasting. The best
models created by L1 are passed on to layer two (L2)
where shared weights are further optimized. Additionally, a
modiﬁed version of the recently introduced RSA is
developed and applied within the context of the opti-
mization framework. This approach has been evaluated on
two real-world datasets, and the results compared with
several state-of-the-art metaheuristics tuned WANN as
well as several standard ML, and AI models applied to the
same problem. Finally, the best-performing models have
been subjected to statistical evaluations to determine the
signiﬁcance of the attained improvements, followed by a
Simulator
for
Autonomy
and
Generality
Evaluation
(SAGE) [21] analysis to determine what features have the
highest impact on the model predictions.
The scientiﬁc contributions of this work may be sum-
marized as the following:
•
A proposal of a novel WANN-based approach for
forecasting crop yields.
•
An introduction of a cooperative two-layer framework
for WANN structure optimization and shared weights
tuning
•
An introduction of a modiﬁed version of the RSA
metaheuristics which is incorporated into the proposed
framework.
The remainder of this work is structured according to the
following: Sect. 2 presents preceding research that has
contributed to the conducted work. In Sect. 3, the proposed
method is described in detail, and the logic behind the
modiﬁed metaheuristic is elaborated. The experimental
setup and developed two-layer experimental framework, as
well as the two utilized datasets, are described in Sect. 4,
and the attained results are presented and discussed in
Sect. 5. Finally, Sect. 6 gives a few concluding words on
the work and presents proposals for future research.
Neural Computing and Applications (2024) 36:14727–14756
14731
123

---

## Page 6
2 Background and related work
The concept of precision agriculture implies the application
of Information and Communication Technologies (ICT) to
provide better situational awareness on the farm, and
therefore provide the possibility of making more effective
decisions. Smart farms are systems with a multi-layered
structure that allows individual components to be added or
removed according to speciﬁc needs. IoT enables the col-
lection,
transmission,
and
exchange
of
information
between components, while AI brings automation of sys-
tem management through autonomous decision-making.
Optimum crop management requires prior soil analysis
and assessment of irrigation needs. Then, the estimate of
actual crop growth and yield can be compared with pro-
jections, taking into account weather conditions and other
factors. Deep convolutional neural networks (CNN or
DCNN) combine the ability to recognize objects by shape,
color, and texture. Computer vision (CV) and YOLOv3
algorithm may be successfully used, with a precision of
over 92%, by harvesting robots for fruit detection and yield
counting, as described in [32]. AI, CV, and YOLO can also
help in the real-time detection of crop diseases, e.g., early
blight disease in potato ﬁelds, apple scab and rust, or
grapevine disease, just to name a few [51]. Existing algo-
rithms for fruit recognition are the basis for creating a new
generation of robots capable of solving the problem of
labor shortages for fruit harvesting.
Precise crop yield estimation may prove to be difﬁcult
due to complex, interrelated environmental factors. Sig-
niﬁcant variations in the assessment can be inﬂuenced by
weather changes in different stages of plant growth, spatial
variability of soil properties, crop rotation, fertilization,
irrigation, etc. There are two basic approaches when esti-
mating crop yields, a crop growth model and a data-driven
model.
The existing literature on crop yield forecasting has
witnessed advancements in various methodologies; how-
ever, a notable research gap exists concerning the explo-
ration and optimization of WANN in this context. While
the potential of WANNs to generate lightweight networks
with shared weights has been acknowledged, their appli-
cation and optimization for crop yield forecasting remain
underexplored. The majority of studies in this domain
focus on traditional approaches or lack comprehensive
investigations into leveraging the capabilities of WANNs.
This research aims to bridge this gap by introducing a
novel two-layer cooperative framework and a modiﬁed
metaheuristic to optimize WANN parameters for enhanced
crop yield forecasting accuracy. The proposed methodol-
ogy addresses the current gap by providing a systematic
exploration of WANNs in the speciﬁc context of crop yield
prediction,
offering
insights
that
contribute
to
the
advancement of predictive modeling in agriculture.
Various mathematical models, the so-called crop growth
models can be used to simulate the interaction of plant
physiological processes with the environment. For the
model to work, it is necessary to provide real data on the
type of soil, solar radiation, precipitation, temperature
changes, adopted management practices, etc. Semi-empir-
ical crop models may provide fair results [25, 46, 61], but
they are expensive in terms of time and money and
impractical for mass applications and agricultural planning.
The empirical approach is more practical and easier to
use than the crop growth model. Here, yield data from the
recent past is used, and a set of the most inﬂuential
parameters on yield variation is determined. Accepting
these parameters as independent, and the harvest yield as
the dependent variable, empirical equations are formed to
calculate the coefﬁcients of these parameters, which are
then used for the ﬁnal estimation of the crop yield. This
approach is economically more viable and easier to
implement and does not require prior information about the
physiological processes involved in plant growth or a
predeﬁned model structure [39].
Modern ICT provided the basis for agriculture to
become more efﬁcient, ﬁrst by massively embracing web
technologies in the early twenty-ﬁrst century. A decade
later, the emergence of affordable sensors, microcon-
trollers, single-board computers (SBC), and eventually
wireless sensor networks (WSN), has inevitably led to the
ever-expanding use of modern electronics in agriculture,
both industrial and subsistence, with the aim of data col-
lection, transfer, aggregation, and analytics, all toward
tasks automation and increased productivity. Internet of
Things (IoT), fog computing (FC), and cloud computing
(CC) have become indispensable components of modern
farming (Fig. 6).
Metaheuristic algorithms have proven to be powerful
optimization algorithms, with the ability to address even
NP-hard problems. Swarm intelligence algorithms are
notably interesting for their ability to tackle these problems
using a relatively simple set of rules imposed on a popu-
lation. By following these rules, overarching behaviors
occur on a global scale leading the algorithm toward
promising areas in the search space and eventually optimal
solutions.
Some notably powerful algorithms are inspired by nat-
ure such as the artiﬁcial bee colony (ABC) [15, 29] algo-
rithm, ﬁreﬂy algorithm (FA) [30, 67], particle swarm
optimization (PSO) [62]
algorithm,
bat
algorithm
(BA) [68],
Harris
hawks
optimization
algo-
rithm (HHO) [23],
and
whale
optimization
algo-
rithm (WOA) [37].
More
novel
algorithm
examples
include the reptile search algorithm (RSA) [1] and the
14732
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 7
chimp optimization algorithm (ChOA) [31]. Finally, while
demonstrating admirable performance, these algorithms do
not come without shortcomings, and one notable approach
for
improving
performance
comes
from
algorithm
hybridization.
Hybrid algorithms have been applied to several real-
world problems and demonstrated admirable performance.
Some notable examples come from health care [8, 70].
Ways of tackling computer security issues have also been
improved through the use of hybrid algorithms [26, 69].
Forecasting has also been improved with hybrid algorithms
as demonstrated on crude oil [27], stock prices [4, 28], and
energy prediction [45, 56].
3 Methods
The following section presents an overview of WANN
principles. After this, the original RSA is presented fol-
lowed by the introduced modiﬁcations. Finally, the pro-
posed two-layer framework is presented and discussed.
3.1 Weight agnostic artificial neural networks
Weight agnostic neural network is a neural architecture
search (NAS) technique and an evolutionary strategy in the
development of neural networks where the model weights
are not trained [19]. The goal is to ﬁnd the smallest neural
network architecture capable of coping with several
reinforcement learning (RL) tasks without training weights.
WANNs are inspired by animals where newborns come
with innate reﬂexes (e.g., walking, swimming, and hiding
from predators), not having to acquire them through trial
and error, i.e., training. The task of WANN is to provide
satisfactory performance with a single common weight,
even when randomly assigned.
WANNs imply smaller network sizes, with fewer con-
nections between nodes and with the optimal overall
architecture. Performance depends exclusively on the net-
work architecture and can prove to be inferior compared to
other methods, based on the given scenario. The model
weights are not optimized for the given task and therefore
are underutilized, and there are no clear stopping criteria
since the search space is unbounded. A low number of
iterations will lead to poor network performance, while too
many iterations will take more computing resources than
necessary [35].
The WANN algorithm can be described through the
following steps:
1.
Initialize. Generate an initial population of minimal
neural network topologies, consisting of input and
output layers.
2.
Evaluate. Each network’s performance with the dif-
ferent common values assigned in each pass. Use of a
ﬁxed sequence, e.g., - 2, - 1, - 0.5, ? 0.5, ? 1, and
? 2, can help reduce the variance between evaluations,
Fig. 6 Data ﬂow in agriculture—Active/passive remote sensing, IoT and fog/cloud computing
Neural Computing and Applications (2024) 36:14727–14756
14733
123

---

## Page 8
and use of the values greater than 2 will lead to similar
behavior due to saturation of the activation functions.
3.
Rank. After evaluation, the networks get ranked based
on the achieved performance and simplicity. Compar-
ing two network models with similar performance, the
one with the simpler structure gets chosen.
4.
Vary. New network topologies are created by mutation
of existing simple networks by adding nodes, and
neurons or changing the activation function, and the
best
topology
gets
chosen
through
tournament
selection.
At this point, the algorithm may go back to Step (2), and
the process repeats. The outcome is weight agnostic
topology of gradually increasing complexity and enhanced
performance in each successive generation. When the
number of iterations hits the allowed maximum, the algo-
rithm will stop.
WANNs are capable of learning abstract associations,
without the need for encoding explicit relationships
between inputs. The use of learned features can be evalu-
ated through the execution of continuous control tasks, e.g.,
CartPoleSwingUP,
BipedalWalker,
and
CarRacing-v0
tasks as described in [5, 19].
Unlike the conventional ﬁxed topology networks which
require extensive tuning in order to produce desired
behavior, WANNs may accomplish this with random
shared weights due to architecture strongly biased toward
solution. Although the magnitude of weights may not be
crucial, their respective value and consistency of sign are,
and thus, WANNs can fail with randomly assigned indi-
vidual weights. Finally, the use of single shared weight is
much simpler compared to the use of gradient-based
methods.
Besides RL tasks, WANNs may also be used in solving
high-dimensional classiﬁcation tasks, e.g., image classiﬁ-
cation, as demonstrated on MNIST dataset in [19, 34].
Restricted to a single weight value, WANNs performed in
MNIST digits classiﬁcation as well as a single-layer neural
network with thousands of weights, and yet, the WANN
structure remains ﬂexible to allow further weight training
and accuracy improvements.
WANNs structure provides different predictions at each
weight value, which may be treated as a distinct classiﬁer.
This gives the possibility of use of a single WANN with
multiple weight values as a self-contained ensemble. Vice
versa, as WANNs are optimized to perform well using a
shared weight over a range of values, this single parameter
can be used to increase the network performance, which
may prove to be useful in few-shot learning [16] and
continual learning [43].
3.2 Original reptile search algorithm (RSA)
Inspired by the social, hunting, and encircling behaviors of
crocodiles, the RSA algorithm is a novel gradient-free and
population-based optimization algorithm originally intro-
duced by [1]. By mathematically simulating these pro-
cesses, the RSA can address complex tasks. By simulating
agent cooperation robustness is further augmented. The
algorithm is comprised of several stages described below.
3.2.1 Initialization stage
The ﬁrst step in the optimization procedure is creating a
population of agents (X) as per Eq. 1 that represents
potential solutions. These solutions are created through a
stochastic process. The best-attained solution is treated as
optimal through subsequent iterations.
X ¼
x1;1
  
x1;j
x1;n1
x1;n
x2;1
  
x2;j
  
x2;n
..
.
..
.
..
.
..
.
..
.
xi;1
  
xi;j
  
xi;n
..
.
..
.
..
.
..
.
..
.
xN1;1
  
xN1;j
  
xN1;n
xN;1
  
xN;j
xN;n1
xN;n
2
66666666666664
3
77777777777775
ð1Þ
in this context, X refers to a collection of potential solutions
that are generated randomly using Eq. 2. Here xi;j repre-
sents the value at the j-th position of the i-th solution. N
represents the total number of potential solutions in the set
X, and n represents the dimension size of the given
problem.
xij ¼ rand  ðUB  LBÞ þ LB; j ¼ 1; 2; . . .; n
ð2Þ
in which the term rand refers to a randomly generated
value. The lower and upper bounds of the given problem
are represented by LB and UB, respectively.
3.2.2 Encircling (exploration) stage
The algorithm employs two distinct search stages: explo-
ration and exploitation. The transition between behaviors is
determined by four variables, which involve separating
iterations into four segments. During the exploration phase,
the RSA deploys different search strategies to explore the
search space and approach a better solution. These strate-
gies include the high walking strategy and the belly
walking strategy.
The current stage of searching is governed by two
conditions, with the high walking movement strategy
triggered for t values less than or equal to T
4, and the belly
14734
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 9
walking movement strategy activated for t values between
T
4and T
2, as well as t values greater than T
4. This indicates that
the aforementioned condition is met during approximately
half of the total exploration iterations, with high walking
and belly walking strategies being utilized for the respec-
tive portions. Both of these approaches involve explo-
ration-based search techniques. Additionally, to generate
diverse solutions and explore varied regions, a stochastic
scaling coefﬁcient is considered for each element. This
coefﬁcient follows a simple rule that mimics the encircling
behavior of crocodiles. In this study, we introduce position
updating equations for the exploration stage, as outlined in
Eq. 3.
xx;jðt þ 1Þ
¼
BestjðtÞ  gði;jÞðtÞ  b  Rði;jÞðtÞ  rand;
t  T
4
BestjðtÞ  xðr1;jÞ  ESðtÞ  rand;
t  T
2 and t [ T
4
8
>
<
>
:
ð3Þ
where the j-th position in the best solution obtained so far is
represented by BestjðtÞ. The variable rand represents a
random number ranging from 0 to 1. The value of t indi-
cates the current iteration number, while T represents the
maximum iteration count. The operator gði;jÞ is used for
hunting and corresponds to the j-th position in the i-th
solution. By applying Eq. (4), gði;jÞ can be computed. The
parameter b, ﬁxed at 0.1, determines explorative accuracy
during the encircling stage. It determines the high walking
behavior over iterations. The reduction function, Rði;jÞ, is
used to decrease the search area and is calculated using
Eq. (5). The position of the i-th solution is denoted by
xðr1;jÞ, where r1 is a random number between 1 and N. The
value in N represents population size. The probability ratio,
ESðtÞ, takes decreasing random values in the range ½2; 2
over the iterations and is calculated using Eq. (6)
gði;jÞ ¼BestjðtÞ  Pði;jÞ;
ð4Þ
Rði;jÞ ¼ BestjðtÞ  xðr2;jÞ
BestjðtÞ þ 
;
ð5Þ
ESðtÞ ¼2  r3  ð1  1
TÞ;
ð6Þ
in the given equations, the value of epsilon is small, r2 is an
arbitrary value from a range [1, N]. The correlation value
of 2 is used in Eq. (6) to generate values in the range [2, 0],
while r3 represents a random integer value in the range
½1; 1. The percentage difference between the j-th location
of the optimal obtained solution so far and the j-th position
of the current solution is indicated by Pði;jÞ. This value is
computed with Eq. (7)
Pði;jÞ ¼ a þ
xði;jÞMðxiÞ
BestjðtÞ  ðUBðjÞ  LBðjÞ þ 0
ð7Þ
in which, MðxiÞ represents the average position of the i-th
agent, which can be determined using Eq. (8). The upper
and lower boundaries of the j-th position are represented by
UBðjÞ and LBðjÞ, respectively. The parameter a, ﬁxed at
0.1, represents a sensitive control value that determines the
exploration accuracy, which determines the difference
between agent ﬁtness during hunting through the run.
MðxiÞ ¼ 1
n
X
n
j¼1
xði; jÞ:
ð8Þ
3.2.3 Hunting (exploitation) stage
This section describes the predatory behavior of RSA,
which involves hunting. The hunting behavior of croco-
diles is discussed, speciﬁcally their two strategies: hunting
coordination and cooperation. These strategies utilize dif-
ferent intensiﬁcation techniques, which focus on exploiting
local search areas. With their intensiﬁed approach, croco-
diles can more easily approach their target prey compared
to encircling mechanisms. As a result, the exploitation can
identify a near-optimal solution, although it may require
multiple attempts. In addition, during this stage, exploita-
tion mechanisms are utilized to conduct a more focused
search close to the optimal solution, while also emphasiz-
ing communication between the mechanisms.
The RSA’s exploitation mechanisms use two primary
search strategies (hunting coordination and hunting coop-
eration) to explore potential solutions and locate the opti-
mal
solution.
These
strategies
are
represented
mathematically in Eq. (9). During this phase, the search is
guided by speciﬁc conditions: The hunting coordination
strategy is employed when t is between 3/4T and 2T/4,
while the hunting cooperation strategy is used when t is
between T and 3/4T. Additionally, stochastic methods are
used to generate denser solutions and focus on promising
regions locally. To simulate the hunting behavior of cro-
codiles, the authors employed a simple rule. The paper
proposes position-updating equations for the exploitation
phase, which are also represented in Eq. (9).
xx;jðt þ 1Þ
¼
BestjðtÞ  Pði;jÞðtÞ  rand;
t  3T
4 and t [ T
2
BestjðtÞ  gði;jÞðtÞ    Rði;jÞðtÞ  rand;
t  T and t [ 3T
4
8
>
<
>
:
ð9Þ
The variable BestjðtÞ represents the j-th location in the best
solution found up to the current time step t. gði;jÞ refers to
the hunting operator for the j-th location in the i-th
Neural Computing and Applications (2024) 36:14727–14756
14735
123

---

## Page 10
solution, which is determined by Eq. (4). The variable Pði;jÞ
represents the percentage difference between the j-th
location in the best solution and the j-th location in the
current agent and is computed using Eq. (7). The value of
gði;jÞ is also calculated using Eq. (4), with a small constant
value . Finally, Rði;jÞ is applied to sharing the search space
and is computed using Eq. (5).
The exploitation search mechanisms, including hunting
coordination and cooperation, aim to avoid being stuck in
local optima. The mechanisms help the exploration search
ﬁnd the optimal agent and maintain diversity among can-
didate agents. The authors designed two parameters, b and
a, to generate a stochastic variable following every itera-
tion, which facilitates exploration during the early itera-
tions and the later ones. This aspect of the search is
particularly useful when faced with local stagnation,
especially in the ﬁnal iterations.
Algorithm 1 Original RSA pseudocode
3.3 Multi-swarm RSA (MSRSA)
Metaheuristic algorithms rely on an effective balance
between the two primary mechanisms. Exploration helps
algorithms locate promising areas, while exploitation
focuses on promising regions helping locate near-optimal
(sub-optimal) solutions within the smaller region. While
these mechanisms help metaheuristics overcome many
difﬁcult and even NP-hard tasks, it is also important to note
that as per the no-free lunch (NFL) [63] theorem of opti-
mization, no single metaheuristic is equally suited to all
problems. All metaheuristics have certain advantages as
well as limitations. It is important to emphasize that con-
stant experimentation and improvement of existing meta-
heuristics
are
essential
for
determining
the
most
suitable tools for tackling emerging challenges.
One promising approach for tackling deﬁciencies pre-
sent in certain metaheuristics is hybridization. By com-
bining attributes of compatible algorithms, the resulting
approach can overcome the deﬁciencies of the original and
even produce results that are more than the sum of their
1: Initialize RSA parameters α, β and generate a solution population
2: while t < T do
3:
Determine agent ﬁtness
4:
Select best solution
5:
Update ES parameters
6:
for each solution i in N do
7:
for each solution j in n do
8:
Refresh parameters η, R and P
9:
if t ≤T
4 then
10:
Agents utilize the high-walking strategy described in Eq. 3
11:
else if t ≤T
2 and t > T
4 then
12:
Agents utilize the belly-walking strategy described in Eq. 3
13:
else if t ≤3t
4 and t > t
2 then
14:
Agents utilize the hunting coordination strategy described in Eq. 9
15:
else
16:
Agents utilize the hunting cooperation strategy described in Eq. 9
17:
end if
18:
end for
19:
end for
20: end while
21: return optimal attained solution Best(X)
14736
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 11
parts. While this may result in a slightly increased com-
plexity, hybrid algorithms demonstrate excellent perfor-
mance justifying the slight increase in complexity. Two
major approaches of hybridization exist today: low-level
(LLH) and high-level hybridization (HLH). In LLH, search
mechanisms of an algorithm are replaced by different
mechanisms, while in HLH can be considered as self-
contained.
The introduced metaheuristic takes the LLH approach,
introducing mechanisms of two well-known metaheuris-
tics, the ABC and FA, into the robust base of the novel
RSA. The FA is well known for its powerful exploitation
mechanism, while the ABC poses a powerful exploration
mechanism. These two algorithms are, therefore, respec-
tively, used to boost the exploration and exploitation of the
original RSA.
The initialization procedure for the introduced method
incorporates random population generation as well as two
additional mechanisms to boost initial population diversity.
The two mechanisms incorporated into the metaheuristic
are chaotic maps initialization and quasi-reﬂection-based
learning (QRL). Given a population with a size N, an initial
portion of N
2 is randomly initialized within the constraints of
the given search space. This subpopulation is then divided
into two. These are then processed using QLR and chaotic
maps, respectively. The one reminding N
4 of this population
is generated by applying chaotic maps, while the ﬁnal N
4 is
created through the use of the QRL mechanism. These
mechanisms are further described in the following.
Applying chaotic maps can help aid the search proce-
dures of metaheuristics. Several options for chaotic maps
exist; however, empirical experimentation suggests that the
application of logistic maps yields is best suited to this
application.
In the initialization stage, a pseudo-random number h0 is
used to seed a chaotic sequence as per Eq. 10
hi þ 1 ¼ lhi  ð1  hiÞ; i ¼ 1; 2; . . .; N  1
ð10Þ
in this context, N refers to the size of the population, i
represents the sequence number, and l is a control
parameter for a chaotic sequence with an empirically
selected value of 4. The value of h0 falls between 0 and 1,
but is not equal to 0.25, 0.5, 0.75, or 1.
Each potential agent is mapped based on the generated
chaotic sequence as demonstrated in Eq. 11.
Xc
i ¼ hiXi
ð11Þ
where the variable Xc
i represents the updated position of
individual i following chaotic disturbances.
The QRL method involves producing quasi-reﬂexive-
opposite solutions by following the principle that if an
individual is located far away from the optimal solution,
there is a higher likelihood that the opposite solution could
be situated closer to the optimum.
When implementing the QRL process as described
previously, the quasi-reﬂexive-opposite individual Xqr of
the solution X can be generated using Eq. 12 for each
component j of the X solution:
Xqr ¼ rnd
 LB þ UB
2
; X

ð12Þ
where rnd

LBþUB
2
; X

denotes the generation of a ran-
dom value form a uniform distribution, between LBþUB
2
and X, with LB and UB denoting the lower and upper
boundaries, respectfully. This initialization procedure is
used for every individual in the population.
The population is divided into a pair of subpopulations.
Each subpopulation is utilized to apply an LLH version of
the RSA algorithm. One population leveraging the ABC
algorithm hybridized into the RSA for a boost in explo-
ration, while the second utilizes the FA introduced in the
RSA to focus on exploitation.
The utilized mechanisms from the ABC algorithm are
described with a set of equations. The scouting phase is
described in Eq. 13.
xi;j ¼; bj þ randð0; 1Þ  ðubj  lbjÞ
ð13Þ
in which xi;j represents the j parameter of bee i form the
population, randð0; 1Þ denotes a random value from a
uniform distribution between 0 and 1, and lbj and ubJ
represent the lower and upper bounds of parameter j.
The bee and onlooker formulas are given in Eq. 14.
vi;j ¼
xi;j þ /  ðxx;j  xk;jÞ;
Rj\MR
x þ i; j;
otherwise

ð14Þ
in which xi;j denotes the j-th element of the previous
solution i, neighboring solution k parameters are denoted
with xk;j, while / denotes a random value in range [0, 1],
and MR deﬁnes the modiﬁcation rate.
The primary search mechanism for the FA algorithm is
described in Eq. 15.
xtþ1
i
¼ xt
i þ b0  ecr2
i;jðxt
j  xt
iÞ þ atðk  0:5Þ
ð15Þ
Neural Computing and Applications (2024) 36:14727–14756
14737
123

---

## Page 12
where xi and xj are the positions of the i-th and j-th ﬁreﬂies,
r ij is the distance between them, b0 and c are the
parameters controlling the attractiveness, a is the step size,
and randi is a random vector.
The hybrid search mechanisms for the LLH ABC and
FA subpopulation are shown in Algorithm 2 and Algo-
rithm 3, respectively.
Algorithm 2 ABC-RSA hybrid search process pseudocode
for solution Xi in population do
if rand(0, 1) > 0.5 then
Updated Xi with ABC search Karaboga & Basturk (2008)
else
Updated Xi with RSA search Abualigah et al. (2022)
end if
end for
Algorithm 3 FA-RSA hybrid search process pseudocode
for solution Xi in population do
if rand(0, 1) > 0.5 then
Updated Xi with FA search Yang & He (2013)
else
Updated Xi with RSA search Abualigah et al. (2022)
end if
end for
The described ABC and FA have been carefully chosen
for their characteristics. The role of the ABC algorithm is
to boost the hybrid algorithms’ exploratory power. Like-
wise, the FA has been chosen due to the potential of its
exceptionally powerful exploitation mechanism to boost
the hybrid algorithms’ exploitation power.
One additional mechanism inspired by the GA is intro-
duced called transfer learning. This mechanism considers
the best-performing individuals from each subpopulation as
Fig. 7 Structure of the two-
layer framework utilized for
research
14738
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 13
potential parents for new agents. The new agents adopt a
certain set of traits from their parents and represent a
combination of the two. This is simulated using a uniform
crossover between agent traits. To govern this process, an
additional value control parameter representing population
crossover and denoted as PC is introduced. This value has
been empirically determined to give the best results when
PC ¼ 0:1. When applying uniform crossover, two parents
are selected from a population, and offspring is generated
based on agent values, these offspring agents replace the
worst performing in each respective population. The ﬁtness
of these newly generated agents is not evaluated after
generation, thus computational complexity is maintained.
Finally, a high-level overview of the complete proposed
MS-RSA algorithm can be seen in Algorithm 4.
Algorithm 4 Introduced MSRSA algorithm high-level pseudocode
3.4 Experimental framework
The experimental cooperative framework is comprised of
two layers. Each layer is tasked with handling one speciﬁc
task. The layers are labeled Layer 1 (L1) and Layer 2 (L2).
Both evaluated datasets have been subjected to both stages
of the framework to select the optimal models suited to
forecasting yields. A visualization of the framework is
shown in Fig. 7.
3.5 Metaheuristic optimizers
Metaheuristic algorithms present a popular choice for
selecting near-optimal parameters of baseline algorithms.
Contemporary ML and AI algorithms are usually designed
with good general performance in mind. However, while
showing good general performance, algorithms usually
require adaptation for a speciﬁc problem. This is done
through a set of exposed parameters that are available to
programmers. The process of selection is not without its
challenges, as the number of combinations often makes this
an NP-hard problem. This work evaluates several con-
temporary optimizers alongside the introduced algorithms.
Brief descriptions of these algorithms, with their respective
inspirations and basic search strategies, are discussed
below.
The recently introduced ChOA [31] is inspired by the
individual intelligence and mating motivation observed in
chimpanzees during group hunting. The algorithm is
designed to address two common issues in optimization
problems: slow convergence speed and getting trapped in
local optima, especially in high-dimensional scenarios. The
algorithm incorporates a mathematical model representing
diverse intelligence and mating motivation in chimps. Four
types of simulated chimps—attacker, barrier, chaser, and
driver—are utilized to capture the range of intelligence
observed in chimpanzee groups. The hunting behavior is
divided into four main steps: driving, chasing, blocking,
and attacking.
Initialize global parameters: t = 0, T, and N.
Initialize: control parameters of ABC, FA, and RSA meta-heuristics.
Randomly generate N
2 of initial population P0
Generate N
4 of population P by applying QRL to N
4 of P0
Generate N
4 of population P by applying chaotic maps to N
4 of P0
Combine generated population into population P
Split population P in half as Pa and Pb
while t ≤T do
Apply FA-RSA hybrid search for population Pa
Apply ABC-RSA hybrid search for population Pb
Evaluate population performance
Apply transfer learning to population Pa and Pb
end while
return the best solution
Neural Computing and Applications (2024) 36:14727–14756
14739
123

---

## Page 14
Several well-known algorithms have also been com-
pared including in the comparisons as well. Such as the
GA [38], a search and optimization method inspired by
natural selection. It operates with a population of potential
solutions, represented as chromosomes. The algorithm
involves the selection of individuals based on their ﬁtness,
crossover (genetic recombination) to create offspring, and
mutation to introduce random changes. Through iterations,
the population evolves, mimicking the process of natural
evolution. GAs are versatile and effective for solving
complex optimization problems across various domains
due to their ability to explore vast solution spaces and
handle multiple local optima simultaneously.
The PSO [62] is an optimization algorithm based on the
collective behavior of social organisms, particularly the
movement patterns of bird ﬂocks or ﬁsh schools. In PSO, a
population of potential solutions is represented as particles,
each navigating through the solution space. These particles
adjust their positions based on their own experience (local
best) and the shared knowledge of the entire swarm (global
best). The movement is inﬂuenced by both the particle’s
current velocity and the historical best positions. This
collaborative exploration and exploitation process encour-
ages convergence toward optimal solutions. PSO is known
for its simplicity and efﬁciency in ﬁnding solutions to
optimization problems, particularly in continuous and high-
dimensional spaces. The algorithm’s ability to balance
exploration and exploitation makes it suitable for various
applications, including engineering, ﬁnance, and ML.
The ABC [29] algorithm is a technique inspired by the
foraging behavior of honeybees. In ABC, the population
consists of artiﬁcial bees, and the algorithm is designed to
mimic the food source exploration process observed in a
bee colony. The optimization process involves three main
components: employed bees, onlooker bees, and scout
bees. Employed bees explore the solution space, repre-
senting potential solutions. Onlooker bees select solutions
based on the employed bees’ performance and exploit these
solutions for further exploration. Scout bees, in turn,
introduce randomness by exploring new solutions when the
algorithm stagnates or fails to improve. The iterative nature
of ABC allows for the continuous reﬁnement of solutions,
making it suitable for various optimization problems,
especially in domains such as engineering, logistics, and
data analysis.
The FA [67] ) is inspired by the light-ﬂashing behavior
of ﬁreﬂies in nature. In FA, potential solutions to an opti-
mization problem are represented as ﬁreﬂies, and the
algorithm seeks to improve these solutions iteratively. The
attractiveness of a ﬁreﬂy is determined by its brightness,
inﬂuenced by both its distance from other ﬁreﬂies and their
respective brightness levels. Brighter ﬁreﬂies attract others,
and the algorithm simulates this process to converge
toward optimal solutions.
The main steps of the ﬁreﬂy algorithm include the ini-
tialization of ﬁreﬂy positions, the computation of their
attractiveness, the movement toward brighter ﬁreﬂies, and
the updating of the solution space. FA effectively balances
exploration and exploitation, making it suitable for various
optimization problems. It has been applied in ﬁelds such as
engineering, ﬁnance, and image processing, demonstrating
its versatility and effectiveness in ﬁnding solutions to
complex optimization challenges.
The BA [68] is a metaheuristic optimization method
inspired by bats’ echolocation behavior. It utilizes a pop-
ulation of virtual bats for solving optimization problems,
incorporating both local and global search strategies. BA
represents solutions as bat positions, adjusting their emis-
sion rates (loudness) for exploration–exploitation trade-
offs. The algorithm’s random walks facilitate global
exploration. Known for its simplicity and effectiveness, BA
has been successfully applied to diverse optimization
domains, including engineering, ﬁnance, and data science.
The HHO [23] algorithm is a nature-inspired optimiza-
tion technique based on the cooperative hunting behavior
of Harris’s Hawks. In HHO, potential solutions to an
optimization problem are represented as hawks, and the
algorithm mimics their collaboration during hunting. The
optimization process involves exploration, exploitation,
and communication among the hawks to improve solutions
iteratively.
The key features of HHO include the representation of
solutions as hawk positions, the integration of explorative
and exploitative movements, and the adoption of a leader-
follower strategy. The leader attracts followers based on
their ﬁtness, and the followers adjust their positions
accordingly. HHO has shown promise in solving various
optimization problems due to its ability to balance explo-
ration and exploitation inspired by the collaborative hunt-
ing nature of Harris’s hawks.
The WOA [37] is a method based on the cooperative
hunting behavior of humpback whales. It represents
potential solutions as whale positions and incorporates
exploration and exploitation strategies. WOA has demon-
strated effectiveness in solving diverse optimization prob-
lems, making it applicable to ﬁelds such as engineering,
ﬁnance, and data
14740
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 15
4 Experimental setup
During experimentation, WWANNs are assigned the task
of predicting crop yields across two distinct datasets.
Metaheuristics are employed to optimize the hyperparam-
eters of WANN within a two-layer framework to enhance
performance. The ﬁrst layer involves architecture selection,
and in the second layer, shared weights are optimized.
Subsequently, the outcomes undergo meticulous validation
and interpretation using the SAGE method.
4.1 Employed datasets
The wild blueberry (Vaccinium angustifolium Aiton) that
can be found on Kaggle 1 is inﬂuenced by cross-pollination
that requires bees [2, 12]. Thus, it is affected by current bee
density [2], but also by other factors including weather, soil
fertility, pests, disease, and others. To produce useful
results, ML algorithms for crop yield prediction generally
require large amounts of data, and the availability of
training data of sufﬁcient quality and quantity may appear
as a problem. The wild blueberry predictive yield models
require data that sufﬁciently characterize the inﬂuence of
spatial characteristics of plants, bees, and weather condi-
tions on production. Experiments may be performed on a
calibrated version of the blueberry simulation model. The
simulated dataset is examined with proper feature selection
and afterward used to build four ML-based prediction
models, which may be used for comparison with real-life
data acquired in the ﬁelds. Wild blueberry yield prediction
dataset [41, 54] was generated by a wild blueberry polli-
nation model, a spatially explicit simulation model vali-
dated
by
ﬁeld
observations,
and
experimental
data
collected in Maine (USA) during the past three decades.
Another crop yield prediction dataset [44] that can also
be found on Kaggle 2 brings yield data on the most com-
mon agricultural cultures per country per year (maize,
potatoes, rice, wheat, sorghum, soybeans, yams, cassava,
sweet potatoes, and plantains) combined with data on
average rainfall, temperature, and use of pesticides. Data
sheets were compiled from publicly available datasets from
the Food and Agriculture Organization (FAO) and World
Data Bank.
Both datasets underwent pre-processing, involving the
transformation of categorical features, notably the crop
species, through the utilization of the one-hot encoding
technique to enhance forecasting accuracy. However, this
approach results in an expansion of the feature set for each
dataset. Speciﬁcally, the crop yield dataset experienced a
transformation from the original seven features to a total of
116 features, while the blueberry dataset expanded from
the initial 18 features to a total of 17 used as inputs in the
speciﬁc test case.
4.2 Evaluation metrics
To ensure a thorough examination, several metrics have
been utilized during experimentation. The utilized metrics
include the mean square error (MSE) described in Eq. 16,
root-mean-square error (RMSE) described in Eq. 17, mean
absolute error (MAE) described in Eq. 18, as well as the
coefﬁcient of determination R2 described in Eq. 19 metric.
It is important to note that the R2 metric is utilized as the
primary guiding objective function utilized during the
network architecture selection process in L1 of the
framework. While MSE is used as an objective function
when optimizing shared weights in L2 of the framework.
MSE ¼ 1
n
X
n
i¼1
ðyi  ^yiÞ2
ð16Þ
RMSE ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
n
X
n
i¼1
ðyi  ^yiÞ2
s
ð17Þ
MAE ¼ 1
n
X
n
i¼1
jyi  ^yij
ð18Þ
R2 ¼1 
Pn
i¼1ðyi  ^yiÞ2
Pn
i¼1ðyi  yÞ2
ð19Þ
where n is the total number of observations, yi is the actual
value of the i-th observation, ^yi is the predicted value of the
i-th
observation,
and
y
is
the
mean
value
of
all
observations.
4.3 Experimental setup and framework
adjustments
The initial step is the framework involves selecting a
suitable network architecture. To accomplish this, a pop-
ulation of potential architectures is created and evolved
through a predeﬁned number of iterations. For the blue-
berry dataset, a population of 200 individuals was used
with 400 generations allocated for improvement. Due to the
larger number of input parameters, the crop yield dataset
was assigned a larger population of 300 individuals, with
800 generations allocated for improvement. Metaheuristics
were leveraged to select control parameters of the WANN.
The
parameters
selected
for
optimization
and
their
respective ranges are shown in Table 1. It is also important
to
note
that
apart
from
hyperparameters,
activation
1 https://www.kaggle.com/datasets/saurabhshahane/wild-blueberry-
yield-prediction.
2 https://www.kaggle.com/datasets/patelris/crop-yield-prediction-
dataset.
Neural Computing and Applications (2024) 36:14727–14756
14741
123

---

## Page 16
functions for each node also needed to be selected. The
considered functions include sigmoid, tanh, gauss, relu,
sin, inv, and identity. Due to extensive computation
demands, each metaheuristic was assigned a population
size of 6 and given 15 iterations to improve network
weights to attain optimal performance. Furthermore, to
provide grounds for a fair comparison, the evaluations have
been repeated over 20 independent runs to account for the
heuristics inherent in this class of algorithms.
After each iteration, individual architectures are evalu-
ated using the R2 metrics. A selection of shared weights is
assigned that are used to construct and evaluate networks.
Population ﬁtness is assessed based on the mean R2 value
of all individuals in a population tested with each possible
shared weight value. This process allows the network
architecture to grow as needed introducing new neurons
and connections for the network’s evolution to better
address the given task. The best-performing architecture is
passed to layer two or the framework.
During
L2
optimization,
each
metaheuristic
was
assigned a population size of 40 and given 30 iterations to
improve network weights to attain optimal performance.
Furthermore, to provide grounds for a fair comparison, the
evaluations have been repeated over 30 independent runs to
account for the heuristics inherent in this class of
algorithms.
In the ﬁrst stage, metaheuristic algorithms are tasked
with selecting optimal hyperparameters for the evolving
neural networks. In the second, they were tasked with
optimizing the values of the shared weights to boost net-
work performance. Several metaheuristics have been con-
sidered for tackling this task, and their performance has
been subjected to a comparative analysis with the intro-
duced MSRSA. The evaluated algorithms include the
original RSA [1] as well as the novel ChOA [31]. Several
well-known algorithms have also been compared including
the GA [38], PSO [62], ABC [29], FA [67], BA [68],
HHO [23], and WOA [37]. For each of the utilized meta-
heuristics, the parameters used during the optimizations are
the values suggested in the works that originally introduced
them. The control parameter of the proposed metaheuristics
PC was set to PC ¼ 0:1 as this value has been empirically
determined to give the best results.
5 Results and discussion
The following section demonstrates the results attained in
each layer of the framework individually. Following the
presentation, the results are discussed in detail.
5.1 L1 observed outcomes
In L1, metaheuristics algorithms were used to select opti-
mal control parameters for evolving WANN architectures
suited for yield forecasting. The results attained by net-
works optimized in L1 are shown and discussed in the
following segment.
5.1.1 Wild blueberry optimal network architecture
During the architecture selection process, ﬁtness metrics
were monitored and tracked to determine the inﬂuence of
the competing metaheuristics on the optimization process.
Table 2 demonstrates the results attained during the best,
worst, median, and mean runs, as well as the standard
deviation and results variance. Furthermore, ﬁtness con-
vergence rates are shown in Fig. 8.
As demonstrated, the networks tuned by the introduced
metaheuristic attained the best results compared to all other
metaheuristic-optimized networks.
Fitness distributions are observed in Fig. 9.
As can be observed, the proposed MSRSA attained the
lowest variation in results across several runs, suggesting
that it demonstrates the highest reliability and stability
compared to other algorithms. Furthermore, compared to
the unoptimized version of the WANN, it attained signif-
icantly better results, with the basic WANN with default
parameters obtaining a ﬁtness value of 0.056813. The
optimal evolved network architecture by L1 of the frame-
work is shown in Fig. 10.
It can be observed that the proposed MSRSA algorithm
shows the highest stability compared to other algorithms.
Finally, the best-performing network architecture is shown
in Fig. 10.
The selected hyperparameters for the best-performing
WANN model are given in Table 3
The relative simplicity of the constructed network is
worth emphasizing with a total of only 14 neuron nodes
and only 61 active weighted connections. Furthermore,
Table 1 Hyperparamaters optimized by metaheuristics in L1 with
their respective ranges
Parameter
Range
Connection addition probability
[0.1, 0.4]
Connection removal probability
[0.0, 0.1]
Node addition probability
[0.1, 0.4]
Bias mutation power within
[0.3, 0.6]
Weight mutation power
[0.3, 0.6]
Weight mutation rate
[0.6, 0.9]
Weight replacement rate
[0.05, 0.2]
Survival threshold
[0.1, 0.3]
14742
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 17
even though the ﬁtness value of the entire best population
in L1 was only 0.381873, and the relative network sim-
plicity, the optimal genome attained an admirable R2 score
of 0.884506 with a shared weight of 1. This network was
subjected to further optimization in L2 where further
improvements were attained.
5.1.2 Crop yield optimal network architecture
While network architectures were evolved, the ﬁtness
metrics were recorded to better understand the effects each
evaluated metaheuristic has on the process of optimization.
Table 4 demonstrates the results attained during the best,
worst, median, and mean runs, as well as the standard
deviation and results variance. Additionally, ﬁtness con-
vergence is demonstrated in Fig. 8.
As demonstrated, the networks tuned by the introduced
metaheuristic attained the best results compared to all other
metaheuristic-optimized networks. However, it is also
Table 2 Fitness results attained
by each metaheuristic-
optimized population for the
best, worst, median, and mean
execution for blueberry dataset
Method
Best
Worst
Mean
Median
Std
Var
WANN-L1-MSRSA
0.381873
0.362779
0.370417
0.368508
0.007330
0.000054
WANN-L1-RSA
0.362758
0.319227
0.336458
0.331924
0.016928
0.000287
WANN-L1-GA
0.354724
0.315704
0.330603
0.322799
0.016582
0.000275
WANN-L1-PSO
0.375432
0.326626
0.351029
0.351029
0.019432
0.000378
WANN-L1-ABC
0.380562
0.327283
0.352591
0.350117
0.018449
0.000340
WANN-L1-FA
0.375432
0.326626
0.344403
0.349152
0.018865
0.000356
WANN-L1-BA
0.353724
0.326346
0.342040
0.346152
0.009567
0.000092
WANN-L1-HHO
0.365758
0.336482
0.350870
0.350620
0.013798
0.000190
WANN-L1-WOA
0.380246
0.338419
0.355530
0.351727
0.016203
0.000263
WANN-L1-ChOA
0.379234
0.356906
0.366605
0.363189
0.008853
0.000078
Bold values indicate the best attained results
Fig. 8 Population ﬁtness converges rates attained by each metaheuristic for the blueberry dataset
Fig. 9 Population ﬁtness converges rates attained by each meta-
heuristic for the blueberry dataset
Neural Computing and Applications (2024) 36:14727–14756
14743
123

---

## Page 18
important to note that the performance of the population
remains relatively poor regardless of the optimization
algorithms, with the average population ﬁtness being a net
negative value. This is likely due to the relatively high
complexity of the crop yield dataset and the large number
of available features making it harder for lighter network
structures to determine adequate architectures with fewer
connections. An unoptimized version of WANN was also
tested and applied to this speciﬁc task under identical test
condictions. The resulting average population ﬁtness was
only 0:3793214, signiﬁcantly less than even the worst-
performing optimized version (Fig. 11).
Fitness distributions are observed in Fig. 12.
As can be observed, the proposed MSRSA attained the
lowest variation in results across several runs, suggesting
that it demonstrates the highest reliability and stability
compared to other algorithms. The optimal evolved net-
work architecture by L1 of the framework is shown in
Fig. 13.
The relatively simple architecture evolved by WANN
failed to sufﬁciently address this task in L1, with most
populations having a very low R 2 score. With the best
genome attaining an R 2 value of  0:103878, the selected
architecture contained a total of 15 nodes with 259 con-
nections and a shared weight value of  1:9854476. The
poor performance is very likely due to the high complexity
of the crop ﬁeld dataset, with signiﬁcantly more inputs
compared to the previous dataset. However, by optimizing
shared weights, performances can signiﬁcantly improve in
L2 of the framework.
Fig. 10 Best selected WANN model architecture for the wild blueberry yield forecasting
Table 3 Best selected WANN hyperparameters for the blueberry
dataset
Parameter
Value
Connection addition probability
0.321
Connection removal probability
0.045
Node addition probability
0.275
Bias mutation power within
0.392
Weight mutation power
0.421
Weight mutation rate
0.698
Weight replacement rate
0.093
Survival threshold
0.281
14744
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 19
5.2 L2 observed outcomes
In L2, metaheuristics are tasked with selecting optimal
shared weights within the already constructed network
architecture. The results attained by networks optimized in
L2 are shown and discussed in the following segment.
5.2.1 Wild blueberry dataset results
In the second stage of the optimization, several state-of-
the-art algorithms were tasked with ﬁne-tuning the shared
network weight. The experiments were carried out over 20
dependent runs to account for the randomness inherent to
this class of algorithms. The resulting model’s performance
was recorded, and the results are demonstrated. The
objective function used in L2 is the MSE function, and the
results attained by each metaheuristic-optimized WANN in
the best, worst, mean, and median run are demonstrated in
Table 5. The already decent performance attained in L1 is
Table 4 Fitness results attained
by each metaheuristic-
optimized population for the
best, worst, median, and mean
execution for crop yield dataset
Method
Best
Worst
Mean
Median
Std
Var
WANN-L1-MSRSA
- 0.179189
- 0.184565
- 0.181115
- 0.180533
0.002161
0.000005
WANN-L1-RSA
- 0.187728
- 0.210483
- 0.195976
- 0.189624
0.009391
0.000088
WANN-L1-GA
- 0.185432
- 0.203975
- 0.193350
- 0.194704
0.006928
0.000048
WANN-L1-PSO
- 0.183748
- 0.205798
- 0.196702
- 0.195692
0.007015
0.000049
WANN-L1-ABC
- 0.190423
- 0.209466
- 0.197658
- 0.196136
0.005251
0.000028
WANN-L1-FA
- 0.181525
- 0.205124
- 0.194586
- 0.196719
0.008725
0.000076
WANN-L1-BA
- 0.191256
- 0.208469
- 0.200727
- 0.197950
0.005915
0.000035
WANN-L1-HHO
- 0.186524
- 0.205124
- 0.196258
- 0.197453
0.005724
0.000033
WANN-L1-WOA
- 0.182385
- 0.205124
- 0.191832
- 0.191764
0.008216
0.000068
WANN-L1-ChOA
- 0.181345
- 0.192226
- 0.185199
- 0.183612
0.004382
0.000019
Bold values indicate the best attained results
Fig. 11 Population ﬁtness converges rates attained by each metaheuristic for crop yield dataset
Fig. 12 Population ﬁtness converges rates attained by each meta-
heuristic for crop yield dataset
Neural Computing and Applications (2024) 36:14727–14756
14745
123

---

## Page 20
-1
0
3827
-2
12830
43762
33279
-3
-4
-5
-6
5967
-7
-8
588
190
-9
-10
-11
-12
-13
-14
-15
-16
-17
33739
-18
-19
-20
-21
32537
-22
-23
-24
43621
-25
43580
-26
-27
40698
-28
-29
-30
-31
-32
-33
-34
-35
-36
-37
-38
-39
-40
-41
-42
-43
-44
-45
-46
-47
-48
-49
-50
47839
-51
-52
-53
-54
30360
-55
-56
-57
-58
-59
-60
-61
-62
-63
-64
-65
-66
-67
-68
-69
-70
-71
-72
-73
-74
-75
-76
-77
-78
-79
-80
-81
-82
-83
-84
-85
-86
-87
-88
-89
-90
-91
-92
-93
-94
-95
-96
-97
-98
-99
-100
-101
-102
-103
-104
-105
-106
-107
-108
-109
-110
-111
-112
-113
-114
-115
Fig. 13 Best selected WANN model architecture for the wild blueberry yield forecasting
Table 5 Overall objective
function results for each
evaluated metaheuristic-
optimized network for the
blueberry dataset
Method
Best
Worst
Mean
Median
Std
Var
WANN-MSRSA
0.003781
0.003849
0.003805
0.003784
3.00E205
9.00E210
WANN-RSA
0.003781
0.009779
0.006182
0.003788
2.94E-03
8.63E-06
WANN-GA
0.003790
0.009796
0.006391
0.004756
2.82E-03
7.95E-06
WANN-PSO
0.003781
0.009785
0.004566
0.003866
1.77E-03
3.12E-06
WANN-ABC
0.003781
0.005991
0.004264
0.003935
6.68E-04
4.46E-07
WANN-FA
0.003795
0.009787
0.005310
0.004286
2.27E-03
5.14E-06
WANN-BA
0.003781
0.009820
0.004590
0.003870
1.77E-03
3.14E-06
WANN-HHO
0.003781
0.009779
0.006180
0.003781
2.94E-03
8.64E-06
WANN-WOA
0.003781
0.007446
0.004541
0.004080
1.06E-03
1.13E-06
WANN-ChOA
0.003781
0.009799
0.005154
0.004057
2.32E-03
5.40E-06
Bold values indicate the best attained results
Table 6 Best-performing
metaheuristics optimized
models detailed evaluation
results for blueberry dataset
R 2
R
MAE
MSE
RMSE
WANN-MSRSA
0.886555
0.941571
346.011202
203217.857675
450.796914
WANN-RSA
0.886555
0.941571
346.009608
203217.857707
450.796914
WANN-GA
0.886262
0.941415
349.834464
203742.899000
451.378886
WANN-PSO
0.886547
0.941566
346.575170
203233.432952
450.814189
WANN-ABC
0.886547
0.941566
346.577654
203233.568756
450.814340
WANN-FA
0.886135
0.941348
343.011388
203970.083060
451.630472
WANN-BA
0.886549
0.941568
345.638895
203228.331793
450.808531
WANN-HHO
0.886555
0.941570
346.134007
203218.612043
450.797751
WANN-WOA
0.886542
0.941563
345.421983
203242.551190
450.824302
WANN-ChOA
0.886554
0.941570
346.255353
203220.825626
450.800206
Bold values indicate the best attained results
Table 7 Best-performing
metaheuristics optimized
models detailed evaluation
results for blueberry dataset
normalized
R 2
R
MSE
MAE
RMSE
WANN-MSRSA
0.886555
0.941571
0.047194
0.003781
0.061486
WANN-RSA
0.886555
0.941571
0.047194
0.003781
0.061486
WANN-GA
0.886262
0.941415
0.047715
0.003790
0.061565
WANN-PSO
0.886547
0.941566
0.047271
0.003781
0.061488
WANN-ABC
0.886547
0.941566
0.047271
0.003781
0.061488
WANN-FA
0.886135
0.941348
0.046785
0.003795
0.061600
WANN-BA
0.886549
0.941568
0.047143
0.003781
0.061488
WANN-HHO
0.886555
0.941570
0.047211
0.003781
0.061486
WANN-WOA
0.886542
0.941563
0.047114
0.003781
0.061490
WANN-ChOA
0.886554
0.941570
0.047227
0.003781
0.061486
Bold value indicates the best attained results
14746
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 21
further improved by metaheuristics in L2 of the framework
through shared weight ﬁne-tuning (Table 6).
As can be observed, the introduced metaheuristic
obtained the best results compared to all other evaluated
algorithms. However, to provide further insight into the
improvements made by the introduced modiﬁcations, the
best-performing models have been evaluated using addi-
tional metrics. The results are demonstrated in Table 7.
It can be observed that the introduced metaheuristic
attained the best MSE results as this was the optimization
target. Several metaheuristics share the ﬁrst place for R2
and R, while the FA-optimized WANN attained the best
MAE. This is in line with the NFL theorem, which states
that no single approach is the best for all problems.
Convergence rates of each optimized WANN through
each metaheuristic iteration are shown in Fig. 14, along-
side distribution plots of the results.
Fig. 14 Objective and R2 metrics convergence and distribution plots for blueberry dataset
Fig. 15 Compared model KDE plots for the objective and R2 function for blueberry dataset
Neural Computing and Applications (2024) 36:14727–14756
14747
123

---

## Page 22
Fig. 16 Forcasts made by the best-performing model compared to actual values for blueberry dataset
Table 8 Overall objective function results for each evaluated metaheuristic-optimized network for the crop yield dataset
Method
Best
Worst
Mean
Median
Std
Var
Shared weights
WANN-MSRSA
0.013859
0.013859
0.013859
0.013859
3.77E-09
1.42E-17
0.5090907
WANN-RSA
0.013859
0.013863
0.013860
0.013859
1.53E-06
2.33E-12
0.5092000
WANN-GA
0.013859
0.050279
0.018659
0.013896
1.10E-02
1.21E-04
0.5091530
WANN-PSO
0.013859
0.015255
0.014046
0.013893
4.07E-04
1.65E-07
0.5094388
WANN-ABC
0.013862
0.015336
0.014249
0.013945
5.10E-04
2.60E-07
0.5101118
WANN-FA
0.013862
0.014181
0.013949
0.013900
1.05E-04
1.10E-08
0.5102335
WANN-BA
0.013859
0.014491
0.014020
0.013912
2.07E-04
4.29E-08
0.5090701
WANN-HHO
0.013859
0.013859
0.013859
0.013859
1.51E209
2.29E218
0.5090904
WANN-WOA
0.013859
0.017332
0.014670
0.013951
1.22E-03
1.48E-06
0.5091373
WANN-ChOA
0.013859
0.014189
0.013970
0.013936
1.14E-04
1.30E-08
0.5088298
Bold values indicate the best attained results
Table 9 Best-performing
metaheuristics optimized
models detailed evaluation
results for crop yield dataset
R 2
R
MAE
MSE
RMSE
WANN-MSRSA
0.482586
0.694684
35,400.128652
2,995,299,339.114700
54,729.327961
WANN-RSA
0.482585
0.694683
35,397.693838
2,995,305,202.212500
54,729.381526
WANN-GA
0.482586
0.694684
35,398.742785
2,995,301,242.651200
54,729.345352
WANN-PSO
0.482576
0.694677
35,392.324638
2,995,358,929.938700
54,729.872373
WANN-ABC
0.482497
0.694620
35,376.849054
2,995,814,282.431200
54,734.032214
WANN-FA
0.482475
0.694604
35,373.996468
2,995,944,866.999200
54,735.225102
WANN-BA
0.482586
0.694684
35,400.584903
2,995,299,546.213100
54,729.329853
WANN-HHO
0.482586
0.694684
35,400.134405
2,995,299,339.147700
54,729.327962
WANN-WOA
0.482586
0.694684
35,399.090389
2,995,300,408.265700
54,729.337729
WANN-ChOA
0.482580
0.694680
35,405.883295
2,995,332,650.132000
54,729.632286
Bold values indicate the best attained results
14748
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 23
Table 10 Best-performing
metaheuristics optimized
models detailed evaluation
results for crop yield dataset
normalized
R 2
R
MAE
MSE
RMSE
WANN-MSRSA
0.482586
0.694684
0.076147
0.013859
0.117725
WANN-RSA
0.482585
0.694684
0.076142
0.013859
0.117725
WANN-GA
0.482586
0.694684
0.076144
0.013859
0.117725
WANN-PSO
0.482576
0.694677
0.076130
0.013859
0.117726
WANN-ABC
0.482497
0.694620
0.076097
0.013862
0.117735
WANN-FA
0.482475
0.694604
0.076091
0.013862
0.117738
WANN-BA
0.482586
0.694684
0.076148
0.013859
0.117725
WANN-HHO
0.482586
0.694684
0.076147
0.013859
0.117725
WANN-WOA
0.482586
0.694684
0.076145
0.013859
0.117725
WANN-ChOA
0.482580
0.694680
0.076160
0.013859
0.117726
Bold value indicates the best attained results
Fig. 17 Objective and R2 metrics convergence and distribution plots for crop yield dataset
Fig. 18 Compared model KDE plots for the objective and R2 function for crop yield dataset
Neural Computing and Applications (2024) 36:14727–14756
14749
123

---

## Page 24
It can be observed that the introduced metaheuristic
improved convergence rates in comparison with the origi-
nal algorithm. Furthermore, results distributions suggest
that the introduced algorithm demonstrates the lowest
result distribution, suggesting that the introduced algorithm
has the highest level of robustness and reliability. This is
further reinforced by the KDE plots shown in Fig. 15.
Finally, the predictions cast by the best-performing
metaheuristic-optimized WANN in comparison with actual
yields are shown in Fig. 16.
5.2.2 Crop yield dataset results
Similarly, the second optimization layer applied several
state-of-the-art algorithms tasked with ﬁne-tuning the
shared network weight for forecasting crop yield. The
experiments were carried out over 20 dependent runs to
account for the randomness inherent to this class of
algorithms.
The
resulting
model’s
performance
was
recorded, and the results are demonstrated. The objective
function used in L2 is the MSE function, and the results
attained by each metaheuristic-optimized WANN in the
best, worst, mean, and median run are demonstrated in
Table 8. Additionally, it is important to note, that since
networks evolved in the ﬁrst layer of the framework
attained quite modest results, the application of meta-
heuristics to shared weight ﬁne-tuning demonstrated a
signiﬁcant improvement in performance compared to the
initial results.
The detailed metrics are shown in Table 9 for each of
the best runs. The results signify that several metaheuristics
share the best position for R2 while the novel-introduced
metaheuristics attained the best MSE and RMSE scores.
Nevertheless, the FA once again demonstrated the best
results for MAE further solidifying the NFL theorem
(Table 10).
Convergence rates of each function and ﬁnal distribu-
tions are shown in Fig. 17 followed by KDE diagrams in
Fig. 18.
Finally, the forecasts of the best-performing model
optimized by metaheuristics compared to actual values are
shown in Fig. 19.
The selected hyperparameters in L1 for the best-per-
forming WANN architecture are given in Table 11.
Considering both steps in the optimization process, the
role of metaheuristics optimization cannot be understated.
While in the ﬁrst step, WANN attained more modest out-
comes likely due to the increased data complexity of the
crop yield dataset coupled with the relative simplicity of
the evolved networks, the major improvements made by
Fig. 19 Forcasts made by the best-performing model compared to actual values for crop yield dataset
Table 11 Best selected WANN hyperparameters for the crop yield
dataset
Parameter
Values
Connection addition probability
0.421
Connection removal probability
0.0363
Node addition probability
0.3043
Bias mutation power within
0.415
Weight mutation power
0.3929
Weight mutation rate
0.6353
Weight replacement rate
0.0850
Survival threshold
0.2475
14750
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 25
shared weight tuning in L2 can to a degree mitigate the
shortcomings of L1.
5.3 Comparative analysis with other well-known
ML and ANN models
The proposed approach has also been put to a comparison
with several well-known and well-performing ML and
ANN models. The compared methods include: eXtreme
Gradient Boosting (XGBoost) [7], support vector machines
(SVM) [57] with various kernel functions, and several
traditional ANN network architectures. Network architec-
tures with one, two, and three hidden layers were applied to
the task.
For the SVM, popular kernel functions have been con-
sidered. The results attained using the radial basis function
(RBF) are marked as SVM (RBF). Outcomes attained
when using a polynomial kernel function are marked as
SVM (poly). And ﬁnally, those attained using a linear
kernel function are marked as SMV (linear).
Network architecture marked ANN1, ANN2, and ANN3
have different structures for each dataset. For the blueberry
dataset, ANN1 has one hidden layer with 16 neurons total,
ANN2 has two hidden layers with 32 neurons and 16, and
ANN3 consists of three hidden layers with 32, 16, and 8
neurons, respectively. For the crop yield dataset, ANN1 has
one hidden layer with 230 neurons total, ANN2 has two
hidden layers with 230 neurons and 115, and ANN3 con-
sists of three hidden layers with 230, 115, and 58 neurons,
respectively. All networks utilized the Adam optimizer and
the relu activation function.
Due to the stochastic nature of the training process,
experiments have been carried out over 20 executions.
Mean average results attained over 20 runs of each method
applied to the blueberry dataset are shown in Table 12,
while results applied to crop yield are shown in Table 13.
As crop forecasting is a regression problem, the SVM is
applied as a support vector regressor (SVR). It is also
important to note that during experimentation, one-hot
encoding is not used for XGBoost and SVM giving these
methods a slight advantage due to a lower number of input
features.
From the presented results, several interesting deduc-
tions can be drawn. Firstly, the methods that do not use
one-hot encoding, and thus work with fewer features, have
an advantage. While state-of-the-art techniques such as
Table 12 Comparison of
contemporary ML and ANN
with the proposed
metaheuristic-optimized
WANN on the blueberry dataset
Method
R2
R
MAE
MSE
RMSE
XGBoost
0.958875
0.979222
0.017698
0.000570
0.133033
Decision tree
0.975964
0.987909
0.022048
0.000801
0.028302
SVR (rbf)
0.881070
0.938653
0.050651
0.003963
0.062955
SVR (poly)
0.920317
0.959332
0.042021
0.002655
0.051531
SVR (linear)
0.927540
0.963089
0.041622
0.002415
0.049140
ANN1
0.837727
0.915274
0.062137
0.005408
0.073537
ANN2
0.848218
0.920987
0.059874
0.005068
0.071120
ANN3
0.908051
0.952917
0.044957
0.003064
0.055355
L2-WANN-MSRSA
0.886555
0.941571
0.047194
0.003781
0.061486
Bold values indicate the best attained results
Table 13 Comparison of
contemporary ML and ANN
with the proposed
metaheuristic-optimized
WANN on the crop yield
dataset
Method
R 2
R
MAE
MSE
RMSE
XGBoost
0.662238
0.813780
0.056891
0.009047
0.095116
Decision tree
0.548474
0.740590
0.057000
0.012094
0.109974
SVR (rbf)
0.047267
0.217409
0.117025
0.025519
0.159748
SVR (poly)
0.020311
0.142516
0.119558
0.026241
0.16199
SVR (linear)
- 137266.535531
0
34.375134
3676.780997
60.636466
ANN1
0.435144
0.659654
0.081690
0.015130
0.123004
ANN2
0.322357
0.567765
0.092270
0.018151
0.134726
ANN3
0.286340
0.535107
0.101853
0.019117
0.138260
L2-WANN-MSRSA
0.482586
0.694684
0.076147
0.013859
0.117725
Bold values indicate the best attained results
Neural Computing and Applications (2024) 36:14727–14756
14751
123

---

## Page 26
XGBoost perform the best, helped by the fact that the
number of features in the utilized dataset is reduced ANN
displays admirable performance as well.
It is also important to note that the goal of this com-
parison was not to prove that there are no better methods
than the use of WANN. Even optimized through the use of
metaheuristics, their
networks have
their
limitations.
However, their advantage is in the lightly constructed
architectures that require less computation to conclude.
One especially interesting fact is that compared to sev-
eral ANN architectures, the proposed WANN despite
having a signiﬁcantly simpler structure with only 14 and 15
neurons each, attained better performance than most more
complex ANN architectures. A signiﬁcant advantage when
working with systems that have limited computational
power.
5.4 Findings validation and best model
interpretation
An important part of modern computer science research is
determining whether the improvements made show statis-
tical signiﬁcance. Outcomes alone are insufﬁcient to
determine an advantage of one algorithm over others. In
this work, nine established methods were evaluated
alongside the proposed MSRSA based on their ability to
optimize the models’ performance for WANN for crop
yield forecasting. The comparison was conducted over two
datasets and two problems, the L1 and L2 parts of the
framework, that address the WANN structure and shared
weights tuning, respectively, yielding in total of four dif-
ferent experiments.
[9] suggested using statistical evaluations in these
scenarios is preceded by the adequate sampling of each
method by determining objective averages through multi-
ple
independent
executions
for
each
problem.
This
approach can be inconclusive in cases where the samples
do not follow a normal distribution or even produce mis-
leading conclusions. It is also important to note that
researchers remain divided on whether taking the average
objective function value for statistical tests is appropriate
when
comparing
stochastic
methods [14,
52].
Nevertheless, the objective functions over 20 independent
runs for each of the four problems are considered in this
research.
To determine the statistical signiﬁcance of the obtained
results, the best values from each of the 20 runs of every
algorithm were selected for both wild blueberry and crop
yield prediction datasets instances. These values were then
observed as data series. However, before applying the
appropriate statistical test from the family of parametric or
non-parametric, the safe usage of parametric tests, which
involves investigating the independence, normality, and
homoscedasticity of the data variances [33], needs to be
investigated.
The independence condition is satisﬁed because each
run is executed separately from its pseudo-random number
seed. However, the normality requirement is not satisﬁed
since the acquired samples do not originate from a normal
distribution. This can be observed from the KDE plots and
further reinforced by the Shapiro–Wilk test for single-
problem analysts [55]. By conducting the Shapiro–Wilk
test, p-values are computed for every method–problem
pair, and these results are shown in Table 14.
Both standard threshold values a ¼ 0:05 and a ¼ 0:1
indicated that the null hypothesis (H0) can be rejected,
therefore deducing that none of the samples (for neither of
the problem–method pair) come from a normal distribu-
tion. Therefore, since the normality condition for safe
usage of parametric tests was not satisﬁed, there was no
need to verify the homoscedasticity constraint, and it was
decided to continue the statistical analysis by employing
the non-parametric tests.
Due to the limited number of problems addressed in the
study (four in total), a multi-problem analysis is not con-
ducted because an insufﬁcient number of samples can
produce misleading results. It was, therefore, proceeded
with the pair-wise non-parametric test, where the intro-
duced MSRSA was distinguished as the control method.
The non-parametric Wilcoxon signed-rank test [58]
between the introduced MSRSA and every other method
for each of the problems being addressed for each frame-
work layer was conducted. The results of this analysis are
summarized in Table 15. Generated p-values higher than
the threshold of a ¼ 0:05 are marked as bold.
Table 14 Shapiro–Wilk test
scores for the single-problem
analysis
Problem
MSRSA
RSA
GA
PSO
ABC
FA
BA
HHO
WOA
ChOA
Blueberry yield L1
0.020
0.015
0.018
0.023
0.011
0.012
0.019
0.008
0.013
0.012
Crop yield L1
0.018
0.016
0.013
0.021
0.007
0.011
0.015
0.011
0.014
0.017
Blueberry yield L2
0.003
0.009
0.006
0.011
0.005
0.012
0.009
0.008
0.006
0.003
Crop yield L2
0.002
0.007
0.007
0.009
0.003
0.010
0.006
0.004
0.005
0.006
14752
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 27
Generated Wilcoxon signed-rank test p-values showed
in Table 15 exhibit that, in the scenario of L1 experiments
(WANN structure tuning), proposed MSRSA signiﬁcantly
outperformed all other methods yielding all p-values which
are substantially lower than 0.5. Therefore, in this extre-
mely computationally extensive experiment, the MSRSA
proved a robust and efﬁcient optimizer.
Although in L2 simulations (WANN shared weights
tuning), according to the Wilcoxon signed-rank analysis,
the MSRSA outperformed most of the other methods in
terms of signiﬁcant improvements, there are some instan-
ces where other approaches showed competitive perfor-
mance. More precisely, in the case of L2 blueberry yield
prediction, the MSRSA did not show noteworthy results
compared to the ABC approach when the threshold of 0.05
is taken into account. Similarly, in the L2 crop yield pre-
diction simulations, according to the generated p-values,
the RSA and HHO showed similar performance as the
MSRSA at both threshold values, 0.1 and 0.05.
Nonetheless, as an overall statistical analysis conclu-
sion, the MSRSA exhibited performance in both experi-
ments which are statistically signiﬁcantly better than most
of all other metaheuristics that were taken for analysis.
Finally, the best model generated model by the proposed
MSRSA in L2 experiment for the wild blueberry dataset is
taken, and the SAGE [13] method is applied to observe the
feature importance. Analysis through SAGE allows for the
isolation of single parameters across complexity dimen-
sions. It can be used to evaluate both narrow AI systems
and general systems. By evaluating the response of a model
to variable changes a conclusion can be drawn on its ability
to extract relations and attain autonomy as well as how well
the model can exploit these to achieve goals. The SAGE
method is applied to determine the importance within each
feature for the best-constructed model providing poten-
tially very useful information for further studies, as it
indicates parameters that researchers may want to focus on
in order to attain accurate forecasts using the proposed
model as well as ligher models if needed.
Since the SAGE library sagemaker does not natively
support WANNs, the code for generating SAGE values was
written from scratch in Python. However, since the crop
yield dataset in the pre-processing phase involves one-hot
encoding for categorical variables, there was no logic to
run the SAGE for the best-generated model for this dataset.
The feature importance bar plot for the wild blueberry
best model is depicted in Fig. 20.
According to the SAGE analysis outcomes, the front set
features have the highest impact on model predictions. The
next highest impacting feature is the seeds feature followed
by fruit mass.
6 Conclusion
The presented work put forth a proposal for a novel two-
layer
framework
for
constructing
optimized
network
architectures based on neuroevolutionary algorithms. By
using WANN, much of the training required by traditional
neural networks can be avoided. Additionally, the respon-
sibility of the network is shifted from ﬁne-tuned weights
and biases toward the network architecture. One result of
taking this approach is the generation of simpler and tighter
neural networks. However, the performance of these net-
works is heavily dependent on adequate parameter selec-
tion. This work introduces a novel MSRSA algorithm that
partakes in both aspects of network optimization and
demonstrates the best performance in both.
Table 15 Wilcoxon signed-rank
test ﬁndings
MSRSA versus others
RSA
GA
PSO
ABC
FA
BA
HHO
WOA
ChOA
Blueberry yield L1
0.008
0.009
0.015
0.019
0.011
0.010
0.016
0.023
0.031
Crop yield L1
0.009
0.011
0.020
0.017
0.040
0.013
0.023
0.037
0.046
Blueberry yield L2
0.025
0.024
0.042
0.056
0.019
0.021
0.033
0.040
0.025
Crop yield L2
0.19
0.032
0.036
0.038
0.059
0.029
0.20
0.042
0.063
Bold values indicate the best attained results
Fig. 20 The SAGE feature importance bar plot for wild blueberry
simulations
Neural Computing and Applications (2024) 36:14727–14756
14753
123

---

## Page 28
The proposed framework possesses a two-layer struc-
ture. Optimal network architectures are evolved in the ﬁrst
layer, while the share weights are further optimized in layer
2 to improve performance. The approach has been tested
on two real-world blueberry and crop yield datasets with
mixed results. Depending on data complexity, L1 attained
decent results when working with the simple blueberry
dataset, while attaining noticeably more modest results on
the more complex crop yield dataset. However, it is
important to note that following L2 optimization, the net-
works have seen a signiﬁcant improvement following
shared weight optimization by metaheuristic algorithms.
The best-performing model for the blueberry dataset has
been subjected to SAGE analysis to determine the features
that have the highest impact on model forecasts. Addi-
tionally, the performance of WANNs has been compared to
several proven AI and ML methods to determine their
relative effectiveness. While the proposed approach did not
match the performance of state-of-the-art methods, the
method nonetheless proves promising outperforming sig-
niﬁcantly
more
computationally
demanding
network
architectures.
One notable advantage of this approach is the relative
simplicity of the ﬁnal models, featuring few nodes and
connections in comparison with traditional networks han-
dling similar tasks. This feature can be a signiﬁcant
advantage when creating models for systems with limited
computational power. This process is somewhat balanced
by the demanding process of generating optimized models.
Nevertheless, by introducing metaheuristic optimization,
generation times can be signiﬁcantly reduced and model
performance improved.
As with any study, certain limitations are present within
this work. The high cost of the comparative analysis
between optimization algorithms limits population sizes
and allocated iterations, parameters that might improve the
performance of slower converging algorithms or improve
the exploratory power of fast converging ones. Further-
more, only a limited number of optimization algorithms
have been considered in the optimization. Future works
hope to address some of the state’s limitations and will
focus on exploring the potential of WANN for tackling
pressing real-world problems. Additionally, the potential of
the introduced MSRSA algorithm will be explored in other
optimization areas.
Funding Open access funding provided by the Scientiﬁc and Tech-
nological Research Council of Tu¨rkiye (TU¨ BI˙TAK). Luka Jovanovic,
Miodrag
Zivkovic,
Nebojsa
Bacanin,
and
Milos
Dobrojevic
acknowledge funding provided by the Institute of Physics Belgrade,
through the grant by the Ministry of Education, Science and Tech-
nological Development of the Republic of Serbia, as well as by the
Science Fund of the Republic of Serbia, Grant No. #7373,
Characterizing crises-caused air pollution alternations using an arti-
ﬁcial intelligence-based framework - crAIRsis and Grant No. #7502,
Intelligent Multi-Agent Control and Optimization Applied to Green
Buildings
and
Environmental
Monitoring
Drone
Swarms
-
ECOSwarm.
Data availability Data will be made available on request.
Declarations
Conflict of interest The authors declare that they have no conflict of
interest.
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
1. Abualigah L, Abd Elaziz M, Sumari P, Geem ZW, Gandomi AH
(2022) Reptile search algorithm (rsa): a nature-inspired meta-
heuristic optimizer. Expert Syst Appl 191:116158
2. Asare E, Hoshide AK, Drummond FA, Criner GK, Chen X
(2017) Economic risk of bee pollination in maine wild blueberry,
vaccinium angustifolium. J Econ Entomol 110:1980–1992.
https://doi.org/10.1093/jee/tox191
3. Bacanin N, Simic V, Zivkovic M, Alrasheedi M, Petrovic A
(2023) Cloud computing load prediction by decomposition rein-
forced attention long short-term memory network optimized by
modiﬁed particle swarm optimization algorithm. Ann Oper Res.
https://doi.org/10.1007/s10479-023-05745-0
4. Bacanin N, Zivkovic M, Jovanovic L, Ivanovic M, Rashid TA
(2022) Training a multilayer perception for modeling stock price
index predictions using modiﬁed whale optimization algorithm.
In: Computational vision and bio-inspired computing: proceed-
ings of ICCVBIC 2021, Springer, pp 415–430
5. Brockman G, Cheung V, Pettersson L, Schneider J, Schulman J,
Tang J, Zaremba W (2016) Openai gym. arXiv preprint arXiv:
1606.01540
6. Central Intelligence Agency (2023). The world factbook: land
use. https://www.cia.gov/the-world-factbook/ﬁeld/land-use/
7. Chen T, He T, Benesty M, Khotilovich V, Tang Y, Cho H, Chen
K, Mitchell R, Cano I, Zhou T et al. (2015) XGBoost: extreme
gradient boosting. R package version 0.4-2, vol. 1, pp 1–4
8. Cuk A, Bezdan T, Jovanovic L, Antonijevic M, Stankovic M,
Simic V, Zivkovic M, Bacanin N (2024) Tuning attention based
long-short term memory neural networks for Parkinson’s disease
detection using modiﬁed metaheuristics. Sci Rep 14:4309
9. Derrac J, Garcı´a S, Molina D, Herrera F (2011) A practical
tutorial on the use of nonparametric statistical tests as a
methodology for comparing evolutionary and swarm intelligence
algorithms. Swarm Evol Comput 1:3–18
14754
Neural Computing and Applications (2024) 36:14727–14756
123

---

## Page 29
10. Devarajan GG, Nagarajan SM, Ramana T, Vignesh T, Ghosh U,
Alnumay W (2023) Ddnsas: deep reinforcement learning based
deep q-learning network for smart agriculture system. Sustain
Comput: Inform Syst 39:100890
11. Dobrojevic M, Bacanin N (2022) IoT as a backbone of intelligent
homestead
automation.
Electronics.
https://doi.org/10.3390/
electronics11071004
12. Drummond FA (2016) Behavior of bees associated with the wild
blueberry agro-ecosystem in the USA. Int J Entomol Nematol
2:21–26
13. Eberding LM, Sheikhlar A, Tho´risson KR (2020) Sage: task-
environment platform for autonomy and generality evaluation. In:
International
conference
on
artiﬁcial
general
intelligence.
Springer, submitted in
14. Eftimov T, Korosˇec P, Seljak BK (2017) A novel approach to
statistical comparison of meta-heuristic stochastic optimization
algorithms using deep statistics. Inf Sci 417:186–215
15. Farfa´n JF, Cea L (2021) Coupling artiﬁcial neural networks with
the artiﬁcial bee colony algorithm for global calibration of
hydrological models. Neural Comput Appl 33:8479–8494
16. Finn C, Abbeel P, Levine S (2017) Model-agnostic meta-learning
for fast adaptation of deep networks. In: International conference
on machine learning, PMLR, pp 1126–1135
17. Food and Agriculture Organization (FAO) (2021). Chapter 2:
agriculture, food security, nutrition and the sdgs. https://www.fao.
org/3/w2612e/w2612e06a.htm
18. Food and Agriculture Organization (FAO) (2022). Ug99: the
stem rust that changed the game. https://www.fao.org/agriculture/
crops/rust/stem/rust-report/stem-ug99racettksk/en
19. Gaier A, Ha D (2019) Weight agnostic neural networks. In:
Wallach H, Larochelle H, Beygelzimer A, d’ Alche´-Buc F, Fox
E, Garnett R (eds) Advances in neural information processing
systems. vol. 32, Curran Associates, Inc. https://proceedings.
neurips.cc/paper/2019/ﬁle/e98741479a7b998f88b8f8c9f0b6b6f1-
Paper.pdf
20. Gibney E (2018) China is poised to become world leader in AI
research.
Nature
553:5.
https://doi.org/10.1038/d41586-018-
02742-3
21. Glass GV (1966) Testing homogeneity of variances. Am Educ
Res J 3:187–190
22. Global Agriculture (2019) Industrial agriculture and small-scale
farming.
https://www.globalagriculture.org/report-topics/indus
trial-agriculture-and-small-scale-farming.html
23. Heidari AA, Mirjalili S, Faris H, Aljarah I, Mafarja M, Chen H
(2019) Harris hawks optimization: algorithm and applications.
Futur Gener Comput Syst 97:849–872
24. Herren RV (2019) Science of animal agriculture. Cengage
25. Horie T, Yajima M, Nakagawa H (1992) Yield forecasting. Agric
Syst 40:211–236. https://doi.org/10.1016/0308-521x(92)90022-g
26. Jovanovic L, Jovanovic D, Antonijevic M, Nikolic B, Bacanin N,
Zivkovic M, Strumberger I (2023) Improving phishing website
detection using a hybrid two-level framework for feature selec-
tion and XGBoost tuning. J Web Eng 22:543–574
27. Jovanovic L, Jovanovic D, Bacanin N, Jovancai Stakic A,
Antonijevic M, Magd H, Thirumalaisamy R, Zivkovic M (2022)
Multi-step crude oil price prediction based on lstm approach
tuned by salp swarm algorithm with disputation operator. Sus-
tainability 14:14616
28. Jovanovic L, Milutinovic N, Gajevic M, Krstovic J, Rashid TA,
Petrovic A (2022b) Sine cosine algorithm for simple recurrent
neural network tuning for stock market prediction. In: 2022 30th
telecommunications forum (TELFOR), IEEE, pp 1–4
29. Karaboga D, Basturk B (2008) On the performance of artiﬁcial
bee colony (ABC) algorithm. Appl Soft Comput 8:687–697
30. Kaya S (2023) A hybrid ﬁreﬂy and particle swarm optimization
algorithm with local search for the problem of municipal solid
waste collection: a real-life example. Neural Computi Appl
35:7107–7124
31. Khishe M, Mosavi MR (2020) Chimp optimization algorithm.
Expert Syst Appl 149:113338
32. Kuznetsova A, Maleva T, Soloviev V (2020) Using yolov3
algorithm with pre- and post-processing for apple detection in
fruit-harvesting robot. Agronomy 10:1016
33. LaTorre A, Molina D, Osaba E, Poyatos J, Del Ser J, Herrera F
(2021) A prescription of methodological guidelines for compar-
ing bio-inspired optimization algorithms. Swarm Evol Comput
67:100973
34. LeCun Y, Cortes C, Christopher B (2020) Mnist database. MNIST
handwritten digit database, Yann LeCun, Corinna Cortes and
Chris Burges. http://yann.lecun.com/exdb/mnist/
35. Li J, Galazis C, Popov L, Ovchinnikov L, Kharybina T, Vesnin S,
Losev A, Goryanin I (2022) Dynamic weight agnostic neural
networks and medical microwave radiometry (MWR) for breast
cancer diagnostics. Diagnostics 12:2037
36. Macrotrends (2023) Hunger statistics: world hunger and poverty
facts and statistics. https://www.macrotrends.net/countries/rank
ing/hunger-statistics
37. Mirjalili S, Lewis A (2016) The whale optimization algorithm.
Adv Eng Softw 95:51–67
38. Mirjalili S, Mirjalili S (2019) Genetic algorithm. Evolut Algoritm
Neural Netw: Theory Appl:43–55
39. Muruganantham P, Wibowo S, Grandhi S, Samrat NH, Islam N
(2022) A systematic literature review on crop yield prediction
with deep learning and remote sensing. Rem Sens 14:1990.
https://doi.org/10.3390/rs14091990
40. Niles MT, Wirkkala KB, Belarmino EH, Bertmann F (2021)
Home food procurement impacts food security and diet quality
during covid-19. BMC Public Health 21. https://doi.org/10.1186/
s12889-021-10960-0
41. Obsie EY, Qu H, Drummond F (2020) Wild blueberry yield
prediction using a combination of computer simulation and
machine
learning
algorithms.
Comput.
Electron.
Agric.
178:105778. https://doi.org/10.1016/j.compag.2020.105778
42. Ofﬁce IL (2010) Safety and health in agriculture. International
Labour Ofﬁce
43. Parisi GI, Kemker R, Part JL, Kanan C, Wermter S (2019)
Continual lifelong learning with neural networks: a review.
Neural Netw 113:54–71
44. Patel R (2021) Crop yield prediction dataset. https://www.kaggle.
com/datasets/patelris/crop-yield-prediction-dataset
45. Pavlov-Kagadejev M, Jovanovic L, Bacanin N, Deveci M, Ziv-
kovic M, Tuba M, Strumberger I, Pedrycz W (2024) Optimizing
long-short-term memory models via metaheuristics for decom-
position aided wind energy generation forecasting. Artif Intell
Rev 57:45
46. Prasad NR, Patel NR, Danodia A, Manjunath KR (2021) Com-
parative performance of semi-empirical based remote sensing and
crop simulation model for cotton yield prediction. Model Earth
Syst Environ 8:1733–1747. https://doi.org/10.1007/s40808-021-
01180-x
47. Predic´ B, Jovanovic L, Simic V, Bacanin N, Zivkovic M,
Spalevic P, Budimirovic N, Dobrojevic M (2023) Cloud-load
forecasting via decomposition-aided attention recurrent neural
network tuned by modiﬁed particle swarm optimization. Com-
plex Intell Syst 10(2):2249–2269
48. Roser M (2019) Two centuries of rapid global population growth
will come to an end. https://ourworldindata.org/world-popula
tion-growth-past-future
49. Roser M, Ritchie H (2021a) Agricultural production. https://our
worldindata.org/agricultural-production
Neural Computing and Applications (2024) 36:14727–14756
14755
123

---

## Page 30
50. Roser M, Ritchie H (2021b) Index of cereal production yield and
land use. https://ourworldindata.org/grapher/index-of-cereal-pro
duction-yield-and-land-use
51. Roy AM, Bhaduri J (2021) A deep learning enabled multi-class
plant disease detection model based on computer vision. AI
2:413–428. https://doi.org/10.3390/ai2030026
52. Samadianfard S, Kargar K, Shadkani S, Hashemi S, Abbaspour
A, Safari MJS (2022) Hybrid models for suspended sediment
prediction: optimized random forest and multi-layer perceptron
through genetic algorithm and stochastic gradient descent meth-
ods. Neural Comput Appl 34:3033–3051
53. Sands DC, Morris CE, Dratz EA, Pilgeram AL (2009) Elevating
optimal human nutrition to a central goal of plant breeding and
production of plant-based foods. Plant Sci 177:377–389. https://
doi.org/10.1016/j.plantsci.2009.07.011
54. Shahane S (2021) Wild blueberry yield prediction. https://www.
kaggle.com/saurabhshahane/wild-blueberry-yield-prediction
55. Shapiro SS, Francia R (1972) An approximate analysis of vari-
ance test for normality. J Am Stat Assoc 67:215–216
56. Stoean C, Zivkovic M, Bozovic A, Bacanin N, Strulak-Wo´jci-
kiewicz R, Antonijevic M, Stoean R (2023) Metaheuristic-based
hyperparameter tuning for recurrent deep learning: application to
the prediction of solar energy generation. Axioms 12:266
57. Suthaharan S, Suthaharan S (2016) Support vector machine. In:
Machine learning models and algorithms for big data classiﬁca-
tion: thinking with examples for effective learning, pp 207-235
58. Taheri S, Hesamian G (2013) A generalization of the Wilcoxon
signed-rank test and its applications. Stat Pap 54:457
59. Todorovic M, Stanisic N, Zivkovic M, Bacanin N, Simic V,
Tirkolaee EB (2023) Improving audit opinion prediction accuracy
using
metaheuristics-tuned
XGBoost
algorithm
with
inter-
pretable results through shap value analysis. Appl Soft Comput
149:110955
60. United
Nations
Conference
on
Trade
and
Development
(UNCTAD) (2023) UNCTADstat - UNCTAD’s statistical data-
base.
http://unctadstat.unctad.org/wds/TableViewer/tableView.
aspx?ReportId=95
61. Vishwakarma DK, Kumar R, Kumar A, Kushwaha NL, Kush-
waha KS, Elbeltagi A (2022) Evaluation and development of
empirical models for wetted soil fronts under drip irrigation in
high-density apple crop from a point source. Irrig Sci. https://doi.
org/10.1007/s00271-022-00826-7
62. Wang D, Tan D, Liu L (2018) Particle swarm optimization
algorithm: an overview. Soft Comput 22:387–408
63. Wolpert DH, Macready WG (1997) No free lunch theorems for
optimization. IEEE Trans Evol Comput 1:67–82
64. World Bank (2022) Cereal yield (kg per hectare). https://data.
worldbank.org/indicator/AG.YLD.CREL.KG
65. Worldometer (2022) Largest countries in the world by area 2022.
https://www.worldometers.info/geography/largest-countries-in-
the-world/
66. Worldometers
(2023)
World
population.
https://www.world
ometers.info/world-population/#pastfuture
67. Yang X-S, He X (2013) Fireﬂy algorithm: recent advances and
applications. Int J Swarm Intell 1:36–50
68. Yang X-S, Hossein Gandomi A (2012) Bat algorithm: a novel
approach for global engineering optimization. Eng Comput
29:464–483
69. Zivkovic M, Jovanovic L, Ivanovic M, Bacanin N, Strumberger I,
Joseph PM (2022a) XGBoost hyperparameters tuning by ﬁtness-
dependent optimizer for network intrusion detection. In: Com-
munication and intelligent systems: proceedings of ICCIS 2021,
Springer, pp 947–962
70. Zivkovic M, Jovanovic L, Ivanovic M, Krdzic A, Bacanin N,
Strumberger I (2022b) Feature selection using modiﬁed sine
cosine algorithm with covid-19 dataset. In: Evolutionary com-
puting
and
mobile
sustainable
networks:
proceedings
of
ICECMSN 2021, Springer, pp 15–31
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
14756
Neural Computing and Applications (2024) 36:14727–14756
123

---
