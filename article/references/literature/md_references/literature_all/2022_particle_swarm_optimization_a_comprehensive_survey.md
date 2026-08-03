# 2022_particle_swarm_optimization_a_comprehensive_survey

**Source File**: `article\references\literature\2022_particle_swarm_optimization_a_comprehensive_survey.pdf`
**Total Pages**: 31

---

<!-- Page 1 -->
## Page 1

Received November 26, 2021, accepted January 10, 2022, date of publication January 13, 2022, date of current version January 27, 2022.
Digital Object Identifier 10.1109/ACCESS.2022.3142859
Particle Swarm Optimization: A Comprehensive Survey
TAREQ M. SHAMI
1, AYMAN A. EL-SALEH
2, (Senior Member, IEEE),
MOHAMMED ALSWAITTI
3, (Member, IEEE), QASEM AL-TASHI
4,5,
MHD AMEN SUMMAKIEH
6, (Member, IEEE), AND
SEYEDALI MIRJALILI
7,8, (Senior Member, IEEE)
1Department of Electronic Engineering, University of York, York YO10 5DD, U.K.
2Department of Electronics and Communication Engineering, College of Engineering, A’Sharqiyah University, Ibra 400, Oman
3School of Electrical and Computer Engineering, Department of Information and Communication Technology, Xiamen University Malaysia, Sepang 43900,
Malaysia
4Department of Imaging Physics, The University of Texas MD Anderson Cancer Center, Houston, TX 77030, USA
5Faculty of Administrative and Computer Sciences, University of Albaydha, Albaydha, Yemen
6Faculty of Engineering, Multimedia University, Cyberjaya, Selangor 63100, Malaysia
7Centre for Artiﬁcial Intelligence Research and Optimization, Torrens University Australia, Fortitude Valley, QLD 4006, Australia
8Yonsei Frontier Laboratory, Yonsei University, Seoul 03722, Republic of Korea
Corresponding author: Mohammed Alswaitti (alswaitti.mohammed@xmu.edu.my)
This work was supported by Xiamen University Malaysia (XMUM) under the XMUM Research Fund (XMUMRF)
(Grant number: XMUMRF/2019-C4/IECE/0012).
ABSTRACT Particle swarm optimization (PSO) is one of the most well-regarded swarm-based algorithms in
the literature. Although the original PSO has shown good optimization performance, it still severely suffers
from premature convergence. As a result, many researchers have been modifying it resulting in a large
number of PSO variants with either slightly or signiﬁcantly better performance. Mainly, the standard PSO has
been modiﬁed by four main strategies: modiﬁcation of the PSO controlling parameters, hybridizing PSO with
other well-known meta-heuristic algorithms such as genetic algorithm (GA) and differential evolution (DE),
cooperation and multi-swarm techniques. This paper attempts to provide a comprehensive review of PSO,
including the basic concepts of PSO, binary PSO, neighborhood topologies in PSO, recent and historical
PSO variants, remarkable engineering applications of PSO, and its drawbacks. Moreover, this paper reviews
recent studies that utilize PSO to solve feature selection problems. Finally, eight potential research directions
that can help researchers further enhance the performance of PSO are provided.
INDEX TERMS Applications of PSO, binary PSO, evolutionary computation, feature selection, hybrid
algorithms, meta-heuristic algorithms, particle swarm optimization, PSO variants.
I. INTRODUCTION
A lot of engineering applications, such as electrical power
systems and signal processing, require an efﬁcient and
effective algorithm that can solve their ﬁled-related optimiza-
tion problems. Real-world optimization problems have been
solved by swarm algorithms such as particle swarm opti-
mization (PSO) [1] and ant colony optimization (ACO) [2]
as well as other meta-heuristic algorithms including genetic
algorithm (GA) [3] and differential evolution (DE) [4].
Generally, most meta-heuristic algorithms can solve many
different types of optimizations problems. Nevertheless, these
algorithms may have one or more of the following drawbacks:
• Having a lot of parameters to be tuned.
• Requiring
high
programming
skills
to
build
the
algorithm.
The associate editor coordinating the review of this manuscript and
approving it for publication was Donato Impedovo
.
• High computational cost.
• The need of transforming algorithms into binary
forms.
PSO was initially introduced by Kennedy and Eberhart [1]
in 1995. The PSO algorithm has attracted a lot of researchers
in the last decade due to its simple implementation and
fewer controlling parameters. The idea and formulation of
the PSO algorithm were stimulated from observing the
societal behavior of birds ﬂocking and ﬁsh schooling.
In nature, a swarm of birds ﬂies in the space following
a leader who has the closest position to the food. The
social behavior of birds can be translated into algorithmic
operations, as in PSO, to solve optimization problems where
the swarm of birds is interpreted as a swarm of particles
and each particle represents a candidate solution. The
swarm of particles searches the space in given dimensions
and ﬁnds the best solution that optimizes the problem at
hand. The following points summarize some of the facts
VOLUME 10, 2022
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
10031


---

<!-- Page 2 -->
## Page 2

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
that make the PSO algorithm an attractive optimization
algorithm:
• PSO is simple to implement and code.
• PSO has only three controlling parameters (inertia
weight, cognitive ratio, and social ratio). A slight change
in any of these three controlling parameters results in a
different performance as shown in [5] and [6].
• PSO is ﬂexible to hybridize with other optimization
algorithms.
PSO is efﬁcient in controlling the balance between
exploration and exploitation. Particles in the exploration
phase explore the space extensively while the exploitation
phase focuses on promising regions. The more balance
between exploration and exploitation, the better the PSO
performance.
The abovementioned advantages have made PSO a promis-
ing candidate for optimizing a wide variety of real-world
optimization problems and applications. In the literature,
there have been a few PSO review papers that can be
split into two categories: the ﬁrst category reviews PSO
and its applications on a speciﬁc ﬁeld [7], [8] whereas the
second reviews existing PSO variants [9], [10]. Although the
article in [9] reviewed recent studies on PSO, the authors
considered PSO in continuous search space only whereas
PSO in the binary form was somehow excluded. In addition,
the authors did not consider several important aspects such as
the applications of PSO in optimization problems.
A recent article [10] reviewed the research works carried
on PSO but it was limited to binary PSO variants only.
Recently, a survey paper on PSO has been published in [11]
where several PSO variants in both continuous and discrete
spaces are reviewed. However, the article does not include
neighborhood topologies as well as the hybridization of PSO
with other common meta-heuristic algorithms such as ACO
and gravitational search algorithm (GSA). In addition, it is
only focused on the application of PSO on solar photovoltaic
systems without considering other engineering applications
of PSO. Table 1 summarizes recent and important state-of-
the-art PSO survey papers.
The main aim of this paper is to present a comprehensive
review of PSO that includes continuous PSO, binary PSO,
different PSO topologies, hybrid PSO variants, types of PSO
variants (e.g., cooperative PSO and multi-swarm PSO), and
the applications of PSO variants in optimization problems.
More importantly, this review paper focuses on PSO-based
feature selection. To the best of the authors’ knowledge,
there has been no publication on a comprehensive survey
that covers the recent advances in PSO variant developments
and the implementation of PSO to solve feature selection
problems.
The main contributions of this review article can be
summarized as follows:
1- A comprehensive and critical review of PSO and its
variants is provided. The limitations of existing PSO variants
are identiﬁed and some insightful recommendations are
provided to overcome these limitations. In addition, clear
guidance that includes that the essential steps to develop novel
robust PSO variants is provided.
2- This paper attempts to provide a thorough review of
the applications of PSO to feature selection problems due to
their extreme importance in the artiﬁcial intelligence ﬁeld.
Moreover, a comprehensive review of PSO-based feature
selection is still lacking.
3- Eight potential research directions are identiﬁed to
further enhance the optimization performance of PSO.
The rest of this paper is organized as follows. Section II
illustrates the formulation of the PSO algorithm and other
basic concepts related to PSO. It also highlights different
neighborhood topologies used in PSO. In Section III, the
modiﬁcations introduced to the original PSO by inertia
weight and constriction factor concepts are discussed.
In addition, it reviews several strategies that have been
used to control the PSO parameters and it critically reviews
several recent high-performance PSO variants. Section III
also reviews historical prominent variants of PSO. Section IV
presents the PSO in binary form and its variants. In Section V,
the steps required for validating novel PSO variants are
provided. Section VI focuses on the application of PSO to
solve feature selection problems. Moreover, prominent engi-
neering applications of PSO are overviewed in Section VI.
Section VII demonstrates the drawbacks of PSO while
Section VII provides some potential research directions that
can help PSO researchers to enhance the performance of PSO
further. Finally, Section IX concludes the overall remarks of
this paper.
II. BASIC CONCEPTS OF PSO
A. PARTICLE SWARM OPTIMIZATION
The ﬁrst PSO was presented by Kennedy and Eberhart
as a continuous real-valued algorithm [1]. This version is
referred to as the standard PSO (SPSO) throughout this paper.
In SPSO, a swarm of particles ﬂies in a D-dimensional
search space seeking an optimal solution. Each particle i
possesses a current velocity vector Vi = [vi1, vi2, . . . , viD]
and a current position vector Xi
=
[xi1, xi2, . . . , xiD],
where D is the number of dimensions. The SPSO process
starts by randomly initializing Vi and Xi. Then, in each
iteration, the best position that has been found by particle
i Pbesti
=
[Pbesti1, Pbesti2, . . . , PbestiD] and the best
position that has been found by the whole swarm Gbest =
[Gbest1, Gbest2, . . . , GbestD] guide particle i to update its
velocity and position by (1) and (2):
vid (t + 1) = vid (t) + c1r1 (Pbestid (t) −xid (t))
+ c2r2 (Gbestd (t) −xid (t)) ,
(1)
xid (t + 1) = xid (t) + vid (t + 1) ,
(2)
where c1 and c2 are the cognitive and social acceleration
coefﬁcients, and r1 and r2 are two uniform random values
generated within [0, 1] interval. The pseudo-code of the
SPSO for solving a minimization problem is shown in
Algorithm 1.
10032
VOLUME 10, 2022


---

<!-- Page 3 -->
## Page 3

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
TABLE 1. Summary of the state-of-the-art PSO review papers.
VOLUME 10, 2022
10033


---

<!-- Page 4 -->
## Page 4

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
Algorithm 1 The Pseudo-Code of the SPSO for Solving a
Minimization Problem [1]
1: Initialization
2: Deﬁne the swarm size S and the number of dimensions
D
3: for each particle i ∈[1..S]
4: Randomly generate Xi and Vi, and evaluate the ﬁtness of
Xi denoting it as f (Xi)
5: Set Pbesti = Xi and f (Pbesti) = f (Xi)
6: end for
7: Set Gbest = Pbest1 and f (Gbest) = f (Pbest1)
8: for each particle i ∈[1..S]
9:
if f (Pbesti) < f (Gbest) then
10:
f (Gbest) = f (Pbesti)
11:
end if
12: end for
13: while t < maximum number of iterations
14: for each particle i ∈[1..S]
15: Evaluate its velocity vid (t + 1) using Equation (1)
16: Update the position xid (t + 1) of the particle using
Equation (2)
17: if f (xi (t + 1)) < f (Pbesti) then
18: Pbesti = xi (t + 1)
19:
f (Pbesti) = f (xi (t + 1)
20: end if
21: if f (Pbesti) < f (Gbest) then
22:
Gbest = Pbesti
23:
f (Gbest) = f (Pbesti)
24: end if
25: end for
26: t = t + 1
27: end while
28: return Gbest
B. VELOCITY CLAMPING
Velocity clamping was initially introduced by Eberhart and
Kennedy [29] to avoid the velocity explosion and divergence.
Velocity clamping limits the particles to move within a
boundary in the search space by setting up a maximum
velocity Vmax. If the updated velocity of a particle is found
to exceed the maximum velocity Vmax, then it is set to Vmax
as follows:
vid (t + 1) = min(vid (t + 1) , Vmax)
(3)
Although the velocity clamping helps to prevent the velocity
from explosion, ﬁnding a proper value of Vmax is very
essential and it is not an easy task. A poor performance might
occur if the Vmax is not selected properly. For large values
of Vmax, the particles might ﬂy in a very random manner
and skip the optimal solution. On the contrary, for small
values of Vmax, the particles would have a very narrow search
space which might result in being trapped in a local optimum.
To resolve this critical problem, the maximum velocity Vmax
can be set as follows [30], [31]:
Vmax = δ(xmax −xmin)
(4)
where xmax and xmin are the maximum and minimum values
of the search space boundary respectively, and δ ∈(0, 1].
C. POPULATION SIZE
Population size is deﬁned as the number of particles in
the swarm. It is a crucial parameter that characterizes the
convergence performance of PSO. The main concern here is
ﬁnding the optimal swarm size at which the best convergence
performance of PSO can be attained. This concern has been
addressed in [32], [33] where the effect of the swarm size
on PSO performance was investigated. The conclusion drawn
in [32], [34] states that a small number of particles does not
support the swarm to explore more areas in the search space
and produces poor solutions while a large number of particles
improves the solution quality yet increases the computational
complexity. Also, it is concluded that the optimal swarm
size relies on the characteristics of the ﬁtness function to be
optimized. In the literature of PSO, it is common to set the
population size to a size between 20 to 50 particles [35]–[39].
D. STOPPING CRITERIA
Typically, there are two types of stopping criteria that are
used to terminate the PSO run. In the ﬁrst stopping criterion,
the execution of PSO stops when a predeﬁned number of
iterations is reached. This criterion has been widely used in
the literature (e.g., [39], [38]). The second stopping criterion
is the number of function evaluations (FEs) [35], [40]–[42],
calculated as follows:
FEs = S × T
(5)
where S is the swarm size and T is the maximum number of
iterations.
E. CONTROLLING PARAMETERS OF PSO
In general, PSO has three main controlling parameters:
inertia weight w, the cognitive component c1, and the social
component c2. These parameters have a remarkable effect on
the PSO performance where the best performance can only
be obtained by a proper setting of these parameters. In the
literature, many research efforts have been carried out to
enhance the performance of PSO by tuning these controlling
parameters through different mechanisms. The following
subsections focus on the state-of-the-art mechanisms for
tuning these three parameters.
1) INERTIA WEIGHT
The existing inertia weight mechanisms can be classiﬁed into
three groups. The ﬁrst group includes mechanisms where
the inertia weight is either static or random. This type
of mechanism does not require any feedback or historical
knowledge input. In the second group, the inertia weight
changes with time. In other words, the inertia weight is
10034
VOLUME 10, 2022


---

<!-- Page 5 -->
## Page 5

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
a function of the iteration number. This mechanism is
known as time-varying inertia weight. The third group is
called adaptive inertia weight where the inertia weight keeps
adjusting its value based on a feedback parameter. These three
mechanisms are further elaborated as follows:
2) THE STATIC AND RANDOM INERTIA WEIGHT
As mentioned earlier, the inertia weight was introduced by
Shi and Eberhart. In their work, a range of inertia weight
values have been tested and the results showed that a better
performance is obtained when w is in the range [0.8, 1.2].
In [45], the inertia weight was presented as a random
value. This method is suitable for applications in a dynamic
environment since it is not easy to predict whether a large or
a small value of w is needed.
w = 0.5 + (random(0, 1))/2
(6)
where random(0, 1) is a random value in the range [0, 1].
Therefore, w is limited to values in the range [0.5, 1].
3) TIME VARYING INERTIA WEIGHT
In PSO, an extensive global search (exploration) is required
at the early part of the process while the latter part requires
focused local search (exploitation). A static inertia weight
cannot meet such requirements. Thus, Shi and Eberhart [46]
introduced the ﬁrst time-varying inertia weight method called
linearly-varying inertia weight (LVIW) to address this issue.
The mathematical formula of this method is expressed as
follows:
w (t) = (wmax −wmin)
T −t
T

+ wmin,
(7)
where wmax and wmin are the initial and ﬁnal values of the
inertia weight, respectively, T is the maximum number of
iterations, and t is the number of the current iteration.
In their experimental study, Shi and Eberhart [46] noticed
that better performance is achieved if the PSO run starts
by choosing an inertia weight value of 0.9 and linearly
decreasing it until it reaches a value of 0.4 by the end of
the PSO run. This setting indicates that a global search is
performed at the beginning of the PSO run and it gradually
decreases to reﬁne the search to be locally focused. LVIW
is one of the most common, if not the most common, time-
varying techniques that have been widely used by many
researchers. Besides this technique, a lot of time-varying
inertia weight techniques have been proposed with different
performance achievements. The formulae of such techniques
are presented in Table 2.
4) ADAPTIVE INERTIA WEIGHT
In this group, the value of the inertia weight is adjusted based
on at least one feedback parameter. Utilizing the concept of
success rate [47], an adaptive inertia weight technique has
been proposed in [48]. This adaptive technique considers the
percentage of success as the feedback parameter. The inertia
weight of this adaptive strategy is expressed as follows:
w (t) = (wmax −wmin) Ps(t) + wmin,
(8)
where wmax and wmin are in the range [0, 1] and Ps ∈[0, 1]
is the percentage of particles that succeeded to enhance their
ﬁtness in the previous iteration. Other adaptive inertia weight
strategies are shown in Table 2.
5) ACCELERATION COEFFICIENTS
The acceleration coefﬁcients c1 and c2 guide the PSO search
towards the optimal solution. In [1], it was pointed out that a
relatively high value of c1 compared to c2 causes particles to
extremely wander in the search space. Conversely, a relatively
high value of c2 might cause the problem of premature
convergence. The authors recommended to statically set the
values of c1 and c2 to 2. Since then, a lot of authors followed
this recommendation in their PSO studies. Although this
setting appears to be the most common static strategy for
c1 and c2, other settings such as c1 = c2 = 1.49 are also
common. In [38], a hierarchical PSO with a time-varying
acceleration coefﬁcient (HPSO-TVAC) is proposed. At the
beginning of the HPSO-TVAC process, it is suggested to have
a large value of c1 and a small value of c2 to let particles
perform extensive search. On the contrary, a small value of
c1 and a large value of c2 help particles to focus more on
exploitation at the end of the searching process. The following
mathematical expressions illustrates how the values of c1 and
c2 are gradually varied:
c1 =
 c1f −c1i
 t
T + c1i
(9)
c2 =
 c2f −c2i
 t
T + c2i
(10)
where the subscripts f and i denote the ﬁnal and initial values,
respectively. As suggested in [38], the values of c1f , c1i, c2f
and c2i should be set to 0.5, 2.5, 2.5, 0.5, respectively.
F. NEIGHBORHOOD TOPOLOGIES IN PSO
Particles in a swarm are connected in a speciﬁc structure
commonly known as a neighborhood topology within which
they communicate with each other and share information.
A study on how the neighborhood topology could inﬂuence
the behavior of PSO operation was presented in [64]. Exper-
imental results revealed that some neighborhood topologies
perform better than others. The following subsections present
various neighborhood topologies that have been used in PSO
studies and applications.
1) STAR TOPOLOGY
The ﬁrst PSO algorithm that was introduced in [1] was
developed using a star topology where each particle considers
all other particles as its neighbors. The star topology is
also called Gbest in which all particles move towards the
best global particle in the swarm. The velocity and position
update equations for the star topology are the same equations
in (1) and (2), respectively. The star topology achieves
VOLUME 10, 2022
10035


---

<!-- Page 6 -->
## Page 6

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
TABLE 2. A summary of several state-of-the-art inertia weight techniques.
the fastest convergence among other topologies as it has a
great exploration capability. However, it often suffers from
convergence to local optima. The star topology has been
widely used by many researchers in different applications due
to its simple structure and fast convergence behavior.
2) RING TOPOLOGY
In the ring topology, each particle is connected to its two
immediate neighbors forming a circle [64]. The ring topology
is also known as lbest in which a particle is attracted by its
best local particle that has been found in its neighborhood.
The velocity update equation for the ring topology is modiﬁed
as follows:
vid (t + 1) = vid (t) + c1r1 (Pbestid (t) −xid (t))
+ c2r2 (lbestd (t) −xid (t))
(11)
where lbestd (t) is the best local position found in the ith
particle neighborhood. The two neighbors of the ith particle
are the (i −1)th particle and (i + 1)th particle. Particles in
the ring topology ﬂy towards their local best position. This
provides diversity and protects the algorithm from becoming
stuck at local optima. However, the convergence speed of the
ring topology decreases since more information needs to be
exchanged. In addition, the ring structure is not as simple
as the star structure. One of the earliest PSO variants that
implemented the ring topology is the fully informed particle
swarm (FIPS) [65]. In FIPS, the particle’s velocity relies on
all the particles’ best positions of its neighbors. Moreover,
FIPS applies the concept of the constriction factor.
3) VON NEUMANN
The Von Neumann topology is a rectangle matrix, for
example, (3 × 4), resulting in a population of 12 particles
where each particle is connected to the particles below,
above, on its right and left sides, and wrapping the edges.
The Von Neumann showed superior performance over other
topologies in many test problems [66].
4) DYNAMIC TOPOLOGY
In the dynamic topology, the neighborhood is refreshed
and regrouped after a certain number of iterations. In [67],
a dynamic neighborhood is developed where each particle,
10036
VOLUME 10, 2022


---

