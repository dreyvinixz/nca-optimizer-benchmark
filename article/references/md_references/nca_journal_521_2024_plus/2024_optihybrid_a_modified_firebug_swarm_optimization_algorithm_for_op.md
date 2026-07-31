# Optihybrid: a modified firebug swarm optimization algorithm for optimal sizing of hybrid renewable power system

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-10196-0

---

## Page 1
ORIGINAL ARTICLE
Optihybrid: a modified firebug swarm optimization algorithm
for optimal sizing of hybrid renewable power system
Hoda Abd El-Sattar1 • Salah Kamel2 • Fatma A. Hashim3,4 • Sahar F. Sabbeh5,6
Received: 12 June 2023 / Accepted: 5 July 2024 / Published online: 26 August 2024
 The Author(s) 2024
Abstract
In areas where conventional energy sources are unavailable, alternative energy technologies play a crucial role in gen-
erating electricity. These technologies offer various beneﬁts, such as reliable energy supply, environmental sustainability,
and employment opportunities in rural regions. This study focuses on the development of a novel optimization algorithm
called the modiﬁed ﬁrebug swarm algorithm (mFSO). Its objective is to determine the optimal size of an integrated
renewable power system for supplying electricity to a speciﬁc remote site in Dehiba town, located in the eastern province
of Tataouine, Tunisia. The proposed conﬁguration for the standalone hybrid system involves PV/biomass/battery, and three
objective functions are considered: minimizing the total energy cost (COE), reducing the loss of power supply probability
(LPSP), and managing excess energy (EXC). The effectiveness of the modiﬁed algorithm is evaluated using various tests,
including the Wilcoxon test, boxplot analysis, and the ten benchmark functions of the CEC2020 benchmark. Comparative
analysis between the mFSO and widely used algorithms like the original Firebug Swarm Optimization (FSO), Slime Mold
Algorithm (SMA), and Seagull Optimization Algorithm (SOA) demonstrates that the proposed mFSO technique is efﬁcient
and effective in solving the design problem, surpassing other optimization algorithms.
Keywords Alternative energy  Remote area  Optimization  Modiﬁed ﬁrebug swarm algorithm  Hybrid system
Abbreviations
ABC
Artiﬁcial bee colony
ACS
Ant colony algorithm
AO
Aquila optimizer
CDO
Chernobyl disaster optimizer
cEHO
The converged elephant herd optimization
algorithm
COE
Energy cost
CRF
The investment recovery factor
DE
Differential evolution algorithm
DGWO
The discrete gray wolf optimization algorithm
ESSO
Stochastic search algorithm based on the shark
smell optimization algorithm
EXC
Excess energy
FFA
Fireﬂy algorithm
FPA
Flower pollination algorithm
GA
Genetic algorithms
GAHA
Gradient artiﬁcial hummingbird algorithm
GAMS
General algebraic modeling system
GHG
Greenhouse gas emissions
GWO
Gray wolf algorithm
HHO
Harris Hawks optimization algorithm
HOMER
Hybrid
optimization
model
for
electric
renewable
HS
Harmony search algorithm
& Salah Kamel
skamel@aswu.edu.eg
Hoda Abd El-Sattar
eng_ha20@yahoo.com
Fatma A. Hashim
fatma_hashim@h-eng.helwan.edu.eg
Sahar F. Sabbeh
sfsabbeh@uj.edu.sa
1
Luxor Higher Institute of Engineering and Technology,
Luxor 85834, Egypt
2
Department of Electrical Engineering, Faculty of
Engineering, Aswan University, Aswan 81542, Egypt
3
Faculty of Engineering, Helwan University, Cairo, Egypt
4
MEU Research Unit, Middle East University, Amman 1183,
Jordan
5
College of Computer Science and Engineering, University of
Jeddah, 21493 Jeddah, Saudi Arabia
6
Faculty of Computers and Artiﬁcial Intelligence, Benha
University, Benha 13518, Egypt
123
Neural Computing and Applications (2024) 36:21517–21543
https://doi.org/10.1007/s00521-024-10196-0
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
IAOA
The
improved
archimedes
optimization
algorithm
LLP
Loss of load probability
LPS
The loss of power supply at time (t)
LPSP
Loss of power supply probability
mFSO
Modiﬁed ﬁrebug swarm algorithm
MOA
Mayﬂy optimization algorithm
NPC
The net present cost
PDO
Prairie dog optimization algorithm
PSO
Particle swarm optimization
PV
Photovoltaic
QRUN
Quantum model of a RUNge Kutta optimiza-
tion algorithm
SA
Simulated annealing
SCA
Sine cosine algorithm
SMA
Slime mold algorithm
SOA
Seagull optimization algorithm
SOA
Seagull optimization algorithm
STOA
Sooty tern optimization algorithm
TAC
Total annualized cost
WOA
Whale optimization algorithm
List of symbols
Brat
The biomass feed stock consumption rate at
time (t) (kg/h)
Ccap
ann
The yearly capital cost for each component ($/
unit)
Cfuel
ann
The fuel cost of the biomass
Ctot
ann
The total cost over a period of 8760 h
CHB
The battery’s charging energy
CO & M
The operational and upkeep value of the system
elements ($/unit-year)
Crep
The replacement cost for the required system
elements ($/unit)
DISB
The battery’s discharging energy
Fcons
The average feedstock fuel consumption at
time (t)
LHVB
The lower heat value of the biomass feed stock
(MJ/kg)
LHVsyn
The lower heat value of the syngas (MJ/kg)
LSPSmax
The maximum allowable power supply proba-
bility deﬁciency
mB
The mass ﬂow of the biomass feed stock (kg/s)
msyn
The mass ﬂow of the syngas (kg/s)
NG
The generator number
NPV
PV arrays number
PBG tð Þ
The output power of the biomass generator at
time (t) (kW)
Prat
BG
The rated power of the biomass generator (kW)
PDum
The dummy load
Pinv tð Þ
Inverter output power
Pin
inv tð Þ
Inverter input power
PL
The load power demand
PPV tð Þ
PV output power (kW)
Prat
PV
PV rated power (kW)
PRen
Power generated from renewable sources
RI tð Þ
Hourly PV radiation intensity (W/m2)
SOCB
The battery’s state of charge
TA tð Þ
The ambient temperature (C)
Tcell
The cell temperature at time (t) (C)
TN
The cell temperature under a normal operating
condition (C)
Tr
The cell temperature under standard operating
conditions (C)
Greek letters
gwire
The wire efﬁciency (%)
R
The interest rate parameter (%)
gsyn
The efﬁciency of the syngas (%)
M
The overall lifetime of the project (year)
gdis
The discharging efﬁciency of the battery
(%)
gch
The charging efﬁciency of the battery (%)
gPV
PV efﬁciency (%)
ginv
The inverter efﬁciency (%)
x1, x2, and
x3
The weight parameter for each objective
function
X
The
optimization
problem’s
control
variables
Dt
The simulation time durations
c
The rate of the self-discharge
1 Introduction
At present, energy plays a pivotal role in improving the
quality of human life and driving economic progress in
every nation [1]. It is widely recognized that developing
countries, especially rural areas, face signiﬁcant challenges
in accessing sufﬁcient energy. Despite the global emphasis
on employing clean energy sources to mitigate the emis-
sions responsible for climate change, fossil fuels continue
to dominate the production of electricity.
In areas that face electricity challenges, particularly
remote or rural regions where extending the conventional
power grid is difﬁcult due to technical limitations or high
construction expenses, a hybrid grid presents a more viable
solution for electricity provision. This hybrid grid inte-
grates renewable and conventional energy systems, energy
storage units, and AC/DC loads, forming what is com-
monly referred to as microgrid systems [2]. The opti-
mization of microgrid planning involves considering
factors such as customer demands, reliability requirements,
21518
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 3
and economic considerations [2]. The objective of opti-
mization is to identify the most economically beneﬁcial or
efﬁcient alternative among various feasible options, taking
into account the given constraints. Consequently, recent
research has focused extensively on developing optimiza-
tion tools, techniques, and applications [3].
Many researchers have employed various methodologies
to address signiﬁcant issues regarding the optimal design
and sizing of components in hybrid systems. These
methodologies include the use of simulation tools such as
Hybrid
Optimization
Model
for
Electric
Renewable
(HOMER),
HYBRID2,
INSEL,
General
Algebraic
Modeling System (GAMS), TRNSYS, RETSCREEN,
Remote
Area
Power
Supply
Simulator
(RAPSIM),
SOMES, among others [4–6]. Additionally, optimization
algorithms such as Differential evolution algorithm (DE),
Genetic algorithms (GA), Simulated annealing (SA), Par-
ticle swarm optimization (PSO), Ant colony algorithm
(ACS), and others [3] have been utilized.
In [7], a research paper discussed a study conducted on a
hybrid power system consisting of photovoltaic (PV),
diesel, and battery components in the remote Saharan vil-
lage of Tiberkatine in southern Algeria. The main objective
of this study was to simultaneously reduce the total system
cost, unsatisﬁed load, and CO2 emissions by employing the
PSO method. The results obtained from the PSO technique
were compared with those from the HOMER program,
revealing that PSO yielded superior cost-related outcomes
compared to HOMER.
In a separate study described in [8], the authors inves-
tigated a power control strategy for an off-grid hybrid
system combining PV, wind, and lead-acid battery tech-
nologies. They introduced a novel stochastic search algo-
rithm based on the shark smell optimization (ESSO)
algorithm. In [9], a novel method has been proposed for the
optimal design of a hybrid system comprising PV, diesel,
and battery units in the rural community of Ilamane in
southern Algeria. The study addresses multi-objective
optimization problems, including the total cost of the sys-
tem, loss of load probability (LLP), and greenhouse gas
(GHG)
emissions.
The
approach
utilizes
the
PSO
technique.
In a separate paper, [10] introduces a new optimization
approach for designing a hybrid PV, diesel, and battery
system in the Gobi Desert, China. This study focuses on
addressing multi-objective optimization problems, speciﬁ-
cally LLP, CO2 emissions, and the system’s total annual-
ized cost (TAC). The proposed method employs the
converged Elephant Herd Optimization Algorithm (cEHO).
To assess the algorithm’s effectiveness, the results obtained
from the proposed system are compared with those
obtained
from
the
HOMER
software
and
the
PSO
technique.
In [11], the researchers carried out simulations and
optimizations of different conﬁgurations for hybrid energy
systems utilizing PV units, wind turbines, and battery units.
The objective was to minimize the net present cost (NPC)
and the energy cost (COE) in the Yamunanagar district, a
rural area in the State of Haryana, India. The HOMER
software was employed for essential modeling, simulation,
ﬁnancial evaluation, and optimal sizing. In [12], a study
was conducted in Pulau Banggi and Tanjung Labian,
Malaysia, to investigate the impact of integrating PV units
into small hybrid networks. Among the various suggested
conﬁgurations,
the
hybrid
PV/diesel/battery
system
demonstrated the best performance in terms of technical
aspects and supported reliable daily power access.
Authors in reference [13] proposed a design for opti-
mizing the cost of a PV/diesel/battery system in Yarkant,
Xinjiang Uyghur Autonomous Region of China. To address
the optimization problem, they employed an improved
Henrygas solubility optimizer. The effectiveness of this
optimizer strategy was demonstrated by comparing its
simulation results with those obtained from HOMER and
the PSO approach. Authors in [14], proposed an optimal
conﬁguration analysis using HOMER Pro software for a
hybrid renewable system made up of solar panels, biomass,
and batteries. This proposed system is designed, simulated,
and modeled to meet the energy demands of a house in a
remote area of Ecuador’s province of Guayas. Compar-
isons are made between the best conﬁguration in terms of
implementation based on the NPC, the COE, and the initial
capital cost.
In order to meet the electricity demand of a village in
Xuzhou, east China, different conﬁguration analysis of a
PV/biogas/diesel/battery hybrid system integrated with a
battery storage has been carried out in Ref [15]. The
analyses were conducted using HOMER software, and the
results showed that the PV/BG/battery hybrid system was
the most economically viable system. In [16] proposed a
study to cover the demand of the 770 conventional houses
of a residential area in the rural region of Punjab, India
with renewable energy resources. In order to match the
demand, an off-grid hybrid PV/biomass/battery system
combination has been evaluated. The techno-economic-
environmental analysis has been conducted using HOMER
software.
Authors in [17] explored the economic feasibility for
two isolated hybrid system scenarios, the ﬁrst one based on
the connection of PV and Battery and the second scenario
is PV/Biomass/Battery based hybrid system. The suggested
hybrid systems are considered for an un-electriﬁed village
located in Indian state of West Bengal. The optimal sizes
and the system NPC have been investigated using the
discrete
gray
wolf
optimization
(DGWO)
algorithm.
According to the results, a PV/Biomass/Battery based
Neural Computing and Applications (2024) 36:21517–21543
21519
123

