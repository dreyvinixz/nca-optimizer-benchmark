# An optimized ensemble model based on meta-heuristic algorithms for effective detection and classification of breast tumors

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-10719-9

---

## Page 1
ORIGINAL ARTICLE
An optimized ensemble model based on meta-heuristic algorithms
for effective detection and classification of breast tumors
Abeer Saber1 • Samar Elbedwehy2 • Wael A. Awad3 • Esraa Hassan4
Received: 20 March 2024 / Accepted: 14 October 2024 / Published online: 27 December 2024
 The Author(s) 2024
Abstract
One of the most common cancers among women worldwide is breast cancer (BC), and early diagnosis can save lives. Early
detection of BC increases the likelihood of a successful outcome by enabling treatment to start sooner. Even in areas
without access to a specialist physician, machine learning (ML) aids in early BC detection. The medical imaging com-
munity is becoming more interested in using ML, and deep learning (DL) to increase the accuracy of cancer screening.
Many disease-related data are sparse. However, for DL models to perform well, a large amount of data is required. Because
of this, the DL models that are currently in use on medical images are not as effective as they could be. Convolutional
neural network (CNN) models have recently gained popularity in the medical industry, and they perform admirably in
terms of high performance and robustness at image classiﬁcation. The proposed method classiﬁes data using ensemble pre-
trained models such as the dense convolutional network (DenseNet)-121 and EfﬁcientNet-B5 feature extractor networks, as
well as the support vector machine for classiﬁcation. Using a modiﬁed meta-heuristic optimizer, the selected pre-trained
CNN hyperparameters were optimized to improve the performance. The experimental results for the presented model on
the INbreast dataset show that the EfﬁcientNet-B5 model is effective for BC classiﬁcation, with overall accuracy, sen-
sitivity, speciﬁcity, precision, and area under the ROC curve (AUC) values of 99.9%, 99.9%, 99.8%, 99.1%, 1.0,
respectively.
Keywords Deep learning  Optimization  Transfer learning  Breast cancer  Convolutional neural network
1 Introduction
According to a recent ‘‘American Cancer Society’’ [1]
report, 31% of newly diagnosed instances of cancer in
women are in BC, as illustrated in Fig. 1. It is the most
common cancer in women worldwide, with an extremely
high death rate. Currently, the most efﬁcient way to
decrease BC deaths is through early detection and treat-
ment. Immunohistochemistry (IHC) is a diagnostic analysis
technique commonly used by pathologists to ascertain the
hormone receptor status and histopathological grade. As
digital pathology images, which are frequently full slide
images (WSIs), accumulate, the cancer diagnostic becomes
extremely time-consuming and vulnerable to variations in
observation [2, 3].
DL, a subset of artiﬁcial intelligence (AI), applies arti-
ﬁcial neural networks (ANNs) to stimulate the human brain
and learn from enormous data amounts. DL models are
favored over conventional ML algorithms as they can
& Abeer Saber
abeer_saber@du.edu.eg
& Esraa Hassan
esraa.hassan@ai.kfs.edu.eg
1
Information Technology Department, Faculty of Computers
and Artiﬁcial Intelligence, Damietta University,
Damietta 34517, Egypt
2
Department of Data Science, Faculty of Artiﬁcial
Intelligence, Kafrelsheikh University, Kafrelsheikh 33511,
Egypt
3
Department of Computer Science, Faculty of Computers and
Artiﬁcial Intelligence, Damietta University, Damietta 34517,
Egypt
4
Faculty of Artiﬁcial Intelligence, Kafrelsheikh University,
Kafrelsheikh 33511, Egypt
123
Neural Computing and Applications (2025) 37:4881–4894
https://doi.org/10.1007/s00521-024-10719-9
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
concentrate on intricate image features and learn inde-
pendently [4]. Many medical ﬁelds have used DL tech-
niques, and new models are always being created to
enhance the extraction of features. Some of the advantages
of DL include handling large amounts of data, improving
time efﬁciency, mastering unstructured data, advanced
analytics, and cost-effectiveness. Diverse methods are
commonly employed for tasks such as image processing,
segmentation, and classiﬁcation, referred to as DL tech-
niques [5, 13].
Several imaging applications have seen the successful
application of DL approaches in recent years, according to
a review of recent papers on DL applications. In medical
image analysis, CNN models have demonstrated efﬁcacy in
cell recognition, tumor detection, and skin disease classi-
ﬁcation [5, 6]. These designs use layer-based feature
extraction, and the values of a CNN model’s hyperpa-
rameters determine how well the model performs. Finding
these hyperparameters’ ideal values can be challenging,
time-consuming, and need experimentation. Many medical
images pose an NP-hard optimization challenge when it
comes to tuning hyperparameters [7, 8]. A CNN training
process requires a large data amount, yet medical data is
scarce. This problem can be resolved by using transfer
learning (TL) from a natural-images dataset such as
ImageNet along with a ﬁne-tuning approach, as Fig. 2
shows. Performance can be enhanced by applying the TL
concept, which combines the expertise of many CNN
designs. The principal advantages of TL are enhanced
classiﬁcation accuracy and expedited training.
When utilized to address classiﬁcation issues, heuristics
are very appealing and have been applied to numerous real-
world issues [9, 10]. Meta-heuristic algorithms are effec-
tive tools for optimizing the parameters and architecture of
DL models. It can precisely calculate the appropriate
estimation of DL components, such as hyperparameters,
weights, number of layers, and learning rate.
The Grey Wolf Optimizer (GWO) algorithm has been
tested on 29 well-known test functions and performed
comparably to other meta-heuristics, such as particle
swarm optimization (PSO), gravitational search algorithm
(GSA), and differential evolution. It has also effectively
tackled traditional engineering design challenges and real-
world optimization problems in numerous disciplines.
Also, the Hunger Games Search (HGS) method outper-
forms other well-known algorithms on 23 functions and
meets IEEE CEC 2014 benchmarks. It has been used to
solve various engineering difﬁculties, demonstrating its
adaptability. The HGS algorithm excels at solving contin-
uous and discrete optimization problems, making it a
valuable tool. Multimodal optimization issues, in which the
search space contains many local optima, can also be
handled by the HGS method.
The presented study proposes a new model for multi-
class BC detection and classiﬁcation. The current model
consists of three major components (data collection and
preprocessing, choosing the best hyperparameter values,
Fig. 1 The estimation of new cancer cases in 2023
4882
Neural Computing and Applications (2025) 37:4881–4894
123

---

## Page 3
and model training and evaluation) used to improve breast
pictures and thus classiﬁcation outcomes. These stages are
explained in depth in the subsections that follow.
The main motivating factors for this work are outlined
below.
1)
A novel hyperparameter tuning technique that uses
TL and an improved meta-heuristic algorithm is
presented.
2)
We conduct a comprehensive comparison of opti-
mizing the hyperparameters of the proposed CNN
using the HGS and GWO algorithms.
3)
Remove non-breast regions in preprocessing steps to
reduce the training computation time.
4)
Detecting and classifying breast mammography more
precisely using the SVM classiﬁer.
5)
Our results provide an exciting opportunity for more
research and useful applications, which could lead to
more quick and accurate diagnostics and ultimately
enhance the quality of life for those suffering from
BC.
The paper has been laid out as follows: Sect. 2 discusses
the associated work, and Sect. 3 presents the proposed
model. The experimental results are compared with the real
data in Sect. 4. Section 5 brings the context conclusion.
2 Related works
These days, AI knows no bounds and is transforming and
saving lives. AI works to improve and streamline interac-
tions between patients and providers by simulating human
intelligence through computer systems and consists of the
capacity to investigate and solve issues. AI and technology
are advancing applications in healthcare, such as decision
support, image analysis, and patient triage. Computer-aided
diagnosis (CAD) acts as a second set of eyes, indicating
anomalies (such as a tumor or micro-calciﬁcation) on
digital mammograms, and advises the radiologists reading
the images to take appropriate action or not. Radiologists
with CAD performed as though two radiologists were
double reading. Experts and company owners have created
CAD systems to automatically classify BC as benign or
malignant. Choosing the best algorithms for a CAD system
necessitates improving comprehension of the information
included in cancer images [11].
Abeer et al. [12] developed a deep CNN model, which
extracted features from the MIAS dataset using pre-trained
CNNs. It performs well in the six-evaluation metrics. The
VGG16 model outperforms other models in BC diagnosis,
with overall accuracy and precision of 98.96% and 98.87%,
respectively.
Using the INbreast dataset, Akselrod-Ballin et al. [13]
assessed a DL model for BC classiﬁcation using a region-
based CNN. The suggested model had an accuracy rate of
Fig. 2 Transfer learning
technique
Neural Computing and Applications (2025) 37:4881–4894
4883
123