<!-- Page 7 -->
## Page 7

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
in the early stage of the PSO run, exchanges information
with only a small number of particles. This enhances the
exploration process in the early stage of the run. As the
number of iterations increases, the neighborhood of each
particle increases as well. At the end of the PSO run, all
particles communicate with each other resulting in a higher
exploitation capability. A dynamic neighborhood strategy
named dynamic neighborhood learning PSO (DNLPSO) is
presented in [68]. DNLPSO improved the CLPSO algo-
rithm [69] by making the learning particle’s neighborhood
dynamic.
5) OTHER TOPOLOGIES
In [70], a complex neighborhood PSO was proposed where
the neighborhood structure is a complex network that can
be tuned during the PSO run. The star topology and the
ring topology were combined in [71] to form a single PSO
named uniﬁed PSO (UPSO). Other common topologies such
as the pyramid, wheel, and cluster topologies are presented
in [30], [66], [72], [73].
III. PSO VARIANTS
Since the introduction of PSO, many new PSO variants
have been proposed to enhance its optimization performance.
Mainly, PSO is modiﬁed by developing new controlling
parameters strategies, hybridizing PSO with other well-
known meta-heuristic algorithms, cooperation and multi-
swarm approaches. This section reviews recent and historical
PSO variants and identiﬁes their limitations.
A. MODIFICATIONS OF PSO BY THE INERTIA WEIGHT
AND CONSTRUCTION FACTOR METHODS
1) INERTIA WEIGHT
To improve the convergence speed of SPSO, Yuhui and
Eberhart [43] modiﬁed the SPSO velocity update equation
vid(t + 1) by introducing a scaling factor that is multiplied
by vid(t). This scaling factor is termed as Inertia weight and
denoted by w. Based on this modiﬁcation, the velocity update
equation in (1) becomes now in the following form:
vid (t + 1) = wvid (t) + c1r1 (Pbestid (t) −xid (t))
+ c2r2 (Gbestd (t) −xid (t))
(12)
2) CONSTRICTION FACTOR
Clerc and Kennedy modiﬁed the velocity update equation
of the SPSO by introducing the concept of constriction
factor [44]. The role of the constriction factor is to ensure
that the PSO algorithm converges without using velocity
clamping. By using the constriction factor, the velocity update
equation becomes as follows:
vid (t + 1) = χ [vid (t) + c1r1 (Pbestid (t) −xid (t))
+ c2r2 (Gbestd (t) −xid (t))]
(13)
where χ
=
2k/
2 −φ −
p
φ2 −4φ
, φ
=
c1 + c2
and k ∈(0, 1].
The value of φ must be > 4 to ensure convergence. The
value of k controls the balance between exploration and
exploitation. The exploration mode takes place when the
value of k is large whereas the exploitation mode will be
activated when the value of k is small. Eberhart and Shi
stated that a combination of constriction factor and velocity
clamping would speed up the convergence rate [26].
However, the constriction factor approach still faces the
problem of becoming trapped in local optima.
B. RECENT PSO VARIANTS
In the last few years, many PSO variants have been proposed
to overcome the limitations of the original PSO algorithm
and the historical PSO variants. This part critically reviews
PSO variants that are published recently. The authors in [74]
proposed a new PSO variant named prey-predator PSO (PP-
PSO) that implements catch, escape, and breeding strategies
that can assist in enhancing the convergence speed and reduce
the computational time. The proposed approach is tested on
10 classical benchmarking functions and the CEC2017 test
suite for 10, 30, and 100 dimensions. Although this approach
has shown good performance, this good performance comes
at the expense of an unreasonable number of function
evaluations that can reach up to 106 function evaluations.
Moreover, the proposed variant was not tested on real-
world engineering problems. In [75], a multi-swarm PSO
is proposed where a sub-swarm focuses on exploration
while a different sub-swarm is performs exploitation. The
performance of the proposed variant is tested on the CEC
2015 on 10 and 30 dimensions. The performance of this
variant on high-dimensional problems as well as real-world
engineering problems is not investigated. The work in [76]
proposed a competition-based PSO variant where each
particle is allocated a competition coefﬁcient that allows to
distinguish particles and divide them into three groups. The
proposed method is tested on the CEC 2013 benchmarking
functions for 10 and 30 dimensions and retarder designing
problem as a real-world engineering problem. The impact
of increasing the dimensions on the performance of the
competition-based PSO needs to be investigated. The authors
in [77] developed a new PSO variant that utilizes PSO with
two differential mutations. The proposed approach was tested
on 16 well-known benchmarking functions and CEC 2013 on
30 dimensions only.
In [78], a novel PSO variant is proposed where the main
contribution is the utilization of the sigmoid function to
update the PSO acceleration coefﬁcients. The effectiveness
of the proposed variant is evaluated by testing it only
on 8 classical benchmarking functions on 30 dimensions.
Further work is needed to evaluate the performance of this
variant when it solves constrained optimization problems
and real-world engineering problems. An improved social
learning PSO is developed in [79] where the three best
particles are updated using a differential mutation strategy.
The developed approach is tested on the CEC 2013 test suite
on 30 and 50 dimensions. Tough the proposed variant has
VOLUME 10, 2022
10037


---

<!-- Page 8 -->
## Page 8

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
shown good performance, it was compared with PSO variants
only. Moreover, its performance on real-world optimization
problems is not studied. The authors in [80] developed a
novel PSO variant for constrained optimization problems.
The proposed approach was tested on twenty four classical
benchmarking functions for low dimensional problems as
well as on the reservoir drainage plan optimization problem.
With the help of mixed mutation strategies, a new PSO
variant is proposed in [81] based on the idea of dividing
the total population into an elitist population and a general
population. The effectiveness of the proposed algorithm is
evaluated by testing its performance on sixteen well-known
benchmarking functions for 30, 50, and 100 dimensions.
This multi-population PSO variant requires a massive num-
ber of function evaluations to achieve good performance.
In addition, its performance was not validated on real-world
constrained optimization problems. Also, The effectiveness
of this variant was compared with PSO variants only.
The original PSO velocity update equations are modiﬁed
in [82] by adding two new terms that aim to enhance the
performance. The new PSO variants are tested on sixteen
classical benchmarking functions for 50 dimensions without
evaluating their effectiveness on real-world optimization
problems. In addition, its performance is compared with PSO
variants only. A novel PSO variant that is tested on CEC2013
for 30 dimensions is proposed in [83]. The main concept
of the proposed approach is to split the whole population
into several sub-swarms using a chaotic sequence. To achieve
good performance, this variant requires a massive number
of function evaluations which is computationally expensive.
Utilizing complex-order derivatives, an improved version
of PSO, that is tested on CEC 2017 for 20, 30, and 40,
is proposed in [84]. The improved PSO is only compared with
PSO variants without considering other well-known meta-
heuristic algorithms. Based on forgetting ability and multi-
exemplar, a new version of PSO is proposed in [85] where
its effectiveness is tested on CEC 2013 for 30 dimensions.
Although the proposed approach shows good performance in
terms of average ﬁtness and standard deviation for most of the
tested functions, massive function evaluations are needed to
achieve such performance. In [86], inertia weight PSO [87],
CLPSO [69], LIPS [88], HPSO-TVAC [38], and FDR-
PSO [89] algorithms are combined to produce a new single
variant. The performance of the new variant is evaluated on
CEC2005 for 10 and 30 dimensions, and it is compared with
PSO variants only.
PSO
has
recently
been
hybridized
with
several
meta-heuristic algorithms such as the whale optimization
algorithm. PSO is hybridized with the whale optimiza-
tion algorithm in [90] and its performance is evaluated
on 18 classical benchmarking functions as well as on
electronic design optimization problems. Although the
proposed approach shows good performance, the results are
based on only 20 independent runs which might be not
enough to produce accurate results. In [91], a hybrid PSO
algorithm is developed utilizing an adaptive learning strategy.
The effectiveness of the hybrid approach is tested on 12
classical benchmarking test functions and CEC 2013 for
only 30 dimensions. Moreover, its performance is compared
with PSO variants only. By hybridizing PSO with sine
cosine acceleration coefﬁcients, a novel hybrid algorithm is
introduced in [92]. The performance of the hybrid algorithm
is evaluated on 12 well-known benchmarking functions for
10, 30, and 50 dimensions. However, its performance on
constrained optimization problems is not investigated.
In summary, recent PSO variants have shown good
optimization performance. However, all the PSO variants
presented in this subsection except [76], [80], [90] did
not consider constrained real-world optimization problems.
Their performance on real-world constrained optimization
problems needs to be investigated. The performance of
[75]–[78], [80], [82]–[86], [90]–[92] is tested only on low
dimension problems. Therefore, further work is needed to
validate their effectiveness on high-dimensional problems.
The PSO variants presented in [74], [78], [81], [82], [91] did
not provide any statistical analysis which is essential to show
the signiﬁcance and the superiority of these variants. Finally,
the PSO variants in [79], [81], [82], [84], [86], [91] compared
their performance with PSO variants without considering
other robust and well-known optimization algorithms. Table 3
summarizes the recent PSO discussed in this subsection and
presents their ideas and limitations.
C. HISTORICAL PSO VARIANTS IN CONTINUOUS SEARCH
SPACE
Since the introduction of SPSO in 1995, there has been
a continuous research effort in enhancing the convergence
speed, quality of achievable solutions, and stability of
PSO. This has resulted in an enormous number of PSO
variants some of which are dedicated to solving optimization
problems in speciﬁc applications while the rest are used for
general numerical optimization. This subsection discusses in
detail the most important historical PSO variants that have
been developed since the advent of PSO.
1) COOPERATIVE PSO
Cooperation, in context to meta-heuristics, is deﬁned as
exchanging information between a number of agents to
perform a speciﬁc task [93]. Though individual human
beings can work separately and compete with each other
to enhance their performance, better enhancement can be
achieved by cooperation. Potter and De Jong [94] applied
the cooperation concept in genetic algorithms (GAs). In [95],
the same idea was extended to PSO, and a new PSO variant
named cooperative particle swarm optimization (CPSO) was
introduced.
In SPSO, each particle consists of a D-dimensional vector
that represents a candidate solution. The updates of position
and velocity equations that occur in each iteration treat
this D-dimensional vector as one entity. Hence, there might
be some components that are selected to represent the
solution though they are moving far from this solution. These
10038
VOLUME 10, 2022


---

<!-- Page 9 -->
## Page 9

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
TABLE 3. A summary of recent PSO variants and their limitations.
VOLUME 10, 2022
10039


---

<!-- Page 10 -->
## Page 10

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
TABLE 3. (Continued.) A summary of recent PSO variants and their limitations.
components are wrongly selected since SPSO considers the
overall enhancement of the entire vector. Thus, CPSO [95]
was introduced to tackle this problem.
CPSO proposed two models denoted as CPSO-Sk and
CPSO-Hk. In CPSO-Sk, the entire vector is split into n
swarms and each swarm has a 1-D vector. Every single
component of the entire vector is optimized by the swarm that
it belongs to. In this case, the evaluation of the optimization
function is infeasible since the evaluation requires knowledge
of the entire D-dimensional vector. To handle this, a context
vector is invoked to form a vector that acts as a suitable
input for the optimization function. The context vector can
be formed by taking the values of the Gbest particles from
each of the n swarms and concatenating them to build up the
input vector. To evaluate the ﬁtness for the entire particles in
the jth swarm, the jth component takes the value of the ﬁrst
10040
VOLUME 10, 2022


---

<!-- Page 11 -->
## Page 11

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
particle of the jth swarm while the rest of the context vector
components are kept constant at the Gbest values. The same
procedure occurs for the rest of the particles in the jth swarm.
Experimentally, CPSO-Sk has been found to be easily stuck
in sub-optimal regions of the search space. Thus, CPSO-Hk,
which is a combination of CPSO-Sk and SPSO, is used to
overcome this problem.
In [96], a new CPSO variant with the concept of dimension
partition and adaptive velocity control was proposed. With
this approach, the new variant was dedicated to optimizing
multimodal functions by using the two-swarm cooperative
technique while using adaptive velocity control. In this work,
the population is split into two swarms where the SPSO
is applied to the ﬁrst swarm to perform a full dimensional
search and a single-dimensional PSO is applied to the
second swarm to perform a 1-D search. Information is
shared between the two swarms in a communication phase.
Unlike the conventional CPSO, the two swarms in this
new CPSO variant work concurrently. As for the adaptive
velocity control, Vmax is changed dynamically based on how
each particle ﬂies in the search space. This new CPSO
variant showed better performance when compared with
other variants for most of the tested problems.
The work presented in [97] used the CPSO and inertia
weight adaption together to come up with a new PSO variant
named adaptive cooperative PSO (ACPSO). This method
implemented the CPSO that was presented in [95] and
provided an adaptive method that automatically controls the
inertia weight. ACPSO was tested only on three bench-
marking functions and the results showed that its solution
quality and convergence behavior are better than CPSO for
all the three tested functions. However, the performance of
ACPSO still needs to be thoroughly investigated using other
benchmarking functions to prove its effectiveness.
2) MULTI-SWARM PSO
The concept of multi-swarm PSO (MSPSO) has been applied
in several PSO research works. In MSPSO, the population
of particles is split into sub-swarms where each sub-swarm
carries out a speciﬁc task. A sub-swarm task might be
adjusted as time goes on and information is shared among
sub-swarms.
One of the works that considered the use of the MSPSO
concept was presented in [98]. This work presented a multi-
swarm cooperative PSO (MCPSO) that divides the population
into one master swarm and multiple slave swarms. Each slave
swarm performs an independent single PSO run to control
the diversity of the population whereas the formation of the
master swarm depends on its own experience as well as
the slave swarm experience. In MCPSO, the master swarm
can update its particles by either a sequence of competitions
or a sequence of collaboration with the slave swarms. The
ﬁrst case is known as the competitive MCPSO while the
second is called the collaborative MCPSO. The performance
of MCPSO was evaluated on six benchmarking functions and
results have demonstrated that it can perform better than the
SPSO [98], [99].
A Multi-swarm Self-adaptive CPSO (MSCPSO) was
proposed in [100]. The total population in MSCPSO is
split into four sub-swarms where information is shared
among themselves. MSCPSO applied three strategies namely
cooperative, diversity, and self-adaptive strategies to escape
from becoming stuck in local optima, enhance diversity, and
obtain better solutions. An attractive feature of this algorithm
is that it does not add any complexity to the SPSO algorithm.
In other words, its implementation is as simple and easy as the
SPSO. MSCPSO was examined only on six benchmarking
functions for 10 and 30 dimensions. Although MSCPSO has
shown good performance on the six tested benchmarking
functions in the cases of 10 and 30 dimensions, there is
no proof that this algorithm can show good performance
in the case of high-dimension search space or when other
benchmarking functions are tested.
A tribal PSO (TPSO) is proposed in [101] where the
population is split into several tribes or sub-swarms using a
self-clustering algorithm. The process of the TPSO algorithm
consists of four major steps: initializing population, using
a clustering algorithm to generate tribes, performing the
evaluation step where the performance of each particle is
evaluated, and ﬁnally using the tribe’s adaptation method to
add and delete particles.
3) HYBRID PSO
In the ﬁeld of meta-heuristics, hybridization is the process of
selecting the best properties of two distinct algorithms that
can solve the same problem and joining them together to
come up with a novel algorithm that can achieve better results
than the individual algorithms. PSO has been hybridized with
many evolutionary algorithms such as GA, DE, and ACO to
overcome its drawbacks, such as premature convergence. The
hybridization of PSO with GA, DE, ACO as well as with other
techniques is presented in the following.
a: HYBRIDIZATION OF PSO WITH GA
GA was initially introduced by John Holland [102] as one
of the earliest evolutionary algorithms. Combining PSO with
GA is a famous approach that has been widely considered due
to the superior convergence performance as compared to the
individual PSO and GA.
A hybrid PSO and GA (GA-PSO) was proposed in [103]
to solve multimodal problems. The process of GA-PSO starts
by creating a population size of 4D for a problem with
D dimensions. The ﬁtness of each individual is calculated,
and individuals are ranked based on their ﬁtness values.
The selection, crossover, and mutation operators of GA are
applied to the best 2N individuals whereas PSO is applied to
the worst 2N individuals. This hybrid approached is tested
on seventeen multimodal functions and it has shown better
performance in terms of solution quality and convergence
speed when compared with the continuous genetic algorithm
(CGA) [104] and Nelder-Mead PSO (NMPSO) [105].
VOLUME 10, 2022
10041


---

<!-- Page 12 -->
## Page 12

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
In [106], two-hybrid algorithms named GA-PSO and PSO-
GA were introduced. In GA-PSO, the PSO initial population
is created by GA, whereas in PSO-GA, the GA initial
population is created by PSO. It has been observed that the
PSO-GA performs better than GA-PSO, SPSO, and GA.
The work in [107] combined PSO with GA for ﬁeld
development optimization. The resultant hybrid algorithm is
called genetical swarm optimization (GSO). In this hybrid
algorithm, the population is split into two portions and
it is reconstructed by GA and PSO operations in every
iteration. A hybridization constant (HC) was introduced to
indicate the population percentage that is constructed with
GA where HC = 0 indicates that only PSO is used and
HC = 1 indicates that only GA is implemented.
In [108], a hybrid PSO and GA named HPSOGA was
proposed. In this approach, the population is split into two
groups based on a hybrid probability P. The size of the
ﬁrst group is M × P where M is the number of particles
in the whole population, and the size of the other group is
M −(M × P). The ﬁrst group updates its particles positions
by PSO while particles in the other group are updated by
the three GA operations: selection, crossover and mutation.
HPSOGA showed that its performance is better than the
performance of SPSO.
b: HYBRIDIZATION OF PSO WITH DE
DE is a population-based algorithm that was ﬁrst presented
by R. Storn and K. Price [109] in 1995 to solve optimization
problems. The selection, mutation, and crossover operators
of GA are also used in DE but they function differently.
One of the advantages of DE is that it maintains diversity;
however, unlike PSO, it is unable to keep track of the
process history [110]. In [110], a hybrid DE with PSO
(DEPSO) algorithm was proposed to solve economic dispatch
problems. The overall procedure of this proposed algorithm
is based on DE and letting PSO generates a second mutant
operator. DEPSO showed its effectiveness in producing good
solutions and efﬁcient computation. DE and enhanced PSO
(EPSO) were hybridized in [111] where they are executed
in parallel and information is exchanged frequently. This
approach was applied to design antenna arrays. DEPSO
achieves a better global search than the individual DE and
EPSO. In [112], a hybrid approach that combines PSO and
DE is developed. In this approach, each of the PSO iterations
is followed by implementing the three operators of DE
(mutation, recombination, and selection) to the best personal
positions. During the mutation procedure, six DE mutation
techniques can be used. After that, a tournament is conducted
to select the best position.
A hybrid PSO and DE (PSO-DE) was proposed in [113]
to ﬁnd the optimal design of water distribution systems.
The basic idea behind this approach is that DE is not
integrated with PSO at all iterations but only at a predeﬁned
interval of iterations. The results of PSO-DE, in solving
three water distribution problems, showed better solution
accuracy and computation efﬁciency than PSO. To conﬁrm
the effectiveness of PSO-DE, it should be used to solve more
complex optimization problems and be compared with DE.
In [114], the authors proposed a hybrid PSO and DE (DE-
PSO) that is divided into two alternating phases, DE phase,
and PSO phase. This hybrid version begins with the DE
phase until a trail vector is created. The trail vector is added
to the population if it satisﬁes a predeﬁned requirement,
else the proposed algorithm switches to the PSO phase and
creates a new potential solution. DE-PSO is evaluated on
several numerical benchmarking problems and the results
have shown that DE-PSO outperforms the standard PSO
and DE. In [115], a hybrid quantum PSO (QPSO) [116]
with DE named DEQPSO is presented to solve a route
planning problem. The ﬁrst step in DEQPSO is to update
the population by PSO then activate the DE algorithm.
This proposed algorithm introduced a new form of vectors
called the donor vector which makes the DE in this
algorithm somewhat different from the classical DE. Based
on simulation results, DEQPSO outperforms QPSO and DE
in terms of optimal solution and convergence speed.
c: HYBRIDIZATION OF PSO WITH OTHER ALGORITHMS
Besides GA and DE, PSO has been hybridized with other
algorithms such as ACO [117], gravitational search algorithm
(GSA) [118], grey wolf optimizer (GWO) [119], and
simulated annealing (SA) [120], [121].
In [117], a hybrid algorithm based on PSO and ACO
was proposed. The developed hybrid algorithm is named as
hybrid ant particle optimization algorithm (HAP). In each
HAP iteration, separate executions of PSO and ACO are
performed resulting in a new solution for PSO and another
new solution for ACO. The best solution out of these two
solutions is chosen to be the global best of the overall
system. Particles and ant positions are updated based on
the parameters of this obtained global best. HAP has shown
that it can achieve better solutions as compared with SPSO
and ACO. However, HAP was tested only on simple and
low-dimensional benchmarking functions. Its performance
in complex high-dimensional optimization problems needs
to be investigated. A new hybrid method consisting of PSO
and ACO that is used for energy optimization was proposed
in [122]. The concept of this approach is to update the
direction operator of movement if the best solution of ACO
is affected by the best solution of PSO. This hybrid approach
was also used in [123] to tune the controller coefﬁcients in
wind power plants. In [124], a hybrid PSO with ACO is
proposed for the economic dispatch of a power system.
A novel hybrid PSO and GSA (HPSO-GSA) that is tested
on only ﬁve benchmark functions is proposed in [125].
Results have shown that HPSO-GSA performs better than the
individual performance of PSO and GSA for all the selected
ﬁve benchmarking functions. Another combination of PSO
and GSA is the gravitational particle swarm (GPS) [126].
In GPS, the velocities and positions of particles are updated
based on the velocity of PSO as well as the acceleration of
GSA. The results have demonstrated that GPS outperforms
10042
VOLUME 10, 2022


