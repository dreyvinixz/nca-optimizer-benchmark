# Efficient economic operation based on load dispatch of power systems using a leader white shark optimization algorithm

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-09612-2

---

## Page 1
ORIGINAL ARTICLE
Efficient economic operation based on load dispatch of power systems
using a leader white shark optimization algorithm
Mohamed H. Hassan1 • Salah Kamel2 • Ali Selim2 • Abdullah Shaheen3 • Juan Yu4 • Ragab El-Sehiemy5
Received: 1 February 2023 / Accepted: 19 February 2024 / Published online: 27 March 2024
 The Author(s) 2024
Abstract
This article proposes the use of a leader white shark optimizer (LWSO) with the aim of improving the exploitation of the
conventional white shark optimizer (WSO) and solving the economic operation-based load dispatch (ELD) problem. The
ELD problem is a crucial aspect of power system operation, involving the allocation of power generation resources to meet
the demand while minimizing operational costs. The proposed approach aims to enhance the performance and efﬁciency of
the WSO by introducing a leadership mechanism within the optimization process, which aids in more effectively navi-
gating the complex ELD solution space. The LWSO achieves increased exploitation by utilizing a leader-based mutation
selection throughout each generation of white sharks. The efﬁcacy of the proposed algorithm is tested on 13 engineer
benchmarks non-convex optimization problems from CEC 2020 and compared with recent metaheuristic algorithms such
as dung beetle optimizer (DBO), conventional WSO, fox optimizer (FOX), and moth-ﬂame optimization (MFO) algo-
rithms. The LWSO is also used to address the ELD problem in different case studies (6 units, 10 units, 11 units, and 40
units), with 20 separate runs using the proposed LWSO and other competitive algorithms being statistically assessed to
demonstrate its effectiveness. The results show that the LWSO outperforms other metaheuristic algorithms, achieving the
best solution for the benchmarks and the minimum fuel cost for the ELD problem. Additionally, statistical tests are
conducted to validate the competitiveness of the LWSO algorithm.
Keywords Economic load dispatch  White shark optimizer  Optimization algorithms  Leader strategy
& Ragab El-Sehiemy
elsehiemy@eng.kfs.edu.eg
Mohamed H. Hassan
mohamedhosnymoee@gmail.com
Salah Kamel
skamel@aswu.edu.eg
Ali Selim
ali.selim@aswu.edu.eg
Abdullah Shaheen
abdullahshaheen2015@gmail.com
Juan Yu
yujuancqu@qq.com
1
Ministry of Electricity and Renewable Energy, Cairo, Egypt
2
Department of Electrical Engineering, Faculty of
Engineering, Aswan University, Aswan 81542, Egypt
3
Department of Electrical Power Engineering, Faculty of
Engineering, Suez University, Suez 43533, Egypt
4
State Key Laboratory of Power Transmission Equipment and
System Security and New Technology, College of Electrical
Engineering, Chongqing University, Chongqing, China
5
Department of Electrical Engineering, Faculty of
Engineering, Kafrelsheikh University, Kafrelsheikh 33516,
Egypt
123
Neural Computing and Applications (2024) 36:10613–10635
https://doi.org/10.1007/s00521-024-09612-2
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
1 Introduction
As is widely recognized, the extensive and reckless
exploitation and allocation of power and other energy
sources has led to limited and expensive resources,
resulting in signiﬁcant resource wastage and gradual
impacts on social life. Therefore, it is imperative to make
efﬁcient and rational use of these limited energy resources.
Utilizing energy and fostering innovation in energy-related
areas have always been crucial factors in economic
development and ensuring livelihood security. In particu-
lar, the rational and effective distribution of large-scale
power resources is of utmost signiﬁcance [1]. Economic
load dispatch (ELD) is a crucial matter for power system
operations. The ELD aims to reduce fuel costs while ful-
ﬁlling inequality and equality constraints. Equality con-
straints are based on the stability of power between the
productions of the system and the whole demand with
transmission losses. Inequality constraints are based on
power output [2]. Many traditional approaches have been
proposed to solve ELD problems as linear programming,
nonlinear programming, and mixed integer linear pro-
gramming [3]. Nevertheless, the real-world system presents
several signiﬁcant considerations, including factors such as
the valve-point effect, transmission losses, and the inherent
nonlinearity of the generator set. ELD scheduling involves
non-convex optimization challenges, making it exceed-
ingly challenging to address these nonlinear problems
using conventional mathematical approaches. Recently,
metaheuristic techniques are widely used to solve the ELD
problem [4]. In both unimodal and multimodal problems,
exploration and exploitation can be accomplished using
mathematical equations, which are implemented using
speciﬁc techniques. However, the requirements for these
techniques may differ depending on the problem at hand.
Metaheuristic algorithms are employed to solve various
optimization problems [5–7]. The earliest algorithm used to
solve the ELD problem is a genetic algorithm (GA) and its
variants [8], particle swarm optimization (PSO) technique
its variants [9], an improved slime mold algorithm (ISMA)
algorithm [10], and artiﬁcial cooperative search (ACS)
algorithm in [11].
Recently, numerous metaheuristic algorithms have been
established to solve the ELD problem, such as the evolu-
tionary simplex adaptive Hooke–Jeeves algorithm [12],
opposition-mutual
learning differential evolution with
hybrid mutation strategy [13], hybrid gray wolf optimizer
(HGWO)
[14],
improved
ﬁtness-dependent
optimizer
(IFDO) [15], a multigroup marine predator algorithm [16],
chaotic
eagle-strategy
supply–demand
optimizer
(CESSDO) [17], a chaotic slime mold algorithm (CSMA)
[18], and
elementary function disturbance
arithmetic
optimization technique (EFDAO) [19]. In 2018, Singh
et al. suggested an enhanced gray wolf optimizer (GWO) to
solve the ELD problem in collaboration with exploration
and exploitation, which coordinates the behavior of gray
wolf, random search, local random search, and reverse
learning heuristic [20]. In [21], the sine–cosine algorithm
was applied to solve the ELD problem. A comparative
analysis to assess the behaviors of hurricane and sine-
cosine optimizers was carried out for solving the ELD with
considering the ecological emissions [22]. The enhanced
moth-ﬂame optimization algorithm was presented in [23]
to solve different sizes of ELD problem considering the
emission minimization. The enhanced social network
search (ESNS) was suggested to solve the ELD problem
using high- and low-velocity ratio approach to improve the
searching balance between exploration and exploitation of
each solution in [24]. In 2020, Ling et al. proposed the
shrinking
Gaussian
distribution
quantum
performance
optimization algorithm (SG-QPSO) to solve the ELD
problem. By iteratively reducing the Gaussian probability
distribution near the learning tendency point of each par-
ticle, SG-QPSO maintains a strong global search ability at
the beginning and gradually enhances the local search
ability
[25].
To
overcome
the
ELD
difﬁculties,
an
enhanced arithmetic optimization is suggested. There are
two crucial variables in the arithmetic optimization algo-
rithm (AOA) math optimizer acceleration and probability
[26]. It can be seen from the above literature that intelligent
optimization algorithms were used to solve the ELD
problem. Some directly use the original algorithm to solve
the ELD problem, and some use some strategies to opti-
mize the original algorithm to enhance its performance. It
achieved better results in solving the ELD problem. A
comparative study is shown in Table 1 to keep track of
algorithms and their evaluation on standard test systems.
Recently, the white shark optimizer (WSO) has been
suggested to emulate the manners of white sharks, con-
taining their unique intelligences of audible range and
smell when navigating and hunting [46]. In this article, an
effective WSO algorithm is employed to achieve the
optimal solution for the ELD problem. The main reason for
choosing this algorithm in this article is that it has a few
adjustable parameters that have been implemented easily.
This characteristic makes it very potential for applications
in many engineering ﬁelds. In [47], the WSO approach is
applied in OPF solution of power systems with renewable
energy sources. The WSO technique is suffering from
slowing the convergence rate and falling in the local
optima because of unbalance between the exploration and
exploitation
process.
Therefore,
the
traditional
WSO
algorithm needs to be further improved [48]. Thus, the
authors in this work aim to achieve a ﬁne balance between
them using the leader-based mutation-selection approach to
10614
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 3
get more promising results than those gained from the
conventional WSO algorithm, and it can improve search
accuracy and extend global search capabilities.
The ELD problem has received signiﬁcant attention in
recent decades, as highlighted in the summary above.
Although various optimization approaches have been pro-
posed to tackle ELD problems. This article speciﬁcally
focuses on integrating algorithm and constraint processing
technology to address the ELD problems. In the context of
constraint
optimization
problems,
constraint-handling
techniques are just as crucial as algorithm design, as such
problems require managing both ﬁtness function and the
degree of constraint violation. Building on the considera-
tions, a leader white shark optimizer (LWSO) is presented
to solve the ELD problem. By incorporating a leader-based
mutation-selection strategy, the LWSO algorithm aims to
not only optimize the objective function but also effec-
tively manage the constraints involved in the problem. This
leader-based approach enables the algorithm to adapt to
changing dynamics in the optimization landscape and
ensures that the solution obtained adheres to the problem’s
constraints, enhancing the overall robustness of the ELD
optimization process. Furthermore, the LWSO algorithm
provides a promising avenue for further advancements in
solving complex optimization problems, by striking a
balance between exploration and exploitation to achieve
more accurate and globally competitive solutions. The vital
contributions of the article could be brief as below:
•
Applying the proposed LWSO to solve the ELD
problem;
•
Four test networks with 6-, 10-, 11-, and 40-hermal
units are used to conﬁrm the LWSO performance;
•
Comparison between the LWSO and other recent
algorithms such as the Golden Jackal Optimization
(GJO), Northern Goshawk Optimization (NGO), fox
optimizer (FOX), and conventional WSO algorithms
and other literature algorithms such as the Improved
slime mold algorithm (ISMA), tunicate swarm algo-
rithm (TSA), Harris Hawks optimizer (HHO), slime
mold algorithm (SMA), jellyﬁsh search optimizer (JS),
and PSO algorithms is performed.
Table 1 Comparative study of several algorithms and their evaluation on standard test systems
Methodology
Test systems
3 units
6 units
10 units
11 units
13 units
15 units
20 units
40 units
Biogeography-based optimization (BBO) [27]
4
4
4
Cultural self-organizing migrating algorithm (CSOMA) [28]
4
4
Adaptive real coded genetic algorithm (ARCGA) [29]
4
4
Modiﬁed differential evolution (MDE)[30]
4
4
4
Artiﬁcial bee colony algorithm (ABC) [31]
4
4
4
4
Fireﬂy algorithm (FA) [32]
4
4
4
Novel direct search method (NDS) [33]
4
4
4
Novel stochastic search method (NSS) [34]
4
4
4
Seeker optimization algorithm (SOA) [35]
4
Group search optimizer (GSO)[36]
4
4
Sensing cloud optimization (SCO) [37]
4
4
Shufﬂed differential evolution (SDE) [38]
4
4
4
Real coded chemical reaction optimization (RCCRO) [39]
4
Chaotic bat algorithm (CBA) [40]
4
4
4
Hybrid gray wolf optimizer (HGWO) [41]
4
4
4
Improved adaptive differential evolution optimizer (IADE)
[42]
4
4
Equilibrium optimizer (EO) [43]
4
4
4
Clustering cuckoo search optimization (CCSO) [44]
4
4
4
4
4
Hybrid salp swarm algorithm (HSSA) [2]
4
4
4
Chaotic slime mold algorithm (CSMA) [18]
4
4
4
4
Enhanced beluga whale optimization (EBWO) [45]
4
4
Improved slime mold algorithm (ISMA) [10]
4
4
4
4
Neural Computing and Applications (2024) 36:10613–10635
10615
123