---

## Page 4
78%. On the same dataset, Al-Antari et al. [14] constructed
a DL technique to classify BC using feedforward CNN,
ResNet 50, and Inception ResNet-V2 CNNs. The accuracy
of the suggested model was 95.32%.
Chakravarthy et al. created a TL-based framework [15].
The last 3 layers, in AlexNet, GoogleNet, ResNet-50, and
Dense-Net 121 networks are trained using the INbreast
dataset. The SVM classiﬁer is applied to categorize the
breast tumor (BT) classes. The proposed model obtained a
96.6% accuracy rate.
Abeer et al. [16] developed a DL technique that depends
on pre-trained CNNs for detecting and classifying BC
using the INbreast dataset. Breast mammographic images
are preprocessed to enhance the images and minimize
computation time. The model achieved accuracy, sensi-
tivity, speciﬁcity, and AUC values of 97.1%, 96.3%,
97.9%, and 0.988%, respectively.
Abeer et al. [17] developed a DL architecture combining
TL and long short-term memory for automatic BC detec-
tion and diagnosis using the 80–20 method. The model
extracts the learned features from pre-trained CNNs, and
extracts features from the INbreast dataset. The presented
model achieved high accuracy, sensitivity, precision, and
AUC values with 99.236%, 99.1%, 96%, 98.8%, and 0.998,
demonstrating its effectiveness in detecting breast tumors.
Abeer et al. [18] developed a new DL to detect and
classify tumors in mammographic images using TL tech-
niques. The model uses pre-trained networks from VGG-
19, VGG16, and InceptionV3, to decrease training time and
raise classiﬁcation accuracy. The Mammographic Image
Analysis Society dataset is applied for feature extraction.
The model outperforms VGG19 and Inception V3 in
accuracy, sensitivity, and speciﬁcity.
Sahu et al. [19] illustrated a DL-based ensemble clas-
siﬁer is proposed for BC detection, demonstrating efﬁcient
performance with a small dataset. This method integrates
TL models and employs residual learning, depthwise sep-
arable
convolution,
and
inverted
residual
bottleneck
structure. Experimental results show superior classiﬁcation
performance, with 99.17% accuracy for abnormality and
97.75% for malignancy on the mini-DDSM dataset and
94.62% accuracy on BUSI and BUS2, respectively.
Qian et al. [20] presented a novel model to identify
atypical BC using the ZFNet CNN for breast mammo-
graphic images. The method uses Wiener and CALHE
ﬁlters for preprocessing, modiﬁed and trained on the CBIS-
DDSM dataset, and an extreme learning machine to
enhance classiﬁcation performance. The method uses the
Chimp Optimization Algorithm (SWChOA) and bench-
mark meta-heuristic optimization algorithms. When com-
pared to other approaches, the performance level of the
provided methodology was the greatest.
Gudur et al. [21] developed a hybrid genetic algorithm
and CNNs to optimize CNN architecture for BC catego-
rization. This dynamic optimization process extracts rele-
vant features and patterns from histopathology pictures,
improving diagnostic precision. Tests show signiﬁcant
improvement in diagnosis accuracy and reduced manual
hyperparameter adjustment. This combination of genetic
algorithms and CNNs enhances BC diagnosis and treat-
ment outcomes with 98.54%, 99.41%, 98.42%, and 97.02%
for accuracy, precision, recall, and F-Score, respectively.
Rahman et al. [22] presented a computational model for
BC diagnosis using a ResNet-50 CNN. The framework
classiﬁes mammogram images using TL, achieving an
impressive 93% classiﬁcation accuracy. This approach
could save lives and resources by reducing error rates in
screening mammograms.
Srikantamurthy et al. [23] created a hybrid CNN-LSTM
model to categorize four BC subtypes on a dataset as
benign and malignant, reaching 92.5% and 99% overall
accuracy
in
multiclass
and
binary
classiﬁcation,
respectively.
Sharmin et al. [24] developed a hybrid BC detection
approach that integrates DL with ensemble-based ML
methods. Experiments on a publicly available dataset show
the model’s robustness and high performance compared to
state-of-the-art models, achieving accuracy, precision,
recall, and F1 scores of 95%, 94.86%, 94.32%, and
94.57%, respectively.
3 Proposed model
This section presents the proposed novel ensemble model
based on meta-heuristic algorithms GWO and HGS algo-
rithms for hyperparameter optimization-based BT classiﬁ-
cation. To achieve the best accuracy, the meta-heuristic
algorithms select the optimal hyperparameter values of the
networks. The structure of a high-level CAD system for
cancer diagnostics is shown in Fig. 3. Breast tumors are
classiﬁed as benign or malignant using four major pro-
cessing stages. The presented model contains three phases
as shown in Fig. 4, and operates in the following order:
1.
Data collection and preprocessing
2.
Choose the best hyperparameter values
3.
Model training and evaluation
3.1 Data collection and preprocessing
1. Noise removal.
The best techniques for eliminating noise from mam-
mography pictures are the wavelet transform and the
4884
Neural Computing and Applications (2025) 37:4881–4894
123