---

<!-- Page 13 -->
## Page 13

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
SPSO and GSA. However, the parameter setting in GPS is
not optimal. Thus, further work is needed to produce better
results through efﬁcient parameter tuning. An improved
hybrid version of PSO and GSA called centripetal accelerated
PSO (CAPSO) was introduced in [39]. In CAPSO, the
standard velocity of PSO shown in (1) is modiﬁed by adding
two terms called acceleration and centripetal acceleration.
This modiﬁcation is introduced to accelerate the convergence
speed and protect the algorithm from becoming trapped in
local optima.
A hybrid algorithm that consists of PSO and Legendre
pseudo-spectral method (LPM), namely PSO-LPM was
proposed in [127]. PSO-LPM was used to solve planning
problems. PSO-LPM starts the search process with the PSO
algorithm only and it switches to the LPM algorithm if it ﬁnds
that the change in the ﬁtness function has become smaller
than a predeﬁned value. This hybrid approach provides better
convergence speed and global search than both the separate
PSO and LPM. In addition, its performance is not affected by
random initialization. In [128], PSO was combined with the
levy ﬂight distribution method resulting in a new PSO variant
called levy ﬂight PSO (LFPSO). LFPSO alters the SPSO by
adding two new ideas. The ﬁrst idea is giving each particle
a limit value. In each iteration of LFPSO, if a particle does
not provide better solutions, the limit value is increased by
1. The second idea is using the Levy distribution method to
reallocate the positions of particles that have exceeded the
limit value. These two ideas aim to enhance the global search
capability and avoid premature convergence to local optima.
It has been demonstrated that LFPSO outperforms other PSO
variants including CLPSO and HPSO-TVAC as well as other
optimization methods like GA and DE.
d: OTHER HISTORICAL PSO VARIANTS
In [129], a modiﬁed PSO with time-varying acceleration
coefﬁcients (MPSO-TVAC) was presented. This algorithm
proposed a new parameter termed ‘rbest’ which provides
additional information to each particle. As a result, better
exploration is achieved leading to premature convergence
avoidance. In this method, each particle chooses any random
particle from Pbest of all particles, other than its own Pbest,
and it considers it as its own rbest. The velocity update
equation of this algorithm is given in the following form:
vid (t + 1) = vid (t) + c1r1 (Pbestid (t) −xid (t))
+ c2r2 (Gbestd (t) −xid (t))
+ c3r3 (rbestid (t) −xid (t))
(14)
where c3 is an acceleration constant which attracts each
particle to move in the direction of rbest, and r3 is a
uniform random value in the range [0, 1]. In MPSO-TVAC,
the acceleration coefﬁcients c1 and c2 are varied with time
and their formula is provided in [38] whereas the formula of
c3 is expressed as follows:
c3 = c1 (1 −exp (−c2t))
(15)
where t is the current iteration number.
In [130], a novel Gaussian PSO named Gaussian-
distributed PSO (GDPSO) was presented. In GDPSO,
the position of a particle is updated based on Gaussian
distribution. This method does not require parameter tuning
and its performance in solving high-dimension complex
functions is superior to Gaussian PSO (GPSO) [130].
Based on the grey relational analysis, Leu and Yeh [131]
proposed a PSO variant termed grey PSO. In each iteration
of grey PSO, each particle is assigned a unique inertia
weight, a cognitive component, and a social component.
This algorithm achieves faster convergence speed and better
solution accuracy as compared with PSO-LVIW [43], HPSO-
TVAC [38], and APSO [63].
The work in [132] proposed an enhanced PSO incorpo-
rating a weighted particle (EPSOWP). EPSOWP calculates a
weighted particle that guides the particles of a swarm towards
the optimal solution. Based on simulation results, EPSOWP
outperforms the SPSO, GA, and DE algorithms on some
selected benchmarking functions. In [133], a team-oriented
swarm optimization (TOSO) is proposed where the swarm is
divided into two teams. The role of the ﬁrst team is to perform
exploration while the second team performs exploitation. The
two teams interact with each other by sharing information
about Gbest. This PSO variant omits the need for the inertia
weight, cognitive coefﬁcient, and social coefﬁcient. Instead,
it relies on only one parameter known as mutation probability
(pm). Unlike most of the PSO variants, this variant was
tested in very high dimensions (up to 1000 dimension) cases.
Although TOSO has shown good performance for various
benchmarking functions, it still has drawbacks it terms of its
exploration capability.
To avoid the problem of the premature convergence of
SPSO while maintaining fast convergence, PSO with aging
leader and challengers (ALC-PSO) was presented in [35].
In ALC-PSO, the swarm’s leader possesses a lifespan that
can be adjusted by the leader’s leading power (stronger
leading power indicates longer life for the leader) and its
age increases with time. The other particles of the swarms
(challengers) have the chance to claim the leadership once
the leader has become old. The leader attracts other particles
if its leading power is high; otherwise, new particles are
allowed to compete to take the leadership. A median-
oriented PSO (MPSO) was introduced in [134] to avoid
becoming trapped in local optima and to accelerate the
convergence speed. In this approach, each particle updates its
velocity based on the current velocity and a median-oriented
acceleration. This variant omits the need for the inertia
weight w, cognitive coefﬁcient c1c1, and social coefﬁcient
c2c2. Another PSO variant called orthogonal learning PSO
(OLPSO) was proposed in [40]. This PSO variant uses
an orthogonal learning strategy for PSO to achieve faster
convergence speed and better solution quality. The role of
the orthogonal learning strategy is to let the particles move
in better directions. The results of OLPSO demonstrated its
superiority in terms of convergence speed and solution quality
as compared to the SPSO and some other PSO variants.
VOLUME 10, 2022
10043


---

<!-- Page 14 -->
## Page 14

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
FIGURE 1. Percentages of PSO publications from 1997 to 2021.
Figure 1 shows the percentages of PSO publications from
1997 to 2021.
IV. PSO IN DISCRETE SEARCH SPACE
Kennedy and Eberhart introduced the binary version of
PSO (BPSO) in [135]. The BPSO is applied to solve binary
problems where each dimension of a particle can have two
states only: 0 or 1. The values of 1 and 0 can have different
meanings such as true or false, yes or no, selected or not
selected, respectively. The updated velocity vid(t + 1) in
BPSO is the same as the updated velocity in the continuous
PSO but with restricting the values of Xi, Pbesti, and Gbest
to binary values. The result of vid(t + 1) is real continuous
values, though. The vid(t + 1) can be limited to have values
in the range of [0, 1] based on a transfer function. One of
the most common transfer functions is the sigmoidal function
which is given as follows:
sig (vid(t + 1)) =
1
1 + e−(vid(t+1))
(16)
Similar to PSO in continuous search space, a particle
updates its velocity in BPSO using Equation (1). In BPSO,
a particle updates its position based on a probabilistic
equation given by:
xid (t + 1) =
 0
if r4 ≥sig (vid(t + 1))
1
f r4 ≤sig (vid(t + 1))

(17)
where r4 is a uniformly distributed random value in the
interval [0, 1]. From Equation (17), it is observed that
sig (vid(t + 1)) becomes 0 when the value of vid(t +1) is less
than −10. At this state, the updated position xid (t + 1) will
remain 0 and no bit ﬂip will occur. Similarly, sig (vid(t + 1))
becomes 1 when the value of vid(t + 1) is greater than 10 and
the updated position xid (t + 1) will remain 1. In [135], it is
recommended to limit the velocity to ±6 where there will
be a probability of 0.0025 for bits to be ﬂipped. The work
presented in [136] recommended tighter values to limit the
velocity (±4).
Unlike the continuous PSO, only limited research efforts
have attempted to modify the standard BPSO to enhance
its performance. As discussed earlier, the velocity in BPSO
should be limited to ±6 or ±4. In [137], an essential binary
particle swarm optimization (EPSO) is proposed based on
the idea of omitting the velocity component of PSO. Thus,
there is no need to limit the velocity. The EPSO adopted the
concept of queen informants in ACO and applied it in PSO
resulting in a modiﬁed form of EPSO denoted as EPSOq.
In EPSOq, a new informer named the queen informer is added
where it is updated after each loop by Gbest only and its role
is to provide information to other particles. The EPSO and
EPSOq were applied to solve two suites of test functions and
EPSOq showed better performance in terms of convergence
rate and solution quality as compared to the standard BPSO
and EPSO. However, the results of EPSOq are not optimal.
To overcome the problem of nonlinearity that results from
the sigmoid function and the problem of the unusual behavior
of the probability function of a bit-change, an improved
binary particle swarm optimization (IBPSO) is proposed
in [138]. In IBPSO, the XOR and AND operators are
used in the velocity update equation vid(t + 1), and the
updated new position xid(t) depends on the current position.
Utilizing the genotype-phenotype concept, a modiﬁed binary
particle swarm optimization is introduced in [139]. In this
approach, the standard BPSO is modiﬁed by letting the
velocity and the position act as a particle and a solution.
The position in the velocity update equation is a phenotype
and the updated position equation is a genotype that depends
on the current phenotype’s position. This modiﬁed binary
version is evaluated on ten benchmarking functions and
the results have demonstrated that its performance is better
than the standard BPSO. A novel binary particle swarm
optimization (PBPSO) was proposed in [140] to address the
problem of the long time spent by the sigmoid function.
In [141], an adaptive mutation operator was added to the
PBPSO resulting in a new binary variant called adaptive
mutation PBPSO (AMPBPSO). In AMPBPSO, the new
binary position update is based on an adaptive mutation
probability which is evaluated by measuring the distance
between the new binary position and its best position. The
introduced adaptive mutation operator helps to maintain
diversity and enhance local search.
The BPSO ﬁnds some difﬁculties to converge to the
best solution because the binary positions are based on
randomness. In addition, BPSO suffers from becoming
trapped in local minima [135], [142]. A V-shaped transfer
function is used in [143] instead of using the S-shaped
transfer function to avoid unhealthy randomness. In [143],
the new binary position depends on the V-shaped transfer
function and it has three transition states: stays in its
current position, changes its value to 1, or changes its value
to 0. In this case, the randomness of binary positions is
reduced. Though this method is capable of reducing the
randomness of binary positions, it is incapable to solve
the problem of convergence to local minima. To avoid this
later problem, an enhancement to the work done in [143]
was proposed in [144] by adding a mutation operator. The
overall framework in [144] consists of a V-shaped transfer
10044
VOLUME 10, 2022


---

<!-- Page 15 -->
## Page 15

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
function, a new updating position formula, and a mutation
operator. This combination enhances the convergence rate
and diversity of particles and it also helps to escape from the
local minima problem.
In [145], six new S-shaped and V-shaped transfer functions
were introduced and tested on twenty-ﬁve benchmark
functions. Based on the results, the V-shaped family of
transfer functions outperforms the S-shaped family in terms
of the convergence rate and escaping from local minima.
Therefore, it is recommended to use the V-shape family,
particularly the V4 transfer function, to enhance the standard
BPSO performance.
In [146], the velocity update equation is modiﬁed to
have three different equations for the three different cases:
when Gbest
=
Pbesti
=
1, Gbest
=
Pbesti
=
0,
and Gbest ̸= Pbesti. The velocity increases if Gbest =
Pbesti = 1, decreases if Gbest = Pbesti = 0, and remains
unchanged when Gbest ̸= Pbesti. This is justiﬁable by the
consensus among Gbest and Pbesti in the ﬁrst two cases
whereas the third case lacks this consensus. The proposed
algorithm showed superior performance compared with other
BPSO variants. A hierarchical BPSO (BPSOHS) inspired
by multi-level learning behavior was proposed in [147].
Particles in the proposed approach are split into two groups:
leaders and followers. In BPSOHS, the leaders’ velocity and
position updates are the same as the standard BPSO while
the followers’ velocities and positions are updated based on
a random walk probability and a decision from the leaders.
The idea of this method is to enable followers to ﬂy towards
leaders and at the same time to explore an extensive region
near the leader space. Moreover, a mutation technique is
implemented in order to avoid premature convergence.
Utilizing the sigmoid transfer function, the author in [148]
proposed a new binary PSO version where the PSO
acceleration coefﬁcients are modiﬁed based on the ﬁtness
of each particle. The effectiveness of the proposed approach
was tested on four problems in the continuous search space
and its performance in optimizing binary problems is not
validated. In addition, the number of independent runs is
only 10 which is not enough to produce accurate results.
At least 30 independent runs are needed to validate the
performance of the proposed binary variant. Recently, the
work in [149] converted the gaining-sharing knowledge-
based continuous algorithm [150] into a novel binary PSO
variant where both algorithms are based on the idea of
gaining–sharing knowledge that humans experience during
their lifespan. The new binary variant is tested on twenty
two feature selection benchmark datasets and its performance
is compared with the standard binary PSO and other well-
known binary optimization algorithms such as binary GWO
and binary salp swarm algorithm. The proposed approach
was only tested on feature selection problems while its
performance of multi-dimensional knapsack problems is not
investigated. Thus, it would be interesting to study the
performance of this binary variant when it solves multi-
dimensional knapsack problems.
The work in [151] hybridized the binary PSO with the
sine cosine algorithm to solve feature selection problems.
A V-shaped transfer function is used and the performance
of the hybrid variant is compared with some well-known
binary PSO algorithms including the standard one as well
as with other high-performance binary algorithms such
as binary whale optimization algorithm and binary moth
ﬂame optimization algorithm. Although the hybrid approach
has shown good performance, all results are obtained for
10 independent runs only which is not enough to achieve high
accuracy. The authors in [152] developed a hybrid approach
that combines binary PSO with tabu search to solve the set-
union knapsack problem. The performance of this hybrid
approach on feature selection problems is not investigated
yet. Although [151] and [152] have achieved remarkable
performance, this achievement comes at the expense of
complexity.
A new binary PSO variant that is designed to solve feature
selection problems is proposed in [153]. The idea of the
proposed algorithm is to divide the entire population into sub-
swarms where each sub-swarm implements a unique inertia
weight strategy. Although the proposed approach has shown
better classiﬁcation performance compared with the binary
PSO, GA, and binary GSA, it requires more computational
time than the standard binary PSO. In [154], a time-varying
mirrored transfer function is proposed and its performance
is evaluated on CEC 2005 benchmark functions as well as
on 0-1 multidimensional knapsack problems. Results have
shown that the proposed transfer function outperforms the
S-Shaped and V-shaped transfer functions. The perfor-
mance of this new transfer function when used by other-
metaheuristic algorithms is not studied yet. Thus, more
research work is needed to further validate the effectiveness
of this mirrored transfer function. In addition, its performance
on feature selection problems needs to be investigated.
A. BPSO TRANSFER FUNCTIONS
The role of a transfer function is to map the velocity of a
certain dimension of a particle into the probability of bit
ﬂipping. According to [155], three rules must be followed
when selecting a transfer function:
• The probability of changing a bit from 0 to 1 or vice
versa must be high for large absolute values of velocities.
• The probability of unchanging a bit must be high for
small absolute values of velocities.
• The outcome of a transfer function should be in the range
of [0, 1] as it acts as a probabilistic function.
Some transfer functions have been proposed in the
literature such as the sigmoid function, the S-shaped family,
and the V-shaped family [145]. Table 4 lists the most common
transfer functions that can efﬁciently convert a continuous
search space into a binary one. The performance of binary
algorithms is highly dependent on the selection of the transfer
function. Thus, it is crucial to investigate the performance
of new binary variants when different transfer functions
are used to ﬁgure out which transfer function is the most
VOLUME 10, 2022
10045


---

<!-- Page 16 -->
## Page 16

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
TABLE 4. A summary of well-known transfer functions.
suitable for each variant. Some of the transfer functions
listed in Table 4 were originally proposed for binary meta-
heuristic algorithms and not binary PSO. However, they can
be implemented in binary PSO and their performance on
binary PSO is to be studied.
V. VALIDATION OF NEW PSO VARIANTS
This part focuses on the steps that are required to validate
the effectiveness of new PSO variants. These steps can be
summarized as follows:
1. Development of a novel approach based on new ideas,
parameter modiﬁcations, or hybridizations
The ﬁrst step when developing a novel PSO variant is
introducing new ideas particularly concepts that can help
to balance exploration and exploitation. The most common
concepts that help improve the performance of PSO are
modiﬁcation of controlling parameters particularly the inertia
weight, hybridizing PSO with other prominent meta-heuristic
algorithms, and multi-swarm approaches.
2. Testing the novel PSO variant on a wide range of
benchmarking functions
The next step is to validate the performance of the
new PSO variant to solve several unimodal, multimodal,
and composite benchmarking functions. The most common
classical benchmarking functions consist of twenty three
unimodal and multimodal functions that are widely used
by researchers [119], [145], [159], [160]. Although these
functions can validate the exploration and exploitation
abilities of a certain PSO variant, these functions do not fully
represent real-world optimization problems since they are
unconstrained problems. To represent real-world problems
that contain a number of constraints, the CEC2017 test suite
is introduced. Therefore, a strong PSO variant should be able
to provide signiﬁcant improvements when dealing with the
CEC2017. Other widely used benchmarking functions suites
are CEC2005 and CEC2019.
3. Testing the new PSO variant on real-world engineering
problems
This is a crucial step to demonstrate the effectiveness of a
proposed PSO variant. Real-world optimization problems are
challenging since they have a number of constraints that must
be satisﬁed. The introduction of constraints divides particles
into valid and invalid particles. A valid particle is a one
that can meet all constraints whereas a particle is considered
invalid if it violates one or more constraints. One of the most
common ways to penalize a particle when it does not satisfy
all constraints is to assign its ﬁtness a large value such as
1012 when solving a minimization problem. The most widely
used engineering problems that serve as benchmarks to test
the performance of a new optimization algorithm are welded
beam design, speed reducer design, pressure vessel design,
and tension/compression spring design.
4. Comparison with well-known PSO variants and other
meta-heuristic approaches
The fourth step is to compare the performance of the
developed PSO variant with other prominent PSO variants.
However, this is not enough as the performance of the new
PSO variant must be compared with other outstanding meta-
heuristic algorithms since their performance might be better
on a certain set of functions compared with existing PSO
variants.
5. High dimensional performance
A PSO variant might show strong performance when it
deals with low dimension problems; nevertheless, it may
have a poor performance when it solves high dimensional
problems. As a consequence, it is crucial to validate the effec-
tiveness of the new variant when it solves both low and high-
dimensional problems. The performance of a PSO variant
10046
VOLUME 10, 2022


---

<!-- Page 17 -->
## Page 17

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
usually degrades as the number of dimensions increases;
therefore, it is essential to investigate the performance of a
new PSO variant on high-dimensional problems.
6. Sensitivity analysis
PSO controlling parameters have a direct inﬂuence on
optimization performance. Some new PSO variants may add
new parameters besides the three controlling parameters of
the original PSO. Thus, it is crucial to provide a sensitivity
analysis that illustrates the inﬂuence of these parameters on
the performance of the new variant. In addition, it is important
to show which parameters are sensitive to different settings
and also show which parameters are robust.
7. Convergence analysis
Although the average ﬁtness and standard deviation are
two important metrics that help to validate the effectiveness
of an optimization algorithm, a convergence analysis is
required to further demonstrate the ability of an optimization
algorithm to escape from local optima and converge to a
global one.
8. Statistical signiﬁcance analysis
Statistical signiﬁcance analysis is an essential step that
needs to be performed to show that a new PSO variant is
statistically more signiﬁcant than other existing PSO variants
or meta-heuristic algorithms. In the literature, there have been
a signiﬁcant number of non-parametric statistical tests that
help to demonstrate the superiority of one algorithm over
others. Wilcoxon rank-sum test and Friedman test are the
most two common statistical tests that are used to evaluate
the performance of meta-heuristic algorithms.
VI. APPLICATIONS OF PSO
Due to its simplicity and robustness, PSO has been widely
used as an efﬁcient optimization tool for solving various
optimization problems in many real-world applications
such as feature selection, wireless communications, image
processing and electrical power systems. The following
present the applications of PSO in the aforementioned ﬁelds.
A. APPLICATIONS OF PSO TO FEATURE SELECTION
This part focuses on the applications of PSO on feature
selection problems. It starts with an introduction to feature
selection followed by a detailed explanation of how PSO
is applied to solve feature selection problems. Finally,
PSO-based feature selection studies are reviewed.
1) FEATURE SELECTION
Feature selection is a selection process that aims to select y
features from x original features (y < x) to optimize a certain
metric [161]–[163]. Feature selection is a crucial process
in machine learning and data mining as it can signiﬁcantly
help to remove unnecessary and redundant features [164].
For a large number of features, ﬁnding the optimal number
of features is a complicated problem [165]. Generally, the
selection of features is used for four reasons: simplifying data,
reducing computational time, avoiding the dimensionality
curse, and reducing overﬁtting. Figure 2 illustrates the
FIGURE 2. The general steps of feature selection.
feature selection process which goes through ﬁve steps:
initialization, generation, evaluation, stopping criteria, and
validation. In the initialization step, the number of all original
features represents the dimensionality of the search space.
The second step is responsible to select the best subset of
features. Various searching approaches such as conventional
schemes and meta-heuristic algorithms can be utilized to
perform this task. Typically, searching can start with no
features, all features, or a random selection of a subset of
features [166]–[168]. Selected subsets in the second step is
evaluated in step three to check their goodness. The fourth
step requires good stopping criteria that terminate when
good performance is achieved. The ﬁnal step validates the
effectiveness of the obtained subset of features on a test set.
Figure 3 shows the key factors of feature selection
which include searching algorithm, number of objectives,
and evaluations measures. The ﬁrst key factor of feature
selection is the searching algorithm that attempts to ﬁnd
the best subsets of features. Feature selection is an NP-hard
problem particularly for large datasets as it has 2n possible
solutions where n denotes the number of original features.
Thus, searching algorithms play an important role in solving
feature selection problems since they can achieve remarkable
performance with a signiﬁcant reduction in computational
time. The number of objectives represents the second key
factor where a single objective such as minimizing the
classiﬁcation error rate is considered or multiple objectives
such as minimizing the number of features and minimizing
the classiﬁcation error rate are taken into account. Evaluation
measures as the third key factor use an evaluation function
that can determine the strength and the drawbacks of the
selected subset which in turn help to guide the searching
algorithm.
Feature selection approaches can be classiﬁed into
two main categories: ﬁlter and wrapper methods [162],
[169], [170]. The main difference between the two is that
wrapper approaches implement a classiﬁcation algorithm to
VOLUME 10, 2022
10047


