# 2021_tabnet_attentive_interpretable_tabular_learning

**Source File**: `article\references\nca_search\papers\04_mlp_optimization\2021_tabnet_attentive_interpretable_tabular_learning.pdf`
**Total Pages**: 9

---

<!-- Page 1 -->
## Page 1

TabNet: Attentive Interpretable Tabular Learning
Sercan ¨O. Arık, Tomas Pﬁster
Google Cloud AI
Sunnyvale, CA
soarik@google.com, tpﬁster@google.com
Abstract
We propose a novel high-performance and interpretable canon-
ical deep tabular data learning architecture, TabNet. TabNet
uses sequential attention to choose which features to reason
from at each decision step, enabling interpretability and more
efﬁcient learning as the learning capacity is used for the most
salient features. We demonstrate that TabNet outperforms
other variants on a wide range of non-performance-saturated
tabular datasets and yields interpretable feature attributions
plus insights into its global behavior. Finally, we demonstrate
self-supervised learning for tabular data, signiﬁcantly improv-
ing performance when unlabeled data is abundant.
Introduction
Deep neural networks (DNNs) have shown notable success
with images (He et al. 2015), text (Lai et al. 2015) and audio
(Amodei et al. 2015). For these, canonical architectures that
efﬁciently encode the raw data into meaningful representa-
tions, fuel the rapid progress. One data type that has yet to
see such success with a canonical architecture is tabular data.
Despite being the most common data type in real-world
AI (as it is comprised of any categorical and numerical fea-
tures), (Chui et al. 2018), deep learning for tabular data re-
mains under-explored, with variants of ensemble decision
trees (DTs) still dominating most applications (Bansal 2020).
Why? First, because DT-based approaches have certain bene-
ﬁts: (i) they are representionally efﬁcient for decision mani-
folds with approximately hyperplane boundaries which are
common in tabular data; and (ii) they are highly interpretable
in their basic form (e.g. by tracking decision nodes) and there
are popular post-hoc explainability methods for their ensem-
ble form, e.g. (Lundberg, Erion, and Lee 2018) – this is an
important concern in many real-world applications; (iii) they
are fast to train. Second, because previously-proposed DNN
architectures are not well-suited for tabular data: e.g. stacked
convolutional layers or multi-layer perceptrons (MLPs) are
vastly overparametrized – the lack of appropriate inductive
bias often causes them to fail to ﬁnd optimal solutions for tab-
ular decision manifolds (Goodfellow, Bengio, and Courville
2016; Shavitt and Segal 2018; Xu et al. 2019).
Why is deep learning worth exploring for tabular data?
One obvious motivation is expected performance improve-
Copyright c⃝2021, Association for the Advancement of Artiﬁcial
Intelligence (www.aaai.org). All rights reserved.
ments particularly for large datasets (Hestness et al. 2017). In
addition, unlike tree learning, DNNs enable gradient descent-
based end-to-end learning for tabular data which can have a
multitude of beneﬁts: (i) efﬁciently encoding multiple data
types like images along with tabular data; (ii) alleviating the
need for feature engineering, which is currently a key aspect
in tree-based tabular data learning methods; (iii) learning
from streaming data and perhaps most importantly (iv) end-
to-end models allow representation learning which enables
many valuable application scenarios including data-efﬁcient
domain adaptation (Goodfellow, Bengio, and Courville 2016),
generative modeling (Radford, Metz, and Chintala 2015) and
semi-supervised learning (Dai et al. 2017).
We propose a new canonical DNN architecture for tabular
data, TabNet. The main contributions are summarized as:
1. TabNet inputs raw tabular data without any preprocessing
and is trained using gradient descent-based optimization,
enabling ﬂexible integration into end-to-end learning.
2. TabNet uses sequential attention to choose which fea-
tures to reason from at each decision step, enabling in-
terpretability and better learning as the learning capacity
is used for the most salient features (see Fig. 1). This
feature selection is instance-wise, e.g. it can be different
for each input, and unlike other instance-wise feature se-
lection methods like (Chen et al. 2018) or (Yoon, Jordon,
and van der Schaar 2019), TabNet employs a single deep
learning architecture for feature selection and reasoning.
3. Above design choices lead to two valuable properties: (i)
TabNet outperforms or is on par with other tabular learn-
ing models on various datasets for classiﬁcation and re-
gression problems from different domains; and (ii) TabNet
enables two kinds of interpretability: local interpretability
that visualizes the importance of features and how they
are combined, and global interpretability which quantiﬁes
the contribution of each feature to the trained model.
4. Finally, for the ﬁrst time for tabular data, we show signif-
icant performance improvements by using unsupervised
pre-training to predict masked features (see Fig. 2).
Related Work
Feature selection: Feature selection broadly refers to judi-
ciously picking a subset of features based on their useful-
ness for prediction. Commonly-used techniques such as for-
ward selection and Lasso regularization (Guyon and Elisseeff
The Thirty-Fifth AAAI Conference on Artificial Intelligence (AAAI-21)
6679


---

<!-- Page 2 -->
## Page 2

Feature selection
Input processing
Aggregate information
Feature selection
Input processing
Predicted output (whether the income level >$50k)
Professional occupation related
Investment related
Input features
Feedback from 
previous step
Feedback to 
next step
…
…
Figure 1: TabNet’s sparse feature selection exempliﬁed for Adult Census Income prediction (Dua and Graff 2017). Sparse feature
selection enables interpretability and better learning as the capacity is used for the most salient features. TabNet employs multiple
decision blocks that focus on processing a subset of input features for reasoning. Two decision blocks shown as examples process
features that are related to professional occupation and investments, respectively, in order to predict the income level.
Age
Cap. gain
Education
Occupation
Gender
Relationship
53
200000
?
Exec-managerial
F
Wife
19
0
?
Farming-fishing
M
?
?
5000
Doctorate
Prof-specialty
M
Husband
25
?
?
Handlers-cleaners
F
Wife
59
300000
Bachelors
?
?
Husband
33
0
Bachelors
?
F
?
?
0
High-school
Armed-Forces
?
Husband
Age
Cap. gain
Education
Occupation
Gender
Relationship
Masters
High-school
Unmarried
43
0
High-school
F
Exec-managerial
M
Adm-clerical
Wife
39
M
Income > $50k
True
False
True
False
True
True
False
TabNet encoder
TabNet decoder
Decision making
Age
Cap. gain
Education
Occupation
Gender
Relationship
60
200000
Bachelors
Exec-managerial
M
Husband
23
0
High-school
Farming-fishing
M
Unmarried
45
5000
Doctorate
Prof-specialty
M
Husband
23
0
High-school
Handlers-cleaners
F
Wife
56
300000
Bachelors
Exec-managerial
M
Husband
38
10000
Bachelors
Prof-specialty
F
Wife
23
0
High-school
Armed-Forces
M
Husband
Unsupervised pre-training
Supervised fine-tuning
TabNet encoder
Figure 2: Self-supervised tabular learning. Real-world tabular datasets have interdependent feature columns, e.g., the education
level can be guessed from the occupation, or the gender can be guessed from the relationship. Unsupervised representation
learning by masked self-supervised learning results in an improved encoder model for the supervised learning task.
2003) attribute feature importance based on the entire training
data, and are referred as global methods. Instance-wise fea-
ture selection refers to picking features individually for each
input, studied in (Chen et al. 2018) with an explainer model
to maximize the mutual information between the selected
features and the response variable, and in (Yoon, Jordon, and
van der Schaar 2019) by using an actor-critic framework to
mimic a baseline while optimizing the selection. Unlike these,
TabNet employs soft feature selection with controllable spar-
sity in end-to-end learning – a single model jointly performs
feature selection and output mapping, resulting in superior
performance with compact representations.
Tree-based learning: DTs are commonly-used for tabular
data learning. Their prominent strength is efﬁcient picking
of global features with the most statistical information gain
(Grabczewski and Jankowski 2005). To improve the perfor-
mance of standard DTs, one common approach is ensembling
to reduce variance. Among ensembling methods, random
forests (Ho 1998) use random subsets of data with randomly
selected features to grow many trees. XGBoost (Chen and
Guestrin 2016) and LightGBM (Ke et al. 2017) are the two
recent ensemble DT approaches that dominate most of the
recent data science competitions. Our experimental results
for various datasets show that tree-based models can be out-
performed when the representation capacity is improved with
deep learning while retaining their feature selecting property.
Integration of DNNs into DTs: Representing DTs with
DNN building blocks as in (Humbird, Peterson, and McClar-
ren 2018) yields redundancy in representation and inefﬁ-
cient learning. Soft (neural) DTs (Wang, Aggarwal, and Liu
2017; Kontschieder et al. 2015) use differentiable decision
functions, instead of non-differentiable axis-aligned splits.
However, losing automatic feature selection often degrades
performance. In (Yang, Morillo, and Hospedales 2018), a soft
binning function is proposed to simulate DTs in DNNs. (Ke
et al. 2019) proposes a DNN architecture by explicitly lever-
6680


