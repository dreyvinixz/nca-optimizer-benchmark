# Integrating fuzzy metrics and negation operator in FCM algorithm via genetic algorithm for MRI image segmentation

**Year**: 2024 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-024-09994-3

---

## Page 1
ORIGINAL ARTICLE
Integrating fuzzy metrics and negation operator in FCM algorithm
via genetic algorithm for MRI image segmentation
Fatih Kutlu1
• I˙brahim Ayaz2 • Harish Garg3
Received: 13 January 2024 / Accepted: 9 May 2024 / Published online: 4 June 2024
 The Author(s) 2024
Abstract
In this study, we redeﬁne FCM algorithm by integrating fuzzy set theory, fuzzy metrics, and Sugeno negation principles. This
innovative approach overcomes the limitations inherent in conventional machine learning models, especially in situations char-
acterizedbyuncertainty,noise,andambiguity.Ourmodelutilizesthemembershipdegreesfromfuzzysettheory,andtransformsthe
concept of proximity deﬁned by fuzzy metrics into a minimization problem. This transformation is achieved using a linguistic
negationoperator,whichiscrucialforoptimizingFCMalgorithm’sobjectivefunction.Asigniﬁcantinnovationinourresearchisthe
useofGAforoptimizingparameterswithinthecontextsoffuzzymetricsandSugenonegation.Thepreciseoptimizationcapabilities
ofGAgreatlyenhancethesensitivityandadaptabilityofFCMalgorithm,therebyimprovingoverallperformance.Byleveragingthe
meticulous parameter adjustments provided by GA, our approach has shown superior results in practical applications, such as brain
MRI image segmentation, surpassing traditional methods. Experimental results highlight the considerable enhancements our
proposed FCM algorithms bring over existing methods across various performance metrics. In conclusion, this study makes a
valuable addition to the ﬁeld of fuzzy-based machine learning methodologies. It combines the optimization strength of GA with the
ﬂexible classiﬁcation capabilities of fuzzy logic. The integration of Sugeno negation and fuzzy metrics not only improves the
accuracy and precision of FCM algorithm but also provides signiﬁcant beneﬁts in handling complex and ambiguous datasets. This
research signiﬁes a major advance in machine learning and fuzzy logic, setting the stage for future applications and studies.
Keywords Fuzzy C-means  Fuzzy metrics  Sugeno negation  Genetic algorithms  Image segmentation
1 Introduction
The concept of fuzzy set theory, introduced by Zadeh [1],
revolutionized the way we approach problems character-
ized by uncertainty and ambiguity. Unlike classical set
theory, which conﬁnes elements to a binary membership of
either belonging to or not belonging to a set, fuzzy set
theory introduces the idea of partial membership. This
allows for a more nuanced representation of real-world
phenomena, where the boundaries between categories are
not always clear-cut. By quantifying the degree of mem-
bership of elements to sets, fuzzy set theory provides a
powerful mathematical framework to model the vagueness
inherent in many complex systems, ranging from decision-
making processes to pattern recognition and beyond.
Recently, the incorporation of fuzzy concepts into machine
learning methods has signiﬁcantly increased, offering
strong solutions to complicated issues [2]. Traditional
machine learning algorithms often operate under the
assumption of crisp, deterministic logic, where data points
are assigned to distinct categories or classes. However, this
deterministic approach may not be suitable for many
complex scenarios where data points do not clearly belong
to a single category but rather have degrees of membership
& Fatih Kutlu
fatihkutlu@yyu.edu.tr
I˙brahim Ayaz
iayaz@beu.edu.tr
Harish Garg
harishg58iitr@gmail.com; harish.garg@thapar.edu
1
Department of Artiﬁcial Intelligence and Robotics, Van
Yu¨zu¨ncu¨ Yıl University, Van, Turkey
2
Department of Computer Technologies, Bitlis Eren
University, Bitlis, Turkey
3
Department of Mathematics, Thapar Institute of Engineering
and Technology (Deemed University), Patiala,
Punjab 147004, India
123
Neural Computing and Applications (2024) 36:17057–17077
https://doi.org/10.1007/s00521-024-09994-3
(0123456789().,-volV)(0123456789().
,- volV)

---

## Page 2
in multiple categories. The concept of degrees of mem-
bership, a cornerstone of fuzzy set theory, provides a more
nuanced and ﬂexible approach to categorization, making it
a valuable addition to the machine learning toolkit for
handling real-world problems characterized by impreci-
sion, noise, and ambiguity.
Among fuzzy machine learning methods, FCM algo-
rithm, initially deﬁned by Dunn [3] and later improved by
Bezdek [4], has gained widespread acceptance as the most
prevalent technique in the arena of clustering. Unlike the
K-means algorithm, which rigidly assigns each data point
to a single cluster, FCM algorithm allows data points to
have varying degrees of membership across multiple
clusters, offering a more ﬂexible and robust solution to
real-world clustering problems [5].
Recent advancements in machine learning have high-
lighted FCM algorithms versatility and effectiveness of
FCM algorithms across a range of complex applications.
This algorithm has been pivotal in enhancing the perfor-
mance of various machine learning algorithms through its
application in diverse areas, such as pattern recognition,
image segmentation, brain tumor classiﬁcation, and even in
ﬁelds
extending
to
natural
language
processing
and
regression analysis. Starting with the integration of FCM in
automatic clustering for enhanced pattern recognition
through GA [6], the evolution of its applications spans
sophisticated methodologies like patch-based fuzzy local
similarity c-means for image segmentation [7] and extends
to the classiﬁcation of brain tumors using super resolution
and convolutional neural networks in tandem with FCM
[8]. The algorithm has also been utilized in real-time online
pattern recognition using array sensors [9], and in a novel
brain MRI image segmentation method that leverages an
improved multi-view FCM clustering algorithm [10].
Furthermore, the adaptability of FCM is showcased
through its integration with the whale optimization algo-
rithm for innovative image segmentation approaches [11]
and the construction of TSK fuzzy regression models uti-
lizing FCM for enhanced data analysis precision [12].
Notably, FCM has also been applied in the automatic
recognition of face masks using BPNN [13], in anti-noise
image segmentation methods to improve reliability in noisy
environments [14], and in the extraction of topics from
textual data collections, demonstrating its versatility in
handling unstructured data [15]. In more speciﬁc applica-
tions, FCM has contributed to the development of safety
warning models for coal faces using fuzzy clustering and
neural networks [16] and the enhancement of anomaly
detection in databases through a FCM-based isolation
forest method [17]. Lastly, the forecasting of water quality,
leveraging data decomposition and deep learning neural
networks in conjunction with fuzzy clustering, highlights
the algorithm’s capability in environmental applications
[18].
These studies underscore FCM algorithm’s signiﬁcant
role in advancing the ﬁeld of machine learning through its
ﬂexibility and effectiveness in addressing and solving
multifaceted problems across various disciplines. Fuzzy
clustering methodologies can be broadly divided into two
distinct paradigms: one predicated on the concept of fuzzy
relations and the other hinging on the strategic utilization
of the objective function [19]. Fuzzy relations delve into
the intricate structural interconnections among entities,
characterized by degrees of similarity or dissimilarity,
thereby offering a nuanced perspective on their relation-
ships. On the other hand, objective function-based algo-
rithms
ingeniously
transform
the
complex
issue
of
clustering into an optimization problem. The degree of
homogeneity within the cluster is meticulously gauged
through the objective function, and the optimal partitioning
is achieved by minimizing this objective function. These
methods necessitate a clear understanding of the number of
clusters and the speciﬁc attributes of the cluster prototypes
and exhibit a high degree of sensitivity to the initial values
in the clustering process [20].
The transformative capability of fuzzy set theory to
reconceptualize classical sets establishes a broader frame-
work for understanding mathematical constructs. This
paradigm, having yielded a panoply of comprehensive
concepts, positions itself as a potentially superior alterna-
tive to conventional methodologies. A case in point is the
notion of distance, which, under the lens of fuzzy metrics,
obtains a novel interpretation [21–26]. The integration of
the fuzziﬁed interpretation of distance, as offered by fuzzy
metrics, could signiﬁcantly augment FCM algorithm.
Deﬁned by a degree of closeness, the fuzzy metric could
engender a robust clustering mechanism adaptable to
intricate data scenarios, thereby yielding a versatile model
proﬁcient at handling heterogeneous data structures and
noise in image segmentation [27–29].
The aim of this study is to redeﬁne FCM algorithm using
fuzzy metrics and a negation operator. Since the fuzzy
metric is deﬁned based on a degree of closeness, we use a
linguistic negation operator to express this degree as a
degree of distance, thus converting it into a minimization
problem of the objective function, including the original
FCM. The use of this negation operator actually involves a
fuzziﬁcation process when converting the concept of
proximity to distance. This allows us to obtain a more
precise calculation mechanism with a greater number of
meaningful parameters. Both the parameters encountered
in the fuzzy metric and the parameters encountered in the
negation operator are optimized using GA. We have tested
this innovative approach on brain MRI image segmenta-
tion,
where
it
demonstrated
practical
effectiveness.
17058
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 3
Therefore, this paper aims to explore the potential of
redeﬁning FCM algorithm within the boundaries of fuzzy
set theory and fuzzy metrics. By examining the theoretical
foundations, real-world applications, and possible chal-
lenges of this paradigm shift, it aims to promote a more
detailed understanding of clustering algorithms and accel-
erate further progress in the ﬁeld. In this study, we illustrate
how FCM algorithm categorizes data points within a
multidimensional space and determines the centers of these
groups based on the geometric locations of data points. By
evaluating the ’distance’ of each data point to the group
centers using fuzzy metrics, we reveal the algorithm’s
robustness from a geometric perspective. This geometric
framing not only enhances our understanding of the algo-
rithm’s mechanics but also underscores its applicability in
handling complex data structures inherent in machine
learning tasks. To better elucidate the contributions of this
research, we succinctly list the signiﬁcant advancements
made by our study below:
1.
Innovative redeﬁnition of FCM algorithm: We intro-
duce a novel approach by integrating fuzzy set theory,
fuzzy metrics, and Sugeno negation principles into
FCM algorithm, signiﬁcantly enhancing its perfor-
mance, especially in handling data characterized by
uncertainty, noise, and ambiguity.
2.
Enhanced clustering mechanism via fuzzy logic: By
employing fuzzy logic, including fuzzy metrics for
proximity assessment and Sugeno negation for distance
interpretation, we provide a more ﬂexible and accurate
clustering mechanism. This advancement allows for
more nuanced data segmentation, which is particularly
beneﬁcial for medical imaging like MRI.
3.
Parameter
optimization
with
GA:
Our
research
employs GA for the optimization of the parameters
within the fuzzy metrics and the negation operator.
This optimization improves the algorithm’s sensitivity
and adaptability, leading to superior segmentation
outcomes.
4.
Superior performance in MRI image segmentation:
Through rigorous experimentation, our modiﬁed FCM
algorithm demonstrates signiﬁcant improvements over
traditional methods in the segmentation of brain MRI
images. The enhancements are evident in accuracy,
precision, recall, and overall segmentation quality,
underscoring the potential of our methodology to reﬁne
diagnostic processes.
5.
Framework for future fuzzy-based machine learning
models: Our study not only advances the ﬁeld of
machine learning in the context of MRI image
segmentation but also sets a foundation for future
research.
By
highlighting
the
effectiveness
of
integrating fuzzy logic with GA, we pave the way for
exploring other complex data analysis tasks.
These contributions underline the signiﬁcance of our
work, advancing the capabilities of machine learning
models to address and solve multifaceted problems across
various
disciplines,
particularly
in
medical
imaging
analysis.
The paper is divided into several sections: Sect. 2 lays
out basic concepts related to fuzzy sets and fuzzy metrics,
setting the groundwork for our redeﬁned FCM algorithm.
Section 3 introduces our proposed FCM algorithm and
provides information about GA used for optimization. The
ﬁnal section showcases experimental results, demonstrat-
ing the real-world application of our model in brain MRI
image segmentation. To ensure clarity and ease of under-
standing, the abbreviations used throughout this manuscript
are listed below (Table 1):
2 Related works
The segmentation of brain MRI images is a pivotal com-
ponent in medical image analysis, necessitating the precise
delineation of brain tissues for accurate diagnosis, treat-
ment planning, and the monitoring of brain conditions.
Over the years, FCM algorithm and its enhancements have
been instrumental in pushing the boundaries of segmenta-
tion accuracy and efﬁciency. This section encapsulates
signiﬁcant strides made in brain MRI segmentation, with a
special focus on innovations in FCM techniques.
The foundational contribution by Pham and Prince [30]
laid the groundwork for FCM-based segmentation meth-
ods, addressing the challenges posed by noise and intensity
inhomogeneities in MRI images. Following this, Siyal and
Yu [31] demonstrated how modiﬁcations to the standard
FCM could enhance segmentation in the presence of
Table 1 Abbreviations
Abbreviation
Full term
FCM
Fuzzy C-means
GA
Genetic algorithm
MRI
Magnetic resonance imaging
SE
Sensitivity
SP
Speciﬁcity
PR
Precision
F1
F1 score
ACC
Accuracy
IoU
Intersection over union
N/A
Not applicable
Neural Computing and Applications (2024) 36:17057–17077
17059
123

