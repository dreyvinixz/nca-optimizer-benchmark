# 2022_particle_swarm_optimization_algorithm_and_its_applications_a_systematic_review
**Função no projeto**: Revisão da literatura e estrutura textual (estilo de escrita e revisão)
**Arquivo original**: `C:\mysystems\projects\nca-optimizer-benchmark\article\references\2022_particle_swarm_optimization_algorithm_and_its_applications_a_systematic_review.pdf`
**Total de páginas**: 31

---

<!-- Page 1 -->
## Page 1

Vol.:(0123456789)
1 3
Archives of Computational Methods in Engineering (2022) 29:2531–2561 
https://doi.org/10.1007/s11831-021-09694-4
ORIGINAL ARTICLE
Particle Swarm Optimization Algorithm and Its Applications: 
A Systematic Review
Ahmed G. Gad1 
Received: 11 November 2020 / Accepted: 21 April 2021 / Published online: 19 April 2022 
© The Author(s) 2022
Abstract
Throughout the centuries, nature has been a source of inspiration, with much still to learn from and discover about. Among 
many others, Swarm Intelligence (SI), a substantial branch of Artificial Intelligence, is built on the intelligent collective 
behavior of social swarms in nature. One of the most popular SI paradigms, the Particle Swarm Optimization algorithm 
(PSO), is presented in this work. Many changes have been made to PSO since its inception in the mid 1990s. Since their 
learning about the technique, researchers and practitioners have developed new applications, derived new versions, and 
published theoretical studies on the potential influence of various parameters and aspects of the algorithm. Various perspec-
tives are surveyed in this paper on existing and ongoing research, including algorithm methods, diverse application domains, 
open issues, and future perspectives, based on the Systematic Review (SR) process. More specifically, this paper analyzes 
the existing research on methods and applications published between 2017 and 2019 in a technical taxonomy of the picked 
content, including hybridization, improvement, and variants of PSO, as well as real-world applications of the algorithm 
categorized into: health-care, environmental, industrial, commercial, smart city, and general aspects applications. Some 
technical characteristics, including accuracy, evaluation environments, and proposed case study are involved to investigate 
the effectiveness of different PSO methods and applications. Each addressed study has some valuable advantages and una-
voidable drawbacks which are discussed and has accordingly yielded some hints presented for addressing the weaknesses 
of those studies and highlighting the open issues and future research perspectives on the algorithm.
1  Introduction
It has been proven in the literature beyond any doubt that 
meta-heuristic optimization algorithms perform well by 
optimally handling several versatile real-world optimization 
tasks, ranging from robotics [31], wireless networks [195, 
206], power systems [40, 76], job shop scheduling [109, 
137], to classification [35] and training of artificial neural 
networks [83]. While questing the global best (near-opti-
mum) solution, numerous fitness evaluations are required by 
the meta-heuristic algorithms. This typically poses a serious 
barrier against the application of meta-heuristic algorithms 
to high-computational optimization problems that exten-
sively exist in computational fluid dynamic optimization 
[21] and structural optimization [79], among many others. 
For working out those problems, the performance of candi-
date solutions is usually evaluated with high-fidelity numeri-
cal analysis approaches (e.g., computational fluid dynamics 
simulations or finite element analysis), which may deduct 
CPU time from minutes to hours, or even days [80, 222]. 
Therefore, within the paradigm of meta-heuristics, many 
Swarm Intelligence (SI) techniques and variants were pro-
posed to tackle complex/large-scale optimization problems.
SI, a substantial branch of optimization techniques, is the 
characteristic of a system where agents interact locally with 
their environment so that their collective behaviors render 
the emergence of cohesive functional global patterns. Unlike 
Evolutionary Algorithms (EAs), SI techniques are inspired 
by agents’ plain behaviors and self-organizing interactions, 
such as fish schooling, honey bees, bacterial growth, ani-
mal herding, bird flocking, ant colonies foraging, and so on. 
Indeed, Beni [17] was the first to use the SI term in cel-
lular robotic systems, in which simple agents interact with 
neighbors to organize themselves. SI was formally estab-
lished in [18, 19]. The rife SI algorithms include Ant Colony 
Optimization (ACO) [37] and Particle Swarm Optimization 
 *	 Ahmed G. Gad 
	
ahmed.gad@fci.kfs.edu.eg
	
https://ahmedgad.com
1	
Faculty of Computers and Information, Kafrelsheikh 
University, Kafrelsheikh, Egypt


---

<!-- Page 2 -->
## Page 2

2532
	
A. G. Gad 
1 3
(PSO) [91]. Less widespread SI algorithms are Bacterial 
Foraging Optimization (BFO) [141], Artificial Bee Colony 
(ABC) [87], Firefly Algorithm (FA) [201], and many others. 
SI algorithms were primarily developed for steady optimi-
zation problems. However, dynamic environments involve 
several real-world optimization problems [124].
Typically, a swarm is defined as a vast number of simple, 
homogeneous agents interacting locally with their environ-
ment, as well as themselves, with decentralized control to 
authorize the emergence of a global important behavior. 
Swarm-based techniques have recently arisen as a family 
of swarm-based, nature-inspired algorithms that have the 
ability to produce robust, fast, and low cost solutions to 
numerous complex problems [50, 69]. Therefore, SI can 
be figured out as a major category of Artificial Intelligence 
(AI) that is utilized to model the collective behavior of natu-
ral social swarms, such as honey bees, bird flocks, and ant 
colonies. These agents (swarm individuals or insects) are 
relatively gullible with simple own capabilities. However, 
they perform cooperatively tasks substantial for their sur-
vival through interacting together in particular behavioral 
manners. Socially, swarm individuals can directly or indi-
rectly interact among themselves [202]. Direct interaction 
can be through audio or visual contact (e.g., a waggle dance 
of honey bees), while indirect interaction is evident when 
the environment is changed by one individual and the other 
individuals react to the new environment (e.g., pheromone 
tracks of ants that look for food sources through depositing 
on their way). This indirect pattern of interaction is known 
as “stigmergy”, which denotes communication through the 
environment [42]. The research area presented in this thor-
ough paper focuses on SI. More specifically, this review 
strives to explore one of the most popular models of SI, 
PSO, which is inspired by birds’ flocking behavior.
PSO is a swarm-based stochastic algorithm proposed 
originally by Kennedy and Eberhart [44, 91], which exploits 
the concepts of the social behavior of animals like fish 
schooling and bird flocking. In PSO, each potential solution 
to a given problem is viewed as a particle with a certain 
velocity flying through the space of the problem just like 
a flock of birds. Each particle then combines – with some 
random disturbances – some aspect of the record of its own 
historical best location and current location with those of 
one or more agents of the swarm to determine its next move-
ment through the search space. After all particles have been 
moved, the next iteration occurs. The swarm as a whole (e.g., 
a flock of birds collectively searching for food) is probably 
to gradually approach the objective function optimum. PSO 
has eventually gained prevalent vogue amongst researchers 
and emerged to provide high performance in an assortment 
of application areas, with the potential to hybridize and spe-
cialize and demonstrate some appealing emergent behaviors. 
PSO has a main advantage of having fewer parameters to 
tune. PSO obtains the best solution from particles’ inter-
action, but through high-dimensional search space, it con-
verges at a very slow speed towards the global optimum. 
Moreover, in regard to complex and large datasets, it shows 
poor-quality results. If there is a large number of dimen-
sions in the problem at hand, PSO usually fails to discover 
the global optimum solution. This phenomenon is caused 
not only by the presence of local optima trap, but also the 
potential fluctuation of the velocities of particles such that 
the successive range of trials is bounded within a sub-plain 
of the whole search hyper-plain [178].
The local optima issue in PSO has been discussed and 
diverse variants of PSO algorithm were developed to tackle 
that issue. For example, some of these variants have been 
developed by incorporating the capabilities of EAs (e.g., the 
adaptation of PSO parameters, hybrid versions of PSO, etc.), 
thereby producing adaptive PSO versions. Other researchers 
have taken on incorporating evolutionary operators, such as 
crossover, mutation, selection, as well as the Differential 
Evolution algorithm (DE) itself, into PSO. Consequently, 
hybrid versions of PSO have been tested and produced, 
including the hybrid evolutionary PSO [128], Genetic Algo-
rithm (GA) and PSO [48, 116], genetic programming-based 
adaptable evolutionary hybrid PSO [154], and many others 
[62]. Such improvements perform well with PSO and have 
the potential to avoid getting stuck at local optima. How-
ever, the problem of premature convergence in some high-
dimensional complex problems still exists, even if the local 
optima obstacle is absent. Hence, PSO does not always work 
properly for high-dimensional models [54].
To this point, the performance of PSO has generally been 
improved by developing different variants of the algorithm. 
However, few review papers and technical surveys have sys-
tematically addressed the PSO literature [190, 216]. Conse-
quently, the primary objective of this work is to present a 
systematic survey by reviewing the PSO algorithm and its 
different methods, as well as a wide variety of indicative 
application domains. Moreover, some of the addressed stud-
ies have highlighted the main approaches of PSO applica-
tions, including health-care, environmental, industrial, com-
mercial, smart city, and general aspects. The key solicitude 
of those PSO methods and applications is satisfying quality 
standards: services arising from PSO methods and applica-
tions should support user’s requirements that cover the qual-
ity metrics of accuracy and efficiency, such as convergence 
rate, computational cost, consistency, stability, diversity, etc. 
In other words, this paper aims to present a timely, com-
pendious, systematic and an in-depth overview of the PSO 
algorithm between 2017 and 2019 and the opportunities and 
challenges imposed during this period.
The structure of this study is organized as follows. 
Section 2 presents the related works. A brief foundation 
of the PSO is presented in Sect. 3. Section 4 exploits the 


---

<!-- Page 3 -->
## Page 3

2533
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
Systematic Review (SR) procedure to provide the proposed 
research approach and motivation. Section 5 demonstrates 
the various methods of PSO based on the SR method. Sec-
tion 6 systematically outlines and categorizes the applica-
tion approaches in PSO. Also, a technical classification and 
differentiation of the approaches in the addressed papers is 
presented in this section. Section 7 provides a discussion 
on the PSO approaches that have not yet been thoroughly 
analyzed. Finally, Sect. 9 concludes the paper along with 
its limitations.
2  Related Work
A swift explanation is presented in this section for the gen-
eral related studies in the PSO algorithm.
Poli et al. [143] presented an overview of the great efforts 
which have given impetus and direction to research in parti-
cle swarms, as well as some important new applications and 
directions. An analysis of IEEE Xplore and Google Scholar 
citations and publications from 1995 to 2006 were presented 
in this work, illuminating the sense meant by Kennedy and 
Eberhart [92]. The strength of this study was to present com-
prehensive challenges and open issues in the PSO algorithm. 
However, this study did not consider the compatibility of 
PSO application with each presented approach.
Banks et al. [13, 14] offered, in two parts, a timely and 
brief review of the field in general, alongside the opportuni-
ties and challenges emanating from the versatile application 
of PSO. On the one hand, part I [13] has considered the 
history and background of PSO and its position within the 
broader paradigm of natural computing. The review then 
continued to discuss different improvements to the native 
formulation of PSO both in discrete and continuous prob-
lems, swarm behavior analysis, and measures considered 
to address stagnation. Furthermore, the review focused on 
research regarding adaptations for parallel implementation, 
algorithm configuration, and dynamic environments. The 
achievement of this study was identifying two significant 
areas of challenge for future further development: swarm 
stagnation and dynamic environments. The shortcoming of 
this part is the insufficiency of the explanation the related 
work. On the other hand, part II [14] has discussed recent 
studies in some of the impressive areas of research: con-
strained and multi-objective optimization, combinatorial 
problems, and hybridization. In that review, a number of 
domains were briefly touched upon, including the optimi-
zation of neural fuzzy networks, artificial neural networks, 
computational biology, image processing and medical imag-
ing, optimization of electricity generation, network routing, 
and financial forecasting. Nevertheless, the study has a 
main defect of not analyzing the selected studies in terms of 
evaluation parameters, such as convergence rate, diversity, 
accuracy, and processing time, as quality factors in this area.
Kulkarni et al. [96] outlined some issues regrading Wire-
less Sensor Networks (WSNs), introduced PSO, and dis-
cussed the suitability of the algorithm for WSN applications. 
This study also presented a compendious survey of how PSO 
is tailored to tackle the issues of node localization, node 
deployment, data aggregation, and energy-aware clustering 
as optimization problems. The strong point of this review is 
to comprehensively present open issues in WSNs. However, 
the compatibility of high-speed real-time applications with 
each approach was not considered.
Kothari et al. [94] reviewed the studies related to the 
modifications of native PSO and its practical application 
in real-world problems. The rapid modification of PSO has 
been emerged in different examples, including the two-step 
PSO and the PSO-Support Vector Machine (PSO-SVM). 
The integration of the PSO and the practical implementa-
tion of PSO with the industry standard algorithm have also 
generated stunning results. The advantage of this survey was 
to present recent diverse variations in PSO and analyze the 
accuracy of PSO in different domains. The main deficiency 
of this study is the lack of statistical information about the 
discussed standard PSO and its application in various speci-
fied contexts.
Imran et al. [71] discussed diverse variants of PSO in 
regards to swarm initialization, mutation operators, and 
inertia weight. The main advantage of this overview was to 
highlight the importance of introducing the different muta-
tion operators and inertia weight parameter to improve the 
performance of PSO. However, other promising variants of 
PSO were not considered.
Alam et al. [7] surveyed systematically the evolution of 
clustering techniques based on PSO and presented the results 
of rapidly increasing trends in the literature of SI, PSO para-
digm, and PSO-based data clustering approaches, proving 
that there is a tremendous increase in the popularity of such 
approaches. This research affirmed that the approaches are 
novel and simple to implement and builds on communication 
and collaboration. This study outlined different application 
domains of PSO relevant to clustering. However, applica-
tions to more complex problems are absent. Furthermore, 
variants of PSO for clustering high-dimensional data were 
surveyed by Esmin et al. [49]. The main advantage of this 
survey was to present the attempts of different publica-
tions in reducing data dimensions. The weakness is still the 
absence of discussing more clustering-related applications.
Marini and Walczak [123] described comprehensively the 
PSO algorithm to show its ability to solve different kinds 
of optimization problems in chemometrics. The importance 
of the appropriate choice of PSO meta-parameters has 
been highlighted in this work by means of selecting prac-
tical examples in the subject areas of variable selection, 


---

<!-- Page 4 -->
## Page 4

2534
	
A. G. Gad 
1 3
estimating robust Principal Component Analysis (PCA) 
solutions, and signal warping. This tutorial contributed to 
presenting works subject to chemometrics impressively. 
However, it lacked splashing other state-of-the-art fields.
Zhang et al. [216] investigated comprehensively the PSO 
algorithm. They provided advances in PSO, including its 
theoretical analysis (convergence analysis, parameter tuning, 
etc.), hybridization (with GA, DE, ABC, ACO, biogeogra-
phy-based optimization, harmonic search, Tabu Search (TS), 
Artificial Immune System (AIS), and Simulated Annealing 
(SA)), modifications (including fuzzy PSO, chaotic PSO, 
bare-bones PSO, quantum-behaved PSO), population topol-
ogies (including star, ring, random, von Neumann, fully con-
nected, etc.), extensions (to binary, discrete, constrained, and 
multi-objective optimization), and parallel implementation 
(in cloud computing, multiprocessor, multicore, and GPU 
forms). Moreover, they introduced a survey on the applica-
tions of PSO to the following eight fields: biology, chemis-
try, medicine, electrical and electronic engineering, fuel and 
energy, mechanical engineering, operation research, com-
munication theory, and automation control systems. Despite 
all that, the publication analysis demonstrated in this survey 
lacks the presentation of the annual exponential fluctuation 
of publications for each variant and application field.
Wang et al. [190] presented the inception and background 
of the PSO algorithm, and carried out a theoretical analysis 
of the algorithm. Then, they analyzed its current situation of 
application and investigation in algorithm structure, topol-
ogy structure, parameter selection, multi-objective optimiza-
tion, discrete and parallel PSO algorithm, and engineering 
applications. This overview is characterized by suggesting 
distinctive future research directions. However, no analytic 
discussion is introduced in this work.
Summarizing, Table 1 outlines the recent review studies 
on PSO with respect to the general survey and review studies 
discussed in this section. This table lists the key topics, pub-
lication year, and covered years (if available) for each study. 
The deficiencies in the existing review papers propose that 
a comprehensive and systematic literature review should be 
provided to address some of such common weaknesses as:
•	 In existing studies, the methods and applications of PSO 
are not organized in a clear taxonomy, and do not have 
analytical assessment from which one can learn some-
thing beneficial.
•	 Important assessment factors are not involved in the 
methods and applications of PSO in some current studies.
•	 The systematic arrangement is typically absent in the 
structure of literature studies, and the paper selection 
criterion is vague as well.
3  Particle Swarm Optimization: PSO 
Mechanism
3.1  Self‑Organization Features
SI system has a major feature, namely, self-organization, 
in which the components of an initially disordered system 
interact locally to produce a coordination or global order. 
This process is characterized by spontaneousness; that is, 
no agent inside or outside of the system dominates the inter-
action. The self-organization in swarms was interpreted 
by Bonabeau et al. [25] through three key components as 
follows:
•	 Robust dynamical non-linearity (always comprising 
positive and negative feedback) convenient structures 
are promotionally being created with the help of positive 
feedback, while this positive feedback is counterbalanced 
and the collective pattern is stabilized with the help of 
negative feedback.
•	 Trade-off between exploration and exploitation A valu-
able mean creativity artificial approach is provided 
through a suitable balance that is identified by SI.
•	 Multiple interactions Information coming from neigh-
bor agents in the swarm are used by individual agents, 
allowing information to be disseminated throughout the 
network.
Table 1   Relevant studies in PSO
Study
Main context
Publication year
Covered years
Poli et al. [143]
PSO algorithm, new directions, and applications
2007
1995–2006
Banks et al. [13, 14]
PSO field, challenges, and opportunities
2007 & 2008
N/A
Kulkarni et al. [96]
PSO suitability for WSN applications
2011
N/A
Imran et al. [71]
PSO variants
2013
N/A
Alam et al. [7]
PSO-based data clustering
2014
2002–2012
Marini and Walczak [123]
PSO in chemometrics fields
2015
N/A
Zhang et al. [216]
PSO advances and applications
2015
2000–2013
Wang et al. [190]
PSO theory and application
2018
N/A