---

## Page 4
hybrid system scenario produced the lowest NPC and COE.
In [18] introduced the optimum size of a grid-connected
system based on the conﬁguration of PV/biomass gasi-
ﬁer/battery units for a small village in India. The artiﬁcial
bee colony algorithm has been applied to evaluate the
techno-economic analysis and the optimum size of the
suggested microgrid.
In reference [19], a novel optimization technique called
the improved Archimedes optimization algorithm (IAOA)
was introduced to design a hybrid power system in Farafra
Oasis, Egypt. The system consisted of PV modules, a wind
system, a diesel generator, and battery units. Among var-
ious
system
conﬁgurations,
the
hybrid
PV/wind/
diesel/battery setup demonstrated the lowest COE and the
highest efﬁciency. Table 1 provides an overview of rele-
vant literature references, showcasing different hybrid
system conﬁgurations based on the biomass system.
This study focuses on assessing the economic factors
associated with an off-grid hybrid PV/biomass/battery
system designed to fulﬁll the energy needs of a rural area.
The primary objective is to utilize a newly developed
algorithm called modiﬁed Firebug Swarm Algorithm
(mFSO), which effectively reduces the size of the hybrid
system while ensuring it can meet the load demand at the
lowest COE. The Firebug swarm algorithm was speciﬁ-
cally chosen due to its Bio-inspired behavior which
employs the attraction behavior of ﬁrebugs toward better
positions to discover new solutions, exhibits fast conver-
gence rates compared to other metaheuristic search algo-
rithms
which
makes
it
suitable
for
time-sensitive
applications or scenarios where computational resources
are limited. Additionally, FSO has shown resilience in
noisy or uncertain environments and can be easily adapted
or extended to incorporate problem-speciﬁc constraints and
objectives. It can handle various types of optimization
problems, including continuous, discrete, and constrained
optimization, making it versatile in different domains.
The main goal is to compare the performance of this
modiﬁed algorithm with other metaheuristic optimization
algorithms, speciﬁcally evaluating their accuracy and
convergence rate. The key contributions of this paper are as
follows:
•
A novel modiﬁed optimization algorithm dubbed mFSO
has developed in order to overcome the drawbacks of
the original Firebug Swarm Optimizer (FSO), the FSO
algorithm suffers from limitations in exploration and an
imbalanced exploitation-exploration trade-off, leading
to local optima and hindering its ability to ﬁnd optimal
solutions.
•
Assesse the effectiveness of the suggested new mFSO
algorithm through various tests including the Wilcoxon
test, boxplot analysis, and evaluating its performance on
ten benchmark functions from the CEC2020 bench-
mark. The mFSO performance is compared with other
recent optimization algorithms such as the original
FSO, Slime mold algorithm (SMA), Seagull optimiza-
tion algorithm (SOA), Harris Hawks optimization
algorithm
(HHO),
Chernobyl
disaster
optimizer
(CDO), WOA, Prairie Dog Optimization Algorithm
(PDO), COVIDOA, and SCA.
•
Implementing the modiﬁed mFSO method in solving an
engineering application, speciﬁcally in determining the
optimal size of a standalone PV/biomass/battery hybrid
power system in the Dehiba town, located in the eastern
province of Tataouine, Tunisia. The objective is to
minimize the COE while fulﬁlling the load demand for
a rural region.
•
Comparing the performance of the proposed mFSO
method with other algorithms such as the original FSO,
SMA, and SOA to establish its superiority.
The subsequent sections of this paper are organized as
follows: Sect. 2 provides an overview of the meteorologi-
cal data for the speciﬁc area of the case study. Section 3
presents the mathematical model of the hybrid system
components proposed in this study. Section 4 explores the
system optimization problem and the selected reliability
criteria for evaluation. Section 5 delves into the mathe-
matical analysis of the optimization algorithms employed.
In Sect. 6, the modeling outcomes are presented. Finally,
Sect. 7 presents the conclusion of this work.
2 Case study area
The paper introduces a hybrid system speciﬁcally designed
for the climatic conditions of Dehiba region, a small
commune located in the eastern province of Tataouine,
Tunisia. Dehiba is situated approximately 4 km west of the
Libyan frontier and a similar distance east of Wazzin, a
town in Libya. Figure 1 illustrates the precise location of
the Dehiba commune [31]. Figure 2 indicates a hypothet-
ical forecast of the AC loads for a residential building in
this area region throughout one year, with average load of
49.13 kW and maximum load of 160.10 kW. The National
Aeronautics and Space Administration (NASA) database,
which provides hourly meteorological data, particularly for
solar radiation and temperature, has been utilized [32]. The
simulation and analysis were conducted using MATLAB
software, version R2020a, resulting in the obtained ﬁnd-
ings. Figure 3 displays the yearly solar radiation data per
hour [32], while Fig. 4 presents the ambient hourly tem-
perature [32]. In this study, the amount of biomass feed-
stock per hour during one year was estimated based on the
assumptions shown in Fig. 5 [33].
21520
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 5
Table 1 An overview of various hybrid system arrangements based on the biomass system
References
Year
Connection
Hybrid system
conﬁguration
Location
Technique
Evaluation criteria
[20]
2016
On and off
grid
PV/
biomass/battery
–
Artiﬁcial bee colony (ABC)
HOMER
The least levelised
cost of energy
(LCOE)
[21]
2018
On grid
PV/wind/biomass
A town in central
Catalonia
GA
NPC
[22]
2018
Off grid
PV/
biomass/battery
Monshaet Taher village
in the Beni Suef, Egypt
Flower pollination algorithm (FPA)
Harmony search (HS) algorithm
ABC
Fireﬂy algorithm (FFA)
NPC
LPSP
EXC
[23]
2020
Off grid
PV/wind/
biomass/battery
Village in West China
HOMER
COE
[24]
2021
Off grid
PV/wind/biomass/
pump hydro
storage
PV/wind/
biomass/battery
Saudi Arabia
Whale optimization algorithm
(WOA)
FFA
PSO
COE
[25]
2022
Off grid
PV/biomass/fuel
cell (FC)
Biomass/FC
Nowdeh Malek region in
Iran
WOA
PSO
NPC
LPSP
[26]
2022
Off grid
PV/wind/
biomass/battery
PV/
biomass/battery
New Borg El-Arab city,
Egypt
MATLAB/SIMUK
NPC
TAC
[27]
2022
Off grid
PV/wind/
biomass/battery
Dakhla Oasis, Egypt
A quantum model of a RUNge
Kutta optimization algorithm
(QRUN)
RUN
Aquila optimizer (AO)
Gray Wolf algorithm (GWO)
COE
LPSP
EXC
[28]
2022
Off grid
PV/biomass/
diesel/battery
PV/diesel/battery
PV/
biomass/battery
Biomass/
diesel/battery
Eastern India
HOMER
NPC
COE
[29]
2022
Off grid
PV/biomass/FC
Abu-Monqar area, in the
Western Desert of
Egypt
Mayﬂy optimization algorithm
(MOA)
Sooty tern optimization algorithm
(STOA)
WOA
Sine cosine algorithm (SCA)
COE
GHG emissions
LPSP
[30]
2022
Off grid
PV/wind/
biomass/battery
PV/
biomass/battery
Wind/
biomass/battery
PV/wind/battery
Tiba city, Luxor, Egypt
Gradient artiﬁcial hummingbird
algorithm (GAHA)
AHA
SCA
WOA
COE
LPSP
EXC
Neural Computing and Applications (2024) 36:21517–21543
21521
123

---

## Page 6
3 Mathematical model of the suggested
hybrid system components
This study presents a proposed optimal sizing approach for
a renewable hybrid system, which involves the integration
of PV units, a biomass gasiﬁcation system, and batteries as
backup units. The mathematical model describing the
behavior of these components is outlined below, and the
key parameters of these units are provided in Table 2.
3.1 Photovoltaic model
The PV module is a crucial component in the production of
solar energy in the suggested hybrid system, and the fol-
lowing formulas illustrate the PV mathematical modeling
[34, 36]:
Fig. 1 The case study area location on the Google map [31]
Fig. 2 The suggested load
proﬁle
21522
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 7
Fig. 3 The hourly solar
radiation per year for the
suggested case study area [32]
Fig. 4 The hourly proﬁle of the
ambient temperature per year
[32]
Fig. 5 The monthly biomass
average rated proﬁle [33]
Neural Computing and Applications (2024) 36:21517–21543
21523
123

---

## Page 8
PPV tð Þ ¼ NPVPrat
PVgwiregPV

 RI tð Þ
1000


1  0:0037 Tcell tð Þ  Tr
ð
Þ
ð
Þ
ð1Þ
Tcell tð Þ ¼ RI tð Þ TN  20
0:8


