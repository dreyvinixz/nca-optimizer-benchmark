# Supercell thunderstorm algorithm (STA): a nature-inspired metaheuristic algorithm for engineering optimization

**Year**: 2025 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-10848-1

---

## Page 1
ORIGINAL ARTICLE
Supercell thunderstorm algorithm (STA): a nature-inspired
metaheuristic algorithm for engineering optimization
Mohamed H. Hassan1 • Salah Kamel2
Received: 1 November 2023 / Accepted: 29 November 2024 / Published online: 1 February 2025
 The Author(s) 2025
Abstract
In this paper, an optimization algorithm called supercell thunderstorm algorithm (STA) is proposed. STA draws inspiration
from the strategies employed by storms, such as spiral motion, tornado formation, and the jet stream. It is a computational
algorithm speciﬁcally designed to simulate and model the behavior of supercell thunderstorms. These storms are known for
their rotating updrafts, strong wind shear, and potential for generating tornadoes. The optimization procedures of the STA
algorithm are based on three distinct approaches: exploring a divergent search space using spiral motion, exploiting a
convergent search space through tornado formation, and navigating through the search space with the aid of the jet stream.
To evaluate the effectiveness of the proposed STA algorithm in achieving optimal solutions for various optimization
problems, a series of test sequences were conducted. Initially, the algorithm was tested on a set of 23 well-established
functions. Subsequently, the algorithm’s performance was assessed on more complex problems, including ten CEC2019
test functions, in the second experimental sequence. Finally, the algorithm was applied to ﬁve real-world engineering
problems to validate its effectiveness. The experimental results of the STA algorithm were compared to those of con-
temporary metaheuristic methods. The analysis clearly demonstrates that the developed STA algorithm outperforms other
methods in terms of performance.
Keywords Supercell thunderstorm algorithm  Metaheuristics  Global optimization  Optimization problems
1 Introduction
The difﬁculty of real-world optimization problems has
increased, requiring more efﬁcient approaches to ﬁnding
solutions. Optimization involves determining the most
effective strategy for minimizing or maximizing the
objective
function
of
a
given
problem.
Numerous
researchers have explored various methods for solving
these intricate and challenging real-world problems [1]. In
the past twenty years, there has been signiﬁcant academic
interest in nature-inspired computation, as nature provides
valuable inspiration for designing artiﬁcial computing
systems that can discover optimal solutions for complex
mathematical problems [2].
Evolutionary algorithms (EAs) are widely recognized as
highly effective techniques in research. The literature has
seen the utilization of various types of EAs, such as dif-
ferential evolution (DE) [3], genetic algorithm (GA) [4],
and evolutionary programming (EP) [5]. These algorithms
tackle diverse challenges by incorporating prior knowledge
into an evolutionary search process, effectively exploring a
solution space ﬁlled with potential solutions. Though EAs
are unable to achieve the best solution for many problems
in spite of the above-mentioned beneﬁts, hence, several
academics have combined these techniques with existing
technologies to enhance their solutions [6].
Swarm
intelligence
(SI)
represents
an
alternative
approach within the realm of intelligent computing algo-
rithms such as particle swarm optimization (PSO) [7],
which mimics the swarm behavior of birds or ﬁsh; ant
colony optimization (ACO) [8], which imitates the forag-
ing and schooling behavior of ants; and other algorithms,
& Salah Kamel
skamel@aswu.edu.eg
Mohamed H. Hassan
mohamedhosnymoee@gmail.com
1
Ministry of Electricity and Renewable Energy, Cairo, Egypt
2
Department of Electrical Engineering, Faculty of
Engineering, Aswan University, Aswan 81542, Egypt
123
Neural Computing and Applications (2025) 37:7207–7260
https://doi.org/10.1007/s00521-024-10848-1
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
including gravitational search technique (GSA) [9], grey
wolf optimization algorithm (GWO) [10], artiﬁcial bee
colony (ABC) [11], moth ﬂame optimization (MFO) [12],
whale optimization algorithm (WOA) [13], and ant lion
optimizer (ALO) algorithms [14], and many more. Swarm
intelligence addresses various challenges by emulating the
natural behavior of animals as they seek food and move
between locations. This approach is often inﬂuenced by the
problem’s scale and nonlinearity. Despite the widespread
application of conventional analytical methods to resolve
computational and combinatorial problems, many of these
methods struggle to effectively converge on solutions.
Swarm intelligence offers several advantages. For
instance, individual entities within a population can
enhance their search efﬁciency as they move from one
location to another, while the collective populations in a
swarm collectively progress within their respective loca-
tions. In evolutionary algorithms (EAs), weaker and less
capable populations are phased out and replaced by highly
skilled ones. A swarm consistently ventures into uncharted
territories within the search domain, facilitating the rapid
discovery of globally optimal solutions. Nevertheless,
swarm intelligence is not without its downsides. For
instance, the coordinated movements of individuals may
lead to entrapment in local optima, and the persistent
inability of populations to escape from these regions can
prematurely halt the exploration process [15].
Nature-inspired techniques have been devised due to
their effectiveness in tackling a multitude of problems.
There is an opportunity to blend evolutionary approaches
with swarm algorithms to create new capabilities for
problem-solving. These capabilities harness the beneﬁts
provided by swarm intelligence for efﬁcient exploration
within the swarm’s optimal regions while also leveraging
the power of evolutionary methods to continually traverse
the search space and avoid local optima. It’s worth noting
that the No Free Lunch (NFL) theorem stipulates that no
single technique can excel on all problems [16]. This drives
researchers to propose novel techniques or enhance exist-
ing ones to address speciﬁc optimization challenges. Each
algorithm possesses its unique strengths and weaknesses,
and their application to various real-world problems can
yield enhanced outcomes.
Thus, the introduction of techniques such as the super-
cell thunderstorm algorithm (STA), which is a nature-in-
spired method for ﬁnd the optimum solution for the
optimization problems, mimics behavior of supercell
thunderstorms, which are a type of severe thunderstorm
characterized by rotating updrafts, powerful wind shear,
and the potential for producing tornadoes. The optimization
techniques employed by the STA method are delineated
through three distinct approaches: navigating within a
dispersed search space via spiral motion, capitalizing on
opportunities within a converged search space through
tornado formation, and swiftly progressing with a jet
stream. To validate the robustness and effectiveness of
STA, a comprehensive evaluation is conducted using a
combination of twenty-three classical and ten CEC2019
test functions. Moreover, the study employs ﬁve engi-
neering design problems to further evaluate the efﬁciency
of the STA attaining optimal solutions for real-world
challenges. It is compared with eleven existing techniques
from the literature. The ﬁndings reveal that STA performs
exceptionally, showcasing beneﬁts like minimal time
complexity, rapid convergence, high precision in solutions,
general applicability, and robustness. In summary, the
primary contributions of this research can be outlined as
follows:
•
Introduction of STA algorithm: This paper introduces
the
supercell
thunderstorm
algorithm
(STA),
an
approach designed for tackling global optimization
problems and engineering design problems.
•
Comprehensive testing: The paper conducts rigorous
testing of the proposed STA algorithm across a variety
of optimization scenarios. This includes the evaluation
of STA on 23 established test functions, the IEEE
CEC2019 test suite, and 7 distinct engineering design
issues.
•
Comparison with contemporary metaheuristic algo-
rithms: The paper performs comparative analysis by
benchmarking STA against recent metaheuristic algo-
rithms (MAs). This allows for the assessment of STA’s
performance relative to other state-of-the-art optimiza-
tion techniques.
•
Enhanced reliability: The experimental results pre-
sented in the paper demonstrate that the STA algorithm
consistently outperforms alternative optimization algo-
rithms. This substantiates the claim that STA offers a
more reliable and effective solution for addressing a
wide range of optimization challenges.
The subsequent sections of this article are structured as
follows: In Sect. 2, it is provided a brief exploration of the
dynamic traits exhibited by storms and expound upon each
stage of the newly devised supercell thunderstorm algo-
rithm (STA). Section 3 delineates the evaluation method-
ology
and
the
outcomes
obtained.
In
Sect.
4,
the
STA technique is used to solve ﬁve real-world engineering
design problems. Finally, Sect. 5 encapsulates the conclu-
sions drawn from this research.
7208
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 3
2 The supercell thunderstorm algorithm
(STA)
In this section, the suggested nature-inspired algorithm,
named supercell thunderstorm algorithm (STA), is pre-
sented as follows.
2.1 Behavior of supercell thunderstorm
The term ‘‘supercell’’ was coined in the mid-1970s,
although these unique convective storms were ﬁrst identi-
ﬁed as a distinct category in the early 1960s. Supercells are
the rarest type of storms but are known for generating an
exceptionally high amount of severe weather, including
large hail, destructive winds, intense lightning, and torna-
does [17]. Almost all instances of hail measuring 5 cm or
larger in diameter are associated with supercell storms.
Similarly, most of the powerful and violent tornadoes
originate from supercells. Supercells are also known for
producing some of the highest lightning ﬂash rates ever
recorded, with rates exceeding 200 ﬂashes per minute
being possible [17]. A supercell is characterized by the
presence of a mesocyclone, which is a deep and persis-
tently rotating updraft. Consequently, these storms are
sometimes referred to as rotating thunderstorms [18].
Among the four main categories of thunderstorms (super-
cell, squall line, multicell, and single-cell), supercells are
the least common but have the potential to be the most
severe. Figure 1 illustrates the behavior of a supercell
thunderstorm. The interaction between a strong updraft and
highly sheared environmental winds results in a type of
storm that outwardly appears distinct from a multicell
storm, although the underlying physical processes are
similar. Unlike multicell storms, supercells are character-
ized by a robust and long-lasting rotating updraft.
2.2 STA algorithm
The STA technique mimics the behavior of supercell
thunderstorm. Consequently, this algorithm can be sepa-
rated into three parts, namely, spiral motion, formation, and
jet stream. Similar to the majority of metaheuristics, STA
operates as a population-based technique. It begins by
uniformly distributing the initial solutions across the search
space during the initial trial:
Xi ¼ lb þ r1 ub  lb
ð
Þ; i ¼ 1; 2; . . .:; n
ð1Þ
where lb and ub are the lower and upper bounds of the
search space, respectively. r1 denotes a random vector,
which is uniformly distributed in the interval [0, 1]; n is the
number of storm populations.
2.2.1 Spiral motion
Supercell thunderstorms are known for their well-deﬁned
rotation, often taking on a mesocyclone structure. This
rotation is similar to the spiraling motion observed in
natural phenomena, such as hurricanes and tornadoes [19].
Figure 2 displays the spiral motion of supercell thunder-
storms. The STA seeks to replicate this spiral motion by
using mathematical models [1] and algorithms to simulate
the development and persistence of rotation within the
storm.
Storm Motion
Jetstream
Wall Cloud
Flanking line
Cumulonimbus 
cloud
Shelf Cloud
Tornado
Overshooting top
Anvil
Fig. 1 Behavior of supercell
thunderstorm
Neural Computing and Applications (2025) 37:7207–7260
7209
123

---

## Page 4
The mathematical expression for this approach is as
follows:
Xi t þ 1
ð
Þ ¼
a1: Xbest tð Þ þ b1: Xbest tð Þ  Xi tð Þ
j
j
ð
Þ þ a2:Xi tð Þ;
if r1\ t
tmax
a1: Xbest tð Þ þ b2: Xbest tð Þ  MGi tð Þ
j
j
ð
Þ þ a2:Xi tð Þ;
if r1 
t
tmax
8
>
<
>
:
a1 ¼ a þ 1  a
ð
Þ: t
tmax
;
a2 ¼ 1  a
ð
Þ  1  a
ð
Þ: t
tmax
;
b1 ¼ ecs: cos 2pc
ð
Þ;
b2 ¼ ecs: sin 2pc
ð
Þ;
s ¼ e3 þ 1  a
ð
Þ: t
tmax
;
ð2Þ
In this equation, a1 and a2 denote the weight coefﬁ-
cients, which regulate the degree to which individuals
move toward the optimum individual and the preceding
individual, respectively, while a denotes the control coef-
ﬁcient. The control coefﬁcient is a random value that varies
from 0 to 1 through the increase in iteration. The constant
controls how far the storms can follow the optimum and
preceding
individuals
throughout
the
initial
stage.
t
represents the current iteration, and tmax is the maximum
number of iterations. MGi tð Þ represents the mean group
that is attained using considering the means of a group of
points chosen randomly close to the considered solution
candidate. Finally, c represents a random number that
follows a uniform distribution in the interval [0, 1].
2.2.2 Tornado formation
One of the most destructive aspects of supercell thunder-
storms is their ability to produce tornadoes. Tornadoes are
highly localized, intense, and violent wind phenomena that
form within the rotating updraft of a supercell [20]. STA
aims to understand the conditions and processes that lead to
tornado formation within supercells and to simulate these
processes in its algorithms. By doing so, it helps meteo-
rologists better predict when and where tornadoes may
develop within a storm.
The tornado formation has been considered as they have
signiﬁcant impacts on the supercell thunderstorms. The
position of the populations is modiﬁed based on the tor-
nado formation to avoid falling them into local optimum
solutions. This stage can be mathematically described as
below [21]:
where the TF equals 0.7. G1 is the step factor. The symbol
r2 represents a random number while r3; r4; r5; r6 are the
random indices of the storm.
2.2.3 Jet stream
The jet stream is a high-speed, narrow air current located in
the upper levels of the Earth’s atmosphere. It plays a cru-
cial role in weather patterns and can inﬂuence the
Fig. 2 Spiral motion of supercell thunderstorms
Xi t þ 1
ð
Þ ¼
Xi tð Þ þ rand 0; 1
ð
Þ  exp G1: t
tmax




Xr3 tð Þ  Xr4 tð Þ
ð
Þ
Xi tð Þ þ TF 1  rand 0; 1
ð
Þ
ð
Þ þ rand 0; 1
ð
Þ
½
 Xr5 tð Þ  Xr6 tð Þ
ð
Þ
8
<
:
G2 ¼ 2  n 
0:1  0:05: t
tmax


ð3Þ
7210
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 5
development and movement of severe thunderstorms,
including supercells [22]. STA takes into account the
inﬂuence of the jet stream on supercell thunderstorms, as
its interaction with the storm can have a signiﬁcant impact
on their formation, evolution, and track. During this phase,
storms prepare to launch an attack on the optimal point
within the search area, with all other points converging
toward this point. This process can be mathematically
expressed as follows [2]:
The movement of the storms takes unlike forms. Within
this article, a polar equation is harnessed to graphically
represent the trajectory of these storms during Jetstream
motion. Additionally, the optimal point is determined by
calculating the product of the variance between the current
and mean points along the polar x-axis and the variance
between the current and optimal points along the polar y-
axis.
Fig. 3 Co-sequences for the
three main stages of supercell
thunderstorm by STA
Xi t þ 1
ð
Þ ¼
rand  Xbest tð Þ þ d1 ið Þ  Xi tð Þ  3  rand  Xmean tð Þ
ð
Þ þ y1 ið Þ  xi  2  Xbest tð Þ
ð
Þ
r7  0:3
Xi tð Þ þ rand  Xbest tð Þ  Xk tð Þ
j
j
½
 þ rand  Xi tð Þ
j
j  Xk tð Þ
½

