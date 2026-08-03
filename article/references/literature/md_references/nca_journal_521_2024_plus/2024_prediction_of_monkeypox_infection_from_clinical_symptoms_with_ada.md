# Prediction of monkeypox infection from clinical symptoms with adaptive artificial bee colony-based artificial neural network

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-09782-z

---

## Page 1
ORIGINAL ARTICLE
Prediction of monkeypox infection from clinical symptoms
with adaptive artificial bee colony-based artificial neural network
Ahmed Muhammed Kalo Hamdan1
• Dursun Ekmekci1
Received: 22 March 2023 / Accepted: 25 March 2024 / Published online: 27 April 2024
 The Author(s) 2024
Abstract
In 2022, the World Health Organization declared an outbreak of monkeypox, a viral zoonotic disease. With time, the
number of infections with this disease began to increase in most countries. A human can contract monkeypox by direct
contact with an infected human, or even by contact with animals. In this paper, a diagnostic model for early detection of
monkeypox infection based on artiﬁcial intelligence methods is proposed. The proposed method is based on training the
artiﬁcial neural network (ANN) with the adaptive artiﬁcial bee colony algorithm for the classiﬁcation problem. In the
study, the ABC algorithm was preferred instead of classical training algorithms for ANN because of its effectiveness in
numerical optimization problem solutions. The ABC algorithm consists of food and limit parameters and three procedures:
employed, onlooker and scout bee. In the algorithm standard, artiﬁcial onlooker bees are produced as much as the number
of artiﬁcially employed bees and an equal number of limit values are assigned for all food sources. In the advanced
adaptive design, different numbers of artiﬁcial onlooker bees are used in each cycle, and the limit numbers are updated. For
effective exploitation, onlooker bees tend toward more successful solutions than the average ﬁtness value of the solutions,
and limit numbers are updated according to the ﬁtness values of the solutions for efﬁcient exploration. The performance of
the proposed method was investigated on CEC 2019 test suites as examples of numerical optimization problems. Then, the
system was trained and tested on a dataset representing the clinical symptoms of monkeypox infection. The dataset consists
of 240 suspected cases, 120 of which are infected and 120 typical cases. The proposed model’s results were compared with
those of ten other machine learning models trained on the same dataset. The deep learning model achieved the best result
with an accuracy of 75%. It was followed by the random forest model with an accuracy of 71.1%, while the proposed
model came third with an accuracy of 71%.
Keywords Monkeypox  Monkeypox clinical symptoms  Machine learning  Artiﬁcial neural network  Artiﬁcial bee
colony algorithm  Adaptive artiﬁcial bee colony algorithm
1 Introduction
In 2022, the monkeypox virus (MPXV) spread, causing
panic among people, and causing concern among scientists
due to its rapid spread [1]. Approximately 1–11% of cases
lead to death [2]. The World Health Organization (WHO)
announced that the number of people infected with this
virus had increased signiﬁcantly, and it was conﬁrmed that
more than 318,000 patients were infected in August 2022
[3]. This virus belongs to the genus of corticoviruses and is
similar to zoonotic smallpox [4]. It is caused by the
orthopoxvirus and is a genera of the poxviridae family that
is dangerous to humans [5]. Figure 1 shows infection with
monkeypox, which begins to appear after 3 days at most of
the infection with the fever. At ﬁrst, the symptoms are on
the face, and then, they spread to the rest of the body. A
person is considered contagious before the rash appears by
ﬁve days. And it remains until a new layer of skin forms
underneath. It takes between two to four weeks.
The disease was detected for the ﬁrst time in Africa,
speciﬁcally in the Republic of the Congo [4]. And then it
spread among the countries of the world. As of June 2022,
more than 1,256 cases of monkeypox have been reported in
& Ahmed Muhammed Kalo Hamdan
2028126015@ogrenci.karabuk.edu.tr
1
Department of Computer Engineering, Faculty of
Engineering, Karabuk University, 78050 Karabuk, Turkey
123
Neural Computing and Applications (2024) 36:13715–13730
https://doi.org/10.1007/s00521-024-09782-z
(0123456789().,-volV)(0123456789().,-volV)

---

## Page 2
several regions of Spain. Statistics indicate that the
majority of those infected are males. At the same time, the
average age was about 36 years [6]. The method of
infection with monkeypox is direct contact with an infected
person, animal or other material. It is also transmitted
through the mucus of the nose, mouth or eyes [7]. And
having sex is one of the ways the virus is transmitted. [5]
The clinical picture of monkeypox and smallpox is very
similar, and the symptoms that appear upon infection differ
from one case to another. However, skin rash is the most
likely sign of infection, along with anogenital lesions,
lethargy and muscle pain [7]. Monkeypox symptoms last
up to four weeks. Children are also the most vulnerable [8].
Patients with the disease may suffer several side effects,
including bronchiolitis, hypothermia, bacterial infections
and respiratory failure [9]. Diagnosing the condition based
on a range of clinical features is difﬁcult. An accurate
diagnosis of monkeypox requires a molecular test in a
specialized laboratory to distinguish it from other diseases.
The appearance of the ﬁrst positive PCR result may take 5
days from the onset of symptoms [7].
Therefore, early detection of the disease is crucial to
control transmission. It is also necessary to continue
describing the symptoms of the disease and its transmission
mechanisms to reduce its risk among populations [10].
With the spread of artiﬁcial intelligence applications,
researchers have resorted to using it in diagnosing disease
conditions in medical and biomedical applications [11].
They used it in multiple ways, depending on the dataset
collected from the lesions’ images or the infected’s clinical
symptoms.
In the ﬁeld of automatic virus identiﬁcation in trans-
mission electron microscopy (TEM) images, [11] relied on
image datasets to characterize the monkeypox virus. It
consists of 1245 micrographs of 22 viruses taken by TEM.
However, this study was limited to 14 types of viruses,
such as Astrovirus & Adenovirus & CCHF & Ebola, etc.
The study used convolutional neural network (CNN) deep
learning (DL) models to build its model. The accuracy rate
of the proposed method was 93.1%.
[2] Use different approaches in data acquisition. The
data is a set of images of skin lesions. Collected by manual
searches and contact with infected persons. The study
focused on separating monkeypox from similar cases of
different types of smallpox. The approach taken was
VGG16 deep transfer learning. It consists of three layers of
convolutional ﬁlters to extract the features from the images
and then the neural network. It was a perfect idea that he
used transfer learning. The accuracy rate of the results
obtained was 86%.
[12] Research was divided into three separate studies.
All of them were conducted on the proposed approach.
Transfer learning approaches (GRA-TLA) work on multi-
class classiﬁcation using generalization and regularization.
The training dataset is the images of skin lesions. It was
intended to support decision-making assistance to the
hospital. Computational results showed that the proposed
approach could distinguish between infected and non-in-
fected monkeypox individuals with an accuracy of 77–88%
in the ﬁrst and second studies. At the same time, the
residual network (ResNet) had the best performance for
multiclass classiﬁcation in the third study, with an accuracy
rate ranging from 84 to 99%.
[8] Also relied on training data consisting of images to
establish an early detection mechanism for monkeypox that
would help identify infected people. The approach taken in
this paper was to compare several models of ResNet50,
EfﬁcientNetB3 and EfﬁcientNetB7 algorithms. In the end,
it was concluded that the results of the EfﬁcientNetB3
algorithm were the best.
Saleh and Rabie took a different approach than previous
research, focusing on numerical data for clinical symptoms
of the disease from 500 suspected cases from Spain and
Nigeria [13]. The dataset was not limited to monkeypox
but included several other diseases such as acne, alopecia,
normal, psoriasis and smallpox. The human monkeypox
diagnosis (HMD) strategy was applied in the study. In fact,
the proposed method consisted of two phases. First:
extracting the appropriate features, using the improved
binary chimp optimization (IBCO) algorithm, which is a
Fig. 1 Symptoms of infection in monkeypox disease that appear on the skin [41]
13716
Neural Computing and Applications (2024) 36:13715–13730
123