---

<!-- Page 18 -->
## Page 18

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
FIGURE 3. The three key factors of feature selection.
TABLE 5. A comparison between feature selection approaches.
evaluate the goodness of the selected features whereas ﬁlter
methods do not. As a consequence, wrapper approaches
achieve better performance [167], [169], [171], [172].
Some research work [167], [171], [172] adds the embed-
ded approach as a third category of feature selection
approaches. In the embedded approach, the classiﬁer and
the selected features are integrated. Table 5 shows the
strengths and drawbacks of the ﬁlter, wrapper, and embedded
approaches.
2) PSO FEATURE SELECTION MECHANISM
Feature selection is a binary optimization problem by nature.
To represent a solution that has the potential to solve the
feature selection problem, a vector with n features dimension
is needed where each element of a vector can have a value
of either 0 or 1. A value of 0 indicates that a feature is not
selected while 1 indicates the selection of the feature [3].
PSO can form a binary vector that can be used to solve the
feature selection problem. Optimization problems where their
variables are continuous values can be turned into a binary
optimization problem by replacing the continuous variables
with binary variables. PSO in its continuous version allows
candidate solutions to update their positions where each
variable can have a continuous value. In binary optimization,
a position is updated by converting its value from 0 to 1
or from 1 to 0. As a result, for PSO to be able to solve
feature selection problems, a transfer function is applied to
convert the real positions of candidate solutions into binary
ones [7]. Transfer functions rely on a probabilistic approach
to update binary values from 1 to 0 or from 0 to 1. Several
transfer functions have been proposed in the literature where
the S-Shaped and V-Shaped transfer functions are the most
common ones [19].
3) FEATURE SELECTION STUDIES BASED ON PSO
PSO has gained signiﬁcant consideration in the domain of
feature selection to solve different kinds of problems. For
example, the study in [173] proposed an improve BPSO
based on Lévy ﬂight as a local search component and inertia
weight coefﬁcient as a global search component as well as
mutation mechanism for population diversity enhancement.
The KNN classiﬁer for the classiﬁcation process and the
Sigmoid function are implemented for solution mappings.
Sixteen classical datasets were used for validation. The
ﬁndings showed promising performance compared to other
benchmarking methods.
In another study [174], the authors used the BPSO to
address the feature selection problem on input variables
for intelligence joint moment prediction. Experimental data
gathered from ten electromyography (EMG) data and six
joints’ angles were used for validation. ANN classiﬁer is
used for the classiﬁcation process and the Sigmoid function
is implemented for solution mappings. Findings showed
that the proposed approach is able to reduce the number
of input variables of ﬁve joint moments from 16 to less
than 11.
In [153], the authors proposed a co-evolution binary
particle swarm optimization with a multiple inertia weight
strategy. The KNN classiﬁer for the classiﬁcation process
and the Sigmoid transfer function were used to con-
vert the search space into a binary one. Ten benchmark
datasets collected from the UCI repository were used
for validation and the proposed method was compared
against four well-known feature selection methods. Findings
demonstrated a competitive performance compared to other
methods.
In [175], the BPSO was hybridized with differential
evolution to solve feature selection issues in EMG signals
classiﬁcation. The EMG signals of ten healthy subjects
obtained from a publicly accessible EMG database were used
for validation. Discrete wavelet transform was applied to
decompose signals into wavelet coefﬁcients. The sigmoid
transfer function was used to meet the nature of feature
selection and the KNN classiﬁer for the classiﬁcation
process. The performance of the proposed method was com-
pared against four benchmarking feature selection methods.
Findings demonstrated that the proposed method is beneﬁcial
for EMG signals classiﬁcation. In the same domain of EMG
signals classiﬁcation, the work in [176] proposed a new
personal best guide BPSO. The discrete wavelet transform
decomposes a signal into multiresolution coefﬁcients. The
sigmoid transfer function was used to meet the nature of
feature selection and the KNN classiﬁer for the classiﬁcation
process.
10048
VOLUME 10, 2022


---

<!-- Page 19 -->
## Page 19

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
Moreover, a study based on improved BPSO was proposed
in [177] to address the feature selection problems in
gene selection and cancer classiﬁcation. This approach
chooses a small dimensional set of prognostic genes to
classify biological samples of binary and multi-class cancers
using Naive–Bayes classiﬁer and Sigmoid transfer function
were used to meet the nature of feature selection. Eleven
microarray datasets of different cancer types were used
for validation. Experimental results were benchmarked with
seven other well-known methods and ﬁndings demonstrated a
better result of the proposed method in terms of classiﬁcation
accuracy and the number of selected genes.
A hybrid improved PSO with a shufﬂed frog leaping
algorithm was proposed in [178] to address the feature selec-
tion problem. Naive Bayes (NB), KNN, and Support Vector
Machine (SVM) classiﬁers were used for classiﬁcation and
the Sigmoid function was applied. For validation, a dataset
that consists of 1600 reviews of the 20 most popular Chicago
hotels were used. The ﬁndings revealed that the proposed
method attains an optimized feature subset and achieves
higher classiﬁcation accuracy. In another research [179], the
authors proposed a new multiswarm heterogeneous BPSO
using a Win-Win method to solve feature selection problems
in liver and kidney disease diagnosis.
In [180], Hamming distance is introduced as a proximity
measure that can update the binary PSO velocity and
select the important feature subsets. Experimental results on
three benchmark datasets are evaluated using classiﬁcation
accuracies and validity indices as well. Utilizing rough
set theory and its distinction table as a binary table, the
work in [181] proposed a hybrid binary PSO variant that
implements a statistical elimination strategy that can help to
reduce the number of features efﬁciently. The authors in [182]
developed a new multi-swarm PSO variant as a feature
optimization technique in facial recognition systems. Results
have demonstrated that the new PSO variant can signiﬁcantly
outperform the standard PSO and GA. To achieve better
accuracy, another study conducted by [183] proposed a
fuzzy rule-based binary PSO (FRBPSO) that is designed
speciﬁcally to solve feature selection problems. Results on
benchmarking high dimensional microarray datasets show
the merits of the proposed FRBPSO method.
Based on feature sub-set correlation, the authors in [184]
proposed a hybrid PSO with a new local search strategy
for feature selection. In the proposed approach, PSO is
designed to select features that have low correlation. Results
have shown that the proposed PSO achieves higher accuracy
compared with ﬁlter methods. Utilizing the SVM classiﬁer,
PSO is hybridized with GA in [185] as a wrapper feature
selection tool to classify microarray data. Considering
unreliable data in feature selection and based on bare-bones
PSO, a multi-objective PSO approach is proposed in [186].
The work in [187] hybridized PSO with GA to improve
feature selection in Digital Mammogram datasets. Utilizing
the KNN classiﬁer, Al-Tashi et al.. [188] proposed a hybrid
PSO with GWO for wrapper feature selection. This work has
used the sigmoid transfer function for converting the search
space into a binary one.
Multi-objective variants of PSO have been widely applied
to solve feature selection problems. For example, the authors
in [189] developed a PSO-based multi-objective approach
where features are ranked based on their frequency in the
set of archives. The proposed multi-objective scheme is
compared with three multi-objective PSO variants as well
a multi-objective GA on nine benchmark datasets. Results
have shown that the proposed approach is more efﬁcient
in reducing the number of features in large datasets while
it achieves a satisfactory performance that is close to the
performance achieved by other algorithms when it deals with
datasets that have lower than 100 attributes. Nonetheless,
the proposed approach suffers from slow convergence that
restricts reaching the optimum Pareto front. Another work
that utilizes multi-objective PSO is presented in [190] where
a two-step algorithm is proposed for fault diagnosis of
power transformers. The ﬁrst step is responsible to select
the most important features where the second step generates
an ensemble classiﬁer that is formed from the most accurate
classiﬁers. The work in [191] has developed a multi-objective
PSO feature selection approach to predict the dose of
warfarin. The authors in this work have applied artiﬁcial
neural networks as a technique to assess the selected features.
The developed multi-objective PSO approach is compared
with NSGA-II and results have demonstrated that PSO
outperforms NSGA-II in terms of accuracy and the minimum
number of features selected.
An improved multi-objective version of PSO is developed
in [192] to study multi-label feature selection. The authors
implemented an adaptive uniform mutation operator to
enhance the exploration abilities while a local learning
strategy is used to achieve better exploitation. Results
have shown that the proposed scheme performs better
than NSGA-II in terms of exploration. Based on the ﬁlter
approach, a multi-objective BPSO is proposed in [193] for
feature selection to obtain a non-dominated feature subset
that results in a reduction in the number of selected features
as well as higher classiﬁcation accuracy. The work presented
in [194] developed two multi-objective algorithms based
on PSO (NSPSOFS and CMDPSOFS) for solving feature
selection problems. The NSPSOFS algorithm is developed
based on the concept of nondominated sorting in NSGAII
to check the possibility of implementing a simple multi-
objective PSO to solve the problems of feature selection.
The second algorithm known as CMDPSOFS utilizes three
different techniques: mutation, dominance, and crowding.
Testing the two algorithms on twelve classical UCI repository
datasets, results have demonstrated the superiority of these
two algorithms in reducing the number of features and
decreasing the classiﬁcation error rate when compared with
NSGAII and the strength Pareto evolutionary algorithm 2
(SPEA2) [195] and Pareto archived evolutionary strategy
(PAES) [196]. Table 6 summarizes the existing studies on
feature selection using PSO and its variants.
VOLUME 10, 2022
10049


---

<!-- Page 20 -->
## Page 20

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
TABLE 6. A summary of feature selection approaches using PSO and its variants.
B. WIRELESS COMMUNICATIONS
PSO has been extensively applied to solve diverse wireless
communications optimization problems in different areas
such as wireless sensor networks (WSNs) [197]–[200],
cognitive radio networks (CRNs) [201]–[205], intelligent
reﬂecting surfaces (IRSs) systems [206], edge comput-
ing [207]–[209], ad-hoc networks [209], [210], [210]–[212],
signal
processing
[213]–[215]
and
antenna
design
[216]–[218]. PSO is used to tackle many WSNs challenges
such as node localization, optimal deployment and clustering.
A comprehensive survey on the applications of PSO in
WSNs is presented in [219]. Since spectrum sensing in
CRNs is a non-convex optimization problem, CRNs utilize
PSO algorithms to optimize their performance in terms
of energy efﬁciency, spectral efﬁciency and sensing time.
The work in [220] has implemented the standard PSO
algorithm to detect the presence of primary users. According
to the simulation results, PSO can save more than 80x
of energy consumption as well as sensing time. The
performance of the proposed scheme can be further improved
by applying enhanced PSO variants. A hybrid PSO-GSA
approach is used in [118] to optimize energy efﬁciency in 5G
CRNs. Results have shown that the proposed hybrid approach
is more energy efﬁcient than the standard PSO algorithm,
Artiﬁcial Bee Colony (ABC), the energy detector scheme and
the well-known cooperative spectrum sensing method.
In [206], PSO is used for beamforming optimization in
IRSs to minimize the transmission power given that the
signal-to-noise ratio (SNR) does not go below a certain
threshold. Results have demonstrated that PSO can achieve
10050
VOLUME 10, 2022


---

<!-- Page 21 -->
## Page 21

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
near- optimal beamforming solutions. Considering vehicular
ad-hoc networks, a task-distribution PSO is proposed to
efﬁciently distribute tasks among vehicles that belong to
the same cluster [221]. The results shows that the proposed
PSO scheme outperforms GA in terms of overhead reduction
while its overhead performance is comparable with linear
programing. In [210], an adaptive PSO is developed to solve
the clustering problem in ad-hoc networks.
One of the interesting and recent applications of PSO
in the wireless domain is edge computing where intensive
computational tasks are ofﬂoaded from core networks to
the edge that is closer to the user. Considering a smart
internet of things (IoT) system, a self-adaptive PSO algorithm
that utilizes the GA operators (SPSO-GA) is recently
proposed [207] to develop an energy-efﬁcient approach that
can efﬁciently make ofﬂoading decisions for deep neural
networks (DNNs) layers with layer partition operations.
Simulation results have shown that the SPSO-GA algorithm
outperforms the GA and PSO-GA approaches in terms
of energy consumption. The authors in [208] applied a
PSO-GA algorithm to minimize the system cost when
DNN layers are ofﬂoaded over the cloud, edge and user’s
devices. According to the results, the proposed PSO-GA can
signiﬁcantly reduce the system cost compared with PSO and
GA. Combining edge computing and cloud computing, the
work in [209] implemented the BPSO algorithm with the GA
operators to minimize data transmission time when the
workﬂow is executed. Although the results have shown the
superiority of the proposed approach in reducing data
transmission time, data transmission energy is not considered.
The works in [207]–[209] can be further improved by
applying the recent high-performance PSO variants presented
in Section III.
Considering a ﬁnite impulse response (FIR) ﬁlter, the
authors in [222] applied a quantum-behaved PSO algorithm
to develop an adaptive channel equalizer. Based on the
results, the proposed approach achieves a lower bit error
rate compared with GA, SPSO, and the classical least
mean square method. The SPSO algorithm and its variants
are also applied to design inﬁnite impulse response (IIR)
ﬁlters [213]–[215]. Another application of PSO in the
wireless communications ﬁeld is antenna array design. In a
massive multiple-input multiple-output (MIMO) network, a
contraction adaptive PSO algorithm is proposed in [216] to
ﬁnd the optimal positions of antenna array elements that
can optimize an antenna’s performance when it transmits
or receives data. Although the proposed approach has
shown good results, its performance is compared with PSO
variants only. It is evident from the state-of-the-art presented
in this subsection that most of the work has considered
single- objective optimization. In wireless communications,
it is crucial to consider multiple objectives such as energy
efﬁciency, spectral efﬁciency, and latency to develop a robust
and reliable communication system. Therefore, it is essential
to develop novel multi-objective PSO algorithms that takes
several wireless metrics into account.
C. IMAGE PROCESSING
PSO has been successfully applied to solve many image
processing optimization problems in diverse areas such as
image segmentation [223]–[225], image enhancement [226],
image compression [227] and image watermarking [228].
One of the recent and interesting applications of PSO
in image processing is multilevel thresholding image seg-
mentation. The work in [223] modiﬁed the standard PSO
algorithm to perform image threshold segmentation in lung
CT images where the aim is to identify lung tissue. In the
proposed scheme, the symmetric disposition is implemented
to adjust the positions of particles in each iteration. Although
this work has shown fast segmentation speed as well as
good segmentation accuracy, its performance is tested only
on one lung CT image. In [224], PSO is used to segment
medical images to detect brain tumors. This work can be
further improved by applying recent robust PSO variants or
other well-known meta-heuristic algorithms such as GWO
and Equilibrium Optimizer (EO). Considering multilevel
image thresholding, the work in [225] hybridized PSO with
the ﬁreﬂy algorithm (FA) [229] to search for the optimal
threshold values. Based on the results, the proposed hybrid
scheme outperforms GA, PSO, and FA in terms of peak-
signal-to-noise-ratio (PSNR).
In the area of image enhancement, PSO is utilized in [226]
to address the inaccurate nature of retinal images. The
effectiveness of the proposed approach is validated on two
well-known image datasets and results have shown that
PSO can signiﬁcantly enhance the quality of retinal images
compared with GA, ACO, and ABC. The authors in [227]
have proposed to use PSO with Haar Wavelet Transform to
compress medial images. The simulation results have shown
that the proposed scheme can achieve high PSNR which
indicates that the quality of compressed images is close the
quality of original images. In [228], PSO is used with an
intertwining logistic map to develop a blind watermarking
scheme. Testing the proposed method on eight classical
grayscale images, results have shown that PSO can efﬁciently
optimize watermark embedding strength.
D. ELECTRICAL POWER SYSTEMS
PSO has been widely applied to optimize the perfor-
mance of electrical power systems including economic
dispatch [230]–[232], optimal power ﬂow [233]–[235], state
estimation [236], power system controllers [237], [238],
unit commitment [239] and capacitor placement [240].
A detailed and thorough survey on the applications of
PSO in electrical power systems is provided in [241].
The survey focused on ten areas including optimal power
ﬂow, economic dispatch, reactive power dispatch, and
maintenance scheduling. Recently, the works in [242], [243]
have provided a comprehensive review of the applications of
PSO and its variants on the economic dispatch problem. The
authors in [239] have recently reviewed the state-of-the-art
applications of PSO to solve the unit commitment problems.
VOLUME 10, 2022
10051


---

<!-- Page 22 -->
## Page 22

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
According to [239], most of the PSO-based unit commitment
research has considered single-objective optimization that
minimizes cost only while multi-objective optimization that
jointly minimizes cost and emission is not well studied yet.
The work in [240] applied a hybrid ABC-PSO algorithm
in an IEEE 34-node and 69-node radial distribution networks
to ﬁnd the best capacitor placement and size that can help
to reduce power loss. The proposed technique can achieve
lower power loss when compared with the individual PSO
and ABC algorithms; nevertheless, its performance is not
compared with high-performance PSO variants as well as
with other well-known meta-heuristic algorithms such as
GWO and whale optimization algorithm (WOA). The work
in [236] hybridized PSO with gravitational search algorithm
to solve the problem of state estimation in distribution
systems. Results have shown that the proposed hybrid scheme
is more accurate and reliable than the standard PSO algorithm
and the original GSA approach.
Table 7 summarizes the major applications of PSO, shows
the type of PSO used and the major publications for each
application. It is observed from Table 7 that each application
is associated with a different PSO variant which indicates that
there is no dominant PSO variant that can solve most of the
optimization problems. In other words, each PSO variant is
specialized in solving speciﬁc problems.
VII. PSO DRAWBACKS
Despite the excellent performance of its variants, PSO
suffers, in general, from some weaknesses that can be
alleviated by introducing new modiﬁcations to the current
PSO variants. The literature reports several concerns about
PSO performance which can be outlined as follows:
A. PREMATURE CONVERGENCE
One of the major performance problems of PSO is pre-
mature convergence as pointed out in [38], [276]. This
problem occurs due to the lack of population diversity
especially in complex multimodal functions [38]. The work
in [35], [69], [277] presented important PSO variants that
have shown remarkable performance in terms of avoiding
premature convergence. Nevertheless, much more research is
needed to address this problem.
B. THE DIFFICULTY OF CONTROLING THE PSO
PARAMETERS
Although there are only three parameters (c1, c2, w) to be
controlled in PSO, it is difﬁcult to control these parameters
and ﬁnd their appropriate setting at each iteration. Despite
the extensive efforts of proposing several methods to control
c1, c2 and w none of these methods guarantee that the optimal
setting of c1, c2 and w can be achieved.
C. IMPROPER VELOCITY ADJUSTMENT
The improper velocity adjustment occurs when inappropriate
values of c1, c2 and w are chosen. This makes the particles
ﬂy in undesired directions, causing stagnation around or near
the optimum solution [278].
VIII. POTENTIAL RESEARCH DIRECTIONS
Although PSO variants have shown promising results in
solving optimization problems, PSO can still be developed
further to improve its performance when applied to solve
complex real-world optimization problems. The following
provides some potential future directions to be considered by
researchers who are interested in PSO and its applications:
1) The original PSO and its recent variants presented
in Section III can be hybridized with other recent high-
performance metaheuristic algorithms such as Equilib-
rium optimizer (EO) [279], Marine Predators Algorithm
(MPA) [280], Gradient-based optimizer (GBO) [281], Polit-
ical Optimizer (PO) [282], The Arithmetic Optimization
Algorithm (AOA) [283], and Archimedes optimization
algorithm [284].
2) The recent PSO variants presented in Section III can
be converted into binary PSO algorithms and utilized to
solve binary problems such as feature selection and the 0-1
knapsack problem.
3) Some of the binary PSO variants presented in Section IV
are applied to feature selection only while others are applied
to solve the 0-1 knapsack problem. It would be interesting to
apply each recent binary PSO variant to solve both problems
and evaluate the performance.
4) Some of the binary transfer functions presented in
Table 4 have not been investigated and could be utilized to
test the performance of PSO using such transfer functions.
5) The performance of PSO variants on high-dimensional
problems is not well studied yet. The performance of
recent PSO variants on high-dimensional problems can be
investigated. In addition, Further work is needed to develop
new PSO variants that can perform well on low and high-
dimensional problems.
6) The development of new PSO variants that can solve
multi-objective problems is a promising research direction to
be considered.
7) Recent PSO variants can be applied to solve a wide
range of real-world optimization problems such as data
clustering [285], maintenance scheduling [286], lot-sizing
optimization [287], [288], supply-chain network optimiza-
tion [289], [290].
8) One promising research direction is to hybridize
wrapper approaches that implements PSO variants with ﬁlter
methods to solve feature selection problems.
IX. CONCLUSION
PSO is a simple, robust, and fast optimizer that can solve
complex real-world optimization problems. To overcome the
limitations of the standard PSO, extensive research efforts
have been exerted to modify the original PSO algorithm
into better variants by applying several methods including
controlling the PSO parameters, hybridizing PSO with other
searching algorithms, and using multi-swarm techniques.
10052
VOLUME 10, 2022