þ TA tð Þ
ð2Þ
where PPV tð Þ denotes the PV module’s power output, NPV
is the PV arrays number, Prat
PV presents the PV rated power,
gwire and gPV indicate the efﬁciencies of the wire and PV
modules, respectively. RI tð Þ indicates the hourly PV radi-
ation intensity, Tcell is the cell temperature at time (t), TA tð Þ
is the ambient temperature (C), Tr and TN are the cell
temperature under standard operating conditions and under
a normal operating condition (C), respectively.
3.2 Biomass system model
To account for the intermittent nature of solar modules and
ensure the fulﬁllment of load demand, a biomass unit is
incorporated as a signiﬁcant power source in the proposed
hybrid system. The biomass system plays a vital role in
maintaining the stability and reliability of the suggested
hybrid energy system. The following equation is utilized to
calculate the output power of the biomass generator at time
(t) PBG tð Þ
ð
Þ [22, 37, 38];
PBG tð Þ ¼
NG
0:2998
gsyn LHVB Brat tð Þ
LHVsyn
 0:0644Prat
BG


;
ð3Þ
where NG denotes the generator number, LHVB and
LHVsyn are the lower heat value of the biomass feed stock
(14.8MJ/kg) and the syngas (4.766MJ/kg), respectively.
Brat presents the biomass feed stock consumption rate at
time (t), Prat
BG is the rated power of the biomass generator,
and gsyn indicates the efﬁciency of the syngas which can be
estimated by the following formula [39];
gsyn ¼ LHVsynmsyn
LHVBmB
;
ð4Þ
where msyn and mB indicate the mass ﬂow of the biomass
syngas and feed stock, respectively. From the following
formula, the average feedstock fuel consumption at time (t)
Fcons
ð
Þ can be computed [22, 37, 38];
Fcons tð Þ ¼ LHVsyn ð0:0644  NG  Prat
BGÞ þ 0:2998  PBG tð Þ
ð
Þ


gsyn LHVB
;
ð5Þ
3.3 Converter model
The equations provided below depict a simple inverter
model based on input power Pin
inv tð Þ and output power
Pinv tð Þ, in addation to power generated from renewable
sources PRen
ð
Þ [22];
Pinv tð Þ ¼ Pin
inv tð Þ  ginv;
ð6Þ
PRen tð Þ ¼ PPV tð Þ þ PBG tð Þ=ginv;
ð7Þ
where ginv is the inverter efﬁciency.
3.4 Battery model
During peak loads or periods of capacity generation, bat-
teries are employed as an extra source of power in the
system to maintain a steady voltage. During the charging
and discharging phases, the following expressions can be
used to compute the battery’s state of charge (SOCB),
charging energy (CHB), and discharging energy (DISB)
[34, 40];
In the charging stage,
CHB tð Þ ¼ PRen tð Þ  PL tð Þ=ginv
ð
Þ
ð
Þ Dt gCH
ð8Þ
SOCB tð Þ ¼ SOCB t  1
ð
Þ 1  c
ð
Þ þ CHB tð Þ
ð9Þ
In the discharging stage,
DISB tð Þ ¼
PL tð Þ=ginv
ð
Þ  PRen tð Þ
ð
ÞDt gDIS
ð10Þ
SOCB tð Þ ¼ SOCB t  1
ð
Þ 1  c
ð
Þ  DISB tð Þ
ð11Þ
where PL indicates the load power demand, Dt indicates the
simulation time durations, c denotes the rate of the self-
Table 2 The main characteristics of the hybrid system’s parts
PV [34, 35]
Converter unit [35]
Biomass system [24]
Battery [34]
Power (kW)
1
1
40
Capacity 4.8 (kWh)
Efﬁciency (%)
15
95
80
gch ¼ 90
gdis = 85
Capital cost ($/unit)
7000
800
23,700
3880
O&M cost ($/ unit-year)
20
8
0.05 ($/ h)
–
Replacement cost ($/unit)
–
750
15,000
–
Lifespan (year)
25
15
15,000 (h)
25
21524
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 9
discharge, gch and gdis present the charging and discharging
efﬁciencies of the battery unit, respectively.
4 Optimization problem and reliability
criteria
The major goal of this study is to establish the number of
components needed for the proposed hybrid power system
to make it more cost effective. By employing the devel-
oped mFSO approach, the recommended hybrid system’s
objective function is to minimize the COE, LPSP, and
excess energy (Eexc) distributed in the dummy load (PDum).
The PV panels’ number, the number of biomass generator,
and battery module number are the decision variables in
this study. The principal objective function, the optimiza-
tion limitations, the cost and ﬁnancial evaluation, and the
system approach to management are all covered in this
part.
a.
Cost analysis
The NPC provides an estimation of the cumulative
expenses, including signiﬁcant investments and oper-
ational costs, throughout the project’s duration. On the
other hand, the COE (Cost of Energy) represents the
cost per kilowatt-hour ($/kWh) generated by the sys-
tem. By employing the equations mentioned below, we
can express the COE and NPC as follows [34, 41]:
NPC ¼ Ctot
ann
CRF
ð12Þ
CRF ¼ R R þ 1
ð
ÞM
R þ 1
ð
ÞM1
ð13Þ
Ctot
ann ¼ Ccap
ann þ Cfuel
ann þ
X
M
i¼1
CO&M;i þ
X
M
i¼1
Crep;i
ð14Þ
COE ¼
Ctot
ann
P8760
1
PL
ð15Þ
where Ctot
ann is the total cost over a period of 8760 h,
CRF indicates the investment recovery factor, R stands
for the interest rate parameter (6%), M stands for the
overall lifetime of the project (20 year), Ccap
ann presents
the yearly capital cost for each components, CO&M
stands for the operational and upkeep value of the
system elements, Crep is the replacement cost for the
required system elements, and Cfuel
ann stands for the fuel
cost of the biomass.
b.
Objective function and constraints
The subsequent equations demonstrate the objective
function and constraints;
Min F X
ð Þ ¼ Min x1 COE þ x2 LSPS þ x3 Eexc
ð
Þ
ð16Þ
where,
LPSP ¼
X
T
1
LPS tð Þ
PL tð Þ
ð17Þ
LPS tð Þ ¼ PL tð Þ PRen tð Þ þ SOCB t  1
ð
Þ  SOCmin
ð
Þ
 ginv
ð18Þ
Eexc ¼
X
T
1
PDum tð Þ
PL tð Þ
ð19Þ
The maximum number of system components
constraints:
1  NPV  Nmax
PV ;
1  NG  Nmax
G
;
1  NBat  Nmax
Bat ;
ð20Þ
where X stands for the optimization problem’s control
variables (NPV, NG, and NBat) that must be optimized
utilizing the suggested optimization techniques, x1,
x2, and x3 are the weight parameter for each objective
function and LPS presents the loss of power supply at
time (t). For a reliable system, the maximum allowable
LPSP should be considered, in the following equation,
LSPSmax represents the maximum allowable power
supply probability deﬁciency (0.05).
LSPS  LSPSmax
ð21Þ
c.
Operational energy management strategy
As for the operational energy management strategy,
it is illustrated in Fig. 6 [22, 34, 41]. The operational
energy management strategy of a hybrid PV, biomass
system, and battery backup unit entails optimizing the
use of these various energy sources to ensure efﬁcient
and effective energy generation and management. To
meet the system’s energy needs, this strategy balances
the energy generated by various sources. The suggested
hybrid system is built to automatically switch between
energy sources, reduce cost and increase efﬁciency.
In the ﬁrst stage, the hybrid PV system is designed
to generate electricity from solar panels during the day
and store the extra energy in batteries for use at night
and other times of low light. It is preferable to use the
energy produced to satisfy the system’s immediate
demand without the use of storage units. Second, the
biomass system is intended to supplement the energy
produced by the PV system. The system can then use
the energy produced by the biomass system to supple-
ment the energy produced by the PV system, supplying
Neural Computing and Applications (2024) 36:21517–21543
21525
123

---

## Page 10
more of the system’s energy requirements. Last but not
least, the battery backup unit serves as a backup energy
source in case of blackouts or other events that prevent
primary energy sources from producing electricity. When
energy demand is low, the batteries can be charged, and
when energy demand is high, they can be used.
5 Mathematical model of the proposed
algorithms
5.1 Firebug swarm optimization (FSO) algorithm
FSO [42], draws inspiration from Pyrrhocorids apterous,
commonly known as Firebugs, exhibiting two prominent
behavioral traits. During the summer, ﬁrebugs can either
explore individually or gather in groups. Socializing
enables the bugs to reduce the risk of predation and locate
suitable partners for reproduction. The ﬁrebugs’ quest for
the optimal partner can be viewed as a process of discov-
ering a set of optimal solutions for a given problem. FSO
emulates these behaviors mathematically, serving as a
foundation for a global optimization algorithm. These ﬁve
optimization-related behaviors are simulated within FSO:
a) construction of female bug colonies, b) partner selection,
c) chemotactic behavior of females, d) attraction of males
to the ﬁttest female, and e) group cohesion. The mathe-
matical model of FSO is represented as follows:
5.1.1 The construction of female colonies
During this stage, the construction of female colonies takes
place. These colonies serve as the gathering spots where
male bugs search for suitable partners. The primary aim at
this stage is to minimize the associated cost, as the selec-
tion of mates should be done with the least cost possible.
FSO algorithm starts with male bugs (BM) and female bug
(BF) randomly distributed in the search space within the
Fig. 6 The operation strategy ﬂowchart [22, 34, 41]
21526
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 11
search space. The position of each bug is represented by a
random uniform vector variable. Furthermore, each bug is
assigned a cost function value.
5.1.2 Partner selection
Each BM’s initial position is set to match the position of its
partner BF within the colony. Initially, the FSO designates
the top-notch female bug in a group as the leader controlled
by the dominant male. The males’ positions are constantly
adjusted to align with the ﬁttest female in their respective
groups. The FSO updates the positions of all BF in the
colony simultaneously. Furthermore, the cost function
evaluations are highly optimized through vectorization,
where the position vector of all individuals is consolidated
into a single matrix, and their corresponding costs are
stored in a single array to accelerate computation.
5.1.3 Chemotactic movement behavior of female bugs
The columns of the D 9 BF matrix, m(a).F, represent the
position of the female bug (BF). The mathematical formula
to immediately update all BF in each group using Hada-
mard arithmetic functions is shown in Eqs. (22) and (23):
After initialization, the location of each BF is updated as
it moves toward the leading BM in its colony. The loca-
tions of all females in the group are stored as a matrix and
updated
synchronously.
Assume
that
m m
ð Þ:F is a matrix of D  BF
dimensions,
its
columns
represent the position of the female bugs, the equation to
update all females in a speciﬁc group is given as follows:
Mx  repmat m m
ð Þ:x; 1; BF
ð
Þ
ð22Þ
My  repmat m a
ð Þ:x; 1; BF
ð
Þ
ð23Þ
where: a is a randomly generated integer in the range
between 1 and BF, repmat(A, m, n) is a function that
replicates a matrix ‘‘A’’ in a tiled manner to create a larger
matrix of size m-by-n. The resulting matrix has m copies of
A in the row direction and n copies of A in the column
direction. The repmat(A, m, n) function takes three argu-
ments: A: The matrix or array that needs to be replicated,
m: The number of times the matrix A will be replicated in
the row dimension, and n. In the given equation,
Mx  repmatðmðmÞ:x; 1; BFÞ, the repmat function is
used to replicate the matrix mðmÞ:x. NF times in the col-
umn direction. The resulting matrix, Mx, will have the
same rows as m(m).x and BF columns, with each column
being a copy of m(m).x
m m
ð Þ:F  m m
ð Þ:F þ Col1  Mx  m m
ð Þ:F
ð
Þ þ Col2
 My  m m
