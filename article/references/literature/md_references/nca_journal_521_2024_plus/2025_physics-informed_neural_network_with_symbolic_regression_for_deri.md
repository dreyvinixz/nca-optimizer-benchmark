# Physics-informed neural network with symbolic regression for deriving analytical approximate solutions to nonlinear partial differential equations

**Year**: 2025 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-025-11450-9

---

## Page 1
ORIGINAL ARTICLE
Physics-informed neural network with symbolic
regression for deriving analytical approximate solutions
to nonlinear partial differential equations
Joy Das1 • Bivas Bhaumik2 • Soumen De1 • Satyasaran Changdar3
Received: 10 April 2025 / Accepted: 16 June 2025 / Published online: 6 July 2025
 The Author(s) 2025
Abstract
This work explores an interpretable approach based on physics-informed neural networks (PINNs) combined with
symbolic regression (SR) to determine mathematical expressions for the predicted solutions of nonlinear partial
differential equations that describe arterial blood ﬂow inﬂuenced by external magnetic ﬁelds. PINNs are excellent
at capturing the underlying physics, but can be computationally intensive and hard to interpret. The predictive
power of PINN has been combined with evolutionary symbolic regression using PySR, an open-source Python
module that employs genetic programming and customizable mathematical operators, including trigonometric,
exponential, and arithmetic functions. This hybrid approach enables the derivation of concise, transparent
mathematical expressions that closely replicate the behavior of these complex systems. This blend of PINNs and
symbolic regression helps us to better understand how pulsatile blood ﬂow and magnetic ﬁelds interact in the
viscoelastic arterial circulation. The comparison graphs of the SR model and the PINN-predicted data at different
time scales signify a better ﬁt for the discovered mathematical expressions with data. As illustrated by the low
mean squared error and statistical validation on residual losses, the symbolic expressions are extremely accurate
and quick enough for real-time execution. Additionally, the solutions provided by the PINN are validated
numerically to demonstrate the effectiveness of the proposed method. Our results demonstrate that combining
symbolic regression with PINNs provides practical and interpretable solutions in bioﬂuid mechanics, offering a
more transparent and reliable alternative to traditional methods.
Keywords Physics-informed neural network (PINN)  Symbolic regression (SR)  Interpretable machine learning 
Nonlinear partial differential equations (PDEs)  Magnetic bioﬂuid dynamics
1 Introduction
Arterial blood ﬂow in the cardiovascular system is a fundamental aspect of the human circulatory system, as it is
responsible for transporting oxygenated blood from the heart to various tissues and organs of the body [1]. The
heart circulates blood through a complex network of arterial tubes. Unlike inert tubes, the arteries react to
changing ﬂow and pressure circumstances by expanding or contracting to meet changing hemodynamic demands
[2]. Again, blood is considered a biomagnetic ﬂuid, as it contains hemoglobin molecules, which are generally
high concentrations of iron oxides present in red blood cells [3]. Therefore, when a magnetic ﬁeld is applied, the
ﬂowing nature of blood changes due to its magnetic properties [4]. One-dimensional (1D) models are used to
evaluate the effects of blood pressure and ﬂow rate on the arterial and venous walls in the biological circulation
Neural Computing and Applications (2025) 37:20205–20240
https://doi.org/10.1007/s00521-025-11450-9
123
Neural Computing and Applications (2025) 37:20205–20240

---

## Page 2
system [5]. The nonlinear wave dynamics of ﬂuid ﬂow through viscoelastic tubes necessitate particular attention,
as these tubes serve as analogs to major arteries in the human circulatory system. Understanding this dynamic
behavior is critical for comprehending the intricacies of ﬂuid dynamics in such systems [5]. Several cardio-
vascular diseases and hypertension occur in humans due to the improper ﬂow of blood in the arteries. One-
dimensional (1D) ﬂuid dynamical models predict ﬂow, area, and pressure without being nonlinear. The blood
ﬂow dynamical system has various damping components, including ﬂuid viscosity, wall viscoelasticity, and
vessel geometry variations [5, 6]. Thus, capturing pressure pulses and ﬂow rates of blood under the inﬂuence of a
magnetic ﬁeld, as well as characterizing the bending behavior of the vessel wall in arteries, is crucial to overcome
various cardiovascular problems. Analyzing this biomagnetic ﬂuid is beneﬁcial for the development of magnetic
devices for the treatment of malignant tumors, cell separation, and transporting drugs using magnetic particles
[3, 7]. Therefore, a mathematical model should account for mechanical interactions between blood, artery walls,
and tissues.
After advancing in computer technologies, deep learning algorithms have become more interesting and widely
used tools in many branches of applied mathematics and scientiﬁc problems [8]. Artiﬁcial neural network (ANN)
is a deep learning algorithm inspired by the human nervous system and is used for artiﬁcial intelligence and
machine learning [9]. This neural network is constructed with one input layer, one output layer, and several
hidden layers with various activation functions in the hidden layers. This method effectively solves various
complex mathematical problems with high efﬁciency. Before using the ANN for problem-solving, the proposed
neural network must be trained to learn the underlying patterns and relationships within the data by adjusting its
internal parameters, such as weights and biases, through an optimization technique [9]. New computational
procedures work as a motivation to ﬁnd different solutions to various mathematical equations. Some numerical
methods are used to solve partial differential equations (PDEs) through a discretization process. In recent years,
deep learning has become very popular among researchers to solve PDEs [10]. Physics-informed neural network
(PINN) is an emerging machine learning algorithm that effectively solves higher-order nonlinear PDEs with great
efﬁciency. PINNs incorporate the underlying physical laws directly into the training process of the neural
network, and this is achieved by embedding the PDEs into the loss function as additional regularization terms
[10, 11]. As a result, the network learns from the data perfectly and is also guided by the underlying physics,
which improves generalization and assures that the learnt solution is consistent with the known physical behavior
of the system. The capacity of PINN to solve PDE problems offers advantages such as continuous and differ-
entiable approximate solutions and reduced memory requirements. PINN has the beneﬁt of utilizing automated
differentiation methods through the Tensorﬂow and PyTorch libraries [10, 12]. This approach improves PINN
performance by estimating the initial and boundary conditions of the PDEs.
PDEs are essential for modeling intricate systems in various scientiﬁc and engineering disciplines, extending
beyond cardiovascular ﬂows. Addressing these nonlinear and frequently high-dimensional PDEs presents sig-
niﬁcant challenges, which have led to an increased use of neural network-based approaches. The signiﬁcance of
linear and nonlinear PDEs extends across many disciplines, including solid mechanics, ﬂuid dynamics, nonlinear
optics, plasma physics, and the fuzziness concept in pattern classiﬁcation [13–15]. These equations encapsulate
complex physical phenomena such as turbulence, dispersion, and reaction–diffusion processes. Moreover, PINNs
have been successfully applied in diverse areas such as natural language processing, computer vision, stock
market modeling, and several other domains [16, 17]. PINNs offer beneﬁts such as solutions that are free from
mesh constraints, continuous differentiability, and the straightforward incorporation of physical laws, making
them effective tools for addressing PDEs in multiple contexts [10, 11]. These advancements highlight the broad
applicability of partial differential equations (PDEs) and underscore the growing importance of machine learning-
based analytical approaches in discovering interpretable solutions throughout scientiﬁc disciplines.
Nowadays, PINNs have emerged as the leading machine learning approach to predict the solutions of high-
dimensional PDEs accurately. PINNs are typically viewed as black-box solvers due to their difﬁculties in
interpreting neural solutions, which is a signiﬁcant restriction [18, 19]. The interpretability of a machine learning
model is determined by its ability to trace the logical or mathematical linkages between input and output.
123
Neural Computing and Applications (2025) 37:20205–20240
20206
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 3
Furthermore, optimal machine learning models are interpretable when expressed as mathematical formulations.
Symbolic regression (SR) is a fast-growing discipline of machine learning that uses trained datasets to create
symbolic mathematical formulae [20, 21]. The learning process for the SR model is complex as it requires several
mathematical operations and constant values to represent data effectively. Genetic programming approaches are
commonly employed to accomplish this [20]. Limited research has been conducted on interpreting physics-
informed neural networks using a symbolic regression approach [21]. Deep neural networks, or PINNs, can solve
PDEs in natural sciences like physics. This enables SR models to obtain mathematical formulas for approximate
analytical solutions. SR models may be constructed directly from projected solutions using physics-informed
neural networks, changing ‘‘black-box‘‘ models into more interpretable ‘‘white box’’ models. The mathematical
expressions of the solutions of the PDEs can be impactful in identifying the ﬂowing behavior as well as
characteristics of the motion of the blood in human arteries and making suitable medical devices accordingly to
diagnose several cardiovascular diseases.
The main aspect of this work is to create a hybrid framework that combines machine learning with genetic
programming to use symbolic regression in predicting the analytical solution of the ﬁfth-order evolutionary
equation and forced Burgers’ equation, which is derived from a one-dimensional (1D) arterial blood ﬂow model
by using the reductive perturbation technique. The use of symbolic regression in ﬁnding an approximate ana-
lytical form of the solution of a ﬁfth-order partial differential equation is present in [21]. In this aspect, we have
explored the detailed mechanism of how symbolic regression uses genetic programming to effectively identify the
mathematical forms of the solutions, combined with interpretable data of the PINN model. The method may be
used to look at the important aspects of the nonlinear elasticity and viscoelastic characteristics of tube walls, as
well as their bending nature. Our analysis uses the ﬁfth-order nonlinear evolution equation, which is an extension
of the Kawahara equation, to analyze the bending dynamics of the viscoelastic tube wall. This study examines the
use of PINNs and the symbolic regression technique to solve a nonlinear evolutionary equation with ﬁfth-order
dispersion under pressure waves. Moreover, validation entails comparing expected solutions to residuals of the
partial differential equation to conclude the full inquiry.
2 Fundamental formulations describing arterial blood flow
Arterial blood circulation is frequently represented through partial differential equations that illustrate the
dynamic interactions between blood, regarded as a non-Newtonian, biomagnetic ﬂuid, and the ﬂexible arterial
walls [22]. These equations are formulated from the conservation laws pertaining to mass and momentum, and
they have been further enhanced to reﬂect the impacts of viscoelasticity and external forces like magnetic ﬁelds.
The resulting system often includes nonlinear and higher-order dispersive terms that describe wave propagation,
damping effects, and elasticity of the arterial walls.
To better represent the incompressible ﬂow of ﬂuid in an axially symmetric viscoelastic artery, the continuity
and axial momentum equations are formulated as follows:
2.1 Equation of continuity
For incompressible ﬂuids like blood [23], the continuity equation conveys the principle of mass conservation.
o mx
ox þ 1
r
oðrmrÞ
or
¼ 0
ð1Þ
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20207

---

## Page 4
2.2 Equation of momentum
The axial component of Navier’s Stokes equations determines the ﬂuid ﬂow properties within an axially sym-
metric artery tube [5, 24]. Here, the Lorentz force J  B works as an external body force in the momentum
equation due to the presence of a small magnetic ﬁeld effect (BðB0; 0; 0Þ), normal to the blood ﬂow. The current
density J is given by Ohm’s law under the assumption of negligible electric ﬁeld and low magnetic Reynolds
number and is given by
J ¼ rðm  BÞ
ð2Þ
Here, r is the electrical conductivity of the ﬂuid and m represents the ﬂuid velocity vector.
2.2.1 Axial component
o mx
ot þ mr
o mx
or þ mx
o mx
ox þ 1
q
o P
ox ¼ l0 o2 mx
or2 þ 1
r
o mx
or þ o2 mx
ox2


 rB2