---

<!-- Page 23 -->
## Page 23

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
TABLE 7. A summary of PSO applications in various engineering fields
VOLUME 10, 2022
10053


---

<!-- Page 24 -->
## Page 24

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
This work presents an overall review of the distinct research
works that have been conducted on PSO. The review starts
by explaining the basic concepts of PSO. Then, it describes
the different topologies that can be used in PSO, provides a
comprehensive review of the recent and historical prominent
PSO variants. The review also includes PSO in binary
presentation, remarkable engineering applications of PSO,
and drawbacks of PSO. More speciﬁcally, this review
paper has focused on PSO-based feature selection. Finally,
this work provides some potential research directions that
can help researchers further enhance the performance of
PSO. In a nutshell, there are still rooms for improvement
in PSO development to provide better performance when
applied to complex high-dimensional real-world optimization
problems.
REFERENCES
[1] J. Kennedy and R. Eberhart, ‘‘Particle swarm optimization,’’ in Proc. Int.
Conf. Neural Netw. (ICNN), vol. 4, 1995, pp. 1942–1948.
[2] M. Dorigo, M. Birattari, and T. Stutzle, ‘‘Ant colony optimization,’’ IEEE
Comput. Intell. Mag., vol. 1, no. 4, pp. 28–39, Nov. 2006.
[3] J. Holland, Adaptation in Natural and Artiﬁcial Systems. Ann Arbor, MI,
USA: Univ. of Michigan, 1975.
[4] R. Storn and K. Price, ‘‘Differential evolution-a simple and efﬁcient
heuristic for global optimization over continuous spaces,’’ J. Global
Optim., vol. 11, no. 4, pp. 341–359, Dec. 1997.
[5] A. M. Eltamaly, ‘‘A novel strategy for optimal PSO control parameters
determination for PV energy systems,’’ Sustainability, vol. 13, no. 2,
p. 1008, Jan. 2021.
[6] K. R. Harrison, A. P. Engelbrecht, and B. M. Ombuki-Berman, ‘‘Optimal
parameter regions and the time-dependence of control parameter values
for the particle swarm optimization algorithm,’’ Swarm Evol. Comput.,
vol. 41, pp. 20–35, Aug. 2018.
[7] M. Hajihassani, D. J. Armaghani, and R. Kalatehjari, ‘‘Applications of
particle swarm optimization in geotechnical engineering: A comprehen-
sive review,’’ Geotech. Geol. Eng., vol. 36, no. 2, pp. 705–722, Apr. 2018.
[8] A. H. Elsheikh and M. A. Elaziz, ‘‘Review on applications of particle
swarm optimization in solar energy systems,’’ Int. J. Environ. Sci.
Technol., vol. 16, no. 2, pp. 1159–1170, Feb. 2019.
[9] M. R. Bonyadi and Z. Michalewicz, ‘‘Particle swarm optimization for
single objective continuous space problems: A review,’’ Evol. Comput.,
vol. 25, no. 1, pp. 1–54, Mar. 2017.
[10] A. R. Jordehi and J. Jasni, ‘‘Particle swarm optimisation for discrete
optimisation problems: A review,’’ Artif. Intell. Rev., vol. 43, no. 2,
pp. 243–258, 2015.
[11] A. Khare and S. Rangnekar, ‘‘A review of particle swarm optimization
and its applications in solar photovoltaic system,’’ Appl. Soft Comput.,
vol. 13, no. 5, pp. 2997–3006, May 2013.
[12] N. K. Jain, U. Nangia, and J. Jain, ‘‘A review of particle swarm
optimization,’’ J. Inst. Eng., vol. 99, no. 4, pp. 407–411, Mar. 2018.
[13] T. V. Sibalija, ‘‘Particle swarm optimisation in designing parameters of
manufacturing processes: A review (2008–2018),’’ Appl. Soft Comput.,
vol. 84, Nov. 2019, Art. no. 105743.
[14] B. Xin, J. Chen, J. Zhang, H. Fang, and Z.-H. Peng, ‘‘Hybridizing
differential evolution and particle swarm optimization to design powerful
optimizers: A review and taxonomy,’’ IEEE Trans. Syst., Man, Cybern.
C, Appl. Rev., vol. 42, no. 5, pp. 744–767, Sep. 2012.
[15] S. Rana, S. Jasola, and R. Kumar, ‘‘A review on particle swarm
optimization algorithms and their applications to data clustering,’’ Artif.
Intell. Rev., vol. 35, no. 3, pp. 211–222, Mar. 2011.
[16] A. R. Jordehi, ‘‘Particle swarm optimisation (PSO) for allocation of
FACTS devices in electric transmission systems: A review,’’ Renew.
Sustain. Energy Rev., vol. 52, pp. 1260–1267, Dec. 2015.
[17] M.-P. Song and G.-C. Gu, ‘‘Research on particle swarm optimization:
A review,’’ in Proc. Int. Conf. Mach. Learn. Cybern., vol. 4, 2004,
pp. 2236–2241.
[18] M. Juneja and S. K. Nagar, ‘‘Particle swarm optimization algorithm and
its parameters: A review,’’ in Proc. Int. Conf. Control, Comput., Commun.
Mater. (ICCCCM), Oct. 2016, pp. 1–5.
[19] A. A. A. Esmin, R. A. Coelho, and S. Matwin, ‘‘A review on particle
swarm optimization algorithm and its variants to clustering high-
dimensional data,’’ Artif. Intell. Rev., vol. 44, no. 1, pp. 23–45, 2015.
[20] W. Fang, J. Sun, Y. Ding, X. Wu, and W. Xu, ‘‘A review of quantum-
behaved particle swarm optimization,’’ IETE Tech. Rev., vol. 27, no. 4,
pp. 336–348, 2010.
[21] D. P. Tian, ‘‘A review of convergence analysis of particle swarm
optimization,’’ Int. J. Grid Distrib. Comput., vol. 6, no. 6, pp. 117–128,
Dec. 2013.
[22] N. K. Kulkarni, S. Patekar, T. Bhoskar, O. Kulkarni, G. Kakandikar,
and V. M. Nandedkar, ‘‘Particle swarm optimization applications to
mechanical engineering—A review,’’ Mater. Today, Proc., vol. 2,
nos. 4–5, pp. 2631–2639, 2015.
[23] A. J. Rezaee, ‘‘Particle swarm optimisation for dynamic optimisation
problems: A review,’’ Neural Comput., vol. 25, nos. 7–8, pp. 1507–1516,
2014.
[24] A. R. Jordehi, ‘‘A review on constraint handling strategies in par-
ticle swarm optimisation,’’ Neural Comput. Appl., vol. 26, no. 6,
pp. 1265–1275, Aug. 2015.
[25] A. P. Engelbrecht, ‘‘Particle swarm optimization with crossover: A review
and empirical analysis,’’ Artif. Intell. Rev., vol. 45, no. 2, pp. 131–165,
Feb. 2016.
[26] S. Sengupta, S. Basak, and R. A. Peters, ‘‘Particle swarm optimization:
A survey of historical and recent developments with hybridization per-
spectives,’’ Mach. Learn. Knowl. Extraction, vol. 1, no. 1, pp. 157–191,
2019.
[27] A. Banks, J. Vincent, and C. Anyakoha, ‘‘A review of particle swarm
optimization. Part I: Background and development,’’ Natural Comput.,
vol. 6, no. 4, pp. 467–484, Oct. 2007.
[28] A. Banks, J. Vincent, and C. Anyakoha, ‘‘A review of particle swarm
optimization. Part II: Hybridisation, combinatorial, multicriteria and
constrained optimization, and indicative applications,’’ Natural Comput.,
vol. 7, no. 1, pp. 109–124, Mar. 2008.
[29] R. C. Eberhart, P. K. Simpson, R. Dobbins, and R. W. Dobbins,
Computational Intelligence PC Tools. USA: AP Professional, 1996.
[30] A.
P.
Engelbrecht,
Computational
Intelligence:
An
Introduction.
Hoboken, NJ, USA: Wiley, 2007.
[31] M. Ghasemi, E. Akbari, A. Rahimnejad, S. E. Razavi, S. Ghavidel, and
L. Li, ‘‘Phasor particle swarm optimization: A simple and efﬁcient variant
of PSO,’’ Soft Comput., vol. 23, no. 19, pp. 9701–9718, Oct. 2019.
[32] F. Van den Bergh and A. P. Engelbrecht, ‘‘Effects of swarm size on
cooperative particle swarm optimisers,’’ in Proc. 3rd Annu. Conf. Genet.
Evol. Comput., 2001, pp. 892–899.
[33] N. Himanshu and A. Burman, ‘‘Determination of critical failure surface of
slopes using particle swarm optimization technique considering seepage
and seismic loading,’’ Geotech. Geol. Eng., vol. 37, no. 3, pp. 1261–1281,
Jun. 2019.
[34] G. A. F. Alfarisy, W. F. Mahmudy, and M. H. Natsir, ‘‘Optimizing laying
hen diet using multi-swarm particle swarm optimization,’’ Telkomnika,
vol. 16, no. 4, pp. 1712–1723, 2018.
[35] W.-N. Chen, J. Zhang, Y. Lin, N. Chen, Z.-H. Zhan, H. S.-H. Chung,
Y. Li, and Y.-H. Shi, ‘‘Particle swarm optimization with an aging leader
and challengers,’’ IEEE Trans. Evol. Comput., vol. 17, no. 2, pp. 241–258,
Apr. 2013.
[36] A. P. Piotrowski, J. J. Napiorkowski, and A. E. Piotrowska, ‘‘Population
size in particle swarm optimization,’’ Swarm Evol. Comput., vol. 58,
Nov. 2020, Art. no. 100718.
[37] D. Wang, D. Tan, and L. Liu, ‘‘Particle swarm optimization algorithm:
An overview,’’ Soft Comput., vol. 22, no. 2, pp. 387–408, 2018.
[38] A. Ratnaweera, S. K. Halgamuge, and H. C. Watson, ‘‘Self-organizing
hierarchical particle swarm optimizer with time-varying acceleration
coefﬁcients,’’ IEEE Trans. Evol. Comput., vol. 8, no. 3, pp. 240–255,
Jun. 2004.
[39] Z. Beheshti and S. M. H. Shamsuddin, ‘‘CAPSO: Centripetal accelerated
particle swarm optimization,’’ Inf. Sci., vol. 258, pp. 54–79, Feb. 2014.
[40] Z.-H. Zhan, J. Zhang, Y. Li, and Y.-H. Shi, ‘‘Orthogonal learning
particle swarm optimization,’’ IEEE Trans. Evol. Comput., vol. 15, no. 6,
pp. 832–847, Dec. 2011.
[41] E. Koessler and A. Almomani, ‘‘Hybrid particle swarm optimization
and pattern search algorithm,’’ Optim. Eng., vol. 22, pp. 1539–1555,
Jul. 2020.
10054
VOLUME 10, 2022


---

<!-- Page 25 -->
## Page 25

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
[42] Z. Yang and A. Wu, ‘‘A non-revisiting quantum-behaved particle swarm
optimization based multilevel thresholding for image segmentation,’’
Neural Comput. Appl., vol. 32, no. 16, pp. 12011–12031, Aug. 2020.
[43] Y. Shi and R. Eberhart, ‘‘A modiﬁed particle swarm optimizer,’’ in Proc.
IEEE Int. Conf. Evol. Comput., IEEE World Congr. Comput. Intell.,
May 1998, pp. 69–73.
[44] M. Clerc and J. Kennedy, ‘‘The particle swarm—Explosion, stability, and
convergence in a multidimensional complex space,’’ IEEE Trans. Evol.
Comput., vol. 6, no. 1, pp. 58–73, Feb. 2002.
[45] M. Li, H. Chen, X. Shi, S. Liu, M. Zhang, and S. Lu, ‘‘A multi-information
fusion ‘triple variables with iteration’ inertia weight PSO algorithm and
its application,’’ Appl. Soft Comput., vol. 84, Nov. 2019, Art. no. 105677.
[46] Y. Shi and R. C. Eberhart, ‘‘Empirical study of particle swarm
optimization,’’ in Proc. Congr. Evol. Comput. (CEC), vol. 3, 1999,
p. 1950.
[47] H.-G. Beyer and H.-P. Schwefel, ‘‘Evolution strategies—A comprehen-
sive introduction,’’ Natural Comput., vol. 1, no. 1, pp. 3–52, 2002.
[48] A. Nickabadi, M. M. Ebadzadeh, and R. Safabakhsh, ‘‘A novel particle
swarm optimization algorithm with adaptive inertia weight,’’ Appl. Soft
Comput., vol. 11, no. 4, pp. 3658–3670, Jun. 2011.
[49] R. C. Eberhart and Y. Shi, ‘‘Tracking and optimizing dynamic systems
with particle swarms,’’ in Proc. Congr. Evol. Comput., vol. 1, 2001,
pp. 94–100.
[50] K. Lee and J.-B. Park, ‘‘Application of particle swarm optimization to
economic dispatch problem: Advantages and disadvantages,’’ in Proc.
PES Power Syst. Conf. Expo. (PSCE), 2006, pp. 188–192.
[51] B. Jiao, Z. Lian, and X. Gu, ‘‘A dynamic inertia weight particle
swarm optimization algorithm,’’ Chaos, Solitons Fractals, vol. 37, no. 3,
pp. 698–705, Aug. 2008.
[52] S.-K.-S. Fan and Y.-Y. Chiu, ‘‘A decreasing inertia weight particle swarm
optimizer,’’ Eng. Optim., vol. 39, no. 2, pp. 203–228, Mar. 2007.
[53] A. Chatterjee and P. Siarry, ‘‘Nonlinear inertia weight variation for
dynamic adaptation in particle swarm optimization,’’ Comput. Oper. Res.,
vol. 33, no. 3, pp. 859–871, Mar. 2006.
[54] G. Chen, X. Huang, J. Jia, and Z. Min, ‘‘Natural exponential inertia weight
strategy in particle swarm optimization,’’ in Proc. 6th World Congr. Intell.
Control Automat. (WCICA), vol. 1, 2006, pp. 3672–3675.
[55] H.-R. Li and Y.-L. Gao, ‘‘Particle swarm optimization algorithm with
exponent decreasing inertia weight and stochastic mutation,’’ in Proc. 2nd
Int. Conf. Inf. Comput. Sci. (ICIC), vol. 1, 2009, pp. 66–69.
[56] J. Lu, H. Hu, and Y. Bai, ‘‘Radial basis function neural network
based on an improved exponential decreasing inertia weight-particle
swarm optimization algorithm for AQI prediction,’’ Abstract Appl. Anal.,
vol. 2014, pp. 1–9, Jul. 2014.
[57] Y. Feng, G.-F. Teng, A.-X. Wang, and Y.-M. Yao, ‘‘Chaotic inertia weight
in particle swarm optimization,’’ in Proc. 2nd Int. Conf. Innov. Comput.,
Inf. Control (ICICIC), Sep. 2007, p. 475.
[58] X. Yang, J. Yuan, J. Yuan, and H. Mao, ‘‘A modiﬁed particle swarm
optimizer with dynamic adaptation,’’ Appl. Math. Comput., vol. 189,
no. 2, pp. 1205–1213, 2007.
[59] B. K. Panigrahi, V. R. Pandi, and S. Das, ‘‘Adaptive particle swarm
optimization approach for static and dynamic economic load dispatch,’’
Energy Convers. Manage., vol. 49, no. 6, pp. 1407–1415, Jun. 2008.
[60] K. Suresh, S. Ghosh, D. Kundu, A. Sen, S. Das, and A. Abraham, ‘‘Inertia-
adaptive particle swarm optimizer for improved global search,’’ in Proc.
8th Int. Conf. Intell. Syst. Design Appl. (ISDA), Nov. 2008, pp. 253–258.
[61] K. Lei, Y. Qiu, and Y. He, ‘‘A new adaptive well-chosen inertia weight
strategy to automatically harmonize global and local search ability in
particle swarm optimization,’’ in Proc. 1st Int. Symp. Syst. Control Aerosp.
Astronaut. (ISSCAA), 2006, p. 980.
[62] M. S. Arumugam and M. V. C. Rao, ‘‘On the improved performances
of the particle swarm optimization algorithms with adaptive parameters,
cross-over operators and root mean square (RMS) variants for computing
optimal control of a class of hybrid systems,’’ Appl. Soft Comput., vol. 8,
no. 1, pp. 324–336, Jan. 2008.
[63] Z.-H. Zhan, J. Zhang, Y. Li, and H. S.-H. Chung, ‘‘Adaptive particle
swarm optimization,’’ IEEE Trans. Syst., Man, Cybern. B, Cybern.,
vol. 39, no. 6, pp. 1362–1381, Dec. 2009.
[64] J. Kennedy, ‘‘Small worlds and mega-minds: Effects of neighborhood
topology on particle swarm performance,’’ in Proc. Congr. Evol. Comput.,
vol. 3, 1999, p. 1938.
[65] R. Mendes, J. Kennedy, and J. Neves, ‘‘The fully informed particle
swarm: Simpler, maybe better,’’ IEEE Trans. Evol. Comput., vol. 8, no. 3,
pp. 204–210, Jun. 2004.
[66] J. Kennedy and R. Mendes, ‘‘Population structure and particle swarm
performance,’’ in Proc. Congr. Evol. Comput. (CEC), vol. 2, 2002,
pp. 1671–1676.
[67] P. N. Suganthan, ‘‘Particle swarm optimiser with neighbourhood opera-
tor,’’ in Proc. Congr. Evol. Comput. (CEC), vol. 3, 1999, pp. 1958–1962.
[68] M. Nasir, S. Das, D. Maity, S. Sengupta, U. Halder, and P. N. Suganthan,
‘‘A dynamic neighborhood learning based particle swarm optimizer for
global numerical optimization,’’ Inf. Sci., vol. 209, pp. 16–36, Nov. 2012.
[69] J. J. Liang, A. K. Qin, P. N. Suganthan, and S. Baskar, ‘‘Comprehensive
learning particle swarm optimizer for global optimization of multimodal
functions,’’ IEEE Trans. Evol. Comput., vol. 10, no. 3, pp. 281–295,
Jun. 2006.
[70] A. Godoy and F. J. Von Zuben, ‘‘A complex neighborhood based particle
swarm optimization,’’ in Proc. IEEE Congr. Evol. Comput. (CEC),
May 2009, pp. 720–727.
[71] K. E. Parsopoulos and M. N. Vrahatis, ‘‘Uniﬁed particle swarm
optimization in dynamic environments,’’ in Applications of Evolu-
tionary Computing (Lecture Notes in Computer Science), vol. 3449,
F. Rothlauf, Eds. Berlin, Germany: Springer, 2005, pp. 590–599.
[72] R. Mendes, J. Kennedy, and J. Neves, ‘‘Watch thy neighbor or how the
swarm can learn from its environment,’’ in Proc. IEEE Swarm Intell.
Symp. (SIS), Apr. 2003, pp. 88–94.
[73] Y. Xu and D. Pi, ‘‘A reinforcement learning-based communication
topology in particle swarm optimization,’’ Neural Comput. Appl., vol. 32,
pp. 10007–10032, Jul. 2020.
[74] H. Zhang, M. Yuan, Y. Liang, and Q. Liao, ‘‘A novel particle swarm
optimization based on prey–predator relationship,’’ Appl. Soft Comput.,
vol. 68, pp. 202–218, Jul. 2018.
[75] W. Ye, W. Feng, and S. Fan, ‘‘A novel multi-swarm particle swarm
optimization with dynamic learning strategy,’’ Appl. Soft Comput.,
vol. 61, pp. 832–843, Dec. 2017.
[76] J. Gou, Y. X. Lei, W. P. Guo, C. Wang, Y. Q. Cai, and W. Liu, ‘‘A novel
improved particle swarm optimization algorithm based on individual
difference evolution,’’ Appl. Soft. Comput., vol. 57, pp. 468–481,
Aug. 2017.
[77] Y. Chen, L. Li, H. Peng, J. Xiao, Y. Yang, and Y. Shi, ‘‘Particle swarm
optimizer with two differential mutation,’’ Appl. Soft Comput., vol. 61,
pp. 314–330, Dec. 2017.
[78] W. Liu, Z. Wang, Y. Yuan, N. Zeng, K. Hone, and X. Liu, ‘‘A novel
sigmoid-function-based adaptive weighted particle swarm optimizer,’’
IEEE Trans. Cybern., vol. 51, no. 2, pp. 1085–1093, Feb. 2021.
[79] X. Zhang, X. Wang, Q. Kang, and J. Cheng, ‘‘Differential mutation and
novel social learning particle swarm optimization algorithm,’’ Inf. Sci.,
vol. 480, pp. 109–129, Apr. 2019.
[80] M. Kohler, M. M. B. R. Vellasco, and R. Tanscheit, ‘‘PSO+: A new
particle swarm optimization algorithm for constrained problems,’’ Appl.
Soft Comput., vol. 85, Dec. 2019, Art. no. 105865.
[81] W. Li, X. Meng, Y. Huang, and Z.-H. Fu, ‘‘Multipopulation cooperative
particle swarm optimization with a mixed mutation strategy,’’ Inf. Sci.,
vol. 529, pp. 179–196, Aug. 2020.
[82] D. Sedighizadeh, E. Masehian, M. Sedighizadeh, and H. Akbaripour,
‘‘GEPSO: A new generalized particle swarm optimization algorithm,’’
Math. Comput. Simul., vol. 179, pp. 194–212, Jan. 2021.
[83] K. Chen, B. Xue, M. Zhang, and F. Zhou, ‘‘Novel chaotic grouping
particle swarm optimization with a dynamic regrouping strategy for
solving numerical optimization tasks,’’ Knowl.-Based Syst., vol. 194,
Apr. 2020, Art. no. 105568.
[84] J. T. Machado, S. M. A. Pahnehkolaei, and A. Alﬁ, ‘‘Complex-order
particle swarm optimization,’’ Commun. Nonlinear Sci. Numer. Simul.,
vol. 92, Jan. 2021, Art. no. 105448.
[85] X. Xia, L. Gui, G. He, B. Wei, Y. Zhang, F. Yu, H. Wu, and Z.-H. Zhan,
‘‘An expanded particle swarm optimization based on multi-exemplar and
forgetting ability,’’ Inf. Sci., vol. 508, pp. 105–120, Jan. 2020.
[86] N. Lynn and P. N. Suganthan, ‘‘Ensemble particle swarm optimizer,’’
Appl. Soft Comput., vol. 55, pp. 533–548, Jun. 2017.
[87] Y. Shi and R. C. Eberhart, ‘‘Empirical study of particle swarm
optimization,’’ in Proc. Congr. Evol. Comput. (CEC), vol. 3, 1999,
pp. 1945–1950.
[88] B. Y. Qu, P. N. Suganthan, and S. Das, ‘‘A distance-based locally informed
particle swarm model for multimodal optimization,’’ IEEE Trans. Evol.
Comput., vol. 17, no. 3, pp. 387–402, Jun. 2013.
[89] T. Peram, K. Veeramachaneni, and C. K. Mohan, ‘‘Fitness-distance-ratio
based particle swarm optimization,’’ in Proc. IEEE Swarm Intell. Symp.
(SIS), Apr. 2003, pp. 174–181.
VOLUME 10, 2022
10055