---

<!-- Page 5 -->
## Page 5

2535
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
3.2  SI Features
Millonas [127] proposed that SI must satisfy five basic prin-
ciples: adaptability, diverse response, stability, quality, and 
proximity. Table 2 lists their meanings.
3.3  Standard PSO Algorithmic Structure
A swarm of particles updates their relative positions from 
iteration to another, boosting the PSO algorithm to duly 
perform the search process. To get the optimum solution, 
each particle moves towards its prior personal best position 
( 퐩best ) and the global best position ( 퐠best ) in the swarm [215]. 
Assuming a minimization problem, one have
where i ∈{1, 2, … , N} , and
where i denotes particle’s index, t is the current iteration’s 
number, f is the objective function to be optimized (mini-
mized), 퐱 is the position vector (or a potential solution), and 
N is the total number of particles in the swarm. The fol-
lowing equations update, at each current iteration t + 1 , the 
velocity 퐯 and position 퐱 of of each particle i as:
(1)
퐩t
besti = 퐱∗
i ∣f(퐱∗
i
) =
min
k=1,2,…,t
({f(퐱k
i
)})
,
(2)
퐠t
best = 퐱t
∗∣f(퐱t
∗
) =
min
i = 1, 2, … , N
k = 1, 2, … , t
({f(퐱k
i
)})
,
(3)
퐯t+1
i
= 휔퐯t
i + c1퐫ퟏ
(
퐩t
besti −퐱t
i
)
+ c2퐫ퟐ
(퐠t
best −퐱t
i
)
,
(4)
퐱t+1
i
= 퐱t
i + 퐯t+1
i
,
where 퐯 represents the velocity vector, 휔 is the inertia weight 
utilized to balance the local exploitation and global explo-
ration, 퐫ퟏ and 퐫ퟐ are random vectors uniformly distributed 
within the range [0, 1]D (D being the search space dimen-
sionality or the size of the problem at hand), and c1 and c2 , 
called “acceleration coefficients”, are positive constants.
An upper bound is commonly set for the velocity vector. 
As a means to prevent particles from shaving off the search 
space and forcing them to take a proper step size to comb the 
entire search domain, the “velocity clamping” method was 
used [163]. The “constriction coefficient” strategy is another 
method, proposed by Clerc and Kennedy [36], in which the 
velocities can be also constricted by theoretically observing 
and analyzing the swarm dynamics.
By scrutinizing Eq. (3), we can interpret that the first part, 
known as “inertia component”, represents the prior velocity, 
which provides the particles with appropriate momentum 
to rove across the search space. The second part, the “cog-
nitive component”, denotes the own positiveness for every 
particle. It motivates the particles to move towards their own 
best positions found so far over subsequent iterations. The 
third part, known as the “social component”, indicates the 
collective effect of the particles to reach the global optimum 
solution [218].
3.4  PSO Pseudocode
Let f ∶퐑N →퐑 be an objective function which needs to be 
simplified. Then, the function takes a vector of N real num-
bers denoting an N candidate solutions and outputs a real 
number that indicates the value of the objective function. 
The f gradient is either hard to calculate or often unknown. 
Then, the global minimum 
(퐠best
)
 is pursued as exhibited in 
Algorithm 1.
Table 2   SI basic principles
Principle
Definition
Adaptability
Swarm should have the potential to change its search behavior when the computational cost is high
Diverse response
Swarm should not perform its activities along extremely narrow channels
Stability
Swarm should not change its search behavior in response to the environment changes
Quality
Swarm should should have the potential to respond to performance measures in the environment
Proximity
Swarm should should have the potential to smoothly perform time- and space-consuming computations


---

<!-- Page 6 -->
## Page 6

2536
	
A. G. Gad 
1 3
Algorithm 1 PSO pseudocode
Input:
N – Swarm size
D – Problem dimensionality
T – Maximum number of iterations
LB – Lower bound of the search space
UB – Upper bound of the search space
Output:
gt
best – the best position (solution) found so far
1: Start
2:
Initialize the swarm randomly;
3:
for i = 1 to N do
Iterate through the swarm
4:
v0
i ←a random vector within [LB, UB]D;
Initialize particles’ velocity using a uniform distribution
5:
x0
i ←a random vector within [LB, UB]D;
D;
Initialize particles’ positions using a uniform distribution
6:
p0
besti ←x0
i ;
Initialize pbest to its initial position
7:
end for
8:
Apply Eq. (2) to ﬁnd g0
best;
Initialize gbest to position with the minimum ﬁtness value
9:
t ←1;
Initialize ﬁrst iteration number
10:
while t ≤T do
11:
for i = 1 to N do
Iterate through the swarm
12:
r1, r2 ←two independent vectors randomly generated from [0, 1]
13:
Apply Eq. (3);
Update particle’s velocity
14:
Apply Eq. (4);
Update particle’s position
15:
if f (xt
i) < f
pt−1
besti
then
If new solution is better than current personal best
16:
f
pt
besti
←f (xt
i);
Update the best known position of the particle
17:
end if
18:
end for
19:
Apply Eq. (2) to ﬁnd gt
best;
Update the swarm’s overall best known position
20:
t ←t + 1;
21:
end while
Maximum iteration number is reached or termination criterion is satisﬁed
22: End
Elsevier, Springer, IEEE, ACM, MDPI, Taylor & Francis, 
Wiley, Inderscience, MDPI, etc.
In relation to the objectives of this SR paper, comprehen-
sive answers are provided to the following four Analytical 
Questions (AQs) [156]:
•	 AQ1: Into which domains can PSO methods and applica-
tions be classified?
•	 AQ2: Which main contexts can be considered for PSO 
methods and applications?
•	 AQ3: What assessment environments are used for evalu-
ating the PSO methods and applications?
•	 AQ4: What are generally the PSO open perspectives and 
future research directions that can be drawn from the 
work presented in the paper?
After outlining the AQs, the ultimate research selection 
was conducted by applying the inclusion/exclusion criteria. 
With respect to the number of published research papers, 
only conference papers and journal articles indexed in Web 
of Science (WoS) or Scopus proceedings are selected and 
analyzed as peer-reviewed publications for the methods and 
applications of PSO. Finally, I selected 2,140 peer-reviewed 
3.5  PSO Flowchart
The flowchart to demonstrate the flux of PSO is depicted 
in Fig. 1.
4  Proposed Research Approach
This section depends on the SR method to present, in a tax-
onomy, a review of the research studies related to the meth-
ods and applications of PSO [71, 123, 143, 190, 216]. Other 
synonyms and alternatives of the key essential components 
are also considered to commit the final exploration string 
as [49, 94, 96]:
•	 (“Methods” OR “Variants” OR “Hybrid” OR “Improved” 
OR “Software” OR “Application” OR “Application layer” 
OR “Application-based” OR “App”) AND (“PSO”) OR 
(“Particle Swarm Optimization”)
Figure 2 demonstrates the distribution (from 2017 to 2019) 
of research studies published by the most popular ven-
ues regarding the review methods and articles, including 


---

<!-- Page 7 -->
## Page 7

2537
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
papers. Due to the length limitation of the paper, I addressed 
curtly only 84 state-of-the-art research papers from reputed 
journals to address the four AQs in detail in Sects. 5 and 
6. Figure 3 demonstrates the selection criteria and evalua-
tion method for the literature studies. The exclusion phase 
was carried out by omitting white papers, short papers, 
book chapters, non-peer-reviewed studies, and low-quality 
researches (published in rapacious journals) that did not pro-
vide any technical information or scientific discussion. The 
ultimately selected studies are recognized by considering the 
inclusion criteria as follows:
•	 Papers published online from 2017 to 2019.
•	 Papers on PSO topics, including methods and applica-
tions.
•	 Papers prepared in a technical quality method in PSO 
methods and applications.
•	 Papers that follow the quality standards.
The ultimately selected studies are recognized by consider-
ing the exclusion criteria as follows:
•	 Papers that present survey and review studies.
•	 Papers indexed in neither WoS nor Scopus.
•	 Papers written in a language other than English.
•	 Papers not subject to peer-review.
5  Methods of PSO
In fact, the literature is rich in many PSO techniques. To 
organize them, a proper classification criterion is suggested, 
and various PSO methods are classified as per Fig. 4.
5.1  Hybridization
Hybridization is a generic model of two or more algorithms, 
which exploits their advantages while decreasing their 
impediments. The combination of techniques does well for 
tacking a specified problem, given that the obtained results 
can be improved by these combined techniques on their own. 
The exploitation and exploration of an algorithm can com-
pletely be enhanced through hybridization of algorithms [53, 
177, 180]. For example, an algorithm can cater for the lack 
of its preciseness and refine the results through synergy with 
a local search method. The hybrid approach in the field of 
optimization is growing in popularity and utilizes the pur-
port of hybridizing the components from leading optimiza-
tion techniques to improve the performance of traditional 
optimization algorithms.
5.1.1  Meta‑heuristic Algorithms
Many nature-inspired hybrid approaches have been devel-
oped by numerous researchers/scholars for achieving sig-
nificant performance in the exploitation and exploration of 
existing algorithms. To optimally design a Labyrinth Spill-
way (LS) having quarter-round or half-round crest shape, an 
evolutionary Hybrid Algorithm (HA) combining the PSO 
Start
Initialize a swarm of
N particles randomly
Evaluate the current
personal ﬁtness value
f
pt
besti
for each particle i
Is f
pt
besti
better than
previous f
pt−1
besti ?
Recognize pt
besti as the
personal best position for i
Keep the previous pt−1
besti
Assign the best position’s ﬁt-
ness value pt
best∗to gt
best
Maximum epochs, or
optimum reached?
Update the velocity of
Update the position of
each particle using Eq. (3)
each particle using Eq. (4)
End
Yes
No
Yes
No
Fig. 1   The flowchart of PSO
Fig. 2   Distribution of research papers by publisher


---

<!-- Page 8 -->
## Page 8

2538
	
A. G. Gad 
1 3
algorithm with the Bat Algorithm (BA) was developed by 
Ferdowsi et al. [52]. This way, the best outcomes of one 
algorithm substitute the worst ones from the other. More-
over, the proposed algorithm has a high convergence rate 
regarding the optimal absolute outcome and does not get 
stuck into the local minima. Responses and computational 
time of this HA proved that LS with quarter-round crest 
requires more concrete, compared to the half-round one.
In another work, Melton [126] examined a strategy for 
hybridizing two heuristic algorithms, PSO and DE, to better 
address the stagnation problem when solving slew-maneuver 
time-optimal problems having constraints in solution path. 
The stagnation was handled very well by the combined PSO-
DE method, with a reduction of 40% in the computational 
time compared to just applying DE. In [34], a Dynamic 
Multi-Swarm Differential Learning Particle Swarm Opti-
mizer (DMSDL-PSO) was proposed. In this study, the DE 
operators were incorporated into each one of the DMSDL-
PSO’s sub-swarms to form a novel method. DMSDL-PSO 
has a good capability of exploitation and exploration by 
employing a local searcher like Quasi-Newton method to 
enhance the exploitation capability, making, at the same 
time, use of the capability of exploration existing in the dif-
ferential mutation. On the other hand, the optimization per-
formance of DE was improved by developing a novel self-
adaptive mutation DE algorithm based on PSO (DEPSO) 
[194]. DEPSO can significantly utilize the fast convergence 
capability of PSO and the strong global exploration capa-
bility of an improved DE mutation strategy. As a result, the 
diversity of the swarm was managed well throughout the 
evolution, resulting in a higher convergence speed.
In [12], Aydilek proposed a Hybrid algorithm combin-
ing both FA and PSO (HFPSO). HFPSO checks the global 
historically best fitness values in order to properly deter-
mine the proper start of the local search. The high accuracy 
of convergence and runtime was statistically approved by 
evaluating the method using expensive benchmarks from 
the high-dimensional CEC’15 and CEC’17 functions.
Typically, a strong classifier can be created based on the 
strengths of penalization and, say, SVM, proving the effec-
tiveness of Penalized Support Vector Machine (PSVM). In 
[6], Al-Thanoon et al. proposed a new hybrid PSO and FA 
to find the tuned parameters of PSVM, showing a high abil-
ity to escape from being trapped into the local optima trap.
In [223], a hybrid method of PSO and GA was proposed 
by Zhu et al. to optimize an antenna array deployment for 
locating the sources of Partial Discharge (PD) in an entire 
substation. First, an algorithm called Direction-of-Arrival 
(DOA) estimation was presented for testing its applicabil-
ity to arbitrary array configurations. In order to minimize 
the objective functions, the hybrid PSO-GA algorithm was 
applied to optimize the array deployments for the localiza-
tion of both DOA and coordinates.
Genetic Learning PSO (GL-PSO) breeds eminent exem-
plars to steer the motion of particles for the purpose of 
improving the performance of PSO. However, the perfor-
mance of GL-PSO is not satisfactory on complex optimi-
zation problems, in which a global topology is depicted 
for exemplary generation and efficient diversity cannot be 
retained to boost exploration. For the betterment of the 
adaptability and performance of GL-PSO, Lin et al. [106] 
modified two versions of the basic GL-PSO algorithm. In 
Fig. 3   The selection principles and evaluation of research papers


---

<!-- Page 9 -->
## Page 9

2539
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
exemplar generation, a ring topology is depicted to boost 
diversity and so exploration, while the algorithm’s adaptabil-
ity is improved by adopting a Global Learning Component 
(GLC) with control parameters which are linearly adjusted.
Nenavath et al. [135] proposed a novel hybrid algorithm 
of Sine Cosine Algorithm (SCA) and PSO (SCA-PSO) to 
overcome the SCA premature convergence at local minima 
for the two major goals of object tracking and solving opti-
mization problems. Two parameters of PSO, 퐩best and 퐠best , 
were embedded into the conventional SCA to lead the pro-
cess of pursuing the possible candidate solutions, so that the 
퐩best in SCA is then used to initialize PSO swarm to further 
exploit the feasible search spaces.
PSO usually experiences premature convergence, so it 
is easily to be caught into a local optimum solution. Also, 
it is ineffective in balancing exploration and exploitation, 
especially in complex multipeak search functions. To over-
come these shortcomings, a Hybrid Particle Swarm Opti-
mizer with Sine Cosine Acceleration Coefficients (H-PSO-
SCAC) was proposed [32]. First, Sine Cosine Acceleration 
Coefficients (SCAC) were presented to efficiently control the 
convergence to the global optimum solution by guiding the 
local search. Second, the swarm is initialized by adopting 
opposition-based learning method. Additionally, the inertia 
weight is adjusted by utilizing a sine chaotic map. Finally, a 
modified formula for updating position was proposed.
The SCA is mainly stigmatized by its limitation to exploit 
only emerging regions, depending on the parameter settings. 
However, the SCA is well capable of exploration. Taking 
advantage of the PSO capability of strong exploitation, Issa 
et al. [73] developed a new enhanced version of the SCA 
by hybridizing it with PSO. Two layers have formed the 
resulting technique: In the bottom layer, the search agents 
of SCA explore the search space, and in the top layer, the 
region around the best result found by the layer at bottom 
is exploited. Hence, there is a balance between exploitation 
and exploration in the proposed technique, which maintains 
fast convergence and improves the solution quality.
In another research, Sanchez et al. [159] used a column 
generation framework to solve the Binary Cutting Stock 
(BCS) problem by developing a benchmark of different 
approaches. Master- and sub-problem are the main compo-
nents of this framework. Classical integer linear program-
ming was used to solve the master problem, while meta-
heuristic algorithms (PSO, SA, and GA) were used to solve 
the sub-problem. The aim of this benchmark analysis was 
to compare the results of the hybrid meta-heuristics with an 
exact approach.
In [68], Huang et al. presented a methodology to utilize 
various loading-unloading curves to extract the mechani-
cal properties of its bulk materials using an Instrumented 
Indentation Test (IIT). Simulated Annealing PSO (SAPSO) 
coupled with finite iterative element simulation were used 
to obtain the mechanical properties, including strain-hard-
ening rate (K) and strain-hardening exponent (n), from the 
IIT data.
Ibrahim et  al. [70] proposed a hybrid optimization 
approach for solving the feature selection problem. The Salp 
Swarm Algorithm (SSA) was combined with the PSO as 
SSAPSO, in which the performance of the exploitation and 
exploration stages in PSO was significantly amended. Based 
on 15 benchmark functions alongside different UCI datasets, 
the original datasets were refined by removing the confus-
ing or redundant features while yielding or keeping a better 
Fig. 4   Categorization of diverse PSO methods


---

<!-- Page 10 -->
## Page 10

2540
	
