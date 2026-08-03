# Groupers and moray eels (GME) optimization: a nature-inspired metaheuristic algorithm for solving complex engineering problems

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-10384-y

---

## Page 1
ORIGINAL ARTICLE
Groupers and moray eels (GME) optimization: a nature-inspired
metaheuristic algorithm for solving complex engineering problems
Nehal A. Mansour1 • M. Sabry Saraya2 • Ahmed I. Saleh2
Received: 25 November 2023 / Accepted: 24 August 2024 / Published online: 16 November 2024
 The Author(s) 2024
Abstract
As engineering technology advances and the number of complex engineering problems increases, there is a growing need
to expand the abundance of swarm intelligence algorithms and enhance their performance. It is crucial to develop, assess,
and hybridize new powerful algorithms that can be used to deal with optimization issues in different ﬁelds. This paper
proposes a novel nature-inspired algorithm, namely the Groupers and Moray Eels (GME) optimization algorithm, for
solving various optimization problems. GME mimics the associative hunting between groupers and moray eels. Many
species, including chimpanzees and lions, have shown cooperation during hunting. Cooperative hunting among animals of
different species, which is called associative hunting, is extremely rare. Groupers and moray eels have complementary
hunting approaches. Cooperation is thus mutually beneﬁcial because it increases the likelihood of both species successfully
capturing prey. The two predators have complementary hunting methods when they work together, and an associated hunt
creates a multi-predator attack that is difﬁcult to evade. This example of hunting differs from that of groups of animals of
the same species due to the high level of coordination among the two species. GME consists of four phases: primary search,
pair association, encircling or extended search, and attacking and catching. The behavior characteristics are mathematically
represented to allow for an adequate balance between GME exploitation and exploration. Experimental results indicate that
the GME outperforms competing algorithms in terms of accuracy, execution time, convergence rate, and the ability to
locate all or the majority of local or global optima.
Keywords Optimization  Associative hunting  Nature-inspired  Metaheuristic  Grouper and Moray Eel algorithm
1 Introduction
Optimization refers to the process of identifying the most
optimal or superior option among all available solutions.
Optimization aims to select input values within a given set
of permitted values in order to minimize or maximize one
or more deﬁned objective functions. In optimization
algorithms, the procedure for locating the optimal solution
begins with the random generation of a certain number of
solvable solutions that satisfy the problem’s constraints.
Afterward,
these randomized
solutions
are
improved
through the utilization of the algorithm’s phases, and a
procedure relied on repetition. When the algorithm is
entirely executed, the best proposed solution for the opti-
mization problem is determined [1].
Despite the fact that many optimization algorithms have
been developed, some of them may be highly effective at
addressing a particular set of optimization challenges,
while being incapable of addressing another set. This is due
to the fact that the mathematical models and characteristics
of different real-world problems vary. Consequently, the
efﬁciency of handling all optimization issues cannot be
guaranteed by any single optimization technique [2]. Real-
world optimization problems have become more difﬁcult,
necessitating more efﬁcient solution methods, so various
& Nehal A. Mansour
nehal.anees.mansour@nilehi.edu.eg
M. Sabry Saraya
mohamedsabry83@mans.edu.eg
Ahmed I. Saleh
aisaleh@mans.edu.eg
1
Artiﬁcial Intelligence Lab, Nile Higher Institute for
Engineering and Technology, Mansoura, Egypt
2
Computers and Control Department, Faculty of Engineering,
Mansoura University, Mansoura, Egypt
123
Neural Computing and Applications (2025) 37:63–90
https://doi.org/10.1007/s00521-024-10384-y
(0123456789().,-volV)
(0123456789().,-volV)

---

## Page 2
researchers have studied various methods for dealing with
these complex and difﬁcult real-world problems [3]. Cer-
tain researchers employ conventional techniques, including
conjugate gradient, quasi-Newton, and sequential quadratic
programming, in order to address these optimization
problems. However, due to the nonlinearity, presence of
several decision variables, and complex restrictions in most
real-world optimization problems, solving them efﬁciently
becomes challenging using traditional techniques [3]. The
advantages of metaheuristic algorithms include that they
don’t rely on the problem model, don’t require gradient
information, have a robust search capability, are widely
applicable, and can achieve a satisfactory balance between
optimal solutions and computational cost. Because of their
ability to efﬁciently generate optimal solutions using
computational resources, metaheuristic algorithms have
frequently been embraced as an appropriate method to
tackle optimization challenges. [4].
To identify the optimal solution, each of these meta-
heuristic algorithms depends on exploration and exploita-
tion
in
the
search
space.
Exploration
denotes
the
algorithm’s pursuit of potential regions within a vast search
space, while exploitation signiﬁes the algorithm’s attempt
to identify the optimal solution within those potential
regions; thus, the solution quality is determined by the
equilibrium between the two search behaviors. Maintaining
a delicate equilibrium between exploration and exploitation
is of utmost importance in metaheuristic algorithms to
prevent ﬂuctuations in the convergence rate and to identify
both local and global optimal solutions. In order to achieve
optimal convergence, metaheuristic algorithms frequently
use parameter controls to effectively balance between them
[5].
A novel nature-inspired algorithm, namely Groupers and
Moray Eels (GME) Optimization, is proposed in this paper
to be more effective for solving various optimization
problems. GME mimics the associative hunting between
groupers and moray eels. GME consists of four phases:
primary search, pair association, encircling or extended
search, and attacking and catching. The optimization rule
in GME typically involves selecting the best solutions and
the process continues for a predetermined number of iter-
ations or until a termination criterion is satisﬁed, such as
the desired level of solution quality or the completion of a
predetermined number of iterations. This means that as the
iterations progress, the population is updated, and the
quality of the solutions improves. GME aims to converge
towards an optimal or near-optimal solution to the given
problem. GME also behaves in balance in the exploration
and exploitation phases with an adaptive mechanism over
search space. Moreover, the key contributions of this paper
are summarized below:
•
A new nature-inspired optimization algorithm called
GME is proposed to mimic the associative hunting
strategy between different species which are: grouper
and moray eels, and it is very rare to observe this
cooperation in nature.
•
Based on the good results obtained in the experimental
section of the paper;
o
The suggested GME algorithm can successfully
escape the local optima trap.
This happened
because it combines evidence from the behavior
of two different animals, each of which has a
unique movement pattern. This results in good
search domain coverage and balanced behavior
between the exploitation and exploration phases.
o
GME is relatively easy, and simple to implement
when
compared
with
most
metaheuristic
algorithms.
•
The performance evaluation of the GME algorithm is
evaluated by comparing its results to those of other
well-known metaheuristic methods. The experimental
results suggest that the GME algorithm performs better
in solving difﬁcult optimization issues.
The overall structure of this paper is as follows: litera-
ture review is provided in Sect. 2. Section 3 describes the
inspiration for GME and constructs the corresponding
mathematical model. A discussion of the results has been
provided in Sect. 4. The conclusion and future research
take place in the last section.
2 Literature review
This section is divided into three subsections. An expla-
nation
of
nature-inspired
optimization
algorithms
is
described in Sect. 2.1. On the other hand, cooperative
versus associative hunting is explained in Sect. 2.2. Sec-
tion 2.3 discusses the characteristics of Groupers and
Moray Eels Pair.
2.1 Nature-inspired algorithms
In the real world, optimization entails not just enhancing
effectiveness but also minimizing time and computational
cost. In reality, there are a lot of difﬁcult and complex
optimization problems that need to be solved. There are
two techniques for resolving issues and obtaining opti-
mized solutions: heuristic and metaheuristic algorithms. In
metaheuristic algorithms, the best solution is found from
the random search space and predeﬁned boundaries,
whereas heuristic algorithms are dependent on a speciﬁc
problem. Both exact and approximate approaches can be
64
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 3
used to address Nondeterministic Polynomial time (NP-
hard) issues [6, 7]. The exact procedures, which have a
high cost and exponential time complexity, ensure the best
solution. The heuristic and metaheuristic algorithms belong
to the family of approximate algorithms. Although they
cannot be guaranteed to discover the exact solution, they
may be closer to it as they have a lower complexity and
faster execution time. The second group is typically pre-
ferred. Examples of heuristic algorithms are such as; Hill
climbing (HC), Simulated Annealing (SA) [8], and Best
First Search (BFS) [9]. The metaheuristic approaches can
offer a useful and practical solution for many NP-hard
problems and typically outperform heuristic methods in
ﬁnding the best solutions for different types of problems in
terms of actual execution time.
The metaheuristic approaches are more ﬂexible and
attempt to ﬁnd the best solutions in global search areas
with low processing costs in a short amount of execu-
tion time with simple implementation. They also avoid
falling into local traps. In particular, metaheuristic algo-
rithms have the potential to be more effective in solving
complicated issues [10]. Additionally, according to no free-
lunch (NFL), there isn’t an algorithm that can solve all
optimization problems to the best of its ability [2]. Con-
sequently, there is a signiﬁcant demand for the develop-
ment of novel metaheuristic algorithms that may be used
for a variety of issues. Metaheuristic optimization algo-
rithms have thus gained popularity in recent years in var-
ious scientiﬁc ﬁelds due to their wide range of applications
and beneﬁts. Metaheuristic algorithms are divided into two
types: single solution-based algorithms and multiple solu-
tions-based algorithms. When the search process starts with
a single candidate solution it is called a single solution-
based algorithm, but in multiple solution-based algorithms,
the optimization is carried out using a population of solu-
tions. Metaheuristic algorithms with a population perform
better than those with a single solution [11, 12].
Exploration and exploitation are the two fundamental
phases of metaheuristic algorithms, and each algorithm has
its strategy for implementing the principles of both phases.
The greater the balance between these two phases in the
proposed algorithms, the higher the success rate. The ran-
domness and proper coefﬁcients deﬁned in the algo-
rithms are important. It is critical to carefully adjust the
relevant coefﬁcient parameters to achieve a suitable bal-
ance between these two phases. The exploration algorithms
look for new solutions in new areas, this means the
exploration entails a global search. This step needs more
searching thus the applicable algorithm chooses solutions
at random from the search space. The phase of exploitation
follows the exploration phase and focuses on using current
solutions and modifying them so their ﬁtness improves.
The algorithm’s ability to escape traps is inﬂuenced by the
randomness of the search in exploration [6, 13].
Nature-inspired metaheuristic algorithms are high-level
heuristics that draw inspiration from a variety of sources,
including physical and chemical systems [14, 15], swarm
intelligence, biological systems [16], artiﬁcial systems, and
so on. Swarm intelligence, physics-based, and evolutionary
algorithms are the three main categories of metaheuristic
algorithms as shown in Fig. 1. The Darwinian Theory of
Evolution serves as a source of inspiration for evolutionary
algorithms (EAs) [17, 18]. EAs use a population-based
approach for problem-solving, where the entire population
has an impact on the best solution. They address problems
inside a stochastic search domain and utilize the most
optimal solution from the previous iteration to generate
new solutions in the following iteration, as the most suit-
able solutions in the current iteration are more likely to
contribute to the creation of a new solution in the next
iteration. The genetic algorithm (GA) is a well-known EA
algorithm that is inspired by generation reproduction.
Another algorithm inspired by nature’s evolution is the
differential evolution (DE) algorithm. The DE algorithm
differs from the GA algorithm in the selection procedure
used to generate the next generation. Other examples of an
EA are the Biogeography-Based Optimizer (BBO), Tabu
Search (TS), Black Window optimization (BWO), and
Evolutionary programming (EP) [19]. Physics-based algo-
rithms are another type of metaheuristic technique. These
algorithms are inspired by nature’s physics rules and
operate at random. The search space and optimal solution
in this type of algorithm follow physical rules such as
gravitational force, electromagnetic force, and mechanical
force [20]. This category includes well-known algorithms
such as the gravitational local search (GLSA), curved space
optimization (CSO), the gravitational search algorithm
(GSA), big bang-big crunch (BBBC), and black hole (BH).
The
third
category
of
metaheuristic
algorithms
is
swarm intelligence (SI). In general, SI approaches are
inﬂuenced by the social behaviors of creatures that live in
nature in swarms, ﬂocks, and herds [16, 21, 22]. In this type
of algorithm, search agents attempt to ﬁnd an ideal solution
by incorporating social intelligence. There are many
algorithms in this category such as; grey wolf optimization
(GWO), particle swarm optimization (PSO), artiﬁcial bee
colony (ABC), whale optimization algorithm (WOA), and
ant colony optimization (ACO). In this paper, many
swarm-based algorithms are used to compare their perfor-
mance with the GME which are; Cheetah Optimizer (CO)
[23], Fennec Fox Optimization (FFA) [24], Hermit Crab
Optimization Algorithm (HCOA) [25], Improved Salp
Swarm Algorithm (ISSA) [26], Osprey Optimization
Algorithm (OOA) [27], Red-Tailed Hawk algorithm (RTH)
[28], Walrus Optimization Algorithm (WaOA) [7].
Neural Computing and Applications (2025) 37:63–90
65
123

