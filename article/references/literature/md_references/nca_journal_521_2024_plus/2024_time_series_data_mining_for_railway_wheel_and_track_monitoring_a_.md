# Time series data mining for railway wheel and track monitoring: a survey

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-10138-w

---

## Page 1
REVIEW
Time series data mining for railway wheel and track monitoring:
a survey
Afonso Lourenço1
• Diogo Ribeiro2 • Marta Fernandes1 • Goreti Marreiros1
Received: 19 October 2023 / Accepted: 27 June 2024 / Published online: 24 July 2024
 The Author(s) 2024
Abstract
The railway sector has witnessed a signiﬁcant surge in condition-based maintenance, thanks to the proliferation of sensing
technologies and data-driven methodologies, such as machine learning. However, despite the plethora of algorithms
designed to detect and classify track irregularities and wheel out-of-roundness, they often fall short when put to the test in
real-world scenarios. These shortcomings typically stem from their inability to meet all four critical requirements for
constructing an effective maintenance plan: (R1) suitability of the condition-based maintenance strategy, (R2) availability
of relevant data, (R3) proper problem formulation, and (R4) accurate evaluation of data mining methods. In response to the
absence of a uniﬁed framework and standardized guidelines, this survey delves into the realm of time series sensor data and
wheel-track interface components for railway structural health monitoring. This survey aims to bridge this gap by offering
an extensive categorization, pinpointing existing challenges, and outlining potential directions for future research. Through
these efforts, this survey provides a more thorough and targeted exploration of the subject matter, contributing to the
advancement of this ﬁeld.
Keywords Condition-based maintenance  Artiﬁcial intelligence  Railway infrastructure  Sensing technologies 
Time series analysis
1 Introduction
The railway sector relies on reliability and maintainability
to ensure the smooth and secure transportation of passen-
gers and freight [1]. With trains designed to operate for
decades and maintenance costs accounting for a signiﬁcant
portion of the total expenditure, there is an urgent need to
keep safety and quality of service at an optimal level while
minimizing the operational costs. In fact, with high trafﬁc
levels, massive axle loads, and constantly changing con-
ditions, even minor ﬂaws in the railway track can be
transformed into signiﬁcant problems. In particular, the
wheel-track interface has received a lot of attention in the
literature, as it incurs most of the cost of maintenance for
both railway vehicles and infrastructure [2]. Examples of
such components include wheels, rails, sleepers, fastenings,
and ballast, among others. These components are exposed
to various environmental and operational conditions, which
can induce corrosion, cracks, and other types of damage. In
addition, surfaces of the wheel-track are subjected to high
stick, sliding, and contact stresses in rolling contact, with
the increasing hazard function being a common pattern
observed in the failure rates of these mechanical compo-
nents [3, 4]. To address this increasing probability of
failure over time, it is imperative to perform maintenance
actions proactively.
By implementing a preventive maintenance strategy,
railway operators can reduce the likelihood of downtime,
increase equipment lifespan, and avoid costly emergency
& Afonso Lourenc¸o
fonso@isep.ipp.pt
Diogo Ribeiro
drr@isep.ipp.pt
Marta Fernandes
mmdaf@isep.ipp.pt
Goreti Marreiros
mgt@isep.ipp.pt
1
GECAD, School of Engineering, Polytechnic of Porto, Porto,
Portugal
2
CONSTRUCT-LESE, School of Engineering, Polytechnic of
Porto, Porto, Portugal
123
Neural Computing and Applications (2024) 36:16707–16725
https://doi.org/10.1007/s00521-024-10138-w
(0123456789().,-volV)(0123456789().,-volV)

---

## Page 2
repairs. The railway industry often uses a periodic
replacement scheme based either on tonnage or kilometers
traveled for vehicles and accumulated load or passing
trafﬁc for tracks [5]. Furthermore, these maintenance
interventions are intuitively affected by expert knowledge
on the effect of structural parameters on degradation rate.
For example, change in rail proﬁles, closeness to switches
and direct fastening systems increase the rate of degrada-
tion. In addition, the railway industry tends to have a
comprehensive maintenance plan, by proactively lubricat-
ing, refurbishing, calibrating, tamping, and drive-by visual
inspecting equipment on a regularly scheduled basis.
However, these plans tend to be too conservative to com-
pensate for the fact that they fail to tackle the speciﬁc root
cause, which not only results in very high maintenance
costs but can also reduce the component lifespan. For
instance, it has been proven that despite tamping improves
the condition of the track geometry, excessive ballast set-
tlement can degrade the structural parameters of railway
systems [6]. Ideally, the maintenance action should be
performed just before the component failure. To tackle this
challenge, the railway industry has witnessed the emer-
gence of low-cost and easily maintainable condition mon-
itoring systems, enabled by digital automation systems, Big
Data, and Industrial Internet of Things (IoT) technologies.
Both onboard and wayside condition monitoring are
increasingly embraced with analysis tools to evaluate the
railway load [7], as illustrated in Fig. 1.
The condition of a system is quantiﬁed by periodically
or
continuously
collecting
information
from
sensors
mounted on its components, and actions are taken only
when evidence of abnormal behavior is detected. This trend
has given rise to an increasing use of artiﬁcial intelligence
in condition-based maintenance, with numerous publica-
tions on this approach [8]. However, implementing data
mining techniques for railway maintenance remains a
challenge due to the absence of a common framework and
standards [9]. For instance, many studies neglect to account
for the fact that deploying a greater number of sensors
inevitably leads to increased costs. These costs arise from
the need for additional equipment, maintenance, and data
processing infrastructure. Therefore, a condition-based
maintenance strategy is most advantageous for critical
components whose failure does not occur instantaneously
and can result in substantial function loss and safety risks.
To address these issues, the survey investigates the chal-
lenges and opportunities of employing artiﬁcial intelli-
gence for condition-based maintenance in railway systems,
with a particular emphasis on the wheel-track interface and
time series sensors. With this central research question in
mind, the following speciﬁc questions (SQs) were posed:
(SQ1) What are the most common types of sensors used
to collect time series data in railway systems, particularly
for the wheel-track interface?
(SQ2) What are the most used machine learning
algorithms for condition-based maintenance in railway
systems, and how do they compare in terms of accuracy
and computational efﬁciency?
(SQ3) What are the most effective preprocessing tech-
niques for time series data in the context of railway
maintenance, and how can they be optimized for
different types of sensors and maintenance tasks?
(SQ4) How are artiﬁcial intelligence-based maintenance
models adapted to account for streaming data and
automated maintenance decision-making?
(SQ5) How are computational expense, interpretability,
and cost considerations incorporated into artiﬁcial intel-
ligence-based maintenance models to improve trust and
adoption by maintenance staff and decision-makers?
(SQ6) What are the key opportunities and challenges in
scaling up the use of artiﬁcial intelligence for condition-
based maintenance in railway systems, and what strate-
gies can be employed to overcome these challenges?
These questions were addressed in the form of a com-
prehensive survey, which identiﬁed how the current
Fig. 1 Types of condition
monitoring for proactive
maintenance: onboard and
wayside
16708
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 3
literature complies with the key requirements (R) for cre-
ating an effective maintenance plan:
(R1)
Condition-based
maintenance
strategy
is
appropriate.
(R2) Available data.
(R3) Problem is appropriately formulated.
(R4) Data mining methods are evaluated correctly.
As for R1, the mechanical components in the wheel-
track interface present a gradual degradation process, e.g.,
wear and rolling contact fatigue, and a major threat to the
operational safety of a railway system, thus condition-
based maintenance is the right strategy [8]. Regarding R2,
the dynamic context of the railway system is exceptionally
challenging. Numerous measurement methods are used for
bogies and tracks, including 3D-laser cameras, ultrasonic
devices, eddy current, magnetic ﬂux leakage, manual
inspection, and others. As the data available impacts the
selection and success of data mining methods, this survey
focuses solely on time series, not only because it is the
most common format of sensor data [7], but also due to the
complexity of dealing with the sequential structure of data,
with order and temporal dependencies. The most prominent
problems arise from the high dimensionality and difﬁculty
in devising similarity measures that consider temporal
patterns, trends, periodicity, and other unique characteris-
tics of time series data. Regarding R3, it is necessary to
select effective preprocessing techniques to deal with the
temporal dimension, such as for data representation, simi-
larity measurement, and indexing. In addition, the model-
ing strategy can be posed as a fault diagnosis or prognosis
task. Finally, for R4 there are also signiﬁcant gaps in
evaluation standards, characterized by the absence of
proper
performance
metrics,
interpretability,
cost
incorporation, and considerations for streaming environ-
ments [9, 10]. Figure 2 illustrates these requirements.
Within this context, this literature review poses the
central question: What are the key challenges and oppor-
tunities in applying artiﬁcial intelligence to condition-
based maintenance of railway systems, particularly in the
context of the wheel-track interface, and how can they be
addressed? To consider relevant papers, the choice of
keywords for building the search strings was based on
terms commonly found in the literature:
(‘‘PdM’’ OR ‘‘CBM’’ OR ‘‘diagnosis’’ OR ‘‘progno-
sis’’ OR ‘‘condition monitoring’’ OR ‘‘RUL’’ OR
‘‘PHM’’) AND (‘‘railway’’ OR ‘‘rail’’ OR ‘‘track’’ OR
‘‘wheel-track’’) AND (‘‘data-driven’’ OR ‘‘big data’’
OR ‘‘AI’’ OR ‘‘ML’’ OR ‘‘DL’’ OR ‘‘statistical’’).
Note that this survey exclusively focused on primary
research papers published in English between 2010 and
2023. Papers that didn’t use measurement systems related
to time series or did not primarily focus on wheel and track
condition monitoring were excluded from consideration.
Following the stated search strategy, a total of 125 publi-
cations were thoroughly reviewed. Multiple databases were
assessed during the research process, including Science-
Direct, SAGE, IEEE Xplore, Taylor & Francis, MDPI, and
Springer. The survey is structured as illustrated in Fig. 3.
Section 2 provides a comprehensive overview of related
work, highlighting the main differences. Section 3 presents
the parts and type of defects for which condition-based
maintenance is an adequate strategy. Section 4 covers the
kind of data being used, namely the measurement methods,
typical characteristics of sensor data and support with
physical-based models. Section 5 provides a thorough
overview of the approaches developed to deal with time
series sensor data, with different goals, learning tasks,
Fig. 2 An effective maintenance plan requires the maintenance strategy to be appropriate, available data, problem to be appropriately
formulated, and data mining methods to be evaluated correctly
Neural Computing and Applications (2024) 36:16707–16725
16709
123

---