A. G. Gad 
1 3
efficiency, demonstrating the improvement in the SSAPSO 
with respect to the prediction accuracy without affecting the 
computational cost.
Laskar et al. [98] proposed a new hybrid algorithm named 
as the Hybrid Whale PSO (HWPSO) algorithm. Since 
Whale Optimization Algorithm (WOA) is known for its very 
good capability of exploration, it is hybridized with PSO in 
a novel way to overwhelm the limitations related to a PSO 
phase (i.e., stagnation impact). The HWPSO has employed 
two novel techniques during hybridization: “Forced” whale 
in the exploration phase so that the WOA can guide PSO 
to better avoid getting stuck into local optima, and “Cap-
ping” phenomenon in the exploitation phase for restricting 
the search mechanism of WOA in order to converge to the 
global optimum value more fast.
A new form of multi-swarm BBPSO, in which its updat-
ing distributions are reoriented by adaptively learning the 
optimal alignments, is presented by Vafashoar and Mey-
bodi [183]. The idea is that, along appropriate directions, 
the prospect of generating new particles is maximized. Due 
to the lack of a priori knowledge of these alignment direc-
tions, the proposed method adaptively learns suitable align-
ments by employing a learning mechanism. Cellular learning 
automata were adopted to build this learning mechanism. 
For each particle in the presented method, multiple align-
ment strategies are developed. Moreover, these strategies are 
adjusted so that, during the search process, the particles are 
attracted toward the most promising regions based on the 
cellular learning automata.
Durán-Rosal et  al. [43] proposed novel approaches 
based on time series segmentation. The proposed methods 
include the PSO algorithm adaptation to this problem, as 
well as more advanced variants of PSO (e.g., BBPSO and its 
exploitation variant (BBePSO)). Furthermore, a new algo-
rithm, called Dynamic exploitation BBPSO (DBBePSO), 
was derived, in which the importance of the cognitive and 
social components are updated throughout the successive 
generations. A final local search step is considered to further 
improve the solutions obtained from these algorithms based 
on the incorporation of two popular traditional segmentation 
algorithms (Top-Down and Bottom-Up).
In [134], Nagra et al. proposed an enhanced Self-Inertia 
Weight Adaptive PSO algorithm with a gradient-based Local 
Search strategy (SIW-APSO-LS) to solve the problem of 
premature convergence in PSO. This proposed algorithm 
takes the advantages of the exploration ability of the adap-
tive PSO with enhanced inertia weight, and the exploitation 
of the gradient-based local search strategy.
In [30], Cao et al. proposed a Comprehensive Learn-
ing Particle Swarm Optimizer (CLPSO) embedded with 
a local search utilizing the CLPSO’s capability of global 
search and the fast convergence capability of local search to 
achieve higher optimization performance. This work takes 
advantage of the introduced so called quasi-entropy index 
for addressing its main issue (specifically, when to start the 
local search) by developing an adaptive local search start-
ing scheme.
In most of the above-discussed studies, PSO was imple-
mented without coherence with other meta-heuristics. For 
instance, a good initial solution can be produced by utilizing 
DE or GA as a starting point, and the PSO can take care of 
the rest of the search. In some cases, an initial solution can 
be produced by using PSO as a starting point, and the search 
can be conducted by others. Furthermore, the PSO, as a sup-
plementary tool, may be hybridized with the deterministic 
local search to boost the exploitation capability and produce 
high-quality solutions. Additionally, the search speed may 
be elevated by the PSO.
5.1.2  Artificial Neural Networks (ANNs)
Artificial Neural Networks (ANNs) can be, in a word, sum-
marized as learning via training [187]. To achieve that, a 
series of input and output vectors is adopted to handle a 
set of data that needs to be trained. At the training time, 
the ANN is applied to the training data iterative, so that 
the desired input-output mapping emerges by balancing 
weights of the network several times in a while. After the 
training stage completes, a foreseeing model is ready and 
the corresponding output vector can be then created from 
input ones unrelated to the training pairs. An appropriate 
set of weights and transferring functions should be carefully 
chosen (via, say, meta-heuristic optimization) to ensure that 
the ANNs can present a quantifiable smooth function that 
would properly link future input and output vectors. Vari-
ous components, including prediction and system control 
and modelling, are inferred to express the broadly connected 
neural systems.
In this regard, Moayedi et al. [131] introduced a PSO-
optimized ANN model to solve the prediction problem of 
Landslide Susceptibility Mapping (LSM). The focus of this 
study was the prediction of landslide hazardous susceptibil-
ity mapping by applying a hybrid model of PSO and ANN 
(PSO-ANN). Two statistical performance metrics, Root 
Mean-Squared Error (RMSE) and coefficient of determi-
nation ( R2 ), were used to assess the predicted results from 
both the original ANN and the PSO-ANN. Comparing the 
two models, the PSO-ANN model was observed to be more 
reliable in LSM estimation than the ANN.
In another work, Junior and Yen [84] proposed a novel 
algorithm based on PSO and Convolutional Neural Network 
(CNN), namely, PSO-CNN. In comparison with other evo-
lutionary approaches, the proposed algorithm is capable of 
fast convergence. In an application to image classification, it 
was able to automatically find deep meaningful CNN archi-
tectures. To allow the use of PSO optimization with CNN, 


---

<!-- Page 11 -->
## Page 11

2541
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
a novel strategy for direct encoding, as well as a velocity 
operator were built.
5.1.3  Support Vector Machine (SVM)
Support Vector Machine (SVM) [56] is an intelligence algo-
rithm lying under supervised machine learning [2]. In this 
algorithm, the data is analyzed and particular visible or hid-
den patterns are quested with the major aim to perform two 
main tasks of classification and regression. SVM is known 
for its potential to perform non-linear classification and 
linear separation of the data, to build another dimensional 
space from existing training datasets by investigating the 
respective categories. The separation process is working by 
increasing the chasm between too close points of various 
categories (i.e., support vectors) to better explore the optimal 
separating hyper plane. It should also point out that SVM 
can perform other tasks like linear classification [41].
In this framework, Hoang et al. [61] proposed a novel 
Differential PSO-based SVM (DPSO-SVM) classifier to 
monitor the conditions of a surge arrester. In the proposed 
method, the parameters of SVM classifiers were optimized 
by investigating the DPSO-SVM technique configuration 
that gives the best results. Input vectors composed of three 
extracted features are used to assess five arrester conditions, 
including degradation (D), tracking (T), pre-fault (A), nor-
mal (N), and abnormal (U). Meanwhile, a DPSO-based 
ANN classifier was also involved, to carry out a compara-
tive study on fault diagnosis.
In another work, Tharwat and Hassanien [179] optimized 
the SVM parameters by employing quantum-behaved PSO 
(QPSO) for reducing the classification error. The proposed 
model, called QPSO-SVM, was evaluated by adopting 7 
traditional classification datasets from the UCI data reposi-
tory. The experimental results revealed the capability of the 
proposed model to obtain the best values of the parameters 
of SVM. Moreover, the results showed lower classification 
error rates than those obtained by the standard versions of 
PSO and GA.
5.1.4  Quantum
40 years ago, quantum computer [20] was invented, and 
in the late 1980s, the quantum computer formal definition 
was given. Due to the potential of the quantum computer in 
various special problems [85], this field has witnessed many 
great efforts. Various popular algorithms are developed, and 
the most well-known one of them is Shor’s quantum factor-
ing algorithm [185]. In 2004, Sun et al. [170] firstly intro-
duced the Quantum-behaved PSO (QPSO) for improving the 
convergence rate of the native PSO. In quantum space, par-
ticles often have the guarantee to reach the real global opti-
mum via searching throughout the full solution space. Later 
in recent decades, QPSO has drawn great attention from 
many scholars. In what follows, some of them are presented.
In [81], Jmal et al. proposed a QPSO method for solving 
the K-Traveling Repairman Problem (K-TRP). The proposed 
approach incorporates a K-TRP-specific repair operator to 
ensure that a feasible solution space will be always there to 
guide the search process and that the quality of solutions is 
significantly improved as much as possible.
In [147], an optimal path planning was proposed for free-
floating two-wheel pendulum robot system based on its self-
balance. First, the corner trajectory of this pendulum robot is 
parametrized by QPSO. The native attitude and the control 
precision of the robot’s terminal attitude and position are 
utilized to formulate the objective function. The addressed 
problem of optimal path planning was considered as a non-
linear optimization problem that is solved using the QPSO 
algorithm to achieve the demanded goal.
Motivated by the characteristics of PSO and quantum the-
ory, Xu et al. [199] proposed a new method, namely, QPSO. 
The QPSO used fractional calculus to enhance its global 
search ability. The discrete expression of the Grünwald-
Letnikov definition, one of the most popular differential 
fractional definitions, was incorporated for better updating 
of the particles’ positions in QPSO.
5.1.5  Rough Set
The theory of rough set [142] is an approach devised to deal 
with uncertainty and ambiguity. The philosophy of this 
approach was built on the fact that every object in the uni-
verse has its own characteristics. The rough set theory is a 
mathematical tool utilized to extract knowledge from infor-
mation obtained from uncertain data [105]. In feature selec-
tion, rough set analysis is utilized because it only requires 
the supplied basic data without the need for any supplemen-
tary information. Also, it is characterized by the suitability 
for exploring the qualitative and quantitative properties of 
data.
Fan et al. [51] proposed an algorithm called RoughPSO 
for solving the convergence to a local optimum in PSO, 
depending on the rough set theory. The RoughPSO uses 
upper- and lower-approximation rough sets to get the mem-
bership values. Then, these values were employed to refine 
the velocity and position for each particle.
In another work, Bhattacharya et al. [23] proposed a 
technique of Feature Selection based on an impromptu PSO 
algorithm and Rough Set (PSORS-FS), to select the most 
relevant features for detecting permission-based Android 
malwares. This work mainly contributed to the recommen-
dation of a new method of random key encoding that con-
verts the conventional PSO algorithm in discrete space. It 
also reduced the issues related to the sigmoid function in 
binary PSO, as well as the particles’ maximum velocity.


---

<!-- Page 12 -->
## Page 12

2542
	
A. G. Gad 
1 3
5.2  Improved PSO
This section is competent of the improvements in PSO based 
on some third-party methods as learning strategy, fuzzy 
logic, mutation, Lévy flight, opposition-based learning, and 
surrogate.
5.2.1  Learning Strategy
In reality, increasing complexity in many optimization 
problems calls for further research on the exploration and 
improvement of diverse optimization algorithms. It has been 
proved that the PSO algorithm is an efficient tool to solve 
different types of optimization tasks. However, for the base 
PSO, the main aim of the updating strategy is to learn the 
global optimum, and it always experiences too fast conver-
gence in addition to poor performance on various complex 
optimization tasks, principally for multimodal problems. 
The mechanism of learning in classical PSO is simple and 
easy to develop, but some likely issues, such as the phenom-
ena of “two steps forward, one step back” and “oscillation”, 
may disrupt it. Therefore, PSO researchers have managed to 
design new efficacious learning strategies for avoiding the 
two phenomena and improving the overall search perfor-
mance. Xu et al. [198] presented a Dimensional Learning 
Strategy (DLS) following the best personal experience of 
each particle to eventually discover and integrate the pro-
pitious information extracted from the optimal solution of 
swarm. Thereafter, different learning strategies are used to 
provide a Two-Swarm Learning PSO algorithm (TSLPSO). 
One of the two sub-swarms used the DLS to create learning 
exemplars for guiding the particles’ local search, while the 
other sub-swarm used the comprehensive learning strategy 
to create learning exemplars for managing the global search 
of particles.
Wang and Liu [193] proposed a Heterogeneous Com-
prehensive Learning PSO (HCLPSO) algorithm to attain 
3D spatial trajectory tracking to realize a new saturated 
approach to control a quadrotor. First, the quadrotor model 
was divided into: an inner position control loop, inside cas-
caded control structure, and an outer attitude control loop. 
Second, the saturated control is applied to limit the quadro-
tor’s thrust force in the outer attitude control loop. Next, 
the parameter adjustment difficulty for the quadrotor was 
alleviated by employing the HCLPSO algorithm to optimize 
the control parameters.
5.2.2  Fuzzy Logic (FL)
Since the performance of PSO is strongly dependent on 
the selection of its settings (i.e., minimum and maximum 
velocity, social and cognitive factors, and inertia weight), 
Fuzzy Logic (FL) can be first exploited to determine the 
best values of these parameters. So far, the PSO implementa-
tions based on FL aim at calculating distinct settings for the 
swarm as a whole. Nobile et al. [138] proposed a new algo-
rithm called Fuzzy Self-Tuning PSO (FST-PSO) which, for 
every particle, independently calculates the minimum and 
maximum velocity, social and cognitive factors, and inertia 
by exploiting FL, thereby creating a completely setting-free 
variant of PSO. The strength and novelty of FST-PSO was 
derived from the fact that there is no experience required to 
formulate PSO, since the optimization process automatically 
adaptively adjusts the behavior of each particle.
In [114], López et al. proposed a Fuzzy Logic Controller 
(FLC) modified by PSO, namely, Fuzzy-PSO to increment 
the lifetime of power electronics with a faster response of 
drive’s speed in a brushless DC electric motor. Furthermore, 
the reference temperature and the desired speed are proposed 
as parameters to formulate an objective function.
5.2.3  Mutation
Salajegheh and Salajegheh [157] combined PSO with gradi-
ent directions of first and second order, thereby achieving a 
great increasing in the approach robustness. The literature 
was thoroughly searched to choose an appropriate set of 
design problems, and the results of the standard PSO and the 
counterparts are compared with each other. In the proposed 
approach, the overall optimization cost was trivial as a result 
of decreasing the number of initial particles.
A modified variant, namely, Repository and Mutation 
based PSO (RMPSO) was proposed in [75]. In RMPSO, 
global and personal best solutions with the same fitness val-
ues are stored in two maintained extra repositories. And, 
another proposed Enhanced Leader PSO (ELPSO) indicated 
that the swarm optimum could be improved by applying five 
successive mutation strategies.
5.2.4  Lévy Flight (LF)
Lévy Flight (LF) is a particular category of random walk in 
which a heavy power tails law is applied for the distribution 
of step lengths. A global search is done or conducted by an 
algorithm with the occasional aid of larger steps. A better 
trade-off between the two capabilities of exploration and 
exploitation in an algorithm could be gained by applying 
the LF trajectory [47], and the ability to avoid local optima 
gives plus points.
In [213], Zhang et al. established an optimization model 
for the task scheduling model in the Multiple-Input and Mul-
tiple-Output (MIMO) radar, and proposed a hybrid Discrete 
PSO (DPSO) algorithm with LF for solving the problem. 


---

<!-- Page 13 -->
## Page 13

2543
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
The internal structure of tasks, the features of the MIMO 
radar task scheduling, and the three main principles of task 
scheduling were all considered in the optimization model. 
In another work, Tang et al. [175] employed the signal level 
of Automatic Identification System (AIS) to build a new 
method for estimating the atmospheric profile refractivity, 
specifically the parameters of surface-based duct in the mari-
time environment. Due to the complexity and non-linearity 
of this optimization problem, LF with QPSO algorithm (LF-
QPSO) was proposed to find the optimal solution.
In [100], Li et al. developed a novel Unsupervised LF 
with PSO method (ULPSO) for image classification, giving 
a good exploration-exploitation balance. ULPSO depends on 
a new searching mechanism that targets the worst particle in 
the swarm at each iteration to update its position with LF.
5.2.5  Opposition‑Based Learning (OBL)
Tizhoosh [181] originally introduced the basic idea of 
Opposition-Based Learning (OBL). Based on the concept of 
OBL, typically, the fitness values of current agents and their 
opposites are evaluated [119]. Then, the suggested algorithm 
selects N agents with the highest/lowest fitness values.
In [86], Kang et al. proposed a hybrid PSO algorithm to 
improve the PSO performance by maximizing PSO diver-
sity introduced by OBL. Probabilistic OBL was adapted for 
a swarm by the proposed hybrid algorithms. Unlike other 
fusions of PSO and OBL, the fitness of the entire swarm was 
improved by selecting the fittest particles from the current 
swarm and its opposite one.
In [189], Wang et al. addressed the learning strategy 
impact on a scheduling problem with two-stage assembly 
flow shop. Three different machines were used to, in turn, 
process several different workpieces. The total completion 
time was minimized by developing a branch-and-bound 
technique combined with a lower bound procedure and 
several developed dominance rules to obtain the optimal 
scheduling solution. Besides, high-quality feasible solutions 
were obtained by devising a new Dominance Rule-based 
Opposition-based PSO algorithm (DR-OPSO).
5.2.6  Surrogate
Surrogate-assisted optimization was established to handle 
expensive and complex problems in real-world applications. 
The methodology of this type of optimization depends on 
the maximal exhaustion of the available information for 
minimizing the number of expensive evaluations required 
for a given objective function, thereby reducing the related 
costs, resources, and time [169].
Related to this, Yu et al. [207] proposed a hierarchical 
surrogate-assisted particle swarm optimizer comprising a 
Social Learning-based PSO algorithm (SL-PSO) and the 
standard PSO algorithm itself with the goal of solving high-
dimensional problems. The cooperation between SL-PSO 
and standard PSO was proposed so that the search space 
can be thoroughly exploited and explored, and the surrogate 
model global and local search performance is simultane-
ously improved.
In [203], Yang et al. proposed an Improved Surrogate-
Assisted PSO (ISAPSO) algorithm, in which global and 
local surrogates are integrated into a hybrid PSO. The global 
surrogate uses an efficient global optimization algorithm to 
work as a global searcher for speeding up the PSO global 
search process, and reduces the computational burden by 
predicting the fitness values. Meanwhile, the local surrogate 
explores the expected optimum solution so that it can later 
locally search through the neighborhood of this solution.
5.3  Variants of PSO
Different variants of the PSO algorithm are addressed in 
this section.
5.3.1  Binary
Continuous meta-heuristics cannot handle a variety of opti-
mization problems. Therefore, combinatorial optimization 
has emerged, which includes a type of optimization called 
binary optimization. The {0, 1} set elements are distinct 
decision variables in binary optimization problems. Thus, 
the binary optimization problem can have 0 and 1 as poten-
tial values for each decision variable. In other words, the 
decision variables can be digitally expressed as 0 or 1 with 
respect to the binary optimization problem at hand.
Sameer et al. [158] proposed a new Modified Binary PSO 
with a Kernel Fuzzy Clustering Method (MBPSO-KFCM) 
for selecting relevant features and determining the number 
of clusters in fuzzy data clustering. To enhance the quality 
of cluster analysis, Gustafson-Kessel (GK) algorithm was 
established and improved. The datasets Taiwanese, German, 
and Australian credit were used to test the performance of 
the three proposed algorithms. The results showed that fuzzy 
partition (classification) is robust based on the fuzzy Rand 
validity metrics, which provides an opportunity to reduce 
the risk associated with loans.
In [89], Karbassi Yazdi et al. proposed a Binary PSO vari-
ant (BPSO) for optimally solving the problem of ship routing 
and scheduling in Liquefied Natural Gas (LNG) extraction, 
transportation, and regasification.
5.3.2  Chaotic
Generally, chaotic, adapted from the term “chaos”, formally 
refers to such a property that describes the unpredictable 
behavior of a complicated system. In chaotic systems, a 