ð Þ:F


ð24Þ
where Col1 and Col2 are the strength of attraction toward
the ﬁrst and the second colonies. These are coefﬁcient
vectors or matrices that control the movement of the ﬁreﬂy.
They are typically random values within a speciﬁed range.
The term Col1  Mx  m m
ð Þ:F
ð
Þ represents the attraction
toward the target position Mx. It calculates the difference
between the target position and the current position of the
ﬁreﬂy m, and then scales this difference by the coefﬁcients in
Col1. The element-wise multiplication adjusts the movement
magnitude for each dimension of the position vector. Simi-
larly, the term Col2  My  m m
ð Þ:F


represents the
attraction toward the target position My. It calculates the
difference between the target position and the current posi-
tion of the ﬁreﬂy m, and then scales this difference by the
coefﬁcients in Col2. Finally, the updated position of the
ﬁreﬂy, m m
ð Þ:F, is obtained by adding the attraction terms to
the current position, m m
ð Þ:F. By iteratively applying this
equation to all ﬁreﬂies in the swarm, the FSO algorithm
simulates the movement and attraction behavior of ﬁreﬂies
toward brighter positions, aiming to converge toward opti-
mal or near-optimal solutions.
It’s worth noting that the speciﬁc values and calculations
of Col1 and Col2 may vary depending on the implementation
and problem being solved. These coefﬁcients are often
generated randomly or adaptively adjusted during the opti-
mization process to balance exploration and exploitation.
5.1.4 The male’s attraction to the fittest female
Every male is drawn to the most physically ﬁt female
worldwide, regardless of which colony she belongs to. If
each male were to only move toward the ﬁttest female
within its own colony, it could result in the group dis-
persing. Hence, males are capable of moving toward the
ﬁttest female outside their colony to avoid premature or
early convergence. This behavior also allows for the
exploration of larger areas within the search space, as
illustrated in the following equation.
m m
ð Þ:x  m m
ð Þ:x þ Col3  g  m m
ð Þ:x
ð
Þ
ð25Þ
where: This term m m
ð Þ:x represents the updated position of
the male bug after applying the movement equation, Col3 is a
coefﬁcient that controls the movement of the bug toward the
global best position. It is typically a random value within a
speciﬁed range,  represents the element-wise multiplication
(Hadamard product) between two vectors or matrices, and g
represents the global best position in the search space. It is
often the position associated with the highest ﬁtness or
objective function value among all ﬁreﬂies.
By iteratively applying this equation to all bugs in the
swarm, the algorithm aims to simulate the attraction
behavior of male bugs toward the global best position,
Neural Computing and Applications (2024) 36:21517–21543
21527
123

---