## Page 4
methods,
and
implementation
components.
Section 6
studies the most common evaluation procedures: perfor-
mance, interpretability, cost, and computational expense.
Finally,
Sect. 7
links
existing
literature
to
potential
research directions, and Sect. 8 concludes the survey.
2 Related work
In the context of prior research, early literature reviews
focused on discussing different types of sensors, mea-
surement objectives, and conditions. One notable contribu-
tion, in 2011, proposed a taxonomy that categorized
monitoring systems into infrastructure-based infrastructure
monitoring (I2I), infrastructure-based rolling stock moni-
toring (I2V), rolling stock-based infrastructure monitoring
(V2I), and rolling stock-based rolling stock monitoring
(V2V) [11]. Another comprehensive overview, in 2014,
examined the use of wireless sensors for monitoring
structures, vehicles, and machinery, shedding light on their
practical applications [12]. However, the most widely
adopted taxonomy formed the basis for a review conducted
in 2017, which further classiﬁed monitoring systems into
inspection and in-service categories, including onboard and
wayside measurement [7]. In terms of wayside detection,
monitoring systems were extensively reviewed, in 2005,
focusing on vibration-based systems [6], and, in 2019,
focusing on image processing for visual inspection [13]. In
terms of in-service vehicles, a literature review, in 2015,
addressed track geometry condition [14]. Furthermore, the
literature has given considerable attention to wheel out-of-
roundness. A comprehensive review, in 2000, provided a
thorough analysis of the causes and modeling techniques of
wheel out-of-roundness [15]. An extension to this review,
in 2003, included causes of wheel corrugation and low-
order polygonal wear, along with mitigation measures to
tackle these challenges [16]. Additionally, in 2005, the
effects and implications of wheel out-of-roundness on
vehicle and track components were examined [17]. Since
then, numerous studies have emerged over the past decade,
continuously updating the state-of-the-art knowledge in
this
ﬁeld
[18].
Regarding
methods
for
condition
monitoring, early surveys primarily focused on the appli-
cation of physical-based degradation prediction models
[19]. However, the advent of Big Data has led to a growing
trend of using artiﬁcial intelligence for condition-based
maintenance, with numerous publications exploring this
approach. Despite these advancements, there remains a
scarcity of surveys in railway maintenance that speciﬁcally
focus on the application of artiﬁcial intelligence. Three
notable surveys, in 2019, 2020, and 2021, addressed
maintenance applications, measurement methods, data-
driven models, and evaluation considerations, providing
valuable insights into these areas [8–10]. However, these
surveys covered a wide range of railway subdomains,
sensor types, and failures, which somewhat limited their
depth of analysis. In contrast, the survey presented in this
paper aims to bridge the research gap by focusing on the
formulation, development, and evaluation of data mining
methods for condition-based maintenance, particularly in
the context of time series sensor data and wheel-track
interface components. By providing an extensive catego-
rization, identifying open challenges, and outlining future
research directions, this survey offers a more comprehen-
sive and focused examination of the subject matter, con-
tributing to the advancement of the ﬁeld.
3 Condition-based maintenance
The ﬁrst requirement for an effective maintenance plan
driven by artiﬁcial intelligence is ensuring the adequacy of
the condition-based maintenance strategy. This section
speciﬁcally concentrates on the mechanical components in
the wheel-track interface that present a gradual degradation
process, e.g., wear and rolling contact fatigue, and a major
threat to the operational safety of a railway system. Thus,
ensuring condition-based maintenance is the right strategy
[8].
In a railway system, the monitoring of the wheel-track
interface involves multiple crucial components that require
ongoing surveillance. Understanding the concept of failure
and its associated failure modes is of utmost importance in
this regard. Failure occurs when an item is no longer able
Fig. 3 Organization of the survey: eight sections
16710
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 5
to perform its required function, resulting in a fault or state
of inability, while each failure mode represents a distinct
way the performance requirement fails. Given the com-
plexity of the wheel-track interface and the diverse range of
potential failure modes, this survey focuses on aggregating
trends at the component level while highlighting the most
common failure modes. These monitoring objects can be
categorized into distinct areas of focus: wheel geometry,
bogie structural components, track geometry, and track
structural components.
Firstly, wheel geometry monitoring entails the assess-
ment of essential wheel parameters such as diameter, ﬂange
height, and tread proﬁle [4, 20–35]. By closely monitoring
these geometric attributes, abnormalities can be promptly
identiﬁed, enabling timely maintenance actions to be taken.
One signiﬁcant concern is the presence of out-of-round
wheels. These include ﬂats formed when a wheel set locks
and skids along the rail, polygonization caused by repeti-
tive loading and unloading cycles, and corrugated treads
formed by excessive friction or contact with external
objects. In addition to wheel geometry, monitoring the
health and performance of other associated bogie compo-
nents is vital. Among these components, the axle bearing
serves a critical role by facilitating the transfer of loads and
minimizing friction during the movement of the train
[36–38]. Table 1 summarizes the reviewed works accord-
ing to monitoring objects focusing on wheel geometry and
bogie structural components.
Track geometry monitoring is a critical process that
focuses on evaluating various irregularities that can have
negative effects on train stability and passenger comfort.
These irregularities include track misalignment, uneven-
ness, and deviations from the desired rail geometric
parameters [22, 39–67]. Key parameters of concern are
longitudinal level for wear, cant for centrifugal force, twist
for unevenness, alignment for lateral force, wide gauge, as
well as other horizontal and vertical deformities. These
failures typically initiate as small wear and cracks, but
quickly propagate due to the substantial shear and normal
stresses on the rail caused by rolling-sliding contact load-
ing. As cracks progress, they can result in spalling, leading
to material detachment from the rail surface.
Nonetheless, it should be noted that track geometry
irregularities not only are responsible for train accidents,
but they can also lead to the birth of structural defects.
These defects encompass several critical aspects, including
the condition of joints, turnouts/switches, rolling element
bearings, fasteners, sleepers, ballast, and subgrade. Joints
are used to connect two rail sections together [68]. They
provide ﬂexibility to accommodate temperature changes
and allow the rail to expand and contract without signiﬁ-
cant damage. Turnouts, also known as switches, enable
trains to change tracks or move from one line to another
[69, 70]. Rolling element bearings are used in various parts
of the railway system to reduce friction and allow smooth
rotation [37, 71, 72]. Fasteners, such as clips or bolts, are
used to secure the rail to the sleepers that provide support
and stability to the track [56, 73, 74]. The ballast, a layer of
crushed stones or gravel, provides support, drainage, and
stability to the track, while the subgrade refers to the
underlying soil or formation on which the track is con-
structed [42, 75, 76]. The failure modes associated with
these structural defects primarily involve wear, predomi-
nantly in curves, fatigue in the form of surface or subsur-
face cracks, and plastic ﬂow resulting in rail corrugation.
Table 2 summarizes the monitoring objects focusing on
track geometry and track structural components.
The existing studies in this ﬁeld have predominantly
adopted a single-component perspective, which oversim-
pliﬁes the modeling process by isolating interconnected
system effects [77]. As a result, it often leads to inconsis-
tent system-level conclusions. It is important to recognize
that railway systems are complex and heterogeneous,
composed of interdependent components such as rails,
sleepers, joints and fasteners, ballast, and subgrade.
Therefore, a more comprehensive approach is necessary,
considering the multicomponent system dependence cate-
gorized into economic, stochastic, and structural depen-
dence [78]. While a few studies have addressed the
economic dependence aspect by exploring the cost beneﬁts
of simultaneous maintenance of multiple components
[79–82], the literature remains largely insufﬁcient in
addressing both structural dependence, which involves
maintenance connections between parts, and stochastic
dependence, where the failure of one component affects the
performance of other parts of the system. In fact, the pre-
vailing multicomponent perspective found in the reviewed
literature merely offers limited explanations of the dynamic
Table 1 Categorization of works based on monitoring objects: wheel geometry and axle bearing
Item
Failure modes
References
Wheel
Geometry
Flats due to sliding and skidding, corrugated treads and polygonization with uneven wear, material fallout, such as
shelling or spalling
[4, 20–35]
Axle bearing
Material loss due to wear, inadequate lubrication, and fatigue
[36–38]
Neural Computing and Applications (2024) 36:16707–16725
16711
123

---

