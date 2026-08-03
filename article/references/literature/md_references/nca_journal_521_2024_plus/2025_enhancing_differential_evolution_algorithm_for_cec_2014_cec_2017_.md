# Enhancing differential evolution algorithm for CEC 2014, CEC 2017, CEC 2021, and CEC 2022 test suites

**Year**: 2025 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-025-11678-5

---

## Page 1
S.I.: 2022 INDIA INTERNATIONAL CONGRESS ON COMPUTATIONAL INTELLIGENCE
Enhancing differential evolution algorithm for CEC 2014,
CEC 2017, CEC 2021, and CEC 2022 test suites
Rohit Salgotra1
• Pankaj Sharma5 • Krishanu Kundu3 • Saravanakumar Raju2 •
Amir H. Gandomi4
Received: 26 September 2023 / Accepted: 23 July 2025 / Published online: 8 October 2025
 The Author(s) 2025
Abstract
Differential evolution (DE) has demonstrated its signiﬁcant contribution to the optimization of different real-
world applications as well as standard benchmarks. This paper presents a novel variant of the DE algorithm,
known as the LSHADESPA algorithm. The LSHADESPA algorithm incorporates three signiﬁcant modiﬁcations
to enhance its performance. Firstly, a proportional shrinking population mechanism is employed to reduce the
computational burden. Secondly, a simulated annealing (SA)-based scaling factor is introduced to improve the
exploration properties of the algorithm. Finally, an oscillating inertia weight-based crossover rate is utilized to
strike a balance between exploitation and exploration. These modiﬁcations aim to enhance the overall efﬁciency
and effectiveness of the DE algorithm. The proposed LSHADESPA algorithm has been empirically evaluated on
a set of benchmark problems, namely the CEC 2014, CEC 2017, CEC 2021, as well as CEC 2022. The
experimental outcomes show that the LSHADESPA algorithm performs superior to other MH algorithms.
Additionally, the Wilcoxon rank-sum as well as the Friedman rank test proves the statistical signiﬁcance of the
proposed LSHADESPA in comparison to other algorithms under comparison. The outcomes indicate that the
LSHADESPA algorithm has statistical signiﬁcance, with Friedman statistics for the CEC 2014, CEC 2017, and
CEC 2022 benchmark functions achieving the lowest f-rank value compared to the other MH algorithms which
are found to be 41, 77, and 26, respectively, and obtained 1st rank. Note that this paper is an invited extended
version of the paper published in ISCMI 2022 conference.
Keywords Evolutionary algorithm (EA)  Differential evolution (DE)  LSHADE  CEC benchmark problems 
Optimization
Abbreviations
DE
Differential evolution
IW
Inertia weight
SP
Shrinking population
MH
Meta-heuristic
SA
Simulated annealing
CR
Crossover rat
LP
Linear programming
QP
Quadratic programming
NLP
Nonlinear programming
IP
Integer programming
EA
Evolutionary algorithm
Neural Computing and Applications (2025) 37:27593–27630
https://doi.org/10.1007/s00521-025-11678-5
123
Neural Computing and Applications (2025) 37:27593–27630

---

## Page 2
GA
Genetic algorithms
OF
Objective function
GP
Genetic programming
EDA
Estimation of distribution algorithm
D
Dimension
IMEHO
Improved elephant herding optimization
NP
Population size
MVMO
Mean-variance mapping optimization
tmax
Maximum iterations
RW-GWO
Random walk gray wolf optimizer
NFL
No free lunch theorem
PBIL
Population-based incremental learning
SaDE
Self-adaptive DE
B-BBO
Blended biogeography-based optimization
std
Standard deviation
ISOS
Improved symbiotic organisms search
PSO
Particle swarm optimization
KOA
Kepler optimization algorithm
LSO
Light spectrum optimizer
VNBA
Variable neighborhood bat algorithm
ES
Evolution strategies
CEC
Congress on evolutionary computation
CCS
Chaotic cuckoo search
1 Introduction
Optimization [1] is a mathematical discipline focused on ﬁnding the best solution to a problem out of all feasible
solutions. It involves maximizing desired factors and minimizing undesired ones to reach the optimal design,
decision, or operation. Optimization has applications across engineering, economics, operations research, control
theory, and other quantitative ﬁelds. The key components of an optimization [2] problem are: Objective function
(OF) is the quantity to be maximized or minimized, and it represents the goal or performance metric, decision
variables are those variables that can be set or changed to affect the OF value, and ﬁnally, constraints denote
limits or conditions the variables must satisfy. The optimization statement combines these elements: Minimize/
Maximize f(x) Subject to constraints by choosing x. There are various classiﬁcations of optimization problems
that have speciﬁc algorithms developed to solve them efﬁciently: (a) Linear programming (LP) (OF and con-
straints are linear functions) [3], (b) Quadratic programming (QP) (OF is a quadratic function [4], constraints are
linear), (c) nonlinear programming (NLP) (OF or constraints are nonlinear functions [5]), (d) integer program-
ming (IP) (decision variables must take integer values) [6], and (e) stochastic programming (involves uncertainty
modeled using random variables) [7]. Some common mathematical techniques used to solve optimization
problems include: (a) calculus methods, (b) Direct search, (c) Convex optimization, (d) Dynamic programming,
and (e) Heuristics [8].
Optimization algorithms can be broadly categorized into two main classes: derivative-based as well as
derivative-free methods. Derivative-based methods like gradient descent are faster but require the OF to be
differentiable. Derivative-free methods like evolutionary algorithms are more ﬂexible. Key trends involve gra-
dient-free, stochastic, adaptive, hybrid, meta-learning, and quantum techniques [9–11]. These expand capabilities
123
Neural Computing and Applications (2025) 37:27593–27630
27594
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 3
and improve efﬁciency and robustness across diverse challenges. To identify optimal or near-optimal solutions to
complicated problems, a meta-heuristic (MH) search algorithm replicates the stages of natural evolution. There
are two types of MH search algorithms: local as well as global search. Local search techniques begin with an
initial solution and enhance it repeatedly by investigating its neighborhood, i.e., a subset of the search space
which is near to the present solution. And global search algorithms retain a population of solutions and employ
genetic operators such as crossover as well as mutation to generate new solutions from current ones. The right
balance of exploration as well as exploitation searches is the foundation for all MH algorithms to properly tackle
various sorts of optimization challenges. Existing MH algorithm may be categorized into four primary types: (a)
evolutionary algorithm (EAs), (b) swarm intelligence computational methods, (c) human-oriented algorithms as
well as (d) physics-oriented algorithms [12, 13]. Evolution of EAs is driven by Darwin’s theory called ‘‘survival
of the ﬁttest.’’ These EAs use crossover, mutation, and selection to produce new offspring solutions of higher
quality. Evolutionary algorithms [14] are a family of population-based optimization algorithms inspired by
biological evolution. The key characteristics EAs are population of candidate solutions, selection based on ﬁtness,
variation through recombination as well as mutation, and iterative improvement across generations. The major
classes of EAs are: Genetic algorithms (GA) [15], Evolution strategies (ES) [16], Genetic programming (GP)
[17], Differential evolution (DE), Estimation of distribution algorithms (EDA) [18]. The present paper proposes a
self-adaptive DE algorithm. DE is a population-based search algorithm that enhances candidate solutions based
on evolutionary principles like mutation, crossover, as well as selection. The various review study related to the
DE algorithm is discussed as follows. Neri et al. [19] were among the ﬁrst to review the research progress on DE,
focusing on a study of several enhanced DE structures with extra components released up to 2009, in addition to
their ability in solving selected conventional as well as rotating problems of diverse dimensional sizes. Das et al.
[20, 21] released two review articles to carefully examine the advances in DE research up to 2011–2016,
correspondingly. The key themes discussed in these review articles are adjustments made to current DE variations
to tackle various sorts of optimization environments. Also, the review paper released by Jebaraj et al. [22] focuses
on the potential uses of DE to tackle static as well as dynamic economic or emission dispatch challenges reported
up to 2016. The issue articulation in perspective of the OF, in addition to the equality as well as inequality
restrictions associated to various economic alongside emission dispatch concerns, was ﬁrst presented, followed by
a description of current DE variants aimed to address these problems. The review study by Opara et al. [23]
concentrated on assessments of DE , compared to most current research that examined alterations performed on
DE variations along with technical aspects. This study fully covered substantial quantities like convergence
characteristics, computational complexity, population diversity, as well as population dynamics frameworks
related to DE published till 2019. In the same year, Javaid [24] released a review study; however, it only included
DE versions along with their uses in energy control challenges till 2016. Review by Bilal et al. [25] highlighted
the most recent advances in DE investigations reported till 2018. Aside from the adjustments made to the initial
DE, this attempt performed a full bibliometric assessment of the DE in order to provide its publishing numbers
based on various journal quartiles as well as publishers.
The main DE variants are as follows. JADE uses self-adaptive control to adjust control parameters F and CR
[26]. SHADE introduces history-based adaptive parameter control and external archive [27]. LSHADE incor-
porates linear population size reduction to improve convergence. LSHADE-EpSin [28] uses ensemble sinusoidal
parameter adaptation. LSHADE-cnEpSin [29] adds covariance matrix learning to LSHADE-EpSin. LSHADE-
SPACMA [30] is hybrid of LSHADE and CMA-ES. ELSHADE-SPACMA is enhanced version of LSHADE-
SPACMA. These variants introduce modiﬁcations like adaptive parameter control, linear population size
reduction, and hybridization to improve DE’s exploration/exploitation balance, convergence speed, and solution
diversity. The primary goal of adaptive DE aims to aid in the exploration and exploitation of relationships that
prevent early convergence difﬁculties and to optimize the ﬁnal ﬁndings. Differential evolution with self-adapting
populations [31] dynamically modiﬁes the crossover and mutation parameters as well as the population count.
Fuzzy adaptive differential evolution [32] is a form of DE method that adjusts the controller settings for crossover
and mutation processes using fuzzy logic controllers. The mutation strategies ‘‘DE/rand/1’’ along with ‘‘DE/
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27595

---

## Page 4
current-to-best/2’’ are both subjected to self-adaptive differential evolution [33]. jDE is a comparable adaptive DE
method to the conventional DE/rand/1/bin approach. Based on the modiﬁed parameters, JDE enhances the
population count during the optimization process, resulting in vectors which are more probable to survive. The
MDE employs a single array, that is updated whenever a superior approach is discovered. As a result, continually
updating the same array improves convergence time, resulting in fewer evaluation processes than with traditional
DE. Modiﬁed DE with P-Best Crossover uses F and Cr values generated by a Cauchy distribution with a position
parameter, which are then modiﬁed on the power average of all F/Cr ratios generating successful offspring [34].
JADE is an option of modifying the parameters during each generation in order to achieve progressive self-
adaptation depending on success rate [26]. Differential Covariance Matrix Adaptation Evolutionary Algorithm for
Real Parameter Optimization was suggested by Saurav et al. The covariance matrix adaptation, like a quasi-
Newton approach, aims to estimate the reverse Hessian matrix. Furthermore, the greedy selection approach of DE
is used to enhance individuals in the following generation to boost the utility of the said approach [35].
Population initialization becomes a critical activity since it inﬂuences the quality of the eventual solution as well
as the algorithm’s convergence time. The choice of this nonrepeatable procedure is critical, since the level of
accuracy of the initial population collected inﬂuences the entire ﬂow of the DE algorithm. Rahnamayan et al. [36]
proposed an initialization approach based on opposition-based learning for producing the initial population of
candidate solutions. Ozer et al. [37] suggested a chaotically initialized DE method that has a quicker convergence
rate and is more resilient to premature convergence. Melo et al. [38] introduced smart sampling DE , which can
discover the potential solution region in search arena by using the potency of machine learning. Zhu et al. [39]
devised an adaptive population tuning system to dynamically regulate the population count of DE depending on
the anticipated population dispersion as well as searching status. Cluster-based population initialization sampling
strategy for DE was introduced by Poikolainen et al. [40] to anticipate the most feasible regions under decision
space.
The current study proposes a self-adaptive DE algorithm based on the inherent features of the LSHADE-
cnEpSin algorithm. Their major modiﬁcations are added to improve an algorithm’s overall performance. The CR
is ﬁrst adapted by employing oscillating iw, then the F is adapted employing SA-based modiﬁcation, and lastly
shrinking adaptation is used to lower the population count throughout the course of the rounds. The current work
employs LSHADE as the core method, as well as SA-based changes, in addition to simple sinusoidal waves, have
been performed to successfully pick a suitable F parameter. Proposed improvements attempt to add adaptive
qualities to the algorithm to ensure no user-oriented alterations are necessary. The proposed approach is called
LSHADE with SP adaptations (LSHADESPA). The work is the extended version of the paper accepted in ISCMI
2022 conference [41].
In this paper, the effectiveness of the LSHADESPA algorithm has been tested by utilizing renowned CEC
2014 [42], CEC 2017 [43], CEC 2021 [44], and CEC 2022 [45] test functions. A comparison is conducted
between popular and recently introduced algorithms, such as i Laplacian BBO (LX-BBO) [46], population-based
incremental learning (PBIL) [47], blended biogeography-based optimization (B-BBO) [46], Kepler optimization
algorithm (KOA) [48], variable neighborhood bat (VNBA) [47], improved symbiotic organisms search (ISOS)
[49], Self-adaptive DE (SaDE) [50], evolutionary algorithms with eigen crossover (EA4eig) [51], adaptive
differential evolution with optional external archive (JADE) [26], success history-based adaptive DE (SHADE)
[52], improved elephant herding optimization (IMEHO) [47], LSHADE [53], mean-variance mapping opti-
mization (MVMO) [54], enhanced versions of CS (CV1.0) [55], improved version of CS (CVnew) [56], random
walk gray wolf optimizer (RW-GWO) [57], DE [58], light spectrum optimizer (LSO) [59], chaotic cuckoo search
(CCS) [47], PSO [58, 60], and nonlinear population size reduction success-history adaptive DE with rank-based
selective pressure midpoint of the population (NL-SHADE-RSP-MID) [61]. The statistical signiﬁcance of the
suggested algorithm has been assessed employing two tests: the Wilcoxon rank-sum test as well as the Friedman
test [62–64]. The main contribution of the paper is:
123
Neural Computing and Applications (2025) 37:27593–27630
27596
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 5
•
A new variant of the DE algorithm utilizing three modiﬁcations (proportional SP; SA-based scaling factor as
well as oscillating iw-based crossover rate) known as the LSHADESPA algorithm is proposed.
•
The LSHADESPA algorithm has been evaluated on the CEC 2014 [42] CEC 2017 [43], CEC 2021 [44], and
CEC 2022 [45, 65] benchmarks test suite and compared with the other algorithms.
•
Two statistical tests, including the Wilcoxon rank-sum as well as Friedman tests, have been performed to
establish the statistical signiﬁcance of the LSHADESPA algorithm.
The entire paper is divided into six sections. The introduction section provides background information and
key ideas, while Sect. 2 covers the fundamentals of DE algorithm. Section 3 begins with the proposal’s general
how’s as well as why’s while going into further depth about each change that has been made to the proposed
LSHADESPA algorithm. This part also explains the justiﬁcation for the proposal and provides theoretical
information on how each modiﬁcation increases the proposal’s importance. Section 4 deals with results along
with detailed discussions. Section 5 presents the summary of results, drawbacks, and insightful implication,
whereas conclusions are being highlighted in the last section. The organization of the article is presented in Fig. 1.
2 Basics of DE
2.1 DE algorithm
Differential evolution is a population-based stochastic optimization algorithm used for optimizing real-valued
nonlinear as well as nondifferentiable OF0s. It works by iteratively improving candidate solutions based on
evolutionary principles of mutation, crossover, as well as selection. The key steps in differential evolution are: (1)
Initialization—Generate an initial population of candidate solutions randomly. (2) Mutation- For each candidate
solution, mutate it by adding the weighted difference of two random distinct candidates to a third one. (3)
Crossover—Crossover the mutated candidate with the original candidate solution to generate a trial candidate. (4)
Selection—Evaluate the trial candidate. If it is better than the original candidate, replace the original with the trial
candidate. Repeat steps 2–4 until convergence or maximum iterations. The main parameters in differential
evolution algorithm are: (a) Population size (NP)—Number of candidate solutions in a population. Typical values
are 5–10 times the number of dimension (D). (b) Mutation factor (F)—Scales the difference vectors during
mutation. Typical range is 0.5 to 1. (c) Crossover probability (CR)—Probability that trial vector inherits
parameter values from the mutant. Typical range is 0.8–1. Mutation generates new vectors by adding the
Fig. 1 Organization of the
article
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27597