---

<!-- Page 14 -->
## Page 14

2544
	
A. G. Gad 
1 3
function is used to “map” or associate algorithm chaotic 
behavior with some parameters, using two typical chaotic 
maps: logistic and sine. Chaos has distinctive properties of 
non-repeatability and periodicity. So, it has the ability to do 
general searches at higher speeds compared to the probabil-
istic stochastic searches [72].
In [200], Xu et al. proposed a new Chaotic Search PSO 
algorithm (CS-PSO) which enhances the PSO algorithm 
with the CS method for solving combinatorial optimization 
problems. In the initialization phase, the particles were posi-
tioned depending on the advance knowledge of the combi-
natorial optimization problems. Furthermore, in the chaos 
perturbing phase, the positions and velocities of particles are 
perturbed by introducing a brand-new range of rules for sat-
isfying the adaptability and the capability of the ideal global 
search with the major aim to effectively avoid the fruitless 
early convergence that haunts the standard PSO algorithm.
In another work, Wang et al. [188] presented an efficient 
multi-objective optimization approach that combines an 
adaptive chaotic PSO and the IsoGeometric Analysis (IGA) 
to optimize the Ceramic Volume Fraction (CVF) distribu-
tion under eigenfrequencies in Functionally Graded Plates 
(FGPs). And, the B-spline basis function was used to repre-
sent the CVF distribution.
In [209], Yue et al. proposed a hybrid PSO algorithm 
based on the chaos theory for solving the mobile loca-
tion estimation problem. In the proposed location estima-
tion approach, it was crucial to consider the influence of 
measurement error arising from the nonlinear optimization 
problem and Angle Of Arrival (AOA)/Time Difference Of 
Arrival (TDOA) hybrid location method. The proposed 
algorithm recognized the AOA/TDOA hybrid location algo-
rithm to track the object to significantly enhance the locating 
accuracy and the performance of the estimation process in 
general.
5.3.3  Multi‑objective
Multi-Objective Problems (MOPs) [108] is to be introduced 
in this section. Minimizing or maximizing multiple conflict-
ing objective functions are two main tasks often considered 
in MOPs [148, 221]. Unlike single objective optimization 
ones, MOPs involve multiple contradictory objective func-
tions. It is not easy to simultaneously optimize many func-
tions. Hence, for obtaining an optimal solution set, there 
should be balance between the objective functions. Some 
constraints and at least two objectives must be included in a 
multi-objective optimization problem. In a solution space, 
the objectives and constraints are satisfied through finding 
mutually acceptable solutions.
In [214], Zhang et al. proposed a multi-objective parti-
cle swarm optimizer based on a competitive mechanism, 
in which the current swarm performs, at each iteration, 
pairwise competitions which in turn are used to update the 
position particles. On the other hand, a bi-objective prob-
lem was formulated for the hand posture estimation problem 
[160]. To solve this problem, the concepts of Evolutionary 
Population Dynamics (EPD) were employed for developing 
an improved version of MOPSO. This problem has different 
types of parameters. Therefore, some of the parameters were 
significantly calibrated by the MOPSO algorithm.
In [219], Zheng et al. presented an adaptive neighbor-
hood function for developing a Multi-Objective Cellular 
PSO (MOCPSO). Three objective functions were taken for 
drilling a wellbore trajectory less costly, more quickly, and 
safely, compared to other potential trajectories. Then, a set of 
Pareto optimal solutions is gained by applying the MOCPSO 
algorithm to the three objective functions for designing a 
cheaper and safer wellbore trajectory.
Adhikari and Srirama [5] developed a new Container-
based Energy-Efficient Scheduling method (CEES) that 
responds effectively to different types of fast submitted 
Internet of Things (IoT) and non-IoT tasks. A Multi-Objec-
tive Accelerated PSO (MOAPSO) technique was used in 
the proposed method to ensure a minimum delay by finding 
the most appropriate container for executing each task. To 
better utilize cloud resources, cloud environment involves 
other important missions of resource scheduling, which can 
be explored in [64].
6  PSO Applications
In accordance with the SR process adopted in this study, this 
section is to provide a technical review of the designated 
PSO applications in the actual literature. Figure 5 demon-
strates a comprehensive taxonomy of the PSO applications 
in different domains, including health-care, environmental, 
industrial, commercial, smart city, and general aspects. Each 
category of PSO applications is likely to face some issues 
that should be highlighted to come up with thriving solu-
tions, enabling further efficient and viable PSO implementa-
tion in future real-world applications. Consequently, studies 
focusing on some pivotal issues are reviewed to prop PSO 
applications in a particular context associated with these 
issues. For example, in environmental applications, the main 
contexts, such as economic emission dispatch, parameter 
identification of PhotoVoltaics (PV), pollution forecasting, 
segmentation and classification of plants, flood control and 
routing, water quality monitoring, and many other issues, are 
floated in different aspects of environmental PSO applica-
tions. Thus, this paper presents a taxonomy based on diverse 
categories of PSO applications in selected research studies 
in which special subjunctives are addressed and discussed. 
Considering the concerns and challenges in various types 
of PSO applications, I firstly addressed different categories 


---

<!-- Page 15 -->
## Page 15

2545
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
in the PSO applications and then reported the main subjects 
which have been paid special attention in each category. 
PSO applications have some general concerns, so a division 
in the taxonomy, namely “general aspects”, was adopted to 
refer to the studies that introduced a proposal to cope with a 
particular challenge in any general type of PSO applications. 
In other words, a new conceptual approach is introduced 
based on the studies shown as being of general aspects, thus 
promoting the development of any type of PSO application.
The upcoming subsections present diverse approaches in 
PSO applications. In addition, various researches will be 
compared from several sides, such as key subject, case stud-
ies, strengths, shortcomings, and special outputs.
6.1  Health‑Care Applications
Table 3 illustrates a summary of some seminal researches 
and important information to assess health-care approaches 
in PSO applications. Some of the major contexts in the 
health-care domain are based on intelligent diagnosis, dis-
ease detection by medical robots, medical image segmenta-
tion, and disease classification.
6.2  Environmental Applications
Table 4 illustrates a summary of the recent researches 
and important information to assess the environmental 
approaches in PSO applications. The approaches include 
case studies, such as wild vegetation environmental moni-
toring, agriculture environmental monitoring, flood control 
and routing, water quality monitoring, and pollutant concen-
tration monitoring systems.
6.3  Industrial Applications
Table 5 illustrates a summary of the recent researches and 
important information to assess the industrial approaches in 
PSO applications. Some of the major contexts in the indus-
trial domain include economic dispatch problem in power 
systems, optimizing Phasor Measurement Units (PMUs) 
placement, allocating daily electrical loads, deploying 
WSNs, predicting the defection of products, and optimizing 
the design and operation of microgrids.
6.4  Commercial Applications
Table 6 illustrates a summary of some seminal researches 
and important information to assess the commercial 
approaches in PSO applications. Some of the major contexts 
in the commercial domain include prediction of cost and 
price, risk assessment, and profit calculation.
6.5  Smart City Applications
Table 7 illustrates a summary of some seminal researches 
and important information to assess the smart city 
approaches in PSO applications. The approaches include 
case studies, such as smart city, smart home, appliance 
scheduling, and vehicular monitoring systems.
6.6  General Aspects of PSO Applications
Table 8 describes a summary of some seminal researches 
and important information to assess the general approaches 
in PSO applications. Some of the major contexts in the 
Fig. 5   The taxonomy of PSO applications


---

<!-- Page 16 -->
## Page 16

2546
	
A. G. Gad 
1 3
Table 3   Summary of some seminal researches in health-care applications
Research
Main subject
Strengths
Shortcomings
New finding(s)
Pashae et al. [140]
Disease diagnostic system by identifying 
the most beneficial genes for classifica-
tion
• Identifying biologically and statisti-
cally significant genes from the clinical 
datasets
• A better performance of the fusion of 
Binary Black Hole Algorithm (BBHA) 
and BPSO (4-2)
• Not considering computational time
• Hybrid meta-heuristic approach
Zeng et al. [212]
Diagnosis of Alzheimer’s Disease
• Outperforming several SVM models and 
two other state-of-the-art deep learning 
methods
• Experimenting with only one dataset, 
ADNI
• Framework
Jain et al. [74]
Cancer diagnosis and classification using 
DNA microarray technology
• Providing a serious solution to the inher-
ent local optimum problem in traditional 
BPSO
• Ensuring faster and more reliable gene 
selection in classification
• Not considering computational time
• Two-phase hybrid model
Li et al. [104]
Medical image segmentation
• Getting better exploited contextual 
information
• Improving the performance of dynamic 
context cooperative QPSO
• Limited variation of image segmentation 
problems
• Algorithm
Raj and Ray [151]
ECG signal analysis
• Positive predictivity
• High sensitivity
• High overall accuracy
• Not performing real-time analysis
• Not incorporating many classes of 
arrhythmia signals for analysis
• High computational time
• Hybrid algorithm
Srisukkham et al. [168]
Intelligent Leukaemia diagnosis
• Escaping from the local optima trap
• Accelerated chaotic search
• Not considering the velocity, as well as, 
only updating the particles’ positions
• Two modified BBPSO algo-
rithms


---

<!-- Page 17 -->
## Page 17

2547
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
Table 4   Summary of some seminal researches in environmental applications
Research
Main subject
Case study
Strengths
Shortcomings
New finding(s)
Kumar et al. [97]
Short-term temperature predic-
tion using ambient sensors
Environmental monitoring
• Improving the generalization 
performance
• Improving the accuracy
• Not testing in a real environ-
ment
• Hybrid model
Zarei et al. [210]
Multi-purpose water reservoir
Shahid Dam Reservoir in Fars, 
southern Iran
• Low computational time
• High mean water release 
values
• High reliability
• Not evaluating monetary cost
• Hybrid evolutionary algorithm
Chen et al. [33]
Forecasting short-term atmos-
pheric pollutant concentration 
based on PSO-SVM
Temple of Heaven, Beijing
• High forecasting accuracy
• Low runtime
• Considering temporary 
emergencies (such as major 
holidays) as influential factors
• Hybrid forecasting model
Rahgoshay et al. [149] Predicting daily suspended 
sediment load
Royan and Veynakeh earth 
dams in Semnan, Iran
• Increasing accuracy
• Reducing the computational 
time and RMSE
• Structure is so simple and 
does not have complex 
parameters
• Support vector method
Kour and Arora [95]
Segmentation and classification 
of plants based on leaf images 
using hybrid PSO-SVM
Agriculture environment
• High accuracy
• Low computational time
• Not considering plants with 
medicinal and scientific 
significance
• Automatic vision-based 
method
Cao et al. [29]
Remote sensing to monitor 
water quality based on HJ-1A 
HSI imagery
Inland waters in Weishan Lake, 
China
• High prediction
• High stability
• Fast convergence
• Using hyperspectral sensors 
with low spectral resolution
• Not testing on diverse lakes
• Catastrophe strategy-modified 
BPSO
Ali Ghorbani et al. [8]
Forecasting daily pan evapora-
tion based on hybrid ANN-
QPSO embedded into a multi-
layer perceptron method
Talesh meteorological station in 
Northern Iran
• High level of accuracy
• Not addressing non-stationar-
ity in the climate datasets
• Uncertainty in the forecasted 
evaporation data
• Forecasting & decision-support 
tool
Ehteram et al. [45]
Improving the Muskingum 
flood routing method
Wilson, Karahan, and Viess-
man and Lewis floods in the 
USA and UK
• Increasing significance in 
Obtaining the best solutions
• Decreasing the computational 
time
• Building the Muskingum 
models with little parameters
• Hybrid BA and PSO algorithm
Camci et al. [28]
Quality inspection for rice 
farms by employing quad-
copters
Rice farms in Longsheng, 
China
• High performance in han-
dling noise and uncertainties 
in the system
• Ineffective quadcopter control 
in natural landscapes
• Control structure


---

<!-- Page 18 -->
## Page 18

2548
	
A. G. Gad 
1 3
general domain include service allocation, image segmen-
tation, scheduling, prediction, and security management.
7  Discussion and Comparisons
Similar to many other meta-heuristic algorithms, PSO has 
distinctive advantages, as well as some unavoidable short-
comings. Although there is no evidence of convergence for 
this algorithm, the results presented in this study indicate its 
competitiveness over, for example, EAs in terms of conver-
gence rates and accuracy in many cases. Table 9 lists some 
of the impacting strengths and weaknesses of PSO.
Previous sections discussed the review process of the 
selected studies regarding PSO methods and applications. 
In turn, this section statistically analyzes those methods and 
application areas. Furthermore, the proposed AQs proposed 
in Sect. 4 are called to present some analytical reports as 
follows:
Table 5   Summary of some seminal researches in industrial applications
Research
Main subject
Strengths
Shortcomings
New finding(s)
Maiyar and Thakkar [120]
Food grain transportation 
problem
• Reducing food grain 
wastages
• Economic and environ-
mental results
• Not considering perish-
able food grain products
• Algorithm
• Decision support tool
Alnaqi et al. [10]
Prediction of energetic 
performance of a building 
integrated photovoltaic/
thermal system
• High performance
• High reliability
• Not considering scal-
ability
• Neural network model
• Hybrid algorithm
Mohebbi et al. [132]
Optimal design of a 
mechatronic quadrotor 
system
• Integrated concurrent 
design
• Not evaluating on a 
multi-agent platform
• Algorithm
Wang et al. [192]
Recognizing and diagnos-
ing potential faults for 
nuclear power plants
• Improving the classifica-
tion accuracy
• Reducing the training 
time
• Reducing noise
• Not evaluating actual 
data
• Hybrid fault diagnosis 
method
• Hybrid algorithm
Liu et al. [111]
Multi-objective optimi-
zation design of the 
airborne electro-optical 
platform
• Reducing mass
• Improving stability
• Reducing mechanical 
resonance
• Only three targets were 
considered in the multi-
objective optimization 
problem
• Hybrid algorithm
Ghorbani et al. [57]
Optimal sizing of an 
off-grid house with PV 
panels, Wind Turbines 
(WTs), and battery
• Increased reliability
• Minimizing the total 
monetary cost
• Not presenting the total 
accuracy evaluation
• Hybrid PV-WT generat-
ing unit
• Hybrid algorithm
Jiang et al. [77]
Generating association 
rules for supporting 
effective design based on 
online customer reviews
• Low time-consuming
• Low monetary cost
• Inability to detect spam-
ming reviews
• Affected by sentimental 
reviews
• Algorithm
• Decision support system
Song et al. [167]
Positioning a 3D wind 
turbine with multiple hub 
heights on flat terrain
• High power production
• Low monetary cost
• Lack of assessment on 
complicated and realistic 
wind farm optimization 
problems
• Hybrid algorithm
Qi et al. [145]
Predicting the unconfined 
compressive strength of 
cemented paste backfill
• Low cost
• Low response time
• High accuracy
• Not foreseeing the long-
term strength
• Omission of some influ-
encing variables
• Algorithm
Lopes et al. [113]
Distribution of electrical 
loads throughout the day 
in an industrial environ-
ment
• Minimizing the cost of 
industry production
• Better-quality solutions
• Not evaluating computa-
tional time
• Testing on small datasets
• Hybrid algorithm
Rahman and Zobaa [150]
Optimizing PMUs place-
ment
• Reducing the computa-
tional cost
• Reducing the number of 
PMUs needed for IEEE 
300-bus system
• Not considering scal-
ability
• Algorithm


---

<!-- Page 19 -->
## Page 19

2549
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
•	 AQ1: Into which domains can PSO methods and applica-
tions be classified?
According to the taxonomy exhibited in Sect. 5, Fig. 6 
depicts a comparison of the percentages of PSO methods as 
of the date of this study. I considered three PSO methods that 
span hybridization, improvement, and variants. As shown in 
Fig. 7, PSO variants have the largest share of PSO methods 
in the literature at 42%. Of course, hybridization techniques 
have 32%, and improved PSO approaches have 26% usage 
of the PSO methods.
 
