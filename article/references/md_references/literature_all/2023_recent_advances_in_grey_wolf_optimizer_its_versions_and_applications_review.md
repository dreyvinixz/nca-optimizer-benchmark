# 2023_recent_advances_in_grey_wolf_optimizer_its_versions_and_applications_review

**Source File**: `article\references\literature\2023_recent_advances_in_grey_wolf_optimizer_its_versions_and_applications_review.pdf`
**Total Pages**: 38

---

<!-- Page 1 -->
## Page 1

Date of publication xxxx 00, 0000, date of current version xxxx 00, 0000.
Digital Object Identifier 10.1109/ACCESS.2017.DOI
Recent advances in Grey Wolf Optimizer,
its versions and applications: Review
SHARIF NASER MAKHADMEH1, MOHAMMED AZMI AL-BETAR 1,2, IYAD ABU DOUSH3,4,
MOHAMMED A. AWADALLAH5,6, SOFIAN KASSAYMEH6, SEYEDALI MIRJALILI7,8, and
RAED ABU ZITAR9
1Artificial Intelligence Research Center (AIRC), College of Engineering and Information Technology, Ajman University, Ajman, United Arab Emirates
2Department of Information Technology, Al-Huson University College, Al-Balqa Applied University, P.O. Box 50, Al-Huson, Irbid, Jordan
3Computing Department, College of Engineering and Applied Sciences, American University of Kuwait, Salmiya, Kuwait.
4Computer Science Department, Yarmouk University, Irbid, Jordan.
5Department of Computer Science, Al-Aqsa University, P.O. Box 4051, Gaza, Palestine
6Artificial Intelligence Research Center (AIRC), Ajman University, Ajman, United Arab Emirates
7Centre for Artificial Intelligence Research and Optimisation, Torrens University Australia, Fortitude Valley, Brisbane, 4006 QLD, Australia.
8Yonsei Frontier Lab, Yonsei University, Seoul, Republic of Korea.
9Sorbonne Center of Artificial Intelligence, Sorbonne University-Abu Dhabi, Abu Dhabi, UAE.
Corresponding author: First A. Author (e-mail: m.albetar@ajman.ac.ae )
ABSTRACT
The Grey Wolf Optimizer (GWO) has emerged as one of the most captivating swarm intelligence methods,
drawing inspiration from the hunting behavior of wolf packs. GWO’s appeal lies in its remarkable
characteristics: it is parameter-free, derivative-free, conceptually simple, user-friendly, adaptable, flexible,
and robust. Its efficacy has been demonstrated across a wide range of optimization problems in diverse
domains, including engineering, bioinformatics, biomedical, scheduling and planning, and business. Given
the substantial growth and effectiveness of GWO, it is essential to conduct a recent review to provide
updated insights. This review delves into the GWO-related research conducted between 2019 and 2022,
encompassing over 200 research articles. It explores the growth of GWO in terms of publications, citations,
and the domains that leverage its potential. The review thoroughly examines the latest versions of GWO,
categorizing them based on their contributions. Additionally, it highlights the primary applications of GWO,
with computer science and engineering emerging as the dominant research domains. A critical analysis
of the accomplishments and limitations of GWO is presented, offering valuable insights. Finally, the
review concludes with a brief summary and outlines potential future developments in GWO theory and
applications. Researchers seeking to employ GWO as a problem-solving tool will find this comprehensive
review immensely beneficial in advancing their research endeavors.
INDEX TERMS Grey wolf Optimizer, Swarm Intelligence, Optimization, Evolutionary Computation
I. INTRODUCTION
Metaheuristics are strategic-based techniques capable of
intelligently exploring the search space of optimization
problems to discover near-optimal solutions [1]. These
metaheuristic-based algorithms can be categorized into two
main types: local search-based algorithms and population-
based algorithms [2], [3]. Furthermore, they can be further
classified into evolutionary-based algorithms, physical-based
algorithms, chemical-based algorithms, human-based algo-
rithms, and Swarm intelligence algorithms [4], [5].
Local search-based algorithms initiate with an initial so-
lution and iteratively improve it by exploring neighbour-
ing solutions. This iterative process persists until either the
maximum number of iterations is reached or the algorithm
converges to a local optimum. simulated annealing [6], tabu
search [7], greedy randomized adaptive search procedure
(GRASP) [8], variable neighborhood search [9], iterated
local search [10], β-hill climbing [11], and vortex search
algorithm [12] are a few examples of local search-based
algorithms [13].
Evolutionary-based algorithms represent a traditional form
of population-based algorithms, where a population of solu-
tions is initially generated. Through iterative steps involving
recombination, mutation, and natural selection, these solu-
tions are progressively improved. These algorithms like ge-
netic algorithm [14], evolutionary programming [15], genetic
VOLUME 4, 2016
1
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 2 -->
## Page 2

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
programming [16], differential evolution [17], biogeography-
based optimization [18], and probability-based incremental
learning (PBIL) [19].
Physical-based and chemical-based algorithms draw in-
spiration from the principles governing physical laws and
chemical interactions among components. These algorithms
like plasma generation optimization [20], ray optimization
[21], solar system algorithm [22], equilibrium optimizer
[23], gravitational search algorithm [24], billiards-inspired
optimization [25], henry gas solubility optimization [26],
simulated annealing [6], vortex search algorithm [12], and
chemical reaction optimization [27].
Social or human-based algorithms predominantly derive
inspiration from social or human behavior. These algo-
rithms like harmony search [28], brain storm optimization
[29], heap-based optimizer [30], teaching-learning-based op-
timization [31], political optimizer [32], ali baba and the
forty thieves [33], group teaching optimization algorithm
[34], ebola optimization search algorithm [35], football game
inspired algorithm [36], coronavirus herd immunity opti-
mizer [37], arithmetic Optimization Algorithm [38], stock
exchange trading optimization [39], and poor and rich op-
timization algorithm [40].
Swarm intelligence (SI) algorithms often find their in-
spiration in the collective behavior observed in various an-
imal species, including birds, frogs, bats, rats, bees, ants,
and others.[4]. The SI’s algorithms normally emulate the
prey hunting process, searching for food based on the lo-
cal interactions between the swarm members or based on
their environment (stigmergy) [41]. Therefore, swarm groups
are self-organized. It is normally initiated with a swarm
of candidate solutions. Usually, the swarm can be divided
into two main groups: the leaders and followers, where the
interactions occur by attracting the follower to the leaders;
thus, converging to the optimal solution.
The most popular SI algorithms are ant colony optimiza-
tion [42], particle swarm optimization [43], krill herd op-
timization [44], cuckoo search [45], firefly algorithm [46],
white shark optimizer [47], artificial bee colony [48], chicken
swarm optimization [49], snake optimizer [50], ant lion
optimizer [51], elephant herding optimisation [52], sparrow
search algorithm [53], horse herd optimization [54], dragon-
fly algorithm [55], rat swarm optimizer [56], moth-flame op-
timization [57], whale optimization algorithm [58], komodo
mlipir algorithm [59], Salp Swarm Optimizer [60], chimp
optimization algorithm [61], coronavirus herd immunity op-
timizer [37], dwarf mongoose optimization algorithm [62],
lemurs optimizer [63], grey wolf optimizer (GWO) [64], and
many others.
The GWO is the fastest-grown SI algorithm introduced
by Mirjalili et al. [64] to imitate the hunting behaviour of
the grey packs in nature. The GWO is a powerful optimizer
due to its impressive features over others, such as it can be
easily adapted, parameter-free, derivative-free, memory-less,
computational-less, flexible, and sound-and-complete. In the
initial searching stage, the GWO starts with high intensity
on the exploration stage, while in the last course of runs,
the GWO provides more attention to the exploitation phase
through the gradual changes in the positions of the three-
best leaders. Therefore, GWO is able to tackle a plethora of
optimization problems from a wide range of research fields,
such as engineering, networking and communication, image
processing, robotics, mathematics, bioinformatics, biomedi-
cal, and others [65].
To tackle the complex search space characteristics of real-
world and combinatorial optimization problems, particularly
those with non-convex, nonlinear, and highly constrained
features, significant adjustments have been made to the
fundamental structure of the Grey Wolf Optimizer (GWO).
These modifications have enabled it to handle multi-objective
problems and highly constrained scenarios effectively. More-
over, GWO has been enriched by incorporating elements
from other optimization algorithms to enhance its perfor-
mance. Additionally, hybridization with other optimization
algorithms has been employed to strike a balance between
exploration and exploitation capabilities, thereby improving
the quality of solutions generated by GWO. Indeed, many
instances of GWO are proposed in the literature, each of
which is suitable for specific research applications [66], [67],
[68], [65].
The Grey Wolf Optimizer (GWO) starts by initializing
a random swarm of grey wolves. These wolves are then
organized into four groups: Alpha, Beta, Delta, and Omega.
Each group is sequentially ranked based on its role in the
hunting process, with Alpha being the best solution, followed
by Beta and Delta in the swarm. The Omega group consists
of follower wolves that are attracted by the three best wolves.
During the collaborative loop, the GWO assesses the distance
between the Omega group and the third-best wolves (Alpha,
Beta, Delta). It then updates the positions of these wolves
using intelligent mechanisms, such as chasing, encircling,
and attacking prey. Two predefined parameters are utilized
to strike a balance between exploration and exploitation,
ensuring an effective optimization process. [64].
The GWO has been spread across many research topics.
In our previous review article [69], the growth of GWO
rapidly increased from 2014 to 2018 period of time. Many
GWO applications and variants have been reviewed and
summarized. However, from 2019 to 2021, the growing slop
is exponentially increased, where GWO is adopted as the
main optimizer to tackle other optimization applications.
Interestingly, during this short period, more than 700 articles
with the GWO in the title have been published in high-quality
journals held by high-prestigious publishers as recorded in
the Scopus index dataset, as presented in Section III. The
main contributions of this review are summarized as follows:
• Conduct a comprehensive investigation of the GWO
studies in a specific period to draw a map for the
scientists and researchers planning to work in the related
domains by guiding them to apply the GWO to different
problems.
2
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 3 -->
## Page 3

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
• Conduct an encyclopedic study of all GWO aspects
and prove its robustness and effectiveness in addressing
various kinds of single and multi-objective optimization
problems.
• Conduct a new theoretical analysis to highlight the main
and most prominent drawbacks of the GWO and suggest
several solutions to address such drawbacks.
•
In order to review the GWO growth in the last three
years (i.e., 2019-2021), this review can be considered as
an extension to the previous GWO paper, which covers the
following GWO advances:
• The basics theory of GWO is discussed to show its
leading operators and functions, as shown in Section II.
• The growth of GWO is reviewed in terms of the total
number of articles, citations, topics, authors, institu-
tions, and countries. This growth review is conducted to
prove the viability and efficiency of the GWO and why
it is heavily used (See Section III).
• The recent variations of GWO that were proposed over
the last three years are also summarized in Section IV.
• The applications tackled by GWO over the last three
years are illustrated and tabulated, as shown in the
section V.
• A critical analysis is presented to reveal the main pros
and cons of GWO, thus suggesting research directions
to fill these gaps, as shown in Section VII.
• Finally, the main GWO theoretical foundations and pos-
sible future directions of GWO concluded this review.
II. BASIC CONCEPTS OF GREY WOLF OPTIMIZER
GWO is a nature-inspired optimization method introduced
in 2014 [64]. It is considered one of the essential SI al-
gorithms that estimate the global optimum for optimization
problems. Just like other SI algorithms, the GWO considers
the optimization problems as a black box without the needing
for gradient information to perform optimization.
GWO’s primary inspirations are twofold: social hierarchy
and hunting technique in a wolf pack. In the former case,
a wolf pack’s leadership is divided into three hierarchical
categories: Alpha, Beta, and Delta. The remainder of the
members in a pack are considered to be Omega, as shown in
Fig. 1. Different decision-making around hunting, migration,
mating, etc., in a pack are made through this social leader-
ship. In the latter case, the critical mechanism of search in
GWO mimics the hunting process of grey wolves in nature.
The mathematical models for these processes are presented
and discussed below.
Grey wolves tend to encircle prey to exhaust and slow
them down. In nature, it happens on a landscape, so this can
be modeled on a 2D plane. The encircle mechanism can be
formulated as follows:
τ =| µ · X(z) −Y (z) |
(1)
FIGURE 1: GWO hierarchical categories
where X(z) shows the position of prey in z-th unit of time
(e.g. iteration), Y (z) indicates the position of a wolf in z-th
unit of time, and µ = 2 · rand1 where rand1 is a random
number between 0 to 1.
In the above equations, the vector can be of any dimension.
This allows space definition around artificial wolves and
preys in any n-dimensional search space.
Encircling prey is done via chasing prey by grey wolves.
This is mathematically modeled using the following equa-
tions in GWO:
Y (z + 1) = X(z) −ν · τ
(2)
ν = 2κ · rand2 −κ
(3)
where κ is a variable that is usually changed from 2 to 0,
and rand2 is a random number between 0 to 1.
The decision-making using alpha, beta, and delta is mod-
eled using the following equations:
τα =| µ1·Yα−Y |,
τβ =| µ2·Yβ−Y |,
τδ =| µ3·Yδ−Y |
(4)
Y1 = Yα −ν1 ·τα,
Y2 = Yβ −ν2 ·τβ,
Y3 = Yδ −ν3 ·τδ
(5)
Y (z + 1) = Y1 + Y2 + Y3
3
(6)
where Yα(z) shows the position of the alpha wolf (first
best solution) in z-th unit of time, Yβ(z) is the position of
the beta (second best solution) in z-th unit of time, and Yδ(z)
indicates the position of delta wolf (third best solution) in z-
th unit of time.
Eqs. 4 and 5 create three position vectors for alpha, beta,
and delta wolves considering the position of an omega wolf
(Yω(z)). These three vectors will be then used in Eq. 6 to
update the position using averaging.
The GWO pseudo-code is given in Algorithm 1.
VOLUME 4, 2016
3
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 4 -->
## Page 4

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
Algorithm 1 The GWO pseudo-code
1: Create a random population of artificial wolves Yi(i =
1, 2, . . . , n)
2: Assign initial values to the main controlling parameters:
κ, ν, and µ
3: while (end condition is not met) do
Evaluate and rank wolves by calculating their objec-
tive values Choose (or update if needed) Yα(z), Yβ(z),
and Yδ(z)
4:
for each wolf (Yi) do
5:
Update the main controlling parameters: κ, ν, and
µ
6:
Update the position of the current search agent by
Eq. (6)
7:
end for
8: end while
9: return Yα
III. THE GROWTH OF GREY WOLF OPTIMIZER IN THE
LITERATURE
The GWO has gained substantial consideration from sig-
nificant research communities to tackle a wide variety of
optimization problems. The primary purpose of this section
is to provide a comprehensive review of the GWO growth
from different aspects, including the number of GWO yearly
publications, the number of citations acquired for GWO
publications, the leading publishers and journals concerned
with GWO publications, the main authors, institutions, and
countries used GWO to tackle their optimization problems.
The data analyzed in this section are extracted from the
Scopus database.
Since the GWO foundation, its number of published arti-
cles is more than 800, as shown in Fig. 2. It is a fantastic al-
gorithm that is substantially grown and used for a wide range
of optimization problems. The majority of the publications
were Journal articles that indicate their high maturity and
robustness. Year by year, the researchers’ attention to GWO
is significantly increased. Although it is not considered the
most recent swam-based algorithm, it is still attracting the
attention of the optimization research communities due to its
superb features.
2014
2015
2016
2017
2018
2019
2020
2021
0
20
40
60
80
100
120
140
160
180
200
220
Number of publications
 
 
Article
Conference Paper
Book Chapter
4
22
29
46
94
161
187
177
FIGURE 2: The number of GWO publications per year
Due to the GWO solid theory, its related research ar-
ticles are accepted by highly-prestigious publishers, such
as IEEE, Elsevier, Springer-Nature, MDPI, Hindawi, Taylor
& Francis, Wiley, Hindawi, and others. As shown in Fig.
3, IEEE, Elsevier, and Springer-Nature are the publishers
with the largest portion of GWO-related articles. The IEEE
publisher accepted more than 200 articles, most of which are
engineering-related optimization problems.
The high-reputed journals that are specialists in the op-
timization research domains have also published significant
GWO research works. In Fig. 4, the top scientific journals
that accepted GWO articles to solve different optimization
problems are presented. Notably, the IEEE Access journal
has accepted more than 40 articles. Applied soft computing
journal, which is from top journals of the optimization do-
main, has also accepted more than 35 GWO-related articles.
Other top journals have also accepted more than 10 GWO-
related articles on average. This proves the stagnated theory
of the GWO.
IEEE Access
Applied Soft Computing Journal
Expert Systems With Applications
Neural Computing And Applications
Energies
Knowledge Based Systems
Applied Sciences Switzerland
Journal Of Physics Conference Series
Journal Of Ambient Intelligence And Humanized Computing
Soft Computing
0
10
20
30
40
50
11
9
7
7
6
6
13
13
36
41
FIGURE 4: The number of GWO publications per Journals
The idea of GWO is stemmed by Seyedali Mirjalili in 2014
[64]. The same author has utilized the GWO to tackle several
optimization problems. Deep K followed by Shubham Gupta
and Mohammed Al-Betar, conducted the highest publications
of GWO-based research articles, as presented in Fig. 5.
Mirjalili, Seyedali
Deep, K.
Gupta, Shubham
Azmi Al−Betar, Mohammed
Castillo, Oscar
Saxena, Akash
Soria, José
Kamel, Salah
Kumar, Rajesh Satish
Gao, Liang
Li, Xinyu
Long, Wen
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
13
12
11
10
10
9
9
8
8
8
15
17
FIGURE 5: The number of GWO publications per author
After a deeper look at Fig. 6, the researchers from China,
India, Iran, and Egypt have intensively utilized the GWO
in their research work. Researchers from other countries, as
highlighted in the Map, also used the GWO to some extent.
The GWO has proven its viability through its considerations
by many scholars worldwide.
4
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 5 -->
## Page 5

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
2015
2016
2017
2018
2019
2020
2021
2022
0
30
60
90
120
150
180
210
 
 
IEEE
Springer
Elsevier
Hindawi
John Wiley & Sons
MDPI
Taylor & Francis
Others
93
71
39
26
159
186
177
29
IEEE (26%)
Springer (20%)
Elsevier (18%)
Hindawi (2%)
John Wiley (2%)
MDPI (5%)
Taylor & Francis (2%)
Others (25%)
(a)
(b)
FIGURE 3: The number of GWO publications per publisher
FIGURE 6: The number of GWO publications per country
In terms of GWO publication per affiliation, more than
twenty GWO-based research were developed by researchers
at Huazhong University of Science and Technology, as shown
in Fig. 7. The Indian Institute of Technology Roorkee re-
searchers published more than eighteen GWO research pa-
pers. We believe the GWO is a powerful method that lightens
the spot for many research works.
Huazhong University of Science and Technology
Indian Institute of Technology Roorkee
Aswan University
Malaviya National Institute of Technology Jaipur
Universiti Malaysia Pahang
Ministry of Education China
Al−Balqa Applied University
Tijuana Institute of Technology
University of Tehran
Ain Shams University
Chongqing University
Griffith University
0
4
8
12
16
20
24
14
14
13
13
11
11
10
10
10
20
18
16
FIGURE 7: The number of GWO publications per Affilia-
tions
Citation is another indication of the viability and applica-
bility of the GWO. Amazingly, the GWO research has gained
more than 6200 accumulative citations based on the Scopus
citation report, as shown in Fig. 8. Indeed, the GWO is the
most cited swarm-based intelligence method grown rapidly
and gained high interest from several researchers due to its
efficient performance.
VOLUME 4, 2016
5
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 6 -->
## Page 6

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
2013
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
0
1000
2000
3000
4000
5000
6000
7000
8000
Nubmber of citations
107
18
328
741
1585
3088
4848
7217
1307
FIGURE 8: The number of citations per year
GWO addressed a wide range of optimization problems
from multidisciplinary topics. As can be noticed by the pie
chart in Fig. 9, the GWO has been intensively used to tackle
computer science problems with more than 500 publica-
tions. Engineering problems are the second-largest research
topic addressed by GWO, where more than 450 publications
tackled engineering problems. The GWO showed its high
performance in addressing other optimization problems in
other research fields, such as mathematics, energy, physics
and astronomy, environmental science, and business and
accounting.
Computer Science (30%)
Engineering (27%)
Mathematics (12%)
Energy (6%)
Physics & Astronomy (5%)
Materials Science (5%)
Decision Sciences (3%)
Chemical Engineering (2%)
Environmental Science (2%)
Earth and Planetary Sciences (1%)
Business & Management (1%)
Others (5%)
FIGURE 9: The number of GWO publications per Subject
IV. RECENT VARIANTS OF GREY WOLF OPTIMIZER
The GWO is an optimization method that is easy to use
and produces high-quality results. It was initially designed
for solving continuous optimization problems but has since
been adapted for other types of optimization problems. Re-
searchers have also made modifications to the GWO to
improve its performance, including improved and hybridized.
In addition, several studies change the algorithm optimization
processes to address multiobjective optimization problems.
These variations have been studied and applied to a variety
of different applications and optimization problems in the
following sections.
A. MODIFIED VERSIONS OF GREY WOLF OPTIMIZER
Like other algorithms, the GWO has weaknesses in ob-
taining optimal solutions during the search processes in some
cases. Thus, several investigations were presented to enhance
the GWO optimization processes and handle the disadvan-
tages, such as local optima stagnation, low convergence
speed, low exploration capabilities, and imbalance between
exploration and exploitation [66], [70], [71], [72]. Besides,
the GWO searching behaviour was modified to deal with
various search spaces, such as discrete and binary search
spaces [73], [74], [75]. Fig. 10 shows the studies that belong
to each modified version.
1) Random Walk Grey Wolf Optimizer
In the original GWO, each wolf in the group is updating
their position according to the position of the leader wolves.
This updating mechanism can be modified and enhanced by
changing its behaviour to randomly update the positions in
some cases to avoid local optimal stagnation, either for a part
of the pack or all the wolves [66].
Gupta and Deep [66] presented an innovative approach,
termed random walk GWO, as a modified version of the
Grey Wolf Optimizer (GWO) algorithm. This modification
aimed to overcome the challenge of premature convergence
and prevent getting stuck in local optima. In their GWO
algorithm, the leaders take on an exploratory role by en-
gaging in random walks throughout the search space. Mean-
while, the remaining wolves update their positions based on
the leaders’ positions. To evaluate the performance of the
proposed method, the authors conducted experiments using
30 test functions from the CEC 2014 collection, as well
as four real-world engineering problems. The experimental
results highlighted the efficiency of the random walk GWO
approach when compared to both the original version of
GWO and other comparative algorithms.
In another study, the same method was adopted by the
same authors for solving the optimal coordination of the
overcurrent relays problem with satisfactory results against
the original version of GWO and other competitors [76].
A novel modified version of GWO was specifically de-
signed for synchronizing chaotic satellite systems [77]. The
proposed method introduced the concept of random search-
ing positions and incorporated memoization of the best so-
lution at each iteration to enhance the searchability of the
algorithm. The effectiveness of the proposed method was
demonstrated through numerical experiments, comparing it
to other state-of-the-art methods. The results highlighted the
utility and superiority of the modified GWO algorithm, sur-
passing the performance of the compared methods in terms
of optimization quality and convergence speed.
Heidari et al. (2019) made significant advancements to
enhance the performance of the basic GWO by incorporating
various innovative components. These components included
random leaders, opposition-based learning, levy combat pat-
terns, random spiral-form movements, and a greedy selec-
tion strategy. These components were used to strengthen
the global research and local exploiting capabilities, as well
as to deepen GWO’s searching benefits in dealing with in-
creasingly complicated situations. The effectiveness of the
enhanced GWO algorithm against a wide range of state-
of-the-art optimizers across 23 benchmark testing functions
and 30 well-known CEC problems is studied. Additionally,
6
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 7 -->
## Page 7

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
FIGURE 10: Studies for each modified version
the proposed method was utilized for fine-tuning the kernel
extreme learning machine in addressing two real-world prob-
lems. The experimental findings and analyses demonstrate
that the enhanced GWO outperformed the classical GWO
and some other well-established methods. Notably, the sug-
gested method exhibited faster convergence rates and consis-
tently delivered higher solution quality across the evaluated
problems.
Adhikary and Acharyya [78] introduced an advanced vari-
ant of the GWO algorithm called Randomized Balanced
GWO. This algorithm enhances the search capabilities by
incorporating three successive enhancement strategies, along
with a social hierarchy mechanism and random walk. The
algorithm is evaluated using a diverse range of benchmark
functions from the CEC-2014, spanning various scales. Fur-
thermore, both constrained and unconstrained real-life prob-
lems were employed to assess the algorithm’s performance.
The obtained results against state-of-the-art methods show
the superiority of the proposed algorithm.
Liu et al. [79] tackle the flaws in the algorithm by using
a dimensional learning strategy (DLS). In addition, the Levy
flying technique is also used to explore the abilities of the
algorithm. To instruct the grey wolves in the swarm, the
proposed approach uses three dominant wolves to create an
exemplar wolf using the DLS. The proposed method evalua-
tion process goes through 23 standard functions and some en-
gineering problems. The practical findings demonstrate that
the DLGWO performs well in tackling global optimization
issues.
2) Binary Grey Wolf Optimizer
The pure version of the GWO was introduced to tackle
continuous optimization problems. Other versions of GWO
were introduced to deal with other search spaces, such as
binary search spaces. Usually, to deal with binary search
spaces, the transfer functions like the S-Shaped, V-Shaped,
and U-Shaped are combined within the original GWO.
Hu et al. [73] introduced an enhanced binary variant of
the Grey Wolf Optimizer (GWO) algorithm specifically de-
signed for feature selection problems. In their approach, they
utilized S-shaped and V-shaped transfer functions to trans-
form the continuous GWO into a binary form. Additionally,
they modified the equation for updating the parameter a to
improve the balance between exploration and exploitation
capabilities. To assess the effectiveness of their method, the
researchers conducted experiments on 29 well-known test
functions and utilized 12 datasets sourced from the UCI
repository. The experimental results clearly demonstrated the
superiority of the proposed method over other binary versions
of GWO, as evidenced by the enhanced fitness values and
improved optimization of classification accuracy.
Al-Tashi et al. [74] presented a binary multi-objective
Grey Wolf Optimizer (GWO) tailored for feature selection
problems. Two distinct versions of their algorithm based on
S-shape and V-shape transfer functions are designed to deal
with the binary nature of the feature selection. The primary
objective of their proposed method was to optimize both
the number of selected features and classification accuracy.
To evaluate the performance of the proposed versions, the
authors conducted experiments using 15 datasets obtained
from the UCI repository. The experimental results showcased
the effectiveness of the proposed methods when compared
to other well-established optimization techniques, demon-
strating superior performance in terms of classification ac-
curacy, the number of selected features, and computational
efficiency.
Safaldin et al. (2021) introduced an integrated approach
that combines a binary Grey Wolf Optimizer (GWO) and
Support Vector Machine (SVM) for intrusion detection in
wireless sensor networks. Intrusion detection, a feature se-
VOLUME 4, 2016
7
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 8 -->
## Page 8

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
lection problem within the wireless network domain, was the
focus of their study. To convert the GWO algorithm from
a continuous to a binary version, the researchers utilized
a sigmoidal transfer function. The SVM was employed for
classification purposes. The proposed method’s performance
was assessed using the NSL-KDD’99 dataset. Experimen-
tal results demonstrated that the proposed approach outper-
formed the binary version of particle swarm optimization
in terms of intrusion detection accuracy and computational
time.
Chantar et al. [80] introduced an alternative binary GWO
specifically tailored for Arabic text classification. Their pro-
posed method incorporated an elite-based crossover as a
wrapper feature selection technique for this classification
task. To convert the original continuous GWO into a binary
version, the researchers utilized an S-shaped transfer func-
tion. The integration of the elite-based crossover ensured a
more flexible balance between exploration and exploitation
capabilities. The study investigated various learning models,
including decision trees, K-nearest neighbor, Naive Bayes,
and SVM classifiers, to determine which classifier yielded
the best performance for Arabic text classification. The
evaluation utilized three Arabic datasets, namely Alwatan,
Akhbar-Alkhaleej, and Al-Jazeera-News. The experimental
results demonstrated that the proposed method outperformed
other approaches in terms of accuracy and the number of
selected features, establishing its superiority in Arabic text
classification tasks.
Luo and Zhao [81] introduced an enhanced binary version
of the GWO specifically designed for solving the multidi-
mensional knapsack problem. Their proposed method in-
corporated several key modifications to improve the algo-
rithm’s performance. First, they utilized an elite population
generator to construct the initial population, ensuring that
the search process begins with good-quality solutions rather
than random ones. This strategy enhances the algorithm’s
ability to converge toward optimal solutions more efficiently.
Next, a repair procedure was implemented to maintain the
feasibility of solutions throughout the search process. To
enhance the exploration ability of the GWO algorithm, the
equation for updating the position of each wolf in the group
was modified. This modification enables the algorithm to
explore the search space more comprehensively, facilitating
the discovery of diverse and potentially superior solutions. In
addition, the S-shape and V-shape were employed to convert
the continuous values of the algorithm to binary values. The
performance of the proposed method was evaluated using
two datasets of varying sizes and complexity obtained from
the online OR library. Numerical results demonstrated the
superiority of the proposed method compared to other binary
comparative algorithms, affirming its effectiveness in solving
the multidimensional knapsack problem.
An advanced binary version of GWO is introduced for the
profit-based unit commitment of price-taking GENCO in the
electricity market [82]. The primary objective of GENCO
is to efficiently schedule available units to maximize profit
in the competitive electricity market sector. To convert the
original continuous GWO algorithm into a binary version, the
researchers introduced three different versions, each incorpo-
rating a distinct transfer function. These transfer functions
included crossover sigmoidal, conventional sigmoidal, and
tangent hyperbolic functions. This transformation enabled
the GWO algorithm to operate in the binary domain, suitable
for solving the profit-based unit commitment problem. Three
algorithms were evaluated using two test systems, one with
three units and another with ten units. Numerical results
clearly demonstrated the superiority of their algorithms over
other comparative algorithms found in the literature that was
used to solve the same problem in terms of average profit
convergence.
Abdel-Basset et al. [83] addressed the feature selection
problem by utilizing two improvements for the original
GWO. Firstly, the GWO was modified to deal with the
binary search spaces using the sigmoid function. Secondly,
a mutation operator was utilized in two phases to improve
the exploitation capability and increase its accuracy. Several
comparisons with well-known methods were conducted to
investigate the proposed method’s performance. The exper-
iments proved the significance of the proposed method com-
pared with the other methods.
The authors in [84] introduced a novel binary modified
variant of GWO, called BIGWO, specifically designed for
feature selection in Parkinson’s Disease Diagnosis. The re-
searchers incorporated mutation operators into the BIGWO
algorithm to enhance its exploration capability, enabling a
more comprehensive search for optimal FS solutions. To
address FS problems, the continuous GWO algorithm was
transformed into a binary version using S-shaped and V-
shaped transfer functions. The BIGWO was evaluated us-
ing four datasets related to Parkinson’s Disease Diagnosis
sourced from the UCI repository. The experimental results
provided compelling evidence of the superiority of BIGWO
when compared to four other algorithms commonly used for
FS tasks.
Alyasseri et al. [85] conducted research on the challeng-
ing problem of electroencephalogram (EEG) signal channel
selection, which was formulated as a binary optimization
problem. To tackle this problem, the researchers employed
the binary version of the GWO (BGWO) to locate the opti-
mal solution. Furthermore, for EEG-based biometric person
identification, they considered the use of a support vector
machine (SVM) classifier with a radial basis function (SVM-
RBF). Three alternative autoregressive coefficients were in-
vestigated for feature extraction. The developed technique is
assessed using the accuracy, f-score, recall, and specificity
criteria on a common EEG motor picture dataset. The results
of the evaluation revealed that the BGWO-SVM approach
outperformed other methods in terms of competitive classi-
fication accuracy and the number of selected channels.
8
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 9 -->
## Page 9

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
3) Cellular Grey Wolf optimizer
The incorporation of cellular automata (CA) principles
into evolutionary algorithms has gained popularity in the field
of optimization. This integration aims to enhance exploration
capabilities and mitigate the issue of getting trapped in local
optima. In line with this trend, researchers working on the
Grey Wolf Optimizer (GWO) have also recognized the po-
tential benefits of integrating CA into the GWO framework
to address its limitations [86], [87]. By incorporating CA
principles, the GWO algorithm can benefit from improved
exploration and a reduced risk of converging to local opti-
mum solutions.
Lu et al. [86] introduced an enhanced version of the GWO
for addressing hybrid flow shop scheduling problems with a
focus on mitigating noise pollution. In the proposed method,
the CA concept is integrated with the multi-objective GWO
to empower its exploration ability. The key modification
involved updating each solution in the population based on
the positions of its neighboring solutions. The neighbours
of each solution are determined according to cellular topo-
logical structures. Additionally, the authors incorporated a
variable neighborhood search into the framework of their
method to enhance its exploitation capability. These mod-
ifications were introduced to achieve an optimal balance
between exploration and exploitation during the search pro-
cess. Such modifications were introduced to find the optimal
balance between the exploration and exploitation abilities
during the search process. To evaluate the performance of
the proposed method, the researchers conducted experiments
using a well-known benchmark dataset. The experimental re-
sults demonstrated the effectiveness of the proposed method,
as it achieved satisfactory results when compared to other
optimization methods commonly used for similar problems.
Cao et al. [87] introduced a novel approach, referred to as
cellular GWO, specifically tailored for simulating and opti-
mizing urban growth. In this method, the GWO is triggered
to optimize the urban growth rules within a cellular automata
(CA) framework. The urban growth rules in the CA frame-
work capture the relationships between spatial variables and
the land-use status of each cell, providing a mechanism
to simulate the dynamic changes in urban areas. To assess
the efficiency of the proposed method, a real-world dataset
from Nanjing City, China, spanning the period from 2005 to
2013, was utilized. The simulation results demonstrated the
superior performance of the proposed method compared to a
well-known alternative method in terms of accuracy for the
urban cells and the kappa coefficient.
4) Adaptive Grey Wolf Optimizer
The GWO is a multipurpose metaheuristic search algo-
rithm that uses the minimum number of adjustable parame-
ters. The GWO proved its efficiency in many benchmarks and
industrial applications. However, the researchers are always
imperative to improve the performance of the GWO by
self-tuning or problem by the dependent adaptation for its
parameters. Enhancing performance and ensuring efficient
convergence are crucial aspects of avoiding the limitations
of local minima. This necessitates a delicate equilibrium
between exploration and exploitation. Traditionally, achiev-
ing this balance involves employing nonlinear operators that
inherently adjust the parameters of the GWO algorithm. The
following papers provide noteworthy examples in this do-
main, illustrating the application of such operators to enhance
GWO performance.
Yildirim and Alatas [70] introduced a novel approach
that combines automatic data mining with the GWO al-
gorithm for multi-objective optimizations. The proposed
method was extensively tested on diverse datasets, aiming to
identify optimal classification rules and assess the effective-
ness of the proposed enhancements. Their GWO method was
compared against several comparative techniques, including
naive Bayes, k-NN, support vector machines, and decision
trees. Additionally, the approach was applied to five real-
world datasets. The obtained results convincingly demon-
strated the efficiency and accuracy of their GWO algorithm,
showcasing its superiority over the alternative methods in
terms of achieving optimal solutions.
Rashid et al. [88] proposed an adaptive GWO to train
recurrent neural networks. The application was to discover
the students’ weaknesses and apply better learning methods
in the future. The proposed method presented much better
accuracy in forecasting the students’ performance than the
compared methods.
Optimal placement and sizing of active power filters con-
sidering the distribution of photovoltaic generation were
investigated by Lakum and Mahajan [89] proposing a new
adaptive GWO. The optimal placement achieved by the pro-
posed method was tested in 3 different cases. The proposed
method was compared with the original GWO. The proposed
method showed a significant performance compared with the
original GWO.
Liu et al. [90] proposed an adaptive GWO and self-adapted
GWO to optimize the problem of optimal cascaded daily
pumping of water. The proposed methods used exploitation
operators to support the exploration operators of the standard
GWO. They also used dynamically adjusting operators in
the proposed algorithms. The proposed methods were tested
on 23 benchmark functions, and both showed competitive
results. They also used them to optimize the operations of six
cascaded pumping stations. The proposed methods proved to
be more efficient and economical than other methods.
Fu et al. [91] introduced an adaptive mutation GWO to
build a forecasting model for the vibrations tendency of
hydro-power generators. The authors used the multi-scale
chaotic ingredient analysis method and tested their method
on six predictive models. During the evaluation phase, the
proposed method underwent rigorous testing using several
datasets and was subjected to a thorough comparative anal-
ysis with other existing approaches. Notably, the results
obtained from these experiments clearly showcased the su-
periority of the proposed method over all the compared
alternatives.
VOLUME 4, 2016
9
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 10 -->
## Page 10

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
Li et al. [92] introduced another variant of adaptive GWO
with the objective of optimizing thermal comfort values
within an HVAC system. To accurately predict the thermal
level, a backpropagation neural network was integrated into
the proposed method. Through a comprehensive comparative
analysis, the obtained results were contrasted against well-
established techniques in the field. The findings from this
study demonstrated the exceptional performance of the pro-
posed GWO method, showcasing significantly elevated levels
of thermal comfort. Furthermore, it effectively achieved ad-
ditional energy savings, further emphasizing its superiority
when compared to other established methods.
In a similar vein, Dhar et al. [93] presented an innovative
and improved version of the GWO algorithm, referred to
as cmaGWO. Their objective was to apply this enhanced
algorithm for global optimization and parameter tuning of
the Forward and Backward mapping models in the context
of direct metal deposition processes. To enhance the balance
between exploration and exploitation abilities, the authors
incorporated the covariance matrix adaptation technique to
update the initial perspective prey location in their cmaGWO
algorithm. To evaluate its performance, the cmaGWO was
rigorously tested on a set of 23 classical test functions as well
as 5 additional test functions from CEC-2017. The numerical
results obtained from these experiments provided compelling
evidence for the effectiveness of the cmaGWO approach
when compared to both the original GWO algorithm and
other comparative methods. Notably, when employed to tune
both the forward and backward mappings, the cmaGWO
algorithm showcased superior performance in terms of mean
absolute percentage error.
In their work, Meidani et al. [94] introduced an innovative
approach to enhance the Grey Wolf Optimizer (GWO) by
incorporating adaptive mechanisms. The proposed method
dynamically tunes the searching and neighboring parameters
based on the fitness history of candidate solutions throughout
the search process. This intelligent adaptation enables the
algorithm to automatically converge towards a promising
optimum within the shortest possible time. Moreover, the
authors extended their adaptive GWO by integrating a three-
point fitness history, which further refines the convergence
parameters. The experimental results obtained from applying
the adaptive GWO approach showcased its superior ability
to achieve improved solutions when compared to the original
GWO algorithm.
5) Chaotic Grey Wolf Optimizer
The chaotic mapping mechanism is a random technique
normally integrated with the optimization algorithms to en-
hance diversity control. In chaotic optimization algorithms,
the solution contains chaotic variables rather than random
variables. There are different chaotic map functions, each
with a different mathematical formulation to convert from the
original version to the chaotic version. Many chaotic GWO
algorithms are introduced in the literature, as summarized
below.
Lu et al. [95] introduced an advanced version of the GWO
algorithm by incorporating principles from chaos theory.
This integration aimed to address the inherent limitation
of GWO by being trapped in local optima. The authors
proposed eleven versions of chaotic GWO, each utilizing a
different chaotic map function, in order to determine the most
effective performance behavior. To assess the algorithm’s
capabilities, the researchers conducted extensive evaluations
using the CEC 2005 dataset and four engineering problems.
Through these experiments, the GWO algorithm employing
the Chebyshev map function exhibited superior performance
compared to the other versions of chaotic GWO. Moreover,
simulation results demonstrated the remarkable superiority of
the proposed chaotic GWO approach over other comparative
algorithms when applied to the same problems.
Saxena et al. [96] presented an innovative approach by
introducing a chaotic variant of the GWO algorithm for
unconstrained numerical optimization. In their method, the
β-chaotic sequence was seamlessly integrated with GWO
to adaptively control the exploration and exploitation capa-
bilities. This integration aimed to strike the ideal balance
between exploration and exploitation throughout all stages
of the search process. The researchers conducted extensive
evaluations using a set of test functions derived from the
CEC 2017 collection, as well as two real-world engineering
problems. The simulation results revealed that the proposed
chaotic GWO algorithm consistently outperformed other ver-
sions of GWO, as well as other comparative algorithms from
the existing literature when applied to the same problem set.
Another chaotic GWO was proposed by Zhang and Hong
[97] for forecasting electric loads. The authors combined
the variational mode decomposition and the chaotic GWO
to enhance the search experience and identify optimal pa-
rameter settings for the support vector regression model.
The utilization of the Tent chaotic mapping function within
their model aimed to augment the diversity of the search
process, facilitating improved solution exploration. The pro-
posed model was evaluated using two real-world datasets
sampled from New South Wales (Australia) and National
Grid (UK). The experimental results demonstrated that the
proposed model outperformed other comparative models in
terms of forecasting accuracy, showcasing its superior per-
formance and effectiveness in electric load forecasting.
The multi-robot task allocation problem was addressed by
Li and Yang [98] proposing a new improved GWO utilizing
the chaotic approach to enhance the initial population and its
diversity, thus, enhancing the solutions’ quality. Furthermore,
to further enhance the optimization process, an adaptive strat-
egy was employed to refine the best solution while ensuring
a balance between exploration and exploitation. Through
rigorous testing on diverse datasets, the proposed method
consistently outperformed the compared approaches in terms
of solution quality.
Similarly, Hu et al. [99] proposed a modified variant of the
GWO called SCGWO, specifically tailored for global opti-
mization and feature selection (FS) problems. The SCGWO
10
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 11 -->
## Page 11

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
method incorporates two key enhancements: an improved
spread strategy and a chaotic local search mechanism, aimed
at enhancing the performance of GWO. The improved spread
strategy is designed to bolster the algorithm’s global search
capabilities, enabling it to effectively navigate potential local
optima. Meanwhile, the chaotic local search mechanism ac-
celerates the convergence speed, allowing for faster and more
efficient optimization. To assess its performance, SCGWO
was rigorously evaluated using a diverse range of classical
test functions and 32 FS datasets sourced from the UCI
repository. The simulation results showcased the remarkable
effectiveness of SCGWO compared to other comparative
methods, both in terms of convergence speed and solution
quality.
6) Gaussian Grey Wolf Optimizer
Wang et al. [100] proposed a new modified version of
the GWO to address the premature convergence problem.
The proposed method was introduced to enhance the GWO
exploration capability by combining its searching parameters
with the gaussian estimation of distribution approach. In
addition, the Gaussian distribution-based inferior solutions
repair method was proposed to modify the ill-shaped distri-
bution of the GWO population. In the experimental results,
the performance of the proposed method was compared with
that of other state-of-the-art methods using the CEC 2014
benchmarking function. The obtained results proved the high
performance of the proposed method compared to the other
methods.
A
new
version
of
the
GWO
was
proposed
by
Khalilpourazari et al. [101] to address well-known complex
benchmark functions optimally. The authors utilized the
gradient information on the original GWO to accelerate its
convergence into the optimal solution. In addition, the Lévy
flight and Gaussian approaches were used to enhance the
exploration and exploitation capabilities of the GWO, as well
as avoid local optimal stagnation. The proposed method was
evaluated using different benchmark functions. The proposed
method demonstrated all compared methods in optimizing
the problems.
Similarly, the authors in [102] combined the GWO and
the Gaussian kernel function in a new algorithm called
kernel-based Picture Fuzzy C-Means clustering with GWO
(KPFCM-GWO). In their algorithm, the Gaussian kernel
function is utilized as a symmetrical measure of distance
between data points and cluster centers, while the GWO is
used to tune the best settings of PFCM. The simulation results
demonstrate the effectiveness of the KPFCM-GWO against
other clustering methods.
7) Dynamic Grey Wolf Optimizer
Dynamical GWO is used to provide more flexibility and
search capability for the algorithm by modifying the popula-
tion size when needed or enhancing information exchange
among the best wolves. It also uses nonlinear operators
to balance the search strategy by either focusing on local
or global search strategies. The papers below show several
applications using the concepts of the dynamic GWO.
Luo [103] proposed a dynamic GWO to change the
wolves’ positions dynamically. In this version, the leader
wolves always keep estimating the location of the prey. That
gives more flexibility and tracking ability to the algorithm.
The proposed method outperformed the original GWO based
on the CEC2017 testing suite. The proposed method was also
used in solving engineering problems at lower computation
costs. It showed more convergence speed and quality of the
solutions.
A dynamically dimension-ed GWO was proposed by Yan
et al. [104]. This dynamical GWO used an interaction strat-
egy between the best three wolves to exchange location
information. It also used a nonlinear control parameter to
balance exploration with exploitation searches. Experiments
were done on 23 benchmark functions and three well-known
engineering applications. The proposed method showed a
fast convergence and high robustness compared to other
compared methods.
8) Opposition Grey Wolf Optimizer
Opposition-based GWO is introduced to solve the stag-
nation and lack of diversity problems the standard GWO
may have. The GWO uses a nonlinear operator to introduce
jumping and escaping local minima. This implies more ex-
ploitation of search space areas around the best solutions
found. Many applications were efficiently solved based on
the opposition-learning theory-based GWO. The papers be-
low present some of the applications that used such a concept.
An opposition-based competitive GWO was used by Too
and Abdullah [71] to find the optimal feature selection and
classification of EMGs. The authors accessed the publicly
available EMG database for training and testing. They use the
binary version of the GWO and convert it into a continuous
version of GWO in order to perform a search in continuous
space. The proposed method proved its high capabilities
in optimizing the problem and achieving the best results
compared with the compared methods.
Yu et al. [105] proposed an opposition-based GWO to
optimize complex and multi-modal functions. The authors
used a jumping rate for the opposition dynamically ad-
justed by a nonlinear function to balance exploitation with
exploration. Several experiments were conducted, and the
proposed method proved to be much better than conventional
techniques.
A random opposition-based GWO was used by Long et
al. [106]. This method was used to avoid the GWO from
getting stuck in local minima. In addition, the proposed
method aims to obtain a better balance between exploration
and exploitation. The proposed method was evaluated on
23 benchmark test functions and 30 benchmarks from IEEE
CEC 2014. The results obtained were competitive with other
optimization techniques.
Feng et al. [107] improved GWO to optimize 12 classical
test functions in addition to the two cascaded hydropower
VOLUME 4, 2016
11
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 12 -->
## Page 12

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
constraint optimization problems. The goal was to smooth
the peak loads of the power system. Quasi-oppositional
learning and an elite mutation operator were employed in
this improved GWO version. Elastic ball strategy and heuris-
tic constraint handling were used. The results showed that
the proposed method outperformed several existing classical
techniques.
Long et al. [108] used a new version of oppositional GWO
based on the process of the refraction of lights in physics.
Theoretical proof for convergence is provided. Testing for
the RL-GWO was done on 23 benchmark functions and the
other 30 test functions from CEC 2014. It has been shown
that the proposed method is efficient and reliable in solving
optimization problems.
Another opposition-based GWO version was proposed by
Guttula and Nandanavanam [109] to find the optimal design
of a microstrip patch antenna. The authors used a nonlinear
model based on the antenna parameters. The proposed model
proved its high optimization capabilities by obtaining better
performance than other conventional methods. The resulting
design was superior, with higher values of antenna gains.
The training of an echo state network was implemented by
Chen et al. [110] using selective opposition GWO. The main
aim of such a model is to predict nonlinear and chaotic time
series. The proposed method was applied to typical chaotic
time series such as Mackey-Glass and Lorenz. Simulations
showed that the proposed method has better prediction per-
formance than other state-of-the-art methods.
Gupta and Deep [111] introduced an enhanced GWO
called the opposition-based chaotic GWO. The proposed
methods mitigate the stagnation problem that the stan-
dard GWO may suffer from by introducing more exploita-
tion searches and applying opposition-based learning. The
method was applied to three standard engineering problems
and 23 standard benchmark tests. Experiments showed the
new method’s reliability and superiority over the standard
GWO.
The opposition-based learning approach and explorative
equation were combined with the GWO to enhance its ex-
ploration and exploitation abilities, thus, improving the solu-
tions’ quality [112]. The validation of the proposed method
was tested using 23 standard benchmark test problems. The
obtained results showed the high performance of the pro-
posed method in addressing the optimization problems.
The authors in [113] introduced another modified version
of GWO, called EOCSGWO, for global optimization and
to optimize the parameter of an auto drum-fashioned brake.
In EOCSGWO, the elite opposition-based learning strategy
and k-best gravitational search strategy are combined with
the GWO to enhance its performance. The elite opposition-
based learning strategy is introduced to take advantage of the
best wolves in the next generations, while the k-best gravita-
tional search strategy is used to enhance the global search
ability. The performance of the EOCSGWO is evaluated
using 10 classical test functions and compared to the seven
other variants of GWO. The simulation results illustrated the
superiority of the EOCSGWO against others. Finally, the
EOCSGWO is applied to find the best parameter settings
of an auto drum-fashioned brake with satisfactory results
compared to the initial design.
The new quasi-opposition-based learning was combined
with the GWO in [114] to emphasize its exploitation and
exploration capabilities, as well as escape the stagnation in
local optima. The proposed method was tested by finding
the best factors for adaptive model predictive control. The
obtained results by the proposed method proved its high
performance in achieving the optimal factors compared to
other methods.
Another modified GWO version was proposed in [115]
based on the dynamic opposite learning to improve the lo-
cal and global search behaviour and find better results for
the CEC2014 23 benchmark functions. In the experimental
phase, the proposed method was compared with ten original
and improved optimization methods. The proposed method
almost outperformed all compared methods.
Rezaei et al.[116] develop a novel version of the GWO
to address the lack of a velocity operator in the technique
of position-updating that leads to a limitation in exploration
capability. So, this modification enhances the algorithm’s ca-
pabilities for exploration and exploitation by controlling the
step size in both early iterations and later iterations, making
them large and then small, respectively. The experimental
findings show that the VAGWO technique is a computa-
tionally efficient one that produces incredibly precise results
when used to optimize highly dimensional and complicated
issues.
Sun et al. [117] developed a new version of the GWO in or-
der to improve optimization performance. The modification
was made to address falling into the local optimal problem by
incorporating a refraction opposite learning (REL) technique.
The proposed method resolves the problem of low swarm
population variation in the late iteration of GWO by effec-
tively utilizing the REL. Additionally, the equilibrium pool
technique also lessens the possibility of wolves migrating to
the local extremum areas. IEEE CEC 2019 test functions as
well as 21 commonly used benchmark functions are utilized
to evaluate the performance of a modified algorithm.
9) Structured population Grey Wolf Optimizer
The GWO can be enhanced by structuring the population
into different groups depending on the rank or quality of
every sub-group. Different learning strategies could be used
for different sub-groups based on some decision mechanism.
The primary aim of such enhancement is to improve the
efficiency and capability of the GWO to solve large-scale and
complex optimization problems with the best performance.
Several related studies have been proposed and summarized
below.
Tu et al. [118] proposed a hierarchy-strengthened GWO
to optimize a 50-dimensional problem based on the CEC
2014. The proposed method was tested with large-scale
optimization problems with 100 decision variables. Finally,
12
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 13 -->
## Page 13

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
the feature selection problem was used for further testing.
The proposed method divides the population into dominant
wolves and omega wolves. Dominant wolves were trained
with an elite learning strategy. The omega wolves were
trained with differential evolution and enhanced GWO. This
is all done to balance the exploitation and exploration strate-
gies of the proposed method. Testing proved the efficiency of
the proposed method and the speed of convergence.
Ezhilsabareesh et al. [119] used grouped GWO to optimize
PID controllers. This is done to achieve maximum efficiency
tracking for the generators of different axial velocities. The
generator’s work was introduced based on the oscillating
water column wave energy converters. The obtained results
of optimization showed an increase in the system’s efficiency.
A synchronous-asynchronous processing scheme was
adapted for the GWO using a set of nonlinear functions and
operations to increase diversity by Rodríguez et al. [120].
In that sense, a better balance between exploration and ex-
ploitation was achieved. More accuracy and local minimum
avoidance were obtained. Evaluation of the proposed method
was implemented with the 2017 benchmark set of functions
and real-world problems. The results prove the effectiveness
and quality of the new method.
A multi-group GWO was proposed by AlShabi et al.
[121]. The new method consists of several packs or clans,
each consisting of 4 levels of wolves. That resulted in a
higher speed of convergence and more efficient reach to the
solutions. The technique was used to extract the parameters
of a single-diode photovoltaic solar cell. The results obtained
for the proposed method were much better than those of
other comparative techniques. The achieved results were
even better than those for standard GWO.
The authors in [122] introduced a new modified variant
of GWO for global optimization. Their algorithm is called
adult-pup teaching–learning based interactive grey wolf op-
timization (AP-TLB-IGWO). In AP-TLB-IGWO, the adult
wolves and pup wolves act as search agents. The search
agents between the two subpopulations concurrently and
independently explore the entire search space for optimal
results. In addition, Information sharing takes place between
adult and pup wolves to enhance diversification and to make
the right balance between the exploration and exploitation
abilities during all stages of the search process. The per-
formance of the AP-TLB-IGWO was evaluated using 23
classical test functions, 30 test functions from CEC2014, 30
test functions from CEC2017, and five classical engineering
problems. The simulation results demonstrated the effective-
ness of the AP-TLB-IGWO compared to the original GWO
and other modified versions of GWO and other comparative
methods.
10) New parameter for Grey Wolf Optimizer
The searching behaviour of GWO can also be modified by
integrating its components with new optimization parameters
to address different drawbacks based on the added parameter.
The selection behaviour of the best solutions in GWO was
modified to enhance its searching capabilities and find better
solutions in the search space by utilizing a new adaptive
parameter to assign an appropriate weight for the solutions
[67]. The proposed method tested a feature selection problem
in the medical science domain. In the evaluation phase, the
proposed method was evaluated and compared with well-
known methods. The proposed method outperformed the
compared method in achieving the best solutions.
The GWO searchability was improved by utilizing a
crossover operation and adaptive control parameter by Liu
et al. [123]. The crossover operation was used to increase
the population diversity of the GWO and the adaptive pa-
rameter to maintain balance the exploration and exploitation.
The proposed method was evaluated using benchmark op-
timization functions. The obtained results proved the high
performance of the proposed method compared to six well-
known methods.
A modified GWO was introduced to address the supplier
selection and order quantity allocation problems [124]. In
the proposed method, a new weighted coefficient param-
eter and a displacement vector were utilized to enhance
the exploration capabilities and avoid unfeasible solutions.
In the evaluation phase, the proposed method was tested,
evaluated, and compared with other optimization methods.
The proposed method proved its high capability to optimize
such problems efficiently.
The GWO was improved by Miao et al. [125] to overcome
its drawbacks and enhance its search performance in address-
ing global optimization problems. The enhancement of the
GWO starts by utilizing a new adaptive coefficients parame-
ter to achieve better convergence speed. Subsequently, a new
position-updating equation is used to emphasize the explo-
ration capabilities and find better solutions. The experimental
results proved the high performance of the proposed method
in optimizing well-known global functions and outperform-
ing the compared methods.
Komijani et al. [126] proposed an extended GWO by uti-
lizing a new coefficient parameter to optimize the fractional-
order proportional derivative sliding mode controller. In the
evaluation results, the proposed method was compared with
the original GWO. The obtained results proved the high ca-
pability of the proposed method in optimizing the controller
and achieving better solutions.
An extended GWO was proposed by utilizing a new co-
efficients parameter to enhance the algorithm searchability
and obtain better solutions [127]. The proposed method was
evaluated by testing its performance in optimizing a novel
control approach sliding mode control. The proposed method
exhibited better results than all compared results in the eval-
uation stage.
New dynamic inertia weights were proposed to control the
grey wolf social hierarchy and make the wolf more adaptable
for better exploring and exploiting the search space [128].
The proposed method was mainly used to optimize the sup-
port vector machine parameters and find the best accuracy of
VOLUME 4, 2016
13
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 14 -->
## Page 14

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
traditional coal spontaneous combustion temperature predic-
tion. In the evaluation stage, the proposed method was tested
on different datasets and constraints. The proposed method
showed high performance in finding the best accuracy.
11) Fractional Grey Wolf Optimizer
A further alterations method that can impact how well
the GWO searches is the functional method. In searching
space, the functional technique is mostly employed to alter
the wolves’ movements [72], [129].
Deshmukh and Rani [72] used an upgraded release of the
GWO to solve the resolution issue for multi-view facial video
super-resolution. To significantly improve the performance
of the GWO search agents and achieve the optimal ex-
ploitation and exploration balance, a particular GWO release
is suggested based on the fractional technique and GWO
elements. The suggested method’s outcomes were contrasted
with those of other widely used approaches. In solving such
a problem, the suggested solution performed better than all
those that were compared.
Ma et al. [129] suggested a unique fractional GWO to
improve the GWO’s accuracy and produce better outcomes.
The advanced model was also used to improve the planned
fractional GWO searching functionality. Utilizing four op-
timization issues, the suggested approach was assessed and
contrasted with the other eight GWO methods. The findings
collected demonstrated the suggested method’s superior per-
formance compared to existing approaches.
12) Mutation operator for Grey Wolf Optimizer
The GWO search agents can be paired with an evolution-
ary element known as a mutation operator to improve their
searching powers and produce superior outcomes [130].
Niu et al. [130] suggested an enhanced GWO approach
to expand diversity utilizing the adaptive mutation method,
boost local search capacity using the hyperbolic acceleration
strategy, and maximize convergence speed using the elitist
selection strategy. By modifying the suggested method’s
parameters for water resource systems, it was put to the test.
In comparison to the compared methodologies, the suggested
method provided superior schedules, according to the simu-
lations.
In [131], an alpha-guided GWO approach was put up
as a way to speed up the original GWO’s convergence
and produce better results. The suggested strategy was also
enhanced to prevent stagnation in local optima by using
a mutation operator to alter the seeking agents’ location-
updating behavior and enhance exploration. Utilizing well-
known optimization functions, the suggested technique was
evaluated. In comparison to all other ways, the suggested
method produced better outcomes.
To solve scheduling issues in the electricity industry, Sidea
et al. [132] presented an improved GWO based on the el-
ements of the mutation technique. The suggested modifica-
tion’s primary goal is to prioritize exploration and exploita-
tion while striking the ideal balance between the two. Along
with the scheduling issues, the effectiveness of the suggested
strategy was examined using 23 conventional benchmark
functions. The suggested strategy fared better at maximizing
the search spaces and producing the best results than all other
strategies that were examined.
A mutation-driven modified grey wolf optimizer was sug-
gested by Singh and ChandBansal [133]. The improved algo-
rithm uses a mutation-driven approach and a greedy way to
choose the grey wolf, which changes the control value. Four
actual engineering design challenges from the real world
and 23 well-known standard benchmark functions are used
to assess the suggested approach. The outcomes demon-
strate that the suggested algorithm beats other comparable
approaches by delivering the best outcomes and achieving a
faster convergence to the ideal solution.
The GWO was combined, involving uniform as well as
nonuniform mutation agents, by the developers of [134] to
improve its exploration capabilities for sizing optimization
of truss design issues with continuous and discrete decision
variables. Their algorithm’s effectiveness was evaluated us-
ing four issues and ten distinct situations. The simulation
findings proved the suggested GWO’s efficacy by producing
an optimal design with the fewest weights that was on par
with or superior to the other comparison algorithms described
in the literature.
13) Neighbour Search for Grey Wolf Optimizer
In order to improve local search abilities and prevent stasis
in local optima, optimization approaches primarily use the
neighborhood searching approach [135].
In order to overcome issues with engineering and gen-
eral optimization, Nadimi-Shahraki et al. [135] presented an
updated GWO. The suggested approach was developed to
overcome the original GWO flaws, such as the unequal distri-
bution of exploitation and exploration, the absence of popula-
tion variety, and the sluggish convergence pace. The improve-
ment in GWO is accomplished by applying the movement
strategy, also known as the level of learning-based hunting
strategy, to boost neighboring search behavior and exchange
data among the solutions. Six cutting-edge approaches were
compared to the performance of the suggested method. The
collected findings demonstrated the excellent performance
of the suggested approach, showing that it outperformed the
strategies that were being evaluated in terms of results.
In order to best handle the welding shop inverse scheduling
issue, Wang et al. [75] suggested a new GWO version. The
suggested version was developed to improve the GWO’s lo-
cal search capabilities by utilizing the neighborhood search-
ing strategy while modifying the GWO’s searching behavior
to handle discrete optimization challenges. The efficacy of
the suggested approach was examined by contrasting it with
numerous cutting-edge approaches in the simulation find-
ings. The suggested approach demonstrated its efficacy by
surpassing all other methods that were compared.
In order to solve the welding shop inverse scheduling prob-
lem specifically for welding shop settings, Wang et al. [136]
14
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 15 -->
## Page 15

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
offer an improved version of the GWO that adds dynamic
incidents in addition to minimizing parameter modification.
First, for typical discrete optimization problems, encoding
based on a matrix and initiation by the crucial path are pro-
posed. These methods can shorten the duration of searches
and improve search efficiency. The second step is to im-
plement a variable neighborhood search strategy to enhance
the presented method’s local search functionality. In order
to minimize parameter alterations, the performance of the
suggested algorithm is then evaluated in three distinct types
of cases. Comparisons with cutting-edge methodologies are
also done. The results in practice show how successful the
proposed strategy is in handling WSISIP.
14) Greedy Approach for Grey Wolf Optimizer
The GWO was altered by utilizing the greedy technique
to improve hunting operations and the horizontal crossover
operator to improve and refine the best three wolves’ capacity
to search, according to [137]. A modification was made to the
GWO in order to handle the multiobjective optimal power
flow optimization issue and maximize all of its goals. On
IEEE 30- and 118-bus systems, the suggested technique was
verified. The outcomes showed that the suggested approach
performed superiorly to the approaches that were evaluated.
To preserve the balance among exploitation and explo-
ration, Gupta et al. [138] suggested an upgraded variant of
the GWO that utilized the memory method. The crossover,
greedy choosing, and individual ideal history techniques of
the solutions are all used in the suggested approach to carry
out its intended function. Utilizing well-known benchmark
functions, the suggested technique was assessed. The sug-
gested strategy fared better at optimizing the functions than
all the strategies that were compared.
Gupta et al. [139] suggested an enhanced leadership-based
GWO to increase the wolves’ capacity for searching and the
precision of their searches by employing greedy selecting
and the Levy-flight strategy. The suggested technique was
validated using industry benchmarks like IEEE CEC 2006
and IEEE CEC 2014. The obtained results demonstrated the
recommended method’s reliable effectiveness in solving the
challenges.
A novel hybrid GWO model using integer coding and
greedy techniques was presented by Huang et al. [140] to im-
prove the GWO’s ability to effectively handle discrete search
spaces. Additionally, in order to improve the exploration and
exploitation capabilities, the GWO searching behavior was
altered by using a central location and two-opt with Azimut
techniques. The proposed strategy was put to the test during
the experimental phase by utilizing the task distribution for
the unmanned aerial vehicle challenge. The acquired findings
were contrasted with those of the original GWO and addi-
tional approaches in order to effectively assess the suggested
approach. The outcomes demonstrated the great effectiveness
of the suggested approach in solving the issue.
Another modified version of GWO, known as G-
SCNHGWO, was presented by the authors in [141] to ad-
dress issues with economic load dispatch. In G-SCNHGWO,
sine and cosine functions are used in the GWO’s architecture
to improve exploration and prevent the local optimum issue.
Additionally, G-SCNHGWO makes use of the greedy non-
hierarchical idea to strengthen the algorithm’s searchability
and balance the capabilities of exploitation and exploration at
all phases of the search procedure. Four real-world datasets
are used to assess the G-SCNHGWO’s performance, and the
comparison with other rivals yields promising findings.
15) Other improved versions of Grey Wolf Optimizer
Other improvements to the GWO searching behavior have
been suggested in various research studies to develop it and
solve its shortcomings in order to find better answers to a
variety of optimization challenges.
In order to increase the GWO’s capacities for exploration
and exploitation and overcome the GWO’s searching limita-
tions, Khanum et al. [142] developed two improvements. Ini-
tially, a novel parameter that alters the equations of surround-
ing and location updates for search agents was proposed,
which changed the encircling, updating locations, and hunt-
ing procedures. Second, the GWO components were merged
with the Minkowski technique. Using well-known test func-
tions, the suggested strategy was evaluated and contrasted
with alternative approaches. The outcomes demonstrated the
suggested method’s effectiveness by outperforming all other
approaches that were compared.
By balancing exploration and exploitation functionally and
boosting the sensitivity factor of the fuzzy clustering iterative
method, Zou et al. [143] proposed an improved version of
the GWO based on the immune clone selection approach to
increase the GWO’s searchability. The simulation’s results
showed that all of the compared outcomes were successful in
accomplishing and optimizing the goals.
To locate and retrieve the earthquake catalog based on
the idea of ergodicity, Vijay et al. developed and handled
the cluster event optimization issue [144]. In order to in-
crease the exploration and exploitation capabilities of the
GWO and achieve optimal balance, the defined problem was
handled and improved utilizing a new modified GWO that
was developed based on the quantum method. 24 benchmark
functions were used to assess the suggested technique. The
collected findings demonstrated the suggested technique’s
solid efficacy by exceeding all other approaches that were
examined.
To improve its searching efficiency and capacities in deal-
ing with the design membership problem and optimizing
seismic structure damage, Azizi et al. [145] suggested an
improved GWO. Twenty benchmark datasets with nonlinear
behavior involving up to 400 design variables were used to
evaluate the suggested methodology. When contrasted with
all other state-of-the-art approaches, the suggested method
performed better.
The capabilities of the technique were improved, and local
optima were avoided by using a new variation of the GWO
that was suggested in [146]. In order to overcome issues
VOLUME 4, 2016
15
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 16 -->
## Page 16

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
with global optimization, the proposed approach was cre-
ated. Three popular engineering challenges were employed
together with 23 commonly used benchmark test functions to
evaluate the strategy. It turns out that the suggested algorithm
is both highly competitive and frequently superior.
Le et al. [147] suggested an improved GWO to overcome
the learning rate determination issue in the multilayer type-
2 asymmetric fuzzy controller. Two phases were suggested
for improving the GWO: remembering the swarm’s optimal
location and enhancing the ability of the agents to search.
When compared to alternative ways, the suggested solution
demonstrated superior effectiveness in managing the issue
and maximizing its goal.
In order to improve the convergence behavior of the classic
GWO, Guo et al. [148] presented a new GWO edition by
mixing its elements along with the nonlinear tangent trigono-
metric function. By changing its settings to remedy the power
point tracking issue, the suggested solution was put to the
test. The suggested approach, along with other widely used
optimization techniques, has been compared with the results
of the experiment. In most instances, the suggested technique
produced superior outcomes compared to the comparative
methods.
Guo et al. [149] used both tracking and searching tech-
niques to improve preliminary GWO optimization efficiency,
broaden the population, and keep the ratio of exploration to
exploitation in check. Using test functions and traditional
engineering issues, the suggested technique was evaluated.
A sizable amount of comparative research was carried out to
demonstrate the offered approaches’ reliable performance. In
terms of issue optimization, the outcomes achieved exceeded
all examined strategies.
Wang and Xie [150] used an improved edition of the GWO
to solve the deployment issue for wireless sensor networks. It
was suggested that the GWO be improved in order to increase
the population’s capacity for exploitation and exploration.
The first component is for encircling the outside layer, while
the second part is for encircling the internal layer. Employing
popular test functions, the suggested technique was evalu-
ated. The outcomes demonstrated the great performance of
the suggested approach.
In order to effectively solve global optimization issues,
Seyyedabbasi et al. [151] proposed two updated variants of
the GWO. In the initial update, a larger version of the GWO’s
model was used to increase the number of search agents in
charge of the searching process. The second change enhanced
the position updating strategies and raised the standard of
the answers by using an incremental framework. 33 test
functions were utilized to assess the suggested technique in
the evaluation findings. The outcomes demonstrated that the
suggested strategy outperformed all other strategies that were
examined.
To improve the GWO’s ability to search and find superior
options for global functions, a multi-strategy ensemble GWO
was suggested [152]. The suggested approach was presented
in three steps: enhance global-best solutions to improve local
search capabilities; employ adaptable cooperative tactics to
boost population variation and global search capabilities;
and implement dispersed foraging methods to equalize ex-
ploitation and exploration. The suggested technique evalu-
ated well-known functions against various optimization tech-
niques. The suggested approach produced the best outcomes
when compared to all other methods.
By suggesting an integer-encoding GWO approach, Xing
et al. [153] improve the simulated network function location
optimization issue. The integer encoding strategy and a novel
updating mechanism for the wolves in the search space are
used in the suggested method to highlight exploitation and
exploration skills and achieve the optimal balance. Twenty
test examples were used to evaluate the performance of the
suggested technique. The outcomes were contrasted with
those of other cutting-edge techniques. The results demon-
strated the outstanding efficacy of the suggested approach.
To increase the classification performance and resilience
of the probabilistic neural network, an upgraded GWO was
put out in [154]. The suggested approach was put forth to
enhance the GWO’s convergence and exploration capabili-
ties. When compared to other ways, the suggested strategy
performed well in the assessment findings for optimizing the
issue and finding the best answers.
By adopting an entirely improved variation on GWO, the
disassembly sequence planning issue was handled by Xie et
al[155]. Three coefficients, the viable solution generator, the
neighborhood search operator, and the directed search coef-
ficient, were included in the suggested technique to verify
the viability of the solutions. On the basis of two engineer-
ing situations, the suggested technique was evaluated. The
outcomes demonstrated the great efficiency of the suggested
approach to solving the issue.
Yang et al. [156] used an upgraded GWO to optimize
an energy-aware approach, ensuring the precision of the
discovered solution. The suggested approach was put forward
to improve exploration and exploitation skills and preserve
equilibrium. To assess its effectiveness, the effectiveness of
the suggested approach has been contrasted with a number
of cutting-edge techniques. The suggested approach outper-
formed every strategy that was compared.
In order to effectively optimize the gene picking issue,
Alomari et al. [157] proposed a new, improved GWO version.
The TRIZ-inventive approach’s components were used to
introduce the suggested improvement in order to broaden
the population’s variety and raise the caliber of the answers.
During the assessment stage, nine popular datasets were
used to evaluate the proposed technique. Seven cutting-edge
approaches were examined, and their effectiveness was con-
trasted to that of the suggested approach. In terms of achiev-
ing the ideal answer, the suggested technique outperformed
the comparative method.
The fuzzy technique [158] helped the GWO better balance
convergence and variation in populations. In order to high-
light local and global optimization, mutation and crossover
operators were also modified for the suggested approach.
16
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 17 -->
## Page 17

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
Five technical optimization tasks and CEC-2014 were used to
assess the performance of the suggested technique. Addition-
ally, the outcomes of the suggested strategy were evaluated
against a number of popular optimization techniques. When
compared to various optimization techniques, the suggested
strategy produced the best outcomes.
To increase the GWO population variety and convergence
to ideal agents, the Cross-Dimensional Coordination GWO
was suggested in [159]. The best answer is updated using all
previous best information acquired by honest agents in the
suggested approach, which employs a revolutionary learning
mechanism. CEC06-2019 and 12 engineering issues were
used in the assessment step to assess the effectiveness of
the suggested strategy. The proposed strategy was also con-
trasted with a number of cutting-edge techniques. Most of the
compared approaches were outperformed by the suggested
strategy.
A
strengthened
exploitation
and
exploration
GWO
(REEGWO) was proposed by Yu et al. [160]. By giving
the highest three wolves varying weights based on their
understanding of the position of the prey, the methodology is
changed. Also used to enhance method exploration is tourna-
ment choice. The data collected demonstrates that REEGWO
performs better than the other four new GWO versions. The
suggested method also performs better than other heuristic
algorithms.
The grey wolf optimizer was created by Nadimi-Shahraki
et al. [161] using a gaze cues learning framework. The
suggested method uses neighbor gaze cues learning (NGCL)
and random gaze cues learning (RGCL) to lessen the GWO
algorithm’s strong selection pressure and heterogeneity. The
method is assessed using two optimum power flow issues,
four genuine engineering layout issues, and the CEC’18
test functions. The suggested approach outperformed nine
metaheuristic methods in the evaluation.
The Parallel Cooperative Coevolutionary Grey Wolf Op-
timizer (PCCGWO) was introduced by Jarray et al. [162]
to address the issue of route design for unmanned aerial
vehicles (UAVs). The suggested method uses several smaller-
dimensional subspaces. In order to search for an agent in
a portion of the search area, it produces several swarms
from the initial population. Then, to shorten the calculation
time needed to address the issue, a parallel master-slave
architecture is employed. The outcomes demonstrate the
suggested algorithm’s effectiveness in terms of output and
nonparametric statistical findings.
B. HYBRIDIZED VERSIONS OF GREY WOLF OPTIMIZER
Another improvement technique utilized for the GWO is
hybridization. Such an approach is proposed by combin-
ing the GWO with components from another optimization
method. Several studies utilized the hybridization approach,
which is summarized below.
1) Local Search with Grey Wolf Optimizer
Makhadmeh et al. [163] introduced a novel hybrid GWO
with an efficient local search method to enhance its exploita-
tion capabilities and avoid local search stagnation, thus, im-
proving its searchability. The utilized local search method for
the GWO is called the min-conflict algorithm. Furthermore,
the proposed method was formulated as a multi-objective
optimization method to address optimization problems with
multiple objectives. The proposed method was tested and
evaluated using a well-known multi-objective engineering
optimization problem called the power scheduling problem
in a smart home. The performance of the method was in-
vestigated through several scenarios. The acquired results
presented the performance of the proposed method, where
it exceeded almost all other methods.
Guo et al. [164] integrated the simulated annealing and
a stochastic simulation approach with multi-objective GWO
for line balancing scheduling in disassembling numerous
products. Three conflicting objectives were considered by
the proposed method, where objectives are: maximizing the
minimizing energy consumption and disassembly profit and
minimizing carbon emission. The method’s performance was
evaluated using real-world datasets. Simulation outcomes
demonstrated the proposed method’s efficiency against three
other multi-objective methods.
Hoballah et al. [165] used hybrid GWO to develop a code
matrix depending on dissolved gas percentages for reliable
defect identification while accounting for measurement er-
rors. The criteria that map the boundaries of gas ratios for
various fault kinds were created using a fuzzy approach. Each
percentile range of gas was separated into three zones, each
with three fuzzy memberships. After that, a fuzzy system is
created to link the gas percentages to the fault category. Thus
order to improve the accuracy, the membership limitations
were then optimized via heuristic techniques. The suggested
code reduces the effect of measurement errors on output fault
diagnostics. The proposed approach demonstrated its ease of
use in diagnosing transformer faults and its reliability against
error margins.
El-Kenawy et al. [166] developed a modified binary GWO
depending on the stochastic fractal search to discover the
important characteristics by attaining search locally and
globally and make a balance between them. To begin, the
proposed GWO was created by using an exponential form
of the iterations number of the original GWO to expand the
search area for global search and crossover/mutation oper-
ations to boost population variety and improve local search
capabilities. Then, the Gaussian distribution approach was
utilized for walk randomly in a growth process; the stochastic
fractal search diffusion procedure was used to find the best
solution for the modified GWO. The proposed method’s
continuous values are then transformed into binary values to
deal with feature selection problems. Nineteen UCI datasets
were examined to ensure the stability and effectiveness of
the proposed method. For classification tasks, the K-Nearest
Neighbor method was used to assess the quality of a sub-
VOLUME 4, 2016
17
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 18 -->
## Page 18

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
set of characteristics. The results showed that the proposed
method beat binary versions of state-of-the-art optimization
techniques.
Helmi et al. [167] introduced a new lightweight feature
selection approach. The GWO was hybridized with the
gradient-based optimizer to address such an optimization
problem. The support vector machine was employed to iden-
tify the features selected by the proposed method. Extensive
tests were done to examine the proposed method’s perfor-
mance. Overall, the obtained results from the method proved
its high performance.
Al-Betar et al. [168] increased the convergence qualities of
the GWO by hybridizing it with the hill-climbing optimizer.
GWO is quite effective in a broad search, but hill-climbing
is highly effective in a deep search. The balance between ex-
ploration and exploitation is properly managed by integrating
wide and deep search capabilities in a single optimization
framework. The suggested hybrid algorithm was assessed
utilizing five distinct test cases. The proposed method was
assessed utilizing 49 different comparison methods. In most
test instances, the results the proposed method gained surpass
those others obtained.
Sun et al. [169] used the GWO and gradient algorithm
to present a sub-pixel displacement measuring approach.
The correlation between the reference image and distorted
image subsets was first investigated using the zero-mean nor-
malization cross-correlation function. Second, the beginning
integer pixel value was acquired and is seen as the initial
displacement by utilizing the GWO global searching capa-
bility. Finally, a Barron gradient method was used to acquire
the final sub-pixel displacement. The presented approach can
successfully assess the deformation and displacement of rigid
structures compared to the state-of-the-arts using synthetic
speckle pictures.
Qin et al. [170] reduced total delivery delay and production
cost using a multi-objective casting production scheduling
framework. In this method model, a hybridization discrete
multi-objective GWO is proposed. To improve the quality
of the initial population, an initialization method focused
on minimizing work transit time and process time was de-
veloped. To avoid the GWO’s premature convergence, an
improved tabu search method was combined with the GWO.
To evaluate the effectiveness of the proposed method, a
case study of a genuine foundry enterprise was presented.
Experimental findings showed that the suggested method out-
performed five other multi-objective algorithms in terms of
classification accuracy. The implementation of the proposed
scheduling model was verified utilizing a real-world testing
system.
Xu et al. [171] suggested a novel hybrid GWO with local
search to tackle engineering problems. The presented method
was introduced to improve the local search strategy of the
GWO. The experimental results showed that the presented
approach could handle the problem more efficiently and with
relatively high solutions.
The authors in [172] introduced another hybrid GWO
algorithm for disassembly sequencing and line-balancing
scheduling problem. In their hybrid algorithm, the simulated
annealing is injected within the framework of the GWO to
improve its performance and balance the exploration and
exploitation abilities. The simulation results displayed the
significance of the hybrid method in terms of solution quality
and computational time.
Alomari et al. [173] use the GWO and combine it with the
Triz operator as a wrapper approach to address the problem of
text classification by hybridizing the filter-wrapper technique
based Principal Component Analysis to develop a filter to
choose an informative and suitable subset of traits, which
in turn decreases the data dimensionality. The experiment
employs three datasets of Arabic-language text to evaluate
the proposed method’s performance. The findings confirm
the proposed method’s efficiency in terms of classification
accuracy.
2) Swarm Intelligence with Grey Wolf Optimizer
The GWO can be hybridized with swarm intelligence
methods to enhance its capabilities in addressing complex,
multi-objective, and large-scale search spaces. The integra-
tion of two or more meta-heuristics forms a synergy that is
needed to enhance the capabilities of the search algorithm.
Some of these algorithms are more exploitation-oriented, and
others are more exploration-oriented. Some are more appro-
priate for binary search spaces or mixed-integer optimization.
Hybridized techniques can be considered to avoid stagnation
in local optima or speed up convergence. When mixing two
or more hybridization algorithms, more richness and versatil-
ity in solutions can be discovered. The following papers show
examples of using swarm intelligence with GWO in solving
complex optimization problems.
Goudos et al. [174] addressed antenna design and fab-
rication problems for the 5G mobile devices proposing a
new hybrid optimization method based on the GWO and the
components of the Jaya optimizer. In the proposed method,
the components and features of the two algorithms were
combined to emphasize exploration and exploitation with
maintaining the balance between them. The proposed ap-
proach was evaluated using different well-known benchmark
functions. The proposed method showed better performance
in addressing the problem than the compared methods.
Another hybrid approach on the basis of the GWO com-
ponents and symbiotic organisms search was introduced by
Qu et al. [175] to handle the same problem. The symbiotic
organism’s search was utilized to improve the exploitation
abilities and the convergence rate of the original GWO,
thus, finding better solutions. The achieved outcomes by the
proposed approach were compared with that achieved by the
GWO, symbiotic organisms search, and simulated annealing
algorithms. The proposed approach exceeded all compared
approaches in handling the problem.
Al-Wajih et al. [176] proposed a new binary GWO and
harris hawks optimization mimetic approach to solving the
optimum feature selection problem. The proposed method
18
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 19 -->
## Page 19

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
provided a balance between exploration and exploitation and
used sigmoid transfer functions to convert the continuous
values of search space into binary. The testing was done
on 18 standard UCI problems, and the results were com-
pared with other comparable binary optimization methods.
The proposed method showed more accuracy and lowered
computational cost than the other techniques.
A hybrid crow search algorithm with GWO was proposed
by Rizk-Allah et al. [177] to solve large-scale optimization
problems. The GWO operates more on exploration, while
the crow search algorithm focuses more on local search. The
proposed method was introduced to avoid getting stuck in
local minima and achieve fast convergence. A dynamic fuzzy
learning mechanism was used to search for the best solution
areas. The method was tested using 15 CEC 2015 benchmark
suites and four large-scale engineering problems. Compar-
isons with competitive techniques proved the effectiveness
of the proposed method.
Chen et al. [178] used the hybridization of chaotic GWO
with the dragonfly algorithm to solve the complex and highly
nonlinear problem of short-term hydrothermal scheduling.
The GWO can provide local solutions, while the dragonfly
algorithm is more into global solutions with premature con-
vergence. The combination of the two algorithms provided
a more capable technique. Three systems were used for
testing and compared to the outcomes of other methods. The
new method showed superiority over the other techniques in
obtaining better scheduling schemes.
The hybrid of the GWO with the Cuckoo search algorithm
was proposed by Mouhou and Badr [179] to find a low-
order model with a good fit for the ideal transfer function
applied to fractional order functions. Comparisons are made
between the two techniques. Different numerical examples
were used. The results confirmed the effectiveness of the
proposed method compared to the other methods.
A nonlinear PI controller of a voltage source converter for
an HVDC offshore system was optimized by Mahmoud et al.
[180]. A hybrid version of the GWO and the cuckoo search
algorithm was utilized in obtaining the controller parameters.
The performance of the controller was tested in dynamic
and transient conditions. Real wind speed patterns were used
in the evaluation stage. The proposed method outperformed
results obtained by other competitive methods, especially
during different faults.
A new hybrid approach based on GWO and cuckoo search
algorithm was proposed to extract PV cell parameters by
Long et al. [181]. The proposed method used a learning
strategy that utilizes opposition learning to maintain diversity
in the population. The introduced approach provided a great
balance between exploration and exploitation search. The
introduced approach was experimented on ten benchmark
test functions and then applied to PV models under different
conditions. Results showed a promising approach for the PV
cell parameters extraction.
Karakoyun et al. [182] proposed a GWO hybridized with
the shuffled frog leaping algorithm. Some modifications were
also applied to the proposed method to enhance its perfor-
mance based on the cases handled. The proposed method
was tested on 36 benchmark problems. Four comparison
metrics were used for comparisons in addition to several
statistical tests. The results were competitive and better than
the existing methods.
A hybrid between the sine-cosine search algorithm and the
GWO was proposed by Gupta et al. [183]. The goal was to
strike a balance between exploitation and exploration, as the
two algorithms vary in nature and search mechanism. The
GWO has social and collective behaviour that helps in reach-
ing un-visited areas in the search space. The hybridization of
both algorithms offers a synergy between the two algorithms
resulting in additional positive characteristics. Testing was
done on large dimension problems with sizes 30-100 in
addition to a set of benchmark engineering problems. Results
proved the superiority of the proposed method over other
methods.
The authors in [184] integrated two swarm-baed algo-
rithms, called HGEOGWO, for 3D path scheduling of mul-
tiple unmanned aerial vehicles in power inspection. The
learning strategy is combined with the golden eagle opti-
mizer, PELGEO, to enhance the search process capability
and avoid trapping in local optima. Next, the GWO algorithm
is combined with the differential mutation strategy, called
DMSGWO, to empower its exploration ability. Finally, the
HGEOGWO and PELGEO are integrated using an adaptive
hybridization strategy to take advantage of the two algo-
rithms. The performance of the HGEOGWO is tested using
CEC 2013 test functions and compared to other comparative
methods used to solve the same problems. The numerical
results illustrated the power of the HGEOGWO in terms of
solution quality and stability of the algorithm. Furthermore,
the HGEOGWO is applied to solve 3D path planning of
multiple unmanned aerial vehicles in power inspection with
satisfactory results.
Makhadmeh et al. [185] proposed a grey wolf optimizer
hybridized with a multi-verse optimizer (MVO) to solve the
problem of the power scheduling. The new method is called
MVOG. The technique updates the worst solution generated
by MVO using the GWO. The technique is applied to the
other four optimization methods. The results show that the
MVOG outperformed the compared state-of-the-art methods.
3) Evolutionary Algorithms with Grey Wolf Optimizer
Saxena et al. [186] combined the components of the
evolutionary algorithm, including the selection operator and
crossover and mutation operation, and the GWO search
agents to efficiently update the positions of the search agents
and balance global and local search; thus, finding better
solutions. The introduced method performance was validated
using benchmarked functions and real-world optimization
problems. The suggested strategy exhibited and achieved
more satisfactory outcomes than the compared method.
Similarly, the authors in [187] integrated the deep learning
convolutional neural networks with the enhanced version of
VOLUME 4, 2016
19
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 20 -->
## Page 20

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
GWO, called EGWO-GA, for early COVID-19 discovery by
precise diagnosis. In EGWO-GA, the operators of the genetic
algorithm, including crossover and mutation, were integrated
within the framework of the GWO to improve the population
variety and exploitation ability. The EGWO-GA was evalu-
ated using two benchmark CXR image datasets. The simula-
tion outcomes dementated the usefulness and robustness of
the EGWO-GA against other comparative algorithms.
Wang and Li [188] presented a hybrid GWO with differen-
tial evolution to prove a good global and local search balance,
speed up convergence, and enhance GWO’s accuracy. The
proposed method was proposed for featuring evolution and
elimination mechanisms. In the simulation tests, the results
were carried out using 12 common benchmark functions.
The results of the experiments revealed that the proposed
method had a faster convergence rate and higher optimization
accuracy.
Tawhid and Ibrahim [189] developed a novel technique for
solving systems of complicated nonlinear equations utilizing
a hybridization method that combined the GWO with differ-
ential evolution. A new improved encircling and crossover
approaches are applied. The introduced approach perfor-
mance was estimated using numerical experiments involving
13 optimization problems across 100 dimensions and seven
benchmark equations. Empirical results revealed that the
suggested approach beat competing approaches throughout
the literature by finding the best candidate solutions for
most nonlinear equation systems and optimization problems,
demonstrating its efficiency in contrast to other methods.
Davahli et al. [190] presented an IoT intrusion detection
system with great performance for resource-constrained IoT
wireless networks. The genetic algorithm and the GWO were
combined to address such a problem. The testing findings
showed that the proposed method has the best performance
compared to all compared methods.
Lei and Ouyang [191] introduced a kernel-based fuzzy
clustering strategy combining an upgraded GWO with a
kernel-based intuitionistic fuzzy C-means clustering method
competent for image segmentation differential mutations.
The hybrid approach was examined based on a comparison
study. The proposed method exceeded all methods in han-
dling the problem.
Mohsin et al. [192] proposed a hybrid optimization tech-
nique based on differential evolution and GWO. In terms of
balancing exploration and exploitation, the proposed method
outperformed the compared versions.
Bouzary and Frank Chen [193] presented a novel hybrid
strategy based on the genetic algorithm’s evolutionary oper-
ators and GWO. The incorporated crossover and mutation
operators serve two purposes. Several tests were devised
and carried out to illustrate the efficiency of the suggested
algorithm, and the results showed that the new algorithm
outperformed both the current discrete varieties of GWO and
the genetic algorithm.
A new GWO version was proposed in [194] to explore
and search deeply in the search space and efficiently address
the job shop scheduling problem. The method was proposed
utilizing four crossover operators and a local search strat-
egy. The presented approach was tested using 69 famous
benchmarks and compared with six approaches. The acquired
results confirmed the approach’s high performance compared
to the compared methods.
The GWO was hybridized with the genetic algorithm in
[195] to enhance the exploration and exploitation capabilities
of the GWO to track the global peak for the energy sector
problem. The introduced approach was tested and assessed
by comparing its GWO and genetic algorithm performance.
The approach achieved better results than the compared
approaches.
4) Other Grey Wolf Optimizer hybridization
Chen et al. [196] developed a novel method that applies
support vector regression and GWO address the proton life
problem. The support vector regression is utilized to develop
the degradation model. While the GWO is utilized to tune
the hyperparameters of support vector regression to have a
better prediction using the model. The proposed method is
able to predict fuel cell degradation with a low mean absolute
percentage error when compared to other methods.
Yang et al. [197] developed GWO-feature weighted-
multiple kernel-support vector regression to forecast Full-
face tunnel boring machine penetration rate. A tunnel in
China is chosen to evaluate the algorithm’s performance. The
introduced approach is compared against three other models.
The obtained results showed that the new hybrid model is
producing accurate prediction results.
Zamfirache et al.[198] propose the GWO in combination
with a reinforcement learning (RL)-based control approach
to train the neural networks using policy iteration. This
method is contrasted with the traditional PI RL-based control
method that employs gradient descent and RL-based control
methods as well as the particle swarm optimization algo-
rithm. The analyses are carried out with the use of nonlin-
ear servo scheme laboratory apparatus, and each strategy is
assessed according to how effectively it handles the best ref-
erence following supervision for an empirical servo scheme
location control mechanism. According to the experimental
findings, the GWO algorithm provides a superior solution to
the control objective taken into account in this work when
compared to the GD and PSO algorithms.
Shariati et al. [199] combine extreme learning machine
and GWO to develop a new hybrid ELM-GWO model for
estimating concrete compressive strength parameters. The
introduced approach was compared with several approaches,
including support vector regression with radial basis func-
tion, adaptive neuro-fuzzy inference system, extreme learn-
ing machine, SVR with a polynomial kernel, and artificial
neural network. Findings show that incorporating the ELM
model into GWO may effectively enhance this model’s per-
formance, and it is inferred that the ELM-GWO model can
achieve higher performance indices than other methods.
20
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 21 -->
## Page 21

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
C. MULTIOBJECTIVE VERSIONS OF GREY WOLF
OPTIMIZATION
Multi-objective Optimization Problems (MOPs) optimize
problems that have multiple objectives [200]. Most engi-
neering problems and real-world applications are considered
to be multi-objective. Usually, these multiple objectives are
conflicting. For example, when solving the assembly line
problem one of the goals can be maximizing production and
minimizing power consumption. Hence, one objective opti-
mal solution may not produce other objectives’ best solution
[201].
Design space exploration procedure during architectural
synthesis has two conflicting objectives power performance
and the occupied area by resources. GWO is used to tackle
this multi-objective problem [202]. Utility coefficients and
utility ranking techniques are introduced to develop a unique
solution. The results showed that the proposed algorithm has
a better exploration and less exploration time when compared
to other comparative methods on the evaluated datasets.
Multi-objective GWO (MOGWO) was developed by Dash
et al. [203] for effective speech enhancement. The best set
of values for different noise levels to increase the quality of
speech is selected. The noisy speech was then categorized
into four levels using predefined audio features. These values
were then used to enhance an unknown noisy speech signal.
The algorithm was evaluated on two speech datasets, and
the results showed the superiority of the proposed technique
compared to other comparative methods.
Li et al. [204] proposed a MOGWO for solving multi-
objective complementary scheduling of hydro-thermal-RE
power systems. The proposed method was utilized with real
and integral variables. The proposed algorithm was tested
using a hybrid system consisting of cascade hydropower
stations, thermal power units, and renewable energy power
plants with superior results against the other competitors.
A MOGWO with the Lévy technique was developed by
Mahmoud et al. [205] to solve the voltage rise/drop by
controlling the optimal voltage in distribution systems. The
number of tap movements of transformers and the PV units’
active power curtailment was considered when developing
the solution. The proposed method was evaluated using 24-h
simulation with different load types and with a 119-bus PV
distribution system. The results demonstrated the efficiency
of the proposed solution when compared with three other op-
timizers in terms of curtailed power of PV and tap movement
rate of transformers.
The single document text summarization problem was
tackled using a multi-objective framework that utilizes
multi-objective differential evolution, MOGWO, and multi-
objective water cycle algorithm [206]. The document sen-
tences were clustered, then using the proposed multi-
objective, the solution fitness was measured using the two
conflicting objective compactness and separation of the sen-
tence clusters. After that, a scoring feature was used to
develop the summary. Two datasets were used to evaluate the
proposed method. The comparison against other comparative
methods showed the competitiveness of the proposed tech-
nique.
A MOGWO that utilized k-Nearest Neighbor was pro-
posed to classify power quality disturbances by 2D-Riesz
transform by Karasu and Saraç [207]. The power quality dis-
turbances events are collected. Then the 1D signals are trans-
formed into 2D signals to develop the 2D-Riesz transform.
A set of statistical and image-based features was determined.
The evaluation with multiple events and noisy data showed
that the proposed method produced efficient results when
compared to other comparative methods.
A MOGWO based on decomposition was proposed by
Zapotecas-Martinez et al. [208]. It estimated the Pareto
solutions cooperatively by determining the neighbourhood
relation between the scalarizing sub-problems. The proposed
algorithm was evaluated using two real engineering problems
and a set of well-known benchmark problems. The obtained
results showed the superiority of the proposed method when
compared to six comparative bio-inspired methods.
The optimal mapping of cloud tasks to the set of resources
is called the task schedule problem. This problem was tackled
by Alsadie [209] using a MOGWO by satisfying high com-
puting and storage requirements while reducing makespan
and resource utilization. The GoCJ, HCSP, and Synthetic
datasets were used to evaluate the proposed algorithm. The
obtained results showed that the proposed algorithm outper-
formed the other comparative methods.
The generated power by the PV array is highly affected
by the shadow phenomenon. A MOGWO was proposed by
Yousri et al. [210] to reconfigure the shaded PV array opti-
mally. The objective is to reduce the row current difference
and increase the output power. The proposed solution was
validated using six shade patterns 9-9 PV array. The obtained
results revealed the efficiency of the proposed algorithm.
The voltage quality problem requires the pulse width mod-
ulation to utilize the scission-style harmonic elimination to
enhance the voltage quality of the asymmetrical multi-level
inverter. The MOGWO was developed by Darvish Falehi
[211] to solve this problem. It was then compared against the
non-dominated sorting genetic algorithm II. The experimen-
tal results showed the effectiveness of the proposed algorithm
in solving this problem as it optimized the ameliorated volt-
age quality of the odd-nary multi-level structure.
Thresholding was utilized as a MOP by using the Otsu and
Kapur techniques by Karakoyun et al. [212]. The goal is to
develop a better image segmentation algorithm. A discrete
MOGWO to tackle multi-level thresholding segmentation
was proposed. The obtained results showed the superiority
of the proposed algorithm when compared with other com-
parative methods.
The flexible job shop scheduling problem with job prece-
dence constraints was tackled by Zhu and Zhou [213] using a
MOGWO that utilized a mixed-integer programming math-
ematical model. A repair technique using a binary tree was
applied to fix the job precedence constraint. The proposed
algorithm was evaluated on well-known test instances. The
VOLUME 4, 2016
21
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 22 -->
## Page 22

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
evaluation results showed the efficiency of the proposed
algorithm when compared to other techniques in terms of
diversity metrics, cardinality, and convergence.
The problem of multi-objective service composition and
optimal selection in cloud manufacturing was tackled in
[214] by developing an enhanced MOGWO. The proposed
technique used backward learning to improve the exploration
capabilities of the algorithm. After that, a nonlinear adjust-
ment strategy was used to improve the algorithm’s global
exploration. The proposed algorithm was compared against
other comparative algorithms using a set of benchmark prob-
lems. The results proved the proposed method’s performance
in outperforming other comparative techniques.
In order to overcome information overload and browse
answers more efficiently, it is vital to provide a set of core
answers which cover most topics questioned. Li et al. [215]
proposed a MOGWO to solve this problem. It started by
using the bi-term topic model for texts of different sizes.
After that, the core answers coverage, quality, number, and
redundancy were defined. The algorithm was then used to
get a predefined number of core answers. Real datasets were
used to evaluate the proposed algorithm. The results showed
the feasibility of the proposed algorithm.
The problem of maximizing the transmission in microwave
power transmission applications requires another conflicting
objective which was reducing the peak radiation level. A
MOGWO was proposed in [216] to tackle this problem. The
algorithm generated a new antenna design that satisfies the
problem constraints. The proposed algorithm was evaluated
on continuous aperture with different Fresnel parameters,
space solar power satellite models, and array antennas. The
obtained results showed the feasibility of the proposed algo-
rithm.
To improve the transmission capacity of fiber optics, the
optimal design of orbital angular momentum of light was
proposed using the MOGWO [217]. The goal is to identify
the optimal fiber cross-section refractive index profile. The
proposed algorithm was compared against single-objective
GWO. The results showed the proposed algorithm’s effec-
tiveness in producing 20 OAM modes supportive of optimal
designs.
Predicting an offshore wind farm’s short-term wind power
using a two-stage hybrid model was proposed by Lu et al.
[218]. The ensemble empirical mode decomposition with
adaptive noise was utilized to make smoother raw data. Then,
to ensure prediction stability and accuracy, a MOGWO was
used to optimize the kernel-based nonlinear extension of the
Arps decline model. The offshore wind farms in Belgium his-
torical data were used to evaluate the proposed method. The
results showed that the multi-objective optimizer improves
the prediction performance.
The problem of choosing a set of requirements to develop
in the next release of the software was tackled by Ghasemi et
al. [219] using MOGWO and whale optimization algorithm.
To satisfy the problem constraints, the cost-to-score ratio and
the roulette wheel techniques are applied. The MOGWO,
whale optimization algorithm, and other three evolutionary
algorithms were used to solve such a problem. The proposed
algorithms were evaluated using four datasets. The results
showed the high performance of the proposed methods in
addressing such a MOP.
The assembly line balancing considering preventive main-
tenance of machines problem was solved in [137] using an
enhanced MOGWO. The algorithm applies variable step-
size decoding mechanisms and tailored specific neighbour
operators to improve the algorithm convergence. The pro-
posed algorithm was compared against three other variants
and six evolutionary algorithms. The obtained results showed
that the proposed algorithm outperformed other comparative
methods.
A novel MOGWO that applied the search strategies:
boundary mutation strategy, sorting and crowding distance-
based elitism strategy, and adaptive chaotic mutation strategy
was proposed by Liu et al. [220]. The algorithm utilized a
fixed-sized external archive to maintain the discovered non-
dominated solutions. The proposed algorithm was evaluated
on a set of well-known MOPs. The experimental results
with other comparative multi-objective optimization algo-
rithms showed the efficiency of the proposed algorithm.
The algorithm was then evaluated on the multi-objective
real-world scheduling problem of the cascade hydropower
stations problem. The proposed algorithm produced good
quality solutions, and it is a competitive method compared
to other comparable methods.
The resource allocation problem was addressed by Kishor
and Niyog [221] considering multiobjective function con-
taining optimizing response time and imbalance between
resources. A modified GWO was proposed based on the con-
cept of the best response approach to increase the searching
capabilities of the GWO. In addition, the GWO was modeled
as a MOGWO to deal with the two objectives of the problem.
The experimental results proved the high performance of the
proposed method in optimizing the two objectives compared
with the other methods.
The MOGWO was adapted and hybridized in [222] to
enhance its optimization performance in addressing an enter-
prise service composition problem. The proposed hybridiza-
tion was introduced on the bases of the components of
evolutionary optimization, including crossover and mutation.
The experiments were conducted in different stages and
comparisons. The proposed hybrid MOGWO showed its high
performance in addressing the problem by outperforming all
compared multi-objective methods.
An improved MOGWO version was proposed in [223]
to address the multi-objective energy scheduling problem
in smart homes and optimize four objectives together. The
proposed method was introduced on the basis of the neigh-
bourhood selection strategy to emphasize the exploitation
capabilities. The proposed method was tested using 30 differ-
ent smart home scenarios and compared with different well-
known optimization methods in several stages. The proposed
method proved its robust performance compared to the other
22
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 23 -->
## Page 23

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
methods.
Cao et al. [224] developed a nondominated-sorting grey
wolf optimizer algorithm (NSGWO) to solve the multiobjec-
tive problem of load dispatch of coal-fired power plants. The
proposed technique applies a reference-point selection and a
simulated binary crossover. The proposed algorithm outper-
forms other techniques in terms of economy, environmental
protection, and speediness.
Yin and Sun [225] proposed distributed multi-objective
grey wolf optimizer to solve economic dispatch optimization.
The technique solves the optimization of large-scale multi-
area interconnected power systems by sharing bus informa-
tion between areas. The algorithm is evaluated using IEEE
39-bus and 118-bus systems. The obtained results show that
the proposed algorithm outperforms other centralized opti-
mization techniques with a better performance.
V. APPLICATIONS OF GREY WOLF OPTIMIZER
The effectiveness of GWO and its variants enables it to
successfully tackle a wide range of real-world applications.
This include electrical and electronic engineering [147],
[148], [185], renewable energy [226], [181], [195], network-
ing and communication [214], [186], mechanical engineering
[220], [130], medical applications [227], [67], classifica-
tion [228], [157], [229], [173], [85], chemical engineering
[230], [231], petroleum engineering [129], [215], industrial
engineering [232], [219], software engineering [65], civil
engineering [233], [234], geotechnical & geoenvironmental
Engineering [235], [236], planing & scheduling [170], [110],
robotics [237], [127], image processing [238], [239], [240],
and mathematical functions [123], [241], and others [242],
[243], [244].
Table 1 presents the applications of the GWO and its
variations. The applications are categorized according to the
domain, the problem name, the GWO variant (i.e., original,
modified, hybrid, and multi-objective), and the dataset used.
A summary of some of the main applications tackled
by the GWO and its variations is demonstrated next. Elec-
trical and electronic engineering problems are solved by
variations of the GWO. This includes developing a new
controller [147], maximize power point tracking for PV
system [148], optimal charging pattern of Li-ion batteries
[110], [245], optimizing electrical power system with dis-
tributed power generating stations [76], [246], [247], [163],
[248], fractional-order proportional-integral controller [249],
optimal placement of Distributed Generation (DG) units in
radial distribution system [250], and economic load dispatch
problem [168], [141].
The renewable energy optimization problem is tackled by
GWO and its modifications. The following are some of these
applications predicting solar diffuse fraction [226], param-
eter extraction of solar photovoltaic models [181], [195],
prediction of offshore wind farm power [218], estimating
photovoltaic solar cell model [121], parameter extraction of
photovoltaic cells and modules [251], and optimal configura-
tion of photovoltaic power plant [252], [253].
The networking and communication domain is another
area that has been tackled by GWO and its variations, in-
cluding service composition in cloud manufacturing [214],
virtual network function placement [153], wireless sensor
network coverage optimization [125], energy-efficient load
balancing [254], energy-efficient routing in wireless sensor
networks [255], antenna aperture illuminations [216], design
optimization of orbital angular momentum fibers [217], and
optimize the enterprise service composition problem [222].
Mechanical engineering has optimization problems of di-
verse types, which are solved using GWO, such as the opti-
mal operation of cascade hydropower stations [220], trans-
former fault diagnosis [154], predictive torque control for
electric buses [256], design of highly uniform magnetic field
cylinder coils in atomic sensors [257], and fault diagnosis of
rolling bearing [258].
Medical applications are another domain that utilizes the
GWO. This includes applying the algorithm to solve com-
pressive sensing MRI reconstruction [227], predicting di-
abetes complications [67], COVID-19 pandemic modeling
and prediction [101], and breast cancer classification [259],
[173].
Classification is an important machine learning problem
that is applied to solve several real-world problems such
as extractive single document summarization [228], gene
selection [157], feature selection [83], [152], [118], [166],
[74], [73], [99], [84], Arabic text classification [80], and
classification of power quality disturbances [207]. On the
other hand, the integration between the GWO and machine
learning techniques was applied to the forecasting domain
such as streamflow forecasting [260], [261], short-term load
forecasting [262], and navigation technology [263].
Similarly, the GWO is investigated for tackling chemical
engineering problems like modeling and optimization of lead
and cobalt biosorption from water with Rafsanjan pista-
chio shell [230], and reference evapotranspiration estimating
[231]. Furthermore, the GWO was successfully utilized for
solving problems in the petroleum industry, such as forecast-
ing the natural gas and coal consumption in Chongqing China
[129], prediction for the favorable reservoir of oil based on
data sampled from the Niuzhuang area (China) [215], opti-
mizing cetane improver concentration in the biodiesel-diesel
blend [264], optimizing biodiesel production from abundant
waste oils [265], forecasting fuel combustion-related CO2
emissions [266], and traditional coal spontaneous combus-
tion temperature prediction [128].
The GWO is successfully adopted for various problems
from the industry domain using real-world or simulation
datasets such as assembly line balancing problem [137],
disassembly sequence planning [155], [164], bi-objective
next release problem [219], degree reduction of SG-Bezier
surfaces [232], supplier selection and order quantity allo-
cation problem [192], daily optimal operation of cascade
pumping stations [90], optimization of thermal efficiency
and unburned carbon in fly ash of coal-fired utility boiler
[267], optimal QoS-aware service composition and optimal
VOLUME 4, 2016
23
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 24 -->
## Page 24

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
selection in cloud manufacturing [193], pattern recognition
method for mixture control charts [226], enhancement of an
impulse turbine for oscillating water column [119], design of
the spur gear pairs with minimum weight [268], forecasting
of automobile sales [269], optimization of an auto drum
fashioned brake [113], multi-objective disassembly sequenc-
ing and line balancing planning in disassembling multiple
products [172], and optimal control parameters and design
of the output filter of a grid-tied three-phase inverter [270].
In the same way, the GWO-based algorithms are applied
for solving optimization problems in the civil engineering
domains, like control of the nonlinear building using an op-
timum inverse Takagi-Sugeno-Kang model of magnetorheo-
logical damper [271], predicting the compressive strength of
normal and High-Performance Concretes [233], the equip-
ment detection and localization of large-scale construction
Jobsite by far-field construction surveillance video [234],
estimation of soil moisture content using a dataset from De-
hgolan plain - Iran [68], predicting the dynamic modulus of
asphalt mixture [272], optimization of construction duration
and schedule robustness [273], and predict the compressive
strength of concrete with partial replacements for cement
[274].
Geotechnical & Geoenvironmental Engineering has di-
verse kinds of optimization problems that are tackled by
the GWO-based algorithms such as groundwater remediation
[235], predicting soil electrical conductivity [236], urban
growth simulation and optimization using dataset sampled
from Nanjing city - China [87], spatial prediction of land-
slide susceptibility using real-world dataset sampled from
Tehri Garhwal, State of Uttarakhand - India [275], and wa-
ter resources management using a real-world dataset from
Shangjingyou station and Fenhe reservoir station of Fenhe
River [276], estimates of greenhouse gas emission in Turkey
[277].
The Planning & scheduling is another area that has been
tackled by the GWO-based algorithms like casting produc-
tion scheduling problem [170], flow shop scheduling prob-
lems with multi-machine collaboration [110], [136], hybrid
flow shop scheduling problem considering noise pollution
[86], flexible job shop scheduling problem with hierarchical
job precedence constraints [213], [194], task scheduling for
cloud data centers [209], short-Term hydrothermal schedul-
ing [178], knapsack problem [81], and welding shop inverse
scheduling problem [75].
Furthermore, the GWO-based algorithms are introduced to
enhance the performance of robotics from various perspec-
tives such as the path planning for Unmanned Aerial Vehicle
(UAV) [278], [175], [114], multi-UAV Path Planning [140],
3D path planning of multiple UAVs in power inspection
[184], multi-robot exploration & Hybrid & ordinary and
complex maps [237], sliding mode control of 2-DOF robot
manipulator [127], [126].
The GWO is introduced different optimization problems
in the image processing domain like joint denoising and
unmixing of multispectral images [238], camera calibration
method [239], multi-level image thresholding [212], multi-
modal image registration [279], classification of magnetic
resonance brain images [280], image segmentation [191],
non-blind RGB watermarking [281], sub-pixel displacement
measurement [169], and key points selected to simplify the
point cloud [282].
Finally, the performance of the GWO-based algorithms
was evaluated using different benchmark test functions such
as the classical test functions [111], [183], [192], [104], CEC
2006 [139], CEC 2014 [108], [283], [122], [115], [158], CEC
2017 [123], [96], [103], [122], CEC 2018 [135], CEC 2019
[115], classical engineering problems [96], [103], [111],
[183], [122], multi-objective test functions (i.e., LZ09F,
WFG, and ZDT) [208], [182]. Other problems were tackled
by GWO like designing convolutional neural network-long
short-term memory networks for time series analysis [242],
stock selection [123], extracting core answers in community
question answering [215], and automatic speech emotion
detection [243].
VI. COMPARISON BETWEEN GREY WOLF OPTIMIZER
VARIANTS
This section discusses the effectiveness and robustness of
three GWO variants, including original, modified, and hy-
bridized. The original version is the GWO [64], the modified
is the link-based grey wolf optimizer (LBGWO) [223], and
the hybrid is GWO with β-hill climbing optimizer (β-GWO)
[168]. The CEC-2017 test functions are utilized to conduct
such a comparison. The same GWO parameters configuration
is used for the three methods to ensure a fair comparison. The
number of iterations is 5000, and the population size is 30
with 30 independent runs. The achieved results by the three
algorithms are compared in terms of the mean (AVG) and
standard deviation (STD).
The CEC-2017 benchmark test set features 30 test func-
tions, with 29 of them being stable and one being un-
stable. These tests provide a highly demanding evaluation
environment. These functions imitate the intricate nature of
real search spaces, which contain numerous local optimums
with various shaped functions across different areas. The 30
functions are categorized into: (1) Unimodal functions, rep-
resented by functions 1 to 3, (2) Basic multimodal functions,
represented by functions 4 to 10, (3) Hybrid functions, repre-
sented by functions 11 to f20, and (4) Composite functions,
represented by functions 21 to 30.
The obtained results by the three algorithms are presented
in Table 2, where the best results are presented in bold.
According to the results of the unimodal test functions
(i.e., C-17-f1 to C-17-f3), it can be seen that the BGWO
obtained the best results in the three test functions, whereas
the GWO achieved the second best for the same functions.
In addition, the BGWO obtained the best STD among all
compared algorithms. This proves that the BGWO has su-
perior search characteristics against the other optimization
algorithms in unimodal functions.
24
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 25 -->
## Page 25

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
TABLE 1: Application of GWO on different domains
Domain
Problem
Variant
Dataset source
Ref.
Electrical and Elec-
tronic Engineering
Developed a new controller
Modified
Numerical simulation
[147]
Optimize the model parameters of clean coal power genera-
tion
Original
Numerical simulation
[284]
Optimize PV system with boost full-bridge isolated converter
(BFBIC)
Modified
Numerical simulation
[148]
Optimal charging pattern of Li-ion batteries
Original
Numerical simulation
[110]
Optimizing coordinating of protective devices in electrical
power system
Modified
Numerical simulation
[76]
Fractional order proportional integral (FOPI) controller for
power factor correction (PFC)
Original
Numerical simulation
[249]
Optimal placement of Distributed Generation (DG) units in
radial distribution system
Multi-objective
IEEE-33 bus radial distribution system
[249]
Direction overcurrent relays coordination
Multi-objective
8-bus system and IEEE-30 bus system
[285]
Predict the remaining useful life for fuel cell under different
load currents
Original
Numerical simulation
[110]
Optimal power flow (OPF) problem
Modified
IEEE 30-bus system and IEEE 118-bus
system
[137]
Economic load dispatch problem
Hybrid
five different test cases of ELD problems
[168]
Economic load dispatch problem
Modified
four different test cases of ELD problems
[141]
Optimal placement and sizing of active power filters in radial
distribution system
Modified
IEEE-69 bus test system
[89]
Forecasting electric loads
Modified
Numerical simulation
[97]
Vibration tendency forecasting of hydropower generator
Modified
Ertan Hydropower Station in China
[91]
Photovoltaic-Wind-Battery Energy System Design Consider-
ing Outage Concept
Original
Ahvaz city in Iran
[286]
Thermal comfort and energy consumption prediction
Modified
Simulation dataset
[92]
Complementary scheduling of hydro-thermal-RE power sys-
tem
Hybrid
Simulation dataset
[204]
Optimal placement and sizing of multiple active power filters
in radial distribution system
Original
IEEE 519
[287]
Forecasting energy production and conversion of China
Original
China Statistical Yearbook 2019, and
IRENA Renewable Capacity Statistics
2020
[288]
Energy-Aware Service Composition in Cloud Manufacturing
Modified
Simulated dataset
[156]
Ameliorate voltage quality of odd-nary multi-level structure
Multi-objective
Simulation dataset
[211]
Energy mix optimization in Polish
Original
Polityka Energetyczna Polski 2040
[289]
An optimal power allocation scheme of microgrid
Original
Simulation dataset
[290]
Approximation of Fractional-Order Systems
Hybrid
Simulation dataset
[179]
Predict the remaining useful life of fuel cell
Hybrid
Simulation dataset
[196]
Distributed economic dispatch optimization
Multi-objective
Simulation dataset
[225]
Renewable energy
Predicting Solar Diffuse Fraction
Hybrid
Simulation dataset
[226], [195], [253]
Parameter extraction of solar photovoltaic models
Hybrid
Simulation dataset
[181]
Prediction of offshore wind farm power
Multi-objective
http://www.elia.be/en
[218]
Estimating photovoltaic solar cell model
Modified
Simulation dataset
[121]
Parameter extraction of photovoltaic cells and modules
Modified
Simulation dataset
[251]
Optimal configuration of photovoltaic power plant
Original
Simulation dataset
[252]
Optimal Operation of Hydropower System
Modified
Numerical simulation
[107]
Load dispatch of coal-fired power plants
Multi-objective
Simulation dataset
[224]
Networking
and
Communication
Multi-objective service composition and optimal selection
(MO-SCOS) problem in cloud manufacturing
Multi-Objective
MO-SCOS problems
[214]
Harmonic estimator design
Modified
Numerical simulation
[186]
Virtual network function placement (VNF-P) problem
Modified
http://userweb.swjtu.edu.cn/Userweb/hxx/research.htm
[153]
Wireless sensor network coverage optimization problem
Modified
Simulation dataset
[125]
Energy efficient load balancing approach for avoiding energy
hole problem in WSN
Modified
Simulation dataset
[254]
Electromagnetics
Modified
Numerical simulation
[291]
Antenna aperture illuminations for microwave power trans-
mission
Multi-objective
Numerical simulation
[216]
Design optimization of orbital angular momentum fibers
Multi-objective
Numerical simulation
[217]
Peak-to-average power ratio reduction technique in OFDM
scheme for high-speed wireless applications
Original
Simulation dataset
[292]
Wireless Sensor Network Deployment of 3D Surface
Modified
Numerical simulation
[150]
Energy-Efficient Routing in Wireless Sensor Networks
Modified
Simulation dataset
[255]
Self-Organizing Interval Type-2 Fuzzy Asymmetric CMAC
Design to Synchronize Chaotic Satellite Systems
Modified
Simulation dataset
[77]
Estimating modal amplitude and phase of multimode near
field patterns
Hybrid
Numerical simulation
[293]
Chaotic time series prediction using echo state network
Modified
Numerical simulation
[110]
enterprise service composition problem
Hybrid
Simulation dataset
[222]
VOLUME 4, 2016
25
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 26 -->
## Page 26

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
TABLE 1: Continue...
Domain
Problem
Variant
Dataset source
Ref.
Mechanical
engineering
Optimal operation of cascade hydropower stations
Multi-objective
Jinsha River CHSs in China
[220]
Multiple Hydropower Reservoirs Operation
Hybrid
Wu River in southwest China
[130]
Transformer fault diagnosis
Hybrid
Jiangxi Power Company dataset
[154]
Predictive Torque Control for Electric Buses
Original
Simulation dataset
[256]
Transformer Fault Diagnosis Using Dissolved Gases Consid-
ering Uncertainty in Measurements
Hybrid
Egyptian Electricity Utility
[165]
Design of Highly Uniform Magnetic Field Cylinder Coils in
Atomic Sensors
Original
Simulation dataset
[257]
Robust Control of Underwater Vehicle-Manipulator System
Hybrid
Vehicle-6DOF manipulator
[294]
Predicate full-face tunnel boring machine performance
Hybrid
Simulation dataset
[214]
Fault diagnosis of rolling bearing
Hybrid
NSF I/UCR Center on Intelligent Main-
tenance Systems dataset
[258]
Medical
applications
Compressive sensing MRI reconstruction
Original
https://ranger.uta.edu/
huang/Down-
loads.htm
[227]
Predict diabetes complications
Modified
UCI Repository of Machine Learning
Databases
[67]
COVID-19 pandemic modelling and prediction
Modified
https://data.humdata.org/dataset/novel-
coronavirus-2019-ncov-cases
[101]
Breast cancer classification
Hybrid
GLCM dataset
[259], [173]
Classification
Extractive single document summarization
Multi-objective
DUC2001 and DUC2002 dataset
[228]
Gene selection
Hybrid
Microarray benchmark datasets
[157]
Feature Selection
Modified
UCI repository
[83], [152], [118],
[166],
[74],
[73],
[99], [84]
Feature Selection
Hybrid
UCI repository
[295], [296], [176]
Hyperspectral feature selection
Modified
Indian Pines, Pavia University, and Sali-
nas
[297]
Feature selection for inconsistent heterogeneous information
systems
Hybrid
IHIS dataset
[298]
Feature selection method for human activity recognition us-
ing smartphone sensors
Hybrid
UCI-HAR
[167]
Arabic text classification
Hybrid
Akhbar-Alkhaleej dataset
[80]
Classification of power quality disturbances
Multi-objective
LV-25P/LA-55P, and NI-cDAQ datasets
[207]
Streamflow forecasting
Modified
Shangjingyou station and , Fenhe reser-
voir station
[260], [261]
Short-term load forecasting
Hybrid
Simulation dataset
[262]
Navigation technology
Hybrid
North University of China
[263]
Chemical engineer-
ing
Modeling and optimization of lead and cobalt biosorption
from water with Rafsanjan pistachio shell
Hybrid
NA
[230]
Reference evapotranspiration estimating
Hybrid
Simulation dataset
[231]
Petroleum
Engineering
Forecasting the natural gas and coal consumption in
Chongqing China
Hybrid
Chongqing dataset
[129]
Prediction for favorable reservoir of oil
Hybrid
3D seismic data of Niuzhuang area
[215]
Optimizing cetane improver concentration in the biodiesel-
diesel blend
Original
Simulation dataset
[264]
Optimizing biodiesel production from abundant waste oils
Hybrid
Simulation dataset
[265]
Forecasting fuel combustion-related CO2 emissions
Hybrid
Simulation dataset
[266]
Geotechnical
&
Geoenvironmental
Engineering
Groundwater Remediation
Hybrid
NA
[235]
Predicting soil electrical conductivity
Hybrid
Simulation dataset
[236]
Urban growth simulation and optimization
Modified
Nanjing City, China
[87]
Spatial prediction of landslide susceptibility
Hybrid
Tehri Garhwal, State of Uttarakhand, In-
dia
[275]
Water resources management
Modified
Shangjingyou station and Fenhe reser-
voir station of Fenhe River
[276]
Estimates of greenhouse gas emission in Turkey
Hybrid
TURKSTAT, other Turkish datasets
[277]
Civil Engineering
Predicting the compressive strength of normal and High-
Performance Concretes
Hybrid
NA
[233]
The equipment detection and localization of large-scale con-
struction job site by far-field construction surveillance video
Hybrid
PASCAL Visual Object Classes (VOC)
2007, 2012 and MS COCO
[234]
Estimation of soil moisture content
Hybrid
Agricultural lands of Dehgolan plain,
Iran
[68]
Predicting the dynamic modulus of asphalt mixture
Hybrid
XXX
[272]
Optimization of construction duration and schedule robust-
ness
Hybrid
PSPLIB dataset
[273]
Predict the compressive strength of concrete with partial
replacements for cement
Hybrid
NA
[274]
Control of the nonlinear building using an optimum inverse
Takagi-Sugeno-Kang model of magnetorheological damper
Modified
Numerical simulation
[271]
Robotics
Multi-robot exploration
Hybrid
ordinary and complex maps
[237]
Sliding Mode Control of 2-DOF Robot Manipulator
Modified
Simulation dataset
[127]
Sliding Mode Control of 2-DOF Robot Manipulator
Hybrid
Simulation dataset
[126]
The path planning for 3D multi-Unmanned Aerial Vehicle
(UAV)
Modified
Simulation dataset
[278], [175], [114]
The path planning for Unmanned Aerial Vehicle (UAV)
Hybrid
Simulation dataset
[175]
Multi-UAV Path Planning
Hybrid
Simulation dataset
[140]
3D path planning of multiple UAVs in power inspection
Hybrid
Simulation dataset
[184]
26
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 27 -->
## Page 27

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
TABLE 1: Continue...
Domain
Problem
Variant
Dataset source
Ref.
Industrial Engineer-
ing
Degree reduction of SG-Bezier surfaces
Hybrid
4 × 4, and 6 × 6 SG-Bezier surfaces
[232]
Bi-Objective next release problem
Multi-objective
http://
researchers.lille.inria.fr/
xuan/-
page/ project/nrp
[219]
Disassembly sequence planning
Modified
vise, ball valve, azimuth thruster pro-
peller, robot arm
[155]
Assembly line balancing problem considering preventive
maintenance scenarios
Modified
https://assembly-line-balancing.de/
[137]
Supplier selection and order quantity allocation problem
Modified
Simulation dataset
[192]
Daily optimal operation of cascade pumping stations
Hybrid
Simulation dataset
[90]
Optimization of thermal efficiency and unburned carbon in
fly ash of coal-fired utility boiler
Original
DCS dataset
[267]
Optimal QoS-aware service composition and optimal selec-
tion in cloud manufacturing
Hybrid
Simulation dataset
[193]
Pattern recognition method for mixture control charts
Modified
Numerical simulation
[226]
Multi-UAV multi-target urban tracking path planning prob-
lems
Modified
Numerical simulation
[100]
Enhancement of an impulse turbine for oscillating water
column
Modified
Numerical simulation
[119]
Design of the spur gear pairs with minimum weight
Original
Numerical simulation
[268]
Disassembly sequencing and line balancing problem
Multi-Objective
Numerical simulation
[164]
Forecasting of automobile sales
Original
Suteng and Kaluola
[269]
Optimization of an auto drum fashioned brake
Modified
Numerical simulation
[113]
Optimal control parameters and design of the output filter of
a grid-tied three-phase inverter
Original
Numerical simulation
[270]
multi-objective disassembly sequencing and line balancing
planning in disassembling multiple products
Hybrid
Numerical simulation
[172]
Planing & schedul-
ing
Casting production scheduling problem
Multi-objective
Simulation dataset
[170]
Flow Shop Scheduling Problem with Multi-machine Collab-
oration
Modified
FSSP-MC instances
[110]
Flexible job shop scheduling problem with hierarchical job
precedence constraints
Hybrid
https://github.com/zzw95/FJSP_JPC/tree/master/
test_instances
[213], [194]
Hybrid flowshop scheduling problem considering noise pol-
lution
Multi-objective
HFSP benchmarks
[86]
Task schedule for cloud data centers
Multi-objective
GoCJ, HCSP and Synthetic dataset
[209]
Short-Term Hydrothermal Scheduling
Hybrid
Three STHS systems
[178]
knapsack problem
Binary
http://people.brunel.ac.uk/mastjjb/jeb/orlib/
mknapinfo.html
[81]
Welding shop inverse scheduling problem (WSISP)
Modified
WSISP problems
[75], [136]
Power scheduling problem in smart home
Hybrid
seven consumption scenarios
[185]
Path planning of Unmanned Aerial Vehicles
Modified
Simulation dataset
[162]
Image processing
Joint denoising and unmixing of multispectral images
Modified
tensor
[238]
Camera calibration method
Modified
Simulation dataset
[239]
Multi-level image thresholding
Modified
Berkeley dataset
[212]
Multimodal image registration
Hybrid
Synthetic dataset
[279]
Classification of magnetic resonance brain images
Hybrid
Harvard Medical School, and BRATS
[280]
Image Segmentation
hybrid
Iris, and UCI
[191]
Non-blind RGB watermarking
Modified
RGB images and Watermarked images
[281]
Sub-pixel displacement measurement
Hybrid
Synthetic speckle images
[169]
Key points selected to simplify the point cloud
Modified
The Stanford 3D Scanning Repository
[282]
Others
Designing Convolutional Neural Network-Long Short-Term
Memory (CNN-LSTM) networks for time series analysis
Modified
Cbenchmark problems
[242]
Software Engineering
Hybrid
UCI repository
[65]
Stock selection
Hybrid
http://choice.eastmoney.com/
[123]
Extracting core answers in community question answering
Original
Zhihu and Yahoo!Answers QA dataset
[215]
Automatic speech emotion detection
Hybrid
SAVEE and TESS datasets
[243]
Test functions
Hybrid
CEC 2017
[123]
Modified
CEC 2017 and engineering problems
[96], [103], [120]
Multi-objective
DTLZ
[208]
Hybrid
DTLZ, LZ09F, WFG and ZDT
[182]
Modified
CEC 2018
[135]
Hybrid
Integer and mixed-integer problems
[241]
Hybrid
classical test functions, and engineering
problems
[111], [183]
Hybrid
classical test functions
[192]
Modified
classical test functions, and engineering
problems
[104], [198], [116],
[117], [79]
Modified
classical test functions, and CEC 2014
[108], [115], [158]
Hybrid
classical test functions, and CEC 2014
[283]
Modified
classical test functions
[142], [151], [105]
Modified
CEC 2006 and CEC 2014
[139]
Modified
classical test functions, CEC 2014, and
KELM
[299]
Modified
classical test functions, CEC 2014, and
engineering problems
[106]
Modified
CEC 2014, CEC 2017, and engineering
problems
[138], [122]
Modified
CEC 2014, CEC 2017, and large-scale
numerical optimization problems
[300]
Modified
test functions and real-world problems
[105]
Modified
CEC 2019 and real-world problems
[105]
Modified
CEC 2018 and real-world problems
[78]
VOLUME 4, 2016
27
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 28 -->
## Page 28

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
TABLE 2: Comparison between GWO, LGWO, and BGWO
Function
Measure
GWO
LGWO
BGWO
Fun 1
AVG
11564013.83
277635737.77
3013.85
STD
77129790.73
398464430.50
690.91
Fun 2
AVG
4019015.57
1334283570.97
7534.64
STD
16277161.73
4535252236.03
690.91
Fun 3
AVG
1107.81
3706.89
300.43
STD
1601.53
2452.92
1.05
Fun 4
AVG
409.46
440.52
400.00
STD
9.04
34.80
0.00
Fun 5
AVG
509.31
528.47
500.00
STD
4.91
5.68
0.01
Fun 6
AVG
600.36
610.32
600.01
STD
1.81
5.90
0.00
Fun 7
AVG
723.82
747.59
704.37
STD
6.11
7.89
5.99
Fun 8
AVG
810.34
821.34
800.00
STD
5.45
6.76
0.01
Fun 9
AVG
917.91
964.09
900.00
STD
60.13
77.23
0.00
Fun 10
AVG
1456.41
1959.39
1000.05
STD
296.43
313.45
0.06
Fun 11
AVG
1130.59
1328.03
1100.00
STD
39.19
801.00
0.01
Fun 12
AVG
124550.98
920846.21
1233.12
STD
945659.94
754327.14
12.94
Fun 13
AVG
4534.84
8876.58
1304.09
STD
5894.38
3425.20
0.94
Fun 14
AVG
1815.34
3291.46
1400.46
STD
1378.90
1828.60
0.52
Fun 15
AVG
2024.14
3905.45
1500.22
STD
1107.76
2259.67
0.29
Fun 16
AVG
1680.12
1834.81
1600.04
STD
72.64
156.33
0.01
Fun 17
AVG
1737.13
1774.27
1700.05
STD
16.98
36.50
0.02
Fun 18
AVG
20934.37
27568.68
1802.23
STD
13635.92
9917.83
0.87
Fun 19
AVG
2664.92
7554.32
1900.27
STD
46814.38
5407.43
0.16
Fun 20
AVG
2076.49
2097.00
2000.05
STD
50.30
59.35
0.01
Fun 21
AVG
2301.76
2311.70
2108.34
STD
29.41
41.47
28.87
Fun 22
AVG
2322.78
2330.89
2222.47
STD
117.39
30.18
40.82
Fun 23
AVG
2613.13
2640.10
2300.01
STD
6.25
11.11
0.00
Fun 24
AVG
2732.55
2748.79
2500.02
STD
3.97
61.86
0.00
Fun 25
AVG
2925.58
2935.87
2808.55
STD
19.45
22.48
143.62
Fun 26
AVG
3150.69
3316.66
2622.37
STD
419.32
395.55
66.67
Fun 27
AVG
3095.30
3130.37
3086.89
STD
9.42
35.79
0.00
Fun 28
AVG
3361.30
3410.47
2900.28
STD
83.36
122.38
149.82
Fun 29
AVG
3169.45
3217.27
3045.58
STD
42.26
42.51
0.08
Fun 30
AVG
289160.55
1477449.27
3426.58
STD
677985.04
2134784.53
17.46
In terms of multimodal test functions, it can be observed
that the BGWO was ranked first by obtaining the best results
in all test functions, including the fourth to the tenth func-
tions, while the GWO was ranked second. The LGWO was
reported third by achieving the worst results in all test func-
tions. Furthermore, the BGWO outperformed the compared
algorithms in achieving the best STD. Based on the above
discussion, we can conclude that the BGWO is superior
in searching for optimal solutions compared to GWO and
LGWO.
For the Hybrid test functions, also the BGWO obtained the
best outcomes compared with the GWO and LBGWO, where
it achieved the best AVG and STD results in all test functions.
Accordingly, the BGWO outperformed the competing algo-
rithms in optimizing the Hybrid test functions. According
to Composite functions, the BGWO also outperformed the
compared algorithms by obtaining the best AVG and STD in
all and seven functions, respectively.
VII. CRITICAL ANALYSIS OF GREY WOLF OPTIMIZER
THEORY
The critical analysis section will provide the research gaps
in the optimization framework of GWO when dealing with
some non-convex, nonlinear, multimodal, and constrained
optimization problems. During our theoretical review, differ-
ent GWO versions have been proposed by either combining
efficient operators from other optimization algorithms or
hybridizing GWO with other algorithms to improve the bal-
ance between the exploration and exploitation search process
when dealing with rugged and deep search spaces.
Based on the optimization behaviour of GWO, it has two
groups which are the follower (i.e., omega) and three leaders
(i.e., alpha, beta, and delta). The leaders represent the best
three solutions so far found (i.e., first-best, second-best, and
third-best). The members of omega groups are attracted by
the leader groups and their base values. This structure reveals
very efficient outcomes when dealing with "free optimiza-
tion problem (FOP)" 1. However, when the "constrained
optimization problem (COP)" is subject to be addressed,
the ruggedness and the shape of the search space will be
substantially increased. Therefore, the process of focusing
on the leaders to attract followers might drive the search
toward premature convergence. Thus, the search shall also
be injected with random elements to improve the diversity of
the search space. For example, the GWO has been combined
with a random walk to improve the exploration process [76],
[77]. Furthermore, the Chaotic concepts as exploiter engines
have been incorporated inside GWO [96], [97], [98]. Also,
in the Opposition GWO, the diversity behaviour is improved
[71], [105]
Another issue that has been tackled in the theory of GWO
is the definition of the search space based on the nature of
the problem decision variables. In its base article published
in 2014, GWO was proposed to deal with the continuous
domains (or real values decision variables). However, there
are different encoding systems in the genotype space for
the different types of optimization problems, such as binary,
discrete, permutation, graph structure, and network. To deal
with these genotype spaces, the theory of GWO has to be
adjusted. For example, different binary GWO instances have
been proposed to deal with binary search space [74], [301],
[80], [81], [82]. These instances are different in terms of
the to-binary transfer function, the recombination process,
and the randomness process. Also, the discrete search space
has been well-defined and the GWO operators have adjusted
1this refers to the problems with only objective function not restricted by
any constraints
28
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 29 -->
## Page 29

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
accordingly [75], [140], [164]. In dealing with permutation
search space like the traveling salesman problem where the
decision variables are not duplicated and not missed, the
operator of GWO has been also modified to preserve the
integrity of the solution during the inheritance process [302].
In any evolutionary algorithm (EA) like GWO, the losing
diversity dilemma can be dealt with either implicitly or
explicitly. The implicit approach is normally injected with
problem encoding by adding restricted values to the solution
to define a forbidding area. In the explicit approaches, the
structured population algorithms such as island model [303],
Cellular automata [86], [87] and Gaussian theory [100], [101]
are used to improve the diversity power of GWO.
The parameter values in evolutionary algorithms play im-
portant role in the convergence behaviour and ensure the
right balance between the exploration and exploitation of
the search space. Although the initial version of GWO has
been established without any parameter settings, there are
three control parameters that are initialized randomly within
specific ranges (i.e., a, A, and C). However, these con-
trol parameters have a great impact on the performance of
GWO. Therefore, several trials to improve the convergence
behaviour of GWO have been conducted, such as adaptive
GWO [70], [88], [91], and Dynamic GWO [103], [104].
Indeed, the convergence strength of any evolutionary al-
gorithm, such as GWO is proved when dealing with large-
scale optimization problems. This is because the complexity
is increased and the search space will be huge. Therefore, to
deal with a large-scale optimization problem, the structured
GWO is proposed in many pieces of research [118], [119],
[120]. To empower the research behaviour, the hybrid mech-
anism with local search has also revealed very successful
outcomes such as Neighbour GWO [135], [75] and memetic
GWO [163], [164]. Finally, the exploration and exploitation
process is balanced during the search using Fractional GWO
[72], [129].
The main limitation of the GWO is connected to the NFL
optimization theorem, which is also a challenge faced by
other optimization algorithms. The NFL theorem asserts that
no single optimization algorithm can outperform all others
for every type of optimization problem or every instance of
the same problem [304]. Consequently, the convergence of
the GWO heavily depends on the properties of the problem’s
search space. Therefore, in an unfamiliar search space, it is
essential to adapt or combine the GWO with other techniques
to tackle the optimization task.
VIII. CONCLUSION AND FUTURE WORK
Grey wolf optimizer (GWO) gains substantial attention
from a wide range of research communities due to its superb
features. The strengths of GWO lie in its ability to synergy
the trade-off between exploration and exploitation during
the search process. Accomplishing an outstanding review for
GWO is not a trivial task due to the fact that it is growing
rapidly over the last three years where more than 750 articles
(Journal paper, conference, book chapter, book, review, etc.)
have been published. Therefore, in this review paper, we have
only focused on the Scopus journal papers published in the
last four years (2019-2022).
Although GWO behaves perfectly when dealing with
mathematical or free optimization problems. Its performance
is degraded when addressing non-convex, multimodal, non-
linear, highly-constrained optimization problems with deep
and rugged search space. Therefore, different versions of
GWO have been proposed in the literature to deal with such
problems. In some state-of-the-art, the GWO is hybridized
with other optimization algorithms especially the algorithm
is empowered using local search (i.e., memetic strategy) to
enhance its search capability. Also, GWO has been adjusted
to deal with multi-objective optimization problems.
Due to its proven efficiency, researchers from different
research backgrounds have been encouraged to utilize GWO
for their optimization problems. Therefore, GWO has been
used to solve different kinds of optimization problems from
different research domains such as electrical and electronic
engineering, renewable energy, networking and communi-
cation, mechanical engineering, and many others. Indeed,
researchers nowadays like to start with GWO to tackle their
problems because it has an efficient and simple optimization
framework. We believe that GWO will gain much interest in
the future.
The main limitations of GWO are reviewed in previous
sections which are related to losing diversity due to its focus
on the three best solutions to adjust other solutions. Addition-
ally, its degraded performance when dealing with large-scale
optimization problems and the parameter settings dilemma
to boost its performance. The discrete, binary, permutation
genotype space required tweaking in the GWO optimization
structure to deal with the genotype space shape.
Several future research directions can be tackled by re-
searchers. The following are some of these possible future
research directions:
Structured population: A Structured population means di-
viding the population into several parts. It can be in
different forms such as island models, cellular automata,
hierarchical models, etc. [305]. This population orga-
nization can improve the diversity of the developed
solutions. The GWO is modified using island models
to tackle specific problems (e.g., [306]). In the future,
other structured population models can be utilized and
evaluated.
Adaptive Parameters: The performance of GWO depends
on the chosen values of its control parameters. Consid-
erable research work is proposed to develop parameter-
free GWO [70], [88], [90]. Developing a black box
robust parameter-free GWO can be a future direction.
Hybrid Strategy: The complexity of real-world problems
requires improving GWO capabilities as it requires deal-
ing with a deep and rugged problem search space [223].
The exploration and exploitation processes of GWO can
be improved by hybridizing the technique with other
techniques as a possible path for future investigation for
VOLUME 4, 2016
29
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 30 -->
## Page 30

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
optimization problems that are non-linear, non-convex,
highly constrained, combinatorial, and multimodal.
Tackling multi-objective problems : A number of research
works is applied to apply GWO to tackle multi-objective
problems (e.g., [217], [216], [214]). The GWO can
utilize popular multi-objective optimization frameworks
such as NSGA II and MOEA/D [307]. The multi-
objective stopping criterion influences the final solution
quality. Another future direction can be choosing the
proper multi-objective stopping technique [308].
CONFLICT OF INTEREST
The authors declare that they have no conflict of interest
DATA AVAILABILITY
The datasets generated during and/or analyzed during the
current study are available from the corresponding author
upon reasonable request.
REFERENCES
[1] Ibrahim H Osman and Gilbert Laporte. Metaheuristics: A bibliography.
Annals of Operations research, 63:511–623, 1996.
[2] Christian Blum and Andrea Roli.
Metaheuristics in combinatorial
optimization: Overview and conceptual comparison. ACM computing
surveys (CSUR), 35(3):268–308, 2003.
[3] Sofian Kassaymeh, Salwani Abdullah, Mohamad Al-Laham, Mohammed
Alah, Mohammed Azmi Al-Betar, and Zalinda Othman.
Salp swarm
optimizer for modeling software reliability prediction problems. Neural
Processing Letters, pages 1–37, 2021.
[4] Fernando Fausto, Adolfo Reyna-Orta, Erik Cuevas, Ángel G Andrade,
and Marco Perez-Cisneros. From ants to whales: metaheuristics for all
tastes. Artificial Intelligence Review, 53(1):753–810, 2020.
[5] Zaid
Abdi
Alkareem
Alyasseri,
Osama
Ahmad
Alomari,
Mo-
hammed Azmi Al-Betar, Sharif Naser Makhadmeh, Iyad Abu Doush,
Mohammed A Awadallah, Ammar Kamal Abasi, and Ashraf Elnagar.
Recent advances of bat-inspired algorithm, its versions and applications.
Neural Computing and Applications, 34(19):16387–16422, 2022.
[6] Scott Kirkpatrick, C Daniel Gelatt Jr, and Mario P Vecchi. Optimization
by simulated annealing. science, 220(4598):671–680, 1983.
[7] Fred Glover. Tabu search: A tutorial. Interfaces, 20(4):74–94, 1990.
[8] Thomas A Feo and Mauricio GC Resende. Greedy randomized adaptive
search procedures. Journal of global optimization, 6:109–133, 1995.
[9] Nenad Mladenovi´c and Pierre Hansen. Variable neighborhood search.
Computers & operations research, 24(11):1097–1100, 1997.
[10] Thomas Stützle and Rubén Ruiz. Iterated local search. Handbook of
heuristics, 1:2, 2018.
[11] Mohammed Azmi Al-Betar. β-hill climbing: an exploratory local search.
Neural Computing and Applications, 28(Suppl 1):153–168, 2017.
[12] Berat Do˘gan and Tamer Ölmez.
A new metaheuristic for numerical
function optimization: Vortex search algorithm. Information sciences,
293:125–145, 2015.
[13] Sofian Kassaymeh, Mohamad Al-Laham, Mohammed Azmi Al-Betar,
Mohammed Alweshah, Salwani Abdullah, and Sharif Naser Makhadmeh.
Backpropagation neural network optimization and software defect esti-
mation modelling using a hybrid salp swarm optimizer-based simulated
annealing algorithm. Knowledge-Based Systems, 244:108511, 2022.
[14] John H Holland. Genetic algorithms. Scientific american, 267(1):66–73,
1992.
[15] Xin Yao, Yong Liu, and Guangming Lin.
Evolutionary programming
made faster. IEEE Transactions on Evolutionary computation, 3(2):82–
102, 1999.
[16] John R Koza and John R Koza. Genetic programming: on the program-
ming of computers by means of natural selection, volume 1. MIT press,
1992.
[17] Rainer Storn and Kenneth Price.
Differential evolution-a simple and
efficient heuristic for global optimization over continuous spaces. Journal
of global optimization, 11(4):341, 1997.
[18] Dan Simon. Biogeography-based optimization. IEEE transactions on
evolutionary computation, 12(6):702–713, 2008.
[19] Shumeet Baluja. Population-based incremental learning. a method for
integrating genetic search based function optimization and competitive
learning. Technical report, Carnegie-Mellon Univ Pittsburgh Pa Dept Of
Computer Science, 1994.
[20] Ali Kaveh, Hossein Akbari, and Seyed Milad Hosseini. Plasma gener-
ation optimization: a new physically-based metaheuristic algorithm for
solving constrained optimization problems. Engineering Computations,
2020.
[21] A Kaveh and M Khayatazad. A new meta-heuristic method: ray opti-
mization. Computers & structures, 112:283–294, 2012.
[22] Farouq Zitouni, Saad Harous, and Ramdane Maamri. The solar system
algorithm: a novel metaheuristic method for global optimization. IEEE
Access, 9:4542–4565, 2020.
[23] Afshin Faramarzi, Mohammad Heidarinejad, Brent Stephens, and
Seyedali Mirjalili. Equilibrium optimizer: A novel optimization algo-
rithm. Knowledge-Based Systems, 191:105190, 2020.
[24] Esmat Rashedi, Hossein Nezamabadi-Pour, and Saeid Saryazdi.
Gsa:
a gravitational search algorithm. Information sciences, 179(13):2232–
2248, 2009.
[25] A Kaveh, M Khanzadi, and M Rastegar Moghaddam. Billiards-inspired
optimization algorithm; a new meta-heuristic method.
In Structures,
volume 27, pages 1722–1739. Elsevier, 2020.
[26] Fatma A Hashim, Essam H Houssein, Mai S Mabrouk, Walid Al-
Atabany, and Seyedali Mirjalili. Henry gas solubility optimization: A
novel physics-based algorithm. Future Generation Computer Systems,
101:646–667, 2019.
[27] Albert Lam and Victor OK Li. Chemical reaction optimization: a tutorial.
Memetic Computing, 4(1):3–17, 2012.
[28] Zong Woo Geem, Joong Hoon Kim, and Gobichettipalayam Vasudevan
Loganathan. A new heuristic optimization algorithm: harmony search.
simulation, 76(2):60–68, 2001.
[29] Yuhui Shi. Brain storm optimization algorithm. In International confer-
ence in swarm intelligence, pages 303–309. Springer, 2011.
[30] Qamar Askari, Mehreen Saeed, and Irfan Younas. Heap-based optimizer
inspired by corporate rank hierarchy for global optimization.
Expert
Systems with Applications, 161:113702, 2020.
[31] R Venkata Rao, Vimal J Savsani, and DP Vakharia. Teaching–learning-
based optimization: a novel method for constrained mechanical design
optimization problems. Computer-aided design, 43(3):303–315, 2011.
[32] Qamar Askari, Irfan Younas, and Mehreen Saeed. Political optimizer: A
novel socio-inspired meta-heuristic for global optimization. Knowledge-
based systems, 195:105709, 2020.
[33] Malik Braik, Mohammad Hashem Ryalat, and Hussein Al-Zoubi.
A
novel meta-heuristic algorithm for solving numerical optimization prob-
lems: Ali baba and the forty thieves. Neural Computing and Applications,
34(1):409–455, 2022.
[34] Yiying Zhang and Zhigang Jin. Group teaching optimization algorithm:
A novel metaheuristic method for solving global optimization problems.
Expert Systems with Applications, 148:113246, 2020.
[35] Olaide Nathaniel Oyelade, Absalom El-Shamir Ezugwu, Tehnan IA
Mohamed, and Laith Abualigah. Ebola optimization search algorithm: A
new nature-inspired metaheuristic optimization algorithm. IEEE Access,
10:16150–16177, 2022.
[36] Elyas Fadakar and Masoud Ebrahimi. A new metaheuristic football game
inspired algorithm. In 2016 1st conference on swarm intelligence and
evolutionary computation (CSIEC), pages 6–11. IEEE, 2016.
[37] Mohammed Azmi Al-Betar, Zaid Abdi Alkareem Alyasseri, Mo-
hammed A Awadallah, and Iyad Abu Doush. Coronavirus herd immunity
optimizer (chio).
Neural Computing and Applications, 33(10):5011–
5042, 2021.
[38] Laith Abualigah, Ali Diabat, Seyedali Mirjalili, Mohamed Abd Elaziz,
and Amir H Gandomi. The arithmetic optimization algorithm. Computer
methods in applied mechanics and engineering, 376:113609, 2021.
[39] Hojjat Emami. Stock exchange trading optimization algorithm: a human-
inspired method for global optimization. The Journal of Supercomputing,
78(2):2125–2174, 2022.
[40] Seyyed Hamid Samareh Moosavi and Vahid Khatibi Bardsiri. Poor and
rich optimization algorithm: A new human-based and multi populations
algorithm. Engineering Applications of Artificial Intelligence, 86:165–
181, 2019.
[41] Jagdish Chand Bansal, Pramod Kumar Singh, and Nikhil R Pal. Evolu-
tionary and swarm intelligence algorithms, volume 779. Springer, 2019.
30
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 31 -->
## Page 31

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
[42] Marco Dorigo and Gianni Di Caro.
Ant colony optimization: a new
meta-heuristic.
In Proceedings of the 1999 congress on evolutionary
computation-CEC99 (Cat. No. 99TH8406), volume 2, pages 1470–1477.
IEEE, 1999.
[43] James Kennedy and Russell Eberhart. Particle swarm optimization. In
Proceedings of ICNN’95-International Conference on Neural Networks,
volume 4, pages 1942–1948. IEEE, 1995.
[44] Amir Hossein Gandomi and Amir Hossein Alavi. Krill herd: a new bio-
inspired optimization algorithm. Communications in nonlinear science
and numerical simulation, 17(12):4831–4845, 2012.
[45] Xin-She Yang and Suash Deb. Cuckoo search via lévy flights. In 2009
World congress on nature & biologically inspired computing (NaBIC),
pages 210–214. IEEE, 2009.
[46] Xin-She Yang et al. Firefly algorithm. Nature-inspired metaheuristic
algorithms, 20:79–90, 2008.
[47] Malik Braik, Abdelaziz Hammouri, Jaffar Atwan, Mohammed Azmi Al-
Betar, and Mohammed A Awadallah. White shark optimizer: A novel
bio-inspired meta-heuristic algorithm for global optimization problems.
Knowledge-Based Systems, page 108457, 2022.
[48] Dervis Karaboga.
An idea based on honey bee swarm for numerical
optimization. Technical report, Technical report-tr06, Erciyes university,
engineering faculty, computer ..., 2005.
[49] Xianbing Meng, Yu Liu, Xiaozhi Gao, and Hengzhen Zhang. A new
bio-inspired algorithm: chicken swarm optimization.
In International
conference in swarm intelligence, pages 86–94. Springer, 2014.
[50] Fatma A Hashim and Abdelazim G Hussien. Snake optimizer: A novel
meta-heuristic optimization algorithm. Knowledge-Based Systems, page
108320, 2022.
[51] Seyedali Mirjalili.
The ant lion optimizer.
Advances in engineering
software, 83:80–98, 2015.
[52] Gai-Ge Wang, Suash Deb, Xiao-Zhi Gao, and Leandro Dos Santos
Coelho.
A new metaheuristic optimisation algorithm motivated by
elephant herding behaviour. International Journal of Bio-Inspired Com-
putation, 8(6):394–409, 2016.
[53] Jiankai Xue and Bo Shen.
A novel swarm intelligence optimization
approach: sparrow search algorithm. Systems Science & Control En-
gineering, 8(1):22–34, 2020.
[54] Farid MiarNaeimi, Gholamreza Azizyan, and Mohsen Rashki.
Horse
herd optimization algorithm: A nature-inspired algorithm for high-
dimensional optimization problems.
Knowledge-Based Systems,
213:106711, 2021.
[55] Seyedali Mirjalili. Dragonfly algorithm: a new meta-heuristic optimiza-
tion technique for solving single-objective, discrete, and multi-objective
problems. Neural Computing and Applications, 27(4):1053–1073, 2016.
[56] Gaurav Dhiman, Meenakshi Garg, Atulya Nagar, Vijay Kumar, and Mo-
hammad Dehghani. A novel algorithm for global optimization: rat swarm
optimizer. Journal of Ambient Intelligence and Humanized Computing,
12(8):8457–8482, 2021.
[57] Seyedali Mirjalili. Moth-flame optimization algorithm: A novel nature-
inspired heuristic paradigm.
Knowledge-based systems, 89:228–249,
2015.
[58] Seyedali Mirjalili and Andrew Lewis. The whale optimization algorithm.
Advances in engineering software, 95:51–67, 2016.
[59] Suyanto Suyanto, Alifya Aisyah Ariyanto, and Alifya Fatimah Ariyanto.
Komodo mlipir algorithm. Applied Soft Computing, 114:108043, 2022.
[60] Sofian Kassaymeh, Salwani Abdullah, Mohammed Al-Betar, Mo-
hammed Alweshah, Mohamad Al-Laham, and Zalinda Othman. Self-
adaptive salp swarm algorithm for optimization problems. Soft Comput-
ing, 2022.
[61] M Khishe and Mohammad Reza Mosavi. Chimp optimization algorithm.
Expert systems with applications, 149:113338, 2020.
[62] Jeffrey O Agushaka, Absalom E Ezugwu, and Laith Abualigah. Dwarf
mongoose optimization algorithm. Computer Methods in Applied Me-
chanics and Engineering, 391:114570, 2022.
[63] Ammar Kamal Abasi, Sharif Naser Makhadmeh, Mohammed Azmi
Al-Betar, Osama Ahmad Alomari, Mohammed A Awadallah, Zaid
Abdi Alkareem Alyasseri, Iyad Abu Doush, Ashraf Elnagar, Eman H
Alkhammash, and Myriam Hadjouni.
Lemurs optimizer: A new
metaheuristic algorithm for global optimization.
Applied Sciences,
12(19):10057, 2022.
[64] Seyedali Mirjalili, Seyed Mohammad Mirjalili, and Andrew Lewis. Grey
wolf optimizer. Advances in engineering software, 69:46–61, 2014.
[65] M. A. Al-Betar A. I. Hammouri M. A. Al-Ma’aitahe S. Kassaymeh,
M. Alweshah. Software effort estimation modeling and fully connected
artificial neural network optimization using soft computing techniques.
Cluster Computing, 1, 2023.
[66] Shubham Gupta and Kusum Deep.
A novel random walk grey wolf
optimizer. Swarm and evolutionary computation, 44:101–112, 2019.
[67] F. Jeyafzam, B. Vaziri, M.Y. Suraki, A.A.R. Hosseinabadi, and A. Slowik.
Improvement of grey wolf optimizer with adaptive middle filter to adjust
support vector machine parameters to predict diabetes complications.
Neural Computing and Applications, 33(22):15205–15228, 2021.
[68] S. Maroufpoor, E. Maroufpoor, O. Bozorg-Haddad, J. Shiri, and
Z. Mundher Yaseen. Soil moisture simulation using hybrid artificial in-
telligent model: Hybridization of adaptive neuro fuzzy inference system
with grey wolf optimizer algorithm. Journal of Hydrology, 575:544–556,
2019.
[69] Hossam Faris, Ibrahim Aljarah, Mohammed Azmi Al-Betar, and Seyedali
Mirjalili. Grey wolf optimizer: a review of recent variants and applica-
tions. Neural computing and applications, 30(2):413–435, 2018.
[70] Gungor Yildirim and Bilal Alatas. New adaptive intelligent grey wolf
optimizer based multi-objective quantitative classification rules mining
approaches. Journal of Ambient Intelligence and Humanized Computing,
pages 1–25, 2021.
[71] Jingwei Too and Abdul Rahim Abdullah. Opposition based competitive
grey wolf optimizer for emg feature selection. Evolutionary Intelligence,
pages 1–15, 2020.
[72] Amar B Deshmukh and N Usha Rani. Fractional-grey wolf optimizer-
based kernel weighted regression model for multi-view face video super
resolution. International Journal of Machine Learning and Cybernetics,
10(5):859–877, 2019.
[73] P. Hu, J.-S. Pan, and S.-C. Chu. Improved binary grey wolf optimizer
and its application for feature selection. Knowledge-Based Systems, 195,
2020.
[74] Q. Al-Tashi, S.J. Abdulkadir, H.M. Rais, S. Mirjalili, H. Alhussian, M.G.
Ragab, and A. Alqushaibi. Binary multi-objective grey wolf optimizer
for feature selection in classification. IEEE Access, 8:106247–106263,
2020.
[75] C. Wang, L. Zhao, X. Li, and Y. Li. An improved grey wolf optimizer for
welding shop inverse scheduling. Computers and Industrial Engineering,
2021.
[76] S. Gupta and K. Deep. Optimal coordination of overcurrent relays using
improved leadership-based grey wolf optimizer.
Arabian Journal for
Science and Engineering, 45(3):2081–2091, 2020.
[77] T.-L. Le, T.-T. Huynh, and S.-K. Hong. Self-organizing interval type-2
fuzzy asymmetric cmac design to synchronize chaotic satellite systems
using a modified grey wolf optimizer. IEEE Access, 8:53697–53709,
2020.
[78] J. Adhikary and S. Acharyya. Randomized balanced grey wolf optimizer
(rbgwo) for solving real life optimization problems.
Applied Soft
Computing, 117, 2022.
[79] X. Liu, Y. Wang, and M. Zhou.
Dimensional learning strategy-based
grey wolf optimizer for solving the global optimization problem. Com-
putational Intelligence and Neuroscience, 2022, 2022.
[80] H. Chantar, M. Mafarja, H. Alsawalqah, A. A. Heidari, I. Aljarah, and
H. Faris. Feature selection using binary grey wolf optimizer with elite-
based crossover for arabic text classification.
Neural Computing and
Applications, 32(16):12201–12220, 2020.
[81] K. Luo and Q. Zhao. A binary grey wolf optimizer for the multidimen-
sional knapsack problem. Applied Soft Computing Journal, 83, 2019.
[82] Srikanth Reddy, Lokesh Kumar Panwar, Bijaya K Panigrahi, Rajesh
Kumar, and Ameena Alsumaiti. Binary grey wolf optimizer models for
profit based unit commitment of price-taking genco in electricity market.
Swarm and evolutionary computation, 44:957–971, 2019.
[83] M. Abdel-Basset, D. El-Shahat, I. El-henawy, V.H.C. de Albuquerque,
and S. Mirjalili. A new fusion of grey wolf optimizer algorithm with a
two-phase mutation for feature selection. Expert Systems with Applica-
tions, 139, 2020.
[84] Rajalaxmi Ramasamy Rajammal, Seyedali Mirjalili, Gothai Ekambaram,
and Natesan Palanisamy. Binary grey wolf optimizer with mutation and
adaptive k-nearest neighbour for feature selection in parkinson’s disease
diagnosis. Knowledge-Based Systems, 246:108701, 2022.
[85] Z.A.A. Alyasseri, O.A. Alomari, S.N. Makhadmeh, S. Mirjalili, M.A.
Al-Betar, S. Abdullah, N.S. Ali, J.P. Papa, D. Rodrigues, and A.K. Abasi.
Eeg channel selection for person identification using binary grey wolf
optimizer. IEEE Access, 10:10500–10513, 2022.
VOLUME 4, 2016
31
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 32 -->
## Page 32

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
[86] C. Lu, L. Gao, Q. Pan, X. Li, and J. Zheng. A multi-objective cellular
grey wolf optimizer for hybrid flowshop scheduling problem considering
noise pollution. Applied Soft Computing Journal, 75:728–749, 2019.
[87] M. Cao, M. Huang, R. Xu, G. Lü, and M. Chen.
A grey wolf opti-
mizer–cellular automata integrated model for urban growth simulation
and optimization. Transactions in GIS, 23(4):672–687, 2019.
[88] Tarik A Rashid, Dosti K Abbas, and Yalin K Turel.
A multi hidden
recurrent neural network with a modified grey wolf optimizer. PloS one,
14(3):e0213237, 2019.
[89] A. Lakum and V. Mahajan. A novel approach for optimal placement and
sizing of active power filters in radial distribution system with nonlinear
distributed generation using adaptive grey wolf optimizer. Engineering
Science and Technology, an International Journal, 24(4):911–924, 2021.
[90] X. Liu, Y. Tian, X. Lei, H. Wang, Z. Liu, and J. Wang. An improved self-
adaptive grey wolf optimizer for the daily optimal operation of cascade
pumping stations. Applied Soft Computing Journal, 75:473–493, 2019.
[91] W. Fu, K. Wang, J. Tan, and K. Shao. Vibration tendency prediction
approach for hydropower generator fused with multiscale dominant
ingredient chaotic analysis, adaptive mutation grey wolf optimizer, and
kelm. Complexity, 2020, 2020.
[92] L. Li, Y. Fu, J.C.H. Fung, H. Qu, and A.K.H. Lau.
Development of
a back-propagation neural network and adaptive grey wolf optimizer
algorithm for thermal comfort and energy consumption prediction and
optimization. Energy and Buildings, 253, 2021.
[93] Ananda Rabi Dhar, Dhrubajyoti Gupta, Shibendu Shekhar Roy,
Aditya Kumar Lohar, and Nilrudra Mandal. Covariance matrix adapted
grey wolf optimizer tuned extreme gradient boost for bi-directional
modelling of direct metal deposition process.
Expert Systems with
Applications, 199:116971, 2022.
[94] K. Meidani, A.P. Hemmasian, S. Mirjalili, and A. Barati Farimani.
Adaptive grey wolf optimizer.
Neural Computing and Applications,
34(10):7711–7731, 2022.
[95] Chao Lu, Liang Gao, Xinyu Li, Chengyu Hu, Xuesong Yan, and Wenyin
Gong. Chaotic-based grey wolf optimizer for numerical and engineering
optimization problems. Memetic Computing, 12(4):371–398, 2020.
[96] A. Saxena, R. Kumar, and S. Das. β-chaotic map enabled grey wolf
optimizer. Applied Soft Computing Journal, 75:84–105, 2019.
[97] Z. Zhang and W.-C. Hong. Application of variational mode decomposi-
tion and chaotic grey wolf optimizer with support vector regression for
forecasting electric loads. Knowledge-Based Systems, 228, 2021.
[98] Jing Li and Fan Yang. Task assignment strategy for multi-robot based
on improved grey wolf optimizer. Journal of Ambient Intelligence and
Humanized Computing, 11(12):6319–6335, 2020.
[99] Jiao Hu, Ali Asghar Heidari, Lejun Zhang, Xiao Xue, Wenyong Gui,
Huiling Chen, and Zhifang Pan. Chaotic diffusion-limited aggregation
enhanced grey wolf optimizer: insights, analysis, binarization, and fea-
ture selection. International Journal of Intelligent Systems, 37(8):4864–
4927, 2022.
[100] X. Wang, H. Zhao, T. Han, H. Zhou, and C. Li. A grey wolf optimizer
using gaussian estimation of distribution and its application in the multi-
uav multi-target urban tracking problem.
Applied Soft Computing
Journal, 78:240–260, 2019.
[101] S. Khalilpourazari, H. Hashemi Doulabi, A. Özyüksel Çiftçio˘glu, and
G.-W. Weber. Gradient-based grey wolf optimizer with gaussian walk:
Application in modelling and prediction of the covid-19 pandemic.
Expert Systems with Applications, 177, 2021.
[102] Can-Ming Yang, Ye Liu, Yi-Ting Wang, Yan-Ping Li, Wen-Hui Hou,
Sheng Duan, and Jian-Qiang Wang. A novel adaptive kernel picture fuzzy
c-means clustering algorithm based on grey wolf optimizer algorithm.
Symmetry, 14(7):1442, 2022.
[103] K. Luo. Enhanced grey wolf optimizer with a model for dynamically
estimating the location of the prey. Applied Soft Computing Journal,
77:225–235, 2019.
[104] F. Yan, J. Xu, and K. Yun. Dynamically dimensioned search grey wolf
optimizer based on positional interaction information. Complexity, 2019,
2019.
[105] X. Yu, W.Y. Xu, X. Wu, and X. Wang. Reinforced exploitation and ex-
ploration grey wolf optimizer for numerical and real-world optimization
problems. Applied Intelligence, 2021.
[106] W. Long, J. Jiao, X. Liang, S. Cai, and M. Xu. A random opposition-
based learning grey wolf optimizer. IEEE Access, 7:113810–113825,
2019.
[107] Z.-K. Feng, S. Liu, W.-J. Niu, Y. Liu, B. Luo, S.-M. Miao, and S. Wang.
Optimal operation of hydropower system by improved grey wolf opti-
mizer based on elite mutation and quasi-oppositional learning.
IEEE
Access, 7:155513–155529, 2019.
[108] W. Long, T. Wu, S. Cai, X. Liang, J. Jiao, and M. Xu. A novel grey wolf
optimizer algorithm with refraction learning.
IEEE Access, 7:57805–
57819, 2019.
[109] R. Guttula and V.R. Nandanavanam. Patch antenna design optimization
using opposition based grey wolf optimizer and map-reduce framework.
Data Technologies and Applications, 54(1):103–120, 2020.
[110] R. Chen, B. Yang, S. Li, S. Wang, and Q. Cheng. An effective multi-
population grey wolf optimizer based on reinforcement learning for flow
shop scheduling problem with multi-machine collaboration. Computers
and Industrial Engineering, 162, 2021.
[111] S. Gupta and K. Deep. An opposition-based chaotic grey wolf optimizer
for global optimisation tasks. Journal of Experimental and Theoretical
Artificial Intelligence, 31(5):751–779, 2019.
[112] Jagdish Chand Bansal and Shitu Singh. A better exploration strategy in
grey wolf optimizer. Journal of Ambient Intelligence and Humanized
Computing, 12(1):1099–1118, 2021.
[113] Yongliang Yuan, Xiaokai Mu, Xiangyu Shao, Jianji Ren, Yong Zhao, and
Zhenxi Wang. Optimization of an auto drum fashioned brake using the
elite opposition-based learning and chaotic k-best gravitational search
strategy based grey wolf optimizer algorithm. Applied Soft Computing,
123:108947, 2022.
[114] M. Elsisi. Improved grey wolf optimizer based on opposition and quasi
learning approaches for optimization: case study autonomous vehicle
including vision system.
Artificial Intelligence Review, 55(7):5597–
5620, 2022.
[115] Y. Wang, C. Jin, Q. Li, T. Hu, Y. Xu, C. Chen, Y. Zhang, and Z. Yang.
A dynamic opposite learning-assisted grey wolf optimizer. Symmetry,
14(9), 2022.
[116] F. Rezaei, H.R. Safavi, M.A. Elaziz, S.H.A. El-Sappagh, M.A. Al-Betar,
and T. Abuhmed. An enhanced grey wolf optimizer with a velocity-aided
global search mechanism. Mathematics, 10(3), 2022.
[117] L. Sun, B. Feng, T. Chen, D. Zhao, and Y. Xin. Equalized grey wolf
optimizer with refraction opposite learning. Computational Intelligence
and Neuroscience, 2022, 2022.
[118] Q. Tu, X. Chen, and X. Liu. Hierarchy strengthened grey wolf optimizer
for numerical optimization and feature selection. IEEE Access, 7:78012–
78028, 2019.
[119] K. Ezhilsabareesh, R. Suchithra, and A. Samad. Performance enhance-
ment of an impulse turbine for owc using grouped grey wolf optimizer
based controller. Ocean Engineering, 190, 2019.
[120] Alma Rodríguez, Octavio Camarena, Erik Cuevas, Itzel Aranguren,
Arturo Valdivia-G, Bernardo Morales-Castañeda, Daniel Zaldívar, and
Marco Pérez-Cisneros.
Group-based synchronous-asynchronous grey
wolf optimizer. Applied Mathematical Modelling, 93:226–243, 2021.
[121] M. AlShabi, C. Ghenai, M. Bettayeb, F.F. Ahmad, and M. El Haj As-
sad. Multi-group grey wolf optimizer (mg-gwo) for estimating photo-
voltaic solar cell model. Journal of Thermal Analysis and Calorimetry,
144(5):1655–1670, 2021.
[122] Nabanita Banerjee and Sumitra Mukhopadhyay. Ap-tlb-igwo: Adult-pup
teaching–learning based interactive grey wolf optimizer for numerical
optimization. Applied Soft Computing, 124:109000, 2022.
[123] M. Liu, K. Luo, J. Zhang, and S. Chen.
A stock selection algorithm
hybridizing grey wolf optimizer and support vector regression. Expert
Systems with Applications, 179, 2021.
[124] A. Alejo-Reyes, E. Cuevas, A. Rodríguez, A. Mendoza, and E. Olivares-
Benitez. An improved grey wolf optimizer for a supplier selection and
order quantity allocation problem. Mathematics, 8(9), 2020.
[125] Z. Miao, X. Yuan, F. Zhou, X. Qiu, Y. Song, and K. Chen. Grey wolf
optimizer with an enhanced hierarchy and its application to the wireless
sensor network coverage optimization problem. Applied Soft Computing
Journal, 96, 2020.
[126] H. Komijani, M. Masoumnezhad, M.M. Zanjireh, and M. Mir. Robust
hybrid fractional order proportional derivative sliding mode controller
for robot manipulator based on extended grey wolf optimizer. Robotica,
2019.
[127] M. Rahmani, H. Komijani, and M.H. Rahman. New sliding mode control
of 2-dof robot manipulator based on extended grey wolf optimizer.
International Journal of Control, Automation and Systems, 18(6):1572–
1580, 2020.
[128] S. Li, K. Xu, G. Xue, J. Liu, and Z. Xu. Prediction of coal spontaneous
combustion temperature based on improved grey wolf optimizer algo-
rithm and support vector regression. Fuel, 324, 2022.
32
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 33 -->
## Page 33

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
[129] X. Ma, X. Mei, W. Wu, X. Wu, and B. Zeng. A novel fractional time
delayed grey model with grey wolf optimizer and its applications in
forecasting the natural gas and coal consumption in chongqing china.
Energy, 178:487–507, 2019.
[130] W.-J. Niu, Z.-K. Feng, S. Liu, Y.-B. Chen, Y.-S. Xu, and J. Zhang.
Multiple hydropower reservoirs operation by hyperbolic grey wolf opti-
mizer based on elitism selection and adaptive mutation. Water Resources
Management, 35(2):573–591, 2021.
[131] P. Hu, S. Chen, H. Huang, G. Zhang, and L. Liu. Improved alpha-guided
grey wolf optimizer. IEEE Access, 7:5421–5437, 2019.
[132] D.O. Sidea, I.I. Picioroaga, and C. Bulac. Optimal battery energy storage
system scheduling based on mutation-improved grey wolf optimizer
using gpu-accelerated load flow in active distribution networks. IEEE
Access, 9:13922–13937, 2021.
[133] S. Singh and J.C. Bansal.
Mutation-driven grey wolf optimizer with
modified search mechanism[formula presented]. Expert Systems with
Applications, 194, 2022.
[134] Habes Alkhrisat, Lamees Mohammad Dalbah, Mohammed Azmi Al-
Betar, Mohammed A Awadallah, Khaled Assaleh, and Mohamed De-
riche. Size optimization of truss structures using improved grey wolf
optimizer. IEEE Access, 2023.
[135] M.H. Nadimi-Shahraki, S. Taghian, and S. Mirjalili. An improved grey
wolf optimizer for solving engineering problems. Expert Systems with
Applications, 166, 2021.
[136] C. Wang, L. Zhao, X. Li, and Y. Li. An improved grey wolf optimizer for
welding shop inverse scheduling. Computers and Industrial Engineering,
163, 2022.
[137] K. Meng, Q. Tang, Z. Zhang, and C. Yu.
Solving multi-objective
model of assembly line balancing considering preventive maintenance
scenarios using heuristic and grey wolf optimizer algorithm. Engineering
Applications of Artificial Intelligence, 100, 2021.
[138] S. Gupta and K. Deep. A memory-based grey wolf optimizer for global
optimization tasks. Applied Soft Computing Journal, 93, 2020.
[139] S. Gupta and K. Deep.
Enhanced leadership-inspired grey wolf opti-
mizer for global optimization problems. Engineering with Computers,
36(4):1777–1800, 2020.
[140] G. Huang, Y. Cai, J. Liu, Y. Qi, and X. Liu. A novel hybrid discrete
grey wolf optimizer algorithm for multi-uav path planning. Journal of
Intelligent and Robotic Systems: Theory and Applications, 103(3), 2021.
[141] Ali S Alghamdi. Greedy sine-cosine non-hierarchical grey wolf optimizer
for solving non-convex economic load dispatch problems.
Energies,
15(11):3904, 2022.
[142] R.A. Khanum, M.A. Jan, A. Aldegheishem, A. Mehmood, N. Alrajeh,
and A. Khanan. Two new improved variants of grey wolf optimizer for
unconstrained optimization. IEEE Access, 8:30805–30825, 2020.
[143] Qiang Zou, Li Liao, Yi Ding, and Hui Qin. Flood classification based on
a fuzzy clustering iteration model with combined weight and an immune
grey wolf optimizer algorithm. Water, 11(1):80, 2019.
[144] Rahul Kumar Vijay and Satyasai Jagannath Nanda. A quantum grey wolf
optimizer based declustering model for analysis of earthquake catalogs
in an ergodic framework. Journal of Computational Science, 36:101019,
2019.
[145] Mahdi Azizi, Siamak Talatahari, and Agathoklis Giaralis. Active vibra-
tion control of seismically excited building structures by upgraded grey
wolf optimizer. IEEE Access, 9:166658–166673, 2021.
[146] F. Yan, X. Xu, and J. Xu. Grey wolf optimizer with a novel weighted
distance for global optimization. IEEE Access, 8:120173–120197, 2020.
[147] T.-L. Le, T.-T. Huynh, and S.K. Hong. A modified grey wolf optimizer for
optimum parameters of multilayer type-2 asymmetric fuzzy controller.
IEEE Access, 8:121611–121629, 2020.
[148] K. Guo, L. Cui, M. Mao, L. Zhou, and Q. Zhang. An improved gray
wolf optimizer mppt algorithm for pv system with bfbic converter under
partial shading. IEEE Access, 8:103476–103490, 2020.
[149] M.W. Guo, J.S. Wang, L.F. Zhu, S.S. Guo, and W. Xie. An improved grey
wolf optimizer based on tracking and seeking modes to solve function
optimization problems. IEEE Access, 8:69861–69893, 2020.
[150] Z. Wang and H. Xie. Wireless sensor network deployment of 3d surface
based on enhanced grey wolf optimizer. IEEE Access, 8:57229–57251,
2020.
[151] A. Seyyedabbasi and F. Kiani. I-gwo and ex-gwo: improved algorithms
of the grey wolf optimizer to solve global optimization problems. Engi-
neering with Computers, 37(1):509–532, 2021.
[152] Q. Tu, X. Chen, and X. Liu. Multi-strategy ensemble grey wolf optimizer
and its application to feature selection. Applied Soft Computing Journal,
76:16–30, 2019.
[153] H. Xing, X. Zhou, X. Wang, S. Luo, P. Dai, K. Li, and H. Yang. An integer
encoding grey wolf optimizer for virtual network function placement.
Applied Soft Computing Journal, 76:575–594, 2019.
[154] Y. Zhou, X. Yang, L. Tao, and L. Yang.
Transformer fault diagnosis
model based on improved gray wolf optimizer and probabilistic neural
network. Energies, 14(11), 2021.
[155] J. Xie, X. Li, and L. Gao.
Disassembly sequence planning based on
a modified grey wolf optimizer.
International Journal of Advanced
Manufacturing Technology, 116(11-12):3731–3750, 2021.
[156] Y. Yang, B. Yang, S. Wang, W. Liu, and T. Jin.
An improved grey
wolf optimizer algorithm for energy-aware service composition in cloud
manufacturing. International Journal of Advanced Manufacturing Tech-
nology, 105(7-8):3079–3091, 2019.
[157] O.A. Alomari, S.N. Makhadmeh, M.A. Al-Betar, Z.A.A. Alyasseri, I.A.
Doush, A.K. Abasi, M.A. Awadallah, and R.A. Zitar.
Gene selection
for microarray data classification based on gray wolf optimizer enhanced
with triz-inspired operators. Knowledge-Based Systems, 223, 2021.
[158] H. Qin, T. Meng, and Y. Cao. Fuzzy strategy grey wolf optimizer for
complex multimodal optimization problems. Sensors, 22(17), 2022.
[159] B. Wang, L. Liu, Y. Li, and M. Khishe. Robust grey wolf optimizer for
multimodal optimizations: A cross-dimensional coordination approach.
Journal of Scientific Computing, 92(3), 2022.
[160] X. Yu, W.Y. Xu, X. Wu, and X. Wang. Reinforced exploitation and ex-
ploration grey wolf optimizer for numerical and real-world optimization
problems. Applied Intelligence, 52(8):8412–8427, 2022.
[161] M.H. Nadimi-Shahraki, S. Taghian, S. Mirjalili, H. Zamani, and
A. Bahreininejad. Ggwo: Gaze cues learning-based grey wolf optimizer
and its applications for solving engineering problems. Journal of Com-
putational Science, 61, 2022.
[162] R. Jarray, M. Al-Dhaifallah, H. Rezk, and S. BouallÃ¨gue. Parallel co-
operative coevolutionary grey wolf optimizer for path planning problem
of unmanned aerial vehicles. Sensors, 22(5), 2022.
[163] Sharif Naser Makhadmeh, Ahamad Tajudin Khader, Mohammed Azmi
Al-Betar, Syibrah Naim, Ammar Kamal Abasi, and Zaid Abdi Alka-
reem Alyasseri. A novel hybrid grey wolf optimizer with min-conflict
algorithm for power scheduling problem in a smart home. Swarm and
Evolutionary Computation, 60:100793, 2021.
[164] X. Guo, Z. Zhang, L. Qi, S. Liu, Y. Tang, and Z. Zhao. Stochastic hybrid
discrete grey wolf optimizer for multi-objective disassembly sequencing
and line balancing planning in disassembling multiple products. IEEE
Transactions on Automation Science and Engineering, 2021.
[165] A. Hoballah, D.-E.A. Mansour, and I.B.M. Taha. Hybrid grey wolf op-
timizer for transformer fault diagnosis using dissolved gases considering
uncertainty in measurements. IEEE Access, 8:139176–139187, 2020.
[166] E.-S.M. El-Kenawy, M.M. Eid, M. Saber, and A. Ibrahim. Mbgwo-sfs:
Modified binary grey wolf optimizer based on stochastic fractal search
for feature selection. IEEE Access, 8:107635–107649, 2020.
[167] A.M. Helmi, M.A.A. Al-Qaness, A. Dahou, R. Damaševiˇcius, T. Krilav-
iˇcius, and M.A. Elaziz. A novel hybrid gradient-based optimizer and grey
wolf optimizer feature selection method for human activity recognition
using smartphone sensors. Entropy, 23(8), 2021.
[168] M.A. Al-Betar, M.A. Awadallah, and M.M. Krishan.
A non-convex
economic load dispatch problem with valve loading effect using a hybrid
grey wolf optimizer. Neural Computing and Applications, 32(16):12127–
12154, 2020.
[169] L. Sun, C. Tang, M. Xu, and Z. Lei. Sub-pixel displacement measure-
ment based on the combination of a gray wolf optimizer and gradient
algorithm. Applied Optics, 60(4):901–911, 2021.
[170] H. Qin, P. Fan, H. Tang, P. Huang, B. Fang, and S. Pan. An effective
hybrid discrete grey wolf optimizer for the casting production scheduling
problem with multi-objective and multi-constraint.
Computers and
Industrial Engineering, 128:458–476, 2019.
[171] Jianzhong Xu, Fu Yan, Kumchol Yun, Lifei Su, Fengshu Li, and Jun
Guan.
Noninferior solution grey wolf optimizer with an independent
local search mechanism for solving economic load dispatch problems.
Energies, 12(12):2274, 2019.
[172] Xiwang Guo, Zhiwei Zhang, Liang Qi, Shixin Liu, Ying Tang, and Ziyan
Zhao. Stochastic hybrid discrete grey wolf optimizer for multi-objective
disassembly sequencing and line balancing planning in disassembling
multiple products.
IEEE Transactions on Automation Science and
Engineering, 19(3):1744–1756, 2021.
VOLUME 4, 2016
33
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 34 -->
## Page 34

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
[173] O.A. Alomari, A. Elnagar, I. Afyouni, I. Shahin, A.B. Nassif, I.A.
Hashem, and M. Tubishat. Hybrid feature selection based on principal
component analysis and grey wolf optimizer algorithm for arabic news
article classification. IEEE Access, 10:121816–121830, 2022.
[174] S.K. Goudos, T.V. Yioultsis, A.D. Boursianis, K.E. Psannis, and
K. Siakavara. Application of new hybrid jaya grey wolf optimizer to
antenna design for 5g communications systems. IEEE Access, 7:71061–
71071, 2019.
[175] C. Qu, W. Gai, M. Zhong, and J. Zhang. A novel reinforcement learning
based grey wolf optimizer algorithm for unmanned aerial vehicles (uavs)
path planning. Applied Soft Computing Journal, 89, 2020.
[176] R. Al-Wajih, S.J. Abdulkadir, N. Aziz, Q. Al-Tashi, and N. Talpur. Hybrid
binary grey wolf with harris hawks optimizer for feature selection. IEEE
Access, 2021.
[177] R.M. Rizk-Allah, A. Slowik, and A.E. Hassanien.
Hybridization of
grey wolf optimizer and crow search algorithm based on dynamic fuzzy
learning strategy for large-scale optimization. IEEE Access, 8:161593–
161611, 2020.
[178] G. Chen, M. Gao, Z. Zhang, and S. Li. Hybridization of chaotic grey
wolf optimizer and dragonfly algorithm for short-term hydrothermal
scheduling. IEEE Access, 8:142996–143020, 2020.
[179] A. Mouhou and A. Badri. Low integer-order approximation of fractional-
order systems using grey wolf optimizer-based cuckoo search algorithm.
Circuits, Systems, and Signal Processing, 2021.
[180] Hassan Y Mahmoud, Hany M Hasanien, Ahmed H Besheer, and Al-
moataz Y Abdelaziz.
Hybrid cuckoo search algorithm and grey wolf
optimiser-based optimal control strategy for performance enhancement
of hvdc-based offshore wind farms. IET Generation, Transmission &
Distribution, 14(10):1902–1911, 2020.
[181] W. Long, S. Cai, J. Jiao, M. Xu, and T. Wu. A new hybrid algorithm
based on grey wolf optimizer and cuckoo search for parameter extraction
of solar photovoltaic models. Energy Conversion and Management, 203,
2020.
[182] M. Karakoyun, A. Ozkis, and H. Kodaz. A new algorithm based on gray
wolf optimizer and shuffled frog leaping algorithm to solve the multi-
objective optimization problems. Applied Soft Computing Journal, 96,
2020.
[183] S. Gupta, K. Deep, H. Moayedi, L.K. Foong, and A. Assad. Sine cosine
grey wolf optimizer to solve engineering design problems. Engineering
with Computers, 37(4):3123–3149, 2021.
[184] Ji-Xiang Lv, Li-Jun Yan, Shu-Chuan Chu, Zhi-Ming Cai, Jeng-Shyang
Pan, Xian-Kang He, and Jian-Kai Xue. A new hybrid algorithm based on
golden eagle optimizer and grey wolf optimizer for 3d path planning of
multiple uavs in power inspection. Neural Computing and Applications,
34(14):11911–11936, 2022.
[185] S.N. Makhadmeh, A.K. Abasi, and M.A. Al-Betar. Hybrid multi-verse
optimizer with grey wolf optimizer for power scheduling problem in
smart home using iot. Journal of Supercomputing, 78(9):11794–11829,
2022.
[186] A. Saxena, R. Kumar, and S. Mirjalili. A harmonic estimator design with
evolutionary operators equipped grey wolf optimizer. Expert Systems
with Applications, 145, 2020.
[187] Anandbabu Gopatoti and P Vijayalakshmi. Cxgnet: A tri-phase chest
x-ray image classification for covid-19 diagnosis using deep cnn with en-
hanced grey-wolf optimizer. Biomedical Signal Processing and Control,
page 103860, 2022.
[188] Jie-Sheng Wang and Shu-Xia Li. An improved grey wolf optimizer based
on differential evolution and elimination mechanism. Scientific reports,
9(1):1–21, 2019.
[189] Mohamed A Tawhid and Abdelmonem M Ibrahim.
A hybridization
of grey wolf optimizer and differential evolution for solving nonlinear
systems. Evolving Systems, 11(1):65–87, 2020.
[190] Azam Davahli, Mahboubeh Shamsi, and Golnoush Abaei. Hybridizing
genetic algorithm and grey wolf optimizer to advance an intelligent and
lightweight intrusion detection system for iot wireless networks. Journal
of Ambient Intelligence and Humanized Computing, 11(11):5581–5609,
2020.
[191] X. Lei and H. Ouyang. Kernel-based intuitionistic fuzzy clustering image
segmentation based on grey wolf optimizer with differential mutation.
IEEE Access, 9:85455–85463, 2021.
[192] N.S. Mohsin, B.F. Abd, and R.S. Alhamadani. A hybrid grey wolf opti-
mizer with multi-population differential evolution for global optimization
problems. Periodicals of Engineering and Natural Sciences, 9(2):400–
409, 2021.
[193] H. Bouzary and F. Frank Chen. A hybrid grey wolf optimizer algorithm
with evolutionary operators for optimal qos-aware service composition
and optimal selection in cloud manufacturing. International Journal of
Advanced Manufacturing Technology, 101(9-12):2771–2784, 2019.
[194] X.Y. Li, J. Xie, Q.J. Ma, L. Gao, and P.G. Li.
Improved gray wolf
optimizer for distributed flexible job shop scheduling problem. Science
China Technological Sciences, 65(9):2105–2115, 2022.
[195] K. Yadav, B. Kumar, J.M. Guerrero, and A. Lashab. A hybrid genetic
algorithm and grey wolf optimizer technique for faster global peak
detection in pv system under partial shading. Sustainable Computing:
Informatics and Systems, 35, 2022.
[196] K. Chen, S. Laghrouche, and A. Djerdir. Remaining useful life prediction
for fuel cell based on support vector regression and grey wolf optimizer
algorithm.
IEEE Transactions on Energy Conversion, 37(2):778–787,
2022.
[197] H. Yang, Z. Wang, and K. Song. A new hybrid grey wolf optimizer-
feature weighted-multiple kernel-support vector regression technique to
predict tbm performance.
Engineering with Computers, 38(3):2469–
2485, 2022.
[198] I.A. Zamfirache, R.-E. Precup, R.-C. Roman, and E.M. Petriu. Policy it-
eration reinforcement learning-based control using a grey wolf optimizer
algorithm. Information Sciences, 585:162–175, 2022.
[199] M. Shariati, M.S. Mafipour, B. Ghahremani, F. Azarhomayun, M. Ah-
madi, N.T. Trung, and A. Shariati.
A novel hybrid extreme learning
machine–grey wolf optimizer (elm-gwo) model to predict compressive
strength of concrete with partial replacements for cement. Engineering
with Computers, 38(1):757–779, 2022.
[200] Iyad Abu Doush, Mohammad Qasem Bataineh, and Mohammed El-Abd.
The hybrid framework for multi-objective evolutionary optimization
based on harmony search algorithm. In First International Conference
on Real Time Intelligent Systems, pages 134–142. Springer, 2017.
[201] Sharif Naser Makhadmeh, Osama Ahmad Alomari, Seyedali Mirjalili,
Mohammed Azmi Al-Betar, and Ashraf Elnagar.
Recent advances in
multi-objective grey wolf optimizer, its versions and applications. Neural
Computing and Applications, 34(22):19723–19749, 2022.
[202] Prathap Siddavaatam and Reza Sedaghat. Grey wolf optimizer driven
design space exploration: A novel framework for multi-objective trade-
off in architectural synthesis.
Swarm and Evolutionary Computation,
49:44–61, 2019.
[203] Tusar Kanti Dash, Sandeep Singh Solanki, Ganapati Panda, and
Suresh Chandra Satapathy.
Development of statistical estimators for
speech enhancement using multi-objective grey wolf optimizer. Evolu-
tionary Intelligence, pages 1–12, 2020.
[204] C. Li, W. Wang, and D. Chen. Multi-objective complementary scheduling
of hydro-thermal-re power system via a multi-objective hybrid grey wolf
optimizer. Energy, 171:241–255, 2019.
[205] Karar Mahmoud, Mahmoud M Hussein, Mohamed Abdel-Nasser, and
Matti Lehtonen.
Optimal voltage control in distribution systems with
intermittent pv using multiobjective grey-wolf-lévy optimizer.
IEEE
Systems Journal, 14(1):760–770, 2019.
[206] N. Saini, S. Saha, A. Jangra, and P. Bhattacharyya.
Extractive single
document summarization using multi-objective optimization: Exploring
self-organized differential evolution, grey wolf optimizer and water cycle
algorithm. Knowledge-Based Systems, 164:45–67, 2019.
[207] S. Karasu and Z. Saraç.
Classification of power quality disturbances
by 2d-riesz transform, multi-objective grey wolf optimizer and machine
learning methods.
Digital Signal Processing: A Review Journal, 101,
2020.
[208] Saul Zapotecas-Martinez, Abel Garcia-Najera, and Antonio Lopez-
Jaimes. Multi-objective grey wolf optimizer based on decomposition.
Expert Systems with Applications, 120:357–371, 2019.
[209] D. Alsadie. Tsmgwo: Optimizing task schedule using multi-objectives
grey wolf optimizer for cloud data centers.
IEEE Access, 9:37707–
37725, 2021.
[210] D. Yousri, S.B. Thanikanti, K. Balasubramanian, A. Osama, and A. Fathy.
Multi-objective grey wolf optimizer for optimal design of switching
matrix for shaded pv array dynamic reconfiguration.
IEEE Access,
8:159931–159946, 2020.
[211] A. Darvish Falehi. Novel harmonic elimination strategy based on multi-
objective grey wolf optimizer to ameliorate voltage quality of odd-nary
multi-level structure. Heliyon, 6(3), 2020.
[212] M. Karakoyun, S. Gulcu, and H. Kodaz.
D-mosg: Discrete multi-
objective shuffled gray wolf optimizer for multi-level image thresholding.
Engineering Science and Technology, an International Journal, 2021.
34
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 35 -->
## Page 35

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
[213] Z. Zhu and X. Zhou. An efficient evolutionary grey wolf optimizer for
multi-objective flexible job shop scheduling problem with hierarchical
job precedence constraints. Computers and Industrial Engineering, 140,
2020.
[214] Y. Yang, B. Yang, S. Wang, T. Jin, and S. Li. An enhanced multi-objective
grey wolf optimizer for service composition in cloud manufacturing.
Applied Soft Computing Journal, 87, 2020.
[215] K. Li, G. Zhou, Y. Yang, F. Li, and Z. Jiao. A novel prediction method
for favorable reservoir of oil field based on grey wolf optimizer and twin
support vector machine. Journal of Petroleum Science and Engineering,
189, 2020.
[216] X. Li and Y.-X. Guo.
Multiobjective optimization design of aperture
illuminations for microwave power transmission via multiobjective grey
wolf optimizer.
IEEE Transactions on Antennas and Propagation,
68(8):6265–6276, 2020.
[217] S.M. Mirjalili, H. Taleb, M.Z. Kabir, and P. Bianucci. Design optimiza-
tion of orbital angular momentum fibers using the gray wolf optimizer.
Applied Optics, 59(20):6181–6190, 2020.
[218] H. Lu, X. Ma, K. Huang, and M. Azimi. Prediction of offshore wind farm
power using a novel two-stage model combining kernel-based nonlinear
extension of the arps decline model with a multi-objective grey wolf
optimizer. Renewable and Sustainable Energy Reviews, 127, 2020.
[219] M. Ghasemi, K. Bagherifard, H. Parvin, S. Nejatian, and K.-H. Pho.
Multi-objective whale optimization algorithm and multi-objective grey
wolf optimizer for solving next release problem with developing fairness
and uncertainty quality indicators.
Applied Intelligence, 51(8):5358–
5387, 2021.
[220] J. Liu, Z. Yang, and D. Li.
A multiple search strategies based grey
wolf optimizer for solving multi-objective optimization problems. Expert
Systems with Applications, 145, 2020.
[221] Avadh Kishor and Rajdeep Niyogi. A fair and efficient resource sharing
scheme using modified grey wolf optimizer. Evolutionary Intelligence,
pages 1–18, 2021.
[222] A. Safaei, R. Nassiri, and A.M. Rahmani. Enterprise service composition
in iiot manufacturing: integer linear optimization based on the hybrid
multi-objective grey wolf optimizer. International Journal of Advanced
Manufacturing Technology, 122(1):427–445, 2022.
[223] Sharif Naser Makhadmeh, Ammar Kamal Abasi, Mohammed Azmi Al-
Betar, Mohammed A Awadallah, Iyad Abu Doush, Zaid Abdi Alkareem
Alyasseri, and Osama Ahmad Alomari.
A novel link-based multi-
objective grey wolf optimizer for appliances energy scheduling problem.
Cluster Computing, 25(6):4355–4382, 2022.
[224] Y. Cao, T. Li, T. He, Y. Wei, M. Li, and F. Si. Multiobjective load dispatch
for coal fired power plants under renewable energy accommodation based
on a nondominated sorting grey wolf optimizer algorithm.
Energies,
15(8), 2022.
[225] L. Yin and Z. Sun.
Distributed multi-objective grey wolf optimizer
for distributed multi-objective economic dispatch of multi-area intercon-
nected power systems. Applied Soft Computing, 117, 2022.
[226] R. Claywell, L. Nadai, I. Felde, S. Ardabili, and A. Mosavi. Adaptive
neuro-fuzzy inference system and a multilayer perceptron model trained
with grey wolf optimizer for predicting solar diffuse fraction. Entropy,
22(11):1–14, 2020.
[227] M. Ragab, O.A. Omer, and M. Abdel-Nasser.
Compressive sensing
mri reconstruction using empirical wavelet transform and grey wolf
optimizer. Neural Computing and Applications, 32(7):2705–2724, 2020.
[228] Naveen Saini, Sriparna Saha, Anubhav Jangra, and Pushpak Bhat-
tacharyya.
Extractive single document summarization using multi-
objective optimization: Exploring self-organized differential evolution,
grey wolf optimizer and water cycle algorithm.
Knowledge-Based
Systems, 164:45–67, 2019.
[229] Zaid Abdi Alkareem Alyasseri, Osama Ahmad Alomari, Sharif Naser
Makhadmeh, Seyedali Mirjalili, Mohammed Azmi Al-Betar, Salwani
Abdullah, Nabeel Salih Ali, Joao P Papa, Douglas Rodrigues, and Am-
mar Kamal Abasi. Eeg channel selection for person identification using
binary grey wolf optimizer. Ieee Access, 10:10500–10513, 2022.
[230] P. Moradi, S. Hayati, and T. Ghahrizadeh. Modeling and optimization of
lead and cobalt biosorption from water with rafsanjan pistachio shell, us-
ing experiment based models of ann and gp, and the grey wolf optimizer.
Chemometrics and Intelligent Laboratory Systems, 202, 2020.
[231] S. Maroufpoor, O. Bozorg-Haddad, and E. Maroufpoor. Reference evap-
otranspiration estimating based on optimal input combination and hybrid
artificial intelligent model: Hybridization of artificial neural network with
grey wolf optimizer algorithm. Journal of Hydrology, 588, 2020.
[232] X. Qin, Y. Qiao, and G. Hu. Degree reduction of sg-bézier surfaces based
on grey wolf optimizer. Mathematical Methods in the Applied Sciences,
43(10):6416–6429, 2020.
[233] E.M. Golafshani, A. Behnood, and M. Arashpour. Predicting the com-
pressive strength of normal and high-performance concretes using ann
and anfis hybridized with grey wolf optimizer. Construction and Building
Materials, 232, 2020.
[234] T. Zeng, J. Wang, B. Cui, X. Wang, D. Wang, and Y. Zhang. The equip-
ment detection and localization of large-scale construction jobsite by far-
field construction surveillance video based on improving yolov3 and grey
wolf optimizer improving extreme learning machine. Construction and
Building Materials, 291, 2021.
[235] P. Majumder and T.I. Eldho. Artificial neural network and grey wolf op-
timizer based surrogate simulation-optimization model for groundwater
remediation. Water Resources Management, 34(2):763–783, 2020.
[236] A. Mosavi, S. Samadianfard, S. Darbandi, N. Nabipour, S.N. Qasem,
E. Salwana, and S. S. Band. Predicting soil electrical conductivity using
multi-layer perceptron integrated with grey wolf optimizer. Journal of
Geochemical Exploration, 220, 2021.
[237] K. Albina and S.G. Lee. Hybrid stochastic exploration using grey wolf
optimizer and coordinated multi-robot exploration algorithms.
IEEE
Access, 7:14246–14255, 2019.
[238] B. Martin, J. Marot, and S. Bourennane. Mixed grey wolf optimizer for
the joint denoising and unmixing of multispectral images. Applied Soft
Computing Journal, 74:385–410, 2019.
[239] X. Shu, T. Bao, Y. Hu, Y. Li, and K. Zhang. Camera calibration method
using synthetic speckle pattern with an improved gray wolf optimizer
algorithm. Applied Optics, 60(34):10477–10480, 2021.
[240] Y. Wang, Q. Zhu, H. Ma, and H. Yu. A hybrid gray wolf optimizer for
hyperspectral image band selection. IEEE Transactions on Geoscience
and Remote Sensing, 60, 2022.
[241] S. Gupta and K. Deep. An efficient grey wolf optimizer with opposition-
based learning and chaotic local search for integer and mixed-integer
optimization problems. Arabian Journal for Science and Engineering,
44(8):7277–7296, 2019.
[242] H. Xie, L. Zhang, and C.P. Lim. Evolving cnn-lstm models for time series
prediction using enhanced grey wolf optimizer. IEEE Access, 8:161519–
161541, 2020.
[243] S. Ramesh, S. Gomathi, S. Sasikala, and T.R. Saravanan.
Automatic
speech emotion detection using hybrid of gray wolf optimizer and naïve
bayes. International Journal of Speech Technology, 2021.
[244] Ammar Kamal Abasi, Ahamad Tajudin Khader, Mohammed Azmi Al-
Betar, Syibrah Naim, Sharif Naser Makhadmeh, and Zaid Abdi Alkareem
Alyasseri. An improved text feature selection for clustering using binary
grey wolf optimizer.
In Proceedings of the 11th National Technical
Seminar on Unmanned System Technology 2019: NUSYS’19, pages
503–516. Springer, 2021.
[245] Sharif Naser Makhadmeh, Ahamad Tajudin Khader, Mohammed Azmi
Al-Betar, and Syibrah Naim. An optimal power scheduling for smart
home appliances with smart battery using grey wolf optimizer. In 2018
8th IEEE international conference on control system, computing and
engineering (ICCSCE), pages 76–81. IEEE, 2018.
[246] Sharif Naser Makhadmeh, Ahamad Tajudin Khader, Mohammed Azmi
Al-Betar, and Syibrah Naim. Multi-objective power scheduling problem
in smart homes using grey wolf optimiser. Journal of Ambient Intelli-
gence and Humanized Computing, 10(9):3643–3667, 2019.
[247] Sharif Naser Makhadmeh, Ahamad Tajudin Khader, Mohammed Azmi
Al-Betar, Syibrah Naim, Zaid Abdi Alkareem Alyasseri, and Ammar Ka-
mal Abasi. Particle swarm optimization algorithm for power scheduling
problem using smart battery. In 2019 IEEE Jordan international joint con-
ference on electrical engineering and information technology (JEEIT),
pages 672–677. IEEE, 2019.
[248] Sharif Naser Makhadmeh, Mohammed Azmi Al-Betar, Zaid Abdi Alka-
reem Alyasseri, Ammar Kamal Abasi, Ahamad Tajudin Khader, Robertas
Damaševiˇcius, Mazin Abed Mohammed, and Karrar Hameed Abdulka-
reem.
Smart home battery for the multi-objective power scheduling
problem in a smart home using grey wolf optimizer.
Electronics,
10(4):447, 2021.
[249] C. Komathi and M.G. Umamaheswari. Design of gray wolf optimizer
algorithm-based fractional order pi controller for power factor correc-
tion in smps applications.
IEEE Transactions on Power Electronics,
35(2):2100–2118, 2020.
[250] S. Kumar, K.K. Mandal, and N. Chakraborty.
Optimal placement of
different types of dg units considering various load models using novel
VOLUME 4, 2016
35
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 36 -->
## Page 36

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
multiobjective quasi-oppositional grey wolf optimizer. Soft Computing,
25(6):4845–4864, 2021.
[251] M. Yesilbudak. Parameter extraction of photovoltaic cells and modules
using grey wolf optimizer with dimension learning-based hunting search
strategy. Energies, 14(18), 2021.
[252] T.E.K. Zidane, M.R.B. Adzman, M.F.N. Tajuddin, S. Mat Zali, and
A. Durusu.
Optimal configuration of photovoltaic power plant using
grey wolf optimizer: A comparative analysis considering cdte and c-si
pv modules. Solar Energy, 188:247–257, 2019.
[253] S. Hosseini-Hemati, S. Derafshi Beigvand, H. Abdi, and A. Rastgou.
Society-based grey wolf optimizer for large scale combined heat and
power economic dispatch problem considering power losses. Applied
Soft Computing, 117, 2022.
[254] A. Lipare, D.R. Edla, and V. Kuppili. Energy efficient load balancing
approach for avoiding energy hole problem in wsn using grey wolf
optimizer with novel fitness function. Applied Soft Computing Journal,
84, 2019.
[255] S.M.M.H. Daneshvar, P. Alikhah Ahari Mohajer, and S.M. Mazinani.
Energy-efficient routing in wsn: A centralized cluster-based approach via
grey wolf optimizer. IEEE Access, 7:170019–170031, 2019.
[256] A. Djerioui, A. Houari, M. Machmoum, and M. Ghanes.
Grey wolf
optimizer-based predictive torque control for electric buses applications.
Energies, 13(19), 2020.
[257] Q. Cao, Y. Liu, T. Zhao, K. Yang, C. Tang, R. Tao, D. Hu, and Y. Zhai.
Design of highly uniform magnetic field cylinder coils based on grey
wolf optimizer algorithm in atomic sensors.
IEEE Sensors Journal,
21(18):19922–19929, 2021.
[258] J. Gai, J. Shen, Y. Hu, and H. Wang. An integrated method based on hy-
brid grey wolf optimizer improved variational mode decomposition and
deep neural network for fault diagnosis of rolling bearing. Measurement:
Journal of the International Measurement Confederation, 162, 2020.
[259] B. Sathiyabhama, S.U. Kumar, J. Jayanthi, T. Sathiya, A.K. Ilavarasi,
V. Yuvarajan, and K. Gopikrishna. A novel feature selection framework
based on grey wolf optimizer for mammogram image analysis. Neural
Computing and Applications, 33(21):14583–14602, 2021.
[260] Xuehua Zhao, Hanfang Lv, Yizhao Wei, Shujin Lv, and Xueping Zhu.
Streamflow forecasting via two types of predictive structure-based gated
recurrent unit models. Water, 13(1):91, 2021.
[261] Xuehua Zhao, Hanfang Lv, Shujin Lv, Yuting Sang, Yizhao Wei, and
Xueping Zhu. Enhancing robustness of monthly streamflow forecasting
model using gated recurrent unit based on improved grey wolf optimizer.
Journal of Hydrology, 601:126607, 2021.
[262] Zixing Chen, Tao Jin, Xidong Zheng, Yulong Liu, Zhiyuan Zhuang,
and Mohamed A Mohamed.
An innovative method-based ceemdan–
igwo–gru hybrid algorithm for short-term load forecasting.
Electrical
Engineering, 104(5):3137–3156, 2022.
[263] Lening Zhao, Jie Li, Kaiqiang Feng, Xiaokai Wei, Jinhao Song, and
Yubing Jiao. A hybrid optimization algorithm for gwo fine-tuning gru-
aided akf during gps outage. Measurement, 206:112302, 2023.
[264] E. Ileri, A.D. Karaoglan, and S. Akpinar. Optimizing cetane improver
concentration in biodiesel-diesel blend via grey wolf optimizer algorithm.
Fuel, 273, 2020.
[265] O.D. Samuel, M.O. Okwu, O.J. Oyejide, E. Taghinezhad, A. Afzal, and
M. Kaveh. Optimizing biodiesel production from abundant waste oils
through empirical method and grey wolf optimizer. Fuel, 281, 2020.
[266] W. Xie, W.-Z. Wu, C. Liu, T. Zhang, and Z. Dong.
Forecasting fuel
combustion-related co2 emissions by a novel continuous fractional non-
linear grey bernoulli model with grey wolf optimizer.
Environmental
Science and Pollution Research, 28(28):38128–38144, 2021.
[267] Y. Zhao, Q. Wu, H. Li, S. Ma, P. He, J. Zhao, and Y. Li. Optimization of
thermal efficiency and unburned carbon in fly ash of coal-fired utility
boiler via grey wolf optimizer algorithm.
IEEE Access, 7:114414–
114425, 2019.
[268] M. Dorterler, I. Sahin, and H. Gokce. A grey wolf optimizer approach
for optimal weight design problem of the spur gear.
Engineering
Optimization, 51(6):1013–1027, 2019.
[269] Fei Qu, Yi-Ting Wang, Wen-Hui Hou, Xiao-Yu Zhou, Xiao-Kang Wang,
Jun-Bo Li, and Jian-Qiang Wang.
Forecasting of automobile sales
based on support vector regression optimized by the grey wolf optimizer
algorithm. Mathematics, 10(13):2234, 2022.
[270] J. Faria, J. Fermeiro, J. Pombo, M. Calado, and S. Mariano. Proportional
resonant current control and output-filter design optimization for grid-
tied inverters using grey wolf optimizer. Energies, 13(8), 2020.
[271] B. Farahmand Azar, H. Veladi, F. Raeesi, and S. Talatahari. Control of
the nonlinear building using an optimum inverse tsk model of mr damper
based on modified grey wolf optimizer.
Engineering Structures, 214,
2020.
[272] E. Mohammadi Golafshani, A. Behnood, and M.M. Karimi. Predicting
the dynamic modulus of asphalt mixture using hybridized artificial neural
network and grey wolf optimizer.
International Journal of Pavement
Engineering, 2021.
[273] M. Zhao, X. Wang, J. Yu, L. Bi, Y. Xiao, and J. Zhang. Optimization of
construction duration and schedule robustness based on hybrid grey wolf
optimizer with sine cosine algorithm. Energies, 13(1), 2020.
[274] M. Shariati, M.S. Mafipour, B. Ghahremani, F. Azarhomayun, M. Ah-
madi, N.T. Trung, and A. Shariati.
A novel hybrid extreme learning
machine–grey wolf optimizer (elm-gwo) model to predict compressive
strength of concrete with partial replacements for cement. Engineering
with Computers, 2020.
[275] A. Jaafari, M. Panahi, B.T. Pham, H. Shahabi, D.T. Bui, F. Rezaie,
and S. Lee.
Meta optimization of an adaptive neuro-fuzzy inference
system with grey wolf optimizer and biogeography-based optimization
algorithms for spatial prediction of landslide susceptibility.
Catena,
175:430–445, 2019.
[276] X. Zhao, H. Lv, S. Lv, Y. Sang, Y. Wei, and X. Zhu. Enhancing robustness
of monthly streamflow forecasting model using gated recurrent unit based
on improved grey wolf optimizer. Journal of Hydrology, 601, 2021.
[277] E. Uzlu.
Estimates of greenhouse gas emission in turkey with grey
wolf optimizer algorithm-optimized artificial neural networks. Neural
Computing and Applications, 33(20):13567–13585, 2021.
[278] R.K. Dewangan, A. Shukla, and W.W. Godfrey.
Three dimensional
path planning using grey wolf optimizer for uavs. Applied Intelligence,
49(6):2201–2217, 2019.
[279] X. Yan, Y. Zhang, D. Zhang, and N. Hou. Multimodal image registration
using histogram of oriented gradient distance and data-driven grey wolf
optimizer. Neurocomputing, 392:108–120, 2020.
[280] H.M. Ahmed, B.A.B. Youssef, A.S. Elkorany, Z.F. Elsharkawy, A.A.
Saleeb, and F.A. El-Samie.
Hybridized classification approach for
magnetic resonance brain images using gray wolf optimizer and support
vector machine.
Multimedia Tools and Applications, 78(19):27983–
28002, 2019.
[281] B. Dappuri, M.P. Rao, and M.B. Sikha.
Non-blind rgb watermark-
ing approach using svd in translation invariant wavelet space with en-
hanced grey-wolf optimizer. Multimedia Tools and Applications, 79(41-
42):31103–31124, 2020.
[282] Y. Feng, J. Tang, B. Su, Q. Su, and Z. Zhou. Point cloud registration
algorithm based on the grey wolf optimizer. IEEE Access, 8:143375–
143382, 2020.
[283] A.A. Alomoush, A.A. Alsewari, H.S. Alamri, K. Aloufi, and K.Z. Zamli.
Hybrid harmony search algorithm with grey wolf optimizer and modified
opposition-based learning. IEEE Access, 7:68764–68785, 2019.
[284] Ahmad Al-Momani, Omar Mohamed, and Wejdan Abu Elhaija. Multiple
processes modeling and identification for a cleaner supercritical power
plant via grey wolf optimizer. Energy, 252:124090, 2022.
[285] A. Korashy, S. Kamel, L. Nasrat, and F. Jurado.
Developed
multi-objective grey wolf optimizer with fuzzy logic decision-making
tool for direction overcurrent relays coordination.
Soft Computing,
24(17):13305–13317, 2020.
[286] A. Naderipour, Z. Abdul Malek, M. Zahedi Vahid, Z. Mirzaei Seifabad,
M. Hajivand, and S. Arabi Nowdeh. Optimal, reliable and cost-effective
framework of photovoltaic-wind-battery energy system design consider-
ing outage concept using grey wolf optimizer algorithm - case study for
iran. IEEE Access, 7:182611–182623, 2019.
[287] A. Lakum and V. Mahajan. Optimal placement and sizing of multiple
active power filters in radial distribution system using grey wolf optimizer
in presence of nonlinear distributed generation. Electric Power Systems
Research, 173:281–290, 2019.
[288] Y. Wang, R. Nie, X. Ma, Z. Liu, P. Chi, W. Wu, B. Guo, X. Yang,
and L. Zhang. A novel hausdorff fractional ngmc(p,n) grey prediction
model with grey wolf optimizer and its applications in forecasting energy
production and conversion of china. Applied Mathematical Modelling,
97:381–397, 2021.
[289] D. Hasterok, R. Castro, M. Landrat, K. Piko´n, M. Doepfert, and
H. Morais. Polish energy transition 2040: Energy mix optimization using
grey wolf optimizer. Energies, 14(2), 2021.
36
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 37 -->
## Page 37

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
[290] J. Zhang, X. Wang, and L. Ma. An optimal power allocation scheme of
microgrid using grey wolf optimizer. IEEE Access, 7:137608–137619,
2019.
[291] X. Li and K.M. Luk.
The grey wolf optimizer and its applications
in electromagnetics. IEEE Transactions on Antennas and Propagation,
68(3):2186–2197, 2020.
[292] R.S. Suriavel Rao and P. Malathi.
A novel pts: grey wolf optimizer-
based papr reduction technique in ofdm scheme for high-speed wireless
applications. Soft Computing, 23(8):2701–2712, 2019.
[293] N. Sugawara, T. Fujisawa, K. Nakamura, Y. Sawada, T. Mori,
T. Sakamoto, R. Imada, T. Matsui, K. Nakajima, and K. Saitoh. Modal
amplitude and phase estimation of multimode near field patterns based
on artificial neural network with the help of grey-wolf-optimizer. Optical
Fiber Technology, 67, 2021.
[294] Y. Dai, D. Wu, S. Yu, and Y. Yan.
Robust control of underwater
vehicle-manipulator system using grey wolf optimizer-based nonlinear
disturbance observer and h-infinity controller. Complexity, 2020, 2020.
[295] R. Al-Wajih, S.J. Abdulkadir, N. Aziz, Q. Al-Tashi, and N. Talpur. Hybrid
binary grey wolf with harris hawks optimizer for feature selection. IEEE
Access, 9:31662–31677, 2021.
[296] M. Abdel-Basset, K.M. Sallam, R. Mohamed, I. Elgendi, K. Munasinghe,
and O.M. Elkomy. An improved binary grey-wolf optimizer with simu-
lated annealing for feature selection. IEEE Access, 9:139792–139822,
2021.
[297] F. Xie, C. Lei, F. Li, D. Huang, and J. Yang. Unsupervised hyperspectral
feature selection based on fuzzy c-means and grey wolf optimizer.
International Journal of Remote Sensing, 40(9):3344–3367, 2019.
[298] A. Hamed and H. Nassar.
Efficient feature selection for inconsistent
heterogeneous information systems based on a grey wolf optimizer and
rough set theory. Soft Computing, 25(24):15115–15130, 2021.
[299] A.A. Heidari, R. Ali Abbaspour, and H. Chen. Efficient boosted grey
wolf optimizers for global search and kernel extreme learning machine
training. Applied Soft Computing Journal, 81, 2019.
[300] W. Long, S. Cai, J. Jiao, and M. Tang.
An efficient and robust grey
wolf optimizer algorithm for large-scale numerical optimization. Soft
Computing, 24(2):997–1026, 2020.
[301] Mukaram Safaldin, Mohammed Otair, and Laith Abualigah. Improved
binary gray wolf optimizer and svm for intrusion detection system in
wireless sensor networks. Journal of ambient intelligence and humanized
computing, 12(2):1559–1576, 2021.
[302] Karuna Panwar and Kusum Deep. Transformation operators based grey
wolf optimizer for travelling salesman problem. Journal of Computa-
tional Science, 55:101454, 2021.
[303] Bilal H Abed-alguni and Malek Barhoush. Distributed grey wolf opti-
mizer for numerical optimization problems. Jordanian J. Comput. Inf.
Technol.(JJCIT), 4(03), 2018.
[304] David H Wolpert and William G Macready. No free lunch theorems for
optimization. IEEE transactions on evolutionary computation, 1(1):67–
82, 1997.
[305] Ting Yee Lim.
Structured population genetic algorithms: a literature
survey. Artificial Intelligence Review, 41(3):385–399, 2014.
[306] Bilal H Abed-Alguni and Noor Aldeen Alawad. Distributed grey wolf
optimizer for scheduling of workflow applications in cloud environments.
Applied Soft Computing, 102:107113, 2021.
[307] Iyad Abu Doush and Mohammad Qasem Bataineh. Hybedrized nsga-ii
and moea/d with harmony search algorithm to solve multi-objective op-
timization problems. In International Conference on Neural Information
Processing, pages 606–614. Springer, 2015.
[308] Iyad Abu Doush, Mohammed El-Abd, Abdelaziz I Hammouri, and
Mohammad Qasem Bataineh. The effect of different stopping criteria
on multi-objective optimization algorithms.
Neural Computing and
Applications, pages 1–31, 2021.
SHARIF NASER MAKHADMEH is a full-time
research associate (FTRA) at Artificial Intelli-
gence Research Center (AIRC) - Ajman Univer-
sity, United Arab Emirates. He received his B.Sc.
in Computer Science from Yarmouk University,
Jordan, in 2013 and MSc in Information Technol-
ogy from the Universiti Utara Malaysia (UUM),
Malaysia, in 2015. He obtained a PhD degree
in Artificial Intelligence from Universiti Sains
Malaysia (USM), Malaysia, in 2020. His research
interests include optimization algorithms, artificial intelligence, engineering
and scheduling problem, smart home.
MOHAMMED AZMI AL-BETAR is an associate
professor at the Master of Artificial Intelligence
(MSAI) program in the Collage of Engineering
and IT at Ajman University and previously was at
the Department of Computer Science in Al-Balqa
Applied University, Irbid, Jordan. He is currently
the director of the Artificial Intelligence Research
Center (AIRC) and a Head of the Evolutionary
computation research group which publish more
than 175 scientific publications in high quality and
well-reputed journals and conferences. Dr. Al-Betar ranked in Stanford study
of the world’s top 2% of scientists. His research interests are mainly directed
to metaheuristic optimization methods and hard combinatorial optimisation
problems including Scheduling, engineering and Timetabling.
VOLUME 4, 2016
37
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---