---

## Page 6
weighted difference of two randomly selected candidates to a third one. Some common mutation strategies are:
(a) DE/rand/1—Randomly pick three candidates (x1, x2, x3), generate mutant as x3 þ F  ðx1  x2Þ (b) DE/best/
1—Pick best candidate as base x3, generate mutant as x3 þ F  ðx1  x2Þ Mutation expands search space and
enhances diversity in the population. Crossover mixes the mutated candidate with the original candidate to
generate a trial candidate. Binomial crossover mixes parameters at random based on a crossover probability CR.
Exponential crossover starts from the left and copies consecutive mutant parameters until a random number
exceeds CR. Crossover increases diversity of candidates and avoids premature convergence. The trial candidate
competes against the original candidate. If the trial candidate has better ﬁtness, it replaces the original candidate in
the population. This greedy selection pressure pushes the population toward optimal solutions. In summary,
differential evolution is a simple yet powerful population-based direct search algorithm for global optimization. It
is easy to implement, robust, fast, and requires minimal parameter tuning. With mutation, crossover, and
selection, it can solve complex real-world optimization problems efﬁciently.
An initial population of n solution vectors is generated for a d-dimensional optimization problem with d
parameters. Every generation t has a unique set of solutions, denoted by ai, for which i = 1, 2,..., n.
ai ¼ at
1;i; at
2;i; :::; at
d;i;
ð1Þ
This vector can be considered the chromosomes or genomes. The mutation scheme is used to carry out the
mutation. We ﬁrst randomly select three different vectors (ap, aq, and ar) for each vector ai at any time or
generation t. Then, the mutation process generates a so-called donor vector.
vtþ1
i
¼ at
p þ Fðat
q  at
rÞ
ð2Þ
where F 2 ½O; 2 is a parameter, often referred to as the differential weight. This requires that the minimum
number of the population size is n  4.
The crossover is controlled by a crossover parameter CR 2 ½O; 1, controlling the rate or probability for
crossover. The process of crossover can be conducted using two distinct methods: binomial as well as expo-
nential. The binomial system executes crossover operations on each of the d components or variables/parameters.
By generating a uniformly distributed random number ri 2 ½O; 1, the jth component of vi is formulated as
utþ1
j; i ¼
vj:i if ri  CR;
at
j; iOtherwise

ð3Þ
123
Neural Computing and Applications (2025) 37:27593–27630
27598
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 7
Algorithm 1 Differential evolution algorithm
3 Proposed approach
In the following subsections, an detailed analysis of the proposal’s requirements and the methodology utilized for
designing the proposed algorithm is presented.
3.1 Requirement of the proposal
In regard to recent advancements in optimization algorithms, the challenge of determining the superiority or
inferiority of particular algorithms has become a regular and signiﬁcant challenge. The No Free Lunch theorem
(NFL) has been recognized in the discipline, demonstrating that the utilization of a single optimization algorithm
cannot be generally successful for estimating the performance of all research challenges within various domains
[66]. In the present work similar adoption of DE algorithm is followed. The importance of this proposal comes
from the fact that while DE algorithms have excellent qualities. But the DE algorithm shows deﬁciencies in terms
of their exploitation and exploration phases, respectively. Therefore, this process results in the occurrence of local
optimal solutions, and this restricts getting to of the global optimum. In order to address the challenges mentioned
above, a new version of the DE algorithm known as LSHADESPA algorithm has been proposed. The LSHA-
DESPA algorithm incorporates three signiﬁcant modiﬁcations to enhance its performance. Firstly, a proportional
SP mechanism is employed to decrease the computational cost. Secondly, a SA-based scaling factor (F) is
introduced to enhance the exploration properties of the algorithm. Lastly, an oscillating iw-based CR is utilized to
achieve a balance between exploitation as well as exploration.
In summary, the LSHADESPA algorithm has undergone multiple modiﬁcations to enhance its operational
efﬁciency. The subsequent subsection provides an overview of the way in which each modiﬁcation has been
incorporated.
3.2 The proposal
The proposal section provides a brief overview of the novel proposed algorithm known as LSHADESPA
algorithm. The LSHADE algorithm has been enhanced with adaptive properties through the implementation of
three key modiﬁcations. These include the integration of oscillating iw-based CR, the utilization of SA-based
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27599

---

## Page 8
mutation factor F, and the incorporation of an adaptive SP strategy [41]. The algorithm commences by initializing
the variable N within a conﬁned search space, as speciﬁed by Eq. (4).
xi
t;0 ¼ xi
min þ a xi
max  xi
min


10pti ¼ 1; 2; :::; D
ð4Þ
For tth search agent, the parameter value for a D-dimensional problem is denoted by a 2 ½0; 1, while xmin and
xmax represent the lower as well as upper limits, respectively, of the problem under consideration.
Following the initialization process, the next phase involves the execution of the mutation operation. In the
present scenario, the mutation strategy employed is derived from the JADE algorithm. This strategy follows to the
current-to-best strategy, as outlined in Eq. (5)
xg
tþ1 ¼ xg
t þ Fg
t :ðxg
pbest  xg
t Þ þ Fg
t :ðxg
r1  xg
r2Þ
ð5Þ
The trial vector, denoted as xg
tþ1, is derived through mutation from the population size N. The solution xg
r1 is a
randomly selected solution from the mutated trial vector. The solution xg
pbest represents the personal best solution
for the gth iteration. Finally, the solution xg
r2 is obtained from an external archive A, which contains solutions from
previous inferior parents. In the initial phases, the archive is comprised of a set of xi
t individuals. But following
each generation g, a selection process is implemented whereby random individuals are removed from the overall
population. This is done to create space for the inclusion of new individuals from the archive.
To tackle the decrease in population size, a strategy known as the SP strategy, as outlined in reference [67], is
implemented. In the framework of a generalized algorithm, it is observed that an initial phase of increased
exploration is needed, while in the later stages, a shift toward adaptive exploitation becomes imperative. The
algorithm beneﬁts from reducing the population size as the number of iterations increases, as the algorithm
effectively decreases the total number of search agents needed for carrying out the operation. In simpler term, the
process of exploration needs a greater number of search agents in order to investigate all feasible locations inside
the search space. On the other hand, exploitation can be achieved with a restricted number of search agents due to
the concentration of the optimal solution within speciﬁc portions. Therefore, it is necessary to modify the
population in order to effectively explore the search space in the early phases by utilizing a larger population.
Following that, the population should converge toward a ﬁnal solution through exploitation, which can be
achieved by utilizing a smaller population.
In the present work, a phenomena of decreased population that is proportionally inﬂuenced by a study [67] are
utilized. This methodology employs the principle of population reduction through an enhancement in ﬁtness. The
adoption of this algorithm is justiﬁed by the need to address multi-modal challenges, which require solutions that
possess the ability to effectively explore extensive solution areas. Therefore, in the scenario where the initial
population size is signiﬁcantly large, it is possible for new solutions to thoroughly explore the whole search space,
as well as over the course of iterations, these solutions may gradually converge toward the global best solution,
which is located in a particular direction. Therefore, it becomes feasible to decrease the population size. The
decreased population size facilitates greater genetic drift as well as helps in the exploration of new solutions while
keeping the optimal solutions. In the last phases, every individual within the population is given an
equitable opportunity to attain the status of the global optimal solution . In a generalized case, the equation that
represents the decrease in population is presented in Eq. (6).
Ntþ1 ¼ P
1  Dbf best
t


Pt;
if Dbf best
t
 Dbfmaxbest
1  Dbfmaxbest
ð
ÞPt;
if Dbf best
t
 Dbfmaxbest