---

<!-- Page 26 -->
## Page 26

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
[90] N. M. Laskar, K. Guha, I. Chatterjee, S. Chanda, K. L. Baishnab, and
P. K. Paul, ‘‘HWPSO: A new hybrid whale-particle swarm optimization
algorithm and its application in electronic design optimization problems,’’
Appl. Intell., vol. 49, no. 1, pp. 265–291, Jan. 2019.
[91] F. Wang, H. Zhang, K. Li, Z. Lin, J. Yang, and X. Shen, ‘‘A hybrid particle
swarm optimization algorithm using adaptive learning strategy,’’ Inf. Sci.,
vol. 436, pp. 162–177, Apr. 2018.
[92] K. Chen, F. Zhou, S. Wang, Y. Wang, F. Wan, and L. Yin, ‘‘A hybrid
particle swarm optimizer with sine cosine acceleration coefﬁcients,’’ Inf.
Sci., vol. 422, pp. 218–241, Jan. 2018.
[93] M.
Karimi-Mamaghan,
M.
Mohammadi,
P.
Meyer,
A. M. Karimi-Mamaghan, and E.-G. Talbi, ‘‘Machine learning at
the service of meta-heuristics for solving combinatorial optimization
problems: A state-of-the-art,’’ Eur. J. Oper. Res., vol. 296, no. 2,
pp. 393–422, Jan. 2022.
[94] M. A. Potter and K. A. De Jong, ‘‘A cooperative coevolutionary approach
to function optimization,’’ in Parallel Problem Solving From Nature—
PPSN III. Berlin, Germany: Springer, 1994, pp. 249–257.
[95] F. van den Bergh and A. P. Engelbrecht, ‘‘A cooperative approach to
particle swarm optimization,’’ IEEE Trans. Evol. Comput., vol. 8, no. 3,
pp. 225–239, Jun. 2004.
[96] R.-Y. Wang, Y.-T. Hsiao, and W.-P. Lee, ‘‘A new cooperative particle
swarm optimizer with dimension partition and adaptive velocity control,’’
in Proc. IEEE Int. Conf. Syst., Man, Cybern. (SMC), Oct. 2012,
pp. 103–109.
[97] L. Wang, ‘‘An improved cooperative particle swarm optimizer,’’ Telecom-
mun. Syst., vol. 53, no. 1, pp. 147–154, May 2013.
[98] B. Niu, Y. Zhu, H. Wu, and X. He, ‘‘MCPSO: A multi-swarm cooperative
particle swarm optimizer,’’ Appl. Math. Comput., vol. 185, no. 2,
pp. 1050–1062, 2007.
[99] H. Rau, S. D. Budiman, and G. A. Widyadana, ‘‘Optimization of the
multi-objective green cyclical inventory routing problem using discrete
multi-swarm PSO method,’’ Transp. Res. E, Logistics Transp. Rev.,
vol. 120, pp. 51–75, Dec. 2018.
[100] J. Zhang and X. Ding, ‘‘A multi-swarm self-adaptive and cooperative
particle swarm optimization,’’ Eng. Appl. Artif. Intell., vol. 24, no. 6,
pp. 958–967, 2011.
[101] C.-H. Chen and Y.-Y. Liao, ‘‘Tribal particle swarm optimization for
neurofuzzy inference systems and its prediction applications,’’ Commun.
Nonlinear Sci. Numer. Simul., vol. 19, no. 4, pp. 914–929, Apr. 2014.
[102] J. H. Holland, Adaptation in Natural and Artiﬁcial Systems: An Intro-
ductory Analysis With Applications to Biology, Control, and Artiﬁcial
Intelligence. Ann Arbor, MI, USA: Univ. of Michigan, 1975.
[103] Y.-T. Kao and E. Zahara, ‘‘A hybrid genetic algorithm and particle swarm
optimization for multimodal functions,’’ Appl. Soft Comput., vol. 8, no. 2,
pp. 849–857, 2008.
[104] R. Chelouah and P. Siarry, ‘‘A continuous genetic algorithm designed for
the global optimization of multimodal functions,’’ J. Heuristics, vol. 6,
no. 2, pp. 191–213, Jun. 2000.
[105] S.-K. S. Fan, Y.-C. Liang, and E. Zahara, ‘‘Hybrid simplex search and
particle swarm optimization for the global optimization of multimodal
functions,’’ Eng. Optim., vol. 36, no. 4, pp. 401–418, Aug. 2004.
[106] J. Robinson, S. Sinton, and Y. Rahmat-Samii, ‘‘Particle swarm, genetic
algorithm, and their hybrids: Optimization of a proﬁled corrugated horn
antenna,’’ in Proc. IEEE Antennas Propag. Soc. Int. Symp., vol. 1,
Jun. 2002, pp. 314–317.
[107] Z. Chai, A. Nwachukwu, Y. Zagayevskiy, S. Amini, and S. Madasu,
‘‘An integrated closed-loop solution to assisted history matching and ﬁeld
optimization with machine learning techniques,’’ J. Petroleum Sci. Eng.,
vol. 198, Mar. 2021, Art. no. 108204.
[108] N. M. Isa, A. L. Bukar, T. C. Wei, and A. Marwanto, ‘‘Optimal sizing of
hybrid fuel cell and PV employing hybrid PSO-GA,’’ in Proc. IEEE Conf.
Energy Convers. (CENCON), Oct. 2019, pp. 159–164.
[109] R. Storn and K. Price, ‘‘Differential evolution—A simple and efﬁcient
adaptive scheme for global optimization over continuous spaces,’’ ICSI
Berkeley, Berkeley, CA, USA, Tech. Rep. TR-95-012, 1995.
[110] S. Sayah and A. Hamouda, ‘‘A hybrid differential evolution algorithm
based on particle swarm optimization for nonconvex economic dispatch
problems,’’ Appl. Soft Comput., vol. 13, no. 4, pp. 1608–1619, 2013.
[111] H. M. Elragal, M. A. Mangoud, and M. T. Alsharaa, ‘‘Hybrid differential
evolution and enhanced particle swarm optimisation technique for
design of reconﬁgurable phased antenna arrays,’’ IET Microw., Antennas
Propag., vol. 5, no. 11, pp. 1280–1287, 2011.
[112] M. G. Epitropakis, V. P. Plagianakos, and M. N. Vrahatis, ‘‘Evolving
cognitive and social experience in particle swarm optimization through
differential evolution: A hybrid approach,’’ Inf. Sci., vol. 216, pp. 50–92,
Dec. 2012.
[113] A. Sedki and D. Ouazar, ‘‘Hybrid particle swarm optimization and
differential evolution for optimal design of water distribution systems,’’
Adv. Eng. Informat., vol. 26, no. 3, pp. 582–591, Aug. 2012.
[114] M. Pant, R. Thangaraj, C. Grosan, and A. Abraham, ‘‘Hybrid differential
evolution—Particle swarm optimization algorithm for solving global
optimization problems,’’ in Proc. 3rd Int. Conf. Digit. Inf. Manage.
(ICDIM), Nov. 2008, pp. 18–24.
[115] Y. Fu, M. Ding, C. Zhou, and H. Hu, ‘‘Route planning for unmanned
aerial vehicle (UAV) on the sea using hybrid differential evolution and
quantum-behaved particle swarm optimization,’’ IEEE Trans. Syst., Man,
Cybern., Syst., vol. 43, no. 6, pp. 1451–1465, Nov. 2013.
[116] J. Sun, B. Feng, and W. Xu, ‘‘Particle swarm optimization with particles
having quantum behavior,’’ in Proc. Congr. Evol. Comput., vol. 1, 2004,
pp. 325–331.
[117] M. S. Kıran, M. Gündüz, and Ö. K. Baykan, ‘‘A novel hybrid algorithm
based on particle swarm and ant colony optimization for ﬁnding the
global minimum,’’ Appl. Math. Comput., vol. 219, no. 4, pp. 1515–1521,
Nov. 2012.
[118] G. Eappen and T. J. Shankar, ‘‘Hybrid PSO-GSA for energy efﬁcient
spectrum sensing in cognitive radio network,’’ Phys. Commun., vol. 40,
Jun. 2020, Art. no. 101091.
[119] S. Mirjalili, S. M. Mirjalili, and A. Lewis, ‘‘Grey wolf optimizer,’’ Adv.
Eng. Softw., vol. 69, pp. 46–61, Mar. 2014.
[120] P. J. Van Laarhoven and E. H. Aarts, ‘‘Simulated annealing,’’ in
Simulated Annealing: Theory and Applications. Dordrecht, The Nether-
lands: Springer, 1987, pp. 7–15.
[121] X. Pan, L. Xue, Y. Lu, and N. Sun, ‘‘Hybrid particle swarm optimization
with simulated annealing,’’ Multimedia Tools Appl., vol. 78, no. 21,
pp. 29921–29936, Nov. 2019.
[122] J. Rangaraj and M. Anitha, ‘‘Implementing energy optimization by a
novel hybrid technique for performance improvement in mobile ad hoc
network,’’ Int. J. Appl. Eng. Res., vol. 12, no. 22, pp. 12029–12035, 2017.
[123] O. M. Kamel, A. A. Z. Diab, T. D. Do, and M. A. Mossa, ‘‘A
novel hybrid ant colony-particle swarm optimization techniques based
tuning STATCOM for grid code compliance,’’ IEEE Access, vol. 8,
pp. 41566–41587, 2020.
[124] H. Suyono, E. Subekti, H. Purnomo, T. Nurwati, and R. N. Hasanah,
‘‘Economic dispatch of 500 kV Java–Bali power system using hybrid
particle swarm-ant colony optimization method,’’ in Proc. 12th Int. Conf.
Electr. Eng. (ICEENG), Jul. 2020, pp. 5–10.
[125] S. Jiang, Z. Ji, and Y. Shen, ‘‘A novel hybrid particle swarm optimization
and gravitational search algorithm for solving economic emission load
dispatch problems with various practical constraints,’’ Int. J. Electr. Power
Energy Syst., vol. 55, pp. 628–644, Feb. 2014.
[126] H.-C. Tsai, Y.-Y. Tyan, Y.-W. Wu, and Y.-H. Lin, ‘‘Gravitational
particle swarm,’’ Appl. Math. Comput., vol. 219, no. 17, pp. 9106–9117,
May 2013.
[127] Y. Zhuang and H. Huang, ‘‘Time-optimal trajectory planning for
underactuated spacecraft using a hybrid particle swarm optimization
algorithm,’’ Acta Astronaut., vol. 94, no. 2, pp. 690–698, Feb. 2014.
[128] H. Haklı and H. Uˇguz, ‘‘A novel particle swarm optimization algorithm
with Levy ﬂight,’’ Appl. Soft Comput., vol. 23, pp. 333–345, Oct. 2014.
[129] M. N. Abdullah, A. H. A. Bakar, N. A. Rahim, H. Mokhlis, H. A. Illias,
and J. J. Jamian, ‘‘Modiﬁed particle swarm optimization with time
varying acceleration coefﬁcients for economic load dispatch with
generator constraints,’’ J. Electr. Eng. Technol., vol. 9, no. 1, pp. 15–26,
Jan. 2014.
[130] J.-W. Lee and J.-J. Lee, ‘‘Gaussian-distributed particle swarm optimiza-
tion: A novel Gaussian particle swarm optimization,’’ in Proc. IEEE Int.
Conf. Ind. Technol. (ICIT), Feb. 2013, pp. 1122–1127.
[131] M.-S. Leu and M.-F. Yeh, ‘‘Grey particle swarm optimization,’’ Appl. Soft
Comput., vol. 12, no. 9, pp. 2985–2996, Sep. 2012.
[132] N.-J. Li, W.-J. Wang, C.-C. J. Hsu, W. Chang, H.-G. Chou, and
J.-W. Chang, ‘‘Enhanced particle swarm optimizer incorporating a
weighted particle,’’ Neurocomputing, vol. 124, pp. 218–227, Jan. 2014.
[133] F. M. F. Haﬁz and A. Abdennour, ‘‘A team-oriented approach to particle
swarms,’’ Appl. Soft Comput., vol. 13, no. 9, pp. 3776–3791, Sep. 2013.
[134] Z. Beheshti, S. M. H. Shamsuddin, and S. Hasan, ‘‘MPSO: Median-
oriented particle swarm optimization,’’ Appl. Math. Comput., vol. 219,
no. 11, pp. 5817–5836, Feb. 2013.
10056
VOLUME 10, 2022


---

<!-- Page 27 -->
## Page 27

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
[135] J. Kennedy and R. C. Eberhart, ‘‘A discrete binary version of the particle
swarm algorithm,’’ in Proc. IEEE Int. Conf. Syst., Man, Cybern. Comput.
Cybern. Simulation, vol. 5, Oct. 1997, pp. 4104–4108.
[136] N. Tawalbeh, H. M. Abusamaha, and A. Al-Salaymeh, ‘‘Domestic
appliances scheduling using BPSO and IoT,’’ in Proc. IEEE PES Innov.
Smart Grid Technol. Eur. (ISGT-Europe), Sep. 2019, pp. 1–5.
[137] E. Chen, J. Li, and X. Liu, ‘‘In search of the essential binary discrete
particle swarm,’’ Appl. Soft Comput., vol. 11, no. 3, pp. 3260–3269,
Apr. 2011.
[138] X. Yuan, H. Nie, A. Su, L. Wang, and Y. Yuan, ‘‘An improved binary
particle swarm optimization for unit commitment problem,’’ Expert Syst.
Appl., vol. 36, no. 4, pp. 8049–8055, May 2009.
[139] S. Lee, S. Soak, S. Oh, W. Pedrycz, and M. Jeon, ‘‘Modiﬁed binary
particle swarm optimization,’’ Prog. Natural Sci., vol. 18, no. 9,
pp. 1161–1166, Sep. 2008.
[140] L. Wang, X. Wang, J. Fu, and L. Zhen, ‘‘A novel probability binary
particle swarm optimization algorithm and its application,’’ J. Softw.,
vol. 3, no. 9, pp. 28–35, Dec. 2008.
[141] L. Wang, X. Fu, J. Fang, H. Wang, and M. Fei, ‘‘Optimal node placement
in industrial wireless sensor networks using adaptive mutation probability
binary particle swarm optimization algorithm,’’ in Proc. 7th Int. Conf.
Natural Comput., Jul. 2011, pp. 2199–2203.
[142] I. M. Swesi and A. A. Bakar, ‘‘An enhanced binary particle swarm
optimization (EBPSO) algorithm based a V-shaped transfer function for
feature selection in high dimensional data,’’ Int. J. Adv. Soft Comput.
Appl., vol. 9, no. 3, pp. 1–22, 2017.
[143] J. H. Liu, R. H. Yang, and S. H. Sun, ‘‘The analysis of binary particle
swarm optimization,’’ J. Nanjing Univ., Natural Sci., vol. 47, no. 5,
pp. 504–514, Sep. 2011.
[144] J. Yang, H. Zhang, Y. Ling, C. Pan, and W. Sun, ‘‘Task allocation
for wireless sensor network using modiﬁed binary particle swarm
optimization,’’ IEEE Sensors J., vol. 14, no. 3, pp. 882–892, Mar. 2014.
[145] S. Mirjalili and A. Lewis, ‘‘S-shaped versus V-shaped transfer functions
for binary particle swarm optimization,’’ Swarm Evol. Comput., vol. 9,
pp. 1–14, Apr. 2013.
[146] A. H. El-Maleh, A. T. Sheikh, and S. M. Sait, ‘‘Binary particle swarm
optimization (BPSO) based state assignment for area minimization of
sequential circuits,’’ Appl. Soft Comput., vol. 13, no. 12, pp. 4832–4840,
Dec. 2013.
[147] W. Bin, P. Qinke, Z. Jing, and C. Xiao, ‘‘A binary particle swarm
optimization algorithm inspired by multi-level organizational learning
behavior,’’ Eur. J. Oper. Res., vol. 219, no. 2, pp. 224–233, Jun. 2012.
[148] Y. Mehmood, M. Sadiq, W. Shahzad, and F. Amin, ‘‘Fitness-based
acceleration coefﬁcients to enhance the convergence speed of novel
binary particle swarm optimization,’’ in Proc. Int. Conf. Frontiers Inf.
Technol. (FIT), Dec. 2018, pp. 355–360.
[149] P. Agrawal, T. Ganesh, and A. W. Mohamed, ‘‘A novel binary gaining–
sharing knowledge-based optimization algorithm for feature selection,’’
Neural Comput. Appl., vol. 33, no. 11, pp. 5989–6008, 2021.
[150] A. W. Mohamed, A. A. Hadi, and A. K. Mohamed, ‘‘Gaining-sharing
knowledge based algorithm for solving optimization problems: A novel
nature-inspired algorithm,’’ Int. J. Mach. Learn. Cybern., vol. 11,
pp. 1501–1529, Jul. 2020.
[151] L. Kumar and K. K. Bharti, ‘‘A novel hybrid BPSO–SCA approach
for feature selection,’’ Natural Comput., vol. 20, no. 1, pp. 39–61,
2021.
[152] G. Lin, J. Guan, Z. Li, and H. Feng, ‘‘A hybrid binary particle swarm
optimization with Tabu search for the set-union knapsack problem,’’
Expert Syst. Appl., vol. 135, pp. 201–211, Nov. 2019.
[153] J. Too, A. R. Abdullah, and N. M. Saad, ‘‘A new co-evolution binary
particle swarm optimization with multiple inertia weight strategy for
feature selection,’’ Informatics, vol. 6, no. 2, p. 21, May 2019.
[154] Z. Beheshti, ‘‘A time-varying mirrored S-shaped transfer function for
binary particle swarm optimization,’’ Inf. Sci., vol. 512, pp. 1503–1542,
Feb. 2020.
[155] E. Rashedi, H. Nezamabadi-Pourand, and S. Saryazdi, ‘‘BGSA: Binary
gravitational search algorithm,’’ Natural Comput., vol. 9, no. 3,
pp. 727–745, Sep. 2010.
[156] M. J. Islam, X. Li, and Y. Mei, ‘‘A time-varying transfer function for
balancing the exploration and exploitation ability of a binary PSO,’’ Appl.
Soft Comput., vol. 59, pp. 182–196, Oct. 2017.
[157] Z. Beheshti, ‘‘A novel x-shaped binary particle swarm optimization,’’ Soft
Comput., vol. 25, no. 4, pp. 3013–3042, Feb. 2021.
[158] S. Mirjalili, H. Zhang, S. Mirjalili, S. Chalup, and N. Noman, ‘‘A novel
U-shaped transfer function for binary particle swarm optimisation,’’ in
Proc. 9th Int. Conf. Soft Comput. Problem Solving (SocProS). Liverpool,
U.K.: Springer, 2020, pp. 241–259.
[159] S. Mirjalili and A. Lewis, ‘‘The whale optimization algorithm,’’ Adv. Eng.
Softw., vol. 95, pp. 51–67, Feb. 2016.
[160] J. G. Digalakis and K. G. Margaritis, ‘‘On benchmarking functions for
genetic algorithms,’’ Int. J. Comput. Math., vol. 77, no. 4, pp. 481–506,
Sep. 2001.
[161] P. M. Narendra and K. Fukunaga, ‘‘A branch and bound algorithm
for feature subset selection,’’ IEEE Trans. Comput., vol. C-26, no. 9,
pp. 917–922, Sep. 1977.
[162] B. H. Nguyen, B. Xue, and M. Zhang, ‘‘A survey on swarm intelligence
approaches to feature selection in data mining,’’ Swarm Evol. Comput.,
vol. 54, May 2020, Art. no. 100663.
[163] Q. Al-Tashi, H. M. Rais, S. J. Abdulkadir, S. Mirjalili, and H. Alhussian,
‘‘A review of grey wolf optimizer-based feature selection methods
for classiﬁcation,’’ in Evolutionary Machine Learning Techniques.
Singapore: Springer, 2020, pp. 273–286.
[164] Q. Al-Tashi, H. M. Rais, S. J. Abdulkadir, and S. Mirjalili, ‘‘Feature
selection based on grey wolf optimizer for oil & gas reservoir
classiﬁcation,’’ in Proc. Int. Conf. Comput. Intell. (ICCI), Oct. 2020,
pp. 211–216.
[165] Q. Al-Tashi, H. Rais, and S. Jadid, ‘‘Feature selection method based
on grey wolf optimization for coronary artery disease classiﬁcation,’’ in
Proc. Int. Conf. Reliable Inf. Commun. Technol. Kuala Lumpur, Malaysia:
Springer, 2018, pp. 257–266.
[166] P. Langley, ‘‘Selection of relevant features in machine learning,’’ in Proc.
AAAI Fall Symp. Relevance, vol. 184, 1994, pp. 245–271.
[167] E. Hancer, B. Xue, and M. Zhang, ‘‘A survey on feature selec-
tion approaches for clustering,’’ Artif. Intell. Rev., vol. 53, no. 6,
pp. 4519–4545, Aug. 2020.
[168] A. Mukhopadhyay, U. Maulik, S. Bandyopadhyay, and C. A. C. Coello,
‘‘A survey of multiobjective evolutionary algorithms for data mining:
Part I,’’ IEEE Trans. Evol. Comput., vol. 18, no. 1, pp. 4–19, Feb. 2014.
[169] M. Dash and H. Liu, ‘‘Feature selection for classiﬁcation,’’ Intell. Data
Anal., vol. 1, nos. 1–4, pp. 131–156, 1997.
[170] I. Guyon and A. Elisseeff, ‘‘An introduction to variable and feature
selection,’’ J. Mach. Learn. Res., vol. 3, pp. 1157–1182, May 2003.
[171] H. Liu and Z. Zhao, ‘‘Manipulating data and dimension reduction
methods: Feature selection,’’ in Computational Complexity: Theory,
Techniques, and Applications. New York, NY, USA: Springer, 2012,
pp. 1790–1800.
[172] H. Liu, H. Motoda, R. Setiono, and Z. Zhao, ‘‘Feature selection: An ever
evolving frontier in data mining,’’ in Proc. Feature Selection Data Mining,
2010, pp. 4–13.
[173] B. Ji, X. Lu, G. Sun, W. Zhang, J. Li, and Y. Xiao, ‘‘Bio-inspired feature
selection: An improved binary particle swarm optimization approach,’’
IEEE Access, vol. 8, pp. 85989–86002, 2020.
[174] B. Xiong, Y. Li, M. Huang, W. Shi, M. Du, and Y. Yang, ‘‘Feature
selection of input variables for intelligence joint moment prediction
based on binary particle swarm optimization,’’ IEEE Access, vol. 7,
pp. 182289–182295, 2019.
[175] J. Too, A. R. Abdullah, and N. Mohd Saad, ‘‘Hybrid binary particle
swarm optimization differential evolution-based feature selection for
EMG signals classiﬁcation,’’ Axioms, vol. 8, no. 3, p. 79, Jul. 2019.
[176] J. Too, A. Abdullah, N. M. Saad, and W. Tee, ‘‘EMG feature selection and
classiﬁcation using a Pbest-guide binary particle swarm optimization,’’
Computation, vol. 7, no. 1, p. 12, Feb. 2019.
[177] I. Jain, V. K. Jain, and R. Jain, ‘‘Correlation feature selection based
improved-binary particle swarm optimization for gene selection and can-
cer classiﬁcation,’’ Appl. Soft Comput., vol. 62, pp. 203–215, Jan. 2018.
[178] S. P. Rajamohana and K. Umamaheswari, ‘‘Hybrid approach of improved
binary particle swarm optimization and shufﬂed frog leaping for feature
selection,’’ Comput. Electr. Eng., vol. 67, pp. 497–508, Apr. 2018.
[179] S. Gunasundari, S. Janakiraman, and S. Meenambal, ‘‘Multiswarm
heterogeneous binary PSO using win-win approach for improved feature
selection in liver and kidney disease diagnosis,’’ Comput. Med. Imag.
Graph., vol. 70, pp. 135–154, Dec. 2018.
[180] H. Banka and S. Dara, ‘‘A Hamming distance based binary particle
swarm optimization (HDBPSO) algorithm for high dimensional feature
selection, classiﬁcation and validation,’’ Pattern Recognit. Lett., vol. 52,
pp. 94–100, Jan. 2015.
VOLUME 10, 2022
10057


