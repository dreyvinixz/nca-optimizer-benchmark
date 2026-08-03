# Modified Archimedes optimization algorithm for global optimization problems: a comparative study

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-09497-1

---

## Page 1
ORIGINAL ARTICLE
Modified Archimedes optimization algorithm for global optimization
problems: a comparative study
Mustafa Nurmuhammed1
• Ozan Akdag˘ 2
• Teoman Karadag˘ 3
Received: 9 April 2023 / Accepted: 14 January 2024 / Published online: 26 February 2024
 The Author(s) 2024
Abstract
Archimedes Optimization Algorithm (AOA) is a recent optimization algorithm inspired by Archimedes’ Principle. In this
study, a Modiﬁed Archimedes Optimization Algorithm (MDAOA) is proposed. The goal of the modiﬁcation is to avoid
early convergence and improve balance between exploration and exploitation. Modiﬁcation is implemented by a two phase
mechanism: optimizing the candidate positions of objects using the dimension learning-based (DL) strategy and recal-
culating predetermined ﬁve parameters used in the original AOA. DL strategy along with problem speciﬁc parameters lead
to improvements in the balance between exploration and exploitation. The performance of the proposed MDAOA algo-
rithm is tested on 13 standard benchmark functions, 29 CEC 2017 benchmark functions, optimal placement of electric
vehicle charging stations (EVCSs) on the IEEE-33 distribution system, and ﬁve real-life engineering problems. In addition,
results of the proposed modiﬁed algorithm are compared with modern and competitive algorithms such as Honey Badger
Algorithm, Sine Cosine Algorithm, Butterﬂy Optimization Algorithm, Particle Swarm Optimization Butterﬂy Optimization
Algorithm, Golden Jackal Optimization, Whale Optimization Algorithm, Ant Lion Optimizer, Salp Swarm Algorithm,
and Atomic Orbital Search. Experimental results suggest that MDAOA outperforms other algorithms in the majority of the
cases with consistently low standard deviation values. MDAOA returned best results in all of 13 standard benchmarks, 26
of 29 CEC 2017 benchmarks (89.65%), optimal placement of EVCSs problem and all of ﬁve real-life engineering
problems. Overall success rate is 45 out of 48 problems (93.75%). Results are statistically analyzed by Friedman test with
Wilcoxon rank-sum as post hoc test for pairwise comparisons.
Keywords Benchmark functions  Modiﬁed optimization algorithms  Optimization algorithms  Swarm intelligence
1 Introduction
Optimization algorithms are used in many ﬁelds involving
engineering problems. In recent years, the concepts of
efﬁciency and speed have become even more important for
applications that are important in terms of both transaction
and time cost, such as data mining or image processing.
Complex problems with higher dimensions, more variables
and constraints have emerged. Different solution approa-
ches are followed in line with the needs of the speciﬁc
applications. Solving engineering problems using tradi-
tional numerical solving techniques is inefﬁcient and time
consuming. In cases where it is not possible to calculate the
solution set analytically within an acceptable timeframe,
metaheuristic optimization algorithms come into play.
These algorithms do not guarantee the best results, but they
produce near-best solutions in a reasonable amount of time.
Especially in the 90 s, the articles published in this ﬁeld
have pioneered many publications and hundreds of opti-
mization algorithms today. Genetic Algorithm (GA), Par-
ticle Swarm Optimization (PSO), and Tabu Search are
among the most well-known algorithms [1–3]. Many
studies have been carried out in this area and have been
grouped according to the areas inspired by the algorithm.
They are classiﬁed as evolutionary, physics-based, swarm-
& Mustafa Nurmuhammed
mustafa.nurmuhammed@inonu.edu.tr
1
Department of Electric and Energy, Malatya OIZ Vocational
School, Inonu University Malatya, Malatya, Turkey
2
Department of Computer Engineering, Malatya Turgut O¨ zal
University, Malatya, Turkey
3
Department of Electrical and Electronics Engineering, Inonu
University, Malatya, Turkey
123
Neural Computing and Applications (2024) 36:8007–8038
https://doi.org/10.1007/s00521-024-09497-1
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
based and human-based algorithms [4]. Evolutionary
algorithms are inspired by the phenomenon of evolution.
The better candidate solutions are grouped together in
order to form the next generation of possible solutions.
Consequently, new generation solution sets provide more
accurate results than older ones. Genetic algorithm is a
well-known optimization algorithm falling under this cat-
egory. Genetic algorithm includes genetic items and events
such as chromosomes, crossover, and mutation. Physics-
based algorithms are inspired by the physic rules such as
AOA [5] that is developed simulating the Archimedes’
Principle. Human-based algorithms are inspired by human
behaviors. Mother Optimization Algorithm (MOA) is an
algorithm based on the interaction of a mother with her
children [6]. Swarm-based algorithms are inspired by the
biologic and social behavior of various animals in order to
solve complex problems. These algorithms mimic a swarm
based animals’ prey searching or mating behavior in a
computational optimization method. PSO, Salp Swarm
Algorithm (SSA), and Whale Optimization Algorithm
(WOA) are examples of swarm based algorithms [4, 7].
In
the
last
decade,
optimization
algorithms
have
improved and new algorithms are proposed providing
intuitive solution approaches and better resolutions to
problems. For instance, Honey Badger Algorithm (HBA) is
a population-based optimizer which is inspired by behavior
of honey badger [8]. Sine Cosine Algorithm (SCA) tries to
ﬁnd the best solution using sine and cosine functions [9]. In
study [10] Butterﬂy Optimization Algorithm (BOA) is
introduced. This algorithm mimics the mating and food
searching behavior of butterﬂies. In study [11] a nature-
inspired optimization is proposed called Golden Jackal
Optimization (GJO). GJO is particularly driven by the
collective hunting habits of golden jackals which are
mainly searching, surrounding and capturing the prey.
Whale Optimization Algorithm (WOA) is another swarm-
based metaheuristic algorithm [4]. WOA is developed with
inspiration from the hunting method of whales. Fennec Fox
Optimization (FFA), is inspired by digging and escape
behavior of fennec fox [12]. In [13] Mutated Leader
Algorithm (MLA) is proposed where initial random solu-
tions are updated by a mutated leader. Two-stage Opti-
mization (TSO) is an algorithm that updates population
members based on the good members of the population
[14]. Activities such as random walks are used in the
algorithm to provide diversity in population. Salp Swarm
Algorithm (SSA) is a swarm-based algorithm proposed in
[7]. It is inspired by navigation and hunting behaviors of
salps. Atomic Orbital Search (AOS) is a physics-based
algorithm utilizing laws of quantum-based atomic theory
[15].
According to a theorem, (no free lunch—NFL), a
speciﬁc optimization algorithm cannot provide best results
over a range of problems [16]. Therefore, in recent years,
numerous new optimization algorithms are published and
hybrid or modiﬁed algorithms are proposed to obtain better
results. There are many studies on providing a hybrid
solution to problems. For instance PSO is used along with
Seeker Optimization Algorithm (SOA) to develop a new
hybrid algorithm called SOAPSO [17]. It is tested on
various benchmark functions. In literature [18] a hybrid
optimization algorithm is formed with WOA and Modiﬁed
Differential Evolution (MDE). Study aims to improve areas
of the local optimum, population diversity, and early con-
vergence of WOA. Another hybrid algorithm is HPSOBOA
which combines PSO with BOA [19]. It uses both algo-
rithms in order to obtain superior results.
In research [20] authors introduce a new approach using
trigonometric operators to improve the exploitation phase
of the original AOA method. Sine and cosine functions are
used to avoid local optima. In studies [21, 22] TLBO is
modiﬁed to improve solutions and accelerate convergence
speed. In the ﬁrst study, modiﬁcation is done by altering
updating mechanism of a single solution. In the second
study, population individuals group mechanisms are pre-
sented into phases. Moreover, in another study, Harris
Hawks Optimization Algorithm (HHO) is modiﬁed [23]. In
the modiﬁed version, various update strategies are intro-
duced. In study [24] Moth Flame Optimization (MFO)
algorithm is modiﬁed to avoid cases of local optima and
early convergence. Modiﬁcation is done by utilizing a
modiﬁed dynamic opposite learning (DOL) strategy which
aims to ﬁnd a better solution by determining a quasi-op-
posite number. A modiﬁed version of BOA is proposed in
[25]. Algorithm parameters such as the switching proba-
bility, power of exponent (a), stimulus intensity (I), and
sensor modality (c) are modiﬁed in search of better
working efﬁciency of BOA. The Arithmetic Optimization
Algorithm is a recently proposed study inspired by the
arithmetic operators. This algorithm is modiﬁed by incor-
porating an operator for opposition-based learning (OBL)
and a constant parameter [26]. Similarly, in studies
[27–34], algorithms are hybridized or improved in order to
obtain better results for various ﬁelds of studies such as
optimal power ﬂow, mobile robot path planning, and cen-
trifugal pump optimization.
The modiﬁcation process can be carried out by adjusting
the coefﬁcients in the algorithm or by changing the parts of
the structure of an algorithm. Modiﬁcation is focused on
obtaining better results while considering the performance
of the algorithm. Although there are many studies on the
improvement of optimization algorithms, problem-oriented
improvements are anticipated to be achievable. Studies
have been carried out on modifying the algorithm around a
speciﬁc problem and relatively better results are obtained
[35–38].
8008
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 3
This study aims to increase the performance of AOA in
a wide range of problems. AOA features simplicity, scal-
ability, and few control options. In addition, it has been
evaluated on complex test functions and better results have
been achieved when compared to other algorithms in the
study [5]. Furthermore, it has an efﬁcient and robust
structure with regard to exploration and exploitation bal-
ance. At the exploration stage of the search, new solutions
are searched in the unknown areas. At the exploitation
stage, algorithms search solutions already found in the
neighborhood. This way ﬁtness value improves and more
accurate solutions are acquired. The balance between the
two stages signiﬁcantly improves the success of the
algorithm.
Therefore, to further increase the effectiveness of AOA,
part of the algorithm and parameters were modiﬁed to
calculate the problem-speciﬁc coefﬁcients. The candidate
positions of objects are optimized using the DL strategy
given in [39, 40]. In addition, another metaheuristic algo-
rithm, HBA, was used to calculate the coefﬁcients. In other
words, optimization algorithm is optimized by another
algorithm.
A summary of contributions of this study is:
•
MDAOA, a modiﬁed version of AOA, is developed
which provides better results on a wide range of
problem functions.
•
Modiﬁcation is applied with a two-step process:
optimizing the candidate positions of objects using the
dimension learning-based strategy and modifying pre-
determined ﬁve parameters used in the original AOA.
Parameters are optimized with a different optimization
algorithm, namely HBA, in order to solve a speciﬁc
engineering problem.
•
Avoiding early convergence and improving balance
between exploration and exploitation phases of AOA
are accomplished.
•
The proposed modiﬁed algorithm, MDAOA, is tested
on four groups of problem functions: standard bench-
mark functions, CEC 2017 test suite, engineering
problems, and optimal placement of EVCSs on IEEE-
33 distribution system. Results indicate that the Mod-
iﬁed AOA (MDAOA) algorithm can produce better
results than other well-known algorithms by calculating
the problem-speciﬁc parameters.
The rest of the paper is organized as: Sect. 2 presents
AOA before applying modiﬁcation steps, and HBA which
is used in the modiﬁcation process. Section 3 describes the
modiﬁcation of AOA. In Sect. 4, the simulation results are
presented in detail. The conclusion based on the results is
presented in Sect. 5.
2 Optimization algorithms
2.1 Archimedes optimization algorithm
AOA is an optimization algorithm inspired by the Archi-
medes’ Principle [5]. An object is immersed in a liquid and
pushed up by a buoyancy force. This force is equivalent to
the mass of the displaced liquid. According to this
approach, every object immersed in the liquid tries to be at
the equilibrium state. In this state, the buoyant force and
the weight of the object are equal. This condition is given
in Eq. 1. Equations 1–13 are taken from the reference [5].
Fb ¼ wo; pbvbab ¼ povoao
ð1Þ
where v is the volume, p is the density, b indicates ﬂuid, o
indicates immersed object, and a is the acceleration. The
speed in the liquid is determined by the volume and weight
of the objects.
In AOA, submerged objects generate a population. Ini-
tial search is performed with random values which is a
common practice in most optimization algorithms. For
every iteration, the values of density and volume are
updated until the algorithm’s ending criteria are fulﬁlled.
Steps implemented in AOA can be listed as:
Step 1 Values of the objects are randomly assigned as in
Eq. 2.
Oi ¼ lbi  rand  ubi  lbi
ð
Þ
i ¼ 1; 2; . . .; N
ð2Þ
where N is population, Oi is the ith object in N, lbi is the
lower bound and ubi is the upper bound. Volume (vol) and
density (den) values are randomly initialized as in Eq. 3.
Acceleration (acci) is initialized in Eq. 4 [5].
deni ¼ rand; voli ¼ rand
ð3Þ
acci ¼ lbi þ rand  ubi  lbi
ð
Þ
ð4Þ
Step 2 Density and volume are updated by Eq. 5.
dentþ1
i
¼ dent
i þ rand  denbest  dent
i