---

## Page 5
median ﬁlter [25]. The 3 9 3 median ﬁlter is used in this
study to remove noise from the mammographic images.
2.
Morphological analysis.
Morphological analysis is a collection of image pro-
cessing methods that manipulate images depending on their
forms. By adding a structural element (SE) to an input
image, morphological operations yield an identically sized
output image. The result of a morphological operation
determines each pixel’s value by comparing it to its
neighbors in the corresponding pixel in the input image.
Morphological procedures, like spatial ﬁltering, entail
moving the structuring element across every pixel in the
source image to produce a pixel in the altered new image.
The morphological operation that is carried out determines
the value of this new pixel [26]. The operations of mor-
phological analysis are illustrated in Fig. 5.
3
Constructed limited histogram equalization.
One type of adaptive histogram equalization that pre-
vents over-ampliﬁcation of noise is called Constructed
Limited
Histogram
Equalization
(CLAHE).
Using
CLAHE, an image is divided into small areas known as
tiles, and each tile is subjected to a unique application of
histogram equalization. The histogram is then clipped at a
predeﬁned threshold value to limit the contrast in each tile.
The clipped portion of the histogram is then uniformly
redistributed over all histogram bins. An image with
enhanced edge deﬁnition and increased local contrast in
every area of the image is the result of this procedure [27].
4
Augmentation.
Rather than gathering more data, image augmentation
can be used to improve model classiﬁcation accuracy [28].
Thus, the effectiveness of the proposed model is improved
by the data augmentation approaches that increase the
number of samples. Several data augmentation methods
were used on the training dataset to raise the model’s
accuracy. These covers ﬂipping both horizontally and
vertically, shearing, width and height shifts, and brightness
and rotation modiﬁcations as presented in Algorithm 1.
Algorithm 1
Breast data augmentation (BDA).
3.2 Choose the best hyperparameter values
A CNN training process needs a large data amount, and
medical data is scarce, particularly in breast tumors. This
issue can be ﬁxed by combining TL from a natural-images
dataset like ImageNet with a ﬁne-tuning strategy. Applying
the TL approach, which integrates the knowledge of sev-
eral CNN designs, can improve performance. Improved
classiﬁcation accuracy and quicker training are the two
main beneﬁts of TL. A model transfer, whereby the target
domain’s network characteristics are applied, performance-
optimized, and pre-trained using the source data, is a
suitable technique for training models.
A.
Grey wolf optimization algorithm.
A population-based meta-heuristic algorithm known as
the Grey Wolf Optimizer (GWO) simulates the actual
hunting and leading patterns of grey wolves. The program
simulates the leadership hierarchy using 4 sorts of grey
wolves: alpha, beta, delta, and omega. To optimize, the
Fig. 3 The general architecture
for CAD systems
Neural Computing and Applications (2025) 37:4881–4894
4885
123