---

## Page 3
hybrid selection algorithm. The second stage: composed of
three machine learning algorithms weighted naı¨ve Bayes
(WNB), weighted k-nearest neighbor’s (KNN) and deep
learning. In fact, a ﬁnal election is made for the output of
these three algorithms.
Computer-aided healthcare has become an essential ﬁeld
for artiﬁcial intelligence researchers as it provides the
advantage of early diagnosis for many diseases [14].
Medical data (especially images) required for disease
diagnosis can be processed with artiﬁcial intelligence
algorithms, and disease diagnosis can be made. When the
literature studies are examined, it is noticed that the pro-
posed methods for the early detection of monkeypox also
focus on image processing techniques. However, the fact
that medical data is generally obtained in chronological
order and cannot be collected simultaneously makes it
challenging to apply image processing techniques [15]. In
addition, although image processing techniques produce
successful solutions to problems with signiﬁcant differ-
ences, they may fail in classiﬁcation mainly due to the
close similarity between similar classes [16]. In this con-
text, taking a different approach from image processing,
Saleh and Rabie used a numerical dataset of disease
symptoms. However, in their study, they focused only on
the detection of monkeypox and similar diseases. This
paper presents a predictive model that will enable early
detection of monkeypox disease. Unlike other studies,
analysis data on disease symptoms were discussed in the
study instead of images taken from diseased individuals.
The artiﬁcial neural networks (ANN) were used to diag-
nose and predict disease. However, the artiﬁcial bee colony
(ABC) algorithm was used instead of classical learning
algorithms for network training due to its effectiveness in
numerical optimization problems. In addition, the adaptive
model (aABC for short) was preferred for faster conver-
gence, not the standard version of the ABC algorithm. The
study offers a novel approach to the literature with an ANN
model trained with an adaptive metaheuristic approach for
the early detection of monkeypox disease. The method’s
performance has been tested on clinical data from the bmj
center [9] and compared with KNN, SVC, deep learning
and random forest algorithms. The ﬁndings demonstrate
that the proposed method can be used for the early diag-
nosis of monkeypox disease.
The structure of this paper is organized as follows:
Sect. 2 describes the approach taken in this paper. Sec-
tion 3 presents experimental studies. Findings and discus-
sions are presented in Sect. 4. Section 5 reports on the
conclusion.
2 Methodology
This section describes in detail the proposed method for the
early detection of monkeypox. First, the classical ANN
model, the model’s training and the Levenberg–Marquardt
learning algorithm, which is widely used, are mentioned.
Since the proposed method involves training the ANN
model with a metaheuristic approach, the ABC algorithm,
which produces successful solutions for numerical opti-
mization problems, is described. Next, the aABC approach,
which updates the ABC parameters during the search
process, is presented as an adaptive version of the algo-
rithm. Finally, the section explains how the ANN is trained
with the aABC algorithm.
2.1 Artificial neural network (ANN)
ANN model used to diagnose monkeypox patients will be
described in detail. Artiﬁcial neural networks (ANN) are
one of the most widely applied classiﬁcation techniques for
solving prediction problems [17]. The principle of ANN is
based on the analysis of the biological nervous systems of
an organism. ANN consists of a set of nodes and a number
of interrelated processing components. ANN uses learning
algorithms to simulate knowledge and store this knowledge
in weighted connections, which reﬂect the activity of the
human brain [18]. ANN architecture consists of three main
components: input layers, hidden layers and output layers
(Fig. 2). ANN model must be trained ﬁrst in cases with
known classes [19].
The input layer in the neural network receives input
signals. Each neuron in the input layer corresponds to a
speciﬁc input parameter. This layer passes the neural net-
work’s input to the hidden layers. The number of hidden
layers varies from one model to another. The number of
hidden layers is determined empirically. Neurons receive
the signals coming from the ﬁrst layers, and then process
them by some nonlinear function of their total inputs. Each
neuron refers to a real number that indicates its contribu-
tion to the output. The neuron has a weight that is adjusted
during the network training process. This weight affects the
neuron’s contribution by multiplying it by the cell’s input.
The activation function of the neuron differs from one layer
to another, depending on the nature of the problem to be
solved. The number of output layer neurons is determined
by the nature of the problem, whether it is a binary clas-
siﬁcation or more. The output of the output layer is the
output of the neural network.
Neural Computing and Applications (2024) 36:13715–13730
13717
123

---

## Page 4
2.2 Training of ANN
Training a neural network involves adjusting the weights of
neurons to improve the prediction or classiﬁcation process
in a task. This process is done using a training algorithm
and a set of training data [20]. The process of training a
neural network consists of several stages, which are as
follows:
•
First, Initialization: the weights and their biases are
randomly initialized.
•
The next stage, the forward propagation stage: the input
data is passed into the network, and the activation
values for each neuron in the network are calculated
using weights and biases.
•
Loss calculation: The output of the input data is
predicted, compared with the real values, and the
difference between them is calculated as a loss.
•
Back propagation: the loss propagates back through the
network to calculate the loss gradient at each layer and
at each neuron.
•
Finally, the weights and biases are updated using
gradient, and the process is repeated until the loss is
minimized.
There are several algorithms that can be used for
training ANNs, including Adam optimization, stochastic
gradient descent (SGD) and backpropagation [21]. The
choice of algorithm depends on the complexity of the
network and the type of task it is being trained for. It is also
important to note that the quality and quantity of the
training data can have a signiﬁcant impact on the perfor-
mance of the network [22].
2.3 Levenberg–Marquardt algorithm (L–M)
The Levenberg–Marquardt algorithm is an optimization
algorithm commonly used to train artiﬁcial neural net-
works. It is a modiﬁcation of the Gauss–Newton algorithm
and is designed to efﬁciently solve nonlinear least-squares
problems. The basic idea behind the Levenberg–Marquardt
algorithm is to use a combination of gradient descent and
Gauss–Newton methods to update the network weights and
biases during training [23]. The algorithm calculates the
Hessian matrix, which describes the curvature of the error
surface, and combines it with a damping factor to prevent
the algorithm from taking excessively large steps during
optimization. The Levenberg–Marquardt method adap-
tively switches between the Gauss–Newton update and the
gradient descent update when updating parameters. In
Marquardt’s update relationship as Eq. 1, the damping
parameter k is scaled by the diagonal of the Hessian JTW J
for each parameter.
JTWJ þ kdiag JTWJ