---

## Page 4
intensity inhomogeneities. Singh and Bala [32] further
advanced this ﬁeld by proposing a DCT-based local and
non-local FCM algorithm that balanced noise reduction
with the preservation of image details.
Bai et al. [33] introduced an improved probabilistic
FCM method that, through the application of a similarity
measure, effectively mitigated the ‘‘cluster-size sensitiv-
ity’’ problem while bolstering resistance to noisy images.
That same year, Huang et al. [34] merged FCM clustering
with rough set theory to achieve superior segmentation
outcomes for fuzzy boundary regions. Liu et al. [35] pro-
posed a novel FCM approach that utilized multiple-surface
approximation and interval memberships for bias correc-
tion and segmentation of brain MRI, marking a signiﬁcant
methodological advance.
The work of Valsalan et al. [36] presented a knowledge-
based FCM method that signiﬁcantly expedited brain tissue
segmentation from MRI scans by leveraging a CUDA-en-
abled GPU machine. Tavakoli-Zaniani et al. [37] devel-
oped
a
modiﬁed
FCM
algorithm
based
on
double
estimation, which proved effective in segmenting brain
structures from noisy MR images, demonstrating enhanced
robustness against noise.
Integrating evolutionary algorithms for learning model
optimization, our study introduces a distinct synthesis of
FCM algorithm enhancements, fuzzy set theory, and GA
optimization, speciﬁcally tailored for MRI image seg-
mentation. Unlike the focused applications seen in [38, 39],
which apply FCM and GA in supervisory control and
disease diagnosis, respectively, our research pioneers the
use of these methodologies to signiﬁcantly enhance seg-
mentation accuracy within the complex domain of medical
imaging. Neves-Jr. et al.’s exploration into the chemical
industry processes and Chen et al.’s advancement in Tra-
ditional Chinese Medicine diagnosis demonstrate the ver-
satility of combining FCM with GA; however, our
approach optimizes this integration for the nuanced chal-
lenges inherent in MRI image segmentation. This opti-
mization includes a detailed focus on fuzzy metrics and
Sugeno negation principles, key to addressing noise and
ambiguity
in
segmentation
tasks.
Furthermore,
our
methodology differentiates itself from [40], who investi-
gated the efﬁciency of GA in learning FCM through
metaheuristic methods, by not only utilizing GA for sup-
plementary optimization but embedding it as a core com-
ponent of redeﬁning FCM algorithm itself. The comparison
with simulated annealing underscores the potential of
evolutionary algorithms in reﬁning learning models, yet
our implementation showcases a novel application in
medical imaging that leverages GA’s robust optimization
capabilities more fully. Additionally, Wang et al. [41]
highlighted GA’s utility in optimizing cluster results for
signal sorting, illustrating GA’s broad applicability in
solving complex clustering challenges. Our study, how-
ever, extends these concepts to the medical imaging
domain, demonstrating a notable enhancement in MRI
image segmentation. Our experimental ﬁndings on the
BraTS2018 dataset afﬁrm the efﬁcacy of our approach,
revealing signiﬁcant improvements in accuracy, precision,
and recall rates compared to conventional methods.
Building on the seminal works in the ﬁeld, our research
marks a notable advancement in the utilization of evolu-
tionary algorithms for the optimization of learning models,
particularly within medical imaging analysis. We present a
transformative enhancement of FCM algorithm through an
intricate integration of GA for parameter optimization,
alongside the application of fuzzy set theory, fuzzy metrics,
and the Sugeno negation operator. This multifaceted
approach not only effectively navigates the challenges
posed by data ambiguity, noise, and imprecision but also
fosters a more ﬂexible and reﬁned strategy for addressing
segmentation dilemmas.
The innovative melding of these technologies within our
study not only illuminates the superior effectiveness of an
evolved FCM algorithm in medical image segmentation
but also signiﬁes a substantial leap forward in the ﬁeld. By
melding the optimization strength of GA with the adaptive
classiﬁcation capabilities of fuzzy logic, we unveil a robust
and nuanced solution to the complexities of medical
imaging. This research endeavors to signiﬁcantly enrich the
corpus of FCM-based segmentation methodologies, estab-
lishing a foundational framework for future explorations
and advancements in medical imaging analysis.
3 Fuzzy sets and fuzzy metric
Definition 3.1
[1] A fuzzy set A on non-empty set X is a
set
of
ordered
pair
A ¼
x; lA x
ð Þ
ð
Þ : x 2 X
f
g
where
lA : X ! I ¼ 0,1
½
. For each 8x 2 X, the value lA x
ð Þ is
called as membership degree of x to A and the function lA
is called membership function of A. Let denote set of all
fuzzy sets on X by FSX.
Each classical (crisp) set can be interpreted as a fuzzy
set with its characteristic function, suggesting that fuzzy set
theory provides a more expansive perspective than classi-
cal set theory. By re-examining various mathematical
concepts through the lens of fuzzy set theory, we can
generate new, wider, and more practical concepts that
surpass traditional methods. The concept of distance is a
particularly noteworthy example of these notions. In fuzzy
set theory, distance, often explored through the notion of a
metric, has many generalizations, with the fuzzy metric
concept being a key example. The measure of proximity or
closeness, used in the fuzzy metric concept, indicates the
17060
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 5
distance between points. Before providing the deﬁnition of
fuzzy metrics, let us ﬁrst establish the deﬁnitions of several
key concepts that will be employed within the proposed
FCM algorithm.
Definition 3.2
[42] If N : 0,1
½
 ! 0,1
½
 function satisﬁes