---

## Page 6
algorithm comprises three key hunting steps: searching for
prey, encircling prey, and attacking prey.
The GWO is a nature-inspired meta-heuristic algorithm
that replicates the natural leadership hierarchy and hunting
mechanism of grey wolves. To replicate the leadership
hierarchy, the algorithm employs four kinds of grey
wolves: alpha, beta, delta, and omega. To perform opti-
mization, the algorithm has three main hunting steps:
searching for prey, encircling prey, and attacking prey. The
GWO algorithm starts with a population of wolves, each
representing a possible solution to the optimization issue.
The algorithm then iteratively modiﬁes each wolf’s posi-
tion based on some performance metric until it reaches an
optimal solution.
•
Social hierarchy
The GWO method is based on a mathematical model of
the wolf social order. The strongest solution is alpha (a),
Fig. 4 The proposed model
4886
Neural Computing and Applications (2025) 37:4881–4894
123

---

## Page 7
followed by beta (b) and delta (d), which are the second
and third-best solutions, respectively. The remaining
solutions are referred to as omega (x). The alpha, beta, and
delta wolves lead the optimization process, while the
omega wolves follow. This is the foundation of the GWO
algorithm’s optimization approach.
•
Encircling prey
The following equations can be used to mathematically
model grey wolf encircling behavior during hunting:
D~ ¼ jC
!  XP tð Þ  X~ tð Þj
ð1Þ
X~ t þ 1
ð
Þ ¼ X~p tð Þ  A~  D~
ð2Þ
where t refers the current number of iterations, X!
p denotes
the prey location vector, X! denotes the location of a single
wolf, and A and C can be calculated by the following:
A~ ¼ 2a~ r~1  a~
ð3Þ
C~ ¼ 2  r~2
ð4Þ
As the number of iterations increases, the vector is
reduced linearly from 2 to 0. r!
1 and r!
2 are random
vectors with values ranging from 0 to 1.
•
Hunting
Grey wolves have the natural ability to locate their prey
and circle them to get a better look. However, it is
impossible to pinpoint the precise location of the optimum
(prey) in an abstract search space. To mathematically
model the hunting behavior of grey wolves, the GWO
algorithm considers the alpha as the best solution, with beta
and delta also having some knowledge about the potential
location of prey. As a result, the top 3 solutions are saved,
and the remaining search agents (omegas) must alter their
locations to reﬂect these positions. To model this behavior,
the following formulas are suggested. The equations below
are applied to calculate the positions of the leaders.
D~a ¼ C1  X~a  A~


ð5Þ
D~b ¼ C2  X~b  A~


ð6Þ
D~d ¼ C3  X~d  A~


ð7Þ
X~1 ¼ X~a  A1  D~a


ð8Þ
X~2 ¼ X~b  A2  D~b


ð9Þ
X~3 ¼ j X~d  A3  D~b
ð10Þ
X! t þ 1
ð
Þ ¼ X!
1 þ X!
2 þ X!
3
3
ð11Þ
X~ t þ 1
ð
Þ ¼ w1X~1 þ w2X~2 þ w3X~3; where
X
3
i¼1
wi ¼ 1
ð12Þ
•
Exploration
Wolves have the instinct to identify their prey’s location
and move around it to encircle it. However, in an abstract
search space, knowing the precise location of the optimum
(prey) is impossible. The GWO considers alpha to be the
best solution for mathematically modeling grey wolf
hunting behavior, with beta and delta also having some
knowledge about potential prey location. As a result, the
ﬁrst 3 best answers are kept, and the remaining search
agents (omegas) must change their locations based on those
of the best search agents.
•
Exploitation
The grey wolves in the GWO algorithm mostly follow
the alpha, beta, and delta but also deviate from them to
Fig. 5 The morphological
analysis operations
Neural Computing and Applications (2025) 37:4881–4894
4887
123

---