hlm ¼ JTW y  ^y
ð
Þ
ð1Þ
The algorithm adjusts the damping factor during training
to balance the trade-off between convergence speed and
stability. It starts with a high damping factor to provide
stability during early stages of training and gradually
decreases it to allow faster convergence. Compared to other
optimization algorithms, the Levenberg–Marquardt algo-
rithm typically converges faster and more accurately,
especially when dealing with highly nonlinear problems.
However, it can be computationally expensive and may
require careful tuning of the damping factor to achieve
optimal results [24].
Fig. 2 Structure artiﬁcial neural
network (ANN)
13718
Neural Computing and Applications (2024) 36:13715–13730
123

---

## Page 5
2.4 Artificial bee colony (ABC)
It falls under swarm intelligence algorithms. Inspired by
nature, mimics the work of bee swarms [25].
Swarm of bees are often concentrated in the ﬁeld the
most ﬂowering. The bees reach this region by applying the
swarm optimization algorithm [26]. That is, they spread
initially in the ﬁeld so that each bee records the area with
the most ﬂowers. Then, each bee moves randomly, and if it
ﬁnds a denser area, it updates its information and so on.
Upon
completion
of
the
random
search,
each
bee
announces what it has found. And then the bee swarm
selects the best location [27].
It is one of the methods of artiﬁcial intelligence in meta-
heuristic research problem [28]. ABC is an effective tool in
ﬁnding and improving solutions. In general, its work can be
summed up in ﬁnding and exploiting sources of food and
then looking for a new alternative. In ABC algorithm, food
reﬂects the initial solutions through which bees will look
for the perfect solution. The quality of the food ﬁtness
represents the assessment of the solution, while the limit
factor indicates the amount of food available in the source.
However, cycle represents the number of searches (S.
[29]).
Three groups of honeybees carry out foraging activities:
(a)- Scout bees: Their duty is to ﬁnd random food sources
(X). (b)- Employed bees: Their number equals the number
of food sources. Each employed bee moves from available
resources to a speciﬁc source. She also performs a local
search using Eq. (2) to ﬁnd a new resource next to the
resource it went to. (c)- Onlooker bees: The number of
onlooker bees equals the number of food sources [30].
When the employed bees return to the hive, they watch
each one’s waggle dance and determine the appropriate
food source to go to.
vij ¼ xij þ /ijðxij  xkjÞ
ð2Þ
In Eq. (2), x i represents the solution i that the employed
(or onlooker) bee will be interested in. This solution for
employed bees, i. means solution, but onlooker bees
determine the solution they will be interested in by the
choice they make with the roulette wheel. j is a randomly
chosen item of the solution, / is a randomly chosen
coefﬁcient in the range [- 1, 1], and xk is a randomly
chosen solution from among the current solutions.
The basic steps of making the ABC algorithm can be
summarized as follows:—Generate an initial solution
group.—Sending employed bees to food sources.—Send-
ing onlooker bees to the most appropriate source of food.—
Save the optimal source.—Repeat previous steps. Figure 3
shows the working diagram of ABC algorithm.
2.5 Adaptive artificial bee colony (aABC)
aABC algorithm overcomes some of the problems faced by
ABC algorithm. It depends on the nature of the problem to
be solved. In fact, aABC agrees with ABC in the main bee
divisions, employed bees, scout bees and onlooker bees.
However, the modiﬁcation that occurs in the mechanism of
action of both onlooker bees and scout bees was observed
(Inspired by [31]).
First Amendment: Onlooker bees select the best food
source from a group of foods accessed by employed bees.
However, onlooker bees can evaluate the solution based on
the speciﬁc ﬁtness of each solution according to the fol-
lowing Eq. 3:
pi ¼
fitness xi
ð Þ
Pn
j¼1 fitness xj
 
ð3Þ
Then, the mean ﬁtness of all solutions is calculated.
Onlooker bees only search for solutions with greater than
mean ﬁtness. The goal of this process is to search further in
the set of solutions with low ﬁtness. Hence giving it more
importance.
Second Amendment: Scout bees remove spent solutions
from the entire population. The depletion of the solution is
calculated by limit factor. In fact, each solution is assigned
limit value depending on the ﬁtness of the solution.
According to the following Eq. 4:
Limit i½  ¼ fitness i½   food  D
Pn
i¼1 fitness i½ 
ð4Þ
Because the bee algorithm gives high results in search
issues, these changes have affected the accuracy of the
algorithm.
To solve a speciﬁc problem f, assume the computational
time complexity of evaluating the function value of OðfÞ.
The maximum cycle number of iterations was set to MCN
and colony size to CS. The time complexity of classical
ABC
for
this
problem
is
OðMCN  ðCS  f þ CS  fð ÞÞ ¼ OðMCN  CS  fÞ.
So,
the time complexity in the initialization phase is OðCS  fÞ,
and the time complexity in the iterative process in the
employed and onlooker bee procedures is OðMCN  ðCS 
f þ CS  fÞÞ [32]. So, standard ABC’s total computational
time complexity is OðCS  fÞ. aABC shares the total limit
value used in standard ABC according to the ﬁtness value
of the solutions instead of dividing them equally among the
solutions. So, the computational time complexity of aABC
is the same with the standard ABC.
Neural Computing and Applications (2024) 36:13715–13730
13719
123

---