## Page 6
interaction between rolling stock and track components.
Some studies focus on examining the interaction between
friction on sharp curves, gauge corners, and track condi-
tions with defects [83–86]. Others investigate the impact of
overloads, weight-in-motion, and unbalanced loads on the
rail [87–90]. Furthermore, recent works have utilized a
simpliﬁed track quality index that integrates various fac-
tors, including dynamic effects, speeds, loads, and rail
geometry parameters [39, 58, 91, 92], and key features of
rail geometry parameters, such as gauge and twist, repre-
sented with standard deviations [57, 58, 93].
4 Data sources
The second requirement for an effective maintenance plan
driven by artiﬁcial intelligence is addressing the charac-
teristics of the available data in the challenging dynamic
context of the railway system. To make optimal mainte-
nance decisions, a vast amount of dynamic data from dif-
ferent sources is required, including service failure data,
signal data, ballast history, grinding history, remedial
action history, trafﬁc data, and inspection data. As the data
available impacts the selection and success of data mining
methods, this survey focuses solely on time series, not only
because it is the most common format of sensor data [7],
but also due to the complexity of dealing with the
sequential structure of data, with order and temporal
dependencies. There are four main measurement method-
ologies: manual inspection, dedicated track inspection
vehicles, onboard systems, and wayside systems. Different
sensors are used depending on the methodology. This
survey speciﬁcally concentrates on sensors that capture
time series data, such as eddy current, vibration, dis-
placement, impact load detectors, optical ﬁber, and ultra-
sonic sensors.
4.1 Measurement techniques
Manual inspection involves a walking patrol looking for
signs of track defects. Onboard techniques involve instal-
ling sensors on the vehicle to monitor the condition of the
track and the wheels themselves [57, 94, 95]. These can be
mounted on in-service vehicles that provide real-time data
for long lengths of track [36, 51, 52, 62, 84–86, 96–102].
Alternatively, track inspection vehicles are normally car-
ried out periodically and rarely on busy routes [21, 22,
48, 49, 53, 54, 103, 104]. In addition, wayside measure-
ment systems allow the extraction of signiﬁcant amounts of
data referring to all the operating vehicles with a reduced
number of sensors [23, 24, 83, 87, 91, 92, 105–109].
Table 3 highlights the four measurement techniques.
Within these measurement techniques, various sensors
are available to efﬁciently monitor and control different
process parameters, including force, machine vision, opti-
cal geometry, acoustic, ﬁber Bragg grating, pressure
transmitter, eddy current signal, ultrasonic, magnetic, and
thermal. Force measurement detectors are widely used to
monitor the impact between wheels and the track structure.
These detectors employ vibration-based systems to accu-
rately capture the forces involved [36, 37, 51, 83, 93,
102, 110–112]. Vertical loads are typically measured in
zones where the train is not accelerating or braking, while
lateral loads are best measured in narrow curves. A com-
monly used sensor is the wheel impact load detector, which
weighs each wheel multiple times and provides dynamic
impact
load
information
at
the
wheel
level
[36, 37, 51, 83, 93, 102, 110–112]. In addition, many
systems
deal
directly
with
acceleration
data
[43, 56, 62, 68, 113, 114]. Machine vision technology
utilizes advanced computer algorithms to process digital
image data obtained from vehicle’s underframes and side
frames [13, 91]. By analyzing this information, machine
vision systems can capture various wheel features, e.g.,
ﬂange height, ﬂange thickness, rim thickness, and diame-
ter, as well as the condition of vehicle components. Laser-
based systems also play a signiﬁcant role in track and
wheel monitoring [24, 58, 60, 91]. For example, optical
geometry detectors employ cameras mounted on tangent
tracks to calculate various parameters for each set of axles
based on the angle of attack and tracking position. These
systems enable precise measurements of the track’s ele-
vation, curvature, and alignment, which are crucial for
ensuring safe and efﬁcient railway operations. Longitudinal
level, a commonly measured parameter, helps maintain
track stability and smoothness [55, 75, 104, 115]. Acoustic
Table 2 Categorization of
works based on monitoring
objects: track geometry, joint,
turnout, rolling bearing, ballast,
and fastener
Item
Failure modes
References
Track Geometry
Rail head, breaks, longitudinal level, twist, and cant
[22, 39–67]
Joint
Misalignment and wear
[68]
Turnout
Misalignment
[69, 70]
Rolling bearing
Wear and overheating
[37, 71, 72]
Fastener and Sleeper
Corrosion and exposure to moisture
[56, 73, 74]
Ballast and Subgrade
Settlement and deformation
[42, 75, 76]
16712
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 7
emission monitoring involves processing the unique noise
signatures emitted [23, 116, 117]. By analyzing these
acoustic signals, anomalous patterns can be detected. In
addition, ultrasonic sensors are extensively employed in
track
and
wheel
monitoring
applications
[21, 44, 59, 61, 85, 103, 108, 109]. They use ultrasonic
waves to measure parameters such as distance, thickness,
and defects in materials. Fiber Bragg grating sensors are
widely utilized in track and wheel monitoring due to their
immunity to electromagnetic interference, multiplexing
capabilities, long reach, lightweight nature, and high signal
ﬁdelity [20, 87, 92, 106, 107, 118]. These measure
parameters such as strain [43, 53, 54, 57, 83, 84], tem-
perature [36, 96], and pressure [91]. Eddy current testing
involves inducing electrical currents in conductive mate-
rials to evaluate their integrity and detect ﬂaws or discon-
tinuities [44, 59, 63, 69]. Magnetic are also used to detect
the changes in the signature of metallic objects [22, 86].
4.2 Type of data
Furthermore, combining contextual data, e.g., maintenance
inspection history and trafﬁc volume, with sensors is cru-
cial for more accurate analysis, trend identiﬁcation, and
decision-making [39, 59, 63, 91, 104, 119, 120]. The use of
both real and simulated data is prevalent in railway con-
dition monitoring. Simulated data provides researchers
with several beneﬁts [4, 26, 29–32, 86, 90, 110, 120, 121].
One notable advantage lies in the ability to conduct con-
trolled
and
repeatable
experiments,
which
empower
researchers to manipulate variables and observe their
impacts without the constraints of real-world data collec-
tion. Nevertheless, it is crucial to acknowledge the limi-
tations and the necessity for validation through ﬁeld trials
using authentic data. Field trials offer invaluable insights
into the performance, reliability, and generalizability of
models, algorithms, and interventions [36, 39, 40, 43,
53, 54, 58, 66, 91, 96, 97, 105, 106, 114, 115, 119, 122].
They enable researchers to identify potential issues, assess
the inﬂuence of confounding factors, and uncover unex-
pected outcomes. In fact, the current state of research still
demonstrates an absence of algorithms that have been
validated using real streaming data. Some efforts have been
made to address this challenge by developing algorithms
that perform computationally intensive training ofﬂine,
resulting in models ready for rapid real-time predictions
[20, 36, 49, 56, 91, 92, 96, 100, 101, 123, 124]. Table 4
presents an overview of these data types, highlighting the
absence of practical implementations of complete online
algorithms.
5 Problem formulation
The third requirement for an effective maintenance plan
driven by artiﬁcial intelligence is to select effective pre-
processing techniques to deal with the high dimensionality
and temporal dimension, such as for data representation,
similarity measurement, and indexing. In addition, it is
crucial to consider not only the available data but also the
desired output that the model should provide, and time-
frame involved. To illustrate this process, let’s consider the
example of rail wear caused by the friction between train
wheels and the tracks. It is important to formulate speciﬁc
goals based on the business requirements or the mainte-
nance staff needs. For instance, are there requirements to
detect rail sections with an uneven longitudinal level in
real-time? Or perhaps the goal is to predict sections nearing
the end of their useful lifespan and schedule replacements
for the next year, treating it as a classiﬁcation problem?
Another approach could involve survival analysis to pre-
dict the probability of the contact rail having a level below
a speciﬁc threshold within the next three years. Alterna-
tively, the goal might be to forecast the longitudinal level
in one year’s time. Once the problem formulation aligns
with the available data, it becomes crucial to select
appropriate data mining methods as well as key imple-
mentation components representative of time series data.
For example, if the focus is primarily on condition moni-
toring, a state space model might be adequate for capturing
the dynamics of the system. However, if there is a lot of
contextual information available, other machine learning
models such as neural networks, decision trees, or support
Table 3 Categorization of works based on measurement: manual inspection, inspection vehicle, in-service vehicles, and wayside sensors
Method
Description
References
Manual inspection
Walking patrol looking for signs of potential failure
[57, 94, 95]
Inspection vehicles
Mechanized track patrol carried out with sparse frequency
[21, 22, 48, 49, 53, 54, 103, 104]
In-service vehicles
Onboard sensors providing real-time data
[36, 51, 52, 62, 84–86, 96–102]
Wayside sensors
Fixed sensors providing real-time data
[23, 24, 83, 87, 91, 92, 105–109]
Neural Computing and Applications (2024) 36:16707–16725
16713
123

---

## Page 8
vector machines might be better suited to handle the
multidimensionality.
5.1 Modeling strategy
Predictive maintenance involves six modeling strategies,
serving distinct purposes and relying on speciﬁc types of
data. These strategies can be grouped into fault diagnosis
and fault prognosis. When a machine experiences a
breakdown, a substantial amount of time is typically spent
on pinpointing the causes of the failure, while only a minor
portion is allocated to the actual repair.
Fault diagnosis involves identifying the factors respon-
sible for the deterioration observed in a component with
three stages involved: detection, isolation, and identiﬁca-
tion [4, 20, 21, 25, 26, 29–32, 37, 42,
50, 57,
68–70, 73, 74,
94–96, 100, 107, 109, 111, 112,
116, 121, 123–132]. Detection involves anomaly detection
and benchmarking machine behavior to identify deviations.
Isolation determines the speciﬁc kind, location, and time of
fault occurrence, such as identifying the exact component
of the track, bogie, or defective wheel. Identiﬁcation
focuses on quantifying the size and behavior of the fault.
Fault prognosis aims to answer questions related to the
timing and extent of failure or degradation in the observed
equipment, in three different ways: failure prediction,
survival analysis, and remaining useful life (RUL) esti-
mation. Failure prediction involves classifying failures
within a speciﬁed time window, which helps optimize
maintenance
strategies
[34,
39,
41,
47–49,
60,
91, 98, 101, 104, 105, 110, 114, 119]. Survival analysis is
used to assess the probability of failure over time, pro-
viding insights into component reliability and longevity
[23, 24, 83, 87, 91, 92, 105–109]. Finally, it is possible to
estimate the remaining useful life of the components
[36, 40, 41, 43,
45, 49, 51, 52, 54,
62, 64, 72,
84–86, 96–102, 118, 120, 133]. Table 5 highlights several
works
with
fault
diagnosis
and
prognosis
modeling
strategies.
5.2 Learning method
The modeling strategy highly inﬂuences the learning
method of choice. For failure diagnosis, the most common
are query by content which involves measuring the simi-
larity of individual instances against a normal baseline
[132], anomaly detection which involves ranking a set of
instances, from the most anomalous to the most normal
[96, 121, 126] and clustering by ﬁnding intrinsic groups of
types or severities of damage [44, 128, 129]. While these
techniques provide essential avenues for failure diagnosis
without the need for labeled data, their unsupervised nature
poses inherent limitations. Without access to ground truth
labels, these techniques struggle to distinguish outliers or
anomalies accurately, leading to false positives and false
negatives. Moreover, their reliance solely on intrinsic
dataset properties makes them sensitive to changes in data
distribution over time, hindering their ability to adapt and
accurately identify deviations from normal behavior.
Additionally, clustering algorithms may encounter chal-
lenges when dealing with high-dimensional or nonlinear
data. In this regard, classiﬁcation models have indeed
demonstrated superior performance [45, 119]. Furthermore,
their use enables the extension to the more enriching
modeling strategies for failure prediction and RUL esti-
mation. By leveraging labeled data, these techniques can
not only accurately identify failure instances but also pro-
vide valuable insights into the progression of failures over
time. This allows for the development of more sophisti-
cated predictive models that consider various factors
inﬂuencing failures, such as temporal patterns, environ-
mental conditions, and operating parameters. However,
despite this potential, traditional algorithms continue to
dominate the literature and often lag the state of the art,
indicating that the full realization of these advantages has
not yet been achieved. For example, kNN struggles with
computational complexity and sensitivity to irrelevant
features [97, 101, 134], while decision trees are prone to
overﬁtting and instability [91, 97, 134]. Ensemble methods
like random forests [43, 61, 97, 119] and AdaBoost [73, 74]
Table 4 Categorization of works based on characteristics of data: simulated, real, contextual, and stream
Type
Description
References
Simulated
data
Controlled and repeatable experiments
[4, 26, 29–32, 86, 90, 110, 120, 121]
Real data
Acknowledge all uncontrollable interferences
[36, 39, 40, 43, 53, 54, 58, 66, 91, 96, 97, 105, 106, 114, 115, 119, 122]
Contextual
data
Failures, ballast history, trafﬁc, inspections, and
interventions
[39, 59, 63, 91, 104, 119, 120]
Data stream
Recognize high-rate frequency of continuous ﬂow
of data
[20, 36, 49, 56, 91, 92, 96, 100, 101, 123, 124]
16714
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 9
enhance classiﬁcation accuracy but are sensitive to noisy
data and outliers. Logistic regression assumes linear rela-
tionships and may underperform with nonlinear data
[39, 46, 121]. Support vector machines’ performance
depends on kernel and parameter selection, making them
less suitable for large datasets and noisy environments
[37, 43, 51, 58–60, 69, 91, 94, 101, 120, 134]. To overcome
these limitations and push the boundaries of failure diag-
nosis and prognosis, recent efforts have explored novel
benchmark models. For instance, deep learning architec-
tures like convolutional neural networks (CNNs) and
recurrent neural networks (RNNs) offer the capability to
handle complex, high-dimensional data, and capture tem-
poral
dependencies
effectively
[57, 100, 101, 110, 111, 120]. Moreover, Bayesian methods
present a promising avenue for enhancing failure diagnosis
tasks [42, 63, 101, 104, 121]. Unlike traditional methods
that often struggle with uncertainty estimation, Bayesian
approaches offer a principled framework for probabilistic
inference, allowing for robust uncertainty quantiﬁcation in
predictions. By explicitly modeling uncertainty, Bayesian
methods can provide more reliable assessments of failure
likelihoods, particularly in the railway setting with limited
or noisy data. Additionally, Bayesian techniques facilitate
the incorporation of prior knowledge or domain expertise
into the modeling process, enabling more informed deci-
sion-making and improved generalization performance.
Lastly, for survival analysis both probability distribution
models [63, 75] and stochastic processes [72, 76, 115] are
used
in
incorporating
time-related
variables
and
considering the dynamic nature of failures. Table 6
encapsulates the link between common learning methods
and tasks.
5.3 Implementation components
When analyzing time series sensor data, it is also important
to consider several factors that can impact the success of
data mining methods. Noise, inconsistencies, missing, or
duplicated data are common challenges in railway condi-
tion monitoring with low-cost sensors. Fluctuations in
reported values may result from minor variations in sensor
sensitivity, unrelated events near the sensor, or transmis-
sion errors. To circumvent these, the fundamental shape
characteristics of the time series signals are typically
extracted through three groups of techniques: shape-based,
feature-based, and model-based [135]. For short time ser-
ies, shape-based representation is the most used, while for
long time series both feature-based and model-based rep-
resentations are derived and compared. Furthermore, these
techniques are often accompanied by various signal pre-
processing stages. The most common are noise ﬁltering,
scaling differences, and contextualization [10]. Noise ﬁl-
tering is handled with traditional signal processing tech-
niques
like
digital
ﬁlters
or
wavelet
thresholding.
Resampling is also typically used to smooth the noise in
high-frequency signals. Scaling differences between time
series are handled with normalization and transformation
invariances. Contextualization is handled with data fusion
techniques. This need for contextualization comes from the
fact that sensors are distributed in the railway environment.
Table 5 Categorization of works based on modeling strategies: fault diagnosis, failure prediction, RUL estimation, survival analysis
Measurement
Problem
framing
References
Fault
Diagnosis
Is there a
potential
failure?
Where?
What? How
severe?
[4, 20, 21, 25, 26, 29–32, 37, 42, 50, 57, 68–70, 73, 74, 94–96, 100, 107, 109, 111, 112, 116, 121, 123–132]
Failure
prediction
Will a failure
happen in
the next
year?
[34, 39, 41, 47–49, 60, 91, 98, 101, 104, 105, 110, 114, 119]
RUL
Estimation
When will the
next failure
happen?
[36, 40, 41, 43, 45, 49, 51, 52, 54, 62, 64, 72, 84–86, 96–102, 118, 120, 133]
Survival
analysis
What is the
probability
of failure
over time?
[23, 24, 83, 87, 91, 92, 105–109]
Neural Computing and Applications (2024) 36:16707–16725
16715
123