Similarly, according to the taxonomy exhibited in Sect. 6, 
Fig. 8 depicts a comparison of the portions of PSO appli-
cations as of the date of this study. Six PSO application 
domains, including health-care, environmental, industrial, 
commercial, smart city, and general aspects applications, 
are considered. If we look closely, the general approach has 
the largest percentage of application areas in the literature 
with a usage ratio of 27%. Of course, industrial applications 
have 20%, environmental applications have 17%, smart city 
applications have 16%, health-care applications have 11%, 
and commercial applications have 9% usage out of the over-
all PSO applications domain.
•	 AQ2: Which main contexts can be considered for PSO 
methods and applications?
Within the framework of this study, the main contexts of 
PSO methods and applications are shown in Fig. 9. It has 
been observed that the electrical engineering field received 
the most attention from scholars and practitioners with 13 
studies, while prediction, image processing, and mechanical 
engineering approaches were 6 studies.
•	 AQ3: What assessment environments are used for evalu-
ating the PSO methods and applications?
According to Fig. 10, it has been observed that 47% of the 
research studies apply simulation tools to evaluate the pre-
sented case studies in the PSO community. In addition, it has 
been observed that 33% of the research papers have imple-
mented approaches to develop PSO methods and applica-
tions. Moreover, 11% of the researches have not presented 
any simulation or implementation for the indicated methods 
and application domain. Finally, 9% of the existing studies 
use datasets to apply analysis approaches (e.g., testing and 
prediction) for assessing the involved case studies.
8  Challenges and Future Opportunities
While PSO has been effectively applied in versatile domains, 
challenges are required to be addressed and drawn as future 
research directions. In the past few years, PSO has gained an 
increasing interest from researchers and has been utilized in 
different areas of applications. However, critical problems 
and issues remain. Thus, more research efforts should be 
done by scholars and researchers to conquer the challenges 
and problems that may hinder the future application of PSO. 
Moreover, further inspirations and more effective techniques 
should be pursued to develop novel PSO approaches. For 
example, the research community needs to address new 
methodologies for complex problems. Based on the litera-
ture review, I discuss below different open issues and related 
topics for potential future research.
I should point out that the assortment of PSO methods 
and applications mentioned in this study applied the SR pro-
cess so that the challenges discussed in the following two 
subsections are presented as the AQ4:
Table 6   Summary of some seminal researches in commercial applications
Research
Main subject
Strengths
Shortcomings
New finding(s)
Jiao et al. [78]
Optimal location for an 
electric business centre
• Social benefits
• Low cost
• High transportation 
convenience
• Not including the multi-
objective concept
• Location estimation 
model
• Hybrid algorithm
Tang et al. [174]
Forecasting building mate-
rials’ prices
• High scalability
• Fast convergence rate
• High prediction precision
• Not evaluating computa-
tional time
• Price prediction model
• Hybrid algorithm
Shen and Han [165]
Profit calculation module 
of financial accounting 
information system
• Getting real-time finan-
cial processing results
• Not considering compu-
tational cost
• Accounting information 
system
Yi et al. [205]
Cost prediction of trans-
mission line project
• Strong practical signifi-
cance
• Improving the accuracy
• Not evaluating scalability • Intelligent cost prediction 
model
Pradeepkumar and Ravi 
[144]
Forecasting volatility from 
financial time series
• Yielding statistically 
significant results
• Not evaluating the overall 
computational time
• Neural network model


---

<!-- Page 20 -->
## Page 20

2550
	
A. G. Gad 
1 3
Table 7   Summary of some seminal researches in smart city applications
Research
Main subject
Case study
Strengths
Shortcomings
New finding(s)
Abid et al. [4]
Managing energy in smart homes
Residential area of ten homes • Low cost
• Low power consumption
• Not comparing the presented 
method with other existing ones
• Not evaluating accuracy
• Energy management 
strategy
• Algorithm
Zhang et al. [217]
GIS-based placement of charging 
stations for electric vehicles
Changping, Beijing, China
• High revenue
• High coverage
• Low cost
• Considering only two scenarios
• Algorithm
• Placement model
Li et al. [102]
Forecasting Day-ahead traffic flow
Highways
• High stability
• High accuracy
• High time-consuming
• The dataset is for a small fraction 
of a highway
• Hybrid model
• Algorithm
Jordehi [82]
Scheduling shiftable appliances
Smart home
• Reducing consumers’ daily 
electricity bill without affecting 
their comfort
• Not considering scalability
• Hybrid algorithm
Le et al. [99]
Estimating and controlling the 
heating load of buildings
Smart city
• Robust technique
• High reliability
• Not evaluating cost
• Low accuracy of some proposed 
models
• Hybrid algorithm
Ma et al. [118]
Appliance scheduling
Residential unit
• Obtaining profits from selling 
electricity to the power grid
• Good convergence performance
• Uncertainty of renewable genera-
tion
• Appliance scheduling 
model
Hu et al. [65]
Scheduling urban traffic light
An area centering Xudong, 
Wuhan, China
• Elaborating traffic congestion
• Controlling vehicle movements
• Not considering the case of self-
organized cities
• Not considering scalability
Not evaluating cost
• Hybrid algorithm
Sato et al. [161]
Multifaceted optimization of power 
grids
Smart city
• Improving the solution quality
• Not evaluating monetary cost
• Low scalability
• Not verifying the robustness
• Hybrid algorithm
Ramya et al. [152] Retrieval of deprived riot video 
data
Smart city
• Can be used with other signal 
and image processing techniques
• Identifying the previous criminal 
records in a particular region of 
the smart city
• Low accuracy when processing 
large databases
• Algorithm


---

<!-- Page 21 -->
## Page 21

2551
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
Table 8   Summary of some seminal researches in general aspects of PSO applications
Research
Main subject
Strengths
Shortcomings
New finding(s)
Bhattacharya et al. [24]
Permission based detection of 
Android malwares
• High scalability
• High classification perfor-
mance
• Considering only the per-
missions set
• Not handling float datasets
• Hybrid algo-
rithm
Sivaranjani et al. [166]
Speckle noise removal in 
SAR images
• Considering reference and 
no-reference metrics in 
experiments
• Optimizing threshold values
• Not considering scalability
• Algorithm
• Framework
Zarrouk et al. [211]
Job shop scheduling problem
• Low CPU time
• High-quality solutions
• Not considering the cost
• Algorithm
Mansouri et al. [122]
Task scheduling in cloud 
computing
• Low resource usage
• Low execution time
• Not trying in a real cloud 
environment
• Not combining fault toler-
ance parameters in cloud
• Not considering the prec-
edence of tasks and load 
balancing
• Algorithm
Lin et al. [107]
Set-union knapsack problem
• High-quality solutions
• High computational cost
Hybrid algorithm
Zhong et al. [220]
Travelling salesman problem
• High balance between 
intensification and diversi-
fication
• Not comparing with a sub-
stantial number of previous 
optimization techniques
• Algorithm
Mokhtari and Noroozi [133]
Flow shop scheduling 
problem
• No job earliness or tardi-
ness
• Considering only com-
mercial optimization of 
problem instances with 
small size
• Algorithm
Sun et al. [172]
Locating attacks’ position in 
WSNs
• Low energy consumption
Low task processing time
• Not locating the attack 
source nodes
• Algorithm
Thabit and Mohades [176]
Path planning of multi-robots
• Short, safe, and smooth 
paths
• Not implementing real-
world case studies
• Algorithm
Nouiri et al. [139]
Job shop scheduling problem
• Decentralizing decisions
• Effectiveness in directing 
real production
• High energy consumption
• Not all entities participate 
in the final solution
• Architecture
Alswaitti et al. [11]
Data clustering
• High cluster compactness
• High classification accuracy
• Lack of assessment on real-
world applications
• Algorithm
Suresh and Lal [173]
Segmentation of satellite 
images based on multilevel 
thresholding
• Robust and fast algorithm
• High Stability
• Low quality metric values
• High computational time
• Algorithm
Sheikholeslami and Navimi-
pour [164]
Service allocation in cloud 
computing
• High revenue for cloud 
users and providers
• Fast resource provisioning
• High resource utilization
• No sensitivity analysis 
for different weighting 
parameters
• Not implementing in realis-
tic cloud environment
• Not evaluating customer 
satisfaction
• Algorithm
Table 9   Advantages and disadvantages of PSO
Advantages
Disadvantages
• Simple implementation
• Relatively few parameters to tuned
• Ability to run parallel computations
• Robustness
• Higher efficiency and probability to find the global optima
• Fast convergence
• No overlapping or mutation
• Low computational time
• Ability to build accurate mathematical models for solving complex 
problems
• Difficulty to initialize control parameters
• Inability to work out the problem of swarm scattering
• Premature convergence and trapping into the local minima especially 
on solving high-dimensional problems


---

<!-- Page 22 -->
## Page 22

2552
	
A. G. Gad 
1 3
•	 AQ4: What are generally the PSO open perspectives and 
future research directions that can be drawn from the 
work presented in the paper?
8.1  Open Issues
Premature convergence When applying the traditional PSO 
algorithm, if the search gets closer to the local optimal solu-
tion through random initial conditions, the optimal solution 
for a single particle (individual particle optimum) and the 
optimal solution for all particles (the group/global optimum) 
would both converge towards the local optimal solution, and 
a deceptive optimization result will therefore be obtained. 
Thus, it is not possible to guarantee the capability of finding 
the global optimal solution. As a result, the fast convergence 
capability will be ineffective. Over the past few years, the 
issue of stagnation (premature convergence) has been a sub-
ject of research in the PSO community [197, 208]. A road-
map for future research in this regard can be created based 
on some topics, including particles’ stability analysis [26], 
redistributing mechanism [146], and random sampling of 
control parameters [171].
Convergence speed controller Despite the typical fast 
convergence of PSO, it may be trapped into a local optimum 
due to premature converge. Therefore, a convergence speed 
controller was devised for the ultimate goal of solving this 
Learning Strategy
19%
Fuzzy Logic
23%
Muta	on
13%
Lévy Flight
16%
Opposi	on-Based 
Learning
16%
Surrogate
13%
Fig. 6   Percentage of the presented PSO methods
Fig. 7   Total percentage of the presented PSO methods
Fig. 8   Percentage of the presented PSO applications
Fig. 9   Percentage of the main 
contexts for PSO methods and 
applications


---

<!-- Page 23 -->
## Page 23

2553
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
problem. Two adaptive approaches were proposed to adjust 
the convergence speed. First, when the particle prematurely 
converges, the convergence speed is slowed down. Second, 
when the particle cannot update its best solution in the pre-
sent time, the convergence speed of PSO is accelerated. 
Thus, a key residual challenge is developing an effective 
convergence speed controller [110]. In the same context, for 
improving the convergence speed of PSO-based algorithms, 
the social and cognitive components of the velocity update 
formula are modified based on the fitness of each particle 
[125]. In addition, the convergence speed is adaptively con-
trolled to empower the PSO algorithm for solving large-scale 
numerical optimization problems [66]. Hence, designing 
an appropriate convergence speed controller framework for 
PSO has become a major challenge in this topic.
High-dimensional search space Because of the curse of 
dimensionality problem, the effectiveness of PSO applica-
tion to classification of high-dimensional data has recently 
gained a major concern [9]. In a recent study, the effec-
tiveness of PSO approach for feature selection has been 
demonstrated. However, due to the large search space, the 
challenge sill exists to apply PSO-based feature selection to 
high-dimensional datasets with tens of thousands of features 
[182]. In addition, the PSO algorithm can be adapted for 
the problem of high-dimensional feature selection, providing 
thereby an efficient technique for achieving similar or even 
better classification accuracy by not using all features but 
instead selecting only a small set of relevant features from 
a wide range of features [58]. The key challenges in this 
area include novel approaches like Monte Carlo methods 
[22] that simultaneously minimize the number of chosen 
features and maximize the classification accuracy in PSO 
applications.
Memory requirement All living systems have memory 
as an essential feature. According to the evolutionism per-
spective, it is worthwhile examining the potential helpful 
role of historical memory in the process of EAs. That is 
mainly because the explicit or implicit historical memory in 
PSO improves the search process by storing promising solu-
tions and reusing them in later stages [101]. Furthermore, 
a new inertia weight can be generated by using historical 
memory through a parameter adaptation mechanism. There-
fore, improving PSO using historical memory is a pressing 
challenge [60, 103]. And how to set the memory size adap-
tively can be also considered as an interesting topic to be 
addressed in the future [117].
Parameter & topology selection In PSO-based algo-
rithms, the best performance can be achieved by elaborately 
determining the control parameters. However, choosing 
these parameters cannot be adequately guided. To address 
the job of parameter selection, future efforts in this topic 
should include choosing the best parameters based on simu-
lations [38], parametric analysis in a computational envi-
ronment with limited resources [162], and hyper-parameter 
selection based on heuristics [115]. On the other hand, the 
performance of PSO in engineering applications is signifi-
cantly affected by topology selection, and each problem has 
its appropriate optimal topology. However, this issue still 
lacks much study. As a future direction, topology selection 
for PSO can be better guided by taking into account factors 
affecting the optimality of algorithmic parameters (i.e., the 
topological degree and the number of particles) with the aim 
of selecting a proper class of deterministic regular topolo-
gies [112]. Other challenges including, studying and evaluat-
ing the performance of tree topology [155] and suggesting 
different topologies for the PSO optimizer in order to reach, 
for example, an optimal Proportional-Integral-Derivative 
(PID) controller design [3], are also pressing issues which 
calls for further research and audit.
8.2  Future Perspectives
PSO was practically applied for the first time to the domain 
of neural network training, which was indicated by the 
algorithm itself [93]. Many more areas of PSO methods 
and application have been explored ever since, including 
signal processing, power systems, combinatorial optimiza-
tion, design, data mining, control, telecommunications, and 
many others. To date, applications of PSO algorithms are 
reported in hundreds of publications [46, 59]. Although the 
main use of PSO is to solve unconstrained, single-objective 
optimization problems, a development has been made to 
PSO algorithms for solving constrained problems, multi-
objective optimization problems, problems with dynamically 
changing landscapes, discrete problems, and for finding mul-
tiple solutions as well [16]. However, several PSO methods 
and applications can be sophisticated in some areas as future 
research directions in this topic as follows:
Nuero Fuzzy Network (NFN) Nuero Fuzzy Network 
(NFN) is an intelligent method for system identification, 
Fig. 10   Percentage of the PSO assessment environments offered in 
the literature


---

<!-- Page 24 -->
## Page 24

2554
	
A. G. Gad 
1 3
modelling, prediction, and control. In NFN, gradient-based 
algorithms are generally used for training. However, these 
algorithms have some disadvantages concerning, for exam-
ple, getting stuck at local minima, which needs for complex 
gradient computations to be conquered. Accordingly, Kara-
kuzu et al. [88] used improved PSO to introduce the first 
embedded high-speed, low-cost implementation of NFN 
hardware through online training. It has been observed that 
that the effectiveness of the proposed NFN implementation 
is similar to other approaches in the literature, thereby gener-
ating a novel idea for future research. In a different approach 
to NFNs, Vijay and Jena [186] utilized the PSO to minimize 
the quadratic performance indices for obtaining optimal slid-
ing control parameters and PID parameters. In this study, 
Lyapunov stability theorem was used to improve the stabil-
ity of the system by integrating sliding mode control into 
artificial neuro fuzzy inference system. Thus, it can be con-
cluded that NFN can be applied to the robot manipulator for 
real-time control, where good control performance can be 
obtained by adaptively changing sliding control parameters 
under different input disturbances.
Color image processing In this regard, Gaussian PSO 
(GPSO) was used to develop a color image quantization 
algorithm [15]. In the proposed algorithm, each particle in 
the swarm is randomly initialized with k centroids (i.e. color 
triplets). The cluster with the closest centroid to a pixel in 
the image is recognized to assign this pixel to that cluster. 
The centroids obtained by K-means clustering are refined 
by applying the GPSO. Experimentation showed that using 
GPSO method for the color image quantization gives sig-
nificantly better image quality than conventional PSO-based 
approaches. In anther work, a multi-level color image thresh-
olding algorithm was developed on the bases of GLLA histo-
gram and Tsallis-Havrda-Charvát entropy of degree 훼 [27]. 
Compared with the existing models, the proposed model 
achieved better performance results by applying the PSO 
algorithm. However, so far only a limited number of studies 
reported how to apply together the quantization and multi-
level thresholding techniques to a color image.
Image registration Image registration is defined as tak-
ing several 2D images from various sources, such as Com-
puter Assisted Tomography (CAT) and Magnetic Resonance 
Imaging (MRI) scans, and combining them into a 3D image. 
Recently, a hybrid approach for registering medical images 
has been developed by employing a PSO method [1] and 
an adjusted mutual information as a similarity index, or 
general meta-heuristics [184]. However, there are still trend 
applications for future research, including registering the 
images of a printed circuit board placed on a conveyor belt 
using an improved scale invariant feature transform, feature 
extraction technique combined with PSO [39]. Also, using 
PSO algorithm for remote sensing images registration less 
affected by the correction rate [196] is another major trend 
for future research.
Computational biology A long DNA chain first needs 
to be divided into subset fragments for determining its 
sequence. Therefore, combinatorial optimization researchers 
used the DNA Fragment Assembly method (DFA) to solve 
the NP-hard problem of reassembling the fragment. The 
DFA problem is solved by applying the overlap-layout-con-
sensus model to maximize the overlapping score measure-
ment using a memetic PSO algorithm based on two initiali-
zation operators, as well as the local search operator [67]. 
On 19 DNA fragment datasets, the results revealed that the 
PSO algorithm combining SA-based variable neighborhood 
local search and TS achieves the best overlap scores. Future 
works could address interesting issues, such as reducing 
the computational time by using DNA sequence compres-
sion, improving the initialization method of the algorithm, 
using an alternative search approach, and so on. In a simi-
lar biological application, some variants of the PSO algo-
rithm have been utilized to extensively tackle the molecular 
docking problem and the problem of conformational search 
in protein-ligands [55, 136]. Ultimately, the literature has 
reported significant results. Thus, it is natural to solve bio-
logical problems by applying the PSO algorithm.
Recommender systems PSO was utilized as a tuning 
mechanism in a further area in which software tools are cre-
ated to develop recommendations to entrepreneurs or even 
end users. Explicit feedback data (i.e., votes or ratings) are 
usually used to build most of the existing recommender 
models. However, real-life scenarios do not always contain 
explicit feedback data. For example, a hybrid music recom-
mender system was suggested based on implicit feedback 
data by utilizing graph-based algorithms for making songs 
recommendations based on the user-s preferences and behav-
ior [90]. Furthermore, PSO-based web-page recommenda-
tion system was developed on health-care multimedia data 
to track user navigation behavior by utilizing semantic web 
mining [121]. In the future work, these systems can be fur-
ther extended to include other E-health care application, and/
or social networking sites like twitter and Facebook.
9  Conclusions and Recommendations
In this literature, the exploration query on 3,632 papers pub-
lished between 2017 and 2019 was executed to fulfill the 
proposed SR process. 2,140 papers related to PSO methods 
and applications were selected. Amongst them, I briefly 
discussed and analyzed only 84 papers to retain the proper 
length of the paper. According to AQ1, on the one hand, the 
PSO variants have the most percentage of the PSO methods 
in the literature by 42% of quota. Of course, hybridization 
techniques have 32%, and improved PSO techniques have 