---

## Page 4
•
Statistical analysis is performed for 20 trails of studied
techniques, and the strength and convergence rates for
LWSO are discussed.
The rest of the paper is arranged as Sect. 2 presents the
ELD problem’s mathematical model; the original WSO
and the proposed LWSO techniques are explained in
Sect. 3; the results and discussions are shown in Sect. 4;
and ﬁnally, Sect. 5 presents conclusion of the article.
2 Mathematical model of ELD problem
The fuel cost function for this problem follows a quadratic
form, and the total fuel costs take into account the valve-
point effects in accordance with the output of thermal
generations while satisfying their respective constraints.
The function can be expressed as follows [49]:
F1 ¼
X
NG
i¼1
ai þ biPGi þ ciP2
Gi þ di sin ei Pmin
Gi  PGi








ð1Þ
where ai; bi; and ci are the cost coefﬁcients for the ith unit;
Pi refers to the power output of these units; and NG denotes
the number of generations.
The balance of power constraint in this problem ensures
that the total output power generation PT (in MW) is equal
to the sum of the total load demand PD (in MW) and the
power loss PLoss (in MW) in the entire system. This
equality constraint can be mathematically represented as
follows [50]:
PT ¼
X
NG
i1
PGi ¼ PD þ PLoss;
ð2Þ
PLoss denotes the active output power of the units, and it
can be calculated from Kron’s loss formula as below:
PLoss ¼
X
NG
i¼1
X
NG
j¼1
PGiBijPGj þ
X
NG
i¼1
B0iPGi þ B00;
ð3Þ
where Boo, Boi, and Bij refer to the coefﬁcients of the power
loss.
The inequality bound is attained during each thermal
generator works within its operating constraints as follows:
Pmin
Gi  PGi  Pmax
Gi ;
ð4Þ
where Pmin
Gi ,, and Pmax
Gi
represent the operating bounds of
generator i.
The constraint violation can be expressed as follows [51]:
V ¼
X
NG
i¼1
PGi  PD  PLoss


ð5Þ
3 Methodology
3.1 Conventional WSO
The WSO algorithm is inspired by the behaviors of the
white sharks when hunting to assist them to live in the
ocean depths [46]. Its results prove its strength in solving
different types of optimization problems. Therefore, the
WSO provides numerous advantages for composite opti-
mization problems. The models of the WSO algorithm
determine the optimal value of the fuel cost. This section
brieﬂy
describes
the
basics
of
the
proposed
WSO
algorithm.
3.1.1 Initialization of WSO
The initialization position of each white shark can be cal-
culated from the following equation [47]:
w ¼
w1
1
w1
2
. . . ::
w1
d
w2
1
w2
2
. . . ::
w2
d
. . . :
. . . :
. . . ::
. . . ::
wn
1
wn
2
. . . ::
wn
d
2
664
3
775
ð6Þ
In this context, the variable w represents the position of
the white sharks in the search area, while the variable
d represents the number of variables in the problem.
3.1.2 Update the parameters of the WSO algorithm
v ¼ n  randð1; nÞ
½
 þ 1
ð7:1Þ
p1 ¼ pmax þ pmax  pmin
ð
Þ  eð4k
KÞ2
ð7:2Þ
p2 ¼ pmin þ pmax  pmin
ð
Þ  eð4k
KÞ2
ð7:3Þ
l ¼
2
2  s 
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
s2  4s
p