## Page 6
2.6 Proposed model
It aims to take advantage of the ability of aABC to ﬁnd the
optimal solutions, in training the weights of the ANN
neural network [33]. Figure 4 shows the method for
training ANN weights using aABC.
The proposed model is a neural network composed of
one input layer, two hidden layers and one output layer.
This network is trained by aABC algorithm, which is as
follows:
•
Generate an initial population to search for weights. At
this stage, all the neural network weights are arranged
in the form of vectors, each cell in this vector represents
a speciﬁc weight of the neural network weights. This
vector takes arbitrary values (the initialization of the
neural network weights). However, population size is
related to food factor, which determines the number of
vectors that will be generated. The length of a single
vector is deﬁned by D, which is the number of weights
of the neural network.
•
Each vector is evaluated using the RMSE equation as in
Eq. 5. Vector evaluation is calculated after all the
training data has been passed and the resulting error is
calculated. In fact, each vector has its own ﬁtness.
Fig. 3 Flowchart of the work of
ABC algorithm [30]
13720
Neural Computing and Applications (2024) 36:13715–13730
123

---

## Page 7
RMSE ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
X
N
i¼1
yo  yp

2
,
N
v
u
u
t
ð5Þ
•
The weights training process follows the previously
mentioned bee algorithm methodology. The number of
training times is subject to the Epoch factor.
•
Vector with the least error value is selected and saved.
In each Epoch cycle, it is considered as the ideal
solution within this cycle. In fact, this cycle’s best
vector is compared with the previous best vector, and
the vector with the lowest ﬁtness is retained.
•
At the end of the training, best vector representing the
weights of the neural network is obtained among all
cases.
•
The ﬁnal neural network is evaluated, veriﬁed and
measured for accuracy. Figure 6 shows the mechanism
of the proposed model.
3 Experimental study
aABC was coded in the.Net platform in C# 2022 pro-
gramming language and ran on a computer with an
Intel(R) Core (TM) i3 6006U 2.00 GHz processor, 12 GB
RAM and Windows 10 Pro 64-bit operating system. In this
section, the performance of the proposed method is tested
on CEC 2019 test suites, and the method’s success is
compared with classical ABC and other metaheuristic
methods. The section also describes the dataset used for
MonkeyPox disease detection. Then, some features of the
proposed model, performance measurements and assigned
hyperparameter values are mentioned.
3.1 Testing on CEC 2019 test suite
The CEC 2019 test suite, called the ’100 Digit Challenge’,
includes ten multi-modal functions designed to represent
complex optimization problems. Minimization problems
characterize these functions and are scalable. Additionally,
it mentions that some functions (CEC01-CEC03) remain
unaltered, while others (CEC04-CEC10) undergo shifts
and rotations. Moreover, competitors can modify up to two
parameters within the functions. The information is concise
and well structured, providing a good understanding of the
nature of the test suites.
The success of aABC on the CEC2019 suite has been
evaluated based on the results given in [34] Therefore, for a
fair comparison, the parameter values of the ABC and
aABC algorithms were determined by the parameter set in
([34]). Accordingly, the food is assigned as 15 (in this case,
the CS is 30), and the limit is assigned as food*D. The
comparison algorithms were run independently 30 times
for each pattern, and MCN in each experiment was
assigned to 500. For each function’s solution, search range
and dimensions (D) are given in Table 4.
Other metaheuristics compared to aABC include: the
ﬂower pollination algorithm for global optimization (FPA)
[35], gray wolf optimizer (GWO) [36], salp swarm algo-
rithm (SSA) [37], cuckoo search (CS) [38], sine cosine
algorithm (SCA) [39] and adaptive ﬂower pollination
algorithm (AFPA) [34].
3.2 Aabc’s discussion of statistical performance
For each CEC 2019 test problem, the solution search range
and dimensions (D) are given in Table 4. These algorithms
were run independently 30 times for each function, and the
maximum cycle number (MCN) in each experiment was
assigned to 500. The following ﬁgures show the results of
tests on the previously mentioned algorithms.
Fig. 4 Flow diagram of methodology
Neural Computing and Applications (2024) 36:13715–13730
13721
123

---

## Page 8
CEC03
CEC04
CEC05
CEC01
CEC02
Fig. 5 Time-complexity results
of algorithms
13722
Neural Computing and Applications (2024) 36:13715–13730
123

---

## Page 9
CEC07
CEC08
CEC09
CEC10
CEC06
Fig. 5 continued
Neural Computing and Applications (2024) 36:13715–13730
13723
123

---

## Page 10
Results from the experiments are shown in Fig. 5. ABC
and aABC methods could not produce very successful
solutions for the CEC01 function, but they reached the best
solution for the CEC02 function, like the other four algo-
rithms. All compared algorithms for the CEC03 function
achieved the best results. The best solutions for the CEC04
and CEC05 functions were obtained with aABC. The
classical ABC method produced the third-best solution for
the CEC04 function and the second-best solution after
aABC for the CEC05 function. For functions CEC06 and
CEC07, aABC is the second-best solution. In CEC09 and
CEC10 functions, aABC produced the second-best solu-
tions. In this case, aABC produced the best solution in ﬁve
out of ten cases in the CEC2019 test suites. When the
solution averages of the algorithms are examined, it is seen
that aABC produces successful solutions across the func-
tions. As a general evaluation, the success of the ABC
algorithm in numerical optimization problems has been
Fig. 6 Snapshot form used dataset
Fig. 7 Heatmap displays the
correlation between dataset
features
Table 1 Statistical methods for measuring the accuracy of a machine
learning model. [42]
Method name
Equation
Accuracy
TpþFp
TpþTnþFpþFn
Precision
Tp
TpþFp
Sensitivity
Tp
TpþFn
F1-score
2  RecallPrecision
RecallþPrecision
13724
Neural Computing and Applications (2024) 36:13715–13730
123

---