; voltþ1
i
¼ voltþ1
i
þ rand  volbest  volt
i


ð5Þ
where volbest and denbest are the best volume and density
values.
Step 3 The transfer operator (TF) is increased, on the
other hand, the density factor is decreased. This enables the
changeover
between
phases
(exploration–exploitation)
with equilibrium state after the collisions. This is accom-
plished by the Eq. 6.
TF ¼ exp t  tmax
tmax


ð6Þ
where t indicates the iteration number. tmax is the maximum
number
of
iterations.
Density
decreasing
factor
(d)
decreases over time using Eq. 7:
Neural Computing and Applications (2024) 36:8007–8038
8009
123

---

## Page 4
dtþ1 ¼ exp tmax  t
tmax



t
tmax


ð7Þ
Step 4 Exploration phase: In this step, collisions occur
according to the TF value. Object’s acceleration (acci) is
updated by Eq. 8.
acctþ1
i
¼ denmr þ volmr  accmr
dentþ1
i
 voltþ1
i
ð8Þ
where deni stands for density and voli is volume. acci
indicates acceleration of object i, mr indicates values of
random material.
Step 5 Exploitation phase: Depending on the TF value,
the collision does not take place. In this case, object’s
acceleration is updated by Eq. 9.
acctþ1
i
¼ denbest þ volbest  accbest
dentþ1
i
 voltþ1
i
ð9Þ
where accbest is the best acceleration value.
Step 6 Normalize acceleration step: In this step, accel-
eration is excessive in circumstances where the solution is
far from the global minimum and decreases over time in
other cases. Therefore, acctþ1
i;norm adjusts the change of step
size for each object. For this, Eq. 10 is used.
acctþ1
inorm ¼ u 
acctþ1
i
 min acc
ð
Þ
max acc
ð
Þ  min acc
ð
Þ þ l
ð10Þ
where u and l are the upper and lower values.
Step 7 Update step. In this step, positions are updated.
If TF less than or equal to 0.5 (exploration phase) Eq. 11
is used.
xtþ1
i
¼ xt
i þ C1  rand  acctþ1
inorm  d  xrand  xt
i


ð11Þ
where C1 is equal to 2. If TF is greater than 0.5,
exploitation phase is executed. Object positions are upda-
ted using Eq. 12.
xtþ1
i
¼ xt
best þ F  C2  rand  acctþ1
inorm  d
 T  xbest  xt
i