0 mx
ð3Þ
Here, the components of the ﬂow velocity in the axial and radial directions are denoted by mx and mr, respectively.
The ﬂuid’s kinematic viscosity is represented by l0, and its density by q. The pressure ﬁeld within the ﬂuid,
P ¼ Pðx; tÞ, is considered to vary with both spatial position and time.
We now use the following non-dimensional variables in the equations above to reduce them to one-dimen-
sional form:
r ¼ R0
0r0;
x ¼ k0x0;
t ¼ k0
V0
0
t0
mx ¼ V0
0m0
x
mr ¼ U0
0m0
r;
P ¼ qV0
0
2P0:
ð4Þ
Also note that
~x ¼ R0
0
k0 ¼ U0
0
V0
0
ð5Þ
where ~x is a small parameter. Thus, using the above dimensionless variables and the condition V0
0R0
0
U0
0k0 Eq. (1) takes
the following form
oðr0m0
rÞ
or0
þ oðr0m0
xÞ
ox
¼ 0
ð6Þ
Now, using the above dimensionless variables and dividing Eq. (3) by V0
0
2, multiplying it by r0k0, neglecting the
term of order ~x2, and thus using Eq. (5), we get the following form of the momentum equation:
o
ot r0m0
x


þ o
or0 r0m0
rm0
x


þ o
ox ðr0m0
x
2Þ þ o
ox r0P0
ð
Þ ¼
m0k
V0
0R0
0
2
o
or0
r0 om0
x
or0




 k0
0
V0
0
rB2
0r0m0
x
ð7Þ
The power generalization velocity proﬁle is expressed as follows [25, 26]:
123
Neural Computing and Applications (2025) 37:20205–20240
20208
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 5
m0
xðr0; x; tÞ ¼ c þ 2
c
1 
r0
~R
0

c


~V
0ðx; tÞ;
~V
0ðx; tÞ ¼ 2
~R
02
Z R0ðx;tÞ
0
mðr0; x; tÞr0dr0
ð8Þ
and
a ¼
1
~R
02 ~
U
02
Z R0
0
2m02
x r0dr0
ð9Þ
Here, ~R
0 ¼ ~R
0ðx; tÞ denotes the instantaneous radius of the arterial tube, while c characterizes the sharpness of the
axial velocity proﬁle. The parameter a serves as a correction factor, and the term mx refers to how the axial
velocity component varies along the radial direction, whereas the average velocity across the cross section is
given by ~V
0ðx; tÞ.
To derive the averaged quantities, we integrate both the continuity and momentum equations over the radial
domain, speciﬁcally from r0 ¼ 0 to r0 ¼ ~R
0. In doing so, we apply the streamline boundary condition, which
assumes that the ﬂuid velocity remains tangential along the wall surface, as
mr0
½
r0¼ ~R
0¼ o ~R
0
ox m0
x
 	
r0¼ ~R
0þ o ~R
0
ot
ð10Þ
Now, integrating continuity Eq. (1) and using the streamline condition, we obtain the averaged continuity
equation as
o
ot
~R
02 þ o
ox
~R
02 ~V
0


¼ 0
ð11Þ
Similarly, integrating Eq. (3) and using Eqs. (6) and (7), and also utilizing the streamline condition, we get the
averaged momentum equation as
o
ot
~R
02 ~V
0


þ o
ox a ~R
02 ~V
02


þ ~R
02 oP0
ox ¼ 2m0k0 ~R
0
V0
0 ~R
2
0
om0
x
or0


r0¼ ~R
0 k0rB2
0
2V0
0
~V
0 ~R
02
ð12Þ
Utilizing the velocity proﬁle in Eq. (8) and introducing A ¼ p ~R
02, the one-dimensional form of the averaged
equations, which deﬁne the cross section, is expressed as
2.2.2 Equation of Fluid mass in one-dimensional form
o
ot
~R
02 þ o
ox
~R
02 ~V
0


¼ 0
ð13Þ
2.2.3 Momentum Equation in one-dimensional form
o ~V
0
ot þ ~V
0 o ~V
0
ox þ oP0
ox ¼ 2 c þ 2
ð
Þ m0k0 ~V
0
V0
0R02
0A  krB2
0
2V0
0
~V
0
ð14Þ
In this case, the arterial tube’s cross-sectional area is A(x, t). When A is substituted, Eq. (13) becomes
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20209

---