## Page 8
explore the search space. The coefﬁcient vector A! is used
with random values greater than one or less than - 1 to
model this divergence behavior, which encourages search
agents to explore globally. Another component that pro-
motes exploration and avoids local optima is the use of C!
with random values in [0, 2]. This vector assigns random
weights to prey, which can either emphasize or deempha-
size their role in determining distance. In contrast to A!, the
values of C! are not decreased linearly, and random values
are used throughout the optimization process to emphasize
exploration in both the initial and ﬁnal iterations. This
component is particularly useful when the optimization
process becomes stuck at local optima.
The detailed algorithm of the modiﬁed GWO- ensemble
model is shown in Algorithm 2.
Algorithm 2 Pseudo code of the modiﬁed GWO- ensemble model.
B.
Hunger game search optimization algorithm.
The HGS algorithm is an optimization method based on
meta-heuristics and motivated by foraging and hunger
instincts of animals. It is designed to tackle optimization
problems based on social behaviors, speciﬁcally emulating
how hunger affects a single animal’s behavior. The idea of
hunger is included by the algorithm in the search process
by using adaptive weights for stimulating the hunger effect.
A step-by-step explanation of how the HGS algorithm is
presented as follows:
•
Initialization: The algorithm generates random candi-
date solutions from the search space.
•
Hunger adaptation: An adaptive weight generated from
the concept of hunger is devised and applied to model
the effect of hunger on the candidate solutions. This
weight is updated dynamically throughout the search
process, affecting the exploration and exploitation of
the search space.
•
Fitness evaluation: The ﬁtness of each candidate
solution is evaluated based on the objective function
of the optimization problem. The ﬁtness value indicates
the quality of the solution.
•
Selection: The selection process is based on the ﬁtness
values of the candidate solutions. The algorithm uses a
ﬁtness-proportional selection mechanism to choose the
best solutions for the next generation.
•
Crossover and mutation: The selected candidate solu-
tions undergo crossover and mutation operations to
generate new candidate solutions for the next genera-
tion. These operations help to explore and exploit the
search space more effectively.
•
Hunger update: The adaptive weight is updated based
on the hunger level of the candidate solutions. The
4888
Neural Computing and Applications (2025) 37:4881–4894
123

---

## Page 9
hunger level is deﬁned by the distance among the
present solution and the best solution found thus far.
The higher the distance, the hungrier the solution, and
the higher the adaptive weight.
•
Termination: When a stopping criterion is reached, like
arriving to the maximum iterations number or obtaining
a good solution, the algorithm terminates.
The hunger game search optimizer for the suggested
model is shown in Fig. 6.
The HGS algorithm has several advantages, including
simplicity, high performance, adaptability, and efﬁciency
in ﬁnding and developing the target solution space. The
algorithm is based on the concept of hunger, which is a
critical motivator for animals, and applies an adaptive
weight depending on the idea of hunger to inﬂuence each
search step. This means that the search process is simulated
in a way that mimics how animals search for food. The
algorithm has been validated on a comprehensive group of
benchmark problems and has demonstrated excellent
intensiﬁcation
and
diversiﬁcation
capabilities.
The
approach has been used to solve numerous optimization
issues, including global optimization, feature selection, and
engineering design, and has shown reliable performance
and excellent accuracy. The algorithm is straightforward to
understand and has many potential applications in various
ﬁelds, including computer science, engineering, ﬁnance,
and biomedicine.
Fig. 6 The Hunger Game Search optimizer for the ensemble model
Neural Computing and Applications (2025) 37:4881–4894
4889
123

---

## Page 10
3.3 Model training and evaluation
In this study, feature extraction is carried out using the
DenseNet-121, and EfﬁcientNet-B5 networks. The Ima-
geNet dataset is used to train this network. Colors, lines,
and other input features are recognized by the ﬁlters in the
network layers. Small parts and insigniﬁcant shapes can
then be identiﬁed. The category that the input image is part
of can be identiﬁed from the generated output. The pre-
trained models are then used to categorize various objects
in the new dataset. Excepting the ﬁnal three layers, all
trained parameters are frozen and carried over to the target
task from the source task. The previously processed pho-
tographs are then utilized to continue network training.
As a result, there are very few newly trained dense
layers. Furthermore, the previously trained layers in the
pre-trained network are integrated with these layers to
create a new class categorization. As a result, the training
process can be completed fast, with minimal training data
required when compared to CNN training from scratch.
The collected features are then utilized to train an SVM
classiﬁer to perform classiﬁcation tasks. The HGS algo-
rithm is used to ﬁne-tune the hyperparameters to ﬁnd the
best ones.
A CNN architecture, DenseNet-121 belongs to the
DenseNet model family. A 121-layer deep neural network
called DenseNet-121 is intended for use in image classiﬁ-
cation applications. It has been pre-trained on the Ima-
geNet dataset, which contains over a million images across
1000 classes. It has several important qualities, like:
Dense blocks: Four dense blocks, each containing sev-
eral convolutional layers, make up DenseNet-121. Each
layer in a dense block is feed-forward connected to every
other layer, enabling feature reuse, and mitigating the
vanishing-gradient issue.
Transition layers: A transition layer decreases the
amount of feature maps and their spatial dimensions among
dense blocks.
Global average pooling: A global average pooling layer
at the network’s end averages the feature maps across the
spatial dimensions to generate a single feature vector for
every picture. After that, a fully connected layer receives
this feature vector for classiﬁcation.
Speciﬁcally, EfﬁcientNet-B5 is trained at 456 9 456
resolution on ImageNet-1k. The novel scaling technique
that underpins the model architecture uniformly scales the
network’s dimensions to improve performance. It provides
the features and information listed below:
Model architecture: The EfﬁcientNet-B5 model is built
upon the EfﬁcientNet family of models, which aim to
provide higher performance and accuracy efﬁciency.
•
Training: At a resolution of 456 9 456, ImageNet-1k is
used to train the model.
•
Pretrained weights: For TL and ﬁne-tuning tasks,
EfﬁcientNet-B5 has pretrained weights available.
•
Model usage: Image classiﬁcation tasks can be per-
formed with EfﬁcientNet-B5.
EfﬁcientNet-B5 is renowned for its cutting-edge Ima-
geNet accuracy as well as its efﬁciency in both inference
speed and model size. For a variety of computer vision
tasks, such as image segmentation, and image classiﬁca-
tion, it is an effective tool.
The efﬁcacy and efﬁciency of the EfﬁcientNet family of
models, which includes EfﬁcientNet-B5 in a range of
computer vision applications, have led to a rise in popu-
larity among DL experts.
SVM, a supervised ML technique, is utilized for
regression and classiﬁcation applications. SVMs have a
wide range of applications, including handwriting recog-
nition, spam detection, face detection, and anomaly
detection. Because SVMs can handle high-dimensional
data and nonlinear relationships, they are useful in a variety
of applications.
4 Experimental results
1
Dataset.
The INbreast dataset is a mammographic dataset with
115 cases (410 images), of which 25 cases (two images per
case) are from women who only have one affected breast
and 90 cases (four images per case) are from women who
have both breasts affected. There are four different types of
lesions in the dataset. The Key features of the INbreast are
illustrated in Table 1.
2
Experimental results.
This section describes numerous tests to examine the
proposed model’s performance on the INbreast dataset. TL
is used in an ensemble of DenseNet-121 and EfﬁcientNet-
B5 networks to improve classiﬁcation results. The efﬁ-
ciency of the proposed ensemble model was tested using
authentication indicators produced by the evaluation met-
rics for 3 classes, as illustrated in Fig. 7. The dataset was
separated into three categories: benign, malignant, and
normal. Then it was divided into 80% training and 20%
testing activities. The advantages of preprocessing were
evaluated by running experiments twice, before and after
preprocessing. Tables 2 and 3 show the classiﬁer’s per-
formance results before and after preprocessing for the
proposed ensemble model. It has been noticed that data
preprocessing can improve the classiﬁcation results of
breast mammography images.
4890
Neural Computing and Applications (2025) 37:4881–4894
123