---

<!-- Page 25 -->
## Page 25

2555
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
26% of portions of PSO methods. On the other hand, the 
general approach has the most percentage of the applica-
tion domains in the literature by 27% of quota, emphasiz-
ing the broad application of PSO in diverse subject areas. 
Also, industrial applications, environmental applications, 
smart city applications, health-care applications, commer-
cial applications have 20%, 17%, 16%, 11%, and 9% por-
tions of all existing PSO applications, respectively. It has 
also been observed that electrical engineering approaches 
have the highest percentage, with 13 studies, and prediction, 
image processing, and mechanical engineering approaches 
are with 6 studies, based on AQ2. According to AQ3, 47% 
of the research studies applied simulation tools to evaluate 
the case studies presented in the PSO environment.
According to the adopted SR process, I must acknowledge 
that not all present studies may have been analyzed; non-
peer reviewed, non-English book chapters, survey articles, 
and editorial papers were omitted. In this study, the findings 
of more than 120 authors and diverse studies were consid-
ered to perform a comprehensive research of the methods 
and application approaches in PSO. However, as the research 
ended in November 2019, it is not possible to guarantee that 
all relevant seminal works are covered herein, especially 
with the increasing number of studies in this field.
Finally, the SR method presented in this review focused 
primarily on PSO methods and applications. Through this 
study, the PSO methods and applications were comprehen-
sively understood. In addition, open issues and future per-
spectives were considered. However, the PSO algorithm still 
needs further research in the following areas:
•	 Studying the effects of heterogeneity in PSO algorithms.
•	 Hybridizing PSO with novel optimization techniques, 
such as Salp Swarm Algorithm (SSA) [130], Whale 
Optimization Algorithm (WOA) [129], Lion Optimiza-
tion Algorithm (LOA) [204], Elephant Herding Optimi-
zation (EHO) [191], and Jaya Algorithm (JA) [63, 153].
•	 Implementation of innovated smart city applications, 
such as smart metering, smart farming, smart logistics, 
and smart buildings.
•	 Further applications for addressing different issues in 
cloud computing.
•	 Addressing more complex/large-scale real-world prob-
lems, NP-hard problems, and discrete optimization prob-
lems to discover new limitations of PSO.
Funding  Open access funding provided by The Science, Technology & 
Innovation Funding Authority (STDF) in cooperation with The Egyp-
tian Knowledge Bank (EKB).
Declaration 
Conflict of interest  The single/corresonding author declares no con-
flict of interest.
Open Access  This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes 
were made. The images or other third party material in this article are 
included in the article's Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in 
the article's Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a 
copy of this licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
References
	 1.	 Abdel-Basset M, Fakhry AE, El-Henawy I, Qiu T, Sangaiah AK 
(2017) Feature and intensity based medical image registration 
using particle swarm optimization. J Med Syst 41(12):197
	 2.	 Abdelkader HE, Gad AG, Abohany AA, Sorour SE (2022) An 
efficient data mining technique for assessing satisfaction level of 
online learning for higher education students during the covid-
19. IEEE Access
	 3.	 Aberbour J, Graba M, Kheldoun A (2015) Effect of cost function 
and pso topology selection on the optimum design of pid param-
eters for the avr system. In: 2015 4th international conference on 
electrical engineering (ICEE). IEEE, pp 1–5
	 4.	 Abid S, Zafar A, Khalid R, Javaid S, Qasim U, Khan ZA, Javaid 
N (2017) Managing energy in smart homes using binary particle 
swarm optimization. In: Conference on complex, intelligent, and 
software intensive systems. Springer, pp 189–196
	 5.	 Adhikari M, Srirama SN (2019) Multi-objective accelerated par-
ticle swarm optimization with a container-based scheduling for 
internet-of-things in cloud environment. J Netw Comput Appl 
137:35–61
	 6.	 Al-Thanoon NA, Qasim OS, Algamal ZY (2019) A new hybrid 
firefly algorithm and particle swarm optimization for tun-
ing parameter estimation in penalized support vector machine 
with application in chemometrics. Chemom Intell Lab Syst 
184:142–152
	 7.	 Alam S, Dobbie G, Koh YS, Riddle P, Rehman SU (2014) 
Research on particle swarm optimization based clustering: a sys-
tematic review of literature and techniques. Swarm Evol Comput 
17:1–13
	 8.	 Ali Ghorbani M, Kazempour R, Chau KW, Shamshirband S, 
Taherei Ghazvinei P (2018) Forecasting pan evaporation with 
an integrated artificial neural network quantum-behaved particle 
swarm optimization model: A case study in talesh, northern iran. 
Eng Appl Comput Fluid Mech 12(1):724–737
	 9.	 Ali Yahya A (2018) Centroid particle swarm optimisation for 
high-dimensional data classification. J Exp Theor Artif Intell 
30(6):857–886
	 10.	 Alnaqi AA, Moayedi H, Shahsavar A, Nguyen TK (2019) Pre-
diction of energetic performance of a building integrated pho-
tovoltaic/thermal system thorough artificial neural network and 
hybrid particle swarm optimization models. Energy Convers 
Manag 183:137–148
	 11.	 Alswaitti M, Albughdadi M, Isa NAM (2018) Density-based par-
ticle swarm optimization algorithm for data clustering. Expert 
Syst Appl 91:170–186


---

<!-- Page 26 -->
## Page 26

2556
	
A. G. Gad 
1 3
	 12.	 Aydilek IB (2018) A hybrid firefly and particle swarm optimiza-
tion algorithm for computationally expensive numerical prob-
lems. Appl Soft Comput 66:232–249
	 13.	 Banks A, Vincent J, Anyakoha C (2007) A review of particle 
swarm optimization. Part i: background and development. Nat 
Comput 6(4):467–484
	 14.	 Banks A, Vincent J, Anyakoha C (2008) A review of particle 
swarm optimization. Part ii: hybridisation, combinatorial, multic-
riteria and constrained optimization, and indicative applications. 
Nat Comput 7(1):109–124
	 15.	 Barman D, Hasnat A, Sarkar S, Murshidanad MAR (2016) Color 
image quantization using gaussian particle swarm optimization 
(ciq-gpso). In: 2016 international conference on inventive com-
putation technologies (ICICT). IEEE, vol 1, pp 1–4
	 16.	 Beheshti Z, Shamsuddin SM, Hasan S (2015) Memetic binary 
particle swarm optimization for discrete optimization problems. 
Inf Sci 299:58–84
	 17.	 Beni G (1988) The concept of cellular robotic system. In: Pro-
ceedings IEEE international symposium on intelligent control 
1988. IEEE, pp 57–62
	 18.	 Beni G, Hackwood S (1992) Stationary waves in cyclic swarms. 
In: Proceedings of the 1992 IEEE international symposium on 
intelligent control. IEEE, pp 234–242
	 19.	 Beni G, Wang J (1993) Swarm intelligence in cellular robotic 
systems. In: Robots and biological systems: towards a new bion-
ics? Springer, pp 703–712
	 20.	 Benioff P (1980) The computer as a physical system: a micro-
scopic quantum mechanical Hamiltonian model of computers as 
represented by turing machines. J Stat Phys 22(5):563–591
	 21.	 Bernardino HS, Barbosa HJ, Fonseca LG (2011) Surrogate-
assisted clonal selection algorithms for expensive optimization 
problems. Evol Intel 4(2):81–97
	 22.	 Beskos A, Crisan D, Jasra A, Kamatani K, Zhou Y (2017) A 
stable particle filter for a class of high-dimensional state-space 
models. Adv Appl Probab 49(1):24–48
	 23.	 Bhattacharya A, Goswami RT, Mukherjee K (2018) A feature 
selection technique based on rough set and improvised pso algo-
rithm (psors-fs) for permission based detection of android mal-
wares. Int J Mach Learn Cybern, pp 1–15
	 24.	 Bhattacharya A, Goswami RT, Mukherjee K (2019) A feature 
selection technique based on rough set and improvised pso algo-
rithm (psors-fs) for permission based detection of android mal-
wares. Int J Mach Learn Cybern 10(7):1893–1907
	 25.	 Bonabeau E, Marco DdRDF, Dorigo M, Théraulaz G, Theraulaz 
G et al (1999) Swarm intelligence: from natural to artificial sys-
tems, 1st edn. Oxford University Press, Oxford
	 26.	 Bonyadi MR, Michalewicz Z (2015) Stability analysis of the par-
ticle swarm optimization without stagnation assumption. IEEE 
Trans Evol Comput 20(5):814–819
	 27.	 Borjigin S, Sahoo PK (2019) Color image segmentation based 
on multi-level tsallis-havrda-charvát entropy and 2d histogram 
using pso algorithms. Pattern Recogn 92:107–118
	 28.	 Camci E, Kripalani DR, Ma L, Kayacan E, Khanesar MA (2018) 
An aerial robot for rice farm quality inspection with type-2 fuzzy 
neural networks tuned by particle swarm optimization-sliding 
mode control hybrid algorithm. Swarm Evol Comput 41:1–8
	 29.	 Cao Y, Ye Y, Zhao H, Jiang Y, Wang H, Shang Y, Wang J (2018) 
Remote sensing of water quality based on hj-1a hsi imagery with 
modified discrete binary particle swarm optimization-partial least 
squares (mdbpso-pls) in inland waters: a case in weishan lake. 
Eco Inform 44:21–32
	 30.	 Cao Y, Zhang H, Li W, Zhou M, Zhang Y, Chaovalitwongse 
WA (2018) Comprehensive learning particle swarm optimiza-
tion algorithm with local search for multimodal functions. IEEE 
Trans Evol Comput
	 31.	 Chen CH, Liu TK, Chou JH (2014) A novel crowding genetic 
algorithm and its applications to manufacturing robots. IEEE 
Trans Ind Inf 10(3):1705–1716
	 32.	 Chen K, Zhou F, Yin L, Wang S, Wang Y, Wan F (2018) A 
hybrid particle swarm optimizer with sine cosine acceleration 
coefficients. Inf Sci 422:218–241
	 33.	 Chen S, Jq Wang, Hy Zhang (2019) A hybrid pso-svm model 
based on clustering algorithm for short-term atmospheric pol-
lutant concentration forecasting. Technol Forecast Soc Chang 
146:41–54
	 34.	 Chen Y, Li L, Peng H, Xiao J, Wu Q (2018) Dynamic multi-
swarm differential learning particle swarm optimizer. Swarm 
Evol Comput 39:209–221
	 35.	 Chernbumroong S, Cang S, Yu H (2014) Genetic algorithm-
based classifiers fusion for multisensor activity recognition of 
elderly people. IEEE J Biomed Health Inform 19(1):282–289
	 36.	 Clerc M, Kennedy J (2002) The particle swarm-explosion, stabil-
ity, and convergence in a multidimensional complex space. IEEE 
Trans Evol Comput 6(1):58–73
	 37.	 Colorni A, Dorigo M, Maniezzo V et al (1992) Distributed 
optimization by ant colonies. In: Proceedings of the first Euro-
pean conference on artificial life, Cambridge, MA, vol 142, pp 
134–142
	 38.	 Cui H, Shu M, Song M, Wang Y (2017) Parameter selection and 
performance comparison of particle swarm optimization in sen-
sor networks localization. Sensors 17(3):487
	 39.	 Dai L, Guan Q, Liu H (2018) Robust image registration of 
printed circuit boards using improved sift-pso algorithm. J Eng 
16:1793–1797
	 40.	 Del Valle Y, Venayagamoorthy GK, Mohagheghi S, Hernandez 
JC, Harley RG (2008) Particle swarm optimization: basic con-
cepts, variants and applications in power systems. IEEE Trans 
Evol Comput 12(2):171–195
	 41.	 Deng W, Yao R, Zhao H, Yang X, Li G (2019) A novel intel-
ligent diagnosis method using optimal ls-svm with improved pso 
algorithm. Soft Comput 23(7):2445–2462
	 42.	 Dorigo M, Bonabeau E, Theraulaz G (2000) Ant algorithms and 
stigmergy. Future Gen Comput Syst 16(8):851–871
	 43.	 Durán-Rosal AM, Gutiérrez PA, Carmona-Poyato Á, Hervás-
Martínez C (2019) A hybrid dynamic exploitation barebones par-
ticle swarm optimisation algorithm for time series segmentation. 
Neurocomputing 353:45–55
	 44.	 Eberhart R, Kennedy J (1995) A new optimizer using particle 
swarm theory. In: MHS’95. Proceedings of the sixth interna-
tional symposium on micro machine and human science. IEEE, 
pp 39–43
	 45.	 Ehteram M, Binti Othman F, Mundher Yaseen Z, Abdulmoh-
sin Afan H, Falah Allawi M, Najah Ahmed A, Shahid S, Singh 
PV, El-Shafie A (2018) Improving the muskingum flood routing 
method using a hybrid of particle swarm optimization and bat 
algorithm. Water 10(6):807
	 46.	 Elsheikh A, Elaziz MA (2019) Review on applications of particle 
swarm optimization in solar energy systems. Int J Environ Sci 
Technol 16(2):1159–1170
	 47.	 Emary E, Zawbaa HM, Sharawi M (2019) Impact of Lévy 
flight on modern meta-heuristic optimizers. Appl Soft Comput 
75:775–789
	 48.	 Esmin AA, Lambert-Torres G, De Souza AZ (2005) A hybrid 
particle swarm optimization applied to loss power minimization. 
IEEE Trans Power Syst 20(2):859–866
	 49.	 Esmin AA, Coelho RA, Matwin S (2015) A review on particle 
swarm optimization algorithm and its variants to clustering high-
dimensional data. Artif Intell Rev 44(1):23–45
	 50.	 Ewees AA, Elaziz MA, Houssein EH (2018) Improved grass-
hopper optimization algorithm using opposition-based learning. 
Expert Syst Appl 112:156–172


---

<!-- Page 27 -->
## Page 27

2557
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
	 51.	 Fan JC, Li Y, Tang LY, Wu GK (2018) Roughpso: rough set-
based particle swarm optimisation. Int J Bio Inspir Comput 
12(4):245–253
	 52.	 Ferdowsi A, Farzin S, Mousavi SF, Karami H (2019) Hybrid bat 
& particle swarm algorithm for optimization of labyrinth spill-
way based on half & quarter round crest shapes. Flow Measure-
ment and Instrumentation
	 53.	 Fister I, Strnad D, Yang XS (2015) Adaptation and hybridization 
in nature-inspired algorithms. In: Adaptation and hybridization 
in computational intelligence. Springer, pp 3–50
	 54.	 Gao H, Xu W (2011) Particle swarm algorithm with hybrid muta-
tion strategy. Appl Soft Comput 11(8):5129–5142
	 55.	 García-Nieto J, López-Camacho E, García-Godoy MJ, Nebro 
AJ, Aldana-Montes JF (2019) Multi-objective ligand-protein 
docking with particle swarm optimizers. Swarm Evol Comput 
44:439–452
	 56.	 Ghaddar B, Naoum-Sawaya J (2018) High dimensional data clas-
sification and feature selection using support vector machines. 
Eur J Oper Res 265(3):993–1004
	 57.	 Ghorbani N, Kasaeian A, Toopshekan A, Bahrami L, Maghami A 
(2018) Optimizing a hybrid wind-pv-battery system using ga-pso 
and mopso for reducing cost and increasing reliability. Energy 
154:581–591
	 58.	 Gu S, Cheng R, Jin Y (2018) Feature selection for high-dimen-
sional classification using a competitive swarm optimizer. Soft 
Comput 22(3):811–822
	 59.	 Hajihassani M, Armaghani DJ, Kalatehjari R (2018) Applications 
of particle swarm optimization in geotechnical engineering: a 
comprehensive review. Geotech Geol Eng 36(2):705–722
	 60.	 Hino T, Ito S, Liu T, Maeda M (2016) Set-based particle swarm 