## Page 11
repeated, and the effect of aABC on the classical ABC
method has been proven.
3.3 Dataset
The dataset based on a study published by the bmj: Clinical
features and novel presentations of human monkeypox in a
central London center during the 2022 outbreak: descrip-
tive case series. [40] Features: Patient_ID, Systemic Ill-
ness, Rectal Pain, Sore Throat, Penile Edema, Oral
Lesions, Solitary Lesion, Swollen Tonsils, HIV Infection,
Sexually
Transmitted
Infection
and
Target
Variable:
MonkeyPox. The Monkeypox dataset comprises 240 cases
classiﬁed into two categories: ’positive’ and ’negative’.
The positive cases are monkeypox patients, the negative
cases are those who do not have monkeypox. In fact, a
negative case does not mean that he is in good health but
does not have monkeypox. However, this data determines
whether or not he only had monkeypox. Figure 6. Snapshot
of the monkeypox dataset. This dataset consists of 11
features, which include the patient’s clinical symptoms of
inﬂammation, fever and others. These features are used to
describe the symptoms that appear on the patient in order to
indicate the condition of each patient.
We calculated the linear correlation coefﬁcient between
features (Fig. 7). We found that the data had varying cor-
relations with each other. Also, the dataset does not contain
null values. We coded the words as follows: True: 1, False:
0. We also divided this data into two groups, 80% for
training and 20% for testing. In general, the percentage of
infected and non-infected cases was distributed in equal
proportions between these two groups.
In fact, the monkeypox dataset was divided into 168
cases as a training set of data and 72 cases as a test set of
data. The number of positive cases is 120 and the negative
cases are 120. Figure 7 shows how the features relate to
each other.
3.4 Performance evaluation
Statistical methods are used to measure the accuracy of
classiﬁcation algorithms. These methods contribute to
determining the standardization of the applied algorithm
such as: accuracy, precision, F1-score and sensitivity. In
our dataset, Monkeypox can be classiﬁed as True Positive
or True Negative if the individuals have been accurately
classiﬁed. It can be classiﬁed as False Positive or False
Negative if misdiagnosed. Speciﬁc statistical measures are
detailed in Table 1.
3.4.1 Root mean square error (RMSE)
It is a standard method for measuring model error. It is also
called loss function. Know its equation as follows:
Table 2 Performance of
proposed model
Phase
Performance
Accuracy (%0
F1-score (%)
Precision (%)
Sensitivity (%)
Training
78
76
81
84
Testing
71
72
69
67
Fig. 8 a Confusion matrix of training phase for the proposed model. b Confusion matrix for testing
Neural Computing and Applications (2024) 36:13715–13730
13725
123

---

## Page 12
RMSE ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
X
N
i¼1
yo  yp

2
,
N
v
u
u
t
ð6Þ
The value of this equation tells us the distance differ-
ence between the vector of expected values and the vector
of observed values. In data science, this formula is used to
evaluate trained models. It gives us the error rate between
the training results and original results.
3.4.2 Hyperparameter
The proposed model consists of four layers: one input
layer, two hidden layers and one output layer. It contains
11, 10, 10, 1 neurons per layer, respectively. For the hidden
layers, the activation function of the RELU Function has
been set as in Eq. 7 and for the output layer, the activation
function of the Sigmoid Function has been set as in Eq. 8.
As for the parameters of aABC algorithm, they are as
follows:
Epoch ¼ 400
food ¼ 50
Limit i½  ¼ fitness i½   food  D
P fitness i½ 
In order to avoid falling into the problem of (Vanishing
gradient), the RELU function was used for the hidden
layers. It is the basic way to solve this problem. However,
to solve (Overﬁtting) K-Folds technique was relied in
training the model.
yj ¼ f j x
ð Þ ¼ maxð0; xÞ
ð7Þ
Fig. 9 a Represents AUC-ROC curve during training phase. b AUC-ROC during testing phase
Fig. 10 Statistical results on the accuracy of all applied algorithms
13726
Neural Computing and Applications (2024) 36:13715–13730
123

---

## Page 13
yj ¼ f j x
ð Þ ¼
1
1 þ ex
ð8Þ
4 Result and discussion
The proposal model is tested with a sample dataset con-
sisting of 72 values taken from the dataset, it is a mixture of
monkeypox cases collected at the bmj.
The sample data consisted only of cases of monkeypox
with different symptoms. This also discusses the number of
positive cases and negative cases with different symptoms,
thus proposing ANN model diagnostic method based on
aABC algorithm. aABC is one of the evolutionary algo-
rithms that contribute to the training of neural network
weights.
Table 2 presents the results of the proposed model
during training and testing. The performance of the model
was measured by several criteria. They appear as follows:
in the training period accuracy, F1-score, precision and
sensitivity take the values 78%, 76%, 81%, 84%, respec-
tively. When testing, accuracy, F1-score, precision and
Table 3 Summarizes the performance of ten different models over 30 runs
Trials
Methods
ANN training by
aABC
ANN training
by ABC
Deep
learning
SVC
KNN
Random
forest
Bagging
classiﬁer
Decision
tree
Gradient
boosting
Naı¨ve
Bayes
1
69.0%
64.0%
72.9%
45.8%
65.1%
71.1%
59.5%
62.8%
63.8%
65.2%
2
67.0%
62.0%
68.8%
45.8%
65.1%
71.1%
66.6%
62.8%
63.8%
65.2%
3
64.0%
62.0%
64.6%
45.8%
65.1%
71.1%
60.9%
62.8%
63.8%
65.2%
4
58.0%
61.0%
68.8%
45.8%
65.1%
71.1%
60.5%
62.8%
63.8%
65.2%
5
67.0%
57.0%
62.5%
45.8%
65.1%
71.1%
52.1%
62.8%
63.8%
65.2%
6
58.0%
58.0%
60.4%
45.8%
65.1%
71.1%
45.5%
62.8%
63.8%
65.2%
7
54.0%
67.0%
72.9%
45.8%
65.1%
71.1%
62.5%
62.8%
63.8%
65.2%
8
57.0%
56.0%
68.8%
45.8%
65.1%
71.1%
66.6%
62.8%
63.8%
65.2%
9
65.0%
57.0%
66.6%
45.8%
65.1%
71.1%
62.5%
62.8%
63.8%
65.2%
10
67.0%
65.0%
70.8%
45.8%
65.1%
71.1%
60.8%
62.8%
63.8%
65.2%
11
58.0%
61.0%
70.8%
45.8%
65.1%
71.1%
61.5%
62.8%
63.8%
65.2%
12
69.0%
65.0%
68.8%
45.8%
65.1%
71.1%
50.0%
62.8%
63.8%
65.2%
13
64.0%
65.0%
66.6%
45.8%
65.1%
71.1%
52.4%
62.8%
63.8%
65.2%
14
61.0%
60.0%
66.6%
45.8%
65.1%
71.1%
65.2%
62.8%
63.8%
65.2%
15
60.0%
53.0%
64.6%
45.8%
65.1%
71.1%
68.2%
62.8%
63.8%
65.2%
16
62.0%
67.0%
64.6%
45.8%
65.1%
71.1%
65.1%
62.8%
63.8%
65.2%
17
71.0%
57.0%
68.8%
45.8%
65.1%
71.1%
62.5%
62.8%
63.8%
65.2%
18
61.0%
60.0%
70.8%
45.8%
65.1%
71.1%
69.8%
62.8%
63.8%
65.2%
19
67.0%
61.0%
66.6%
45.8%
65.1%
71.1%
50.0%
62.8%
63.8%
65.2%
20
61.0%
54.0%
64.6%
45.8%
65.1%
71.1%
63.6%
62.8%
63.8%
65.2%
21
61.0%
65.0%
70.8%
45.8%
65.1%
71.1%
53.3%
62.8%
63.8%
65.2%
22
64.0%
64.0%
66.6%
45.8%
65.1%
71.1%
57.8%
62.8%
63.8%
65.2%
23
58.0%
62.0%
72.9%
45.8%
65.1%
71.1%
51.2%
62.8%
63.8%
65.2%
24
67.0%
57.0%
68.8%
45.8%
65.1%
71.1%
60.9%
62.8%
63.8%
65.2%
25
62.0%
65.0%
68.8%
45.8%
65.1%
71.1%
57.8%
62.8%
63.8%
65.2%
26
64.0%
56.0%
75.0%
45.8%
65.1%
71.1%
55.3%
62.8%
63.8%
65.2%
27
61.0%
64.0%
68.8%
45.8%
65.1%
71.1%
56.6%
62.8%
63.8%
65.2%
28
64.0%
58.0%
58.3%
45.8%
65.1%
71.1%
58.5%
62.8%
63.8%
65.2%
29
60.0%
68.0%
66.6%
45.8%
65.1%
71.1%
57.8%
62.8%
63.8%
65.2%
30
64.0%
58.0%
70.8%
45.8%
65.1%
71.1%
58.8%
62.8%
63.8%
65.2%
Best
71.0%
68.0%
75.0%
45.8%
65.1%
71.1%
69.8%
62.8%
63.8%
65.2%
Worst
54.0%
53.0%
58.3%
45.8%
65.1%
71.1%
45.5%
62.8%
63.8%
65.2%
Mean
62.8%
61.0%
67.9%
45.8%
65.1%
71.1%
59.1%
62.8%
63.8%
65.2%
SD
0.040
0.040
0.037
0.000
0.000
0.000
0.058
0.000
0.000
0.000
Neural Computing and Applications (2024) 36:13715–13730
13727
123

---

## Page 14
sensitivity standards were taken as 71%, 72%, 69%, 67%,
respectively. Figure 8 presents the confusion matrix of the
proposed model during training and testing.
The performance of ten models of machine learning and
deep learning algorithms and the proposed model are
summarized in Table 2. All ten models were trained on the
same dataset. The training and validation process for all
algorithms was repeated 30 times, and the accuracy of each
stage was recorded separately.
We also used another method to measure model per-
formance called the AUC-ROC curve, as shown in Fig. 9.
It is one of the evaluation tools approved in the classiﬁ-
cation. This graph measures the performance of the clas-
siﬁcation model when there are only two classes, a positive
class and a negative class. This curve indicates a ROC
curve that plots the False Positive Rate (FPR) on the hor-
izontal axis (X) against the True Positive Rate (TPR) on the
vertical axis (Y).
AUC-ROC is the area under this graph. If the area under
the curve is large, this indicates good performance of the
model in distinguishing between positive and negative
classes. Therefore, we notice that the threshold value is
close to 1, and therefore, the area covered by this curve is
larger. Therefore, the model has good performance. This
curve is found based on the confusion matrix values
mentioned previously. Emphasis is also placed on positive
and negative values in the model’s performance.
Figure 9a represents a curve for the results of the
training period, while ﬁgure (b) represents the results for
the validation period. When the model’s performance
improves, the vertical axis values become close to 1, while
the horizontal axis values become close to 0. For each of
the two ﬁgures listed above, A and B.
Figure 10 conﬁrms the superior performance of the RF
algorithm compared to all other algorithms, with an aver-
age accuracy of 71.1%. (ANN) Deep learning model results
secured the second position, achieving an average accuracy
of 67.9%. Meanwhile, NB and KNN demonstrated com-
mendable average performance. In terms of the highest
accuracy, the (ANN) deep learning model took the lead
with 75%, followed by the RF algorithm at 71.1%. While
the model proposed in this paper showed the third-best
performance, achieving an accuracy of 71%. However, the
remaining seven models exhibited lower and unsatisfactory
performance compared to (SVC), as indicated in Table 3.
For other statistical metrics such as F1 score, sensitivity
and accuracy, their ranges did not differ signiﬁcantly from
the accuracy measure.
The performance of our custom architectural model
trained from scratch using aABC algorithm can be com-
pared to other machine learning models. In fact, the pro-
posed model could not outperform DL or even RF. While it
was able to show better results than the rest. It is also noted
from Table 3 that the proposed model with DL, bagging
classiﬁer, changes the accuracy of each model every time it
is tested, while the models such as SVC, KNN, RF, NB and
decision tree maintained one result throughout the testing
period. That is, algorithms that rely on a statistical prin-
ciple are more stable than learning algorithms, although
they did not outperform learning algorithms in their best
performance, which is conﬁrmed by the statistical mea-
sures in Table 3.
In this paper, they relied on collected dataset from
people with the disease and suspects. They were collected
at the bmj center. Our study differs from previous studies in
this respect. This appears clearly if we look at the differ-
ence between the results obtained in this study and the
results of previous research. Our goal was to obtain an
early detection model of the disease using the clinical
symptoms that appear on the person when suspected.
5 Conclusion
The paper provides a brief summary of the emergence of
the monkeypox virus, a zoonotic disease transmitted from
animals to humans. This virus belongs to the highly viru-
lent Orthopoxvirus family. The spread of this disease in
societies alarms many people. Therefore, society needs an
automated system for early detection that helps detect
infection with this disease if it occurs. Early prediction can
prevent complications for people with the disease and save
human lives. This study aims to provide a model for dis-
tinguishing monkeypox infection by the clinical symptoms
associated with the disease that appear on the infected
person. The proposed model hybridized aABC algorithm
with ANN. Several models trained on the same training
datasets were compared. The ANN deep learning model
achieved the best performance with an accuracy of 75%,
while the proposed model obtained an accuracy of 71%.
The proposed model is supported by several published
studies that use an AI-based diagnostic model. We hope
this article will contribute to future researchers and prac-
titioners beneﬁting from the presented approach to develop
a diagnostic mechanism for monkeypox disease. In the next
study, we plan to prepare an AI method that can extract
features for monkeypox using real-time data and classify
them at a higher accuracy rate.
Appendix
See Table 4 .
13728
Neural Computing and Applications (2024) 36:13715–13730
123

---

## Page 15
Funding Open access funding provided by the Scientiﬁc and Tech-
nological Research Council of Tu¨rkiye (TU¨ BI˙TAK).
Data availability The collected data is available as open data via an
online data repository: https://doi.org/https://doi.org/10.34740/KAG
GLE/DSV/4271503.
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
1. Singh S, Rao A, Kumar K, Mishra A, Prajapati VK (2023)
Translational vaccinomics and structural ﬁltration algorithm to
device multiepitope vaccine for catastrophic monkeypox virus.
Comput Biol Med. https://doi.org/10.1016/j.compbiomed.2022.
106497
2. Shahyeez Ahamed BSH, Usha R, Sreenivasulu G (2022) A deep
learning-based methodology for predicting monkey pox from
skin sores. In: MysuruCon 2022 - 2022 IEEE 2nd Mysore Sub
Section International Conference. https://doi.org/10.1109/Mysur
uCon55714.2022.9972746
3. Rimmer S, Barnacle J, Gibani MM, Wu MS, Dissanayake O,
Mehta R, Herdman T, Gilchrist M, Muir D, Ebrahimsa U, Mora-
Peris B, Dosekun O, Garvey L, Peters J, Davies F, Cooke G,
Abbara A (2023) The clinical presentation of monkeypox: a
retrospective case-control study of patients with possible or
probable monkeypox in a West London cohort. Int J Infect Dis
126:48–53. https://doi.org/10.1016/j.ijid.2022.11.020
4. Yinka-Ogunleye A, Aruna O, Dalhat M, Ogoina D, McCollum A,
Disu Y, Mamadu I, Akinpelu A, Ahmad A, Burga J, Ndoreraho
A, Nkunzimana E, Manneh L, Mohammed A, Adeoye O, Tom-
Aba D, Silenou B, Ipadeola O, Saleh M, Satheshkumar PS (2019)
Outbreak of human monkeypox in Nigeria in 2017–18: a clinical
and epidemiological report. Lancet Infect Dis 19(8):872–879.
https://doi.org/10.1016/S1473-3099(19)30294-4
5. Rodrı´guez BS, Guzma´n Herrador BR, Franco AD, Sa´nchez-Seco
Farin˜as MP, del Amo Valero J, Aginagalde Llorente AH, Pe´rez
de Agreda JPA, Malonda RC, Castrillejo D, Chirlaque Lo´pez
MD, Chong EJ, Balbuena SF, Garcı´a VG, Garcı´a-Cenoz M,
Herna´ndez LG, Montalba´n EG, Carril FG, Cortijo TG, Bueno SJ,
Iba´n˜ez Pe´rez AC (2022) Epidemiologic features and control
measures during monkeypox outbreak, Spain, June 2022. Emerg
Infect Dis 28(9):1847–1851. https://doi.org/10.3201/EID2809.
221051
6. Kannan SR, Sachdev S, Reddy AS, Kandasamy SL, Byrareddy
SN, Lorson CL, Singh K (2022) Mutations in the monkeypox
virus replication complex: Potential contributing factors to the
2022 outbreak. J Autoimmun. https://doi.org/10.1016/j.jaut.2022.
102928
7. Thornhill JP, Barkati S, Walmsley S, Rockstroh J, Antinori A,
Harrison LB, Palich R, Nori A, Reeves I, Habibi MS, Apea V,
Boesecke C, Vandekerckhove L, Yakubovsky M, Sendagorta E,
Blanco JL, Florence E, Moschese D, Maltez FM, Orkin CM
(2022) Monkeypox virus infection in humans across 16 coun-
tries—April–June 2022. New England J Med 387(8):679–691.
https://doi.org/10.1056/nejmoa2207323
8. Dwivedi M, Tiwari RG, Ujjwal N (2023). Deep learning methods
for early detection of monkeypox skin lesion. pp 343–348. https://
doi.org/10.1109/icsc56524.2022.10009571
9. Patel A, Bilinska J, Tam JCH, Da Silva Fontoura D, Mason CY,
Daunt A, Snell LB, Murphy J, Potter J, Tuudah C, Sundramoorthi
R, Abeywickrema M, Pley C, Naidu V, Nebbia G, Aarons E,
Botgros A, Douthwaite ST, Pannerden VNT (2022) Clinical
features and novel presentations of human monkeypox in a
central London centre during the 2022 outbreak: descriptive case
series. The BMJ. https://doi.org/10.1136/bmj-2022-072410
10. Silva MST, dos Santos DG, Coutinho C, Ribeiro MPD, Cardoso
SW, Veloso VG, Grinsztejn B (2022) The ﬁrst case of acute HIV
and monkeypox coinfection in Latin America. Braz J Infect Dis.
https://doi.org/10.1016/j.bjid.2022.102736
11. Matuszewski DJ, Sintorn IM (2021) TEM virus images: Bench-
mark dataset and deep learning classiﬁcation. Comput Methods
Progr Biomed. https://doi.org/10.1016/j.cmpb.2021.106318
12. Ahsan MM, Uddin MR, Ali MS, Islam MK, Farjana M, Sakib
AN, Momin K. Al, Luna SA (2023) Deep transfer learning
approaches for Monkeypox disease diagnosis. Expert Syst Appl.
https://doi.org/10.1016/j.eswa.2022.119483
13. Saleh AI, Rabie AH (2023) Human monkeypox diagnose (HMD)
strategy based on data mining and artiﬁcial intelligence tech-
niques. Comput Biol Med. https://doi.org/10.1016/j.compbiomed.
2022.106383
14. Guo K, Chen T, Ren S, Li N, Hu M, Kang J (2022) Federated
learning empowered real-time medical data processing method
for smart healthcare. IEEE/ACM Trans Comput Biol Bioinf.
https://doi.org/10.1109/TCBB.2022.3185395
15. Zhu X, Guo K, Ren S, Hu B, Hu M, Fang H (2022) Lightweight
image super-resolution with expectation-maximization attention
Table 4 CEC2019 Benchmark functions [34]
No
Name
Area
Dimension
CEC01
Storn’s Chebyshev polynomial
ﬁtting problem
[- 8192,
8192]
9
CEC02
Inverse Hilbert matrix problem
[- 16384,
16384]
16
CEC03
Lennard–Jones minimum
energy cluster
[- 4, 4]
18
CEC04
Rastrigin’s function
[- 10, 10]
10
CEC05
Griewangk’s function
[- 10, 10]
10
CEC06
Weierstrass function
[- 10, 10]
10
CEC07
Modiﬁed Schwefel’s function
[- 10, 10]
10
CEC08
Expanded Schaffer’s F6
function
[- 10, 10]
10
CEC09
Happy cat function
[- 10, 10]
10
CEC10
Ackley function
[- 10, 10]
10
Neural Computing and Applications (2024) 36:13715–13730
13729
123

---

## Page 16
mechanism.
IEEE
Trans
Circuits
Syst
Video
Technol
32(3):1273–1284. https://doi.org/10.1109/TCSVT.2021.3078436
16. Guo K, Shen C, Hu B, Hu M, Kui X (2023) RSNet: relation
separation network for few-shot similar class recognition. IEEE
Trans Multimed 25:3894–3904. https://doi.org/10.1109/TMM.
2022.3168146
17. Mohammedqasem R, Mohammedqasim H, Asad Ali Biabani S,
Ata O, Alomary MN, Almehmadi M, Amer Alsairi A, Azam
Ansari M (2023) Multi-objective deep learning framework for
COVID-19 dataset problems. J King Saud Univ - Sci. https://doi.
org/10.1016/j.jksus.2022.102527
18. Lee VH, Hew JJ, Leong LY, Tan GWH, Ooi KB (2020) Wear-
able payment: a deep learning-based dual-stage SEM-ANN
analysis. Expert Syst Appl. https://doi.org/10.1016/j.eswa.2020.
113477
19. Pham BT, Nguyen MD, van Dao D, Prakash I, Ly HB, Le TT, Ho
LS, Nguyen KT, Ngo TQ, Hoang V, Son LH, Ngo HTT, Tran
HT, Do NM, van Le H, Ho HL, Tien Bui D (2019) Development
of artiﬁcial intelligence models for the prediction of compression
coefﬁcient of soil: an application of Monte Carlo sensitivity
analysis. Sci Total Environ 679:172–184. https://doi.org/10.1016/
j.scitotenv.2019.05.061
20. Yadav RK (2020) PSO-GA based hybrid with adam optimization
for ANN training with application in medical diagnosis. Cogn
Syst Res 64:191–199. https://doi.org/10.1016/j.cogsys.2020.08.
011
21. Veza I, Irianto Panchal H, Paristiawan PA, Idris M, Fattah IMR,
Putra NR, Silambarasan R (2022) Improved prediction accuracy
of biomass heating value using proximate analysis with various
ANN training algorithms. Res Eng. https://doi.org/10.1016/j.
rineng.2022.100688
22. Chen S, Ren Y, Friedrich D, Yu Z, Yu J (2020) Sensitivity
analysis to reduce duplicated features in ANN training for district
heat demand prediction. Energy and A I:2. https://doi.org/10.
1016/j.egyai.2020.100028
23. O¨ zdog˘an H, U¨ ncu¨ YA, S¸ekerci M, Kaplan A (2023) Estimations
for (n, a) reaction cross sections at around 14.5MeV using
Levenberg–Marquardt algorithm-based artiﬁcial neural network.
Appl Radiat Isot. https://doi.org/10.1016/j.apradiso.2022.110609
24. de Oliveira FR, de Oliveira FR (2023) A locally convergent
inexact projected Levenberg–Marquardt-type algorithm for large-
scale constrained nonsmooth equations. J Comput Appl Math.
https://doi.org/10.1016/j.cam.2023.115121
25. Kabalci Y, Kockanat S, Kabalci E (2018) A modiﬁed ABC
algorithm approach for power system harmonic estimation
problems. Electric Power Syst Res 154:160–173. https://doi.org/
10.1016/j.epsr.2017.08.019
26. Al-Ammar EA, Farzana K, Waqar A, Aamir M, Saifullah UH
(2021) ABC algorithm based optimal sizing and placement of
DGs in distribution networks considering multiple objectives. Ain
Shams Eng J 12(1):697–708. https://doi.org/10.1016/j.asej.2020.
05.002
27. Naidu K, Mokhlis H, Bakar AHA, Terzija V (2017) Performance
investigation of ABC algorithm in multi-area power system with
multiple
interconnected
generators.
Appl
Soft
Comput
J
57:436–451. https://doi.org/10.1016/j.asoc.2017.03.044
28. Hancer E, Xue B, Karaboga D, Zhang M (2015) A binary ABC
algorithm based on advanced similarity scheme for feature
selection. Appl Soft Comput J 36:334–348. https://doi.org/10.
1016/j.asoc.2015.07.023
29. Singh S, Chauhan P, Singh NJ (2020) Capacity optimization of
grid connected solar/fuel cell energy system using hybrid ABC-
PSO algorithm. Int J Hydrogen Energy 45(16):10070–10088.
https://doi.org/10.1016/j.ijhydene.2020.02.018
30. Najari S, Gro´f G, Saeidi S, Gallucci F (2019) Modeling and
optimization of hydrogenation of CO 2: estimation of kinetic
parameters via artiﬁcial bee colony (ABC) and differential evo-
lution
(DE)
algorithms.
Int
J
Hydrogen
Energy
44(10):4630–4649.
https://doi.org/10.1016/j.ijhydene.2019.01.
020
31. Karaboga D, Akay B (2011) A modiﬁed artiﬁcial bee colony
(ABC) algorithm for constrained optimization problems. Appl
Soft Comput J 11(3):3021–3031. https://doi.org/10.1016/j.asoc.
2010.12.001
32. Wang H, Wu Z, Rahnamayan S, Sun H, Liu Y, Pan JS (2014)
Multi-strategy ensemble artiﬁcial bee colony algorithm. Inf Sci
279:587–603. https://doi.org/10.1016/j.ins.2014.04.013
33. Kapila D, Bhagat N (2021) Efﬁcient feature selection technique
for brain tumor classiﬁcation utilizing hybrid fruit ﬂy based abc
and ann algorithm. Mater Today: Proc 51:12–20. https://doi.org/
10.1016/j.matpr.2021.04.089
34. Singh P, Mittal N (2021) An efﬁcient localization approach to
locate sensor nodes in 3D wireless sensor networks using adap-
tive
ﬂower
pollination
algorithm.
Wireless
Netw
27(3):1999–2014. https://doi.org/10.1007/s11276-021-02557-7
35. Yang
X-S
(n.d.)
Flower
pollination
algorithm
for
global
optimization
36. Mirjalili S, Mirjalili SM, Lewis A (2014) Grey Wolf Optimizer.
Adv Eng Softw 69:46–61. https://doi.org/10.1016/j.advengsoft.
2013.12.007
37. Mirjalili S, Gandomi AH, Mirjalili SZ, Saremi S, Faris H, Mir-
jalili SM (2017) Salp swarm algorithm: a bio-inspired optimizer
for engineering design problems. Adv Eng Softw 114:163–191.
https://doi.org/10.1016/j.advengsoft.2017.07.002
38. Yang X-S, and Deb S (2010) Cuckoo search via levy ﬂights.
http://arxiv.org/abs/1003.1594
39. Mirjalili S (2016) SCA: A sine cosine algorithm for solving
optimization problems. Knowl-Based Syst 96:120–133. https://
doi.org/10.1016/j.knosys.2015.12.022
40. Monkey-Pox
PATIENTS
Dataset.|Kaggle.
(n.d.).
Retrieved
March 15, 2023, from https://www.kaggle.com/datasets/muham
mad4hmed/monkeypox-patients-dataset
41. Monkeypox Skin Lesion Dataset | Kaggle. (n.d.). Retrieved
March 15, 2023, from https://www.kaggle.com/datasets/naﬁn59/
monkeypox-skin-lesion-dataset
42. Ali SN, Ahmed MT, Paul J, Jahan T, Sani SM, Noor N, Hasan T
(2022) Monkeypox skin lesion detection using deep learning
models: a feasibility study. https://www.kaggle.com/datasets/
naﬁn59/monkeypox-skin-lesion-dataset
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
13730
Neural Computing and Applications (2024) 36:13715–13730
123

---