---

## Page 10
On the one hand, wayside sensors present spatial rela-
tionships which indirectly determine a temporal correlation
between observations. On the other hand, onboard sensors
are consistently facing dynamic contexts of weather, soil
type, and others. To circumvent this problem, the most
used
technique
is
principal
component
analysis
[4, 26, 45, 58, 60, 95]. Also, a recent work proposed deep
autoencoder to capture and compress the salient features of
the input data [45].
Feature-based is the most used approach to represent the
fundamental shape characteristics of a time series in wheel-
track condition monitoring. Various advanced signal pro-
cessing methods have been proposed that extract con-
densed damage-sensitive knowledge, with both statistical
and frequency-domain features, e.g., the Fourier transform
[52, 85, 113]. However, time–frequency techniques have
been the most widely used, due to their ability to identify
content of a signal in the frequency-domain without losing
information
abouts
its
time
domain
characteristics
[84, 102, 105, 113]. Three commonly used techniques are:
the
Wavelet
Transform
[37, 50, 56, 58, 62, 84, 99, 102, 111, 130], Wigner-Ville
Transform [84, 102], and Short-time Fourier Transform
[4, 84, 102]. Furthermore, other approaches were devel-
oped to help dealing with the nonlinear effects on the
suggested time-dependent characteristics. For instance,
changes in train speed tend to affect the impact load, but
this can vary based on the speciﬁc length of wheel ﬂats, not
following the pattern of increased impact load with higher
train speeds [136]. Some alternatives were then suggested
to extract the features, such as a time–frequency kurtosis to
reduce surrounding noise and highlight faulty signal pat-
terns of wheel ﬂats [116], spectral kurtosis [31], symbolic
data [131], and empirical mode decomposition to transform
the signal into several intrinsic mode functions that isolate
the failure signal mode from interferences and a criterion
based on signal lag and envelope spectrum [29, 30].
Model-based
representation
consists
in
directly
describing the dynamic behavior of the signal, such as
autoregressive models [33, 64, 115], state space models,
e.g.,
the
Hidden
Markov
Model
[34, 35, 38, 41, 42, 48, 55, 133] and regression [43, 134]. In
fact, model-based representations are also frequently used
to extract coefﬁcients which are then used in a feature-
based approach [75, 91, 97, 110]. Recently, there has also
been an increased use of deep learning models. Recurrent
neural networks (RNNs) have become popular architec-
tures used for railway condition monitoring, including long
short-term
memory
(LSTM)
for
capturing
long-term
dependencies in sequential data [40, 43, 53, 119]. Alter-
natively, convolutional neural networks (CNNs) despite
commonly associated with image recognition tasks, also
have been applied to time series data with some modiﬁ-
cations [68, 112].
Shape-based representation directly focuses on distin-
guishing or matching any pair of time series with an
intuitive distance. To formalize this measure, it is neces-
sary to establish a notion of similarity based on perceptual
criteria rather than strict mathematical identity. In railway
condition monitoring, dynamic time warping (DTW)
[70, 127, 129, 132] has been preferred over the Euclidean
distance [125], as it allows for the recognition of percep-
tually similar objects, even if they are not identical in
mathematical terms. Table 7 categorizes these algorithms
into the three described groups.
Finally, the stationarity of time series data must be
considered. A stationary time series has consistent mean,
variance, and autocorrelation over time. However, IoT data
often exhibit non-stationarity in the form of concept drifts,
seasonality and change points. Concept drift refers to
changes in the statistical distribution of data over time,
while seasonality involves cyclical changes occurring over
longer time scales. Change points represent abrupt and
permanent shifts in the normal state of a monitored system.
The standard solution involves the identiﬁcation of change
points, then determining functions for curve ﬁtting the
intervals between them [27, 36, 137].
6 Evaluation metrics
The ﬁnal requirement for an effective maintenance plan
driven by artiﬁcial intelligence is to properly evaluate the
devised models for performance, interpretability, cost
Table 6 Categorization of works based on learning methods: query by content, anomaly detection, clustering, classiﬁcation, forecasting,
regression, probability distribution model, and stochastic process
Learning task
Common learning methods
References
Fault diagnosis
Query by Content, anomaly detection, clustering
[44, 96, 121, 124, 126, 128, 129, 132]
Failure prediction
Classiﬁcation
[39, 41, 60, 91, 98, 101, 105, 110, 114, 119]
RUL Estimation
Forecasting, regression
[36, 40, 41, 43, 45, 49, 54, 64, 72, 97, 118, 120, 133]
Survival analysis
Probability distribution model, stochastic process
[63, 72, 75, 76, 115]
16716
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 11
incorporation, and considerations of streaming environ-
ments. Assessing the predictive capabilities of an intelli-
gent system for determining when train maintenance is
needed extends beyond mere accuracy evaluations. It
entails a comprehensive evaluation encompassing various
facets. These include performance assessment, considera-
tion of cost implications associated with false positives and
false negatives, the interpretability of the model, and
continuous
monitoring
of
the
system’s
performance
through real-time data analysis. Moreover, datasets related
to rail defects often exhibit a highly imbalanced distribu-
tion, with a substantial majority of observations falling
within the non-defective category. This skewing signiﬁ-
cantly challenges the reliability of standard evaluation
metrics. Therefore, the selection of an appropriate evalu-
ation metric becomes pivotal. In this regard, three primary
categories of metrics should be considered: threshold
metrics,
ranking
metrics,
and
probability
metrics
[48, 91, 96, 97, 110, 121, 132, 138]. Threshold metrics,
such as accuracy, sensitivity–speciﬁcity, and precision-re-
call, quantify classiﬁcation prediction errors. Ranking
metrics evaluate classiﬁers based on their ability to sepa-
rate classes and include the ROC curve and precision-recall
curve. Probabilistic metrics quantify uncertainty in a clas-
siﬁer’s predictions, which is useful for penalizing wrong
but highly conﬁdent predictions. Intrinsically related to this
imbalanced distribution is the notion of a false alarm or
false safe prediction. From the engineer’s perspective, high
false alarm prediction usually leads to ineffective and
unnecessary decision-making, while false safe prediction
can cause huge loss for the railway service suspensions.
While it is crucial to customize these deﬁnitions to suit the
speciﬁc needs and data characteristics of a business, there
has been a limited exploration of the economic implica-
tions stemming from the performance of these proposed
methodologies [65–67, 122]. To compute these costs
accurately, it is imperative to consider mandatory regula-
tions, operational imperatives related to equipment uptime
and ensuring the safety of personnel, as well as the con-
straints associated with the availability of maintenance
staff and track infrastructure.
Additionally, in most studies, a signiﬁcant challenge
emerges in bridging the gap between evaluating sensor
types, their placement, and repair strategies, all while
accommodating the need for human operators to receive
assistance from AI in managing multi-objective trade-offs
and addressing diverse priorities [139]. This inherent gap in
the problem formulation is unavoidable, stemming from
the nuanced dynamics of these trade-offs, necessitating
case-speciﬁc decision-making. To address this inherent
incompleteness, the incorporation of explanations becomes
pivotal in ensuring the trustworthiness of the decision-
making process [48, 55, 75, 83, 91, 95, 96, 119]. This
includes developing visual analytics techniques, prototyp-
ical examples, and deductive argumentative systems for
explanations. Finally, the large volumes of sensor data
impose on algorithms memory and time constraints. Thus,
algorithms must be evaluated on scalability and accuracy
over time in data stream settings [91, 132, 140]. Table 8
categorizes these metrics into the four described groups.
7 Discussion
Despite the substantial body of work dedicated to this ﬁeld
in recent years, the research seems to have been predom-
inantly motivated by the exploration of novel approaches,
rather than a direct response to practical issues. In fact,
there is a lack of robust business-oriented justiﬁcations for
problem formulation, temporal dimension detailing, and
technique selection within current practices. To address
this gap, forthcoming research should delve into method-
ologies explicitly integrating business objectives into the
analytical pipeline, in light of the four discussed require-
ments for creating an effective maintenance plan: condi-
tion-based
maintenance
strategy
appropriateness,
data
source, problem formulation, and complete evaluation.
This detachment from practicality in the literature is
exempliﬁed by the neglect of more complex fault diagnosis
tasks, such as isolating speciﬁc types, locating occurrences,
and accurately quantifying fault behavior. Additionally,
fault prognosis has tended to prioritize timing over
assessing the full extent of failure or degradation. There is
a pressing need for literature to move beyond mere
anomaly detection and single-component behavior bench-
marking to identify peak deviations. To tackle these
Table 7 Categorization of works based on implementation components for time series: feature-based, model-based, and shape-based
Measurement
Problem framing
Works
Feature-
based
Statistical, time–frequency, spectral, model
coefﬁcients
[4, 29–31, 50, 52, 56, 58, 62, 84, 84, 84, 85, 99, 102, 102, 102, 111, 113]
Model-based
Autoregressive, HMM, Regression, RNN, LSTM
[33–35, 38, 40–43, 48, 52, 55, 64, 97, 115, 133]
Shape-based
Euclidean, DTW
[70, 125, 127, 129, 132]
Neural Computing and Applications (2024) 36:16707–16725
16717
123