---

<!-- Page 28 -->
## Page 28

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
[181] S. Dara, H. Banka, and C. S. R. Annavarapu, ‘‘A rough based hybrid
binary PSO algorithm for ﬂat feature selection and classiﬁcation in gene
expression data,’’ Ann. Data Sci., vol. 4, no. 3, pp. 341–360, Sep. 2017.
[182] K. Mistry, L. Zhang, S. C. Neoh, C. P. Lim, and B. Fielding, ‘‘A micro-GA
embedded PSO feature selection approach to intelligent facial emotion
recognition,’’ IEEE Trans. Cybern., vol. 47, no. 6, pp. 1496–1509,
Jun. 2017.
[183] S. Agarwal, R. Rajesh, and P. Ranjan, ‘‘FRBPSO: A fuzzy rule based
binary PSO for feature selection,’’ Proc. Nat. Acad. Sci., India A, Phys.
Sci., vol. 87, no. 2, pp. 221–233, Jun. 2017.
[184] P. Moradi and M. Gholampour, ‘‘A hybrid particle swarm optimization
for feature subset selection by integrating a novel local search strategy,’’
Appl. Soft. Comput., vol. 43, pp. 117–130, Jun. 2016.
[185] E.-G. Talbi, L. Jourdan, J. Garcia-Nieto, and E. Alba, ‘‘Comparison
of population based metaheuristics for feature selection: Application to
microarray data classiﬁcation,’’ in Proc. IEEE/ACS Int. Conf. Comput.
Syst. Appl., Mar./Apr. 2008, pp. 45–52.
[186] Z. Yong, G. Dun-Wei, and Z. Wan-Qiu, ‘‘Feature selection of unreliable
data using an improved multi-objective PSO algorithm,’’ Neurocomput-
ing, vol. 171, pp. 1281–1290, Jan. 2016.
[187] J. Jona and N. Nagaveni, ‘‘A hybrid swarm optimization approach for
feature set reduction in digital mammograms,’’ WSEAS Trans. Inf. Sci.
Appl., vol. 9, no. 11, pp. 340–349, 2012.
[188] Q. Al-Tashi, S. J. A. Kadir, H. M. Rais, S. Mirjalili, and H. Alhussian,
‘‘Binary optimization using hybrid grey wolf optimization for feature
selection,’’ IEEE Access, vol. 7, pp. 39496–39508, 2019.
[189] M. Amoozegar and B. Minaei-Bidgoli, ‘‘Optimizing multi-objective PSO
based feature selection method using a feature elitism mechanism,’’
Expert Syst. Appl., vol. 113, pp. 499–514, Dec. 2018.
[190] A. Peimankar, S. J. Weddell, T. Jalal, and A. C. Lapthorn, ‘‘Evolutionary
multi-objective fault diagnosis of power transformers,’’ Swarm Evol.
Comput., vol. 36, pp. 62–75, Oct. 2017.
[191] M. K. Sohrabi and A. Tajik, ‘‘Multi-objective feature selection for
warfarin dose prediction,’’ Comput. Biol. Chem., vol. 69, pp. 126–133,
Aug. 2017.
[192] Y. Zhang, D.-W. Gong, X.-Y. Sun, and Y.-N. Guo, ‘‘A PSO-based multi-
objective multi-label feature selection method in classiﬁcation,’’ Sci.
Rep., vol. 7, no. 376, pp. 1–12, Mar. 2017.
[193] B. Xue, L. Cervante, L. Shang, W. N. Browne, and M. Zhang, ‘‘A multi-
objective particle swarm optimisation for ﬁlter-based feature selection in
classiﬁcation problems,’’ Connection Sci., vol. 24, nos. 2–3, pp. 91–116,
Sep. 2012.
[194] B. Xue, M. Zhang, and W. N. Browne, ‘‘Particle swarm optimization
for feature selection in classiﬁcation: A multi-objective approach,’’ IEEE
Trans. Cybern., vol. 43, no. 6, pp. 1656–1671, Dec. 2013.
[195] E. Zitzler, M. Laumanns, and L. Thiele, ‘‘SPEA2: Improving the strength
Pareto evolutionary algorithm,’’ Eidgenössische Technische Hochschule
Zürich (ETH), Institut für Technische Informatik Kommunikationsnetze
(TIK), Zürich, Switzerland, TIK-Rep. 004284029, 2001, vol. 103.
[196] J. Knowles and D. Corne, ‘‘The Pareto archived evolution strategy: A
new baseline algorithm for Pareto multiobjective optimisation,’’ in Proc.
Congr. Evol. Comput. (CEC), vol. 1, 1999, pp. 98–105.
[197] B. Xia, T. Liu, T. Ding, and Z. Wang, ‘‘An improved PSO localization
algorithm for UWB sensor networks,’’ Wireless Pers. Commun., vol. 117,
no. 3, pp. 2207–2223, Apr. 2021.
[198] Y. Hu, Y. Ding, and K. Hao, ‘‘An immune cooperative particle
swarm optimization algorithm for fault-tolerant routing optimization
in heterogeneous wireless sensor networks,’’ Math. Problems Eng.,
vol. 2012, Dec. 2012, Art. no. 743728.
[199] Z.-H. Zhan, J. Zhang, K.-J. Du, and J. Xiao, ‘‘Extended binary particle
swarm optimization approach for disjoint set covers problem in wireless
sensor networks,’’ in Proc. Conf. Technol. Appl. Artif. Intell., Nov. 2012,
pp. 327–331.
[200] Y.-M. Zhao and A. Lu, ‘‘Application of adaptive chaos PSO algorithm
in WSN coverage optimization,’’ Commun. Technol., vol. 1, no. 1, p. 10,
2018.
[201] Z.-J. Teng, L.-Y. Xie, H.-L. Chen, and H. Zhang, ‘‘Application research
of chaotic binary particle swarm optimization algorithm in dynamic
spectrum allocation,’’ J. Comput., vol. 31, no. 4, pp. 288–299, 2020.
[202] A. H. Mahdi, J. Mohanan, M. A. Kalil, and A. Mitschele-Thiel, ‘‘Adaptive
discrete particle swarm optimization for cognitive radios,’’ in Proc. IEEE
Int. Conf. Commun. (ICC), Jun. 2012, pp. 6550–6554.
[203] J. Zhou, H. Qin, Y. Zhang, R. Yang, Y. Liu, and C. Li, ‘‘Binary quantum
elite particle swarm optimization algorithm for spectrum allocation
in cognitive wireless medical sensor network,’’ J. Phys., Conf. Ser.,
vol. 1924, no. 1, May 2021, Art. no. 012030.
[204] Y. Yang, Q. Zhang, Y. Wang, T. Emoto, M. Akutagawa, and S. Konaka,
‘‘Adaptive resources allocation algorithm based on modiﬁed PSO for
cognitive radio system,’’ China Commun., vol. 16, no. 5, pp. 83–92,
May 2019.
[205] A. A. El-Saleh, T. M. Shami, R. Nordin, M. Y. Alias, and I. Shayea,
‘‘Multi-objective optimization of joint power and admission control
in cognitive radio networks using enhanced swarm intelligence,’’
Electronics, vol. 10, no. 2, p. 189, Jan. 2021.
[206] V. D. P. Souto, R. D. Souza, B. F. Uchôa-Filho, A. Li, and Y. Li,
‘‘Beamforming optimization for intelligent reﬂecting surfaces without
CSI,’’ IEEE Wireless Commun. Lett., vol. 9, no. 9, pp. 1476–1480,
Sep. 2020.
[207] X. Chen, J. Zhang, B. Lin, Z. Chen, K. Wolter, and G. Min, ‘‘Energy-
efﬁcient ofﬂoading for DNN-based smart IoT systems in cloud-edge
environments,’’ IEEE Trans. Parallel Distrib. Syst., vol. 33, no. 3,
pp. 683–697, Mar. 2022.
[208] B. Lin, Y. Huang, J. Zhang, J. Hu, X. Chen, and J. Li, ‘‘Cost-driven off-
loading for DNN-based applications over cloud, edge, and end devices,’’
IEEE Trans. Ind. Informat., vol. 16, no. 8, pp. 5456–5466, Aug. 2020.
[209] B. Lin, F. Zhu, J. Zhang, J. Chen, X. Chen, N. N. Xiong, and J. L. Mauri,
‘‘A time-driven data placement strategy for a scientiﬁc workﬂow
combining edge computing and cloud computing,’’ IEEE Trans. Ind.
Informat., vol. 15, no. 7, pp. 4254–4265, Jul. 2019.
[210] J. S. Priya, M. Femina, and R. A. Samuel, ‘‘APSO-MVS: An adaptive
particle swarm optimization incorporating multiple velocity strategies
for optimal leader selection in hybrid MANETs,’’ Soft Comput., vol. 24,
pp. 18349–18365, May 2020.
[211] G. Husnain, S. Anwar, and F. Shahzad, ‘‘Performance evaluation of
CLPSO and MOPSO routing algorithms for optimized clustering in
vehicular ad hoc networks,’’ in Proc. 14th Int. Bhurban Conf. Appl. Sci.
Technol. (IBCAST), Jan. 2017, pp. 772–778.
[212] J. Toutouh and E. Alba, ‘‘Parallel multi-objective metaheuristics for smart
communications in vehicular networks,’’ Soft Comput., vol. 21, no. 8,
pp. 1949–1961, Apr. 2017.
[213] P. Lagos-Eulogio, J. C. Seck-Tuoh-Mora, N. Hernandez-Romero, and
J. Medina-Marin, ‘‘A new design method for adaptive IIR system
identiﬁcation using hybrid CPSO and DE,’’ Nonlinear Dyn., vol. 88, no. 4,
pp. 2371–2389, Jun. 2017.
[214] K. Yamamoto and K. Suyama, ‘‘Active enumeration of local minima for
IIR ﬁlter design using PSO,’’ in Proc. Asia–Paciﬁc Signal Inf. Process.
Assoc. Annu. Summit Conf. (APSIPA ASC), Dec. 2017, pp. 910–917.
[215] M. Dash, T. Panigrahi, and R. Sharma, ‘‘Robust estimation of IIR system’s
parameter using adaptive particle swarm optimization algorithm,’’ in
Computational Intelligence in Data Mining. Singapore: Springer, 2019,
pp. 41–50.
[216] X. Zhang, D. Lu, X. Zhang, and Y. Wang, ‘‘Antenna array design by a
contraction adaptive particle swarm optimization algorithm,’’ EURASIP
J. Wireless Commun. Netw., vol. 2019, no. 1, pp. 1–7, Dec. 2019.
[217] R. Bera, D. Mandal, R. Kar, and S. P. Ghoshal, ‘‘Non-uniform single-ring
antenna array design using wavelet mutation based novel particle swarm
optimization technique,’’ Comput. Electr. Eng., vol. 61, pp. 151–172,
Jul. 2017.
[218] J. Liu, H. Miao, X. Yuan, and J. Shi, ‘‘Photonic crystal microstrip antenna
array design using an improved Boolean particle swarm optimization,’’
in Urban Intelligence and Applications. Wuhan, China: Springer, 2020,
pp. 39–53.
[219] R. V. Kulkarni and G. K. Venayagamoorthy, ‘‘Particle swarm optimization
in wireless-sensor networks: A brief survey,’’ IEEE Trans. Syst., Man,
Cybern. C, Appl. Rev., vol. 41, no. 2, pp. 262–267, Mar. 2011.
[220] J. Chen, S. Huang, H. Li, X. Lv, and Y. Cai, ‘‘PSO-based agent
cooperative spectrum sensing in cognitive radio networks,’’ IEEE Access,
vol. 7, pp. 142963–142973, 2019.
[221] M. B. Taha, C. Talhi, H. Ould-Slimane, and S. Alrabaee, ‘‘TD-PSO: Task
distribution approach based on particle swarm optimization for vehicular
ad hoc network,’’ Trans. Emerg. Telecommun. Technol., vol. 31, p. e3860,
Jan. 2020.
[222] R. Sinha, A. Choubey, S. K. Mahto, and P. Ranjan, ‘‘Quantum behaved
particle swarm optimization technique applied to FIR-based linear and
nonlinear channel equalizer,’’ in Advances in Computer Communication
and Computational Sciences. Singapore: Springer, 2019, pp. 37–50.
[223] Y. Zhao, X. Yu, H. Wu, Y. Zhou, X. Sun, S. Yu, S. Yu, and H. Liu, ‘‘A fast
2-D Otsu lung tissue image segmentation algorithm based on improved
PSO,’’ Microprocessors Microsyst., vol. 80, Feb. 2021, Art. no. 103527.
[224] S. Mahalakshmi and T. Velmurugan, ‘‘Detection of brain tumor by
particle swarm optimization using image segmentation,’’ Indian J. Sci.
Technol., vol. 8, no. 22, p. 1, Sep. 2015.
10058
VOLUME 10, 2022


---