---

## Page 11
The results of the proposed ensemble model when GWO
optimizes the model before and after preprocessing are
presented in Table 2. From this table, it can be observed
that
before
preprocessing:
(1)
the
suggested
model
Table 1 The INbreast dataset features
Key features of the INbreast dataset
Total cases
It contains 115 cases (410) images
Lesions type
Masses, asymmetries, calciﬁcations, and distortions
Contours
Created by experts and provided in XML ﬁle
Public availability
It is publicly available for research purposes at: https://www.kaggle.com/datasets/martholi/inbreast
Fig. 7 The authentication indicators
Table 2 The INbreast dataset
results were applied using the
ensemble pre-trained CNN and
GWO optimizer
CNN
Class
Performance of the classiﬁer
Accuracy (%)
Sensitivity
Speciﬁcity
Precision
AUC
Before preprocessing
Benign
Malignant
Normal
Average
65.9
66.5
68.1
66.83
45.2
43.4
49.8
46.1
69.37
69.9
68.4
69.22
56.9
60.3
60.9
59.3
0.51
0.53
0.53
0.52
After preprocessing
Benign
Malignant
Normal
Average
99.6
99.8
99.4
99.6
99.8
99.8
99.6
99.7
99.5
99.6
99.4
99.5
97.9
98.3
98.1
98.1
0.99
1.0
0.99
0.99
The bold values is the key takeaways or summarized results from the data
Table 3 The INbreast dataset
results were applied using the
ensemble pre-trained CNN and
HGS optimizer
CNN
Class
Performance of the classiﬁer
Accuracy (%)
Sensitivity
Speciﬁcity
Precision
AUC
Before preprocessing
Benign
Malignant
Normal
Average
66.6
66.8
68.5
67.3
66.8
63.9
68.2
66.3
70.1
67.8
69.8
69.2
56.8
60.3
61.1
59.4
0.55
0.52
0.53
0.53
After preprocessing
Benign
Malignant
Normal
Average
99.8
100
99.8
99.8
100
100
99.9
99.9
99.8
100
99.7
99.8
98.3
98.1
97.9
98.1
1.0
1.0
1.0
1.0
The bold values is the key takeaways or summarized results from the data
Neural Computing and Applications (2025) 37:4881–4894
4891
123

---