optimization with status memory for knapsack problem. Artif 
Life Robot 21(1):98–105
	 61.	 Hoang TT, Cho MY, Alam MN, Vu QT (2018) A novel differen-
tial particle swarm optimization for parameter selection of sup-
port vector machines for monitoring metal-oxide surge arrester 
conditions. Swarm Evol Comput 38:120–126
	 62.	 Houssein EH, Gad AG, Hussain K, Suganthan PN (2021) Major 
advances in particle swarm optimization: theory, analysis, and 
application. Swarm Evol Comput 63:100868
	 63.	 Houssein EH, Gad AG, Wazery YM (2021) Jaya algorithm and 
applications: a comprehensive review. Metaheuristics and Opti-
mization in Computer and Electrical Engineering, pp 3–24
	 64.	 Houssein EH, Gad AG, Wazery YM, Suganthan PN (2021) Task 
scheduling in cloud computing based on meta-heuristics: review, 
taxonomy, open challenges, and future trends. Swarm Evol Com-
put 62:100841
	 65.	 Hu W, Wang H, Qiu Z, Nie C, Yan L (2018) A quantum particle 
swarm optimization driven urban traffic light scheduling model. 
Neural Comput Appl 29(3):901–911
	 66.	 Huang H, Lv L, Ye S, Hao Z (2019) Particle swarm optimiza-
tion with convergence speed controller for large-scale numerical 
optimization. Soft Comput 23(12):4421–4437
	 67.	 Huang KW, Chen JL, Yang CS, Tsai CW (2015) A memetic par-
ticle swarm optimization algorithm for solving the dna fragment 
assembly problem. Neural Comput Appl 26(3):495–506
	 68.	 Huang L, Guan K, Xu T, Zhang J, Wang Q (2019) Investigation 
of the mechanical properties of steel using instrumented indenta-
tion test with simulated annealing particle swarm optimization. 
Theor Appl Fract Mech 102:116–121
	 69.	 Hussien AG, Houssein EH, Hassanien AE (2017) A binary whale 
optimization algorithm with hyperbolic tangent fitness function 
for feature selection. In: 2017 eighth international conference on 
intelligent computing and information systems (ICICIS). IEEE, 
pp 166–172
	 70.	 Ibrahim RA, Ewees AA, Oliva D, Elaziz MA, Lu S (2018) 
Improved salp swarm algorithm based on particle swarm 
optimization for feature selection. J Ambient Intelli Hum Com-
put, pp 1–15
	 71.	 Imran M, Hashim R, Khalid NEA (2013) An overview of particle 
swarm optimization variants. Procedia Eng 53:491–496
	 72.	 Ismail FH, Houssein EH, Hassanien AE (2018) Chaotic bird 
swarm optimization algorithm. In: International conference 
on advanced intelligent systems and informatics. Springer, pp 
294–303
	 73.	 Issa M, Hassanien AE, Oliva D, Helmi A, Ziedan I, Alzohairy 
A (2018) Asca-pso: adaptive sine cosine optimization algorithm 
integrated with particle swarm for pairwise local sequence align-
ment. Expert Syst Appl 99:56–70
	 74.	 Jain I, Jain VK, Jain R (2018) Correlation feature selection based 
improved-binary particle swarm optimization for gene selection 
and cancer classification. Appl Soft Comput 62:203–215
	 75.	 Jana B, Mitra S, Acharyya S (2019) Repository and mutation 
based particle swarm optimization (rmpso): a new pso variant 
applied to reconstruction of gene regulatory network. Appl Soft 
Comput 74:330–355
	 76.	 Ji B, Song X, Sciberras E, Cao W, Hu Y, Pickert V (2014) Multi-
objective design optimization of igbt power modules considering 
power cycling and thermal cycling. IEEE Trans Power Electron 
30(5):2493–2504
	 77.	 Jiang H, Kwong C, Park W, Yu K (2018) A multi-objective pso 
approach of mining association rules for affective design based 
on online customer reviews. J Eng Des 29(7):381–403
	 78.	 Jiao R, Huang X, Ouyang H, Li G, Zheng Q, Jiang Z (2019) Opti-
mal electric business centre location by centre-decentre quantum 
particle swarm optimization. Syst Sci Control Eng 7(1):222–233
	 79.	 Jin Y, Sendhoff B (2009) A systems approach to evolutionary 
multiobjective structural optimization and beyond. IEEE Comput 
Intell Mag 4(3):62–76
	 80.	 Jin Y, Olhofer M, Sendhoff B (2002) A framework for evolution-
ary optimization with approximate fitness functions. IEEE Trans 
Evol Comput 6(5):481–494
	 81.	 Jmal S, Haddar B, Chabchoub H (2019) Apply the quantum par-
ticle swarm optimization for the k-traveling repairman problem. 
Soft Computing, pp 1–14
	 82.	 Jordehi AR (2019) Binary particle swarm optimisation with 
quadratic transfer function: a new binary optimisation algorithm 
for optimal scheduling of appliances in smart homes. Appl Soft 
Comput
	 83.	 Juang CF (2004) A hybrid of genetic algorithm and particle 
swarm optimization for recurrent network design. IEEE Trans 
Syst Man Cybernet Part B (Cybern) 34(2):997–1006
	 84.	 Junior FEF, Yen GG (2019) Particle swarm optimization of deep 
neural networks architectures for image classification. Swarm 
and Evolutionary Computation
	 85.	 Kane BE (1998) A silicon-based nuclear spin quantum computer. 
Nature 393(6681):133
	 86.	 Kang Q, Xiong C, Zhou M, Meng L (2018) Opposition-based 
hybrid strategy for particle swarm optimization in noisy environ-
ments. IEEE Access 6:21888–21900
	 87.	 Karaboga D (2005) An idea based on honey bee swarm for 
numerical optimization. Technical report, Technical report-tr06, 
Erciyes university, engineering faculty, computer
	 88.	 Karakuzu C, Karakaya F, Çavuşlu MA (2016) Fpga implementa-
tion of neuro-fuzzy system with improved pso learning. Neural 
Netw 79:128–140
	 89.	 Karbassi Yazdi A, Kaviani MA, Emrouznejad A, Sahebi H 
(2019) A binary particle swarm optimization algorithm for ship 
routing and scheduling of liquefied natural gas transportation. 
Transp Lett, pp 1–10
	 90.	 Katarya R, Verma OP (2018) Efficient music recommender sys-
tem using context graph and particle swarm. Multimed Tools 
Appl 77(2):2673–2687


---

<!-- Page 28 -->
## Page 28

2558
	
A. G. Gad 
1 3
	 91.	 Kennedy J, Eberhart R (1995) Particle swarm optimization (pso). 
In: Proceedings of IEEE international conference on neural net-
works, Perth, Australia, pp 1942–1948
	 92.	 Kennedy J, Eberhart R, Shi Y (2001) Swarm intelligence. Mor-
gan Kaufmann, San Francisco
	 93.	 Kennedy J, Eberhart R (1995) Particle swarm optimization. In: 
Proceedings of IEEE international conference on neural networks 
IV, vol 1000, p 33
	 94.	 Kothari V, Anuradha J, Shah S, Mittal P (2011) A survey on 
particle swarm optimization in feature selection. In: International 
conference on computing and communication systems.. Springer, 
pp 192–201
	 95.	 Kour VP, Arora S (2019) Particle swarm optimization based sup-
port vector machine (p-svm) for the segmentation and classifica-
tion of plants. IEEE Access 7:29374–29385
	 96.	 Kulkarni RV, Venayagamoorthy GK (2011) Particle swarm 
optimization in wireless-sensor networks: a brief survey. IEEE 
Trans Syst Man Cybern Part C (Applications and Reviews) 
41(2):262–267
	 97.	 Kumar S, Pal SK, Singh R (2019) A novel hybrid model based 
on particle swarm optimisation and extreme learning machine for 
short-term temperature prediction using ambient sensors. Sustain 
Cities Soc 49:101601
	 98.	 Laskar NM, Guha K, Chatterjee I, Chanda S, Baishnab KL, Paul 
PK (2019) Hwpso:a new hybrid whale-particle swarm optimiza-
tion algorithm and its application in electronic design optimiza-
tion problems. Appl Intell 49(1):265–291
	 99.	 Le LT, Nguyen H, Zhou J, Dou J, Moayedi H et al (2019) Esti-
mating the heating load of buildings for smart city planning using 
a novel artificial intelligence technique pso-xgboost. Appl Sci 
9(13):2714
	100.	 Li H, Zhang S, Zhang C, Li P, Cropp R (2017) A novel unsuper-
vised Lévy flight particle swarm optimization (ulpso) method for 
multispectral remote-sensing image classification. Int J Remote 
Sens 38(23):6970–6992
	101.	 Li J, Zhang J, Jiang C, Zhou M (2015) Composite particle swarm 
optimizer with historical memory for function optimization. 
IEEE Trans Cybern 45(10):2350–2363
	102.	 Li L, Qin L, Qu X, Zhang J, Wang Y, Ran B (2019) Day-ahead 
traffic flow forecasting based on a deep belief network optimized 
by the multi-objective particle swarm algorithm. Knowl Based 
Syst 172:1–14
	103.	 Li W (2018) Improving particle swarm optimization based on 
neighborhood and historical memory for training multi-layer 
perceptron. Information 9(1):16
	104.	 Li Y, Bai X, Jiao L, Xue Y (2017) Partitioned-cooperative quan-
tum-behaved particle swarm optimization based on multilevel 
thresholding applied to medical image segmentation. Appl Soft 
Comput 56:345–356
	105.	 Li Z, Shi K, Dey N, Ashour AS, Wang D, Balas VE, McCauley 
P, Shi F (2017) Rule-based back propagation neural networks 
for various precision rough set presented kansei knowledge pre-
diction: a case study on shoe product form features extraction. 
Neural Comput Appl 28(3):613–630
	106.	 Lin A, Sun W, Yu H, Wu G, Tang H (2019) Global genetic learn-
ing particle swarm optimization with diversity enhancement by 
ring topology. Swarm Evol Comput 44:571–583
	107.	 Lin G, Guan J, Li Z, Feng H (2019) A hybrid binary particle 
swarm optimization with tabu search for the set-union knapsack 
problem. Expert Syst Appl
	108.	 Lin Q, Ma Y, Chen J, Zhu Q, Coello CAC, Wong KC, Chen F 
(2018) An adaptive immune-inspired multi-objective algorithm 
with multiple differential evolution strategies. Inf Sci 430:46–64
	109.	 Lin TL, Horng SJ, Kao TW, Chen YH, Run RS, Chen RJ, Lai 
JL, Kuo IH (2010) An efficient job-shop scheduling algorithm 
based on particle swarm optimization. Expert Syst Appl 
37(3):2629–2636
	110.	 Liu F, Huang H, Li X, Hao Z (2019) Automated test data gen-
eration based on particle swarm optimisation with convergence 
speed controller. CAAI Trans Intell Technol 2(2):73–79
	111.	 Liu G, Chen W, Chen H (2019) Quantum particle swarm with 
teamwork evolutionary strategy for multi-objective optimization 
on electro-optical platform. IEEE Access 7:41205–41219
	112.	 Liu Q, Wei W, Yuan H, Zhan ZH, Li Y (2016) Topology selec-
tion for particle swarm optimization. Inf Sci 363:154–173
	113.	 Lopes RF, Costa FF, Oliveira A, Lima ACdC (2018) Algorithm 
based on particle swarm applied to electrical load scheduling in 
an industrial setting. Energy 147:1007–1015
	114.	 López MG, Ponce P, Soriano LA, Molina A, Rivas JJR (2019) 
A novel fuzzy-pso controller for increasing the lifetime in 
power electronics stage for brushless dc drives. IEEE Access 
7:47841–47855
	115.	 Lorenzo PR, Nalepa J, Ramos LS, Pastor JR (2017) Hyper-
parameter selection in deep neural networks using parallel par-
ticle swarm optimization. In: Proceedings of the genetic and 
evolutionary computation conference companion. ACM, pp 
1864–1871
	116.	 Løvbjerg M, Rasmussen TK, Krink T (2001) Hybrid particle 
swarm optimiser with breeding and subpopulations. In: Proceed-
ings of the 3rd annual conference on genetic and evolutionary 
computation. Morgan Kaufmann Publishers Inc., pp 469–476
	117.	 Luo W, Sun J, Bu C, Liang H (2016) Species-based particle 
swarm optimizer enhanced by memory for dynamic optimiza-
tion. Appl Soft Comput 47:130–140
	118.	 Ma K, Hu S, Yang J, Xu X, Guan X (2018) Appliances schedul-
ing via cooperative multi-swarm pso under day-ahead prices and 
photovoltaic generation. Appl Soft Comput 62:504–513
	119.	 Mahdavi S, Rahnamayan S, Deb K (2018) Opposition based 
learning: a literature review. Swarm Evol Comput 39:1–23
	120.	 Maiyar LM, Thakkar JJ (2019) Environmentally conscious 
logistics planning for food grain industry considering wastages 
employing multi objective hybrid particle swarm optimization. 
Transp Res Part E Log Transp Rev 127:220–248
	121.	 Manikandan R, Saravanan V (2019) A novel approach on par-
ticle agent swarm optimization (paso) in semantic mining for 
web page recommender system of multimedia data: a health care 
perspective. Multimedia Tools and Applications, pp 1–23
	122.	 Mansouri N, Zade BMH, Javidi MM (2019) Hybrid task sched-
uling strategy for cloud computing by modified particle swarm 
optimization and fuzzy theory. Comput Ind Eng 130:597–633
	123.	 Marini F, Walczak B (2015) Particle swarm optimization (pso). 
A tutorial. Chemom Intell Lab Syst 149:153–165
	124.	 Mavrovouniotis M, Li C, Yang S (2017) A survey of swarm intel-
ligence for dynamic optimization: algorithms and applications. 
Swarm Evol Comput 33:1–17
	125.	 Mehmood Y, Sadiq M, Shahzad W, Amin F (2018) Fitness-based 
acceleration coefficients to enhance the convergence speed of 
novel binary particle swarm optimization. In: 2018 international 
conference on frontiers of information technology (FIT). IEEE, 
pp 355–360
	126.	 Melton RG (2018) Differential evolution/particle swarm 
optimizer for constrained slew maneuvers. Acta Astronaut 
148:246–259
	127.	 Millonas MM, et al (1993) Swarms, phase transitions, and collec-
tive intelligence (paper 1); and a nonequilibrium statistical field 
theory of swarms and other spatially extended complex systems 
(paper 2). Technical rep
	128.	 Miranda V, Fonseca N (2002) Epso-evolutionary particle swarm 
optimization, a new algorithm with applications in power sys-
tems. In IEEE/PES transmission and distribution conference and 
exhibition, vol 2. IEEE, pp 745–750


---

<!-- Page 29 -->
## Page 29

2559
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
	129.	 Mirjalili S, Lewis A (2016) The whale optimization algorithm. 
Adv Eng Softw 95:51–67
	130.	 Mirjalili S, Gandomi AH, Mirjalili SZ, Saremi S, Faris H, Mir-
jalili SM (2017) Salp swarm algorithm: a bio-inspired optimizer 
for engineering design problems. Adv Eng Softw 114:163–191
	131.	 Moayedi H, Mehrabi M, Mosallanezhad M, Rashid ASA, Prad-
han B (2018) Modification of landslide susceptibility mapping 
using optimized pso-ann technique. Engineering with Comput-
ers, pp 1–18
	132.	 Mohebbi A, Achiche S, Baron L (2019) Integrated and concur-
rent detailed design of a mechatronic quadrotor system using a 
fuzzy-based particle swarm optimization. Eng Appl Artif Intell 
82:192–206
	133.	 Mokhtari H, Noroozi A (2018) An efficient chaotic based pso for 
earliness/tardiness optimization in a batch processing flow shop 
scheduling problem. J Intell Manuf 29(5):1063–1081
	134.	 Nagra AA, Han F, Ling QH (2018) An improved hybrid self-
inertia weight adaptive particle swarm optimization algorithm 
with local search. Engineering Optimization, pp 1–18
	135.	 Nenavath H, Jatoth RK, Das S (2018) A synergy of the sine-
cosine algorithm and particle swarm optimizer for improved 
global optimization and object tracking. Swarm Evol Comput 
43:1–30
	136.	 Ng MC, Fong S, Siu SW (2015) Psovina: the hybrid particle 
swarm optimization algorithm for protein-ligand docking. J Bio-
inform Comput Biol 13(03):1541007
	137.	 Nguyen S, Zhang M, Johnston M, Tan KC (2014) Automatic 
programming via iterated local search for dynamic job shop 
scheduling. IEEE Trans Cybern 45(1):1–14
	138.	 Nobile MS, Cazzaniga P, Besozzi D, Colombo R, Mauri G, Pasi 
G (2018) Fuzzy self-tuning pso: a settings-free algorithm for 
global optimization. Swarm Evol Comput 39:70–85
	139.	 Nouiri M, Bekrar A, Jemai A, Niar S, Ammari AC (2018) An 
effective and distributed particle swarm optimization algo-
rithm for flexible job-shop scheduling problem. J Intell Manuf 
29(3):603–615
	140.	 Pashaei E, Pashaei E, Aydin N (2019) Gene selection using 
hybrid binary black hole algorithm and modified binary particle 
swarm optimization. Genomics 111(4):669–686
	141.	 Passino KM (2002) Biomimicry of bacterial foraging for dis-
tributed optimization and control. IEEE Control Syst Mag 
22(3):52–67
	142.	 Pawlak Z (1982) International of computer and information sci-
