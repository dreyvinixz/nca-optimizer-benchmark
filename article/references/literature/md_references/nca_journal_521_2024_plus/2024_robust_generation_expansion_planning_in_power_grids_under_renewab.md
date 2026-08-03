# Robust generation expansion planning in power grids under renewable energy penetration via honey badger algorithm

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-09485-5

---

## Page 1
ORIGINAL ARTICLE
Robust generation expansion planning in power grids
under renewable energy penetration via honey badger algorithm
Adel A. Abou El-Ela1 • Ragab A. El-Sehiemy2
• Abdullah M. Shaheen3 • Ayman S. Shalaby4 •
Mohamed T. Mouwaﬁ1
Received: 13 August 2022 / Accepted: 14 January 2024 / Published online: 23 February 2024
 The Author(s) 2024
Abstract
Robust reliability Generation Expansion Planning (GEP) turns out to be a crucial step for an efﬁcient energy management
system in a modern power grid, especially under renewable energy employment. The integration of all such components in
a GEP model makes it a large-scale, nonlinear, and mixed-variable mathematical modeling problem. In this paper, the
presence of wind energy uncertainty is analyzed. Both long and short-term uncertainties are incorporated into the proposed
GEP model. The ﬁrst step concerns the impact of long-term wind uncertainties through the annual variations of the
capacity credit of two real sites in Egypt at Zafaranh and Shark El-ouinate. The second step deals with the short-term
uncertainties of each wind site. The wind speed uncertainty of each wind site is modeled by probability distribution
function. Then, wind power is estimated from the wind power curve for each wind site and Monte-Carlo Simulation is
performed. Fast Gas Turbine and/or Pump Hydro Storage are incorporated to cope with short-term uncertainties. Sensi-
tivity analysis is implemented for 3, 6, and 12 stages as short and long planning horizons to minimize the total costs with
wind energy penetration and emission reduction over planning horizons. Also, a novel Honey Badger Algorithm (HBA)
with model modiﬁcations such as Virtual Mapping Procedure, Penalty Factor Approach, and the Modiﬁed of Intelligent
Initial Population Generation is utilized for solving the proposed GEP problem. The obtained results are compared with
other algorithms to ensure the superior performance of the proposed HBA. According to the results of the applicable test
systems, the proposed HBA performs better than the others, with percentage reductions over CSA, AO, BES, and PSO
ranging up to 4.2, 2.72, 2.7, and 3.4%, respectively.
Keywords Emission reduction constraint  Honey badger algorithm  Monte-Carlo simulation  Reliability constrained
generation expansion planning  Virtual mapping procedure  Wind uncertainties
List of symbols
i
Discount rate
K
Added unit in stage t which
are
selected
of
different
technologies
N
Number of selected candi-
date units of technology k
ut
Capacity vector of all candi-
date unit types in the stage
to
Number of years between the
reference date for discount-
ing and the ﬁrst year of study
s
Number of years in each
stage t
CIk
Investment cost of each new
candidate unit k added in
stage t
SV ut
ð Þ
Salvage value cost
EENS
Expected energy not served
O Xt
ð
Þ
Expected energy not served
cost
& Ragab A. El-Sehiemy
elsehiemy@eng.kfs.edu.eg
1
Electrical Engineering Department, Faculty of Engineering,
Menouﬁya University, Shebeen El-Kom 32511, Egypt
2
Electrical Engineering Department, Faculty of Engineering,
Kafrelsheikh University, Kafr El-Shaikh 33516, Egypt
3
Department of Electrical Engineering, Faculty of
Engineering, Suez University, Suez 43221, Egypt
4
Middle Delta Electricity Production Company (MDEPCo),
Talkha, Mansoura, Egypt
123
Neural Computing and Applications (2024) 36:7923–7952
https://doi.org/10.1007/s00521-024-09485-5
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
dk;t
Salvage
factor
of
unit
k added in stage t
T
Number
of
stages
in
the
planning horizon
Xt, Gt;k
The capacity and the expec-
ted energy produced for all
existing and selected candi-
date units of each type k
FOMk; VOMk
Fixed and variable operating
and maintenance costs
CEENS
Cost of EENS in $/MWh
k
Percent
reduction
in
total
emission from the base case
V
Wind speed
xi
Honey badger position
lbi, ubi
Lower and upper limits of
each position in the search
space
r1; r2; r3; r4; r5; r6; r7
A random number between 0
and 1
S
Source strength
di
Distance between xprey prey
and ith badger position
itermax
Maximum iterations number
Ch
Constant equal to 2
b
Ability of the honey badger
to get food which is greater
than
or
equal
to
1
(default = 6)
T
^
Number of hours
LOLE
Loss of load expectation
IC
Total installed capacity
LP
Peak load
Ei
Expected energy produced of
the ith generator
pi
Availability
of
the
ith
generator
Ui
Sum of capacities from 1st to
ith generator
invadd, operadd, fixadd, and
Sadd
Investment,
salvage,
ﬁxed
and operation costs of FGT
and PHS generating units
EEF
Equivalent energy function
PDF
Probability
distribution
function
MCS
Monte-Carlo Simulation
Xt;k
Total capacity of existence
and new units
Umax;t
Maximum
construction
number of each generation
type at stage t
LDt
Peak load in stage t
Xt;j
Capacity of fuel type j in
stage t
SRmin; SRmax
Minimum
and
maximum
required reserve capacity in
stage t
e
Maximum reliability criteria
LOLP
Loss of load probability
ELDC
Effective
load
distribution
curve
CF
Capacity factor
vi, vr, vo
Cut-in,
rated,
and
cut-out
wind speeds
K, C
Shape
and
scale
Weibull
parameter
FR j
min, FR j
max
Lower and upper bounds of
jth fuel type mix ratio in
stage t
Xt;w
Wind output power of each
wind site
emj
Emission coefﬁcient
c
Discrete step size of the load
Yw
State of wind site penetration
in stage t
LDe
Effective load
LDd
Original load
LDoi
Probabilistic load caused by
the forced outage of the ith
generator.
qi
FOR of the ith generator
TCi
Objective function modiﬁed
by PFA of ith individual
Obi
Objective
function
value
without addition penalty fac-
tors for any constraints
x
Penalty factor for the con-
straints validated
p1; p2; p3; p4; p5
Violation
amounts
of
the
constraint of spinning reserve
margin;
fuel
mix
ratio,
LOLP,
wind
penetration
level, and emission reduc-
tion, respectively
a1, a2, a3 and a4
Polynomial
coefﬁcients
using
polyﬁt
function
in
MATLAB
xi
Honey badger position
VMP
Virtual mapping procedure
MIIPG
Modiﬁed of intelligent initial
population generation
CAPmin;t, CAPmax;t
Minimum
and
maximum
required
capacities
for
a
stage t
7924
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 3
CAPmin;t1; CAPmax;t1
Minimum
and
maximum
capacities
in
the
previous
stage
PFA
Penalty factor approach
TCi
Objective function modiﬁed
by PFA of ith individual
PHS
Pump hydro storage
Obi
Objective
function
value
without
additional
penalty
factors
FGT
Fast gas turbine
1 Introduction
1.1 Motivation and main concepts
Generation Expansion Planning (GEP) is one of the most
relevant problems in the planning of electric energy sys-
tems. It addressed the problem of identifying the most
adequate technology, expansion size, sitting, and timing for
the construction of new plant capacity considering eco-
nomic criteria and technical power system constraints.
However, it is necessary to guarantee that demands will be
continuously supplied in all conditions were either an
unexpected peak demand is occurred or an important unit
fails [1]. The expansion planning criteria can be considered
as conditions and limitations based on the decision-making
process [2]. They are reﬂections of the positive features,
which the planners would like to have in any future plan
[3, 4] and preparing preventive control actions for active
power [5] and reactive power issues [6].
Recently, the inclusion of uncertainties with various
aspects has been considered in the GEP model as an
effective approach to energy efﬁciency, conservations, CO2
emission and environmental concerns. Thus, the planning
should be investigated to affect by changing in parameters
due to uncertainties and its capability to accommodate any
changes [7]. In general, uncertainty analysis is critical for
assessing the risks of any system that contains any type of
uncertainty. The uncertainty which depends on nondeter-
ministic in nature cannot be reduced while the uncertainty,
which caused by limited knowledge about the system, is
reduced as the search space expands [8]. However, inte-
grating high share Renewable Energy Sources (RESs)
within the power system planning had imposed a signiﬁ-
cant impact of uncertainties. Therefore, ignoring the vari-
ability and stochastic nature of RES within the GEP model
may result in a lack of robustness of the planning results.
Due to the ﬂuctuation and the unpredictable characteristics
of wind speed, wind power will have signiﬁcant impact on
the system security, stability, and reliability [9]. Therefore,
techniques and approaches for dealing with such wind
uncertainties should be more efﬁcient and accurate which
can be classiﬁed as probabilistic and possibilistic approa-
ches [10]. Besides wind power uncertainty, there are other
uncertainty sources such as load growth, fuel price, fuel
costs, and the outage of generating units have also impact
on expansion plans. Moreover, there are several studies
considering wind energy penetration and PV as renewable
sources for microgrid system such as [11, 12].
1.2 Literature review
In the planning process, the nature of the GEP problem is
nonlinear, mixed-integer, highly constrained, and dynamic.
The study of GEP without considering RESs has been
introduced such as [13, 14] based on minimizing the total
costs and satisfying reliability constraints. In recent years,
several studies have been conducted on the reﬂection of
environmental protection by adding emission limit con-
straints. Also, the impact of integrated RESs in power
systems and their resulting uncertainties has been treated in
the modeling of GEP problem. Expansion capacity plan-
ning requires not only total costs minimization, but also
wind power uncertainty analysis and emission control
should be handled over the planning horizon [15, 16].
The GEP problem has been solved by several analytical
and optimization techniques without considering uncer-
tainty analysis such as a Non-dominated Sorting Genetic
Algorithm version II (NSGA-II), Modiﬁed Shufﬂed Frog
Leaping Algorithm (MSFLA) that have been used in Refs.
[14, 18 and 17], respectively. Also, Loss Of Load Proba-
bility (LOLP) has been computed as a reliability criterion
in GEP problem which is evaluated based on the cumula-
tive method as [19] where it has been modeled as Mixed
Integer Programming (MIP). As a result, a model of least
cost generation capacity expansion to control carbon
dioxide emissions was presented, taking into account the
effects of uncertain load and wind power generation
[20, 21]. Moreover, the generation and transmission
expansion planning (TEP) has been addressed without
considering RESs uncertainty as [22]. The GEP dimen-
sionality is large which the length of a string is equal to the
product of the number of planning stages and the number
of candidate unit’s types. So that, the Virtual Mapping
Procedure (VMP), Penalty Factor Approach (PFA), and the
Modiﬁed
of
Intelligent
Initial
Population
Generation
(MIIPG) have been accomplished to decrease the GEP
problem search space and reduce the computational time
[17, 23].
Neural Computing and Applications (2024) 36:7923–7952
7925
123