## Page 12
achieves the best accuracy, sensitivity, and precision when
classifying normal cases with 68.1%, 49.8%, and 60.9%,
respectively. (2) The best speciﬁcity is achieved when
classifying malignant cases with 69.9%. On the other hand,
after preprocessing, the accuracy, speciﬁcity, precision,
and AUC reached 99.8%, 99.6%, 98.3%, and 1.0, respec-
tively, in the malignant class.
When the ensemble model is optimized with the HGS
algorithm, the model achieves the best results in almost all
values, as illustrated in Table 3. The model achieved the
best results for classifying normal cases before prepro-
cessing with 68.5%, 68.2%, 69.8%, 61.1%, and 0.53 for
accuracy, sensitivity, speciﬁcity, precision, and AUC,
respectively. After preprocessing, the best results achieved
in classifying normal cases were 99.8%, 99.9%, 99.7%,
97.9%, and 1.0 on the same performance metrics.
When compared to the malignant data, the ensemble
network performs the best, with an overall performance of
100% for accuracy, sensitivity, speciﬁcity, and AUC when
the hyperparameters are adjusted using the HGS algorithm.
On the other hand, when the hyperparameters are adjusted
using the GWO algorithm, the classiﬁcation performance
achieves 99.8%, 99.8%, 99.6%, 98.3%, and 1.0 for accu-
racy, sensitivity, speciﬁcity, precision, and AUC, respec-
tively. When compared with the normal data, it achieved
99.8%, 99.9%, 99.7%, 97.9%, and 1.0 for accuracy, sen-
sitivity, speciﬁcity, precision, and AUC, respectively, when
optimized with HGS while achieving 99.4%, 99.6%,
99.4%, 98.1%, and 0.99 with GWO, with the same metrics.
The training and loss curves for the optimized ensemble
model with GWO are shown in Figs. 8 and 9. The training
and loss curves for the optimized ensemble model with
HGS are shown in Figs. 10 and 11. The results indicate that
the proposed model achieves the best average results with
the HGS optimizer with 99.8%, 99.9%, 99.8%, 98.1%, and
1.0 for accuracy, sensitivity, speciﬁcity, precision, and
AUC. On the same dataset, the experiments are compared
with the other ﬁve of the most recently related models in
Table 4. The analysis of the results proves that the
Fig. 8 The training curve for the optimized ensemble model with
GWO
Fig. 9 The loss curve for the optimized ensemble model with GWO
Fig. 10 The training curve for the optimized ensemble model with
HGS
Fig. 11 The loss curve for the optimized ensemble model with HGS
4892
Neural Computing and Applications (2025) 37:4881–4894
123

---

## Page 13
presented model achieved the best results in terms of
accuracy, sensitivity, speciﬁcity, precision, and AUC.
5 Conclusion
In this paper, a novel optimized ensemble DL model-based
meta-heuristic algorithm is proposed for enhancing the
classiﬁcation results on the INbreast mammographic data-
set to help doctors in tumor detection and diagnosis more
accurately. The INbreast images were classiﬁed into
benign, malignant, and normal classes. The original dataset
was pre-processed to improve tumor contract in mammo-
graphic images and determine the cancerous regions more
precisely. Data augmentation was also applied to increase
the dataset size to improve the classiﬁcation result. The
optimized ensemble model achieved the best accuracy,
sensitivity, precision, F-score, and AUC, and contrasted
with alternative models. Finally, it can be said that when
compared
to
other
current
methods,
a
noticeable
improvement may be obtained in the optimized ensemble
CNN employing meta-heuristic algorithms in the screening
process. The results demonstrated 99.8% accuracy, 99.9%
sensitivity, 99.8 speciﬁcity, 98.1% precision, and 1.0 AUC.
Comparing this model to the other related methods, it is
better.
Funding Open access funding provided by The Science, Technology
& Innovation Funding Authority (STDF) in cooperation with The
Egyptian Knowledge Bank (EKB). Ministry of Scientiﬁc Research,
Egypt
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
1. Siegel RL, Miller KD, Wagle NS, Jemal A (2023) Cancer
statistics 2023. CA Cancer J Clin 73(1):17–48. https://doi.org/10.
3322/caac.21763
2. Saber A, Sakr M, Abo-Seida OM, Keshk A (2021) Automated
breast cancer detection and classiﬁcation techniques–a survey. In:
2021 international mobile, intelligent, and ubiquitous computing
conference (MIUCC), IEEE, pp 200–207
3. Sakr M, Saber A, Abo-Seida OM, Keshk A (2020) Machine
learning for breast cancer classiﬁcation using k-star algorithm.
Appl Math Inf Sci J 14(5):855–863
4. Shen C, Nguyen D, Zhou Z, Jiang SB, Dong B, Jia X (2020) An
introduction to deep learning in medical physics: advantages
potential and challenges. Phys Med Biol 65(5):05TR01
5. Zhang X, Zhang X, Wang W (2023) Convolutional neural net-
work. In: Intelligent information processing with matlab, Singa-
pore: Springer Nature Singapore, pp 39–71
6. Hassan E, Shamim Hossain M, Saber A, Elmougy S, Ghoneim A,
Muhammad G (2024) A quantum convolutional network and
ResNet (50)-based classiﬁcation architecture for the MNIST
medical dataset. Biomed Signal Process Control 87:105560
7. Rere LM, Fanany MI, Arymurthy AM (2016) Metaheuristic
algorithms for convolution neural network. Comput Intell Neu-
rosci. https://doi.org/10.1155/2016/1537325
8. Hakim WL, Rezaie F, Nur AS, Panahi M, Khosravi K, Lee CW,
Lee S (2022) Convolutional neural network (CNN) with meta-
heuristic optimization algorithms for landslide susceptibility
mapping in Icheon South Korea. J Environ Manag 305:114367
9. Hussien AG, Abualigah L, Abu Zitar R, Hashim FA, Amin M,
Saber A, Almotairi KH, Gandomi AH (2022) Recent advances in
harris hawks optimization: a comparative study and applications.
Electronics 11(12):1919
10. Zheng R, Hussien AG, Qaddoura R, Jia H, Abualigah L, Wang S,
Saber A (2023) A multi-strategy enhanced African vultures
optimization
algorithm
for
global
optimization
problems.
J Comput Des Eng 10(1):329–356
11. Chan H-P, Samala RK, Hadjiiski LM (2019) CAD and AI for
breast cancer—recent development and challenges. Br J Radiol
93(1108):20190580
12. Saber A, Sakr M, Abo-Seida OM, Keshk A, Chen H (2021) A
novel deep-learning model for automatic detection and classiﬁ-
cation of breast cancer using the transfer-learning technique.
IEEE Access 9:71194–71209
13. Ballin AA, Karlinsky L, Alpert S, Hasoul S, Ben-Ari R, Barkan E
(2016) A region-based convolutional network for tumor detection
and classiﬁcation in breast mammography. In: Deep learning and
Table 4 Comparison between
related works and the presented
model based on the INbreast
dataset
Method
Accuracy (%)
Sensitivity (%)
Speciﬁcity (%)
Precision (%)
AUC
Akselrod-Ballin et al. [13]
78
–
–
–
–
Al-Antari et al. [14]
95.3
–
–
–
–
Chakravarthy et al. [15]
96.6
–
–
–
–
Abeer et al. [16]
97.1
96.3
97.9
–
0.988
Abeer et al. [17]
99.2
98.8
99.1
96
0.998
The proposed
99.8
99.9
99.8
98.1
1.0
The bold values is the key takeaways or summarized results from the data
Neural Computing and Applications (2025) 37:4881–4894
4893
123