r7 [ 0:3

d1 ið Þ ¼
dr ið Þ
max dr
j
j
ð
Þ ; y1 ið Þ ¼
yr ið Þ
max yr
j
j
ð
Þ
dr ið Þ ¼ r ið Þ  sinh h ið Þ
ð
Þ; yr ið Þ ¼ r ið Þ  cosh h ið Þ
ð
Þ
h ið Þ ¼ a2  p  expðrandðrand n; 1
ð
Þ; andr ið Þ ¼ h ið Þ
ð4Þ
Neural Computing and Applications (2025) 37:7207–7260
7211
123

---

## Page 6
2.3 STA stages, exploration, and exploitation
Figure 3 shows the three stages of the proposed STA
algorithm. In the initial optimization phase, as illustrated in
stage 1 of the ﬁgure, the storms engage in a spiral motion.
This spiral motion aids the storms in distinctively exploring
their respective areas, leading to a thorough examination of
the ﬁeld. Subsequently, each storm, with its new location,
undergoes objective assessment, and if the new location
proves more suitable than the previous one, it is adopted.
This marks the transition to the second phase of the tech-
nique, which aims to facilitate the shift from exploration to
exploitation. In this stage, the storms also commence the
formation of tornado groups.
The formation of a tornado serves as a pivotal reference
point, bolstering the strength of the storms. During this
stage, half of the individuals are designated for exploration,
while the remaining half take charge of exploitation. As the
storm positions draw nearer to each other and the step
length decreases compared to the previous stage, the Jet-
stream plays a crucial role in aiding the proposed STA
technique to effectively steer clear of local optima,
resulting in improved overall performance. The adaptive
convergence factor introduced in this stage plays a signif-
icant role in guiding the storms to conﬁne their search
Fig. 4 Flowchart of the STA algorithm
7212
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 7
efforts to a speciﬁc neighborhood for exploitation, pre-
venting them from squandering resources on less promising
areas within the domain. The ﬁgure outlines the ﬁnal stage,
labeled as stage 3. The ﬂowchart illustrating the STA
technique is shown in Fig. 4. Additionally, Algorithm 1
provides the pseudocode deﬁning the STA technique.
Algorithm 1 Pseudocode of the STA technique
Neural Computing and Applications (2025) 37:7207–7260
7213
123

---

## Page 8
Table 1 Benchmark functions
Function
Dim
Range
fmin
F1 x
ð Þ ¼ P
N
i¼1
x2
i
50, 100, 500
[ - 100, 100]
0
F2 x
ð Þ ¼ P
N
i¼1
xi
j j þ Q
N
i¼1
xi
j j
50, 100, 500
[ - 10, 10]
0
F3 x
ð Þ ¼ P
N
i¼1
P
i
j1
xj
 
!2
50, 100, 500
[ - 100, 100]
0
F4 x
ð Þ ¼ maxi
xi
j j; 1  i  N
f
g
50, 100, 500
[ - 100, 100]
0
F5 x
ð Þ ¼ P
N1
i¼1
½100 xiþ1  x2
i

2þ xi  1
ð
Þ2
50, 100, 500
[ - 30, 30]
0
F6 x
ð Þ ¼ P
N
i¼1
xi þ 0:5
j
j
ð
Þ2
50, 100, 500
[ - 100, 100]
0
F7 x
ð Þ ¼ P
N
i¼1
ix4
i þ random 0; 1
½

50, 100, 500
[ - 1.28, 1.28]
0
F8 x
ð Þ ¼ P
N
i¼1
xi sin
ﬃﬃﬃﬃﬃﬃ
xi
j j
p


50, 100, 500
[ - 500, 500]
- 418.9829 9 dim
F9 x
ð Þ ¼ P
N
i¼1
½x2
i  10 cos 2pxi
ð
Þ þ 10
50, 100, 500
[ - 5.12, 5.12]
0
F10 x
ð Þ ¼ 20 exp 0:2
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
N
P
N
i¼1
x2
i
s
 
!
 exp
1
N
P
N
i¼1
cos 2pxi
ð
Þ


þ 20 þ e
50, 100, 500
[ - 32, 32]
0
F11 x
ð Þ ¼
1
4000
P
N
i¼1
x2
i  Q
N
i¼1
cos
xiﬃ
i
p

 
þ 1
50, 100, 500
[ - 600, 600]
0
F12 x
ð Þ ¼ p
n
10 sin py1
ð
Þ þ P
n1
i¼1
yi  1
ð
Þ2 1 þ 10 sin2 pyiþ1
ð
Þ


þ yn  1
ð
Þ2


þ P
n
i¼1
u xi; 10; 100; 4
ð
Þ
yi ¼ 1 þ xiþ1
4 u xi; a; k; m
ð
Þ ¼
k xi  a
ð
Þmxi [ a
0  a\xi\a
k xi  a
ð
Þmxi\  a
8
<
:
50, 100, 500
[ - 50, 50]
0
F13 x
ð Þ ¼ 0:1
sin2 3px1
ð
Þ þ
X
n
i¼1
xi  1
ð
Þ2 1 þ sin2 pxi þ 1
ð
Þ


(
þ xn  1
ð
Þ2 1 þ sin2 2pxn
ð
Þ

o
þ
X
n
i¼1
u xi; 5; 100; 4
ð
Þ
50, 100, 500
[ - 50, 50]
0
F14 x
ð Þ ¼
1
500 þ P
25
j¼1
1
jþP2
i¼1 xiaij
ð
Þ
6
 
!1
2
[ - 65, 65]
1
F15 x
ð Þ ¼ P
11
i¼1
ai 
x1 b2
i þbix2
ð
Þ
b2
i þbix3þx4

2
4
[ - 5, 5]
0.00030
F16 x
ð Þ ¼ 4x2
1  2:1x4
1 þ 1
3 x6
1 þ x1x2  4x2
2 þ 4x4
2
2
[ - 5, 5]
- 1.0316
F17 x
ð Þ ¼ x2  5:1
4p2 x2
1 þ 5
p x1  6


þ 10 1  1
8p


cos x1 þ 10
2
[ - 5, 5]
0.398
F18 x
ð Þ ¼ 1 þ x1 þ x2 þ 1
ð
Þ2 19  14x1 þ 3x2
1  14x2 þ 6x1x2 þ 3x2
2


h
i
 30 þ 2x1  3x2
ð
Þ2 18  32x1 þ 12x2
1 þ 48x2  36x1x2 þ 27x2
2


h
i
2
[ - 2, 2]
3
3
[1, 3]
- 3.86
7214
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 9
2.3.1 Computational complexity analysis of the proposed
STA algorithm
Computational complexity serves as an important metric
for assessing the effectiveness of methods in dealing with
optimization problems. Numerous factors impact a tech-
nique’s complexity, including the number of individuals
involved (n), the dimensionality of the problem’s variables
(d), and the maximum number of iterations (tmax). In the
case of STA, the comprehensive computational complexity
can be deﬁned as follows:
O STA
ð
Þ ¼ Oðproblem definition) þ O(initialization)
þ Oðfunction evaluationÞ þ Oðposition updating in Spiral Motion phaseÞ
þ Oðposition updating in Tornado Formation phaseÞ
þ ðposition updating in Jetstream phase)
¼ O 1 þ n þ Tn þ 1
2 Tnd þ 1
2 Tnd þ Tnd


ﬃO 2Tnd þ Tn þ n
ð
Þ
3 Experimental results and discussion
The existing examination evaluates the efﬁciency of the
STA by several benchmark functions and real-world opti-
mization issues. Two series of benchmark test functions
ensemble including twenty-three classical functions, and
ten CEC2019 benchmarks are employed to the numerical
assessment phase; furthermore, ﬁve engineering optimiza-
tion problems have been selected as exemplars of real-
world challenges. The STA algorithm has been employed
for 500 iterations with a population size of 50 to address
both the benchmark functions and practical applications.
To assess the stability and reliability of the STA algorithm,
it has been implemented independently 30 individual runs.
The results, including the mean performance, standard
deviation (STD), the worst-so-far solutions, and the best-
so-far solutions, have been documented. In order to afﬁrm
the superior performance of STA, it has been subjected to a
rigorous comparison with a renowned metaheuristic opti-
mization technique using both the Wilcoxon rank-sum test
(WRST) and Friedman’s mean rank test. These tests serve
to validate the STA algorithm’s dominance, as detailed in
the subsequent sections.
3.1 Definition of twenty-three classical test
functions
In this subsection, a set of widely recognized benchmark
functions is used to assess the performance of the STA
method introduced in this paper. These benchmark func-
tions are categorized into three groups: unimodal, multi-
modal, and multimodal functions with ﬁxed dimensions.
The group of unimodal benchmark test functions includes
Table 1 (continued)
Function
Dim
Range
fmin
F19 x
ð Þ ¼  P
4
i¼1
ciexp  P
3
j¼1
aij xj  pij

2
 
!
F20 x
ð Þ ¼  P
4
i¼1
ciexp  P
6
j¼1
aij xj  pij

2
 
!
6
[0, 1]
- 3.32
F21 x
ð Þ ¼  P
5
i¼1
X  ai
ð
Þ X  ai
ð
ÞTþci

1
4
[0, 10]
- 10.1532
F22 x
ð Þ ¼  P
7
i¼1
X  ai
ð
Þ X  ai
ð
ÞTþci

1
4
[0, 10]
- 10.4028
F23 x
ð Þ ¼  P
10
i¼1
X  ai
ð
Þ X  ai
ð
ÞTþci

1
4
[0, 10]
- 10.5363
Neural Computing and Applications (2025) 37:7207–7260
7215
123

---

## Page 10
Fig. 5 Qualitative metrics of
some mathematical benchmark
functions: 2D views of the
functions, search history, and
convergence curve using the
STA algorithm
7216
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 11
seven functions denoted as F1 to F7. Each of these func-
tions has a single global optimal solution, making them a
common choice for evaluating the algorithm’s proﬁciency
in effectively exploiting local solutions. On the other hand,
the multimodal functions, from F8 to F23, not only feature
a globally optimal solution but also comprise multiple
locally optimal solutions. These functions are used to
challenge the technique’s ability to explore globally and
avoid falling into local optima. Table 1 presents the
mathematical formulas and characteristics of these bench-
mark functions.
3.2 Convergence analysis of STA
Figure 5 shows qualitative metrics for the analysis of the
convergence and performance of the proposed STA tech-
nique in the benchmark functions. The ﬁrst column of the
chart provides a visual representation of the functions in a
two-dimensional format, offering vision into the topologi-
cal characteristics of the search space. The second column
depicts the search history, serving as the ﬁrst discussed
metric. This representation showcases a more clustered
distribution of the population around optimal points in
unimodal functions and a more dispersed performance in
the case of multimodal functions. The former pattern aids
in effectively exploiting results as needed for unimodal
functions, while the latter signiﬁes exploration across the
domain, assisting the proposed STA algorithm in searching
the entire space for multimodal functions.
The third metric is the convergence curve, illustrating
the progress of the best solution found up to that point. The
ﬁgure presents a deﬁnite shape for the convergence curve
corresponding to each function group. In unimodal func-
tions, this curve appears notably smooth, showcasing a
consistent improvement in results as iterations progress.
Conversely, for multimodal functions, the curve takes on a
stepwise behavior, a characteristic often observed in such
functions. It’s evident from each group that in unimodal
functions, STA quickly identiﬁes and converges toward the
optimal solution in the early iterations, striving to enhance
solutions as iterations continue. In contrast, for multimodal
functions, populations persistently explore the entire area
even in the later iterations, in their pursuit of discovering
better solutions.
3.3 Sensitive analysis of the STA
This subsection emphases on the sensitivity examination of
a control parameter utilized in STA. This parameter is TF
that contribute to the optimization process. This parameter
is evaluated at one value from 0.1 to 0.9; consequently,
there are 9 scenarios for each value of TF parameter as
shown in Table 2. In this evaluation, The STA technique is
employed for 500 iterations with a population size of 50 to
address eight benchmark functions (namely, F1, F3, F5, F8,
F10, F13, F17, and F21).
Table 3 displays the statistical outcomes achieved across
these functions in different scenarios. An analysis of the
results reveals that the seventh scenario, where TF
(Transfer function) is set to 0.7, consistently produces
superior results across all tested functions when compared
to other scenarios. Subsequently, the sixth and eighth
scenarios secure the second and third positions, respec-
tively, in terms of performance.
3.4 Scalability analysis of the STA
The effect of varying the number of solutions is studied
across a range of benchmark functions. To comprehen-
sively assess STA’s sensitivity to parameters, a multitude
of solution numbers (i.e., 10, 20, 30, 40, and 50) are sys-
tematically tested, allowing for a comparison of the chan-
ges in solution numbers over 500 iterations. The results
demonstrate that even when employing different search
agents, the STA optimizer retains its advantages, indicating
that STA exhibits robustness and is less susceptible to the
inﬂuence of population size variations. Also, the results
show that the best solution for the most functions when the
population size is 40 as shown in Fig. 6. Therefore, the
population size will be 40 for the rest of problem in the
whole of paper.
3.5 Simultaneous analysis of population size
and transfer function parameter
To conﬁrm the choice of a transfer function (TF) value of
0.7 and to understand the interplay between population size
and TF parameters, it is essential to conduct a thorough
analysis. These factors are often interdependent, meaning
that changes in one can signiﬁcantly inﬂuence the behavior
and outcomes of the other. This section explores the
necessity and beneﬁts of simultaneously analyzing popu-
lation size and TF parameters to achieve more precise and
Table 2 Scenarios of the tuning
parameter
Scenario no
TF value
1
0.1
2
0.2
3
0.3
4
0.4
5
0.5
6
0.6
7
0.7
8
0.8
9
0.9
Neural Computing and Applications (2025) 37:7207–7260
7217
123

---

## Page 12
Table 3 Effect of the STA parameter (i.e., TF) tested on several benchmark functions
Fun no
Measure
Scenario no
Scenario 1
Scenario 2
Scenario 3
Scenario 4
Scenario 5
Scenario 6
Scenario 7
Scenario 8
Scenario 9
F1
Best
5.1E-285
4.1E-285
2.1E-293
2.5E-297
0
0
0
0
0
Mean
2E-252
8.7E-255
9.2E-259
5.4E-263
3.8E-272
8.4E-281
1.5E-298
0
0
Worst
4E-251
1.7E-253
1.4E-257
1.1E-261
7.5E-271
1.5E-279
3E-297
0
0
Std
0
0
0
0
0
0
0
0
0
F3
Best
9E-284
1.1E-286
1.6E-293
5.7E-296
0
0
0
0
0
Mean
6.2E-247
1.1E-244
1.9E-254
6E-259
1.7E-253
6.1E-291
3.2E-302
0
0
Worst
1.2E-245
2.2E-243
3.7E-253
1.2E-257
3.4E-252
1.1E-289
6.4E-301
0
0
Std
0
0
0
0
0
0
0
0
0
F5
Best
0.031441
0.052195
0.133658
0.078908
0.074772
0.009377
0.487775
0.156419
0.196188
Mean
8.46689
10.68305
21.10775
13.33364
15.86999
5.617916
14.07777
5.762929
12.74664
Worst
26.78626
26.75084
27.06626
26.82969
26.84433
26.71339
26.68714
26.49116
26.80643
Std
12.21611
13.42055
11.04624
13.78411
13.39902
11.03442
12.998
10.82241
13.03734
F8
Best
- 12,568.6
- 12,569.4
- 12,569.1
- 12,568.6
- 12,569.2
- 12,569.4
- 12,569.5
- 12,569.2
- 12,568.6
Mean
- 12,546.5
- 12,568
- 12,563.9
- 12,486.3
- 12,519.9
- 12,567.7
- 12,568.6
- 12,521.8
- 12,438.2
Worst
- 12,350.1
- 12,566.7
- 12,527.6
- 12,222.3
- 12,220.8
- 12,565.2
- 12,567.8
- 12,349.3
- 11,891.2
Std
69.01128
0.800318
12.78822
129.2528
112.8739
1.515989
0.484987
91.10059
215.8892
F10
Best
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
Mean
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
Worst
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
8.88E-16
Std
0
0
0
0
0
0
0
0
0
F13
Best
0.000372
0.001322
0.000881
0.000442
0.000745
0.001451
0.001849
0.001924
0.003582
Mean
0.004026
0.006679
0.008521
0.00815
0.007496
0.004951
0.011466
0.024497
0.011765
Worst
0.012912
0.016034
0.023166
0.016596
0.024839
0.014294
0.030762
0.134355
0.026751
Std
0.004762
0.005972
0.008577
0.006607
0.008062
0.004975
0.011046
0.040342
0.008792
F14
Best
0.998004
0.998004
0.998004
0.998004
0.998004
0.998004
0.998004
0.998004
0.998004
Mean
1.987311
1.196809
1.295817
2.284728
1.79204
1.196414
1.693032
2.768162
2.384131
Worst
5.928845
1.992031
2.982105
5.928845
2.982105
2.982105
2.982105
10.76318
5.928845
Std
1.612014
0.419119
0.669811
1.616004
0.911728
0.627428
0.816969
2.977148
1.557577
F17
Best
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
Mean
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
Worst
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
Std
0
0
0
0
0
0
0
0
0
7218
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 13
reliable results. Speciﬁcally, three scenarios for the TF
parameter values (0.6, 0.7, and 0.8) are considered, with a
constant population size of 40. From these scenarios,
Scenario 7a (TF = 0.7 and population size = 40) achieved
the best solutions for the most functions. This indicates that
a TF value of 0.7, in combination with a population size of
40, provides a more optimized and effective modeling
framework as shown in Table 4 and Fig. 7.
3.6 Dynamic evolution of other parameters
in STA algorithm
This subsection illustrates the dynamic changes in the other
parameters over iterations. The resulting plots, displayed in
Fig. 8a–c,
demonstrate
how
these
parameters
evolve
throughout the optimization process, providing visual
insight into their behavior.
3.7 Performance of the proposed STA algorithm
In this subsection, we compare the results obtained using
the STA algorithm with those of recent optimization
algorithms such as the tunicate swarm algorithm (TSA)
[23], salp swarm algorithm (SSA) [24], sine cosine algo-
rithm (SCA) [25], multi-verse optimizer (MVO) [26], moth
ﬂame optimization (MFO) [12], grey wolf optimizer
(GWO) [10], whale optimization algorithm (WOA) [13],
Runge–Kutta optimizer (RUN) [27], weighted mean of
vectors (INFO) [28], particle swarm optimization (PSO)
[29], and differential evolution (DE) [3]. The analysis was
conducted using MATLAB R2016a on a Windows 8.1,
64-bit operating system. All computations were performed
on a computer with an Intel Core i5-4210U CPU running at
a speed of 2.40 GHz and 8 GB of RAM. Table 5 presents
the parameter settings for the optimization methods.
3.8 Stability analysis of STA
With the purpose of evaluate the consistency and effec-
tiveness of the proposed STA optimizer in handling high-
dimensional optimization challenges, thirteen functions
from Tables 6, 7, and 8 have been employed. These
functions are tested at three different dimensional levels,
speciﬁcally, 50, 100, and 500 dimensions. The tables pre-
sent calculated values for the worst, average, best, and
standard deviation (STD) across the benchmark functions,
providing a comprehensive overview of the algorithm’s
performance in these high-dimensional scenarios. These
tables present the results of STA and other algorithms on
unimodal test functions (F1–F7). The results indicate that
STA consistently outperforms the majority of the tested
approaches across a signiﬁcant portion of these evaluation
functions. These ﬁndings serve to underscore STA’s
Table 3 (continued)
Fun no
Measure
Scenario no
Scenario 1
Scenario 2
Scenario 3
Scenario 4
Scenario 5
Scenario 6
Scenario 7
Scenario 8
Scenario 9
F21
Best
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
Mean
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 9.13816
- 10.146
Worst
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 10.1532
- 5.0552
- 10.0811
Std
2.68E-08
3.69E-09
2E-08
1.43E-08
9.28E-09
2.68E-08
1.74E-09
2.139925
0.022797
Mean
5.422222
5.238889
5.572222
5.661111
5.088889
4.172222
4.166667
4.75
4.927778
Ranking
7
6
8
9
5
2
1
3
4
Neural Computing and Applications (2025) 37:7207–7260
7219
123

---

## Page 14
Fig. 6 Effect of the STA search
agents tested on several
benchmark functions
7220
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 15
remarkable capacity for exploitation, enabling it to efﬁ-
ciently converge toward optimal solutions with precision
and speed. Functions F8 through F13, characterized by
their multimodal nature in high dimensions, are speciﬁcally
scrutinized in the tables. The data presented in these
tables clearly illustrate STA’s exceptional prowess in
exploration when compared to alternative methods. Nota-
bly, in the case of high-dimensional multimodal functions,
STA surpasses all other algorithms. Furthermore, it’s worth
noting that STA often achieves the global optimum in most
problems with a precision level (Std) that closely rivals that
of high-performance algorithms. STA’s proﬁciency in
Table 4 Effect of the STA parameters (i.e., TF and population size) tested on several benchmark functions
Fun no
Measure
Scenario no
Scenario 6a
Scenario 7a
Scenario 8a
F1
Best
0
0
0
Mean
6.1E-282
0
4.5E-291
Worst
6.1E-281
0
4.5E-290
Std
0
0
0
F3
Best
0
0
0
Mean
3.5E-279
0
1.5E-291
Worst
3.5E-278
0
1.5E-290
Std
0
0
0
F5
Best
0.149669
0.094993
0.255372
Mean
8.589324
8.16284
10.53579
Worst
26.80054
27.19263
26.75991
Std
12.29507
12.58151
12.16273
F8
Best
- 12,568.6
- 12,569.5
- 12,568
Mean
- 12,539.6
- 12,564.9
- 12,474.3
Worst
- 12,344
- 12,553.9
- 11,986.9
Std
69.51059
5.052002
186.7556
F10
Best
8.88E-16
8.88E-16
8.88E-16
Mean
8.88E-16
8.88E-16
8.88E-16
Worst
8.88E-16
8.88E-16
8.88E-16
Std
0
0
0
F13
Best
0.003129
0.001756
0.002429
Mean
0.016029
0.012463
0.013953
Worst
0.032028
0.043148
0.03904
Std
0.010916
0.012456
0.013755
F14
Best
0.998004
0.998004
0.998004
Mean
3.061278
1.692637
2.570147
Worst
10.76318
2.982105
10.76318
Std
3.274854
0.941212
2.990575
F17
Best
0.397887
0.397887
0.397887
Mean
0.397887
0.397887
0.397887
Worst
0.397887
0.397887
0.397887
Std
0
0
0
F21
Best
- 10.1532
- 10.1532
- 10.1532
Mean
- 10.1532
- 10.1532
- 10.1532
Worst
- 10.1532
- 10.1532
- 10.1532
Std
2.13E-06
2.83E-08
7.21E-08
Ranking
2
1
3
Neural Computing and Applications (2025) 37:7207–7260
7221
123

---

## Page 16
exploration is attributed to its unique optimization stages.
In summary, the extensive evaluation demonstrates the
remarkable proﬁciency of the proposed STA algorithm in
terms of both exploitation and exploration, as observed
across a range of benchmark functions. It consistently
outperforms other algorithms on the majority of test
problems, underscoring its effectiveness in locating global
optima for both unimodal and multimodal functions. The
innovative jetstream mechanism plays a pivotal role in
augmenting the exploration process, enabling the algorithm
to navigate the solution space efﬁciently and uncover high-
quality solutions.
The test results of STA when it is used to solve the
composite benchmark functions are displayed in Table 9.
The means in the table present that STA is superiorly
competitive on the composite benchmark functions, per-
forming superlative on eight of the ten functions.
3.8.1 Wilcoxon’s rank test results
In this subsection, the differences between STA and other
techniques are further analyzed statistically using the
Wilcoxon rank-sum test (WRST), which is a paired test
that checks for signiﬁcant differences between two algo-
rithms. The results of the test between STA and each
technique at a signiﬁcance level of a = 0.05 are presented
in Tables 10, 11, 12, and 13, where the symbols ‘‘?/=/ - ’’
show whether STA executes better, likewise, or worse than
the comparison technique. Tables also present the statisti-
cal outcomes for STA across various dimensions and
functions,
indicating
whether
STA
exhibits
superior,
equivalent, or inferior performance compared to the ref-
erence algorithm. Notably, STA consistently surpasses
other well-known techniques in the statistical assessments
of F1–F13 across different dimensions (Dim=50, 100, 500)
and in ﬁxed-dimensional functions F14–F23. These results
afﬁrm the substantial superiority of STA across a wide
array of functions when compared to alternative tech-
niques. Therefore, it is concluded that the STA technique
shows the best performance compared to well-known
optimization techniques.
3.8.2 Friedman’s rank test results
Table 14 shows the statistical results attained by Friedman
tests for Dim=50 [30]. The smaller the ranking value, the
better the performance of the techniques. The statistical
results obtained by Friedman tests between STA and each
technique are presented in Tables 14, 15, 16, and 17. From
the results, the highest ranking presents that STA is the best
optimizer among the eight techniques.
Furthermore, radar charts and mean ranks, obtained
through the Friedman test for all 23 benchmark functions
across various algorithms, are depicted in Figs. 9 and 10.
These visual representations make it clear that the proposed
STA algorithm achieves the lowest mean rank value,
Fig. 7 Simultaneous analysis of population size and transfer function (TF) parameter in STA
7222
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 17
Fig. 8 Parameter’s evolution
over 500 iterations,
demonstrating its variation as
inﬂuenced by iteration number
and random factors
Neural Computing and Applications (2025) 37:7207–7260
7223
123

---

## Page 18
signifying its top-ranking status among all the techniques.
As a result, according to the Friedman test methodology,
the STA technique emerges as the best performing algo-
rithm in this comparative analysis.
3.9 The performance of the STA technique
for the CEC2019 function
The algorithm benchmarking made use of the CEC2019
function, and the evaluation of their performance was
conducted with the demanding benchmark functions from
the CEC2019 test suite, as outlined in Table 18 [31]. This
test suite features ten exceptionally challenging and com-
plex composite functions, providing a stringent assessment
for the algorithms. The proﬁles of these benchmark func-
tions are elaborated in Table 18. As described in the pre-
vious
section,
the
proposed
STA
and
seven
other
algorithms for comparison were individually run 20 times
on each function, with ﬁxed parameters of a maximum
iteration (500) and a population size (20).
The results, including the best, mean, worst values, and
standard deviation, derived from this testing, are presented
in Table 19. An examination of Table 19 reveals that STA
surpasses the other six algorithms in performance across
these test functions, with the exception of the SSA
algorithm. To sum it up, this section extensively validates
the effectiveness and superiority of the STA method
through a series of experiments on both classical bench-
mark functions and the IEEE CEC2019 test suite. Whether
dealing with straightforward or intricate numerical chal-
lenges, STA consistently delivers commendable results.
The convergence plot of the executed algorithms is
depicted in Fig. 11. A close examination of these curves
reveals that, for most functions, STA exhibits comparable
convergence. Furthermore, the ﬁndings indicate that STA
attains more stable and resilient solutions across the range
of functions tested.
3.9.1 Wilcoxon’s rank test results
In this subsection, the differences between STA and other
techniques are further analyzed statistically by the Wil-
coxon rank-sum test (WRST). Table 20 presents the sta-
tistical results of STA for CEC 2019 benchmark functions,
signifying whether STA achieves better, similarly, or worse
than the comparison technique. STA outperforms other
recent techniques in the statistics of CEC 2019 benchmark
functions, which approves the signiﬁcant dominance of
STA in most functions compared to other techniques.
Table 5 Conﬁguration parameters of optimization algorithms used for the comparative evaluation of the STA algorithm
Algorithms
Parameters setting
Value
STA
TF
0.7
TSA
Parameter pmin
1
Parameter pmax
4
SSA
m0
0
SCA
A
2
MVO
Existence probability
[0.2 1]
Traveling distance rate
[0.6 1]
MFO
Convergence constant a
[ - 2 - 1]
Spiral factor b
1
GWO
Convergence constant a
[2 0]
WOA
Convergence constant a
[2 0]
Spiral factor b
1
INFO
Updating rule, vector combining, and a local search
c = 2, d = 4
PSO
Topology
Fully connected
Cognitive constant
1
Social constant
1
Inertia weight
Linear reduction from 0.9 to 0.1
Velocity limit
10% of the dimensions range of the variables
DE
Lower bound of scaling factor
0.2
Upper bound of scaling factor
0.8
Crossover probability
0.2
7224
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 19
Table 6 Numerical results of test functions by the STA technique and other recent techniques (Dim = 50)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F1
Best
0
4.94E-18
0.004906
33.32809
5.210607
335.0467
1.04E-22
7.7E-92
3.2E-189
2.22E-54
71.98515
1.646147
Mean
0
3.64E-17
0.016992
297.8526
6.336375
6730.139
3.94E-22
9.61E-80
9.7E-181
1.47E-53
156.8815
2.264439
Worst
0
9.95E-17
0.031853
596.2896
9.423383
20,986.97
1.9E-21
7.26E-79
9.7E-180
2.58E-53
220.9806
3.448237
Std
0
3.32E-17
0.008844
185.8823
1.149383
7003.32
5.39E-22
2.33E-79
0
8.59E-54
48.31066
0.524019
F2
Best
1.1E-166
7.79E-12
3.43301
0.027616
2.545176
25.89061
4.3E-14
8.21E-58
2.6E-106
1.37E-26
7.300573
0.354093
Mean
2.6E-156
2.73E-11
6.859054
0.273129
211.4024
69.51458
1.43E-13
9.2E-54
9.7E-101
2.92E-26
11.19535
0.438072
Worst
1.9E-155
7.08E-11
11.18203
0.884014
1026.436
109.9938
3.08E-13
6.52E-53
7E-100
5.08E-26
20.28549
0.546616
Std
6.2E-156
2.34E-11
2.512395
0.274395
301.739
26.07109
8.36E-14
2.06E-53
2.3E-100
1.04E-26
3.69193
0.067005
F3
Best
0
0.06713
2860.627
19,823.75
2346.106
28,472.9
0.000113
150,280.6
7.3E-172
7.91E-51
3356.175
95,848.25
Mean
0
3.904113
5372.172
47,214.44
3631.238
66,863.24
0.058813
189,225.4
1E-156
3.14E-50
7534.004
115,156.4
Worst
2.7E-308
22.01668
13,062.56
71,107.93
5632.253
101,453.1
0.204459
242,694.3
6.9E-156
7.19E-50
13,233.57
145,512.4
Std
0
6.649753
3029.367
17,275.57
1057.151
22,405.94
0.069756
26,995.59
2.3E-156
2.03E-50
3531.584
15,138.68
F4
Best
1.1E-165
1.132868
11.66573
54.31861
6.682571
71.55181
1.79E-05
0.007274
8.8E-92
9.38E-28
15.52084
43.01534
Mean
3.9E-147
5.9826
16.01565
68.22212
12.39642
80.77858
9.3E-05
63.79077
2.05E-82
1.92E-27
19.48773
46.30453
Worst
3.9E-146
14.71519
20.09609
79.46513
18.59179
85.50423
0.000317
89.64472
2.02E-81
3.03E-27
23.74059
50.85756
Std
1.2E-146
3.560643
2.781428
7.48548
3.894705
4.296418
9E-05
27.11176
6.4E-82
7.22E-28
2.584407
2.655663
F5
Best
0.507384
46.29801
223.015
555,023.3
152.0399
86,127.17
45.88793
47.36974
42.30211
42.01119
1126.573
1584.619
Mean
2.482297
48.31843
629.1213
4,621,271
1075.32
374,194.9
47.10489
48.28409
45.08219
42.91719
9265.137
2722.944
Worst
10.05396
48.82544
1467.098
11,707,299
3195.382
1,114,389
48.42923
48.61907
47.71038
45.76272
32,379.57
5385.467
Std
2.805999
0.789266
488.8727
4,001,865
995.0657
385,811
0.975488
0.39635
1.69276
1.22528
9547.532
1270.351
F6
Best
0.008724
4.790712
0.004036
22.16827
4.513485
694.4274
1.498429
0.227273
1.17E-08
5.19E-07
26.92149
1.585543
Mean
0.01149
6.459395
0.071517
1018.466
7.001966
8642.816
2.427215
0.5979
1.93E-08
3.95E-06
169.6937
2.480075
Worst
0.014997
8.165545
0.269641
2431.091
9.977119
19,963.65
3.442145
0.95174
3.81E-08
1.97E-05
327.6728
3.717883
Std
0.002124
1.173835
0.092692
835.1625
1.640179
5938.867
0.700231
0.227541
8.42E-09
5.88E-06
103.7083
0.670122
F7
Best
2.86E-06
0.009345
0.276106
0.318376
0.045404
1.339389
0.001459
0.0001
3.04E-05
8.91E-05
0.254364
0.152597
Mean
3.2E-05
0.017204
0.359529
3.627413
0.086992
11.59266
0.002251
0.00459
0.000164
0.001071
0.364667
0.186942
Worst
9.01E-05
0.030836
0.463542
14.25454
0.108367
47.45529
0.00355
0.015745
0.000266
0.002323
0.531178
0.210389
Std
2.93E-05
0.006706
0.069661
4.551747
0.018973
13.65194
0.000767
0.00576
7.73E-05
0.000915
0.093351
0.019745
F8
Best
- 20,948.3
- 10,201.3
- 12,471.6
- 6256.98
- 13,669.2
- 16,289.6
- 11,229.8
- 20,949
- 14,251.9
- 14,820
- 11,614.8
- 11,229.8
Mean
- 20,747.9
- 8903.03
- 11,301.3
- 5054.39
- 12,690.7
- 13,808.3
- 9578.55
- 17,819.2
- 12,525.8
- 13,981.5
- 9848.42
- 9578.55
Worst
- 19,632.4
- 8046.88
- 10,410.1
- 4526.78
- 10,903.5
- 11,593.3
- 7952.33
- 13,657.4
- 10,966.3
- 12,712.2
- 8050.61
- 7952.33
Std
409.8983
652.4233
635.3939
567.5683
820.7617
1252.331
877.3302
3213.602
1031.787
639.7093
1040.304
877.3302
F9
Best
0
234.6548
27.89215
33.1459
141.3051
275.3027
2.84E-13
0
0
0
70.14356
227.472
Mean
0
385.7538
73.24871
99.37777
232.2828
334.1206
1.783417
0
0
0
91.95302
253.1081
Worst
0
466.2065
98.54029
184.8707
286.3291
439.9644
6.294313
0
0
0
139.4802
271.2363
Std
0
71.44653
25.66795
46.52476
48.83893
55.24766
2.506596
0
0
0
23.16544
14.55975
Neural Computing and Applications (2025) 37:7207–7260
7225
123

---

## Page 20
Therefore, it is concluded that the STA technique shows
the best performance compared to other methods.
3.9.2 Friedman’s rank test results
Table 21 shows the statistical results attained by Friedman
tests. From the results, we can get the ranks of eleven
techniques as follows: STA, INFO, MFO, SSA, MVO,
RUN, PSO, DE, GWO, WOA, TSA, and SCA.
To illustrate the ranking of all the compared techniques
for each of the ten benchmark functions, a radar
chart (Fig. 12) is employed. This outcome provides
additional conﬁrmation of our algorithm’s effectiveness in
uncovering global optima for a variety of problems.
In Fig. 13, the mean ranks derived from the Friedman
test for the CEC 2019 benchmark functions using various
algorithms are presented. This graph offers a compre-
hensive comparison of the algorithms’ performance on
these demanding benchmark functions. Mean ranks pro-
vide valuable insights into the relative effectiveness of
each algorithm, facilitating a more transparent assessment
of their overall performance.
4 STA for engineering design problems
In this section, we employ the proposed STA algorithm to
address a series of classical engineering problems char-
acterized by diverse constraints, encompassing both
equalities and inequalities. We evaluate the performance
of the STA technique in comparison to commonly utilized
optimization methods when tackling these engineering
design problems. The chosen problems for analysis are
widely recognized in the ﬁeld and encompass the three-
bar truss design (BTD), cantilever beam design (CBD),
welded beam design (WBD), speed reducer design (SRD),
and gear train design (GTD). Metaheuristic algorithms
have demonstrated their effectiveness in resolving such
constrained engineering challenges. To assess the efﬁ-
ciency of the proposed STA algorithm, we compared its
outcomes with those achieved by other metaheuristic
algorithms, which include the original TSA, SSA, SCA,
MVO, MFO, GWO, INFO, RUN, PSO, DE, and WOA
algorithms. For consistency, we maintain the same simu-
lation assumptions as outlined in the preceding section.
4.1 Three-bar truss design problem
The three-bar truss design is a well-known problem in
civil engineering, necessitating the adjustment of two
parameters to achieve the minimal weight when creating a
truss [32]. Figure 14 provides a visual representation of
Table 6 (continued)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F10
Best
8.88E-16
3.96E-10
2.944608
1.941069
2.251562
9.536026
1.29E-12
8.88E-16
8.88E-16
8.88E-16
4.247921
0.448162
Mean
8.88E-16
0.793999
3.969388
13.88716
2.898352
18.61905
3.76E-12
3.02E-15
8.88E-16
8.88E-16
6.098461
0.554878
Worst
8.88E-16
3.170612
5.106013
20.47026
4.198885
19.96462
8.14E-12
7.99E-15
8.88E-16
8.88E-16
8.471722
0.746894
Std
0
1.296854
0.661868
8.48939
0.577439
3.242559
2.15E-12
2.48E-15
0
0
1.199777
0.098698
F11
Best
0
0
0.086347
1.746396
1.043482
3.243613
0
0
0
0
1.629435
0.819291
Mean
0
0.006021
0.176798
8.855115
1.063598
64.79344
0.004122
0
0
0
2.944815
0.957524
Worst
0
0.023715
0.224638
39.36212
1.086747
184.891
0.030204
0
0
0
4.649402
1.023951
Std
0
0.009821
0.044595
11.27299
0.01329
57.96801
0.009796
0
0
0
0.788509
0.059627
F12
Best
0.00042
5.094209
4.442921
203,911.7
2.172469
572.7398
0.038673
0.006573
2.05E-09
2.52E-08
5.224863
1.372818
Mean
0.000587
10.6096
8.628854
8,210,509
5.829395
810,249.7
0.097574
0.018775
3.3E-09
1.13E-07
12.35002
1.908009
Worst
0.000901
18.86702
18.33786
57,132,888
11.33018
4,434,882
0.145051
0.039853
4.68E-09
5.01E-07
19.70848
2.665093
Std
0.000138
5.243874
4.060513
17,467,648
2.893219
1,503,950
0.036921
0.011515
8.93E-10
1.41E-07
5.340621
0.442747
F13
Best
0.007846
3.953745
43.12097
290,905.2
0.39604
35,635.68
1.319047
0.318217
6.7E-08
0.109128
66.41409
2.197696
Mean
0.024254
5.014923
63.30228
21,854,085
1.028946
82,687,306
1.852244
0.856902
0.006402
0.323894
80.21083
4.76924
Worst
0.053684
5.849648
91.49223
75,902,909
1.720694
4.11E ? 08
2.405556
1.654764
0.021024
0.882735
111.6855
6.717124
Std
0.018055
0.575313
16.51973
23,702,134
0.442204
1.73E ? 08
0.300261
0.378988
0.008917
0.224292
15.90642
1.558853
7226
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 21
Table 7 Numerical results of test functions by the STA technique and other recent techniques (Dim = 100)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F1
Best
0
4.1E-12
378.3603
865.5214
107.5467
11,857.36
1.73E-14
1.27E-89
3.5E-195
4.22E-54
2161.874
2620.355
Mean
7.8E-287
9.89E-11
591.4813
7917.665
127.9969
52,881.83
5.04E-14
1.91E-79
2.6E-168
5.99E-53
4155.112
2948.598
Worst
7.8E-286
5.06E-10
860.3858
16,946.95
158.5009
80,203.25
1.28E-13
1.52E-78
2.6E-167
1.35E-52
6866.153
3363.482
Std
0
1.59E-10
165.2978
5603.092
17.91651
21,214.56
3.53E-14
4.8E-79
0
5.21E-53
1309.889
243.2402
F2
Best
5.1E-168
1.1E-08
28.51299
1.345816
48,230.13
188.6975
3.06E-09
4.42E-57
3.4E-102
3.67E-26
46.23552
47.03475
Mean
8E-150
8.22E-08
36.22312
7.734513
3.21E ? 26
236.7506
6.99E-09
1.36E-52
1.3E-96
6.23E-26
64.38809
52.8432
Worst
5.5E-149
1.93E-07
45.19741
28.26774
3.21E ? 27
283.4226
1.83E-08
1.33E-51
7.95E-96
1.12E-25
85.95636
64.26155
Std
1.8E-149
5.17E-08
6.087066
8.238584
1.02E ? 27
32.66327
4.47E-09
4.18E-52
2.66E-96
2.54E-26
13.48897
5.590189
F3
Best
0
1608.512
20,124.78
132,024.1
49,764.28
166,062.3
13.83577
710,176.1
2.1E-158
4.06E-50
32,142.77
511,471.7
Mean
2.7E-287
7075.585
41,778.53
232,124.5
63,084.45
248,569.8
361.7355
912,806.9
5.2E-152
3.25E-49
47,700.97
618,769.8
Worst
2.7E-286
11,754.09
89,298.81
358,011.9
73,644.13
342,151.5
1618.854
1,282,225
2.8E-151
9.85E-49
65,843
747,777.6
Std
0
3349.821
22,841.31
70,510.1
7308.01
57,281.1
510.3926
168,393.6
8.9E-152
3.86E-49
11,339.44
72,058.66
F4
Best
2.2E-163
42.93747
19.91026
83.4743
54.53998
87.87274
0.039943
28.97343
1.55E-92
6.71E-28
26.77773
87.18888
Mean
1.5E-146
51.81269
24.81886
88.50527
58.03784
91.72805
0.381645
76.93045
6.65E-83
2.03E-27
31.00809
89.83904
Worst
1.5E-145
83.09193
31.20894
93.22804
65.78134
94.63268
1.83412
95.93349
4.21E-82
4.3E-27
38.01327
92.74066
Std
4.9E-146
11.44159
3.639748
2.793757
3.471043
2.627332
0.534005
24.70817
1.3E-82
1.11E-27
3.483549
1.649486
F5
Best
0.980602
97.74535
29,294.79
38,988,583
2674.524
93,050,917
95.93029
97.51317
94.55342
91.64101
481,832
3,773,920
Mean
6.332139
98.3651
59,116.76
1.19E ? 08
6981.168
1.67E ? 08
97.81836
98.09964
96.68201
93.78239
946,600.2
6,506,272
Worst
15.74872
98.62866
113,857.6
1.81E ? 08
33,372.45
2.39E ? 08
98.51145
98.27593
98.25104
95.42777
1,681,374
11,653,848
Std
5.64575
0.313931
28,592.57
47,008,190
9349.51
40,860,489
0.910646
0.232995
1.265715
1.157989
417,217.5
2,220,964
F6
Best
0.034199
12.36507
458.3328
3382.668
97.81795
34,136.61
6.657808
1.727985
5.39E-07
1.014726
3394.583
2313.334
Mean
0.047486
14.14842
734.3811
9346.223
121.936
60,976.1
8.138721
2.985413
0.000158
1.55265
4440.483
2805.015
Worst
0.078961
16.9627
1179.041
14,853.74
136.651
106,398
9.90864
5.384838
0.001494
2.305538
5885.616
3067.965
Std
0.012886
1.324649
205.5416
4913.27
12.46786
21,128.22
0.952747
1.02795
0.00047
0.426929
766.788
277.8063
F7
Best
8.3E-07
0.016629
1.087689
47.97846
0.306437
57.07258
0.003488
0.000103
1.58E-05
9.96E-05
2.58486
7.063484
Mean
2.17E-05
0.043235
1.845356
170.1335
0.524315
236.0788
0.004872
0.002072
0.00023
0.000957
5.050338
9.035567
Worst
6.22E-05
0.075556
2.908462
264.2855
0.668304
423.0744
0.00719
0.006339
0.000587
0.001791
10.83312
11.63818
Std
1.88E-05
0.018899
0.575068
70.18115
0.128859
133.4702
0.001002
0.002278
0.000198
0.000554
2.269359
1.733864
F8
Best
- 41,865.5
- 14,540.5
- 25,242.7
- 8919.39
- 25,411.4
- 25,941.3
- 19,934.6
- 41,895.4
- 28,015.5
- 28,036.7
- 21,731.5
- 18,529.9
Mean
- 41,774.2
- 13,229.4
- 22,321.2
- 7451.65
- 23,576.4
- 23,186.5
- 15,738
- 36,736.6
- 24,692.6
- 26,211.7
- 18,082.3
- 16,666.4
Worst
- 41,543.9
- 11,903.3
- 18,851.2
- 6126.82
- 22,336.4
- 18,641.6
- 6659.6
- 29,091.2
- 20,805.6
- 24,028.5
- 14,534.4
- 14,534.4
Std
107.3667
868.4634
2346.993
947.7936
1137.049
2121.292
3591.254
5334.586
2286.131
1662.977
2128.227
1491.002
F9
Best
0
773.7447
125.2122
152.5709
566.3136
664.5154
6.14E-11
0
0
0
256.4373
738.8997
Mean
0
956.2932
176.3458
263.5528
643.0111
799.0757
9.651146
0
0
0
346.8623
811.1128
Worst
0
1204.263
272.667
476.2615
776.2912
892.8116
18.24781
0
0
0
443.1879
872.0398
Std
0
139.0176
46.48856
115.0505
80.23399
70.41346
6.234152
0
0
0
55.03576
38.4504
Neural Computing and Applications (2025) 37:7207–7260
7227
123

---

## Page 22
this problem. The mathematical model for this design is
expressed as follows.
Minimize f A1; A2
ð
Þ ¼ l  2
ﬃﬃ
2
p
x1 þ x2


Subject to G1 ¼
ﬃﬃ
2
p
x1 þ x2
ﬃﬃ
2
p
x2
1 þ 2x1x2
P  r  0;
G2 ¼
x2
ﬃﬃ
2
p
x2
1 þ 2x1x2
P  r  0
G3 ¼
1
ﬃﬃ
2
p
x2 þ x1
P  r  0
In these equations, l ¼ 100 cm; P ¼ 2kN
cm2 ; r ¼ 2kN
cm2.
Variable range: 0  x1; x2  1:00,
This optimization problem holds signiﬁcant impor-
tance in civil engineering applications as it aims to attain
an efﬁcient and lightweight design for truss structures.
Table 22 shows the performance of several algorithms,
such as TSA, SSA, SCA, MVO, MFO, GWO, WOA,
INFO, RUN, PSO, DE, and the proposed STA algorithm
as well as the algorithms employed to solve three-bar
truss design issue including ray and sain [33], artiﬁcial
atom algorithm (AAA) [34], mine blast algorithm (MBA)
[35], differential evolution with dynamic stochastic
selection (DEDS) [36], grasshopper optimization algo-
rithm (GOA) [37], hybridizing particle swarm optimiza-
tion with differential evolution (PSO-DE) [38], and
cuckoo search algorithm (CS) [39]. The results reveal that
the STA algorithm outperforms the other algorithms. It
achieves a minimum weight of 263.895, with optimal
values for 9 1 and 9 2 being 0.788675 and 0.408248,
respectively. Figure 15 displays the convergence curves
and the boxplot for these algorithms while solving the
problem. Furthermore, Table 23 provides a comparative
analysis of the statistical results, with the mean and
standard deviation values obtained by the proposed STA
algorithm being superior to all other counterparts.
4.2 Cantilever beam design problem
The objective of the cantilever beam design problem is to
reduce the weight of a cantilever with ﬁve hollow blocks,
as depicted in Fig. 16 [40]. This involves ﬁve variables,
and the mathematical representation of the structural
optimization problem is as follows:
Consider: x~¼ x1x2x3x4x5
½

Minimize f X
ð Þ ¼ 0:0624 x1 þ x2 þ x3 þ x4 þ x5
ð
Þ
Subject to G X
ð Þ ¼ 61
x3
1
þ 37
x3
2
þ 19
x3
3
þ 7
x3
4
þ 1
x3
5
 1  0;
Variable range:0:01  xi  1:00; i 2 1; . . .:; 5:
Table 24 tabulates the optimal solutions to this prob-
lem attained by the STA optimizer and the results are
compared with these of recent techniques and the algo-
rithms used to solve cantilever beam design problem
Table 7 (continued)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F10
Best
8.88E-16
2.56E-07
6.823348
1.715173
3.956072
19.46019
1.7E-08
8.88E-16
8.88E-16
8.88E-16
9.929306
8.105028
Mean
8.88E-16
2.54E-06
8.470158
17.99463
10.77182
19.84911
3.1E-08
4.44E-15
8.88E-16
8.88E-16
11.23433
8.529307
Worst
8.88E-16
6.97E-06
11.95637
20.64303
20.26549
19.95754
4.59E-08
7.99E-15
8.88E-16
8.88E-16
13.06912
8.822892
Std
0
2.07E-06
1.581998
6.140519
8.039878
0.17521
1.02E-08
3.35E-15
0
0
1.04149
0.288819
F11
Best
0
4.57E-12
2.94161
9.838384
1.947822
363.1009
1.49E-14
0
0
0
28.30909
21.34351
Mean
0
0.003107
6.621054
100.8828
2.066827
505.6021
3.87E-14
0
0
0
39.41129
28.2486
Worst
0
0.031074
10.37547
203.679
2.476388
708.3487
1.31E-13
0
0
0
52.26416
32.03504
Std
0
0.009826
2.299602
72.36172
0.156005
120.593
3.41E-14
0
0
0
9.344024
3.263482
F12
Best
0.000424
5.415622
14.14765
1.01E ? 08
11.53487
49,188,224
0.111616
0.016963
3.28E-08
0.002051
39.71103
4,292,849
Mean
0.000675
12.28207
26.21394
3.04E ? 08
16.7856
2.82E ? 08
0.243176
0.029446
7.67E-08
0.006856
1122.436
9,405,800
Worst
0.00085
20.15531
49.16219
5.96E ? 08
27.1092
6.9E ? 08
0.424833
0.040757
2.24E-07
0.017215
6683.961
20,003,600
Std
0.000132
5.129635
11.13134
1.45E ? 08
4.570245
2.21E ? 08
0.075968
0.007438
5.82E-08
0.004643
2224.137
4,525,187
F13
Best
0.017214
10.36722
182.811
1.13E ? 08
107.0288
2.13E ? 08
5.587851
0.609042
0.00025
2.946222
43,123.9
13,059,823
Mean
0.039222
12.43319
493.9032
5.39E ? 08
154.832
6.67E ? 08
6.493904
1.740396
0.025125
5.598381
188,058.2
22,030,774
Worst
0.060058
15.45363
1683.419
8.77E ? 08
192.7361
1.11E ? 09
7.155638
2.707473
0.068181
9.897633
560,427.6
31,427,543
Std
0.01315
1.386865
510.5826
2.75E ? 08
23.44756
3.37E ? 08
0.479376
0.655007
0.022548
2.371115
161,403.6
5,828,554
7228
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 23
Table 8 Numerical results of test functions by the STA technique and other recent techniques (Dim = 500)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F1
Best
0
0.001893
62,067.97
106,814.6
69,212.2
1,101,214
0.000359
7.76E-85
3.4E-185
1.12E-53
131,315.6
1,464,623
Mean
6.2E-293
0.012947
70,965.19
164,070.5
88,323.78
1,162,497
0.000548
2.94E-76
3.8E-164
2.05E-52
159,498.3
1,506,774
Worst
6.2E-292
0.029717
77,541.7
228,785
100,655.4
1,222,267
0.00115
2.68E-75
2.9E-163
6.18E-52
173,739.4
1,555,415
Std
0
0.009072
5173.569
35,208.1
9127.749
44,543.91
0.000237
8.42E-76
0
2.16E-52
13,386.15
26,595.93
F2
Best
8.3E-165
0.004845
431.8474
23.0235
1.8E ? 154
1.64E ? 73
0.004109
2.76E-55
7.4E-99
1.4E-25
653.4217
1.3E ? 213
Mean
1.2E-153
0.006862
462.2622
66.5909
1.9E ? 218
2.2E ? 109
0.005531
1.19E-50
5.55E-89
2.82E-25
972.8254
3E ? 223
Worst
1.2E-152
0.014331
505.5605
138.8087
1.9E ? 219
2.2E ? 110
0.00757
9.49E-50
5.49E-88
4.33E-25
1169.916
3E ? 224
Std
3.7E-153
0.002746
21.20328
37.54569
65,535
7E ? 109
0.001046
2.94E-50
1.73E-88
1.06E-25
189.8349
65,535
F3
Best
0
982,117.5
793,322.8
6,570,642
1,598,513
4,200,822
235,225.7
11,310,381
1.5E-147
1.29E-47
608,338.4
13,133,362
Mean
2.6E-302
1,367,741
1,115,118
7,144,948
1,820,255
5,086,544
334,609.9
19,559,475
4.6E-136
4.71E-47
1,066,890
15,278,384
Worst
1.3E-301
1,693,425
1,357,365
8,053,920
1,988,160
6,906,083
443,497.7
31,840,128
3E-135
1.3E-46
1,745,694
19,277,264
Std
0
310,292.6
206,711.4
673,089.4
157,934.3
1,257,236
99,718.99
7,690,346
9.6E-136
3.6E-47
353,229.7
1,821,670
F4
Best
6.8E-175
99.04009
32.1551
98.81637
91.87189
98.62133
51.75566
41.75266
2.19E-84
1.91E-28
41.0117
98.80389
Mean
2.8E-140
99.20716
36.09473
99.11544
94.03506
98.77144
62.76924
87.66102
1.49E-78
1.18E-27
51.75798
99.21992
Worst
2.8E-139
99.41109
45.29265
99.41946
95.58507
98.92027
67.84426
98.97866
1.12E-77
2.93E-27
60.56493
99.46512
Std
8.7E-140
0.123676
4.162495
0.190769
1.17558
0.115321
4.456214
20.38406
3.49E-78
7.57E-28
6.526692
0.202991
F5
Best
3.609439
1380.159
16,697,856
1.41E ? 09
91,774,361
4.61E ? 09
497.4158
495.3234
492.6181
496.5455
74,741,695
6.59E ? 09
Mean
62.31615
43,487.94
20,515,939
1.74E ? 09
1.14E ? 08
4.93E ? 09
497.7697
496.0706
494.2847
496.7852
1.05E ? 08
7.04E ? 09
Worst
109.4461
172,168.2
26,196,244
2.21E ? 09
1.49E ? 08
5.39E ? 09
497.9476
496.7729
495.2495
497.0414
1.87E ? 08
7.33E ? 09
Std
42.8145
53,479.37
2,642,841
2.58E ? 08
20,678,691
2.33E ? 08
0.161382
0.518417
0.95265
0.177492
32,812,785
2.58E ? 08
F6
Best
0.39516
97.73253
66,769.06
73,047.18
78,253.23
1,099,287
86.35288
17.89194
1.083312
64.56382
137,787.5
1,473,120
Mean
0.511359
101.082
72,212.41
182,361.7
88,432.07
1,151,232
88.78923
23.78796
1.478187
69.18278
159,874.4
1,501,572
Worst
0.679021
105.8421
76,918.46
338,000.4
98,992.73
1,190,893
90.52986
29.57335
1.751566
74.76969
172,833.2
1,548,503
Std
0.097551
2.843378
3445.456
88,436.46
6057.424
31,783.97
1.352624
4.145
0.205294
3.277371
13,099.22
26,284.19
F7
Best
7.84E-07
0.762517
136.5866
12,228.86
619.6518
31,918.48
0.023291
3.12E-05
2.93E-05
0.000472
515.074
52,795.27
Mean
2.61E-05
1.528576
163.513
15,570.37
727.3755
36,364.8
0.035312
0.003164
0.000219
0.001261
897.7774
57,172.89
Worst
8.44E-05
3.089053
203.6756
22,352.78
869.8485
41,340.88
0.054219
0.013534
0.000567
0.002476
1631.962
60,363.92
Std
2.88E-05
0.778756
21.09103
3538.065
85.65161
3051.979
0.009082
0.004289
0.000168
0.000732
308.0781
2510.143
F8
Best
- 209,176
- 35,882.3
- 73,894.7
- 16,861
- 80,519.2
- 72,783.2
- 71,967
- 209,455
- 123,368
- 102,763
- 58,698.2
- 58,698.2
Mean
- 208,141
- 33,300.4
- 64,945
- 15,768.2
- 78,129.9
- 62,313.8
- 60,298.7
- 193,972
- 97,119.3
- 98,199.3
- 50,711.4
- 52,918.2
Worst
- 205,290
- 29,201.6
- 58,729.3
- 14,251.3
- 75,079.6
- 55,272.9
- 51,719
- 144,600
- 74,593.7
- 87,834.6
- 46,001.8
- 50,419.5
Std
1293.724
2423.981
4717.24
929.4627
1826.625
5465.831
6279.925
26,028.9
17,220.69
4238.092
3493.398
3145.718
Neural Computing and Applications (2025) 37:7207–7260
7229
123

---

## Page 24
Table 8 (continued)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F9
Best
0
5228.249
2723.724
379.8043
5911.853
6521.588
35.18143
0
0
0
3419.589
8504.725
Mean
0
5945.568
2915.717
1133.231
6321.152
6897.345
50.3377
0
0
0
3775.655
8652.841
Worst
0
6630.217
3093.985
2161.389
6720.62
7225.044
82.37053
0
0
0
4050.472
8750.344
Std
0
537.8106
140.248
541.1296
213.462
180.8596
13.58614
0
0
0
195.9292
72.78386
F10
Best
8.88E-16
0.003274
12.754
14.06618
20.78006
20.01038
0.000672
8.88E-16
8.88E-16
8.88E-16
15.27714
21.03636
Mean
8.88E-16
0.005354
13.35621
19.46291
20.82752
20.25615
0.000922
4.09E-15
8.88E-16
8.88E-16
15.88607
21.0774
Worst
8.88E-16
0.008477
13.9354
20.83839
20.8994
20.38568
0.001168
7.99E-15
8.88E-16
8.88E-16
16.39356
21.10121
Std
0
0.00169
0.329336
2.78739
0.032963
0.138704
0.000186
2.02E-15
0
0
0.322423
0.020788
F11
Best
0
0.000557
579.5803
1189.001
738.9494
10,055.73
3.87E-05
0
0
0
1239.765
13,169.59
Mean
0
0.001608
637.3652
1881.146
801.9722
10,331.76
0.008048
0
0
0
1453.111
13,558.8
Worst
0
0.003827
722.2998
3048.317
882.829
10,699.85
0.080008
0
0
0
1781.849
13,854.98
Std
0
0.000978
40.84853
604.472
45.31254
233.1235
0.025284
0
0
0
155.7532
248.8978
F12
Best
0.000377
173,650.5
38,856.61
4.78E ? 09
44,293,353
9.94E ? 09
0.653806
0.017164
0.001209
0.254133
17,481,355
1.64E ? 10
Mean
0.000706
600,131.9
172,645.9
6.19E ? 09
86,592,912
1.19E ? 10
0.693955
0.052096
0.001481
0.299525
40,707,475
1.74E ? 10
Worst
0.000905
2,906,619
301,758.8
7.07E ? 09
1.37E ? 08
1.32E ? 10
0.759184
0.082509
0.001726
0.363503
1.09E ? 08
1.81E ? 10
Std
0.000189
823,882.4
98,105.54
7.77E ? 08
27,567,071
8.58E ? 08
0.036453
0.020677
0.000162
0.028821
27,835,510
5.9E ? 08
F13
Best
0.163863
168,109.9
8,660,548
5.83E ? 09
1.76E ? 08
2.06E ? 10
47.09021
6.00445
1.251251
49.57657
1.45E ? 08
3.14E ? 10
Mean
0.230713
314,775.2
14,536,381
9.31E ? 09
2.69E ? 08
2.2E ? 10
49.19635
13.06554
2.889947
49.74887
2.15E ? 08
3.24E ? 10
Worst
0.289573
520,668.8
21,701,001
1.13E ? 10
3.76E ? 08
2.33E ? 10
50.50283
22.98249
3.922078
49.78513
3.2E ? 08
3.39E ? 10
Std
0.037716
130,224.5
4,132,938
1.88E ? 09
59,799,447
9.37E ? 08
1.174419
4.428498
0.836929
0.06128
60,140,174
7.06E ? 08
7230
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 25
Table 9 Numerical results of composite test functions by the STA technique and other recent techniques
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F14
Best
0.998004
0.998004
0.998004
0.998025
0.998004
0.998004
0.998004
0.998004
0.998004
0.998004
0.998004
0.998004
Mean
1.887908
9.467442
1.196414
2.188736
1.689498
1.887908
4.721197
1.891047
3.844082
2.76463
2.384526
1.887908
Worst
5.928845
15.50382
2.982105
2.982105
5.928845
5.928845
10.76318
2.982105
10.76318
10.76318
5.928845
5.928845
Std
1.642059
5.128187
0.627428
1.024235
1.6148
1.642059
4.258338
0.986546
3.74834
3.287764
1.485597
1.642059
F15
Best
0.000307
0.000308
0.000502
0.000484
0.000526
0.000566
0.000309
0.000317
0.000307
0.000307
0.000338
0.000857
Mean
0.000309
0.008453
0.00283
0.001099
0.000669
0.001656
0.008364
0.000839
0.000765
0.000674
0.000542
0.000959
Worst
0.000317
0.020363
0.020363
0.001559
0.00074
0.008334
0.020363
0.002252
0.001223
0.001223
0.000746
0.001134
Std
3.13E-06
0.010254
0.006165
0.000445
8.24E-05
0.002367
0.010328
0.000607
0.000483
0.000473
0.000114
9.82E-05
F16
Best
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
Mean
- 1.03163
- 1.03163
- 1.03163
- 1.0316
- 1.03163
- 1.03162
- 1.03162
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
Worst
- 1.03163
- 1.03163
- 1.03163
- 1.03155
- 1.03163
- 1.03159
- 1.03159
- 1.03163
- 1.03163
- 1.03163
- 1.03163
- 1.03163
Std
1.96E-16
5.4E-07
1.51E-14
2.75E-05
3.27E-07
1.23E-05
1.23E-05
5.77E-10
1.72E-13
5.35E-15
5.6E-15
5.35E-15
F17
Best
0.397887
0.397888
0.397887
0.398085
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
0.397887
Mean
0.397887
0.397912
0.397887
0.399802
0.397888
0.397887
0.397896
0.397893
0.397887
0.39809
0.39809
0.397888
Worst
0.397887
0.397969
0.397887
0.40375
0.397889
0.397888
0.397955
0.397916
0.397887
0.398959
0.398959
0.397895
Std
0
2.5E-05
2.68E-14
0.001765
3.74E-07
2.83E-07
2.1E-05
1.08E-05
3.04E-11
0.000429
0.000429
2.43E-06
F18
Best
3
3.000008
3
3
3
3
3
3
3
3
3
3
Mean
3
8.400024
3
3.000034
3.000004
3
3.000011
3.000013
3
3
3
3
Worst
3
30.00006
3
3.000095
3.000016
3.000001
3.000024
3.000041
3.000001
3.000001
3.000001
3.000001
Std
1.97E-15
11.38421
2.55E-13
3.36E-05
5.05E-06
3.25E-07
8.34E-06
1.52E-05
2.43E-07
2.43E-07
2.43E-07
2.43E-07
F19
Best
- 3.86278
- 3.86277
- 3.86278
- 3.86184
- 3.86278
- 3.86278
- 3.86278
- 3.86271
- 3.86278
- 3.86278
- 3.86278
- 3.86278
Mean
- 3.86278
- 3.86195
- 3.86278
- 3.85578
- 3.86278
- 3.86278
- 3.86194
- 3.85756
- 3.86278
- 3.86199
- 3.86278
- 3.86278
Worst
- 3.86278
- 3.8549
- 3.86278
- 3.85088
- 3.86278
- 3.86277
- 3.85492
- 3.82596
- 3.86278
- 3.85492
- 3.86277
- 3.86277
Std
6.55E-10
0.002477
7.43E-14
0.004038
7.37E-07
2.75E-06
0.00247
0.011236
6.13E-09
0.002485
3.66E-06
3.66E-06
F20
Best
- 3.322
- 3.32115
- 3.322
- 3.21771
- 3.32199
- 3.322
- 3.32199
- 3.32113
- 3.322
- 3.322
- 3.322
- 3.322
Mean
- 3.28611
- 3.26789
- 3.22065
- 2.86738
- 3.26193
- 3.25066
- 3.25552
- 3.2376
- 3.23877
- 3.26255
- 3.27444
- 3.26892
Worst
- 3.20114
- 3.15398
- 3.18014
- 2.24178
- 3.20085
- 3.2031
- 3.08056
- 3.04064
- 3.2031
- 3.2031
- 3.2031
- 3.20114
Std
0.057778
0.069004
0.053797
0.304519
0.063315
0.061396
0.092273
0.112977
0.057431
0.062662
0.061396
0.059554
F21
Best
- 10.1532
- 10.1461
- 10.1532
- 4.85594
- 10.1531
- 10.1532
- 10.152
- 10.153
- 10.1532
- 10.1532
- 10.1532
- 10.1532
Mean
- 9.6434
- 5.10638
- 8.39112
- 3.1047
- 8.63267
- 7.13429
- 8.89423
- 7.3576
- 10.1532
- 9.5536
- 8.90092
- 9.77729
Worst
- 5.0552
- 2.61976
- 2.68286
- 0.87829
- 5.05513
- 2.68286
- 2.63042
- 2.62996
- 10.1532
- 5.0552
- 2.68286
- 7.31463
Std
1.61213
3.477945
2.911156
1.750653
2.447805
3.299494
2.713752
3.02625
9.86E - 10
1.605544
2.700844
0.90985
F22
Best
- 10.4029
- 10.2978
- 10.4029
- 4.96823
- 10.4028
- 10.4029
- 10.4023
- 10.3997
- 10.4029
- 10.4029
- 10.4029
- 10.4029
Mean
- 10.4029
- 7.33299
- 8.10903
- 2.71188
- 8.04437
- 9.73501
- 10.4016
- 7.52469
- 9.25733
- 7.67612
- 8.344
- 10.4018
Worst
- 10.4029
- 1.82993
- 2.75193
- 0.90712
- 2.76589
- 3.7243
- 10.4002
- 1.83567
- 1.83567
- 2.7659
- 2.7659
- 10.3965
Std
5.7E - 08
3.771518
3.693541
1.880192
3.117236
2.111947
0.000675
3.332978
2.760538
3.57696
3.374895
0.002073
Neural Computing and Applications (2025) 37:7207–7260
7231
123

---

## Page 26
including generalized convex approximation (GCA) [41],
ant lion optimizer (ALO) [14], method of moving asymp-
totes (MMA) [41], symbiotic organisms search (SOS) [42],
and improved slime mold algorithm (ISMA) [43]. The
results demonstrate that the STA technique efﬁciently
solves the problem and the design with the minimum
weight
x~ = [6.014644
5.310063
4.494105
3.501842
2.153006].
Figure 17 illustrates the convergence curves and box
plots for all algorithms when dealing with the Cantilever
Beam Design problem. Table 25 presents the statistical
information, encompassing best, mean, median, worst, and
STD. Consequently, it can be inferred that the STA opti-
mizer exhibits greater consistency in addressing this
problem.
4.3 Welded beam design
The aim of this engineering problem is to minimize the
production cost of a welded beam [44]. It entails the con-
sideration of several optimization constraints, including
shear stress (s), buckling load on the bar (Pc), end
deﬂection of the beam (d), and bending stress in the beam
(h). The problem encompasses four variables: the thickness
of the weld (h), the length of the attached part to the bar (l),
the height of the bar (t), and the thickness of the bar (b) (as
depicted in Fig. 18). Mathematically, the problem can be
expressed as follows.
Consider : x~¼ x1x2x3x4
½
 ¼ hltb
½
;
Minimize f x~
ð Þ ¼ 1:1047x2
1x2 þ 0:04811x3x4 14:0 þ x2
ð
Þ;
Subject to g1 x~
ð Þ ¼ s x~
ð Þ  smax  0;
g2 x~
ð Þ ¼ r x~
ð Þ  rmax  0
g3 x~
ð Þ ¼ d x~
ð Þ  dmax  0;
g4 x~
ð Þ ¼ x1  x4  0;
g5 x~
ð Þ ¼ p  pc x~
ð Þ  0;
g6 x~
ð Þ ¼ 0:125  x1  0;
g7 x~
ð Þ ¼ 1:10471x2
1x2  0:0481x3x4 14:0 þ x2
ð
Þ  5:0  0
Variable range: 0:1  x1  2:00,
0:1  x2  10:0;
0:1  x3  10:0;
0:1  x4  2:00;
Table 26 shows the results achieved from the analysis,
representing that the STA technique outperforms other
techniques and the algorithms used to solve welded beam
design problem including such as GOA [37], ray opti-
mization (RO) [45], effective co-evolutionary differential
evolution (ECDE) [46], genetic algorithm (GA) [47],
Table 9 (continued)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F23
Best
- 10.5364
- 10.3575
- 10.5364
- 9.39089
- 10.5363
- 10.5364
- 10.536
- 10.5359
- 10.5364
- 10.5364
- 10.5364
- 10.5364
Mean
- 10.0003
- 4.33786
- 9.99562
- 5.10027
- 8.21714
- 8.54781
- 10.5348
- 8.13812
- 9.19621
- 7.71521
- 7.70842
- 8.51933
Worst
- 5.17565
- 1.85281
- 5.12848
- 3.07402
- 2.8066
- 2.87114
- 10.5331
- 2.8065
- 3.83543
- 2.42734
- 2.42734
- 2.42734
Std
1.695222
3.257715
1.710137
1.609525
3.733619
3.241771
0.000965
3.162138
2.825383
3.664768
3.729461
3.311793
7232
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 27
Table 10 Statistical results of the Wilcoxon rank-sum test (Dim = 50)
STA vs
Fun
TSA
SSA
SCA
MVO
MFO
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
F1
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F2
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F3
8.74E-05
?
8.74E-05
?
8.74E-05
?
8.74E-05
?
8.74E-05
?
F4
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F5
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F6
1.83E-04
?
1.73E-02
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F7
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F8
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F9
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F10
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F11
2.31E-04
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F12
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F13
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
WRST (? / = / - )
13/0/0
13/0/0
13/0/0
13/0/0
13/0/0
STA vs
Fun
GWO
WOA
RUN
INFO
PSO
DE
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
F1
6.39E-
05
?
6.39E-
05
?
6.39E-
05
?
6.39E-
05
?
6.39E-
05
?
6.39E-
05
?
F2
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F3
8.74E-
05
?
8.74E-
05
?
8.74E-
05
?
8.74E-
05
?
8.74E-
05
?
8.74E-
05
?
F4
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F5
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F6
1.83E-
04
?
1.83E-
04
?
1.83E-
04
-
1.83E-
04
-
1.83E-
04
?
1.83E-
04
?
F7
1.83E-
04
?
1.83E-
04
?
7.69E-
04
?
2.46E-
04
?
1.83E-
04
?
1.83E-
04
?
F8
1.83E-
04
?
3.45E-
01
=
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F9
6.39E-
05
?
NaN
=
NaN
=
NaN
=
6.39E-
05
?
6.39E-
05
?
F10
6.39E-
05
?
1.43E-
02
?
NaN
=
NaN
=
6.39E-
05
?
6.39E-
05
?
F11
1.68E-
01
=
NaN
=
NaN
=
NaN
=
6.39E-
05
?
6.39E-
05
?
F12
1.83E-
04
?
1.83E-
04
?
1.83E-
04
-
1.83E-
04
-
1.83E-
04
?
1.83E-
04
?
F13
1.83E-
04
?
1.83E-
04
?
1.13E-
02
-
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
WRST (? /
= / - )
12/1/0
10/3/0
7/3/3
8/3/2
13/0/0
13/0/0
Neural Computing and Applications (2025) 37:7207–7260
7233
123

---

## Page 28
Table 11 Statistical results of the Wilcoxon rank-sum test (Dim = 100)
STA vs
Fun
TSA
SSA
SCA
MVO
MFO
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
F1
1.32E-04
?
1.32E-04
?
1.32E-04
?
1.32E-04
?
1.32E-04
?
F2
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F3
8.74E-05
?
8.74E-05
?
8.74E-05
?
8.74E-05
?
8.74E-05
?
F4
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F5
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F6
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F7
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F8
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F9
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F10
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F11
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F12
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F13
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
WRST (? / = / - )
13/0/0
13/0/0
13/0/0
13/0/0
13/0/0
STA vs
Fun
GWO
WOA
RUN
INFO
PSO
DE
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
F1
1.32E-
04
?
1.32E-
04
?
1.32E-
04
?
1.32E-
04
?
1.32E-
04
?
1.32E-
04
?
F2
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F3
8.74E-
05
?
8.74E-
05
?
8.74E-
05
?
8.74E-
05
?
8.74E-
05
?
8.74E-
05
?
F4
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F5
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F6
1.83E-
04
?
1.83E-
04
?
1.83E-
04
–
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F7
1.83E-
04
?
1.83E-
04
?
1.01E-
03
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F8
1.83E-
04
?
2.83E-
03
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.73E-
04
?
F9
6.39E-
05
?
=
NaN
=
NaN
=
6.39E-
05
?
6.39E-
05
?
F10
6.39E-
05
?
5.66E-
03
?
NaN
=
NaN
=
6.39E-
05
?
6.39E-
05
?
F11
6.39E-
05
?
=
NaN
=
NaN
=
6.39E-
05
?
6.39E-
05
?
F12
1.83E-
04
?
1.83E-
04
?
1.83E-
04
–
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F13
1.83E-
04
?
1.83E-
04
?
6.40E-
02
=
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
WRST (? /
= / - )
13/0/0
11/2/0
7/4/2
10/3/0
13/0/0
13/0/0
7234
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 29
Table 12 Statistical results of the Wilcoxon rank-sum test (Dim = 500)
STA vs
Fun
TSA
SSA
SCA
MVO
MFO
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
F1
1.63E-04
?
1.63E-04
?
1.63E-04
?
1.63E-04
?
1.63E-04
?
F2
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F3
1.03E-04
?
1.03E-04
?
1.03E-04
?
1.03E-04
?
1.03E-04
?
F4
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F5
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F6
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F7
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F8
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F9
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F10
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F11
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
F12
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F13
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
WRST (? / = / - )
13/0/0
13/0/0
13/0/0
13/0/0
13/0/0
STA vs
Fun
GWO
WOA
RUN
INFO
PSO
DE
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
F1
1.63E-
04
?
1.63E-
04
?
1.63E-
04
?
1.63E-
04
?
1.63E-
04
?
1.63E-
04
?
F2
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F3
1.03E-
04
?
1.03E-
04
?
1.10E-
04
?
1.10E-
04
?
1.10E-
04
?
1.10E-
04
?
F4
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F5
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F6
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F7
1.83E-
04
?
1.31E-
03
?
1.31E-
03
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F8
1.83E-
04
?
9.10E-
01
=
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.78E-
04
?
F9
6.39E-
05
?
=
=
=
6.39E-
05
?
6.39E-
05
?
F10
6.39E-
05
?
5.31E-
04
?
=
=
6.39E-
05
?
6.39E-
05
?
F11
6.39E-
05
?
=
=
=
6.39E-
05
?
6.39E-
05
?
F12
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
F13
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
WRST (? /
= / - )
13/0/0
10/3/0
10/3/0
10/3/0
13/0/0
13/0/0
Neural Computing and Applications (2025) 37:7207–7260
7235
123

---

## Page 30
harmony search (HS) [48], an effective co-evolutionary
particle swarm optimization (CPSO) [49], and marine
predators algorithm (MPA) [21] by attaining a design with
the minimum cost value; it becomes evident that when the
parameters are set to h = 0.20572964, l = 3.47048867,
t = 9.03662391, and b = 0.20572964, the manufacturing
cost of the welded beam design problem can be reduced to
1.72485230859736. Thus, the proposed STA algorithm
exhibits promising capabilities in addressing the welded
beam design problem.
Figure 19 displays the convergence patterns and box
plots of all methods applied to the welded beam design
problem. In Table 27, you can ﬁnd statistical data,
including best, mean, median, worst, and STD. Thus, it can
be deduced that the STA technique exhibits superior reli-
ability for this problem, and the results underscore the STA
algorithm’s outperformance when compared to other
algorithms including WOA, SSA, SCA, MFO, MVO,
GWO, TSA, INFO, RUN, PSO, DE, Rao_1 [50], Rao_2
[50], Rao_3 [50], FISA [50], and MPA [21].
Table 13 Statistical results of the Wilcoxon rank-sum test
STA vs
Fun
TSA
SSA
SCA
MVO
MFO
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
F14
7.48E-04
?
5.31E-01
=
1.70E-02
?
8.14E-02
=
1.17E-01
=
F15
2.20E-03
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
?
F16
1.29E-04
?
1.28E-04
?
1.29E-04
?
1.29E-04
-
2.26E-02
-
F17
6.39E-05
?
5.89E-05
?
6.39E-05
?
6.39E-05
?
3.68E-01
=
F18
1.71E-04
?
1.71E-04
?
1.71E-04
?
1.71E-04
?
9.38E-01
=
F19
1.63E-04
?
3.29E-02
?
1.63E-04
?
1.63E-04
-
1.60E-03
-
F20
2.57E-02
?
3.76E-02
?
4.40E-04
?
2.11E-02
?
5.64E-01
=
F21
4.40E-04
?
7.91E-01
=
1.83E-04
?
2.20E-03
?
8.49E-01
=
F22
1.83E-04
?
3.45E-01
=
1.83E-04
?
1.83E-04
-
2.38E-02
-
F23
3.30E-04
?
7.34E-01
=
2.46E-04
?
1.31E-03
-
1.35E-01
=
WRST (? / = / - )
10/0/0
6/4/0
10/0/0
5/1/4
1/6/3
STA vs
Fun
GWO
WOA
RUN
INFO
PSO
DE
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
F14
5.70E-
03
?
3.73E-
02
?
2.76E-
02
?
3.73E-
01
=
4.46E-
01
=
1.17E-
01
=
F15
1.31E-
03
?
2.46E-
04
?
9.70E-
01
=
4.73E-
01
=
1.83E-
04
?
1.83E-
04
?
F16
1.29E-
04
?
1.29E-
04
?
1.29E-
04
?
1.47E-
03
?
1.14E-
02
?
1.47E-
03
?
F17
6.39E-
05
?
6.39E-
05
?
7.51E-
04
?
1.68E-
01
=
1.68E-
01
=
1.68E-
01
=
F18
1.71E-
04
?
1.71E-
04
?
1.64E-
02
?
1.06E-
02
–
8.77E-
01
=
1.12E-
02
-
F19
1.63E-
04
?
1.63E-
04
?
2.04E-
03
?
1.29E-
01
=
3.44E-
02
–
2.01E-
02
-
F20
3.12E-
02
?
1.73E-
02
?
7.34E-
01
=
2.66E-
01
=
9.82E-
02
=
8.50E-
01
=
F21
2.20E-
03
?
7.69E-
04
?
2.12E-
01
=
3.22E-
01
=
1.94E-
02
-
6.77E-
01
=
F22
1.83E-
04
?
1.83E-
04
?
9.70E-
01
=
4.71E-
01
=
1.39E-
01
=
2.41E-
01
=
F23
2.83E-
03
?
1.01E-
03
?
4.27E-
01
=
9.70E-
01
=
4.25E-
01
=
3.84E-
01
=
WRST (? /
= / - )
10/0/0
10/0/0
5/5/0
1/8/1
2/6/2
2/6/2
7236
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 31
Table 14 Friedman test for the twelve techniques (Dim = 50)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F1
1
6
7
10.8
9
12
5
3
2
4
10.2
8
F2
1
6
9.4
7.3
11.1
11.3
5
3
2
4
10.2
7.7
F3
1
5
7.1
9.2
6.4
9.8
4
12
2
3
7.5
11
F4
1
5.2
6.9
10.6
6.4
11.7
4
10.1
2
3
7.9
9.2
F5
1
5.6
7.4
12
7.8
11
4
5.3
2.9
2.2
9.6
9.2
F6
3.2
8.4
3.8
10.9
8.6
11.8
6.4
5
1
2
10.3
6.6
F7
1
6
9.5
11
7
11.8
4.4
4
2.3
3.3
9.7
8
F8
1.4
10.5
7
12
5.3
3.7
9.3
1.9
5.5
3.5
8.6
9.3
F9
2.5
11.7
6.9
7.2
9.5
11.1
5
2.5
2.5
2.5
6.9
9.7
F10
2.25
6.4
9.1
10.9
8.4
11.4
5
3.25
2.25
2.25
10.1
6.7
F11
2.95
5.65
7
10.9
9
11.8
3.55
2.95
2.95
2.95
10.3
8
F12
3
8.7
8.5
11.7
7.5
11.3
5
4
1
2
9.3
6
F13
1.8
7.5
9.1
11.7
4.5
11.3
5.9
4.5
1.2
3.1
9.9
7.5
Mean ranks
1.776923
7.126923
7.592308
10.47692
7.730769
10.76923
5.119231
4.730769
2.276923
2.907692
9.269231
8.223077
Neural Computing and Applications (2025) 37:7207–7260
7237
123

---

## Page 32
Table 15 Friedman test for the twelve algorithms (Dim = 100)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F1
1
6
8
10.6
7
12
5
3
2
4
10.2
9.2
F2
1
6
8
7
12
11
5
3
2
4
9.7
9.3
F3
1
5
6.6
9.4
7.5
9.6
4
12
2
3
6.9
11
F4
1
7.4
5.2
10.1
8.1
11.4
4
9.4
2
3
5.8
10.6
F5
1
5.5
8
11.2
7
11.8
4.6
4.6
3.3
2
9
10
F6
2
6
8
10.8
7
12
5
4
1
3
10.2
9
F7
1
6
8
11.4
7
11.6
4.9
3.4
2.3
3.4
9
10
F8
1.1
10.9
6
11.9
5.4
5.5
9.4
1.9
4.8
3.3
8.5
9.3
F9
2.5
11.7
6.1
7.1
9.1
10.6
5
2.5
2.5
2.5
7.8
10.6
F10
2.2
6
8.2
11.4
8.6
10.9
5
3.4
2.2
2.2
9.6
8.3
F11
2.5
6
8.1
10.6
7
12
5
2.5
2.5
2.5
10
9.3
F12
2
6.5
7.5
11.6
7
11.4
5
3.9
1
3.1
9
10
F13
1.6
6
8
11.4
7
11.6
4.8
3
1.4
4.2
9
10
Mean ranks
1.530769
6.846154
7.361538
10.34615
7.669231
10.87692
5.130769
4.353846
2.230769
3.092308
8.823077
9.738462
7238
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 33
Table 16 Friedman test for the twelve algorithms (Dim = 500)
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F1
1
6
7.1
9.6
7.9
11
5
3
2
4
9.4
12
F2
1
5.8
8
7
11.1
10
5.2
3
2
4
9
11.9
F3
1
6.3
5.8
10
8
9
4
11.7
2
3
5.9
11.3
F4
1
11
4
10.6
7.3
8.8
6
7.7
2
3
5.3
11.3
F5
1
6
7
10
8.5
11
5
3.1
2
3.9
8.5
12
F6
1
6
7.1
9.2
8.2
11
5
3
2
4
9.5
12
F7
1.1
6
7
10
8.2
11
5
3.1
2.4
3.4
8.8
12
F8
1.6
11
6.3
12
4.9
7.3
7.7
1.4
3.6
3.5
9.55
9.15
F9
2.5
9.4
7
6
9.8
10.8
5
2.5
2.5
2.5
8
12
F10
2.1
6
7
9.9
10.7
9.2
5
3.7
2.1
2.1
8.2
12
F11
2.5
5.9
7
9.7
8
11
5.1
2.5
2.5
2.5
9.3
12
F12
1
7
6
10
8.8
11
5
3
2
4
8.2
12
F13
1
6
7
10
8.8
11
4.5
3
2
4.5
8.2
12
Mean ranks
1.369231
7.107692
6.638462
9.538462
8.476923
10.16154
5.192308
3.9
2.238462
3.415385
8.296154
11.66538
Neural Computing and Applications (2025) 37:7207–7260
7239
123

---

## Page 34
4.4 Speed reducer design
This problem, as depicted in Fig. 20, is a renowned design
challenge in mechanical systems. It revolves around opti-
mizing the speed reducer, a vital component in gearbox
applications. The objective is to minimize 11 constraints
related to the weight of the speed reducer [51]. Among
these constraints, seven are nonlinear, while the remaining
are linear inequalities. The four crucial parameters inﬂu-
encing the optimization process include bending stress of
the gear teeth, surface stress, transverse deﬂections of the
shafts, and stresses in the shafts. To address this opti-
mization problem, seven variables must be considered: face
width (b), module of teeth (m), the number of teeth in the
pinion (z), length of the ﬁrst shaft between bearings (l1),
length of the second shaft between bearings (l2), diameter
of the ﬁrst shaft (d1), and diameter of the second shaft (d2).
The equation representing this problem is as follows:
Minimize f b; m; z; l1; l2; d1; d2
ð
Þ
¼ 0:7854x1x2
2 3:333x2
3 þ 14:9334x3  43:0934


 1:508x1 x2
6 þ x2
7


þ 7:4777 x3
6 þ x3
7


þ 0:7854 x4x2
6 þ x5x2
7


Subject to G1 ¼
27
x1x2
2x3
 1  0; G2 ¼ 397:5
x1x2
2x2
3
 1  0;
G3 ¼ 1:93x3
4
x2x4
6x3
 1  0; G4 ¼ 1:93x3
5
x2x4
7x3
 1  0;
G5 ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
745x4
x2x3

2
þ16:9  106
s
110x3
6
1  0; G6 ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
745x5
x2x3

2
þ157:5  106
s
85x3
7
 1  0;
G7 ¼ x2x3
40  1  0; G8 ¼ 5x2
x1
 1  0;
G9 ¼ x1
12x2
 1  0;
G10 ¼ 1:5x6 þ 1:9
x4
 1  0; G11 ¼ 1:1x7 þ 1:9
x5
 1  0
Variable
range:
2:6  x1  3:6; 0:7  x2  0:8; 17 
x3  28; 7:3  x4; x5  8:3; 2:9  x6  3:9; 5  x7  5:5;
The achieved results that are presented in Table 28
demonstrate the STA algorithm ﬁnds a minimum cost
design value in comparison with recent optimization
methods including WOA, SSA, SCA, MFO, MVO, GWO,
TSA, INFO, RUN, PSO, DE, SES [52], PSO [53], GSA [9],
hybrid Harris Hawks sine cosine algorithm (hHHO-
SCA) [54], multidisciplinary design optimization (MDO)
[55], HS [56], adaptive ﬁreﬂy algorithm (AFA) [57], socio-
behavioral simulation model (SBSM) [58], and aquila
Table 17 Friedman test for the
twelve algorithms
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F14
4.85
11
4
8.9
6.35
4
9.1
7.4
7.7
4.75
6.15
3.8
F15
2.2
7.5
8.4
8.9
6
8.7
6.9
6.5
5.4
3.9
5
8.6
F16
2.1
10.6
4.95
11.8
10.1
2.45
9
8
6.3
4.3
3.95
4.45
F17
2.75
10.2
5.6
11.8
8
3.25
9.6
8.1
5.5
4.7
4.7
3.8
F18
3.75
10.9
6.2
10.5
8.6
4.3
9.6
9.9
5.35
2.45
3.85
2.6
F19
4.45
9.8
5
11.7
7.3
2.6
8.95
11.2
6.1
4.4
3.35
3.15
F20
4.9
7.2
8.5
11.3
6.8
4.6
6.7
8.1
6.7
4.55
3.45
5.2
F21
5
10.1
5.5
11.3
7.4
5.4
8.2
9.1
4.5
4.2
2.9
4.4
F22
4.7
9.7
5.6
11.5
7.4
3.05
6.95
8.7
5.9
4.95
4.35
5.2
F23
4.6
10.9
4.5
9.4
7.9
3.75
6.9
8.3
5.65
5.75
5.5
4.85
Mean ranks
3.93
9.79
5.825
10.71
7.585
4.21
8.19
8.53
5.91
4.395
4.32
4.605
7240
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 35
optimizer (AO) [59]. Figure 21 showcases the convergence
plots and box plots for all methods when tackling this
problem. Notably, the proposed STA algorithm takes the
lead in solving the speed reducer design challenge. In
Table 29, you can ﬁnd the statistical outcomes for the STA
and the other chosen algorithms. A glance at Table 29
reveals that the STA outperformed all the selected meth-
ods. Consequently, it is evident that the proposed STA
technique exhibits greater reliability for this engineering
design problem.
4.5 Gear train design
As mentioned in Reference [60], the main goal of opti-
mizing the gear train design is to approach a gear trans-
mission ratio as closely as possible to 1/6.931. Let TA, TB,
TD, and TF denote the number of teeth on gears A, B, D,
and F, respectively. As each gear’s number of teeth must be
an integer within the range of 12–60, this optimization
problem is converted into a constrained optimization
problem with discrete variables. The formulation of the
optimization problem is presented as follows:
Fig. 9 Radar chart for the compared algorithms performance for 23 benchmark functions
Neural Computing and Applications (2025) 37:7207–7260
7241
123

---

## Page 36
Minimize
f ¼
1
6:931  TDTB
TATF

2
Variable range:
12  TA  60; 12  TB  60; 12  TD  60; 12  TF  60;
ð1000Þ
Table 30 presents the optimal solutions found by STA and
other techniques. This table reveals that the results obtained
through the proposed STA technique are superior, with an
optimal value of 0, while SCA yields the minimum results. The
outcomes underscore the efﬁciency of the STA algorithm in
solving the problem, with the design featuring the minimum
ﬁtness represented by x~ = [27.11492, 12.03429, 15.79045,
48.57386]. These experimental ﬁndings demonstrate that the
proposed
STA
technique
exhibits
robust
exploitation
capabilities.
Figure 22illustratestheconvergencecurvesandboxplotsof
the gear train design problem using the STA algorithm and
other algorithms. The proposed STA algorithm is thoroughly
assessed and compared with various optimization techniques,
including WOA, SSA, SCA, MFO, MVO, GWO, INFO, RUN,
PSO, DE, and TSA, all within the context of the gear train
design problem. Table 31 provides the statistical outcomes for
these algorithms, evaluating their performance based on met-
rics such as ‘‘best,’’ ‘‘mean,’’ ‘‘worst,’’ and ‘‘Std.’’ The STA
algorithm delivers outstanding results, achieving a ﬁtness value
of 0, which signiﬁes its capability to discover an optimal
solution for the gear train design problem. Furthermore, it
maintains an average ﬁtness value of 0, indicating that, on
average, it performs exceptionally well, closely approaching
the optimal value. With a remarkably low standard deviation of
0, the STA algorithm demonstrates consistent performance and
stability, consistently ﬁnding solutions that are close to the
optimum. In summary, based on the statistical ﬁndings, the
proposed STA algorithm exhibits exceptional performance
when addressing the gear train design problem, surpassing the
other evaluated algorithms. Its ability to consistently discover
near-optimal solutions and its minimal variability make it a
promising
choice
for
similar
constrained
optimization
problems.
Fig. 10 Mean ranks achieved using Friedman test for 23 benchmark functions using several techniques
Table 18 Modern ten test
functions from CEC2019
No
Functions
Dimension
Range
fmin
CEC01
Storn’s Chebyshev polynomial ﬁtting
9
[ - 8192, 8192]
1
CEC02
Inverse Hilbert matrix
16
[ - 16,384, 16384]
1
CEC03
Lennard–Jones minimum energy cluster
18
[ - 4, 4]
1
CEC04
Rastrigin’s
10
[ - 100,100]
1
CEC05
Griewangk’s
10
[ - 100,100]
1
CEC06
Weierstrass
10
[ - 100,100]
1
CEC07
Modiﬁed Schwefel’s
10
[ - 100,100]
1
CEC08
Expanded Schaffer’s F6
10
[ - 100,100]
1
CEC09
Happy cat
10
[ - 100,100]
1
CEC10
Ackley
10
[ - 100,100]
1
7242
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 37
Table 19 Numerical results for CEC 2019 benchmark functions by the STA technique and other well-known algorithms
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
CEC01
Best
43,622.41
41,425.08
66,415,704
1,134,504
8.45E ? 08
1.38E ? 08
50,387.31
5,290,653
37,688.56
33,479.17
3.93E ? 08
1.3E ? 10
Mean
46,736.45
1.15E ? 08
8.8E ? 08
1.47E ? 09
2.82E ? 09
1.58E ? 09
26,315,942
6.1E ? 09
224,371.9
218,888.7
1.08E ? 09
1.92E ? 10
Worst
50,525.77
9.16E ? 08
2.42E ? 09
4.49E ? 09
5.4E ? 09
3.85E ? 09
1.09E ? 08
1.96E ? 10
858,516.1
816,513.2
2.32E ? 09
3.18E ? 10
Std
2214.798
3.24E ? 08
8E ? 08
1.69E ? 09
1.49E ? 09
1.47E ? 09
36,164,915
8.15E ? 09
342,205.2
331,402.3
6.86E ? 08
6.99E ? 09
CEC02
Best
18.34286
18.35309
18.34303
18.38074
18.75652
18.34286
18.34317
18.34287
18.34286
18.34286
18.34286
18.34286
Mean
18.34286
19.04584
18.34316
18.41653
18.93496
18.34286
18.34329
18.34299
18.34286
18.40996
18.40996
18.40996
Worst
18.34286
19.71664
18.3433
18.46598
19.24245
18.34286
18.34343
18.34318
18.34287
18.75652
18.75652
18.75652
Std
1.92E-09
0.518036
8.84E-05
0.027092
0.177624
0
8.59E-05
0.000103
3.64E-06
0.146511
0.146511
0.146511
CEC03
Best
13.7024
13.7024
13.7024
13.70241
13.7024
13.7024
13.7024
13.7024
13.7024
13.7024
13.7024
13.7024
Mean
13.7024
13.70242
13.7024
13.70244
13.7024
13.7024
13.7024
13.7024
13.7024
13.7024
13.7024
13.70241
Worst
13.7024
13.7025
13.7024
13.70252
13.7024
13.70241
13.7024
13.7024
13.7024
13.7024
13.7024
13.70241
Std
3.8E-15
3.55E-05
1.9E-15
3.73E-05
6.06E-10
5.95E-07
1.03E-08
1.34E-09
6.17E-12
1.9E-15
1.9E-15
2.95E-06
CEC04
Best
57.73173
81.5409
13.93446
352.7773
16.57394
14.92942
25.5996
76.83637
50.7479
13.93446
23.88402
17.34498
Mean
107.6644
1521.603
19.9042
714.3438
22.9174
49.25513
65.90642
149.1863
79.86647
56.21981
65.47301
49.72934
Worst
166.1862
3499.279
26.86889
929.846
29.25836
125.3686
125.3686
322.1732
106.4645
125.3686
125.3686
125.3686
Std
35.87244
1546.456
4.353187
194.8007
4.314048
47.47531
40.38744
78.22833
16.80202
44.87829
49.70768
46.96969
CEC05
Best
2.100903
2.48348
2.07386
2.921345
2.121544
2.105804
2.103819
2.126415
2.110833
2.066378
2.068869
2.073649
Mean
2.275706
3.125763
2.274428
3.0394
2.283273
2.225399
2.172697
2.577741
2.245223
2.489082
2.217829
2.476063
Worst
2.612948
4.082989
2.561093
3.161164
2.68216
2.469529
2.229679
3.012205
2.457652
3.060081
2.374036
3.060081
Std
0.181432
0.497765
0.14507
0.068568
0.176481
0.122782
0.044175
0.321724
0.131509
0.461367
0.134922
0.470172
CEC06
Best
3.700687
9.021334
2.021989
9.745317
5.726581
4.056413
9.166096
6.936844
5.401056
6.25418
7.325756
7.858454
Mean
6.966442
10.3951
5.910235
10.83007
7.331443
5.913596
10.74232
8.743194
8.118925
9.086115
9.339122
8.783592
Worst
8.955334
11.2337
11.23916
11.37011
9.517057
9.819279
11.83582
10.38597
12.19503
11.0334
11.00086
9.35998
Std
1.676464
0.891807
4.327551
0.572787
1.19549
1.788181
0.827094
1.046412
2.260056
1.512504
1.371517
0.551644
CEC07
Best
209.3351
283.5501
149.9107
150.2866
91.69736
31.04649
45.73065
99.32761
27.3364
111.9067
99.89545
26.73722
Mean
328.8059
401.7173
288.5733
533.8364
248.4322
271.6748
394.7951
233.2405
202.053
246.2391
253.739
157.9107
Worst
555.1042
693.1061
559.7542
720.5753
452.2623
384.1799
671.6189
420.1858
336.9728
487.9605
313.8561
336.9728
Std
125.4988
148.9945
140.8175
169.6072
138.9276
129.2101
241.2132
107.4047
101.6348
124.2886
74.10955
91.22916
CEC08
Best
3.121673
5.362277
3.361663
4.479511
3.049914
4.171314
2.959204
4.747345
3.076661
3.764119
2.671945
4.287645
Mean
4.533882
5.938339
4.882455
5.273074
4.325981
5.496916
4.012204
5.618261
4.207812
5.119399
4.391559
5.252786
Worst
5.76691
6.535425
5.82449
5.818729
5.456317
6.255529
5.608334
6.237018
5.140331
6.212304
6.222693
6.057648
Std
0.871468
0.444951
0.767731
0.520554
0.880478
0.683365
0.86905
0.512808
0.727455
0.800999
1.162107
0.555703
CEC09
Best
3.622603
5.03499
3.34267
15.05558
3.343156
3.35637
3.456414
4.40995
3.812663
3.35279
3.497789
3.403389
Mean
4.300534
128.9178
4.403402
61.10513
3.354034
3.39608
4.541109
4.978612
4.703334
4.168103
4.263155
4.197348
Worst
5.63545
363.4384
6.37797
226.6713
3.377815
3.476955
5.923895
6.308317
6.37797
6.37797
6.37797
6.37797
Std
0.762632
171.1759
1.324221
68.20797
0.011825
0.035825
0.76071
0.67589
1.125221
1.369464
1.306224
1.346643
CEC10
Best
3.013515
21.27973
2.225259
21.27363
21.00983
20.99977
2.210882
21.0038
21.10492
20.99353
21.03478
21.0891
Mean
18.74145
21.39531
18.78171
21.34458
21.01606
21.10525
18.90376
21.11745
21.36222
21.005
21.28683
21.16377
Worst
21.00646
21.47131
21.3859
21.44923
21.02573
21.26351
21.39299
21.36276
21.49687
21.02088
21.44819
21.2391
Std
6.355106
0.062043
6.692133
0.055831
0.00528
0.098934
6.745653
0.148718
0.112623
0.009107
0.153693
0.062043
Neural Computing and Applications (2025) 37:7207–7260
7243
123

---

## Page 38
Fig. 11 Convergence curves of
all algorithms for CEC 2019
benchmark functions
7244
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 39
Table 20 Statistical results of the Wilcoxon rank-sum test for CEC 2019 benchmark functions
STA vs
Fun
TSA
SSA
SCA
MVO
MFO
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
CEC01
6.50E-02
=
1.55E-04
?
1.55E-04
?
1.55E-04
?
1.55E-04
?
CEC02
1.55E-04
?
1.55E-04
?
1.55E-04
?
1.55E-04
–
1.55E-04
–
CEC03
1.55E-04
?
1.00E ? 00
=
1.55E-04
?
1.55E-04
?
4.67E-01
=
CEC04
2.34E-01
=
1.55E-04
-
1.55E-04
?
1.55E-04
–
2.78E-02
-
CEC05
3.11E-04
?
9.59E-01
=
1.55E-04
?
7.21E-01
=
7.98E-01
=
CEC06
1.55E-04
?
5.74E-01
=
1.55E-04
?
1.00E ? 00
=
1.95E-01
=
CEC07
1.85E-01
=
4.87E-01
=
2.07E-02
?
2.23E-01
=
1.00E ? 00
=
CEC08
2.95E-03
?
3.28E-01
=
1.30E-01
=
9.59E-01
=
2.81E-02
?
CEC09
6.22E-04
?
5.56E-01
=
1.55E-04
?
1.55E-04
-
1.55E-04
-
CEC10
1.55E-04
?
3.82E-01
=
1.55E-04
?
1.55E-04
?
1.09E-03
?
WRST (? / = / - )
7/3/0
2/7/1
9/1/0
3/4/3
3/4/3
STA vs
Fun
GWO
WOA
RUN
INFO
PSO
DE
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
CEC01
3.11E-
04
?
1.55E-
04
?
3.97E-
01
=
8.60E-01
=
1.55E-04
?
1.55E-
04
?
CEC02
1.55E-
04
?
1.55E-
04
?
1.55E-
04
?
9.09E-02
=
9.93E-02
=
9.68E-
02
=
CEC03
1.55E-
04
?
1.55E-
04
?
3.11E-
04
?
1.00E ? 00
=
1.00E ? 00
=
1.55E-
04
?
CEC04
8.22E-
02
=
2.79E-
01
=
1.05E-
01
=
2.78E-02
-
1.08E-01
=
2.78E-
02
-
CEC05
4.42E-
01
=
4.99E-
02
?
9.59E-
01
=
6.45E-01
=
4.25E-01
=
8.78E-
01
=
CEC06
1.55E-
04
?
2.07E-
02
?
5.74E-
01
=
2.07E-02
?
1.04E-02
?
6.99E-
03
?
CEC07
7.77E-
01
=
1.85E-
01
=
7.86E-
02
=
2.23E-01
=
4.25E-01
=
2.95E-
03
-
CEC08
3.28E-
01
=
1.04E-
02
?
5.05E-
01
=
3.28E-01
=
7.98E-01
=
1.05E-
01
=
CEC09
5.74E-
01
=
1.30E-
01
=
2.67E-
01
=
1.87E-01
=
1.25E-01
=
1.01E-
01
=
CEC10
1.04E-
02
?
1.09E-
03
?
1.55E-
04
?
1.05E-01
=
1.55E-04
?
1.55E-
04
?
WRST (? /
= / - )
5/5/0
7/3/0
3/7/0
1/8/1
3/7/0
4/4/2
Neural Computing and Applications (2025) 37:7207–7260
7245
123

---

## Page 40
4.5.1 Wilcoxon’s rank test results
The proposed STA has been evaluated against several other
optimization algorithms, namely TSA, SSA, SCA, MVO,
MFO, GWO, RUN, INFO, PSO, DE, and WOA, on a set of
real-world constrained engineering design problems. The
results of this evaluation are summarized in Table 32,
which displays the p-values and the corresponding winners
for each comparison between STA and the other algorithms
for various optimization problems including BTD, CBD,
WBD, SRD, and GTD. In summary, the proposed STA
algorithm demonstrates competitive performance com-
pared to other optimization algorithms across various
engineering design problems. It outperforms or is statisti-
cally
equivalent
to
several
algorithms
for
different
problems.
Table 21 Friedman test using the twelve algorithms for CEC 2019 benchmark functions
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
F14
2.4375
3.375
7.875
7.875
9.75
8.25
4.9375
8.875
2.0625
2.5625
8.25
11.75
F15
4.25
11
7.375
9.375
11.5
1.9375
8
6.375
5.25
4.0625
4.3125
4.5625
F16
3.125
10.5
2.8125
11.75
7.625
4.5625
8.375
7.25
5.75
2.8125
2.8125
10.625
F17
8.25
9.75
2.125
11.5
2.5
4.75
6.625
9.25
7.25
5.1875
6.25
4.5625
F18
5
10.625
5.75
11.125
5.75
5.25
3.625
8.125
5.125
6.625
4.875
6.125
F19
3.5
9.875
4.75
10.25
3.875
2.625
10.25
6
5.25
7.25
7.875
6.5
F20
7
9.375
6.375
10.5
5.375
6.625
8
5.125
4.8125
5.25
6
3.5625
F21
4.875
10.5
5.875
7.75
4.5
9
3.125
9.375
3.75
7
4.75
7.5
F22
7.125
10.875
4.75
11.625
1.375
2.875
7.25
8.125
7.125
5.125
6
5.75
F23
1.875
10.625
4.75
9.5
3.875
5.375
7.875
5.875
10
2.625
8.75
6.875
Mean ranks
4.74375
9.65
5.24375
10.125
5.6125
5.125
6.80625
7.4375
5.6375
4.85
5.9875
6.78125
Fig. 12 Radar chart for the compared algorithms performance for CEC 2019 benchmark functions
7246
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 41
4.5.2 Friedman’s rank test results
Table 33 presents the results of the Friedman test, which
assessed the performance of eight different optimization
algorithms across a set of real-world constrained engi-
neering design problems. For the BTD problem, STA
achieved a mean rank of 2.6, indicating its superior
performance compared to the other algorithms, with WOA
having the highest mean rank of 11.6. In the case of the
CBD problem, STA obtained a mean rank of 3.6, making it
one of the top-performing algorithms after that INFO, RUN
and SSA, while SCA had the highest mean rank of 11.6.
Regarding the WBD problem, STA achieved a mean rank
of 2.4, placing it among the top-performing algorithms.
MFO had the lowest mean rank of 1.35, indicating its
strong performance. For the SRD problem, STA’s mean
rank was 2.8, signifying competitive performance, while
SCA had the highest mean rank of 11.9. In the GTD
problem, STA obtained a mean rank of 3.15, demonstrating
strong performance, while SCA had the highest mean rank
of 11.4. Overall, the mean ranks for each algorithm across
different problems were calculated. STA had a mean rank
of 2.91, making it one of the top-performing algorithms in
this evaluation, while SCA had the highest mean rank of
11.26. These results suggest that STA consistently per-
formed well across multiple engineering design problems
during compared to the other techniques.
Fig. 13 Mean ranks achieved using Friedman test for CEC 2019 benchmark functions using several techniques
Fig. 14 Schematic of three-bar truss problem
Neural Computing and Applications (2025) 37:7207–7260
7247
123

---

## Page 42
Table 22 Results for the three-
bar truss problem
Algorithms
Optimum values for variables
Optimal cost
x1
x2
STA
0.78867514354
0.40824825645
263.8958429412
TSA
0.788303894793
0.409302223077
263.8962341653
SSA
0.7886705766
0.4082611737
263.8958429566
SCA
0.790289750
0.403708161
263.898512530
MVO
0.78869593269
0.40818939236
263.8958687956
MFO
0.78886299861
0.40771718127
263.8958688599
GWO
0.7884720971
0.4088228569
263.8958733906
WOA
0.78715946310
0.41255221852
263.89753998011
RUN
0.788611292
0.408428885
263.8958459
INFO
0.78867513
0.408248295
263.8958429
PSO
0.788670295
0.408261971
263.895843
DE
0.788685459
0.408219107
263.8958451
Ray and sain [33]
0.795
0.395
264.3
AAA [34]
0.788735
0.408078
263.8959
MBA [35]
0.788565
0.40856
263.8959
DEDS [36]
0.788675
0.408248
263.8958
GOA [37]
0.788898
0.40762
263.8959
PSO-DE [38]
0.788675
0.408248
263.8958
CS [39]
0.78867
0.40902
263.9716
Fig. 15 Convergence curves and boxplots of the studied techniques for three-bar truss problem
7248
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 43
Conversely, in Fig. 23, a radar chart provides a visual
representation of the ranks achieved by all the compared
algorithms. This chart offers a succinct and intuitive way to
observe how each algorithm fares in comparison to others
when dealing with real-world constrained engineering
design problems. The radar chart’s multi-dimensional
approach allows for a rapid assessment of each algorithm’s
strengths and weaknesses in addressing the diverse array of
problems encountered in real-world constrained engineer-
ing design. Furthermore, Fig. 24 displays the Mean ranks
acquired through the Friedman test for real-world con-
strained engineering design problems. These ﬁgures unam-
biguously illustrate that the STA technique secures the
most favorable average rank, indicating its top position
among all the techniques.
5 Conclusion
His article presents the development of a novel meta-
heuristic technique called the supercell thunderstorm
algorithm (STA). The STA algorithm is inspired by the
behavior of supercell thunderstorms in nature, which are
severe thunderstorms known for their rotating updrafts,
strong wind shear, and potential for tornado formation. The
algorithm is designed with three main components: spiral
motion, formation, and jet stream, to optimize procedures.
To evaluate the effectiveness of the STA algorithm, it is
rigorously tested on a set of 23 benchmark functions with
varying dimensions. The evaluation focuses on the algo-
rithm’s ability to explore and exploit solution spaces
effectively, thus avoiding local optima. The initial results
Table 23 Statistical results for the three-bar truss problem
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
Best
263.8958
263.8962
263.8958
263.8985
263.8959
263.8959
263.8959
263.8975
263.8958
263.8958
263.8958
263.8958
Mean
263.8958
263.8975
263.8959
263.9195
263.8962
263.8977
263.8961
263.9675
263.8959
263.9048
263.8959
263.8963
Worst
263.8959
263.8986
263.8959
263.9653
263.8966
263.9021
263.8962
264.1226
263.8965
263.9569
263.896
263.8966
Std
1.51E-05
0.000693
2.59E-05
0.023031
0.000253
0.002142
0.000121
0.079033
0.00021
0.020397
4.3E-05
0.000231
Fig. 16 Schematic of cantilever beam design problem
Neural Computing and Applications (2025) 37:7207–7260
7249
123

---

## Page 44
Table 24 Attained results of the
cantilever beam design problem
Algorithms
Optimal values for variables
Optimum cost
x1
x2
x3
x4
x5
STA
6.014644
5.310063
4.494105
3.501842
2.153006
1.339956431
TSA
5.95913658
5.31046273
4.47525089
3.53800374
2.19482723
1.34020730
SSA
6.0170359
5.3087936
4.4943621
3.5010606
2.1524080
1.3399564
SCA
6.15679718
5.27683125
4.36523884
3.69294174
2.16157645
1.35117125
MVO
6.0194905
5.3204335
4.4967766
3.4949515
2.1423633
1.3399786
MFO
6.01966309
5.32538293
4.48700697
3.49353430
2.14825345
1.33996766
GWO
6.0203108
5.3015291
4.4956415
3.5024256
2.1537854
1.3399584
WOA
5.96412747
5.35766213
4.91330380
3.31761582
2.02746203
1.34660269
RUN
6.0162641
5.30899182
4.493281909
3.50266012
2.1524633
1.339956458
INFO
6.016183999
5.30897862
4.4943691
3.5013780
2.15274992
1.33995636
PSO
6.01396675
5.31876938
4.4823418
3.51008259
2.1486565
1.3399662
DE
6.000452
5.328834
4.521241
3.489147
2.135171
1.34003
GCA_I [41]
6.01
5.304
4.49
3.498
2.15
1.34
ALO [14]
6.01812
5.31142
4.48836
3.49751
2.158329
1.33995
GCA_II [41]
6.01
5.3
4.49
3.49
2.15
1.34
MMA [41]
6.01
5.3
4.49
3.49
2.15
1.34
SOS [42]
6.01878
5.30344
4.49587
3.49896
2.15564
1.33996
ISMA [43]
6.017757
5.310892
4.493758
3.501106
2.150159
1.33996
Fig. 17 Convergence curves and boxplots for cantilever beam design problem using the studied methods
7250
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 45
clearly demonstrate that the STA algorithm outperforms
well-known algorithms such as the tunicate swarm algo-
rithm (TSA), salp swarm algorithm (SSA), sine cosine
algorithm (SCA), multi-verse optimizer (MVO), moth
ﬂame optimization (MFO), grey wolf optimizer (GWO),
whale optimization algorithm (WOA), Runge–Kutta opti-
mizer (RUN), weighted mean of vectors (INFO), particle
swarm optimization (PSO), and differential evolution (DE).
Across all 31 benchmark functions, the STA algorithm
consistently exhibits superior performance in terms of
exploration, exploitation, avoidance of local optima, and
convergence characteristics. Statistical tests are conducted
to conﬁrm the STA algorithm’s superiority over other
metaheuristics. Furthermore, the study validates the effec-
tiveness of the STA algorithm in solving complex com-
position functions by employing the CEC2019 functions.
The results demonstrate that STA efﬁciently discovers
optimal solutions for a majority of benchmark functions
while keeping a balanced approach between exploration
and exploitation. As well as the benchmark functions, the
STA algorithm is applied to ﬁve real-world constrained
engineering design issues, including three-bar truss design
(BTD), cantilever beam design (CBD), welded beam
design (WBD), speed reducer design (SRD), and gear train
design (GTD). These practical applications highlight the
high-performance capabilities of the STA algorithm in
navigating unexplored search spaces.
The remarkable performance demonstrated by the STA
algorithm, as discussed earlier, opens up a broad range of
promising research directions for future exploration. These
avenues encompass the application of STA to various
problem domains, including PV parameter extraction,
smart home challenges, industrial and engineering issues,
neural networks, image processing tasks, text and data
mining problems, big data challenges, signal denoising,
resource management applications, network optimization,
Table 25 Numerical results for the cantilever beam design problem
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
Best
1.339956
1.340207
1.339956
1.351171
1.339979
1.339968
1.339958
1.346603
1.339956
1.339956
1.339966
1.34003
Mean
1.33996
1.340416
1.339957
1.362864
1.340054
1.339991
1.339967
1.36271
1.339957
1.339957
1.340009
1.340085
Worst
1.339967
1.340593
1.339957
1.36894
1.340186
1.340032
1.339973
1.386139
1.339957
1.339957
1.34014
1.340186
Std
3.8E-06
0.000136
3.78E-07
0.005474
5.73E-05
2.46E-05
4.84E-06
0.013973
2.96E-07
2.93E-07
5.04E-05
5.69E-05
Fig. 18 Schematic of welded beam design problem
Neural Computing and Applications (2025) 37:7207–7260
7251
123

---

## Page 46
other test functions, feature selection, image segmentation,
task scheduling, and many more.
Additionally, there is ample opportunity to extend the
applicability of STA to real-world scenarios involving
discrete, binary, and multi-objective optimization issues.
Table 26 Results of the welded
beam design problem
Methods
Optimum values for variables
Optimal cost
h
l
t
b
STA
0.20572964
3.47048867
9.03662391
0.20572964
1.72485231
TSA
0.20576363
3.48760424
9.03504322
0.20626527
1.73103528
SSA
0.20251079
3.54113817
9.03662389
0.20572965
1.72933413
SCA
0.204143709
3.562728278
9.317920839
0.205398635
1.781148515
MVO
0.20546654
3.48127685
9.03693041
0.20573182
1.72597517
MFO
0.20572964
3.47048867
9.03662391
0.20572964
1.72485231
GWO
0.205692461
3.472186880
9.038687658
0.205722209
1.725325363
WOA
0.201062681
3.523553491
9.164860059
0.206328680
1.751559804
RUN
0.204799353
3.49062759
9.036623764
0.20572965
1.726122525
INFO
0.20572964
3.470488666
9.03662391
0.20572964
1.72485231
PSO
0.20572964
3.470488662
9.036623905
0.20572964
1.72485231
DE
0.20567864
3.47413978
9.03698296
0.20573164
1.72534632
GOA [37]
0.182129
3.856979
10
0.202376
1.87995
RO [45]
0.203687
3.528467
9.004233
0.207241
1.735344
ECDE [46]
0.203137
3.542998
9.033498
0.206179
1.733461
GA [47]
0.2489
6.173
8.1789
0.2533
2.43
HS [48]
0.2442
6.2231
8.2915
0.24
2.3807
CPSO [49]
0.202369
3.544214
9.04821
0.205723
1.72802
MPA [21]
0.205728
3.470509
9.036624
0.20573
1.724853
Fig. 19 Convergence curves and boxplots using all algorithms for welded beam design issue
7252
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 47
To further enhance the performance of the STA algorithm,
it is worth investigating approaches such as incorporating
disruptive elements, mutation mechanisms, Levy ﬂight
dynamics,
and
other
stochastic
components.
These
explorations can be conducted within the context of both
local and global search strategies, while also considering
the integration of additional evolutionary operators.
Furthermore, it may be worthwhile to explore the
development of a discrete version of the STA algorithm to
address discrete optimization challenges effectively. These
avenues of future research hold great promise for unlock-
ing additional potential in the application and advancement
of the STA algorithm.
Table 27 Numerical results for the welded beam design problem
Algorithm
Best
Mean
Worst
Std
STA
1.724852
1.724853
1.724864
3.58E-06
TSA
1.731035
1.735537
1.738094
0.002721
SSA
1.729334
1.880685
2.175366
0.152304
SCA
1.781149
1.807943
1.839232
0.018036
MVO
1.725975
1.731615
1.741135
0.005823
MFO
1.724852
1.724856
1.724892
1.26E-05
GWO
1.725325
1.725536
1.726064
0.000237
WOA
1.75156
1.804441
1.885408
0.048632
RUN
1.726123
1.759784
1.843008
0.033599
INFO
1.724852
1.757138
1.843008
0.03708
PSO
1.724852
1.732419
1.790889
0.020672
DE
1.725346
1.725588
1.726064
0.000235
Rao-1 [50]
1.724852
1.724852
1.724852
2.62
Rao-2 [50]
1.724852
1.724852
1.724852
9.83E-04
Rao-3 [50]
1.724852
1.724852
1.724852
2.06E-03
FISA [50]
1.724852
1.724852
1.724852
5.93E-05
MPA [21]
1.724853
1.724861
1.724873
6.41E-06
Fig. 20 Schematic of speed reducer design problem
Neural Computing and Applications (2025) 37:7207–7260
7253
123

---

## Page 48
Table 28 Comparison results for speed reducer design problem
Algorithms
Optimum values for variables
Optimal cost
b
m
p
l1
l2
d1
d2
STA
3.5
0.7
17
7.3
7.71532
3.350215
5.286654
2994.471
TSA
3.51003
0.7
17
7.567897
7.72085
3.355346
5.28914
3003.789
SSA
3.50101
0.7
17
7.582481
7.920558
3.350826
5.286725
3002.064
SCA
3.53224
0.706
17
8.3
7.996289
3.407131
5.302415
3074.796
MVO
3.50672
0.7
17
7.3
8.005923
3.350915
5.28701
3003.895
MFO
3.5
0.7
17
7.3
7.71532
3.350215
5.286654
2994.471
GWO
3.50034
0.7
17
7.350353
7.757172
3.353536
5.287135
2997.119
WOA
3.50094
0.7
17
7.589163
7.906494
3.350765
5.287461
3002.241
RUN
3.5
0.7
17
7.3
7.719811
3.35023
5.286656
2994.575
INFO
3.5
0.7
17
7.3
7.71532
3.350215
5.286654
2994.471
PSO
3.5
0.7
17
7.3
7.71532
3.350215
5.286654
2994.472
DE
3.504446
0.7
17
7.511366
7.858522
3.356191
5.286703
3002.787
SES [52]
3.50616
0.7008
17
7.460181
7.962143
3.3629
5.308949
3025.005
PSO [53]
3.5001
0.7
17.0002
7.5177
7.7832
3.3508
5.2867
3145.922
GSA [9]
3.6
0.7
17
8.3
7.8
3.369658
5.289224
3051.12
hHHO-SCA [54]
3.50612
0.7
17
7.3
7.99141
3.452569
5.286749
3029.873
MDO [55]
3.5
0.7
17
7.3
7.670396
3.542421
5.245814
3019.583
HS [56]
3.52012
0.7
17
8.37
7.8
3.36697
5.288719
3029.002
AFA [57]
3.50749
0.7001
17
7.719674
8.080854
3.351512
5.287051
3010.137
SBSM [58]
3.50612
0.7
17
7.549126
7.85933
3.365576
5.289773
3008.08
AO [59]
3.5021
0.7
17
7.3099
7.7476
3.3641
5.2994
3007.733
Fig. 21 Convergence curves and boxplots using all algorithms for speed reducer design problem
7254
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 49
Table 29 Numerical results for speed reducer design problem
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
Best
2994.471
3003.789
3002.064
3041.012
3003.895
2994.471
2997.119
3002.241
2994.575
2994.471
2994.472
3002.787
Mean
2994.53
3019.463
3023.785
3070.708
3023.272
2994.471
2999.108
3050.551
2996.981
2994.814
2994.927
3030.501
Worst
2995.058
3026.007
3053.4
3101.098
3043.344
2994.471
3002.097
3231.458
3000.866
2995.76
2996.736
3044.471
Std
0.185479
6.461037
18.06583
16.18592
13.48128
3.71E-13
2.028856
66.90673
2.343144
0.565308
0.868838
12.93881
Neural Computing and Applications (2025) 37:7207–7260
7255
123

---

## Page 50
Table 30 Results of the gear
train design problem
Algorithms
Optimal values for variables
Optimum cost
TA
TB
TD
TF
STA
27.11492
12.03429
15.79045
48.57386
0
TSA
60
16.10947
23.06112
42.91472
5.58E-17
SSA
51.03928
13.02365
14.41983
25.5026
1.84E-26
SCA
59.624
19.62691
23.4388
53.47629
6.86E-14
MVO
30.21696
20.32619
12
55.94772
1.69E-17
MFO
44.87759
12
13.24268
24.54276
0
GWO
53.72381
15.38978
21.10562
41.9044
1.33E-17
WOA
57.8992
28.6439
16.67487
57.17653
0
RUN
53.48283
12.0551
12.01219
18.7661
0
INFO
42.61166
15.89775
15.01064
38.81523
0
PSO
54.90092
18.17824
21.30102
48.88421
0
DE
55.48742
39.1983
13.22674
64.7623
5.75E-14
Fig. 22 Convergence curves and boxplots of all algorithms for gear train design problem
Table 31 Statistical results for gear train design problem
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
Best
0
5.58E-17
1.84E-26
6.86E-14
1.69E-17
0
1.33E-17
0
0
0
0
5.75E-14
Mean
0
9E-15
7.48E-22
4.64E-12
6.98E-15
0
1.28E-14
0
8.79E-18
0
0
2.17E-12
Worst
0
6.59E-14
4.62E-21
2.23E-11
3.13E-14
0
7.82E-14
0
3.45E-17
0
0
8.88E-12
Std
0
2.03E-14
1.41E-21
8.16E-12
1.01E-14
0
2.44E-14
0
1.31E-17
0
0
3.3E-12
7256
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 51
Table 32 Statistical results of the Wilcoxon rank-sum test for real-world constrained engineering design problems
STA vs
Fun
TSA
SSA
SCA
MVO
MFO
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
BTD
1.83E-04
?
2.73E-01
=
1.83E-04
?
2.46E-04
?
2.46E-04
?
CBD
1.83E-04
?
3.12E-02
-
1.83E-04
?
1.83E-04
?
1.83E-04
?
WBD
1.83E-04
?
1.83E-04
?
1.83E-04
?
1.83E-04
-
2.04E-03
-
SRD
1.82E-04
?
1.82E-04
?
1.82E-04
?
1.82E-04
-
1.40E-04
-
GTD
6.39E-05
?
6.39E-05
?
6.39E-05
?
6.39E-05
?
=
WRST (? / = / - )
5/0/0
3/1/1
5/0/0
3/0/2
2/1/2
STA vs
Fun
GWO
WOA
RUN
INFO
PSO
DE
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
P
Winner
BTD
2.46E-
04
?
1.83E-
04
?
1.40E-
02
?
2.44E-
02
–
2.12E-
01
=
7.55E-
04
?
CBD
5.80E-
03
?
1.83E-
04
?
3.12E-
02
-
9.11E-
03
–
2.46E-
04
?
1.79E-
04
?
WBD
1.83E-
04
?
1.83E-
04
?
1.83E-
04
?
4.71E-
01
?
1.01E-
03
?
1.81E-
04
?
SRD
1.82E-
04
?
1.82E-
04
?
4.37E-
04
?
1.37E-
01
?
1.70E-
03
?
1.78E-
04
?
GTD
6.39E-
05
?
=
2.21E-
03
?
=
=
6.39E-
05
?
WRST (? /
= / - )
5/0/0
4/1/0
4/0/1
2/1/2
3/2/0
5/0/0
Table 33 Friedman test using
the twelve algorithms for real-
world constrained engineering
design problems
Function
STA
TSA
SSA
SCA
MVO
MFO
GWO
WOA
RUN
INFO
PSO
DE
BTD
2.6
9.2
3.3
10.9
6.9
8.3
6.5
11.6
4.6
3.1
3.9
7.1
CBD
3.6
10
2.5
11.6
8.1
6.6
5
11.4
2.4
1.8
6.5
8.5
WBD
2.4
7.2
10.6
10.5
6.8
1.35
4.6
10.4
9
6.05
4.4
4.7
SRD
2.8
8.5
8.6
11.9
8.8
1.35
6
9.6
4.9
2.25
3.8
9.5
GTD
3.15
8.9
6.3
11.4
9.1
3.15
9.1
3.15
5.95
3.15
3.15
11.5
Mean ranks
2.91
8.76
6.26
11.26
7.94
4.15
6.24
9.23
5.37
3.27
4.35
8.26
Neural Computing and Applications (2025) 37:7207–7260
7257
123

---

## Page 52
Fig. 23 Radar chart for the compared algorithms performance for real-world constrained engineering design problems
Fig. 24 Mean ranks achieved using Friedman test for real-world constrained engineering design problems
7258
Neural Computing and Applications (2025) 37:7207–7260
123

---

## Page 53
Author contributions Mohamed H. Hassan involved in conceptual-
ization, methodology, software, writing— original draft preparation.
Salah Kamel took part in conceptualization, methodology, software
writing—original draft preparation.
Funding Open access funding provided by The Science, Technology
& Innovation Funding Authority (STDF) in cooperation with The
Egyptian Knowledge Bank (EKB).
Data and materials availability Data sharing is not applicable to this
article as no datasets were generated or analyzed during the current
study.
Declarations
Conflict of interest The authors declare that there is no conflict of
interest regarding the publication of this manuscript.
Ethical approval This article does not contain any studies with human
participants or animals performed by any of the authors.
Informed consent Not applicable.
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
1. Xie L, Han T, Zhou H et al (2021) Tuna swarm optimization: a
novel swarm-based metaheuristic algorithm for global optimiza-
tion. Comput Intell Neurosci 2021:1–22. https://doi.org/10.1155/
2021/9210050
2. Alsattar HA, Zaidan AA, Zaidan BB (2020) Novel meta-heuristic
bald eagle search optimisation algorithm. Artif Intell Rev
53:2237–2264. https://doi.org/10.1007/s10462-019-09732-5
3. Storn R, Price K (1997) Differential evolution – a simple and
efﬁcient heuristic for global optimization over continuous spaces.
J
Global
Optim
11:341–359.
https://doi.org/10.1023/A:
1008202821328
4. Booker LB, Goldberg DE, Holland JH (1989) Classiﬁer systems
and genetic algorithms. Artif Intell 40:235–282. https://doi.org/
10.1016/0004-3702(89)90050-7
5. Yao X, Liu Y, Lin G (1999) Evolutionary programming made
faster. IEEE Trans Evol Comput 3:82–102. https://doi.org/10.
1109/4235.771163
6. Whitley D (2001) An overview of evolutionary algorithms:
practical
issues
and
common
pitfalls.
Inf
Softw
Technol
43:817–831. https://doi.org/10.1016/S0950-5849(01)00188-4
7. Wang D, Tan D, Liu L (2018) Particle swarm optimization
algorithm: an overview. Soft comput 22:387–408. https://doi.org/
10.1007/s00500-016-2474-6
8. Dorigo M, Birattari M, Stutzle T (2006) Ant colony optimization.
IEEE Comput Intell Mag 1:28–39. https://doi.org/10.1109/MCI.
2006.329691
9. Rashedi E, Nezamabadi-pour H, Saryazdi S (2009) GSA: a
gravitational search algorithm. Inf Sci (N Y) 179:2232–2248.
https://doi.org/10.1016/j.ins.2009.03.004
10. Mirjalili S, Mirjalili SM, Lewis A (2014) Grey wolf optimizer.
Adv Eng Softw 69:46–61. https://doi.org/10.1016/j.advengsoft.
2013.12.007
11. Karaboga D, Basturk B (2007) Artiﬁcial bee colony (ABC)
Optimization algorithm for solving constrained optimization
problems. In: Foundations of fuzzy logic and soft computing.
Springer, Berlin, Heidelberg, pp 789–798. https://doi.org/10.
1007/978-3-540-72950-1_77
12. Mirjalili S (2015) Moth-ﬂame optimization algorithm: a novel
nature-inspired
heuristic
paradigm.
Knowl
Based
Syst
89:228–249. https://doi.org/10.1016/j.knosys.2015.07.006
13. Mirjalili S, Lewis A (2016) The whale optimization algorithm.
Adv Eng Softw 95:51–67. https://doi.org/10.1016/j.advengsoft.
2016.01.008
14. Mirjalili S (2015) The ant lion optimizer. Adv Eng Softw
83:80–98. https://doi.org/10.1016/j.advengsoft.2015.01.010
15. del Valle Y, Venayagamoorthy GK, Mohagheghi S et al (2008)
Particle swarm optimization: basic concepts, variants and appli-
cations in power systems. IEEE Trans Evol Comput 12:171–195.
https://doi.org/10.1109/TEVC.2007.896686
16. Alamir N, Kamel S, Hassan MH, Abdelkader SM (2023) An
effective quantum artiﬁcial rabbits optimizer for energy man-
agement in microgrid considering demand response. Soft comput.
https://doi.org/10.1007/s00500-023-08814-5
17. Markowski P (2007) Supercell thunderstorms. In: Atmospheric
convection:
research
and
operational
forecasting
aspects.
Springer, Vienna, pp 29–43. https://doi.org/10.1007/978-3-211-
69291-2_5
18. Lemon LR (1998) On the mesocyclone ‘‘dry intrusion’’ and tor-
nadogenesis. In: Preprints, 19th Conf. on severe local storms,
Minneapolis, MN, Amer Meteor Soc p 755
19. Davies-Jones R (1984) Streamwise vorticity: the origin of updraft
rotation in supercell storms. J Atmos Sci 41:2991–3006. https://
doi.org/10.1175/1520-0469(1984)041%3c2991:SVTOOU%3e2.
0.CO;2
20. Markowski P, Richardson Y (2011) Mesoscale meteorology in
midlatitudes. Wiley, New Jersey
21. Faramarzi A, Heidarinejad M, Mirjalili S, Gandomi AH (2020)
Marine predators algorithm: a nature-inspired metaheuristic.
Expert Syst Appl 152:113377. https://doi.org/10.1016/j.eswa.
2020.113377
22. Doswell CA, Bosart LF (2001) Extratropical synoptic-scale
processes and severe convection. Severe convective storms.
American Meteorological Society, Boston, MA, pp 27–69
23. Kaur S, Awasthi LK, Sangal AL, Dhiman G (2020) Tunicate
swarm algorithm: a new bio-inspired based metaheuristic para-
digm for global optimization. Eng Appl Artif Intell 90:103541.
https://doi.org/10.1016/j.engappai.2020.103541
24. Mirjalili S, Gandomi AH, Mirjalili SZ et al (2017) Salp swarm
algorithm: a bio-inspired optimizer for engineering design prob-
lems. Adv Eng Softw 114:163–191. https://doi.org/10.1016/j.
advengsoft.2017.07.002
25. Mirjalili S (2016) SCA: a sine cosine algorithm for solving
optimization problems. Knowl Based Syst 96:120–133. https://
doi.org/10.1016/j.knosys.2015.12.022
26. Mirjalili S, Mirjalili SM, Hatamlou A (2016) Multi-verse opti-
mizer: a nature-inspired algorithm for global optimization. Neural
Comput Appl 27:495–513. https://doi.org/10.1007/s00521-015-
1870-7
Neural Computing and Applications (2025) 37:7207–7260
7259
123

---

## Page 54
27. Ahmadianfar I, Heidari AA, Gandomi AH et al (2021) RUN
beyond the metaphor: an efﬁcient optimization algorithm based
on Runge Kutta method. Expert Syst Appl 181:115079
28. Ahmadianfar I, Heidari AA, Noshadian S et al (2022) INFO: an
efﬁcient optimization algorithm based on weighted mean of
vectors. Expert Syst Appl 195:116516
29. Kennedy J, Eberhart R Particle swarm optimization. In: Pro-
ceedings of ICNN’95—international conference on neural net-
works. IEEE, pp 1942–1948
30. Wang Y, Wang P, Zhang J et al (2019) A novel bat algorithm
with multiple strategies coupling for numerical optimization.
Mathematics 7:135. https://doi.org/10.3390/math7020135
31. Sang-To T, Le-Minh H, Mirjalili S et al (2022) A new movement
strategy of grey wolf optimizer for optimization problems and
structural damage identiﬁcation. Adv Eng Softw 173:103276.
https://doi.org/10.1016/j.advengsoft.2022.103276
32. Yang Y, Gao Y, Tan S et al (2022) An opposition learning and
spiral modelling based arithmetic optimization algorithm for
global continuous optimization problems. Eng Appl Artif Intell
113:104981. https://doi.org/10.1016/j.engappai.2022.104981
33. Ray T, Saini P (2001) Engineering design optimization using a
swarm with an intelligent information sharing among individuals.
Eng
Optim
33:735–748.
https://doi.org/10.1080/
03052150108940941
34. Erdogan Yildirim A, Karci A (2018) Application of three bar
truss problem among engineering design optimization problems
using artiﬁcial atom algorithm. In: 2018 international conference
on artiﬁcial intelligence and data processing (IDAP). IEEE,
pp 1–5
35. Sadollah A, Bahreininejad A, Eskandar H, Hamdi M (2013) Mine
blast algorithm: a new population based algorithm for solving
constrained engineering optimization problems. Appl Soft Com-
put 13:2592–2612. https://doi.org/10.1016/j.asoc.2012.11.026
36. Zhang M, Luo W, Wang X (2008) Differential evolution with
dynamic stochastic selection for constrained optimization. Inf Sci
(N Y) 178:3043–3074. https://doi.org/10.1016/j.ins.2008.02.014
37. Saremi S, Mirjalili S, Lewis A (2017) Grasshopper optimisation
algorithm: theory and application. Adv Eng Softw 105:30–47.
https://doi.org/10.1016/j.advengsoft.2017.01.004
38. Liu H, Cai Z, Wang Y (2010) Hybridizing particle swarm opti-
mization with differential evolution for constrained numerical
and engineering optimization. Appl Soft Comput 10:629–640.
https://doi.org/10.1016/j.asoc.2009.08.031
39. Gandomi AH, Yang X-S, Alavi AH (2013) Cuckoo search
algorithm: a metaheuristic approach to solve structural opti-
mization problems. Eng Comput 29:17–35. https://doi.org/10.
1007/s00366-011-0241-y
40. Fan Q, Huang H, Li Y et al (2021) Beetle antenna strategy based
grey wolf optimization. Expert Syst Appl 165:113882. https://doi.
org/10.1016/j.eswa.2020.113882
41. Chickermane H, Gea HC (1996) Structural optimization using a
new local approximation method. Int J Numer Method Eng
39:829–846
42. Cheng M-Y, Prayogo D (2014) Symbiotic organisms search: a
new
metaheuristic
optimization
algorithm.
Comput
Struct
139:98–112. https://doi.org/10.1016/j.compstruc.2014.03.007
43. Zhao J, Gao Z-M, Sun W (2020) The improved slime mould
algorithm with Levy ﬂight. J Phys Conf Ser 1617:012033. https://
doi.org/10.1088/1742-6596/1617/1/012033
44. Yu C, Cai Z, Ye X et al (2020) Quantum-like mutation-induced
dragonﬂy-inspired optimization approach. Math Comput Simul
178:259–289. https://doi.org/10.1016/j.matcom.2020.06.012
45. Kaveh A, Khayatazad M (2012) A new meta-heuristic method:
ray optimization. Comput Struct 112–113:283–294. https://doi.
org/10.1016/j.compstruc.2012.09.003
46. Huang F, Wang L, He Q (2007) An effective co-evolutionary
differential evolution for constrained optimization. Appl Math
Comput 186:340–356. https://doi.org/10.1016/j.amc.2006.07.105
47. Deb K (1991) Optimal design of a welded beam via genetic
algorithms. AIAA J 29:2013–2015. https://doi.org/10.2514/3.
10834
48. Lee KS, Geem ZW (2005) A new meta-heuristic algorithm for
continuous engineering optimization: harmony search theory and
practice. Comput Method Appl Mech Eng 194:3902–3933.
https://doi.org/10.1016/j.cma.2004.09.007
49. He Q, Wang L (2007) An effective co-evolutionary particle
swarm optimization for constrained engineering design problems.
Eng Appl Artif Intell 20:89–99. https://doi.org/10.1016/j.engap
pai.2006.03.003
50. Ghasemi M, Rahimnejad A, Akbari E et al (2023) A new meta-
phor-less simple algorithm based on Rao algorithms: a fully
informed search algorithm (FISA). PeerJ Comput Sci 9:e1431.
https://doi.org/10.7717/peerj-cs.1431
51. Seyyedabbasi A, Kiani F (2023) Sand cat swarm optimization: a
nature-inspired algorithm to solve global optimization problems.
Eng Comput 39:2627–2651. https://doi.org/10.1007/s00366-022-
01604-x
52. Mezura-Montes E, Coello Coello CA, Landa-Becerra R Engi-
neering optimization using simple evolutionary algorithm. In:
Proceedings. 15th IEEE international conference on tools with
artiﬁcial intelligence. IEEE Comput. Soc, pp 149–156
53. Stephen S, Christu D, Dalvi A (2018) Design optimization of
weight of speed reducer problem through matlab and simulation
using ansys. Int J Mech Eng Technol 9:339–349
54. Kamboj VK, Nandi A, Bhadoria A, Sehgal S (2020) An intensify
Harris Hawks optimizer for numerical and engineering opti-
mization problems. Appl Soft Comput 89:106018. https://doi.org/
10.1016/j.asoc.2019.106018
55. Lu S, Kim HM (2010) A regularized inexact penalty decompo-
sition algorithm for multidisciplinary design optimization prob-
lems with complementarity constraints. J Mech Des 132:041005.
https://doi.org/10.1115/1.4001206
56. Geem ZW, Kim JH, Loganathan GV (2001) A new heuristic
optimization
algorithm:
harmony
search.
SIMULATION
76:60–68
57. Baykasog˘lu A, Ozsoydan FB (2015) Adaptive ﬁreﬂy algorithm
with chaos for mechanical design optimization problems. Appl
Soft Comput 36:152–164. https://doi.org/10.1016/j.asoc.2015.06.
056
58. Akhtar S, Tai K, Ray T (2002) A socio-behavioural simulation
model
for
engineering
design
optimization.
Eng
Optim
34:341–354. https://doi.org/10.1080/03052150212723
59. Abualigah L, Yousri D, Abd Elaziz M et al (2021) Aquila opti-
mizer: a novel meta-heuristic optimization algorithm. Comput
Ind Eng 157:107250. https://doi.org/10.1016/j.cie.2021.107250
60. Ma B, Lu P, Zhang L et al (2021) Enhanced sparrow search
algorithm with mutation strategy for global optimization. IEEE
Access
9:159218–159261.
https://doi.org/10.1109/ACCESS.
2021.3129255
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
7260
Neural Computing and Applications (2025) 37:7207–7260
123

---