---

## Page 4
2.2 Cooperative versus associative hunting
The pursuit of prey may require the collaborative efforts of
multiple individuals in order to achieve a successful hunt.
When hunting alone, the probability of successfully cap-
turing wildlife that is particularly resistant or nimble may
be low. Some have hypothesized that a comparable difﬁ-
culty has resulted in intricate collaborative hunting conduct
among chimpanzees, wherein the participating individuals
assume distinct hunting roles. Collaborative hunting can
also be beneﬁcial when the prey is too sizable to be sub-
dued by a solitary hunter.
Both cooperative and associative hunting are ﬁred due to
one or more factors such as; (i) the prey’s energy to con-
tinue the chase. For example, the prey may be very fast and
have a high ability to continue chasing for a long time,
which requires cooperation between the individuals to
follow one after the other until the prey loses its ability to
continue chasing; (ii) the prey can be slow; and however,
prey size plays an effective role in the evolution of coop-
erative hunting. The large-sized prey certainly needs many
individuals to be taken down. For example, a group of lions
must cooperate to land an African buffalo [29].
Generally, group hunting maximizes the success rate of
catching the prey. Moreover, based on several studies, the
larger the group size, (i) the more captures per hunt, (ii) the
greater the range of prey that can be taken, and (iii) the
greater the likelihood of making multiple kills per hunt
[29]. Figure 2 illustrates the difference between coopera-
tive and associative hunting.
2.3 Groupers and moray eels pair
The moray eel and the grouper ﬁsh form an unexpected
friendship in the vibrant depths of the ocean. Watch as
these two species use their unique hunting abilities to
conquer the food in the water. A grouper reaches an eel’s
hiding spot and jerks its head quickly, indicating that it
wants to hunt. The eel detects the signal and follows the
grouper. The grouper shakes its head again as it guides the
eel to a location where prey is located. The grouper cannot
penetrate this area, but the eel may enter tight ﬁssures and
hunt the prey out. Although either the grouper or the eel
will catch a certain prey animal, researchers have discov-
ered that each animal consumes the prey at a different
period. As a result, the pair should go hunting together.
Moray eels, unlike many predators, have limited eyesight
and must rely on their extraordinary sense of smell to hunt.
Because moray eels rely primarily on smell, their preferred
food is frequently weakened or dead to make it easier to
detect. This makes them excellent reef cleaners [30]. The
collaboration appeared to beneﬁt both morays and groups,
with each species experiencing greater hunting success
than when hunting alone, as shown in Fig. 3.
3 Materials and methods
The Theorem of No Free Lunch (NFL) states that there is
no assurance that an algorithm that performs well at opti-
mizing a speciﬁc group of problems will perform well at
optimizing all other optimization problems. We claim that
this problem is due to the fact that all previous algorithms
assume one model of movement because they depend on
agents from the same species and therefore the movement
of all of them is constant. NFL pushes researchers to create
new metaheuristic algorithms to tackle optimization issues
in several ﬁelds more successfully. The NFL theorem also
inﬂuenced the authors of this work to implement a new
metaheuristic
algorithm
depending
on
agents
from
Evolutionary Algorithm 
BBO
GA
GP
DE
TS
EP
Metaheuristic algorithms 
Optimization algorithms 
Heuristic algorithms  
Physics-based algorithms  
CSO 
GSA
BH
GLSA 
BBBC
Swarm Intelligence
GME
PSO 
ACO
ABC
WOA
GWO
HC 
SA 
BFS 
CSP  
Fig. 1 Different types of optimization algorithms
66
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 5
different species to propose effective optimum results to
optimization challenges. In nature, there are many obser-
vations about the existence of cooperation between animals
of different species such as; Honey Badger and Wolf, and
grouper and moray eel. In this research, we will introduce a
new algorithm based on cooperation between groupers and
moray eels where each of them has a different strategy in
the attack. When these two predators combine their hunting
abilities, more than one agent is looking for prey with
different strategies, and fast access to prey, and prey has
little chance of surviving. If the prey hides below the reef,
the sinuous shape and ambush techniques of the moray eel
come into play. If the victim runs into open water, the
grouper’s speed and agility will seal its doom. This coop-
erative behavior appears to be an indication of high intel-
ligence. The cooperation between the groupers and moray
eels (i.e. cooperation in hunting between different species)
provides better results than the hunting between the same
species.
3.1 The proposed groupers and moray eels
(GME) optimization
In GME optimization, the ﬂock consists of an even number
of search agents. Hence, it can be easily divided later into
pairs. Each pair consists of two individuals, the ﬁrst
consists of grouper ﬁshes, and the other one contains the
eels as shown in Fig. 4. The pair works together to catch
the prey so that each individual has a speciﬁc function.
There is no overlap in the tasks within the same pair, but
the pair individuals work together in a distinct harmony,
which increases the possibility of successful prey catching.
The cooperation between grouper ﬁsh and Moray eel
during the hunting process goes through four phases, which
are; (i) Primary search (PS) for a prey, (ii) Pair association
(PA), (iii) Encircling or extended search (ES), and (iv)
Attacking and catching (AC). GME begins with a popu-
lation of potential solutions. These solutions are created
stochastically within the problem’s stated upper (UB) and
lower (LB) bounds. Each potential solution to the opti-
mization issue is represented by a candidate solution. The
goal is to discover the optimum solution for a certain goal
or ﬁtness function. Based on the problem’s requirements,
the evaluated values for the ﬁtness function are used as the
primary criterion for assessing the quality of the proposed
solutions. As a result, the best value for the ﬁtness function
corresponds to the best candidate solution (i.e., the best
search agent), while the worst value corresponds to the
worst candidate solution (i.e., the worst search agent) in
each iteration of the optimization process. This means that
the population is updated as iterations go, and the quality of
the
solutions
improves.
In
GME,
the
optimization
Group Hunting
Cooperative 
Associative
Hunting strategies
1 
2 
Individual Hunting
Individual
Group
Cooperative (Social) 
Associative
Description  
It is a method of hunting in 
which a single hunter does not 
enjoy any support, whether 
from individuals of the same 
taxa or of another taxa. 
Cooperative 
hunting 
between 
the 
same 
related taxa, in which 
every individual works for 
the benefit of the group. 
Cooperative hunting involves taxa that are distantly 
related, wherein one species facilitates the access of 
other participants to prey. However, each pursues his 
own advantage.(i.e. the associative hunting is a 
cooperative hunting between different species ) 
Number of agents
Single 
Multiple 
Multiple 
Success rate  
Low 
Medium 
High 
Agent type 
Single 
Single 
Multiple 
Examples  
 Tiger 

Lions 

Wolves 

Whales. 

Hyenas. 
 Groupers and Moray Eels. 
 Coyotes and Badgers. 
Fig. 2 Different hunting strategies
Neural Computing and Applications (2025) 37:63–90
67
123

---