<!-- Page 29 -->
## Page 29

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
[225] T. R. Farshi and A. K. Ardabili, ‘‘A hybrid ﬁreﬂy and particle
swarm optimization algorithm applied to multilevel image thresholding,’’
Multimedia Syst., vol. 27, no. 1, pp. 125–142, Feb. 2021.
[226] S. K. Ghosh, B. Biswas, and A. Ghosh, ‘‘A novel approach of retinal
image enhancement using PSO system and measure of fuzziness,’’ Proc.
Comput. Sci., vol. 167, pp. 1300–1311, Jan. 2020.
[227] M. M. S. Rani and P. Chitra, ‘‘A hybrid medical image coding method
based on Haar wavelet transform and particle swarm optimization
technique,’’ Int. J. Pure Appl. Math., vol. 118, no. 8, pp. 3056–3067, 2018.
[228] X. Kang, Y. Chen, F. Zhao, and G. Lin, ‘‘Multi-dimensional particle
swarm optimization for robust blind image watermarking using inter-
twining logistic map and hybrid domain,’’ Soft Comput., vol. 24, no. 14,
pp. 10561–10584, Jul. 2020.
[229] X.-S. Yang, ‘‘Fireﬂy algorithms for multimodal optimization,’’ in Proc.
Int. Symp. Stochastic Algorithms. Berlin, Germany: Springer, 2009,
pp. 169–178.
[230] Z. Xin-gang, L. Ji, M. Jin, and Z. Ying, ‘‘An improved quantum particle
swarm optimization algorithm for environmental economic dispatch,’’
Expert Syst. Appl., vol. 152, Aug. 2020, Art. no. 113370.
[231] M. Mohammadian, A. Lorestani, and M. M. Ardehali, ‘‘Optimization of
single and multi-areas economic dispatch problems based on evolutionary
particle swarm optimization algorithm,’’ Energy, vol. 161, pp. 710–724,
Oct. 2018.
[232] W. T. Elsayed, Y. G. Hegazy, M. S. El-Bages, and F. M. Bendary,
‘‘Improved random drift particle swarm optimization with self-adaptive
mechanism for solving the power economic dispatch problem,’’ IEEE
Trans. Ind. Informat., vol. 13, no. 3, pp. 1017–1026, Jun. 2017.
[233] U. Khaled, A. M. Eltamaly, and A. Beroual, ‘‘Optimal power ﬂow using
particle swarm optimization of renewable hybrid distributed generation,’’
Energies, vol. 10, no. 7, p. 1013, Jul. 2017.
[234] S.
Khunkitti,
A.
Siritaratiwat,
S.
Premrudeepreechacharn,
R. Chatthaworn, and N. R. Watson, ‘‘A hybrid DA-PSO optimization
algorithm for multiobjective optimal power ﬂow problems,’’ Energies,
vol. 11, no. 9, p. 2270, Mar. 2019.
[235] K. Teeparthi and D. M. V. Kumar, ‘‘Multi-objective hybrid PSO-APO
algorithm based security constrained optimal power ﬂow with wind and
thermal generators,’’ Eng. Sci. Technol. Int. J., vol. 20, no. 2, pp. 411–426,
Apr. 2017.
[236] Z. Ullah, M. R. Elkadeem, S. Wang, and J. Radosavljević, ‘‘A novel
PSOS-CGSA method for state estimation in unbalanced DG-integrated
distribution systems,’’ IEEE Access, vol. 8, pp. 113219–113229, 2020.
[237] R. K. Sahu, S. Panda, and G. T. C. Sekhar, ‘‘A novel hybrid PSO-
PS optimized fuzzy PI controller for AGC in multi area interconnected
power systems,’’ Int. J. Electr. Power Energy Syst., vol. 64, pp. 880–893,
Jan. 2015.
[238] J. Y. Zhang and Y. Jiang, ‘‘Wide-area power system damping control
coordination based on particle swarm optimization with time delay
considered,’’ IOP Conf. Ser., Earth Environ. Sci., vol. 86, no. 1, Oct. 2017,
Art. no. 012029.
[239] G. Shaari, N. Tekbiyik-Ersoy, and M. Dagbasi, ‘‘The state of art in particle
swarm optimization based unit commitment: A review,’’ Processes, vol. 7,
no. 10, p. 733, Oct. 2019.
[240] S. Sharma and S. Ghosh, ‘‘FIS and hybrid ABC-PSO based optimal
capacitor placement and sizing for radial distribution networks,’’ J.
Ambient Intell. Hum. Comput., vol. 11, no. 2, pp. 901–916, Feb. 2020.
[241] B. Yang, Y. Chen, and Z. Zhao, ‘‘Survey on applications of particle swarm
optimization in electric power systems,’’ in Proc. IEEE Int. Conf. Control
Autom., May 2007, pp. 481–486.
[242] G. Abbas, J. Gu, U. Farooq, M. U. Asad, and M. El-Hawary, ‘‘Solution
of an economic dispatch problem through particle swarm optimization: A
detailed survey—Part I,’’ IEEE Access, vol. 5, pp. 15105–15141, 2017.
[243] G. Abbas, J. Gu, U. Farooq, A. Raza, M. U. Asad, and M. E. El-Hawary,
‘‘Solution of an economic dispatch problem through particle swarm
optimization: A detailed survey—Part II,’’ IEEE Access, vol. 5,
pp. 24426–24445, 2017.
[244] P. Shao, Z. Wu, X. Zhou, and D. C. Tran, ‘‘FIR digital ﬁlter design using
improved particle swarm optimization based on refraction principle,’’ Soft
Comput., vol. 21, no. 10, pp. 2631–2642, May 2017.
[245] A. Ghosh, A. Ghosh, A. Chowdhury, A. Konar, E. Kim, and A.
K. Nagar, ‘‘Linear phase low pass FIR ﬁlter design using genetic
particle swarm optimization with dynamically varying neighbourhood
technique,’’ in Proc. IEEE Congr. Evol. Comput. (CEC), Jun. 2012,
pp. 1–7.
[246] K. Basu and S. Nanda, ‘‘An adaptive ﬁltering technique with self-
adaptive PSO for estimation of non-stationary signals,’’ in Proc. Int. Conf.
Commun. Signal Process. (ICCSP), Apr. 2016, pp. 1057–1061.
[247] R. Malik, R. Dhir, and S. Mittal, ‘‘Remote sensing and landsat image
enhancement using multiobjective PSO based local detail enhancement,’’
J. Ambient Intell. Hum. Comput., vol. 10, no. 9, pp. 3563–3571,
Sep. 2019.
[248] G. R. Mamta and M. Dutta, ‘‘PSO based blind deconvolution technique of
image restoration using cepstrum domain of motion blur,’’ in Computa-
tional Vision and Bio Inspired Computing. Cham, Switzerland: Springer,
2018, pp. 947–958.
[249] S. Rengasamy and P. Murugesan, ‘‘PSO based data clustering with
a different perception,’’ Swarm Evol. Comput., vol. 64, Jul. 2021,
Art. no. 100895.
[250] M. Sharma and J. K. Chhabra, ‘‘Sustainable automatic data clustering
using hybrid PSO algorithm with mutation,’’ Sustain. Comput., Informat.
Syst., vol. 23, pp. 144–157, Sep. 2019.
[251] Y. Gupta and A. Saini, ‘‘A new swarm-based efﬁcient data clustering
approach using KHM and fuzzy logic,’’ Soft Comput., vol. 23, no. 1,
pp. 145–162, Jan. 2019.
[252] R. L. Patibandla, B. T. Rao, P. S. Krishna, and V. R. Maddumala, ‘‘Medical
data clustering using particle swarm optimization method,’’ J. Crit. Rev.,
vol. 7, no. 6, pp. 363–367, 2020.
[253] T. Y. Tan, L. Zhang, C. P. Lim, B. Fielding, Y. Yu, and E. Anderson,
‘‘Evolving ensemble models for image segmentation using enhanced
particle swarm optimization,’’ IEEE Access, vol. 7, pp. 34004–34019,
2019.
[254] Z. Zheng, N. Saxena, K. K. Mishra, and A. K. Sangaiah, ‘‘Guided
dynamic particle swarm optimization for optimizing digital image
watermarking in industry applications,’’ Future Gener. Comput. Syst.,
vol. 88, no. 11, pp. 92–106, 2018.
[255] B. Xia, Z. Ren, and C. S. Koh, ‘‘A novel reliability-based optimal design
of electromagnetic devices based on adaptive dynamic Taylor Kriging,’’
IEEE Trans. Magn., vol. 53, no. 6, pp. 1–4, Jun. 2017.
[256] O. U. Rehman, S. Tu, S. Khan, H. Khan, and S. Yang, ‘‘A modiﬁed
quantum particle swarm optimizer applied to optimization design of
electromagnetic devices,’’ Int. J. Appl. Electromagn. Mech., vol. 58, no. 3,
pp. 347–357, Nov. 2018.
[257] X. Chen, B. Xu, and W. Du, ‘‘An improved particle swarm optimization
with biogeography-based learning strategy for economic dispatch prob-
lems,’’ Complexity, vol. 2018, Jul. 2018, Art. no. 7289674.
[258] T. Liu, L. Jiao, W. Ma, J. Ma, and R. Shang, ‘‘Cultural quantum-behaved
particle swarm optimization for environmental/economic dispatch,’’
Appl. Soft Comput., vol. 48, pp. 597–611, Nov. 2016.
[259] A. Goudarzi, Y. Li, and J. Xiang, ‘‘A hybrid non-linear time-varying
double-weighted particle swarm optimization for solving non-convex
combined environmental economic dispatch problem,’’ Appl. Soft Com-
put., vol. 86, Jan. 2020, Art. no. 105894.
[260] F. Berrouk and K. Bounaya, ‘‘Optimal power ﬂow for multi-FACTS
power system using hybrid PSO-PS algorithms,’’ J. Control, Autom.
Electr. Syst., vol. 29, no. 2, pp. 177–191, Apr. 2018.
[261] A.
Man-Im,
W.
Ongsakul,
J.
G.
Singh,
and
M.
N.
Madhu,
‘‘Multi-objective
optimal
power
ﬂow
considering
wind
power
cost functions using enhanced PSO with chaotic mutation and
stochastic weights,’’ Electr. Eng., vol. 101, no. 3, pp. 699–718,
Sep. 2019.
[262] M. He, S. Wang, C. Fernandez, C. Yu, X. Li, and E. D. Bobobee,
‘‘A novel adaptive particle swarm optimization algorithm based high
precision parameter identiﬁcation and state estimation of lithium-
ion battery,’’ Int. J. Electrochem. Sci., vol. 16, no. 5, May 2021,
Art. no. 21054.
[263] X. Yang, Y. Chen, B. Li, and D. Luo, ‘‘Battery states online esti-
mation based on exponential decay particle swarm optimization and
proportional-integral observer with a hybrid battery model,’’ Energy,
vol. 191, Jan. 2020, Art. no. 116509.
[264] Y. Wang, G. Gao, X. Li, and Z. Chen, ‘‘A fractional-order model-based
state estimation approach for lithium-ion battery and ultra-capacitor
hybrid power source system considering load trajectory,’’ J. Power
Sources, vol. 449, Feb. 2020, Art. no. 227543.
[265] K. Balu and V. Mukherjee, ‘‘Siting and sizing of distributed generation
and shunt capacitor banks in radial distribution system using constriction
factor particle swarm optimization,’’ Electr. Power Compon. Syst., vol. 48,
nos. 6–7, pp. 697–710, Apr. 2020.
[266] R. Krishnasamy, R. Aathi, and P. Jeyabalan, ‘‘Application of compre-
hensive learning particle swarm optimization to least cost generation
expansion planning problem with solar plant,’’ in Proc. IEEE Int.
Conf. Clean Energy Energy Efﬁcient Electron. Circuit Sustain. Develop.
(INCCES), Dec. 2019, pp. 1–5.
VOLUME 10, 2022
10059


---

<!-- Page 30 -->
## Page 30

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
[267] H. Doagou-Mojarrad, H. Rastegar, and G. B. Gharehpetian, ‘‘Probabilis-
tic interactive fuzzy satisfying generation and transmission expansion
planning using fuzzy adaptive chaotic binary PSO algorithm,’’ J. Intell.
Fuzzy Syst., vol. 30, no. 3, pp. 1629–1641, Mar. 2016.
[268] S. Rastgoufard and D. Charalampidis, ‘‘Tuned support vector regression
by modiﬁed particle swarm optimization for online power system static
security evaluation,’’ in Proc. IEEE Texas Power Energy Conf. (TPEC),
Feb. 2018, pp. 1–6.
[269] N. Kumar and V. Mahajan, ‘‘Reconﬁguration of distribution network for
power loss minimization & reliability improvement using binary particle
swarm optimization,’’ in Proc. IEEE 8th Power India Int. Conf. (PIICON),
Dec. 2018, pp. 1–6.
[270] J. Li, H. Huang, B. Lou, Y. Peng, Q. Huang, and K. Xia, ‘‘Wind farm
reactive power and voltage control strategy based on adaptive discrete
binary particle swarm optimization algorithm,’’ in Proc. IEEE Asia Power
Energy Eng. Conf. (APEEC), Mar. 2019, pp. 99–102.
[271] W. Moondee and W. Srirattanawichaikul, ‘‘Reactive power management
of MV distribution grid with inverter-based PV distributed generations
using PSO algorithm,’’ in Proc. 45th Annu. Conf. IEEE Ind. Electron.
Soc. (IECON), Oct. 2019, pp. 2239–2244.
[272] T. M. Aljohani, A. F. Ebrahim, and O. Mohammed, ‘‘Single and
multiobjective optimal reactive power dispatch based on hybrid artiﬁcial
physics–particle swarm optimization,’’ Energies, vol. 12, no. 12, p. 2333,
Jun. 2019.
[273] S. Kanata, G. H. M. Sianipar, and N. U. Maulidevi, ‘‘Optimization
of reactive power and voltage control in power system using hybrid
artiﬁcial neural network and particle swarm optimization,’’ in Proc.
2nd Int. Conf. Appl. Electromagn. Technol. (AEMT), Apr. 2018,
pp. 67–72.
[274] N. Zeng, H. Zhang, W. Liu, J. Liang, and F. E. Alsaadi, ‘‘A
switching delayed PSO optimized extreme learning machine for
short-term load forecasting,’’ Neurocomputing, vol. 240, pp. 175–182,
May 2017.
[275] Y. K. Semero, J. Zhang, and D. Zheng, ‘‘EMD–PSO–ANFIS-
based hybrid approach for short-term load forecasting in micro-
grids,’’ IET Gener., Transmiss. Distrib., vol. 14, no. 3, pp. 470–475,
Feb. 2020.
[276] X. Tao, W. Guo, Q. Li, C. Ren, and R. Liu, ‘‘Multiple scale self-adaptive
cooperation mutation strategy-based particle swarm optimization,’’ Appl.
Soft Comput., vol. 89, Apr. 2020, Art. no. 106124.
[277] K. Chaitanya, D. V. L. N. Somayajulu, and P. R. Krishna, ‘‘Memory-
based approaches for eliminating premature convergence in par-
ticle swarm optimization,’’ Appl. Intell., vol. 51, pp. 4575–4608,
Jan. 2021.
[278] T. Krink, J. S. Vesterstrom, and J. Riget, ‘‘Particle swarm optimisation
with spatial particle extension,’’ in Proc. Congr. Evol. Comput. (CEC),
2002, pp. 1474–1479.
[279] A. Faramarzi, M. Heidarinejad, B. Stephens, and S. Mirjalili, ‘‘Equilib-
rium optimizer: A novel optimization algorithm,’’ Knowl.-Based Syst.,
vol. 191, Mar. 2020, Art. no. 105190.
[280] A. Faramarzi, M. Heidarinejad, S. Mirjalili, and A. H. Gandomi, ‘‘Marine
predators algorithm: A nature-inspired Metaheuristic,’’ Expert Syst.
Appl., vol. 152, Aug. 2020, Art. no. 113377.
[281] I. Ahmadianfar, O. Bozorg-Haddad, and X. Chu, ‘‘Gradient-based
optimizer: A new metaheuristic optimization algorithm,’’ Inf. Sci.,
vol. 540, pp. 131–159, Nov. 2020.
[282] Q. Askari, I. Younas, and M. Saeed, ‘‘Political optimizer: A novel socio-
inspired meta-heuristic for global optimization,’’ Knowl.-Based Syst.,
vol. 195, May 2020, Art. no. 105709.
[283] L. Abualigah, A. Diabat, S. Mirjalili, M. A. Elaziz, and A. H. Gandomi,
‘‘The arithmetic optimization algorithm,’’ Comput. Methods Appl. Mech.
Eng., vol. 376, Apr. 2021, Art. no. 113609.
[284] F. A. Hashim, K. Hussain, E. H. Houssein, M. S. Mabrouk, and
W. Al-Atabany, ‘‘Archimedes optimization algorithm: A new metaheuris-
tic algorithm for solving optimization problems,’’ Appl. Intell., vol. 51,
no. 3, pp. 1531–1551, 2021.
[285] M. Alswaitti, M. Albughdadi, and N. A. M. Isa, ‘‘Density-based particle
swarm optimization algorithm for data clustering,’’ Expert Syst. Appl.,
vol. 91, pp. 170–186, Jan. 2018.
[286] C. Duan, C. Deng, A. Gharaei, J. Wu, and B. Wang, ‘‘Selective
maintenance scheduling under stochastic maintenance quality with
multiple maintenance actions,’’ Int. J. Prod. Res., vol. 56, no. 23,
pp. 7160–7178, Dec. 2018.
[287] A. Gharaei, S. A. H. Shekarabi, and M. Karimi, ‘‘Modelling and
optimal lot-sizing of the replenishments in constrained, multi-product
and bi-objective EPQ models with defective products: Generalised
cross decomposition,’’ Int. J. Syst. Sci., Oper. Logistics, vol. 7, no. 3,
pp. 262–274, Jul. 2020.
[288] A. Gharaei, M. Karimi, and S. A. H. Shekarabi, ‘‘Joint economic lot-
sizing in multi-product multi-level integrated supply chains: Generalized
benders decomposition,’’ Int. J. Syst. Sci., Oper. Logistics, vol. 7, no. 4,
pp. 309–325, Oct. 2020.
[289] M. Rabbani, N. Foroozesh, S. M. Mousavi, and H. Farrokhi-Asl,
‘‘Sustainable supplier selection by a new decision model based on
interval-valued fuzzy sets and possibilistic statistical reference point
systems under uncertainty,’’ Int. J. Syst. Sci., Oper. Logistics, vol. 6, no. 2,
pp. 162–178, Apr. 2019.
[290] N. H. Shah, U. Chaudhari, and L. E. Cárdenas-Barrón, ‘‘Integrating
credit and replenishment policies for deteriorating items under quadratic
demand in a three echelon supply chain,’’ Int. J. Syst. Sci., Oper. Logistics,
vol. 7, no. 1, pp. 34–45, Jan. 2020.
TAREQ M. SHAMI received the B.Eng. (Hons.)
and M.Sc.Eng. degrees in electronics majoring in
telecommunications from Multimedia University,
Melaka and Cyberjaya, Malaysia, in 2012 and
2017, respectively, and the Ph.D. degree in
electronic engineering from the University of
York, in 2021. His Ph.D. research was part of
the European-funded Marie Curie ITN-5GAuRA
Project. His current research interests include 5G
small cell networks, radio resource management,
cell-less architectures, optimization algorithms, multi-objective optimiza-
tion, and feature selection.
AYMAN A. EL-SALEH (Senior Member, IEEE)
received the B.Sc. degree in communications
engineering from Omar El-Mukhtar University
(OMU), Libya, in 1999, and the M.Sc. degree in
microelectronics engineering and the Ph.D. degree
in wireless communications from the Universiti
Kebangsaan Malaysia (UKM), in 2006 and 2012,
respectively. He joined the Faculty of Engineer-
ing, Multimedia University (MMU), in October
2006, where he was a Senior Lecturer and the
Chairperson of the Centre for Wireless Technology (CWT). In April
2017, he was appointed as the Lead of Connectivity Research Theme,
MMU. He joined A’Sharqiyah University, Oman, in September 2017,
where he is currently an Associate Professor. He published more than
70 journals and conference papers. His research interests include cognitive
radio networks, heterogeneous LTE/LTE-advanced cellular networks, and
applications of artiﬁcial intelligence and evolutionary algorithms in wireless
communications. He was an Executive Committee Member of the IEEE
Malaysia ComSoc/VTS Joint Chapter, in 2015 and 2016. He is a reviewer
of several indexed journals.
10060
VOLUME 10, 2022


---

<!-- Page 31 -->
## Page 31

T. M. Shami et al.: Particle Swarm Optimization: Comprehensive Survey
MOHAMMED
ALSWAITTI
(Member, IEEE)
received the B.Eng. degree in computer engineer-
ing from the Islamic University of Gaza (IUG),
Palestine, in 2010, the M.Sc. degree in electronic
systems design engineering from the Universiti
Sains Malaysia (USM), Malaysia, in 2011, and the
Ph.D. degree in computational intelligence under
the Malaysian International Scholarship (MIS)
Scheme. He worked as a Lecturer with the Soft-
ware Engineering and Information Technology
Faculties, University of Palestine, and as an Instructor at the Educational
Technology Centre, IUG. He worked as a Graduate Assistant with the
Electrical and Electronic Engineering Department, USM. He is currently
an Assistant Professor at the School of Electrical and Computer Engi-
neering, Xiamen University Malaysia (XMUM). He acts as the Research
Coordinator with the school where his research is focused on nature-
inspired optimization-based clustering techniques, machine/deep learning
applications, and pattern recognition. Recently, he managed to publish
several articles in the top tier journals in AI ﬁeld through securing research
funds and collaborations with research institutions all over the world.
Besides, he is a regular keynote speaker at academic and industry conferences
and workshops and does voluntary work as a reviewer and an associate editor
for journals and language editing services.
QASEM AL-TASHI received the B.Sc. degree
in software engineering from the Universiti
Teknologi Malaysia, in 2012, the M.Sc. degree
in software engineering from the Universiti
Kebangsaan Malaysia, in 2017, and the Ph.D.
degree in information technology from the Uni-
versiti Teknologi PETRONAS, in 2021. He was
a Research Scientist at Universiti Teknologi
PETRONAS. He is currently a Postdoctoral
Fellow at The University of Texas MD Anderson
Cancer Center, Houston, TX, USA. He is also an Academic Staff with
Albaydha University, Yemen. His research interests include artiﬁcial neural
networks, multi-objective optimization, feature selection, and swarm intel-
ligence evolutionary algorithms, classiﬁcation, and data analytics. He is a
Section Editor of the Journal of Applied Artiﬁcial Intelligence (JAAI) and the
Journal of Information Technology and Computing (JITC). He is a Reviewer
of several high-impact factor journals, such as Artiﬁcial Intelligence Review,
IEEE ACCESS, Knowledge-Based Systems, Soft Computing, Journal of
Ambient Intelligence and Humanized Computing, Applied Soft Computing,
Neurocomputing, Applied Artiﬁcial Intelligence, and Plos One.
MHD AMEN SUMMAKIEH (Member, IEEE)
received the B.Eng. degree (Hons.) in commu-
nication and electronics engineering from the
UCSI University, Malaysia, in 2016, and the
M.Eng.Sc. degree from Multimedia University,
Malaysia, in 2020. His research interests include
heterogeneous LTE-advanced cellular networks,
user association, metaheuristic algorithms, and
antennas design.
SEYEDALI (ALI) MIRJALILI (Senior Member,
IEEE) is currently the Director of the Centre for
Artiﬁcial Intelligence Research and Optimization,
Torrens University Australia, Brisbane. He is
internationally recognized for his advances in
swarm intelligence and optimization, including the
ﬁrst set of algorithms from a synthetic intelligence
standpoint—a radical departure from how natural
systems are typically understood—and a system-
atic design framework to reliably benchmark,
evaluate, and propose computationally cheap robust optimization algorithms.
He has published over 250 publications with over 31900 citations and
an H-index of 62. As the most cited researcher in robust optimization,
he is in the list of 1% highly cited researchers and named one of
the world’s most inﬂuential researchers by the Web of Science. He is
working on the applications of multi-objective and robust meta-heuristic
optimization techniques as well. His research interests include robust
optimization, engineering optimization, multi-objective optimization, swarm
intelligence evolutionary algorithms, and artiﬁcial neural networks. He is
an Associate Editor of several journals, including Neurocomputing, Applied
Soft Computing, Advances in Engineering Software, Applied Intelligence,
and IEEE ACCESS.
VOLUME 10, 2022
10061


---