ð12Þ
where C2 = 6. T = C3 9 TF. The value of T increases with
time in the range of [C3 9 0.3, 1]. F indicates the ﬂag
parameter used for altering the direction Eq. 13:
F ¼
þ1
if P  0:5
1
if P [ 0:5

ð13Þ
where P ¼ 2  rand  C4.
Step 8 Evaluation step. In this step, the ﬁtness function is
evaluated. If a better result is found, it is remembered.
2.2 Honey Badger algorithm
Five constant values in AOA are optimized using HBA. It
is a well performing algorithm tested on standard bench-
mark functions, engineering problems, and CEC 2017
benchmark functions. Results indicate that it can be
effective in solving complex problems. In addition, HBA
performs well in terms of balance of exploration and
exploitation phases as well as convergence speed. As a
result, HBA is employed in order to ﬁnd the constant
parameters of AOA.
HBA was inspired by the foraging behavior of the honey
badger [8]. Food source or prey is located in two ways:
smelling and digging or by following a bird that guides the
honey badger to a source of honey. The ﬁrst phase is
digging where the prey’s rough location is established
through smelling. Next, an appropriate location is selected
for digging. The second phase is honey mode. In this phase,
the honey guide bird is tracked in order to locate the source
of honey. The pseudo code of HBA applied in the study is
given in Algorithm 1 [8].
8010
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 5
Algorithm 1 The pseudo code of HBA applied in the study
The system parameters are speciﬁed, and the initial
positions are randomly determined. The population of
honey badgers are represented in the matrix below [8].
Candidate solutions ¼
x11
x12
  
x1d
...
...
...
...
xn1
xn2
  
xnd
2
64
3
75
ith position of honey badger xi ¼
x1
i ; x2
i ;
  
xd
i


Fitness evaluation results are stored in the matrix using
Eq. 14. Equations 14–19 are obtained from reference [8]. ri
is a random number between 0 and 1 where i = 1,..,n, and
n = 7.
xi ¼ lbi þ r1  ubi  lbi
ð
Þ
ð14Þ
where N is population, xi is the ith honey badger position.
The ﬁtness function is calculated for each honey badger.
The best position of xprey is remembered and ﬁtness value
is assigned to fprey. Afterward, Ii, the smell intensity, is
calculated using Eq. (15).
Ii ¼ r2 
S
4pd2
i
S ¼ xi  xiþ1
ð
Þ2
ð15Þ
di ¼ xprey  x
Decreasing factor (a) is updated using Eq. (16).
a ¼ C  exp
t
tmax


ð16Þ
The positions of the xnew are updated by either Eq. 17 or
Eq. 19 depending on a random number.
xnew ¼ xprey þ Fxb  I  xprey þ F  r3  a  di
 cos 2pr4
ð
Þ  1  cos 2pr5
ð
Þ
½

j
j
ð17Þ
F is the ﬂag which changes direction. Its value is
determined by Eq. 18.
F ¼
1
if r6  0:5
1
else

ð18Þ
Honey phase is the second part of Step 5. Equation 19
simulates the condition where the honey guide bird is
followed to ﬁnd honey.
xnew ¼ xprey þ F  r7  a  di
ð19Þ
where xnew is the updated position of honey badger. x prey
indicates the location of food/prey.
Updated positions are evaluated and assigned to fnew.
The steps are repeated until the ending criteria are met.
3 Modifying Archimedes optimization
algorithm
In [5], AOA is compared with recent and state-of-the-art
optimization algorithms. AOA can provide very good
solutions to the standard, real-world engineering as well as
CEC benchmark functions. However, carefully analyzing
and testing through benchmark functions, it has been
observed that population diversity can be increased leading
to an improved balance between exploitation and explo-
ration and more precise set of solutions. In order to achieve
modiﬁcation, two stages are applied: optimizing the can-
didate positions of objects using the dimension learning-
Neural Computing and Applications (2024) 36:8007–8038
8011
123

---

## Page 6
based strategy and predetermined ﬁve parameters used in
the original AOA with a different optimization algorithm,
namely HBA, in order to solve a speciﬁc engineering
problem.
3.1 Stage 1: applying dimension learning-based
steps
In this stage, each iteration has two strategies to update the
object’s position to a better position: DL strategy and
standard AOA search strategies similar to the work in [35].
In original AOA, Steps 4 through 7 given in Sect. 2 are
used for balancing exploration and exploitation phases. By
applying this stage to the AOA, balance of exploration and
exploitation is improved.
The DL strategy uses a distinctive methodology to
establish neighborhood for each object. According to this
approach, neighborhood data can be conveyed among
objects. DL strategy consists of four phases.
3.1.1 Initiation step
N is the population of objects. They are distributed ran-
domly by Eq. 20.
Xij ¼ lj þ frndj 0; 1
½
  uj  lj


; i 2 1; . . .; N
½
; j
2 1; . . .; D
½

ð20Þ
where D is dimension. Xi(t) represents the position of ith
immersed
object
for
iteration
t. frnd indicates
F
distribution.
3.1.2 Movement/transfer step
In dimension learning strategy, objects are relocated by
surrounding objects in order to be a new location candidate
for Xi(t).
Objects’ new position dimensions are computed by
Eq. 23. First, radius between the current and candidate
positions are computed by Eq. 21. [39, 40].
Radi tð Þ ¼ xi tð Þ  xiAOA t þ 1
ð
Þ
k
k
ð21Þ
Afterward, object’s neighbors are computed by Eq. 22.
Ni tð Þ ¼ fXj tð ÞjDi Xi tð Þ; Xj tð Þ


 Radi tð Þ; Xj tð Þ
2 populationg
ð22Þ
where Ni(t) is matrix containing the neighbors of Xi(t).
3.1.3 Selecting/and updating step
Neighbor relocating is performed by Eq. 23
XiDL;d t þ 1
ð
Þ ¼ Xi;d tð Þ þ frndx Xn;d tð Þ  Xr;d tð Þ


ð23Þ
where Xn;d tð Þ is a random neighbor 2 Ni tð Þ. Xr;d tð Þ is a
random object selected population.
The ﬁtness values of Xi-AOA(t ? 1) and Xi-DL,d(t ? 1)
are compared. The former and latter locations are com-
pared and updated with Eq. 24. [40].
Xi t þ 1
ð
Þ ¼
XiAOA t þ 1
ð
Þ;
if fobject XiAOA
ð
Þ\fobject XiDL
ð
Þ
XiDL t þ 1
ð
Þ
otherwise

ð24Þ
3.1.4 Termination step
This process is repeated for all iterations.
3.2 Stage 2: updating parameters
In this stage, the C3, C4 values in the AOA algorithm take
different values for the use of CEC 2017 and Engineering
problems and Standard Optimization Functions. In the
AOA
article,
sensitivity
analysis
was
performed
by
selecting three CEC 2017 test functions. Partial cost
function values obtained by changing the constant param-
eters are given in Table 1.
It is stated in AOA article that different values could be
tried depending on the difﬁculty and landscape of the
problem
[5].
Implementing
algorithms
with
default
parameters may perform
well,
however, ﬁne tuning
parameters for a speciﬁc problem returns better solutions.
For example, in [35] the structure of AOA is modiﬁed for
solving the optimal power ﬂow problem on three different
power systems. Results of implementing the modiﬁed
algorithm show effectiveness obtained by the modiﬁcation.
Therefore, one or more parameters of an algorithm or part
of its structure can be modiﬁed in order to increase effec-
tiveness of outcome. These parameters could be optimized
by another optimization algorithm. This may result in a
high amount of computational cost because the search
domain is very wide and optimization algorithms need to
change and try new values constantly to ﬁne tune param-
eters. Since, this part is only required once for each type of
problem, running the modiﬁed algorithm afterward will not
differ in terms of complexity and computational time. After
the new parameters are found, a new modiﬁed algorithm is
Table 1 Sensitivity analysis for the parameter values [5]
Scenario
Parameter values
Value of ﬁtness function
C1
C2
C3
C4
f5
f12
f26
23
2
6
2
0.5
7.56E?02
8.62E?06
7.13E?03
8012
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 7
Table 2 Original [5] values of
C3, C4, p1, p2, p3
Original AOA
CEC and Engineering problems
Standard Optimization Functions
C3
2
1
C4
0.5
2
p1
0.5
p2
0.5
p3
0.5
Table 3 Parameters for
algorithms used in comparison
AOA
Objects Number = 50
C1 = 2,
C2 = 6
C3 = 2; C4 = 0.5; (CEC and engineering problems)
C3 = 1; C4 = 2; (standard Optimization functions)
HBA
Honey Badger number = 50
b (the ability of a honey badger to obtain food) = 6
C = 2
SCA
Number of agents = 50,
a = 2,
r1(0) = 2 (r1 decreases linearly from a to 0)
BOA
The population size n is 50,
p = 0.8 ( probability switch)
power exponent = 0.1 (initial value of a)
sensory modality = 0.01 (initial value of c)
HPPSOBOA
The butterﬂy swarm size = 50
c1 = c2 = 0.5
w = 0.7 (Inertia factor)
p = 0.6 (probability factor)
power_exponent = 0.1 (initial value of a)
sensory_modality = 0.01(initial value of c)
Vmax = 1
GJO
Population of prey = 50
c1 = 1.5
WOA
Whales Number = 50
a = variable decreases linearly from 2 to 0
b = 1
ALO
Number of search agents = 50,
SSA
Number of salp population = 50,
AOS
Number of initial population = 50,
LayerNumber = 5 (Maximum number of Layers around nucleus)
FotonRate = 0.1 (Foton Rate for position determination of electrons)
Neural Computing and Applications (2024) 36:8007–8038
8013
123

---

## Page 8
Table 4 Function parameters of selected standard benchmark functions [8]
Function
No:
Name
Name
Dim
Lower
bound
Upper
bound
f(x*)
1
Sphere f1 x
ð Þ ¼ P
D
i¼1
x2
i
Unimodal
30
- 100
100
0
2
Chung Reynolds f2 x
ð Þ ¼
P
D
i¼1
x2
i

2
Unimodal
30
- 100
100
0
3
Sum of Squares f3 x
ð Þ ¼ P
D
i¼1
ix2
i
Unimodal
30
- 10
10
0
4
Powell Singular-2 f4 x
ð Þ ¼ P
D2
j¼2
xi1  10xi
ð
Þ2þ5 xiþ1  xiþ2
ð
Þ2þ xi  xiþ1
ð
Þ4þ10 xi1  xiþ2
ð
Þ4
Unimodal
30
- 4
5
0
5
Schwefel 2.20 f5 x
ð Þ ¼ P
D
i¼1
xi
j j
Unimodal
30
- 100
100
0
6
Csendes f6 x
ð Þ ¼ P
D
i¼1
x6
i 2 þ sin
1
xi
	 
h
i
Multimodal
30
- 1
1
0
7
Ackley f7 x
ð Þ ¼ 20 exp 0:2
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
D
P
D
i¼1
x2
i
s
 
!
 exp
1
D
P
D
i¼1
cos 2pxi
ð
Þ


þ 20 þ e
Multimodal
30
- 32
32
0
8
Brown f8 x
ð Þ ¼ P
D1
i¼1
x2
i

x2
iþ1þ1þ x2
iþ1

x2
i þ1
h
i
Multimodal
30
- 1
4
0
9
Griewank f9 x
ð Þ ¼ 1 þ P
D
i¼1
x2
i
4000  Q
D
i¼1
cos
xiﬃ
_I
p


Multimodal
30
- 600
600
0
10
Rastrigin f10 x
ð Þ ¼ 10D þ P
D
i¼1
x2
i  10 cos 2pxi
ð
Þ


Multimodal
30
- 5.12
5.12
0
11
Zakharov f11 x
ð Þ ¼ P
D
i¼1
x2
i þ
P
D
i¼1
0:5ixi

2
þ P
D
i¼1
0:5ixi

4
Multimodal
30
- 5
10
0
12
Matyas f12 x
ð Þ ¼ 0:26 x2
1 þ x2
2


 0:48x1x2
Fixed-
dimensional
2
- 10
10
0
13
Colville f13 x
ð Þ ¼ 100 x1  x2
2

2þ 1  x1
ð
Þ2þ90 x4  x2
3

2þ 1  x3
ð
Þ2þ10:1 x2  1
ð
Þ2
þ x4  1
ð
Þ2þ19:8 x2  1
ð
Þ x4  1
ð
Þ
Fixed-
dimensional
4
- 10
10
0
8014
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 9
executed. The pseudo code of the proposed MDAOA is
given in Algorithm 2.
Algorithm 2 The pseudo code of the proposed MDAOA
In addition to C3 and C4, three ﬁxed probability values
are optimized. Probability values are as follows:
•
p1 is the probability compared with Transfer Operator
(TF) parameter,
•
p2 is the probability compared with the ﬂag (F) for
changing the search direction,
•
p3 is used in Step 5 of AOA to compare TF value to
determine either exploration or exploitation phases.
These probabilities are optimized by HBA considering
the lower and upper boundary limits. Second and third
columns in Table 2 indicates the original values of AOA
parameters.
The ﬂowchart of the proposed MDAOA is given in
Fig. 1.
4 Experimental results
The effectiveness of the MDAOA algorithm is evaluated in
four groups of functions. Standard benchmark functions,
CEC 2017 test suite, ﬁve engineering problems and optimal
placement of EVCSs into the IEEE-33 bus distribution
system.
Neural Computing and Applications (2024) 36:8007–8038
8015
123

---

## Page 10
In addition to AOA and Modiﬁed AOA, the formulated
objective function is run with recent optimization algo-
rithms with proven effectiveness using various benchmark
functions (CEC, engineering and standard). Algorithms
used for comparison are: Honey Badger Algorithm (HBA-
2021), Sine Cosine Algorithm (SCA-2016), Butterﬂy
Optimization Algorithm (BOA-2019), Particle Swarm
Optimization Butterﬂy Optimization Algorithm (PSO-
BOA-2020), Golden Jackal Optimization (GJO-2022),
Whale Optimization Algorithm (WOA-2016), Ant Lion
Optimizer (ALO-2015), Salp Swarm Algorithm (SSA-
2017),
Atomic
Orbital
Search
(AOS-2021)
[4, 7–11, 15, 19, 41].
All algorithm evaluations are applied for 30 runs to
provide sufﬁcient consistency (tmax = 1000). Table 3 shows
parameters for algorithms used in comparison.
The Matlab programming of optimization algorithms
was obtained from Matlab File Exchange. Comparisons of
algorithms are executed using MATLAB R2019 version,
on a Microsoft Windows 10 operating system environment.
4.1 Standard benchmark functions
The group of standard benchmark functions is the ﬁrst of
the four test function groups. Unimodal, multimodal and
ﬁxed dimensional functions are used to evaluate in multiple
aspects. The function parameters of selected standard
benchmark functions are shown in Table 4.
Convergence curve graphs of 13 standard benchmark
functions are presented in Fig. 2 which shows ﬁtness val-
ues and number of iterations. Results of 30 runs with
maximum iteration of 1000 are presented in Table 5. Bold
numbers indicate the minimum values. Results indicate
that MDAOA provides best results on all of the standard
benchmark functions. In addition, the average standard
deviation values are consistently low and better on most
functions when compared to other algorithms in the com-
parison group.
To conclude comparison information from the solution
sets in the study, two hypotheses are deﬁned: the null
hypothesis H0 and the alternative hypothesis H1. H0 indi-
cates that medians errors of compared algorithms are
identical and equal to zero while H1 suggests at least one of
the medians errors of compared algorithms is not identical
from the others and different from zero. A level of statis-
tical signiﬁcance (a) is a threshold value deﬁned in order to
decide whether or not to accept or reject the hypothesis.
The level of signiﬁcance in this study is considered to be
0.05.
In order to determine the most appropriate method to
compare the proposed algorithm with the other algorithms
statistically, a normality test is performed. For this purpose,
Shapiro–Wilk (SW) test is used. Based on the results, the
Set Objective function of MDAOA to Obj. Function 
of problem i.e. MDAOA(Obj_Function)
Set parameters of HBA. Set objective function to 
output of MDAOA. 
Start
Determine optimization problem
Load problem related info (Constraints, search 
range, dimension)
Execute HBA and find parameters of modified 
MDAOA
Constants of MDAOA 
calculated for the 
problem?
Initialize population, densities and volumes
Update density and volume
Update acc
Normalize acc
Update new positions
Exploration phase
Radi(t) computed by Eq. 21
TF ≤ 0.5
NO
YES
Evaluate function for each individual
Update acc
Normalize acc
Update flag F
Update new positions
Exploitation phase
Build neighborhood using radius
d ≤ D
 Xi-DL,d(t+1) computed by Eq. 23
Evaluate fitness for individuals. Choose the best
Termination 
criteria met?
Return best fitness and best solution variables
 d = d+1
Define five constant parameters as design variables of 
HBA. parameters. i.e.HBA(MDAOA(Obj_Function))
YES
YES
NO
NO
YES
NO
Fig. 1 Flowchart of the proposed MDAOA
8016
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 11
Friedman test is utilized to compare the algorithms errors
which are produced in every iteration similar to the studies
in [8, 19, 24, 34]. The Friedman test is a nonparametric
statistical test where errors of algorithms are compared in
order to check if there is a statistical signiﬁcance [42].
Mean ranks are presented in Table 5. Next, Bonferroni
corrected Wilcoxon rank-sum test is employed as post hoc
test for making pairwise comparisons of the algorithms
similar to the studies in [6, 12, 19, 24]. In other words, two
solutions sets are compared based on the median values
which are statistically signiﬁcant. If the p-value is lower
than the level of signiﬁcance which is set at 0.05, algo-
rithms output statistically signiﬁcant results. P-values
computed by the Bonferroni corrected Wilcoxon rank-sum
test are presented in Table 5.
According to the table, MDAOA returns best results on
all functions. MDAOA is the only function to provide the
minimum results on ﬁve functions and shares best results
on the remaining eight function with consistently low
standard deviation values. According to Table 5, MDAOA
has the lowest Friedman mean rank and ranks ﬁrst in
optimizing standard benchmark functions.
4.2 Competitions on evolutionary computation
2017
Competitions on Evolutionary Computation 2017 (CEC
2017) is a test bed which provides an environment to test
the performance of unconstrained numerical optimization
algorithms. The CEC 2017 includes 29 benchmark func-
tions, (f2 is excluded) among which are unimodal, multi-
modal,
hybrid,
and
composition
functions.
In
these
benchmark functions, optimization algorithms’ perfor-
mance on avoiding local minima, exploitation and explo-
ration
performance
are
evaluated.
Search
range
for
functions is [- 100, 100]. The dimension is 30. Summary
of the CEC 2017 test functions are presented in Table 6.
In this group, 29 CEC 2017 benchmark functions are
evaluated. Convergence curve graphs indicating minimum
ﬁtness values and number of iterations are presented in
Fig. 3. Results including mean, median and standard
deviation of 30 runs with maximum iteration of 1000 are
presented in Table 7. MDAOA returned optimum results
for 26 of the total 29 benchmark functions. Consequently,
MDAOA can perform well on a wide range of problems.
4.3 Optimal placement of EVCS
in the distribution network
Placement of EVCSs is critical due to the adverse effects
such as deterioration of the voltage proﬁle, increase of
active power losses, instant load peaks, overloading of
transmission lines and transformers which may take place
in the absence of planned deployment. Thus, in this study,
EVCSs are aimed to be placed at the best locations
(speciﬁc buses) that minimize the effect of EVCSs in the
distribution network as much as possible. This placement is
performed based on an index that consists of power loss,
voltage deviation, and voltage stability index (VSI-the
ability of a system to return to normal operating condition
after a disturbance) solved using standard AOA and the
modiﬁed MDAOA. The results include the EVCSs loca-
tions in the appropriate buses of the distribution network.
4.3.1 Objective function
The multi-objective function given in Eq. 25 is used in the
EVCS placement problem.
min w1f1 þ w2f2 þ w3
f3


ð25Þ
Here, w1, w2 and w3 are weight factors and represent the
coefﬁcients of the f1, f2, and f3 functions. The objective
function f1, calculated by Eq. 26, is used to minimize the
power loss value.
f1 ¼ min
X
nbranch
i¼1
I2
i Ri
(
)
ð26Þ
The objective function f2, calculated by Eq. 27 is used
for minimum voltage deviation value.
f2 ¼ min
X
nmax
i¼1
1  Vi
ð
Þ2100MVAb
(
)
ð27Þ
The value of VSI is preferred to be greater than 0.
However, the higher this value, the better the stability of
the system would be. In order to calculate the VSI values,
the formula in reference [44] is used. The objective func-
tion that calculates the VSI values is presented in Eq. 28.
VSI ¼ max 2V2
k V2
kþ1  2V2
kþ1 Pkþ1r þ Qkþ1x
ð
Þ  Z
j j2 P2
kþ1 þ Q2
kþ1


n
o
ð28Þ
The lowest single VSI value among the entire VSI
values, represents the weakest link in terms of system
stability. The lowest VSI value is found by the Eq. 29 and
w3 in Eq. 25 is divided by this value.
f3 ¼ min VSI
f
g
ð29Þ
4.3.2 Constraints
The following constraints (Eq. 30) are used to secure
optimal power ﬂow including minimum voltage, power and
voltage stability of the distribution network.
Neural Computing and Applications (2024) 36:8007–8038
8017
123

---

## Page 12
Fig. 2 Convergence curves of standard benchmark functions
8018
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 13
Fig. 2 continued
Neural Computing and Applications (2024) 36:8007–8038
8019
123

---

## Page 14
0\VSIi
i ¼ 1; 2; . . .N
Active power Pmin
i
 Pi  Pmax
i
i ¼ 1; 2; . . .N
Reactive power Qmin
i
 Qi  Qmax
i
i ¼ 1; 2; . . .N
Bus voltage Vmin
i
 Vi
j
j  Vmax
i
i ¼ 1; 2; . . .N
ð30Þ
where N is the number of buses. Pi is active power of ith
bus. Qi : is reactive power of ith bus. Vi: is voltage of ith
bus.
Figure 4 shows the comparison of convergence curve
graphs of 11 optimization algorithms. Numerical results
are presented in Table 8. Results show that compared to
other techniques, MDAOA has achieved successful results
with lowest average standard deviation values. This shows
that MDAOA can be used in the EVCS placement prob-
lem, which is an important and challenging issue in power
system engineering.
4.4 Constrained engineering design problems
Validity and efﬁciency of the proposed MDAOA is eval-
uated through ﬁve real life constrained engineering prob-
lems. The problems are highly complex with multiple
design variables and constraints. However, MDAOA
returned optimum results on all of the ﬁve engineering
problems. Table 9 shows the list of engineering design
problems with relative parameters.
4.4.1 Tension/compression spring design
The tension/compression spring design problem is used as
a benchmark function. It is an optimization problem aiming
to minimize the cost of a spring with three variables. These
are: the number of active coils (N), wire diameter (d), and
the diameter of coil (D). The problem has four constraints
requiring deﬂection, stress and surge frequency. The ﬁg-
ure of the problem is shown in Fig. 5.
The problem is mathematically formulated as:
x ¼ x1; x2; x3
½
 ¼ d; D; N
½

ð31Þ
f x
ð Þ ¼ x3 þ 2
ð
Þx2x2
1
ð32Þ
Constraints:
g1 x
ð Þ ¼ 1 
x3
2x3
71785x4
1
 0;
g2 x
ð Þ ¼
4x2
2  x1x2
12566 x2x3
1  x4
1

 þ
1
5108x2
1
 1  0;
g3 x
ð Þ ¼ 1  140:45x1
x2
2x3
 0;
g4 x
ð Þ ¼ x1 þ x2
1:5
 1  0;
ð33Þ
Range of variables
0:05  x1  2:00; 0:25  x2  1:30; 2:00  x3  15:00
Comparative
convergence curves are
presented
in
Fig. 6. The numerical results are shown in Table 10.
Results demonstrate that solutions calculated by MDAOA
and GJO are superior in the comparison group.
4.4.2 Pressure vessel design
The pressure vessel design problem is an optimization
problem aiming to minimize the manufacturing cost of a
cylindrical pressure vessel. The design and the parameters
of the optimization are shown in Fig. 7. These are: shell
thickness (Ts), inner radius (R), length of the cylindrical
section (L) (excluding head) and head thickness (Th).
The mathematical formulation of the problem is:
x ¼ x1; x2; x3; x4
½
 ¼ Ts; Th; R; L
½

ð34Þ
f x
ð Þ ¼ 0:6224x1x3x4 þ 1:7781x2x2
3 þ 3:1661x2
1x4
þ 19:84x2
1x3
ð35Þ
Constraints:
g1 x
ð Þ ¼ x1 þ 0:0193x3  0;
g2 x
ð Þ ¼ x2 þ 0:00954x3  0;
g3 x
ð Þ ¼ px2
3x4  4
3 px3
3 þ 1; 296; 000  0;
g4 x
ð Þ ¼ x4  240  0;
ð36Þ
Range of variables
0  x1  99; 0  x2  99;
10  x3  200; 10  x4  200
Convergence curves are presented in Fig. 8. The com-
parative results are shown in Table 10. Results show that
MDAOA outperforms other algorithms in the comparison
group.
Fig. 2 continued
8020
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 15
Table 5 Comparison of results of 13 standard benchmark functions
Fun
Meas
AOA
MDAOA
HBA
SCA
BOA
PSOBOA
GJO
WOA
ALO
SSA
AOS
1
Mean
8.18E-85
0.00E?00
7.41E-296
5.88E-03
1.04E-13
9.38E-118
1.88E-127
9.84E-170
4.63E-07
8.88E-09
4.61E-149
SD
3.74E-84
0.00E?00
0.00E?00
2.34E-02
7.10E-15
2.80E-117
4.23E-127
0.00E?00
4.11E-07
1.75E-09
2.41E-148
Median
3.20E-98
0.00E?00
2.38E-302
1.52E-04
1.04E-13
7.02E-119
4.81E-129
8.22E-180
2.84E-07
8.81E-09
9.44E-154
P Value (Wilcoxon)
1.21E-11
–
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
2
Mean
1.95E-184
0.00E?00
0.00E?00
4.80E-04
1.21E-16
2.37E-248
1.31E-252
0.00E?00
1.04E-13
8.23E-17
6.71E-289
SD
0.00E?00
0.00E?00
0.00E?00
1.63E-03
8.19E-18
0.00E?00
0.00E?00
0.00E?00
3.59E-13
3.13E-17
0.00E?00
Median
7.82E-221
0.00E?00
0.00E?00
1.26E-08
1.20E-16
4.32E-252
1.83E-257
0.00E?00
1.41E-14
7.56E-17
1.49E-306
P Value (Wilcoxon)
1.21E-11
–
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.34E-02
1.21E-11
1.21E-11
4.57E-11
3
Mean
1.83E-89
0.00E?00
1.05E-296
1.09E-04
9.90E-14
6.60E-116
1.66E-128
1.13E-170
7.26E-01
5.13E-02
2.41E-149
SD
9.71E-89
0.00E?00
0.00E?00
2.20E-04
7.64E-15
2.28E-115
5.28E-128
0.00E?00
1.05E?00
8.94E-02
1.21E-148
Median
3.56E-110
0.00E?00
2.22E-302
1.48E-05
9.77E-14
1.55E-117
1.66E-130
1.25E-178
3.82E-01
1.87E-02
5.37E-155
P Value (Wilcoxon)
1.21E-11
–
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
4
Mean
1.20E-25
1.83E-204
1.11E-157
2.83E-01
6.82E-14
4.97E-116
7.04E-09
1.74E-06
6.95E-01
6.13E-01
6.95E-34
SD
6.57E-25
0.00E?00
6.10E-157
7.64E-01
6.00E-15
2.03E-115
1.79E-08
5.09E-06
3.82E-01
4.40E-01
3.80E-33
Median
2.43E-47
0.00E?00
7.95E-216
7.78E-03
6.87E-14
1.00E-117
1.13E-11
7.65E-09
6.47E-01
5.02E-01
1.02E-74
P Value (Wilcoxon)
3.16E-11
–
2.38E-09
3.16E-11
3.16E-11
3.16E-11
3.16E-11
3.16E-11
3.16E-11
3.16E-11
3.16E-11
5
Mean
1.18E-45
1.36E-243
3.92E-157
3.55E-05
7.30E-11
1.51E-56
4.37E-73
1.20E-108
2.39E?01
5.12E?00
6.31E-78
SD
4.19E-45
0.00E?00
7.24E-157
9.91E-05
5.03E-12
2.47E-56
6.48E-73
4.02E-108
1.38E?01
6.45E?00
1.74E-77
Median
1.47E-55
1.77E-256
1.51E-158
4.15E-06
7.32E-11
5.40E-57
2.03E-73
1.17E-112
2.12E?01
3.04E?00
4.00E-79
P Value (Wilcoxon)
1.69E-16
–
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
6
Mean
0.00E?00
0.00E?00
0.00E?00
7.78E-253
3.61E-09
0.00E?00
0.00E?00
0.00E?00
6.61E-43
1.20E-44
0.00E?00
SD
0.00E?00
0.00E?00
0.00E?00
0.00E?00
2.67E-09
0.00E?00
0.00E?00
0.00E?00
1.39E-42
2.54E-44
0.00E?00
Median
0.00E?00
0.00E?00
0.00E?00
1.59E-271
2.96E-09
0.00E?00
0.00E?00
0.00E?00
2.47E-44
1.84E-45
0.00E?00
P Value (Wilcoxon)
–
1.21E-11
1.21E-11
1.21E-11
1.21E-11
7
Mean
1.60E?01
8.88E-16
8.88E-16
1.40E?01
3.36E-11
8.88E-16
4.68E-15
3.85E-15
2.03E?00
1.95E?00
4.20E-15
SD
8.12E?00
0.00E?00
0.00E?00
8.94E?00
1.44E-11
0.00E?00
9.01E-16
2.30E-15
6.54E-01
6.76E-01
1.30E-15
Median
2.00E?01
8.88E-16
8.88E-16
2.00E?01
3.11E-11
8.88E-16
4.44E-15
4.44E-15
2.07E?00
1.90E?00
4.44E-15
P Value (Wilcoxon)
1.20E-11
–
1.21E-11
1.21E-11
4.16E-13
2.90E-07
1.21E-11
1.21E-11
5.42E-11
8
Mean
3.57E-298
0.00E?00
0.00E?00
2.23E-153
3.87E-22
1.67E-110
0.00E?00
1.59E-275
1.24E-15
3.83E-16
0.00E?00
SD
0.00E?00
0.00E?00
0.00E?00
8.70E-153
5.06E-22
8.94E-110
0.00E?00
0.00E?00
1.34E-15
4.72E-16
0.00E?00
Median
0.00E?00
0.00E?00
0.00E?00
9.55E-161
2.36E-22
7.37E-121
0.00E?00
3.23E-294
8.32E-16
2.24E-16
0.00E?00
P Value (Wilcoxon)
2.78E-02
–
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
9
Mean
4.71E-02
0.00E?00
0.00E?00
1.71E-01
3.63E-16
0.00E?00
0.00E?00
6.43E-03
1.31E-02
6.65E-03
1.37E-03
SD
1.35E-01
0.00E?00
0.00E?00
2.34E-01
7.33E-16
0.00E?00
0.00E?00
1.74E-02
1.22E-02
7.60E-03
5.61E-03
Median
0.00E?00
0.00E?00
0.00E?00
2.63E-02
0.00E?00
0.00E?00
0.00E?00
0.00E?00
1.02E-02
7.40E-03
0.00E?00
P Value (Wilcoxon)
4.19E-01
–
1.21E-11
3.13E-03
4.19E-01
1.21E-11
1.21E-11
9.99E-01
Neural Computing and Applications (2024) 36:8007–8038
8021
123

---

## Page 16
Table 5 (continued)
Fun
Meas
AOA
MDAOA
HBA
SCA
BOA
PSOBOA
GJO
WOA
ALO
SSA
AOS
10
Mean
2.24E?01
0.00E?00
0.00E?00
1.67E?01
1.88E?01
0.00E?00
0.00E?00
0.00E?00
7.03E?01
5.18E?01
1.37E?01
SD
3.94E?01
0.00E?00
0.00E?00
2.52E?01
5.74E?01
0.00E?00
0.00E?00
0.00E?00
1.96E?01
1.83E?01
1.95E?01
Median
0.00E?00
0.00E?00
0.00E?00
1.56E-01
0.00E?00
0.00E?00
0.00E?00
0.00E?00
6.67E?01
5.17E?01
0.00E?00
P Value (Wilcoxon)
1.46E-03
–
1.21E-11
2.79E-02
1.21E-11
1.21E-11
1.46E-03
11
Mean
1.75E-70
3.66E-265
6.37E-156
4.51E?00
6.37E-14
1.23E-115
5.10E-56
4.82E?02
4.97E?00
1.88E-03
1.83E-105
SD
6.01E-70
0.00E?00
3.36E-155
3.05E?00
6.12E-15
3.22E-115
2.68E-55
1.08E?02
7.06E?00
3.44E-03
6.08E-105
Median
2.60E-75
0.00E?00
5.49E-163
4.51E?00
6.42E-14
1.26E-117
7.00E-59
4.58E?02
2.63E?00
3.56E-04
1.73E-109
P Value (Wilcoxon)
9.40E-11
–
9.40E-11
9.40E-11
9.40E-11
9.40E-11
9.40E-11
9.40E-11
9.40E-11
9.40E-11
9.40E-11
12
Mean
4.71E-287
0.00E?00
0.00E?00
1.98E-126
4.95E-21
3.53E-125
0.00E?00
0.00E?00
4.53E-16
2.71E-16
0.00E?00
SD
0.00E?00
0.00E?00
0.00E?00
9.79E-126
1.25E-20
9.86E-125
0.00E?00
0.00E?00
4.93E-16
3.46E-16
0.00E?00
Median
0.00E?00
0.00E?00
0.00E?00
2.69E-132
1.91E-21
2.29E-127
0.00E?00
0.00E?00
3.29E-16
1.55E-16
0.00E?00
P Value (Wilcoxon)
1.37E-02
–
1.21E-11
1.21E-11
1.21E-11
1.21E-11
1.21E-11
13
Mean
0.00E?00
0.00E?00
1.30E?00
0.00E?00
7.74E?00
1.55E?01
0.00E?00
0.00E?00
0.00E?00
0.00E?00
5.18E-01
SD
0.00E?00
0.00E?00
1.86E?00
0.00E?00
3.98E?00
8.17E?00
0.00E?00
0.00E?00
0.00E?00
0.00E?00
1.34E?00
Median
0.00E?00
0.00E?00
0.00E?00
0.00E?00
6.92E?00
1.59E?01
0.00E?00
0.00E?00
0.00E?00
0.00E?00
0.00E?00
P Value (Wilcoxon)
–
6.18E-03
1.21E-11
1.21E-11
4.19E-01
Friedman Mean Rank
5.58
2.58
2.96
9.00
7.77
5.54
4.81
4.81
9.92
8.92
4.12
Rank
6
1
2
9
7
5
4
4
10
8
3
Bold numbers indicate minimum values
8022
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 17
4.4.3 Welded beam design
Welded beam design problem is a cost minimization
optimization problem of manufacturing a welded beam
shown in Fig. 9. Cost function includes four decision
variables: weld thickness (h), bar thickness (b), length of
the attached section of the bar (l), and the bar’s height (t).
There are seven constraints some of which are shear stress
(s), bucking load on the bar (Pc) and bending stress (h).
Mathematical formulation of the problem is:
The problem is mathematically formulated as:
x ¼ x1; x2; x3; x4
½
 ¼ h; l; t; b
½

ð37Þ
f x
ð Þ ¼ 1:10471x2
1x2 þ 0:04811x3x4 14 þ x2
ð
Þ
ð38Þ
Constraints:
g1 x
ð Þ ¼ s x
ð Þ  smax  0;
g2 x
ð Þ ¼ r x
ð Þ  rmax  0;
g3 x
ð Þ ¼ x1  x4  0;
g4 x
ð Þ ¼ 1:10471x2
1 þ 0:04811x3x4 14 þ x2
ð
Þ  5  0;
g5 x
ð Þ ¼ 0:125  x1  0;
g6 x
ð Þ ¼ d x
ð Þ  dmax  0;
g7 x
ð Þ ¼ P  Pc x
ð Þ  0;
ð39Þ
Range of variables
0:1  x1  2; 0:1  x2  10; 0:1  x3  10; 0:1  x4  2
where
sðxÞ ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
ðs0Þ2 þ 2s0s00 x2
2R þ ðs00Þ2
r
; s0 ¼
P
ﬃﬃ
2
p
x1x2
; s00 ¼ MR
J
R ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
x2
2
4 þ
x1 þ x3
2
	

2
r
; M ¼ P L þ x2
2
	

J ¼ 2
ﬃﬃ
2
p
x1x2
x2
2
12 þ
x1 þ x3
2
	

2




r x
ð Þ ¼ 6PL
x4x2
3
d x
ð Þ ¼ 4PL3
Ex3
3x4
Pc x
ð Þ ¼
4:013E
ﬃﬃﬃﬃﬃﬃ
x2
3x6
4
36
q
L2
1  x3
2L
ﬃﬃﬃﬃﬃﬃ
E
4G
r
 
!
L = 14 in, dmax = 0.25 in, P = 6000 Lb, E = 30 9 106
psi, G = 12 9 106 psi, smax = 13,600 psi, rmax = 30,000
psi.
The convergence curve graph is shown in Fig. 10.
Results are shown in Table 10. The solution calculated by
MDAOA is better than all other algorithms in the com-
parison group.
4.4.4 Speed reducer problem
In this engineering design problem, the goal is to choose
parameters for a speed reducer used in a small aircraft that
yields minimum weight. It has seven design variables and
eleven constraints. These are: teeth module, face width,
number of teeth on pinion, length between bearings for
both ﬁrst and second shafts, and diameters of both ﬁrst and
Table 6 Summary of the CEC 2017 Test Functions [43]
Fun. Number
Min. of Fun
Unimodal functions (shifted and rotated)
f1(x)
100
f3(x)
300
f4(x)
400
Simple, multimodal, functions (shifted and rotated)
f5(x)
500
f6(x)
600
f7(x)
700
f8(x)
800
f9(x)
900
f10(x)
1000
Hybrid functions
f11(x)
1100
f12(x)
1200
f13(x)
1300
f14(x)
1400
f15(x)
1500
f16(x)
1600
f17(x)
1700
f18(x)
1800
f19(x)
1900
f20(x)
2000
Composition functions
f21(x)
2100
f22(x)
2200
f23(x)
2300
f24(x)
2400
f25(x)
2500
f26(x)
2600
f27(x)
2700
f28(x)
2800
f29(x)
2900
f30(x)
3000
Neural Computing and Applications (2024) 36:8007–8038
8023
123

---

## Page 18
Fig. 3 Convergence curves of CEC 2017 benchmark functions
8024
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 19
Fig. 3 continued
Neural Computing and Applications (2024) 36:8007–8038
8025
123

---

## Page 20
Fig. 3 continued
8026
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 21
Fig. 3 continued
Neural Computing and Applications (2024) 36:8007–8038
8027
123

---

## Page 22
Fig. 3 continued
8028
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 23
Table 7 Comparison of results of 29 CEC 2017 benchmark functions
Fun
Meas
AOA
MDAOA
HBA
SCA
BOA
PSOBOA
GJO
WOA
ALO
SSA
AOS
1
Mean
3.50E?09
1.06E?03
2.81E?03
7.72E?08
4.13E?09
2.95E?09
3.55E?08
9.91E?05
2.12E?03
3.75E?03
1.44E?05
SD
1.85E?09
1.33E?03
2.73E?03
2.44E?08
1.84E?09
2.40E?09
3.93E?08
1.45E?06
2.34E?03
3.52E?03
8.83E?04
Median
3.19E?09
5.31E?02
1.44E?03
7.26E?08
3.83E?09
2.34E?09
3.54E?08
6.73E?05
1.19E?03
2.34E?03
1.13E?05
P Value (Wilcoxon)
1.69E-16
–
4.11E-02
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
6.32E-01
1.53E-03
1.69E-16
3
Mean
8.51E?02
3.00E?02
3.00E?02
1.74E?03
6.83E?03
1.44E?04
2.61E?03
1.64E?03
3.00E?02
3.00E?02
3.03E?02
SD
9.78E?02
2.16E-03
1.66E-12
1.11E?03
2.25E?03
2.47E?03
2.18E?03
2.29E?03
6.90E-09
6.80E-10
2.31E?00
Median
4.23E?02
3.00E?02
3.00E?02
1.39E?03
7.24E?03
1.50E?04
1.92E?03
6.73E?02
3.00E?02
3.00E?02
3.02E?02
P Value (Wilcoxon)
3.38E-16
–
1.38E-09
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.22E-02
2.41E-04
1.69E-16
4
Mean
5.86E?02
4.02E?02
4.01E?02
4.46E?02
1.13E?03
2.10E?03
4.38E?02
4.26E?02
4.05E?02
4.07E?02
4.10E?02
SD
1.03E?02
1.42E?00
6.04E-01
2.37E?01
2.63E?02
6.03E?02
3.14E?01
3.61E?01
1.43E?00
1.27E?01
1.62E?01
Median
5.48E?02
4.02E?02
4.01E?02
4.41E?02
1.12E?03
2.17E?03
4.31E?02
4.08E?02
4.05E?02
4.06E?02
4.08E?02
P Value (Wilcoxon)
1.69E-16
–
1.64E-04
1.69E-16
1.69E-16
1.69E-16
1.69E-16
3.00E-11
5.96E-07
3.77E-05
4.11E-05
5
Mean
5.41E?02
5.11E?02
5.16E?02
5.46E?02
5.83E?02
6.27E?02
5.27E?02
5.50E?02
5.19E?02
5.20E?02
5.21E?02
SD
9.86E?00
3.96E?00
7.05E?00
6.67E?00
1.33E?01
1.42E?01
9.72E?00
2.13E?01
1.22E?01
1.09E?01
9.32E?00
Median
5.42E?02
5.11E?02
5.15E?02
5.47E?02
5.85E?02
6.25E?02
5.29E?02
5.46E?02
5.16E?02
5.16E?02
5.23E?02
P Value (Wilcoxon)
1.69E-16
–
2.51E-01
1.69E-16
1.69E-16
1.69E-16
2.31E-09
6.76E-16
1.09E-02
3.51E-04
2.91E-05
6
Mean
6.17E?02
6.00E?02
6.01E?02
6.17E?02
6.26E?02
6.60E?02
6.06E?02
6.30E?02
6.08E?02
6.10E?02
6.15E?02
SD
6.60E?00
3.18E-03
3.64E?00
2.92E?00
7.93E?00
4.14E?00
5.10E?00
9.76E?00
7.50E?00
7.66E?00
8.41E?00
Median
6.18E?02
6.00E?02
6.00E?02
6.18E?02
6.25E?02
6.61E?02
6.04E?02
6.27E?02
6.06E?02
6.09E?02
6.14E?02
P Value (Wilcoxon)
1.69E-16
–
3.09E-09
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
7
Mean
7.48E?02
7.21E?02
7.31E?02
7.74E?02
7.87E?02
8.24E?02
7.51E?02
7.85E?02
7.37E?02
7.34E?02
7.56E?02
SD
1.52E?01
5.18E?00
1.00E?01
9.98E?00
1.20E?01
1.17E?01
1.64E?01
3.11E?01
1.02E?01
1.32E?01
1.82E?01
Median
7.49E?02
7.22E?02
7.31E?02
7.74E?02
7.86E?02
8.30E?02
7.48E?02
7.84E?02
7.37E?02
7.31E?02
7.51E?02
P Value (Wilcoxon)
2.04E-11
–
9.53E-04
1.69E-16
1.69E-16
1.69E-16
6.76E-16
2.05E-13
1.27E-09
3.14E-06
1.13E-14
8
Mean
8.20E?02
8.09E?02
8.16E?02
8.41E?02
8.50E?02
8.51E?02
8.25E?02
8.45E?02
8.22E?02
8.21E?02
8.24E?02
SD
4.54E?00
3.05E?00
5.76E?00
8.60E?00
5.23E?00
6.35E?00
8.82E?00
1.52E?01
1.04E?01
9.84E?00
9.42E?00
Median
8.18E?02
8.08E?02
8.14E?02
8.40E?02
8.50E?02
8.51E?02
8.24E?02
8.48E?02
8.19E?02
8.19E?02
8.24E?02
P Value (Wilcoxon)
2.70E-13
–
5.45E-05
1.69E-16
1.69E-16
1.69E-16
6.00E-12
2.70E-13
2.75E-08
2.31E-09
1.83E-10
9
Mean
1.06E?03
9.00E?02
9.02E?02
1.00E?03
1.12E?03
1.82E?03
9.52E?02
1.48E?03
9.34E?02
9.65E?02
1.05E?03
SD
1.10E?02
1.16E-01
4.92E?00
3.85E?01
1.63E?02
1.52E?02
5.84E?01
3.38E?02
6.51E?01
1.92E?02
1.38E?02
Median
1.05E?03
9.00E?02
9.00E?02
1.00E?03
1.09E?03
1.81E?03
9.37E?02
1.37E?03
9.02E?02
9.02E?02
1.00E?03
P Value (Wilcoxon)
1.25E-10
–
4.64E-06
1.25E-10
1.25E-10
1.25E-10
1.90E-10
1.25E-10
3.81E-09
5.60E-09
1.54E-10
10
Mean
1.96E?03
1.85E?03
1.86E?03
2.30E?03
2.58E?03
2.86E?03
1.77E?03
2.11E?03
1.89E?03
1.77E?03
1.76E?03
SD
2.87E?02
2.99E?02
4.28E?02
2.46E?02
1.52E?02
1.76E?02
2.76E?02
3.72E?02
2.68E?02
2.92E?02
2.43E?02
Median
2.00E?03
1.76E?03
1.82E?03
2.31E?03
2.61E?03
2.89E?03
1.76E?03
2.10E?03
1.90E?03
1.80E?03
1.76E?03
P Value (Wilcoxon)
9.90E-01
–
9.90E-01
1.13E-06
4.60E-14
6.76E-16
9.90E-01
4.53E-02
9.90E-01
9.90E-01
9.90E-01
Neural Computing and Applications (2024) 36:8007–8038
8029
123

---

## Page 24
Table 7 (continued)
Fun
Meas
AOA
MDAOA
HBA
SCA
BOA
PSOBOA
GJO
WOA
ALO
SSA
AOS
11
Mean
1.18E?03
1.10E?03
1.11E?03
1.19E?03
1.27E?03
1.45E?03
1.16E?03
1.19E?03
1.17E?03
1.18E?03
1.15E?03
SD
7.87E?01
2.19E?00
1.18E?01
3.71E?01
7.34E?01
2.35E?02
6.02E?01
6.27E?01
3.76E?01
5.98E?01
3.54E?01
Median
1.16E?03
1.10E?03
1.11E?03
1.19E?03
1.26E?03
1.38E?03
1.15E?03
1.17E?03
1.16E?03
1.17E?03
1.15E?03
P Value (Wilcoxon)
1.69E-16
–
7.74E-03
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
2.70E-13
4.59E-13
1.16E-13
12
Mean
6.11E?06
1.24E?04
1.88E?04
1.79E?07
1.67E?07
1.29E?07
7.25E?05
6.12E?06
1.20E?06
1.74E?06
2.26E?06
SD
1.06E?07
1.24E?04
1.79E?04
1.90E?07
2.03E?07
3.27E?07
1.39E?06
6.59E?06
1.46E?06
1.82E?06
2.03E?06
Median
1.84E?06
8.02E?03
1.33E?04
1.06E?07
9.36E?06
4.32E?06
9.02E?04
2.98E?06
6.55E?05
1.22E?06
1.78E?06
P Value (Wilcoxon)
2.04E-11
–
9.90E-01
1.69E-16
1.69E-16
1.69E-16
2.49E-12
1.69E-16
3.53E-13
6.76E-16
4.59E-13
13
Mean
8.61E?03
2.42E?03
5.52E?03
2.07E?04
8.72E?04
4.02E?04
1.09E?04
1.63E?04
1.24E?04
1.73E?04
1.13E?04
SD
2.84E?03
7.08E?02
6.59E?03
1.39E?04
8.99E?04
2.25E?04
6.81E?03
1.33E?04
1.02E?04
1.24E?04
1.01E?04
Median
8.11E?03
2.17E?03
2.61E?03
1.72E?04
6.33E?04
3.54E?04
8.94E?03
1.59E?04
8.85E?03
1.57E?04
7.78E?03
P Value (Wilcoxon)
1.69E-16
–
8.50E-01
1.69E-16
1.69E-16
1.69E-16
5.07E-15
1.86E-08
2.31E-09
2.67E-09
3.77E-05
14
Mean
1.47E?03
1.44E?03
1.50E?03
1.61E?03
2.56E?03
2.56E?03
1.90E?03
1.89E?03
1.52E?03
1.57E?03
1.50E?03
SD
1.85E?01
1.53E?01
5.30E?01
8.47E?01
1.02E?03
8.59E?02
1.08E?03
1.05E?03
3.79E?01
1.51E?02
3.04E?01
Median
1.47E?03
1.44E?03
1.49E?03
1.58E?03
2.16E?03
2.35E?03
1.50E?03
1.53E?03
1.52E?03
1.52E?03
1.50E?03
P Value (Wilcoxon)
3.84E-07
–
6.64E-07
1.69E-16
1.69E-16
1.69E-16
2.35E-14
6.76E-16
1.64E-14
3.12E-12
2.48E-11
15
Mean
1.69E?03
1.56E?03
1.62E?03
2.31E?03
6.24E?03
4.71E?03
3.66E?03
4.77E?03
4.76E?03
2.68E?03
3.47E?03
SD
2.86E?02
3.88E?01
8.83E?01
6.31E?02
3.16E?03
2.78E?03
1.72E?03
4.16E?03
3.86E?03
1.78E?03
1.70E?03
Median
1.58E?03
1.55E?03
1.60E?03
2.14E?03
5.61E?03
3.79E?03
3.68E?03
2.90E?03
2.83E?03
2.15E?03
2.71E?03
P Value (Wilcoxon)
5.50E-02
–
1.31E-01
1.69E-16
1.69E-16
1.69E-16
6.31E-14
1.69E-16
6.76E-16
3.21E-15
1.69E-16
16
Mean
1.81E?03
1.61E?03
1.70E?03
1.74E?03
1.87E?03
2.27E?03
1.77E?03
1.85E?03
1.76E?03
1.74E?03
1.75E?03
SD
7.37E?01
2.50E?01
1.00E?02
6.06E?01
8.96E?01
7.81E?01
1.38E?02
1.39E?02
1.31E?02
1.13E?02
9.24E?01
Median
1.84E?03
1.60E?03
1.72E?03
1.75E?03
1.87E?03
2.27E?03
1.75E?03
1.83E?03
1.74E?03
1.74E?03
1.75E?03
P Value (Wilcoxon)
4.59E-13
–
3.91E-02
8.59E-14
6.76E-16
1.69E-16
6.31E-14
2.35E-14
1.24E-12
3.12E-12
2.05E-13
17
Mean
1.76E?03
1.73E?03
1.74E?03
1.78E?03
1.79E?03
1.83E?03
1.76E?03
1.79E?03
1.77E?03
1.77E?03
1.76E?03
SD
1.26E?01
9.15E?00
3.30E?01
1.51E?01
1.78E?01
2.75E?01
2.35E?01
4.80E?01
4.10E?01
3.55E?01
2.58E?01
Median
1.75E?03
1.72E?03
1.74E?03
1.78E?03
1.79E?03
1.82E?03
1.76E?03
1.77E?03
1.76E?03
1.76E?03
1.76E?03
P Value (Wilcoxon)
6.31E-14
–
3.32E-01
1.69E-16
6.76E-16
1.69E-16
1.54E-10
6.31E-14
3.02E-10
1.98E-12
2.49E-12
18
Mean
3.13E?03
3.20E?03
1.38E?04
1.11E?05
3.80E?05
8.14E?04
3.99E?04
1.58E?04
1.43E?04
1.55E?04
2.51E?04
SD
1.05E?03
9.19E?02
1.47E?04
7.44E?04
4.22E?05
7.16E?04
1.08E?04
1.19E?04
1.01E?04
1.10E?04
1.55E?04
Median
2.74E?03
2.95E?03
6.12E?03
9.05E?04
2.15E?05
6.50E?04
3.99E?04
1.16E?04
1.16E?04
1.15E?04
2.10E?04
P Value (Wilcoxon)
9.90E-01
–
6.49E-03
1.69E-16
1.69E-16
2.35E-14
6.76E-16
1.71E-09
1.99E-09
1.29E-10
5.93E-13
19
Mean
2.29E?03
1.93E?03
2.01E?03
4.42E?03
3.31E?04
1.29E?04
8.22E?03
3.87E?04
1.01E?04
2.73E?03
5.80E?03
SD
1.16E?03
1.93E?01
6.31E?01
3.96E?03
3.70E?04
8.93E?03
5.51E?03
5.28E?04
9.61E?03
1.18E?03
4.58E?03
Median
1.93E?03
1.92E?03
2.01E?03
2.66E?03
1.81E?04
1.04E?04
1.02E?04
1.53E?04
5.51E?03
2.14E?03
3.44E?03
P Value (Wilcoxon)
9.90E-01
–
3.09E-09
1.69E-16
1.69E-16
1.69E-16
1.54E-10
1.69E-16
1.69E-16
3.02E-10
1.69E-16
8030
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 25
Table 7 (continued)
Fun
Meas
AOA
MDAOA
HBA
SCA
BOA
PSOBOA
GJO
WOA
ALO
SSA
AOS
20
Mean
2.06E?03
2.02E?03
2.04E?03
2.09E?03
2.14E?03
2.26E?03
2.11E?03
2.18E?03
2.15E?03
2.09E?03
2.08E?03
SD
4.88E?01
9.47E?00
5.05E?01
2.09E?01
3.05E?01
1.79E?01
6.65E?01
8.18E?01
9.01E?01
5.43E?01
4.64E?01
Median
2.04E?03
2.02E?03
2.03E?03
2.09E?03
2.14E?03
2.26E?03
2.12E?03
2.16E?03
2.16E?03
2.08E?03
2.08E?03
P Value (Wilcoxon)
6.33E-11
–
3.91E-02
1.69E-16
1.69E-16
1.69E-16
3.30E-14
1.69E-16
1.69E-16
5.07E-15
3.30E-14
21
Mean
2.31E?03
2.22E?03
2.27E?03
2.24E?03
2.21E?03
2.29E?03
2.31E?03
2.31E?03
2.31E?03
2.27E?03
2.22E?03
SD
5.11E?01
4.17E?01
6.01E?01
5.45E?01
4.69E?00
5.02E?01
4.56E?01
6.50E?01
3.85E?01
6.16E?01
3.39E?01
Median
2.33E?03
2.21E?03
2.31E?03
2.21E?03
2.21E?03
2.27E?03
2.33E?03
2.33E?03
2.32E?03
2.31E?03
2.21E?03
P Value (Wilcoxon)
1.86E-08
–
9.90E-01
4.37E-04
5.76E-03
1.13E-06
9.30E-10
2.67E-09
1.02E-06
9.90E-01
9.90E-01
22
Mean
2.34E?03
2.29E?03
2.30E?03
2.36E?03
2.33E?03
3.01E?03
2.35E?03
2.38E?03
2.33E?03
2.30E?03
2.30E?03
SD
3.56E?01
2.34E?01
9.07E-01
3.26E?01
2.04E?01
2.37E?02
4.76E?01
3.46E?02
1.50E?02
2.49E?01
1.73E?01
Median
2.33E?03
2.30E?03
2.30E?03
2.37E?03
2.33E?03
2.97E?03
2.33E?03
2.31E?03
2.30E?03
2.30E?03
2.31E?03
P Value (Wilcoxon)
2.05E-13
–
5.91E-01
3.00E-11
1.94E-07
1.69E-16
3.21E-15
4.20E-10
8.69E-03
6.49E-03
3.14E-06
23
Mean
2.67E?03
2.61E?03
2.62E?03
2.66E?03
2.63E?03
2.80E?03
2.64E?03
2.65E?03
2.63E?03
2.62E?03
2.63E?03
SD
3.11E?01
4.82E?00
1.05E?01
7.57E?00
6.61E?01
5.55E?01
1.10E?01
2.29E?01
1.27E?01
1.20E?01
1.84E?01
Median
2.65E?03
2.61E?03
2.62E?03
2.66E?03
2.66E?03
2.80E?03
2.64E?03
2.65E?03
2.63E?03
2.62E?03
2.63E?03
P Value (Wilcoxon)
1.69E-16
–
1.43E-03
1.69E-16
1.90E-06
1.69E-16
1.12E-11
2.48E-11
9.92E-06
2.22E-02
9.92E-06
24
Mean
2.63E?03
2.52E?03
2.75E?03
2.76E?03
2.57E?03
2.86E?03
2.74E?03
2.75E?03
2.72E?03
2.73E?03
2.68E?03
SD
1.40E?02
7.75E?01
4.86E?01
6.46E?01
2.43E?01
5.30E?01
6.51E?01
8.69E?01
9.79E?01
6.36E?01
1.18E?02
Median
2.54E?03
2.50E?03
2.75E?03
2.78E?03
2.57E?03
2.86E?03
2.76E?03
2.77E?03
2.75E?03
2.75E?03
2.75E?03
P Value (Wilcoxon)
1.20E-04
–
3.12E-12
4.60E-14
1.26E-06
1.69E-16
6.31E-14
1.55E-13
1.02E-06
5.80E-10
2.04E-11
25
Mean
3.08E?03
2.88E?03
2.93E?03
2.96E?03
3.38E?03
3.70E?03
2.94E?03
2.93E?03
2.92E?03
2.93E?03
2.94E?03
SD
6.63E?01
8.16E?01
2.15E?01
1.52E?01
1.77E?02
2.21E?02
2.63E?01
8.98E?01
2.33E?01
2.31E?01
3.49E?01
Median
3.06E?03
2.90E?03
2.94E?03
2.96E?03
3.41E?03
3.67E?03
2.94E?03
2.95E?03
2.94E?03
2.94E?03
2.94E?03
P Value (Wilcoxon)
1.69E-16
–
2.27E-03
2.03E-15
1.69E-16
1.69E-16
5.27E-11
4.76E-09
5.24E-02
6.65E-02
3.46E-05
26
Mean
3.19E?03
2.84E?03
2.99E?03
3.08E?03
3.04E?03
4.17E?03
3.09E?03
3.43E?03
3.00E?03
2.91E?03
3.06E?03
SD
4.36E?02
5.73E?01
2.46E?02
3.16E?01
7.41E?01
4.25E?02
1.94E?02
5.25E?02
3.18E?02
2.97E?01
1.41E?02
Median
3.06E?03
2.84E?03
2.90E?03
3.07E?03
3.03E?03
4.29E?03
3.04E?03
3.21E?03
2.90E?03
2.90E?03
3.08E?03
P Value (Wilcoxon)
4.70E-04
–
8.24E-05
1.69E-16
5.93E-13
1.69E-16
1.69E-16
1.08E-10
3.14E-06
3.56E-08
5.27E-11
27
Mean
3.19E?03
3.09E?03
3.11E?03
3.10E?03
3.12E?03
3.35E?03
3.10E?03
3.13E?03
3.10E?03
3.09E?03
3.12E?03
SD
4.30E?01
1.25E?00
3.52E?01
1.70E?00
1.52E?01
9.71E?01
2.00E?01
3.30E?01
1.17E?01
2.50E?00
3.08E?01
Median
3.19E?03
3.09E?03
3.10E?03
3.10E?03
3.11E?03
3.34E?03
3.10E?03
3.11E?03
3.10E?03
3.09E?03
3.11E?03
P Value (Wilcoxon)
1.69E-16
–
7.60E-06
1.69E-16
1.69E-16
1.69E-16
1.64E-14
5.07E-15
9.12E-12
4.70E-04
7.61E-15
28
Mean
3.59E?03
3.18E?03
3.39E?03
3.30E?03
3.57E?03
3.91E?03
3.37E?03
3.41E?03
3.32E?03
3.23E?03
3.26E?03
SD
1.58E?02
3.13E?01
2.39E?02
8.28E?01
2.44E?02
1.15E?02
8.47E?01
1.59E?02
1.32E?02
1.11E?02
1.05E?02
Median
3.63E?03
3.18E?03
3.40E?03
3.26E?03
3.60E?03
3.91E?03
3.41E?03
3.41E?03
3.41E?03
3.17E?03
3.22E?03
P Value (Wilcoxon)
4.20E-10
–
3.33E-02
1.13E-14
8.59E-14
1.69E-16
5.07E-15
7.36E-09
6.72E-04
7.72E-01
4.06E-04
Neural Computing and Applications (2024) 36:8007–8038
8031
123

---

## Page 26
second shafts. Schematic of the speed reducer design
problem is presented in Fig. 11.
The problem is mathematically formulated as:
x ¼ x1; x2; x3; x4; x5; x6; x7
½

ð40Þ
f x
ð Þ ¼ 0:7854x1x2
2  3:3333x2
3 þ 14:9334x3  43:0934


 1:508x1 x2
6 þ x2
7


þ 7:4777 x3
6 þ x3
7


þ 0:7854 x4x2
6 þ x5x2
7


ð41Þ
Constraints:
g1 x
ð Þ ¼
27
x1x2
2x3
 1  0;
g2 x
ð Þ ¼ 397:5
x1x2
2x2
3
 1  0;
g3 x
ð Þ ¼ 1:93x3
4
x2x3x4
6
 1  0;
g4 x
ð Þ ¼ 1:93x3
5
x2x3x4
7
 1  0;
g5 x
ð Þ ¼
1
110x3
6
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
745x4
x2x3

2
þ16:9  106
s
 1  0;
g6 x
ð Þ ¼
1
85x3
7
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
745x5
x2x3

2
þ157:5  106
s
 1  0;
g7 x
ð Þ ¼ x2x3
40  1  0;
g8 x
ð Þ ¼ 5x2
x1
 1  0;
g9 x
ð Þ ¼ x1
12x2
 1  0;
g10 x
ð Þ ¼ 1:5x6 þ 1:9
x4
 1  0;
g11 x
ð Þ ¼ 1:1x7 þ 1:9
x5
 1  0;
ð42Þ
Range of variables
2:6  x1  3:6; 0:7  x2  0:8; 17  x3  28; 7:3
 x4  8:3; 7:8  x5  8:3;
2:9  x6  3:9; 5  x7  5:5
The comparison of convergence curves of the algo-
rithms are shown in Fig. 12. According to results given in
Table 10, the proposed algorithm returns superior results
along with HBA.
4.4.5 Three bar truss design
Three bar truss design problem is a weight minimization
problem as shown in Fig. 13. Buckling, deﬂection, and
stress are constraints of the system.
Table 7 (continued)
Fun
Meas
AOA
MDAOA
HBA
SCA
BOA
PSOBOA
GJO
WOA
ALO
SSA
AOS
29
Mean
3.24E?03
3.16E?03
3.22E?03
3.23E?03
3.29E?03
3.52E?03
3.19E?03
3.35E?03
3.24E?03
3.21E?03
3.21E?03
SD
4.06E?01
1.89E?01
6.83E?01
2.85E?01
3.58E?01
1.09E?02
4.51E?01
1.19E?02
6.22E?01
5.84E?01
4.91E?01
Median
3.23E?03
3.15E?03
3.19E?03
3.23E?03
3.28E?03
3.52E?03
3.18E?03
3.34E?03
3.23E?03
3.20E?03
3.20E?03
P Value (Wilcoxon)
2.05E-13
–
5.43E-04
1.64E-14
1.69E-16
1.69E-16
2.41E-04
6.76E-16
7.96E-10
2.41E-04
6.20E-06
30
Mean
9.23E?05
5.53E?04
3.20E?06
9.26E?05
1.93E?06
4.51E?06
8.69E?05
1.33E?06
5.01E?05
4.11E?05
7.09E?05
SD
1.69E?06
4.42E?04
7.63E?06
5.58E?05
1.66E?06
7.52E?06
1.09E?06
1.87E?06
7.27E?05
8.76E?05
1.08E?06
Median
1.49E?05
4.18E?04
1.07E?06
8.49E?05
1.47E?06
2.73E?06
2.51E?05
4.90E?05
4.91E?04
2.98E?04
7.67E?04
P Value (Wilcoxon)
5.11E-03
–
9.90E-01
2.70E-13
1.69E-16
1.69E-16
7.38E-05
3.46E-05
9.90E-01
9.90E-01
7.72E-01
Friedman Mean Rank
6.12
1.38
3.12
7.64
9.14
10.45
5.95
8.07
4.86
4.07
5.21
Rank
7
1
2
8
10
11
6
9
4
3
5
Bold numbers indicate minimum values
8032
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 27
The mathematical formulation of the problem is:
x ¼ x1; x2
½
 ¼ A1; A2
½
; A1 ¼ A3
ð43Þ
f x
ð Þ ¼
2
ﬃﬃ
2
p
x1 þ x2
	

 L
ð44Þ
Constraints:
g1 x
ð Þ ¼
ﬃﬃ
2
p
x1 þ x2
ﬃﬃ
2
p
x2
1 þ 2x1x2
P  r  0;
g2 x
ð Þ ¼
x2
ﬃﬃ
2
p
x2
1 þ 2x1x2
P  r  0;
g3 x
ð Þ ¼
1
ﬃﬃ
2
p
x2 þ x1
P  r  0;
ð45Þ
Range of variables
0  x1  1; 0  x2  1
where
L ¼ 100 cm; P ¼ 2 kN=cm2; r ¼ 2 kN=cm2
The convergence curve of the problem for MDAOA and
the other algorithms are shown in Fig. 14. Results in
Table 10 shows that MDAOA returned the minimum result
for all functions.
5 Conclusion
In this study, a novel MDAOA optimization algorithm is
proposed based on modifying the AOA. The goal of the
modiﬁcation is to avoid early convergence and improve
balance between exploitation and exploration. This is
accomplished by two phase mechanism: optimizing the
candidate
positions
of
objects
using
the
dimension
Table 8 Comparison of results of the EVCS Placement Problem
Fun
Meas
AOA
MDAOA
HBA
SCA
BOA
PSOBOA
GJO
WOA
ALO
SSA
AOS
1
Mean
3.09E?02
3.00E?02
3.02E?02
3.03E?02
3.20E?02
3.27E?02
3.01E?02
3.07E?02
3.10E?02
3.14E?02
3.04E?02
SD
4.69E?00
9.51E-01
3.34E?00
2.76E?00
5.47E?00
5.05E?00
2.43E?00
6.41E?00
7.45E?00
6.93E?00
4.23E?00
Median
3.11E?02
3.00E?02
3.00E?02
3.01E?02
3.20E?02
3.26E?02
3.00E?02
3.07E?02
3.11E?02
3.14E?02
3.04E?02
P (Wilcoxon)
1.47E-09
–
3.52E-01
2.33E-04
4.08E-11
4.00E-11
8.51E?00
1.73E-07
1.86E-08
8.60E-11
4.67E-05
Friedman Mean Rank
6.62
2.57
3.57
4.26
9.67
10.76
2.83
5.78
6.88
8.38
4.69
Rank
7
1
3
4
10
11
2
6
8
9
5
Bold numbers indicate minimum values
Fig. 4 Convergence curves of EVCS Placement Problem
Neural Computing and Applications (2024) 36:8007–8038
8033
123

---

## Page 28
learning-based strategy and calculating predetermined ﬁve
parameters used in the original AOA.
MDAOA uses an additional measure to select the win-
ning object and update the existing location. The DL
strategy uses a diverse approach to form a neighborhood
for individual object in which neighborhood data can be
conveyed among other objects. The learning dimension
used in the proposed work can improve the balance
between exploitation and exploration by means of four
phases: initiation, movement/transfer, selection/updating,
and termination strategies.
In the second phase of modiﬁcation, ﬁve constant values
of AOA are computed by another optimization algorithm,
HBA. These parameters are computed once for each opti-
mization problem. Next, the new modiﬁed algorithm
MDAOA is applied to a wide range of problems. The
efﬁciency of the proposed algorithm is tested on 13 stan-
dard benchmark functions, 29 CEC 2017 benchmark
functions, optimal placement of EVCSs on the IEEE-33
distribution system and ﬁve real-life engineering problems.
Furthermore, results of the proposed modiﬁed algorithm
are compared with ten algorithms published in recent years.
Comparison includes statistical analysis employing Fried-
man test with Wilcoxon rank-sum as post hoc test for
pairwise comparisons. Experimental results and statistical
analysis indicate that MDAOA performed well with con-
sistently low standard deviation values. MDAOA returned
best results in all of 13 standard benchmarks, 26 of 29 CEC
2017 benchmarks (89.65%), optimal placement of EVCSs
problem and all of ﬁve real-life engineering problems.
Overall success rate is 45 out of 48 problems (93.75%).
Although MDAOA shared the lead for 13 functions, it was
the only algorithm that provided the best results for 32
functions. The algorithm presented in the study can be
especially used in engineering optimization studies as well
as constrained, unimodal, multimodal, hybrid, and com-
position functions.
Table 9 Problem parameters
Problem description
Lower bound
Upper bound
Dimension
f1
Tension/compression spring design [45, 46]
[0.05, 0.25, 2]
[2, 1.3, 15]
3
f2
Pressure vessel design [47]
[0,0, 10, 10]
[99, 99, 200, 200]
4
f3
Welded beam design [48]
[0.1, 0.1, 0.1, 0.1]
[2, 10]
4
f4
Speed reducer problem [49]
[2.6, 0.7, 17, 7.3, 7.8, 2.9, 5.0]
[3.6, 0.8, 28, 8.3, 8.3, 3.9, 5.5]
7
f5
Three bar truss design [50]
[0, 0]
[1]
2
Fig. 6 Convergence curves of tension/compression spring design
engineering problem
Fig. 5 Tension/compression spring design
8034
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 29
Table 10 Comparison of results of ﬁve engineering problems
Fun
Meas
AOA
MDAOA
HBA
SCA
BOA
PSOBOA
GJO
WOA
ALO
SSA
AOS
1
Mean
1.39E-02
1.27E-02
1.31E-02
1.30E-02
1.39E-02
1.41E-02
1.27E-02
1.35E-02
1.36E-02
1.30E-02
1.31E-02
SD
1.27E-03
9.40E-06
1.27E-03
1.14E-04
9.30E-04
1.29E-03
1.85E-05
1.11E-03
1.52E-03
5.09E-04
6.23E-04
Median
1.36E-02
1.27E-02
1.28E-02
1.30E-02
1.36E-02
1.34E-02
1.27E-02
1.31E-02
1.29E-02
1.28E-02
1.28E-02
P (Wilcoxon)
8.59E-14
–
4.31E-07
1.69E-16
1.69E-16
1.69E-16
6.31E-14
2.67E-09
1.13E-14
5.07E-15
2.05E-13
2
Mean
6.27E?04
5.90E?03
5.93E?03
6.81E?03
4.55E?04
5.96E?04
6.26E?03
7.77E?03
6.24E?03
6.89E?03
6.63E?03
SD
7.95E?04
1.46E?01
6.14E?01
5.06E?02
3.08E?04
3.61E?04
4.94E?02
1.10E?03
3.96E?02
1.91E?03
4.78E?02
Median
1.28E?04
5.90E?03
5.90E?03
6.75E?03
3.90E?04
4.90E?04
6.02E?03
7.49E?03
6.07E?03
6.38E?03
6.50E?03
P (Wilcoxon)
1.69E-16
–
9.99E-01
1.69E-16
1.69E-16
1.69E-16
4.58E-08
1.69E-16
9.16E-07
3.38E-16
1.16E-13
3
Mean
2.74E?00
1.72E?00
1.72E?00
1.86E?00
2.08E?10
3.20E?10
1.73E?00
2.29E?00
1.77E?00
1.80E?00
1.80E?00
SD
7.15E-01
8.46E-09
1.79E-05
3.69E-02
1.14E?11
1.28E?11
3.57E-03
6.72E-01
5.92E-02
7.90E-02
9.07E-02
Median
2.67E?00
1.72E?00
1.72E?00
1.86E?00
3.01E?00
4.72E?00
1.73E?00
2.09E?00
1.74E?00
1.77E?00
1.76E?00
P (Wilcoxon)
3.00E-10
–
4.97E-08
3.00E-10
3.00E-10
3.00E-10
3.00E-10
3.00E-10
3.00E-10
3.00E-10
3.00E-10
4
Mean
9.73E?09
2.99E?03
2.99E?03
3.10E?03
1.96E?11
3.18E?03
3.01E?03
3.17E?03
3.00E?03
3.04E?03
3.01E?03
SD
5.33E?10
5.40E-06
1.27E-12
3.03E?01
7.66E?11
4.51E?01
4.80E?00
2.08E?02
5.01E?00
2.70E?01
2.03E?01
Median
3.14E?03
2.99E?03
2.99E?03
3.09E?03
3.25E?03
3.19E?03
3.01E?03
3.13E?03
3.00E?03
3.03E?03
3.00E?03
P (Wilcoxon)
1.69E-16
–
9.17E-11
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
5
Mean
2.64E?02
2.64E?02
2.64E?02
2.64E?02
2.65E?02
2.71E?02
2.65E?02
2.64E?02
2.64E?02
2.64E?02
2.64E?02
SD
3.10E-04
9.45E-07
2.81E-05
5.14E-02
9.23E-01
5.27E?00
3.46E?00
3.29E-01
3.84E-04
6.28E-04
5.90E-02
Median
2.64E?02
2.64E?02
2.64E?02
2.64E?02
2.65E?02
2.70E?02
2.64E?02
2.64E?02
2.64E?02
2.64E?02
2.64E?02
P (Wilcoxon)
3.02E-10
–
5.34E-07
1.69E-16
1.69E-16
1.69E-16
1.69E-16
1.69E-16
3.89E-12
2.31E-09
1.69E-16
Friedman Mean Rank
8.50
2.20
2.70
6.60
10.30
10.40
3.50
7.40
4.50
5.20
4.70
Rank
9
1
2
7
10
11
3
8
4
6
5
Bold numbers indicate minimum values
Neural Computing and Applications (2024) 36:8007–8038
8035
123

---

## Page 30
Fig. 7 Pressure vessel design problem
Fig. 8 Convergence curves of Pressure vessel design problem
Fig. 9 Schematic of welded beam design problem
Fig. 10 Convergence curves of Welded beam design problem
Fig. 11 Schematic of speed reducer design problem
Fig. 12 Convergence curves of speed reducer design problem
8036
Neural Computing and Applications (2024) 36:8007–8038
123

---

## Page 31
Proposed method improves the performance of the
original AOA; however, it requires a preprocessing for
parameter optimization using another algorithm. Future
studies can be conducted to eliminate this step to develop a
self-adaptive approach. In addition, more real-life opti-
mization problems such as the optimal placement of
EVCSs problem solved in this study can be identiﬁed in
order to be optimized by MDAOA.
Acknowledgements This research is supported by Inonu University—
the Scientiﬁc Research Projects (BAP) Unit (No. FDK-2023-3163). The
Authors would like to thank Dr. Ahmet Kadir Arslan for comments and
discussions which helped improving the quality of the paper.
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
1. JH Holland 1992 Genetic algorithms Sci Am 267 66 73
2. Kennedy J, Eberhart R (1995) Particle swarm optimization. In:
Proceedings of ICNN’95—ınternational conference on neural
networks, vol 4, pp 1942–1948. https://doi.org/10.1109/ICNN.
1995.488968
3. F Glover 1987 Tabu search methods in artiﬁcial intelligence and
operations research ORSA Artiﬁcial Intelligence Newsletter
4. S Mirjalili A Lewis 2016 The Whale optimization algorithm Adv
Eng Softw 95 51 67 https://doi.org/10.1016/j.advengsoft.2016.01.
008
5. FA Hashim K Hussain EH Houssein MS Mabrouk W Al-Atabany
2021 Archimedes optimization algorithm: a new metaheuristic
algorithm for solving optimization problems Appl Intell 51 3
1531 1551 https://doi.org/10.1007/s10489-020-01893-z
6. I Matousˇova´ P Trojovsky´ M Dehghani E Trojovska´ J Kostra 2023
Mother optimization algorithm: a new human-based meta-
heuristic approach for solving engineering optimization Sci Rep
13 1 1 26 https://doi.org/10.1038/s41598-023-37537-8
7. S Mirjalili AH Gandomi SZ Mirjalili S Saremi H Faris SM
Mirjalili 2017 Salp Swarm Algorithm: a bio-inspired optimizer
for engineering design problems Adv Eng Softw 114 163 191
https://doi.org/10.1016/j.advengsoft.2017.07.002
8. FA Hashim EH Houssein K Hussain MS Mabrouk W Al-Atabany
2022 Honey Badger Algorithm: New metaheuristic algorithm for
solving optimization problems Math Comput Simul 192 84 110
https://doi.org/10.1016/j.matcom.2021.08.013
9. S Mirjalili 2016 SCA: a Sine Cosine Algorithm for solving
optimization problems Knowl-Based Syst 96 120 133 https://doi.
org/10.1016/j.knosys.2015.12.022
10. S Arora S Singh 2019 Butterﬂy optimization algorithm: a novel
approach for global optimization Soft Comput 23 3 715 734
https://doi.org/10.1007/s00500-018-3102-4
11. N Chopra M Mohsin Ansari 2022 Golden jackal optimization: a
novel nature-inspired optimizer for engineering applications
Expert Syst Appl 198 116924 https://doi.org/10.1016/j.eswa.
2022.116924
12. E Trojovska M Dehghani P Trojovsky 2022 Fennec fox opti-
mization: a new nature-inspired optimization algorithm IEEE
Access 10 84417 84443 https://doi.org/10.1109/ACCESS.2022.
3197745
13. FA Zeidabadi SA Doumari M Dehghani Z Montazeri P Tro-
jovsky´ G Dhiman 2022 MLA: a new mutated leader algorithm for
solving optimization problems Comput Mater Contin 70 3 5631
5649 https://doi.org/10.32604/cmc.2022.021072
14. SA Doumari H Givi M Dehghani Z Montazeri V Leiva JM
Guerrero 2021 A new two-stage algorithm for solving opti-
mization problems Entropy 23 4 1 17 https://doi.org/10.3390/
e23040491
Fig. 14 Convergence curves of three bar truss design problem
Fig. 13 Schematic of three bar truss design problem
Neural Computing and Applications (2024) 36:8007–8038
8037
123

---

## Page 32
15. M Azizi 2021 Atomic orbital search: a novel metaheuristic
algorithm Appl Math Model 93 657 683 https://doi.org/10.1016/j.
apm.2020.12.021
16. DH Wolpert WG Macready 1997 No free lunch theorems for
optimization IEEE Trans Evol Comput 1 1 67 82
17. H Liu S Duan H Luo 2022 A hybrid engineering algorithm of the
seeker algorithm and particle swarm optimization Mater Test 64
7 1051 1089 https://doi.org/10.1515/mt-2021-2138
18. J Luo B Shi 2019 A hybrid whale optimization algorithm based
on modiﬁed differential evolution for global optimization prob-
lems Appl Intell 49 5 1982 2000 https://doi.org/10.1007/s10489-
018-1362-4
19. M Zhang D Long T Qin J Yang 2020 A chaotic hybrid butterﬂy
optimization algorithm with particle swarm optimization for
high-dimensional optimization problems Symmetry (Basel) 12 11
1 27 https://doi.org/10.3390/sym12111800
20. I Neggaz N Neggaz H Fizazi 2022 Boosting Archimedes opti-
mization algorithm using trigonometric operators based on fea-
ture selection for facial analysis Neural Comput Appl https://doi.
org/10.1007/s00521-022-07925-8
21. P Niu Y Ma S Yan 2019 A modiﬁed teaching–learning-based
optimization algorithm for numerical function optimization Int J
Mach Learn Cybern 10 6 1357 1371 https://doi.org/10.1007/
s13042-018-0815-8
22. Y Ma X Zhang J Song L Chen 2021 A modiﬁed teaching–
learning-based optimization algorithm for solving optimization
problem Knowl-Based Syst 212 106599https://doi.org/10.1016/j.
knosys.2020.106599
23. Y Zhang X Zhou PC Shih 2020 Modiﬁed Harris Hawks opti-
mization algorithm for global optimization problems Arab J Sci
Eng 45 12 10949 10974 https://doi.org/10.1007/s13369-020-
04896-7
24. S Kumar S Apu K Saha S Nama M Masdari 2022 An improved
moth ﬂame optimization algorithm based on modiﬁed dynamic
opposite learning strategy Springer
25. S Sharma S Chakraborty A Kumar S Sukanta N Saroj K Sahoo
2022 mLBOA: A modiﬁed butterﬂy optimization algorithm with
lagrange interpolation for global optimization J Bionic Eng 19 4
1161 1176 https://doi.org/10.1007/s42235-022-00175-3
26. Y Zhou F Ge G Dai Q Yang H Zhu N Yousseﬁ2022 Modiﬁed
arithmetic optimization algorithm : a new approach for optimum
modeling of the CCHP system J Electr Eng Technol https://doi.
org/10.1007/s42835-022-01140-0
27. AM Shaheen AM Elsayed RA El-Sehiemy SSM Ghoneim MM
Alharthi AR Ginidi 2022 Multi-dimensional energy management
based on an optimal power ﬂow model using an improved quasi-
reﬂection jellyﬁsh optimization algorithm Eng Optim https://doi.
org/10.1080/0305215X.2022.2051021
28. S Kumar A Sikander 2022 A modiﬁed probabilistic roadmap
algorithm for efﬁcient mobile robot path planning Eng Optim
https://doi.org/10.1080/0305215X.2022.2104840
29. LM Thi TT Mai Anh N Van Hop 2022 An improved hybrid
metaheuristics and rule-based approach for ﬂexible job-shop
scheduling subject to machine breakdowns Eng Optim https://doi.
org/10.1080/0305215X.2022.2098283
30. X Gan J Pei W Wang S Yuan B Lin 2022 Application of a
modiﬁed MOPSO algorithm and multi-layer artiﬁcial neural
network in centrifugal pump optimization Eng Optim https://doi.
org/10.1080/0305215X.2021.2015585
31. Z Tang 2022 Enhancing the search ability of a hybrid LSHADE
for global optimization of interplanetary trajectory design Eng
Optim https://doi.org/10.1080/0305215X.2021.2019250
32. J Jelovica Y Cai J Jelovica 2022 Improved multi-objective
structural optimization with adaptive repair-based constraint
handling repair-based constraint handling Eng Optim https://doi.
org/10.1080/0305215X.2022.2147518
33. KW Huang ZX Wu CL Jiang ZH Huang SH Lee 2023 WPO: a
whale particle optimization algorithm Int J Comput Intell Syst
https://doi.org/10.1007/s44196-023-00295-6
34. M Yassami P Ashtari 2023 A novel hybrid optimization algo-
rithm: dynamic hybrid optimization algorithm Multimed Tools
Appl https://doi.org/10.1007/s11042-023-14444-8
35. O Akdag 2022 A ımproved archimedes optimization algorithm
for multi/single-objective optimal power ﬂow Electr Power Syst
Res 206 107796 https://doi.org/10.1016/j.epsr.2022.107796
36. S Suganya SC Raja P Venkatesh 2017 Simultaneous coordination
of distinct plug-in Hybrid Electric Vehicle charging stations: a
modiﬁed Particle Swarm Optimization approach Energy 138 92
102 https://doi.org/10.1016/j.energy.2017.07.036
37. QM Alzubi M Anbar Y Sanjalawe MA Al-Betar R Abdullah
2022 Intrusion detection system based on hybridizing a modiﬁed
binary grey wolf optimization and particle swarm optimization
Expert Syst Appl 204 117597 https://doi.org/10.1016/j.eswa.
2022.117597
38. M Nurmuhammed O Akdag T Karadag 2023 A novel modiﬁed
Archimedes optimization algorithm for optimal placement of
electric
vehicle
charging
stations
in
distribution
networks
Alexandria Eng J 84 81 92 https://doi.org/10.1016/j.aej.2023.10.
055
39. Kaur N (2021) DLHO-: an enhanced version of harris hawks
optimization by dimension learning-based hunting for breast
cancer and other serious diseases detection, pp 0–40
40. MH Nadimi-shahraki S Taghian S Mirjalili 2021 An improved
grey wolf optimizer for solving engineering problems Expert Syst
Appl 166 113917 https://doi.org/10.1016/j.eswa.2020.113917
41. S Mirjalili 2015 The ant lion optimizer Adv Eng Softw 83 80 98
https://doi.org/10.1016/j.advengsoft.2015.01.010
42. M Friedman 1937 The use of ranks to avoid the assumption of
normality implicit in the analysis of variance J Am Stat Assoc 32
200 675 701 https://doi.org/10.1080/01621459.1937.10503522
43. Awad NH, Ali MZ, Suganthan PN, Liang JJ, Qu BY (2017)
Problem deﬁnitions and evaluation criteria for the CEC 2017
44. S Deb K Tammi K Kalita P Mahanta 2018 Impact of electric
vehicle charging station load on distribution network Energies 11
1 1 25 https://doi.org/10.3390/en11010178
45. JS Arora 1989 Introduction to optimum design McGraw-Hill
New York
46. Belegundu AD, ARORA JS (1982) A study of mathematical
programming methods for structural optimization[Ph. D. Thesis]
47. Kannan SNKBK (1994) An augmented Lagrange multiplier
based method for mixed integer discrete continuous optimization
and its applications to mechanical design. J Mech Des Trans
ASME
48. SS Rao 1996 Engineering optimization 3 Wiley
49. E Sandgren 1990 Nonlinear integer and discrete programming in
mechanical design optimization ASME J Mech Des 112 223 322
50. T Ray P Saini 2001 Engineering design optimization using a
swarm with an intelligent information sharing among individuals
Eng
Optim
33
6
735
748
https://doi.org/10.1080/
03052150108940941
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
8038
Neural Computing and Applications (2024) 36:8007–8038
123

---