ence. Rough Set 11:341–356
	143.	 Poli R, Kennedy J, Blackwell T (2007) Particle swarm optimiza-
tion. Swarm Intell 1(1):33–57
	144.	 Pradeepkumar D, Ravi V (2017) Forecasting financial time series 
volatility using particle swarm optimization trained quantile 
regression neural network. Appl Soft Comput 58:35–52
	145.	 Qi C, Fourie A, Chen Q (2018) Neural network and particle 
swarm optimization for predicting the unconfined compres-
sive strength of cemented paste backfill. Constr Build Mater 
159:473–478
	146.	 Qi X, Ju G, Xu S (2018) Efficient solution to the stagnation 
problem of the particle swarm optimization algorithm for phase 
diversity. Appl Opt 57(11):2747–2757
	147.	 Qian Q, Wu J, Wang Z (2019) Optimal path planning for two-
wheeled self-balancing vehicle pendulum robot based on quan-
tum-behaved particle swarm optimization algorithm. Personal 
and Ubiquitous Computing, pp 1–11
	148.	 Qu B, Zhu Y, Jiao Y, Wu M, Suganthan PN, Liang J (2018) A 
survey on multi-objective evolutionary algorithms for the solu-
tion of the environmental/economic dispatch problems. Swarm 
Evol Comput 38:1–11
	149.	 Rahgoshay M, Feiznia S, Arian M, Hashemi SAA (2019) Simula-
tion of daily suspended sediment load using an improved model 
of support vector machine and genetic algorithms and particle 
swarm. Arab J Geosci 12(9):277
	150.	 Rahman NHA, Zobaa AF (2017) Integrated mutation strategy 
with modified binary pso algorithm for optimal pmus placement. 
IEEE Trans Ind Inf 13(6):3124–3133
	151.	 Raj S, Ray KC (2017) Ecg signal analysis using dct-based 
dost and pso optimized svm. IEEE Trans Instrum Meas 
66(3):470–478
	152.	 Ramya ST, Arunagiri B, Rangarajan P (2017) Novel effective 
x-path particle swarm optimization based deprived video data 
retrieval for smart city. Cluster Computing, pp 1–10
	153.	 Rao R (2016) Jaya: a simple and new optimization algorithm for 
solving constrained and unconstrained optimization problems. 
Int J Ind Eng Comput 7(1):19–34
	154.	 Rashid M, Baig AR (2010) Psogp: a genetic programming based 
adaptable evolutionary hybrid particle swarm optimization. Int J 
Innov Comput Inf Control 6(1):287–296
	155.	 Rojas-García ÁA, Hernández-Aguirre A, Valdez SI (2019) On 
the selection of the optimal topology for particle swarm optimi-
zation: a study of the tree as the universal topology. In: Proceed-
ings of the genetic and evolutionary computation conference. 
ACM, pp 55–62
	156.	 Rouff CA, Hinchey MG, Truszkowski WF, Rash JL (2006) 
Experiences applying formal approaches in the development of 
swarm-based space exploration systems. Int J Softw Tools Tech-
nol Transf 8(6):587–603
	157.	 Salajegheh F, Salajegheh E (2019) Psog: enhanced particle 
swarm optimization by a unit vector of first and second order 
gradient directions. Swarm Evol Comput 46:28–51
	158.	 Sameer F, Bakar MA, Zaidan A, Zaidan B (2019) A new algo-
rithm of modified binary particle swarm optimization based on 
the Gustafson-Kessel for credit risk assessment. Neural Comput 
Appl 31(2):337–346
	159.	 Sanchez IAL, Vargas JM, Santos CA, Mendoza MG, Mocte-
zuma CJM (2018) Solving binary cutting stock with matheuris-
tics using particle swarm optimization and simulated annealing. 
Soft Comput 22(18):6111–6119
	160.	 Saremi S, Mirjalili S, Lewis A, Liew AWC, Dong JS (2018) 
Enhanced multi-objective particle swarm optimisation for esti-
mating hand postures. Knowl Based Syst 158:175–195
	161.	 Sato M, Fukuyama Y, Iizaka T, Matsui T (2018) Total optimi-
zation of energy networks in a smart city by multi-swarm dif-
ferential evolutionary particle swarm optimization. IEEE Trans 
Sustain Energy
	162.	 Serani A, Leotardi C, Iemma U, Campana EF, Fasano G, Diez 
M (2016) Parameter selection in synchronous and asynchronous 
deterministic particle swarm optimization for ship hydrodynam-
ics problems. Appl Soft Comput 49:313–334
	163.	 Shahzad F, Masood S, Khan NK (2014) Probabilistic opposi-
tion-based particle swarm optimization with velocity clamping. 
Knowl Inf Syst 39(3):703–737
	164.	 Sheikholeslami F, Navimipour NJ (2017) Service allocation in 
the cloud environments using multi-objective particle swarm 
optimization algorithm based on crowding distance. Swarm Evol 
Comput 35:53–64
	165.	 Shen J, Han L (2019) Design process optimization and profit 
calculation module development simulation analysis of financial 
accounting information system based on particle swarm optimi-
zation (pso). Information Systems and e-Business Management, 
pp 1–14
	166.	 Sivaranjani R, Roomi SMM, Senthilarasi M (2019) Speckle noise 
removal in sar images using multi-objective pso (mopso) algo-
rithm. Appl Soft Comput 76:671–681
	167.	 Song M, Chen K, Wang J (2018) Three-dimensional wind turbine 
positioning using gaussian particle swarm optimization with dif-
ferential evolution. J Wind Eng Ind Aerodyn 172:317–324


---

<!-- Page 30 -->
## Page 30

2560
	
A. G. Gad 
1 3
	168.	 Srisukkham W, Zhang L, Neoh SC, Todryk S, Lim CP (2017) 
Intelligent leukaemia diagnosis with bare-bones pso based fea-
ture optimization. Appl Soft Comput 56:405–419
	169.	 Stork J, Friese M, Zaefferer M, Bartz-Beielstein T, Fischbach 
A, Breiderhoff B, Naujoks B, Tušar T (2020) Open issues in 
surrogate-assisted optimization. In: High-performance simula-
tion-based optimization. Springer, pp 225–244
	170.	 Sun J, Feng B, Xu W (2004) Particle swarm optimization with 
particles having quantum behavior. In: Proceedings of the 
2004 congress on evolutionary computation (IEEE Cat. No. 
04TH8753), vol 1. IEEE, pp 325–331
	171.	 Sun L, Song X, Chen T (2019) An improved convergence particle 
swarm optimization algorithm with random sampling of control 
parameters. J Control Sci Eng 2019
	172.	 Sun Z, Liu Y, Tao L (2018) Attack localization task allocation in 
wireless sensor networks based on multi-objective binary particle 
swarm optimization. J Netw Comput Appl 112:29–40
	173.	 Suresh S, Lal S (2017) Multilevel thresholding based on chaotic 
Darwinian particle swarm optimization for segmentation of satel-
lite images. Appl Soft Comput 55:503–522
	174.	 Tang B, Han J, Guo G, Chen Y, Zhang S (2019) Building mate-
rial prices forecasting based on least square support vector 
machine and improved particle swarm optimization. Archit Eng 
Des Manag 15(3):196–212
	175.	 Tang W, Cha H, Wei M, Tian B (2019) Estimation of surface-
based duct parameters from automatic identification system using 
the Lévy flight quantum-behaved particle swarm optimization 
algorithm. J Electromagn Waves Appl, 1–11
	176.	 Thabit S, Mohades A (2018) Multi-robot path planning based 
on multi-objective particle swarm optimization. IEEE Access 
7:2138–2147
	177.	 Thangaraj R, Pant M, Abraham A, Bouvry P (2011) Particle 
swarm optimization: hybridization perspectives and experimental 
illustrations. Appl Math Comput 217(12):5208–5226
	178.	 Thangaraj R, Pant M, Abraham A, Snasel V (2012) Modified 
particle swarm optimization with time varying velocity vector. 
Int J Innov Comput Inf Control 8(1):201–218
	179.	 Tharwat A, Hassanien AE (2019) Quantum-behaved particle 
swarm optimization for parameter optimization of support vec-
tor machine. J Classif, pp 1–23
	180.	 Ting T, Yang XS, Cheng S, Huang K (2015) Hybrid metaheuris-
tic algorithms: past, present, and future. In: Recent advances in 
swarm intelligence and evolutionary computation. Springer, pp 
71–83
	181.	 Tizhoosh HR (2005) Opposition-based learning: a new scheme 
for machine intelligence. In: International conference on compu-
tational intelligence for modelling, control and automation and 
international conference on intelligent agents, web technologies 
and internet commerce (CIMCA-IAWTIC’06), vol 1. IEEE, pp 
695–701
	182.	 Tran B, Zhang M, Xue B (2016) A pso based hybrid feature 
selection algorithm for high-dimensional classification. In: 2016 
IEEE congress on evolutionary computation (CEC). IEEE, pp 
3801–3808
	183.	 Vafashoar R, Meybodi MR (2019) Cellular learning automata 
based bare bones pso with maximum likelihood rotated muta-
tions. Swarm Evol Comput 44:680–694
	184.	 Valsecchi A, Bermejo E, Damas S, Cordón O (2018) Metaheuris-
tics for medical image registration. Handbook of Heuristics, pp 
1079–1101
	185.	 Vandersypen LM, Steffen M, Breyta G, Yannoni CS, Sherwood 
MH, Chuang IL (2001) Experimental realization of Shor’s 
quantum factoring algorithm using nuclear magnetic resonance. 
Nature 414(6866):883
	186.	 Vijay M, Jena D (2017) Pso based neuro fuzzy sliding mode 
control for a robot manipulator. J Electr Syst Inf Technol 
4(1):243–256
	187.	 Villarrubia G, De Paz JF, Chamoso P, De la Prieta F (2018) 
Artificial neural networks used in optimization problems. Neu-
rocomputing 272:10–16
	188.	 Wang C, Yu T, Curiel-Sosa JL, Xie N, Bui TQ (2019) Adaptive 
chaotic particle swarm algorithm for isogeometric multi-objec-
tive size optimization of fg plates. Structural and Multidiscipli-
nary Optimization, pp 1–22
	189.	 Wang D, Qiu H, Wu CC, Lin WC, Lai K, Cheng SR (2018) 
Dominance rule and opposition-based particle swarm optimi-
zation for two-stage assembly scheduling with time cumulated 
learning effect. Soft Computing, pp 1–12
	190.	 Wang D, Tan D, Liu L (2018) Particle swarm optimization algo-
rithm: an overview. Soft Comput 22(2):387–408
	191.	 Wang GG, Deb S, Coelho LdS (2015) Elephant herding optimi-
zation. In: 2015 3rd international symposium on computational 
and business intelligence (ISCBI). IEEE, pp 1–5
	192.	 Wang H, Peng Mj, Hines JW, Zheng Gy, Liu Yk, Upadhyaya BR 
(2019) A hybrid fault diagnosis methodology with support vector 
machine and improved particle swarm optimization for nuclear 
power plants. ISA Trans
	193.	 Wang JJ, Liu GY (2019) Saturated control design of a quadro-
tor with heterogeneous comprehensive learning particle swarm 
optimization. Swarm Evol Comput 46:84–96
	194.	 Wang S, Li Y, Yang H (2019) Self-adaptive mutation differential 
evolution algorithm based on particle swarm optimization. Appl 
Soft Comput 81:105496
	195.	 Wu TY, Lin CH (2014) Low-sar path discovery by particle 
swarm optimization algorithm in wireless body area networks. 
IEEE Sens J 15(2):928–936
	196.	 Wu Y, Miao Q, Ma W, Gong M, Wang S (2017) Psosac: parti-
cle swarm optimization sample consensus algorithm for remote 
sensing image registration. IEEE Geosci Remote Sens Lett 
15(2):242–246
	197.	 Xu G, Wu ZH, Jiang MZ (2015) Premature convergence of stand-
ard particle swarm optimisation algorithm based on Markov 
chain analysis. Int J Wirel Mobile Comput 9(4):377–382
	198.	 Xu G, Cui Q, Shi X, Ge H, Zhan ZH, Lee HP, Liang Y, Tai R, 
Wu C (2019) Particle swarm optimization based on dimensional 
learning strategy. Swarm Evol Comput 45:33–51
	199.	 Xu L, Muhammad A, Pu Y, Zhou J, Zhang Y (2019) Frac-
tional-order quantum particle swarm optimization. PLoS ONE 
14(6):e0218285
	200.	 Xu X, Rong H, Trovati M, Liptrott M, Bessis N (2018) Cs-pso: 
chaotic particle swarm optimization algorithm for solving com-
binatorial optimization problems. Soft Comput 22(3):783–795
	201.	 Yang XS (2009) Firefly algorithms for multimodal optimization. 
In: International symposium on stochastic algorithms. Springer, 
pp 169–178
	202.	 Yang XS, Cui Z, Xiao R, Gandomi AH, Karamanoglu M (2013) 
Swarm intelligence and bio-inspired computation: theory and 
applications. Newnes, London
	203.	 Yang Z, Qiu H, Gao L, Cai X, Jiang C, Chen L (2019) A surro-
gate-assisted particle swarm optimization algorithm based on 
efficient global optimization for expensive black-box problems. 
Eng Optim 51(4):549–566
	204.	 Yazdani M, Jolai F (2016) Lion optimization algorithm (loa): 
a nature-inspired metaheuristic algorithm. J Comput Des Eng 
3(1):24–36
	205.	 Yi T, Zheng H, Tian Y, Liu Jp (2018) Intelligent prediction of 
transmission line project cost based on least squares support vec-
tor machine optimized by particle swarm optimization. Math-
ematical Problems in Engineering 2018


---

<!-- Page 31 -->
## Page 31

2561
Particle Swarm Optimization Algorithm and Its Applications: A Systematic Review﻿	
1 3
	206.	 Yoon Y, Kim YH (2013) An efficient genetic algorithm for maxi-
mum coverage deployment in wireless sensor networks. IEEE 
Trans Cybern 43(5):1473–1483
	207.	 Yu H, Tan Y, Zeng J, Sun C, Jin Y (2018) Surrogate-assisted 
hierarchical particle swarm optimization. Inf Sci 454:59–72
	208.	 Yuan Q, Yin G (2014) Analyzing convergence and rates of 
convergence of particle swarm optimization algorithms using 
stochastic approximation methods. IEEE Trans Autom Control 
60(7):1760–1773
	209.	 Yue Y, Cao L, Hu J, Cai S, Hang B, Wu H (2019) A novel hybrid 
location algorithm based on chaotic particle swarm optimization 
for mobile position estimation. IEEE Access 7:58541–58552
	210.	 Zarei A, Mousavi SF, Gordji ME, Karami H (2019) Optimal 
reservoir operation using bat and particle swarm algorithm and 
game theory based on optimal water allocation among consum-
ers. Water Resources Management, pp 1–23
	211.	 Zarrouk R, Bennour IE, Jemai A (2019) A two-level particle 
swarm optimization algorithm for the flexible job shop schedul-
ing problem. Swarm Intelligence, pp 1–24
	212.	 Zeng N, Qiu H, Wang Z, Liu W, Zhang H, Li Y (2018) A new 
switching-delayed-pso-based optimized svm algorithm for diag-
nosis of Alzheimer’s disease. Neurocomputing 320:195–202
	213.	 Zhang H, Xie J, Hu Q, Shao L, Chen T (2018) A hybrid dpso 
with Lévy flight for scheduling mimo radar tasks. Appl Soft 
Comput 71:242–254
	214.	 Zhang X, Zheng X, Cheng R, Qiu J, Jin Y (2018) A competitive 
mechanism based multi-objective particle swarm optimizer with 
fast convergence. Inf Sci 427:63–76
	215.	 Zhang Y, Balochian S, Agarwal P, Bhatnagar V, Housheya OJ 
(2014) Artificial intelligence and its applications. Mathematical 
Problems in Engineering 2014
	216.	 Zhang Y, Wang S, Ji G (2015) A comprehensive survey on par-
ticle swarm optimization algorithm and its applications. Math-
ematical Problems in Engineering 2015
	217.	 Zhang Y, Zhang Q, Farnoosh A, Chen S, Li Y (2019) Gis-based 
multi-objective particle swarm optimization of charging stations 
for electric vehicles. Energy 169:844–853
	218.	 Zhang YD, Wang S, Dong Z (2014) Classification of Alzheimer 
disease based on structural magnetic resonance imaging by ker-
nel support vector machine decision tree. Prog Electromagn Res 
144:171–184
	219.	 Zheng J, Lu C, Gao L (2019) Multi-objective cellular particle 
swarm optimization for wellbore trajectory design. Appl Soft 
Comput 77:106–117
	220.	 Zhong Y, Lin J, Wang L, Zhang H (2018) Discrete comprehen-
sive learning particle swarm optimization algorithm with metrop-
olis acceptance criterion for traveling salesman problem. Swarm 
Evol Comput 42:77–88
	221.	 Zhou A, Qu BY, Li H, Zhao SZ, Suganthan PN, Zhang Q (2011) 
Multiobjective evolutionary algorithms: a survey of the state of 
the art. Swarm Evol Comput 1(1):32–49
	222.	 Zhou Z, Ong YS, Lim MH, Lee BS (2007) Memetic algorithm 
using multi-surrogates for computationally expensive optimiza-
tion problems. Soft Comput 11(10):957–971
	223.	 Zhu M, Li J, Chang D, Zhang G, Chen J (2018) Optimization 
of antenna array deployment for partial discharge localization in 
substations by hybrid particle swarm optimization and genetic 
algorithm method. Energies 1(11):1813
Publisher's Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.


---