ð7:4Þ
a ¼ sgnðw j
k  uÞ [ 0
ð7:5Þ
b ¼ sgnðw j
k  uÞ\0
ð7:6Þ
w0 ¼  a; b
ð
Þ
ð7:7Þ
f ¼ fmin þ fmax  fmin
fmax þ fmin
ð7:8Þ
mv ¼
1
a0 þ eðk
2KÞ=a1
ð7:9Þ
SS ¼ 1  eða2k
KÞ


ð7:10Þ
where v refers to the white sharks’ index vector getting the
optimal location deﬁned p1 and p2 denote the white sharks’
forces, and l denotes the constriction factor proposed in
WSO. a and b refer to one-dimensional binary vectors w0
10616
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 5
denotes a logical vector. f represents the frequency of the
white shark’s wavy motion. mv denotes the movement
force which is related to the number of iterations. ss
denotes a parameter proposed to rapid the sense’s strength
of smell and sight of the sharks during following other
white sharks that are close to optimum prey.
3.1.3 Speed of movement to prey
When a white shark identiﬁes a prey’s position using
hearing a pause in the waves because the prey moves, as
below:
ui
kþ1 ¼ l ui
k þ p1 wgbestk  wi
k


 c1 þ p2 w
vi
k
best  wi
k

	
 c2
h
i
ð8Þ
the new rapidity vector of the ith shark can be represented
by vi
k?1.
3.1.4 Movement in the best prey’s way
In this scenario, the movement of sharks as their approa-
ched ﬁsh was depicted.
wi
kþ1 ¼
wi
k: ! w0 þ u:a þ l:b; rand\mv
wi
k þ ui
k=f; rand  mv
(
ð9Þ
3.1.5 Movement in the way of the best shark
Equation (10) expresses how the white sharks can maintain
their position ahead of the most beneﬁcial one that is closer
to the goal. This phenomenon is achieved through the
following equation:
wi
k¼1
0
¼ wgbestk þ r1D~wsgnðr2  0:5Þ r3\Ss
ð10Þ
w´i
k?1 is the upgraded shark’s location, sgn(r2 - 0.5)
returns 1 or -1 to adapt the search track, and r1, r2 and r3
are the random values. Dw denotes the length for both goal
and shark, and it can be calculated as follows:
D
!
w ¼ rand  wgbest  wi
k




ð11Þ
The ﬂowchart of the WSO algorithm is shown in Fig. 1.
3.2 The procedure of the improved LWSO
algorithm
The proposed method to address the possibility of the
optimum value dropping into local minima is called leader-
based mutation selection [52]. This modiﬁcation relies on
the best position vector (witer
best1), the second-best position
vector (witer
best1), and the third-best position vector (xt
best2)
based on their objective function values for the new posi-
tion vector (wi new
ð
Þ) between the members of the popu-
lation. The new mutation position vector (wi mut
ð
Þ) is
calculated using the following equation:
wi mut
ð
Þ ¼ wi new
ð
Þ þ 2 
1 
iter
Max iters


 2  rand  1
ð
Þ 2  witer
best

 witer
best1 þ witer
best2


Þ þ 2  rand  1
ð
Þ witer
best  wi new
ð
Þ


ð12Þ
After that, the following location is reorganized as
follows:
wi iter þ 1
ð
Þ ¼
wi mut
ð
Þf wi mut
ð
Þ
ð
Þ\f wi new
ð
Þ
ð
Þ
wi new
ð
Þf wi mut
ð
Þ
ð
Þ  f wi new
ð
Þ
ð
Þ

ð13Þ
Lastly, the optimal solution is updated by the following
equation:
wbest ¼
wi mut
ð
Þf wi mut
ð
Þ
ð
Þ\f wbest
ð
Þ
wi new
ð
Þf wi new
ð
Þ
ð
Þ\f wbest
ð
Þ

ð14Þ
Figure 2 displays the ﬂowchart of the LWSO algorithm,
which includes the residence of the leader-based mutation
selection. Moreover, Algorithm 1 describes the LWSO
algorithm’s pseudocode. This improvement enhances the
exploration of the LWSO technique through simultaneous
crossover and mutation using the three best leaders. The
combination of crossover and mutation in genetic algo-
rithms is a powerful strategy to address trapping and slow
convergence. Crossover facilitates the sharing of valuable
genetic information, while mutation introduces randomness
and diversity, collectively promoting a more effective and
efﬁcient exploration–exploitation trade-off. The proposed
LWSO algorithm offers several advantages over the orig-
inal WSO technique:
The advantages of LWSO can be concluded as follows:
1.
Enhanced Exploration: Simultaneous crossover and
mutation using the three best leaders can lead to
increased diversity in the search space. This enhance-
ment allows the algorithm to explore a wider range of
solutions, potentially leading to better optimization
outcomes.
2.
Improved Convergence: Combining crossover and
mutation can help the algorithm converge faster to
better solutions. Crossover promotes the sharing of
genetic information between solutions, while mutation
introduces random variations that can help escape local
optima.
3.
Better Solution Quality: By leveraging the best leaders,
the algorithm can focus on the most promising regions
of the search space, increasing the likelihood of ﬁnding
high-quality solutions.
Neural Computing and Applications (2024) 36:10613–10635
10617
123

---

## Page 6
Start
Inialize the parameter of the
problem and the WSO algorithm
Generate random populaon of
the WSO
While
iter< Max_iters
Return best WSO
posion
End
Generate the inialposion of
the WSO
Inialize the velocity of the
inialpopulaon
Evaluate the posion of the
inial populaon
Updatetheparameters ν, p1,
p2, μ, a, b, wo, f , mv and ss
using Equaon (7)
update the velocity using
Equaon (8)
update the posion of the
WSO using Equaon (9)
Adjust the posion of the WSO
that proceed beyond the
boundary
Evaluate and update the new
posions
Yes
No
Fig. 1 The ﬂowchart of the proposed WSO algorithm
Start
Inialize the parameter of the 
problem and the WSO algorithm 
Generate random populaon of 
the WSO 
While 
iter< Max_iters
Return best WSO 
posion
End
Generate the inial posion of 
the WSO
Inialize the velocity of the 
inial populaon
Evaluate the posion of the 
inial populaon
Update the parameters v, p1, 
p2, μ, a, b, wo, f , mv, and ss  
using Equaon (7)
update the velocity using 
Equaon (8)
update the posion of the 
WSO using Equaon (9)
Adjust the posion of the WSO 
that proceed beyond the 
boundary
Evaluate and update the new 
posions
No
(Leader-based mutation-selection  )
Update the best soluon 
found so far xbest using Eq. 
(14)
Update the posion of each 
individual using Eq. (12) 
Evaluate the objecve 
funcon value of each 
individual using Eq. (13) 
Yes
Fig. 2 Flowchart of proposed LO algorithm
10618
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 7
However, like any algorithm, LWSO may have its own
shortcomings. One potential disadvantage of the proposed
LWSO algorithm could be:
Increased
Computational
Complexity:
Simultaneous
crossover and mutation can signiﬁcantly increase the com-
putational requirements of the algorithm. This can lead to
longer execution times and higher resource usage, making it
less suitable for problems with strict time or resource con-
straints.
Algorithm 1: Pseudocode of the LWSO algorithm
3.3 Analysis of algorithm computational
complexity
The time complexity of the proposed LWSO algorithm
depends on the population size (N), the maximum number
of iterations (T), the dimensions of the problem (D), and
the function assessment’s cost (C). In the original WSO,
the time complexity of initializing the population is O(N x
D). The time complexity of the assessment of the cost
function demands is O(N x C x T). The time complexity of
updating positions is O(N x D x T). Therefore, the general
Neural Computing and Applications (2024) 36:10613–10635
10619
123

---

## Page 8
time complexity of WSO is O(N x D ? N x C x D ? N x
D x T). The time complexity of LWSO is O(2 9 N x D x
T ? N x D ? N x D x T).
3.4 Taxonomy of leader-based mutation
selection
Forming a taxonomy for leader-based mutation selection
includes categorizing and organizing the key elements
related to this speciﬁc optimization technique. Figure 3
shows a taxonomy for leader-based mutation selection.
4 Simulation results and discussion
4.1 Simulation results of real-world engineering
problems
To evaluate the performance of the LWSO algorithm
in
solving
the
real-world
non-convex,
constrained
leader-based mutation selection
Mutation Strategy
Leader Selection 
Criteria
Leader-Follower 
Strategy
Adaptive 
Mutation
Fitness-Based 
Leader Selection
Diversity-Based 
Leader Selection
Frequency of 
Mutation
Impact on 
Convergence
Constant 
Mutation Rate
Dynamic 
Mutation Rate
Enhanced 
Exploitation
Balanced 
Exploration and 
Exploitation
Application 
Domains
Single-Objective 
Optimization
Multi-Objective 
Optimization
Fig. 3 The taxonomy of leader-based mutation selection
Table 2 Real-world optimization engineering benchmark cases included in the CEC 2020 and their bounds [53]
Function
Case study and its lower and upper bounds
Decision
variables
Constraints
Global
optima
RC8
Process synthesis problem: 0 B x1 B 1:6; x2 e {0 1}
2
2
2
RC12
Process synthesis problem: 0 B x2; x3; x1 B 100; x7; x6; x5; x4 e {0 1}
7
9
2.92
RC13
Process design problem: 27 B x3; 9 1; x2 B 45; x4 e {78, 79, …. 102}; x5 e {33, 34, …. 45}
5
3
26,900
RC15
Weight minimization of a speed reducer
0:7 B x2 B 0:8; 17 B x3 B 28; 2:6 B x1 B 3:6; 5 B x7 B 5:5; 7:3 B x5; x4 B 8:3;
2:9 B x6 B 3:9
7
11
2990
RC17
Tension/compression spring design (case 1)
0:05 B x1 B 2:00; 0:25 B x2 B 1:30; 2:00 B x3 B 15:0
3
3
0.0127
RC18
Pressure vessel design with integer variables
10 B 9 4; x3 B 200; 1 B x2; x1 B 99
4
4
5890
RC19
Welded beam design: 0:1 B x3; x2 B 10; 0:1 B x4 B 2; 0:125 B x1 B 2
4
5
1.67
RC20
Three-bar truss design problem: 0 B x1; x2 B 1
2
3
264
RC21
Multiple disk clutch brake design problem: 60 B x1 B 80; 90 B x2 B 110; 1 B x3 B 3;
0 B x4 B 1000; 2 B x5 B 9
5
7
0.0235
RC28
Rolling element bearing: x1 e {125 150}; x2 e {10.5 31}; x3 e {4.51 50.49}; x4 e {0.515 0.6};
x5 e {0.515 0.6}; x6 e {0.4 0.5}; x7 e {0.6 0.7}; x8 e {0.3 0.4}; x9 e {0.02 1}; x10 e {0.6
0.85}
10
9
14,600
RC29
Gas transmission compressor design (GTCD);
20 B x1 B 50; 1 B x2 B 10; 20 B x3 B 50; 0:1 B x4 B 60
4
1
2,960,000
RC31
Gear train design problem: 12 B x2; x3; x4; x1 B 60
4
1
0
RC32
Himmel Lau’s function: 78 B x1 B 102; 33 B x2 B 45; 27 B x3, x4, x5 B 45;
5
6
-30,700
10620
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 9
Table 3 Statistical indices for the engineering benchmark studied cases
Functions
Index
WSO
LWSO
DBO
FOX
MFO
RC8
Min
2
2
2
2
2
Average
2
2
2
2
2
Median
2
2
2
2
2
Max
2
2
2
2
2
Std
2.88E-16
2.44E-16
2.44E-16
7.1E-08
2.28E-16
Rank
4
1
1
5
1
RC12
Min
2.924831
2.924831
2.924831
2.924872
2.924839
Average
2.924831
2.940521
3.378957
2.946508
2.96061
Median
2.924831
2.924831
3.081732
2.925031
2.946961
Max
2.924831
3.081732
4.074353
3.082564
3.081732
Std
1.43E-07
0.048293
0.481632
0.047529
0.053133
Rank
1
2
5
3
4
RC13
Min
26,887.42
26,887.42
26,887.42
26,887.42
26,887.42
Average
26,887.42
26,887.42
26,887.42
27,135.01
26,887.42
Median
26,887.42
26,887.42
26,887.42
26,887.42
26,887.42
Max
26,887.42
26,887.42
26,887.42
28,368.22
26,887.42
Std
8.52E-05
2.05E-06
1.12E-11
473.4105
1.12E-11
Rank
4
3
1
5
1
RC15
Min
2994.648
2994.429
2994.424
2995.595
2994.424
Average
6E ? 14
5E ? 13
6E ? 14
6.5E ? 14
2998.352
Median
1E ? 15
2994.439
1E ? 15
1E ? 15
2994.424
Max
1E ? 15
1E ? 15
1E ? 15
1E ? 15
3033.702
Std
5.03E ? 14
2.24E ? 14
5.03E ? 14
4.89E ? 14
12.08925
Rank
3
2
4
5
1
RC17
Min
0.012665
0.012665
0.012666
0.012677
0.012674
Average
0.012665
0.012665
0.012742
5E ? 13
0.012827
Median
0.012665
0.012665
0.012719
0.012781
0.012719
Max
0.012665
0.012665
0.012928
1E ? 15
0.014283
Std
1.69E-08
8.3E-13
7.56E-05
2.24E ? 14
0.000356
Rank
2
1
3
5
4
RC18
Min
6247.675
6247.72
6247.673
6359.528
6247.673
Average
6247.681
6247.934
6544.502
39,927.73
6283.05
Median
6247.681
6247.853
6382.985
15,046.06
6247.673
Max
6247.688
6248.808
7319.001
239,304.1
6436.743
Std
0.003228
0.236775
400.6724
65,645.18
63.7404
Rank
1
2
4
5
3
RC19
Min
1.670218
1.670218
1.670218
1.67593
1.670218
Average
1.670218
1.670218
1.700254
1.756922
1.670219
Median
1.670218
1.670218
1.670218
1.722726
1.670218
Max
1.670218
1.670218
1.816712
1.994586
1.670239
Std
6.2E-08
5.61E-08
0.055884
0.080852
4.83E-06
Rank
2
1
4
5
3
RC20
Min
263.8958
263.8958
263.8958
263.8958
263.8958
Average
263.8958
263.8958
263.8959
263.8959
263.8985
Median
263.8958
263.8958
263.8959
263.8959
263.8967
Max
263.8958
263.8958
263.8961
263.8962
263.9237
Std
4.29E-12
1.3E-14
4.76E-05
7.87E-05
0.006081
Rank
2
1
3
4
5
Neural Computing and Applications (2024) 36:10613–10635
10621
123

---

## Page 10
engineering optimization problems, it is conducted tests on
13 optimization problems in chemical and mechanical
engineering, sourced from CEC 2020. The constraint
functions’ lower and upper limits violation were obtained
from [53], and the obtained results were compared with
other optimization solvers including DBO [54], WSO,
FOX [55], and MFO [56]. Table 2 provides essential
information about the benchmark functions used in the
study. As all these problems have multiple inequality
constraints, any algorithm designed to solve them must
integrate
a
constraint-handling
technique.
Common
approaches include repairing, decoding, preserving, and
penalizing, among others. In the presented case studies, the
ﬁrm penalty method was implemented to handle the
constraints. The population is set as 200 for all 13 bench-
marks. The maximum iterations equal 500 for the case
studies.
Table 3 presents the results of statistical indices for CEC
2020 optimization problems, compared the performance of
the LWSO algorithm and other competitive optimization
algorithms and further indicates ranking for all the 13 case
studies. From this table, the applied techniques are sorted.
It can be seen from this ranking order that the LWSO
algorithm superiors the other compared algorithms on 13
function problems. MFO and DBO display strong efﬁ-
ciency that are the second and third optimal. It can be
concluded from this discussion that the LWSO algorithm is
an effective algorithm for acquiring the optimal solutions
of
these
non-convex
constrained
f
problems.
The
Table 3 (continued)
Functions
Index
WSO
LWSO
DBO
FOX
MFO
RC21
Min
0.235242
0.235242
0.235242
0.235242
0.235242
Average
0.235242
0.235242
0.235242
0.235243
0.235242
Median
0.235242
0.235242
0.235242
0.235243
0.235242
Max
0.235242
0.235242
0.235242
0.235243
0.235242
Std
5.94E-09
1.87E-11
1.14E-16
9.23E-08
1.14E-16
Rank
4
3
1
5
1
RC28
Min
5599.448
5599.448
5599.448
5599.448
5599.448
Average
5599.448
5599.448
5599.448
5599.448
5599.448
Median
5599.448
5599.448
5599.448
5599.448
5599.448
Max
5599.448
5599.448
5599.448
5599.448
5599.448
Std
0
0
0
0
0
Rank
1
1
1
1
1
RC29
Min
2,964,895
2,964,895
2,964,895
2,989,723
2,964,897
Average
2,964,895
2,964,895
3,011,451
3,086,914
2,965,099
Median
2,964,895
2,964,895
2,964,897
3,096,913
2,964,998
Max
2,964,895
2,964,895
3,147,942
3,104,538
2,966,063
Std
9.68E-05
1.85E-05
74,628.94
29,668.78
302.1104
Rank
2
1
4
5
3
RC31
Min
3.89E-20
5.46E-19
0
3.38E-19
0
Average
3.91E-16
8.34E-17
0
4.3E-17
0
Median
7.25E-17
1.44E-17
0
6.21E-18
0
Max
1.95E-15
4.52E-16
0
3.28E-16
0
Std
5.92E-16
1.33E-16
0
8.09E-17
0
Rank
5
4
1
3
1
RC32
Min
-30,665.5
-30,665.5
-30,665.5
-30,665.5
-30,665.5
Average
-30,665.5
-30,665.5
-30,665.5
-30,648.6
-30,665.5
Median
-30,665.5
-30,665.5
-30,665.5
-30,665.5
-30,665.5
Max
-30,665.5
-30,665.5
-30,665.5
-30,514.8
-30,665.5
Std
0.001059
0.002432
3.73E-12
41.5896
3.73E-12
Rank
3
4
1
5
1
Average rank
2.615385
2
2.538462
4.307692
2.230769
Final ranking
4
1
3
5
2
10622
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 11
Fig. 4 The convergence curves for all techniques and benchmark functions
Neural Computing and Applications (2024) 36:10613–10635
10623
123

---

## Page 12
Fig. 5 Boxplots for all
techniques and benchmark
functions
10624
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 13
convergence rates of these algorithms for the tested func-
tions are shown in Fig. 4. To approve the performance of
the proposed algorithm, a boxplot of each algorithm and
objective function is presented in Fig. 5. Figure 5 displays
the boxplots of the LWSO algorithm, for most of the
functions, these plots are narrow and among the smallest
values.
Table 4 Statistical results of the Wilcoxon rank-sum test
LWSO vs
WSO
DBO
FOX
MFO
Function
P
Winner
P
Winner
P
Winner
P
Winner
F1
8.77E-03
?
1.00E ? 00
=
1.13E-08
?
3.42E-01
=
F2
1.60E-05
?
1.96E-06
?
9.75E-06
?
1.30E-05
?
F3
6.01E-07
?
8.01E-09
-
6.80E-08
?
8.01E-09
-
F4
1.03E-06
?
1.56E-01
=
7.47E-07
?
3.50E-06
-
F5
6.80E-08
?
5.73E-08
?
6.80E-08
?
5.37E-08
?
F6
6.80E-08
-
1.60E-04
?
6.80E-08
?
2.83E-01
?
F7
1.20E-06
?
4.25E-01
=
6.80E-08
?
3.75E-04
?
F8
1.12E-08
?
1.13E-08
?
1.13E-08
?
1.13E-08
?
F9
6.80E-08
?
8.01E-09
-
6.80E-08
?
8.01E-09
-
F10
NaN
=
NaN
=
NaN
=
NaN
=
F11
1.43E-07
?
7.85E-08
?
6.80E-08
?
6.80E-08
?
F12
3.79E-01
=
8.01E-09
-
1.14E-01
=
8.01E-09
-
F13
1.20E-01
=
8.01E-09
-
9.17E-08
?
8.01E-09
-
WRST (? / = /-)
9/3/1
5/4/4
11/2/0
6/2/5
Table 5 Friedman test for the
ﬁve algorithms
Function
LWSO
WSO
DBO
FOX
MFO
F1
2.35
3.05
2.35
5
2.25
F2
1.35
1.9
4.575
3.55
3.625
F3
3
4
1.5
5
1.5
F4
2.4
3.975
3.275
4.05
1.3
F5
1
2
3.825
4.5
3.675
F6
2.75
1.75
3.55
4.8
2.15
F7
2.3
3.45
2.75
4.85
1.65
F8
1
2
3.45
3.75
4.8
F9
3
4.1
1.5
4.9
1.5
F10
3
3
3
3
3
F11
1
2.05
3.55
4.8
3.6
F12
4.15
4.15
1.5
3.7
1.5
F13
3.4
3.6
1.5
5
1.5
Mean ranks
2.361538
3.001923
2.794231
4.376923
2.465385
Table 6 Parameter settings of
the competitive algorithms and
the proposed LWSO algorithm
Algorithm
Parameters
FOX
C1 = 0.18; C2 = 0.82
WSO
fmin = 0.07; fmax = 0.75; s = 4.125; a0 = 6.25; a1 = 100; a2 = 0.0005
LWSO
fmin = 0.07; fmax = 0.75; s = 4.125; a0 = 6.25; a1 = 100; a2 = 0.0005
Neural Computing and Applications (2024) 36:10613–10635
10625
123

---

## Page 14
4.2 Wilcoxon’s rank test results
In this subsection, the differences between the proposed
LWSO and well-known optimization algorithms are further
analyzed statistically using the Wilcoxon rank-sum test
(WRST), which is a paired test that checks for signiﬁcant
differences between two algorithms. The results of the test
between LWSO and each technique at a signiﬁcance level
of a = 0.05 are presented in Table 4, where the symbols
‘‘?/=/-’’ show whether LWSO executes better, similarly,
or worse than the comparison technique. This table also
presents the statistical results of LWSO in different
dimensions and functions, signifying whether LWSO per-
forms better, similarly, or worse than the comparison
algorithm. LWSO outperforms other comparative tech-
niques in the statistics of 13 optimization problems in
chemical and mechanical engineering, sourced from CEC
Table 7 Optimum solution
values for the fuel cost of the
ﬁrst test system with six
generators
Method
LWSO
WSO
GJO
NGO
FOX
P1 (MW)
0.120969
0.121006
0.107986
0.127545
0.122977
P2 (MW)
0.286312
0.286337
0.284068
0.255888
0.289468
P3(MW)
0.583557
0.583694
0.597299
0.638613
0.559545
P4 (MW)
0.992854
0.992772
0.996569
1.002144
0.994244
P5 (MW)
0.52397
0.523801
0.527366
0.485919
0.53871
P6 (MW)
0.351899
0.351949
0.346111
0.348028
0.355219
V (MW)
2.03E-11
2.56E-10
5.26E-08
8.42E-08
3.6E-07
PL
0.025562
0.025558
0.025399
0.024136
0.026164
Fuel cost ($/h)
605.9984
605.9984
606.0342
606.3391
606.041
The best values obtained are in bold
Fig. 6 Boxplots of various algorithms (system 1)
Fig. 7 Fuel cost convergence curves of various algorithms (system 1)
Table 8 Statistical results for fuel cost $/h (case study 1)
Method
Min
Max
Median
Average
Std
LWSO
605.9984
605.9984
605.9984
605.9984
2.33E-13
WSO
605.9984
605.9984
605.9984
605.9984
2.04E-07
GJO
606.0342
606.714
606.23
606.2743
0.186672
NGO
606.3391
607.369
606.7276
606.7602
0.285229
FOX
606.041
606.4303
606.0805
606.0977
0.082404
PSO
606.006
606.0501
606.0225
606.0253
0.0171
JS
606.3315
607.6245
606.9829
606.9632
0.323814
SMA
606.0017
606.1084
606.0159
606.0227
0.026
TSA
606.0248
606.4199
606.0501
606.1181
0.1508
HHO
606.5292
626.7676
611.3046
611.5524
3.826237
ISMA
605.9984
606.0374
606.0126
606.013
0.0142
The best values obtained are in bold
10626
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 15
2020, which approves the signiﬁcant dominance of LWSO
in most functions compared to other techniques. Therefore,
it can be concluded that the proposed LWSO technique
exhibits
the
best
performance
compared
to
other
algorithms.
4.3 Friedman’s rank test results
Table 5 presents the statistical results obtained by Fried-
man tests [57]. The smaller the ranking value, the better the
performance of the algorithm. From the results, we can get
the ranks of ﬁve algorithms as follows: LWSO, MFO,
DBO, WSO, and FOX. The highest-ranking shows that
LWSO is the best algorithm among the ﬁve algorithms.
4.4 Results of the studied cases
The LWSO technique is investigated on several ELD
problems. Also, a comparison is performed between the
LWSO and other optimization algorithms including GJO
[58], NGO [59], FOX, and conventional WSO algorithms.
The coding and simulation of the LWSO technique are
accomplished in the Matlab 2016a software. The LWSO
technique and other well-known algorithms are run using a
Table 9 Optimal solution of the
fuel cost of the second test
system with 10 generators
Method
LWSO
WSO
GJO
NGO
FOX
P1
55
54.99769
55
55
55
P2
80
79.98464
80
80
80
P3
106.9388
106.9542
107.5513
106.7959
107.1167
P4
100.5743
100.3228
100.1761
100.4317
100.1467
P5
81.5070
81.54307
81.88875
81.38856
80.10082
P6
83.0188
83.27021
82.40525
83.41902
84.6699
P7
300
299.9963
300
300
300
P8
340
339.9925
340
340
340
P9
470
469.9954
470
470
470
P10
470
469.9792
470
470
469.9999
V (MW)
1.47E-06
0.00114
0.021904
0.001767
7.21E-06
PL
87.03884
87.03719
87.04334
87.03696
87.03395
Fuel cost ($/h)
111,497.63
111,497.76
111,498.46
111,497.71
111,498.25
The best values obtained are in bold
Fig. 8 Boxplots of various algorithms (System 2)
Fig. 9 Fuel cost convergence curves of various algorithms (System 2)
Neural Computing and Applications (2024) 36:10613–10635
10627
123

---

## Page 16
Table 10 Statistical results for
fuel cost $/h (System 2)
Method
Min
Max
Median
Average
Std
LWSO
111,497.63
111,497.63
111,497.63
111,497.63
0.000162
WSO
111,497.8
111,497.9
111,497.8
111,497.8
0.028971
GJO
111,498.5
111,501.6
111,499.5
111,499.8
0.978837
NGO
111,497.7
111,498.3
111,498.1
111,498
0.152862
FOX
111,498.2
112,266.3
111,518.6
111,618.3
223.1766
PSO
111,497.64
111,497.83
111,497.70
111,497.71
0.06644
SMA
111,497.65
111,509.36
111,497.78
111,499.72
3.43854
TSA
111,498.42
111,503.88
111,499.93
111,500.55
1.876489
JS
111,505.9
111,513.3
111,508.8
111,508.9
1.578434
HHO
111,503.9
111,664.6
111,565.6
111,566.9
35.06826
ISMA
111,497.63
111,497.72
111,497.65
111,497.66
0.02839
The best values obtained are in bold
Table 11 Optimal solution for
the total generation cost of the
third test system with
11-generator
Method
LWSO
WSO
GJO
NGO
FOX
P1 (MW)
57.11343
57.11342
57.19094
58.49754
57.42616
P2 (MW)
40.43608
40.43604
40.11951
39.5701
40.32525
P3 (MW)
57.88132
57.88106
57.51134
60.87681
58.45923
P4 (MW)
277.7031
277.7034
277.3188
275.3541
270.2858
P5 (MW)
186.8794
186.8792
189.4806
181.686
183.7433
P6 (MW)
249.186
249.1862
250.2199
249.0324
250.007
P7 (MW)
177.074
177.0738
174.615
178.1559
176.6359
P8 (MW)
380.1974
380.1976
382.8858
377.7396
385.7118
P9 (MW)
341.6148
341.6144
343.0202
344.6969
341.2841
P10 (MW)
378.5835
378.5834
374.0441
381.0812
385.1406
P11 (MW)
353.3309
353.3315
353.5938
353.3104
350.9809
V (MW)
4.55E-13
2.39E-10
5.2E-06
1.13E-03
3.70E-06
Fuel cost ($/h)
12,274.4
12,274.4
12,274.45
12,274.55
12,274.57
The best values obtained are in bold
Fig. 10 Fuel
cost
convergence
curves
of
various
algorithms
(System 3)
Fig. 11 Boxplots of different algorithms (case study 3)
10628
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 17
laptop with a core i5 processor and 8 GB RAM. Table 6
records the parameters’ settings of the tested algorithms.
Four power systems with different generators and load
levels are considered as: The ﬁrst one has six generators
and the load demand equals 283.4 MW; the second system
involve 10 generators and the load demand increased to
2000 MW; and the third test system has 11 generators with
loading level of 2500 MW. The last test system has 40
generators, and the loading level reaches 10,500 MW.
4.4.1 System 1: six thermal generators
Six generator units make up this system, and together they
must provide 2.834 p.u. of power to meet the load
requirement. The system characteristics include the cost
coefﬁcients and generation limits taken from [49]. Table 7
depicts the power outputs of each generator, total power
loss, the total constraint violation (V), and total fuel cost
associated with the six-unit power system and their com-
parison with numerous algorithms. It can be detected that
LWSO algorithm gives the lowest value of total fuel cost
compared with these recent techniques. The LWSO tech-
nique shows the effectiveness of objective function values
and attains cogent and plausible results. Furthermore, the
system constraints are satisﬁed.
The program implementation records the optimal fuel
cost for each run, resulting in a collection of 20 optimal
values per algorithm. These values are then used to gen-
erate boxplots, as shown in Fig. 6. A thorough analysis of
these boxplots conﬁrms the superior performance of
LWSO technique compared to established optimization
techniques. Additionally, comparing the techniques’ per-
formances can be achieved by observing the fuel cost
across iterations. Figure 7 presents the convergence curves
of the techniques used in this test case. This ﬁgure approves
the competence of the LWSO algorithm in reaching the
lowest cost in minimum iterations. Furthermore, the com-
parison of the best, average, median, worst, and std values
of the proposed LWSO and most recently published ELD
algorithms such as ISMA [10], SMA [10], HHO [10],
TSA [10], PSO[10], and JS [10] is tabulated in Table 8. It
is clear from this table that the proposed LWSO technique
succeeds in achieving the optimum solution for the ELD
problem in this case.
4.4.2 System 2: ten thermal generators
In this system, the LWSO algorithm and the other tech-
niques are veriﬁed on the ten-generator system. The pop-
ulation size and maximum iterations equal 1000 and 500,
respectively. The generation bounds and coefﬁcients of
fuel cost were taken from the solution [10]. Table 9 shows
the optimal fuel costs acquired using all techniques. It was
proven that the LWSO technique achieves the best value of
111,497.63 $/h, and the least violation 1.47E-06 MW
compared with the original WSO, GJO, NGO, and FOX.
The performance of the studied algorithms on the ELD
problem is illustrated in Fig. 8, which depicts a boxplot. It
is noteworthy that the LWSO algorithm has a narrower
boxplot than the original WSO and other established
algorithms in many instances, indicating greater consis-
tency in terms of median, maximum, and minimum values.
Figure 9 displays the convergence curves of the fuel cost.
According to Fig. 9, the proposed LWSO algorithm con-
verges to the minimum value in a number of iterations
which is lower than the one for the original WSO tech-
nique. Furthermore, the comparison of the statistical mea-
sures’ values of the proposed LWSO and most recently
published ELD algorithms such as ISMA [10], SMA [10],
HHO [10], TSA [10], PSO [10], and JS [10] is presented in
Table 10. It is observable that the LWSO succeeds in
achieving the optimum solution for this system.
4.4.3 System 3: eleven thermal generators
In case 3, the solution of ELD problem is obtained by the
LWSO algorithm, and the load demand is PD = 2500 MW.
The generation bounds and coefﬁcients of fuel cost were
taken from the solution [10]. The results acquired using the
LWSO are compared with GJO, NGO, and FOX methods,
as well as the original WSO algorithm which is shown in
Table 11. These results show that the optimal solution
found using the LWSO algorithm is less than the solution
found
using
other
well-known
techniques.
Figure 10
Table 12 Statistical results for fuel cost $/h (System 3)
Method
Min
Max
Median
Average
Std
LWSO
12,274.4
12,274.4
12,274.4
12,274.4
3.73E-12
WSO
12,274.4
12,274.4
12,274.4
12,274.4
6.62E-11
GJO
12,274.45
12,274.96
12,274.58
12,274.65
0.154377
NGO
12,274.55
12,274.78
12,274.65
12,274.66
0.072292
FOX
12,274.57
12,278.27
12,275.48
12,275.69
0.869111
EBWO
12,274.46
12,274.7
12,274.54
12,274.55
0.065663
BWO
12,278.83
12,292.9
12,285.54
12,285.32
3.633401
SCSO
12,274.49
12,275
12,274.57
12,274.6
0.123994
SOA
12,282.33
12,305.01
12,289.87
12,291.6
6.814349
PSO
12,274.4
12,274.56
12,274.42
12,274.44
0.04804
SMA
12,274.4
12,274.41
12,274.41
12,274.41
0.001163
TSA
12,276.19
12,285.53
12,277.43
12,278.44
2.732958
JS
12,274.4
12,274.4
12,274.4
12,274.4
0.000652
HHO
12,274.4
12,274.45
12,274.41
12,274.42
0.0096
ISMA
12,274.4
12,274.41
12,274.4
12,274.4
0.001423
The best values obtained are in bold
Neural Computing and Applications (2024) 36:10613–10635
10629
123

---

## Page 18
Table 13 The optimal solution for the fuel cost of the forty-unit system
Method
LWSO
WSO
GJO
NGO
FOX
Method
LWSO
WSO
GJO
NGO
FOX
P1
110.9654
111.1925
113.6833
110.8855
113.9983
P21
523.283
523.4478
525.4317
523.2815
523.3476
P2
110.9943
77.9684
112.6781
110.9345
113.9893
P22
523.305
523.4257
527.1042
523.2833
549.9879
P3
97.42296
97.5468
120
97.40107
120
P23
523.277
523.3181
526.4473
523.2952
532.1728
P4
179.7423
179.774
180.6674
179.7332
130.1123
P24
523.284
523.3792
530.0041
523.2861
523.3539
P5
88.36963
88.34238
87.88707
88.0054
97
P25
523.277
523.2416
536.0151
523.28
549.9994
P6
140
139.814
140
105.4092
140
P26
523.279
523.5083
526.7506
523.2889
523.7803
P7
259.6432
259.5433
276.916
259.6132
248.4128
P27
10.00
10.12625
14.3028
10.00492
10.0003
P8
284.6089
284.783
296.1365
284.6145
290.0736
P28
10.00
10.21457
10.84856
10.00333
10.00231
P9
284.6118
284.5785
287.3377
284.6104
299.77
P29
10.00
10.14601
10.18514
10.00159
10.02122
P10
130.0038
204.6317
131.344
130.0006
204.8026
P30
97
96.33838
89.92187
87.86835
97
P11
168.8049
243.5479
94
168.7994
168.7965
P31
190
181.105
190
159.915
189.999
P12
94.00018
168.8596
174.1461
168.8024
168.8108
P32
189.995
159.911
190
189.999
189.999
P13
214.7693
304.5492
129.2097
214.7632
304.5214
P33
189.997
163.521
189.992
189.999
190
P14
394.2811
394.2222
393.9505
394.2795
394.2786
P34
164.826
164.901
178.036
164.850
199.999
P15
394.2739
394.2383
394.326
394.2795
304.5188
P35
164.969
164.973
200
164.840
200
P16
394.2681
304.5736
304.7691
394.2786
394.2859
P36
165.02
167.813
175.599
164.8
200
P17
489.3012
399.7212
491.3892
489.2826
309.881
P37
109.999
91.0754
109.761
109.998
110
P18
489.308
489.2648
489.2901
489.2859
310.1625
P38
109.997
89.2555
107.652
109.996
109.999
P19
511.2919
511.2622
512.7854
511.2796
511.289
P39
89.2420
89.1315
96.4641
89.1723
109.999
P20
511.2867
511.3533
511.4638
511.2811
511.3617
P40
511.290
511.349
512.432
511.283
511.278
Objective function C($/h)
121,444.6
122,488.5
122,176.1
121,602.1
123,745.7
10630
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 19
presents the convergence curve of the LWSO algorithm
and other algorithms, which demonstrates the high accu-
racy and speed of the LWSO to reach the best solution
compared to that of the studied intelligent techniques. The
results of all algorithms for this case are represented in
boxplots shown in Fig. 11 and show that the quartile of
LWSO has a smaller range as compared to that of these
recent techniques. Table 12 tabulates the best, worst,
average, median, and std values of various ELD solutions
among 20 trial runs, which proves that LWSO succeeded in
determining the optimal solution in comparison with other
techniques including EBWO [45], BWO [45], SCSO [45],
and SOA [45], ISMA [10], SMA [10], HHO [10], JS [10],
TSA [10], and PSO [10].
4.4.4 System 4: forty generators
In the fourth system, assessments are executed on the forty-
unit system. The generation bounds and coefﬁcients of fuel
cost were taken from [10]. The maximum iterations of the
proposed LWSO, original WSO, and other studied tech-
niques are increased to 1500 to increase the whole imple-
mentation for a large-scale power system. Table 13 shows
the power schedules achieved using execution least eco-
nomics. In this table, the fuel costs obtained by the LWSO
algorithm are less than WSO, GJO, NGO, and FOX algo-
rithms. The convergence curves of this case of the forty-
unit system for reducing the total cost by the proposed
LWSO and other studied techniques are displayed in
Fig. 12. It is obvious that the performance of the LWSO for
attaining the optimal solution to the economic load dis-
patch approves the strength of the LWSO algorithm. Fig-
ure 13 shows the boxplots of classiﬁcation accuracy results
achieved using the proposed LWSO and conventional
WSO, GJO, NGO, and FOX algorithms for fuel cost. The
boxplot represents the spread of classiﬁcation precision
values for each technique on a given dataset, with each
technique being run twenty times. The boxplot enables
comparison of techniques based on ﬁve essential statistical
measures: minimum precision value, maximum precision
value, lower quartile, upper quartile, and median. The
higher the boxplot, the greater the classiﬁcation accuracy
achieved by the technique. The LWSO consistently deliv-
ers the highest classiﬁcation accuracy values across most
datasets. Figures demonstrate that the LWSO technique has
a higher median and smaller interquartile ranges in most
datasets, which serves as evidence of the technique’s
effectiveness and robustness.
Moreover, Table 14 shows the ﬁve essential statistical
measures values of various ELD solutions via 20 individual
runs. Additionally, Table 14 includes results from alter-
native techniques such as enhanced beluga whale opti-
mization (EBWO) [45], beluga whale optimization (BWO)
[45], sand cat swarm optimization (SCSO) [45], skill
optimization algorithm (SOA) [45], ISMA [10], SMA [10],
HHO [10], JS [10], TSA [10], PSO [10], parallel particle
swarm optimization (PPSO) [16], slap swarm algorithm
(SSA) [16], marine predator algorithm (MPA) [16],
multigroup marine predator algorithm (MGMPA) [16], and
hybrid slap swarm algorithm (HSSA) [2]. These algorithms
show varying levels of performance in terms of fuel cost
Fig. 12 Fuel cost convergence curves of various algorithms (System
4)
Fig. 13 Boxplots of various algorithms (System 4)
Neural Computing and Applications (2024) 36:10613–10635
10631
123

---

## Page 20
optimization. Overall, the statistical results in Table 14
afﬁrm the effectiveness of the LWSO algorithm in
achieving lower fuel costs compared to other techniques,
showcasing its potential as a robust optimization approach
for the forty-unit power system.
Table 15 presents the value of the objective function for
various cases using different algorithms, demonstrating the
effectiveness of the proposed LWSO algorithm. In Case 1,
the LWSO algorithm yields a highly competitive objective
function value of 605.9984, identical to the WSO algo-
rithm. However, as we move on to the more complex
scenarios, such as Case 2, Case 3, and Case 4, LWSO
Table 14 Statistical results for
fuel cost $/h (System 4)
Method
Min
Max
Median
Average
Std
LWSO
121,444.6
121,855.6
121,679.2
121,680.2
98.69825
WSO
122,488.5
123,982.5
123,359.4
123,286.7
490.7263
GJO
122,176.1
123,620
122,940.9
122,900.6
320.9004
NGO
121,602.1
122,235.9
121,872
121,872.8
149.3719
FOX
123,745.7
129,811.1
126,112.2
125,954.3
1391.512
EBWO
121,600.9
122,180.9
121,991.8
122,012.6
163.4211
BWO
122,875.8
123,858.9
123,395.8
123,398.6
240.7044
SCSO
123,633.3
128,464.7
125,210.6
125,219.7
1092.271
SOA
125,704.4
128,066.9
127,074.1
127,019.5
667.1643
PSO
121,627.99
122,077.55
121,892.71
121,893.32
151.4660
SMA
121,621.68
121,994.65
121,781.88
121,770.54
153.4794
TSA
125,385.34
126,380.35
125,368.53
125,628.15
661.7595
JS
122,577.7
123,413
123,331
123,181.8
246.9075
HHO
122,439.237
123,801.25
122,974.36
122,966.90
364.4271
ISMA
121,546.89
121,859.73
121,726.95
121,702.82
164.1745
PPSO
125,503.09
129,631.35
–
129,631.35
1033.37
SSA
123,565.75
127,442.23
–
127,442.23
905.64
MPA
123,180.98
126,614.40
–
126,614.40
927.37
MGMPA
122,634.69
125,523.19
–
125,523.19
755.10
HSSA
121,960.27
–
–
–
–
The best values obtained are in bold
Table 15 The value of the objective function for the studied cases
using the proposed algorithms
Method
Case 1
Case 2
Case 3
Case 4
LWSO
605.9984
111,497.63
12,274.4
121,444.6
WSO
605.9984
111,497.8
12,274.4
122,488.5
GJO
606.0342
111,498.5
12,274.45
122,176.1
NGO
606.3391
111,497.7
12,274.55
121,602.1
FOX
606.041
111,498.2
12,274.57
123,745.7
The best values obtained are in bold
Table 16 Statistical results of
the Wilcoxon rank-sum test
LWSO vs
WSO
GJO
NGO
FOX
Function
P
Winner
P
Winner
P
Winner
P
Winner
Case 1
8.01E-09
?
8.01E-09
?
8.01E-09
?
8.01E-09
?
Case 2
6.8E-08
?
6.8E-08
?
6.8E-08
?
6.8E-08
?
Case 3
7.99E-09
?
8.01E-09
?
8.01E-09
?
8.01E-09
?
Case 4
6.67E-08
?
6.67E-08
?
5.83E-05
?
6.67E-08
?
WRST (? / = /-)
4/0/0
4/0/0
4/0/0
4/0/0
Table 17 Friedman test for the ﬁve algorithms
Function
LWSO
WSO
GJO
NGO
FOX
Case 1
1
2
3.9
4.95
3.15
Case 2
1
2.05
4.1
2.95
4.9
Case 3
1
2
3.4
3.7
4.9
Case 4
1.1
3.85
3.2
1.9
4.95
Mean ranks
1.025
2.475
3.65
3.375
4.475
10632
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 21
consistently outperforms other algorithms. Notably, in
Case 2, it produces a signiﬁcantly lower objective function
value of 111,497.63 compared to the next best, WSO, with
111,497.8. These results highlight LWSO’s exceptional
ability to optimize and ﬁnd solutions that outshine its
counterparts, offering a promising solution for a wide range
of real-world problems and optimization tasks.
4.5 Wilcoxon’s rank test results
Table 16 displays the outcomes of the test conducted
between LWSO and each technique, employing a signiﬁ-
cance level of a = 0.05. Additionally, the table presents the
statistical ﬁndings for LWSO across various scenarios,
indicating its superior, comparable, or inferior performance
relative to the comparison algorithm. LWSO demonstrates
superiority over other comparative techniques in the sta-
tistical results for four instances of ELD optimization
problems, underscoring its substantial dominance in most
functions compared to alternative techniques. Hence, it can
be inferred that the proposed LWSO technique showcases
the most effective performance when juxtaposed with other
algorithms.
4.6 Friedman’s rank test results
In Table 17, the statistical results derived from Friedman
tests are showcased. A smaller ranking value corresponds
to a superior algorithmic performance. Based on the
results, the rankings of the ﬁve algorithms are as follows:
LWSO, WSO, NGO, GJO, and FOX. The highest rank
signiﬁes that LWSO stands out as the top-performing
algorithm among the ﬁve considered.
5 Conclusion
In this article, an efﬁcient LWSO algorithm has been
proposed to attain the optimum solution to the ELD
problem. Using the leader strategy in LWSO enhances the
exploitation capability to avoid local optima and improve
the local and global search. The performance of the LWSO
algorithm has been assessed by using thirteen benchmark
optimization problems that exist in the CEC2020 test suite,
and it has been found that LWSO achieved better or similar
results than DBO, FOX, and MFO algorithms and the
conventional WSO. The efﬁcacy of the LWSO has been
assessed using evaluation metrics and statistical tests.
Results from the Friedman ranking test and the Wilcoxon
signed-rank test indicate a signiﬁcant enhancement in the
solution accuracy of the sizing problem when employing
the LWSO, surpassing the performance of these recent
algorithms. On another problem set, the proposed LWSO
algorithm is veriﬁed on 6-, 10-, 11-, and 40-thermal units-
based test systems. Furthermore, the performance of
LWSO in addressing the ELD problem has been scruti-
nized, revealing a consistently superior success rate com-
pared to WSO, GJO, NGO, and FOX algorithms. The
statistical analysis based on 20 individual runs has been
carried out for each case, and the results are compared with
the previous works of the literature. The dominance of the
LWSO algorithm over others has been conﬁrmed. In the
future work, the LWSO algorithm could be applied to
effectively solve other complex optimization problems in
several ﬁelds.
Acknowledgements This work was supported in part by the National
Key R&D Program of China (No. 2021YFE0191000) and in part by
Science, Technology, & Innovation Funding Authority (STDF) (No.
43180).
Funding Open access funding provided by The Science, Technology
& Innovation Funding Authority (STDF) in cooperation with The
Egyptian Knowledge Bank (EKB).
Data availability All required data are involved in the text.
Declarations
Conflict of interest Authors have no conflict of interest.
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
1. Fu L, Ouyang H, Zhang C et al (2022) A constrained cooperative
adaptive multi-population differential evolutionary algorithm for
economic
load
dispatch
problems.
Appl
Soft
Comput
121:108719. https://doi.org/10.1016/j.asoc.2022.108719
2. Alkoffash MS, Awadallah MA, Alweshah M et al (2021) A Non-
convex economic load dispatch using hybrid Salp Swarm algo-
rithm. Arab J Sci Eng 46:8721–8740. https://doi.org/10.1007/
s13369-021-05646-z
3. Das D, Bhattacharya A, Ray RN (2020) Dragonﬂy algorithm for
solving probabilistic economic load dispatch problems. Neural
Comput
Appl
32:3029–3045.
https://doi.org/10.1007/s00521-
019-04268-9
4. Hassan MH, Yousri D, Kamel S, Rahmann C (2022) A modiﬁed
Marine predators algorithm for solving single- and multi-objec-
tive combined economic emission dispatch problems. Comput
Ind Eng 164:107906. https://doi.org/10.1016/j.cie.2021.107906
Neural Computing and Applications (2024) 36:10613–10635
10633
123

---

## Page 22
5. Velasco L, Guerrero H, Hospitaler A (2024) A literature review
and critical analysis of metaheuristics recently developed. Archiv
Comput
Methods
Eng
31:125–146.
https://doi.org/10.1007/
s11831-023-09975-0
6. Abbaszadeh Shahri A, Khorsand Zak M, Abbaszadeh Shahri H
(2022) A modiﬁed ﬁreﬂy algorithm applying on multi-objective
radial-based
function
for
blasting.
Neural
Comput
Appl
34:2455–2471. https://doi.org/10.1007/s00521-021-06544-z
7. Abbaszadeh Shahri A, Pashamohammadi F, Asheghi R, Abbas-
zadeh Shahri H (2022) Automated intelligent hybrid computing
schemes to predict blasting induced ground vibration. Eng
Comput
38:3335–3349.
https://doi.org/10.1007/s00366-021-
01444-1
8. Kumar M, Dhillon JS (2018) Hybrid artiﬁcial algae algorithm for
economic load dispatch. Appl Soft Comput 71:89–109. https://
doi.org/10.1016/j.asoc.2018.06.035
9. Gholamghasemi M, Akbari E, Asadpoor MB, Ghasemi M (2019)
A new solution to the non-convex economic load dispatch
problems using phasor particle swarm optimization. Appl Soft
Comput 79:111–124. https://doi.org/10.1016/j.asoc.2019.03.038
10. Hassan MH, Kamel S, Abualigah L, Eid A (2021) Development
and application of slime mould algorithm for optimal economic
emission dispatch. Expert Syst Appl 182:115205. https://doi.org/
10.1016/j.eswa.2021.115205
11. Kaboli SHrA, Alqallaf AK, (2019) Solving non-convex economic
load dispatch problem via artiﬁcial cooperative search algorithm.
Expert Syst Appl 128:14–27. https://doi.org/10.1016/j.eswa.2019.
02.002
12. Farhan Tabassum M, Saeed M, Ahmad Chaudhry N et al (2021)
Evolutionary simplex adaptive Hooke-Jeeves algorithm for eco-
nomic load dispatch problem considering valve point loading
effects. Ain Shams Eng J 12:1001–1015. https://doi.org/10.1016/
j.asej.2020.04.006
13. Liu T, Xiong G, Wagdy Mohamed A, Nagaratnam Suganthan P
(2022) Opposition-mutual learning differential evolution with
hybrid mutation strategy for large-scale economic load dispatch
problems with valve-point effects and multi-fuel options. Inf Sci
(N Y). https://doi.org/10.1016/j.ins.2022.07.148
14. Al-Betar MA, Awadallah MA, Krishan MM (2020) A non-con-
vex economic load dispatch problem with valve loading effect
using a hybrid grey wolf optimizer. Neural Comput Appl
32:12127–12154. https://doi.org/10.1007/s00521-019-04284-9
15. Tahir BH, Rashid TA, Rauf HT et al (2022) Improved ﬁtness-
dependent optimizer for solving economic load dispatch problem.
Comput Intell Neurosci 2022:1–16. https://doi.org/10.1155/2022/
7055910
16. Pan J, Shan J, Chu S et al (2022) A multigroup marine predator
algorithm and its application for the power system economic load
dispatch. Energy Sci Eng 10:1840–1854. https://doi.org/10.1002/
ese3.957
17. Hassan MH, Kamel S, Eid A et al (2023) A developed eagle-
strategy supply-demand optimizer for solving economic load
dispatch problems. Ain Shams Eng J 14:102083. https://doi.org/
10.1016/j.asej.2022.102083
18. Singh T (2022) Chaotic slime mould algorithm for economic load
dispatch problems. Appl Intell 52:15325–15344. https://doi.org/
10.1007/s10489-022-03179-y
19. Hao W-K, Wang J-S, Li X-D et al (2022) Arithmetic optimiza-
tion algorithm based on elementary function disturbance for
solving economic load dispatch problem in power system. Appl
Intell
52:11846–11872.
https://doi.org/10.1007/s10489-021-
03125-4
20. Singh D, Dhillon JS (2019) Ameliorated grey wolf optimization
for economic load dispatch problem. Energy 169:398–419.
https://doi.org/10.1016/j.energy.2018.11.034
21. Rizk-Allah RM, Mageed HMA, El-Sehiemy RA et al (2017) A
new sine cosine optimization algorithm for solving combined
non-convex economic and emission power dispatch problems. Int
J Energy Convers 5:180–192
22. El-Sehiemy RA, Rizk-Allah RM, Attia A (2019) Assessment of
hurricane versus sine-cosine optimization algorithms for eco-
nomic/ecological emissions load dispatch problem. Int Trans
Electr Energy Syst 29:e2716
23. Elsakaan AA, El-Sehiemy RA, Kaddah SS, Elsaid MI (2018) An
enhanced moth-ﬂame optimizer for solving non-smooth eco-
nomic dispatch problems with emissions. Energy 157:1063–1078
24. Hassan MH, Kamel S, Jurado F, Desideri U (2024) Global
optimization of economic load dispatch in large scale power
systems using an enhanced social network search algorithm. Int J
Electr Power Energy Syst 156:109719. https://doi.org/10.1016/j.
ijepes.2023.109719
25. Ping L, Sun J, Chen Q (2020) Solving power economic dispatch
problem with a novel quantum-behaved particle swarm opti-
mization algorithm. Math Probl Eng 2020:1–11. https://doi.org/
10.1155/2020/9741595
26. Hao WK, Wang JS, Li XD, Song HM, Bao YY (2022) Proba-
bility distribution arithmetic optimization algorithm based on
variable order penalty functions to solve combined economic
emission dispatch problem. Applied Energy 316:119061. https://
doi.org/10.1016/j.apenergy.2022.119061
27. Bhattacharya A, Chattopadhyay PK (2010) Biogeography-based
optimization for different economic load dispatch problems.
IEEE Trans Power Syst 25:1064–1077. https://doi.org/10.1109/
TPWRS.2009.2034525
28. dos Coelho LS, Mariani VC (2010) An efﬁcient cultural self-
organizing migrating strategy for economic dispatch optimization
with valve-point effect. Energy Convers Manag 51:2580–2587.
https://doi.org/10.1016/j.enconman.2010.05.022
29. Amjady N, Nasiri-Rad H (2010) Solution of nonconvex and
nonsmooth economic dispatch by a new Adaptive Real Coded
Genetic Algorithm. Expert Syst Appl 37:5239–5245. https://doi.
org/10.1016/j.eswa.2009.12.084
30. Amjady N, Sharifzadeh H (2010) Solution of non-convex eco-
nomic dispatch problem considering valve loading effect by a
new Modiﬁed Differential Evolution algorithm. Int J Electr
Power Energy Syst 32:893–903. https://doi.org/10.1016/j.ijepes.
2010.01.023
31. Hemamalini S, Simon SP (2010) Artiﬁcial bee colony algorithm
for economic load dispatch problem with non-smooth cost
functions. Electric Power Comp Syst 38:786–803. https://doi.org/
10.1080/15325000903489710
32. Yang X-S, Sadat Hosseini SS, Gandomi AH (2012) Fireﬂy
Algorithm for solving non-convex economic dispatch problems
with valve loading effect. Appl Soft Comput 12:1180–1186.
https://doi.org/10.1016/j.asoc.2011.09.017
33. Lin W-M, Gow H-J, Tsai M-T (2011) Combining of Direct
Search and Signal-to-Noise Ratio for economic dispatch opti-
mization. Energy Convers Manag 52:487–493. https://doi.org/10.
1016/j.enconman.2010.07.022
34. Tsai M-T, Gow H-J, Lin W-M (2011) A novel stochastic search
method for the solution of economic dispatch problems with non-
convex fuel cost functions. Int J Electr Power Energy Syst
33:1070–1076. https://doi.org/10.1016/j.ijepes.2011.01.026
35. Shaw B, Mukherjee V, Ghoshal SP (2011) Seeker optimisation
algorithm: application to the solution of economic load dispatch
problems. IET Gener Transm Distrib 5:81. https://doi.org/10.
1049/iet-gtd.2010.0405
36. Moradi-Dalvand M, Mohammadi-Ivatloo B, NajaﬁA, Rabiee A
(2012) Continuous quick group search optimizer for solving non-
convex economic dispatch problems. Electric Power Syst Res
93:93–105. https://doi.org/10.1016/j.epsr.2012.07.009
10634
Neural Computing and Applications (2024) 36:10613–10635
123

---

## Page 23
37. Fonte PM, Monteiro C, Maciel Barbosa FP (2013) Sensing Cloud
Optimization applied to a non-convex constrained economical
dispatch. In: IECON 2013 - 39th Annual Conference of the IEEE
Industrial Electronics Society. IEEE, pp 2163–2168
38. Srinivasa Reddy A, Vaisakh K (2013) Shufﬂed differential evo-
lution for economic dispatch with valve point loading effects. Int
J Electr Power Energy Syst 46:342–352. https://doi.org/10.1016/j.
ijepes.2012.10.012
39. Bhattacharjee K, Bhattacharya A, Halder nee Dey S (2014)
Chemical reaction optimisation for different economic dispatch
problems. IET Gen Trans Distrib 8:530–541. https://doi.org/10.
1049/iet-gtd.2013.0122
40. Adarsh BR, Raghunathan T, Jayabarathi T, Yang X-S (2016)
Economic
dispatch
using
chaotic
bat
algorithm.
Energy
96:666–675. https://doi.org/10.1016/j.energy.2015.12.096
41. Jayabarathi T, Raghunathan T, Adarsh BR, Suganthan PN (2016)
Economic dispatch using hybrid grey wolf optimizer. Energy
111:630–641. https://doi.org/10.1016/j.energy.2016.05.105
42. Hamdi M, Idomghar L, Chaoui M, Kachouri A (2019) An
improved adaptive differential evolution optimizer for non-con-
vex Economic Dispatch Problems. Appl Soft Comput 85:105868.
https://doi.org/10.1016/j.asoc.2019.105868
43. Agnihotri S, Atre A, Verma HK (2020) Equilibrium Optimizer
for Solving Economic Dispatch Problem. In: 2020 IEEE 9th
Power India International Conference (PIICON). IEEE, pp 1–5
44. Yu J, Kim C-H, Rhee S-B (2020) Clustering cuckoo search
optimization for economic load dispatch problem. Neural Com-
put Appl 32:16951–16969. https://doi.org/10.1007/s00521-020-
05036-w
45. Hassan MH, Kamel S, Jurado F et al (2023) Economic load
dispatch solution of large-scale power systems using an enhanced
beluga whale optimizer. Alex Eng J 72:573–591. https://doi.org/
10.1016/j.aej.2023.04.002
46. Braik M, Hammouri A, Atwan J et al (2022) White Shark
Optimizer: a novel bio-inspired meta-heuristic algorithm for
global optimization problems. Knowl Based Syst 243:108457.
https://doi.org/10.1016/j.knosys.2022.108457
47. Ali MA, Kamel S, Hassan MH et al (2022) Optimal power ﬂow
solution of power systems with renewable energy sources using
white sharks algorithm. Sustainability 14:6049. https://doi.org/10.
3390/su14106049
48. Liang J, Liu L (2023) Optimal path planning method for
unmanned surface vehicles based on improved shark-inspired
algorithm. J Mar Sci Eng 11:1386. https://doi.org/10.3390/
jmse11071386
49. Zou D, Li S, Li Z, Kong X (2017) A new global particle swarm
optimization for the economic emission dispatch with or without
transmission losses. Energy Convers Manag 139:45–70. https://
doi.org/10.1016/j.enconman.2017.02.035
50. Hassan MH, Kamel S, Salih SQ et al (2021) Developing chaotic
artiﬁcial ecosystem-based optimization algorithm for combined
economic emission dispatch. IEEE Access 9:51146–51165.
https://doi.org/10.1109/ACCESS.2021.3066914
51. Singh M, Dhillon JS (2016) Multiobjective thermal power dis-
patch using opposition-based greedy heuristic search. Int J Electr
Power Energy Syst 82:339–353. https://doi.org/10.1016/j.ijepes.
2016.03.016
52. Naik MK, Panda R, Wunnava A, et al (2021) A leader Harris
hawks optimization for 2-D Masi entropy-based multilevel image
thresholding. Multimed Tools Appl 1–41
53. Kumar A, Wu G, Ali MZ et al (2020) A test-suite of non-convex
constrained optimization problems from the real-world and some
baseline results. Swarm Evol Comput 56:100693. https://doi.org/
10.1016/j.swevo.2020.100693
54. Xue J, Shen B (2023) Dung beetle optimizer: a new meta-
heuristic algorithm for global optimization. J Supercomput
79:7305–7336. https://doi.org/10.1007/s11227-022-04959-6
55. Mohammed H, Rashid T (2023) FOX: a FOX-inspired opti-
mization algorithm. Appl Intell 53:1030–1050. https://doi.org/10.
1007/s10489-022-03533-0
56. Mirjalili S (2015) Moth-ﬂame optimization algorithm: a novel
nature-inspired
heuristic
paradigm.
Knowl
Based
Syst
89:228–249. https://doi.org/10.1016/j.knosys.2015.07.006
57. Wang Y, Wang P, Zhang J et al (2019) A novel bat algorithm
with multiple strategies coupling for numerical optimization.
Mathematics 7:135. https://doi.org/10.3390/math7020135
58. Chopra N, Mohsin Ansari M (2022) Golden jackal optimization:
a novel nature-inspired optimizer for engineering applications.
Expert Syst Appl 198:116924. https://doi.org/10.1016/j.eswa.
2022.116924
59. Dehghani M, Hubalovsky S, Trojovsky P (2021) Northern
Goshawk optimization: a new swarm-based algorithm for solving
optimization problems. IEEE Access 9:162059–162080. https://
doi.org/10.1109/ACCESS.2021.3133286
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
Neural Computing and Applications (2024) 36:10613–10635
10635
123

---