---

<!-- Page 3 -->
## Page 3

Mask
M: [1, 0]
Mask
M: [0, 1]
!"
!#
FC
W: [$", - $", 0, 0]
b: [-a $", a $", -1, -1]
%
&
[!", !#]
[!"]
[!#]
!" > %
!# < &
!" > %
!# > &
!" < %
!# > &
!" < %
!# < &
$"!" −$"%
−$"!" + $"%
−1
−1
FC
W: [0, 0, $# , - $# ]
b: [-1, -1, -d $#, d $# ]
−1
−1
$#!# −$#&
−$#!# + $#&
ReLU
+
Softmax
ReLU
Figure 3: Illustration of DT-like classiﬁcation using conventional DNN blocks (left) and the corresponding decision manifold
(right). Relevant features are selected by using multiplicative sparse masks on inputs. The selected features are linearly
transformed, and after a bias addition (to represent boundaries) ReLU performs region selection by zeroing the regions.
Aggregation of multiple regions is based on addition. As C1 and C2 get larger, the decision boundary gets sharper.
aging expressive feature combinations, however, learning is
based on transferring knowledge from gradient-boosted DT.
(Tanno et al. 2018) proposes a DNN architecture by adap-
tively growing from primitive blocks. TabNet differs from
these as it embeds soft feature selection with controllable
sparsity via sequential attention.
Self-supervised learning: Unsupervised representation
learning improves supervised learning especially in small
data regime (Raina et al. 2007). Recent work for text (Devlin
et al. 2018) and image (Trinh, Luong, and Le 2019) data
has shown signiﬁcant advances – driven by the judicious
choice of the unsupervised learning objective (masked input
prediction) and attention-based deep learning.
TabNet for Tabular Learning
DTs are successful for learning from real-world tabular
datasets. With a speciﬁc design, conventional DNN building
blocks can be used to implement DT-like output manifold,
e.g. see Fig. 3). In such a design, individual feature selec-
tion is key to obtain decision boundaries in hyperplane form,
which can be generalized to a linear combination of features
where coefﬁcients determine the proportion of each feature.
TabNet is based on such functionality and it outperforms DTs
while reaping their beneﬁts by careful design which: (i) uses
sparse instance-wise feature selection learned from data; (ii)
constructs a sequential multi-step architecture, where each
step contributes to a portion of the decision based on the
selected features; (iii) improves the learning capacity via non-
linear processing of the selected features; and (iv) mimics
ensembling via higher dimensions and more steps.
Fig. 4 shows the TabNet architecture for encoding tabu-
lar data. We use the raw numerical features and consider
mapping of categorical features with trainable embeddings.
We do not consider any global feature normalization, but
merely apply batch normalization (BN). We pass the same D-
dimensional features f ∈ℜB×D to each decision step, where
B is the batch size. TabNet’s encoding is based on sequential
multi-step processing with Nsteps decision steps. The ith
step inputs the processed information from the (i −1)th step
to decide which features to use and outputs the processed
feature representation to be aggregated into the overall deci-
sion. The idea of top-down attention in the sequential form
is inspired by its applications in processing visual and text
data (Hudson and Manning 2018) and reinforcement learn-
ing (Mott et al. 2019) while searching for a small subset of
relevant information in high dimensional input.
Feature selection: We employ a learnable mask M[i] ∈
ℜB×D for soft selection of the salient features. Through
sparse selection of the most salient features, the learning
capacity of a decision step is not wasted on irrelevant
ones, and thus the model becomes more parameter efﬁ-
cient. The masking is multiplicative, M[i] · f. We use an
attentive transformer (see Fig. 4) to obtain the masks us-
ing the processed features from the preceding step, a[i −1]:
M[i] = sparsemax(P[i −1] · hi(a[i −1])). Sparsemax nor-
malization (Martins and Astudillo 2016) encourages sparsity
by mapping the Euclidean projection onto the probabilistic
simplex, which is observed to be superior in performance and
aligned with the goal of sparse feature selection for explain-
ability. Note that PD
j=1 M[i]b,j = 1. hi is a trainable func-
tion, shown in Fig. 4 using a FC layer, followed by BN. P[i]
is the prior scale term, denoting how much a particular feature
has been used previously: P[i] = Qi
j=1(γ −M[j]), where γ
is a relaxation parameter – when γ = 1, a feature is enforced
to be used only at one decision step and as γ increases, more
ﬂexibility is provided to use a feature at multiple decision
steps. P[0] is initialized as all ones, 1B×D, without any prior
on the masked features. If some features are unused (as in self-
supervised learning), corresponding P[0] entries are made 0
to help model’s learning. To further control the sparsity of the
selected features, we propose sparsity regularization in the
form of entropy (Grandvalet and Bengio 2004), Lsparse =
PNsteps
i=1
PB
b=1
PD
j=1
−Mb,j[i] log(Mb,j[i]+ϵ)
Nsteps·B
, where ϵ is a
small number for numerical stability. We add the sparsity reg-
ularization to the overall loss, with a coefﬁcient λsparse. Spar-
sity provides a favorable inductive bias for datasets where
most features are redundant.
Feature processing: We process the ﬁltered features using
a feature transformer (see Fig. 4) and then split for the
decision step output and information for the subsequent
step, [d[i], a[i]] = fi(M[i] · f), where d[i] ∈ℜB×Nd and
a[i] ∈ℜB×Na. For parameter-efﬁcient and robust learning
with high capacity, a feature transformer should comprise
layers that are shared across all decision steps (as the same
features are input across different decision steps), as well as
6681


---

<!-- Page 4 -->
## Page 4

Features
Feature 
transformer
Mask
Attentive 
transformer
+
Step 1
BN
Split
Split
…
ReLU
Mask
Attentive 
transformer
Split
ReLU
Step 2
Output
+
Feature 
transformer
Feature 
transformer
Agg.
Feature
attributes
+
Agg.
+
…
…
FC
(a) TabNet encoder architecture
Feature 
transformer
Step 1
+
Encoded representation
…
Reconstructed 
features
FC
Feature 
transformer
Step 2
FC
…
…
(b) TabNet decoder architecture
Feature 
transformer
+
FC
BN
GLU
FC
BN
GLU
+
FC
BN
GLU
0.5
+
FC
BN
GLU
0.5
0.5
Shared across decision steps
Decision step dependent
(c)
Attentive 
transformer
FC
BN
Sparsemax
+
Prior scales
+
(d)
Figure 4: (a) TabNet encoder, composed of a feature transformer, an attentive transformer and feature masking. A split block
divides the processed representation to be used by the attentive transformer of the subsequent step as well as for the overall
output. For each step, the feature selection mask provides interpretable information about the model’s functionality, and the
masks can be aggregated to obtain global feature important attribution. (b) TabNet decoder, composed of a feature transformer
block at each step. (c) A feature transformer block example – 4-layer network is shown, where 2 are shared across all decision
steps and 2 are decision step-dependent. Each layer is composed of a fully-connected (FC) layer, BN and GLU nonlinearity. (d)
An attentive transformer block example – a single layer mapping is modulated with a prior scale information which aggregates
how much each feature has been used before the current decision step. sparsemax (Martins and Astudillo 2016) is used for
normalization of the coefﬁcients, resulting in sparse selection of the salient features.
decision step-dependent layers. Fig. 4 shows the implementa-
tion as concatenation of two shared layers and two decision
step-dependent layers. Each FC layer is followed by BN and
gated linear unit (GLU) nonlinearity (Dauphin et al. 2016),
eventually connected to a normalized residual connection
with normalization. Normalization with
√
0.5 helps to sta-
bilize learning by ensuring that the variance throughout the
network does not change dramatically (Gehring et al. 2017).
For faster training, we use large batch sizes with BN. Thus,
except the one applied to the input features, we use ghost BN
(Hoffer, Hubara, and Soudry 2017) form, using a virtual batch
size BV and momentum mB. For the input features, we ob-
serve the beneﬁt of low-variance averaging and hence avoid
ghost BN. Finally, inspired by decision-tree like aggregation
as in Fig. 3, we construct the overall decision embedding
as dout = PNsteps
i=1
ReLU(d[i]). We apply a linear mapping
Wﬁnaldout to get the output mapping.1
Interpretability: TabNet’s feature selection masks can shed
light on the selected features at each step. If Mb,j[i] = 0,
then jth feature of the bth sample should have no contribution
to the decision. If fi were a linear function, the coefﬁcient
Mb,j[i] would correspond to the feature importance of fb,j.
Although each decision step employs non-linear processing,
1For discrete outputs, we additionally employ softmax during
training (and argmax during inference).
their outputs are combined later in a linear way. We aim
to quantify an aggregate feature importance in addition to
analysis of each step. Combining the masks at different steps
requires a coefﬁcient that can weigh the relative importance
of each step in the decision. We simply propose ηb[i] =
PNd
c=1 ReLU(db,c[i]) to denote the aggregate decision con-
tribution at ith decision step for the bth sample. Intuitively, if
db,c[i] < 0, then all features at ith decision step should have
0 contribution to the overall decision. As its value increases,
it plays a higher role in the overall linear combination. Scal-
ing the decision mask at each decision step with ηb[i], we
propose the aggregate feature importance mask, Magg−b,j =
PNsteps
i=1
ηb[i]Mb,j[i]
. PD
j=1
PNsteps
i=1
ηb[i]Mb,j[i].2
Tabular self-supervised learning: We propose a decoder
architecture to reconstruct tabular features from the Tab-
Net encoded representations. The decoder is composed of
feature transformers, followed by FC layers at each deci-
sion step. The outputs are summed to obtain the recon-
structed features. We propose the task of prediction of miss-
ing feature columns from the others. Consider a binary mask
S ∈{0, 1}B×D. The TabNet encoder inputs (1 −S) · ˆf
and the decoder outputs the reconstructed features, S · ˆf. We
initialize P[0] = (1 −S) in encoder so that the model em-
2Normalization is used to ensure PD
j=1 Magg−b,j = 1.
6682


---

<!-- Page 5 -->
## Page 5

Model
Test AUC
Syn1
Syn2
Syn3
Syn4
Syn5
Syn6
No selection
.578 ± .004
.789 ± .003
.854 ± .004
.558 ± .021
.662 ± .013
.692 ± .015
Tree
.574 ± .101
.872 ± .003
.899 ± .001
.684 ± .017
.741 ± .004
.771 ± .031
Lasso-regularized
.498 ± .006
.555 ± .061
.886 ± .003
.512 ± .031
.691 ± .024
.727 ± .025
L2X
.498 ± .005
.823 ± .029
.862 ± .009
.678 ± .024
.709 ± .008
.827 ± .017
INVASE
.690 ± .006
.877 ± .003
.902 ± .003
.787 ± .004
.784 ± .005
.877 ± .003
Global
.686 ± .005
.873 ± .003
.900 ± .003
.774 ± .006
.784 ± .005
.858 ± .004
TabNet
.682 ± .005
.892 ± .004
.897 ± .003
.776 ± .017
.789 ± .009
.878 ± .004
Table 1: Mean and std. of test area under the receiving operating characteristic curve (AUC) on 6 synthetic datasets from (Chen
et al. 2018), for TabNet vs. other feature selection-based DNN models: No sel.: using all features without any feature selection,
Global: using only globally-salient features, Tree Ensembles (Geurts, Ernst, and Wehenkel 2006), Lasso-regularized model, L2X
(Chen et al. 2018) and INVASE (Yoon, Jordon, and van der Schaar 2019). Bold numbers denote the best for each dataset.
phasizes merely on the known features, and the decoder’s last
FC layer is multiplied with S to output the unknown features.
We consider the reconstruction loss in self-supervised phase:
PB
b=1
PD
j=1

(ˆfb,j−fb,j)·Sb,j
√PB
b=1(fb,j−1/B PB
b=1 fb,j)2

2
. Normalization
with the population standard deviation of the ground truth
is beneﬁcial, as the features may have different ranges. We
sample Sb,j independently from a Bernoulli distribution with
parameter ps, at each iteration.
Experiments
We study TabNet in wide range of problems, that contain
regression or classiﬁcation tasks, particularly with published
benchmarks. For all datasets, categorical inputs are mapped
to a single-dimensional trainable scalar with a learnable em-
bedding and numerical columns are input without and pre-
processing.3 We use standard classiﬁcation (softmax cross
entropy) and regression (mean squared error) loss functions
and we train until convergence. Hyperparameters of the Tab-
Net models are optimized on a validation set and listed in
Appendix. TabNet performance is not very sensitive to most
hyperparameters as shown with ablation studies in Appendix.
In Appendix, we also present ablation studies on various de-
sign and guidelines on selection of the key hyperparameters.
For all experiments we cite, we use the same training, val-
idation and testing data split with the original work. Adam
optimization algorithm (Kingma and Ba 2014) and Glorot
uniform initialization are used for training of all models.4
Instance-wise Feature Selection
Selection of the salient features is crucial for high perfor-
mance, especially for small datasets. We consider 6 tabular
datasets from (Chen et al. 2018) (consisting 10k training
samples). The datasets are constructed in such a way that
only a subset of the features determine the output. For Syn1-
Syn3, salient features are same for all instances (e.g., the
output of Syn2 depends on features X3-X6), and global fea-
ture selection, as if the salient features were known, would
give high performance. For Syn4-Syn6, salient features are
3Specially-designed feature engineering, e.g. logarithmic trans-
formation of variables highly-skewed distributions, may further
improve the results but we leave it out of the scope of this paper.
4An open-source implementation will be released.
instance dependent (e.g., for Syn4, the output depends on ei-
ther X1-X2 or X3-X6 depending on the value of X11), which
makes global feature selection suboptimal. Table 1 shows that
TabNet outperforms others (Tree Ensembles (Geurts, Ernst,
and Wehenkel 2006), LASSO regularization, L2X (Chen
et al. 2018)) and is on par with INVASE (Yoon, Jordon, and
van der Schaar 2019). For Syn1-Syn3, TabNet performance
is close to global feature selection - it can ﬁgure out what
features are globally important. For Syn4-Syn6, eliminating
instance-wise redundant features, TabNet improves global
feature selection. All other methods utilize a predictive model
with 43k parameters, and the total number of parameters is
101k for INVASE due to the two other models in the actor-
critic framework. TabNet is a single architecture, and its size
is 26k for Syn1-Syn3 and 31k for Syn4-Syn6. The compact
representation is one of TabNet’s valuable properties.
Performance on Real-World Datasets
Model
Test accuracy (%)
XGBoost
89.34
LightGBM
89.28
CatBoost
85.14
AutoML Tables
94.95
TabNet
96.99
Table 2: Performance for Forest Cover Type dataset.
Forest Cover Type (Dua and Graff 2017): The task is clas-
siﬁcation of forest cover type from cartographic variables.
Table 2 shows that TabNet outperforms ensemble tree based
approaches that are known to achieve solid performance
(Mitchell et al. 2018). We also consider AutoML Tables 5, an
automated search framework based on ensemble of models
including DNN, gradient boosted DT, AdaNet (Cortes et al.
2016) and ensembles (?) with very thorough hyperparameter
search. A single TabNet without ﬁne-grained hyperparameter
search outperforms it.
Poker Hand (Dua and Graff 2017): The task is classiﬁca-
tion of the poker hand from the raw suit and rank attributes of
the cards. The input-output relationship is deterministic and
hand-crafted rules can get 100% accuracy. Yet, conventional
DNNs, DTs, and even their hybrid variant of deep neural DTs
5https://cloud.google.com/automl-tables/
6683


---

<!-- Page 6 -->
## Page 6

Model
Test accuracy (%)
DT
50.0
MLP
50.0
Deep neural DT
65.1
XGBoost
71.1
LightGBM
70.0
CatBoost
66.6
TabNet
99.2
Rule-based
100.0
Table 3: Performance for Poker Hand induction dataset.
(Yang, Morillo, and Hospedales 2018) severely suffer from
the imbalanced data and cannot learn the required sorting and
ranking operations (Yang, Morillo, and Hospedales 2018).
Tuned XGBoost, CatBoost, and LightGBM show very slight
improvements over them. TabNet outperforms other methods,
as it can perform highly-nonlinear processing with its depth,
without overﬁtting thanks to instance-wise feature selection.
Model
Test MSE
Model size
Random forest
2.39
16.7K
Stochastic DT
2.11
28K
MLP
2.13
0.14M
Adaptive neural tree
1.23
0.60M
Gradient boosted tree
1.44
0.99M
TabNet-S
1.25
6.3K
TabNet-M
0.28
0.59M
TabNet-L
0.14
1.75M
Table 4: Performance on Sarcos dataset. Three TabNet mod-
els of different sizes are considered.
Sarcos (Vijayakumar and Schaal 2000): The task is re-
gressing inverse dynamics of an anthropomorphic robot arm.
(Tanno et al. 2018) shows that decent performance with a
very small model is possible with a random forest. In the very
small model size regime, TabNet’s performance is on par
with the best model from (Tanno et al. 2018) with 100x more
parameters. When the model size is not constrained, TabNet
achieves almost an order of magnitude lower test MSE.
Model
Test acc. (%)
Model size
Sparse evolutionary MLP
78.47
81K
Gradient boosted tree-S
74.22
0.12M
Gradient boosted tree-M
75.97
0.69M
MLP
78.44
2.04M
Gradient boosted tree-L
76.98
6.96M
TabNet-S
78.25
81K
TabNet-M
78.84
0.66M
Table 5: Performance on Higgs Boson dataset. Two TabNet
models are denoted with -S and -M.
Higgs Boson (Dua and Graff 2017): The task is distinguish-
ing between a Higgs bosons process vs. background. Due to
its much larger size (10.5M instances), DNNs outperform DT
variants even with very large ensembles. TabNet outperforms
MLPs with more compact representations. We also compare
to the state-of-the-art evolutionary sparsiﬁcation algorithm
(Mocanu et al. 2018) that integrates non-structured sparsity
into training. With its compact representation, TabNet yields
almost similar performance to sparse evolutionary training
for the same number of parameters. Unlike sparse evolution-
ary training, the sparsity of TabNet is structured – it does not
degrade the operational intensity (Wen et al. 2016) and can
efﬁciently utilize modern multi-core processors.
Model
Test MSE
MLP
512.62
XGBoost
490.83
LightGBM
504.76
CatBoost
489.75
TabNet
485.12
Table 6: Performance for Rossmann Store Sales dataset.
Rossmann Store Sales 6: The task is forecasting the store
sales from static and time-varying features. We observe that
TabNet outperforms commonly-used methods. The time fea-
tures (e.g. day) obtain high importance, and the beneﬁt of
instance-wise feature selection is observed for cases like hol-
idays where the sales dynamics are different.
Interpretability
Synthetic datasets: Fig. 5 shows the aggregate feature im-
portance masks for the synthetic datasets from Table 1.7 The
output on Syn2 only depends on X3-X6 and we observe that
the aggregate masks are almost all zero for irrelevant features
and TabNet merely focuses on the relevant ones. For Syn4,
the output depends on either X1-X2 or X3-X6 depending
on the value of X11. TabNet yields accurate instance-wise
feature selection – it allocates a mask to focus on the indi-
cator X11, and assigns almost all-zero weights to irrelevant
features (the ones other than two feature groups).
Real-world datasets: We ﬁrst consider the simple task of
mushroom edibility prediction (Dua and Graff 2017). Tab-
Net achieves 100% test accuracy on this dataset. It is indeed
known (Dua and Graff 2017) that “Odor” is the most discrim-
inative feature – with “Odor” only, a model can get > 98.5%
test accuracy (Dua and Graff 2017). Thus, a high feature
importance is expected for it. TabNet assigns an importance
score ratio of 43% for it, while other methods like LIME
(Ribeiro, Singh, and Guestrin 2016), Integrated Gradients
(Sundararajan, Taly, and Yan 2017) and DeepLift (Shrikumar,
Greenside, and Kundaje 2017) assign less than 30% (Ibrahim
et al. 2019). Next, we consider Adult Census Income. Tab-
Net yields feature importance rankings consistent with the
well-known (Lundberg, Erion, and Lee 2018; Sarkar 2020)
(see Appendix) For the same problem, Fig. 6 shows the clear
separation between age groups, as suggested by “Age” being
the most important feature by TabNet.
Self-Supervised Learning
Table 7 shows that unsupervised pre-training signiﬁcantly
improves performance on the supervised classiﬁcation task,
especially in the regime where the unlabeled dataset is much
6https://www.kaggle.com/c/rossmann-store-sales
7For better illustration here, the models are trained with 10M
samples rather than 10K as we obtain sharper selection masks.
6684


---

<!-- Page 7 -->
## Page 7

/
M[1]
M[2]
M[3]
M[4]
Magg
Syn2 dataset
X11
X1 X2 X3 X4 X5
X6
X7 X8 X9 X10
Test samples
M[1]
M[2]
M[3]
M[4]
Magg
Syn4 dataset
M[5]
Figure 5: Feature importance masks M[i] (that indicate feature selection at ith step) and the aggregate feature importance mask
Magg showing the global instance-wise feature selection, on Syn2 and Syn4 (Chen et al. 2018). Brighter colors show a higher
value. E.g. for Syn2, only X3-X6 are used.
.
Figure 6: First two dimensions of the T-SNE of the decision
manifold for Adult and the impact of the top feature ‘Age’.
Figure 7: Training curves on Higgs dataset with 10k samples.
Training
Test accuracy (%)
dataset size
Supervised
With pre-training
1k
57.47 ± 1.78
61.37 ± 0.88
10k
66.66 ± 0.88
68.06 ± 0.39
100k
72.92 ± 0.21
73.19 ± 0.15
Table 7: Mean and std. of accuracy (over 15 runs) on Higgs
with Tabnet-M model, varying the size of the training dataset
for supervised ﬁne-tuning.
larger than the labeled dataset. As exempliﬁed in Fig. 7 the
model convergence is much faster with unsupervised pre-
training. Very fast convergence can be useful for continual
learning and domain adaptation.
Conclusions
We have proposed TabNet, a novel deep learning architec-
ture for tabular learning. TabNet uses a sequential attention
mechanism to choose a subset of semantically meaningful
features to process at each decision step. Instance-wise fea-
ture selection enables efﬁcient learning as the model capacity
is fully used for the most salient features, and also yields
more interpretable decision making via visualization of se-
lection masks. We demonstrate that TabNet outperforms pre-
vious work across tabular datasets from different domains.
Lastly, we demonstrate signiﬁcant beneﬁts of unsupervised
pre-training for fast adaptation and improved performance.
6685


---

<!-- Page 8 -->
## Page 8

Acknowledgements
Discussions with Jinsung Yoon, Long T. Le, Kihyuk Sohn,
Ariel Kleiner, Zizhao Zhang, Andrei Kouznetsov, Chen Xing,
Ryan Takasugi and Andrew Moore are gratefully acknowl-
edged.
Ethical Impact
Tabular data is the most common data type of real-world
AI (Chui et al. 2018). Tabular data learning problems occur
in many crucial AI applications from Healthcare, Energy,
Finance, Retail, Manufacturing, Physical Sciences etc. Tab-
Net is a novel deep neural network architecture to improve
performance of tabular data learning, while also providing
explainable insights on its reasoning. To emphasize broad
applicability, in this paper, we show strong results of TabNet
in wide range of applications from Environmental Sciences,
Physics, Retail, Robotics and Public Sector.
Besides strong performance, TabNet provides explainable
insights on its reasoning, both locally and globally. In some
major tabular data applications, transparency is crucial, due to
regulatory reasons or due to the expectations of non-technical
users. For example, a doctor should know why an AI model
would suggest a particular treatment, or a loan ofﬁcer should
know why an AI model would ﬂag a customer as high default
risk. Indeed, because of this reason, deep learning has not
been able to penetrate much into such transparency-sensitive
tabular learning applications. We believe TabNet would be an
important contribution along this direction (although it does
not constitute the complete solution). The feature attribution
masks of TabNet can shed light on what features the model
is using for reasoning, for each instance separately, and can
be useful in building trust to the model for decision makers,
or can provide guidance for regulatory authorities. Such in-
sights can also be used by data scientists to improve model
performance via feature engineering.
Last but not least, we demonstrate the potential of self-
supervised learning for tabular data, for the ﬁrst time to our
knowledge. Self-supervised learning has been one of the most
active AI research areas recently, but almost all of the litera-
ture has been focusing on text or image data. We demonstrate
that the real world tabular datasets also have structured in-
formation that a self-supervised learning framework based
on TabNet can utilize efﬁciently. We show signiﬁcant perfor-
mance improvements with unsupervised pre-training and we
expect this direction to improve AI penetration into applica-
tions where human labeling is very costly (which is the case
for Healthcare, Finance or Retail for example, as the human
labelers should have domain-speciﬁc expertise).
References
Amodei, D.; Anubhai, R.; Battenberg, E.; Case, C.; Casper, J.;
et al. 2015. Deep Speech 2: End-to-End Speech Recognition
in English and Mandarin. arXiv:1512.02595 .
Bansal, S. 2020. Historical Data Science Trends on Kaggle.
URL https://www.kaggle.com/shivamb/data-science-trends-
on-kaggle.
Chen, J.; Song, L.; Wainwright, M. J.; and Jordan, M. I. 2018.
Learning to Explain: An Information-Theoretic Perspective
on Model Interpretation. arXiv:1802.07814 .
Chen, T.; and Guestrin, C. 2016. XGBoost: A Scalable Tree
Boosting System. In KDD.
Chui, M.; Manyika, J.; Miremadi, M.; Henke, N.; Chung, R.;
et al. 2018. Notes from the AI Frontier. McKinsey Global
Institute .
Cortes, C.; Gonzalvo, X.; Kuznetsov, V.; Mohri, M.; and
Yang, S. 2016. AdaNet: Adaptive Structural Learning of
Artiﬁcial Neural Networks. arXiv:1607.01097 .
Dai, Z.; Yang, Z.; Yang, F.; Cohen, W. W.; and Salakhutdinov,
R. 2017. Good Semi-supervised Learning that Requires a
Bad GAN. arxiv:1705.09783 .
Dauphin, Y. N.; Fan, A.; Auli, M.; and Grangier, D. 2016.
Language Modeling with Gated Convolutional Networks.
arXiv:1612.08083 .
Devlin, J.; Chang, M.; Lee, K.; and Toutanova, K. 2018.
BERT: Pre-training of Deep Bidirectional Transformers for
Language Understanding. arXiv:1810.04805 .
Dua, D.; and Graff, C. 2017. UCI Machine Learning Reposi-
tory. URL http://archive.ics.uci.edu/ml. Accessed: 2019-11-
10.
Gehring, J.; Auli, M.; Grangier, D.; Yarats, D.; and Dauphin,
Y. N. 2017. Convolutional Sequence to Sequence Learning.
arXiv:1705.03122 .
Geurts, P.; Ernst, D.; and Wehenkel, L. 2006. Extremely
randomized trees. Machine Learning 63(1): 3–42. ISSN
1573-0565.
Goodfellow, I.; Bengio, Y.; and Courville, A. 2016. Deep
Learning. MIT Press.
Grabczewski, K.; and Jankowski, N. 2005. Feature selection
with decision tree criterion. In HIS.
Grandvalet, Y.; and Bengio, Y. 2004. Semi-supervised Learn-
ing by Entropy Minimization. In NIPS.
Guyon, I.; and Elisseeff, A. 2003. An Introduction to Variable
and Feature Selection. JMLR 3: 1157–1182.
He, K.; Zhang, X.; Ren, S.; and Sun, J. 2015. Deep Residual
Learning for Image Recognition. arXiv:1512.03385 .
Hestness, J.; Narang, S.; Ardalani, N.; Diamos, G. F.; Jun,
H.; Kianinejad, H.; Patwary, M. M. A.; Yang, Y.; and Zhou,
Y. 2017. Deep Learning Scaling is Predictable, Empirically.
arXiv:1712.00409 .
Ho, T. K. 1998. The random subspace method for construct-
ing decision forests. PAMI 20(8): 832–844.
Hoffer, E.; Hubara, I.; and Soudry, D. 2017. Train longer,
generalize better: closing the generalization gap in large batch
training of neural networks. arXiv:1705.08741 .
Hudson, D. A.; and Manning, C. D. 2018.
Composi-
tional Attention Networks for Machine Reasoning. CoRR
abs/1803.03067. URL http://arxiv.org/abs/1803.03067.
6686


---

<!-- Page 9 -->
## Page 9

Humbird, K. D.; Peterson, J. L.; and McClarren, R. G. 2018.
Deep Neural Network Initialization With Decision Trees.
IEEE Trans Neural Networks and Learning Systems .
Ibrahim, M.; Louie, M.; Modarres, C.; and Paisley, J. W.
2019. Global Explanations of Neural Networks: Mapping
the Landscape of Predictions. arxiv:1902.02384 .
Ke, G.; Meng, Q.; Finley, T.; Wang, T.; Chen, W.; et al. 2017.
LightGBM: A Highly Efﬁcient Gradient Boosting Decision
Tree. In NIPS.
Ke, G.; Zhang, J.; Xu, Z.; Bian, J.; and Liu, T.-Y. 2019.
TabNN: A Universal Neural Network Solution for Tabular
Data. URL https://openreview.net/forum?id=r1eJssCqY7.
Kingma, D. P.; and Ba, J. 2014. Adam: A Method for Stochas-
tic Optimization. In ICLR.
Kontschieder, P.; Fiterau, M.; Criminisi, A.; and Bul, S. R.
2015. Deep Neural Decision Forests. In ICCV.
Lai, S.; Xu, L.; Liu, K.; and Zhao, J. 2015. Recurrent Convo-
lutional Neural Networks for Text Classiﬁcation. In AAAI.
Lundberg, S. M.; Erion, G. G.; and Lee, S. 2018. Consis-
tent Individualized Feature Attribution for Tree Ensembles.
arXiv:1802.03888 .
Martins, A. F. T.; and Astudillo, R. F. 2016. From Softmax
to Sparsemax: A Sparse Model of Attention and Multi-Label
Classiﬁcation. arXiv:1602.02068 .
Mitchell,
R.;
Adinets,
A.;
Rao,
T.;
and
Frank,
E.
2018.
XGBoost: Scalable GPU Accelerated Learning.
arXiv:1806.11248 .
Mocanu, D.; Mocanu, E.; Stone, P.; Nguyen, P.; Gibescu, M.;
and Liotta, A. 2018. Scalable training of artiﬁcial neural net-
works with adaptive sparse connectivity inspired by network
science. Nature Communications 9.
Mott, A.; Zoran, D.; Chrzanowski, M.; Wierstra, D.; and
Rezende, D. J. 2019. S3TA: A Soft, Spatial, Sequential, Top-
Down Attention Model. URL https://openreview.net/forum?
id=B1gJOoRcYQ.
Radford, A.; Metz, L.; and Chintala, S. 2015. Unsupervised
Representation Learning with Deep Convolutional Genera-
tive Adversarial Networks. arXiv:1511.06434 .
Raina, R.; Battle, A.; Lee, H.; Packer, B.; and Ng, A. Y. 2007.
Self-Taught Learning: Transfer Learning from Unlabeled
Data. In ICML.
Ribeiro, M.; Singh, S.; and Guestrin, C. 2016. Why Should I
Trust You?: Explaining the Predictions of Any Classiﬁer. In
KDD.
Sarkar, D. 2020.
Notebook on Nbviewer.
URL
https://nbviewer.jupyter.org/github/dipanjanS/data science
for all/blob/master/tds model interpretation xai/Human-
interpretableMachineLearning-DS.ipynb#.
Shavitt, I.; and Segal, E. 2018. Regularization Learning
Networks: Deep Learning for Tabular Datasets.
Shrikumar, A.; Greenside, P.; and Kundaje, A. 2017. Learn-
ing Important Features Through Propagating Activation Dif-
ferences. arXiv:1704.02685 .
Sundararajan, M.; Taly, A.; and Yan, Q. 2017. Axiomatic
Attribution for Deep Networks. arXiv:1703.01365 .
Tanno, R.; Arulkumaran, K.; Alexander, D. C.; Crimin-
isi, A.; and Nori, A. V. 2018.
Adaptive Neural Trees.
arXiv:1807.06699 .
Trinh, T. H.; Luong, M.; and Le, Q. V. 2019.
Selﬁe:
Self-supervised
Pretraining
for
Image
Embedding.
arXiv:1906.02940 .
Vijayakumar, S.; and Schaal, S. 2000. Locally Weighted
Projection Regression: An O(n) Algorithm for Incremental
Real Time Learning in High Dimensional Space. In ICML.
Wang, S.; Aggarwal, C.; and Liu, H. 2017. Using a random
forest to inspire a neural network and improving on it. In
SDM.
Wen, W.; Wu, C.; Wang, Y.; Chen, Y.; and Li, H. 2016.
Learning Structured Sparsity in Deep Neural Networks.
arXiv:1608.03665 .
Xu, L.; Skoularidou, M.; Cuesta-Infante, A.; and Veeramacha-
neni, K. 2019. Modeling Tabular data using Conditional
GAN. arXiv:1907.00503 .
Yang, Y.; Morillo, I. G.; and Hospedales, T. M. 2018. Deep
Neural Decision Trees. arXiv:1806.06988 .
Yoon, J.; Jordon, J.; and van der Schaar, M. 2019. INVASE:
Instance-wise Variable Selection using Neural Networks. In
ICLR.
6687


---