---

## Page 4
In addition to the above, RES uncertainty is incorpo-
rated into generation and transmission expansion planning
for a long and short-term planning horizon. In [24], the
GEP problem with a certain penetration level of RESs has
been solved by dynamic programming, while the wind and
solar plants was modeled in Wein Automatic System
Planning (WASP-IV).Besides, the effect of renewable
energy uncertainties was assessed in the reliability and
stability of power system. So that, it is important to develop
decision support tools to help generation companies for
achieving maximum their proﬁt in a deregulated electricity
market as [25, 26]. Also, a coordinated generation and
transmission expansion planning in a deregulated electric-
ity market have been addressed with wind power uncer-
tainty analysis as [27]. The wind farm uncertainty was
modeled by a normal PDF, and MCS has been utilized to
include the uncertainty into the GEP or GEP/TEP problem.
The combined GEP and TEP were handled with correlation
of load and generation uncertainties that system uncer-
tainties have been modeled with PDF and MCS to generate
different random scenarios [28]. Also, Particle Swarm
Optimizer (PSO) has been used to solve the TEP problem
with reactive power planning and consideration of wind
and load uncertainties as [29] while SFLA was performed
in [30]. MCS was utilized to simulate the wind output
power based on its PDF. Also, a deep learning method is
one of the recent methods to deal with time series data such
as the long short-term memory (LSTM) network algorithm
which have been used for the same problems as in [31, 32].
But it has more steps to create output and consume more
time which is not effective for expansion planning. How-
ever, the wind power uncertainty has been represented by
annual variation of capacity factor based on historical data
of wind location where the effect of wind power variation
is analyzed at a certain probability of expectation [33].
Furthermore, both long and short-term wind power uncer-
tainties were modeled within the GEP problem. The annual
variation of the capacity credit was used to simulate the
wind power long-term uncertainty. On the other side, the
short-term uncertainty was simulated based on the hourly
variation of wind power as [34]. Added to that, reserve
margin has been adopted to cope with the uncertainty effect
[34], while additional capacities of Pump Hydro Storage
(PHS) and Fast Gas Turbine (FGT) have been utilized to
cope with short-term uncertainty problems [35]. The
problem of short-term uncertainty was modeled using the
autoregressive moving average model. The main shortage
in [33–35] is that the forced outage rate (FOR) of gener-
ating units was not taken into account at variable cost
calculations where the FOR constitutes serious impacts on
energy supplied of each generating units and reliability
indies.
Furthermore, different battery technologies and demand
side management options have been used to cope with the
renewable energy uncertainties for off-grid hybrid renew-
able energy systems [36]. In this paper, the PV and biomass
as renewable energy sources have been considered but the
wind energy, which has more intermittent and variability of
output power and affect the cycling charge of batteries, was
not considered. However, the wind energy penetration in
microgrid system design is considered in [37, 38], but it
was dispatched as a certain value and wind energy uncer-
tainty, and variability was not taken into account that has
big effect on the system reliability. Furthermore, For the
optimal sizing and techno-economic assessment of the
intended hybrid microgrid system consist of solar diesel
generator, PV, battery storage, and wind turbine, four
dispatch approaches have been unitized: load following,
generator order, combined dispatch, and cycle charging
strategy while the system reliability study were carried out
using Dig-SILENT Power Factory [39, 40]. Also, uncer-
tainty of wind energy was not considered through system
reliability calculation. Moreover, the wind speed and
power conversions uncertainties are ignored in [41] and the
wind power is calculated by speciﬁed model not based on a
wind site study.
For reliability indies and variable cost calculations, the
probabilistic production cost simulation using the Equiva-
lent Energy Function (EEF) [14, 42] and Effective Load
Distribution Curve (ELDC) [43] methods shows suit-
able accuracy with small computational time. Moreover,
the RES uncertainties have been handled by the point
estimate method for yearly peak loads uncertainties [44]
and for distributed GEP in power distribution networks
[45]. In [46, 47], the uncertainty of wind power has been
modeled as a constraint depending on the wind availability
in each hour. Therefore, the adoption of an hourly com-
mitment of generating unit was considered to show the
short-term impacts of long-term strategies through the
decision-making process. In [15], the GEP analysis with
different electricity scenarios for a mixed hydro-thermal
and wind plants was performed which have impact in terms
of costs and CO2 emissions over the planning period. The
carbon emissions have been added as an objective function
as in [48].
Considering the incorporation of RESs into GEP prob-
lem, a whale optimization algorithm was carried out with
adjustment strategies to decrease the GEP problem search
space such as MIIGP, VMP, and PFA [49]. However, wind
and solar output power have been studied at certain sce-
narios of penetration and emission reduction levels. In [50],
differential evolution algorithm was used for minimizing
the least cost GEP with certain penetration levels of wind
capacity with emission reduction with certain penetration
levels of solar power plants as [51, 52]. Also, wind power
7926
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 5
was considered at only speciﬁc capacities through the
modeling of GEP problem without discussing varied sce-
narios [53]. However, there are several wind scenarios
which are not considered to lead to negative impact in
reliability and security system.
1.3 Research gap and main contribution
RESs uncertainty consideration has a vital role in the
planning and operation analysis of power system. Uncer-
tainty analysis has an impact on the reliability and stability
of the power system. So that, it is necessary, integrating the
RES uncertainty analysis into the expansion planning
problems. The presence of wind energy uncertainties is
incorporated into the proposed GEP model in this paper.
The ﬁrst step is to assess the impact of long-term wind
uncertainties using annual variations in capacity credit at
two real-world sites in Egypt, Zafaranh and Shark El-oui-
nate. The second step addresses each wind site’s short-term
uncertainties. A PDF is used to model the wind speed
uncertainty at each wind site. The wind power curve for
each wind site is then used to estimate wind power, and
MCS is performed. Sensitivity analysis is used for three,
six, and twelve stages as short and long planning horizons
to reduce total costs associated with wind energy penetra-
tion and emission reduction constraints over planning
horizons.
The contributions of this paper can be summarized as
follows:
•
A robust multi-stage reliability constrained GEP model
with wind power uncertainty and emission reduction is
proposed to minimize the total costs under satisfaction
constraints.
•
The wind power is modeled by a PDF and MCS to
simulate their accompanied uncertainties into the GEP
model where two real wind sites with different mean
and variance wind speeds are simulated.
•
PHS and FGT are proposed to cope with the impact of
short-term uncertainty.
•
ELDC as a probabilistic production simulation (PPS)
method is utilized to calculate the reliability indies and
variable costs.
•
The GEP results are analyzed at different reserve
margins.
•
A novel HBA with adjustable strategies of VMP, PFA,
and MIIPG is proposed to achieve optimal and robust
expansion planning.
1.4 Paper structure
The following portions of this work are organized as fol-
lows: Section II presents the conventional GEP model,
whereas Section III establishes the proposed GEP model
including the wind power uncertainty. Section IV describes
the developed HBA for reliability constrained dynamic
GEP. Section V deﬁnes the discussions and simulation
ﬁndings. Finally, section VI concludes this paper.
2 Conventional GEP model
The Conventional GEP model as base case study can be
formulated [14, 17, and 49] as follows:
2.1 Objective function
The objective function of the GEP problem is to minimize
total costs over the planning period. In this context, the
candidate units are responsible for the investment and
salvage costs, but the candidate and existing units are
jointly responsible for the operation, maintenance, and
outage expenses.
Capital investment cost (I ut
ð ÞÞ is the cost of purchasing
new candidate units that can be provided by
I ut
ð Þ ¼ ð1 þ iÞtc 
X
N
k¼1
CIk  ut;k


ð1Þ
tc ¼ to þ s  t  1
ð
Þ
ð2Þ
•
Salvage value cost SV ut
ð Þ is the actual cost of
producing a unit at a speciﬁc time, considering the
depreciation rate, which is determined as follows:
SV ut
ð Þ ¼ ð1 þ iÞTs 
X
N
k¼1
dk;t  CIk  ut;k


ð3Þ
Ts ¼ to þ s  T
ð4Þ
The investment cost for a candidate unit chosen by
the expansion plan is assumed at the start of the stage
when it enters service. The salvage value, on the other
hand, is determined at the conclusion of the planning
horizon [54].
•
Operating and maintenance cost (M Xt
ð
ÞÞ is the oper-
ational and maintenance costs for existing and new
candidate units which is assumed to occur in the middle
of the corresponding planning stage as follows:
M Xt
ð
Þ ¼
X
s1
y¼0
1 þ i
ð
Þ tcþ0:5þy
ð
Þ
h

X
N
k¼1
FOMk  Xt;k þ VOMk  Gt;k


#
ð5Þ
Neural Computing and Applications (2024) 36:7923–7952
7927
123

---

## Page 6
Each generation unit’s ﬁxed cost is determined by its
capacity, and its variable cost is determined by the antici-
pated amount of energy that each generation unit will
produce at each stage. Therefore, good prediction of the
variable costs and reliability indies is essential to provide
more precise estimation of the predicted energy produced
by each generation unit.
Based on the expected energy not served (EENS), it is
possible to calculate the anticipated energy generated by
each generation unit. The EENS and LOLP, which are
reliability indies, can be calculated by conventional method
or PPS method to obtain cost modeling. The established
capacity outage probability table, load probability table,
and margin between them are the components of the tra-
ditional technique, which is used to compute reliability
indies [55]. Because of the generous size of the GEP
problem, this conventional method is not suitable and takes
more computational time. Thus, there are other PPS
methods that are more efﬁcient for estimating the variable
costs and the reliability indies with smaller computational
time. In this context, the EEF method is one of PPS
methods, but it depends on the greatest common factor for
all adding capacities of existing and candidate units
[42, 49]. Also, the ELDC is another method for any addi-
tional capacity in the planning [43].
•
Expected energy not served (EENS) cost
The EENS reﬂects an important reliability status in
electrical power systems where customer satisfaction
with continuous supply will inﬂuence the utility’s
competitive ability. Thence, continuous energy supply,
which indicates better system reliability, can achieve
customer satisfaction. However, depending on its FOR,
any generating unit might not be available at any given
time. As a cost term, EENS should be minimized
because it cannot be made zero. This can be stated as
follows:
O Xt
ð
Þ ¼
X
s1
y¼0
½ð1 þ iÞðtcþ0:5þyÞ  EENSt  CEENS
ð6Þ
As a result, ﬁnding the best expansion planning is
comparable to ﬁnding the objective function for solving
the reliability restricted GEP problem as follows:
Ob ¼
X
T
t¼1
I ut
ð Þ þ M Xt
ð
Þ þ O Xt
ð
Þ  SV ut
ð Þ
½

ð7Þ
2.2 Constraints
•
Upper construction limit (utÞ: the quantity of all tech-
nology that has committed to meeting the stage t
maximum construction number is as follows:
0  ut  Umax;t
ð8Þ
•
Spinning reserve constrain (SR)t: The existing and new
selected candidate units must meet the predicted load
demand and capacity reserve margin limitation, which
is represented as follows:
1 þ SRmin
ð
Þ  LDt 
X
N
k¼1
Xt;k  1 þ SRmax
ð
Þ  LDt
ð9Þ
•
Fuel mix ratio: The capacity of all the existing units
must be limited when choosing candidate technology
for expansion planning as follows:
FR j
min 
Xt;j
PN
k¼1 Xt;k
 FR j
max
ð10Þ
Reliability constraint (LOLP): To continue supplying
electricity continuously, both the new and current units
need to meet the reliability criterion. A reliability metric
called Loss of Load Probability (LOLP) is typically used to
show how robust a system is in the face of unforeseen
events.
LOLPðXtÞ  e
ð11Þ
2.3 Effective load distribution curve (ELDC)
The calculation of expected energy produced by each
generation unit, and reliability indices are especially criti-
cal issues for solving the GEP problem. For that purpose,
PPS methods have been widely used for such calculations.
The ELDC is used in this study for LOLP, and EENS
calculation. Then, expected energy produced is calculated
based on EENS calculation [43]. In the ELDC, the capacity
and FOR of the generator i are equivalent to ci and 0 with
the ﬁctitious load added to the original load. The sum of the
original load and the probabilistic additional load is called
effective load as formulated as:
LDe ¼ LDd þ
X
N
i¼1
LDoi
ð12Þ
The ELDC is described in Fig. 1 can be calculated as:
Ui LDe
ð
Þ ¼
Z
Ui1 LDe  LDoi
ð
Þfoi LDoi
ð
ÞdLDoi
ð13Þ
where Ui LDe
ð
Þ is the PDF of the ELDC convolved with the
7928
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 7
PDFs of the outage capacities of the generators, 1st to
ith;Ui1 LDe  LDoi
ð
Þ is the PDF of the ELDC convolved
with the PDFs of the outage capacities of all the generator,
1st to N-1. Also,f oi LDoi
ð
Þ is the PDF of the outage capacity
of the ith generator. The ELDC can be generated by con-
volving the load curve and the plant outage capacity which
leads to the following:
PnðxÞ ¼ 1  qi
ð
ÞPn x
ð Þ þ qiPn x  c
ð
Þ
ð14Þ
Using the UN x
ð Þ, LOLE and EENS can be calculated
using ELDC as following:
EENS ¼
Z
ICþLP
IC
UN x
ð Þdx ¼
X
x¼ICþLP
x¼IC
P
nðxÞ
ð15Þ
EENS ¼
Z
ICþLP
IC
UN x
ð Þdx ¼
X
x¼ICþLP
x¼IC
P x
ð Þ
ð16Þ
The expected energy produced Ei of the ith generator
can be derived as follows:
Ei ¼ T pi
Z Ui
Ui1
Ui1 LD
ð
ÞdLD
ð17Þ
The probabilistic generated energy DEi of the ith gen-
erator can be calculated as following:
DEi ¼ EENSi1  EENSi
ð18Þ
3 Proposed GEP model including wind
power uncertainty
The impacts of long and short-term wind power uncer-
tainties are considered in the proposed robust GEP model.
The long-term uncertainty is represented based on the wind
capacity credit of each wind site which achieves the
expansion constraints. Also, the short-term uncertainty is
tackled by the MCS model.
3.1 Proposed GEP considering wind energy long-
term uncertainty
Long-term uncertainty of the wind power is embedded into
the planning model through the variation of the wind
capacity credit of each site. The reliability indices such as
LOLP and EENS are calculated based on existing and
candidate units by PPS methods. FOR of wind plants are
calculated, in this study, by sliding window technique as
[49, 50]. It is assumed that FOR values for wind energy are
constant over the study period. Based on that technique, the
capacity factor of each wind site is estimated by annual
wind energy produced divided by the rated capacity. The
capacity factor is calculated using Weibull distribution
parameters of wind speed [35] which is different for each
wind site as follows:
CF ¼
eðvi
CÞ
K  eðvr
CÞK
ðvr
CÞK  ðvi
CÞK
 eðvo
C ÞK
"
#
ð19Þ
However, the FOR values for wind plant of each site are
calculated as follows:
FOR ¼ 1  CF
ð20Þ
The output of a wind site is related to the output of a
single wind turbine, and it scales linearly with the number
of wind generators. All wind turbines have similar input–
output characteristics since installing different wind tur-
bines in the same wind site is not usual.
Consequently, the wind power from two Egyptian wind
sites (Zafaranh and Shark El-Ouinate) is added to candidate
units in the base case. The long-term uncertainty of the
wind power is imposed into the planning model through the
variation of the wind capacity credit of each site. The
traditional objective function of GEP model described in
Eq. (7) is updated by adding the costs of investment invw,
operating operw, and ﬁxed fixw terms of each wind site as
follows:
oblong ¼ ob þ obw
ð21Þ
obw ¼ invw þ operw þ fixw  Sw
ð22Þ
Fig. 1 Reliability indices and
ELDC
Neural Computing and Applications (2024) 36:7923–7952
7929
123

---

## Page 8
Also, additional constraints related to the two wind sites
should be merged which are the wind level penetration and
emission reduction constraints over all planning period as
follows:
0:1 
X
Xt;k 
X
T
t¼1
X
2
w¼1
Xt;w  0:2 
X
Xt;k
ð23Þ
X
Xt;w [ 0
ð24Þ
X
T
t¼1
X
N
j¼1
ðXt;jðjÞ  emjÞ\k
ð25Þ
For ease of the construction and manpower, two wind
sites should not be selected in the same stage which is
represented in the following constraint:
X
2
w¼1
Yw  1
ð26Þ
3.2 Proposed GEP considering wind energy
short-term uncertainty
The MCS is used to include wind short-term uncertainty in
the problem. Each site of Zafaranh and Shark El-ouinate
has different mean and variance wind speed which affect
the output capacity of it. Therefore, Weibull distribution
parameters are assessed individually for each site. More-
over, there are two main sources of uncertainties related to
wind RESs: wind speed forecast uncertainty and the wind-
electrical power conversion curve [8]. The wind speed
uncertainty is simulated by accurate estimation of Weibull
parameters, while the wind speed power conversion curve
is selected based on each wind site characteristics. The
scenario-based MCS is a commonly used tool to deal with
wind speed uncertainty in the problem [56]. For each
scenario of MCS, the wind speed is a randomly generated
based on its Weibull PDF which is characterized by the
following equation [57, 58]:
f v
ð Þ ¼
K
C
  v
C
 	K1
exp  v
C
 	K


ð27Þ
where v is the wind speed.
The most efﬁcient model for each site is applied based
on the minimum error of energy density for Zafaranh gz v
ð Þ
and Shark El-ouinate gs v
ð Þ sites, respectively [59] as
follows:
gz v
ð Þ ¼
v  vi
vr  vi

2
ð28Þ
gs v
ð Þ ¼ a1v3 þ a2v2 þ a3v þ a4
ð29Þ
The general form can be represented as the following
equation:
p v
ð Þ ¼
pr
vr  v  vo
pr  g v
ð Þ
vi  v  vr
0
otherwise
8
<
:
ð30Þ
The objective function of the proposed GEP model with
short-term uncertainty ðobscÞ is deﬁned as adding the costs
of adding units ðobaddcapÞ to the base case ðobÞ and wind
costs ðobwÞ as follows:
obsc ¼ oblong þ obaddcap
ð31Þ
obadd ¼ invadd þ operadd þ fixadd  Sadd
ð32Þ
For each scenario, all constraints for the base case and
long-term uncertainty are examined. The addition of new
FGT and/or PHS units under a wind power violation sce-
nario could alter the system’s fuel mix ratio Eq. (10) and
overall emission Eq. (25). Therefore, whenever a new unit
is added, those constraints need to be checked again.
4 Developed HBA for reliability constrained
dynamic GEP Problem
4.1 Honey badger algorithm
HBA is an entirely novel meta-heuristic technique that is
based on how honey badgers hunt for their prey in an
intelligent way. It is brave and prefers to spend time alone
in self-made burrows, only meeting other badgers to mate.
To access bird nests and beehives for food, it can also
climb trees. A honey badger ﬁnds its prey through snifﬁng,
digging, or following a honey guide bird, which can ﬁnd
beehives
but
cannot
obtain
honey.
Exploration
and
exploitation phases are developed from the honey badger’s
dynamic search behavior using digging and honey-ﬁnding
methods [60]. Firstly, an initial population is generated
based on the number of honey badger and their respective
positions as follows:
xi ¼ lbi þ r1  ubi  lbi
ð
Þ
ð33Þ
The intensity (Ini), which is related to concentration,
prey strength, and the distance between the prey and the
honey badger, is then speciﬁed. The motion of the prey will
be fast at high smell intensity and vice versa. The intensity
is deﬁned as follows:
Ini ¼ r2 
S
4pd2
i
ð34Þ
S ¼ ðxi  xiþ1Þ2
ð35Þ
di ¼ xprey  xi
ð36Þ
7930
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 9
The density factor
a
ð Þ is speciﬁed and updated which
controls time varying randomization to ensure a smooth
transition from exploration to exploitation phase. So that,
this factor decreases with iterations to decrease random-
ization with time as follows:
a ¼ Ch  exp
t
itermax


ð37Þ
A ﬂag (F), which alters the search direction, is generated
to enhance escaping from local to optima regions. The
positions of the agents are then updated, and xnew is mod-
iﬁed in accordance with the two stages of the digging phase
and the honey phase as follows:
F ¼
1
if r3  0:5
1
otherwise

ð38Þ
Then, the positions of agent’s xnew are updated via
digging and honey phases A. The honey badger’s digging
phase resembles the shape of a cardioid, which can be
simulated by doing the following:
xnew ¼ xprey þ F  b  I  xprey þ F  r4  a  di
 cos 2pr5
ð
Þ  1  cos 2pr6
ð
Þ
½

j
j
ð39Þ
where b is the ability of the honey badger to get food which
is greater than or equal to 1 (default = 6).
In the honey phase, a honey badger follows the honey
guide bird to reach beehive which is simulated as follows:
xnew ¼ xprey þ F  r7  a  di
ð40Þ
The ﬂowchart diagram of the HBA is shown in Fig. 2.
Therefore, a honey badger performs search closed to prey
location, and the searching process is inﬂuenced by time
varying (a). Also, the HBA performance is signiﬁcantly
affected by two user-deﬁned parameters (bandCh) so that
these parameter values should be selected carefully. In this
context, the best parameter values (b ¼ 6; andCh ¼ 2) of
the proposed algorithm are taken from [60].
B. Enhanced HBA for the proposed large-scale GEP
model.
The proposed GEP problem is a high large dimensional
problem with multiple conﬂicting objectives, uncertainty
analysis and nonlinear constraints which represents a
complex optimization problem. Thus, some modiﬁcations
are proposed to enhance the HBA to deal with this prob-
lem. VMP, PFA, and MIIPG improve the effectiveness of
the meta-heuristic algorithm as follows [23, 49]:
(1)
VMP
This step aims to transform each combination of
candidate units into a dummy variable which repre-
sents a position of each agent in the search space.
Thus, the decision variable of each stage is repre-
sented by single variable only which needs less
memory space. Further, if the mapped variable took
part in all related solutions, a slight change in the
mapped variable will reduce the infeasible solutions.
Thus, a multivariable could be mapped into a single
variable, which is the decision variable in this
problem. As ﬁve diverse types of units are assumed
to be decision variables for each stage, the array size
of the problem solution is increased by multiples of
5.
(2)
MIIPG
Generation of initial population is incorporated to
decrease the search space and improve performance
of heuristic algorithm. Thus, the minimum and
maximum cumulative capacity is assumed to be
available in the previous stages. Consequently, the
minimum and maximum required capacity for each
stage can be calculated based on reserve margin as
follows:
CAPmin;t ¼ 1 þ SRmin
ð
Þ  LDt  CAPmin;t1
ð41Þ
CAPmax;t ¼ 1 þ SRmax
ð
Þ  LDt  CAPmax;t1
ð42Þ
whereCAPmin;t and CAPmax;t are the minimum and
maximum required capacities for a stage t which are
based on forecasted load demand and reserve mar-
gin; CAPmin;t1 and CAPmax;t1 are minimum and
maximum capacities in the previous stage which are
the sum of capacities of existence and selected units.
Their values are always updated with each selected
candidate combination.
Figure 2 shows the ﬂowchart illustrating the detail
of the proposed robust expansion model with long-
term uncertainty representation. According to block
(A), the constraints (8–11) are checked for each
particle. Then, the infeasible particles are penalized
as in block (B) while the wind short-term uncertainty
is studied for feasible solutions only as in block (C).
For each feasible particle in the population, by using
the MCS, the wind speed is randomly generated
based on it is a Weibull PDF. Then, the output power
for each wind site is calculated based on the power
curve for each site. For each wind power scenario,
the reserve, fuel mix ratio and reliability constraints
are checked. If any constraint is violated, additional
capacities are added to cope with wind energy short-
term uncertainty effects.
The wind capacity credit from each wind site is
considered trough the wind long-term uncertainty
analysis. Then for each feasible solution, the wind
speed scenarios are generated based on PDF by MCS
technique to deal with wind short-term uncertainty.
The number of scenarios is 500 to model the
uncertainties.
The
wind
speed
scenarios
and
Neural Computing and Applications (2024) 36:7923–7952
7931
123

---

## Page 10
constraints checked are established for any stage
containing wind power penetration. But the con-
straints are only checked for stages that have no wind
power with a mean value of wind power scenarios of
previous stages. Moreover, the wind power for all
previous stages is taken into account at current stage
study as mean value of wind power scenarios. The
constraints are checked for each scenario, and FGT
and PHS units are used to adapt the scenarios vio-
lated constraints. The LOLP is used as a reliability
criterion which calculated by ELDC. As LOLP value
is proportional to reserve capacity over the planning
horizon, the GEP with uncertain analysis is studied at
different reserve margin. Then, the results of the
wind uncertainty analysis, total expansion planning
cost, and LOLP are compared.
(3)
Modiﬁed objective function with PFA
The PFA can be used to convert a constrained
problem into an unconstrained problem. As a result,
the objective function is modiﬁed to include propor-
tional penalty values for each violated constraint,
avoiding the infeasible solutions in later iterations.
Fig. 2 Flowchart for the
proposed HBA for solving the
GEP incorporating wind power
uncertainty
7932
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 11
The total costs are given as the objective function
with the PFA (TC):
TCi ¼ Obi þ x  ð
X
p1 þ
X
p2 þ p3 þ p4 þ p5Þ
h
i
ð43Þ
Figure 3 describes the evaluation of the expected total
costs with short-term uncertainty representation based on
scenarios of MCS. As shown, each scenario is checked for
the constraints and other generating units of PHS and/or
FGT can be added as referred in block (D), in some cases,
to meet the constraints. Then, the objective function of the
current scenario is calculated, which is saved and MCS is
reiterated. After convergence of MCS, the meaning of all
expected values of scenarios is evaluated. For each sce-
nario, the objective function is calculated after adding the
costs due to addition capacities. Then, the mean value of all
scenarios is considered as the objective function for this
particle.
5 5 Simulation results
5.1 Test system description
The test system consists of 15 existing generation units
(Oil, Liquid Natural Gas (LNG), coal and Nuclear) is
tabulated in Table 1. Five different new generation tech-
nologies are selected as candidate conventional units (Oil,
LNG, Coal, and Nuclear) as in Table 2. The forecasted
peak load is illustrated in Table 3, with initial peak load of
5000 MW, and other data of existing and candidate gen-
eration units are taken from [14, 23, and 61]. In this study,
the discount rate is taken 8.5%; LOLP criterion at each
stage is considered of 0.01. The lower and upper limits for
reserve margin are set at 20 and 50%, respectively. EENS
cost is assumed to be 0.05 $/kWh. The bounds of capacity
mixes by fuel types are 0% and 30% for oil-ﬁred power
plants, 0 and 40% for LNG-ﬁred, 20 and 60% for coal-
ﬁred, and 30 and 60% for nuclear, respectively. The
emission coefﬁcient for oil is 0.85, LNG is 0.5, and coal is
1.05 while the reduction in total emission is considered as
Fig. 3 Evaluation of the
expected total costs
incorporating wind power short-
term uncertainty
Neural Computing and Applications (2024) 36:7923–7952
7933
123

---

## Page 12
10% of base case [49, 50, and 62]. The cost of unserved
energy, or EENS, which is calculated by ELDC method, is
set at 0.05 $/kWh. The initial period is set as two years
while the economic and technical characteristics of the
additional units are listed in Table 2 as [35].
The candidate wind sites, in this study, are Zafranah,
and Shark El-ouinate wind farm sites. The ﬁrst site,
Zafaranh wind farm, is in the Suez Gulf which is approx-
imately 200 km southeast Cairo. While the second site,
Shark El-ouinate, is in depth southern Egyptian desert. The
operational data of wind turbines and their descriptive
statistics, which are considered in this study for the two
sites, are recorded in Table 4. Added to that, the time series
data of the wind speed for the year 2019 in hourly basis of
Zafranah, and Shark El-ouinate wind farm sites are taken
from [63]. As shown in Table 4, the mean wind speed
value of Zafaranh site is greater than its value for Shark El-
ouinate site. But the variance and standard deviation for
Zafaranh site are less than it values for Shark El-ouinate.
Thus, most values of the generated wind speed scenarios
based on PDF for Zafaranh site will be around the corre-
sponding mean and below its maximum speed other than
Shark El-ouinate site which reaches maximum speed val-
ues with a smaller number of scenarios. So, studying each
wind site with its characteristics is especially important for
the reliability, and security of the power system.
5.2 GEP results and discussion
HBA is used to solve the GEP problem as base case and
wind energy uncertainty analysis based on the considered
three policies planning horizon as follows:
Table 1 Technical and economic data of existing generating units
Name
No. of units
Unit capacity (MW)
FOR%
Operating cost ($/kWh)
Fixed O&M cost ($/kW-Mon)
Oil#1
1
200
7.0
0.024
2.25
Oil#2
1
200
6.8
0.027
2.25
Oil#3
1
150
6.0
0.030
2.13
LNG G/T #1
3
50
3.0
0.043
4.52
LNG C/C #1
1
400
10.0
0.038
1.63
LNG C/C #3
1
400
10.0
0.040
1.63
LNG C/C #4
1
450
11.0
0.035
2.00
Coal #1
2
250
15.0
0.023
6.65
Coal #2
1
500
9.0
0.019
2.81
Coal #3
1
500
8.5
0.015
2.81
Nuclear #1
1
1000
9.0
0.005
4.94
Nuclear #2
1
1000
8.8
0.005
4.63
Table 2 Technical and economic data of candidate plants
New units
Umax
Capacity (MW)
FOR %
Operating cost ($/kWh)
Fixed O&M cost ($/kW-Mon)
Capital cost ($/kW)
Lifetime (yrs)
Oil
5
200
7.0
0.021
2.20
812.5
25
LNG C/C
4
450
10.0
0.035
0.90
500.0
20
Coal (bit)
3
500
9.5
0.014
2.75
1062.5
25
Nuclear #1
3
1000
9.0
0.004
4.60
1625.0
25
Nuclear #2
3
700
7.0
0.003
5.50
1750.0
25
FGT
4
150
0.8
53.23*10–3
0.5725
71.474
25
PHS
3
200
5.0
0.227*10–3
0.4363
154.377
50
Table 3 Forecasted peak
demand in Gwatts
Stage
1
2
3
4
5
6
7
8
9
10
11
12
7
9
10
12
13
14
15
17
18
20
22
24
7934
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 13
•
Policy-1: short-term GEP problems with 6-year plan-
ning horizon
•
Policy-2:
long-term
GEP
problems
with
12-year
horizon
•
Policy-3:
long-term
GEP
problems
with
24-year
horizon
Two cases are considered in the ﬁrst two polices in this
paper. The ﬁrst case study is performed using the proposed
framework, and results are compared with different other
techniques in the literature. This case study is the base case
in which the original problem is solved without wind
energy penetration and emission reduction constraint.
Then, the second case study is implemented for solving the
GEP problem which includes wind energy uncertainty
analysis and emission reduction objective function. Added
to that, an extra scenario that aims at minimizing the total
GHG emission as an objective function:
min GHG Emission ¼
X
T
t¼1
X
N
j¼1
ðXt;jðjÞ  emj
 
!
ð41Þ
The long-term and short-term wind uncertainties are
studied with 500 MCS scenarios of wind speed based on
PDF of each wind site. Each planning horizon consists of
two years of stage, making them to be 3, 6, and 12 stages in
short- and long-term planning horizons. The number of
years between the reference date of cost calculations and
the ﬁrst year of study (t) are assumed to be 2 years.
5.3 Policy-1: simulation results for 3-stages case
study
5.3.1 GEP results as base case of 3-stages case study
For policy-1, as a base case study, the GEP model is
solved, without considering wind energy penetration and
emission reduction constraints, using different optimization
techniques. The competitive techniques of Particle Swarm
Optimization (PSO) [23], Crow Search Algorithm (CSA)
[64], Aquila Optimizer (AO) [65], Blad Eagle Search
(BES) [66], and the proposed HBA are carried out for
solving the GEP. For all techniques, the speciﬁed param-
eters are 200 of iteration number, 60 of population size and
30 simulation runs while the population size is taken 30 for
BES only since each individual per each iteration has two
times for function evaluations. Moreover, the penalty fac-
tor value (x), which is used to penalize the infeasible
solutions, is equal to 1015. PSO, CSA, AO, BES, and HBA
are executed and their optimal results, and the associated
statistical indices of each applied algorithm are recorded in
Table 5. This table displays the total number of each type
of power plant in the planning model for comparative
algorithms.
The obtained comparative results show that the pro-
posed HBA has achieved the best total costs compared to
the other applied algorithms, whereas the improvement of
the objective function is equal to 3.2, 1.1 and 0.081% in
costs over the CSA, AO, and BES, respectively. Also, the
proposed HBA provides the smallest standard error and
deviation of 2.27*107 and 1.25*107, respectively. More-
over, the best cost of PSO and HBA are the same and the
average cost of PSO is less than HBA, but HBA provides
the smallest worst total cost with 7.1736*109 $ where the
CSA, AO, BES and PSO achieve 7.3464*109, 7.3267*109,
7.1976*109 and 7.2265*109 $, respectively. In the context,
the HBA is more staple during transfer from run to another
one as shown in Fig. 4. Also, the LOLP values are shown
in Table 6 which indicates that the reliability criterion is
satisﬁed for each applied algorithm. Moreover, Fig. 5
describes the convergence curves of CSA, AO, BES, PSO
and the proposed HBA. It can be observed from Fig. 5 that
the HBA algorithm shows better convergence rates com-
pared to the others. As shown, it provides a higher con-
vergence
rate
in
ﬁnding
the
least
objective
in
approximately 140 iterations.
Table 4 Candidate wind turbine
characteristics
Site
Zafranah
Shark El-ouinat
Wind turbine type
Nordex N43
Nordex-N100
Rated power (Pr) (kw)
600
2500
Hub height (m)
55
100
Cut-in wind speed (m/s)
2.5
3
Cut-off wind speed (m/s)
25
25
Rated wind speed (m/s)
15
12.5
Mean (m/s)
7.1468
6.4966
Maximum (m/s)
15.897
13.508
Minimum (m/s)
1.8
0.077
Standard deviation / Variance (m/s)
1.8666 / 3.4844
/ 6.3198
Neural Computing and Applications (2024) 36:7923–7952
7935
123

---

## Page 14
5.3.2 GEP results considering wind energy uncertainty
3-stages case study
The previous base case for 3-stages GEP model is resolved
considering wind energy long-term and short-term uncer-
tainty analysis. While the emission reduction contraint is
taken into account based on emission value in the base
case. In this policy, a wind power plant source from two
different wind sites are added as two wind plants to the
Table 5 Total Number of newly candidate units at each stage for case 1 and the related Descriptive statistics
Algorithm
Candidate units
Descriptive statistics ($)
Oil
LNG
Coal
Nuclear
#1
Nuclear
#2
Best cost
*109
Average cost
*109
Worst cost
*109
Standard error
*107
Standard dev.
*108
CSA
6
5
4
3
0
6.7331
7.0613
7.3464
2.58
1.41
AO
3
8
3
3
0
6.5924
7.0511
7.3267
2.99
1.64
BES
1
9
3
3
0
6.5734
6.963
7.1976
2.53
1.38
PSO
1
8
3
3
0
6.5204
6.8125
7.2265
3.09
1.69
HBA
1
8
3
3
0
6.5204
6.856
7.1736
2.27
1.25
Fig. 4 Recorded total cost
characteristics of the
competitive algorithms for
policy 1
Table 6 Values of LOLP criterion for policy 1-A
Stages
CSA
AO
BES
PSO
HBA
1
0.009787
0.009787
0.009787
0.009787
0.009787
2
0.00879
0.007991
0.005251
0.005251
0.005251
3
0.005648
0.00374
0.003686
0.008899
0.008899
Fig. 5 Converging
characteristics of the
competitive algorithms for
policy 1
7936
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 15
candidate units in the base case. The total wind contribu-
tion level is up to 10–20% of the installed capacity as an
alternative candidate plant. Also, the emission reduction
coefﬁcient is taken as 10% reduction percent from the base
case over the planning horizons. The proposed HBA are
utilized while the penalty factor value (x) is equal to 1020.
Table 7 summarizes the optimal results obtained for 50 and
60% two reserve capacity margin cases considering the
wind speed scenarios by MCS via PDF for each feasible
particle, as shown in Fig. 6. After generating wind speed
scenarios based on its PDF, wind output power for each
wind site is estimated for Zafaranhand Shark El-Ouinate
site, respectively. Then, the reserve, fuel mix ratio, and
LOLP constraints are checked for each scenario, and the
total cost is calculated for scenarios which satisfy the
constraints. When the particle with wind power scenario
does not satisfy all constraints, the addition capacities of
FGT and/or PHS are added to cope with wind power short-
term uncertainty. Figure 7 shows the total costs for each
scenario as example that are combines the costs of existing,
candidate and addition units.
For scenarios which violate the constraints, the FGT
and/or PHS are added until the constraints are satisﬁed and
the economic effect is added to total costs of scenario. The
total cost of the scenario is saved, and MCS is reiterated
until the scenario’s number is ended. The proposed HBA is
applied for the two different speciﬁed levels of the reserve
margin and the number of newly candidate technology
type, FGT and PHS number units at each planning stage are
tabulated in Table 7 at different reserve margin. The PDF
and CDF of LOLP values of each scenario before and after
adding the FGT and/or PHS units are shown in Fig. 8 as
related to 50% reserve capacity and in Fig. 9 as related to
60% reserve capacity.
The PDF and CDF of LOLP values at each stage
demonstrate the positive impacts of the FGT and/or PHS
additional units on the reliability system target. At stage 1,
as shown in Fig. 8A, the number of scenarios which satisfy
the LOLP constraint is less than 40% of the total scenarios
before adding FGT and/or PHS units. At the same stage,
100% of the scenarios satisfy the LOLP constraint after
adding FGT and/or PHS units. On the other side, at stage 2,
the values of LOLP criteria are achieved without any
addition of FGT and/or PHS units as shown in Fig. 8B.
Moreover, at wind penetration level constraints over the
planning horizon, which mean wind power from previous
stages are considered, no constraints are satisﬁed for all
scenarios at the stage 3 without adding any capacity as
shown in Fig. 8C. Because of the reliability criteria is
affected by reserve capacity, the GEP with wind uncer-
tainty analysis is solved at 60% maximum threshold of the
reserve margin. As shown in Fig. 9A, all wind power
scenarios achieve all the constraints without adding FGT
Table 7 Number of newly candidate units for 50%and 60% reserve Margin
Stages
Number of units at 50% Reserve
Number of units at 60% Reserve
Oil
LNG
Coal
Nuclear #1
Nuclear #2
Wind (Zaf)
Wind (Shark)
FGT
PHS
Oil
LNG
Coal
Nuclear #1
Nuclear #2
Wind (Zaf)
Wind (Shark)
FGT
PHS
1
2
1
3
2
0
0
1
1
1
2
2
2
2
1
0
1
0
0
2
2
1
0
1
1
1
0
0
0
0
0
0
1
0
0
1
2
3
3
0
0
0
0
0
0
1
1
2
0
0
1
0
0
1
0
2
1
Total
4
2
3
3
1
1
2
2
3
2
2
3
3
1
1
2
4
4
Neural Computing and Applications (2024) 36:7923–7952
7937
123

---

## Page 16
and/or PHS units at stage 1. On contrary, adding capacities
FGT and/or PHS units are required for stage 2 in order to
achieve the reliability criteria where at increased wind
penetration level as shown in Fig. 9B. Increasing the nec-
essary reserve margin results in violating the LOLP con-
straint for many scenarios. Therfore, installing more units
of FGT and/or PHS is required as illustrated in Fig. 9C at
stage 3. Thus, the total cost of expansion planning is
increased considering 60% reserve margin, which is
8.205*109 $, which is higher than the case of 50% reserve
margin, which is 8.183*109 $.
5.4 Policy-2: Simulation results for 6 stages case
study
5.4.1 GEP results as base case of 6 stages case study
In this policy, a long-term planning horizon of 12-year (6
stages) is managed. In the ﬁrst case, wind penetration and
emission reduction constraint are not included where the
CSA, AO, BES, PSO, and the proposed HBA are
employed. Their optimal results in terms of the total
number of new conventional candidate generation units for
each stage of the planning horizon and the accompanied
statistical indices are recorded in Table 8.
From Table 8, it is found that the proposed HBA pro-
vides the minimum total costs and better performance than
other algorithms. The proposed HBA has achieved a 2.5,
4.5, 2.5, and 5.16% enhancement in costs over CSA, AO,
BES, and PSO, respectively. It should be noted that the
performance of PSO algorithms is affected by the planning
horizon than the others.
The proposed HBA derives the best performance over
the other competitive algorithms since it achieves the least
total costs of their best, average, worst, standard error, and
standard
deviation
of
1.2996*1010,
1.3675*1010,
1.4211*1010, 4.43*107 and 2.43*108, respectively. More-
over, the recorded costs of the comparative algorithms
indicate
that
the
proposed
HBA
has
smallest
and
stable values of the worst, average, and best of total costs
over all runs as shown in Fig. 10. Also, the proposed HBA
shows the best convergence rate compared to the others in
ﬁnding the least objective target as displayed in Fig. 11.
5.4.2 GEP results considering wind energy uncertainty
via 6 stages case study
In this case, the proposed HBA is utilized for solving the
GEP problem at 50% and 60% reserve margin. The optimal
results of the number of newly candidate technology type,
Fig. 6 Example 500 scenarios
of wind output power of each
wind site
Fig. 7 Expected costs of the
generated scenarios of wind
power in Fig. 5
7938
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 17
Fig. 8 PDF and CDF of LOLP
values before and after adding
FGT and/or PHS units at 50%
reserve capacity
Neural Computing and Applications (2024) 36:7923–7952
7939
123

---

## Page 18
Fig. 9 PDF and CDF of LOLP
values before and after adding
FGT and/or PHS units at 60%
reserve capacity
7940
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 19
FGT and PHS number units at each planning stage are
recorded in as shown in Table 9. As shown, the wind
power is penetrated at 1, 2 and 6 stages for GEP model at
50% or 60% reserve margin.
In addition to that, the LOLP values are represented as
PDF and CDF before and after adding capacities of FGT
and/or PHS for stages 1, and 2 as shown in Fig. 12. As
shown, the number of scenarios which satisfy the LOLP
constraint is less than 40% of the total scenarios before
adding FGT and/or PHS units. At the same stage, 100% of
the scenarios satisfy the LOLP constraint after adding FGT
and/or PHS units. At stage 2, the values of LOLP criteria
Table 8 Total number of newly candidate units in each stage for the base case of policy 2 and the associated Statistical
Algorithm
Candidate units
Statistical results
Oil
LNG
Coal
Nuclear
#1
Nuclear
#2
Best cost
*1010 $
Average cost
*1010 $
Worst cost
*1010 $
Standard error
*107 $
Standard dev.
*108 $
CSA
8
11
6
4
0
1.3327
1.4306
1.445
6.42
3.51
AO
13
9
7
4
0
1.362
1.4473
1.5319
6.87
3.76
BES
14
10
5
4
0
1.3335
1.3982
1.4477
5.57
3.05
PSO
11
12
5
4
0
1.3702
1.4179
1.5179
6.32
3.46
HBA
5
13
6
4
0
1.2996
1.3675
1.4211
4.43
2.43
Fig. 10 Recorded total cost
characteristic of the competitive
algorithms for policy 2
Fig. 11 Converging
characteristics of the
competitive algorithms for
policy 2
Neural Computing and Applications (2024) 36:7923–7952
7941
123

---

## Page 20
are improved as well. At stage 3, there is no wind power
penetration whereas the LOLP criterion is preserved at the
mean value of wind power scenarios of the previous stages
and additional units. At stage 4, no new wind power is
installed. Despite the LOLP constraint is violated in this
stage with 0.02 value, it is maintained to 0.005 after con-
sidering the previous additional units. Moreover, at stages
5, and 6, the wind power is added and checked the con-
straints with previous additional units; the LOLP criterion
is guaranteed within the prescribed limit. Considering the
constraint of the reserve margin at 60%, total planning
costs and reliability criteria are affected which depend on
the timing of wind power deployed.
The results of expansion planning at 60% reserve mar-
gin indicate that the wind power plants are deployed in
later planning stages of 3, 4, 5 and 6, as shown in Table 9
where the LOLP values at stage 3 are displayed in Fig. 13.
The constraints, especially reliability constraint, are not
affected by wind power deployed in later stages and LOLP
criterion is preserved inside the permissible limit and less
than 0.01 without any additional capacities due to increase
spinning reserve and wind power penetrated in the last
stages. Even though no additional units are added, the total
expansion planning costs at 50% reserve margin is less
than it at 60% reserve margin which are 1.6017*1010, and
1.6665*1010, respectively.
5.4.3 Policy- 3:Simulation results for 12 stages case study
GEP results as base case of 12 stages case study
In this policy, a long-term planning horizon 24-year (12
stages) is conducted. CSA, AO, BES, PSO, and the pro-
posed HBA are employed for solving reliability constraint
GEP for this policy. Table 14 shows the total number of
new candidate generation units for each stage. Also, their
achieved result in terms of the statistical indices of each
applied algorithm is recorded in Table 10.
As shown, the proposed HBA has the best performance
compared to the others with percentage reductions of 4.2,
2.72, 2.7, and 3.4% over CSA, AO, BES and PSO,
respectively. Thus, the HBA achieves the optimum relia-
bility constrained GEP with the minimum total cost. It
achieves the least total costs of their best, average, worst,
standard error, and standard deviation of 2.3706*1010,
2.4953*1010,
2.6569*1010,
1.33*108
and
7.31*108,
respectively. The total cost results of each run of the
comparative algorithms are drawn as displayed in Fig. 14
which indicates that the proposed HBA has the least sta-
tistical results compared to others. Also, the proposed HBA
shows the best convergence rate compared to the others in
ﬁnding the least objective target as displayed in Fig. 15.
These ﬁgures show the fast response rate of the proposed
HBA in reaching the most economical solutions.
Table 9 Number of newly candidate units at 50% (60%) reserve margin for policy 2-b
Stages
Candidate units at 50% reserve margin
Candidate units at (60%) reserve margin
Oil
LNG
Coal
Nuclear #1
Nuclear #2
Wind (Zaf)
Wind (Shark)
FGT
PHS
Oil
LNG
Coal
Nuclear #1
Nuclear #2
Wind (Zaf)
Wind (Shark)
FGT
PHS
1
4
1
2
2
0
0
1
2
1
4
3
2
2
0
0
0
0
0
2
1
1
2
0
0
1
0
0
2
1
1
2
1
0
0
0
0
0
3
1
0
1
1
1
0
0
0
0
0
0
0
1
1
1
0
0
0
4
0
1
0
1
0
0
0
0
0
1
1
0
1
0
0
1
0
0
5
3
0
1
1
1
1
0
0
0
1
0
1
0
1
1
0
0
0
6
0
2
0
0
0
0
1
0
0
0
1
0
0
0
0
1
0
0
Total
9
5
6
5
2
2
2
2
3
7
6
6
5
2
2
2
0
0
7942
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 21
Fig. 12 PDF and CDF of LOLP
values before and after adding
capacity at 50% reserve
capacity
Fig. 13 PDF and CDF of LOLP
values before and after adding
capacity at 60% reserve
capacity
Neural Computing and Applications (2024) 36:7923–7952
7943
123

---

## Page 22
Table 10 Total Number of newly candidate units in each stage for the base case of policy- 3-a
Stages
Oil
LNG
Coal
Nuclear
#1
Nuclear
#2
Best cost
*1010 $
Average cost
*1010 $
Worst cost
*1010 $
Standard error
*108 $
Standard dev.
*108 $
CSA
21
19
12
9
3
2.4753
2.6369
2.8054
1.48
8.13
AO
18
17
18
9
0
2.4369
2.595
2.8125
1.86
10.2
BES
21
12
12
8
4
2.4366
2.5521
2.7434
1.34
7.35
PSO
16
20
14
9
3
2.4541
2.5687
2.7193
1.34
7.35
HBA
10
19
10
8
4
2.3706
2.4953
2.6569
1.33
7.31
Fig. 14 Recorded costs
characteristics of the
competitive algorithms for
policy 3
Fig. 15 Converging rates of the
competitive algorithms for
policy 3
7944
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 23
Table 11 Total Number of newly candidate units at 50% (60%) reserve margin for policy 3-b
Stages
Candidate units at 50% reserve margin
Candidate units at 60% reserve margin
Oil
LNG
Coal
Nuclear #1
Nuclear #2
Wind (Zaf)
Wind (Shark)
FGT
PHS
Oil
LNG
Coal
Nuclear #1
Nuclear #2
Wind (Zaf)
Wind (Shark)
FGT
PHS
1
0
0
3
3
0
0
1
1
1
0
0
3
3
0
0
1
1
1
2
0
1
2
0
0
0
1
3
2
1
1
0
1
1
1
0
0
0
3
2
1
0
0
0
1
0
0
0
2
0
1
0
0
0
1
0
0
4
0
2
2
1
0
0
1
0
0
1
2
1
2
0
0
1
0
0
5
0
0
1
1
0
0
0
0
0
2
0
0
0
0
1
0
0
0
6
0
0
0
0
2
1
0
0
0
1
0
3
0
0
1
0
0
0
7
0
0
0
1
0
1
0
0
0
1
0
0
1
0
0)
1
0
0
8
1
1
2
0
0
0
1
0
0
2
0
0
0
2
1
0
0
0
9
0
0
0
0
0
1
0
1
0
0
1
0
0
1
0
0
0
0
10
1
0
1
2
0
0
1
0
0
2
0
0
0
0
0
1
4
3
11
1
1
0
2
1
0
0
0
0
1
1
2
0
0
0
0
0
0
12
0
1
0
1
1
0
0
0
0
0
1
1
1
0
0
1
4
3
Total
10
7
11
11
4
4
5
5
3
13
5
11
8
4
4
6
9
7
Neural Computing and Applications (2024) 36:7923–7952
7945
123

---

## Page 24
Fig. 16 PDF and CDF of LOLP
values before and after adding
capacity at 50% reserve
capacity for policy 3-b
7946
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 25
5.4.4 GEP results considering wind energy uncertainty
for 12 stages case study
In this case of policy 3, for 12 stages (24 year planning
horizon), the proposed HBA is utilized for solving the GEP
problem at 50% and 60% reserve margin. The optimal
results of the total number of newly candidate technology
type are tabulated in Table 11. Also, FGT and PHS number
units at each planning stage are recorded in the two col-
umns Table 11, at different reserve margins. However, the
PDF and CDF of LOLP values for this policy at 50%
reserve margin for stages 1, 2, 6 and 9 are shown in
Fig. 16. For stage 1, less than 40% of the scenarios are
achieved all constraints before adding any units. On the
other side, the LOLP values are achieved for all scenarios
after adding one unit of FGT and one of PHS as shown in
Fig. 16A. The number of addition units for stage 2 is more
than respect to stage 1 because of the number of scenarios
in stage 2, which achieved the constraints, is less than 10%
of total scenarios as shown in Fig. 16B. In stages 3, 4, 5,
6,7, and 8, LOLP target is satisﬁed within the prescribed
limit without any addition units which LOLP value is less
than 0.01 as shown in Fig. 16C. Also, the LOLP constraint
at stage 9 requires addting a nother FGT unit to achieve the
target value. As shown in Fig. 16D, the required addition
capacity is 150 MW of FGT because of 10% of the sce-
narios is infeasible of LOLP constraint. Considering the
constraint of the reserve margin at 60%, the results of
expansion planning is recorded in Table 11 where the
LOLP values at stages a, 10 and 12 are displayed in
Fig. 17. From Fig. 17A, less than 40% scenarios have
LOLP value greater than the limit before adding one unit of
FGT and one of PHS to correct this situation. More addi-
tional units are required at stage 10 to increase the LOLP
value as shown in PDF and CDF in Fig. 17B. At stage 11,
although no wind plant is deployed, the LOLP values are
checked at the mean value of wind power scenarios, which
penetrated in the previous stages, and has 0.089 value.
Therefore, the LOLP target is achieved when checked with
previous adding units at stage 11 while four FGT and three
PHS units are required to adjust the LOLP value at stage
12.
5.4.5 GEP Emission reduction strategy results considering
wind energy uncertainty
The applications are extended to apply the proposed pro-
cedure on two test systems. Each system has two scenarios
the ﬁrst is based on the cost minimization while the second
is based on the minimization of the emission. An assess-
ment of the four scenarios is added. In addition to the
previous four scenarios, the cost based scenario is imple-
mented for large-scale test system. Tables 12 and 13
summarize the comparative 3-stages GEP model results
obtained of two cases of objective functions at 60% reserve
capacity margin for two cases that aimed at minimizing the
total costs and minimizing the GHG emission in Cases 1
and 2, respectively. Similarly, Tables 14 and 15 summarize
the comparative 6 stages GEP model results obtained of
two cases of objective functions at 60% reserve capacity
margin.
Fig. 16 continued
Neural Computing and Applications (2024) 36:7923–7952
7947
123

---

## Page 26
Fig. 17 PDF and CDF of LOLP
values before and after adding
capacity at 60% reserve
capacity for policy 3-b
7948
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 27
6 Conclusion
Reliability constrained GEP problem is a highly complex,
nonlinear, multiple constraints and dynamic problem.
Firstly, the GEP problem is solved without wind energy
penetration and emission reduction constraint as the base
case. The proposed HBA algorithm is applied with GEP
model modiﬁcations to solve GEP problem and compared
with other algorithms in the base case. Thus, the perfor-
mance of the proposed HBA is better than other techniques.
Also, reliability indies such as EENS and LOLP are cal-
culated by ELDC as one of production simulation methods.
The base case results indicate that the proposed HBA has
effective and better performance than compared algo-
rithms. Moreover, the robust GEP model as the short and
long-term planning horizon is proposed in this paper and
solved as the base case. Then, it is presented considering
long and short-term wind uncertainties effect of the high
share of wind energy from two different wind sites. Wind
capacity credit from each wind site is considered during
long-term uncertainty analysis as the ﬁrst step. In the
second step, wind power uncertainty from each site is
modeled by wind speed scenarios based on its PDF and
included in the planning by using MCS. For each scenario,
all constraints are checked and addition capacities by FGT
and/ or PHS units are added to deal with wind short-term
uncertainty. The total costs are calculated in case of
infeasible particles after adding penalty factor, and it cal-
culated for feasible particles with wind scenarios after
addition economic effect of the required capacities. The
GEP models as reference case study and considering wind
long and short-term uncertainties are analyzed for 3, 6, and
12 stages as short and long planning horizons. Simulation
results indicated that considering wind long and short-term
uncertainties in the expansion planning leads to a robust
and ﬂexible planning and guarantees the safe operation of
system under uncertainty conditions. In the future work,
the correlation factor between wind uncertainty scenarios
and using other techniques for uncertainty analysis is
suggested in the search space of the GEP problem with
considering wind uncertainty. However, it is advised that
the system’s reliability be examined during the planning
and operating phases to maintain it at target value, partic-
ularly when wind energy is penetrated. Additionally,
Table 12 Comparative 3-stages
GEP model results
Objective function
Total cost *109 ($)
GHG emission*103 (Ton. CO2)
Case 1: total Cost minimization
8.21
5.4075
Case 2: GHG emission minimization
8.51
5.0525
Table 13 Number of newly
candidate units for 6 stages at
60% reserve Margin
Stages
Oil
LNG
Coal
Nuclear #1
Nuclear #2
Wind (Zaf)
Wind (Shark)
FGT
PHS
1
3
0
3
2
0
1
0
2
2
2
0
0
0
2
0
0
1
1
0
3
0
0
0
1
0
0
1
0
0
Total
3
0
3
5
0
1
2
3
2
Table 14 Comparative 6 stages
GEP model results
Objective function
Total cost *1010 ($)
GHG emission *103 (Ton. CO2)
Case 1: total Cost minimization
1.6665
8.4325
Case 2: GHG emission minimization
1.7603
7.8125
Table 15 Number of newly
candidate units for 6 stages at
60% reserve Margin
Stages
Oil
LNG
Coal
Nuclear #1
Nuclear #2
Wind (Zaf)
Wind (Shark)
FGT
PHS
1
3
3
2
2
0
0
1
0
0
2
0
0
2
2
0
0
1
0
0
3
0
0
0
0
1
0
0
0
0
4
0
1
1
0
2
1
0
0
0
5
0
0
0
1
0
0
1
0
0
6
3
0
1
0
0
1
0
0
0
Total
6
4
6
5
3
2
3
0
0
Neural Computing and Applications (2024) 36:7923–7952
7949
123

---

## Page 28
during the economic dispatch phase of the available gen-
erating units, the emission costs as an objective function
should be taken into consideration. Also, the network-
based GEP can be changed the problem complexity and
therefore needs deep machine learning algorithms to han-
dle the increased complexity.
Funding Open access funding provided by The Science, Technology
& Innovation Funding Authority (STDF) in cooperation with The
Egyptian Knowledge Bank (EKB).
Data availability Authors can conﬁrm that all relevant data are
included in the article.
Declarations
Conflict of interest Authors have no conflict of interest in this work.
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
1. Conejo AJ, Baringo L, Kazempour SJ, Siddiqui AS (2016)
Investment in electricity generation and transmission. Springer
International Publishing, Cham Zug, Switzerland
2. Shaheen AM, El-Sehiemy RA, Farrag SM (2016) A novel ade-
quate bi-level reactive power planning strategy. Int J Electr
Power Energy Syst 78:897–909. https://doi.org/10.1016/j.ijepes.
2015.12.004
3. ELKARMI F (ed. ). (2012) Power system planning technologies
and applications: concepts, solutions and management: concepts,
solutions and management. IGI Global
4. Elattar EE, Shaheen AM, Elsayed AM, El-Sehiemy RA (2020)
Optimal power ﬂow with emerged technologies of voltage source
converter stations in meshed power systems. IEEE Access.
https://doi.org/10.1109/access.2020.3022919
5. El-Ela AAA, Bishr M, Allam S, El-Sehiemy R (2005) Optimal
preventive control actions using multi-objective fuzzy linear
programming technique. Electr Power Syst Res 74:147–155.
https://doi.org/10.1016/j.epsr.2004.08.014
6. El-Sehiemy RA, El Ela AAA, Shaheen A (2015) A multi-ob-
jective fuzzy-based procedure for reactive power-based preven-
tive emergency strategy. Int J Eng Res Africa 13:91–102. https://
doi.org/10.4028/www.scientiﬁc.net/JERA.13.91
7. Babatunde BOM, Munda JL, Hamam Y (2019) A comprehensive
state-of-the-art survey on power generation expansion planning
with intermittent renewable energy source and energy storage. Int
J Energy Res 43(12):6078–6107. https://doi.org/10.1002/er.4388
8. Quan H, Khosravi A, Yang D (2019) A survey of computational
intelligence techniques for wind power uncertainty quantiﬁcation
in
smart
grids.
IEEE
Trans
Neural
Netw
Learn
Syst
31:4582–4599. https://doi.org/10.1109/TNNLS.2019.2956195
9. Jordehi AR (2018) How to deal with uncertainties in electric
power
systems?
A
review.
Renew
Sustain
Energy
Rev
96:145–155. https://doi.org/10.1016/j.rser.2018.07.056
10. MANSOURI, Seyed Amir; JAVADI MS, (2017) A robust opti-
misation framework in composite generation and transmission
expansion planning considering inherent uncertainties. J Exp
Theor Artif Intell 29:717–730. https://doi.org/10.1080/0952813X.
2016.1259262
11. Guo J, Fang Y, Kawamoto E, et al (2022) A review of hydrogen-
based hybrid renewable energy systems: Simulation and opti-
mization with artiﬁcial intelligence A review of hydrogen-based
hybrid renewable energy systems: Simulation and optimization
with artiﬁcial intelligence. https://doi.org/10.1088/1742-6596/
2208/1/012012
12. Ali ES, El-Sehiemy RA, Abou El-Ela AA (2021) Optimal par-
titioning of unbalanced active distribution systems for supply-
sufﬁcient micro-grids considering uncertainty. Int Transact Electr
Energy Syst 31(12):e13210. https://doi.org/10.1002/2050-7038.
13210
13. Akbarzade, Hossein and Amraee T (2018) A Model for Gener-
ation Expansion Planning in Power Systems Considering Emis-
sion Costs. In: 2018 Smart Grid Conf (SGC), IEEE 1–5. https://
doi.org/10.1109/SGC.2018.8777836
14. JADIDOLESLAM, Morteza; EBRAHIMI A, (2015) Reliability
constrained generation expansion planning by a modiﬁed shufﬂed
frog
leaping
algorithm.
Int
J
Electr
Power
Energy
Syst
64:743–751. https://doi.org/10.1016/j.ijepes.2014.07.073
15. Pereira S, Ferreira P, Vaz AIF (2016) Optimization modeling to
support renewables integration in power systems. Renew Sustain
Energy Rev 55:316–325. https://doi.org/10.1016/j.rser.2015.10.
116
16. Abou El-Ela AA, El-Sehiemy RA, Ali ES, Kinawy A-M (2019)
Minimisation of voltage ﬂuctuation resulted from renewable
energy sources uncertainty in distribution systems. IET Gener
Transm Distrib 13:2339–2351. https://doi.org/10.1049/iet-gtd.
2018.5136
17. Jadidoleslam M, Bijami E, Amiri N, Ebrahimi A (2012) Appli-
cation of shufﬂed frog leaping algorithm to long term generation
expansion planning. Int J Comput Electr Eng 4:115
18. Kannan S, Baskar S, McCalley JD, Murugan P (2008) Applica-
tion of NSGA-II algorithm to generation expansion planning.
IEEE Trans Power Syst 24:454–461
19. Rashidaee SA, Amraee T, Fotuhi-Firuzabad M (2018) A linear
model for dynamic generation expansion planning considering
loss of load probability. IEEE Trans Power Syst 33:6924–6934.
https://doi.org/10.1109/TPWRS.2018.2850822
20. Park H, Baldick R (2015) Stochastic generation capacity expan-
sion planning reducing greenhouse gas emissions. IEEE Trans
Power Syst 30:1026–1034
21. Bhuvanesh A, Christa J, Thomas S, Kannan S, Karuppasamy
Pandiyan M (2019) Multistage multiobjective electricity gener-
ation expansion planning for Tamil Nadu considering least cost
and minimal GHG emission. Int Trans Electr Energy Syst
29:e2708. https://doi.org/10.1002/etep.2708
22. Javadi MS, Esmaeel NA (2019) Multi-objective, multi-year
dynamic generation and transmission expansion planning-re-
newable energy sources integration for Iran’s national power
grid. Int Transact Electr Energy Syst 29(4):e2810. https://doi.org/
10.1002/etep.2810
23. Kannan S, Slochanal SM, Subbaraj P, Padhy NP (2004) Appli-
cation of particle swarm optimization technique and its variants
7950
Neural Computing and Applications (2024) 36:7923–7952
123

---

## Page 29
to generation expansion planning problem. Electr Power Syst Res
70(3):203–210. https://doi.org/10.1016/j.epsr.2003.12.009
24. Karunanithi K, Kannan S, Thangaraj C (2015) Generation
expansion planning for Tamil Nadu: a case study. Int Trans Electr
energy Syst 25:1771–1787. https://doi.org/10.1002/etep
25. Pereira AJ, Saraiva JT (2010) A decision support system for
generation expansion planning in competitive electricity markets.
Electr power Syst Res 80(778):787. https://doi.org/10.1016/j.
epsr.2009.12.003
26. Hemmati R, Hooshmand R-A, Khodabakhshian A (2013) Relia-
bility constrained generation expansion planning with consider-
ation of wind farms uncertainties in deregulated electricity
market. Energy Convers Manag 76:517–526. https://doi.org/10.
1016/j.enconman.2013.08.002
27. Hemmati R, Hooshmand R, Khodabakhshian A (2016) Coordi-
nated generation and transmission expansion planning in dereg-
ulated electricity market considering wind farms. Renew Energy
85:620–630. https://doi.org/10.1016/j.renene.2015.07.019
28. SAXENA, Kritika; BHAKAR, Rohit; JAIN P (2018) Coordinated
GEP and TEP Approach with Correlated Generation and Load.
In: 2018 3rd Int Conf Work Recent Adv Innov Eng 1–6
29. Hemmati R, Hooshmand R, Khodabakhshian A (2014) Market
based transmission expansion and reactive power planning with
consideration of wind and load uncertainties. Renew Sustain
Energy Rev 29:1–10. https://doi.org/10.1016/j.rser.2013.08.062
30. Alaee S, Hooshmand RA, Hemmati R (2016) Stochastic trans-
mission expansion planning incorporating reliability solved using
SFLA meta-heuristic optimization technique. CSEE J Power
Energy Syst 2(2):79–86. https://doi.org/10.17775/CSEEJPES.
2016.00025
31. Hochreiter S (1997) Long short-term memory. Neural Comput
9:1735–1780
32. Skrobek D, Krzywanski J, Sosnowski M, Kulakowska A, Zylka
A, Grabowska K, Ciesielska K, Nowak W (2022) Implementation
of deep learning methods in prediction of adsorption processes.
Adv Eng Softw 173:103190. https://doi.org/10.1016/j.advengsoft.
2022.103190
33. ABDALLA, Omar H.; ADMA, Maged A. Abu; AHMED AS
(2019) Generation Expansion Planning Considering High Share
Renewable Energies Uncertainty. In: 2019 21st Int Middle East
Power Syst Conf (MEPCON) IEEE 1–7
34. Abdalla OH, Adma MAA, Ahmed AS (2020) Generation
expansion planning under correlated uncertainty of mass pene-
tration renewable energy sources. IET ENERGY Syst Integr
2:273–281. https://doi.org/10.1049/iet-esi.2020.0008
35. Abdalla OH, Smieee L, Adma MAA, Ahmed AS (2020) Two-
stage robust generation expansion planning considering long- and
short-term uncertainties of high share wind energy. Electr Power
Syst Res 189:106618. https://doi.org/10.1016/j.epsr.2020.106618
36. Kumar PP, Nuvvula RSS, Hossain A, Shezan SKA (2022)
Optimal operation of an integrated hybrid renewable energy
system with demand-side management in a rural context. Ener-
gies 15:5176
37. Hossen MD, Islam MF, Ishraque MF, Shezan SA, Arifuzzaman
SM (2022) Design and implementation of a hybrid solar-wind-
biomass renewable energy system considering meteorological
conditions with the power system performances. Int J Photoen-
ergy 2:2022
38. Shezan SA, Ishraque F, Muyeen SM et al (2022) Selection of the
best dispatch strategy considering techno-economic and system
stability analysis with optimal sizing. Energy Strateg Rev
43:100923. https://doi.org/10.1016/j.esr.2022.100923
39. Shezan SA, Ishraque F, Muyeen SM et al (2022) Effective dis-
patch strategies assortment according to the effect of the opera-
tion for an islanded hybrid microgrid. Energy Convers Manag X
14:100192. https://doi.org/10.1016/j.ecmx.2022.100192
40. Shezan SA, Ishraque MF, Paul LC, Sarkar MR, Rana MM, Uddin
M, Hossain MB, Shobug MA, Hossain MI (2022) Assortment of
dispatch strategies with the optimization of an islanded hybrid
microgrid. MIST Int J Sci Technol 26(10):15–24
41. Farh HMH, Al-shamma AA, Al-shaalan AM, Alkuhayli A (2022)
Technical and economic evaluation for off-grid hybrid renewable
energy system using novel bonobo optimizer. Sustainability
14:1533
42. Xifan, Wang and McDonald JR (1994) Modern power system
planning. 208–229
43. Choi J, Lee KY (2021) Probabilistic power system expansion
planning with renewable energy resources and energy storage
systems. Wiley
44. RASHIDAEE, Seyyed Ali; AMRAEE T (2018) Generation
Expansion Planning Considering the Uncertainty of Yearly Peak
Important Deadlines for Technical Papers. In: Eng 2018 IEEE Ind
Commer Power Syst Eur (EEEIC/I&CPS Eur IEEE 1–4. https://
doi.org/10.1109/EEEIC.2018.8493688
45. Barati F, Jadid S, Zangeneh A (2019) Private investor-based
distributed generation expansion planning considering uncer-
tainties of renewable generations. Energy 15(173):1078–1091.
https://doi.org/10.1016/j.energy.2019.02.086
46. Pereira S, Ferreira P, Vaz AIF (2017) Generation expansion
planning with high share of renewables of variable output. Appl
Energy 190:1275–1288. https://doi.org/10.1016/j.apenergy.2017.
01.025
47. Abdalla OH, Abu Adma MA, Ahmed AS (2021) Generation
expansion planning considering unit commitment constraints and
data-driven robust optimization under uncertainties. Int Transact
Electr Energy Syst 31(6):e12878. https://doi.org/10.1002/2050-
7038.12878
48. Muppidi R, Nuvvula RS, Muyeen SM, Shezan SA, Ishraque MF
(2022) Optimization of a fuel cost and enrichment of line load-
ability for a transmission system by using rapid voltage stability
index
and
grey
wolf
algorithm
technique.
Sustainability
14(7):4347. https://doi.org/10.3390/SU14074347
49. Nawaz U (2020) Least-cost generation expansion planning using
whale optimization algorithm incorporating emission reduction
and renewable energy sources. Int Trans Electr Energy Syst
30:e12238. https://doi.org/10.1002/2050-7038.12238
50. Rajesh K, Kannan S, Thangaraj C (2016) Least cost generation
expansion planning with wind power plant incorporating emis-
sion using differential evolution algorithm. Int J Electr power
energy Syst 80:275–286. https://doi.org/10.1016/j.ijepes.2016.01.
047
51. Rajesh K, Bhuvanesh A, Kannan S, Thangaraj C (2016) Least
cost generation expansion planning with solar power plant using
differential evolution algorithm. Renew Energy 85:677–686.
https://doi.org/10.1016/j.renene.2015.07.026
52. Rajesh K, Karthikeyan K, Kannan S, Thangaraj C (2016) Gen-
eration expansion planning based on solar plants with storage.
Renew Sustain Energy Rev 57:953–964. https://doi.org/10.1016/
j.rser.2015.12.126
53. Booma J, Mahadevan K, Kannan S (2015) Minimum cost esti-
mation of generation expansion planning incorporating wind
power plant. ARPN J Eng Appl Sci 10:2956–2961
54. SEIFI, Hossein; SEPASIAN MS, (2011) Electric power system
planning: issues, algorithms and solutions. Springer, Berlin
55. Billington, Roy and Allan RN (1994) Reliability Evaluation of
Power Systems
56. Shaheen AM, Elattar EE, El RA et al (2020) An improved sun-
ﬂower optimization algorithm based-Monte Carlo simulation for
efﬁciency improvement of radial distribution systems considering
wind power uncertainty. IEEE Access 9:2332–2344. https://doi.
org/10.1109/ACCESS.2020.3047671
Neural Computing and Applications (2024) 36:7923–7952
7951
123

---

## Page 30
57. El-Ela A, Abou El-Ela AA, El-Sehiemy RA et al (2022)
Renewable Energy micro-grid interfacing: economic and envi-
ronmental
issues.
Electronics.
https://doi.org/10.3390/
electronics11050815
58. Shaheen AM, Ginidi AR, El-Sehiemy RA, Elattar EE (2021)
Optimal economic power and heat dispatch in cogeneration
Systems including wind power. Energy 225:120263. https://doi.
org/10.1016/j.energy.2021.120263
59. Akdag˘ SAGO¨ (2011) A comparison of wind turbine power curve
models. Energy Sources, Part A Recover Util Environ Eff
33:2257–2263. https://doi.org/10.1080/15567036.2011.594861
60. Hashim FA, Houssein EH, Hussain K, Mabrouk MS, Al-Atabany
W (2022) Honey badger algorithm: new metaheuristic algorithm
for
solving
optimization
problems.
Math
Comput
Simul
192:84–110. https://doi.org/10.1016/j.matcom.2021.08.013
61. Nawaz U, Malik TN, Ashraf MM (2020) Least-cost generation
expansion planning using whale optimization algorithm incor-
porating emission reduction and renewable energy sources. Int
Transact Electr Energy Syst 30(3):e12238. https://doi.org/10.
1002/2050-7038.12238
62. Rajesh K, Bhuvanesh A, Kannan S, Thangaraj C (2022) Least
cost generation expansion planning with solar power plant using
differential evolution algorithm. Renew Energy 85:677–686.
https://doi.org/10.1016/j.renene.2015.07.026
63. Askarzadeh A (2016) A novel metaheuristic method for solving
constrained engineering optimization problems: crow search
algorithm. Comput Struct. https://doi.org/10.1016/j.compstruc.
2016.03.001
64. Abualigah L, Yousri D, Abd Elaziz M, Ewees AA, Al-Qaness
MA, Gandomi AH (2021) Aquila optimizer: a novel meta-
heuristic
optimization
algorithm.
Comput
Ind
Eng
1(157):107250. https://doi.org/10.1016/j.cie.2021.107250
65. Alsattar HA, Zaidan AA, Zaidan BB (2020) Novel meta-heuristic
bald eagle search optimisation algorithm. Artif Intell Rev. https://
doi.org/10.1007/s10462-019-09732-5
66. Abou El-Ela AA, El-Sehiemy RA, Shaheen AM, Shalaby AS
(2023) Assessment of Wind Energy based on Optimal Weibull
Parameters Estimation using Bald Eagle Search Algorithm: Case
Studies from Egypt. J Electr Eng Technol 18:4061–4078. https://
doi.org/10.1007/s42835-023-01492-1
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
7952
Neural Computing and Applications (2024) 36:7923–7952
123

---