<!-- Page 38 -->
## Page 38

Author et al.: Preparation of Papers for IEEE TRANSACTIONS and JOURNALS
IYAD ABU DOUSH Iyad Abu Doush is a profes-
sor of computer science at the American Univer-
sity of Kuwait. Since 2020, he served as the direc-
tor of the Office of Research and Grants. Dr. Abu
Doush is a consultant in technology accessibility
and an invited expert in Mada (Qatar Assistive
Technology Center). Dr. Abu Doush is a certi-
fied ABET program evaluator (PEV) since March
2021. In 2001 and 2005 respectively, Dr. Abu
Doush was awarded a scholarship from Yarmouk
University to study M.Sc. and Ph.D. in computer science. He obtained
his Ph.D. from the Computer Science Department at New Mexico State
University / USA in 2009. In April 2009, he was awarded a merit-based
enhancement fellowship from graduate school for outstanding service to
New Mexico State University as a teaching and research assistant. Dr. Abu
Doush served as coach and committee member in the ACM Jordanian
Collegiate Programming Contest (JCPC) for three years and the Kuwaiti
Collegiate Programming Contest (KCPC) for two years. He won with one
team in the 2014 JCPC and with two teams the second and third place in the
2017 KCPC. The capstone project team he supervises won the best project
at the 2021 College of Engineering Capstone Projects Fair. Dr. Abu Doush
has been funded several times to do research in his areas of expertise by
different agencies including USAID, Microsoft, King Abdullah II Design &
Development Bureau, Deanship of Research & Graduate Studies at Yarmouk
University, Jordanian Scientific Research Support Fund, and the American
University of Kuwait. Dr. Abu Doush secured a fund in 2016 from USAID to
establish the first accessible computer laboratory for people with disabilities
in northern Jordan at Yarmouk University. Dr. Abu Doush was assigned as
the head of the Computer Science Department at Yarmouk University from
2011 to 2012. Dr. Abu Doush was selected to serve as a visiting researcher
in the Universities of Malaysia, Lithuania, and the USA. Dr. Abu Doush has
published more than 90 articles in international journals and conferences. He
has high h-index and citation records. Dr. Abu Doush served as a reviewer
and committee member of several specialized international journals and
conferences. His research interests include optimization algorithms, machine
learning, human-computer interaction, and accessibility.
MOHAMMED A. AWADALLAH Mohammed A.
Awadallah is an Associate Professor of artificial
intelligence, in the department of computer &
information sciences at Al-Aqsa University, Gaza,
Palestine. He was a dean of the faculty of comput-
ers and information sciences at Al-Aqsa Univer-
sity from July 2018 to November 2021. In addi-
tion, he was appointed as an adjunct research as-
sociate (ARA) at Artificial Intelligence Research
Center (AIRC) at Ajman University, the United
Arab Emirates in February 2021. He was listed as one of the top 2% of
top-cited scientists in the world according to Stanford University indicator
in 2022. The main research interest of Dr. Awadallah is in the area of applied
computing where many real-world complex problems are being solved using
metaheuristic-based optimization methods. He has published more than 90
research papers in international journals and conferences. Furthermore, he
serves as a reviewer and editor for numerous conferences and journals of
high repute.
SOFIAN KASSAYMEH Sofian Kassaymeh re-
ceived his Ph.D. degree in AI and Software Engi-
neering from UKM University, Malaysia, in 2021.
He is currently an assistant professor in the Soft-
ware Engineering Department at AUT Univer-
sity, Jordan. His current research interests include
combinatorial optimization, machine learning, and
metaheuristics.
SEYEDALI MIRJALILI Seyedali Mirjalili is a
Professor at the Center for Artificial Intelligence
Research and Optimization at Torrens University.
He has gained international recognition for his
contributions to nature-inspired artificial intelli-
gence techniques, with over 500 published works
that have received more than 80,000 citations and
an H-index of 85. He has been on the list of the
top 1% of highly-cited researchers since 2019, and
Web of Science named him one of the most influ-
ential researchers in the world. In 2022 and 2023, The Australian newspaper
recognized him as a global leader in Artificial Intelligence and a national
leader in the Evolutionary Computation and Fuzzy Systems fields. He serves
as a senior member of IEEE and holds editorial positions at several top
AI journals, including Engineering Applications of Artificial Intelligence,
Applied Soft Computing, Neurocomputing, Advances in Engineering Soft-
ware, Computers in Biology and Medicine, Healthcare Analytics, Applied
Intelligence, and Decision Analytics.
RAED ABU ZITAR Experienced Professor with a
demonstrated history of working in the higher ed-
ucation industry. Skilled in Analytical Skills, Lec-
turing, Public Speaking, English, and Teamwork.
Strong education professional with a Ph.D. fo-
cused in Computer Engineering from Wayne State
University.Experienced Professor with a demon-
strated history of working in the higher education
industry. Skilled in Analytical Skills, Lecturing,
Public Speaking, English, and Teamwork. Strong
education professional with a Ph.D. focused in Computer Engineering from
Wayne State University.
38
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2023.3304889
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4


---