the following conditions, N is called a negation.
1.
N 0
ð Þ ¼ 1, N 1
ð Þ ¼ 0,
2.
Nis
a
non-increasing
function,
i.e.,
x  y ) N x
ð Þ  N y
ð Þx; y 2 0,1
½
.
If a negation is monotonously decreasing, i.e., x\y )
N x
ð Þ [ N y
ð Þ for x; y 2 0,1
½
 and continuous, it is called a
strict negation. If a strict negation is an involution, i.e.,
N N x
ð Þ
ð
Þ ¼ x for x 2 0,1
½
, it is called a strong negation.
Definition 3.3
[42] If the binary operator T : 0,1
½
 
0,1
½
 ! 0,1
½
 satisﬁed the following conditions for all
a; b; c; d 2 0,1
½
 then it is called a triangular norm (brieﬂy
t-norm).
1.
Bounded Condition: T 1; a
ð
Þ ¼ a
2.
Monotonicity: a  c ve b  d )T a; b
ð
Þ  T c; d
ð
Þ,
3.
Commutativity:T a; b
ð
Þ ¼ T b; a
ð
Þ,
4.
Associativity:T a; T b; c
ð
Þ
ð
Þ ¼ T T a; b
ð
Þ; c
ð
Þ
As can be understood from these properties, the t-norm
is a monotonously non-decreasing function and provides
T a; 0
ð
Þ ¼ 0. Examples of the most used t-norms are min-
imum, algebraic multiplication, and Lukasiewicz t-norms
deﬁned by Tða; bÞ ¼ maxf0; a þ b  1g.
The concept of fuzzy metric, initially deﬁned by Kra-
mosil and Michalek [21] and later revisited by George and
Veeramani [22] to derive the Hausdorff topology, holds a
signiﬁcant place. This deﬁnition focuses not on the con-
crete distance between two points but rather on the fuzzy
grading that gives rise to such a distance.
Definition 3.4
[22] The 3-tuple
X; M; 
ð
Þ is said to be a
fuzzy metric space if X is an arbitrary set, * is a continuous
t-norm and M is a fuzzy set on X2  0; 1
ð
Þ satisfying the
following conditions:
1.
M x; y; t
ð
Þ [ 0
2.
M x; y; t
ð
Þ ¼ 1 if and only if x ¼ y
3.
M x; y; t
ð
Þ ¼ M y; x; t
ð
Þ
4.
M x; y; t
ð
Þ  M y; z; s
ð
Þ  M x; z; t þ s
ð
Þ
5.
M x; y; :
ð
Þ : 0; 1
ð
Þ ! 0; 1
½
 is continuous.
where x, y, z 2 X and t, s [ 0. In this case, M x; y; t
ð
Þ is
referred to as the proximity of x and y with regard to t. In
other terms, it refers to the truth of the statement ‘‘x is as close
to y as t’’. In [22, 25], several methods are deﬁned for
deriving fuzzy metrics from traditional metrics. Following the
deﬁnition of a fuzzy metric space, it is crucial to underscore
the signiﬁcance of each condition detailed within this
framework. At its core, a fuzzy metric space extends the
traditional notion of a metric space by incorporating the
concept of ’fuzziness’, reﬂecting the real-world ambiguity
and gradual variation in distances between points:
1.
Nonzero condition: This ensures that the fuzzy distance
between any two points is always positive, except
when the points coincide, enhancing the model’s
robustness by accounting for the subtle gradations in
proximity that classical metrics might overlook.
2.
Identity of indiscernible: By stipulating that the fuzzy
distance equals one if and only if the points are
identical, this condition aligns with the intuitive
understanding of distance, reinforcing the metric’s
relevance to real-world scenarios where exact matches
are distinct from close resemblances.
3.
Symmetry: The requirement that the fuzzy distance from
point X toY isthe same asfromY toX mirrorsthe physical
world’s symmetry in distances, ensuring the metric’s
applicability across different domains without bias.
4.
Triangle inequality: A cornerstone of metric spaces,
this condition is adapted to the fuzzy context to
maintain the essential logic of distances within a more
ﬂexible framework. It ensures that the direct distance
between two points is always less than or equal to the
distance via a third point, preserving the intuitive
notion of distance despite the introduction of fuzziness.
5.
Continuity: The continuity of the fuzzy metric with
respect to time guarantees that small changes in the
temporal parameter do not lead to abrupt changes in
perceived closeness, reﬂecting the gradual shifts that
characterize real-world phenomena.
Each of these conditions plays a pivotal role in deﬁning
a coherent and applicable metric space that captures the
essence of fuzziness, enabling the precise modeling of
systems and
processes fraught with uncertainty and
imprecision. The integration of fuzzy metric spaces into
our study lays the groundwork for leveraging this mathe-
matical construct in the enhancement of FCM algorithm for
MRI
image
segmentation.
This
approach
not
only
acknowledges but also embraces the inherent ambiguity in
medical imaging, aiming for a segmentation method that is
both nuanced and highly adaptable to the complex, layered
nature of brain MRI data. The innovative aspect of this
notion lies in its ability to develop a more universal and
adaptable distance measurement while preserving the
essential topological characteristics typically associated
with metric spaces. This is done by considering fuzzy
metrics that are not derivable from classical metrics. The
concept of fuzzy metric fuses the established principles of
classical topology with the computational advantages of
degree of closeness. Consequently, this allows for prob-
lems
to
be
addressed
with
a
more
comprehensive,
Neural Computing and Applications (2024) 36:17057–17077
17061
123

---

## Page 6
linguistically nuanced approach while maintaining their
inherent topological and geometric attributes.
4 Proposed FCM algorithm using fuzzy
metrics and negation operator through
GA
FCM algorithm enables the division of images based on the
similarities and differences of grayscale pixels. In a marked
departure from prior methodologies, FCM acknowledges
that entities can belong to multiple clusters. The funda-
mental concept of fuzzy logic posits that each data item has
a degree of membership lying between [0,1], thereby cre-
ating distinctive clusters for each membership [4]. The
aggregate of membership values spanning all classes for a
data point must equal to 1, i.e., uij  0 for i = 1,2…n and
j = 1,2…c:
X
c
j¼1
uij ¼ 1
ð1Þ
where uij is the membership value of the i-th data to the j-th
cluster. The degree of belonging to the cluster that the
object is closest to will be greater than the degree of
belonging to other clusters. The objective function is given
in Eq. 2.
J u; v
ð
Þ ¼
X
N
i¼1
X
C
j¼1
um
ij xi  vj

2; 1  m\1
ð2Þ
Equation 2 consists of the following variables: X repre-
sents the data as a set x1; x2; . ..; xn
f
g; C denotes the number
of clusters in X; m is the weighting exponent, satisfying
m  1; vj corresponds to the center of the j-th cluster; uij
represents the membership value of xi to the j-th cluster; jj  jj
denotes a norm deﬁned on the vector space RN. FCM algo-
rithm prototype can be obtained by minimizing the objective
function J u; v
ð
Þ for each value of C. Speciﬁcally, this
involves taking the partial derivative of J u; v
ð
Þ with respect to
vj and setting it to zero. The cluster centers and membership
values are calculated using Eq. 3 and Eq. 4, respectively:
vi ¼
PN
i¼1 uik
ð
Þmxj
PN
i¼1 uik
ð
Þm
ð3Þ
uij ¼
1
P
c
k¼1
xjvi
k
k
xjvk
k
k

 2
m1
"
#
ð4Þ
Following are the stages taken by FCM algorithm
(Table 2):
We will present FCM algorithm in the context of our
investigation
using
a
novel
method.
The
primary
distinction is that the traditional distance measures will be
replaced with a fuzzy metric-based distance measure. The
fuzzy distances calculated using the fuzzy metric are
changed from the degree of proximity to the degree of
distance using a negation in order to produce a fuzzy
metric-based distance measure. At this point, negation
operators of the Yager or Sugeno types are primarily
employed. As a result, by considering the degree of prox-
imity rather than language, the epistemic meaning of dis-
tance is provided. One of the novel techniques of this work
is the application of the proximity-based distance measure
in FCM algorithm. At this point, it is important to convert
the fuzzy metric’s measurement of closeness into a mea-
surement of distance from the dual. This transition is
accomplished by using strong negations. In this work, the
following fuzzy metrics and negation are used:
i. Let X; d
ð
Þ be any classical metric space (e.g., R; j  j
ð
Þ).
Deﬁne a  b ¼ a:b and
M1 x; y; t
ð
Þ ¼
1
ed x;y
ð
Þ=t
for all x; y 2 X and t [ 0. Then
X; M1; 
ð
Þ is a fuzzy
metric [22].
ii. Let
X; d
ð
Þ be any classical metric space (e.g.,
R; j  j
ð
Þ). Deﬁne a  b ¼ a:b and
M2 x; y; t
ð
Þ ¼
a1ta3
a1ta3 þ a2d x; y
ð
Þ
for all x; y 2 X and a1; a2; a3; t [ 0. Then X; M2; 
ð
Þ is a
fuzzy metric [25].
iii. Let X ¼ Rþ and deﬁne a  b ¼ a:b and
M3 x; y; t
ð
Þ ¼
min x; y
f
g
ð
Þa1þt
max x; y
f
g
ð
Þa1þt

a2
for all x; y 2 X and b1; b2; t [ 0. Then
X; M3; 
ð
Þ is a
fuzzy metric [25].
To interpret these closeness’s into distances from the
dual, employ Sugeno Negation deﬁned as follow:
NS x
ð Þ ¼ 1  x
1 þ kx
for k [  1 and x 2 0; 1
½
 [42].
The objective function in this proposed algorithm is
deﬁned as follows:
J u; v
ð
Þ ¼
X
N
i¼1
X
C
j¼1
um
ij dfuzzy xi; vj

2; 1  m\1
ð5Þ
where dfuzzy xi; vj


= N M xi; vj; t




for N is a strong fuzzy
negation and M is a fuzzy metric. The structure of this
novel clustering algorithm, as deﬁned by the fuzzy metric,
mirrors
that
of
the
traditional
FCM
algorithm.
By
17062
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 7
maintaining the logical framework of FCM and introducing
fuzziness to the concept of distance within it, a new clus-
tering approach has been developed. This method upholds
the topological features of the traditional approach while
capitalizing on the linguistic and logical advantages offered
by fuzzy set theory. Within this innovative approach that
employs fuzzy negation and degree of closeness, it is
apparent that several variables can signiﬁcantly inﬂuence
the clustering results. The efﬁcacy of the clustering pro-
cess, which involves extracting necessary features from the
primary image, is contingent on the choice of these
parameters. Consequently, the utilization of GA for
parameter optimization has led to the development of a
more proﬁcient method.
5 Explanation of programmatic model
construction
To elucidate the construction of our programmatic model,
this section is dedicated to detailing the parameters, sim-
ulation environment setup, and genetic parameters utilized
to initialize GA which plays a pivotal role in optimizing
our modiﬁed FCM algorithm.
5.1 Simulation environment setup
The simulation environment for our study was meticu-
lously architected to facilitate rigorous testing and valida-
tion of the proposed algorithm. This computational setup
was instantiated on a system equipped with an AMD Ryzen
7 CPU, an NVIDIA RTX A5000 GPU, and 128 GB of
RAM, operating under Windows 11. The algorithm itself
was implemented using Python 3.8, which was chosen for
its robust capabilities in numerical computations and
optimization routines.
5.2 Parameters definition and GA initialization
In our study, numerous parameters exist within the inte-
grated fuzzy metrics and negation operator, necessitating
optimization. These parameters, inherently multitudinous,
are not merely a complication but rather a rich source of
ﬁne-tuning potential, offering a higher degree of precision
in the algorithm’s performance. They enable a more
sophisticated modeling of the problem at hand and, there-
fore, more accurate segmentation in our application of MRI
imaging. These parameters have been optimized using GA,
demonstrating the utility of evolutionary computation
methods in handling the complexity and multidimension-
ality of the optimization landscape within the context of
our enhanced FCM algorithm. GA is a computational
method that draws inspiration from the principles of
genetics and natural selection, serving as a powerful opti-
mization and search technique. It is one of the earliest
population-based stochastic algorithms ever proposed, with
its roots deeply embedded in the biological evolution
paradigm [43–45]. GA operates through a series of pro-
cesses that mimic natural evolution, including evaluation,
selection, crossover (recombination), and mutation [44].
These processes are applied to a population of candidate
solutions to an optimization problem, with the aim of
evolving the population toward better solutions. In the
context of GA, these candidate solutions are represented as
vectors of equal size, often referred to as chromosomes.
The chromosomes are assembled randomly to form a
population. Each chromosome encodes a potential solution
to the problem at hand. The ﬁtness of each solution is
evaluated using an objective function, also known as the
ﬁtness function. This function quantiﬁes the quality of the
solutions, guiding the selection process where better solu-
tions (chromosomes with higher ﬁtness) are given a higher
chance to be selected for reproduction. During the cross-
over process, pairs of chromosomes exchange parts of their
structure, creating new offspring that combine traits from
both parents. The mutation process introduces small ran-
dom changes in the offspring, ensuring diversity in the
population and preventing premature convergence to sub-
optimal solutions. As the algorithm progresses, generations
of solutions are produced, each hopefully better than the
last, as they are guided by the ﬁtness function toward
optimal or near-optimal solutions to the problem. This
iterative process of selection, crossover, and mutation
continues until a satisfactory solution is found or a
Table 2 FCM algorithm
Neural Computing and Applications (2024) 36:17057–17077
17063
123

---

## Page 8
predeﬁned termination condition is met. Indeed, in recent
years, there has been an increasing trend toward utilizing
GA for optimizing fuzzy methods. This stems from the fact
that GAs are robust search algorithms based on the
mechanics of natural selection and genetics, making them
particularly suited for exploring complex, multidimen-
sional spaces such as those encountered in fuzzy logic and
systems. They provide a global search approach, avoiding
the local minima traps that other optimization methods may
fall
into.
Therefore,
GA’s
evolutionary
computation
methodology complements the inherent complexity of
fuzzy systems, allowing for a comprehensive optimization
of their numerous parameters. As a result, researchers and
practitioners are increasingly leveraging this combination
to solve complex problems across various ﬁelds, from
image segmentation to decision-making systems [46–48].
In this study, F1 score has been selected as the ﬁtness
function, and the pseudocode for GA constructed based on
this selection is provided in Table 3.
In this study, we leverage GA for optimizing parameters
of FCM algorithm, speciﬁcally devised for the segmenta-
tion of brain MR images. Our approach adopts an F1-
Score-based ﬁtness function, aiming to identify the optimal
set of parameters that maximizes the performance of the
algorithm. This optimization process notably beneﬁts from
the integration of fuzzy metrics and Sugeno negation,
signiﬁcantly enhancing the algorithm’s effectiveness on the
dataset.
The roles of fuzzy metric and Sugeno negation are
crucial in this context. The fuzzy metric offers a more
adaptable method for gauging the proximity between data
points compared to traditional metrics, adeptly managing
the data’s inherent uncertainty and noise. Conversely,
Sugeno negation transforms these proximity values into
distances, thus effectively contributing to solving the
minimization problem of FCM algorithm’s objective
function. This pivotal transformation bolsters the algo-
rithm’s ability to reﬁne segmentation precision while
simultaneously reducing false positives. Within the GA,
the ﬁtness function based on the F1-Score considers the
distance values derived from fuzzy metrics and Sugeno
negation, evaluating the efﬁcacy of each parameter set.
This synthesis guarantees a balanced performance in terms
of accuracy (precision) and sensitivity (recall), thereby
sharpening the segmentation outcomes’ precision and
minimizing the rate of false positives.
The fundamental motivation for selecting GA for this
purpose stems from their exceptional capability to navigate
complex, multidimensional optimization landscapes. Crit-
ical variables, including those within fuzzy metrics and the
Sugeno negation, are meticulously optimized using the
evolutionary computation methodology provided by GAs.
Moreover,
as
delineated
in
Table 3,
the
F1-Score
performance
metric,
recognized
for
its
efﬁcacy
in
addressing class imbalance problems, is integrated into the
GA’s ﬁtness function along with FCM algorithm. The ﬁt-
ness function creates a confusion matrix by conducting a
pixel-based comparison between the U matrix generated by
FCM and the ground truth image of MRI scans. This matrix
forms the foundation for calculating performance based on
the F1-Score metric.
Conclusively, the employment of GA in this study
substantially elevates the sensitivity and adaptability of
FCM algorithm. This integration facilitates more effective
parameter adjustments by the algorithm in datasets char-
acterized by complexity and uncertainty, thereby enhanc-
ing the overall segmentation results. When compared to
similar studies in the literature, this approach underscores
the robustness of combining F1-Score, fuzzy metrics, and
Sugeno negation, illustrating how such integration can
serve as a potent tool in segmentation challenges. The
hyperparameters for the GA were chosen based on values
commonly used in research, including a maximum iteration
count of 50, population size of 30, mutation probability of
0.1, elitism rate of 0.01, and crossover probability of 0.5.
These settings are designed to ensure the efﬁcient operation
of GA, facilitating the achievement of optimal or near-
optimal solutions. Below is a Table 4 summarizing the
optimized parameters, their symbols, descriptions, and the
search ranges used in the optimization process:
This Table provides an overview of the parameters
optimized using GA in this study, including their symbols,
descriptions, and deﬁned search ranges for each parameter.
The selection of parameters and their search ranges has
been carefully tailored to maximize the algorithm’s per-
formance and adaptability to the speciﬁc optimization
problem. The incorporation of these parameters and their
optimization through GA highlights the signiﬁcance of
combining the optimization power of GA with the ﬂexible
classiﬁcation capabilities of fuzzy logic to enhance the
accuracy and precision of FCM algorithm. This integration
not only improves FCM algorithm’s performance but also
signiﬁcantly beneﬁts handling complex and ambiguous
datasets, thereby marking a signiﬁcant advancement in the
ﬁeld of machine learning and fuzzy logic.
6 Experimental results
6.1 Dataset
In this research, the comprehensive and diversiﬁed col-
lection of MR images provided by the Brain Tumor Seg-
mentation (BraTS2018 [49–51]) competition has been
utilized as the primary source of data. The selected dataset
encompasses MR images of 285 patients, classiﬁed into
17064
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 9
two different tumor grades: high-grade gliomas (HGG) and
low-grade gliomas (LGG). This meticulously compiled
dataset offers four different imaging modalities for each
patient: T1-weighted images, T1 post-contrast (enhanced
with contrast agent) images, T2-weighted images, and
Fluid-Attenuated Inversion Recovery (FLAIR) images.
This diversity allows for the distinction of different phys-
iological and anatomical features of the tumor and sur-
rounding tissue, thus increasing the accuracy of the
segmentation process. The dataset includes corresponding
ground truth data, providing a reliable benchmark for the
evaluation of our segmentation results. During the data
processing phase, a careful preprocessing routine has been
applied to maximize the effectiveness of the segmentation
algorithm. This process, aimed at ensuring a homogeneous
examination of the images, includes normalization and
noise reduction techniques. The normalization procedure
scales the intensity values of the MR images to a standard
range, minimizing variations that may arise from different
scanning parameters and devices. This allows the algorithm
to interpret features on the image more consistently and
thereby more clearly delineate the boundaries between
tumor and healthy tissue.
In our application of MRI image segmentation, we delve
into how each pixel or voxel is positioned in space to
determine its afﬁliation with speciﬁc anatomical structures.
Our proposed FCM-based algorithm performs this group-
ing by considering the spatial locations and intensity values
of these pixels, thereby clearly delineating the geometric
boundaries of structures such as tumors. The critical role of
GA in optimizing these parameters signiﬁcantly reﬁnes
segmentation accuracy, thereby improving the geometric
representation of the segmented structures. This approach
not only optimizes the clustering process but also provides
a vivid geometric insight into the segmentation of complex
images, illustrating the potential of our method for accu-
rately identifying and outlining critical anatomical features.
6.2 Performance measures and optimal
parameters
Our approach involved conducting a pixel-based classiﬁ-
cation with FCM algorithm enhanced by three newly pro-
posed fuzzy metrics and Sugeno negation. Each fuzzy
metric was evaluated individually, offering distinct per-
spectives on the segmentation task. The integration of these
fuzzy metrics allowed us to comprehensively explore the
algorithm’s performance under various conditions, con-
tributing to a more thorough understanding of its capabil-
ities and limitations. In addition to FCM algorithm, GA
was employed to optimize hyperparameters of fuzzy met-
rics and Sugeno negation. GA have been proven effective
in tackling high-dimensional and complex optimization
problems, making them an ideal choice for our task. F1-
Score, a well-established performance metric in the ﬁeld of
image segmentation, served as the ﬁtness function in our
GA. FCM algorithm was set with a speciﬁc number of
clusters (C) equating to 6, a small epsilon value of 0.00001
to control the termination criteria, and a maximum iteration
limit set at 100. These settings were carefully chosen based
on preliminary tests and literature recommendations,
Table 3 GA with F1 score as the ﬁtness measure:
Table 4 Optimized parameters and their search ranges in GA optimization
Symbol
Description
Search range
m
Fuzziﬁcation parameter controlling the degree of data point spread across clusters in FCM algorithm
1:1  m  4
k
Sugeno negation parameter affecting the shape of the Sugeno negation operator and consequently the
sensitivity of distance measurement
2  k  4
t
Fuzzy distance criterion reﬂecting the proximity between two points in fuzzy metric space
1024\t  5000
a1, a2,
a3
Additional parameters for fuzzy metrics inﬂuencing the characteristics of fuzzy metrics and the distance
calculations between two points
1:1  ai  10;i ¼ 1; 2;
3
Neural Computing and Applications (2024) 36:17057–17077
17065
123

---

## Page 10
ensuring a balanced trade-off between computational efﬁ-
ciency and result accuracy. The parameters that were
optimized through the GA, including those of both FCM
and fuzzy metrics, are provided in Table 5. These results
demonstrate the effectiveness of the optimization process
and shed light on the optimal conditions under which our
proposed FCM algorithm performs best.
In the realm of brain MRI image segmentation, accu-
rately delineating pathological structures, such as tumors,
is paramount for diagnosis and therapeutic planning.
However, challenges such as the intensity similarity
between tumors and healthy tissues, noise, and boundary
ambiguity in MRI images signiﬁcantly complicate the
segmentation process. Classical methodologies, including
K-means and standard FCM algorithm, exhibit limited
success in overcoming these obstacles. K-means algorithm,
with its rigid assignment of data points to a single cluster,
fails to accommodate the inherently fuzzy boundaries and
varying degrees of membership characterizing biological
tissues. Conversely, while standard FCM offers more
ﬂexibility in membership allocation, it remains susceptible
to noise and outliers, adversely affecting segmentation
quality. The proposed FCM algorithm proposed in this
study, through the integration of fuzzy set theory, fuzzy
metrics, and Sugeno negation principles, addresses these
challenges head-on. This approach enables the algorithm to
more effectively process noise, ambiguity, and the fuzzy
nature
of
data,
thereby
overcoming
the
limitations
encountered by standard FCM. Experimental evaluations
conducted on the BraTS2018 dataset have demonstrated
signiﬁcant improvements in crucial performance metrics
such as precision, accuracy, and the F1 score compared to
classical methods. These enhancements are attributable to
parameter optimization facilitated by GA. The optimiza-
tion process, which notably enhances the algorithm’s sen-
sitivity and adaptability, has resulted in a marked increase
in segmentation quality.
In conclusion, the proposed FCM algorithm, by har-
nessing the synergy of fuzzy logic and GA, offers inno-
vative solutions to complex problems like brain MRI image
segmentation. This study exempliﬁes how the integration
of fuzzy logic and GA can substantially elevate the per-
formance of machine learning models. Moreover, it antic-
ipates the potential extension of this methodology to other
areas of medical imaging, thereby promising to improve
diagnostic and therapeutic processes within the health
sciences.
Pixel-based
classiﬁcation
was
executed
using
the
hyperparameters outlined in Table 4. In order to gauge the
effectiveness of our classiﬁcation, we employed a confu-
sion matrix, a powerful tool that provides a detailed
breakdown of the classiﬁcation results. The confusion
matrix is comprised of four main components, or inF1s, as
follows:
In our study, pixel-based classiﬁcation was conducted
using the outlined hyperparameters in Table 5. To evaluate
the classiﬁcation’s efﬁcacy, a confusion matrix was used. It
consists of four main components:
•
True positives (TP): instances where our algorithm
accurately segmented actual tumor areas.
•
True negatives (TN): instances where the algorithm
correctly recognized non-tumor areas.
•
False positives (FP): instances where the algorithm
incorrectly classiﬁed actual tumor areas as non-tumor.
•
False negatives (FN): instances where non-tumor areas
were mistakenly segmented as tumor areas by our
algorithm.
It should be noted that each instance corresponds to a
pixel in MRI images. Using these in F1s, we evaluated the
effectiveness of
our classiﬁcation
using performance
measurement metrics. The details of these metrics can be
found in Table 6. This comprehensive evaluation approach
allowed us to gain a deep understanding of the algorithm’s
performance in brain tumor segmentation.
Following our comprehensive standardization efforts,
we proceeded with executing the proposed FCM algo-
rithms fortiﬁed with the Sugeno negation and various fuzzy
metrics and standard FCM on an array of randomly
selected images from the dataset. These procedures utilized
optimized parameters, which were meticulously ﬁne-tuned
by GA to maximize the efﬁciency and effectiveness of our
image segmentation endeavors. The proposed algorithms,
through their intensive fuzzy metric calculations, embraced
the rich complexity of the 57,600 data points in each
image, fully exploiting the valuable information inherent in
each pixel. The application of Sugeno negation and fuzzy
metrics further enhanced the sensitivity of the proposed
Table 5 Optimized parameters
resulting from GA in FCM
algorithm with fuzzy metrics
and sugeno negation
Fuzzy metric
m
k
t
a1
a2
a3
Objective function (F1 score)
M1
1.642
3.707
4153
N/A*
N/A
N/A
86.9960%
M2
1.441
3.780
4.985
2.909
9.737
2.114
89.7516%
M3
1.158
2.321
2475
2.751
3.475
N/A
89.7831%
*Fields designated as ’N/A’ represent parameters that do not have corresponding elements in the equations
17066
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 11
FCM algorithms to variations in the pixel intensity, which
is a fundamental attribute in our image segmentation task.
This ultimately allowed the proposed FCMs to more
accurately segment the images into tumor and non-tumor
areas. In order to assess the performance of our approaches,
we delved into a rigorous evaluation process that was
underscored by a visual comparison of the segmented
images and a detailed investigation of key performance
metrics. Visually, the segmented images were juxtaposed
with the corresponding ground truth images. The clarity of
the segmented tumor areas in the modiﬁed FCM results as
compared to those in the classical FCM was profoundly
striking, demonstrating the signiﬁcant improvement in the
segmentation quality achieved through modiﬁcations.
Regarding performance metrics, we utilized the above-
mentioned measures to assess the quality of our segmen-
tation process. It was evident that proposed FCM algo-
rithms
consistently
surpassed
the
performance
of
traditional FCM methods, signifying the enhanced effec-
tiveness of our approach. A notable improvement was
observed in the precision rate, indicative of the proposed
FCM algorithm’s superior capacity to accurately delineate
tumor pixels. Likewise, an enhanced recall rate was wit-
nessed, marking a substantial increase in the identiﬁcation
of actual tumor pixels. Further indicators of overall per-
formance, namely the F1 score, exhibited signiﬁcant
progress, which highlighted an optimized balance between
precision and recall in our segmentation process. In con-
clusion, the performance of the modiﬁed FCMs approach
substantiates its superiority over classical methods and
showcases its potential in reﬁning the overall image seg-
mentation process.
Figure 1 outlines the workﬂow for our enhanced Brain
MRI Image Segmentation process utilizing the integration
of the proposed FCM with GA. The process begins with
image preprocessing that includes noise reduction and
normalization. Following this, FCM algorithm is optimized
by GA for parameter tuning based on the F1-Score, aimed
at improving segmentation precision. The workﬂow cul-
minates with the pixel-based classiﬁcation and evaluation,
where performance metrics are calculated from the con-
fusion matrix to assess the efﬁcacy of the segmentation.
This streamlined approach
demonstrates the model’s
capability for sophisticated MR image analysis.
6.3 Results
In this section, we delve into the results obtained from our
investigation into the segmentation of brain MRI images
using our proposed algorithm. By analyzing both the geo-
metrical
interpretations
and
the
quantitative
metrics
detailed in Tables 7, 8, 9, 10, we aim to provide a
Table 6 Key performance metrics deﬁnitions used for classiﬁcation evaluation
Metrics
Symbol
Formulization
Evaluation focus
Sensitivity
SE
TP
TPþFN
Measures the proportion of true positives correctly identiﬁed
Speciﬁcity
SP
TN
TNþFP
Evaluates the proportion of true negatives correctly identiﬁed
Precision
PR
TP
TPþFP
Measures the proportion of identiﬁed positives that are correct
F1 score
F1
2TP
2TPþFPþFN
Harmonic mean of precision and sensitivity, indicating segmentation quality
Accuracy
ACC
TPþTN
TPþFPþFNþTN
Proportion of total correct predictions
Intersection over union
IoU
TP
TPþFNþFP
Measures overlap between predicted and ground truth segmentation
Fig. 1 Flowchart of the brain MRI image segmentation using the proposed FCM and GA integration
Neural Computing and Applications (2024) 36:17057–17077
17067
123

---

## Page 12
comprehensive overview of the algorithm’s effectiveness.
This not only encompasses its accuracy in pinpointing
tumor regions within the brain but also its capacity to
differentiate between tumorous and non-tumorous tissues.
Such detailed scrutiny is pivotal for assessing the practical
utility of our algorithm in clinical settings, where precision
and reliability are paramount.
The geometrical interpretation and quantitative results
of the metrics presented in Tables 7, 8, 9, 10 provide a
deeper understanding of our algorithm’s performance in
brain MRI image segmentation. These interpretations help
illustrate not only the algorithm’s accuracy in identifying
tumor regions but also its effectiveness in distinguishing
between tumor and non-tumor areas.
•
F1 score: Geometrically, the F1 Score represents the
harmonic mean of precision and recall, illustrating the
balance between the algorithm’s accuracy in identifying
true tumor pixels (true positives) and its ability to
minimize false positives and false negatives. This
metric effectively quantiﬁes the overlap between the
algorithm-identiﬁed tumor areas and the actual tumor
areas, highlighting the segmentation’s precision and
reliability.
•
Precision: Precision measures the ratio of correctly
identiﬁed tumor pixels to all pixels identiﬁed as tumors
by the algorithm. Geometrically, this indicates the
extent to which the segmented tumor area correctly falls
within the actual tumor boundaries. A high precision
score signiﬁes that the majority of the pixels labeled as
tumor by the algorithm are true tumor pixels, minimiz-
ing over-segmentation.
•
Sensitivity (recall): Sensitivity, or recall, reﬂects the
proportion of actual tumor pixels that have been
correctly identiﬁed as such by the algorithm. Geomet-
rically, this metric assesses how much of the actual
tumor area is captured by the algorithm’s segmentation.
High sensitivity indicates that the algorithm effectively
identiﬁes
tumor
areas without
missing
signiﬁcant
portions,
which
is
crucial
for
accurate
medical
diagnoses.
•
Speciﬁcity: Speciﬁcity measures the proportion of non-
tumor pixels correctly identiﬁed as non-tumor by the
algorithm. Geometrically, this metric evaluates how
well the algorithm can delineate non-tumor areas,
ensuring that non-tumor tissues are not incorrectly
classiﬁed as tumors. High speciﬁcity indicates effective
exclusion of non-tumor areas from the segmented tumor
region, reducing false positives.
Incorporating these geometrical interpretations along-
side the numerical results in Tables 7, 8, 9, 10 enriches our
discussion on the algorithm’s segmentation performance. It
provides a clearer visual and mathematical explanation of
how well the proposed algorithm can differentiate between
tumor and non-tumor regions, further substantiating the
effectiveness of our method in medical image segmentation
tasks (Figs. 2, 3, 4, 5).
In this study, the innovative implementation of FCM
algorithm showcases the power of integrating fuzzy set
theory, fuzzy metrics, and Sugeno negation principles.
Descriptive analyses clearly illustrate that the proposed
algorithm achieves higher accuracy, precision, and recall
rates compared to traditional FCM methods. Speciﬁcally,
during experiments conducted on the BraTS2018 dataset,
FCM ? M1 ? Sugeno,
FCM ? M2 ? Sugeno,
and
FCM ? M3 ? Sugeno algorithms obtained F1 scores of
86.99%, 89.75%, and 89.62%, respectively. These ﬁg-
ures represent a notable improvement over the 85.30% F1
score achieved by the conventional FCM method.
The optimization process unfolds across several gener-
ations, each reﬁning the parameter set based on a ﬁtness
function that evaluates segmentation efﬁcacy. Speciﬁcally,
F1 score was utilized as the ﬁtness function due to its
balanced assessment of precision and recall, crucial for
gauging the quality of image segmentation. This evolu-
tionary process facilitates continuous improvement, with
selection, crossover, and mutation operations generating
progressively optimized parameter sets. Such a method-
ological approach ensures that the GA efﬁciently explores
the parameter space, avoiding local optima and steadily
improving segmentation outcomes. Observations from the
application of GA demonstrate substantial enhancements in
segmentation metrics, including accuracy, precision, and
F1 scores, which are indicative of the algorithm’s capacity
to ﬁne-tune parameters effectively across generations. The
iterative reﬁnement process highlights GA’s role in miti-
gating overﬁtting risks while optimizing for global solu-
tions, showcasing its critical contribution to advancing the
performance of FCM algorithm in complex imaging
Table 7 Performance metrics
results on
Brats18_2013_2_1_ﬂair image
Method
ACC
SP
SE
PR
F1
IoU
FCM ? M1 ? SUGENO
99.25%
99.35%
95.66%
79.76%
86.99%
76.98%
FCM ? M2 ? SUGENO
99.37%
99.59%
92.25%
87.38%
89.75%
81.40%
FCM ? M3 ? SUGENO
99.36%
99.58%
92.23%
87.15%
89.62%
81.20%
FCM
99.18%
99.23%
96.95%
76.15%
85.30%
74.37%
17068
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 13
scenarios. These improvements underscore the pivotal
impact of GA in the optimization of learning models,
particularly in the context of medical image segmentation,
where precision is paramount.
Incorporating boxplot visualization in Fig. 6 provides a
comprehensive and comparative analysis of the perfor-
mance of various FCM algorithm conﬁgurations, namely
Standard FCM, FCM ? M1 ? Sugeno, FCM ? M2 ?
Sugeno, and FCM ? M3 ? Sugeno, as evidenced by their
F1 scores. This visualization serves as a pivotal element in
our results section, illustrating not only the distribution and
central tendency of the performance metrics for each
conﬁguration but also highlighting potential outliers that
might indicate variability in performance under certain
conditions. One of the most notable observations from this
analysis is the consistently higher F1 scores achieved by
FCM ? M3 ? Sugeno
conﬁguration,
suggesting
its
enhanced capability in handling image segmentation tasks,
particularly in scenarios that may pose speciﬁc challenges.
The
superior
performance
of
FCM ? M3 ? Sugeno
underscores the effectiveness of integrating Sugeno nega-
tion and optimization techniques in reﬁning the segmen-
tation process, offering a promising avenue for future
research and application. Furthermore, the width of the
boxplots and the identiﬁcation of outliers within these
visual representations offer valuable insights into the con-
sistency and reliability of each method across varied
datasets. Narrower boxplots denote a higher level of con-
sistency in the results produced by a method, underscoring
its robustness. Conversely, the presence of outliers may
signal that the method could exhibit unexpected perfor-
mance deviations under certain conditions, warranting
further investigation to understand and mitigate such
occurrences. By providing a clear and intuitive visual
comparison of FCM conﬁgurations, this boxplot visual-
ization signiﬁcantly enriches our manuscript. It not only
facilitates a deeper understanding and assessment of each
conﬁguration’s
performance
but
also
highlights
the
strengths and areas for improvement of our proposed
modiﬁcations to FCM algorithm. This comprehensive
analysis and visualization strategy thus plays a crucial role
in illustrating the potential impact of our work on
advancing the ﬁeld of image segmentation and guiding
future efforts toward the development of more accurate and
adaptable segmentation algorithms.
Furthermore, SE and SP scores highlighted by the
descriptive analysis results present signiﬁcant ﬁndings.
FCM ? M1 ? Sugeno method exhibited remarkable per-
formance with a sensitivity rate of 95.66% and a speciﬁcity
rate
of
99.35%,
while
FCM ? M2 ? Sugeno
and
FCM ? M3 ? Sugeno methods achieved sensitivity rates
of 92.25% and 92.23%, and speciﬁcity rates of 99.59% and
99.58%, respectively. These outcomes demonstrate the
superiority of the proposed methodologies in differentiat-
ing between tumor and non-tumor regions compared to the
traditional FCM algorithm. These descriptive analyses
validate the precision and effectiveness of the proposed
FCM algorithms in solving complex problems like medical
Table 8 Performance metrics
results on
brats18_2013_10_1_ﬂair image
Method
ACC
SP
SE
PR
F1
IoU
FCM ? M1 ? SUGENO
99.70%
99.94%
81.48%
95.35%
87.87%
78.37%
FCM ? M2 ? SUGENO
99.69%
99.90%
83.35%
91.48%
87.23%
77.35%
FCM ? M3 ? SUGENO
99.35%
99.99%
63.69%
99.38%
77.63%
63.43%
FCM
99.70%
99.92%
82.33%
93.80%
87.69%
78.09%
Table 9 Performance metrics
results on
Brats18_2013_7_1_ﬂair image
Method
ACC
SP
SE
PR
F1
IoU
FCM ? M1 ? SUGENO
99.25%
99.21%
99.92%
85.52%
92.16%
85.46%
FCM ? M2 ? SUGENO
99.17%
99.13%
99.96%
84.01%
91.29%
83.98%
FCM ? M3 ? SUGENO
99.58%
99.61%
99.03%
92.93%
95.88%
92.09%
FCM
99.25%
99.21%
99.92%
85.52%
92.16%
85.46%
Table 10 Performance metrics
results on
brats18_2013_9_1_ﬂair image
Method
ACC
SP
SE
PR
F1
IoU
FCM ? M1 ? SUGENO
99.21%
99.47%
83.96%
73.47%
78.36%
64.43%
FCM ? M2 ? SUGENO
99.25%
99.42%
88.11%
70.68%
78.44%
64.53%
FCM ? M3 ? SUGENO
98.86%
99.62%
67.13%
80.84%
73.35%
57.92%
FCM
98.86%
99.62%
67.13%
80.84%
73.35%
57.92%
Neural Computing and Applications (2024) 36:17057–17077
17069
123

---

## Page 14
image segmentation, characterized by uncertainty, noise,
and ambiguity. The evident improvement in the algo-
rithms’ performance is a direct result of the strategic use of
fuzzy set theory and the optimization of parameters
through GA. This work highlights the potential of inte-
grating fuzzy logic and GA to enhance the performance of
machine learning models and establishes a solid foundation
for future research in this ﬁeld.
Fig. 2 Visualization of segmentation results on Brats18_2013_2_1_ﬂair image
17070
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 15
7 Conclusion and discussion
This study represents a signiﬁcant leap forward in the
application of fuzzy logic within the realm of machine
learning, particularly in the segmentation of brain MRI
images. By integrating fuzzy set theory, fuzzy metrics, and
the Sugeno negation operator into FCM algorithm and
optimizing it through GA, we have unveiled a methodology
that not only transcends traditional machine learning con-
straints but also exhibits unparalleled adaptability and
Fig. 3 Visualization of segmentation results on Brats18_2013_10_1_ﬂair image
Neural Computing and Applications (2024) 36:17057–17077
17071
123

---

## Page 16
precision in the face of data ambiguity, noise, and impre-
cision. Our research stands at the forefront of innovation in
machine learning and image segmentation through its
comprehensive and multifaceted contributions, which are
elaborated as follows:
•
Revitalized FCM algorithm: We have not merely
adjusted but fundamentally transformed FCM algo-
rithm. This transformation involves a pioneering inte-
gration of fuzzy set theory, fuzzy metrics, and the
Sugeno negation operator. By doing so, our approach
bridges
the
gap
between
traditional
segmentation
methods and the need for more adaptive, nuanced
Fig. 4 Visualization of segmentation results on Brats18_2013_7_1_ﬂair image
17072
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 17
solutions in the face of data that is inherently ambigu-
ous, noisy, and imprecise. This represents a paradigm
shift in how algorithms adapt to and interpret complex
datasets.
•
Advanced clustering mechanism through fuzzy logic:
Our study elevates the clustering mechanism by lever-
aging the nuanced capabilities of fuzzy logic. The
introduction of fuzzy metrics to assess proximity and
the innovative use of the Sugeno negation operator to
interpret these metrics as distances offer a more
sophisticated, ﬂexible clustering process. This approach
allows for a dynamic adjustment to the inherent
vagueness and overlaps found in real-world data,
Fig. 5 Visualization of segmentation results on brats18_2013_9_1_ﬂair image
Neural Computing and Applications (2024) 36:17057–17077
17073
123

---

## Page 18
particularly in medical imaging, where such character-
istics are prevalent.
•
Optimization with GA: The strategic use of GA to
optimize the parameters of the fuzzy metric and
negation operators marks a signiﬁcant advancement.
This optimization ensures that the algorithm not only
performs with maximal efﬁciency but also retains its
adaptability across different datasets and segmentation
challenges. It highlights our contribution in applying
evolutionary computation techniques to ﬁne-tune the
algorithm, enhancing its sensitivity and speciﬁcity in
segmenting MRI images.
•
Superior performance in MRI image segmentation: A
key contribution of our research is the demonstrated
superior performance of the modiﬁed FCM algorithm in
the segmentation of brain MRI images. Through
rigorous experimentation and comparison with tradi-
tional methods, our approach has shown signiﬁcant
improvements in accuracy, precision, recall, and overall
segmentation quality. This success underscores the
potential of our methodology to improve diagnostic
processes by providing more reliable and detailed
image analyses.
•
Framework for future research in fuzzy-based machine
learning: Beyond its immediate applications, our study
provides a robust framework for future research into
fuzzy-based machine learning models. By showcasing
the
effectiveness
of
integrating
fuzzy logic with
GAoptimization, we pave the way for further explo-
rations into other complex data analysis tasks beyond
MRI segmentation. Our research invites the academic
community to build upon our ﬁndings, explore new
applications, and continue advancing the boundaries of
what machine learning algorithms can achieve.
•
Advantages and limitations: The advantages of our
approach include increased sensitivity to the nuances of
data, resulting in higher accuracy and precision in
segmentation tasks. Moreover, the adaptability of the
algorithm allows for its application across various
complex datasets, showcasing its robustness. However,
a notable limitation is the increased computational
demand, primarily due to the GA’s optimization
process. This aspect could potentially hinder the
algorithm’s applicability in real-time scenarios or when
dealing with extensive datasets.
In conclusion, by ingeniously amalgamating fuzzy set
theory, fuzzy metrics, and the Sugeno negation operator
with GA, our study carves a novel pathway for the
enhancement of machine learning algorithms for complex
data segmentation tasks. The proposed methodology not
only redeﬁnes FCM algorithm within an advanced fuzzy
logic framework but also paves the way for future research,
promising substantial advancements in the machine learn-
ing and data analysis domains.
8 Future works
Future research should focus on developing methods that
reduce computational demands and enhance the general-
izability of the algorithm. This would enable broader
applications across larger datasets and more complex
Fig. 6 F1 scores comparison of
FCM conﬁgurations
17074
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 19
problem domains. Looking ahead, several avenues for
further research emerge:
•
Algorithm efﬁciency: exploring techniques to reduce
computational demands, such as parallel processing or
more efﬁcient optimization algorithms, will be crucial.
This could widen the algorithm’s applicability, making
it feasible for larger datasets and real-time analysis.
•
Broader
applications:
extending
the
use
of
our
enhanced FCM algorithm beyond MRI image segmen-
tation to other domains, such as natural language
processing
or
environmental
monitoring,
carotid
atherosclerotic plaque etc. [52, 53] could prove bene-
ﬁcial. This would test the algorithm’s versatility and
adaptability to various data types.
•
Development of fuzzy metrics: crafting new fuzzy
metrics tailored to speciﬁc segmentation challenges
could further reﬁne the algorithm, enhancing its preci-
sion and ﬂexibility. This bespoke approach would allow
for nuanced segmentation tasks to be conducted with
even greater accuracy.
Author contributions Fatih Kutlu: conceptualization; formal analysis;
methodology; resources; software; supervision; writing—original
draft; writing—review and editing. I˙brahim Ayaz: data curation;
methodology; resources; software; validation; visualization; writing-
original draft; writing-review and editing. Harish Garg: conceptual-
ization; formal analysis; methodology; resources; software; supervi-
sion; writing—original draft; writing—review and editing.
Funding Open access funding provided by the Scientiﬁc and Tech-
nological Research Council of Tu¨rkiye (TU¨ BI˙TAK). There is no
funding provider.
Data availability statement The dataset utilized in this study is
sourced from BraTS2018, facilitated by the Section for Biomedical
Image Analysis (SBIA) of the University of Pennsylvania. This
dataset is publicly accessible at https://www.med.upenn.edu/sbia/
brats2018/data.html. All the data used in our research is duly cited in
the relevant sections of this document. The usage of this dataset
includes detailed information and guidelines for other researchers in
this ﬁeld, and our study has been conducted in accordance with these
directives.
Declarations
Conflict of interest The authors declare no competing interests.
Ethics approval I hereby declare that this study has been scrutinized
and approved from an ethical standpoint. Throughout the research
process, no ethical issues or conflicts have arisen. Furthermore, dur-
ing the literature review, data collection, and analysis stages, com-
plete adherence to principles of impartiality and accuracy has been
maintained. All data has been obtained reliably and reported accu-
rately. This statement is presented to confirm the full compliance of
the research process with ethical standards. The usage rules of the
open-access data set used in the study were followed.
Consent to participate Informed consent was waived by ethics
groups.
Consent for publication Informed consent was waived by ethics
groups.
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
1. Zadeh LA (1965) Fuzzy sets. Inf Control 8:338–353. https://doi.
org/10.1016/S0019-9958(65)90241-X
2. Couso I, Borgelt C, Hullermeier E, Kruse R (2019) Fuzzy sets in
data analysis: From statistical foundations to machine learning.
IEEE Comput Intell Mag 14:31–44. https://doi.org/10.1109/MCI.
2018.2881642
3. Dunn JC (1973) A fuzzy relative of the ISODATA process and its
use in detecting compact well-separated clusters. J Cybernet
3:32–57. https://doi.org/10.1080/01969727308546046
4. Bezdek JC, Ehrlich R, Full W (1984) FCM: the fuzzy c-means
clustering algorithm. Comput Geosci 10:191–203. https://doi.org/
10.1016/0098-3004(84)90020-7
5. Ghosh S, Kumar S (2013) Comparative analysis of K-means and
fuzzy C-means algorithms. Int J Adv Comput Sci Appl https://
doi.org/10.14569/ijacsa.2013.040406
6. Gao Y, Wang S, Liu S (2009) Automatic clustering based on GA-
FCM for pattern recognition. In: ISCID 2009 - 2009 international
symposium
on
computational
intelligence
and
design.
pp 146–149
7. Tang Y, Ren F, Pedrycz W (2020) Fuzzy C-means clustering
through SSIM and patch for image segmentation. Appl Soft
Comput
87:105928.
https://doi.org/10.1016/J.ASOC.2019.
105928
8. O¨ zyurt F, Sert E, Avcı D (2020) An expert system for brain tumor
detection: Fuzzy C-means with super resolution and convolu-
tional neural network with extreme learning machine. Med
Hypotheses 134:109433. https://doi.org/10.1016/J.MEHY.2019.
109433
9. Cheng-Bing L, Xi-hao M (2021) Array sensors online pattern
recognition based on FCM and ANFIS. Int J Comput Appl
43:352–359. https://doi.org/10.1080/1206212X.2018.1550167
10. Hua L, Gu Y, Gu X et al (2021) A novel brain MRI image
segmentation method using an improved multi-view fuzzy
c-means clustering algorithm. Front Neurosci. https://doi.org/10.
3389/fnins.2021.662674
11. Tongbram S, Shimray BA, Singh LS, Dhanachandra N (2021) A
novel image segmentation approach using fcm and whale opti-
mization algorithm. J Ambient Intell Humaniz Comput 1:1–15.
https://doi.org/10.1007/S12652-020-02762-W/TABLES/11
12. Shi Z, Wu D, Guo C et al (2021) FCM-RDpA: TSK fuzzy
regression model construction using fuzzy C-means clustering,
Neural Computing and Applications (2024) 36:17057–17077
17075
123

---

## Page 20
regularization, Droprule, and Powerball Adabelief. Inf Sci (N Y)
574:490–504. https://doi.org/10.1016/j.ins.2021.05.084
13. Ayyappa Y, Neelakanteswara P, Bekkanti A, et al (2021) auto-
matic face mask recognition system with FCM and BPNN. In:
Proceedings
-
5th
international
conference
on
computing
methodologies and communication, ICCMC 2021. Institute of
Electrical and Electronics Engineers Inc., pp 1134–1137
14. Zhang X, Ning Y, Li X, Zhang C (2021) Anti-noise FCM image
segmentation method based on quadratic polynomial. Signal
Process
178:107767.
https://doi.org/10.1016/j.sigpro.2020.
107767
15. MurﬁH, Rosaline N, Hariadi N (2022) Deep autoencoder-based
fuzzy c-means for topic detection. Array 13:100124. https://doi.
org/10.1016/J.ARRAY.2021.100124
16. Meng F (2021) Safety warning model of coal face based on fcm
fuzzy clustering and ga-bp neural network. Symmetry (Basel).
https://doi.org/10.3390/sym13061082
17. Karczmarek P, Kiersztyn A, Pedrycz W, Czerwin´ski D (2021)
Fuzzy C-Means-based Isolation Forest. Appl Soft Comput
106:107354. https://doi.org/10.1016/J.ASOC.2021.107354
18. Yu JW, Kim JS, Li X et al (2022) Water quality forecasting based
on data decomposition, fuzzy clustering and deep learning neural
network. Environ Pollut 303:119136. https://doi.org/10.1016/J.
ENVPOL.2022.119136
19. Gosain A, Dahiya S (2016) Performance analysis of various fuzzy
clustering
algorithms:
a
review.
Procedia
Comput
Sci
79:100–111. https://doi.org/10.1016/J.PROCS.2016.03.014
20. Ruspini EH, Bezdek JC, Keller JM (2019) Fuzzy clustering: a
historical perspective. IEEE Comput Intell Mag 14:45–55. https://
doi.org/10.1109/MCI.2018.2881643
21. Kramosil I, Michalek J (1975) Fuzzy metrics and statistical
metric spaces. Kybernetika 11:336–344
22. George A, Veeramani P (1994) On some results in fuzzy metric
spaces. Fuzzy Sets Syst 64:395–399. https://doi.org/10.1016/
0165-0114(94)90162-7
23. George A, Veeramani P (1997) Short communication: on some
results of analysis for fuzzy metric spaces. Fuzzy Sets Syst
90:349–353
24. Park JH (2004) Intuitionistic fuzzy metric spaces. Chaos Solitons
Fractals 22:1039–1046. https://doi.org/10.1016/j.chaos.2004.02.
051
25. Gregori V, Morillas S, Sapena A (2011) Examples of fuzzy
metrics and applications. Fuzzy Sets Syst 170:95–111. https://doi.
org/10.1016/j.fss.2010.10.019
26. Kutlu F, Tuncdemir K (2021) Temporal intuitionistic fuzzy
metric spaces. Maejo Int J Sci Technol 15:209–221
27. Ralevic´ NM, Karaklic´ D, Pisˇtinjat N (2019) Fuzzy metric and its
applications
in
removing
the
image
noise.
Soft
comput
23:12049–12061.
https://doi.org/10.1007/S00500-019-03762-5/
METRICS
28. Ralevic´ N, Paunovic´ M (2021) Applications of the fuzzy metrics
in
image
denoising
and
segmentation.
Tehnicˇki
Vjesnik
28:819–826
29. Ralevic NMR, Delicdelic M, Nedovic LN (2022) Aggregation of
fuzzy metrics and its application in image segmentation. Iran J
Fuzzy Syst 19:19–37
30. Pham DL, Prince JL (1999) Adaptive fuzzy segmentation of
magnetic
resonance
images.
IEEE
Trans
Med
Imaging
18:737–752. https://doi.org/10.1109/42.802752
31. Siyal MY, Yu L (2005) An intelligent modiﬁed fuzzy c-means
based algorithm for bias estimation and segmentation of brain
MRI. Pattern Recognit Lett 26:2052–2062. https://doi.org/10.
1016/J.PATREC.2005.03.019
32. Singh C, Bala A (2018) A DCT-based local and non-local fuzzy
C-means algorithm for segmentation of brain magnetic resonance
images. Appl Soft Comput 68:447–457. https://doi.org/10.1016/J.
ASOC.2018.03.054
33. Bai X, Zhang Y, Liu H, Chen Z (2019) Similarity measure-based
possibilistic FCM with label information for brain MRI seg-
mentation. IEEE Trans Cybern 49:2618–2630. https://doi.org/10.
1109/TCYB.2018.2830977
34. Huang H, Meng F, Zhou S et al (2019) Brain image segmentation
based on FCM clustering algorithm and rough set. IEEE Access
7:12386–12396. https://doi.org/10.1109/ACCESS.2019.2893063
35. Liu Z, Bai X, Liu H, Zhang Y (2020) Multiple-surface-approxi-
mation-based FCM with interval memberships for bias correction
and segmentation of brain MRI. IEEE Trans Fuzzy Syst
28:2093–2106. https://doi.org/10.1109/TFUZZ.2019.2930478
36. Valsalan P, Sriramakrishnan P, Sridhar S et al (2020) Knowledge
based fuzzy c-means method for rapid brain tissues segmentation
of magnetic resonance imaging scans with CUDA enabled GPU
machine. J Ambient Intell Humaniz Comput. https://doi.org/10.
1007/S12652-020-02132-6/METRICS
37. Tavakoli-Zaniani M, Sedighi-Maman Z, Fazel Zarandi MH
(2021) Segmentation of white matter, grey matter and cere-
brospinal ﬂuid from brain MR images using a modiﬁed FCM
based on double estimation. Biomed Signal Process Control
68:102615. https://doi.org/10.1016/J.BSPC.2021.102615
38. Neves-Jr F, Arruda LVR, Mendonc¸a M (2009) A combined
FCM-GA approach to supervise industrial process. IFAC Proc
Vol 42:1144–1149. https://doi.org/10.3182/20090630-4-ES-2003.
00188
39. Chen T-C, You P-S, Wu C-H, Lin S-L (2014) Using FCM based
hybrid computational approach for diseases diagnosis in tradi-
tional chinese medicine. Int J Mach Learn Comput 4:389–393.
https://doi.org/10.7763/IJMLC.2014.V4.442
40. Ghazanfari M, Alizadeh S, Fathian M, Koulouriotis DE (2007)
Comparing simulated annealing and genetic algorithm in learning
FCM. Appl Math Comput 192:56–68. https://doi.org/10.1016/J.
AMC.2007.02.144
41. Wang LW, Zhu YQ, Pan YF (2005) FCM algorithm and index
CS for the signal sorting of radiant points. In: 2005 international
conference on machine learning and cybernetics, ICMLC 2005,
pp 4415–4419. https://doi.org/10.1109/ICMLC.2005.1527716
42. Bede B (2013) Mathematics of fuzzy sets and fuzzy logic.
Springer, Berlin
43. Holland JH (1992) Genetic algorithms. Sci Am 267:66–73
44. Li S, Li D (2021) Genetic algorithms. In: Springer Series in
Materials Science. pp 115–131
45. Katoch S, Chauhan SS, Kumar V (2021) A review on genetic
algorithm: past, present, and future. Multimed Tools Appl
80:8091–8126. https://doi.org/10.1007/s11042-020-10139-6
46. Zeebaree DQ, Haron H, Abdulazeez AM, Zeebaree SRM (2017)
Combination of k-means clustering with genetic algorithm: a
review. Int J Appl Eng Res 12:14238–14245
47. Ding Y, Fu X (2016) Kernel-based fuzzy c-means clustering
algorithm
based
on
genetic
algorithm.
Neurocomputing
188:233–238. https://doi.org/10.1016/j.neucom.2015.01.106
48. Li H, Wang F, Li H (2019) Integrating expert knowledge for
Bayesian network structure learning based on intuitionistic fuzzy
set and genetic algorithm. Intell Data Anal 23:41–56. https://doi.
org/10.3233/IDA-183877
49. Bakas S, Reyes M, Jakab A, et al (2018) Identifying the best
machine learning algorithms for brain tumor segmentation, pro-
gression assessment, and overall survival prediction in the
BRATS challenge. Sandra Gonzlez-Vill 124:
50. Menze BH, Jakab A, Bauer S et al (2015) The multimodal brain
tumor image segmentation benchmark (BRATS). IEEE Trans
Med Imaging 34:1993–2024. https://doi.org/10.1109/TMI.2014.
2377694
17076
Neural Computing and Applications (2024) 36:17057–17077
123

---

## Page 21
51. Bakas S, Akbari H, Sotiras A et al (2017) Advancing The Cancer
Genome Atlas glioma MRI collections with expert segmentation
labels and radiomic features. Sci Data. https://doi.org/10.1038/
SDATA.2017.117
52. Huo R, Liu Y, Xu H, Li J, Xin R, Xing Z, Deng S, Wang T, Yuan
H, Zhao X (2022) Associations between carotid atherosclerotic
plaque characteristics determined by magnetic resonance imaging
and improvement of cognition in patients undergoing carotid
endarterectomy. Quant Imaging Med Surg 12(5):2891–2903
53. Han M, He W, He Z, Yan X, Fang X (2022) Anatomical char-
acteristics affecting the surgical approach of oblique lateral
lumbar interbody fusion: an MR-based observational study.
J Orthop Surg Res 17(1):426. https://doi.org/10.1186/s13018-
022-03322-y
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
Neural Computing and Applications (2024) 36:17057–17077
17077

---