---

## Page 12
challenges, three distinct research directions emerge from
the surveyed papers: uncertainty quantiﬁcation, explana-
tion techniques, and multicomponent modeling.
Quantifying model uncertainty is key in railway envi-
ronments where the cost of a mistake can be huge, allowing
for safer actions and human interventions. In this regard,
leveraging the surveyed techniques on probabilistic mod-
eling and Bayesian methods already holds promise for
quantifying uncertainty. However, these measures were
estimated on the whole testing data, which may introduce
biases, akin to the challenges encountered by dealing with
imbalanced classes. The uncertainty associated with the
typically small groups of samples associated with failure
could potentially become biased toward the performance
on the rest of the data. Thus, future research lies in
developing
pointwise
evaluation
measures
to
assess
uncertainty accurately. Indeed, these estimates would not
only serve as crucial indicators but also provide explana-
tions for the model’s predictions. This is pivotal in ensuring
trustworthiness
and
facing
the
inherent
formulation
incompleteness of a condition-based maintenance problem.
Alternatively to uncertainty estimates, relevant and
nonredundant feature subsets can be detected trough
interpretable models or post hoc explanation techniques.
Interpretable models, such as sparse neural networks,
induced by structured weight pruning and group sparsity
regularization, offer transparency by directly showing how
each feature contributes to the prediction outcome. Post
hoc explanation techniques, such as layer-wise relevance
propagation and feature visualization methods, by analyz-
ing the patterns that maximally activate individual neurons
or layers, provide insights into which parts of the input
contribute most to the model’s decision. Furthermore,
ensuring the stability of these explanations over time is
crucial for building trust. Thus, an open challenge in rail-
way maintenance still lies in computing multiple model
explanations over time, tracking attribute-value contribu-
tions for prediction outcomes and the magnitudes of their
changes.
Furthermore, the literature has primarily favored sim-
plistic
single-component
methodologies.
While
some
studies have delved into the economic interdependence by
examining the cost-effectiveness of concurrent mainte-
nance
across
multiple
components,
there
remains
a
notable gap in addressing both stochastic dependence,
wherein the failure of one component impacts the perfor-
mance of other system elements, and structural depen-
dence, pertaining to maintenance interconnections among
various parts. Future research should prioritize the devel-
opment of comprehensive modeling frameworks that
encompass economic, stochastic, and structural dependen-
cies. Embracing such a holistic perspective holds the pro-
mise of unlocking deeper insights into multicomponent
railway systems. This, in turn, would also enrich the value
of complex fault diagnosis tasks by enhancing capabilities
in isolating speciﬁc fault types and pinpointing interde-
pendent occurrences.
To bypass the challenges associated with uncertainty,
explainability, and multicomponent dependence, research-
ers have resorted to using highly speciﬁc labeled data to
train supervised models capable of recognizing fault pat-
terns, their locations, and impacts. However, while this
approach offers a simpliﬁed workaround, labeling data
with such speciﬁcity can indeed be a complex and
resource-intensive endeavor, particularly in real-world
railway systems where faults occur infrequently and under
varying conditions. This practical challenge is further
compounded by the presence of large volumes of data with
imbalanced distributions. Therefore, future research should
prioritize strategies aimed at overcoming the limited
availability
of
labeled
inputs
post-deployment
and
automating data labeling methods. Four lines of research
have been overlooked in this regard and warrant further
exploration: multimodal data fusion, transfer learning,
semi-supervised learning, and active learning.
For instance, while this survey primarily focuses on time
series data, no speciﬁc exclusion criteria were set regarding
the inclusion of other data types. However, it is notable that
there is a surprising scarcity of works integrating contex-
tual data from diverse sources such as failure records,
equipment logs, maintenance history, and trafﬁc images.
This omission highlights the potential of advanced tech-
niques in multimodal data fusion. By harnessing contextual
information for automatic labeling, such efforts could
Table 8 Categorization of works based on evaluation metrics: performance, interpretability, costs, and computational expense
Evaluation
Metric
References
Performance
Threshold, ranking, probabilistic
[48, 91, 96, 97, 110, 121, 132, 138]
Interpretability
Visual analytics, prototypical examples, deductive argumentative systems
[48, 55, 75, 83, 91, 95, 96, 119]
Cost
Mandatory regulations, operational imperatives
[65–67, 122]
Computational expense
Memory requirements, computational time, stream
[91, 132, 140]
16718
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 13
effectively reduce manual efforts and enhance efﬁciency in
model training, particularly when combined with sensor
data.
Besides leveraging knowledge and labels from related
modalities, another research direction lies in learning from
related domains. This is particularly advantageous in the
wheel-track interface, composed of a wide array of
essential components such as wheels, axle bearings, tracks,
joints, turnouts, rolling bearings, ballasts, and fasteners.
This interdependent structural composition suggests that
certain fault patterns and characteristics may be consistent
across various railway systems or similar monitoring
objects within the same system. Transfer learning tech-
niques can effectively harness this shared structure and
underlying patterns by transferring knowledge from pre-
trained models or datasets in related domains to bootstrap
model training. Nonetheless, further research is necessary
to explore the effective transfer of knowledge within this
diverse composition, while ensuring model generalization
across different railway conditions and environments,
encompassing variations in wagon types, track geometries,
wheel geometries, and other relevant factors.
In addition to integrating new sources of information to
alleviate limited labels, a promising but overlooked alter-
native is to address the labeling bottleneck itself. This can
be achieved by selectively querying the labels of unlabeled
instances to an oracle, prioritizing instances that are most
uncertain, such as those near the discriminative hyperplane,
and whose labels would provide the greatest value to the
learning process. Future research should focus on devel-
oping active learning strategies to minimize the cost of
collecting labeled data.
Lastly, instead of worrying about limited data, one can
focus on exploiting the information contained in unlabeled
data points. In this regard, semi-supervised techniques are
extremely useful in addressing issues related to model
updating and retraining in limited labeled data environ-
ments, despite not addressing the primary question of
active learning, which is when to query. Future research
efforts should focus on semi-supervised learning strategies,
such as self-training and co-training, to capitalize on the
potential of unlabeled data and further improve model
performance.
Concerning the labeling process itself, the literature has
been following the annotation scheme in Fig. 4. In RUL
estimation, by counting backwards from a known moment
of failure, stopping when reaching the previous one. In
failure prediction, by considering a ﬁxed window of
instances before the failure as positive examples. In fault
diagnosis, by considering solely the moment of failure as a
positive example.
However, considering most of the mechanical compo-
nents in the wheel-track interface present a slow gradual
degradation process, failures might be months apart. With
tens of thousands of observations in between, it is neither
intuitive nor useful to create the labels at such a magnitude.
Moreover, the moments of failure are not always known.
Indeed, a maintenance inspection happens before a failure
occurs, which shadows the real failure moment. To alle-
viate these issues, future research could lie in merging both
fault diagnosis and prognosis techniques. The RUL back-
ward count could be limited upon reaching the ﬁrst
anomalous observation diagnosed since the previous fail-
ure, as illustrated in Fig. 5. The ﬁrst anomalous state would
be automatically determined by the system’s diagnosed
degradation exceeding and maintaining above a tolerance
threshold.
Indeed, the assumption of unlimited labeled data rep-
resents a fundamental challenge that undermines the
robustness of model performance. Moreover, while much
of the surveyed literature relies heavily on hand-engineered
features tailored speciﬁcally for time series analysis, the
lack of robustness in these features further compounds the
issue. Recent efforts exploring novel deep learning archi-
tectures have underscored the shortcomings of traditional
hand-crafted features, revealing the potential of feature
representation learning to signiﬁcantly enhance model
performance across various tasks. The next natural step lies
in meta-learning, especially within neural networks. By
integrating joint feature, model, and algorithm learning,
future research should target replacing prior hand-designed
learners by learned learning algorithms. In fact, meta-
learning would not only serve as a development tool but
also provide the ability to update and maintain the model.
By building a database of historical experiments and their
outcomes, meta-learning algorithms can quickly identify
Fig. 4 Traditional annotation scheme, where green circles represent
normal behavior and red crosses represent failures
Fig. 5 Proposed annotation scheme, where orange squares represent
anomalous
behavior
and
green
tools
represent
maintenance
interventions
Neural Computing and Applications (2024) 36:16707–16725
16719
123

---