minP;
if Ptþ1 [ minN
8
<
:
ð6Þ
where the population size at generation t is denoted as Ptþ1, and the value of Dbf best
t
is determined by ðbf best
t1 bf best
t2
jbf best
t2 j
Þ,
123
Neural Computing and Applications (2025) 37:27593–27630
27600
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 9
which represents the change in the best ﬁtness, and threshold value is denoted by Dbf best
max. The minimum
population is deﬁned in order to reduce the effect of a small N. The population curve shape is an exponential
pattern during its early stages, maintaining a consistent trajectory during the middle phase, and once again
changing to an exponential growth pattern toward the ﬁnal stages. It is important to observe that the mentioned
curve pattern is consistently observed throughout successive iterations, unless a minimum population size is
reached or termination criteria are met. The utilization of an ensemble of sinusoidal adapted F is employed,
obtaining inspiration from the LSHADE-cnEpSin algorithm. In this work, two sinusoidal decreasing adjustments
are outlined in the given Eqs. (7) and (8).
Fyþ1
i
¼ 1
2 
sinð2p  freq  y þ pÞ  ymax y
ymax
þ 1


; if r1 [ 0:5
ð7Þ
Fyþ1
i
¼ 1
2 
sinð2p  freq  yÞ  ymax y
ymax
þ 1


; if r1\0:5
ð8Þ
In the present conﬁguration, the freq is further adjusted through the utilization of SA iw’s, as described in
reference [68]. This adjustment is mathematically formulated as follows Eq. (9):
freq ¼ amin þ ðamax  aminÞ  pðj1Þ
ð9Þ
where the value of amax, amin as well as j 2 [0, 1] and value of p ¼ 0:95. The utilization of an iw adaptation is
mainly inspired by the enhanced convergence characteristics shown by the SA approach. In addition, this
approach helps in the production of larger step sizes during the ﬁrst stage, which is a critical factor in facilitating
more effective exploration. On the other hand, as the process progresses, it generates smaller steps, which
promotes improved exploitation operations. In addition, exploration as well as exploitation, CR is additionally
carried out through the utilization of the oscillating iw technique [68, 69]. The mathematical expression for
oscillating iw can be represented as following Eq. (10):
CR ¼ bmin þ bmax
2
þ bmin  bmax
2
þ cos 2pg
A
ð10Þ
A ¼
2S1
3 þ 2j
ð11Þ
where the value bmax ¼ 0:9; bmin ¼ 0:5, S1 and j 2 [0,1], respectively. The utilization of this iw is signiﬁcantly
advantageous as it facilitates the algorithm’s smooth transition from the exploration to the exploitation phase
while maintaining optimal speed and avoiding potential trapping in local minima. This allows the algorithm to
show a gradual convergence throughout its earlier stages, followed by a faster convergence in its ﬁnal stages.
Note that after every generation, the archive or memory experiences update to allow for the storage of information
related to previous generations. The algorithm for the proposed algorithm is given in Algorithm 2.
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27601

---

## Page 10
Algorithm 2 LSHADESPA algorithm
123
Neural Computing and Applications (2025) 37:27593–27630
27602
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 11
Algorithm 3 Memory update algorithm in SHADE
In Algorithm 3, the index k (1  k  H) determines which position in the memory should be updated. At the
start of the search, k is set to 1. Each time a new element is added to the history, k is incremented. If k exceeds H,
it is reset to 1.
In the update process, all individuals in generation G fail to produce a trial vector better than the parent, i.e.,
SCR ¼ SF ¼ ;, the memory is not updated.
The weighted Lehmer mean meanWLðSÞ is calculated using the formula below. The ﬁtness improvement Dfk
inﬂuences the parameter adaptation (S refers to either SCR or SF).
meanWLðSÞ ¼
PjSj
k¼1 wk  S2
k
PjSj
k¼1 wk  Sk
ð7Þ
wk ¼
Dfk
PjSCRj
l¼1 Dfl
ð8Þ
Dfk ¼ jfðuk;GÞ  fðxk;GÞj
ð9Þ
When updating MCR, if MCR;k;G ¼? (where ? is a special ‘‘terminal value’’) or maxðSCRÞ ¼ 0 (meaning all
elements of SCR are 0), then MCR;k;Gþ1 is set to ?. If MCR is assigned the terminal value ?, it remains ﬁxed at ?
until the end of the search. This locks CRi to 0, enforcing a ‘‘change-one-parameter-at-a-time’’ policy, which
slows down convergence but is effective for multimodal problems.
3.3 Computational complexity
To determine the computational complexity, the key steps are as:
1.
Mutation & crossover (generating trial vectors):
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27603

---

## Page 12
•
Each individual undergoes mutation and crossover using the current-to-pbest/1/bin strategy.
•
Mutation requires the selection of the best individuals (Oðlog NÞ, if sorted initially).
•
The operations (vector additions, scaling, and binomial crossover) are OðDÞ.
•
Total cost per individual: OðDÞ.
•
Total cost per generation: OðNDÞ.
2.
Selection & archive update:
•
Each individual is compared with its trial vector.
•
Function evaluations dominate: OðDÞ.
•
Archive updates are Oð1Þ.
•
Total cost per generation: OðNDÞ.
3.
Population resizing (occasionally):
•
Sorting is at most OðN log NÞ, but since it happens only when resizing occurs, it is not a dominant cost
compared to OðNDÞ.
•
Removing individuals is OðNÞ, which is negligible compared to OðNDÞ.
3.3.1 Final complexity
Since the dominant operations are mutation, crossover, and function evaluations, the per-generation complexity
simpliﬁes to:
OðNDÞ
Over G generations, the total complexity is:
OðGNDÞ
This means that the run-time scales linearly with the number of generations G, population size N, and problem
dimension D.
4 Results
This section presents an analysis of the performance of the proposed LSHADESPA algorithm across various
benchmark suites. The purpose of this evaluation is to assess the performance of the LSHADESPA algorithm in
comparison to other MH algorithms. The LSHADESPA algorithm is evaluated on the CEC 2014 [42] CEC 2017
[43], CEC 2021 [44] as well as CEC 2022 [45] benchmarks test suite. This section is divided into 4 subsection. In
the ﬁrst subsection, the performance of the LSHADESPA algorithm has been evaluated by utilizing CEC 2014
test suite and compared with the various MH algorithm such as IMEHO [47], LX-BBO [46], PBIL [47], B-BBO
[46], VNBA [47], RW-GWO [57], ISOS [49], as well as CCS [47]. In 2nd subsection, the performance of the
LSHADESPA algorithm is evaluated utilizing a set of 30 benchmark problems from the CEC 2017 and the
outcomes of the LSHADESPA algorithm are compared with the other MH algorithms (CV1.0 [55], SaDE [50],
MVMO [54], JADE [26], SHADE [52], LSHADE [53], SACS [70] as well as CVnew [56]). In the 3rd subsection,
the LSHADESPA algorithm utilizes a set of 10 benchmark challenges from the CEC 2021 competition for further
evaluation. In the last subsection, the performance of the LSHADESPA algorithm is tested with the CEC 2022
challenges and conducted a comparative analysis with other MH optimization algorithms (DE [58], LSO [59],
KOA [48], PSO [58], EA4eig [51], and NL-SHADE-RSP-MID [61])
123
Neural Computing and Applications (2025) 37:27593–27630
27604
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 13
The algorithms were analyzed using a 12th generation, Windows 11 operating system, namely a 64-bit laptop
with an i5-12,500 H, 16.00 GB of RAM, utilizing MATLAB version R2022a.
4.1 Statistical outcomes for CEC 2014 benchmarks
The proposed LSHADESPA algorithm performance is evaluated by using CEC 2014 test function. Various MH
algorithms utilized for comparison are IMEHO [47], LX-BBO [46], PBIL [47], B-BBO [46], VNBA [47], RW-
GWO [57], ISOS [49], as well as CCS [47]. The algorithms employed for comparison have been observed to be
highly efﬁcient in tackling complex optimization challenges.
Experimental testing: The simulations ﬁndings are presented in Table 1 in terms of error mean as well as std
value. The table shows that functions F1, F2, F3, F7, as well as F8 demonstrate that only the LSHADESPA
algorithm is able to produce outcomes that are closely to the global optimal solution, while the remaining MH
optimization techniques may become trapped in local minima. Also for functions F4, F5, F6, F9, F10, F11, F16,
F17, F18, F19, F20, F21, F22, F23, F25, F26, and F20, LSHADESPA algorithm shows superior performance while
comparing with the other MH optimization techniques. Both the algorithms (B-BBO and LX-BBO algorithms)
display similar outcomes in terms of error mean as well as std for the function F12, and it is very highly difﬁcult to
comment which algorithm is good for this test function. For functions F13, F14, as well as F15, IMEHO algorithm
displays best outcomes. Also ISOS algorithms show superior outcomes as compared to other MH algorithms for
function F24. For the functions F28, F29, and F30, the RW-GWO algorithm shows best performance as compared
to the other MH algorithms. Figure 2 illustrates the radarchart of LSHADESPA, LX-BBO, B-BBO, IMEHO,
CCS, RW-GWO, ISOS, PBIL, and VNBA for CEC 2014 numerical challenges.
Statistical testing: Two statistical tests, namely Wilcoxon’s rank-sum [62] as well as the Friedman rank (f-rank)
test [49], are utilized, to assess the statistical importance of the LSHADESPA algorithm. Both tests presented
listed below are of a nonparametric type.
Wilcoxon’s rank-sum test: This test is used to compare the performance of two algorithm and assign the p-rank.
The rank of every test function is provided in the third row of Table 1 for each test function and shows in terms of
win(w)/loss(l)/tie(t). The w condition will arise when the algorithm performs better than the proposed algorithm
and assigns ‘‘?’’ sign. l condition will arise when the proposed algorithm performs better as compared to the other
algorithm and assigns ‘‘-’’ sign. For the last condition, t will occur when both the algorithm performance is the
same and assign ‘‘=’’. So from Table 1 and Fig. 3 it is clearly seen that the proposed LSHADESPA algorithm
shows superior performance as compared to the other MH algorithm.
Friedman rank test: Friedman rank (f-rank) test is also used to validate the performance of the LSHADESPA
algorithm. In the f-rank test every algorithm assigned with unique rank, based on their performance, is presented
in the 4th row of Table 1. The overall f-rank of every algorithm is presented in the last row of Table 1. From
Table 1 and Fig. 4, it is clearly displayed LSHADESPA algorithm obtained the ﬁrst rank.
4.2 Statistical outcomes for CEC 2017 benchmarks
In this subsection, the effectiveness of the LSHADESPA algorithm is evaluated utilizing a set of thirty benchmark
challenges from the CEC 2017 competition. For CEC 2017 benchmark functions, the proposed LSHADESPA
algorithm is contrasted with other MH algorithms, namely SaDE [50], JADE [26], SHADE [52], LSHADE [53],
MVMO [54], CV1.0 [55], SACS [70], and CVnew [56]. All of the algorithms chosen for comparison are extremely
competitive as well as have proven their usefulness in solving [41]. The simulation outcomes for all algorithms
are compared as well as presented in terms of the mean and standard deviation (std) values. From Table 2, it has
been analyzed that for function pF1 the performance of SHADE and LSHADE is optimum. For function,
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27605

---

## Page 14
Table 1 Comparison of the outcomes of LSHADESPA algorithm with other MH algorithms for CEC 2014
Functions
LSHADESPA
LX-BBO
[46]
B-BBO [46]
IMEHO
[47]
CCS [47]
RW-
GWO
[57]
ISOS [49]
PBIL [47]
VNBA
[47]
F1
Mean
0.000E100
1.01E?07
6.50E?06
2.37E?06
1.46E?08
8.02E?06
9.82E?05
3.42E?08
2.43E?08
Std
0.000E100
1.01E?07
1.30E?06
4.32E?06
3.27E?07
3.31E?06
7.05E?05
1.09E?08
5.93E?07
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
6
4
3
7
5
2
9
8
F2
Mean
0.000E100
5.34E?04
2.35E?04
5.49E?03
2.60E?09
2.23E?05
5.27E?00
4.08E?10
1.92E?10
Std
0.000E100
2.14E?04
9.99E?03
4.87E?03
5.22E?08
5.51E?05
1.72E?01
3.39E?09
4.23E?09
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
5
4
3
7
6
2
9
8
F3
Mean
0.000E100
1.63E?04
6.03E?03
1.41E?02
2.70E?03
3.16E?02
4.79E?02
9.19E?04
2.93E?04
Std
0.000E100
1.70E?04
3.15E?03
1.58E?02
7.74E?04
4.34E?02
6.24E?02
1.75E?04
1.39E?04
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
7
6
2
5
3
4
9
8
F4
Mean
4.7014E205
9.99E?01
1.02E?02
3.41E?01
1.24E?02
3.22E?02
5.98E?01
3.43E?03
1.60E?03
Std
3.3507E204
2.84E?01
3.13E?01
4.77E?01
4.09E?01
1.80E?01
3.57E?01
7.56E?02
3.63E?02
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
4
5
6
7
3
2
9
8
F5
Mean
2.0149E101
3.06E?00
3.74E?00
2.10E?01
2.10E?01
2.05E?01
2.03E?01
2.10E?01
2.10E?01
Std
3.2489E202
7.86E-01
4.91E-01
5.99E-02
8.81E-02
7.46E-02
6.67E-02
5.56E-02
5.43E-02
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
9
8
4
7
6
5
3
2
F6
Mean
5.7819E206
1.70E?01
1.99E?01
1.20E?01
2.50E?01
9.84E?00
1.05E?01
3.80E?01
3.30E?01
Std
1.9366E205
3.12E?00
2.70E?00
2.72E?00
2.00E?00
3.49E?00
2.39E?00
1.16E?00
2.58E?00
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
5
6
4
7
2
3
9
8
F7
Mean
0.000E100
1.75E-01
7.81E-02
0.00E?00
2.30E?01
2.53E-01
1.56E-02
3.40E?02
1.11E?02
Std
0.000E100
8.56E-02
4.44E-02
1.19E-01
3.52E?00
1.43E-01
1.83E-02
2.74E?01
1.81E?01
p-
rank
–
–
–
–
–
–
-
–
f-rank
1
5
4
2
7
6
3
9
8
F8
Mean
0.000E100
5.53E?01
4.71E-01
3.30E?01
2.90E?02
4.38E?01
1.47E?01
3.00E?02
1.74E?02
Std
0.000E100
3.78E?02
6.79E-01
9.19E?00
2.23E?01
8.48E?00
3.34E?00
1.03E?01
1.61E?01
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
6
2
4
8
5
3
9
7
F9
Mean
1.2385E101
7.66E?01
9.11E?01
3.20E?01
2.90E?02
6.33E?01
2.56E?02
3.70E?02
2.50E?02
Std
2.6862E100
1.61E?01
1.54E?01
1.15E?01
2.38E?01
1.30E?01
1.34E?01
1.69E?01
2.03E?01
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
4
5
2
8
3
7
9
6
123
Neural Computing and Applications (2025) 37:27593–27630
27606
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 15
Table 1 (continued)
Functions
LSHADESPA
LX-BBO
[46]
B-BBO [46]
IMEHO
[47]
CCS [47]
RW-
GWO
[57]
ISOS [49]
PBIL [47]
VNBA
[47]
F10
Mean
7.3333E202
1.25E?04
6.68E?03
2.26E?03
8.55E?03
9.61E?02
1.78E?03
6.26E?03
3.50E?03
Std
5.2993E202
1.16E?02
4.58E?02
5.72E?02
4.91E?02
2.72E?02
4.09E?01
3.05E?02
3.47E?02
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
9
7
4
8
2
3
6
5
F11
Mean
1.2785E103
1.23E?04
6.71E?03
2.86E?03
8.83E?03
2.68E?03
1.48E?03
7.10E?03
6.80E?03
Std
1.9627E102
3.41E?02
5.17E?02
5.38E?02
5.50E?02
3.68E?02
4.54E?02
2.97E?02
3.79E?02
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
9
5
4
8
3
2
7
6
F12
Mean
1.9835E-01
1.11E202
1.11E202
1.00E?01
1.00E?01
5.45E-01
3.55E-01
1.00E?01
1.00E?01
Std
2.9275E-02
1.75E218
1.75E218
5.26E-01
1.09E?00
1.66E-01
5.73E-02
3.38E-01
3.51E-01
p-
rank
?
?
–
–
–
–
–
–
f-rank
3
1
1
8
9
5
4
6
7
F13
Mean
1.3820E-01
6.55E-01
6.78E-01
0.00E100
0.00E?00
2.80E-01
3.77E-01
0.00E?00
0.00E?00
Std
2.2746E-02
1.56v01
7.98E-02
6.25E202
1.76E-01
6.30E-02
7.10E-02
2.56E-01
3.64E-01
p-
rank
–
–
–
?
?
–
–
–
f-rank
3
8
9
1
2
6
7
4
5
F14
Mean
1.8446E-01
6.20E-01
3.93E-01
0.00E100
1.00E?01
4.23E-01
2.71E-01
1.00E?02
6.00E?01
Std
2.6085E-02
2.96E-01
1.55E-01
9.85E-02
1.88E?00
2.15E-01
5.12E-02
1.16E?01
1.22E?01
p-
rank
–
–
?
–
–
–
–
–
f-rank
2
6
4
1
7
5
3
9
8
F15
Mean
2.3924E?00
1.55E?01
1.88E?01
0.00E100
8.00E?01
8.81E?00
1.06E?01
6.84E?05
2.39E?03
Std
2.5254E-01
5.49E?00
5.64E?00
1.35E100
3.03E?01
1.51E?00
3.71E?00
2.85E?05
1.22E?03
p-
rank
–
–
?
–
–
–
–
–
f-rank
2
5
6
1
7
3
4
9
8
F16
Mean
8.5223E100
1.08E?01
1.06E?01
2.00E?01
2.00E?01
1.03E?01
9.21E?01
2.00E?01
2.00E?01
Std
3.9762E201
5.84E-01
6.25E-01
7.64E-01
1.75E201
6.11E-01
7.31E-01
2.12E-01
3.66E-01
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
4
3
8
5
2
9
6
7
F17
Mean
1.5498E102
1.49E?06
1.27E?06
7.69E?04
1.15E?07
5.71E?05
1.75E?05
9.74E?06
2.53E?06
Std
1.0197E102
9.34E?05
5.46E?05
8.38E?04
4.59E?06
4.10E?05
1.64E?05
2.79E?06
3.34E?06
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
5
4
9
6
3
8
7
2
F18
Mean
6.9997E100
2.89E?03
8.22E?02
3.30E?03
1.10E?08
6.52E?03
3.89E?03
6.16E?08
1.66E?08
Std
2.5029E100
4.27E?03
1.00E?03
3.52E?03
4.66E?07
4.63E?02
5.15E?03
1.68E?08
1.03E?08
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
3
2
4
7
6
5
9
8
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27607

---

## Page 16
Table 1 (continued)
Functions
LSHADESPA
LX-BBO
[46]
B-BBO [46]
IMEHO
[47]
CCS [47]
RW-
GWO
[57]
ISOS [49]
PBIL [47]
VNBA
[47]
F19
Mean
2.5506E100
5.19E?03
7.81E?03
1.05E?01
4.00E?01
1.14E?01
7.79E?01
1.90E?02
1.20E?02
Std
6.5981E201
5.67E?03
4.67E?03
1.74E?00
5.91E?00
2.03E?00
1.78E?00
3.42E?01
3.82E?01
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
8
9
2
4
3
5
7
6
F20
Mean
2.5130E100
2.61E?04
1.62E?04
2.10E?02
1.03E?06
6.27E?02
4.98E?03
3.59E?04
1.69E?04
Std
8.1871E201
1.57E?04
4.11E?03
8.17E?01
9.05E?05
1.12E?03
3.40E?03
1.77E?04
6.57E?03
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
7
5
2
9
3
4
8
6
F21
Mean
9.8109E101
1.11E?06
1.22E?06
2.72E?04
5.66E?06
2.58E?05
8.90E?04
2.52E?06
2.30E?06
Std
9.2975E101
7.95E?05
7.96E?05
1.83E?04
2.73E?06
1.76E?05
1.07E?05
1.19E?06
1.35E?06
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
5
6
2
9
4
3
8
7
F22
Mean
6.3215E101
1.88E?03
1.68E?02
2.10E?02
1.34E?03
2.08E?02
2.75E?02
1.02E?03
8.40E?02
Std
5.4478E101
2.03E?02
2.47E?02
1.01E?02
1.88E?02
2.08E?02
1.45E?02
1.88E?02
1.28E?02
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
9
2
4
8
3
5
7
6
F23
Mean
3.1507E102
4.11E?02
3.43E?02
3.20E?02
3.50E?02
3.15E?02
3.15E?02
6.00E?02
3.90E?02
Std
6.3290E202
6.43E?01
2.84E?01
4.78E-01
7.66E?00
2.77E-01
1.60E?01
6.70E?01
2.47E?01
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
8
5
4
6
2
3
9
7
F24
Mean
2.0977E?02
1.47E?04
3.41E?04
2.40E?02
2.20E?02
2.00E?02
2.00E102
4.00E?02
2.30E?02
Std
1.0903E?01
8.37E?03
2.35E?04
6.46E?00
2.51E?00
3.04E-03
1.50E-03
1.42E?01
2.53E?01
p-
rank
–
–
–
–
?
?
–
–
f-rank
3
8
9
6
4
2
1
7
5
F25
Mean
2.02553E102
5.29E?02
6.53E?02
2.10E?02
2.20E?02
2.04E?02
2.00E?02
2.40E?02
2.10E?02
Std
3.5990E202
4.36E?01
6.01E?01
2.08E?00
4.44E?00
1.18E?00
8.07E-01
6.00E?00
1.07E?01
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
8
9
5
6
3
2
7
4
F26
Mean
1.0013E102
2.12E?00
3.64E?01
1.00E?02
1.00E?02
1.00E?02
1.00E?02
1.00E?02
1.00E?02
Std
2.0795E202
3.46E?00
5.62E?01
6.00E-02
2.06E-01
7.36E-02
9.55E-02
2.09E-01
4.30E-01
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
8
9
2
5
3
4
6
7
F27
Mean
3.0196E102
1.95E?02
3.04E?02
5.80E?02
5.30E?02
4.09E?02
5.43E?02
1.08E?03
1.29E?03
Std
1.4002E101
1.04E?02
1.60E?02
1.41E?02
7.92E?01
6.09E?00
1.36E?02
2.80E?02
3.30E?01
p-
rank
–
–
–
–
–
–
–
–
f-rank
1
4
5
6
3
2
6
8
9
F28
mean
8.3377E?02
1.94E?03
2.12E?03
9.70E?02
1.44E?03
4.34E102
9.68E?02
1.39E?03
1.68E?03
std
1.8931E?01
1.04E?02
4.44E?02
2.44E?02
9.46E?02
8.45E?00
4.12E?01
1.33E?02
2.33E?02
p-
rank
–
–
?
–
–
–
–
–
f-rank
2
8
9
4
6
1
3
5
7
123
Neural Computing and Applications (2025) 37:27593–27630
27608
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 17
pF2,pF11,pF15,pF18, and pF22, performance of LSHADESPA is best among all tested MH algorithms. For pF3
LSHADESPA performs equally like SHADE and LSHADE. For the function pF4, pF17, pF23, pF24, pF25, pF27,
and pF28 functions, CVnew algorithm performed best performance as compared to the other MH algorithms. In the
case of functions pF5, pF7, pF8, pF10, pF20, pF21, and pF29, the outcomes obtained from the LSHADE algorithm
display superior performance when compared to the other MH techniques. From the outcomes obtained, it is clear
that JADE algorithms display superior performance for the function pF6. For functions F9, it can be seen that
LSHADE and LSHADESPA algorithms demonstrate similar outcomes in terms of mean as well as std. On the
other hand, the MVO algorithm comes as the optimal choice for the functions of pF12, pF13 and pF25. In the case
of functions pF16, pF19 and pF30, it can be determined that the SACS algorithm provides the most optimal
outcomes in terms of mean as well as std values. Figure 5 presents the radar of LSHADE, SACS, SHADE, SaDE,
CV1.0, MVMO, JADE, CVnew, and LSHADESPA for CEC 2017 numerical challenges. Note that the proposed
LSHADESPA algorithm is found to be superior than the other MH algorithm under comparison for CEC 2017
benchmark test suite
Statistical testing To validate the performance of the proposed LSHADESPA, statistical test, namely Wil-
coxon’s rank-sum [62] as well as Friedman rank (f-rank) test [49], is performed. This test is nonparametric in
nature and utilized to test the statistical signiﬁcance of the algorithm. First, the rank-sum test determines if the
proposed LSHADESPA algorithm is signiﬁcantly superior or not. LSHADESPA’s performance is provided
below in terms of win(w)/loss(l)/tie(t). The w condition happens if the algorithm under test outperforms the
proposed approach and is represented by the ‘‘?’’ sign. In the l condition, the test algorithm performs worse than
the LSHADESPA algorithm, as indicated by the ‘‘-’’sign. The ﬁnal t circumstance happens when there is no
statistical difference between the algorithms that are under test and is represented by the ’’=’’ symbol. The w/l/t
row in Table 2 and Fig. 6 shows that the proposed LSHADESPA performs much better than other algorithms in
the majority of circumstances. From the table it is clearly indicated that LSHADESPA wins over SHADE in 25
functions, CV1.0 in 29 functions, JADE in 26 functions, MVMO in 25 functions, CVnew in 25 functions,
LSHADE in 14 functions, and over SACS in 25 functions out of total 30 Functions. LSHADESPA lashes out
SaDE in all 30 functions. After the rank-sum test, the efﬁciency of the algorithm is tested by utilizing the f-rank
test. In the fourth row of each algorithm of Table 2, a unique rank is given based on their outcomes. In the last
Table 1 (continued)
Functions
LSHADESPA
LX-BBO
[46]
B-BBO [46]
IMEHO
[47]
CCS [47]
RW-
GWO
[57]
ISOS [49]
PBIL [47]
VNBA
[47]
F29
Mean
7.2308E?02
1.98E?07
3.09E?07
1.21E?03
1.20E?06
2.14E102
5.70E?05
5.70E?06
7.47E?06
Std
1.2212E?01
3.95E?06
6.91E?06
2.16E?02
7.03E?05
2.37E100
2.14E?06
3.33E?06
1.20E?06
p-
rank
–
–
–
–
?
–
–
–
f-rank
2
8
9
3
5
1
4
6
7
F30
Mean
1.1465E?03
6.95E?06
1.38E?07
4.08E?03
7.67E?04
6.69E102
2.38E?05
1.49E?05
1.89E?05
Std
4.3062E?02
1.03E?07
1.08E?07
1.44E?03
3.37E?04
2.14E?02
1.10E?03
5.55E?04
1.03E?05
p-
rank
–
–
–
–
?
–
–
–
f-rank
2
8
9
3
4
1
7
5
6
w/l/t
NA
0/30/0
0/30/0
0/30/0
0/30/0
4/26/0
1/29/0
0/30/0
0/30/0
Overall
f-rank
value
41
190
175
113
191
102
123
221
196
f-rank
1
6
5
3
7
2
4
9
8
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27609

---

## Page 18
row of the table f-rank value is given. From Table 2 and Fig. 7, it is clearly observed that the LSHADESPA
algorithm got the 1st rank.
4.3 Statistical outcomes for CEC 2021 benchmarks
In this section, an evaluation is conducted to assess the performance of the LSHADESPA algorithm. The
evaluation utilizes a set of 10 benchmark problems from the CEC 2021 competition. The minimization problems
presented involve a series of operations, namely basic, rotation, translation, as well as shifting. These operations
can be performed independently or in combination with one another? Additional detail on the CEC 2021
benchmark functions can be found in the reference [71]. The parametric settings utilized for the LSHADESPA
algorithm for the CEC 2021 benchmarks are similar to those utilized in the CEC 2017 benchmarks. The
experiments have been done a total of 30 times, with two different values for the variable D ¼ 10 as well as 20.
Fig. 2 Radarchart of LSHADESPA, LX-BBO, B-BBO, IMEHO, CCS, RW-GWO, ISOS, PBIL, and VNBA for CEC 2014
numerical challenges
123
Neural Computing and Applications (2025) 37:27593–27630
27610
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 19
The maximum number of function evaluations for a problem with D equal to 10 is 200,000. However, for a
problem with D equal to 20, the maximum number of function evaluations increases to 1,000,000. It is worth
noting that each function in both cases has a search range of ½100; 100D. The outcomes obtained from the
simulation for CEC 2021 are presented in Tables 3 and 4. The tables demonstrate that the proposed LSHA-
DESPA algorithm displays an outstanding level of competitiveness. It consistently provides outcomes that are in
closely matching to the optimal solutions for the CEC 2021 challenges.
4.4 Statistical outcomes for CEC 2022 benchmarks
As a further extension, the performance of the LSHADESPA algorithm is evaluated utilizing a set of 12
benchmark problems from the CEC 2022 competition in this subsection [45]. To determine the effectiveness of
the LSHADESPA algorithm, a comparative analysis is conducted against other MH optimization algorithms. The
algorithms employed for comparison include DE [58], LSO [59], KOA [48], PSO [58], EA4eig [51], and NL-
SHADE-RSP-MID [61]. The outcomes of the CEC 2022 problem are presented in Table 5 in terms of mean and
Fig. 3 Comparison of the
performance of the LSHA-
DESPA algorithm with
other algorithms for CEC
2014 (w/l/t scenario)
Fig. 4 Rankings of algo-
rithms for CEC 2014
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27611

---

## Page 20
Table 2 Comparison of the outcomes of LSHADESPA algorithm with other MH algorithms for CEC 2017
LSHADE
SACS
SHADE
SaDE
CV1.0
MVMO
JADE
CVnew
LSHADESPA
pF1
Mean
0.000E100
1.000E?10
0.000E100
1.221E?03
1.000E?10
1.302E-05
5.201E-14
1.000E?10
6.901E-07
Std
(0.000E?00)
(0.000E?00)
(0.000E?00)
(1.940E?03)
(0.000E?00)
(5.571E-06)
(2.481E-14)
(0.000E?00)
(1.741E-06)
p-
rank
?
–
?
–
–
–
?
–
f-rank
1
6
1
9
6
5
3
6
4
pF3
Mean
0.000E?00
4.071E?03
0.000E?00
2.701E?02
1.912E?04
5.262E-07
1.741E?04
8.681E?03
0.000E100
Std
(4.052E?03)
(0.000E?00)
(0.000E?00)
(8.242E?02)
(6.241E?03)
(1.062E-07)
(3.671E?04)
(1.492E?03)
(0.000E100)
p-
rank
=
–
=
–
–
–
–
–
f-rank
1
6
1
5
8
4
9
7
1
pF4
Mean
8.152E?01
4.191E?01
4.921E?01
8.892E?01
3.552E101
5.652E?01
1.121E?02
2.631E?01
3.592E?01
Std
(4.792E?01)
(2.681E?01)
(4.692E?01)
(4.191E?01)
(3.622E?01)
(8.792E?00)
(6.241E?03)
(5.891E?00)
(2.493E?01)
p-
rank
–
–
–
–
?
–
?
–
f-rank
8
4
5
7
2
6
9
1
3
pF5
Mean
1.182E101
2.261E?02
3.241E?01
9.222E?01
3.372E?02
8.042E?01
5.391E?01
2.361E?02
5.121E?01
Std
(2.011E?00)
(2.311E?01)
(5.011E?00)
(1.842E?01)
(8.051E?01)
(1.611E?01)
(8.762E?00)
(3.752E?01)
(1.411E?01)
p-
rank
?
–
?
–
–
–
–
–
f-rank
1
7
2
6
9
5
4
8
3
pF6
Mean
5.611E-05
4.842E-01
8.351E-04
7.422E-03
4.861E?01
5.372E-03
1.411E213
4.041E?01
1.501E-08
Std
(3.682E-04)
(3.381E-01)
(1.000E-03)
(2.311E-02)
(4.791E?01)
(3.272E-03)
(9.061E-14)
(8.101E?00)
(5.5210E-08)
p-
rank
–
–
–
–
–
?
–
–
f-rank
3
7
4
6
9
5
1
8
2
pF7
Mean
6.282E1101
5.471E?02
8.061E?01
1.412E?02
2.711E?02
1.201E?02
1.000E?02
2.191E?02
1.200E?02
Std
(1.691E?00)
(4.032E?01)
(3.741E?00)
(1.932E?01)
(7.232E?01)
(1.242E?01)
(6.451E?00)
(3.432E?01)
(1.771E?01)
p-
rank
?
–
?
–
–
–
?
–
f-rank
1
9
2
6
8
5
3
6
4
pF8
Mean
1.081E101
4.741E?02
5.492E?01
9.382E?01
7.542E?01
3.201E?01
3.261E?02
2.491E?02
5.381E?01
Std
(2.242E?00)
(4.621E?01)
(7.731E?00)
(1.761E?01)
(1.581E?01)
(3.781E?00)
(7.261E?01)
(4.472E?01)
(1.341E?01)
p-
rank
?
–
–
–
–
?
–
–
f-rank
1
9
4
6
5
2
8
7
3
123
Neural Computing and Applications (2025) 37:27593–27630
27612
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 21
Table 2 (continued)
LSHADE
SACS
SHADE
SaDE
CV1.0
MVMO
JADE
CVnew
LSHADESPA
pF9
Mean
0.000E100
4.741E?02
1.071E?00
4.821E?01
1.000E?04
7.353E?00
1.131E?00
1.033E?04
0.000E100
Std
(0.000E100)
(1.708E?03)
(9.347E-01)
(6.222E?01)
(2.893E?03)
(5.745E?00)
(1.254E?00)
(3.091E?03)
(0.000E100)
p-
rank
=
–
–
–
–
–
–
–
f-rank
1
7
3
6
8
5
4
9
1
pF10
Mean
3.143E103
5.292E?03
3.311E?03
6.591E?03
7.062E?03
3.463E?03
3.721E?03
6.061E?03
6.811E?03
Std
(2.501E?02)
(6.093E?02)
(2.893E?02)
(1.592E?03)
(5.301E?02)
(4.282E?02)
(2.513E?02)
(3.521E?02)
(3.461E?02)
p-
rank
?
?
?
–
–
?
?
?
f-rank
1
5
2
8
9
3
4
6
7
pF11
Mean
4.832E?01
6.551E?01
1.191E?02
1.082E?02
1.633E?02
4.712E?01
1.311?02
1.131E?02
3.241E101
Std
(7.881E?00)
(1.031E?01)
(2.901E?01)
(3.501E?01)
(3.332E?01)
(8.693E?00)
(3.361E?01)
(1.862E?01)
(3.402E100)
p-
rank
–
–
–
–
–
–
–
–
f-rank
3
4
6
5
9
2
8
7
1
pF12
Mean
2.132E?03
1.000E?10
5.102E?03
1.093E?05
1.001E?10
1.261E103
5.102E?03
1.000E?10
1.484E?03
Std
(4.491E?02)
(0.000E?00)
(2.853E?03)
(6.201E?04)
(0.000E?00)
(2.773E?02)
(3.282E?03)
(0.000E?00)
(4.888E?02)
p-
rank
–
–
–
–
–
?
–
–
f-rank
3
7
4
6
9
1
5
7
2
pF13
mean
6.232E?01
9.181E?09
2.601E?02
1.212E?03
1.000E?10
4.341E101
3.053E?02
9.792E?09
1.322E?02
Std
(2.842E?01)
(2.732E?09)
(1.433E?02)
(1.452E?03)
(0.000E?00)
(1.732E?01)
(2.641E?02)
(1.393E?09)
(3.121E?01)
p-
rank
?
–
–
–
–
?
–
–
f-rank
2
7
4
6
9
1
5
8
3
pF14
Mean
2.883E101
2.644E?03
2.111E?02
2.161E?03
2.011E?02
4.832E?01
1.011E?04
3.961E?01
4.185E?01
Std
(2.902E?00)
(1.533E?02)
(7.266E?01)
(2.201E?03)
(2.102E?01)
(1.184E?01)
(3.103E?04)
(1.581E?01)
(3.796E?00)
p-
rank
?
–
–
–
–
–
–
?
f-rank
1
8
6
7
5
4
9
2
3
pF15
Mean
4.142E?01
2.381E101
3.201E?02
3.352E?03
1.343E?09
4.412E?01
3.474E?02
2.821E?02
4.083E?01
Std
(9.892E?00)
(5.933E?03)
(1.392E?02)
(2.771E?03)
(3.443E?09)
(1.091E?01)
(4.392E?02)
(3.483E?02)
(6.181E?00)
p-
rank
–
?
–
–
–
–
–
–
f-rank
4
1
6
8
9
3
7
5
2
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27613

---

## Page 22
Table 2 (continued)
LSHADE
SACS
SHADE
SaDE
CV1.0
MVMO
JADE
CVnew
LSHADESPA
pF16
Mean
3.732E?02
2.723E102
7.301E?02
8.142E?02
1.502E?03
8.374E?02
8.533E?02
1.431E?03
7.192E?02
Std
(1.142E?02)
(1.713E?02)
(1.821E?02)
(2.311E?02)
(2.753E?02)
(1.901E?02)
(1.712E?02)
(2.082E?02)
(1.271E?02)
p-
rank
?
?
–
–
–
–
–
–
f-rank
2
1
4
5
9
6
7
8
3
pF17
Mean
2.513E?02
5.012E?02
5.111E?02
5.075E?02
1.214E?03
5.163E?02
6.000E?02
1.101E102
4.383E?02
Mean
(7.421E?01)
(1.152E?02)
(1.081E?02)
(1.522E?02)
(1.824E?02)
(1.301E?02)
(1.185E?02)
(1.892E?02)
(9.761E?01)
p-
rank
?
–
–
–
–
–
–
?
f-rank
2
4
6
5
9
7
8
1
3
pF18
Mean
3.891E?01
1.032E?05
1.853E?02
3.232E?04
5.141E?02
4.123E?01
1.861E?02
1.482E?02
3.221E101
Std
(1.082E?01)
(4.161E?04)
(1.000E?02)
(1.676E?04)
(1.163E?02)
(1.912E?01)
(1.201E?02)
(4.403E?01)
(3.212E100)
p-
rank
–
–
–
–
–
–
–
–
f-rank
2
9
5
7
8
3
6
4
1
pF19
Mean
2.423E?01
1.152E102
1.561E?02
1.101E?04
1.721E?02
1.703E?01
3.232E?02
5.522E?01
2.771E?01
Std
(8.783E?00)
(2.442E?00)
(5.633E?01)
(1.671E?04)
(4.142E?02)
(5.101E?00)
(1.203E?03)
(1.061E?01)
(1.131E?03)
p-
rank
–
?
–
–
–
?
–
–
f-rank
4
1
6
9
7
2
8
5
3
pF20
Mean
1.731E102
3.231E?02
3.321E?02
3.462E?02
1.023E?03
3.241E?02
4.351E?02
2.782E?02
2.731E?02
Std
(7.841E?01)
(8.632E?01)
(1.193E?02)
(1.511E?02)
(2.112E?02)
(1.442E?02)
(1.301E?02)
(1.623E?02)
(7.421E?01)
p-
rank
?
–
–
–
–
–
–
–
f-rank
1
4
6
7
9
5
8
3
2
pF21
Mean
2.092E102
2.513E?02
2.301E?02
2.862E?02
5.383E?02
2.743E?02
2.501E?02
1.151E?02
3.201E?02
Std
(1.901E?00)
(1.113E?02)
(5.082E?00)
(1.331E?01)
(6.222E?01)
(1.573E?01)
(9.601E?00)
(8.744E?01)
(1.444E?01)
p-
rank
?
–
–
–
–
–
–
–
f-rank
1
4
6
7
9
5
8
3
2
pF22
Mean
2.462E?03
1.000E?02
3.131E?03
2.912E?03
7.301E?03
3.232E?03
3.321E?03
5.711E?03
1.000E102
Std
(1.581E?03)
(6.072E?03)
(1.521E?03)
(3.212E?03)
(1.963E?03)
(1.688E?03)
(1.791E?03)
(3.632E?02)
(1.671E103)
p-
rank
–
–
–
–
–
–
–
–
f-rank
4
2
5
3
9
7
6
8
1
123
Neural Computing and Applications (2025) 37:27593–27630
27614
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 23
Table 2 (continued)
LSHADE
SACS
SHADE
SaDE
CV1.0
MVMO
JADE
CVnew
LSHADESPA
pF23
Mean
4.271E?02
5.111E?02
4.561E?02
5.211E?02
7.712E?02
5.021E?02
4.763E?02
1.822E102
4.712E?02
Std
(5.033E?00)
(4.731E?01)
(8.722E?00)
(2.021E?01)
(8.033E?01)
(1.682E?03)
(1.141E?01)
(5.083E?01)
(1.582E?01)
p-
rank
?
–
–
–
–
–
–
?
f-rank
5
7
3
8
9
6
4
1
2
pF24
Mean
5.042E?02
5.303E?02
5.301E?02
5.861E?02
8.292E?02
5.832E?02
5.273E?02
3.221E102
5.301E?02
Std
(2.311E?00)
(2.623E?01)
(7.422E?00)
(1.873E?01)
(1.202E?01)
(1.663E?01)
(7.591E?00)
(8.942E?01)
(1.472E?01)
p-
rank
–
–
–
–
–
–
–
?
f-rank
7
3
5
8
9
6
4
1
2
pF25
Mean
4.822E?02
4.801E?02
5.051E?02
5.701E?02
5.412E?02
5.062E?02
5.183E?02
4.692E102
4.792E?02
Std
(1.602E?01)
(8.623E?00)
(3.611E?01)
(3.041E?01)
(1.482E?01)
(3.102E?01)
(3.431E?01)
(2.231E?01)
(3.071E?00)
p-
rank
–
–
–
–
–
–
–
?
f-rank
4
3
5
9
8
6
7
1
2
pF26
Mean
1.111E?03
3.001E102
1.381E?03
2.512E?03
2.423E?03
1.901E?03
1.542E?03
1.132E?03
1.251E?03
Std
(4.461E?01)
(2.382E-04)
(9.751E?01)
(3.362E?02)
(1.852E?03)
(2.831E?02)
(1.181E?02)
(1.531E?03)
(6.882E?00)
p-
rank
?
?
–
–
–
–
–
–
f-rank
2
1
5
9
8
7
6
4
3
pF27
Mean
5.301E?02
5.242E?02
5.462E?02
7.132E?02
7.351E?02
5.422E?02
5.491E?02
4.501E102
5.142E?02
Std
(1.862E?01)
(2.751E-01)
(2.712E?01)
(6.622E?01)
(8.221E?01)
(1.721E?01)
(2.312E?01)
(7.123E?01)
(6.883E?00)
p-
rank
–
–
–
–
–
–
–
?
f-rank
7
3
5
8
9
4
7
1
2
pF28
Mean
4.701E?02
4.791E?02
4.731E?02
4.982E?02
4.911E?02
4.611E?02
4.842E?02
4.552E102
4.592E?02
Std
(2.213E?01)
(7.532E-04)
(2.381E?01)
(1.501E?01)
(1.901E?01)
(1.492E?01)
(2.051E?01)
(2.302E-01)
(1.133E?01)
p-
rank
–
–
–
–
–
–
–
?
f-rank
4
6
5
9
8
3
7
1
2
pF29
Mean
3.481E102
1.541E?03
4.841E?02
5.134E?02
1.643E?03
4.823E?02
4.714E?02
1.422E?03
5.5321E?02
Std
(1.031E?01)
(1.491E?02)
(1.021E?02)
(1.361E?02)
(2.261E?02)
(1.361E?01)
(8.051E?01)
(1.681E?02)
(3.381E?01)
p-
rank
?
–
–
–
–
–
–
–
f-rank
1
8
4
6
9
3
2
7
5
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27615

---

## Page 24
Table 2 (continued)
LSHADE
SACS
SHADE
SaDE
CV1.0
MVMO
JADE
CVnew
LSHADESPA
pF30
Mean
6.501E?05
1.111E105
6.811E?05
8.081E?05
4.631E?06
5.781E?05
6.671E?05
6.011E?05
6.131E?05
Std
(7.251E?04)
(4.101E?04)
(8.481E?04)
(8.301E?04)
(8.561E?06)
(1.011E?04)
(9.221E?04)
(2.961E?04)
(3.961E?04)
p-
rank
–
?
–
–
–
–
–
–
f-rank
6
1
8
9
2
3
7
4
5
w/l/t
13/14/2
5/24/0
4/24/1
0/29/0
1/28/0
5/24/0
4/25/0
8/21/0
NA
Overall f-rank value
83
144
128
200
227
124
174
139
77
f-rank
2
5
4
8
9
3
7
6
1
123
Neural Computing and Applications (2025) 37:27593–27630
27616
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 25
std for dimension size 10. For the problem, pr1, as well as LSHADESPA, LSO, NL-SHADE-RSP-MID algo-
rithms, shows the same outcomes in terms of mean and std. For problem, pr2, NL-SHADE-RSP-MID algorithms
show the superior performance. Also for the problem, pr3, LSHADESPA, DE, NL-SHADE-RSP-MID, as well as
LSO algoriths demonstrate the same performance in terms of mean and std, and it is difﬁcult to ﬁnd which
algorithm is best for this problem. EA4eig algorithm shows superior performance as compared to the other MH
algorithm for problems pr4, pr6, as well as pr9. Both algorithms (LSHADESPA and NL-SHADE-RSP-MID)
show the best outcomes for the problem pr5. For the problems pr7, pr10, as well as pr11, the LSHADESPA
algorithm shows superior performance in terms of mean and std. NL-SHADE-RSP-MID algorithm shows the
optimal result for the problem pr8. For the problem pr12, LSO as well as LSHADESPA algorithms show exactly
similar results in terms of mean value. Figure 8 shows the radarchart of LSHADESPA, DE, PSO, LSO, EA4eig,
MVMO, NL-SHADE- RSP-MID, and KOA for CEC 2022 numerical challenges.
Fig. 5 Radarchart of LSHADE, SACS, SHADE, SaDE, CV1.0, MVMO, JADE, CVnew, and LSHADESPA for CEC 2017
numerical challenges
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27617

---

## Page 26
Statistical testing After the simulation outcomes, to prove the statistical importance of the proposed LSHA-
DESPA algorithm, the rank-sum test is also performed. To validate the performance of the proposed LSHA-
DESPA, statistical tests, namely Wilcoxon’s rank-sum as well as Friedman rank (f-rank) test, are performed. This
test is nonparametric in nature and utilized to test the statistical signiﬁcance of the algorithm. First, the rank-sum
test determines if the proposed LSHADESPA algorithm is signiﬁcantly superior or not. LSHADESPA’s per-
formance is provided below in terms of win(w)/loss(i)/tie(t). The w condition happens if the algorithm under test
outperforms the proposed approach and are represented by the ‘‘?’’ sign. In the l condition, the test algorithm
performs worse than the LSHADESPA algorithm, as indicated by the ‘‘-’’sign. The ﬁnal t circumstance happens
when there is no statistical difference between the algorithms that are under test and is represented by the ’’=’’
symbol. The bold values in the table corresponds to the best results for that particular test problem. So, from the
w/l/t row presented in the third last row of Table 5 and Fig. 9, it can be observed that the proposed LSHADESPA
algorithm is signiﬁcantly good for most of the problems in comparison with MH other algorithms. Thus, from the
twelve problems, the EA4eig as well as NL-SHADE-RSP-MID is found to be best for four problem functions,
Fig. 6 Comparison of the
performance of the LSHA-
DESPA algorithm with
other algorithms for CEC
2017 (w/l/t scenario)
Fig. 7 Rankings of algo-
rithms for CEC 2017
123
Neural Computing and Applications (2025) 37:27593–27630
27618
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 27
Table 3 Statistical outcomes of LSHADESPA algorithm for CEC 2021 (D = 10)
Best
Worst
Median
Mean
Std
Basic
prt1
0
0
0
0
0
prt2
0
4.93E-01
1.21E-01
1.32E-01
9.69E-02
prt3
1.062E?01
1.042E?01
1.042E?01
1.052E?01
1.59E-15
prt4
2.43E-01
4.87E-01
3.64E-01
3.60E-01
6.21E-02
prt5
0
0
0
0
0
prt6
9.64E-05
2.97E-01
2.38E-02
1.03E-01
1.42E-01
prt7
1.24E-08
4.93E-01
7.03E-05
4.03E-02
1.26E-01
prt8
0
0
0
0
0
prt9
0
0
0
0
0
prt10
4.762E?01
4.742E?01
4.772E?01
4.772E?01
1.09E-02
Bias
prt1
0
0
0
0
0
prt2
0
3.11E-01
1.21E-01
1.47E-01
8.10E-02
prt3
1.0612E?01
1.002E?01
1.0612E?01
1.0612E?01
1.062E?01
prt4
2.36E-01
4.93E-01
3.35E-01
3.46E-01
7.04E-02
prt5
0
2.06E-01
0
1.37E-02
5.26E-02
prt6
1.70E-05
4.97E-01
1.97E-02
1.06E-01
1.64E-01
prt7
2.48E-07
6.68E-02
3.63E-05
3.55E-04
1.18E-03
prt8
0
0
0
0
0
prt9
0
0
0
0
0
prt10
4.772E?01
4.772E?01
4.772E?01
4.772E?01
1.08E-03
Shift
prt1
0
0
0
0
0
prt2
6.23E-02
4.97E-01
1.85E-01
2.10E-01
1.07E-01
prt3
1.062E?01
1.062E?01
1.062E?01
1.062E?01
1.52E-15
prt4
2.04E-01
5.45E-01
3.64E-01
3.55E-01
7.92E-02
prt5
0
1.162E?00
1.02E-01
4.762E?00
2.142E?01
prt6
4.71E-04
3.382E?00
3.15E-02
3.55E-01
3.00E-01
prt7
1.24E-05
1.162E?02
3.40E-04
7.952E?00
2.982E?00
prt8
1.002E?02
1.002E?02
1.002E?01
1.002E?02
2.61E-15
prt9
1.002E?02
3.252E?02
3.252E?01
3.072E?02
5.732E?01
prt10
3.982E?02
3.981E?02
3.981E?02
3.981E?02
2.09E-04
Rotation
prt1
0
0
0
0
0
prt2
2.47E-01
1.671E?01
3.641E?00
4.101E?00
4.291E?00
prt3
1.031E?01
1.281E?01
1.131E?01
1.141E?01
6.85E-01
prt4
3.00E-01
5.67E-01
4.04E-01
4.15E-01
7.43E-02
prt5
0
1.181E?00
2.06E-01
2.64E-01
3.36E-01
prt6
7.88E-03
1.171E?00
7.88E-04
2.52E-02
8.68E-02
prt7
2.04E-05
3.78E-01
7.88E-04
2.52E-02
8.68E-02
prt8
0
0
0
0
0
prt9
0
0
0
0
0
prt10
5.101E?01
7.151E?01
7.081E?01
6.751E?01
7.461E?00
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27619

---

## Page 28
and DE for two problems as compared to the proposed LSHADESPA algorithm. In addition to that, the Friedman
rank test is also utilized to validate the superior performance of the proposed LSHADESPA algorithm. In this test,
every algorithm provides a rank according to its performance, and also average f-rank is obtained from all the
Table 3 (continued)
Best
Worst
Median
Mean
Std
Bias & shift
prt1
0
0
0
0
0
prt2
0
3.10E-01
1.22E-01
1.50E-01
7.96E-02
prt3
1.061E?01
1.061E?01
1.061E?01
1.061E?01
5.71E-14
prt4
2.11E-01
5.25E-01
3.62E-01
3.58E-01
8.96E-02
prt5
0
1.161E?02
0
8.311E?00
3.001E?01
prt6
5.11E-06
4.95E-01
2.05E-02
1.03E-01
1.45E-02
prt7
3.58E-07
4.91E-01
1.58E-03
7.11E-02
1.41E-01
prt8
1.001E?02
1.001E?02
1.001E?02
1.001E?02
0
prt9
3.192E?02
3.252E?02
3.252E?01
3.252E?02
1.192E?00
prt10
4.002E?02
4.002E?02
4.002E?02
4.002E?02
0
Bias & rotation
prt1
0
0
0
0
0
prt2
1.85E-01
7.012E?00
3.552E?00
2.212E?00
1.882E?00
prt3
1.032E?01
1.242E?01
1.131E?01
1.132E?01
6.00E-01
prt4
1.94E-01
4.71E-01
3.55E-01
3.65E-01
7.43E-02
prt5
0
9.93E-01
2.06E-01
2.39E-01
2.25E-01
prt6
1.10E-01
1.342E?00
5.19E-01
5.87E-01
3.18E-01
prt7
2.10E-05
4.97E-01
2.00E-03
1.16E-01
1.79E-01
prt8
0
0
0
0
0
prt9
0
0
0
0
0
prt10
5.102E?01
7.102E?01
7.102E?01
6.682E?01
8.012E?00
Shift & rotation
prt1
0
0
0
0
0
prt2
3.10E-01
3.642E?01
5.352E?00
7.962E?00
8.092E?00
prt3
1.012E?01
1.252E?01
1.132E?01
1.122E?01
5.71E-01
prt4
2.22E-01
7.28E-01
3.96E-01
4.10E-01
1.06E-01
prt5
2.06E-01
1.552E?02
4.14E-01
1.302E?01
3.512E?01
prt6
2.13E-02
1.012E?00
2.31E-01
2.75E-01
2.55E-01
prt7
2.26E-05
6.62E-01
3.48E-03
1.07E-01
1.87E-01
prt8
1.002E?02
1.002E?02
1.002E?02
1.002E?02
2.63E-15
prt9
1.002E?02
3.302E?02
3.262E?01
3.112E?02
5.782E?01
prt10
3.952E?02
4.432E?02
4.182E?02
4.182E?02
2.302E?01
Bias, shift rotation
prt1
0
0
0
0
0
prt2
2.48E-01
2.833E?01
6.963E?01
9.443E?00
7.563E?00
prt3
1.013E?01
1.253E?01
1.123E?01
1.123E?01
5.35E-01
prt4
1.84E-01
5.57E-01
3.79E-01
3.79E-01
9.14E-02
prt5
0
3.883E?01
4.14E-01
3.253E?00
7.693E?00
prt6
2.68E-02
1.013E?00
2.44E-01
2.68E-01
2.04E-01
prt7
4.56E-06
6.18E-01
1.08E-03
8.19E-02
1.64E-01
prt8
1.003E?02
1.003E?02
1.001E?02
1.001E?02
0
prt9
1.001E?02
3.301E?02
3.281E?02
3.111E?02
5.781E?01
prt10
3.951E?02
4.411E?02
3.962E?02
4.152E?02
2.272E?01
123
Neural Computing and Applications (2025) 37:27593–27630
27620
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 29
Table 4 Statistical outcomes of LSHADESPA algorithm for CEC 2021 (D = 20)
Best
Worst
Mean
Median
Std
Basic
Fprt1
0
0
0
0
0
prt2
1.851E-01
1.902E?00
2.791E-01
3.362E?00
3.021E-01
prt3
2.002E?01
2.002E?01
2.002E?01
2.002E?01
1.061E-14
prt4
5.641E-01
1.301E?00
1.061E?00
1.031E?00
1.961E-01
prt5
0
2.061E-01
0
3.451E-02
6.861E-02
prt6
4.711E-01
6.481E-01
5.261E-01
5.281E-01
4.301E-02
prt7
6.431E-02
5.001E-01
4.971E-01
4.821E-E-01
7.911E-02
prt8
0
0
0
0
0
prt9
0
0
0
0
0
prt10
4.851E?01
4.861E?01
4.851E?01
4.851E?01
2.001E-02
Bias
prt1
0
0
0
0
0
prt2
1.541E-01
1.841E?00
2.791E-01
3.201E-01
2.961E-01
prt3
2.001E?01
2.001E?01
2.001E?01
2.001E?01
2.051E-14
prt4
7.462E-01
1.441E?00
1.011E?00
1.011E?00
1.712E-01
prt5
0
2.062E-01
0
1.712E-02
4.782E-02
prt6
4.912E-01
6.38-01
5.312E-01
5.352E-01
3.521E-02
prt7
8.861E-02
6.541E-01
4.961E-01
4.681E-01
9.951E-02
prt8
0
0
0
0
0
prt9
0
0
0
0
0
prt10
4.864E?01
4.864E?01
4.864E?01
4.854E?01
1.961E-02
Shift
prt1
0
1.004E?00
0
0
0
prt2
1.851E-01
7.784E?00
3.411E-01
1.164E?00
1.784E?00
prt3
2.004E?01
2.004E?01
2.004E?01
2.004E?01
1.013E-14
prt4
7.603E-01
1.234E?00
9.933E-E-01
1.004E?00
1.443E-01
prt5
0
1.164E?02
1.023E-01
1.284E?01
3.573E?01
prt6
4.502E-01
6.002E-01
4.972E-01
5.062E-01
2.842E-02
prt7
5.002E-03
1.163E?02
4.971E-01
1.593E?01
4.073E?01
prt8
1.003E?02
1.003E?02
1.003E?02
1.003E?02
0
prt9
3.923E?02
4.003E?02
3.973E?02
3.972E?02
1.482E?00
prt10
4.792E?02
4.832E?02
4.822E?02
4.822E?02
1.472E?00
Rotation
prt1
0
0
0
0
0
prt2
2.471E-01
9.371E?00
2.061E?00
2.791E?00
2.151E?00
prt3
2.051E?01
2.421E?01
3.341E?01
2.231E?01
9.641E-01
prt4
8.161E-01
1.461E?00
1.061E?00
1.091E?00
1.911E-01
prt5
1.592E?00
1.132E?01
4.832E?00
5.232E?00
2.412E?00
prt6
4.763E-01
3.382E?00
1.222E?00
1.492E?00
1.042E?00
prt7
7.493E-01
3.522E?00
1.602E?00
1.762E?00
7.302E-01
prt8
0
0
0
0
0
pr9
0
0
0
0
0
prt10
6.212E?01
6.232E?01
6.222E?01
6.222E?01
3.222E-02
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27621

---

## Page 30
problem displayed in Table 5. From Table 5 and Fig. 10, it can be observed that the LSHADESPA algorithm
obtained 1st rank followed by NL-SHADE-RSP-MID and the EA4eig algorithm.
The LSHADESPA algorithm is the most effective, achieving the highest rank in 41.67% of test instances and
exhibiting an efﬁciency of 81.95% compared to the optimal ranking. The NL-SHADE-RSP-MID follows closely,
winning 33.33% of the cases with a strong 76.39% average rank efﬁciency. DE and PSO also achieve a 33.33%
win rate, but their overall ranking efﬁciency is lower, with DE at 58.33% and PSO at 41.67%, indicating
Table 4 (continued)
Best
Worst
Mean
Median
Std
Bias & shift
prt1
0
0
0
0
0
prt2
1.541E-01
3.582E?00
3.572E?00
8.421E-01
9.012E-01
prt3
2.001E?01
2.001E?01
2.001E?01
2.001E?01
3.442E-14
prt4
6.061E-01
1.471E?00
1.041E?00
1.041E?00
2.211E-01
prt5
0
1.171E?02
1.022E-01
8.811E?00
3.001E?01
prt6
2.322E-01
6.021E-E-01
4.991E-01
4.993E-01
5.893E-02
prt7
1.093E-01
1.161E?02
4.973E-01
2.781E?01
5.071E?01
prt8
1.001E?02
1.001E?02
1.001E?02
1.001E?02
8.282E-14
prt9
3.921E?02
4.011E?02
4.001E?02
4.001E?02
1.303E?00
prt10
4.793E?02
4.833E?02
4.833E?02
4.823E?02
1.243E?00
Bias & rotation
prt1
0
0
0
0
0
prt2
2.162E-01
9.433E?00
2.033E?00
3.143E?00
2.401E?00
prt3
2.011E?01
2.511E?01
2.251E?01
2.262E?01
1.172E?00
prt4
6.662E-01
1.482E?00
1.022E?00
1.021E?00
1.832E-01
prt5
1.491E?00
9.201E?00
4.281E?00
4.401E?00
1.701E?00
prt6
4.762E-01
3.741E?00
1.011E?00
1.393E?00
1.003E?00
prt7
7.612E-01
3.163E?00
1.553E?00
1.633E?00
6.801E-01
prt8
0
0
0
0
0
prt9
0
0
0
0
0
prt10
6.213E?01
6.213E?01
6.223E?01
6.223E?01
2.301E-02
Shift & rotation
prt1
0
0
0
0
0
prt2
3.431E-01
3.403E?02
1.043E?01
3.602E?01
7.512E?01
prt3
2.022E?01
2.472E?01
2.232E?01
2.242E?01
1.082E?00
prt4
6.071E-01
1.332E?00
1.052E?00
1.022E?00
2.06-01
prt5
1.112E?01
1.512E?02
3.252E?01
6.551E?01
5.551E?01
prt6
5.151E-01
2.301E?00
1.491E?00
1.171E?00
6.071v01
prt7
1.921E?00
1.241E?02
4.921E?00
1.281E?01
3.001E?01
prt8
1.001E?02
1.001E?02
1.001E?02
1.001E?02
0
prt9
3.962E?02
4.012E?02
4.012E?02
4.012E?02
1.412E?00
prt10
4.102E?02
4.112E?02
4.112E?02
4.112E?02
6.162E-01
Bias, shift, rotation
prt1
1.002E?10
1.002E?10
1.002E?10
1.002E?10
0
prt2
1.813E?01
2.303E?02
6.913E?00
2.193E?01
4.973E?01
prt3
2.043E?01
2.453E?01
2.233E?01
2.233E?01
1.053E?00
prt4
7.17512E-01
1.533E?00
1.063E?00
1.083E?00
1.9612E-01
prt5
1.573E?01
2.503E?02
5.403E?01
8.603E?01
6.403E?01
prt6
5.3812E-01
2.041E?00
1.491E?00
1.171E?00
5.2011E-01
prt7
1.611E?00
1.211E?01
4.521E?00
4.521E?00
2.001E?00
prt8
1.001E?02
1.004E?02
1.004E?02
1.004E?02
1.121E-13
prt9
3.994E?02
4.034E?02
4.014E?02
4.014E?02
1.051E?00
prt10
4.101E?02
4.091E?02
4.111E?02
4.111E?02
8.171E-01
123
Neural Computing and Applications (2025) 37:27593–27630
27622
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 31
Table 5 Outcomes of LSHADESPA algorithm in comparison to other MH algorithms for CEC 2022 problems
Problem
LSHADESPA
DE [58]
PSO [58]
LSO [59]
EA4eig [51]
NL-SHADE-RSP-MID
[61]
KOA [48]
pr1
Mean
3.000E102
3.000E102
3.000E102
3.000E102
3.000E102
3.001E?02
3.00E?02
Std
0.000E100
0.000E100
2.585E-16
0.000E100
1.340E-09
0.000E100
1.06E-14
p-rank
¼
-
¼
-
¼
-
f-rank
1
1
5
1
7
1
6
pr2
Mean
4.062E?02
4.070E?02
4.235E?02
4.009E?02
4.014E?02
4.000E102
4.02E?02
Std
2.2424E?00
2.090E?00
3.033E?01
2.13E?00
1.953E?00
0.000E100
3.39E?00
p-rank
-
-
-
-
?
-
f-rank
6
5
7
2
3
1
4
pr3
Mean
6.000E102
6.000E102
6.003E?02
6.000E102
6.000E102
6.000E102
6.00E102
Std
0.000E100
0.000E100
6.140E-01
0.000E100
9.980E-10
0.000E100
6.33E-14
p-rank
¼
-
¼
-
=
-
f-rank
1
1
7
1
6
1
5
pr4
Mean
8.015E?02
8.167E?02
8.114E?02
8.107E?02
8.012E102
8.047E?02
8.044E?02
Std
7.498E-01
2.956E?00
5.123E?00
2.96E?00
1.042E?00
1.330E?00
1.62 E?00
p-rank
-
-
-
?
-
-
f-rank
2
7
6
5
1
4
3
pr5
Mean
9.000E102
9.000E102
9.001E?02
9.000E102
9.000E102
9.000E102
9.000E102
Std
0.000E100
1.055E-13
1.181E-01
8.29E-02
1.620E-09
0.000E100
2.00E-02
p-rank
-
-
-
-
¼
-
f-rank
1
3
7
6
4
1
5
pr6
Mean
1.800E103
1.800E103
5.308E?03
1.800E103
1.800E103
1.800E103
1.80E?03
Std
2.522E-01
1.428E-01
2.651E?03
3.400E-01
3.570E-02
1.270E-01
1.80E?03
p-rank
?
-
-
?
?
-
f-rank
4
3
7
5
1
2
6
pr7
Mean
2.000E103
2.001E?03
2.013E?03
2.000E103
2.000E103
2.000E103
2.000E103
Std
1.602E-11
3.668E?00
9.796E?00
5.400E-01
1.170E-E-09
0
1.100E-01
p-rank
-
-
-
-
-
-
f-rank
1
6
7
5
3
2
4
pr8
Mean
2.201E?03
2.200E103
2.227E?03
2.201E?03
2.200E103
2.200E103
2.20E?03
Std
4.741E?00
3.865E-01
3.930E?01
3.83E?00
6.810E-02
2.730E-01
6.20E?00
p-rank
?
-
-
?
?
-
f-rank
4
3
7
5
2
1
6
pr9
Mean
2.525E?03
2.529E?03
2.534E?03
2.529E?03
2.485E103
2.491E?03
2.529E?03
Std
3.214E?00
0.000E?00
1.202E?01
5.680v14
8.540E?01
6.350E-02
0.000E?00
p-rank
-
-
-
?
?
-
f-rank
3
4
7
6
1
2
6
pr10
Mean
2.500E103
2.542E?03
2.572E?03
2.500E?03
2.500E?03
2.600E?03
2.500E?03
Std
3.703E202
4.934E?01
9.683E?01
6.000E-01
3.600E-02
0.000E?00
4.000E-01
p-
rank-
-
-
-
-
-
-
f-rank
1
5
6
4
2
7
3
pr11
Mean
2.600E103
2.660E?03
2.763E?03
2.825E?03
2.600E103
2.862E?03
2.770E?03
Std
0.000E100
8.529E?01
1.178E?02
1.291E?02
1.060E-09
1.770E?00
151.20
p-rank
-
-
-
-
-
-
f-rank
1
3
4
6
2
7
5
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27623

---

## Page 32
Fig. 8 Radarchart of LSHADESPA, DE, PSO, LSO, EA4eig, MVMO, NL-SHADE- RSP-MID, and KOA for CEC 2022
numerical challenges
Table 5 (continued)
Problem
LSHADESPA
DE [58]
PSO [58]
LSO [59]
EA4eig [51]
NL-SHADE-RSP-MID
[61]
KOA [48]
pr12
Mean
2.862E103
2.954E?03
2.871E?03
2.862E103
2.847E?03
2.865E?03
2.864E?03
Std
2.970E?00
6.279E-02
1.292E?01
1.72E?00
3.901E?00
9.720E-01
1.16E?00
p-rank
-
-
=
-
-
-
f-rank
1
7
4
1
6
5
3
w/l/t
NA
2/8/2
0/12/0
0/9/3
4/8/0
4/5/3
0/12/0
Average
f-rank
2.166
4.000
6.166
3.916
3.167
2.833
4.667
Overall f-rank
1
5
7
4
3
2
6
123
Neural Computing and Applications (2025) 37:27593–27630
27624
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 33
inconsistency in performance. LSO maintains a moderate 25% win rate with a 67.37% ranking efﬁciency, while
EA4eig and KOA lag behind, winning only 16.67% of the cases, with ranking efﬁciencies of 73.61% and 61.11%,
respectively. Overall, LSHADESPA proves to be the most stable and high-performing algorithm, whereas PSO is
the weakest, showing the lowest ranking efﬁciency.
5 Discussion
This section is structured into three subsections. The ﬁrst subsection provides an overall summary of the work.
The second subsection focuses on the drawback of the LSHADESPA algorithm. Lastly, the third subsection
discusses potential future Insightful Implications. The details are presented below, subsection.
Fig. 9 Comparison of the
performance of the LSHA-
DESPA algorithm with
other algorithms for CEC
2022 (w/l/t scenario)
Fig. 10 Rankings of algo-
rithms for CEC 2022
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27625

---

## Page 34
5.1 Summary of results
The overall summary of the presented outcomes is given below:
•
In this paper, we introduced a new variant of the DE algorithm known as the LSHADESPA algorithm. By
incorporating the SP mechanism, SA scaling factor, and oscillating inertia weight for added exploration and
exploitation properties.
•
In the CEC 2014 benchmark challenges, which included uni-modal, multi-modal, and composition challenges,
the performance of the LSHADESPA algorithm outperformed that of the IMEHO, LX-BBO, PBIL, B-BBO,
VNBA, RW-GWO, ISOS, as well as CCS algorithms.
•
The proposed LSHADESPA algorithm has been evaluated using the CEC 2017 benchmark dataset. The
evaluation outcomes indicate that the LSHADESPA algorithm is superior to other MH algorithms such as
SaDE, JADE, SHADE, MVMO, CV1.0, CVnew, and SACS.
•
The outcomes obtained from the simulation for CEC 2021 are also presented in this paper. The LSHADESPA
algorithm provides outcomes that closely match the optimal solutions for the CEC 2021 test suite.
•
Additionally, the LSHADESPA algorithm has superior performance compared to the PSO, LSO, DE, EA4eig,
NL-SHADE-RSP-MID, and KOA algorithms, as observed in the comparison with CEC 2022 benchmarks.
•
The statistical signiﬁcance of the LSHADESPA algorithm has been evaluated utilizing Friedman and
Wilcoxon’s tests. These tests provide valuable insights into the algorithm’s performance and potential impact.
•
Overall, these results prove that the added enhancements make the algorithm perform better in terms of
exploration and exploitation and hence result in an improved search operation.
5.2 Drawbacks
•
Despite LSHADESPA’s high performance, it is not guaranteed to ﬁnd global optimum solutions for all
domain research problems due to its stochastic nature.
•
Due to the resizing of population and mutation characteristics, there is a possibility that the computational
complexity becomes O(logN). Although it becomes occasionally and is not a signiﬁcant factor, but when the
problem dimensions increase, the complexity also grows, and this component can become more signiﬁcant.
Thus, the complexity can play a major role and hence can be considered as a drawback for higher-dimensional
analysis.
•
In addition, LSHADESPA’s poor performance is shown in comparison outcomes on benchmark challenges.
The algorithm performed well on CEC 2014, CEC 2017, CEC 2021, and 2022, where the global optima were
quite different from the actual values obtained through the algorithm for some functions. It means that more
work is needed to develop an ideal algorithm that solves all optimization problems.
5.3 Insightful implications
•
The LSHADE algorithm can be included in the list of expert as well as hybrid intelligent systems due to its
simplicity and linear design.
•
In order to optimize algorithms for a wide range of real-world problems, it is essential to incorporate an
accurately calibrated equilibrium between exploration and exploitation.
•
Further investigation can be done to examine the algorithm’s effectiveness by comprehensively examining its
stability, convergence features, and other empirical studies. In addition to this, it is also possible to conduct
theoretical investigations to enhance knowledge of the indicated LSHADE algorithm.
123
Neural Computing and Applications (2025) 37:27593–27630
27626
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 35
•
The majority of research problems in the domain demonstrate a multi-objective nature. Therefore, it is
advantageous to explore algorithms that possess enhanced features, as they can be extended to accommodate
the multi-objective nature of these problems.
6 Conclusion
This study offers a new variant of LSHADE denoted by LSHADESPA algorithm that has been applied to CEC
2014, CEC 2017, CEC 2021 as well as CEC 2022 benchmark problems. The proposed algorithm is improved by
incorporating self-adaptive features such as SP adaptation to minimize computational burden, SA modiﬁcation to
adjust scaling factors to achieve superior exploration characteristics, as well as oscillating adaptation-oriented
crossover rate to ﬁnd a balanced exploration and exploitation operation. All these added properties are tested
using four benchmark datasets, namely CEC 2014, CEC 2017, CEC 2021, and CEC 2022. The algorithm is
compared to SaDE, JADE, LSHADE, SHADE, CmA-ES, MVMO, SACS, VNBA, and others, and it has been
found that LSHADESPA performs better. Further, Wilcoxon rank sum and Friedman test shows that the algo-
rithm is also better signiﬁcantly.
In the future, the LSHADESPA algorithm can be used for image thresholding, genome sequencing, clustering,
and other real-world applications. The algorithm can also be enhanced for better exploration and exploitation
properties for improved performance. Because of the better search properties of LSHADESPA, a binary and
constraint version can be introduced for discrete and other optimization problems.
Funding We gratefully acknowledge the funding support by program ‘‘Excellence initiative—research university’’ for the
AGH University of Krakow as well as the ARTIQ project: UMO-2021/01/2/ST6/00004 and ARTIQ/0004/2021.
Data availability The datasets used and/or analyzed during the current study are available from the corresponding author on
reasonable request.
Declarations
Conflict of interest The authors declare that there is no conflict of interest associated.
Open Access
This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Interna-
tional License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if you modiﬁed the licensed material. You do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party material in this article are included in the article’s
Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.
References
1. Lange K (2013) Optimization, vol 95. Springer, Cham
2. Chong EK, Lu W-S, _Zak SH (2023) An introduction to optimization. Wiley, New York
3. Dantzig GB (2002) Linear programming. Oper Res 50(1):42–47
4. Nocedal J, Wright SJ (2006) Quadratic programming. Numerical optimization. Springer, Cham, pp 448–492
5. Bertsekas DP (1997) Nonlinear programming. J Oper Res Soc 48(3):334–334
6. Wolsey LA (2020) Integer programming. Wiley, New York
7. Pre´kopa A (2013) Stochastic programming, vol 324. Springer, Cham
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27627

---

## Page 36
8. Lin S, Kernighan BW (1973) An effective heuristic algorithm for the traveling-salesman problem. Oper Res
21(2):498–516
9. Zahedi R, Shaghaghi A, Aslani A, Noorollahi Y, Astaraei FR, Eskandarpanah R (2023) Optimization of a hybrid
cooling, heating and power multigeneration system coupled with heat storage tank using a developed algorithm. J Therm
Anal Calorim 149:1–11
10. Shaghaghi A, Omidifar R, Zahedi R, Pourezzat A, Keshavarzzadeh M (2023) Proposing a new optimized forecasting
model for the failure rate of power distribution network thermal equipment for educational centers. Therm Sci Eng
6(2):2087
11. Zahedi R, Aslani A, Gitifar A, Farahani ON, YouseﬁH (2023) Application of artiﬁcial neural network in predicting
building’s energy consumption. In: 2023 8th international conference on technology and energy management (ICTEM),
IEEE, pp 1–5
12. Salgotra R, Sharma P, Raju S, Gandomi AH (2024) A contemporary systematic review on meta-heuristic optimization
algorithms with their matlab and python code reference. Arch Comput Methods Eng 31(3):1749–1822
13. Sharma P, Thangavel S, Raju S, Prusty BR et al (2022) Parameter estimation of solar PV using Ali Baba and forty
thieves optimization technique. Math Prob Eng 2022:5013146
14. Liang J, Ban X, Yu K, Qu B, Qiao K, Yue C, Chen K, Tan KC (2022) A survey on evolutionary constrained
multiobjective optimization. IEEE Trans Evol Comput 27(2):201–221
15. Sohail A (2023) Genetic algorithms in the ﬁelds of artiﬁcial intelligence and data sciences. Ann Data Sci
10(4):1007–1018
16. Hussien AG, Heidari AA, Ye X, Liang G, Chen H, Pan Z (2023) Boosting whale optimization with evolution strategy
and gaussian random walks: an image segmentation method. Eng Comput 39(3):1935–1979
17. Espejo PG, Ventura S, Herrera F (2009) A survey on the application of genetic programming to classiﬁcation. IEEE
Trans Syst Man Cybern Part C (Applications and Reviews) 40(2):121–144
18. Hauschild M, Pelikan M (2011) An introduction and survey of estimation of distribution algorithms. Swarm Evol
Comput 1(3):111–128
19. Neri F, Tirronen V (2010) Recent advances in differential evolution: a survey and experimental analysis. Artif Intell Rev
33:61–106
20. Das S, Suganthan PN (2010) Differential evolution: a survey of the state-of-the-art. IEEE Trans Evol Comput
15(1):4–31
21. Das S, Mullick SS, Suganthan PN (2016) Recent advances in differential evolution-an updated survey. Swarm Evol
Comput 27:1–30
22. Jebaraj L, Venkatesan C, Soubache I, Rajan CCA (2017) Application of differential evolution algorithm in static and
dynamic economic or emission dispatch problem: a review. Renew Sustain Energy Rev 77:1206–1220
23. Opara KR, Arabas J (2019) Differential evolution: a survey of theoretical analyses. Swarm Evol Comput 44:546–558
24. Javaid N (2019) Differential evolution: an updated survey. In: Complex, intelligent, and software intensive systems:
proceedings of the 12th international conference on complex, intelligent, and software intensive systems (CISIS-2018),
Springer, pp 681–691
25. Pant M, Zaheer H, Garcia-Hernandez L, Abraham A et al (2020) Differential evolution: a review of more than two
decades of research. Eng Appl Artif Intell 90:103479
26. Zhang J, Sanderson AC (2009) Jade: adaptive differential evolution with optional external archive. IEEE Trans Evol
Comput 13(5):945–958
27. Zhang R, Song S, Wu C (2013) A hybrid differential evolution algorithm for job shop scheduling problems with
expected total tardiness criterion. Appl Soft Comput 13(3):1448–1458
28. Fathy A, Aleem SHA, Rezk H (2021) A novel approach for PEM fuel cell parameter estimation using lSHADE-EpSin
optimization algorithm. Int J Energy Res 45(5):6922–6942
29. Awad NH, Ali MZ, Suganthan PN (2017) Ensemble sinusoidal differential covariance matrix adaptation with Euclidean
neighborhood for solving cec2017 benchmark problems. In: 2017 IEEE congress on evolutionary computation (CEC).
IEEE, pp 372–379
30. Hadi AA, Mohamed AW, Jambi KM (2021) Single-objective real-parameter optimization: enhanced lSHADE-
SPACMA algorithm. Heuristics for optimization and learning. Springer, Cham, pp 103–121
31. Teo J (2005) Differential evolution with self-adaptive populations. In: International conference on knowledge-based and
intelligent information and engineering systems, Springer, pp 1284–1290
32. Liu J, Lampinen J (2005) A fuzzy adaptive differential evolution algorithm. Soft Comput 9:448–462
33. Qin AK, Suganthan PN (2005) Self-adaptive differential evolution algorithm for numerical optimization. In: 2005 IEEE
congress on evolutionary computation, vol 2. IEEE, pp 1785–1791
34. Islam SM, Das S, Ghosh S, Roy S, Suganthan PN (2011) An adaptive differential evolution algorithm with novel
mutation and crossover strategies for global numerical optimization. IEEE Trans Syst Man Cybern Part B (Cybernetics)
42(2):482–500
35. Ghosh S, Das S, Roy S, Islam SM, Suganthan PN (2012) A differential covariance matrix adaptation evolutionary
algorithm for real parameter optimization. Inf Sci 182(1):199–219
123
Neural Computing and Applications (2025) 37:27593–27630
27628
https://doi.org/10.1007/s00521-025-11678-5

---

## Page 37
36. Rahnamayan S, Tizhoosh HR, Salama MM (2007) A novel population initialization method for accelerating evolu-
tionary algorithms. Comput Math Appl 53(10):1605–1614
37. Ozer AB (2010) Cide: chaotically initialized differential evolution. Expert Syst Appl 37(6):4632–4641
38. de Melo VV, Delbem ACB (2012) Investigating smart sampling as a population initialization method for differential
evolution in continuous problems. Inf Sci 193:36–53
39. Zhu W, Tang Y, Fang J-A, Zhang W (2013) Adaptive population tuning scheme for differential evolution. Inf Sci
223:164–191
40. Poikolainen I, Neri F, Carafﬁni F (2015) Cluster-based population initialization for differential evolution frameworks.
Inf Sci 297:216–235
41. Salgotra R, Mirjalili S, Gandomi AH (2022) Enhancing differential evolution algorithm: adaptation for CEC 2017 and
CEC 2021 test suites. In: 2022 9th international conference on soft computing & machine intelligence (ISCMI), IEEE,
pp 235–240
42. Liang JJ, Qu BY, Suganthan PN (2013) Problem deﬁnitions and evaluation criteria for the CEC 2014 special session and
competition on single objective real-parameter numerical optimization. Comput Intell Lab Zhengzhou Univ Zhengzhou
China Tech Rep Nanyang Technol Univ Singap 635(2):2014
43. Wu G, Mallipeddi R, Suganthan PN (2017) Problem deﬁnitions and evaluation criteria for the CEC 2017 competition on
constrained real-parameter optimization. Natl Univ Def Technol Changsha Hunan PR China Kyungpook Natl Univ
Daegu South Korea Nanyang Technol Univ Singap 9:2017
44. Premkumar M, Jangir P, Kumar BS, Sowmya R, Alhelou HH, Abualigah L, Yildiz AR, Mirjalili S (2021) A new
arithmetic optimization algorithm for solving real-world multiobjective CEC-2021 constrained optimization problems:
diversity analysis and validations. IEEE Access 9:84263–84295
45. Kumar A, Price KV, Mohamed AW, Hadi AA, Suganthan PN (2021) Problem deﬁnitions and evaluation criteria for the
CEC 2022; special session and competition on single objective bound onstrained numerical optimization. Tech Rep
635:2014
46. Garg V, Deep K (2016) Performance of Laplacian biogeography-based optimization algorithm on CEC 2014 continuous
optimization benchmarks and camera calibration problem. Swarm Evol Comput 27:132–144
47. Li W, Wang G-G, Alavi AH (2020) Learning-based elephant herding optimization algorithm for solving numerical
optimization problems. Knowl Based Syst 195:105675
48. Abdel-Basset M, Mohamed R, Azeem SAA, Jameel M, Abouhawwash M (2023) Kepler optimization algorithm: a new
metaheuristic algorithm inspired by Kepler’s laws of planetary motion. Knowl Based Syst 268:110454
49. Tejani GG, Savsani VJ, Patel VK, Mirjalili S (2018) Truss optimization with natural frequency bounds using improved
symbiotic organisms search. Knowl Based Syst 143:162–178
50. Qin AK, Huang VL, Suganthan PN (2008) Differential evolution algorithm with strategy adaptation for global
numerical optimization. IEEE Trans Evol Comput 13(2):398–417
51. Bujok P, Kolenovsky P (2022) Eigen crossover in cooperative model of evolutionary algorithms applied to CEC 2022
single objective numerical optimization. In: 2022 IEEE congress on evolutionary computation (CEC), IEEE, pp 1–8
52. Tanabe R, Fukunaga A (2013) Success-history based parameter adaptation for differential evolution. In: 2013 IEEE
congress on evolutionary computation, IEEE, pp 71–78
53. Tanabe R, Fukunaga AS (2014) Improving the search performance of shade using linear population size reduction. In:
2014 IEEE congress on evolutionary computation (CEC). IEEE, pp 1658–1665
54. Erlich I, Rueda JL, Wildenhues S, Shewarega F (2014) Evaluating the mean-variance mapping optimization on the
IEEE-CEC 2014 test suite. In: 2014 IEEE congress on evolutionary computation (CEC). IEEE, pp 1625–1632
55. Salgotra R, Singh U, Saha S (2018) New cuckoo search algorithms with enhanced exploration and exploitation
properties. Expert Syst Appl 95:384–420
56. Salgotra R, Singh U, Saha S (2018) Improved cuckoo search with better search capabilities for solving CEC 2017
benchmark problems. In: 2018 IEEE congress on evolutionary computation (CEC). IEEE, pp 1–7
57. Gupta S, Deep K (2019) A novel random walk grey wolf optimizer. Swarm Evol Comput 44:101–112
58. Abdel-Basset M, El-Shahat D, Jameel M, Abouhawwash M (2023) Young’s double-slit experiment optimizer: a novel
metaheuristic optimization algorithm for global and constraint optimization problems. Comput Methods Appl Mech Eng
403:115652
59. Abdel-Basset M, Mohamed R, Sallam KM, Chakrabortty RK (2022) Light spectrum optimizer: a novel physics-inspired
metaheuristic optimization algorithm. Mathematics 10(19):3466
60. Shaghaghi A, Zahedi R, Ghorbani M, Ranjbar Z, Arzhangi SS, Keshavarzzadeh M, Alipour H (2024) State estimation
for distribution power systems by applying an advanced optimization approach. Expert Syst Appl 240:122325
61. Biedrzycki R, Arabas J, Warchulski E (2022) A version of NL-shade-RSP algorithm with midpoint for CEC 2022 single
objective bound constrained problems. In: 2022 IEEE congress on evolutionary computation (CEC). IEEE, pp 1–8
62. Derrac J, Garcı´a S, Molina D, Herrera F (2011) A practical tutorial on the use of nonparametric statistical tests as a
methodology for comparing evolutionary and swarm intelligence algorithms. Swarm Evol Comput 1(1):3–18
63. Bakır H (2024) Enhanced artiﬁcial hummingbird algorithm for global optimization and engineering design problems.
Adv Eng Softw 194:103671
Neural Computing and Applications (2025) 37:27593–27630
123
https://doi.org/10.1007/s00521-025-11678-5
27629

---

## Page 38
64. Salgotra R, Sharma P, Raju S (2024) A multi-hybrid algorithm with shrinking population adaptation for constraint
engineering design problems. Comput Methods Appl Mech Eng 421:116781
65. Sharma P, Raju S (2023) Metaheuristic optimization algorithms: a comprehensive overview and classiﬁcation of
benchmark test functions. Soft Comput 28:1–64
66. Wolpert DH, Macready WG (1997) No free lunch theorems for optimization. IEEE Trans Evol Comput 1(1):67–82
67. Hallam JW, Akman O, Akman F (2010) Genetic algorithms with shrinking population size. Comput Stat 25:691–705
68. Bansal JC, Singh P, Saraswat M, Verma A, Jadon SS, Abraham A (2011) Inertia weight strategies in particle swarm
optimization. In: 2011 Third world congress on nature and biologically inspired computing. IEEE, pp 633–640
69. Sharma P, Raju S, Salgotra R (2024) An evolutionary multi-algorithm based framework for the parametric estimation of
proton exchange membrane fuel cell. Knowl Based Syst 283:111134
70. Salgotra R, Singh U, Saha S, Nagar A (2019) New improved SALSHADE-cnEpSin algorithm with adaptive parameters.
In: 2019 IEEE congress on evolutionary computation (CEC). IEEE, pp 3150–3156
71. Mohamed A, Hadi A, Mohamed A, Agrawal P, Kumar A, Suganthan P (2020) Problem deﬁnitions and evaluation
criteria for the CEC 2021 special session and competition on single objective bound constrained numerical optimization.
Technical Report
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.
Authors and Afﬁliations
Rohit Salgotra1
• Pankaj Sharma5 • Krishanu Kundu3 • Saravanakumar Raju2 •
Amir H. Gandomi4
& Rohit Salgotra
rohits@agh.edu.pl
1
Faculty of Physics and Applied Computer Science / Centre of Excellence in Artiﬁcial Intelligence, AGH
University of Krakow, 30-059 Krakow, Poland
2
School of Electrical Engineering, Vellore Institute of Technology, Vellore, Tamil Nadu, India
3
Department of Electronics and Communication Engineering, G.L. Bajaj Institute of Technology and
Management, Greater Noida, India
4
Present Address: Faculty of Engineering and Information Technology, University of Technology Sydney,
Sydney, NSW 2007, Australia
5
Department of Electrical Engineering, National Institute of Technology, Andhra Pradesh, Tadepalligudem,
India
123
Neural Computing and Applications (2025) 37:27593–27630
27630
https://doi.org/10.1007/s00521-025-11678-5

---