## Page 6
procedure often entails selecting the best solutions and
continuing the procedure for a pre-established number of
iterations or until a termination condition is met, such as
reaching a maximum number of iterations or achieving a
certain level of solution quality. GME tries to converge
towards an optimal or near-optimal solution to the given
problem by iteratively updating the population and con-
sidering the best solution acquired thus far.
During the ﬁrst phase, which is PS, only the groupers
search for the potential prey. Once the PS phase has ﬁn-
ished, it is assumed that each grouper ﬁsh has located its
prey and the task now is to choose one of the eels to pursue
and chase that prey among the rocks. This task is accom-
plished during the PA phase. After pair formulation, each
grouper ﬁsh has become associated with an eel. Then, each
pair tries again to search for prey after it has been hidden
Fig. 3 Cooperation between grouper and moray eels
Search agents
(N) 
Fig. 4 Search agent divided into
two groups
68
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 7
among the coral reefs. This is accomplished through the ES
phase. However, each agent searches for prey in its own
way. The eel searches for prey among the rocks inside the
coral reefs, while the grouper spins outside the coral reefs
in spiral rings, waiting for the prey to exit from inside the
coral reefs, hoping that the eel will not be able to catch it.
The ﬁnal phase is the AC phase, in which the prey is caught
by one of the pair of individuals, either the grouper ﬁsh or
the moray eel. Through the next subsections, each of the
pre-mentioned phases will be explained in more detail.
3.2 Primary search (PS) phase
In the wild, groupers are intriguing ﬁsh to observe. They
can travel through the water by propelling themselves
ahead with their bodies. They can also fast shift the
direction of their ﬁns. This adaptability allows grouper to
move quickly through the water, while avoiding predators
and prey. Exploration is mainly carried out during the
search phase in all nature-inspired optimization algorithms,
whereas
encircling
and
attacking are
reserved
for
exploitation. In order to achieve this objective, the search
agents are permitted to navigate the search space at ran-
dom. The search agents’ movements are considered to
be random due to the uncertain location of the optimal
solution (the prey). Without a doubt, a successful prey
search improves the algorithm’s exploration ability.
Groupers move in various ways, depending on their
habitat and hunting strategy. They use the zig-zag swim-
ming method to navigate their way around. This method
allows them to quickly cover a large area and track
potential threats. In this phase, the grouper ﬁsh is looking
for the presence of prey, and its movement is in the form of
a zig-zag, where a random place is imposed for each
grouper ﬁsh, and then each of them begins to move. Fig-
ure 5 shows the different forms of zig-zag movement of a
grouper ﬁsh in the search space.
A zigzag motion occurs when no three successive
positions of the movement are in either increasing or
decreasing order. In other words, if the array of movement
has three elements (hi, hi?1, hi?2) such that; hi \ hi?1-
\ hi?2 or hi [ hi?1 [ hi?2, the movement is not a zig-
zag. In brief, the array’s elements must be ordered in less
than ( \) and greater than ( [) order. Every element is
bigger or smaller than its neighbors. The arrays X = [1, 2,
4–6, 10] and Y = [8, 3, 6, 2, 5, 0, 8, 9] are zigzag
arrays because no three successive array elements are in
rising or decreasing order. Under the assumption that
P represents the overall number of iterations in the PS, ES,
and AC. As for the number of iterations of the PA phase
(PAss), it is equal to 1.
Therefore, the respective values of the number of iter-
ations for PS, ES, and AC denoted as; PSearch
b
c,PEnc, and
PAC can be calculated using the Eqs. (1–3) as:
PSearch ¼
P
3
 
ð1Þ
PEnc ¼
p
3
j k
ð2Þ
while
PAC ¼
P  2  P
3


ð3Þ
For
more
illustration,
assuming
P = 12,
then
PSearch ¼
12
3
 
= 4,
PEnc ¼
12
3 ¼ 4


,
and
PAC ¼ 12  2 12
3 ¼ 4


. Let S be the set of N available
search agents (groupers and moray eels), at the beginning,
the search agents are divided into two equal sets of
groupers and eels. The No. of agents in each set is
n ¼ N=2
ð4Þ
(4). The set of groupers is called G = {g1, g2, g3,………..,
gn},
while
The
set
of
eels
is
called
E = {e1,e2,-
e3,………..,en}.The next step is to randomly distribute the
groupers and eels in the search space using (5). Equation 5
distributes the search agents by generating a random
number between 0 and 1, multiplying it by the difference
Initial 
position 
Hop 1  
Hop 2 
Hop3  
Hop 4  
Hop 5  
Hop 6  
Hop 7  
Hop 8  
Final 
position
Fig. 5 Searching for the prey by a grouper ﬁsh with zig-zag movement
Neural Computing and Applications (2025) 37:63–90
69
123

---

## Page 8
between the upper and lower bounds, and then adding up
the lower bound. This ensures that each agent’s positions
fall within the speciﬁed lower and upper boundaries of the
search space, as stated in (5) [24].
Xinitial
ij
¼ lowj þ rand: upperj  lowj


; i
¼ 1; 2; 3; . . .. . .:; N; j ¼ 1; 2; 3. . .::; D
ð5Þ
where Xinitial
ij
is the initial position of ith search agent of jth
dimension,
upperandlower
are
the
upper
and
lower
boundaries of the search space, N is the number of search
agents, D is the total number of dimensions, and rand
represents a random vector that follows a uniform distri-
bution, with values ranging from 0 to 1.
After that, the objective function is calculated for each
grouper. The groupers begin to move in a zigzag form to
ﬁnd the prey (optimal solution). The zigzag movement
allows the groupers to discover new regions in search space
and increases the exploration ability of the algorithm. At
the end of this phase, the best position for each grouper is
calculated according to the objective function.
Let,Xgmj
!i ¼
Xi
gm1; Xi
gm2; Xi
gm3; Xi
gm4; . . .. . .. . .. . .. . .;
n
Xi
gmDg is the position vector of the mth grouper in the ith
iteration, where 1  i  psearch; 1  j  D, 1  m  n, n is
the total number of groupers, and psearch is the total number
of search iterations. The location vector of each grouper is
updated after each hop in the current iteration during the PS
phase and the corresponding objective function is evalu-
ated, which indicates the proximity of the grouper to the
possible prey. At the end of the current iteration, the
positions from all hops that have the best value of the
objective function will be the initial positions of the next
iteration. The updated position of a grouper can be calcu-
lated using (6), and it depends on the number of hop which
is the number of movement in the iteration. If the number
of hop is even, then the updated position will be a random
position that is greater than the current position but doesn’t
exceed the search space’s maximum boundary; if the
number is odd, the updated position will be a random
position that is less than the current position but greater
than or equal to the search space’s minimum boundary.
The optimal position of each grouper in a given iteration
is determined by the position vector that yields the maxi-
mum value of the objective function when compared to
positions created across all the hops of the iteration. After
ﬁnishing the searching phase, the best position of each
grouper is determined as the position vector that yields the
highest value of the objective function compared to all
other positions of a grouper generated during all iterations
of the PS phase. Once the best position is determined, they
initiate the PA phase from their respective best positions.
As an illustrative example, assume that we have N = 12
search agents (groupers and moray eels) in two-dimen-
sional space x1 and x2. It is assumed that x1 and x2 [ [- 6,
6], which is set to be the domain of the search space. The
number of groupers = 6, and the number of eels = 6. For
simplicity of the illustrative example, we assume that
PSearch ¼ 1; PAss ¼ 1; PEnc ¼ 1; PAtt ¼ 1 and hop = 3. The
initial position vectors for the groupers across search
agents are assigned randomly using (5). The employed
objective function is fðXÞ ¼ x2
1  x1x2 þ x2
2 þ 2x1 þ 4x2 þ
3 Following that, the grouper ﬁsh searches for prey, and its
movement is in the shape of a zig-zag in which after a
random location is imposed for each grouper ﬁsh, each of
them begins to move. The steps of the PS phase are shown
in Algorithm 1. Consider Table 1: which summarizes the
three hops in the ﬁrst iteration of groupers during the pri-
mary search process. At the initial iteration, the position of
six groupers is initialized randomly in the search space
from [-6,6], and then the grouper begins to move in zigzag
form according to no.of hop in the iteration. After the end
of the current iteration, the best position from all hops in
the iteration is selected and will be the initial position of
the next iteration until reached to the total no.of iterations
in the PS phase. Table 2 shows the best position of each
grouper from the PS phase. Table 3 shows the random
positions of the moray eels and the values of the objective
function.
The updated position of grouper
Xhopþ1
gmj
¼ Rand X
ð Þ
where; Xhop
gmj\X  maxðXgmjÞ
if No.of hop is even
Xhopþ1
gmj
¼ Rand X
ð Þ
where; min Xgmj


 X\Xhop
gmj
if No.of hop is odd
(
ð6Þ
70
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 9
Algorithm 1: The steps of the PS phase
As shown in Table 2, the best positions of g1, g3, g5, g6
are obtained from the hop 3. The best value of the objective
function of g2 is obtained from the second hop, while the
best value of g4 is obtained from the ﬁrst hop, this is
because the optimal position of each grouper in a current
iteration is identiﬁed as the vector of position that produces
the highest value of the objective function when compared
to positions generated during all the hops of iteration.
Table 3 shows the positions of eels at the start of the PA
phase. At the end of this phase, the best position for each
grouper is the position that achieves the best value of
objective function during all iterations of the PS phase and
it will be the initial position of a grouper in the PA phase.
3.3 Pair association (PA) phase
Groupers are adept predators, renowned for their rapid
bursts of velocity that render them fearsome adversaries.
Nevertheless, their substantial dimensions and unwieldy
form prevent them from capturing animals that conceal
themselves in narrow crevices and ﬁssures. In such cases,
they employ a unique strategy of seeking out moray eels to
ﬂush out their elusive prey. Both the grouper and moray eel
have distinct predatory abilities. Groupers are predatory
ﬁsh that employ an ambush strategy, utilizing their large
jaws to engulf their prey in its entirety. In addition, they
possess the ability to swiftly propel themselves through the
water in quick bursts. In contrast, moray eels possess a
body structure that enables them to maneuver through
narrow openings in the coral reef in order to reach their
prey. They lack pectoral ﬁns and gill plates, which elimi-
nates the risk of getting trapped. Through collaboration,
Neural Computing and Applications (2025) 37:63–90
71
123

---

## Page 10
these two carnivores may effectively patrol a larger area for
hunting. The grouper operates in the upper water column,
while the moray eel navigates the depths of the reef. The
utilization of these hunting methods greatly diminishes the
likelihood of their target being able to evade capture. When
trapped, the prey has two options: either remain concealed
until the moray eel retrieves it or take the chance of
swimming in the water, where the grouper’s formidable
teeth lie in wait.
During the PS phase, the search agents are distributed
randomly within the search domain, and the corresponding
objective function values are calculated and recorded.
After the PS, the PA phase occurs, where cooperation
between the groupers and the Eels allows them to discover
new areas of the search domain. The intelligence of the
grouper and its high ability to learn shows that it can
choose the best eel in the hunting process. Each grouper
ﬁsh will have an association with an eel, and this process is
called pair identiﬁcation. There are several mechanisms for
dividing the search space into pairs such as; (i) the random
association between eels and groupers i.e. the grouper can
associate with any eel, (ii)The association based on the
nearest distance between eel and grouper, but this requires
many calculations, and (iii) the association based on the
objective function of groupers and eels i.e. the grouper with
the highest value of ﬁtness function associates with the eel
that has the highest value of ﬁtness function and so on. The
Table 1 The three hops of the groupers during PS phase
Initially
First hop
Second hop
Third hop
Agent
9 1
9 2
Objective
function
Agent
9 1
9 2
Objective
function
Agent
9 1
9 2
Objective
function
Agent
9 1
9 2
Objective
function
g1
2.693
1.235
18.777619
g1
4
1.302
28.6952
g1
2.73
1.289
19.2115
g1
5
1.308
38.4029
g2
2.72
4.23
39.1457
g2
1.62
4.653
41.5889
g2
2.3
4.584
41.6959
g2
1.709
4.591
40.9339
g3
4.233
-0.283
29.5303
g3
5.843
0.84
47.9841
g3
5.73
0.657
46.5879
g3
5.904
0.734
48.8064
g4
3.398
-1.578
22.8825
g4
4.453
-2.047
36.8527
g4
4.298
-1.987
34.6091
g4
4.449
2.456
36.6208
g5
-0.568
3.235
27.4293
g5
-0.738
2.875
23.9560
g5
-0.618
3.025
25.2660
g5
-1.73
3.019
28.9461
g6
2.677
3.608
33.3114
g6
3.608
2.873
32.6140
g6
3.095
3.763
36.3347
g6
4.95
2.23
40.2569
Table 2 The best positions of the groupers from the ﬁrst iteration
Agent
Best position
Objective function
9 1
9 2
g1
5
1.308
38.4029
g2
2.3
4.584
41.6959
g3
5.9
0.734
48.8064
g4
4.45
-2.047
36.8527
g5
-1.7
3.019
28.9461
g6
4.95
2.23
40.2569
Table 3 The locations and objective functions of the eels after ran-
dom distribution
Agent
9 1
9 2
Objective function
E1
-0.568
1.833
13.91966
E2
3.871
0.0921
25.747
E3
5.113
4.067
51.3827
E4
-3.12
-4.044
-5.94494
E5
-0.874
-0.188
1.134908
E6
-4.213
-4.189
-4.53317
72
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 11
last method is applied in this paper. Figure 6 shows the
association between groupers and eels according to the
objective function. After the PA is ﬁnished, the ES phase
follows where each search agent moves towards its best
position found during the PS phase. In the AC phase, the
search agents converge towards the optimal solution.
Table 4 illustrates the descending order of eels and
groupers according to their ﬁtness function. Pair 1 consists
of grouper 3 and eel 3 (g3, e3) which have the best value of
objective function, Pair 2 consists of (g2, e2), Pair 3 con-
sists of (g6, E1), Pair 4 consists of (g1, e5), Pair 5 consists
of (g4, e6), and Pair 6 consists of (g5, e4) which have the
lowest value of objective function.
3.4 Encircling or extended search (ES) phase
Each Pair tries to encircle the prey during this phase,
moving independently so they can explore new parts of the
search region. In the open ocean, groupers have been seen
performing a sort of underwater shimmying dance to call
moray eels and indicate that they want to hunt in groups.
The ‘‘Grouper to Eel Encircling Signal’’ (GES) is the name
of this signal. On rare occasions, they will even perform an
underwater headstand, point their heads in the direction of
the ﬁsh’s hiding place, and then wiggle their bodies to
show the neighboring eel, where the prey is lurking. Rarely
when an eel ignores the signal, groupers aggressively
approach the moray and try to force it towards the intended
prey. The moray reacts to the signal by chasing the ﬁsh out
Fig. 6 The association between groupers and eels
Table 4 The association between groupers and eels according to the objective function
Eels in descending order according to objective function
Groupers in descending order according to objective function
Pairs
Agent
9 1
9 2
Objective function
Agent
9 1
9 2
Objective function
E3
5.113
4.067
51.3827
g3
5.904
0.734
48.8064
(g3, E3)
E2
3.871
0.0921
25.747
g2
2.3
4.584
41.6959
(g2, E2)
E1
-0.568
1.833
13.91966
g6
4.95
2.23
40.2569
(g6, E1)
E5
-0.874
-0.188
1.134908
g1
5
1.308
38.4029
(g1, E5)
E6
-4.213
-4.189
-4.53317
g4
4.453
-2.047
36.8527
(g4, E6)
E4
-3.12
-4.044
-5.94494
g5
-1.73
3.019
28.9461
(g5, E4)
Fig. 7 Locating the position of
the prey between a grouper and
an eel
Neural Computing and Applications (2025) 37:63–90
73
123

---

## Page 12
of its hiding place so that it may be caught in the snappy
Grouper’s jaws. Then they engage in an actual attack on
the prey and partake in the meal together, reaping the
beneﬁts of their associative hunting techniques.
The position vector of the mth grouper in D dimensional
space
can
be
represented
as
X~gmj ¼ ðxgm1; xgm2; xgm3; . . .. . .; xgmD),
and
the
position
vector of the mth eel in D dimensional space can be rep-
resented as: X~Emj ¼ ðxEm1; xEm2; xEm3; . . .. . .; xEmD). Given
the unknown location of the prey, which symbolizes the
optimal solution, it is postulated that the prospective prey is
situated in the region bounded by the grouper and the eel,
as shown in Fig. 7.
In an n-dimensional space, the formula for determining
the position of a point that lies between two other points,
while maintaining a speciﬁed distance, is an extension of
the formula used in two dimensions. Let’s assume two
points, point A (location of grouper) and point B (location
of eel). A point that lies between these two points is point C
(location of the prey) as shown in Fig. 7. The position of
the prey can be calculated as follows: First, Eq. (7) is used
to ﬁnd the differences between the coordinates (DxmjÞ of
the position of a grouper(XgmjÞ and the position of an eel
XEmj


in each dimension [31].
Dxmj ¼ XEmj  Xgmj


ð7Þ
Next, the distance between the grouper and the eel is
calculated by squaring the difference for each axis, then
summing them up and taking the square root using (8) [31].
Distance Between the grouper and the eel
¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
X
D
j¼1
Dxmj

2
v
u
u
t
ð8Þ
Finally, the coordinates of the prey in each dimension
can be calculated using (9) [31].
cmj ¼ Xgmj þ L
dis XEmj  Xgmj


ð9Þ
where cmj is the coordinates of the mth prey in each
dimension, xgmjDis the position of a grouper; xEmjD is the
position of an eel, L is the distance between the grouper
and prey, and dis is the distance between the grouper and
the eel as calculated using (8).
After locating the prey, both the grouper and the eel
begin to move toward the prey, each in its own way, as
shown in Fig. 8.
The logarithmic spiral has been selected as the primary
location update method for groupers during the ES phase.
The following requirements must be met for any other
types of spiral to be used: (i) the spiral’s initial point must
be the location of the grouper, (ii) its ﬁnal point must be
the location of the predicted prey, and (iii) the spiral’s
Moray Eel  
Encircling 
sinusoidal motion
Prey
Grouper
Encircling 
Spiral motion
Fig. 8 The grouper and the eel encircle their prey during ES phase
Fig. 9 Modelling the eel motion
in an iteration during ES phase
74
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 13
oscillation range must not exceed the search boundaries. To
update each grouper’s position, we ﬁrst calculate the dis-
tance between it and its potential prey, which is the dif-
ference between their locations using (10).
D1
! ¼ X~prey
m ið Þ  X~gm ið Þ




ð10Þ
The position of a grouper is updated many times in the
same iteration according to the number of hops (h). The
position with the best ﬁtness function value from all hops
after the end of the current iteration will be the initial
position of the second iteration and so on, until reached to
the determined number of iterations in the ES phase. The
spiral equation, as shown in (11) [32], describes the
movement of the groupers toward the prey. The updated
position of mth grouper in the following hop X~gm h þ 1
ð
Þ
depends on; D1;
! which is the distance between the mth
grouper and the prey, constant k that determines the shape
properties of the logarithmic spiral, the predicted location
of the mth prey at iteration i ðX
!
prey
m ið ÞÞ, and w which is a
value can be calculated using (12). It depends on Pencircle;
which is the number of encircling iterations, and h is the
number of hops in the iteration.
X~gm h þ 1
ð
Þ ¼ D1
!:ekw cos 2pw
ð
Þ þ X~prey
m ið Þ
ð11Þ
w ¼ 1  2  h
Pencircle
ð12Þ
A wave can have many different shapes, sine waves
being just one of them. Sine waves are a signiﬁcant shape
because they are frequently found in nature, are simple to
handle mathematically, and can be used to create any
arbitrary wave shape. As a result, sine waves have been
selected as the primary position update mechanism for
moray eels during the ES phase, as shown in Fig. 9.
The eel starts to move in a sinusoidal wave, where its
position is updated several times in the same iteration
according to the number of hops (h). First, the wavelength
(i.e. the distance between the eel and the prey
k~ ið Þ


will
be computed using (13). k~ ið Þ is the difference between the
position of mth eel at iteration i X~Em ið Þ and the position of
mth prey at iteration i X~prey
m ið Þ


.
k~ ið Þ ¼ X~Em ið Þ  X~preym ið Þ




ð13Þ
Then, using (14), the wave amplitude
g! ið Þ


will be
determined by multiplying k~ ið Þ by a factor n n has a ran-
dom value between 0 and 1.
g! ið Þ ¼ k~ ið Þ  n
ð14Þ
d1
d3
d4
d5
d6
d7
d8
d9
Fig. 10 The ﬁrst attack circle
Fig. 11 The second circle
Fig. 12 The third circle
Fig. 13 The nth circle
Neural Computing and Applications (2025) 37:63–90
75
123

---

## Page 14
The distance between the eel and the prey is divided into
hops. The distance between the current and the next hop is
calculated using (15).
The distance between the hops ¼
2p
Total no. of hops
ð15Þ
The positions of the eels will be updated using (16) [33].
The position of the eel (Xiþ1
E ) depends on a, which is a
random value, k~ ið Þ n the value of the sin angle, and the
position of the eel in the current iteration.
Xiþ1
E
¼ a  k~ ið Þ  n  sin g
ð Þ þ Xi
E
ð16Þ
After the end of the current iteration, the best position of
the eel from all hops of the iteration will be selected to be
the initial position of the next iteration.
As an illustrative example for pair 2, which consists of
g2 and e2, each iteration has three hops. In each hop, the
search agents update their positions according to the form
of their movement. In the ﬁrst iteration, the best position
for g2 is obtained from hop 3, while the best of e2 is from
hop 2, these positions are used to be the initial positions of
iteration 2 as shown in Table 5. The best positions for g2
and e2 are determined in the second iteration at hop 3 and
hop 2, respectively; these positions are utilized as the
starting points for iteration 3. The best positions in the ES
phase are obtained from iteration 3 at hop 3 for g2 and e2.
These positions are the initial positions of the next phase.
Algorithm 2 shows the steps of modeling the movement of
the groupers during the ES phase, while the steps of
updating the positions of eels are illustrated in Algorithm 3.
Algorithm 2: Modeling the grouper motion
76
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 15
Algorithm 3: Modeling the eel motion
3.5 Attacking and catching phase
At the AC phase, all search agents, whether groupers or
eels, participate in the attack on the prey after accurately
surrounding its location. In 2D space, the hypothesis relies
on forming a circle around the prey, where the prey is
located in the center of the circle. Figures 10, 11, 12, 13
show the nth attack circles, where the search agents in each
circle are assumed to be nine, as the number of attacking
circles (AB) is the number of attack iterations. In 3D space,
the hypothesis relies on forming a ball around the prey
called the ‘‘attack ball’’ as shown in Fig. 14.
Neural Computing and Applications (2025) 37:63–90
77
123

---

## Page 16
The steps for forming the circle around the predicted
prey are as follows; at ﬁrst, the location of the agent with
the best ﬁtness function is assumed to be the location of the
predicted prey. Then the distance between the predicted
prey and all other agents is calculated. After that, a circle
around the prey is formed and the radius (R) of the circle is
the distance between the prey and the farthest agent. For
the large number of search agents and to reduce the com-
plexity of computation, the radius of the next circle can be
calculated using (17).
Riþ1 ¼ 1  l
ð
Þ  Ri
ð17Þ
, where i = 1, 2, 3, ….., AB-1 and l is a shrinking ratio. For
example, if the distance between the prey and the farthest
agent is equal to 100 and l = 0.2, then the radius of the ﬁrst
circle (R1 = 100). The radius of the second circle is equal
to (1-0.2)*100 = 80. The radius of the third is equal to
(1-0.2)*80 = 64 and so on.
After determining the radius of the second circle, the
search agent will be randomly distributed within the circle
by using the steps of Algorithm 4. In each attacking iter-
ation, the search agents get much closer and closer to the
prey as shown in Figs. 10, 11, 12, 13. The process works
until the number of attacking iterations is reached, and
ﬁnally, the agents catch the prey in the last iteration.
Algorithm 5 shows the steps for generating random points
inside a sphere. Algorithm 6 shows the steps of generating
random points inside the N-dimensional sphere. Algorithm
7 shows the steps of the AC phase.
Algorithm 4: Generating random points inside a circle
Algorithm 5: Generating random points inside a sphere
Algorithm 6: Generating random points inside N-dimensional sphere
78
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 17
Algorithm 7: The steps of AC phase
3.6 Case study: feature selection using GME
optimization algorithm
Due to the exponential rise in data, the quality of infor-
mation (data) is essential for gradually merging data pro-
cessing through pattern recognition, data mining, image
processing, and various ML techniques. Curse of dimen-
sionality (CoD) is one of the NP-hard challenges in data
science because of the big-scale data sets. Therefore, sev-
eral researchers have applied nature-inspired algorithms to
solve large-scale data analytics difﬁculties. Due to over-
ﬁtting in the ML model, large-dimensional data may result
in the majority of noisy, irrelevant, and redundant data.
Dimensionality reduction techniques might be used to
address these problems, and the use of machine learning
(ML) algorithms should be done as a part of the prepro-
cessing stage. The two most popular dimensionality
reduction techniques are feature selection (FS) and feature
extraction (FE), where FS cleans up the noisy, redundant,
and
inconsequential
data,
potentially
improving
the
Fig. 14 The search agent form the attacking ball around the prey in
the search space
Neural Computing and Applications (2025) 37:63–90
79
123

---

## Page 18
effectiveness of an algorithm [34, 35]. Choosing the best
features will reduce computational modelling costs while
increasing the accuracy of ML models. Furthermore, it
increases learning convergence while decreasing storage
demand. As a result, metaheuristic algorithms are now
being employed to overcome these problems [36]. Fig-
ure 15 depicts the beneﬁts of sectioning the best features.
GME is designed to handle continuous optimization
problems in which each agent changes its position inside a
real-valued search region bounded by the constraints of the
particular task. FS is a binary optimization issue in which
the search agents can only use binary 0 and 1 values. As a
result, without adjustments, the algorithm described above
cannot be employed to solve these issues. It is necessary to
create a binary version of GME called (BGME) that can be
applied to the FS issue. Each solution in this study is
denoted by a one-dimensional vector, with its length
determined by the number of features in the dataset. Each
element in the vector can be assigned one of two values: 1
or 0. A value of 1 indicates that the corresponding feature
is selected, while a value of zero indicates that the feature
is not selected, as shown in Fig. 16. As a result, to employ
the GME for the FS problem, a mapping mechanism from
actual values to binary space should be applied. The sug-
gested BGME’s usefulness will be assessed in FS by
identifying the most signiﬁcant features for diagnosing
Coronary Heart Disease (CHD). Using the proposed GME,
the most informative features for CHD diagnosis will be
chosen during the FS.
The process of applying the proposed BGME to choose
the optimal subset of features from the CHD dataset
involves several consecutive steps. BGME commences
with a search agent (S) possessing a collection of search
agents denoted by Y. For instance, S consists of N search
agents, hence including Y = {Y1,Y2,….,Ym,….,YN}. Each
agent, denoted as Ym, within the set S indicates a potential
solution. In other words, a solution would indicate the
Fig. 15 The advantages of feature selection
Features of CHD dataset
All features are selected 
Feature selection using BGME optimization 
The best solution is obtained  
Selected features are: - {f1,f4,……, ff}
F1
F2
F3
F4
F5
…….
…….
Fd-1
Fd
1
1
1
1
1
…….
…….
1
1
1
0
0
1
1
…….
…….
0
1
Fig. 16 The representation of the selected/unselected features
Continuous 
Search Space
Discrete 
Search Space
Transfer Function
Solution
Iteration i
Solution
Iteration i+1
Rand 
0, 1 
Update
0 or 1
Fig. 17 Mapping process from
continuous search space to
discrete search space
80
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 19
number of features that have been selected to minimize the
dimensionality of a particular data set. This process is
repeated for every employed population in the F-dimen-
sional search space, where F represents the total number of
features. In the CHD dataset, the mth agent can be repre-
sented as Ym = (Y1
m, Y2
m,….., Yf
m).
The position (bit) value (i = 1, 2,…, f) of each agent is a
binary value that represents whether the ith feature picked
(one) or not chosen (zero). The assessment of these search
agents should be conducted by utilizing the accuracy value
of the KNN classiﬁer as a ﬁtness function. This evaluation
is performed after randomly generating S, which consists of
N search agents in a binary space. The evaluation function
can be mathematically represented using (18).
Fitness Ym
ð
Þ ¼ AccofKNN Ym
ð
Þ
ð18Þ
where the ﬁtness value of the mth search agent is denoted
as; Fitness (Ym), the accuracy of the KNN classiﬁer,
denoted as Acc of KNN (Ym), is calculated based on the
subset of selected features in the mth search agent. The
collection of groupers and moray eels (search agents)
represented by S is distributed randomly in the search
space. At the beginning, it is necessary to determine the
total number of iterations (P) to calculate the total number
of iterations in each phase of GME, and the number of hops
for the zig-zag movement (hop).In the PS phase, the
groupers begin to move and the position of each grouper is
updated according to the number of hops if it is even or
odd. The mth grouper’s new position has a continuous
value; as a result, a transfer function must be applied in
order to transform this position into a binary value. The
transfer function is regarded as a key component of
metaheuristic-based FS methods due to its ability to map
the continuous search areas into discrete search areas.
The most prevalent example of a sigmoid function that
can be applied to translate the continuous values of the
positions of the search agents to the binary values is the
logistic sigmoid function. It has an ‘‘S’’-shaped curve when
plotted [37], and can be calculated using (19).
sigmoid Yi
m


¼
1
1 þ eYim
ð19Þ
where the natural logarithm’s base is e, and the expression
‘‘rand (0, 1)’’ represents a random value that falls within
the range of 0–1. Based on a solution’s position, it creates a
probability value, and then uses this probability value to
convert the solution to binary as shown in Fig. 17. The
binary solution’s component can be updated between 0 and
1 and vice versa. Sigmoid (Yi
m) is the sigmoid function that
depicts the likelihood that the ith bit will take a value of 0
or 1 as determined by applying (20) [37]. If the value of
rand (0,1) is greater than or equal to the value of sigmoid
(Yi
m), then the binary value of the updated position of the
mth individual at the mth bit
Yi
binarym i þ 1
ð
Þ


will be 1,
otherwise, it will be 0.
Yi
binary
m i þ 1
ð
Þ ¼
1
if rand 0; 1
ð
Þ  sigmoid Yi
m


0
otherwise

ð20Þ
Based on the updated position Yi
binary
m i þ 1
ð
Þ for each
individual, the ﬁtness function in (18) is used to evaluate
each individual in S. During their search for the prey, each
individual in S stores the updated positions and the eval-
uation values. Up until the Psearch is ﬁnished, the PS pha-
se’s steps will be carried out. The optimal location for the
agent at the end of the PS phase in S is the position that
enables it to achieve the highest ﬁtness value during its
search for prey. After the objective function is calculated
for all groupers and eels, they will be ordered in
descending order. The intelligence and high ability to learn
of the grouper ﬁsh shows that it can choose the best eel in
the hunting process. Each grouper ﬁsh will have an asso-
ciation with an eel. Theoretically in the associative phase,
the best grouper (i.e. the grouper with the best value of
ﬁtness function) will associate with the best eel (i.e. the eel
with the best value of ﬁtness function), and so on for the
rest of search agents i.e., the association will be according
to the value of the ﬁtness function.
In the encircling phase, both the grouper and the eel
begin to surround the prey, as each of them moves from the
best positions of the previous phase. According to the
number of encircling iterations (Pencircle) and the number of
hops, the grouper begins to move in the form of a loga-
rithmic spiral, and the eel moves in the form of a sinusoidal
wave.
At
ﬁrst,
the
positions
of
the
potential
prey
X~prey tð Þwill be calculated for each pair, and to transform
the continuous values of positions to binary values, the
sigmoid function will be used. Then, the groupers and eels
will update their positions according to the equations
explained in the previous section. The ﬁtness function is
used to evaluate the updated positions. The positions that
achieve the best values of ﬁtness functions will be used to
be the initial positions of the search agents in the AC phase.
The search agent with the highest ﬁtness function value
will become the prey. Then, the distance between all other
agents and the expected prey is determined. The circle’s
radius (R) is set to be equal to the distance between the
prey and the farthest agent. To accommodate the enormous
number of search agents and to simplify computation, the
shrinking ratio is used to determine the radius of the fol-
lowing circles using (17). The ﬁtness function will be
calculated to locate the predicted prey and draw a circle
with a new radius around it. The search agent will be
dispersed at random inside the circle once its radius has
Neural Computing and Applications (2025) 37:63–90
81
123

---

## Page 20
been determined. The procedure continues until the number
of attacking iterations (PAC) is reached, at which the agents
capture the prey in the last iteration. Finally, the ﬁttest
search agent provides the best solution with the best
combination of features. It should be emphasized that
separating iterations into four phases (PS, PA, ES, and AC)
allows the BGME algorithm to deliver a quick and accurate
subset of features. Also, it allows each phase to try
numerous times to ﬁnd the optimum solution before exe-
cuting the next phase, and the following phases are
implemented more rapidly and precisely. The feature has a
‘‘1’ value in the ﬁttest solution is a selected feature but if
the value is 0, this feature is not selected. Optimizing
feature selection can lead to cost reduction in computa-
tional modeling and enhance the accuracy of ML models.
Moreover, it enhances the rate at which learning reaches a
stable state while reducing the amount of storage required.
4 Results and discussion
This section evaluates the GME algorithm’s performance
and compares it with seven well-known algorithms which
are; CO [23], FFA [24], HCOA [25], ISSA [26], OOA [27],
RTH [28], WaOA [7]. The experiments were executed
using Python on an Intel(R) Core(TM) i7-8550U CPU @
1.80 GHz 2.00 GHz with 16 GB RAM running Windows
11. To assess the efﬁcacy of the proposed algorithm in
comparison with existing optimization algorithms, we
conducted a thorough comparison between our proposed
BGME algorithm
and
other optimization
algorithms.
There are many common parameters for the proposed
algorithm as well as the other algorithms. These parameters
are such as; Population size, and number of iterations. The
population size is set to 25, 50, 75, and 100. The number of
iterations is set to 60, 120, 180, and 240. To assess the
performance of the proposed algorithm in comparison to all
baseline algorithms, we employed three metrics: classiﬁ-
cation accuracy, no.of selected features, and execution
time. The following subsection will discuss one-by-one
evaluation metrics results.
4.1 The used dataset and employed parameters
Heart disease is an umbrella term encompassing several
illnesses that impact the anatomy and function of the heart.
CHD is a cardiovascular condition characterized by
insufﬁcient delivery of oxygenated blood to the heart due
Table 5 The results of the illustrative example during the ES phase for pair 2 (g2, e2)
Agent 1 (g2,e2)
Iteration
1
Grouper
position
Eel position
Prey position
Hop
number
New grouper
position
Objective
function
New eel
position
Objective
function
X1
X2
X1
X2
X1
X2
X1
X2
X1
X2
2.3
4.584
3.871
0.0921
4.185
-0.80628
1
5.677
3.459
52.746
3.851
0.335
25.695
2
2.325
6
59.106
3.979
0.699
27.291
3
6.000
4.998
65.984
3.884
0.430
26.092
Agent 1 (g2,e2)
Iteration
2
Grouper
position
Eel position
Prey position
Hop
number
New grouper
position
Objective
function
New eel
position
Objective
function
X1
X2
X1
X2
X1
X2
X1
X2
X1
X2
6
4.998
3.979
0.699
3.57480
-0.1608
1
5.587
4.921
61.795
4.144
1.0304
29.378
2
4.009
5.251
54.616
4.377
1.496
32.586
3
6.000
5.395
69.316
4.359
1.4612
32.333
Agent 1 (g2,e2)
Iteration
3
Grouper
position
Eel
position
Prey
position
Hop
number
New
grouper
position
Objective
function
New
eel
position
Objective
function
X1
X2
X1
X2
X1
X2
X1
X2
X1
X2
6
5.395
4.376
1.496
4.05120
0.71620
1
5.8352
5.7182
70.9236
4.505
1.754
34.497
2
5.8000
5.8600
72.032
4.583
1.911
35.708
3
6.00
5.8546
73.5676
4.580
5.904
64.563
82
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 21
to narrowed or blocked arteries. It is the primary cause of
death in the United States. According to the Centers for
Disease Control and Prevention, there are 18.2 million
American adults who suffer from coronary artery disease,
which is the predominant form of heart disease in the
nation. Therefore, it is crucial to accurately diagnose car-
diovascular disease [38]. The CHD Dataset is utilized to do
a comparative analysis between the proposed BGME
algorithms and the other optimization algorithms [39]. The
Cleveland dataset consists of 303 observations, 13 features,
and 1 target attribute. Furthermore, the thirteen features
encompass supplementary patient data that is pertinent to
the non-invasive diagnostic test results described before.
The target variable represents the result of the invasive
coronary angiography operation, indicating whether or not
the patient has coronary artery disease. A score of 0 sig-
niﬁes the lack of CHD, whereas labels 1–4 indicate the
existence of CHD. The primary aim of most studies uti-
lizing this dataset has been to distinguish between the
presence (values 1, 2, 3, 4) and absence (value) of a
particular phenomenon. The dataset’s characteristics are
explained in Table 6. Figure 18 displays a snapshot from
the CHD Dataset.
All nature-inspired algorithms generally require both
common control parameters (also referred to as regular
parameters) and algorithm-speciﬁc control parameters
(often referred to as dependent parameters). Commonly
employed are control parameters that are not reliant on the
speciﬁc problem, such as population size, number of
dimensions, number of iterations, and so on. The problem-
dependent parameters refer to control parameters that are
speciﬁc to the algorithm being used. The values of these
parameters are subject to variation depending on the
problem. For illustration, the Genetic Algorithm (GA)
necessitates the speciﬁcation of a mutation probability and
a crossover probability, whereas the particle swarm opti-
mization (PSO) demands the determination of an inertia
weight and learning factors. These dependent variables
may impact the algorithm’s performance. As shown in
Table 7, the proposed algorithm may seem to use more
Table 6 Features of CHD dataset
Feature
Description
Age
Years of age
Sex
Sex (1 represents males and 0 represents females)
CP
Type of chest pain:
Value 1: angina typical
Value 2: Angina atypical
Value 3: non-angina discomfort
Value 4: Asymptomatic
Trestbps
stationary blood pressure at the time of hospital admission, measured in millibars Hg
chol
Cholesterol serum concentration in milligrams per deciliter
FBS
Fasting blood glucose levels exceeding 120 mg/dL (1 = true; 0 = false)
RECG
Resting electrocardiographic ﬁndings (RECG)
Value 0: normal
Value 1: ST-T wave abnormality (T wave inversions and/or ST elevation or depression greater than 0.05 mV)
Value 2: left ventricular hypertrophy that is probable or certain according to Estes’ criteria
thalach
Attainment of the maximal heart rate
Exang
Exercise induced angina (1 = yes; 0 = no)
Old peak
ST depression induced by exercise as opposed to relaxation
Slope
The slope of the ST segment during maximal exercise
Value 1: upsloping
Value 2: ﬂat
Value 3: down sloping
Ca
The quantity of main vessels (0–3) that are coloured with ﬂuoroscopy in order to calcify the vessels
Thal
Outcomes of the nuclear stress test are as follows: three indicate a normal condition, six a ﬁxed defect, and seven a reversible defect
Num
Target variable denoting the angiographic disease status (diagnosis of cardiac disease) in any major vessel
Negative 50% diameter reduction (Value0)
Value 1: Diameter narrowing exceeding 50%
Neural Computing and Applications (2025) 37:63–90
83
123

---

## Page 22
speciﬁc control parameters compared to other algorithms.
However, as will be shown in the results, the high efﬁ-
ciency of the GME has been proven using this relatively
limited number of parameters when compared with other
algorithms that may use a smaller number of speciﬁc
parameters but give bad results.
4.2 Evaluating the performance of BGME
and comparing it with other optimization
algorithms
The Figs. 19, 20, 21, 22 show the comparisons between
different algorithms based on execution time. The execu-
tion time is measured according to different number of
iterations i.e. (60, 120, 180, and 240), and different num-
bers of search agents i.e. (25, 50, 75, and 100). The results
demonstrate that the proposed GME has shown better
execution time than all other algorithms. At no.of search
agent = 25, and no.of iteration = 60, the execution time of
CO, FFA, HCOA, ISSA, OOA, RTH, WaoA, and GME is
404, 313, 560, 765, 652, 740, 810 and 218. At no.of search
of search agent = 25 and no.of iteration = 240, the exe-
cution time of CO, FFA, HCOA, ISSA, OOA, RTH,
WaoA, and GME is 1248, 904, 1205, 1390, 1789, 2020,
2056, and 680. The results of execution time at no.of
search agent = 50, and no.of iteration = 60 for CO, FFA,
HCOA,
ISSA,
OOA,
RTH,
WaoA,
and
GME
is
780,594,990,1374,1340,1376,1432 and 459. The results of
execution time for CO, FFA, HCOA, ISSA, OOA, RTH,
WaoA, and GME is 1789, 1460, 1973, 2286, 2116, 2639,
2369, and 1043 for no.of iterations = 240. Furthermore,
when the number of iterations equals 60, and the no.of
search agents equals 75, the execution time is 1298,1 289,
1234, 1560, 1532, 1604, 1757 and 1123, and when the
no.of iterations = 240, the results obtained are 2123, 1707,
2119, 2562, 2641, 2903, 2569, and 1584 for CO, FFA,
HCOA, ISSA, OOA, RTH, WaoA, and GME, respectively.
Finally, the results are 1567, 1480, 1643, 1966, 1984, 1918,
1934, 1210 at no.of search agents equals 100 and no.of
iterations equals 60 but when the no.of search agents equals
240, the results are; 2314, 2110, 2780, 3080, 2916, 3014,
2943, and 1921 for CO, FFA, HCOA, ISSA, OOA, RTH,
WaoA, and GME, respectively. Consequently, the accuracy
and execution time of the BGME technique increase
gradually with the number of iterations and the number of
search agents as shown in Figs. 19, 20,21, 22, 23, 24, 25,
26. The smallest value of the execution time is for GME at
no.of iteration = 60 and no.of search agents = 25, but the
largest value is for ISSA at no.of iteration = 240 and no.of
search agents = 100. The best values for the execution time
according to different no. of search agents and no.of iter-
ations is for GME. Table 8 summarizes the results of the
execution time in seconds for all optimization algorithms.
The accuracy comparisons for various algorithms can be
measured in terms of the number of search agents (25, 50,
75, and 100) and the number of iterations (60, 120, 180,
and 240) as illustrated in Figs. 23, 24, 25, 26. The proposed
GME has demonstrated the largest value of accuracy. As
shown in Fig. 23, at an iteration count of 60 and number of
search agents equal to 25, the accuracy for CO, FFA,
Fig. 18 Snapshot from the CHD dataset
84
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 23
HCOA, ISSA, OOA, RTH, WaoA, and GME is as follows:
66.3, 70.2, 75.66, 74.2, 81.2, 68.9, 78.32, and 79.2. At 240
iterations and 25 search agents, the accuracy of the
following algorithms is determined: CO, FFA, HCOA,
ISSA, OOA, RTH, WaoA, and GME: 68.53, 74.02, 79.73,
78.04, 83.72, 74.43, 82.34, and 84.12. As the number of
Table 7 The Speciﬁc control parameters for the different algorithms
Parameter
Description
Assigned Value
GME
N
Number of search agents
25, 50, 75, and 100
P
Total number of iterations
60, 120, 180, and 240
hop (h)
Number of hops in the grouper’s movement
3
K
Constant deﬁne the shape of logarithmic spiral
Each agent has its own
value
H
Number of hops in the eel’s movement
3
n
Factor between 0 and 1
[0,1]
a
Random value
0.3
H
Angle may ﬂuctuate anywhere from 0 to 2p
0 to 2p
U
Angle may ﬂuctuate anywhere from 0 to p
0 to p
l
Shrinking ratio to determine the radius (R)
0.2
CO
rˆ -1
i,j
Randomization term
0.4
%1.%2 at
i,j
%1.%2 Randomization term
%1.%2 9 t/T
rˇi,j
Turning factor reﬂects the sharp turns of the cheetahs in the capturing mode
0.5
bt
i,j
interaction factor between the cheetah and leader
0.6
r1
Random number
Random number from [0,
1]
FFA
R
r is a random number
Random number from [0,
1]
I
I is a random number
Random number from the
set {1, 2}
HCOA
GD(a, d)
The Gaussian distribution, characterized by a mean value a and a standard deviation d, is
employed to model the distribution of houses
Pcandidate
t?1(c) = GD(a,
d)
GD(b,k)
The Gaussian distribution, characterized by its mean b and standard deviation, is employed to
model the distribution of dwellings
Candiate_pbestt?1(c,
x) = GD(b, k)
ISSA
C1
C1 is used to balance between exploration and exploitation
c1 = 2e-( 4I L)2
C2
C2 are random numbers that are uniformly distributed between 0 and 1
Random number [ 0, 1]
C3
C3 are random numbers that are uniformly distributed between 0 and 1
Random number [ 0, 1]
R
r is a random numbers that are uniformly distributed between 0 and 1
Random number [ 0, 1]
gm
gm is a non-negative number that quantiﬁes the dispersion index
1
Pm
Pm [ (0, 1) is the probability of the new candidate solution moving according to a probability
distribution
0.5
d j
k
d j k is a numerical representation derived from the chosen probability distribution
Depend on the probability
distribution
Pa
fraction (Pa) of the elite and humble candidate solutions
0.2
OOA
ri,j
Random number
Random number [0, 1]
Ii,j
Ii,j are random numbers
Random number from the
set {1, 2}
RTH
A
A denotes the angel gain and its range between [5–15]
15
R0
represents the initial value of the radius and its range between [0.5–3]
0.5
R
r is a control gain and its range between [1, 2]
1.5
WaOA
Ii,j
Ii,j is integer selected randomly between 1 or 2 and it is used to increase the algorithm’s
exploration ability
2
randi,j
randi,j is a random numbers from [0, 1]
Random from the interval
[0, 1]
Neural Computing and Applications (2025) 37:63–90
85
123

---

## Page 24
iterations is 60 and the number of search agents is 50, the
accuracy for CO, FFA, HCOA, ISSA, OOA, RTH, WaoA,
and GME is 72.4, 76.11, 80.60, 78.6, 85.09, 76.60, 85.6,
and 78.50, respectively. For 240 iterations, the results for
CO, FFA, HCOA, ISSA, OOA, RTH, WaoA, and GME are
as follows: 76.70, 78.30, 82.60, 84.32, 88.35, 84.5, 78.90,
and 92.13 as shown in Fig. 24.In addition, when the
number of search agents is 75 and the number of iterations
is 60, the accuracy is as follows: 79.4, 80.1, 84.77, 86.40,
89.2, 86.05, 89.54, and 94.67. Similarly, when the number
of iterations is set to 240, the corresponding accuracy for
CO, FFA, HCOA, ISSA, OOA, RTH, WaoA, and GME is
82.45, 80.9, 86.5, 88.9, 94.10, 89.21, 93.65, and 97.4 as
shown in Fig. 25. When the number of iterations is 60 and
the number of search agents is 100, the ﬁnal results are
83.10, 82.04, 78.3, 89.53, 94.88, 91.3, 94.11, and 97.87.
However, when the number of search agents is increased to
240, the results are as follows: 83.25, 84, 88.70, 90.87,
95.70, 92.89, 95.21, and 98.6 for CO, FFA, HCOA, ISSA,
OOA, RTH, WaoA, and GME, respectively as illustrated in
Fig. 26.
As illustrated in the Figs. 23, 24, 25, 26 the accuracy of
the BGME method progressively improves as the number
of iterations and search agents increases. The smallest
value of accuracy for GME is at iteration count = 60 and
number of search agents = 25, while its largest value is at
iteration count = 240 and number of search agents = 100.
GME provides the most optimal accuracy values when
varying the number of search agents and iterations. Table 9
provides a summary of the accuracy of each optimization
algorithm. Table 9 demonstrates that the proposed BGME
has shown better classiﬁcation accuracy than all other
algorithms on the CHD dataset. BGME outperformed all
other algorithms with average accuracy 15.38% higher than
CO,14.63% higher than FFA,9.93% higher than HCOA,
7.76% higher than ISSA, 2.93% higher than OOA, 5.74%
higher than RTH, and 3.42% higher thanWaoA.
The average amount of selected features for BGME and
other optimization algorithms across 240 iterations is pre-
sented in Table 10. In comparison to other algorithms,
Fig. 19 Execution time of GME and its competitors according to no
of search agent = 25
Fig. 20 Execution time of GME and its competitors according to no
of search agent = 75
Fig. 21 Execution time of GME and its competitors according to no
of search agent = 50
Fig. 22 Execution time of GME and its competitors according to no
of search agent = 100
86
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 25
BGME has chosen the fewest minimum number of features
in the CHD Dataset, as illustrated in Table 10. In contrast,
the classiﬁcation accuracy of BGME achieved on the
dataset was 98.63. In comparison to all other algorithms, it
is evident from this observation that BGME achieves a
robust equilibrium between the minimum number of
selected features and the classiﬁcation accuracy. Conse-
quently, this analysis suggests that the BGME prioritizes
the selection of informative features that are critical for
achieving higher accuracy in classiﬁcation. Fig. 27 shows
the convergence rate of the GME optimizations algorithm
and the error goes approximately to zero at 360 iterations.
5 Conclusions and future research
Finding the ideal combination of a group of decision
variables to address a certain issue is the process of opti-
mization. Optimization has been used in a wide range of
ﬁelds, disciplines, and applications. Some problems require
Fig. 23 Accuracy of GME and its competitors according to no of
search agents = 25
Fig. 24 Accuracy of GME and its competitors according to no of
search agents = 50
Table 8 The execution time in
(sec) according to different no
of iterations and different no of
search agent
Optimization algorithm
No.of search agents = 25
No.of search agents = 50
Numbers of iterations
Numbers of iterations
60
120
180
240
60
120
180
240
CO
404
753
1020
1284
780
1139
1589
1789
FFA
313
489
669
904
594
965
1138
1460
HCOA
560
710
970
1205
990
1356
1560
1973
ISSA
765
954
1180
1390
1374
1753
2098
2286
OOA
652
912
1489
1789
1340
1670
1997
2116
RTH
740
1321
1753
2020
1376
1864
2346
2639
WaoA
810
1390
1789
2056
1432
1798
2087
2369
GME
218
430
640
680
459
767
975
1043
Optimization algorithm
No.of search agents = 75
No.of search agents = 100
Numbers of iterations
Numbers of iterations
60
120
180
240
60
120
180
240
CO
1298
1507
1678
2123
1567
1854
2090
2314
FFA
1289
1568
1690
1707
1480
1835
2090
2110
HCOA
1234
1690
1879
2119
1643
2015
2498
2780
ISSA
1560
2004
2270
2562
1966
2417
2744
3080
OOA
1532
1932
2356
2641
1984
2254
2864
2916
RTH
1604
2180
2675
2903
1918
2790
2893
3014
WaoA
1757
1997
2310
2569
1934
2130
2670
2943
GME
1123
1289
1410
1584
1210
1419
1754
1921
Neural Computing and Applications (2025) 37:63–90
87
123

---

## Page 26
solutions, while others require improvements to their pre-
sent best solution where the need for more sustainable
solutions is continuously growing. To handle these prob-
lems, this paper proposed a new swarm intelligence opti-
mization algorithm inspired by the cooperation in hunting
between different species (groupers and moray eels) which
is extremely rare. While, this associative behavior appears
Fig. 25 Accuracy of GME and its competitors according to no of
search agents = 75
Fig. 26 Accuracy of GME and its competitors according to no of
search agents = 100
Table 9 The accuracy of GME
and other optimization
techniques according to
different no of iterations and
different no of search agents
Optimization algorithm
No.of search agents = 25
No.of search agents = 50
Numbers of iterations
Numbers of iterations
60 (%)
120 (%)
180 (%)
240 (%)
60 (%)
120(%)
180 (%)
240 (%)
CO
66.30
65.60
66.21
68.53
72.40
73.02
74.44
76.70
FFA
70.20
71.80
73.65
74.02
76.11
77.40
77.98
78.30
HCOA
75.66
77.80
79.03
79.73
80.60
81.22
81.94
82.60
ISSA
74.20
76.10
76.97
78.04
78.60
79.31
82.05
84.32
OOA
81.20
81.75
82.30
83.72
85.09
86.44
86.90
88.35
RTH
68.90
72.40
73.86
74.43
76.60
78.53
81.30
84.50
WaoA
78.32
78.90
81.74
82.34
85.60
86.19
87.09
87.90
GME
79.20
80.30
82.56
84.12
87.50
89.40
90.89
92.13
Optimization algorithm
No.of search agents = 75
No.of search agents = 100
Numbers of iterations
Numbers of iterations
60 (%)
120 (%)
180 (%)
240 (%)
60 (%)
120 (%)
180 (%)
240 (%)
CO
79.40
79.63
81.30
82.45
83.10
83.15
83.20
83.25
FFA
80.10
80.34
80.67
80.90
82.04
82.90
82.96
84.00
HCOA
84.77
85.64
86.06
86.50
87.30
88.67
88.68
88.70
ISSA
86.40
87.30
87.65
88.90
89.53
90.20
90.63
90.87
OOA
89.20
91.80
93.50
94.10
94.88
95.02
95.63
95.70
RTH
86.05
88.10
88.92
89.21
91.30
91.87
92.35
92.89
WaoA
89.54
91.42
91.98
93.65
94.11
94.76
94.90
95.21
GME
94.67
96.14
96.88
97.40
97.87
98.59
98.60
98.63
Table 10 The no of selected features by GME and other optimization
algorithms
No.of features in data set = 13
Optimization algorithms
No.of selected features
CO
11
FFA
10
HCOA
9
ISSA
9
OOA
8
RTH
9
WaoA
8
GME
7
88
Neural Computing and Applications (2025) 37:63–90
123

---

## Page 27
to be evidence of high intelligence, it could be the product
of evolutionary adaptation driven by the rewards of com-
bined hunting. The grouper and moray eel may have sim-
ply discovered that hunting together boosts their chances of
success over time. The two predators have complementary
hunting abilities, and an associated hunt creates a multi-
predator attack that is difﬁcult to evade. The marine
environment still has so many secrets we have yet to
uncover.
GME consists of four phases which are; primary search,
pair
association,
encircling
or
extended
search,
and
attacking and catching. The balance of exploitation and
exploration is a key component of GME;s success. One of
GME’s advantages is that it requires less time because it
requires fewer iterative steps. Using the No Free Lunch
theory from optimization, the binary version of GME
(BGME) has the potential to outperform existing algo-
rithms in binary issues like feature selection. According to
the experimental results, GME outperformed the other
algorithms and earned the best overall performance. Also,
as a result of its capacity to select the most informative
features, while discarding unnecessary data, we recom-
mend this algorithm as an alternative to solving binary
problems. Furthermore, the suggested algorithm is capable
of investigating unexplored areas by other state-of-the-art
algorithms. Future research could focus on the performance
of integrating the GME algorithm with other optimization
methods or investigating the performance of the GME on a
broader range of real-world problems. It is also suggested
that the proposed hunting strategies be hybridized with
other evolutionary algorithms.
Funding Open access funding provided by The Science, Technology
& Innovation Funding Authority (STDF) in cooperation with The
Egyptian Knowledge Bank (EKB). This research did not receive any
funds from any of the supporting institutions or companies.
Data availability Data will be made available on request.
Declarations
Conflict of interest The authors declare that they have no conflict of
interest.
Human or animal rights This paper does not contain any studies with
human participants or animals performed by any of the authors.
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
1. Benmessahel I, Xie K, Chellal M (2020) A new competitive
multiverse optimization technique for solving single-objective
and multiobjective problems. Eng Reports 2(3):1–33. https://doi.
org/10.1002/eng2.12124
2. Kumar SR, Singh KD (2021) Nature-inspired optimization
algorithms: research direction and survey. Neural Evol Comput.
http://arxiv.org/abs/2102.04013
3. Xie L, Han T, Zhou H, Zhang ZR, Han B, Tang A (2021) Tuna
swarm optimization: a novel swarm-based metaheuristic algo-
rithm for global optimization. Comput Intell Neurosci. https://doi.
org/10.1155/2021/9210050
4. Dhiman G (2021) ESA: a hybrid bio-inspired metaheuristic
optimization approach for engineering problems. Eng Comput
37(1):323–353. https://doi.org/10.1007/s00366-019-00826-w
5. Rajakumar R, Dhavachelvan P, Vengattaraman T (2016) A sur-
vey on nature inspired meta-heuristic algorithms with its domain
speciﬁcations. 2016, International Conference on Communication
and Electronics Systems (ICCES), Coimbatore, India. https://doi.
org/10.1109/CESYS.2016.7889811
6. Kumar A, Nadeem M, Banka H (2023) Nature inspired opti-
mization algorithms: a comprehensive overview. Evol Syst
14(1):141–156. https://doi.org/10.1007/s12530-022-09432-6
7. Trojovsky´ P, Dehghani M (2023) A new bio-inspired meta-
heuristic algorithm for solving optimization problems based on
walruses behavior. Sci Rep. https://doi.org/10.1038/s41598-023-
35863-5
8. Sathiyaraj C, Ramachandran M, Amudha M, Kurinjimalar R
(2022) A review on hill climbing optimization methodology.
Recent trends Manag Commer 3(1):1–7. https://doi.org/10.46632/
rmc/3/1/1
9. Fraˇsinaru C, Raˇschip M (2019) Greedy best-ﬁrst search for the
optimal-size sorting network problem. Procedia Comput Sci
159:447–454. https://doi.org/10.1016/j.procs.2019.09.199
10. Dragoi EN, Daﬁnescu V (2021) Review of metaheuristics
inspired from the animal kingdom. Mathematics 9(18):1–52.
https://doi.org/10.3390/math9182335
Fig. 27 The convergence rate for GME optimization technique
Neural Computing and Applications (2025) 37:63–90
89
123

---

## Page 28
11 LeelaKumari Ch, Kamboj VK, Bath SK, Tripathi SL, Khatri M,
Sehgal S (2023) A boosted chimp optimizer for numerical and
engineering
design
optimization
challenges.
Eng
Comput
39(4):2463–2514. https://doi.org/10.1007/s00366-021-01591-5
12. Peraza-Va´zquez H, Pen˜a-Delgado AF, Echavarrı´a-Castillo G,
Morales-Cepeda AB, Velasco-A´ lvarez J, Ruiz-Perez F (2021) A
bio-inspired method for engineering design optimization inspired
by dingoes hunting strategies. Math Probl Eng. https://doi.org/10.
1155/2021/9107547
13. Monga P, Sharma M, Sharma SK (2022) A comprehensive meta-
analysis of emerging swarm intelligent computing techniques and
their research trend. J King Saud Univ - Comput Inf Sci
34(10):9622–9643. https://doi.org/10.1016/j.jksuci.2021.11.016
14. Vahidi B, ForoughiNematolahi A (2019) Physical and physic-
chemical based optimization methods: a review. J Soft Comput
Civ
Eng
3(4):12–27.
https://doi.org/10.22115/SCCE.2020.
214959.1161
15 Nayak J et al (2018) 2018 ‘‘Chemical reaction optimization: a
survey with application and challenges.’’ Adv Intell Syst Comput
758:507–524. https://doi.org/10.1007/978-981-13-0514-6_50
16. MacEdo M et al (2021) Overview on binary optimization using
swarm-inspired algorithms. IEEE Access 9:149814–149858.
https://doi.org/10.1109/ACCESS.2021.3124710
17. Dib O (2023) Novel hybrid evolutionary algorithm for bi-objec-
tive optimization problems. Sci Rep 13(1):1–21. https://doi.org/
10.1038/s41598-023-31123-8
18. Vincent AM, Jidesh P (2023) An improved hyperparameter
optimization framework for AutoML systems using evolutionary
algorithms. Sci Rep 13(1):1–19. https://doi.org/10.1038/s41598-
023-32027-3
19 Wang Z, Pei Y, Li J (2023) A Survey on Search Strategy of
Evolutionary Multi-Objective Optimization Algorithms. Appl Sci.
https://doi.org/10.3390/app13074643
20. Su H et al (2023) RIME: a physics-based optimization. Neuro-
computing 532:183–214. https://doi.org/10.1016/j.neucom.2023.
02.010
21. Rabie AH, Saleh AI, Mansour NA (2023) Red piranha opti-
mization (RPO): a natural inspired meta-heuristic algorithm for
solving
complex
optimization
problems.
J
Ambient
Intell
Humaniz
Comput
14(6):7621–7648.
https://doi.org/10.1007/
s12652-023-04573-1
22 Rabie AH, Mansour NA, Saleh AI (2023) Leopard seal opti-
mization (LSO): a natural inspired meta-heuristic algorithm.
Commun. Nonlinear Sci Numer Simul 125:107338. https://doi.
org/10.1016/j.cnsns.2023.107338
23. Akbari MA, Zare M, Azizipanah-abarghooee R, Mirjalili S,
Deriche M (2022) The cheetah optimizer: a nature-inspired
metaheuristic algorithm for large-scale optimization problems.
Sci Rep 12(1):1–20. https://doi.org/10.1038/s41598-022-14338-z
24. Trojovska E, Dehghani M, Trojovsky P (2022) Fennec fox
optimization: a new nature-inspired optimization algorithm. IEEE
Access 10:84417–84443. https://doi.org/10.1109/ACCESS.2022.
3197745
25. Guo J, Zhou G, Yan K, Shi B, Di Y, Sato Y (2023) A novel
hermit crab optimization algorithm. Sci Rep 13(1):1–26. https://
doi.org/10.1038/s41598-023-37129-6
26. Abed-alguni BH, Paul D, Hammad R (2022) Improved Salp
swarm
algorithm
for
solving
single-objective
continuous
optimization problems. Appl Intell 52(15):17217–17236. https://
doi.org/10.1007/s10489-022-03269-x
27 Dehghani M, Trojovsky´ P (2023) Osprey optimization algorithm:
a new bio-inspired metaheuristic algorithm for solving engineer-
ing optimization problems. Front Mech Eng. https://doi.org/10.
3389/fmech.2022.1126450
28. Ferahtia S, Houari A, Rezk H et al (2023) Red-tailed hawk
algorithm for numerical optimization and real-world problems.
Sci Rep 13:12950. https://doi.org/10.1038/s41598-023-38778-3
29. Steinegger M, Sarhan H, Bshary R (2020) Laboratory experi-
ments reveal effects of group size on hunting performance in
yellow saddle goatﬁsh, Parupeneus cyclostomus. Anim Behav
168:159–167. https://doi.org/10.1016/j.anbehav.2020.08.018
30. Bshary R, Hohner A, Ait-el-Djoudi K, Fricke H (2006) Inter-
speciﬁc
communicative
and
coordinated
hunting
between
groupers and giant moray eels in the red sea. PLoS Biol
4(12):2393–2398. https://doi.org/10.1371/journal.pbio.0040431
31. Cormen TH, Leiserson CE, Rivest RL, Stein C (2009) Intro-
duction to Algrithms, 3rd Edition (The MIT Press)
32. Hassan AA, Abdullah S, Zamli KZ, Razali R (2022) Whale
optimization algorithm strategies for higher interaction strength
T-way testing. Comput Mater Contin 73(1):2057–2077. https://
doi.org/10.32604/cmc.2022.026310
33. Mirjalili S (2016) SCA: a sine cosine algorithm for solving
optimization problems.
Knowledge-Based
Syst 96:120–133.
https://doi.org/10.1016/j.knosys.2015.12.022
34. Mansour NA, Saleh AI, Badawy M, Ali HA (2022) Accurate
detection of Covid-19 patients based on feature correlated naı¨ve
bayes (FCNB) classiﬁcation strategy. J Ambient Intell Humaniz
Comput 13(1):41–73. https://doi.org/10.1007/s12652-020-02883-
2
35 Rabie AH, Saleh AI, Mansour NA (2022) A Covid-19’s integrated
herd immunity (CIHI) based on classifying people vulnerability.
Comput. Biol. Med. 140:105112. https://doi.org/10.1016/j.comp
biomed.2021.105112
36. Rabie AH, Mansour NA, Saleh AI, Takieldeen AE (2022)
Expecting individuals’ body reaction to Covid-19 based on sta-
tistical Naı¨ve Bayes technique. Pattern Recognit 128:108693.
https://doi.org/10.1016/j.patcog.2022.108693
37 Eluri RK, Devarakonda N (2023) Feature selection with a binary
ﬂamingo search algorithm and a genetic algorithm. Multimed
Tools Appl 82(17):26679–26730. https://doi.org/10.1007/s11042-
023-15467-x
38. Biswas N et al (2023) Machine learning-based model to predict
heart disease in early stage employing different feature selection
techniques.
Biomed
Res
Int.
https://doi.org/10.1155/2023/
6864343
39. Koshiga N, Borugadda P, Shaprapawad S (2023) Prediction of
heart disease based on machine learning algorithms. 2023 Inter-
national Conference on Inventive Computation Technologies
(ICICT)
713:720
https://doi.org/10.1109/ICICT57646.2023.
10134422
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
90
Neural Computing and Applications (2025) 37:63–90
123

---