## Page 14
promising algorithms and hyperparameters, accelerating
the optimization process.
In addition to meta-learning, various automated machine
learning (AutoML) techniques present promising avenues
for breaking the strong barrier between the training and
testing phase, such as metaheuristics and Bayesian opti-
mization. While data preprocessing and feature engineering
are acknowledged as crucial for effective time series data
mining in the surveyed literature, automating these pro-
cesses remains challenging due to their inherent lack of
robustness
and
the
need
of
domain-speciﬁc
factors.
Therefore, priority should be given to the development of
combined algorithm selection and hyperparameter tuning
(CASH) techniques tailored explicitly to the unique
demands of railway maintenance applications.
While these methodologies show promise in railway
systems that accumulate knowledge over time, retaining all
historical data remains highly impractical. Conversely,
updating parameters solely based on recent data introduces
a bias toward that data. Indeed, the existing literature
predominantly favors traditional approaches, heavily reli-
ant on the assumption of stationarity, a notion frequently
invalidated by real-world environmental and operational
variations. Despite some proposed solutions, there exists a
pressing demand for memory-constrained algorithms cap-
able of inherently adapting to current concepts while
retaining past knowledge. This highlights the necessity for
incremental algorithms incorporating mechanisms for both
retention and forgetting. For instance, retention could be
achieved through deep generative replay, employing gen-
erative models to encapsulate summaries of previous con-
cepts, while forgetting could be realized through adaptive
windowing
techniques
dynamically
adjusting
window
lengths based on real-time monitoring of environmental
cues, performance indicators, or distributional changes.
Despite these incremental strategies offering promise in
managing the vast data inﬂux within railway environments,
they may still fall short. The aggregation of extensive time
series data from sensors spread across extensive rail net-
works demands a nuanced equilibrium between memory
constraints and predictive performance. This trade-off
underscores the need for scalable algorithms as a focal
point of research, by distributing training data or model
components across multiple processing units, while syn-
chronizing parameter updates.
Finally, to ensure the successful translation of research
ﬁndings into practical applications, it’s essential to conduct
thorough benchmarking while considering the various
factors discussed. Future research should include evalua-
tion of performance metrics, while addressing cost con-
siderations, interpretability, and computational expenses.
Moreover, active engagement of key stakeholders, includ-
ing maintenance staff and management, is crucial at every
developmental stage to ensure widespread acceptance of
these systems.
8 Conclusions
In light of four essential requirements for creating an
effective maintenance plan, this survey has examined the
signiﬁcant progress in low-cost and easily maintainable
condition monitoring systems on railways. Regarding the
suitability of employing a condition-based maintenance
approach, our ﬁndings afﬁrm that this strategy proves most
effective in addressing the gradual deterioration processes
observed at the wheel-track interface, such as wear and
rolling contact fatigue. This interface stands out as the
primary focus in railway monitoring. With respect to data
availability, this survey has prioritized time series data due
to its ubiquity in sensor-generated information and the
inherent complexity associated with its temporal structure.
Within this context, the following suggestions for future
research directions (RD) are presented:
•
(RD1) Formulating the problem in detail to properly
select effective preprocessing techniques for dealing
with the temporal dimension, as well as determining the
modeling strategy.
•
(RD2) Quantifying model uncertainty as pointwise
evaluation measures and explanations of the model’s
predictions, leveraging the surveyed techniques on
probabilistic modeling and Bayesian methods.
•
(RD3) Computing multiple model explanations over
time, with attribute-value contributions for prediction
outcomes and the magnitudes of their changes, trough
interpretable
models
or
post
hoc
explanation
techniques.
•
(RD4) Adopting more comprehensive multicomponent
modeling approaches, that simultaneously encompass
economic, stochastic, and structural dependencies.
•
(RD5) Automating data labeling methods for large
volumes of sensor data while addressing the limited
availability of labeled inputs after model deployment.
•
(RD6) Integrating contextual data on failures, ballast
history, trafﬁc images, inspections, and interventions
data, with multimodal data fusion techniques.
•
(RD7) Exploring effective transfer learning strategies in
shared fault patterns and structural characteristics to
bootstrap model training, while ensuring generalization
across different railway conditions and environments.
•
(RD8) Developing active learning strategies, by selec-
tively querying the labels of unlabeled instances to an
oracle, prioritizing instances that are most uncertain.
16720
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 15
•
(RD9) Exploiting the information contained in unla-
beled data points, with semi-supervised learning strate-
gies, such as self-training and co-training.
•
(RD10) Adopting new labeling processes that consider
both the slow gradual degradation process and unknown
moments of failure, by complementing fault diagnosis
and prognosis techniques.
•
(RD11) Integrating joint feature, model, and algorithm
learning, especially in neural networks, with an addi-
tional meta-learning layer.
•
(RD12) Automating algorithm selection and hyperpa-
rameter tuning with AutoML techniques, such as meta-
learning, metaheuristics, and Bayesian optimization.
•
(RD13) Developing incremental memory-constrained
algorithms with both remembering and forgetting
mechanisms to inherently adapt to current concepts
while preserving past knowledge.
•
(RD14) Developing scalable algorithms, that accom-
modate increased data volume, by distributing training
data or model components across multiple processing
units and synchronizing parameter updates.
•
(RD15) Including evaluation of performance metrics,
while addressing cost considerations, interpretability,
and computational expenses. Moreover, active engage-
ment of key stakeholders is key.
Acknowledgements This work has been supported by the European
Union under the Next Generation EU, through a grant of the Por-
tuguese Republic’s Recovery and Resilience Plan (PRR) Partnership
Agreement, within the scope of the project PRODUTECH R3. It has
received Portuguese National Funds through Portuguese Foundation
for Science and Technology under project UIDP/00760/2020 (https://
doi.org/https://doi.org/10.54499/UIDP/00760/2020),
and
Ph.D.
scholarships PRT/BD/154713/2023, SFRH/BD/136253/2018. The
second author acknowledges the ﬁnancial support from Programmatic
funding UIDP/04708/2020 (https://doi.org/https://doi.org/10.54499/
UIDP/04708/2020) of the CONSTRUCT, funded by national funds
through the FCT/MCTES (PIDDAC).
Funding Open access funding provided by FCT|FCCN (b-on).
Data availability The authors declare that the data supporting the
ﬁndings of this study are available within the paper.
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
1. Hidirov S, Guler H (2019) Reliability, availability and main-
tainability analyses for railway infrastructure management.
Struct Infrastruct Eng 15(9):1221–1233
2. Fro¨hling RD, Hettasch G (2010) Wheel-rail interface manage-
ment: a rolling stock perspective. Proc Inst Mech Eng F J Rail
Rapid Transit 224(5):491–497
3. Chong SY, Lee J-R, Shin H-J (2010) A review of health and
operation monitoring technologies for trains. Smart Struct Syst
6(9):1079–1105
4. Mohammadi M, Mosleh A, Vale C, Ribeiro D, Montenegro P,
Meixedo A (2023) An unsupervised learning approach for
wayside train wheel ﬂat detection. Sensors 23(4):1910
5. Lagneba¨ck R Evaluation of wayside condition monitoring
technologies
for
condition-based
maintenance
of
railway
vehicles
6. Barke D, Chiu WK (2005) Structural health monitoring in the
railway industry: a review. Struct Health Monit 4(1):81–93
7. Alemi A, Corman F, Lodewijks G (2017) Condition monitoring
approaches for the detection of railway wheel defects. Proc Inst
Mech Eng F J Rail Rapid Transit 231(8):961–981
8. Xie J, Huang J, Zeng C, Jiang S-H, Podlich N (2020) Systematic
literature review on data-driven models for predictive mainte-
nance of railway track: implications in geotechnical engineering.
Geosci (Basel) 10(11):425
9. Davari N, Veloso B, de Costa GA, Pereira PM, Ribeiro RP,
Gama J (2021) A survey on data-driven predictive maintenance
for the railway industry. Sensors 21(17):57396
10. Chenariyan Nakhaee M, Hiemstra D, Stoelinga M and van Noort
M (2019) The recent applications of machine learning in rail
track maintenance: A survey. In: Reliability, Safety, and Secu-
rity of Railway Systems. Modelling, Analysis, Veriﬁcation, and
Certiﬁcation: Third International Conference, RSSRail 2019,
Lille,
France,
June
4–6,
Proceedings
3,
Springer,
2019,
pp 91–105
11. Ward CP et al (2011) Condition monitoring opportunities using
vehicle-based sensors. Proc Inst Mech Eng F J Rail Rapid
Transit 225(2):202–218
12. Hodge VJ, O’Keefe S, Weeks M, Moulds A (2014) Wireless
sensor networks for condition monitoring in the railway indus-
try: a survey. IEEE Trans Intell Transp Syst 16(3):1088–1106
13. Liu S, Wang Q, Luo Y (2019) A review of applications of visual
inspection technology based on image processing in the railway
industry. Transport Safety Environ 1(3):185–204
14. Weston P, Roberts C, Yeo G, Stewart E (2015) Perspectives on
railway track geometry condition monitoring from in-service
railway vehicles. Veh Syst Dyn 53(7):1063–1091
15. Nielsen JCO, Johansson A (2000) Out-of-round railway wheels-
a literature survey. Proc Inst Mech Eng F J Rail Rapid Transit
214(2):79–91
16. Nielsen JCO, Lunde´n R, Johansson A, Vernersson T (2003)
Train-track interaction and mechanisms of irregular wear on
wheel and rail surfaces. Veh Syst Dyn 40(1–3):3–54
17. Barke DW, Chiu WK (2005) A review of the effects of out-of-
round wheels on track and vehicle components. Proc Inst Mech
Eng F J Rail Rapid Transit 219(3):151–175
Neural Computing and Applications (2024) 36:16707–16725
16721
123

---

## Page 16
18. Tao G, Wen Z, Jin X, Yang X (2020) Polygonisation of railway
wheels: a critical review. Railway Eng Sci 28:317–345
19. Falamarzi A, Moridpour S, Nazem M (2019) A review of rail
track
degradation
prediction
models.
Aust
J
Civ
Eng
17(2):152–166
20. Ni YQ and Zhang QH (2018) A Bayesian machine learning
approach for online wheel condition detection using track-side
monitoring. In: 2018 International Conference on Intelligent
Rail Transportation (ICIRT), IEEE, pp 1–6
21. Gao X, Wang Z, Peng C, Zhang Y (2011) Research on auto-
matic defect localization for ultrasonic normal probe detection
on railway wheel. In: Seventh international symposium on
precision engineering measurements and instrumentation, SPIE,
pp 747–755
22. Kwon SJ, Seo JW, Lee DH, You WJ (2011) ‘‘Detection of sub-
surface crack in railway wheel using a new sensing system.
Nondestru Charact Comp Mater Aerospace Eng Civ Infrastru
Homeland Security SPIE 2011:909–913
23. Bollas K, Papasalouros D, Kourousis D, Anastasopoulos A
(2013) Acoustic emission monitoring of wheel sets on moving
trains. Constr Build Mater 48:1266–1272
24. Yang K, Ma L, Gao X, Wang L (2012) Proﬁle parameters of
wheelset detection for high speed freight train. In: Fourth
International Conference on Digital Image Processing (ICDIP
2012), SPIE, pp 382–387
25. Jia S, Dhanasekar M (2007) Detection of rail wheel ﬂats using
wavelet approaches. Struct Health Monit 6(2):121–131
26. Guedes A et al (2023) Detection of wheel polygonization based
on wayside monitoring and artiﬁcial intelligence. Sensors
23(4):2188
27. Chen S, Wang K, Zhou Z, Yang Y, Chen Z, Zhai W (2022)
Quantitative detection of locomotive wheel polygonization
under
non-stationary
conditions
by
adaptive
chirp
mode
decomposition. Railway Eng Sci 30(2):129–147
28. Shan W, Wu P, Wu X, Zhang F, Shi H (2019) Effect of wheel
polygonization on the axle box vibrating and bolt self-loosening
of high-speed trains. In: Journal of Physics: Conference Series,
IOP Publishing, p 052044
29. Gonc¸alves V, Mosleh A, Vale C, Montenegro PA (2023) Wheel
out-of-roundness detection using an envelope spectrum analysis.
Sensors 23(4):2138
30. Mosleh A, Montenegro P, Alves Costa P, Calc¸ada R (2021) An
approach for wheel ﬂat detection of railway train wheels using
envelope
spectrum
analysis.
Struct
Infrastru
Eng
17(12):1710–1729.
https://doi.org/10.1080/15732479.2020.
1832536
31. Mosleh A, Montenegro PA, Costa PA, Calc¸ada R (2021) Rail-
way vehicle wheel ﬂat detection with multiple records using
spectral kurtosis analysis. Appl Sci 11(9):4002
32. Mosleh A, Meixedo A, Ribeiro D, Montenegro P, Calc¸ada R
(2022) Early wheel ﬂat detection: an automatic data-driven
wavelet-based approach for railways. Vehicle Syst Dyn. https://
doi.org/10.1080/00423114.2022.2103436
33. Braga JAP, Andrade AR (2021) Multivariate statistical aggre-
gation and dimensionality reduction techniques to improve
monitoring and maintenance in railways: the wheelset compo-
nent. Reliab Eng Syst Saf 216:107932
34. Vrignat P, Avila M, Duculty F, Kratz F (2015) Failure event
prediction using hidden markov model approaches. IEEE Trans
Reliab 64(3):1038–1048
35. Lourenc¸o A et al (2023) Adaptive time series representation for
out-of-round railway wheels fault diagnosis in wayside moni-
toring. Eng Fail Anal. https://doi.org/10.1016/j.engfailanal.2023.
107433
36. Fumeo E, Oneto L, Anguita D (2015) Condition based mainte-
nance in railway transportation systems based on big data
streaming analysis. Procedia Comput Sci 53:437–446
37. Jayaswal P, Verma SN, Wadhwani AK (2011) Development of
EBP-Artiﬁcial neural network expert system for rolling element
bearing fault diagnosis. J Vib Control 17(8):1131–1148
38. Kamlu S, Laxmi V (2019) Condition-based maintenance strat-
egy for vehicles using hidden Markov models. Adv Mech Eng
11(1):1687814018806380
39. Sadeghi J, Askarinejad H (2010) Development of improved
railway
track
degradation
models.
Struct
Infrastruct
Eng
6(6):675–688
40. Guler H (2014) Prediction of railway track geometry deterio-
ration using artiﬁcial neural networks: a case study for Turkish
state railways. Struct Infrastruct Eng 10(5):614–626
41. Bai L, Liu R, Sun Q, Wang F, Xu P (2015) Markov-based model
for the prediction of railway track irregularities. Proc Inst Mech
Eng F J Rail Rapid Transit 229(2):150–159
42. Lam HF, Yang JH, Hu Q, Ng CT (2018) Railway ballast damage
detection
by Markov chain Monte Carlo-based
Bayesian
method. Struct Health Monit 17(3):706–724
43. Falamarzi A, Moridpour S, Nazem M (2019) Development of a
tram track degradation prediction model based on the acceler-
ation data. Struct Infrastruct Eng 15(10):1308–1318
44. Schalk R, Vicencio AN, Zoeteman A, Wolfert R (2017) Data
analytics for the of RCF damages on the Dutch high speed line.
In: Proceedings of the 1st International Conference on Rail
Transportation, Chengdu, China, pp 10–12
45. Li Q, Peng Q, Liu R, Liu L, Bai L (2019) Track grid health
index for grid-based, data-driven railway track health evalua-
tion. Adv Mech Eng 11(11):1687814019889768
46. Ca´rdenas-Gallo I, Sarmiento CA, Morales GA, Bolivar MA,
Akhavan-Tabatabaei R (2017) An ensemble classiﬁer to predict
track geometry degradation. Reliab Eng Syst Saf 161:53–60
47. Lasisi A, Attoh-Okine N (2019) Machine learning ensembles
and rail defects prediction: multilayer stacking methodology.
ASCE
ASME
J
Risk
Uncertain
Eng
Syst
A
Civ
Eng
5(4):04019016
48. Sharma S, Cui Y, He Q, Mohammadi R, Li Z (2018) Data-
driven optimization of railway maintenance for track geometry.
Transp Res Part C Emerg Technol 90:34–58
49. Lee JS, Hwang SH, Choi IY, Choi Y (2020) Deterioration
prediction of track geometry using periodic measurement data
and incremental support vector regression model. J Transp Eng
A Syst 146(1):04019057
50. Molodova M, Li Z, Nu´n˜ez A, Dollevoet R (2014) Automatic
detection of squats in railway infrastructure. IEEE Trans Intell
Transp Syst 15(5):1980–1990
51. Tsunashima H (2019) Condition monitoring of railway tracks
from car-body vibration using a machine learning technique.
Appl Sci 9(13):2734
52. Lederman G, Chen S, Garrett J, Kovacˇevic´ J, Noh HY, Bielak J
(2017) Track-monitoring from the dynamic response of an
operational train. Mech Syst Signal Process 87:1–16
53. Falamarzi A, Moridpour S, Nazem M, Hesami R (2018) Rail
degradation prediction models for tram system: Melbourne case
study. J Adv Transp 2018:6340504
54. Falamarzi A, Moridpour S, Nazem M, Cheraghi S (2018)
Development of a random forests regression model to predict
track degradation index: Melbourne case study. In: Australian
transport research forum, p 12
55. Mercier S, Meier-Hirmer C, Roussignol M (2012) Bivariate
Gamma wear processes for track geometry modelling, with
application to intervention scheduling. Struct Infrastruct Eng
8(4):357–366
16722
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 17
56. Wei J, Liu C, Ren T, Liu H, Zhou W (2017) Online condition
monitoring of a rail fastening system on high-speed railways
based on wavelet packet analysis. Sensors 17(2):318
57. Sadeghi J, Askarinejad H (2012) Application of neural networks
in evaluation of railway track quality condition. J Mech Sci
Technol 26:113–122
58. Lasisi A, Attoh-Okine N (2018) Principal components analysis
and track quality index: a machine learning approach. Transp
Res Part C Emerg Technol 91:230–248
59. Gao S, Szugs T, Ahlbrink R (2018) Use of combined railway
inspection data sources for characterization of rolling contact
fatigue. In: 12th European Conference on Non-Destructive
Testing (ECNDT). Gothenburg
60. Jiang Y, Wang H, Tian G, Yi Q, Zhao J, Zhen K (2019) Fast
classiﬁcation for rail defect depths using a hybrid intelligent
method. Optik (Stuttg) 180:455–468
61. Jamshidi A et al (2016) Probabilistic defect-based risk assess-
ment approach for rail failures in railway infrastructure. IFAC-
PapersOnLine 49(3):73–77
62. Molodova M, Oregui M, Nu´n˜ez A, Li Z, Dollevoet R (2016)
Health condition monitoring of insulated joints based on axle
box acceleration measurements. Eng Struct 123:225–235
63. Oukhellou L, Come E, Bouillaut L, Aknin P (2008) Combined
use of sensor data and structural knowledge processed by
Bayesian network: Application to a railway diagnosis aid
scheme. Transp Res Part C Emerg Technol 16(6):755–767
64. Costa JN, Ambro´sio J, Frey D, Andrade AR (2022) A multi-
variate statistical representation of railway track irregularities
using ARMA models. Veh Syst Dyn 60(7):2494–2510
65. Arasteh khouy I, Larsson-Kra˚ik PO, Nissen A, Kumar U (2016)
Cost-effective track geometry maintenance limits. In: Proc Inst
Mech Eng F J Rail Rapid Transit, vol. 230, no. 2, pp 611–622
66. Khouy IA, Schunnesson H, Juntti U, Nissen A, Larsson-Kra˚ik
P-O (2014) Evaluation of track geometry maintenance for a
heavy haul railroad in Sweden: a case study. Proc Inst Mech Eng
F J Rail Rapid Transit 228(5):496–503
67. Khajehei H, Ahmadi A, Soleimanmeigouni I, Nissen A (2019)
Allocation of effective maintenance limit for railway track
geometry. Struct Infrastruct Eng 15(12):1597–1612
68. Sun Y, Liu Y, Yang C (2019) Railway joint detection using deep
convolutional neural networks. In: 2019 IEEE 15th International
Conference on Automation Science and Engineering (CASE),
IEEE, pp 235–240
69. Zhou F, Xia L, Dong W, Sun X, Yan X, Zhao Q (2016) Fault
diagnosis of high-speed railway turnout based on support vector
machine. In: 2016 IEEE International Conference on Industrial
Technology (ICIT), IEEE, pp 1539–1544
70. Huang S, Zhang F, Yu R, Chen W, Hu F, Dong D (2017)
Turnout fault diagnosis through dynamic time warping and
signal normalization. J Adv Transp 2017:3192967
71. Ahmad W, Khan SA, Islam MMM, Kim J-M (2019) A reliable
technique for remaining useful life estimation of rolling element
bearings using dynamic regression models. Reliab Eng Syst Saf
184:67–76. https://doi.org/10.1016/j.ress.2018.02.003
72. Chaolong J, Weixiang X, Futian W, Hanning W (2012) Track
irregularity time series analysis and trend forecasting. Discrete
Dyn Nat Soc 2012:38787
73. Trinh H, Haas N, Li Y, Otto C, Pankanti S (2012) Enhanced rail
component detection and consolidation for rail track inspection.
In: 2012 IEEE Workshop on the Applications of Computer
Vision (WACV), IEEE, pp 289–295
74. Xia Y, Xie F, Jiang Z (2010) Broken railway fastener detection
based on adaboost algorithm. In: 2010 international conference
on optoelectronics and image processing, IEEE, pp 313–316
75. Audley M, Andrews JD (2013) The effects of tamping on rail-
way track geometry degradation. Proc Inst Mech Eng F J Rail
Rapid Transit 227(4):376–391
76. Soleimanmeigouni I, Ahmadi A, Arasteh Khouy I, Letot C
(2018) Evaluation of the effect of tamping on the track geometry
condition: a case study. In: Proc Inst Mech Eng F J Rail Rapid
Transit, vol. 232, no. 2, pp 408–420
77. Lourenc¸o A, Fernandes M, Canito A, Almeida A, Marreiros G
(2022) Using an explainable machine learning approach to
minimize opportunistic maintenance interventions. In: Gonza´-
lez-Briones A, Almeida A, Fernandez A, El Bolock A, Dura˜es
D, Jorda´n J, Lopes F (eds) Highlights in practical applications of
agents, multi-agent systems, and complex systems simulation.
The PAAMS collection. Springer, Cham, pp 41–54
78. Nicolai RP, Dekker R (2008) Optimal maintenance of multi-
component systems: a review. In: Kobbacy KAH, Murthy DNP
(eds) Complex system maintenance handbook. Springer, Lon-
don, pp 263–286. https://doi.org/10.1007/978-1-84800-011-7_
11
79. Pargar F, Kauppila O, Kujala J (2017) Integrated scheduling of
preventive maintenance and renewal projects for multi-unit
systems with
grouping and
balancing.
Comput
Ind
Eng
110:43–58
80. Gustavsson E (2015) Scheduling tamping operations on railway
tracks using mixed integer linear programming. EURO J Trans
Logist 4(1):97–112
81. Caetano LF, Teixeira PF (2013) Availability approach to opti-
mizing
railway
track
renewal
operations.
J
Transp
Eng
139(9):941–948
82. Verbert K, De Schutter B, Babusˇka R (2017) Timely condition-
based maintenance planning for multi-component systems.
Reliab Eng Syst Saf 159:310–321
83. Palo M, Galar D, Nordmark T, Asplund M, Larsson D (2014)
Condition monitoring at the wheel/rail interface for decision-
making support. Proc Inst Mech Eng F J Rail Rapid Transit
228(6):705–715
84. Liang B, Iwnicki SD, Zhao Y, Crosbee D (2013) Railway
wheel-ﬂat and rail surface defect modelling and analysis by
time–frequency techniques. Veh Syst Dyn 51(9):1403–1421
85. Dwyer-Joyce RS, Yao C, Lewis R, Brunskill H (2013) An
ultrasonic sensor for monitoring wheel ﬂange/rail gauge corner
contact.
Proc
Inst
Mech
Eng
F
J
Rail
Rapid
Transit
227(2):188–195
86. Matsumoto A et al (2014) Actual states of wheel/rail contact
forces and friction on sharp curves–continuous monitoring from
in-service
trains
and
numerical
simulations.
Wear
314(1–2):189–197
87. Pan J, Li W, Dai X (2013) Train overload and unbalanced load
detection based on FBG gauge. In: Fourth Asia Paciﬁc Optical
Sensors Conference, SPIE, pp 347–350
88. Silva R et al (2023) Early identiﬁcation of unbalanced freight
trafﬁc loads based on wayside monitoring and artiﬁcial intelli-
gence. Sensors 23(3):1544
89. Mosleh A, Costa PA, Calc¸ada R (2020) A new strategy to
estimate static loads for the dynamic weighing in motion of
railway vehicles. Proc Inst Mech Eng F J Rail Rapid Transit
234(2):183–200
90. Pinta˜o B, Mosleh A, Vale C, Montenegro P, Costa P (2022)
Development and validation of a weigh-in-motion methodology
for railway tracks. Sensors 22(5):1976
91. Li H et al (2014) Improving rail network velocity: a machine
learning approach to predictive maintenance. Transp Res Part C
Emerg Technol 45:17–26
92. Filograno ML et al (2011) Real-time monitoring of railway
trafﬁc
using
ﬁber
Bragg
grating
sensors.
IEEE
Sens
J
12(1):85–92
Neural Computing and Applications (2024) 36:16707–16725
16723
123

---

## Page 18
93. Ma S, Gao L, Liu X, Lin J (2019) Deep learning for track quality
evaluation of high-speed railway based on vehicle-body vibra-
tion prediction. IEEE Access 7:185099–185107
94. Hu C and Liu X (2016) Modeling track geometry degradation
using support vector machine technique. In: ASME/IEEE Joint
Rail Conference, American Society of Mechanical Engineers, p
V001T01A011
95. Famurewa SM, Zhang L, Asplund M (2017) Maintenance ana-
lytics for railway infrastructure decision support. J Qual Maint
Eng 23(3):310–325
96. Rabatel J, Bringay S, Poncelet P (2011) Anomaly detection in
monitoring sensor data for preventive maintenance. Expert Syst
Appl 38(6):7003–7015
97. Li Z, He Q (2015) Prediction of railcar remaining useful life by
multiple data source fusion. IEEE Trans Intell Transp Syst
16(4):2226–2235
98. Bergmeir C, Sa´inz G, Martı´nez Bertrand C, Benı´tez JM (2013)
A study on the use of machine learning methods for incidence
prediction in high-speed train tracks. In: Recent Trends in
Applied Artiﬁcial Intelligence: 26th International Conference on
Industrial, Engineering and Other Applications of Applied
Intelligent Systems, IEA/AIE 2013, Amsterdam, The Nether-
lands, June 17–21, 2013. Proceedings 26, Springer, pp 674–683
99. Schenkendorf R, Dutschk B, Lu¨ddecke K, Groos JC (2016)
Improved Railway Track Irregularities Classiﬁcation by aModel
Inversion Approach. In: PHM Society European Conference
100. Yin J, Zhao W (2016) Fault diagnosis network design for
vehicle on-board equipments of high-speed railway: a deep
learning approach. Eng Appl Artif Intell 56:250–259
101. Sammouri W, Coˆme E, Oukhellou L, Aknin P, Fonlladosa CE
(2014) Pattern recognition approach for the prediction of
infrequent target events in ﬂoating train data sequences within a
predictive maintenance framework. In: 17th International IEEE
Conference on Intelligent Transportation Systems (ITSC), IEEE,
pp 918–923
102. Liang B, Iwnicki S, Ball A, Young AE (2015) Adaptive noise
cancelling and time–frequency techniques for rail surface defect
detection. Mech Syst Signal Process 54:41–51
103. Peng C et al. (2011) Automatic railway wheelset inspection
system by using ultrasonic technique. In: Seventh International
Symposium
on
Precision
Engineering
Measurements
and
Instrumentation, SPIE, pp 596–601
104. Andrade AR, Teixeira PF (2013) Hierarchical Bayesian mod-
elling of rail track geometry degradation. Proc Inst Mech Eng F
J Rail Rapid Transit 227(4):364–375
105. Li H, Qian B, Parikh D, Hampapur A (2013) Alarm prediction in
large-scale sensor networks—A case study in railroad. In: 2013
IEEE international conference on big data, IEEE, pp 7–14
106. Lai CC et al (2012) Development of a ﬁber-optic sensing system
for train vibration and train weight measurements in Hong
Kong. J Sens 2012:365165
107. Filograno ML, Corredera P, Rodriguez-Plaza M, Andres-
Alguacil A, Gonzalez-Herraez M (2013) Wheel ﬂat detection in
high-speed railway systems using ﬁber Bragg gratings. IEEE
Sens J 13(12):4808–4816
108. Brizuela J, Iban˜ez A, Nevado P, Fritsch C (2010) Railway
wheels ﬂat detector using Doppler effect. Phys Procedia
3(1):811–817
109. Brizuela J, Fritsch C, Iba´n˜ez A (2011) Railway wheel-ﬂat
detection and measurement by ultrasound. Transp Res Part C
Emerg Technol 19(6):975–984
110. Hu H, Tang B, Gong X, Wei W, Wang H (2017) Intelligent fault
diagnosis of the high-speed train with big data based on deep
neural networks. IEEE Trans Industr Inform 13(4):2106–2116.
https://doi.org/10.1109/TII.2017.2683528
111. Go´mez MJ, Corral E, Castejon C, Garcı´a-Prada JC (2018)
Effective crack detection in railway axles using vibration signals
and WPT energy. Sensors 18(5):1603
112. Luo H, Bo L, Peng C, Hou D (2020) Fault diagnosis for high-
speed train axle-box bearing using simpliﬁed shallow informa-
tion fusion convolutional neural network. Sensors 20(17):4930
113. Salvador P, Naranjo V, Insa R, Teixeira P (2016) Axlebox
accelerations: their acquisition and time–frequency characteri-
sation for railway track monitoring purposes. Measurement
82:301–312
114. Karimpour M, Hitihamillage L, Elkhoury N, Moridpour S,
Hesami R (2018) Fuzzy approach in rail track degradation
prediction. J Adv Transp 2018:3096190
115. Quiroga L and Schnieder E (2010) Modelling high speed rail-
road geometry ageing as a discrete-continuous process. In:
Proceedings of the stochastic modeling techniques and data
analysis
international
conference,
SMTDA,
Chania
Crete
Greece
116. Amini A, Entezami M, Huang Z, Rowshandel H, Papaelias M
(2016) Wayside detection of faults in railway axle bearings
using time spectral kurtosis analysis on high-frequency acoustic
emission signals. Adv Mech Eng 8(11):1687814016676000
117. Thakkar NA, Steel JA, Reuben RL (2012) Rail–wheel contact
stress assessment using acoustic emission: a laboratory study of
the effects of wheel ﬂats. Proc Inst Mech Eng F J Rail Rapid
Transit 226(1):3–13
118. Wang Q-A, Ni Y-Q (2019) Measurement and forecasting of
high-speed rail track slab deformation under uncertain SHM
data using variational heteroscedastic gaussian process. Sensors
19(15):3311
119. Gerum PCL, Altay A, Baykal-Gu¨rsoy M (2019) Data-driven
predictive maintenance scheduling policies for railways. Transp
Res Part C Emerg Technol 107:137–154
120. Lee JS, Hwang SH, Choi IY, Kim IK (2018) Prediction of track
deterioration using maintenance data and machine learning
schemes. J Transp Eng A Syst 144(9):04018045
121. Kang S, Sristi S, Karachiwala J, Hu YC (2018) Detection of
anomaly in train speed for intelligent railway systems. In: 2018
International Conference on Control, Automation and Diagnosis
(ICCAD), IEEE, pp 1–6
122. Al-Douri YK, Tretten P, Karim R (2016) Improvement of rail-
way performance: a study of Swedish railway infrastructure.
J Modern Trans 24:22–37
123. Meixedo A, Santos J, Ribeiro D, Calc¸ada R, Todd MD (2022)
Online unsupervised detection of structural changes using train–
induced
dynamic
responses.
Mech
Syst
Signal
Process
165:108268
124. Mosleh A, Meixedo A, Ribeiro D, Montenegro P, Calc¸ada R
(2022) Automatic clustering-based approach for train wheels
condition monitoring. Int J Rail Trans 11:1–26
125. Vileiniskis M, Remenyte-Prescott R, Rama D (2016) A fault
detection method for railway point systems. Proc Inst Mech Eng
F J Rail Rapid Transit 230(3):852–865
126. Meixedo A, Santos J, Ribeiro D, Calc¸ada R, Todd M (2021)
Damage detection in railway bridges using trafﬁc-induced
dynamic responses. Eng Struct 238:112189
127. Kim H, Sa J, Chung Y, Park D, Yoon S (2016) Fault diagnosis
of railway point machines using dynamic time warping. Electron
Lett 52(10):818–819
128. Mosleh A, Meixedo A, Ribeiro D, Montenegro P, Calc¸ada R
(2022) Automatic clustering-based approach for train wheels
condition monitoring. Int J Rail Trans. https://doi.org/10.1080/
23248378.2022.2096132
129. Du H et al. (2019) Dynamic Time Warping and Spectral Clus-
tering Based Fault Detection and Diagnosis of Railway Point
16724
Neural Computing and Applications (2024) 36:16707–16725
123

---

## Page 19
Machines. In: 2019 IEEE Intelligent Transportation Systems
Conference (ITSC), IEEE, pp 595–600
130. Krummenacher G, Ong CS, Koller S, Kobayashi S, Buhmann
JM (2017) Wheel defect detection with machine learning. IEEE
Trans Intell Transp Syst 19(4):1176–1187
131. Alves V, Cury A, Roitman N, Magluta C, Cremona C (2015)
Novelty detection for SHM using raw acceleration measure-
ments. Struct Control Health Monit 22(9):1193–1207
132. Lourenc¸o A, Meira J, Marreiros G (2023) Online adaptive
learning for out-of-round railway wheels detection. In: Pro-
ceedings of ACM SAC Conference
133. Chen Z, Li Y, Xia T, Pan E (2019) Hidden Markov model with
auto-correlated observations for remaining useful life prediction
and
optimal
maintenance
policy.
Reliab
Eng
Syst
Saf
184:123–136
134. Nadarajah N, Shamdani A, Hardie G, Chiu WK, Widyastuti H
(2018) Prediction of railway vehicles’ dynamic behavior with
machine learning algorithms. Electron J Struct Eng 18(1):38–46
135. Esling P, Agon C (2012) Time-series data mining. ACM
Comput Surveys (CSUR) 45(1):1–34
136. Dukkipati RV, Dong R (1999) Impact loads due to wheel ﬂats
and shells. Veh Syst Dyn 31(1):1–22
137. Lourenc¸o A, Fernandes M, Marreiros G, Corchado JM (2022)
Using simulation to evaluate a concept drift detector for con-
dition based maintenance. In: IECON 2022–48th Annual Con-
ference of the IEEE Industrial Electronics Society, IEEE, pp 1–7
138. Bukhsh ZA, Saeed A, Stipanovic I, Doree AG (2019) Predictive
maintenance using tree-based classiﬁcation techniques: a case of
railway switches. Transp Res Part C Emerg Technol 101:35–54
139. Ghofrani F, He Q, Goverde RMP, Liu X (2018) Recent appli-
cations of big data analytics in railway transportation systems: a
survey. Transp Res Part C Emerg Technol 90:226–246
140. Lourenco A, Ferraz C, Meira J, Marreiros G, Bolo´n-Canedo V,
Alonso-Betanzos A (2023) Automated green machine learning
for
condition-based
maintenance.
https://doi.org/10.14428/
esann/2023.ES2023-85
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
Neural Computing and Applications (2024) 36:16707–16725
16725
123

---