## Page 6
~R
0
t þ ~V
0 ~R
0
x þ 0:5 ~R
0 ~V
0 ¼ 0:
ð15Þ
To account for miniature tube wall disruptions, the function ~fðx; tÞ is deﬁned as follows:
~R
0ðx; tÞ ¼ R þ ~fðx; tÞ;
R ¼ equilibrium radius
kfk\\ R:
ð16Þ
Therefore, Eq. (15) is simpliﬁed as follows:
ft þ 0:5 RV0
x þ 0:5fV0
x þ V0fx ¼ 0:
ð17Þ
To resolve the system comprising two equations with three unknowns, as indicated in Eqs. (13) and (14), it is
necessary to establish an extra relationship that guides the motion of the tube wall with the viscoelastic property.
In this analysis, we assume a uniform arterial wall where both the deformation of the wall and its thickness are
negligible compared to the tube radius. The wall strain is considered to be a function of the tube radius, and the
equilibrium radius is assumed to be signiﬁcantly smaller than the wavelength of the propagating wave phe-
nomena. Additionally, we assume that the ﬂuid pressure remains uniform across the cross-sectional area of the
tube, varying only as a function of spatial coordinates and time [27].
Now, we can determine the equation for radial motion in a viscoelastic tube. As stated by Giusti and Mainardi
[28], the inner pressure, represented by Pðx; tÞ, and the wall radius, which is denoted by fðx; tÞ of the tube, satisfy
the following relationship:
P  P0 ¼ qh0ftt  kh0fxx  vh0ftxx þ Kfxxxx þ lft þ jh0
R
f þ j2h0
R2 f
2:
ð18Þ
where
j2  j1 R  2j;
h0 is the wall thickness in its stable condition, P0 is the constant pressure on the tube’s outer surface, and qv is the
volume density of the tubes. While v represents the viscosity coefﬁcient of the tube material, l is the propor-
tionality coefﬁcient that connects the resistance of the medium to the motion of the viscoelastic wall. Further-
more, K represents the proportionality coefﬁcient, and the linear and nonlinear elasticity coefﬁcients of the tube
are denoted by j and j1, respectively. For large Reynolds numbers, we focus on studying nonlinear waves with
deep learning approaches utilizing the long-wave approximation. With these assumptions, Eq. (14) simpliﬁes to:
~V
0
t þ ~V
0 ~V
0
x þ P0
x ¼  krB2
0
2V0
0
~V
0:
ð19Þ
As a result, Eqs. (17), (18), and (19) together depict a ﬂuid low model in one dimension (1D) inside a viscoelastic
tube. Additionally, these equations depict the blood ﬂow system in the arteries of the human body.
Using the dimensionless variables in Eqs. (17), (18), and (19) along with the dimensionless variable
~f ¼
~R
2 f0;
V0 ¼
ﬃﬃﬃﬃﬃﬃﬃ
jh0
2q
s
The following form (without the primes) represents the system of ﬂow equations in dimensionless variables:
123
Neural Computing and Applications (2025) 37:20205–20240
20210
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 7
2.3 Non-dimensional flow equations
ft þ ~Vx þ 1
2 f ~Vx þ ~Vfx ¼ 0
~Vt þ ~V ~Vx þ Px ¼ M ~V
P ¼ cftt  bfxx þ kft  dftxx þ v1fxxxx þ af þ a1f2 þ a2P0:
ð20Þ
Where, a ¼ jh0
2qV2
0
¼ 1;
b ¼
kh0 ~R
2k2qV2
0
;
c ¼ h0 ~R
2k2
d ¼
vh0
2k3qV0
;
k ¼
l ~R
2kqV0
;
a1 ¼ j2h0
4qV2
0
;
v1 ¼
K ~R
2k4qV2
0
;
a2 ¼
1
qV2
0
;
M ¼ krB2
0
2V0
ð21Þ
Nonlinear evolutionary equations for describing the blood ﬂow in a viscoelastic tube can be obtained by the use
of the perturbation technique. The reductive perturbation approach [29, 30] may be used to build approximation
solutions for system Eq. (20). Once the direction of wave propagation has been determined, it makes sense to use
‘‘slow‘‘ time variables to investigate the development of the perturbations since pressure waves (also known as
pulse waves) have a signiﬁcantly greater characteristic velocity as compared to ﬂow velocities. The following
variables can be used in the following step to determine the solution to the system of equations (20):
f ¼ xpf0;
m ¼ xpm0;
P ¼ 1 þ xpP0;
M ¼ xpþ1M0
p 2 N
n ¼ xmðx  tÞ;
s ¼ xnt;
m; n 2 Q;
n [ m
ð22Þ
o
ox ¼ xm o
on ;
o
ot ¼ xn o
os  xm o
on
ð23Þ
By applying the relations given in Eqs. (22) and (23), we can derive a corresponding system of PDEs (i.e.,
Eqs. (24) and (25)) by choosing appropriate values for the indices n, m, p, and q and comparing the powers of x
in the perturbation method. These choices help simplify the general form of the equations and lead to a more
speciﬁc, solvable structure. A detailed and rigorous derivation of these governing equations can be found in the
works of [21], where the authors systematically develop the theoretical framework. Additionally, the magnetic
ﬁeld inﬂuence (the parameter M) can be seamlessly incorporated into the system using the perturbation technique.
This approach allows for the controlled introduction of M as a small parameter, enabling the analysis of its effects
on the overall dynamics of the system without drastically altering the core structure of the equations.
vt þ vvx ¼ 1
2 vxx þ M
2 v;
ð24Þ
vt þ vvx þ 1
2 vxxx þ 1
2 vxxxxx ¼ M
2 v
ð25Þ
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20211

---

## Page 8
3 An advanced deep learning framework designed to effectively address nonlinear
wave equations
In this section, we introduce an advanced technique of machine learning algorithms, speciﬁcally deep neural
networks, for solving nonlinear PDEs. Current research uses a variety of frameworks, including recurrent neural
networks, physics-guided neural networks (PgNNs), and PINNs, to comprehend the physics in scientiﬁc com-
puting [21, 31, 32]. However, we prefer to use deep neural networks to solve nonlinear evolutionary equations to
study wave dynamics. For most PDEs, this method is more suitable and easier to train. A deep neural network is a
basic feed-forward neural network and may be thought of mathematically as a composition of functions with a
very high approximation capacity [33]. Generally referred to as the input layer, output layer, and different hidden
layers, a network architecture is constructed with three separate levels in the ﬁeld of deep learning.
Let us consider a function Ukðx; tÞ : R2 ! Rdsol to perfectly deﬁne the network architecture with inputs (x, t).
Here the neural network consists of ðk  1Þ hidden layers, with Ni neurons present in each hidden layer
ð1  i  k; Nk ¼ dsolÞ, for making the connection between input and output layer as well as transmitting the
outputs from previously hidden layer to next input hidden layer. As explained in [31], we disclose the results from
every hidden layer based on the type of deep neural network model:
Uiðx; tÞ ¼ ract WT
i Ui1ðx; tÞ þ bi


2 RNi
for 1  i  k  1:
Here, weight matrix is represented by WT
i 2 Rkiki1, bias vector is symbolizes as bi 2 RNi, and ract represents the
nonlinear activation function in each hidden layers. In deep learning aspects, a speciﬁc choice of activation
function is very important for better predicting performance. Nonlinear activation functions such as ract are more
capable of learning complicated functions with induced nonlinearity of the network. The ﬁnal layer is then
deﬁned as follows, after we use a linear activation function in the output layer.
Ukðx; tÞ ¼ WT
k Uk1ðxÞ þ bl 2 Rdout:
Regression tasks that seek to predict continuous variables frequently use a linear activation function in the output
layer. By convention, the model chooses the linear activation function if the activation function is not speciﬁed in
the output layer.
3.1 Configuring the problem using the PINN approach
Let us consider a general form of Partial Differential Equations with independent variables x and t, indicated as:
F  vt þ Gv x; t; vx; vxx; vxxx; vxxxx; vxxxxx. . .
ð
Þ ¼ 0;
x 2 S;
t 2 ð0; ~TÞ;
where
ð26Þ
S symbolize the spatial domain and (0, ~T) is the temporal domain subject to a well-deﬁned Dirichlet boundary
condition:
Bðv; x; tÞ ¼ 0
on oS:
ð27Þ
In the above expression, Bðv; x; tÞ denotes the speciﬁed boundary conditions (such as Dirichlet, Neumann, or
Periodic), Gv portrays the function with induced nonlinearity, and v symbolizes the solution of the partial
differential equations speciﬁed in this study. In this aspect, the two-dimensional rectangular domain is denoted by
S  ð0; ~TÞ, and oS represents the boundary points in the rectangular spatio-temporal domain.
123
Neural Computing and Applications (2025) 37:20205–20240
20212
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 9
To offer extra clariﬁcation, various partial derivatives concerning v up to higher order with nonlinear terms are
concluded in the function Gv, whereas the fulﬁllment of partial derivatives as well as the solution v at boundary
points is controlled with the governed boundary constraint Bðv; x; tÞ.
The main concept of the physics-informed neural network [34] is to utilize the deep neural network architecture
to predict the solution as ~vh 	 v. Here, h symbolizes the combination of model parameters that are updated during
the training of the neural network model. This PINN architecture is intended to fulﬁll partial differential equations
naturally using boundary conditions while ensuring that all provided constraints are met.
vðx; tÞ 	 ~vhðx; tÞ ¼ N N L x; t; No; NB; NC; h
ð
Þ:
ð28Þ
Here, No ¼
xi; ti; Iðvðxi; tiÞÞ
ð
ÞPo
i¼1
n
o
represents the Po training distributed samples during the initial phase at t = 0
of the training, NB ¼
xi; ti; Bðvðxi; tiÞÞ
ð
ÞPb
i¼1
n
o
symbolizes training samples of Pb on the boundary oS, and
NC ¼
xi; ti; F ~vðxi; tiÞ
ð
Þ
ð
ÞPc
i¼1
n
o
is a set of Pc randomly assigned training points within S that imposes PDE
physics on the neural network model. Also, h ¼
WT
i ; bi

l1
i¼1 deﬁnes network weights and biases of the neural
network.
The PINN technique integrates losses from the PDE (26) and boundary conditions (27) to restrict the neural
network solution ~v. The total loss function Ltotal modiﬁes the parameters of the neural network h by assessing the
weighted total of the residuals’ L2 norms for both the PDE and the boundary conditions.
In the PINN framework, the physical constraints that are derived from the governing PDEs, which include
conservation laws such as mass and momentum conservation, are embedded directly into the loss function. In our
case, this is implemented by using the DeepXDE [35] library in Python with TensorFlow as the backend, where a
custom PDE residual function is deﬁned to represent the differential operators and the terms that capture the
underlying physics. The solution is estimated using a neural network, and all required derivatives, such as spatial
and temporal derivatives, are calculated via automatic differentiation by using TensorFlow. This approach
Fig. 1 Schematic diagram of PINN, highlighting automatic differentiation of PDE implementation and predicting the
solutions with loss function
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20213

---

## Page 10
automatically traces the computational graph to calculate derivatives of any order, providing more accuracy and
stability than standard numerical differentiation methods, especially for complicated PDEs with higher-order
components. The total loss function is composed of multiple components:
Ltotal h; NC; No; NB
ð
Þ ¼ l1Lphy h; NC
ð
Þ þ l2Lini h; No
ð
Þ þ l3Lbound h; NB
ð
Þ;
ð29Þ
where
Lphy h; NC
ð
Þ ¼ 1
Pc
X
j
~vt þ Gv xi; ti; ~vx; ~vxx; ~vxxx; . . .
ð
Þ
k
k2
2;
Lini h; No
ð
Þ ¼ 1
Po
X
j
kI ~vðxi; tiÞ; xi; ti
ð
Þk2
2;
Lbound h; NB
ð
Þ ¼ 1
Pb
X
j
kB ~vðxi; tiÞ; xi; ti
ð
Þk2
2
Here, l1, l2, and l3 are the network hyperparameters that are used to customize the network weights. Optimizing
hyperparameter values improves the equilibrium of partial losses during training. The total loss function Ltotal of
the neural network is deﬁned as the linear combination of three different losses, i.e., Lphy h; NC
ð
Þ, Lini h; No
ð
Þ,
and Lbound h; NB
ð
Þ. The primary residual loss Ltotal h; NC
ð
Þ requires the neural network to follow the physics of
the provided PDE, whereas the neural network parameters are optimized with the help of loss terms Lini h; No
ð
Þ
and Lbound h; NB
ð
Þ by assuring the fulﬁllment of the initial and boundary conditions of the PDEs. Proper
hyperparameter selection is critical for minimizing the total loss function when training the model. It improves
both accuracy and efﬁciency in predicting the intended result of a certain challenge. Furthermore, the residual loss
term provides insight into how effectively the neural network model performs inside its domain and its ability to
anticipate actual outputs.
4 Genetic programming based on evolutionary algorithm
Evolutionary algorithms (EAs) are a type of optimization algorithm inﬂuenced by natural selection and evolution
[36]. It integrates machine learning techniques to enhance convergence speed as well as optimization performance
with great efﬁciency. The machine learning model extracts patterns from data to guide search tactics, whereas
evolutionary algorithms efﬁciently explore diverse solution spaces with recognition of different patterns.
Nowadays, EAs have become very popular in computational algorithms as it is commonly utilized in solving
various complex scenarios due to their capacity to replicate natural evolution and execute population-based
random searches [37, 38]. Moreover, evolutionary algorithms are stochastic search methods that imitate natural
evolution. It cannot guarantee that optimality may be achieved while dealing with complex real-time problems,
but population based yields an estimated optimum solution suitable for many application contexts [38]. EAs
generally use several techniques that include selection, evolution, and iterative population updates to explore and
develop optimization solutions [36]. Figure 2 demonstrates different operations of the evolutionary algorithm
from initialization to optimal solutions.
123
Neural Computing and Applications (2025) 37:20205–20240
20214
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 11
4.1 Genetic algorithm
Genetic algorithms (GAs) represent a category of evolutionary algorithms (EAs) that emulate the principles of the
natural selection process to address optimization and search challenges [39]. This is a population-based search
algorithm inspired by the biological progression of living organisms. New populations are generated through the
repeated application of genetic operators on the individuals within the existing population. The essential com-
ponents of GAs include chromosome representation, selection, crossover, mutation, and the calculation of the
ﬁtness function [39, 40]. A chromosome comprises a set of values that fully deﬁnes a potential solution
throughout the optimization procedure. The selection process involves identifying elite individuals from the
current population to serve as parents for the next generation. Fitness values are utilized as the criteria to
determine which individuals qualify as elite [37]. The crossover operator generates two new offspring by
selecting and duplicating speciﬁc bits from each of the two parent strings, and mutation in genetic programming
acts as an evolutionary operator that introduces diversity among the population of potential solutions [39, 40].
The ﬁtness function evaluates the quality of the solutions produced in genetic algorithms and is modeled as a part
of the overall optimization technique. It serves as an objective metric and guides the evolutionary search process
by choosing the most successful individuals for reproduction in succeeding generations [38, 39]. Furthermore, the
ﬁtness function plays an important role in assigning the numerical scores to each solution based on its perfor-
mance. A higher ﬁtness value increases the probability of individuals being selected for crossover and mutation.
Therefore, genetic algorithms are more suitable and less expensive in predicting the desired relationships that best
ﬁt the data in computational methods. Moreover, this technique is highly adaptive to their environment and very
helpful in ﬁnding the behavioral patterns of complex, noisy data of real-world problems.
4.2 Symbolic regression
In recent years, neural networks (NNs) have become a very emerging tool in machine learning algorithms to solve
many complex mathematical as well as real-world problems. PINNs are one kind of deep learning architecture
that has gained popularity among researchers to predict the solutions of many complex nonlinear PDEs. While it
is highly effective, a major limitation of PINNs is their difﬁculty in interpretation, which often leads to their
perception as black-box solvers. In the ﬁeld of machine learning-based predictions, symbolic regression (SR) has
Fig. 2 Evolutionary cycle of a standard evolutionary algorithm. Each block represents an operation on a set of possible
solutions
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20215

---

## Page 12
captured the interest of numerous researchers because it effectively ﬁnds analytical formulations for complicated
systems of PDEs [21]. In this study, we have also used this methodology to acquire mathematical expressions for
predicted solutions of our complex evolutionary PDEs.
SR is a genetic programming (GP) approach based on evolutionary algorithms in modern machine learning
techniques. Figure 3 illustrates the relationship between SR and GP, and the broader family of evolutionary
algorithms (EAs). As the diagram shows, both SR and GP represent relatively small, specialized subsets within
the expansive landscape of evolutionary algorithms. When PINN algorithms are applied to a dataset and predict
some solutions, this SR model is used to discover the analytical expressions that best ﬁt the experimental as well
as predicted data with high proﬁciency. The mathematical expressions of predicted performance can be viewed as
a tree structure [18]. In this tree-based structure, the terminal node signiﬁes the variables and constants, whereas
the intermediate cells symbolize several mathematical operations that include addition, multiplication, subtrac-
tion, and division. Symbolic regression uses these fundamental mathematical operations, as well as basis func-
tions like exponential and trigonometric functions, to identify underlying correlations [20]. A SR model is built
by combining operators and coefﬁcients in different ways, creating endless possibilities to explore [41]. The
mathematical operator domain is bounded by a ﬁnite number of operations and a maximum model complexity
criterion. Finding the right model requires an efﬁcient search. In this context, genetic programming is an effective
technique for symbolic regression to ﬁnd the search space. Genetic algorithms evolve models by continuously
improving them based on how well they perform according to a given ﬁtness function. This ﬁtness function helps
to pick the models that are most likely to perform well. Thereafter, the models evolve by mixing parts from
different models (i.e., crossover) and making small random changes (i.e., mutation) to create new candidate
Fig. 4 In genetic program-
ming, different populations
evolve independently on
separate islands, and after a
set number of generations,
individuals migrate
between islands to share
improvements
Fig. 3 Three main compo-
nents of evolutionary com-
puting—symbolic regres-
sion (SR), genetic
programming (GP), and
evolutionary algorithms
(EAs)
123
Neural Computing and Applications (2025) 37:20205–20240
20216
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 13
models [20, 40]. At the same time, natural selection removes candidates with the lowest ﬁtness from the
population. The use of iterative approaches to explore the solution space is determined by a mix of randomness
and precise processes for ﬁtness evaluation, crossover, and mutation.
The ﬁtness function typically measures the discrepancy between experimental results and model forecasts and
frequently utilizes absolute or squared error metrics. Additionally, the minimum squared error in the ﬁtness
function indicates a superior alignment of the expressions with the experimental data. Figure 5 represents a
ﬂowchart of symbolic regression based on a genetic algorithm, highlighting the steps of population selection,
replication, and merging of a new population, and outcome evaluation. Let us consider a mathematical
expression, gðxÞ ¼ cosð2:1xÞ þ 6e20x. This can be viewed as a tree structure, where the ‘‘?’’ operator acts as a
root of the tree, whereas cos(2.1x) and 6e20x represent two branches of the tree. With a deﬁned collection of
basis functions and operators, we can conceptualize randomly generated functions as computational programs
that produce predictions for a target variable. These programs incorporate unspeciﬁed parameters, including
coefﬁcients, that are modiﬁed throughout the optimization process. The effectiveness of each function is assessed
through its ‘‘ﬁtness,‘‘ which is generally quantiﬁed by calculating the sum of squared differences between the
predicted values and the actual data points. Mutation and crossover are two essential operations that are employed
for reﬁning the functions in the optimization process. From Fig. 6, we can see the tree structure of the mutation
operation in the genetic algorithm. In Fig. 6, we observe a symbolic mutation where the original mathematical
expression, written as 3:25x  0:92, undergoes a subtle yet meaningful transformation. Speciﬁcally, the
Fig. 5 A ﬂowchart of the
symbolic regression algo-
rithm shows how it
explores and evolves equa-
tions to uncover the best-
ﬁtting, interpretable rela-
tionships hidden within the
data
Fig. 6 Highlighting muta-
tion operation that modiﬁes
portions of a mathematical
expression in a genetic
algorithm to investigate
novel solutions and
enhance overall
performance
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20217

---

## Page 14
subtraction operator is replaced with an addition operator, resulting in the expression 3:25x þ 0:92. This mutation
illustrates how even a minor symbolic change in the structure of a symbolic equation can lead to a completely
different interpretation or behavior in the model’s output. The crossover operation combines components of two
parent functions to form a new function, and it is generally known as ‘‘offspring.’’ In Fig. 7, we can observe a
clear example of crossover mutation taking place between two parent functions as part of the symbolic regression
process. The original parent functions involved are g1ðxÞ ¼ 3:25x  0:92 a linear expression, and g2ðyÞ ¼ yy, a
nonlinear self-exponential function. During the crossover event, portions of each parent’s expression are
recombined to generate two new offspring functions. The ﬁrst resulting function, g3ðyÞ ¼ y  0:92, emerges by
combining the structure of g2ðyÞ with the constant term from g1ðxÞ. The second offspring, g4ðx; yÞ ¼ ð3:25xÞy,
blends the linear coefﬁcient from g1ðxÞ with the exponential structure of g2ðyÞ, producing a new function that now
depends on both variables. This example highlights how crossover mutations can introduce novel and potentially
more expressive symbolic forms by recombining building blocks from existing expressions.
Therefore, this study introduces a hybrid methodology that integrates PINNs with genetic programming to
obtain analytical solutions for nonlinear PDEs. The predicted solutions from the PINN have been utilized as input
data for symbolic regression within the GP framework. PINNs present the advantage of resolving PDEs without
the need for substantial labeled datasets, as they embed the physical laws directly into the loss function during the
training phase. On the contrary, genetic programming is proﬁcient in revealing symbolic relationships in data,
producing expressions that are understandable and interpretable by humans. This strategy leverages the analytical
clarity of genetic programming alongside the data efﬁciency and ﬂexibility of PINN by integrating these two
techniques. This approach enhances both the precision and applicability of PDE solutions while offering insights
into the fundamental dynamics of the system via concise analytical representations. This makes it especially
beneﬁcial for theoretical examination, model veriﬁcation, and additional scientiﬁc interpretation.
Fig. 7 Crossover mutation in genetic programming swaps parts of two parent programs to create new, potentially better-
performing offspring solutions
123
Neural Computing and Applications (2025) 37:20205–20240
20218
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 15
5 Overview of nonlinear partial differential equations (PDEs)
5.1 Governing PDEs
In this work, we have derived some nonlinear PDEs that arise in the modeling of arterial blood ﬂow. These
equations are highly complex and play a signiﬁcant role in the study of blood ﬂow dynamics in arteries, where
dispersion effects and nonlinear wave interactions critically inﬂuence blood ﬂow propagation. In Eq. (24), the
nonlinear convection term vvx illustrates the mechanism of how blood ﬂow propels itself throughout the large
arteries. Additionally, the term 1
2 vxx represents a diffusion component and accounts for the viscous effects in the
blood ﬂow dynamics. Furthermore, Eq. (25) is a ﬁfth-order evolutionary equation and can be said a higher-order
extension of Eq. (24), including third-order (vxxx) and ﬁfth-order (vxxxxx) dissipative terms. These higher-order
partial derivative terms help to account for the wave dispersion effect as well as enhance stability and regulate
wave steepening, therefore assisting in the characterization of arterial pulse wave propagation over long distances.
Again, in both the equations (i.e., Eqs. (24) & (25)), M
2 v refers to the external forcing term, generally related to
arterial external pressure or wall elasticity.
The discovered symbolic expressions of the solutions of nonlinear PDEs in this study show patterns that align
with well-known hemodynamic behaviors, including nonlinear advection, diffusion, and higher-order dispersive
effects. Coefﬁcients tied to ﬁrst and second order derivatives often relate to aspects like ﬂow velocity and viscous
dissipation, while higher-order terms appear to reﬂect the elasticity of vessel walls and the propagation of pressure
waves. Nonlinear interactions such as vvx suggest convective acceleration, which is commonly observed in
pulsatile blood ﬂow. Connecting these terms and parameters with physical quantities such as viscosity, vessel
compliance, and pressure gradients can help bridge the gap between data-driven discoveries and physiological
understanding. Relating these coefﬁcients to parameters found in classical models or observed experimentally
could enhance our understanding of their physiological signiﬁcance.
5.2 Importance of analytical solution
Analytical solutions of nonlinear PDEs play a fundamental role in understanding the characteristics and behavior
of the equations. Nonlinear PDEs are frequently difﬁcult to solve accurately, but when analytical solutions are
accessible, they offer some major beneﬁts. It has a deep insight into physical behavior. Analytical solutions
produce accurate expressions for the dependent variables that help to understand the qualitative behavior, such as
wave formation, propagation, or dissipation of the system. It identiﬁes important phenomena, including shock
production, soliton dynamics, and wave breaking. Moreover, analytical solutions of nonlinear PDEs reduce
computational costs by quickly evaluating the various values of the parameters without executing complicated
simulations. This is commonly useful in sensitivity analysis, control, and optimization problems.
Furthermore, mathematical formulations of the solution help to increase mathematical understanding by
highlighting the symmetry aspects of PDEs and classifying them based on their solution types and solvability. It
has a major impact on machine learning models, as analytical expressions are used to guide or train the data-
driven machine learning models. Therefore, the analytical solutions of the PDEs in arterial blood ﬂow modeling
are critical in understanding the behavioral pattern of the waves and validating numerical simulations. It plays a
crucial role in a variety of medical applications that include identifying illnesses in the arterial system and
managing blood pressure pulses with medical devices to improve therapy.
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20219

---

## Page 16
6 Results and discussions
This section provides a concise result of our research in identifying the solutions of nonlinear PDEs. A PINN
model architecture was employed, and its predicted outputs were used to derive approximate analytical solutions
through a symbolic regression model. Additionally, the PINN model’s performance was evaluated during training
across various values of the magnetic parameter M. Furthermore, a comprehensive sensitivity analysis of the SR
model’s hyperparameters was performed to understand how different parameter settings inﬂuence the accuracy
and robustness of the obtained analytical solutions.
Fig. 8 Visualization of train loss and test loss over epochs for forced Burger’s equation with four different M values. Here, x-
axis represents the number of epochs (or, steps), and y-axis represents the loss values during the training of the model for
various values of M: a loss curve for M ¼ 0:2, b loss curve for M ¼ 0:4, c loss curve for M ¼ 5 d loss curve for M ¼ 10
123
Neural Computing and Applications (2025) 37:20205–20240
20220
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 17
6.1 Physics-informed neural network (PINN)-based predictions and analysis of the results
In this work, physics-informed neural network (PINN), a machine learning algorithm, has been used to ﬁnd the
predicted solution of forced Burgers’ equation (Eq. 24) and ﬁfth-order evolutionary equation (Eq. 25). Various
conﬁgurations of hidden layers and neurons were empirically tested to identify a structure that provided a good
balance between accuracy and training stability. Although no formal optimization strategy was used, the chosen
Table 1 PINN hyperpa-
rameters and performance
results for the forced
Burgers’ equation at vary-
ing M, showing the impact
of different values of M on
training conﬁguration and
accuracy
PINN hyperparameters for forced Burgers’ equation
Parameter
M ¼ 0:2
M ¼ 0:4
M ¼ 5
M ¼ 10
Learning rate
1e–3
1e–3
1e–3
1e–3
Optimizer
Adam
Adam
Adam
Adam
Hidden layers
5
5
5
5
Neurons per layer
30
30
30
30
Activation function
sin
sin
sin
sin
Training epochs
14,000
16,000
17,500
20,000
Performance metrics:
Training loss
1:79  104
1:79  104
3:61  104
4:11  104
Test Loss
1:78  104
1:78  104
3:29  104
4:09  104
Fig. 9 Illustration showcases the solutions of the forced Burgers’ equation across different time scales, clearly demonstrating
how well the PINN model satisﬁes the boundary conditions for a range of values of the parameter M
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20221

---

## Page 18
architecture aligns with standard practices and was adequate for the complexity of the problem. To solve Eq. (24)
for different values of M, the deep neural network was created with 5 hidden layers and 30 neurons in each layer.
In this instance, the sine activation function was selected to update the network weights during the back
propagation. Following the initial setup, the model was trained across various numbers of iterations and a range of
M values to explore how different conﬁgurations would inﬂuence its performance and convergence behavior. We
set the initial pulse wave as vðx; 0Þ ¼ sinðpxÞ and boundary condition as vð2; tÞ ¼ vð2; tÞ ¼ 0, where x varies
from 2 to 2, and t ranges from 0 to 1. The PINN model was trained using 2500 points within the domain, and
1500 additional points were used to evaluate the model’s performance. Additionally, 700 and 600 data points
were assigned to enforce the boundary and initial conditions, respectively, during the training process. It is crucial
to ensure that the boundary conditions are satisﬁed with high accuracy when training a PINN model, especially
because any signiﬁcant residual loss at the boundaries can lead to inaccuracy or physically inconsistent solutions.
Paying careful attention to these constraints helps maintain the integrity of the model and reinforces its ability to
learn solutions that truly reﬂect the underlying physics. Sometimes, PINN models provide good residual losses
without satisfying the proper boundary conditions, but this leads to inappropriate predictions of the results. From
Fig. 8, throughout the training process, we observed a clear and consistent decrease in the value of the loss
function over successive iterations. This steady decline is a strong indication that the model is effectively learning
from the data, gradually minimizing its error and improving its performance as training progresses.
The parameter M in Eq. (24) has a major impact on achieving the low residual losses in its domain. Lower M
values do not need an excessive number of epochs (or iterations) during the training of the model, whereas higher
M values need a large number of iterations to successfully train the PINN model. Figure 8a shows that the PINN
model was trained for 15,000 iterations to minimize the loss during the training process for the equation with
M ¼ 0:2. Again, from Fig. 8b, it is clear that 16000 epochs were needed to achieve the train loss and test loss as
Fig. 10 Image illustrates the spatial distribution of residual losses across the rectangular domain for the forced Burgers’
equation, highlighting how these losses vary under different values of the parameter M
123
Neural Computing and Applications (2025) 37:20205–20240
20222
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 19
1:79  104 and 1:78  104, respectively, for M ¼ 0:4. Similarly, it is evident from Fig. 8c and d that for the M
values of 5 and 10, iterations of 17,000 and 20,000 were selected, respectively, to achieve low loss values. In that
large value of M, the train loss and test loss were 3:61  104, 3:29  104 and 4:11  104, 4:09  104,
respectively, with the same model conﬁgurations. The training and testing losses corresponding to various PINN
conﬁgurations are systematically presented in Table 1, highlighting the performance across different values of
M. Again, it can be noticed in Table 1 that for large values of M with an increased number of epochs, the train
losses and test losses have slightly greater values than lower M values. These results represent low loss values
across the domain. To achieve similarly lower loss values with higher values of M, it is necessary to increase the
number of training iterations or to adjust network parameters such as the learning rate, number of hidden layers,
and the number of neurons per layer accordingly. Figure 9a–d illustrates the solution curves at different time
scales and demonstrate how well the boundary conditions are satisﬁed by using the PINN model for different
values of the parameter M.
From Fig. 10a–d, the rectangular regions of residual losses can be visualized to assess the model’s performance
across the respective domain. As it is seen from these plots, the maximum residual loss value for M ¼ 0:2,
M ¼ 0:4, M ¼ 5, and M ¼ 10 are 0.04, 0.06, 0.06, and 0.03, respectively, and these values are signiﬁcantly low.
Again, we have calculated the mean residual error of these models. We have got the mean residual errors as
0.003, 0.005, 0.006, and 0.01 for respective PINN models with speciﬁc M values as indicated earlier. These
minimum mean residual errors signify that the PINN models have performed well with high accuracy and better
precision.
Fig. 11 Visualization of PINN solution and symbolic regression solution of forced Burgers’ equation for different M values:
a PINN prediction for M ¼ 0:2, b symbolic solution for M ¼ 0:2, c PINN prediction for M ¼ 0:4, d symbolic Solution for
M ¼ 0:4
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20223

---

## Page 20
6.2 Analytical solution by using symbolic regression for forced Burgers’ equation
Symbolic regression has emerged as a powerful and intuitive approach for discovering compact, inter-
pretable expressions that approximate the solutions of partial differential equations. It provides a data-driven
substitute for conventional numerical techniques by directly learning mathematical connections from data and
enables researchers to ﬁnd beautiful formulations that might otherwise remain undetected and obtain a deeper
understanding of the underlying physics. We apply PySR [42], a Python and Julia module for scientiﬁc symbolic
regression, to discover the best-ﬁtting expressions of PINN-based solutions. This technique was performed after
utilizing the PINN model. Here, the raw data of x and t with predicted values of the PINN model have been used
to ﬁnd the best-ﬁtting curve of the predicted solutions with varying M parameters. In the symbolic regression
model, the iteration was set to 27, whereas the population size was 30. Again, the batch size was set to 264 to
enhance the training as well as the convergence speed. In the PySR model, binary operators such as addition,
multiplication, subtraction, and division were used, whereas exponential, cosine, and sine functions were
Fig. 12 Comparison of PINN-based prediction and symbolic regression solutions of forced Burgers’ equation for different
time scales with distinct small M values: a solution comparison for M ¼ 0:2, b solution comparison for M ¼ 0:4
123
Neural Computing and Applications (2025) 37:20205–20240
20224
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 21
considered for unary operators. The selected functions were chosen to accurately represent the anticipated
physical or analytical characteristics of the solution, while ensuring adequate expressiveness to capture nonlinear
dynamics. The inclusion of binary operators facilitates the formulation of algebraic expressions composed of two
operands. When the SR model is trained, it provides the best mathematical expressions that describe the rela-
tionship between the predicted data and input features such as x and t. The identiﬁed equation brings a prediction
error or Mean Squared Error (MSE) loss term with a speciﬁc complexity value. A lower MSE loss value means
the mathematical expression is a good ﬁt with the provided data, and complexity deﬁnes how many binary and
functional operations have been used in that analytical expression.
Two-dimensional (2D) plots from Figs. 11a–d help to visualize the symbolic regression performances with the
PINN solution throughout the domain. Moreover, from these plots, it is evident that solutions of the symbolic
regression model encapsulate the exact characteristics of PINN predictions. Again, from Fig. 12a and b, it is
evident that symbolic regression effectively ﬁts the predicted data generated by the PINN model. After per-
forming the SR model, the symbolic solution for M ¼ 0:2 is obtained as:
vðx; tÞ ¼ et 3:76
ð
Þ sin
x
0:322


0:321
ð
Þ
1
0:797
ð
Þ t  0:560 þ 0:411
ð
Þ
ð30Þ
Here, the mean absolute error between the PINN and the SR solution is 0.008, which is a signiﬁcantly lower value
Fig. 13 Visualization of the solutions obtained from the PINN and symbolic regression for the forced Burgers’ equation
across various values of M: a PINN prediction at M ¼ 5, b symbolic solution at M ¼ 5, c PINN prediction at M ¼ 10, d
symbolic solution at M ¼ 10
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20225

---

## Page 22
and performs very well in ﬁnding the best-ﬁtting curve. For the mathematical expression (Eq. 30), the SR model
Fig. 14 A comparison of predictions derived from PINN and symbolic regression methods for the forced Burgers’ equation
across various time scales with distinct large values of M: a comparison of solutions for M ¼ 5, b comparison of solutions
for M ¼ 10
Table 2 Quantitative com-
parison of performance
metrics for different values
of M in the context of the
forced Burgers’ equation
Loss metrics for forced-Burgers’ equation
Loss type
M ¼ 0:2
M ¼ 0:4
M ¼ 5
M ¼ 10
Mean residual loss
0.003
0.005
0.006
0.01
MSE loss of symbolic regression
0.0002
0.00005
0.0002
0.00005
Mean absolute error between PINN and SR model
0.008
0.005
0.01
0.006
Complexity of discovered equation
19
25
22
17
The metrics include the mean residual loss of the PINN model, the MSE loss of the symbolic regression
output, the mean absolute error between the PINN and symbolic regression predictions, and the complexity of
the discovered symbolic expressions
123
Neural Computing and Applications (2025) 37:20205–20240
20226
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 23
yields an MSE loss of 0.0002 with a corresponding complexity of 19. This small loss value indicates the best-
ﬁtting relationships with the data. Again, for the value of M ¼ 0:4, the mathematical expression that is found by
the SR model is expressed as:
vðx; tÞ ¼ cos tð Þ sin x  3:14 þ cos
x þ 0:0892 þ 2:43
ð
Þ3:09
ð
Þ 0:158
ð
Þ
ð
Þ 0:957
ð
Þ
1
et4:50
ð31Þ
For this discovered equation, the mean absolute error between the PINN and SR solutions is 0.005. This small
error value indicates a highly accurate and reliable mapping between the input and output data. It demonstrates
that the SR model has captured the underlying relationship exceptionally well, reﬂecting both precision and
robustness in its performance. Furthermore, the derived analytical expression achieves a notably low MSE of
0.00005, which highlights excellent alignment with the reference data. With a symbolic complexity of 25, the
model also retains a manageable level of interpretability, balancing accuracy with simplicity.
Furthermore, for the value of M ¼ 5, the number of iterations was set to 28 with a population size of 30, and
the batch size was the same as for small M values (i.e., M ¼ 0:2 and M ¼ 0:4). But, for the value of M ¼ 10, the
iteration was 25. It is visible from Fig. 13a–d that the larger M values have a signiﬁcant effect on the solution of
Eq. (24). The SR model has successfully discovered the analytical expressions for these large values of M.
Sometimes, the population size and number of iterations need to be adjusted accordingly to obtain the optimal
mathematical expressions that most suit the given data in the SR model.
Figure 14a and b compares the solution graphs for different time scales with larger M values. The predicted
solution of the SR model has very minimal deviation from PINN-predicted values, offering an accurately ﬁtted
relationship between the input and output data. The mathematical solution that the SR model has found for M ¼ 5
is expressed as:
vðx; tÞ ¼
0:776 sin
x
0:315


et2:55 cos sin t  0:474  cos x 1:49
ð
Þ
ð
Þ
ð
Þ
ð
Þ
ð32Þ
In this case, the mean absolute error (MAE) between the PINN solution and the symbolic regression expression is
remarkably low, which is just 0.01. This indicates a very close agreement between the two methods. Furthermore,
the MSE loss associated with Eq. (32) is only 0.0002, and the corresponding expression complexity is 22. Again,
for M ¼ 10 in Eq. (24), the SR model has also predicted the analytical formulation with high precision. The
mathematical expression that the SR model has found for M ¼ 10 is identiﬁed as:
Fig. 15 Demonstrating the residual losses of ﬁfth-order evolutionary PDE in a rectangular domain with varying parameter of
M
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20227

---

## Page 24
vðx; tÞ ¼
t  0:0619  cos
x
0:318


0:166  0:919


sin
x
0:318


ð33Þ
For this equation, the mean absolute error between the PINN model prediction and the SR solution is 0.006. For
Eq. (33), the MSE loss and complexity that we have achieved are 0.00005 and 17, respectively. This low MSE
loss conﬁrms that the discovered equation provides an excellent ﬁt to the given data. A systematic summary of
key performance indicators, including the mean residual loss, mean squared error, mean absolute error, and the
complexity of the discovered equation, based on the predictions of the PINN model, is presented in Table 2. This
table provides insight into how these metrics vary with different values of M, offering a comprehensive evaluation
of the model’s predictive accuracy and the interpretability of the resulting symbolic expressions.
Thus, the SR framework shows a strong capability in accurately capturing the underlying analytical form of
Eq. (24), as demonstrated by the thorough analysis of the two-dimensional results and the associated MSE losses.
This consistently high performance across a range of M values reﬂects the robustness and adaptability of the SR
model in recovering physically meaningful expressions under varying dynamic conditions.
6.3 Symbolic regression solution for fifth-order evolutionary equation
Fifth-order partial differential equations are very challenging to solve due to the presence of nonlinearity and
high-dimensional mathematical complexities. These PDEs are often hard to capture by using conventional
numerical methods because these equations often contain complex boundary interactions within their respective
Fig. 16 Visualization of PINN-predicted solution and symbolic regression solution for ﬁfth-order evolutionary equation with
different M values
123
Neural Computing and Applications (2025) 37:20205–20240
20228
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 25
domains. In this context, PINNs have shown tremendous efﬁcacy by making use of the fundamental physics that
are included in the PDE. PINNs are capable of predicting highly accurate solutions in such scenarios where
conventional numerical methods struggle. Maintaining physical consistency and generalization ability makes the
PINNs a powerful tool to tackle such high-dimensional PDEs with nonlinear terms. In this case, the process of
determining the solution to the PDEs was approached as a forward problem, which means that the governing
equations and initial or boundary conditions are assumed to be known, and the goal was to compute the
corresponding physical response of the system. The PINN architecture was set with 5 hidden layers and 30
neurons in each layer. For this instance, sine activation function was employed to update the network weights and
biases during backpropagation in the PINN model, using a learning rate of 0.001. To solve Eq. (25), we have used
two distinct small values of the parameter M and utilized the symbolic regression technique for individual
predictions. The PINN model was trained for 20,000 for two different values of M. Figure 15a, b depicts the
Fig. 17 A comparison of the ﬁfth-order evolutionary equation estimates made using the PINN and symbolic regression
approaches over a range of time scales with different values of M. Solutions for M ¼ 0:2 and M ¼ 0:4 are compared in
(a) and (b), respectively
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20229

---

## Page 26
residual loss distribution throughout the domain. It is visible from the ﬁgures that the residual losses have
signiﬁcantly lower values for two different parametric values of M. The mean residual loss for M ¼ 0:2 became
0.006, and for the value of M ¼ 0:4, the mean residual loss was 0.0007. These losses signify that our PINN
models have achieved excellent results with great efﬁciency.
Following the training of our PINN model, the mathematical formulations of a ﬁfth-order evolutionary
equation with two different parameters of M were found using the SR model. For Eq. (25) with M ¼ 0:2, the
number of iterations was set to 34, whereas 30 was selected as the population size in the SR model with a batch
size of 264. Similarly, for the value of M ¼ 0:4 in Eq. (25), 40 iterations were selected with a population size of
30. Here, 201 evenly distributed points in x and t domains were utilized to ﬁnd the symbolic regression solutions
with the help of PINN-predicted values. Figure 16a–d presents a set of two-dimensional (2D) visualizations that
highlight both the predictions that are generated by the PINN model and the outcomes of the symbolic regression
analysis. These graphs are based on the projected solutions obtained from our neural network model and serve to
illustrate how effectively the model captures the underlying dynamics of the system through both numerical
approximation and interpretable symbolic expressions. A little but discernible difference between the outcomes of
the PINN and symbolic regression may be seen in the two-dimensional graphs. This little variance raises the
possibility that the symbolic regression model may have provided a more accurate or comprehensible depiction of
the outcome in some areas of the domain by better capturing the underlying relationships within the provided
information.
Figure 17a, b illustrates a detailed graphical comparison that showcases how effectively our SR model
identiﬁes precise and interpretable mathematical expressions that closely approximate the underlying dynamics
governed by the ﬁfth-order partial differential equation (i.e., Eq. 25). The ﬁgures reveal that the SR model
captures the solution behavior with remarkable ﬁdelity, demonstrating only minimal deviation from the actual
model predictions. In particular, for the case where the magnetic parameter is set to M ¼ 0:2, the analytical
expression derived by the SR model exhibits a strong agreement with the reference data. This demonstrates the
resilience of the symbolic regression approach and ﬁnds its capacity to provide physically signiﬁcant equations
that adhere to the system’s governing physics. In this case, the SR model found the following resultant
expression:
vðx; tÞ ¼ ðcosð0:0656  xÞ þ 0:414Þ  1:70 sinðsinð0:0760Þx þ t
 cosð0:177  xÞðx  0:0541Þ  0:176Þ
ð34Þ
For Eq. (34), the mean absolute error between the PINN predictions and the symbolic regression solution is
impressively low, which is only 0.02. Again, the MSE loss associated with this equation is only 0.0008, which
indicates a very tight ﬁt between the PINN-predicted and symbolic expressions. The resulting symbolic
expression has a complexity score of 27 that reﬂects a relatively concise yet expressive mathematical form. The
combination of a low MAE and a small MSE loss demonstrates that the symbolic model attains both smooth
convergence and high predictive accuracy, reﬂecting a well-ﬁtted and physically consistent representation. This
Table 3 Summary of performance metrics for different M values in the ﬁfth-order evolutionary equation, covering PINN
residual loss, symbolic regression MSE, mean absolute error, and expression complexity
Loss metrics for ﬁfth-order evolutionary equation
Loss type
M ¼ 0:2
M ¼ 0:4
Mean residual loss
0.006
0.0007
MSE loss of symbolic regression
0.0008
0.0009
Mean absolute error between PINN and SR model
0.02
0.02
Complexity of discovered equation
27
23
123
Neural Computing and Applications (2025) 37:20205–20240
20230
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 27
further indicates that the model successfully captures the underlying dynamics encoded by the PINN. Again, for
M ¼ 0:4 in Eq. (25), the mathematical expression by the SR model is provided as:
vðx; tÞ ¼ cosðx  2:33Þðx  0:352Þð0:0687Þ þ cosðx  0:799  0:0383Þ
sinðsinðtÞÞ  2:27
ð35Þ
The accuracy of the SR model is evaluated by comparing its solution with the PINN prediction. The mean
absolute error between the PINN solution and symbolic regression prediction for Eq. (35) is found to be 0.02,
which is the same as for the equation with M ¼ 0:02. To further evaluate how effectively the symbolic regression
(SR) model captures the underlying relationship between the input variables and the predicted outputs, both the
predictive accuracy and the structural complexity of the resulting expression were examined. The model achieved
Fig. 18 3D plots of PINN-based predictions and SR solution, derived from obtained mathematical expressions, highlighting
the model performances in achieving solution structures
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20231

---

## Page 28
a remarkably low MSE loss of just 0.0009, indicating a high level of agreement between the predicted and true
values. Additionally, the complexity of the evolved expression was measured at 23, which is quantiﬁed by the
total number of mathematical terms involved, reﬂecting a relatively compact yet expressive formulation of the
learned relationship. This minimum MSE value, as well as Fig. 17, helps to understand the excellent performance
in identifying the accurate and interpretable mathematical expressions with a given dataset in approximating the
PDE solutions using the symbolic regression machine learning algorithm. Table 3 presents a detailed evaluation
of losses of the PINN model’s performance in solving the ﬁfth-order evolutionary equation across different values
of M. The table includes major indicators such as the mean residual loss, mean squared error from symbolic
regression, the mean absolute error between the PINN and symbolic regression outputs, and the complexity of the
derived symbolic expressions. Together, these metrics offer a comprehensive understanding of both the predictive
accuracy of the model and the interpretability of the equations it discovers. Consequently, this approach yields
accurate and suitable outcomes with very minimal errors. Some 3D plots of analytical solutions that have been
derived from the SR model with input data (i.e., x and t) are visualized in Fig. 18a–d. These plots demonstrate the
well-ﬁtted structure with PINN solution data in its domain.
The combined physics-informed neural network and symbolic regression (PINN-SR) framework offers a
powerful approach for deriving interpretable mathematical expressions from complex data. However, this
enhanced capability comes with increased computational demands. Training the PINN requires substantial time
and computational resources, especially for complex nonlinear higher-order PDEs on large datasets. Additionally,
the symbolic regression component examines several mathematical expressions to identify the best ﬁt with PINN
predictive data, which can be very challenging and time-consuming. Strategies such as data preprocessing, early
Table 4 Comprehensive sensitivity analysis of the SR model over 27 evolutionary iterations to discover an accurate
approximate equation for the solution of the forced Burgers’ equation, evaluating how population size affects model
accuracy, expression complexity, and runtime, and identifying balanced trade-offs between accuracy and simplicity
Symbolic regression—model sensitivity analysis
Population size
MSE
Complexity
Runtime (s)
MAE
12
0.0021
24
13.60
0.03
18
0.00045
11
25.56
0.0107
22
0.00045
9
28.60
0.011
26
0.00007
29
38.03
0.005
30
0.00007
18
39.08
0.005
35
0.00042
24
41.64
0.011
40
0.00009
21
59.00
0.005
43
0.00008
18
70.00
0.006
Fig. 19 Histogram of residual losses on test dataset for different seed values for creating diverse training and testing datasets
123
Neural Computing and Applications (2025) 37:20205–20240
20232
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 29
stopping, and parallel computing can help mitigate the computational costs and improve accuracy. A more
detailed discussion of several challenges and recommendations is provided in Sect. 8.
6.4 Sensitivity analysis of hyperparameters in symbolic regression model
Sensitivity analysis is a critical component in the evaluation of machine learning and SR models. It provides
insights into how variations in the hyperparameters of an SR model inﬂuence its overall performance. By
systematically modifying input model parameters, such as population size in evolutionary algorithms, it is
feasible to test the stability, accuracy, and interpretability of the resulting model. This procedure not only depicts
optimal conﬁgurations for model training but also demonstrates the durability of the approach under varying
computational constraints. In the framework of symbolic regression, where both prediction accuracy and
expression simplicity are essential, sensitivity analysis is fundamental in guiding the choice of hyperparameters
that provide effective and interpretable solutions. The effect of population size in the SR model has a highly
impactful effect on ﬁnding better mathematical expressions with the predicted solution of the PINN model.
In our work, Table 4 presents the outcomes obtained by varying population sizes in the SR model with a ﬁxed
number of iterations. The SR model was executed once for each population size, as it exhibits sensitivity to input
data and tends to produce varying outcomes across multiple runs. The results highlight how these changes impact
expression complexity and error metrics such as MSE and MAE, reﬂecting the model’s ability to ﬁt the predicted
data with accurate and interpretable mathematical expressions for the solution of the forced Burgers’ equation
with M ¼ 0:2.
It is noticeable from Table 4 that increasing values of population size take more runtime of the model and slow
down its convergence speed. Furthermore, the small population size accelerates its convergence, but it does not
guarantee that it discovers the optimal mathematical equation that best ﬁts the data of the predicted solution with
the least complexity and minimum errors. Therefore, a suitable population size needs to be set to obtain optimal
mathematical expressions with a fast convergence speed. High equation complexity can lead to overﬁtting and
make the model difﬁcult to interpret, and the discovered equation will be more challenging to understand
analytically. Based on this analysis, 30 population size with 27 iterations in the SR model was selected to achieve
the desired analytical expressions of the predicted data. As observed from Table 4, the SR model performs well
with a population size of 30 and 27 iterations, achieving an MSE of 0.00007, an expression complexity of 18, and
a mean absolute error of 0.005 when compared to the PINN model. Moreover, for larger population sizes, the SR
model tended to produce highly complex mathematical expressions, which were signiﬁcantly more difﬁcult to
interpret in a physical context compared to simpler expressions that exhibited minimal errors.
Fig. 20 Histogram of residual losses on unseen dataset for different seed values to make different datasets to capture the
PINN model performances
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20233

---

## Page 30
7 Statistical and numerical validation of PINN predictions and computing confidence
interval
7.1 Validation on test datasets
To evaluate the robustness and generalization capability of our PINN model, we trained it across 10 different
random seeds that are used to generate new input datasets for training, and computed the mean PDE residuals
with ﬁxed M ¼ 0:2 on a ﬁxed unseen test set of 1500 points for each case.
For the forced Burgers’ equation, the histogram (Fig. 19a) of residuals shows a tightly centered and
approximately symmetric distribution around zero, indicating stable performance across different initializations.
The mean residual across all seeds is found to be 4:91  104, with a standard deviation of 5:03  103 and a
95% conﬁdence interval of 
3:11  103. This suggests a high consistency and minimal bias in the data.
Similarly, for the ﬁfth-order evolutionary equation, the histogram of PDE residuals is shown in Fig. 19b. The
residuals are consistently low across different seeds, with a mean residual of 1:20  103, standard deviation of
9:70  103, and a 95% conﬁdence interval of 
6:01  103. These results demonstrate that the model’s
performance is not sensitive to seed selection, afﬁrming its reproducibility and generalization capability across
different training scenarios.
Overall, the consistently low residuals and tight conﬁdence intervals across different seed values conﬁrm the
reproducibility and generalization capability of the PINN models for both low-order and high-order nonlinear
PDEs.
7.2 Cross-validation on unseen datasets of PINN predictions
To assess the robustness and generalization of our PINN models, we conducted a 10-fold cross-validation on two
representative partial differential equations, denoted by Eqs. (24) and (25). For each equation, the PINN models
were trained using 10 different random seed values to introduce diversity in the training points, and their
performance was evaluated on a ﬁxed, unseen test set with 20,000 data points in each fold.
In the case of Eq. (24), the histogram in Fig. 20a shows that the residual distribution is tightly centered around
zero and displays a symmetric shape, indicating stable and repeatable convergence across folds. The average
residual across all folds is approximately 3:64  104, with a standard deviation of 7:16  103 and a 95%
conﬁdence interval of 
1:14  104. These results suggest that the PINN maintains both accuracy and stability
across different training conditions.
For Eq. (25), the cross-validation results reveal almost similar pattern as shown in Fig. 20b. The residual
distribution remains centered and symmetric, despite the equation’s higher-order complexity. The mean residual
Fig. 21 Comparison of
FDM and PINN solutions
of the forced-Burgers
equation with M ¼ 0 at
different time instances
(i.e., t ¼ 0:4; 0:6; 0:8). The
close agreement between
the two methods across the
spatial domain demon-
strates the accuracy of the
PINN approach in captur-
ing the solution dynamics
123
Neural Computing and Applications (2025) 37:20205–20240
20234
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 31
is 2:55  104, with a standard deviation of 1:29  102 and a 95% conﬁdence interval of 
5:66  105. This
demonstrates the strong consistency of the model.
Overall, the low variability in residuals across folds and the overlapping conﬁdence intervals conﬁrm that our
PINN framework generalizes well and produces reproducible results. The use of cross-validation further validates
the robustness of our method across different random initializations, making it a reliable approach for solving
diverse nonlinear PDEs.
7.3 Numerical validation of deep learning-based solutions
To demonstrate the reliability and accuracy of the proposed method, a numerical approach has been employed to
validate the results obtained from the applied technique. Speciﬁcally, the ﬁnite difference method (FDM) has
been used to verify the outcomes of both the PINN and the SR methods. The numerical validation of the PINN
solution for Eq. (24) with M ¼ 0 is presented through a direct comparison with FDM results at different time
instances t ¼ 0:4; 0:6; 0:8, as shown in Fig. 21. This ﬁgure demonstrates that the PINN-predicted solutions show
excellent agreement with the corresponding FDM results across the entire spatial domain x 2 ½2; 2.
Additionally, the PINN-based solution of Eq. (24), along with the solution derived from the inter-
pretable mathematical expression provided by the SR model, has been compared with numerical solutions using
FDM, as illustrated in Fig. 22a–c, using a periodic pulse wave as the initial condition. Figure 22d depicts the
absolute error distribution between the PINN-predicted and FDM solutions over the domain. It is evident from the
Fig. 22 Comparison of solution proﬁles and error analysis for the forced Burgers’ equation with M ¼ 0, demonstrating the
validity of different computational approaches. a Numerical solution obtained using the FDM, serving as the reference.
b Predicted solution from the PINN, showing close agreement with the FDM results across the spatial domain. c SR solution
derived from the PINN-predicted data, highlighting the model’s ability to extract interpretable and physically meaningful
expressions. d Absolute error distribution between the PINN and FDM solutions over the spatio-temporal domain
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20235

---

## Page 32
ﬁgure that the errors remain sufﬁciently close to zero in most regions. These results provide strong evidence that
the predicted solutions from the PINN align well with the numerical solutions, thereby conﬁrming the accuracy
and reliability of the proposed PINN approach. Thus, the application of deep learning methods in solving and
analyzing nonlinear PDEs represents a promising alternative approach.
8 Some challenges and recommendations in symbolic regression
Symbolic regression is a powerful tool in modern computational algorithms, though it has some major issues
while dealing with complex scientiﬁc problems. It ﬁnds better understandable mathematical expressions for some
typical problems, but sometimes, the SR model discovers very complicated equations that may be too complex to
interpret. To overcome the challenge of complicated equations in symbolic regression, it is beneﬁcial to direct the
SR model toward simpler solutions by imposing greater penalties on more complex mathematical operations.
This approach helps to maintain a balance between accuracy and interpretability in the generated expressions.
Keeping the overall complexity in check and prioritizing simpler formulations during model selection makes the
outcomes clearer, more concise, and more accessible for scientiﬁc understanding. Furthermore, PySR encourages
simpler solutions by applying parsimony pressure, which penalizes overly complex expressions through a tunable
complexity weighting to prevent overﬁtting. This facilitates the identiﬁcation of equations that are not only
accurate but also interpretable and capable of generalizing to unseen data. PySR also uses multi-objective
optimization to strike a balance between ﬁtting the data well and keeping the equations simple. Techniques like
early stopping are used to avoid overtraining, especially when performance stops improving on validation data. In
addition, limiting the use of highly ﬂexible operators helps reduce the chance of overﬁtting in noisy or limited
datasets, making the results more robust and reliable.
Again, SR is computationally expensive for large, noisy datasets. The computational cost arises in identifying
the predicted expressions. The population size and the number of iterations need to be rectiﬁed accordingly to
enhance performance and reduce runtime, as these are the two main model parameters in symbolic regression. To
enhance the efﬁciency of the SR model on large datasets, starting with data puriﬁcation, noise removal, or
dropping the number of input features might be beneﬁcial. Using parallel computing or more advanced hardware
may signiﬁcantly decrease computational time. Additionally, incorporating early stopping when the model’s
performance levels off or testing smaller models before running the entire process can save time and resources.
PySR tries to ﬁnd closed-form analytical expressions by using the genetic algorithm on data. However, math-
ematical operators in predeﬁned search spaces are very limited, as common functions generally include the sine
function, cosine function, exponential function, and logarithmic function.
These mathematical functions with standard mathematical operators can be the cause of insufﬁciency for
describing the governing physics of complex nonlinear PDEs due to the involvement of special functions such as
Bessel and hypergeometric functions, and dependencies of non-polynomial form, like power law relationships in
PDEs. To rectify this problem, a custom operator should be added to the PySR model so that it can effectively call
this custom function during its training process for ﬁtting the data with high performance speed and fewer errors.
Furthermore, genetic programming algorithms may be stuck in local minima, failing to provide better or simpler
equations that ﬁt the given data. Mutation rates should be adjusted very carefully, or a large population size needs
to be used to overcome this issue. Moreover, restarting the search process from a new starting point may be a
useful way to avoid getting stuck in local minima. The method can explore other regions of the search space by
beginning with a new batch of random solutions if the algorithm stops improving or converges to an undesirable
result. This may increase the chances of ﬁnding better and more accurate results efﬁciently. Again, for very small
datasets, the SR model may produce inaccurate predictions. It cannot read the perfect relationship among the data
points for very few points in the datasets. To properly address the ideal, appropriate expressions to these data
points, choosing sufﬁciently large data points inside the predetermined domain with proper tuning of model
parameters is essential.
123
Neural Computing and Applications (2025) 37:20205–20240
20236
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 33
9 Scientific contributions and novelty
The primary scientiﬁc contribution of this work lies in the integration of physics-informed neural networks with
symbolic regression to develop an interpretable, data-efﬁcient framework for discovering approximate analytical
solutions of nonlinear PDEs. Unlike traditional PINNs, which typically yield black-box solutions, the proposed
hybrid approach facilitates the extraction of explicit analytical expressions that preserve physical meaning and
enhance generalizability. This work stands out for its unique blend of deep learning and evolutionary symbolic
regression, which aimed to ﬁnd analytical solutions to nonlinear partial differential equations, speciﬁcally in the
context of magnetically inﬂuenced bioﬂuid dynamics. This remains a relatively unexplored area in current
scientiﬁc research. Compared to prevailing techniques, which often focus solely on forward simulation or
parameter estimation, our framework provides a transparent and compact representation of the system’s behavior
and has been validated through extensive numerical simulations and statistical analysis. This dual beneﬁt of
interpretability and predictive accuracy distinguishes the proposed method from existing approaches.
10 Physiological relevance and future directions
Bridging the gap between mathematical modeling and practical applications is very important, especially in ﬁelds
like biology and medicine, where understanding the underlying physiological processes is crucial. This study
shows that symbolic regression combined with PINN predictions can generate clear and concise mathematical
expressions for nonlinear PDEs, such as the forced Burgers equation and a ﬁfth-order evolutionary equation.
These equations often reﬂect physiological phenomena such as nonlinear advection, viscous dissipation, and
higher-order dispersive effects, which are central to understanding pressure wave propagation and ﬂow dynamics
in arteries. The solutions of these nonlinear PDEs offer insights into key physiological processes such as pressure
wave propagation, arterial wall elasticity, and blood ﬂow dynamics. This understanding is crucial for analyzing
vascular conditions and can support the design of medical devices that respond to the natural behavior of the
cardiovascular system. Increased arterial stiffness is closely linked to cardiovascular risks such as atherosclerosis,
hypertension, and heart failure. Large artery stiffness is measured using pulse wave velocity because stiff arteries
allow pulse waves to ﬂow through them more quickly. This phenomenon can be used in clinical practice to
predict cardiovascular events like heart attacks or strokes, since stiffer arteries make the heart work harder [43].
Additionally, surgical techniques such as angioplasty, along with pulse wave velocity monitoring, help evaluate
recovery and assess the efﬁcacy of the intervention in restoring normal vascular function.
Our main focus has been on mathematical accuracy and computational efﬁciency in obtaining the solutions of
those PDEs. Still, investigating how these mathematical expressions relate to real physiological processes is an
important goal for future work. Comparing the discovered expressions with established physiological models or
experimental data could provide valuable insights into how well these equations reﬂect true biological mecha-
nisms. In addition, collaboration with experts in medicine, physiology, and related ﬁelds is essential for accurately
interpreting the results and assessing whether the derived equations provide meaningful insights or reliable
predictions for biomedical applications. This collaborative and interdisciplinary effort will help turn mathematical
ﬁndings into practical tools for guiding experiments, clinical decisions, and further scientiﬁc research.
11 Conclusions and remarks
In this study, the dynamics of nonlinear pulse propagation were investigated through the viscoelastic tube,
speciﬁcally focusing on the deformation of the tube wall bending. A one-dimensional viscoelastic ﬂuid ﬂow
model was utilized to identify the forced Burgers’ equation and a ﬁfth-order evolutionary equation that simulates
the ﬂuid ﬂow nature in arteries. The main aspect of this research is to ﬁnd the predicted solutions and their
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20237

---

## Page 34
analytical approximate expressions for the solutions of these nonlinear equations. In this regard, genetic pro-
gramming, an evolutionary algorithm in machine learning approach, was used to successfully derive the math-
ematical expressions with high accuracy for the complex nonlinear systems. The following is a summary of the
primary conclusions and contributions:
•
The PINN algorithm with the symbolic regression technique was utilized to ﬁnd the predicted solution as well
as analytical expressions of forced Burgers’ equation and nonlinear ﬁfth-order evolutionary equation
effectively with error Oð103Þ.
•
A sensitivity analysis of the SR model’s hyperparameters was conducted, demonstrating their impact on the
model’s performance and its ability to achieve accurate results.
•
Solutions of the PDEs at different scales were highlighted, demonstrating the accuracy of the PINN model in
satisfying the boundary conditions within the domain.
•
The solutions of the PINN model and the symbolic regression model were compared, highlighting the superior
performance of symbolic regression in producing well-ﬁtted mathematical expressions for the PINN model’s
predicted data.
•
The PINN model integrated with the symbolic regression method produces high-ﬁdelity results, as
demonstrated by both numerical and statistical validation. Residual loss analysis further supports the accuracy
and reliability of the interpretable symbolic expressions.
•
The MSE loss of the analytical solutions obtained through symbolic regression demonstrated a good ﬁt and
offered more profound insights into the relationship between input and output data, especially with appropriate
population size adjustment and total number of iterations in the SR model to obtain optimum results.
Therefore, the mathematical expressions we obtained helped characterize the behavioral patterns of the PDEs and
provided a better understanding of the nature of their solutions. Moreover, blood ﬂow propagation, as well as its
pulsatile nature in a viscoelastic artery, can be understood more accurately with the help of these discovered
mathematical equations.
Overall, this research adds to the expanding understanding of how machine learning, especially PINNs, can be
utilized to address nonlinear PDEs. The techniques described here not only increase simulation accuracy in
intricate physical systems but also open the door for the PINN applications in symbolic regression to identify
analytical solutions for scientiﬁc modeling in the future.
Acknowledgements The authors thank the reviewers and the associate editor for their comments and suggestions to improve
the paper considerably. The author, J. Das, wishes to thank the Council of Scientiﬁc and Industrial Research (CSIR), India,
for providing ﬁnancial support (File No: 09/0028(21164)/2025-EMR-I) as a research scholar at the University of Calcutta,
India.
Author Contributions JD involved in conceptualization (equal); data curation (equal); formal analysis (equal); investigation
(equal); methodology (equal); software (equal); validation (equal); writing—original draft (equal). BB took part in con-
ceptualization (equal); formal analysis (equal); writing—review and editing (equal). SD involved in conceptualization
(equal); formal analysis (equal); funding acquisition (equal); supervision (equal); writing—review and editing (equal). SC
involved in conceptualization (equal); formal analysis (equal); supervision (equal); writing—review and editing (equal).
Funding Open access funding provided by Copenhagen University. The ﬁnancial support was provided by the Council of
Scientiﬁc and Industrial Research (CSIR), India.
Data Availability The data that support the ﬁndings of this study are openly available in GitHub at https://github.com/
satyasaran/SymPINNPDE.git.
Declarations
Conflict of interest The authors have no conflicts to disclose.
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
123
Neural Computing and Applications (2025) 37:20205–20240
20238
https://doi.org/10.1007/s00521-025-11450-9

---

## Page 35
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
1. Thomas B, Sumam K (2016) Blood ﬂow in human arterial system-a review. Procedia Technol 24:339–346
2. Ku DN (1997) Blood ﬂow in arteries. Annu Rev Fluid Mech 29(1):399–434
3. Shah NA, Vieru D, Fetecau C (2016) Effects of the fractional order and magnetic ﬁeld on the blood ﬂow in cylindrical
domains. J Magn Magn Mater 409:10–19
4. Lund LA, Ghoto AA, Al-Khaled K, Ghachem K, Fadhel MA, Khan SU, Kolsi L (2024) Thin ﬁlm ﬂow of blood-based
hybrid nanoparticles subject to slip effects: a stability assessment. Int J Mod Phys B 38(15):2450183
5. Bhaumik B, Changdar S, Chakraverty S, De S (2024) Effects of viscosity and induced magnetic ﬁelds on weakly
nonlinear wave transmission in a viscoelastic tube using physics-informed neural networks. Phys Fluids 36(12):121902
6. Wang X-F, Nishi S, Matsukawa M, Ghigo A, Lagre´e P-Y, Fullana J-M (2016) Fluid friction and wall viscosity of the 1d
blood ﬂow model. J Biomech 49(4):565–571
7. Kissas G, Yang Y, Hwuang E, Witschey WR, Detre JA, Perdikaris P (2020) Machine learning in cardiovascular ﬂows
modeling: predicting arterial blood pressure from non-invasive 4d ﬂow mri data using physics-informed neural net-
works. Comput Methods Appl Mech Eng 358:112623
8. Samaniego E, Anitescu C, Goswami S, Nguyen-Thanh VM, Guo H, Hamdia K, Zhuang X, Rabczuk T (2020) An energy
approach to the solution of partial differential equations in computational mechanics via machine learning: concepts,
implementation and applications. Comput Methods Appl Mech Eng 362:112790
9. Mijwel MM, Esen A, Shamil A (2023) Overview of neural networks. Babylonian J Mach Learn 2023:42–45
10. Pratama A, Danang MA, Bakar IN (2022) Ann-based methods for solving partial differential equations: a survey. Arab J
Basic Appl Sci 29(1):233–248
11. Raissi M, Perdikaris P, Karniadakis GE (2017) Physics informed deep learning (part i): data-driven solutions of
nonlinear partial differential equations. arXiv:1711.10561
12. Li X, Liu Y, Liu Z (2023) Physics-informed neural network based on a new adaptive gradient descent algorithm for
solving partial differential equations of ﬂow problems. Phys Fluids 35(6):063608
13. Fuhg JN, Bouklas N (2022) The mixed deep energy method for resolving concentration features in ﬁnite strain
hyperelasticity. J Comput Phys 451:110839
14. Shihab MA, Taha WM, Hameed RA, Jameel A, Ibrahim S (2023) Implementation of variational iteration method for
various types of linear and nonlinear partial differential equations. Int J Electr Comput Eng 13(2):2131–2141
15. Altaie SA, Anakira N, Jameel A, Ababneh O, Qazza A, Alomari AK (2022) Homotopy analysis method analytical
scheme for developing a solution to partial differential equations in fuzzy environment. Fractal Fraction 6(8):419
16. Shi P, Zeng Z, Liang T (2024) Physics-informed convnet: learning physical ﬁeld from a shallow neural network.
Commun Nonlinear Sci Numer Simul 132:107911
17. Xiang Z, Peng W, Zhou W, Yao W (2022) Hybrid ﬁnite difference with the physics-informed neural network for solving
pde in complex geometries. arXiv:2202.07926
18. Majumdar R, Jadhav V, Deodhar A, Karande S, Vig L, Runkana V (2023) Symbolic regression for pdes using pruned
differentiable programs. arXiv:2303.07009
19. Zhu Z, Hao J, Huang J, Huang B (2023) Bc-pinn: an adaptive physics informed neural network based on biased
multiobjective coevolutionary algorithm. Neural Comput Appl 35(28):21093–21113
20. Oh H, Amici R, Bomarito G, Zhe S, Kirby R, Hochhalter J (2023) Genetic programming based symbolic regression for
analytical solutions to differential equations. arXiv:2302.03175
21. Changdar S, Bhaumik B, Sadhukhan N, Pandey S, Mukhopadhyay S, De S, Bakalis S (2024) Integrating symbolic
regression with physics-informed neural networks for simulating nonlinear wave dynamics in arterial blood ﬂow. Phys
Fluids 36(12):121924
22. Abbasi A, Al-Khaled K, Zouidi F, Khan SU, Khan MI, Bafakeeh OT, Farooq W, Choudhari R (2023) Blood-based
electro-osmotic ﬂow of non-newtonian nanoﬂuid (carreau-yasuda) in a tapered channel with entropy generation. ZAMM
J Appl Math Mech Zeitschrift fu¨r Angewandte Mathematik und Mechanik 103(5):e202100351
23. Wang X (2014) 1D modeling of blood ﬂow in networks: numerical computing and applications. Ph.d thesis, Universite´
Pierre et Marie Curie-Paris VI
24. Ahmad S, Al-Johani A, Sahu S (2021) Effect of magnetic and perturbation parameters on blood ﬂow distribution
through an artery. Appl Appl Math Int J (AAM) 16(1):32
Neural Computing and Applications (2025) 37:20205–20240
123
https://doi.org/10.1007/s00521-025-11450-9
20239

---

## Page 36
25. Kudryashov N, Chernyavskii I (2008) Numerical simulation of the process of autoregulation of the arterial blood ﬂow.
Fluid Dyn 43(1):32–48
26. Nasrin R, Hossain A, Zahan I (2020) Blood ﬂow analysis inside a stenotic artery using power-law ﬂuid model. RDMS
13:1–10
27. Steele BN, Valdez-Jasso D, Haider MA, Olufsen MS (2011) Predicting arterial ﬂow and pressure dynamics using a 1d
ﬂuid dynamics model with a viscoelastic wall. SIAM J Appl Math 71(4):1123–1143
28. Giusti A, Mainardi F (2016) A dynamic viscoelastic analogy for ﬂuid-ﬁlled elastic tubes. Meccanica 51:2321–2330
29. Nikolova E, Jordanov I, Dimitrova Z, Vitanov N (1895) Evolution of nonlinear waves in a blood-ﬁlled artery with an
aneurysm. AIP Conf Proc 1:2017
30. Kudryashov NA, Sinelshchikov DI (2011) Nonlinear evolution equation for describing waves in a viscoelastic tube.
Commun Nonlinear Sci Numer Simul 16(6):2390–2396
31. Cuomo S, Di Cola VS, Giampaolo F, Rozza G, Raissi M, Piccialli F (2022) Scientiﬁc machine learning through physics-
informed neural networks: Where we are and what’s next. J Sci Comput 92(3):88
32. Faroughi SA, Pawar N, Fernandes C, Raissi M, Das S, Kalantari NK, Mahjour SK (2022) Physics-guided, physics-
informed, and physics-encoded neural networks in scientiﬁc computing. arXiv:2211.07377
33. Lagaris IE, Likas A, Fotiadis DI (1997) Artiﬁcial neural network methods in quantum mechanics. Comput Phys
Commun 104(1–3):1–14
34. Yu J, Lu L, Meng X, Karniadakis GE (2022) Gradient-enhanced physics-informed neural networks for forward and
inverse pde problems. Comput Methods Appl Mech Eng 393:114823
35. Lu L, Meng X, Mao Z, Karniadakis GE (2021) Deepxde: a deep learning library for solving differential equations.
SIAM Rev 63(1):208–228
36. Song Y, Wu Y, Guo Y, Yan R, Suganthan PN, Zhang Y, Pedrycz W, Das S, Mallipeddi R, Ajani OS et al (2024)
Reinforcement learning-assisted evolutionary algorithm: a survey and research opportunities. Swarm Evol Comput
86:101517
37. Shukla A, Pandey HM, Mehrotra D (2015) Comparative review of selection techniques in genetic algorithm. IEEE,
pp 515–519
38. Slowik A, Kwasnicka H (2020) Evolutionary algorithms and their applications to engineering problems. Neural Comput
Appl 32:12363–12379
39. Kramer O, Kramer O (2017) Genetic algorithms. Springer, Berlin
40. Katoch S, Chauhan SS, Kumar V (2021) A review on genetic algorithm: past, present, and future. Multimedia Tools
Appl 80:8091–8126
41. Cranmer M (2023) Interpretable machine learning for science with pysr and symbolicregression. arXiv:2305.01582
42. Tonda A (2025) Review of PySR: high-performance symbolic regression in python and julia. Genet Program Evolvable
Mach 26:7
43. Inoue N, Maeda R, Kawakami H, Shokawa T, Yamamoto H, Ito C, Sasaki H (2009) Aortic pulse wave velocity predicts
cardiovascular mortality in middle-aged and elderly Japanese men. Circ J 73(3):549–553
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.
Authors and Afﬁliations
Joy Das1 • Bivas Bhaumik2 • Soumen De1 • Satyasaran Changdar3
& Soumen De
sdeappmath@caluniv.ac.in
& Satyasaran Changdar
sach@di.ku.dk; satyasaran@gmail.com; satyasaran@food.ku.dk
1
Department of Applied Mathematics, University of Calcutta, 92, A.P.C. Road, Kolkata 700009, India
2
Department of Mathematics, National Institute of Technology, Rourkela, Odisha, India
3
Department of Food Science, University of Copenhagen, Copenhagen, Denmark
123
Neural Computing and Applications (2025) 37:20205–20240
20240
https://doi.org/10.1007/s00521-025-11450-9

---