---

## Page 14
data labeling for medical applications, Springer, Cham, Athens,
Greece, pp 197-205
14. Al-Antari MA, Han S-M, Kim T-S (2020) Evaluation of deep
learning detection and classiﬁcation towards computer-aided
diagnosis of breast lesions in digital X-ray mammograms.
Comput Methods Programs Biomed 196:105584
15. Sannasi Chakravarthy SR, Bharanidharan N, Rajaguru H (2023)
Multi-deep CNN based experimentations for early diagnosis of
breast cancer. IETE J Res 69(10):1–16
16. Saber Abeer, Keshk AE, Abo-Seida OM, Sakr M (2022) Tumor
detection and classiﬁcation in breast mammography based on
ﬁne-tuned convolutional neural networks. IJCI Int J Comput
Inform 9(1):74–84
17. Saber A, Hussien AG, Awad WA, Mahmoud A, Allakany A
(2023) Adapting the pre-trained convolutional neural networks to
improve the anomaly detection and classiﬁcation in mammo-
graphic images. Sci Rep 13(1):14877
18. Saber A, Sakr M, Abou-Seida O, Keshk A (2021) A novel
transfer-learning model for automatic detection and classiﬁcation
of breast cancer based deep CNN. Kafrelsheikh J Inf Sci 2(1):1–9
19. Sahu A, Das PK, Meher S (2024) An efﬁcient deep learning
scheme to detect breast cancer using mammogram and ultrasound
breast images. Biomed Signal Process Control 87:105377
20. Qian L, Bai J, Huang Y, Zeebaree DQ, Saffari A, Zebari DA
(2024) Breast cancer diagnosis using evolving deep convolutional
neural network based on hybrid extreme learning machine tech-
nique and improved chimp optimization algorithm. Biomed
Signal Process Control 87:105492
21. Gudur R, Tamboli AI, Kumar I, Joshi K (2024) Integration of
genetic
algorithm
and
convolutional
neural
networks
for
histopathological image analysis in breast cancer diagnosis. Int J
Intell Syst Appl Eng 12(3):542–552
22. Rahman H, Naik Bukht TF, Ahmad R, Almadhor A, Javed AR
(2023) Efﬁcient breast cancer diagnosis from complex mammo-
graphic images using deep convolutional neural network. Comput
Intell Neurosci. https://doi.org/10.1155/2023/7717712
23. Srikantamurthy MM, Subramanyam Rallabandi VP, Dudekula
DB, Natarajan S, Park J (2023) Classiﬁcation of benign and
malignant subtypes of breast cancer histopathology imaging
using hybrid CNN-LSTM based transfer learning. BMC Med
Imaging 23(1):19
24. Sharmin S, Ahammad T, Talukder MA, Ghose P (2023) A hybrid
dependable deep feature extraction and ensemble-based machine
learning approach for breast cancer detection. IEEE Access
25. Mudrakola S, Hegde N (2023) Removal of noise on mammogram
breast images using ﬁltering methods. Concurr Comput Pract Exp
35(1):e7444
26. Lotufo RA, Audigier R, Sau´de AV, Machado RC (2023) Mor-
phological image processing. In: Microscope image processing,
Academic Press, pp 75–117.
27. Musa P, Al RaﬁF, Lamsani M (2018) A review: contrast-limited
adaptive histogram equalization (CLAHE) methods to help the
application of face recognition. In: 2018 3rd international con-
ference on informatics and computing (ICIC), IEEE, pp 1–6
28. Talaat FM, El-Sappagh S, Alnowaiser K, Hassan E (2024)
Improved prostate cancer diagnosis using a modiﬁed ResNet50-
based deep learning architecture. BMC Med Info Decis Making
24(1):23
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
4894
Neural Computing and Applications (2025) 37:4881–4894
123

---