## Page 12
promoting exploration and exploitation to converge toward
optimal or near-optimal solutions.
5.1.5 Group cohesion
The entire group moves together as a uniﬁed unit, with
each male bug following the movement direction of
another BM, as demonstrated in Eq. (26). Every male bug
replicates the movement direction of a randomly selected
male bug that is heading toward the ﬁttest female bug. This
approach allows all males to converge toward a favorable
solution and prevents them from getting trapped in local
minima.
Furthermore,
Female
Sexual
Ornamentation
(FSO) aims to facilitate independent movements of male
bugs along different dimensions, promoting improved
exploration of novel solutions. The update equation
employs element-wise Hadamard multiplication.
m m
ð Þ:x  m m
ð Þ:x þ Col4  g  m b
ð Þ:x
ð
Þ
ð26Þ
where g is the new global best position in the search space,
and Col4 is a coefﬁcient that inﬂuences the movement of
bugs toward the positions associated with the fourth
colonies.
Algorithm 1 Firebug swarm optimization (FSO)
5.2 Proposed modified firebug swarm algorithm
This section introduces the modiﬁed Firebug swarm opti-
mization
algorithm
(mFSO),
which
addresses
the
limitations of the FSO algorithm [42]. It begins by dis-
cussing the drawbacks of the FSO algorithm and subse-
quently presents the design of the modiﬁed ﬁrebug swarm
optimization algorithm (mFSO).
5.2.1 Limitations of the FSO algorithm
The primary drawback of the FSO algorithm lies in its
limited exploration capability and imbalanced exploitation-
exploration trade-off, leading to the occurrence of local
optima and restricting its ability to discover optimal solu-
tions. This issue arises due to exploration being predomi-
nantly
emphasized
in
the
initial
iterations,
while
exploitation dominates in the later iterations.
5.2.2 Architecture of the mFSO
The mFSO model being proposed incorporates three pri-
mary operators, namely: a) a logistic-based chaotic search,
b) an opposite-based learning operator (OBL), and c)
operators for phasor and transition (TO & PO) operations.
Logistic–based
Chaotic
search
Chaotic-based
search
exhibits a semi-random behavior, which enables superior
exploration compared to ergodic methods. Ergodic meth-
ods rely on probability-based searches, which lead agents
to spend more time in search zones with a higher likelihood
of ﬁnding solutions. It has shown good results in some
optimizers like [43, 44]. In our proposed mFSO (modiﬁed
Fireﬂy Algorithm), we utilize the logistic map during the
chaotic local search (CLS) phase, as outlined as follows.
osþ1 ¼ Cos 1  os
ð
Þ
ð27Þ
where: s ¼ 1; 2; :::; T; os 2 0; 1
ð
Þ; and os 6¼ 0:25; 0:5; 0:75.
where os is the chaotic number in iteration k and the
CLS solution is represented as follows:
{s ¼ 1  l
ð
Þ  T þ l{i;
i ¼ 1; 2; . . .:; n
ð28Þ
where: Cs is the best solution’s value, Ci i: the solution’s
measurement value, and l is represented as follows:
l ¼ T  t þ 1
T
ð29Þ
where T is the number of iterations, t is the current itera-
tion, and, { I is represented as:
{i ¼ LOB þ {i  UPB  LOB
ð
Þ
ð30Þ
where LOB & UPB are the lower and the upper boundary,
respectively.
The Opposite-based Learning (OBL) [45] enhances the
algorithm’s ability to exploit and mitigates the risk of local
optima. OBL involves calculating the opposite solution and
21528
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 13
comparing it with the original solution to determine the
optimal solution. This approach effectively improves the
algorithm’s performance.
Let x is a real number falls within [lob, upb]. x is
computed as: x ¼ upb þ lob
ð
Þ  x. Where: upb is the
upper boundary, lob is the lower boundary. For N dimen-
sions x can be calculated as follows:
xi ¼ upbi þ lobi
ð
Þ  xi
ð31Þ
where xi represents position of the male bug in ith
dimension, upbi, lobi are the upper and upper boundaries of
dimension i.
The Phasor operator (PO) is grounded on periodic
function in the interval of p; 2p
½
. The periodic functions
are suitable to represent any algorithms’ arguments using
an angle H where a function of angle Hi is deﬁned for each
agent i. Equations (32) and (33) represent the agent as
follows:
p ht
i
 
¼ cos ht
i

2sint
i
ð32Þ
g ht
i
 
¼ sin ht
i

2cost
i
ð33Þ
where p p ht
i
 
and g ht
i
 
are the values generated by the
Phasor operator.
The calculation of the nonlinear transition operator (TO)
involves the use of the exploration-oriented PO. The TO
plays a crucial role in transitioning from exploration to
exploitation and is determined by the following formula:
TO ¼ exp
t
T
ð34Þ
where: t represents the present step and T represents the
maximum steps number.
The utilization of TO serves the purpose of avoiding
local optima during the search phase. The revised search
equations, incorporating the TO operator, are presented
below.
m m
ð Þ:F  m m
ð Þ:F þ C1  Mx  TO  m m
ð Þ:F
ð
Þ
þ C2  My  TO
 m m
ð Þ:F


ð35Þ
Algorithm 2 Modiﬁed ﬁrebug swarm optimization (mFSO)
Neural Computing and Applications (2024) 36:21517–21543
21529
123

---

## Page 14
6 Simulation results
The results in this section are categorized into two sections:
the evaluation of the mFSO method’s performance and the
application of the mFSO approach in determining the
optimal design for the proposed hybrid system.
6.1 Performance evaluation of mFSO
The evaluation of the mFSO quality is conducted by uti-
lizing it to determine the optimal values for the IEEE
CEC’20 test suite [46] functions. The CEC’20 test suite
consists of ten test functions that are categorized into
unimodal (F1:F4), hybrid (F5:F7), and composition func-
tions (F8:F10). These categories are presented in Table 3.
The mFSO’s performance is assessed by comparing it to
several commonly employed algorithms, namely FSO [42],
SMA [47], SOA [48], HHO [49], CDO [50], WOA [51],
PDO [52], COVIDOA [53], and SCA [54]. The evaluation
criteria encompass various metrics such as the minimum,
maximum, average (mean), and standard deviation of the
ﬁtness scores, as well as the application of the Wilcoxon
rank-sum test [55].
1.
Mean is the ratio of the optimization deﬁned as follow:
Mean ¼ 1
N
X
N
i1
opi
ð36Þ
where: N is the total number of operations, opi is the
optimal solution at operation i.
2.
Minimum represents the optimal or minimum score of
the ﬁtness achieved by the algorithm throughout N
operations. It is deﬁned as follows:
Min ¼ minN
i¼1 opi
ð37Þ
3.
Maximum denotes the poorest or maximum ﬁtness
score produced by the algorithm during N operations. It
can be expressed as follows:
Max ¼ maxN
i¼1 opi
ð38Þ
4.
Standard deviation (Std) assesses the stability and
resilience of the algorithm. A smaller standard devi-
ation indicates greater stability, ensuring consistent
convergence to the same solution. Conversely, a larger
Std value suggests that the algorithm produces more
random outcomes, exhibiting less predictability.
Std ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
N  1
X
opi  Mean
ð
Þ2
r
ð39Þ
5.
Wilcoxon rank-sum P values involves employing the
Wilcoxon test to examine the correlation between the
outputs of the tested algorithms. The null hypothesis
assumes
that
the
comparison
results
are
nearly
identical, while the alternative hypothesis assumes
distinguishable differences between the compared
algorithms. The Wilcoxon test produces a P value.
Rejecting the null hypothesis (P \ 0.05) indicates non-
correlated results, whereas accepting the null hypoth-
esis (P [ 0.05) suggests correlated results.
6.2 Result discussion
The performance evaluation of the proposed mFSO was
conducted by comparing it with several baseline algorithms
using the ten functions from the CEC2020 benchmark. The
results, presented in Table 4, provide insights into the
performance of the algorithms based on various evaluation
metrics such as minimum, maximum, mean, and standard
deviation (Std) of the ﬁtness scores. The best results for
each metric are highlighted in bold.
Upon analyzing the results, it is evident that the mFSO
algorithm demonstrates superiority over the tested algo-
rithms across multiple evaluation metrics for a signiﬁcant
number of test functions. Speciﬁcally, mFSO outperforms
all other algorithms in terms of achieving the minimum or
best ﬁtness score, as well as maintaining the lowest max-
imum ﬁtness score, mean ﬁtness score, and minimum
standard deviation for seven out of the ten test functions
(F3, F4, F6, F7, F8, F9, and F10). This indicates the
algorithm’s robustness and ability to ﬁnd high-quality
solutions consistently.
For function F5, while mFSO does not achieve the
minimum/best ﬁtness value, it demonstrates the best mean
score, standard deviation, and minimum worst ﬁtness
score. On the other hand, the SMA algorithm performs
exceptionally well for F2, achieving the minimum/best
ﬁtness value.
Moreover, in the case of function F1, mFSO achieves
competitive scores in terms of the minimum and maximum
ﬁtness values. The HHO algorithm, on the other hand,
achieves the best mean score, closely followed by the SMA
algorithm,
which
exhibits
the
second-best
standard
deviation.
These ﬁndings highlight the search capabilities and
stability of the mFSO algorithm, showcasing its effec-
tiveness in addressing a wide range of optimization prob-
lems. The algorithm consistently outperforms most of the
tested algorithms across multiple evaluation metrics, indi-
cating its competitiveness and potential as a robust opti-
mization approach.
Based on the discussed results, mFSO exhibits several
advantages over its competitors, as evidenced by the pre-
viously discussed results. First and foremost, mFSO con-
sistently outperforms the tested algorithms in terms of
achieving superior ﬁtness scores across multiple evaluation
21530
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 15
metrics. It demonstrates the ability to obtain the minimum
or best ﬁtness score, maintain the lowest maximum ﬁtness
score, and achieve the best mean ﬁtness score for a sig-
niﬁcant number of test functions. This indicates the algo-
rithm’s effectiveness in ﬁnding high-quality solutions and
its robustness in addressing optimization problems.
Furthermore, mFSO showcases remarkable stability and
search capabilities. It consistently delivers low standard
deviations, indicating the algorithm’s ability to converge to
reliable solutions consistently. The algorithm’s perfor-
mance is particularly notable in terms of maintaining low
standard deviations for various test functions, showcasing
its stability and reliability in ﬁnding optimal or near-opti-
mal solutions.
In addition to evaluating the performance of the pro-
posed mFSO (modiﬁed Firebug Swarm Algorithm), the
Wilcoxon rank sum test was employed to assess the dis-
tinguishability of mFSO from other competing algorithms.
The utilization of statistical tests adds a rigorous and
quantitative analysis to the evaluation process. The Wil-
coxon rank-sum ﬁtness scores, as presented in Table 5,
provide insights into the signiﬁcance of the observed
differences.
The results obtained from the Wilcoxon rank sum test
reveal that a majority of the p-values are below the sig-
niﬁcance level of 0.05. This indicates a statistically sig-
niﬁcant difference between the performance of mFSO and
the other algorithms for the majority of the CEC2020
functions. The signiﬁcance level of 0.05 is commonly used
to determine if the observed differences are unlikely to
have occurred by chance.
The ﬁndings from the Wilcoxon rank sum test contribute
to the credibility and reliability of the mFSO results. By
demonstrating a signiﬁcant difference in performance
compared to the competing algorithms, it strengthens the
argument for the effectiveness of mFSO as a competitive
optimization approach.
6.3 Convergence behavior analysis
To assess the stability and convergence behavior of the
mFSO algorithm, a comprehensive convergence analysis
was conducted to compare the mFSO algorithm with its
competitor algorithms. The convergence curves, as depic-
ted in Fig. 7, provide valuable insights into the conver-
gence
rates
of
the
algorithms
across
the
CEC2020
functions.
The results of the convergence analysis highlight a
signiﬁcant advantage of the mFSO algorithm in terms of its
convergence rate when compared to its competitors. The
convergence curves clearly demonstrate that mFSO exhi-
bits a noticeably faster convergence, characterized by steep
descent and rapid progress toward optimal or near-optimal
solutions. This accelerated convergence is observed for the
majority of the CEC2020 functions.
The superior convergence rate of mFSO translates into
several advantages for the algorithm. Firstly, it indicates
that mFSO has a strong ability to navigate complex opti-
mization landscapes efﬁciently. By quickly converging
toward
promising
solutions,
mFSO
demonstrates
its
effectiveness in exploring and exploiting the search space,
enabling it to ﬁnd high-quality solutions in a shorter
timeframe compared to its competitors.
Furthermore, the rapid convergence rate of mFSO con-
tributes to its computational efﬁciency. The algorithm
requires fewer iterations or evaluations to reach conver-
gence, reducing the computational burden and associated
time requirements. This advantage is particularly signiﬁ-
cant in scenarios where time-sensitive optimization tasks
need to be performed or when computational resources are
limited.
The competitive and efﬁcient convergence behavior
positions mFSO as a promising solution for tackling global
optimization problems. Its rapid convergence rate enhances
its applicability to real-world applications where ﬁnding
high-quality
solutions
within
limited
computational
resources is crucial.
Table 3 Description with
ﬁtness score of CEC2020
functions
Category
#
Description
Fi*
Unimodal
F1
Shifted and rotated Bent Cigar function multimodal
100
F2
Shifted and rotated Schwefel function
1100
F3
Shifted and rotated Lunacek bi-Rastrigin function
700
F4
Expanded Rosenbrock’s plus Griewangk’s function
1900
Hybrid functions
F5
Hybrid function 1 (N = 3)
1700
F6
Hybrid function 2 (N = 4)
1600
F7
Hybrid function 3 (N = 5)
2100
Composition functions
F8
Composition function 1 (N = 3)
2200
F9
Composition function 2 (N = 4)
2400
F10
Composition function 3 (N = 5)
2500
Neural Computing and Applications (2024) 36:21517–21543
21531
123

---

## Page 16
Table 4 Description of the ﬁtness score of CEC2020 benchmark functions
Func
mFSO
FSO
SMA
SOA
HHO
CDO
WOA
PDO
COVIDOA
SCA
F1
Min
117.3452
6.44E ? 09
2910.278
4935.998
2911.317
2.09E ? 10
14,601,681
1.46E ? 10
1.66E ? 10
3062.593
Max
126,018.1
6.07E ? 10
2975.447
9598.643
3014.646
2.17E ? 10
71,896,903
3.19E ? 10
2.82E ? 10
3642.911
mean
17,169.31
2.87E ? 10
2918.09
6813.764
2982.666
2.14E ? 10
30,458,804
2.44E ? 10
2.34E ? 10
3198.291
Std
27,980.13
1.65E ? 10
15.7639
1204.266
25.08729
1.53E ? 08
16,406,206
4.52E ? 09
2.83E ? 09
132.0891
F2
Min
2005.337
3937.424
1394.311
4653.421
2036.777
4449.92
2490.101
4114.999
3911.658
4289.018
Max
3867.284
6586.694
2522.527
6992.462
3828.073
5340.686
5080.244
6160.498
5651.11
5587.367
mean
3141.053
5408.309
1856.884
5650.254
2898.974
4988.261
3744.383
5268.975
5230.084
5106.206
Std
527.5409
658.9826
293.2159
518.6831
463.5156
207.9187
592.9156
499.7603
298.4527
281.5509
F3
Min
729.9967
907.9542
730.2831
1016.487
834.5072
969.2592
845.5028
910.575
1001.941
874.3272
Max
755.7436
1521.988
772.0793
1170.113
970.7506
1015.425
1039.339
1168.342
1095.015
1009.473
mean
743.6245
1005.459
744.9826
1095.175
899.9842
989.8485
956.9715
984.7572
1060.46
930.5996
Std
6.71964
113.463
8.692664
33.57846
30.11809
13.02522
44.84574
58.9956
22.7961
28.6985
F4
Min
1902.018
1938.925
1901.688
25,952.86
1912.752
146,296.4
1918.399
59,391.56
37,006.21
1998.944
Max
1905.438
5,417,118
1904.852
3,109,739
1933.42
391,126.6
2078.22
1,498,315
520,504.4
6031.805
mean
1903.22
684,605.3
1902.819
1,111,983
1923.178
374,766.2
1950.586
382,615.4
145,420.1
2855.096
Std
0.648153
1,353,220
0.889074
930,956
5.257264
55,251.01
36.95402
368,261
95,511.49
798.9788
F5
Min
52,742.48
825,170
12,486.3
414,330.7
45,729.05
450,735.4
71,965.4
715,035.4
776,821
140,780
Max
442,837.9
65,629,576
684,775.4
24,543,450
2,205,722
2,305,548
5,026,621
14,460,360
5,048,014
3,592,751
mean
170,416.1
19,837,718
343,516.4
5,219,985
581,330.9
874,823.4
1,196,338
3,585,139
2,743,005
1,579,073
Std
111,745.3
21,250,809
212,457.2
5,142,683
447,915.4
371,387.2
1,016,894
2,698,418
989,514.5
849,979.1
F6
Min
1607.629
2650.764
1602.877
2994.858
1777.416
2763.323
1793.387
2476.54
2692.025
2142.988
Max
1951.702
4874.783
1857.999
4256.547
2721.199
3468.624
2987.41
3844.72
3453.379
2783.425
Mean
1754.935
3661.459
1663.41
3517.05
2161.23
3089.501
2422.632
3044.855
3066.873
2435.001
Std
112.1234
530.822
81.56327
335.3659
211.6085
170.5488
290.7677
352.376
200.9146
148.9112
7
Min
8133. 554
110,370.3
17,685.34
49,255.6
61,499
416,475.3
10,099.33
243,577.3
141,814.3
61,669.63
Max
104,925.2
30,747,036
873,693.4
21,991,893
825,589.9
1.5E 1 08
3,581,768
10,998,237
3,209,375
1,449,058
Mean
34,012.07
5,681,496
437,271.3
4,322,030
242,057.3
26,280,783
1,011,534
2,854,136
748,861.7
525,085
Std
20,548.38
6,944,591
287,128.8
4,895,366
174,732.6
32,452,698
979,760.4
2,690,746
601,831.1
402,208.5
8
Min
2300.001
3366.739
2300.072
4185.935
2311.901
4213.664
2317.106
3142.644
4325.539
2611.415
Max
2301.571
8032.715
5590.912
7633.11
6081.669
7334.484
6726.993
7071.659
5793.421
7172.079
Mean
2300.256
5743.614
3506.747
6598.57
4060.821
5491.052
3955.565
5221.833
5260.043
4864.664
Std
0.497843
1300.348
1199.259
976.2632
1592.76
1424.256
1696.254
1020.27
300.1079
1906.658
9
Min
2810.655
2949.556
2821.619
3182.327
2917.455
3320.669
2902.366
3053.436
3167.467
2965.215
Max
2855.994
3726.007
2921.926
3810.867
3325.501
3400.527
3089.22
3189.717
3338.597
3040.625
Mean
2832.247
3340.709
2862.01
3501.35
3109.96
3357.358
3000.605
3136.308
3283.912
2997.238
Std
10.54318
216.8719
22.57658
139.0932
92.04638
20.44364
54.72843
34.42742
40.73234
20.51983
21532
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 17
6.4 Boxplot behavior analysis
To further analyze the performance results, a boxplot
analysis was performed to examine the distribution of
achieved results within the ﬁrst three quartiles. Figure 8
illustrates the boxplots for the ten functions of the
CEC2020 benchmark. The boxplot analysis reveals distinct
advantages of the mFSO algorithm compared to its com-
petitors. The boxplots representing mFSO are relatively
narrow, indicating a more concentrated and consistent
performance across the evaluated functions. This suggests
that mFSO consistently achieves results closer to the
optimal or near-optimal solutions, exhibiting less variation
in its performance.
Furthermore, mFSO demonstrates the lowest scores
among all the algorithms for eight out of the ten tested
functions. This highlights its superior performance in terms
of achieving better ﬁtness scores compared to its com-
petitors. The consistent dominance of mFSO in terms of
lower scores accentuates its effectiveness in ﬁnding high-
quality solutions and its competitive edge in the opti-
mization landscape.
The narrower boxplots and the consistently lower scores
achieved by mFSO emphasize its advantage over the
competing algorithms. The concentrated performance dis-
tribution indicates that mFSO consistently converges to
favorable solutions, while the wider boxplots of the other
algorithms indicate more variability and less consistent
performance.
6.5 Exploration–exploitation analysis
The exploration–exploitation curves provide insights into
how the mFSO algorithm balances its exploration and
exploitation processes while searching for optimal solu-
tions. Figure 9 illustrates the performance of mFSO as it
explores the search space and transitions to the exploitation
phase for the ten functions of the CEC2020 benchmark.
The results reveal that mFSO achieves a balanced ratio
of exploration to exploitation in the majority of the tested
functions. Initially, the algorithm dedicates more time to
exploration, which involves searching a wide range of
solutions to gain a comprehensive understanding of the
search space. During this phase, mFSO aims to discover
potential promising regions that may contain optimal or
near-optimal solutions.
As the exploration phase progresses, mFSO gradually
transitions to the exploitation phase, where it focuses on
reﬁning and exploiting the discovered promising regions.
This shift allows the algorithm to concentrate its search
efforts on the most favorable areas of the search space,
aiming to converge toward the optimal solution.
Table 4 (continued)
Func
mFSO
FSO
SMA
SOA
HHO
CDO
WOA
PDO
COVIDOA
SCA
10
Min
2906.29
3167.755
2910.278
4935.998
2911.317
5159.511
2935.195
3618.005
3560.002
3062.593
Max
2967.282
11,746.31
2975.447
9598.643
3014.646
5965.92
3136.19
6405.148
5131.954
3642.911
Mean
2910.281
5617.011
2918.09
6813.764
2982.666
5909.846
3036.056
4786.286
4405.716
3198.291
Std
14.91958
2211.375
15.7639
1204.266
25.08729
143.0422
44.38383
744.7808
372.8546
132.0891
Neural Computing and Applications (2024) 36:21517–21543
21533
123

---

## Page 18
The
balanced
exploration–exploitation
strategy
of
mFSO demonstrates its ability to efﬁciently explore the
search space while also exploiting the valuable information
gained during the exploration phase. This approach con-
tributes to the algorithm’s effectiveness in ﬁnding high-
quality solutions.
By
striking
a
balance
between
exploration
and
exploitation, mFSO avoids getting trapped in local optima
and maintains the potential to discover globally optimal or
near-optimal solutions. The exploration phase ensures that
the algorithm explores diverse regions of the search space,
while the exploitation phase enables the algorithm to
exploit the most promising areas, reﬁning the solutions
toward optimality.
Overall, the exploration–exploitation curves of the
mFSO algorithm signify its ability to achieve a balanced
approach in searching for optimal solutions. The initial
emphasis on exploration followed by a transition to
exploitation showcases the algorithm’s capability to efﬁ-
ciently explore and exploit the search space, ultimately
contributing to its high-performance results.
6.6 Diversity analysis
The diversity analysis of the mFSO algorithm plays a
crucial role in assessing its ability to maintain population
diversity and avoid getting trapped in local optima. The
analysis aims to ensure a balanced exploration–exploitation
strategy and enhance the algorithm’s capability to explore
promising search areas. Figure 10 provides insights into
the diversity analysis of mFSO.
The ﬁndings of the diversity analysis indicate that the
mFSO algorithm effectively sustains population diversity
throughout the optimization process. By maintaining a
diverse set of solutions within the population, mFSO can
explore a wide range of search areas, increasing the like-
lihood of discovering optimal or near-optimal solutions.
The sustained population diversity in mFSO is crucial
for achieving a balanced exploration–exploitation strategy.
A diverse population enables the algorithm to explore
different regions of the search space, preventing it from
prematurely converging to suboptimal solutions. This
diversity allows mFSO to continue exploring and reﬁning
its solutions, enhancing its chances of ﬁnding superior
solutions.
By sustaining population diversity, mFSO also mitigates
the risk of premature convergence. If the algorithm lacks
diversity, it may get trapped in local optima, unable to
escape and explore other potentially better solutions.
However, with effective diversity maintenance, mFSO can
avoid such traps and continue its search for globally opti-
mal or near-optimal solutions.
Table 5 Wilcoxon ranksum test p-value of the mFSO VS. competitor algorithms for benchmark functions
mFSO vs FSO
mFSO vs SMA
mFSO vs SOA
mFSO vs HHO
mFSO vs CDO
mFSO vs WOA
mFSO vs PDO
mFSO vs COVIDOA
mFSO vs SCA
1
3.01986E-11
0.027086318
0.958731491
0.027086318
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
0.087710377
2
3.01986E-11
3.15889E-10
3.01986E-11
0.036438856
3.01986E-11
0.00039881
3.01986E-11
3.01986E-11
3.01986E-11
3
3.01986E-11
0.728265296
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
4
3.01986E-11
0.024156885
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
5
3.01986E-11
0.001679756
3.33839E-11
8.29194E-06
3.01986E-11
3.96477E-08
3.01986E-11
3.01986E-11
1.09367E-10
6
3.01986E-11
9.79171E-05
3.01986E-11
4.61591E-10
3.01986E-11
1.46431E-10
3.01986E-11
3.01986E-11
3.01986E-11
7
3.01986E-11
1.69472E-09
4.50432E-11
6.69552E-11
3.01986E-11
1.01045E-08
3.01986E-11
3.01986E-11
4.97517E-11
8
3.01986E-11
2.66947E-09
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
9
3.01986E-11
1.25408E-07
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
3.01986E-11
10
3.01986E-11
5.96731E-09
3.01986E-11
8.99341E-11
3.01986E-11
3.68973E-11
3.01986E-11
3.01986E-11
3.01986E-11
21534
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 19
The ability of mFSO to sustain population diversity
indicates its robustness and adaptability in handling diverse
optimization
problems.
It
showcases
the
algorithm’s
capacity to explore different regions of the search space,
even in challenging scenarios with complex landscapes and
multiple optima.
In summary, the diversity analysis of the mFSO algo-
rithm demonstrates its effectiveness in maintaining popu-
lation diversity throughout the optimization process. The
sustained diversity enables mFSO to explore promising
search areas, enhance its exploration–exploitation strategy,
and increase the likelihood of attaining superior solutions.
By preventing premature convergence and facilitating
efﬁcient exploration, the algorithm showcases its robust-
ness and adaptability in tackling various optimization
problems.
6.7 The hybrid system results
This paper introduces the mFSO approach, which is a novel
and improved method based on the Firebug Swarm Opti-
mization method (FSO). The mFSO method is utilized to
Fig. 7 Convergence curve of mFSO compared to the other algorithms—CEC2020
Neural Computing and Applications (2024) 36:21517–21543
21535
123

---

## Page 20
determine the optimal size of an isolated hybrid system
conﬁguration. This conﬁguration involves the utilization of
PV panels, a biomass gasiﬁer system, and battery bank
units as a backup storage system. By comparing the results
of the mFSO technique with those of the original FSO,
SMA, and SOA techniques, it is demonstrated that the
recommended mFSO approach possesses superior proper-
ties. The control parameters for each optimization algo-
rithm are adjusted to allow for a maximum of 100
iterations, 50 time runs, and a search agent count of 20.
Figure 11 depicts the convergence curves for the proposed
mFSO optimization technique applied to the hybrid PV/
Biomass/Battery system, considering 100 iterations and 50
time runs.
Figure 12 illustrates the convergence curve of the opti-
mal objective function for the proposed mFSO approach,
along with the FSO, SMA, and SOA approaches, applied to
the recommended hybrid system. It is evident that the
suggested mFSO technique effectively minimizes the
objective function for the given scenario, achieving a value
of 0.09700573 after 43 iterations. The SOA method follows
closely with a value of 0.09703978 after 18 iterations,
followed
by
the
SMA
algorithm
with
a
value
of
0.09709755 after 29 iterations. Lastly, the FSO technique
yields a value of 0.09782792 after 23 iterations.
Fig. 8 Boxplot of mFSO compared to the other algorithms—CEC2020
21536
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 21
Table 6 showcases the top outcomes achieved for the
primary objective function and the most suitable compo-
nent sizing constraints utilizing the recommended mFSO,
FSO, SMA, and SOA approaches for the suggested system
conﬁguration. The mFSO optimization technique recom-
mended attained the lowest COE, amounting to 0.191861
$/kWh, and the least NPC, totaling 1,055,450 $, in com-
parison to the alternative optimization methods employed
in this study.
In order to assess the statistical efﬁcacy of each utilized
optimization technique, the following parameters were
selected to evaluate the effectiveness of the suggested
approaches. These parameters include the selection of
search agents, the number of iterations, and the number of
runs, all set to 20, 100, and 50, respectively. This statistical
evaluation aims to determine various metrics, including
maximum values (Max.), standard deviation (SD), mean,
relative error (RE), median, root mean square error
(RMSE), mean absolute error (MAE), and efﬁciency val-
ues. These values are presented in Table 7 as part of the
statistical analysis.
The annual cost distribution of the hybrid system’s
components using the mFSO method is depicted in Fig. 13.
It is evident that the battery units account for the highest
Fig. 9 Exploration–exploitation curves of mFSO—CEC2020
Neural Computing and Applications (2024) 36:21517–21543
21537
123

---

## Page 22
percentage cost, representing 46% of the total. This is
followed by the biomass system with 44%, the inverter
with 31%, and the PV arrays with 4%.
7 Conclusion
In this article, a novel and enhanced optimization algorithm
known as the modiﬁed Firebug swarm algorithm (mFSO)
has been employed to address the optimal sizing problem
of a hybrid PV/biomass/battery energy system. The
improvements made to the mFSO approach aimed to
overcome the limitations of the original Firebug swarm
optimization (FSO) technique by incorporating three key
operators: a) logistic chaotic local search, b) opposite-
based learning operator (OBL) technique, and c) phasor
and transition operators (TO & PO). The performance of
the proposed mFSO algorithm was assessed using the ten
functions from the CEC2020 benchmark. The results
obtained demonstrate that the mFSO algorithm outper-
formed the other algorithms tested (FSO, Slime mold
algorithm (SMA), Seagull optimization algorithm (SOA),
Fig. 10 Diversity curves of mFSO—CEC2020
21538
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 23
Harris Hawks optimization algorithm (HHO), Chernobyl
disaster optimizer (CDO), Whale Optimization Algorithm
(WOA), Prairie Dog Optimization Algorithm (PDO),
COVIDOA, and Sine Cosine Algorithm (SCA)) in solving
a majority of the optimization problems evaluated. To
determine whether the results of mFSO differed signiﬁ-
cantly from those of the rival algorithms, a Wilcoxon test
was conducted. The majority of the computed p-values
were below 0.05, indicating a signiﬁcant difference
between the mFSO and the other algorithms for most of the
CEC2020 functions. Furthermore, assessing the conver-
gence of the mFSO algorithm was essential to evaluate its
stability. Hence, the convergence of mFSO and its rival
algorithms was analyzed. The ﬁndings revealed that mFSO
exhibited a considerably higher convergence rate compared
to its competitors for most of the functions tested. This fast
convergence rate establishes mFSO as a competitive and
effective
method
for
addressing
global
optimization
problems.
To demonstrate the superior qualities of the recom-
mended mFSO algorithm, its results for the proposed
hybrid power system were compared with the optimization
outcomes obtained using the original FSO, SMA, and SOA
techniques. The investigation revealed that the suggested
mFSO technique successfully minimized the objective
function for the hybrid scenario to 0.09700573 after 43
iterations. Following mFSO, the SOA algorithm achieved a
minimized value of 0.09703978 after 18 iterations, while
the SMA algorithm obtained 0.09709755 after 29 itera-
tions.
Lastly,
the
FSO
method
yielded
a
value
of
0.09782792 after 23 iterations. When comparing the results
from the mFSO technique with other optimization methods
employed in this study, it was observed that the mFSO
approach produced the lowest energy cost (COE) of
0.191861 $/kWh and the lowest net present cost (NPC) of
1,055,450 $.
However, one of the main weaknesses of the mFSO
algorithm lies in its sensitivity to parameter settings.
Although the algorithm has shown promising results in our
experiments, determining the optimal parameter values can
be challenging. In future work, we plan to conduct a
thorough sensitivity analysis to identify the impact of dif-
ferent parameter conﬁgurations on the algorithm’s perfor-
mance. This analysis will allow us to provide better
guidelines for selecting suitable parameter values based on
the problem domain and characteristics. Another area for
improvement is the algorithm’s scalability. While the
mFSO has demonstrated effectiveness for moderate-sized
optimization problems, its performance may degrade when
applied to large-scale or high-dimensional problems. To
address this limitation, we intend to explore techniques
such as parallelization, adaptive parameter control, and
problem decomposition to enhance the scalability of the
algorithm. These enhancements will enable the Firebug
Swarm Algorithm to handle more complex and computa-
tionally demanding optimization tasks. Additionally, we
aim to investigate hybridization of the mFSO with other
optimization techniques to everage the strengths of multi-
ple algorithms can potentially improve the overall search
performance and enhance the algorithm’s ability to handle
challenging optimization landscapes.
Fig. 11 The mFSO
Convergence proﬁle for a 100
iteration 50 time run
Neural Computing and Applications (2024) 36:21517–21543
21539
123

---

## Page 24
Finally, a potential avenue for future research is to
explore the applicability of the modiﬁed Firebug swarm
algorithm (mFSO) in dynamic environments. Investigating
the algorithm’s performance and adaptability when faced
with changing conditions, such as time-varying energy
generation or load demands, would provide valuable
insights. This could involve developing strategies to
dynamically adjust the algorithm’s parameters or operators
to optimize system conﬁgurations in real time. Addition-
ally, exploring the algorithm’s robustness against uncer-
tainties
and
disturbances
would
further
enhance
its
practicality and effectiveness in real-world applications of
hybrid energy systems.
Fig. 12 The most effective
function’s convergence curve
using mFSO, FSO, SMA, and
SOA for 100 iterations
Table 6 The optimization
factors for the recommended
mFSO and other optimizers
mFSO
FSO
SMA
SOA
PV/Biomass/Battery
Best ﬁtness function
0.09700573
0.09782792
0.09709755
0.09703978
Iteration number
43
23
29
18
PV (units)
83
102
88
87
Generators (units)
1
1
1
1
Batteries (units)
97
93
100
98
COE ($/kWh)
0.191861
0.360809
0.194712
0.193097
NPC ($)
1,055,450
1,984,855
1,071,134
1,062,250
LPSP
0.041195
0.003729
0.039228
0.040917
Table 7 The statistical performance of the studied optimization algorithms
mFSO
FSO
SMA
SOA
Max
0.1087339
0.2041083
0.0997326
0.26618555
Mean
0.0973011
0.1267738
0.09841443
0.10199232
Median
0.0970059
0.1207653
0.09835415
0.09956087
SD
0.1676774
2.3919638
0.08677172
2.37239207
RE
0.1522199
14.993772
0.69103036
2.5518073
MAE
0.0002953
0.0292461
0.00134161
0.00495254
RMSE
0.001686
0.0376303
0.00159304
0.02400199
Efﬁciency
99.7226
79.2586
98.644284
97.151846
21540
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 25
Author
contributions Hoda
Abd
El-Sattar:
Conceptualization,
Methodology, Software Salah Kamel: Conceptualization, Methodol-
ogy, Software Fatma A Hashim: Conceptualization, Software, Writ-
ing- Original draft preparation Sahar F. Sabbeh: Conceptualization,
Software, Writing- Original draft preparation.
Funding Open access funding provided by The Science, Technology
& Innovation Funding Authority (STDF) in cooperation with The
Egyptian Knowledge Bank (EKB).
Data availability Data sharing is not applicable to this article as no
datasets were generated or analyzed during the current study.
Declarations
Conflict of interest The authors declare that there is no conflict of
interest regarding the publication of this manuscript.
Ethical approval This article does not contain any studies with human
participants or animals performed by any of the authors.
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
1. Anand P, Rizwan M, Bath SK et al (2022) Optimal sizing of
hybrid renewable energy system for electricity production for
remote areas. Iran J Sci Technol Trans Electr Eng 46:1149–1174.
https://doi.org/10.1007/s40998-022-00524-2
2. Emad D, El-Hameed MA, Yousef MT, El-Fergany AA (2020)
Computational methods for optimal planning of hybrid renewable
microgrids: a comprehensive review and challenges. Arch
Comput Methods Eng 27:1297–1319. https://doi.org/10.1007/
s11831-019-09353-9
3. Fathima AH, Palanisamy K (2015) Optimization in microgrids
with hybrid energy systems-a review. Renew Sustain Energy Rev
45:431–446. https://doi.org/10.1016/j.rser.2015.01.059
4. Bernal-Agustı´n JL, Dufo-Lo´pez R (2009) Simulation and opti-
mization of stand-alone hybrid renewable energy systems. Renew
Sustain Energy Rev 13:2111–2118. https://doi.org/10.1016/j.rser.
2009.01.010
5. Sinha S, Chandel SS (2014) Review of software tools for hybrid
renewable
energy
systems.
Renew
Sustain
Energy
Rev
32:192–205. https://doi.org/10.1016/j.rser.2014.01.035
6. Kumar S, Sharma S, Sood YR et al (2022) A review on different
parametric aspects and sizing methodologies of hybrid renewable
energy system. J Inst Eng (India) Series B 103:1345–1354.
https://doi.org/10.1007/s40031-022-00738-2
7. Fodhil F, Hamidat A, Nadjemi O (2019) Potential, optimization
and sensitivity analysis of photovoltaic-diesel-battery hybrid
energy system for rural electriﬁcation in Algeria. Energy
169:613–624. https://doi.org/10.1016/j.energy.2018.12.049
8. Mirzapour F, Lakzaei M, Varamini G et al (2019) A new pre-
diction model of battery and wind-solar output in hybrid power
system. J Ambient Intell Humaniz Comput 10:77–87. https://doi.
org/10.1007/s12652-017-0600-7
9. Yahiaoui A, Benmansour K, Tadjine M (2016) Control, analysis
and optimization of hybrid PV-diesel-battery systems for isolated
rural city in Algeria. Sol Energy 137:1–10. https://doi.org/10.
1016/j.solener.2016.07.050
10. Ashraf MA, Liu Z, Alizadeh A et al (2020) Designing an opti-
mized conﬁguration for a hybrid PV/diesel/battery energy system
based on metaheuristics: a case study on Gobi desert. J Clean
Prod 270:122467. https://doi.org/10.1016/j.jclepro.2020.122467
11. Krishan O, Suhag S (2019) Techno-economic analysis of a hybrid
renewable energy system for an energy poor rural community.
J Energy Storage 23:305–319. https://doi.org/10.1016/j.est.2019.
04.002
12. Halabi LM, Mekhilef S, Olatomiwa L, Hazelton J (2017) Per-
formance analysis of hybrid PV/diesel/battery system using
HOMER: a case study Sabah, Malaysia. Energy Convers Manag
144:322–339. https://doi.org/10.1016/j.enconman.2017.04.070
13. Ghadimi N, Sedaghat M, Azar KK et al (2023) An innovative
technique for optimization and sensitivity analysis of a PV/DG/
BESS based on converged Henry gas solubility optimizer: a case
study. IET Gener Transm Distrib. https://doi.org/10.1049/gtd2.
12773
14. Lata-Garcia J, Alvarez MP, Fiallos HM (2022) Technical eco-
nomic evaluation of the implementation of a photovoltaic/bio-
mass/energy storage hybrid energy system for isolated areas of
the Cerecita community. In: 2022 international conference on
electrical, computer and energy technologies (ICECET). IEEE,
pp 1–6
15. Li C, Zhang L, Qiu F, Fu R (2022) Optimization and enviro-
economic assessment of hybrid sustainable energy systems: the
case study of a photovoltaic/biogas/diesel/battery system in
Xuzhou, China. Energy Strategy Rev 41:100852. https://doi.org/
10.1016/j.esr.2022.100852
16. Al-Ghussain L, Darwish Ahmad A, Abubaker AM, Mohamed
MA (2021) An integrated photovoltaic/wind/biomass and hybrid
energy storage systems towards 100% renewable energy micro-
grids in university campuses. Sustain Energy Technol Assess
46:101273. https://doi.org/10.1016/j.seta.2021.101273
17. Saha S, Saini G, Chauhan A et al (2023) Optimum design and
techno-socio-economic analysis of a PV/biomass based hybrid
energy system for a remote hilly area using discrete grey wolf
Fig. 13 The mFSO breakdown of the yearly cost of the hybrid
system’s parts
Neural Computing and Applications (2024) 36:21517–21543
21541
123

---

## Page 26
optimization
algorithm.
Sustain
Energy
Technol
Assess
57:103213. https://doi.org/10.1016/j.seta.2023.103213
18. Singh A, Basak P (2021) Conceptualization and techno-economic
evaluation of microgrid based on PV/Biomass in Indian scenario.
J Clean Prod 317:128378. https://doi.org/10.1016/j.jclepro.2021.
128378
19. Kharrich M, Selim A, Kamel S, Kim J (2023) An effective design
of hybrid renewable energy system using an improved archi-
medes optimization algorithm: a case study of Farafra. Egypt
Energy Convers Manag 283:116907. https://doi.org/10.1016/j.
enconman.2023.116907
20. Singh S, Kaushik SC (2016) Optimal sizing of grid integrated
hybrid PV-biomass energy system using artiﬁcial bee colony
algorithm. IET Renew Power Gener 10:642–650. https://doi.org/
10.1049/iet-rpg.2015.0298
21. Gonzalez A, Riba JR, Esteban B, Rius A (2018) Environmental
and cost optimal design of a biomass–Wind–PV electricity gen-
eration system. Renew Energy 126:420–430. https://doi.org/10.
1016/j.renene.2018.03.062
22. Eteiba MB, Barakat S, Samy MM, Wahba WI (2018) Opti-
mization of an off-grid PV/Biomass hybrid system with different
battery technologies. Sustain Cities Soc 40:713–727. https://doi.
org/10.1016/j.scs.2018.01.012
23. Li J, Liu P, Li Z (2020) Optimal design and techno-economic
analysis of a solar-wind-biomass off-grid hybrid power system
for remote rural electriﬁcation: a case study of west China.
Energy
208:118387.
https://doi.org/10.1016/j.energy.2020.
118387
24. Alturki FA, Awwad EM (2021) Sizing and cost minimization of
standalone hybrid WT/PV/biomass/pump-hydro storage-based
energy systems. Energies (Basel) 14:489. https://doi.org/10.3390/
en14020489
25. Sun H, Ebadi AG, Toughani M et al (2022) Designing framework
of hybrid photovoltaic-biowaste energy system with hydrogen
storage considering economic and technical indices using whale
optimization algorithm. Energy 238:121555. https://doi.org/10.
1016/j.energy.2021.121555
26. Gado MG, Nada S, Ookawara S, Hassan H (2022) Energy
management of standalone cascaded adsorption-compression
refrigeration system using hybrid biomass-solar-wind energies.
Energy Convers Manag 258:115387. https://doi.org/10.1016/j.
enconman.2022.115387
27. El-Sattar HA, Kamel S, Hassan MH, Jurado F (2022) Optimal
sizing of an off-grid hybrid photovoltaic/biomass gasiﬁer/battery
system using a quantum model of Runge Kutta algorithm. Energy
Convers Manag 258:115539. https://doi.org/10.1016/j.enconman.
2022.115539
28. Kumar P, Pal N, Sharma H (2022) Optimization and techno-
economic analysis of a solar photo-voltaic/biomass/diesel/battery
hybrid off-grid power generation system for rural remote elec-
triﬁcation in eastern India. Energy 247:123560. https://doi.org/10.
1016/j.energy.2022.123560
29. El-sattar HA, Kamel S, Sultan HM, Zawbaa HM (2022) Optimal
design of photovoltaic, biomass, fuel cell, hydrogen tank units
and electrolyzer hybrid system for a remote area in Egypt. Energy
Rep 8:9506–9527. https://doi.org/10.1016/j.egyr.2022.07.060
30. El-Sattar HA, Kamel S, Hassan MH, Jurado F (2022) An effec-
tive optimization strategy for design of standalone hybrid
renewable energy systems. Energy 260:124901. https://doi.org/
10.1016/j.energy.2022.124901
31. Dehiba map, Tunisia, Tatawin — Google satellite. https://satel
lites.pro/Google/Dehiba_map#32.008000,10.701400,10.
Acces-
sed 28 Aug 2023
32. MERRA - SoDa. https://www.soda-pro.com/web-services/meteo-
data/merra?fbclid=IwAR2vTObCUaC3DpZev3PqLX0FwV-
XATjk0E2qDqp1ZRCWIcVxBQBv6eeWTUA. Accessed 6 Jul
2023
33. El-sattar HA, Kamel S, Sultan H et al (2021) Performance
analysis of a stand-alone PV/WT/biomass/bat system in Alrashda
village in Egypt. Appl Sci 11:10191
34. Zaki Diab AA, Sultan HM, Mohamed IS et al (2019) Application
of different optimization algorithms for optimal sizing of pv/
wind/diesel/battery storage stand-alone hybrid microgrid. IEEE
Access
7:119223–119245.
https://doi.org/10.1109/ACCESS.
2019.2936656
35. Sultan HM, Menesy AS, Kamel S et al (2021) An improved
artiﬁcial ecosystem optimization algorithm for optimal conﬁgu-
ration of a hybrid PV/WT/FC energy system. Alex Eng J
60:1001–1025. https://doi.org/10.1016/j.aej.2020.10.027
36. Diaf S, Diaf D, Belhamel M et al (2007) A methodology for
optimal sizing of autonomous hybrid PV/wind system. Energy
Policy
35:5708–5718.
https://doi.org/10.1016/j.enpol.2007.06.
020
37. Samy MM, Elkhouly HI, Barakat S (2021) Multi-objective
optimization of hybrid renewable energy system based on bio-
mass and fuel cells. Int J Energy Res 45:8214–8230. https://doi.
org/10.1002/er.5815
38. Samy MM, Mosaad MI, Barakat S (2021) Optimal economic
study of hybrid PV-wind-fuel cell system integrated to unreliable
electric utility using hybrid search optimization technique. Int J
Hydrogen
Energy
46:11217–11231.
https://doi.org/10.1016/j.
ijhydene.2020.07.258
39. El-Sattar HA, Kamel S, Jurado F (2020) Fixed bed gasiﬁcation of
corn stover biomass fuel: Egypt as a case study. Biofuels, Bio-
prod Bioreﬁn 14:7–19. https://doi.org/10.1002/bbb.2044
40. Diab AAZ, Sultan HM, Kuznetsov ON (2020) Optimal sizing of
hybrid solar/wind/hydroelectric pumped storage energy system in
Egypt based on different meta-heuristic techniques. Environ Sci
Pollut Res 27:32318–32340. https://doi.org/10.1007/s11356-019-
06566-0
41. El-Sattar HA, Sultan HM, Kamel S et al (2021) Optimal design of
stand-alone hybrid PV/wind/biomass/battery energy storage sys-
tem in Abu-Monqar. Egypt J Energy Storage 44:103336. https://
doi.org/10.1016/j.est.2021.103336
42. Noel MM, Muthiah-Nakarajan V, Amali GB, Trivedi AS (2021)
A new biologically inspired global optimization algorithm based
on ﬁrebug reproductive swarming behaviour. Expert Syst Appl
183:115408. https://doi.org/10.1016/j.eswa.2021.115408
43. Varol Altay E, Alatas B (2020) Bird swarm algorithms with
chaotic mapping. Artif Intell Rev 53:1373–1414. https://doi.org/
10.1007/s10462-019-09704-9
44. Yu Y, Gao S, Cheng S et al (2018) CBSO: a memetic brain storm
optimization
with
chaotic
local
search.
Memet
Comput
10:353–367. https://doi.org/10.1007/s12293-017-0247-0
45. Tizhoosh HR opposition-based learning: a new scheme for
machine intelligence. In: International conference on computa-
tional intelligence for modelling, control and automation and
international conference on intelligent agents, web technologies
and
internet
commerce
(CIMCA-IAWTIC’06).
IEEE,
pp 695–701
46. Yue CT, Price KV, Suganthan PN, et al (2019) Problem deﬁni-
tions and evaluation criteria for the CEC 2020 special session and
21542
Neural Computing and Applications (2024) 36:21517–21543
123

---

## Page 27
competition on single objective bound constrained numerical
optimization. Comput Intell Lab, Zhengzhou Univ, Zhengzhou,
China, Tech Rep 201911
47. Li S, Chen H, Wang M et al (2020) Slime mould algorithm: a
new method for stochastic optimization. Futur Gener Comput
Syst 111:300–323. https://doi.org/10.1016/j.future.2020.03.055
48. Dhiman G, Kumar V (2019) Seagull optimization algorithm:
theory and its applications for large-scale industrial engineering
problems. Knowl Based Syst 165:169–196. https://doi.org/10.
1016/j.knosys.2018.11.024
49. Hussien AG, Amin M (2022) A self-adaptive Harris Hawks
optimization
algorithm
with
opposition-based
learning
and
chaotic local search strategy for global optimization and feature
selection. Int J Mach Learn Cybern 13:309–336. https://doi.org/
10.1007/s13042-021-01326-4
50. Shehadeh HA (2023) Chernobyl disaster optimizer (CDO): a
novel meta-heuristic method for global optimization. Neural
Comput Appl 35:10733–10749. https://doi.org/10.1007/s00521-
023-08261-1
51. Mirjalili S, Lewis A (2016) The whale optimization algorithm.
Adv Eng Softw 95:51–67. https://doi.org/10.1016/j.advengsoft.
2016.01.008
52. Ezugwu AE, Agushaka JO, Abualigah L et al (2022) Prairie dog
optimization algorithm. Neural Comput Appl 34:20017–20065.
https://doi.org/10.1007/s00521-022-07530-9
53. Khalid AM, Hosny KM, Mirjalili S (2022) COVIDOA: a novel
evolutionary optimization algorithm based on coronavirus disease
replication lifecycle. Neural Comput Appl 34:22465–22492.
https://doi.org/10.1007/s00521-022-07639-x
54. Mirjalili S (2016) SCA: a sine cosine algorithm for solving
optimization problems. Knowl Based Syst 96:120–133. https://
doi.org/10.1016/j.knosys.2015.12.022
55. Wilcoxon F (1992) Individual Comparisons by Ranking Methods.
Springer, New York, NY, pp 196–202. https://doi.org/10.1007/
978-1-4612-4380-9_16
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
Neural Computing and Applications (2024) 36:21517–21543
21543
123

---
