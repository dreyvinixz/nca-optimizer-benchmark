# A simple contrastive embedding framework for low-resource fake news detection

**Year**: 2025 | **Journal**: Neural Computing and Applications (NCA, Journal 521)
**DOI**: https://doi.org/10.1007/s00521-025-11467-0

---

## Page 1
ORIGINAL ARTICLE
A simple contrastive embedding framework for low-
resource fake news detection
Iftitahu Ni’mah1,2
• Rini Wijayanti1 • Agung Santosa1 • Asril Jarin1 • Tri Sampurno1 •
Mohammad Teduh Uliniansyah1 • Meng Fang3 • Vlado Menkovski2
•
Mykola Pechenizkiy2
Received: 2 June 2024 / Accepted: 3 July 2025 / Published online: 5 August 2025
 The Author(s) 2025
Abstract
Low-resource fake news detection aims at discerning between true and false claims from low-resource languages
with scarce benchmark datasets. In this resource-constrained scenario, fake news data collected from online hoax
reporting system is inherently skewed because human fact checkers mainly sample claims that are more likely to
be fake or false. Instead of training end-to-end classiﬁer on the extremely imbalanced dataset, our study inves-
tigates a simple framework based on contrastive learning and stacking-based ensemble learning as an alternate
fake news classiﬁcation pipeline for Indonesian language. Our empirical result shows that by combining con-
trastive-based embedding model—Contrast-BERT and ensemble of multilayer perceptrons (MLPs) in inference
stage, we improve the precision score in fake news classiﬁcation up to 26.64%, while maintaining accuracy and
recall scores of above 75%, given extreme class imbalance ratio 1:24. Contrast-BERT is also superior to its
counterparts in unsupervised topic clustering and evidence retrieval by nearly twofold. Furthermore, we observe
that contrastive-based model follows a similar performance trend in Indonesian clickbait benchmark dataset.
Contrast-BERT is more accurate and precise at predicting samples than end-to-end BERT classiﬁer by up to 47%,
given training subset with extreme imbalance ratio  1:19.
Keywords Fake news detection  Low-resource scenario  Contrastive learning  BERT embeddings 
Extreme class imbalance
1 Introduction
Fake news detection is a natural language processing (NLP) task that aims to discern between legitimate and
fabricated information within textual content, such as news articles or other types of text distributed via social
media platforms. If real news refers to an accountable bit of information or a real event, fake news is a counterfeit
that is typically operationalized based on its level of facticity and the author’s immediate intention, such as:
fabrication, propaganda, manipulation, satire, and parody [1]. Fake news creates global and national issues, not
only because it circulates the discourse that confuses the readers [2], but also because polarized information can
highly affect election results [3] and political tensions in a country [2, 4]. News is socially constructed, making it
easy for news creators to use fabricated news as propaganda or an advertisement for polarized readers. In
addition, for people without digital literacy and fact-checking ability, fake news can resemble the look and feel of
real news, and vice versa, worsening the dissemination of misinformation and disinformation on social media
platforms. Therefore, the ability of machine learning algorithms or NLP methods to automatically identify and
Neural Computing and Applications (2025) 37:21407–21433
https://doi.org/10.1007/s00521-025-11467-0
123
Neural Computing and Applications (2025) 37:21407–21433

---

## Page 2
ﬂag texts as real or fake regardless of whether both categories share similar tone, sentiment, or emotion is crucial
to control the spread of misinformation and disinformation and promote the dissemination of factual information
instead.
However, obtaining large, accurately labeled data for training fake news detection models is costly and
challenging. The reason is that high-quality labels are obtained based on the judgment of human experts to fact
check claims or news articles with multiple external sources as references before deciding a verdict [5]. Gen-
eralizing the problem to an unseen target domain beyond English thus introduces language-speciﬁc challenges,
particularly for training fake news detection models in a resource-scarce scenario [6]. In addition to the scarcity of
linguistic resources and limited labeled data, the detection of fake news for low-resource language is challenging
because there exist different cultural and linguistic nuances between English and non-English languages [7, 8];
domain speciﬁcity problem [9]; and inherited errors in translation-based augmentation approaches for low-
resource language [10–12].
Although there has been increasing attention to developing methods for detecting fake news beyond English,
such as for Arabic [13–15], Romanian [16], Malay [17], Hindi [18, 19], and Indonesian language [20], previous
works have not addressed the problem in a realistic scenario of fake news detection with extreme class imbalance.
In a realistic scenario, most of the real-world data for training fake news detection models comes from online
public reports and government fact-checking initiatives, such as Masyarakat Anti Fitnah Indonesia (Maﬁndo)
[21], which are mainly composed of false claims or fake news. In such a fact-checking platform, users submit
claims and news articles that are more likely to be hoax or fake, resulting in data with an extremely imbalanced
class representation where hoax becomes the majority class. Training machine learning models on such extremely
imbalanced data can result in severe performance degradation, particularly on unseen data, where the distribution
is different with the data on which the models are trained.
Our study aims at accurately discerning between true and false claims given extremely imbalanced real-world
fake news data from Indonesian hoax reporting system. In particular, we want to approach the binary classiﬁ-
cation problem through the lens of contextual embeddings, moving beyond a standard end-to-end classiﬁer. We
hypothesize that by recasting the end-to-end fake news classiﬁcation task into the objective of contrastive learning
[22, 23], our approach allows learning data representation nearly unsupervisedly, thus mitigating bias or over-
ﬁtting issues due to extremely imbalanced training samples. Contrastive learning uses a semantic paradigm in
which explicit label supervision is substituted for semantic descriptors, such as positive and negative sentence
pairs. In this study, positive and negative semantic descriptors are speciﬁcally described based on a collection of
sentence pairs from Hoax and Non-Hoax class categories. Then, the model is enforced to recognize similar and
dissimilar samples, given positive and negative data pairs. In inference, the trained contrastive model is mainly
used as an embedding model for unseen evaluation data. The resulting text embeddings are then used as:
(i) features for off-the-shelf MLP classiﬁers in a fake news classiﬁcation pipeline; and (ii) features for clustering
and retrieval evaluation tasks.
This paper ﬁrst discusses two main categories of automated fake news detection approaches: (i) content-based;
and (ii) context-based; and how they are adopted to languages beyond English (Section 2.1). In particular, we
highlight the challenges for processing imbalanced fake news data in Indonesian, Bangla, and Czech; and how
our data differ from currently available fake news and fact-checking datasets, as shown in Table 1 (Section 2.2).
We also brieﬂy discuss the comparison of methods for automated fake news detection, as shown in Table 2
(Section 2.3). Section 3 delves into research questions that guide the empirical experiments in this study. Sec-
tion 4 explains the experimental setup and the resources used in this study. Finally, section 5 presents our
empirical ﬁndings based on the performance measure in classiﬁcation task and clustering; error analysis; and the
ablation study on domain transfer, representation bias, and imbalance ratio. Our empirical experiments yield the
following key insights:
•
Contrastive learning captures ﬁne-grained topics in fake news data as training signals.
Models based on contrastive learning—Contrast-BERT are observed to be more expressive than non-
123
Neural Computing and Applications (2025) 37:21407–21433
21408
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 3
contrastive baselines, particularly for capturing ﬁne-grained topics inferred in training data, as shown in
Tables 7 and 8. This capability is also transferable to new unseen domain within the same language category.
•
Contrastive learning encourages fair representations, particularly toward implicit tone in fake news data.
We observe that Contrast-BERT is less biased than E2E BERT classiﬁer when predicting Hoax samples
under neutral and sensational tone categories as protected or sensitive attributes, as shown in Table 9.
Our contributions can be summarized as follows:
•
We present a simple framework based on contrastive learning and stacking-based ensemble learning for low-
resource fake news detection.
We demonstrate that Contrast-BERT consistently has higher precision scores than E2E BERT classiﬁer in
low-resource fake news classiﬁcation task with an extreme class imbalance issue; particularly for Indonesian,
Bangla, and Czech language.
•
We are the ﬁrst to provide comprehensive training and evaluation checklist (Section 3) for low-resource fake
news detection through the lens of contrastive learning, moving beyond a standard end-to-end (E2E)
classiﬁcation objective.
Table 1 Comparison of currently available fake news and fact-checking datasets
Dataset
Natural
Domain
Language
#Claim
Low
resource
Imbalance ratio
Evidence
Extreme
imbalance
Ratio
(%)
Fake/
Real
Source
Retrieved
Annotated
English datasets
FEVER [39]
7
Multiple
English
109810
7
7
27:73
Wiki
U
U
Liar [40]
U
Multiple
English
10269
7
7
64:46
Fact-
checking
7
7
Snopes [41]
U
Multiple
English
4236
7
7
73:27
Fact-
checking
7
7
CHEF [42]
U
Multiple
Chinese
7226
7
7
60:40
Internet
U
U
Low-resource fake news data
Tallip-ID [6]
7
Multiple
Indonesian
1960
U
7
50:50
7
7
7
Clickbait-ID [43]
U
7
Indonesian
14928
U
7
42:58
7
7
7
BanFakeNews
[44]
U
Multiple
Bangla,
Bangladesh
50074
U
U
2:98
7
7
7
CsFEVER [45]
7
7
Czech
124672
U
7
27:73
Fact-
checking
U
U
CsFEVER-NLI
[45]
7
7
Czech
218385
U
7
29:71
Fact-
checking
U
U
IndoHoax (Ours)
U
Multiple
Indonesian
12532
U
U
96:4
Fact-
checking
U
U
English datasets are not covered in this study.Number of claims (#Claim) is based on training set, except for Tallip-ID where we view data as target
test set only
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21409

---

## Page 4
2 Related work
2.1 Fake news detection in low-resource language
Automated fake news detection in low-resource language, which aims to identify fake news beyond the English
language [15–18, 20], is a nontrivial problem due to the nature of the task that is mainly restricted by limited
high-quality data and linguistic resources [6]. Previous studies have shown that data synthesizing by translation
methods often produces low-quality data because there are cultural gaps and different linguistic nuances between
English and non-English languages [7, 8]; and translation-based augmentation errors [12]. When a machine
learning model is trained on these low-quality data, the performance of the model is expected to deteriorate [10].
Table 2 Comparison of currently available methods for automatic content-based fake news detection. We view OpenAI
large language model (LLM) as a black-box method; thus, the only representation can be accessed is ‘‘Natural’’ repre-
sentation of inputs and outputs
Method
#Params
Input feature
Representation
Contrastive
learning
Backbone
Supervision
Research challenge
Claim
Evidence
Embedding
Natural
Low
resource
Extreme
imbalance
Word
Doc.
Graph
Evidence-aware
MAC
9.0M
U
U
U
U
7
7
7
BiDAF/
LSTM
supervised
7
7
GET
9.4M
U
U
U
U
U
7
7
GNN
supervised
7
7
GETRAL
9.4M
U
U
U
U
U
7
U
GNN
supervised
7
7
ReRead
249.5M
U
U
7
U
7
7
7
BERT
supervised
7
7
OpenAI LLM
GPT3.5
’ 175B
- Claim-only
U
7
7
7
7
U
7
LLM
unsupervised
7
7
- With
evidence
U
U
7
7
7
U
7
LLM
unsupervised
7
7
GPT-4
’ 1:8T
- Claim-only
U
7
7
7
7
U
7
LLM
unsupervised
7
7
- With
evidence
U
U
7
7
7
U
7
LLM
unsupervised
7
7
E2E BERT Classiﬁer
BERT
109.5M
U
U
7
U
7
7
7
BERT
supervised
7
7
BERTðensembleÞ
109.5M
U
U
7
U
7
7
7
BERT
supervised
7
7
BERT Embeddings
No-Fine-
tuning
109.5M
U
U
7
U
7
7
7
BERT
unsupervised
7
7
MLM Tuning
109.5M
U
U
7
U
7
7
7
BERT
unsupervised
7
7
Classif.
Tuning
109.5M
U
U
7
U
7
7
7
BERT
supervised
7
7
Contrast-BERT (Ours)
Pairwise
109.5M
U
U
7
U
7
7
U
BERT
semi-
supervised
U
U
Triplet
109.5M
U
U
7
U
7
7
U
BERT
semi-
supervised
U
U
Unsupervised
109.5M
U
U
7
U
7
7
U
BERT
unsupervised
U
U
123
Neural Computing and Applications (2025) 37:21407–21433
21410
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 5
In Indonesia, automated fake news detection research can be broadly divided into (i) content-based approa-
ches—that mainly depends on linguistic features and dataset speciﬁcity; and (ii) context-based approaches, which
consider multiple contextual information such as source credibility, temporal information, social engagement,
network analysis, and multimodal analysis. Previous studies on content-based fake news detection use traditional
machine learning methods such as Naı¨ve Bayes [24] and XGBoost [25]; or BERT pretrained models [26] as end-
to-end fake news classiﬁer. However, none of these works have addressed problems in a realistic scenario of fake
news detection with extreme class imbalance. Previous studies on the content-based classiﬁcation of real and fake
news also explore the role of subjective sentiment or tone in news data [27–31]. However, in a real-world fake
news classiﬁcation task, non-neutral or sensational tone can be found in both true and false claims. A shared-
stylistic aspect across label categories introduces a new challenge to the content-based and sentiment-guided
classiﬁers. On the other hand, to build an integrated fact-checking and fake news detection framework, context-
based approaches [32–36] typically require high-quality social media data and relevant external knowledge,
which are often inaccessible. It is also difﬁcult to adopt context-based approaches in a new use case or new
domain because the characteristics of data and experimental ﬂows are speciﬁc to the authors’ own domain
[33, 37, 38].
In this study, we further investigate whether currently available automatic fake news detection methods are
able to address challenges in low-resource fake news detection task for Indonesian, Bangla [44], and Czech [45]
language. Table 1 shows the low-resource fake news datasets in this study and how they differ from English
datasets. Among low-resource fake news datasets, our Indonesian dataset is the only one with characteristics:
(i) ‘‘natural’’—data is not synthetically generated based on automatic machine translation methods, it is based on
real-world claim report; (ii) ‘‘extremely imbalanced; and (iii) contains retrieved evidences. BanFakeNews [44]
has the closest characteristics to our data, particularly for containing an extreme class imbalance. However, the
majority of samples in BanFakeNews come from authentic news sources (98%), compared to our data that are
composed of 96% false claims; BanFakeNews also does not contain evidence to fact check the claims.
2.2 Class imbalance
The class imbalance problem, a condition in which one particular class signiﬁcantly outweighs the other class, is a
common challenge in real-world fake news detection. When a classiﬁer or a model based on supervised learning
is trained on this representation of bias, the model can carry and transfer such bias in unseen target data and the
fake news domain [33, 46], introducing higher false positives where samples from the minority class (real news)
are voted as fake news. To address class imbalance in fake news detection, researchers have proposed various
methods that we broadly divided into two: (i) single-stage training; and (ii) dual-stage training. A single-stage
training method focuses on improving model training from the news data have asymmetric to better sample data
during the training stage. For example, latent space resampling [46] resamples class-biased latent vectors via
oversampling, undersampling, and hybrid-sampling techniques. Methods based on ensemble learning [47–49] use
multiple weak classiﬁers as independent experts, rather than relying solely on a biased classiﬁer. Loss re-
weighting [50] aims at increasing the inﬂuence of samples from the minority class category during the training
stage. A dual-stage training method [51, 52], on the other hand, focuses on designing pretext tasks, such as
predicting masked words [53] and contrasting samples [23] to generate training signals, instead of relying on
explicit label supervision. The trained model is then used mainly as an encoder to project natural texts into
multidimensional embedding space. In this study, we focus on a dual-stage training approach. We highlight the
differences between our proposed approach and currently available baselines as shown in Table 2.
2.3 Contrastive learning
The core idea of contrastive learning [54–56] is to contrast between similar and dissimilar pairwise data points. In
a generalizable deﬁnition of what is considered ‘‘similar’’ [57], a pair of data points is called a positive pair if both
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21411

---

## Page 6
points are different representations or views of the same data instance. Data points can be input-input ðxi; xjÞ or
input-label ðxi; yjÞ. For example, contrastive learning approaches in computer vision [22, 58, 59], learn from
input-input pairs, i.e., image-to-image as pairwise data. In this setup, a positive pair is deﬁned by multiple parallel
augmentation of image input prior to training, such as by image rotation, random color cropping, random color
distortions, and random Gaussian blur. However, contrastive learning in NLP, such as SimCSE [23], deﬁnes a
positive pair as a pair of input and its contextual output representation (input–output) ðxi; ycÞ. In this setup, xi is
text input and yc is a variation view of the said text. For example, xi can be a text, yc can be a summarized version
of xi [60–62]. A positive pair can also be deﬁned as a pair of premises and its entailment hypothesis, such as
contrastive learning based on Natural Language Inference (NLI) data [23].
Contrastive learning beneﬁts our current study on fake news detection in low-resource language because it
allows the model to learn representations in a self-supervised manner by comparing pairwise data, eliminating the
requirement for learning from explicit label supervision. In our particular fake news domain where labeled data is
scarce or costly to acquire, this training concept is a useful alternate objective as compared to directly learning
from extremely imbalanced class representation that can may bring negative impact on unseen target domain or
test data. Moreover, many previous empirical studies [63–67] demonstrate the ability of contrastive learning-
based embedding models to produce robust representations in classiﬁcation tasks, including the detection of fake
news [51, 68–70].
Fig. 1 Overview of our contrastive embedding framework for low-resource fake news detection. a Data preparation and
training stage for contrastive-based BERT (Contrast-BERT). b Inference stage where Contrast-BERT is used as embedding
model to project text into embedding or vector representation for ensemble MLP classiﬁers.
123
Neural Computing and Applications (2025) 37:21407–21433
21412
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 7
3 Methodology
Figure 1 illustrates an overview of our contrastive embedding framework for low-resource fake news detection.
We collect data from hoax reporting systems (Table 4) where claims are mainly sampled from hoax candidates as
the majority class, resulting in data with a severe class imbalance ratio of 1:24. Given {Claim (Title),
Context (Article), Fact, Label}, we further preprocess the data to create positive and negative sentence
pairs from both Hoax (false claim) and Non-Hoax (true claim) as input features for a contrastive objective
(Section 3.1). In the data preprocessing stage, we incorporate ﬁltering methods to exclude noisy sentence pairs
(Section 3.2). Our fake news classiﬁcation pipeline is described as sequential processes in the inference stage
(Fig. 1b) where the trained contrastive-based model—Contrast-BERT is used as an embedding model to project
text samples as vector representation as input features for independent MLP classiﬁers. Then, ensemble learning
is described as training multiple MLPs in parallel as weak classiﬁers for smaller subsets with balanced class
representation (Section 3.3). As a checklist for ablation studies and empirical evaluation, we outline our learning
framework with the corresponding research questions as follows:
3.1 Contrastive objective
RQ1: How to recast a fake news detection into a contrastive learning objective?
A contrastive learning framework can be broadly divided based on its learning objective: (i) Unsupervised—
where the model is trained on a collection of unlabeled sentences in a corpus; (ii) weakly supervised learning
based on positive pairs—where positive pairs are explicitly deﬁned to learn representations from ‘‘similar’’
samples as opposed to in-batch negative samples; (iii) supervised learning based on triplet data—where similar
and dissimilar input features are explicitly deﬁned as positive pairs and hard negatives respectively.
We adopt SimCSE contrastive learning framework [23] that originates from SimCLR [22], which approxi-
mates InfoNCE contrastive loss as a cross-entropy objective with in-batch negatives [71, 72]. If Hard Negative
pair ðx; xÞ is not explicitly deﬁned, the negative samples are deﬁned from in-batch training examples. If Positive
Pair ðx; xþÞ is undeﬁned, the positive sentence xþ is deﬁned based on implicit BERT augmentation of individual
sentence. Contrastive learning objective with a batch of N sentence pairs is thus deﬁned as:
L ¼  log
esimðhi;hþ
i Þ=s
PN
j¼1 esimðhi;hþ
j Þ=s ;
ð1Þ
where s is a temperature hyperparameter and simðh1; h2Þ is cosine similarity function between sentences
hT
1 h2
jjh1jj:jjh2jj.
3.1.1 Unsupervised
We construct three independent subsets for training and evaluating an unsupervised model: (i) title-only dataset
dtitle ¼ fstitle
o ; . . .; stitle
i
g from the title part of the claims for training Unsupervised-T; (ii) the concatenation
between title and content dtitleþcontent for training Unsupervised-TC; and (iii) the concatenation between title and
fact dtitleþfact for training Unsupervised-TF. From the resulting collection of sentences fxigm
i¼1; x 2 d, a positive
pair of sentences is composed of fxi; xþ
i g where xþ
i can be deﬁned as a nonessential variation of xi without
modifying its semantic meaning so that xþ
i ¼ fðxiÞ. We utilize dropout masks on fully connected layers and
attention probabilities (default p=0.1) in a standard training of Transformers and BERT-based models as f(.)—a
noise function representing a minimal form of data augmentation, following a similar conﬁguration in the
previous study [23]. We simply project sentences xi into the BERT encoder twice to obtain two independent
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21413

---

## Page 8
sentence embeddings with different dropout masks fz; z0g, representing positive pairs in Eq. 1. Thus, in an
unsupervised setup, the objective becomes:
Lunsup ¼  log
esimðh
zi
i ;h
z0
i
i Þ=s
PN
j¼1 esimðh
zi
i ;h
z0
j
j Þ=s
:
ð2Þ
3.1.2 Weakly supervised (pairwise)
We construct pairwise data fq; sg ¼ fðq0; s0
0Þ; ðq0; s1
0Þ; . . .ðqi; sj
iÞg representing positive pairs ðxi; xþ
i Þ in this study
by pairing the title as the query qi and their target sentence sj
i from document di; di ¼ fs0
i ; . . .; sj
ig is composed of j
sentences. The target document di is extracted from the content of the claim or reference to facts if available. The
training objective for pairwise contrastive learning follows Eq. 1, such that Lpairwise ¼ L.
3.1.3 Supervised (triplet)
We extend the pairwise setup ðxi; xþ
i Þ to triplets containing a negative sample for each positive pair ðxi; xþ
i ; x
i Þ.
For each positive pair ðxi; xþ
i Þ from a particular class category, Hard Negative x
i
is explicitly deﬁned by
randomly sample titles from the opposite class. The training objective is thus deﬁned by:
Ltriplets ¼  log
esimðhi;hþ
i Þ=s
PN
j¼1ðesimðhi;hþ
j Þ=s þ esimðhi;h
j Þ=sÞ
:
ð3Þ
3.2 Filtering
RQ2: How to automatically clean pairwise data to ensure an effective and efﬁcient contrastive learning?
Not all the sentences in the corresponding article or the reference to the fact are equally relevant to the given
claim. This problem is explicitly deﬁned as a noise removal task in [73] where noisy data is removed using an
independent BERT classiﬁer. [51] convert claims and evidence to graphs to capture the long-distance dependency
of relevant information. In fake news detection task, noisy sentence pairs can be present due to topic overlap,
stylistic similarity, and shared entities across label categories (real news vs. fake news) [74–76], exempliﬁed in
the following sentence pairs.
•
False positive pairs due to topic overlap.
Example:
Claim A (fake news): ‘‘NASA conﬁrms alien life on Mars.’’
Claim B (real news): ‘‘NASA’s Curiosity rover has found iron-rich carbonates on Mars.’’
Issue: Both claims discuss a topic about Mars, but they come from different label category. Treating the
samples as positive pairs can propagate the classiﬁcation errors because the model focuses more on topic
semantic similarity, instead of fact-checking property as an important step in a fake news detection task.
•
False positive pairs due to stylistic similarity.
Example:
Claim A (fake news): ‘‘Jokowi Draws Red Line: Malaysia Dared to Send Weapons to Australia!’’
Claim B (real news): ‘‘Record-Breaking! Jokowi claims 187 Trillion Rupiah Poured Into Villages!’’
123
Neural Computing and Applications (2025) 37:21407–21433
21414
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 9
Issue: Both claims share a sensational tone that can lead to error propagation because during the training
stage the model focuses more on a stylistic element rather than the news content or context to be veriﬁed.
•
False positive pairs due to shared entities.
Example:
Sample A (fake news): ‘‘Jokowi warns Malaysia against sending weapons to Australia.’’
Sample B (real news): ‘‘Jokowi claims to have disbursed 187 trillion rupiah in village funds.’’
Issue:Both claims discuss the same entities (Name entity: People). Using this sentence pair as a training
sample can lead to a model that focuses only on associating entity-related news as factor to classify sentences
under the same label category.
To mitigate the presence of noises when pairing sentences, this study adopts two ﬁltering methods used in
previous works: (i) Consistency ﬁltering [77, 78]; and (ii) Threshold ﬁltering [77]. In particular, we focus on the
following aspects when deciding whether a sampled pair can be included in training and evaluation dataset.
1.
The relevance between the claim and the corresponding news content and evidence.
The concept of sentence pairing can be associated with the claim veriﬁcation stage in fact-checking. That
is, given a claim and the corresponding content and evidence or factual knowledge, the task is to verify the
factuality of the claim relevant to the news content and evidence. In a content-based fake news detection and a
contrastive learning approach, this veriﬁcation task can be translated to a pairing task between claim and
content or evidence. First, we split the news contents and evidence into sentences. Then, each claim is paired
with the list of sentences from the news content and evidence to verify the claim. The resulting sentence pairs
are then ﬁltered using consistency ﬁltering between claim as a query and sentences included in top-k retrieval.
Consistency ﬁltering [77, 78]
We project query q and target sentences s onto pretrained embedding models to produce query and corpus
embeddings. For each query, we ﬁnd top-k (k ¼ 5) most similar sentences in the corpus to the query through
cosine similarity. Using nine independent pretraining embedding models listed in Table 3, we ﬁlter out samples
or sentence pairs that are not in the topk retrieved sentences by one of the pretraining embedding models.
2.
The threshold of triplet similarity between positive and negative pairs.
To prevent a false negative pair problem [74], we incorporate a threshold measure to distinguish between
positive and negative pairs. This ﬁltering method is speciﬁc to triplet data pairs that we constructed by
randomly sampling negative sentences from the opposite label category.
Threshold ﬁltering [77]
Table 3 Publicly available base pretrained models for BERT in this study based on model versioning in HuggingFace hub
repository
Category
Pretraining
Base model
Symmetric semantic similarity
Indonesian
(1) LazarusNLP/simcse-indobert-base
Indonesian
(2) LazarusNLP/simcse-indoroberta-base
Indonesian
(3) LazarusNLP/congen-indobert-base
Indonesian
(4) LazarusNLP/congen-simcse-indobert-base
Multilingual
(5) sentence-transformers/paraphrase-multilingual-mpnet-base-v2
Asymmetric semantic search
English
(6) sentence-transformers/msmarco-roberta-base-v3
Indonesian
(7) LazarusNLP/s-indobert-base-mmarco
Classiﬁcation-based Pretraining
Indonesian
(8) indolem/indobertweet-base-uncased
Indonesian
(9) cahya/distilbert-base-indonesian
Indonesian
(10) YagiASAFAS/indonesia-news-classiﬁcation-bert
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21415

---

## Page 10
A threshold k is deﬁned as the similarity difference between positive pairs and negative pairs
rðq; pÞ  rðq; nÞ [ k, so that triplets that have k\0:2 are ﬁltered out. The intuition of this ﬁltering method is to
ensure that positive pair has higher similarity score than negative pair.
3.3 Class imbalance
RQ3: How to address extreme class imbalance problem in current fake news data?
We deﬁne two sequential stages for reducing the overﬁt and the bias of the model toward the majority class.
Contrastive learning Contrastive learning as our main training framework in this study, allows BERT-based
models to extract meaningful representations from unlabeled data by leveraging the concept of pairwise similarity
and dissimilarity as training signals. Its advantages outnumber the end-to-end classiﬁers with the resampling
method. It can learn useful features even when data is scarce and imbalanced [79]. On the other hand, resampling
methods are known with numerous limitations [80], such as: (i) information loss because random undersampling
discards data from the majority class so it potentially removes informative or useful samples; (ii) overﬁtting
because random oversampling introduces data redundancy.
Ensemble MLPs We employ stacking-based ensemble learning [49] to train multiple weak off-the-shelf MLP
classiﬁers, given the resulting embeddings from all embedding models in this study. Concretely, we divide
training data into ten (10) subsets where each subset contains balanced representations from both class labels
(Hoax and Non-Hoax) and four data sources, resulting in 500 Hoax samples and 500 Non-Hoax samples for each
data subset. We train an independent MLP classiﬁer for each training subset, resulting in 10 weak MLP clas-
siﬁers. During the inference stage, we average the probability outputs of all ten weak classiﬁers, resulting in the
ﬁnal prediction. The ensemble method combines multiple weak classiﬁers to create a stronger and more robust
classiﬁer. Compared to the resampling method, ensembles can better mitigate bias due to class imbalance without
discarding potentially informative samples and duplicating samples in training data.
3.4 Pretraining choice
RQ4: Does pretraining choice affect model performance on fake news classiﬁcation?
To further investigate the impact of pretraining objective to build a contrastive learning framework for fake
news detection, we classify ten (10) pretrained embedding models based on three broad categories: (i) Symmetric
semantic similarity—the pretrained embedding models are trained to measure similarity between short texts
(sentences); (ii) Asymmetric semantic search—the pretrained models are trained in a semantic-based retrieval task
where query and document pairs have a different text length; and (iii) classiﬁcation-based pretraining—the
pretrained models are ﬁne-tuned or distilled on multiclass classiﬁcation task. The intuition is that fake news data
have asymmetric characteristics where claims and articles or facts are in different lengths, similar to data
characteristic in pretraining objective based on asymmetric semantic search. So, we want to compare whether
such data assumption holds based on how the ﬁne-tuned model performs on fake news classiﬁcation as target
domain. We list the pretrained models and their corresponding category in Table 3.
3.5 Evaluation tasks
RQ5: How to evaluate contrastive learning in fake news detection domain?
We deﬁne three main evaluation tasks for the evaluation of end-to-end classiﬁers and embedding models in this
study as follows:
123
Neural Computing and Applications (2025) 37:21407–21433
21416
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 11
3.5.1 Fake news classification
We evaluate the models in the binary classiﬁcation task based on two performance measurement settings:
(i) Embedding model ? Ensemble MLP classiﬁers; (ii) end-to-end classiﬁer (BERT for sequence classiﬁcation).
In (i), test samples are projected onto the trained embedding models, including the proposed models based on
contrastive learning. The resulting embedding is used as input features for ensemble MLP classiﬁers. In (ii), test
samples are used as input for the trained BERT classiﬁer, a baseline model with fully supervised learning,
resulting in ﬁnal class probability output.
3.5.2 Clustering
We use clustering evaluation to inspect the quality of embeddings based on their proximity distance in a
presumably optimal embedding space. That is, whether the embeddings are naturally grouped into compact
clusters such that similar text entities are being close to each other, while dissimilar texts or neighboring clusters
of embeddings are sufﬁciently far from each other. In general, the clustering evaluation in this study serves as a
compliance measure to objectively inspect whether the proposed contrastive embedding method conforms to two
key properties for contrastive learning. Alignment and uniformity [81]. It is important to note that a clustering
method is not a classiﬁcation tool such that compact clusters are not necessarily faithful to the predeﬁned class or
label category. Our premise is that supervised embeddings may represent clusters of a fake news classiﬁcation
task (k=2) because the embedding model has been trained to ﬁt the predeﬁned binary class representation of
Hoax and Non-Hoax samples. On the other hand, unsupervised and contrastive embeddings learned text rep-
resentation almost unsupervisedly, thus the embeddings may only capture linguistic entities found in the given
textual content, such as topics. To be fair, we evaluated the quality of the embeddings based on two clustering
setups: (i) k=2; (ii) k=40. We manually create ﬁne-grained topic labels for each sample in test data, resulting in
40 topic categories as ground-truth labels for evaluating clustering performance. The list of annotated topics will
be provided in our publicly shared data and code repository.
3.5.3 Retrieval
In an integrated automated fact-checking framework, a retrieval task is included in the fact or evidence retrieval
stage, and the ﬁnal veriﬁcation of the claim is included as a ﬁltering method or noise removal task. Therefore, it is
important to inspect the embedding model capability as part of a fact-checking system that focuses more on
content-based detection task. In this evaluation task, give the reported claim as a query, the objective is to retrieve
the relevant information that can either support or refute the claims from article and fact references metadata in
corpus.
4 Experiments
4.1 Low-resource datasets
We compare the performance results between our proposed approach and the baselines on non-English language
resources1:
•
IndoHoax—our constructed Indonesian fake news dataset, which is extracted from the real-world fact-
checking and hoax reporting system in Indonesia2 from the timeline of 2018-2023, resulting in training and
1 All datasets are available at https://anonymous.4open.science/r/contrast-BERT.
2 https://maﬁndo.or.id/.
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21417

---

## Page 12
test datasets as shown in Table 4. Unlike the other low-resource datasets in this study, our Indonesian dataset
is composed of (i) diverse topics (i.e., Politics, Law and Criminals, Social, Economy, Education, Technology,
Sports, Health, Entertainment); (ii) ﬁne-grained categorization of misinformation and disinformation (i.e.,
Fabricated content, Impostor content, Satire, Misleading content, Manipulated content, False context, False
connection), and extremely class imbalance ratio (96:4) between fake and real claims.
Preprocessing: We ﬁrst clean IndoHoax data by removing explicit class identiﬁer or sentences in news
content and evidence that summarize whether a claim is true or false, for example: ‘‘This is Hoax,’’ ‘‘[FALSE
CLAIM].’’ We remove new content and evidence that contain less than 20 words. For training a contrastive
learning objective, we create sentence pairs by pairing claims and sentences in news content and evidence. We
remove noisy sentence pairs both in pairwise and triplet datasets by ﬁltering data using consistency and
threshold ﬁltering (Section 3.2).
Class Ratio: Our IndoHoax dataset is inherently imbalanced, where the ratio between fake news samples
and real news is 96:4 (Table 4). In our preliminary experiment, we exercise the fake news classiﬁcation task
by adding more real news data from reputable news sources to the training dataset. However, because the
characteristic of real news data from the newly added domain is different to the current real news subset, the
classiﬁcation performance does not improve, implying a stylistic problem inherently found in the current
dataset. We later discuss this stylistic problem in Section 5 (Fig. 2). Therefore, in this study, we focus more on
Table 4 Real-world fake news data based on Indonesian online hoax reporting systems. The average #token is based on
LazarusNLP/simcse-indobert-base tokenizer on training data. C0=‘‘Non-Hoax,’’ while C1=‘‘Hoax’’
Source
Sample Size
Class Proportion (%)
Average #Tokens
Fact (%)
Train
Test
Train
Test
Title
Content
Fact
Train
Test
C0
C1
C0
C1
Maﬁndo
6983
199
1.2
98.8
50
50
14  5
94  114
227  175
98.3
97.5
Saber-Hoax Jabar
4523
198
3.5
96.5
50
50
12  3
52  37
148  95
89.7
72.5
Opendata Jabar
354
99
15.5
84.5
50
50
14  4
N/A
N/A
0.0
0.0
Klinik-Hoax Jatim
492
98
100
0.0
100
0.0
12  3
47  25
103  41
29.3
0.0
Total
12352
594
6.4
93.6
58.3
41.7
13  4
78  94
196  154
89.6
56.7
Fig. 2 Embedding visualization for Indonesian and Bangla fake news data.
1 All datasets are available at https://anonymous.4open.science/r/contrast-BERT.
2 https://maﬁndo.or.id/.
123
Neural Computing and Applications (2025) 37:21407–21433
21418
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 13
investigating methods for training a fake news classiﬁcation task. We view a new approach with data
augmentation strategy to enforce models to be invariant to topic overlap, stylistic similarity, and shared entities
as a future research direction.
•
Tallip-ID [6]—Indonesian-translated fake news data from multilingual fake news detection. The data contains
a ground-truth topic categorization for each claim. We mainly use this data for zero-shot performance analysis
on topic clustering;
•
Clickbait-ID [43]—Indonesian clickbait benchmark dataset. Speciﬁc for clickbait data, we create multiple
training subsets with different class imbalance ratio to further inspect the performance consistency across
domain and imbalance level. This particular preprocessing step produces: (i) balance subset (50:50); (ii)
mildly balanced (70:30), (75:25); (iii) moderately imbalanced (80:20), (85:15); and (iv) extremely imbalanced
(90:10), (95:5), (98:2);
•
BanFakeNews [44]—Dataset for clickbait detection in Bangla language. This dataset consists mainly of
headlines and the corresponding content of news articles. Each headline is classiﬁed into either ‘‘clickbait’’ or
‘‘nonclickbait’’;
•
CsFEVER and CsFEVER-NLI [45]—Fact-checking datasets that are constructed by translating FEVER
dataset from English to Czech language. We further preprocessed these datasets to produce subsets of data
with a similar class imbalance ratio to the Indonesian dataset (IndoHoax).
DeClare Format
To be able to train evidence-aware fake news detection approaches on our Indonesian dataset, we reconstructed
data into a new structure deﬁned in DeClare [82]. The data transformation results in 10:755 training set and 337
test set for our Indonesian data. The new DeClare formatted dataset is mainly composed of samples containing
claims, the corresponding single summarized evidence, and the URL source of evidences. We discarded samples
that contain no evidence.
4.2 Baselines
Table 2 shows automatic fake news detection methods that are being investigated in this study. We divide
baselines based on three categories:
1.
End-to-end (E2E) classiﬁcation methods, which are further divided into:
(a)
Evidence-aware approaches:
•
MAC (Multi-head Attention network for Fact-Checking) [83]—The method employs multi-head
attention mechanisms to analyze and cross-reference multiple pieces of evidence against a claim;
•
GET (Graph-based sEmantic sTructure) [84]—The method models claims and evidence as graph-
structured data to capture long-distance semantic dependencies through neighborhood propagation;
•
GETRAL (Graph-based sEmantic structure mining framework with ConTRAstive Learning) [51]—
The method integrates supervised contrastive learning and adversarial augmented instances to
enhance GNN representation learning and reduce sensitivity to local evidence;
•
ReRead [73]—The method involves two key steps: (i) training an evidence retriever to obtain
interpretable evidence based on faithfulness and plausibility; and (ii) training a claim veriﬁer to
reexamine the retrieved evidence to enhance accuracy.
(b)
Content-based approach based on BERT pretrained language model [85]. Speciﬁc to BERT-based
methods, we compare BERT models with and without ﬁne-tuning strategy. For ﬁne-tuning BERT, we
mainly focus on a simple mask language modeling (MLM) ﬁne-tuning objective [86] and a binary
classiﬁcation task on target fake news domain.
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21419

---

## Page 14
2.
Two-stage learning [50]—To provide a fair evaluation, we use BERT embeddings without contrastive
learning as a baseline model for two-stage learning approach.
3.
Large language models (LLMs)—LLMs have been utilized as an AI agent to predict the veracity of claim for
fact-checking and fake news detection task [73, 87]. We use OpenAI GPT-3.5-turbo (gpt-3.5-turbo-
0125) and GPT-4-turbo as LLM baseline in this study. For evaluating LLM performance, we compare the
prediction output when LLM use ‘‘claim’’ as the only input to the model and ‘‘claim ? evidence’’ as input.
The class probability score is computed based on the probability of LLM outputs tokens: ‘‘REFUTES’’ (fake)
or ‘‘SUPPORTS’’ (real). Speciﬁc for LLM with evidence as auxiliary input, we do not output the token
probability score because the model generates prediction with reasoning (Chain-of-Thought [88]).
4.3 Training
For all training and evaluation schemes, we employ NVIDIA DGX-A100 GPU with 40GB RAM and CUDA
version: 12.2. The hyperparameters3 are conﬁgured independently for each model. To ensure the reproducibility
aspect, we conﬁgure our evaluation code to run deterministically by using a same set of random seeds across all
models in this study.
5 Result and discussion
5.1 Fake news classification
Performance on Indonesian fake news data We investigate the capability of the proposed Contrast-BERT for
predicting whether a claim is considered fake or real. Table 5 shows the performance comparison on Indonesian
fake news data. We observe that both Pairwise Contrast-BERT and Unsupervised Contrast-BERT outperform
E2E BERT by maintaining a balance score between Precision (P) and Recall (R) when predicting fake and real
claims as positive class label. However, ﬁne-tuning BERT on extremely imbalanced data with a supervision does
not yield a better outcome. Both masked language model (MLM) and classiﬁcation-based tuning method fail to
improve the performance of pretrained BERT on target domain, suggesting that utilizing a pretrained model based
on contrastive learning (base model ‘‘LazarusNLP/simcse-indobert-base’’) is adequate for the current
fake news detection task. Overall, Contrast-BERT is less prone to the overconﬁdence errors, which is demon-
strated by the lowest brier loss (15:8), as shown in Table 5.
Speciﬁc to evidence-aware approaches, we observe that a simple hierarchical attention networks can outper-
form approaches based on graph neural networks (GNNs), such as GET and GETRAL. We believe that a lower
performance score of GNNs is mainly due to the networks are not able to capture useful structure inferred in
IndoHoax. Compared to the English fake news and fact-checking datasets shown in Table 1, IndoHoax does not
contain multiple evidences and the corresponding sources.
Lastly, utilizing a more powerful large language model, such as OpenAI GPT-4; and grounding the model with
an evidence, boost the overall classiﬁcation performance. However, GPT-4 comes at a higher price. Comparing
GPT-4 (’ 1:8T) and models with smaller parameter size, such as BERT (109.5M), thus, is rather an unfair
performance comparison.
Analysis on dataset difﬁculty We investigate whether Indonesian dataset poses a different challenge than the
other low-resource fake news datasets in this study. First, we project data into embedding space via OpenAI
‘‘text-embedding-3-large.’’ Based on the embedding visualization in Figure 2, speciﬁc to the Indonesian
dataset (IndoHoax), we observe that simply adding more data from real news articles does not necessarily address
3 The hyperparameter conﬁguration is available at https://anonymous.4open.science/r/contrast-BERT.
123
Neural Computing and Applications (2025) 37:21407–21433
21420
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 15
the class imbalance problem. The reason is that real news articles come from a different distribution than ‘‘real’’
claim samples in IndoHoax training set. It is also interesting to observe that both fake and real claims in IndoHoax
are highly overlapping, suggesting an inferred stylistic and linguistic challenge for content-based fake news
detection methods.
Error analysis
We further investigate the prediction errors of classiﬁcation models in this study, particularly Contrast-BERT
(Pairwise) and end-to-end (E2E) BERT classiﬁer as follows:
1.
Statistical summary of errors (false positive and false negative)
Table 6 shows the statistical summary of prediction errors and the corresponding model’s conﬁdence. In
this study, false positive (FP) refers to the type of prediction error where the model predicts real news and true
claim as False or ‘‘fake news,’’ while false negative (FN) is the opposite label misclassiﬁcation.
Based on the comparison of model conﬁdence in Table 6, we observe that the model based on contrastive
learning (Contrast-BERT) is less conﬁdent than E2E BERT classiﬁer and native BERT embedding when
misclassifying samples. However, Contrast-BERT is overconﬁdent for predicting true claim, resulting in a
higher number of false negative. We further analyze misclassiﬁed samples based on both false positive and
false negative error types based on topic, name entities, and stylistic or tone implied in test samples.
Table 5 Performance on our Indonesian fake news dataset (IndoHoax) based on claim and evidence as merged input
features. Base model for BERT: LazarusNLP/simcse-indobert-base
Method
"ACC
"FMacro
1
"FMicro
1
Real News
Fake News
#Brier Loss
"F1
"P
"R
"F1
"P
"R
Evidence-aware
MACðensembleÞ
72.7*
71.1
72.7*
64.3
72.8
57.6**
77.8**
72.6**
83.9
19.2
GETðensembleÞ
63.5
52.2
63.5
28.9
86.2
17.4
75.4*
61.4
97.9
20.9
GETRALðensembleÞ
66.2
57.1
66.2
37.4
89.5
23.6
76.8**
63.2
97.9
20.8
ReReadðensembleÞ
44.5
34.4
44.5
8.78
75.0
4.66
60.1
43.3
97.9
26.1
OpenAI LLM
GPT3.5-turbo
- Claim-only
67.5
67.5
67.5
66.9
58.9
77.2**
68.1
78.2**
60.3
25.8
- With evidence
85.9**
84.7**
85.9**
80.4**
95.7
69.3**
89.1**
81.9**
97.8
N/A
GPT-4-turbo
- Claim-only
72.7*
70.8
72.7*
63.2
74.5
54.9**
78.3**
71.9**
86.0
24.1
- With evidence
92.8**
92.4**
92.8**
90.8**
94.8
87.2**
94.1**
91.6**
96.7
N/A
E2E BERT Classiﬁer
BERT
68.7
68.2
68.7
64.2
95.4
48.4
72.1
57.5
96.8
31.0
BERTðensembleÞ
77.7**
77.7**
77.7**
78.4**
89.9
69.5**
77.1**
67.9**
89.1
17.9
BERT Embeddings
No-Fine-tuning
75.2**
74.7**
75.2**
78.3**
79.6
77.1**
71.1
69.6**
72.6
16.3
MLM Tuning
74.6**
73.6**
74.6**
78.6**
76.8
80.6**
68.6
71.1**
66.3
18.2
Classif. Tuning
70.4
70.1
70.4
67.0
94.7
51.9
73.1
59.0
95.9
29.1
Contrast-BERT
Pairwise
77.3**
76.8**
77.3**
80.2**
81.3
79.1**
73.3
72.1**
74.7
15.9
Triplet
74.7**
74.5**
74.7**
76.9**
81.9
72.5**
72.1
67.1**
77.9
16.9
Unsupervised
76.1**
75.5**
76.1**
79.3**
79.8
78.8**
71.7
71.1**
72.3
15.8
Signiﬁcance value q\0.05(*) and q\0.01(**) are computed based on E2E BERT classiﬁer with 95% conﬁdence
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21421

---

## Page 16
2.
Qualitative ﬁndings
We inspect the prediction errors of the proposed Contrast-BERT based on topic overlap, shared name
entities, and stylistic aspect of the news or claims, such as the presence of sensational tone. We observe that a
high topic overlap between class labels is present in the current Indonesian dataset, with an exception that
particular topic categories are dominantly present in one class. For example, ‘‘Government Policy’’ occurs
more in true claims, while ‘‘Financial Scams,’’ ‘‘Political Figures,’’ and ‘‘Sensational/Viral Video’’ occur more
in false claim samples. We observe that a higher proportion of false positives come from the three dominant
topics in false claim samples (‘‘Financial Scams,’’ ‘‘Political Figures,’’ and ‘‘Sensational/Viral Video’’),
suggesting that the model may use cues or signals belong to a fake news category, such as name entities and
sensational tone commonly found in false claims.
•
Correctly classiﬁed ‘‘true claims’’ (real news)
Topics: Campaign & Election (13), COVID-19 Outbreak (21), COVID-19 Vaccine Hoaxes (6),
COVID-19 Disinformation (41), Fake Job Openings (4), Financial Scams (45), Food & Health Rumours
(2), Government Policy (74), Healthcare (27), Natural Disaster (15), Policy & Public-Service
Misinformation around COVID-19 (9), Political Figures (26), Sensational/Viral Video (20).
•
Correctly classiﬁed ‘‘false claims’’ (fake news)
Topics: Campaign & Election (18), Counterfeit Account/Letter (14), COVID-19 Outbreak (22),
COVID-19 Vaccine Hoaxes (3), COVID-19 Disinformation (54), Fake Job Openings (5), Financial Scams
(67), Government Policy (9), Healthcare (40), Natural Disaster (4), Political Figures (29), Sensational/
Viral Video (66).
•
False positive
Topics: Campaign & Election (7), Counterfeit Account/Letter (2), COVID-19 Outbreak (6), COVID-19
Vaccine Hoaxes (2), COVID-19 Disinformation (7), Fake Job Openings (4), Financial Scams (23), Food &
Health Rumours (2), Government Policy (3), Healthcare (10), Natural Disaster (5), Political Figures (14),
Sensational/Viral Video (14).
Example:
Topic: Political Figures
Text:
Claim: Coordinating Minister Luhut Denies Sending an Open Letter to Amien Rais and Prabowo.‘‘
Fact: Coordinating Minister for Maritime Affairs, Luhut Binsar Pandjaitan, ﬁrmly stated that he never
sent an open letter to Amien Rais and Prabowo Subianto, contrary to the news circulating recently.
Label: true claim
Predicted: false claim (fake news).
Topic: Sensational/Viral Video
Text:
Table 6 Summary of errors
based on false positive and
false negative for the pro-
posed Contrast-BERT and
E2E BERT classiﬁer
Metric
Contrast-BERT Pairwise (ours)
E2E BERT
BERT ? Ensemble MLP
TP
FP
FN
TP
FP
FN
TP
FP
FN
Mean conﬁdence
0.837
0.713
0.728
0.996
0.994
0.991
0.996
0.989
0.958
Median conﬁdence
0.878
0.693
0.731
1.0
1.0
1.0
1.0
1.0
1.0
Min conﬁdence
0.502
0.500
0.504
0.590
0.687
0.929
0.528
0.555
0.584
Max conﬁdence
1.0
0.982
0.993
1.0
1.0
1.0
1.0
1.0
1.0
Count
459
73
62
408
178
8
418
166
10
Total
459
135
408
186
418
176
Inference Size
594
123
Neural Computing and Applications (2025) 37:21407–21433
21422
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 17
Claim: A RARE SIGHT—SNOW FALLS IN SAUDI ARABIA.’’
Fact: Snow has fallen in the southwestern mountainous regions of Saudi Arabia. Residents were seen
joyfully enjoying the sight of deserts blanketed in white snow. According to Arab News on Wednesday
(January 15, 2020), the areas that experienced snowfall include the northern parts of Tabuk, Jabal Al
Lawz, Al-Daher, and the Alqan mountains. These snowy regions in Saudi Arabia are popular tourist
destinations.
Label: true claim
Predicted: false claim (fake news).
•
False negative
Topics: Campaign & Election (6), Counterfeit Account/Letter (6), COVID-19 Outbreak (6), COVID-19
Vaccine Hoaxes (1), COVID-19 Disinformation (11), Fake Job Openings (4), Financial Scams (15), Food
& Health Rumours (2), Government Policy (3), Healthcare (7), Natural Disaster (2), Political Figures (5),
Sensational/Viral Video (4).
Performance across languages
Figure 3 shows the performance comparison of four methods: (i) our proposed Contrast-BERT; (ii) E2E
BERT for Sequence Classiﬁcation; (iii) OpenAI GPT3.5-turbo; and (iv) OpenAI GPT-4-turbo. In this exper-
iment, we conﬁgure all datasets to be extremely imbalanced, resulting in imbalance ratio between fake news and
real news as follows: IndoHoax (96:4); BanFakeNews (4:96); CsFEVER (96:4); and CsFEVER-NLI (91:9). In
particular, we observe that the proposed Contrast-BERT outperforms E2E BERT when predicting ‘‘Real’’ claims,
which are sampled from the minority class category, as shown in Figure 3a. Compared to the other low-resource
datasets, both unnatural Czech fake news datasets (CsFEVER and CsFEVER-NLI) introduces challenges for
BERT-based models to predict samples from both minority and majority classes, following a similar low
performance reported in the original paper [45]. Nevertheless, our Contrast-BERT is able to predict the minority
class samples in both CsFEVER and CsFEVER-NLI, compared to E2E BERT that cannot recall all real news
samples (F1 score for real news ¼ 0:0). It is also interesting to observe that OpenAI GPT-4-turbo, which is the
most powerful Black Box model in this study, underperforms on our Indonesian datasets compared to the other
datasets. This suggests that our Indonesian dataset introduces the remaining challenge for future study on content-
based low-resource fake news detection.
Fig. 3 Fake news classiﬁcation performance (%) on low-resource fake news datasets based on F1 Score for ‘‘Real’’ and
‘‘Fake’’ news.
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21423

---

## Page 18
5.2 Clustering on Indonesian data
The clustering performance represents model’s own inductive bias—the implicit structure that the model learns
by connecting different entities in training data [89, 90]. Table 7 shows the performance comparison given the
predeﬁned number of clusters as k=2 and k=40. In binary clustering (k ¼ 2), the number of clusters represents
binary labels in fake news data, while in clustering with k ¼ 40, the number of clusters represents ﬁne-grained
topics inferred in target data, which we manually deﬁne (Section 3.5.2). In general, Contrast-BERT models are
observed to capture ﬁne-grained topics than binary label representation, which is shown by higher completeness
score (0.437), homogeneity (0.487), ARI (0.154), and NMI (0.461) in topic clustering experiment with k¼ 40. In
contrast, supervised embeddings have higher scores when k=2. However, we observe that the natural clusters
formed by the supervised embeddings do not represent the actual label supervision, which is shown by the
considerably low overall performance score for k ¼ 2 across multiple clustering evaluation metrics (\0:2).
5.3 Retrieval on real-world data
Table 7 includes the performance scores for evidence retrieval task where the embedding models rank top-5 most
relevant documents or evidences in the corpus given claim as a query. In general, we observe that both Pairwise
and Triplet Contrast-BERT can retrieve at least 86.4% of relevant document references based on their top-5
prediction. In contrast, supervised embeddings have a poor retrieval performance (HR@5  0:5 and
MRR@5\0:4). This result implies the capability of Contrast-BERT to be used in a retrieval-based fact veriﬁ-
cation based on similarity function, in addition to be used as embedding model in fake news classiﬁcation
pipeline.
5.4 Ablation study
We further investigate the impact of heuristic choices in our experimental design as follows:
Pretraining choice
Table 7 Performance on clustering and retrieval tasks. Base model: LazarusNLP/simcse-indobert-base
Method
Clustering
Retrieval
"Completeness
"Homogeneity
"ARI
"NMI
"HR@5
"MRR@5
k = 2
k = 40
k = 2
k = 40
k = 2
k = 40
k = 2
k = 40
Unsupervised Embeddings
Zero-shot-TF
3.0e4
0.332**
2.8e4
0.365**
8.0e4
0.084**
2.8e4
0.347**
0.783**
0.716**
MLM Fine-tuning-TF
0.005
0.305**
0.005
0.339**
0.009
0.067**
0.005
0.321**
0.737**
0.642**
Supervised Embeddings
E2E BERT-T
0.146
0.185
0.099
0.181
0.126
0.014
0.119
0.183
0.405
0.344
E2E BERT-TC
0.108
0.168
0.100
0.183
0.150
0.017
0.104
0.175
0.421
0.366
E2E BERT-TF
0.097
0.178
0.069
0.201
0.099
0.015
0.081
0.189
0.405
0.328
Contrast-BERT (ours)
Pairwise-TCF
0.043
0.381**
0.043
0.415**
0.053
0.102**
0.043
0.398**
0.882**
0.835**
Triplet-TCF
0.009
0.437**
0.009
0.487**
0.006
0.154**
0.009
0.461**
0.862**
0.815**
Unsupervised-T
0.003
0.249**
0.003
0.262**
0.007
0.039**
0.003
0.256**
0.763**
0.696**
Unsupervised-TC
4.5e4
0.242**
4.5e4
0.261**
3.5e4
0.027*
4.5e4
0.251**
0.734**
0.656**
Unsupervised-TF
0.010
0.280**
0.010
0.310**
0.014
0.044**
0.010
0.295**
0.753**
0.685**
Signiﬁcance value p\0.05(*) and p\0.01(**) are computed based on E2E BERT-T with 95% conﬁdence
123
Neural Computing and Applications (2025) 37:21407–21433
21424
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 19
Figure 4 shows the impact of choosing pretrained embeddings based on our categorical constraints (Table 3).
We observe that utilizing classiﬁcation-based pretrained embeddings (Classify-8 and Classify-10) leads to per-
formance deterioration, producing the lowest accuracy-based performance (Fig. 4a) and the highest brier loss
(Fig. 4b). On the other hand, there is no such signiﬁcant differences between utilizing pretrained embeddings in
Symmetric and Asymmetric category, as shown by small performance difference based on Brier loss between
Symmetric-1 and Asymmetric-6. In general, utilizing base models based on contrastive learning that has been
pretrained on Indonesian Wikipedia pairwise data—Symmetric-1 is shown to be beneﬁcial in current fake news
classiﬁcation task.
Domain transfer
Fig. 4 Performance comparison based on choices of pretrained embeddings.
Table 8 Zero-shot clustering and retrieval performance on Indonesian-translated fake news dataset. Score is based on the
average of 10 runs. Base model: LazarusNLP/simcse-indobert-base
Method
Clustering
Retrieval
"Completeness
"Homogeneity
"ARI
"NMI
"HR@5
"MRR@5
k = 2
k = 7
k = 2
k = 7
k = 2
k = 7
k = 2
k = 7
Unsupervised
Embeddings
Zero-shot-TF
5.5e5
0.209**
5.5e5
0.256**
-6.8e4
0.132**
5.5e5
0.230**
0.821**
0.669**
MLM Fine-tuning-TF
0.001
0.205**
0.001
0.233**
8.4e4
0.154**
0.001
0.218**
0.636**
0.491**
Supervised Embeddings
E2E BERT-T
0.013
0.056
0.002
0.058
0.001
0.048
0.003
0.057
0.438
0.328
E2E BERT-TC
0.006
0.064
0.003
0.072
0.005
0.100**
0.004
0.068
0.412
0.330
E2E BERT-TF
0.002
0.043
8.6e4
0.042
0.002
0.064
0.001
0.043
0.370
0.292
Contrast-BERT (ours)
Pairwise-TCF
0.001
0.311**
0.001
0.377**
0.001
0.182**
0.001
0.341**
0.895**
0.738**
Triplet-TCF
1.3e4
0.349**
1.2e4
0.400**
-3.4e4
0.274**
1.2e4
0.373**
0.864**
0.715**
Unsupervised-T
0.002
0.162**
0.002
0.197**
0.002
0.105**
0.002
0.178**
0.710**
0.546**
Unsupervised-TC
0.006
0.180**
0.006
0.219**
0.006*
0.123**
0.006*
0.198**
0.726**
0.572**
Unsupervised-TF
0.002
0.167**
0.002
0.205**
0.002
0.119**
0.002
0.184**
0.743**
0.604**
Signiﬁcance value q\0.05(*) and q\0.01(**) are computed based on E2E BERT-T with 95% conﬁdence
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21425

---

## Page 20
We investigate the zero-shot classiﬁcation performance on unseen Indonesian-translated fake news dataset
from multilingual fake news detection study [6]. This dataset contains explicit topic categorization (n topic = 7).
Table 8 shows that Pairwise Contrast-BERT and Triplet Contrast-BERT consistently perform well on both topic
clustering with k=7 and evidence retrieval task. The zero-shot performance results imply the generalization
capability of models based on contrastive learning, particularly when unseen data contains sufﬁcient contextual
abstraction such as topic categories. Figure 5 shows 2D visualization of text embeddings from Indonesian-
translated fake news data [6]. We observe that Contrast-BERT models are better at capturing topics as natural
clusters of data.
Representation bias
We further inspect whether the resulting embeddings inherit biases toward textual tone of fake news data.
Although most of Hoax data are created mainly using sensational tone, it is important to note that disregarding
this characteristic of the data as a sensitive attribute or protected feature and allowing machine learning models to
directly pick up the textual tone as essential features during the prediction stage is considered harmful from the
perspective of fairness of AI [91, 92]. First, models can suffer on unseen data or target domain without such
implicit feature, leading to unreliable performance. Second, in a real-world fake news detection system, a false
Fig. 5 2D Visualization of embeddings with TSNE, based on zero-shot embedding projection on unseen Indonesian-
translated fake news data with seven topic categories
Table 9 Measuring bias of the embeddings on neutral tone (minor group category) vs. sensational tone (major group
category) for ‘‘Hoax’’ label (Class label=1). Base model: LazarusNLP/simcse-indobert-base
Metric
Reference
E2E BERT-T
E2E BERT-TF
Zero-shot
Pairwise
(Title only)
(Title?Fact)
Contrast-BERT
Statistical Parity
0
0.3031
0.2458
0.0281
0.0240**
Disparate Impact
1
0.6421
0.6679
0.9279**
1.0448**
Four Fifths Rule
1
0.6421
0.6679
0.9279**
0.9571**
Cohen D
0
0.7445
0.5365
0.0579
0.0483**
Equality of Opportunity Diff
0
0.0038
0.0234
0.0860
0.0988
False Positive Rate Diff
0
0.3035
0.2301
 0.0119
0.0168**
Average Odds Diff
0
0.1536
0.1033
0.0489
 0.0410**
Accuracy Diff
0
0.0478
0.0545
0.0464
0.0553
Signiﬁcance value q\0.05(*) and \0.01(**) are computed based on E2E BERT-T with 95% conﬁdence
123
Neural Computing and Applications (2025) 37:21407–21433
21426
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 21
positive case where a Non-Hoax sample or legitimate news is incorrectly labeled as Hoax or Fake, can harm the
reputation of the news source and the author of the reported claim [33].
We ﬁrst annotate test data by utilizing OpenAI ChatGPT to generate binary labels (Neutral vs. Sensational)
given short claims (Titles). We run LLM inference experiment three times to extract the label prediction based
on the majority vote. The resulting annotated test data is composed of 182 samples with neutral tone and 412
samples with sensational tone. Both Hoax and Non-Hoax subsets contain balanced representation of samples with
sensational tone (206 samples), inferring that sensational tone coexists in both classes. On the other hand, neutral
tone is more skewed (43 Hoax samples vs. 139 Non-Hoax samples). Table 9 shows the scores representing bias
measure for zero-shot classiﬁcation task with BERT embedding models in this study. In general, Pairwise
Contrast-BERT is less biased compared to the other models when predicting Hoax samples under both neutral
and sensational tones.
Imbalance ratio
We investigate performance trend across different class imbalance ratio, ranging from balance class repre-
sentation {50:50} to extremely imbalance ratio {98:2}, given binary class categories: clickbait versus
nonclickbait. Based on results in Fig. 6, we observe that Contrast-BERT is more accurate when training data is
extremely imbalanced (ratio  95:5) based on accuracy and precision metrics. However, Contrast-BERT has
lower F1-score, inferring low recall score. This overall low recall score, similar to the real-world use case of fake
news detection in Table 5, makes sense because Contrast-BERT does not explicitly learn explicit label super-
vision during training stage. Instead, the model exploits alternate training signals solely based on textual content.
In contrast, E2E classiﬁer learns skewed data distribution during training stage, thus, the supervised model carries
bias that the majority samples in unseen target data are from the majority class category (Clickbait), resulting in
higher recall yet lower precision.
6 Conclusion
In this study, we present a simple framework for low-resource fake news detection based on contrastive learning
and stacking-based ensemble learning. Instead of viewing the problem as an end-to-end classiﬁcation task, we
decompose the fake news detection task into two main sequential stages: (1) learning useful embedding models
for fake news detection on extremely imbalanced data; and (2) combining the resulting embedding models and
Fig. 6 Performance across different class imbalance ratio. Scores are computed based on ‘‘Clickbait’’ as positive class
(class-id=1)
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21427

---

## Page 22
ensemble of MLPs as a classiﬁcation pipeline. Our work demonstrates the capability of Contrast-BERT for
addressing an extreme class imbalance problem for low-resource fake news detection tasks, particularly in
Indonesian, Bangla, and Czech languages.
Author contributions The authors conﬁrm contribution to the paper as follows: Conceptualization: Iftitahu Ni’mah, Rini
Wijayanti, Agung Santosa, Asril Jarin, Tri Sampurno, Mohammad Teduh Uliniansyah, and Mykola Pechenizkiy;
Methodology: Iftitahu Ni’mah and Rini Wijayanti; Literature Review: Iftitahu Ni’mah, Rini Wijayanti, and Asril Jarin; Data
collection, preprocessing, and preliminary analysis: Iftitahu Ni’mah, Rini Wijayanti, Agung Santosa, Asril Jarin, Tri
Sampurno, and Mohammad Teduh Uliniansyah; Code implementation: Iftitahu Ni’mah; Analysis and interpretation of
results: Iftitahu Ni’mah, Rini Wijayanti, and Agung Santosa; Writing - original draft preparation: Iftitahu Ni’mah and Rini
Wijayanti; Writing - review and editing: Iftitahu Ni’mah, Rini Wijayanti, Agung Santosa, Asril Jarin, Tri Sampurno, and
Mohammad Teduh Uliniansyah; Supervision: Meng Fang, Vlado Menkovski, and Mykola Pechenizkiy.
Funding No funding was received to assist with the preparation of this manuscript. All authors read and approved the ﬁnal
manuscript.
Data and code availability Data, materials, and code implementation will be made publicly available. An anonymous
temporary repository is available at https://anonymous.4open.science/r/contrast-BERT.
Declarations
Competing interest All authors certify that they have no affiliations with or involvement in any organization or entity with
any financial interest or non-financial interest in the subject matter or materials discussed in this manuscript.
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The
images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
1. Edson C. Tandoc Jr., ZWL, Ling, R (2018) Deﬁning ‘‘fake news’’. Dig J 6(2):137–153. https://doi.org/10.1080/
21670811.2017.1360143
2. Rahman RA, Tang S-M (2022) Fake news and internet shutdowns in Indonesia: symptoms of failure to uphold
democracy. Const Rev 8:151
3. Allcott H, Gentzkow M (2017) Social media and fake news in the 2016 election. J Econ Perspect 31(2):211–36. https://
doi.org/10.1257/jep.31.2.211
4. Utami P (2018) Hoax in modern politics: the meaning of hoax in indonesian politics and democracy. J Ilmu Sosial dan
Ilmu Politik 22(2):85–97. https://doi.org/10.22146/jsp.34614
5. Shu K, Sliva AL, Wang S, Tang J, Liu H (2017) Fake news detection on social media: A data mining perspective. arXiv:
1708.01967
6. De A, Bandyopadhyay D, Gain B, Ekbal A (2021) A transformer-based approach to multilingual fake news detection in
low-resource languages. ACM Trans Asian Low-Resour Lang Inf Process 21(1). https://doi.org/10.1145/3472619
7. Aji AF, Winata GI, Koto F, Cahyawijaya S, Romadhony A, Mahendra R, Kurniawan K, Moeljadi D, Prasojo RE,
Baldwin T, Lau JH, Ruder S (2022) One country, 700? languages: NLP challenges for underrepresented languages and
dialects in Indonesia. In: Muresan S, Nakov P, Villavicencio A (eds) Proceedings of the 60th annual meeting of the
association for computational linguistics. Association for computational linguistics, Dublin, Ireland, vol 1 Long Papers,
pp 7226–7249. https://doi.org/10.18653/v1/2022.acl-long.500. https://aclanthology.org/2022.acl-long.500
8. Wibowo HA, Fuadi EH, Nityasya MN, Prasojo RE, Aji AF (2023) Copal-id: Indonesian language reasoning with local
culture and nuances. arXiv preprint arXiv:2311.01012
9. Nan Q, Wang D, Zhu Y, Sheng Q, Shi Y, Cao J, Li J (2022) Improving fake news detection of inﬂuential domain via
domain- and instance-level transfer. In: Calzolari N, Huang CR, Kim H, Pustejovsky J, Wanner L, Choi KS, Ryu PM,
123
Neural Computing and Applications (2025) 37:21407–21433
21428
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 23
Chen HH, Donatelli L, Ji H, Kurohashi S, Paggio P, Xue N, Kim S, Hahm Y, He Z, Lee TK, Santus E, Bond F, Na SH
(eds) Proceedings of the 29th international conference on computational linguistics. International committee on com-
putational linguistics, Gyeongju, Republic of Korea, pp 2834–2848. https://aclanthology.org/2022.coling-1.250
10. Cohn-Gordon R, Goodman N (2019) Lost in machine translation: a method to reduce meaning loss. In: Burstein J,
Doran C, Solorio T (eds) Proceedings of the 2019 conference of the North American chapter of the association for
computational linguistics: human language technologies, vol 1 (Long and Short Papers). Association for computational
linguistics, Minneapolis, Minnesota, pp 437–441. https://doi.org/10.18653/v1/N19-1042. https://aclanthology.org/N19-
1042
11. Wiedemann G, Remus S, Chawla A, Biemann C (2019) Does BERT make any sense? interpretable word sense
disambiguation with contextualized embeddings. CoRR arXiv:1909.10430
12. S¸ahin GG (2022) To augment or not to augment? A Comparative Study on Text Augmentation Techniques for Low-
Resource NLP. Comput Lingu 48(1):–42. https://doi.org/10.1162/coli_a_00425. https://direct.mit.edu/coli/article-pdf/
48/1/5/2006622/coli_a_00425.pdf
13. Saadany H, Orasan C, Mohamed E (2020) Fake or real? A study of Arabic satirical fake news. In: Aker, A., Zubiaga, A
(eds) Proceedings of the 3rd international workshop on rumours and deception in social media (RDSM). Association for
computational linguistics, Barcelona, Spain (Online), pp 70–80. https://aclanthology.org/2020.rdsm-1.7
14. Khouja J (2020) Stance prediction and claim veriﬁcation: an Arabic perspective. In: Christodoulopoulos C, Thorne J,
Vlachos A, Cocarascu O, Mittal A (eds) Proceedings of the third workshop on fact extraction and veriﬁcation (FEVER).
Association for Computational Linguistics, Online, pp 8–17. https://doi.org/10.18653/v1/2020.fever-1.2. https://aclan
thology.org/2020.fever-1.2
15. Sheikh Ali Z, Mansour W, Elsayed T, Al-Ali A (2021) AraFacts: The ﬁrst large Arabic dataset of naturally occurring
claims. In: Habash N, Bouamor H, Hajj H, Magdy W, Zaghouani W, Bougares F, Tomeh N, Abu Farha I, Touileb S
(eds.) Proceedings of the sixth Arabic natural language processing workshop. Association for computational linguistics,
Kyiv, Ukraine (Virtual), pp 231–236. https://aclanthology.org/2021.wanlp-1.26
16. Broscoteanu D, Ionescu R (2023) A novel contrastive learning method for clickbait detection on RoCliCo: A Romanian
clickbait corpus of news articles. In: Bouamor H, Pino J, Bali K (eds) Findings of the association for computational
linguistics: EMNLP 2023. Association for Computational Linguistics, Singapore, pp 9547–9555. https://doi.org/10.
18653/v1/2023.ﬁndings-emnlp.640. https://aclanthology.org/2023.ﬁndings-emnlp.640
17. Rahim NHA, Basri MSH (2022) Malcov: Covid-19 fake news dataset in the malay language. In: 2022 International
visualization, informatics and technology conference (IVIT), pp. 239–244. https://doi.org/10.1109/IVIT55443.2022.
10033374
18. Kaushal V, Vemuri K (2020) Clickbait in Hindi news media : a preliminary study. In: Bhattacharyya P, Sharma DM,
Sangal R (eds) Proceedings of the 17th international conference on natural language processing (ICON). NLP Asso-
ciation of India (NLPAI), Indian Institute of Technology Patna, Patna, India, pp 85–89. https://aclanthology.org/2020.
icon-main.11
19. Gupta V, Kumari, R, Ashok N, Ghosal T, Ekbal A (2022) MMM: an emotion and novelty-aware approach for
multilingual multimodal misinformation detection. In: He Y, Ji H, Li S, Liu Y, Chang CH (eds) Findings of the
association for computational linguistics: AACL-IJCNLP 2022. Association for computational linguistics, online only,
pp 464–477. https://aclanthology.org/2022.ﬁndings-aacl.43
20. Fawaid J, Awalina A, Krisnabayu RY, Yudistira N (2021) Indonesia’s fake news detection using transformer network.
In: Proceedings of the 6th international conference on sustainable information engineering and technology. SIET ’21.
Association for computing machinery, New York, NY, USA, pp 247–251. https://doi.org/10.1145/3479645.3479666.
https://doi.org/10.1145/3479645.3479666
21. Nurlatifah M, Irwansyah I (2019) Fact-checking journalism Sebagai platform kolaborasi human and machine pada
jurnalisme digital. Jurnal Komunikasi 13(2):121–134. https://doi.org/10.20885/komunikasi.vol13.iss2.art1
22. Chen T, Kornblith S, Norouzi M, Hinton G (2020) A simple framework for contrastive learning of visual representa-
tions. In: Proceedings of the 37th international conference on machine learning. ICML’20. JMLR.org
23. Gao T, Yao X, Chen D (2021) SimCSE: Simple contrastive learning of sentence embeddings. In: Moens MF, Huang X,
Specia L, Yih SWt (eds) Proceedings of the 2021 conference on empirical methods in natural language processing.
Association for computational linguistics, online and Punta Cana, Dominican Republic, pp 6894–6910. https://doi.org/
10.18653/v1/2021.emnlp-main.552. https://aclanthology.org/2021.emnlp-main.552
24. Pratiwi IYR, Asmara RA, Rahutomo F (2017) Study of hoax news detection using naı¨ve bayes classiﬁer in indonesian
language. In: 2017 11th international conference on information & communication technology and system (ICTS),
pp 73–78. https://doi.org/10.1109/ICTS.2017.8265649
25. Haumahu JP, Permana SDH, Yaddarabullah Y (2021) Fake news classiﬁcation for Indonesian news using extreme
gradient boosting (xgboost). IOP Conf Ser Mater Sci Eng 1098(5):052081. https://doi.org/10.1088/1757-899X/1098/5/
052081
26. Fawaid J, Awalina A, Krisnabayu RY, Yudistira N (2021) Indonesia’s fake news detection using transformer network.
In: Proceedings of the 6th international conference on sustainable information engineering and technology. SIET ’21.
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21429

---

## Page 24
Association for computing machinery, New York, NY, USA, pp 247–251. https://doi.org/10.1145/3479645.3479666.
https://doi.org/10.1145/3479645.3479666
27. Saini K, Vishwakarma DK, Dhiman C (2021) Sentiment analysis of twitter corpus related to covid-19 induced lock-
down. In: 2021 2nd international conference on secure cyber computing and communications (ICSCCC), pp 465–470.
https://doi.org/10.1109/ICSCCC51823.2021.9478112
28. Narang P, Singh AV, Monga H (2024) Sentiment score-based classiﬁcation for fake news using machine learning and
lstm-bilstm. Soft Comput 1–18
29. Narang P, Singh AV, Monga H (2024) Enhanced detection of fabricated news through sentiment analysis and text
feature extraction. Int J Inf Technol 1–10
30. Narang P, Singh AV, Monga H (2024) Integrating metaheuristics and two-tiered classiﬁcation for enhanced fake news
detection with feature optimization. EAI Endors Trans Scalable Inf Syst
31. Dhiman C, Kumar G (2024) Textual context guided vision transformer with rotated multi-head attention for sentiment
analysis. In: Companion proceedings of the ACM web conference 2024. WWW ’24. Association for computing
machinery, New York, NY, USA, pp 1823–1830. https://doi.org/10.1145/3589335.3651968. https://doi.org/10.1145/
3589335.3651968
32. Sitaula N, Mohan CK, Grygiel J, Zhou X, Zafarani R (2020) In: Shu K, Wang S, Lee D, Liu H (eds.) Credibility-based
fake news detection. Springer, Cham, pp 163–182. https://doi.org/10.1007/978-3-030-42699-6_9. https://doi.org/10.
1007/978-3-030-42699-6_9
33. Raza S, Ding C (2022) Fake news detection based on news content and social contexts: a transformer-based approach.
Int J Data Sci Anal 13(4):335–362
34. Saikia P, Gundale K, Jain A, Jadeja D, Patel H, Roy M (2022) Modelling social context for fake news detection: a graph
neural network based approach. In: 2022 international joint conference on neural networks (IJCNN), pp 01–08. https://
doi.org/10.1109/IJCNN55064.2022.9892311
35. Fardiah D, Darmawan F, Rinawati R (2022) Fact-checking literacy of covid-19 Infodemic on social media in Indonesia.
Komunikator 14(1):14–29
36. Saputri NI, Sibaroni Y, Prasetiyowati SS (2023) Covid-19 fake news detection on twitter based on author credibility
using information gain and knn methodscovid-19 fake news detection on twitter based on author credibility using
information gain and knn methods. Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi) 7(1):185–192. https://doi.
org/10.29207/resti.v7i1.4871
37. Mosallanezhad A, Karami M, Shu K, Mancenido MV, Liu H (2022) Domain adaptive fake news detection via rein-
forcement learning. In: Proceedings of the ACM web conference 2022. WWW ’22. Association for computing
machinery, New York, NY, USA, pp 3632–3640. https://doi.org/10.1145/3485447.3512258. https://doi.org/10.1145/
3485447.3512258
38. Donabauer G, Kruschwitz U (2024) Challenges in pre-training graph neural networks for context-based fake news
detection: an evaluation of current strategies and resource limitations. arXiv preprint arXiv:2402.18179
39. Thorne J, Vlachos A, Christodoulopoulos C, Mittal A (2018) FEVER: a large-scale dataset for fact extraction and
VERiﬁcation. In: Walker M, Ji H, Stent A (eds) Proceedings of the 2018 conference of the North American chapter of
the association for computational linguistics: human language technologies, vol 1 (Long Papers). Association for
Computational Linguistics, New Orleans, Louisiana, pp 809–819. https://doi.org/10.18653/v1/N18-1074. https://aclan
thology.org/N18-1074
40. Wang WY (2017) ’’liar, liar pants on ﬁre’’: a new benchmark dataset for fake news detection. In: Barzilay R, Kan MY
(eds) Proceedings of the 55th annual meeting of the association for computational linguistics. Association for Com-
putational Linguistics, Vancouver, Canada, vol 2 (Short Papers), pp 422–426. https://doi.org/10.18653/v1/P17-2067.
https://aclanthology.org/P17-2067
41. Hanselowski A, Stab C, Schulz C, Li Z, Gurevych I (2019) A richly annotated corpus for different tasks in automated
fact-checking. In: Bansal M, Villavicencio A (eds) Proceedings of the 23rd conference on computational natural
language learning (CoNLL). Association for computational linguistics, Hong Kong, China, pp 493–503. https://doi.org/
10.18653/v1/K19-1046. https://aclanthology.org/K19-1046
42. Hu X, Guo Z, Wu G, Liu A, Wen L, Yu P (2022) CHEF: a pilot Chinese dataset for evidence-based fact-checking. In:
Carpuat M, Marneffe MC, Meza Ruiz IV (eds) Proceedings of the 2022 conference of the north american chapter of the
association for computational linguistics: human language technologies. Association for computational linguistics,
Seattle, United States, pp 3362–3376. https://doi.org/10.18653/v1/2022.naacl-main.246. https://aclanthology.org/2022.
naacl-main.246
43. William A, Sari Y (2020) Click-id: a novel dataset for Indonesian clickbait headlines. Data in Brief 32:106231 https://
doi.org/10.1016/j.dib.2020.106231
44. Hossain MZ, Rahman MA, Islam MS, Kar S (2020) BanFakeNews: a dataset for detecting fake news in Bangla. In:
Calzolari N, Be´chet F, Blache P, Choukri K, Cieri C, Declerck T, Goggi S, Isahara H, Maegaard B, Mariani J, Mazo H,
Moreno A, Odijk J, Piperidis S (eds) Proceedings of the twelfth language resources and evaluation conference. European
language resources association, Marseille, France, pp 2862–2871. https://aclanthology.org/2020.lrec-1.349
123
Neural Computing and Applications (2025) 37:21407–21433
21430
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 25
45. Ullrich H, Drchal J, Ry´par M, Vincourova´ H, Moravec V (2023) CsFEVER and CTKFacts: acquiring Czech data for
fact veriﬁcation. Lang Resour Eval 57(4):1571–1605. https://doi.org/10.1007/s10579-023-09654-3
46. Bhattacharjee S, Maity S, Chatterjee S (2023) Addressing class imbalance in fake news detection with latent space
resampling. In: Das AK, Nayak J, Naik B, Vimal S, Pelusi D (eds) Computational Intelligence in Pattern Recognition.
Springer, Singapore, pp 427–438
47. Ahmad I, Yousaf M, Yousaf S, Ahmad MO (2020) Fake news detection using machine learning ensemble methods.
Complexity 2020:1–11
48. Elyassami S, Alseiari S, ALZaabi M, Hashem A, Aljahoori N (2022) In: Lahby M, Pathan A.-SK, Maleh Y, Yafooz
WMS (eds) Fake news detection using ensemble learning and machine learning algorithms. Springer, Cham,
pp 149–162. https://doi.org/10.1007/978-3-030-90087-8_7. https://doi.org/10.1007/978-3-030-90087-8_7
49. Rezaei S, Kahani M, Behkamal B, Jalayer A (2022) Early multi-class ensemble-based fake news detection using content
features. Soc Netw Anal Min 13(1):16
50. Shwartz-Ziv R, Goldblum M, Li Y, Bruss CB, Wilson AG (2023) Simplifying neural network training under class
imbalance. In: Oh A, Naumann T, Globerson A, Saenko K, Hardt M, Levine S (eds) Advances in neural information
processing systems. Curran Associates, Inc., vol 36, pp 35218–35245. https://proceedings.neurips.cc/paper_ﬁles/paper/
2023/ﬁle/6ea69f8116b7c01e3c3e43b62e6868fc-Paper-Conference.pdf
51. Wu J, Xu W, Liu Q, Wu S, Wang L (2023) Adversarial contrastive learning for evidence-aware fake news detection with
graph neural networks. IEEE Trans Knowl Data Eng 1–14 https://doi.org/10.1109/TKDE.2023.3341640
52. Yin S, Zhu P, Wu L, Gao C, Wang Z (2024) Gamc: An unsupervised method for fake news detection using graph
autoencoder with masking. Proc AAAI Conf Artif Intell 38(1):347–355. https://doi.org/10.1609/aaai.v38i1.27788
53. Podkorytov M, Bis´ D, Liu X (2021) How can the [mask] know? the sources and limitations of knowledge in bert. In:
2021 international joint conference on neural networks (IJCNN), pp 1–8. https://doi.org/10.1109/IJCNN52387.2021.
9534299
54. Chopra S, Hadsell R, LeCun Y (2005) Learning a similarity metric discriminatively, with application to face veriﬁcation.
In: 2005 IEEE computer society conference on computer vision and pattern recognition (CVPR’05), vol 1,
pp 539–5461. https://doi.org/10.1109/CVPR.2005.202
55. Gutmann M, Hyva¨rinen A (2010) Noise-contrastive estimation: A new estimation principle for unnormalized statistical
models. In: Teh YW, Titterington M (eds) Proceedings of the Thirteenth international conference on artiﬁcial intelli-
gence and statistics. Proceedings of machine learning research. PMLR, Chia Laguna Resort, Sardinia, Italy, vol 9,
pp 297–304. https://proceedings.mlr.press/v9/gutmann10a.html
56. Oh Song H, Xiang Y, Jegelka S, Savarese S (2016) Deep metric learning via lifted structured feature embedding. In:
Proceedings of the IEEE Conference on computer vision and pattern recognition (CVPR)
57. Rethmeier N, Augenstein I (2023) A primer on contrastive pretraining in language processing: Methods, lessons learned,
and perspectives. ACM Comput Surv 55(10). https://doi.org/10.1145/3561970
58. Jaiswal A, Babu AR, Zadeh MZ, Banerjee D, Makedon F (2021) A survey on contrastive self-supervised learning.
Technologies 9(1) https://doi.org/10.3390/technologies9010002
59. Chen T, Kornblith S, Swersky K, Norouzi M, Hinton GE (2020) If-supervised models are strong semi-supervised
learners. In: Larochelle H, Ranzato M, Hadsell R, Balcan MF, Lin H (eds) Advances in neural information processing
systems. Curran Associates, Inc., vol 33, pp 22243–22255. https://proceedings.neurips.cc/paper_ﬁles/paper/2020/ﬁle/
fcbc95ccdd551da181207c0c1400c655-Paper.pdf
60. Lee J, Joe S, Park K, Kim B, Kang H, Park J, Gwon Y (2022) Shufﬂe & divide: Contrastive learning for long text. In:
2022 26th international conference on pattern recognition (ICPR), pp 2935–2941. https://doi.org/10.1109/ICPR56361.
2022.9956208
61. Du Y, Ma T, Wu L, Xu F, Zhang X, Long B, Ji S (2021) Constructing contrastive samples via summarization for text
classiﬁcation with limited annotations. In: Moens MF, Huang X, Specia L, Yih SWt (eds) Findings of the association for
computational linguistics: EMNLP 2021. Association for Computational Linguistics, Punta Cana, Dominican Republic,
pp 1365–1376. https://doi.org/10.18653/v1/2021.ﬁndings-emnlp.118. https://aclanthology.org/2021.ﬁndings-emnlp.118
62. An C, Zhong M, Wu Z, Zhu Q, Huang X, Qiu X (2022) CoLo: A contrastive learning based re-ranking framework for
one-stage summarization. In: Calzolari N, Huang CR, Kim H, Pustejovsky J, Wanner L, Choi KS, Ryu PM, Chen HH,
Donatelli L, Ji H, Kurohashi S, Paggio P, Xue N, Kim S, Hahm Y, He Z, Lee TK, Santus E, Bond F, Na SH (eds)
Proceedings of the 29th international conference on computational linguistics. International committee on computational
linguistics, Gyeongju, Republic of Korea, pp 5783–5793(2022). https://aclanthology.org/2022.coling-1.508
63. Hammouchi H, Ghogho M (2022) Evidence-aware multilingual fake news detection. IEEE Access 10:116808–116818
https://doi.org/10.1109/ACCESS.2022.3220690
64. Al-Ash HS, Wibowo WC (2018) Fake news identiﬁcation characteristics using named entity recognition and phrase
detection. In: 2018 10th international conference on information technology and electrical engineering (ICITEE),
pp 12–17. https://doi.org/10.1109/ICITEED.2018.8534898
65. Lin N, Qin G, Wang G, Zhou D, Yang A (2023) An effective deployment of contrastive learning in multi-label text
classiﬁcation. In: Rogers A, Boyd-Graber J, Okazaki N (eds) Findings of the Association for computational linguistics:
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21431

---

## Page 26
ACL 2023. Association for computational linguistics, Toronto, Canada, pp 8730–8744. https://doi.org/10.18653/v1/
2023.ﬁndings-acl.556. https://aclanthology.org/2023.ﬁndings-acl.556
66. Jia O, Huang H, Ren J, Xie L, Xiao Y (2023) Contrastive learning with text augmentation for text classiﬁcation. Appl
Intell 53(16):19522–19531. https://doi.org/10.1007/s10489-023-04453-3
67. Khalid B, Dai S, Taghavi T, Lee S (2024) Label supervised contrastive learning for imbalanced text classiﬁcation in
Euclidean and hyperbolic embedding spaces. In: Goot R, Bak J, Mu¨ller-Eberstein M, Xu W, Ritter A, Baldwin T (eds)
Proceedings of the ninth workshop on noisy and user-generated text (W-NUT 2024). Association for computational
linguistics, San _Giljan, Malta, pp 58–67. https://aclanthology.org/2024.wnut-1.6
68. Wang L, Zhang C, Xu H, Xu Y, Xu X, Wang S (2023) Cross-modal contrastive learning for multimodal fake news
detection. In: Proceedings of the 31st ACM International Conference on Multimedia. MM ’23. Association for com-
puting machinery, New York, NY, USA, pp 5696–5704. https://doi.org/10.1145/3581783.3613850. https://doi.org/10.
1145/3581783.3613850
69. Xu, F., Fu, P., Huang, Q., Zou, B., Aw, A., Wang, M.: Leveraging contrastive learning and knowledge distillation for
incomplete modality rumor detection. In: Bouamor, H., Pino, J., Bali, K. (eds.) Findings of the Association for
Computational Linguistics: EMNLP 2023, pp. 13492–13503. Association for Computational Linguistics, Singapore
(2023). https://doi.org/10.18653/v1/2023.ﬁndings-emnlp.900. https://aclanthology.org/2023.ﬁndings-emnlp.900
70. Zheng P, Chen H, Hu S, Zhu B, Hu J, Lin CS, Wu X, Lyu S, Huang G, Wang X (2024) Few-shot learning for
misinformation detection based on contrastive models. Electronics 13(4). https://doi.org/10.3390/electronics13040799
71. Chen T, Sun Y, Shi Y, Hong L (2017) On sampling strategies for neural network-based collaborative ﬁltering. In:
Proceedings of the 23rd ACM SIGKDD international conference on knowledge discovery and data mining. KDD ’17.
Association for computing machinery, New York, NY, USA, pp 767–776. https://doi.org/10.1145/3097983.3098202.
https://doi.org/10.1145/3097983.3098202
72. Henderson M, Al-Rfou R, Strope B, Sung Yh, Luka´cs L, Guo R, Kumar S, Miklos B, Kurzweil R (2017) Efﬁcient
natural language response suggestion for smart reply. ArXiv e-prints
73. Hu X, Hong Z, Guo Z, Wen L, Yu P (2023) Read it twice: Towards faithfully interpretable fact veriﬁcation by revisiting
evidence. In: Proceedings of the 46th international ACM SIGIR conference on research and development in information
retrieval. SIGIR ’23. Association for computing machinery, New York, NY, USA, pp 2319–2323. https://doi.org/10.
1145/3539618.3592049. https://doi.org/10.1145/3539618.3592049
74. Wang, T, Chen L, Zhu X, Lee Y, Gao J (2023) Weighted contrastive learning with false negative control to help long-
tailed product classiﬁcation. In: Sitaram S, Beigman Klebanov B, Williams JD (eds) Proceedings of the 61st annual
meeting of the association for computational linguistics (Industry Track). Association for Computational Linguistics,
Toronto, Canada, vol 5, pp 574–580. https://doi.org/10.18653/v1/2023.acl-industry.55. https://aclanthology.org/2023.
acl-industry.55/
75. Wu J, Xu W, Liu Q, Wu S, Wang L (2023) Adversarial contrastive learning for evidence-aware fake news detection with
graph neural networks. IEEE Trans Knowl Data Eng 01:1–14. https://doi.org/10.1109/TKDE.2023.3341640
76. Zhang W, Gui L, He Y (2021) Supervised contrastive learning for multimodal unreliable news detection in covid-19
pandemic. In: Proceedings of the 30th ACM international conference on information & knowledge management. CIKM
’21. Association for computing machinery, New York, NY, USA, pp 3637–3641. https://doi.org/10.1145/3459637.
3482196. https://doi.org/10.1145/3459637.3482196
77. Gu¨nther M, Mastrapas G, Wang B, Xiao H, Geuter J (2023) Jina embeddings: a novel set of high-performance sentence
embedding models. In: Tan L, Milajevs D, Chauhan G, Gwinnup J, Rippeth E (eds) Proceedings of the 3rd workshop for
natural language processing open source software (NLP-OSS 2023). Association for computational linguistics, Sin-
gapore, pp 8–18. https://doi.org/10.18653/v1/2023.nlposs-1.2. https://aclanthology.org/2023.nlposs-1.2
78. Wang L, Yang N, Huang X, Jiao B, Yang L, Jiang D, Majumder R, Wei F (2022) Text embeddings by weakly-
supervised contrastive pre-training. arXiv preprint arXiv:2212.03533
79. Marrakchi Y, Makansi O, Brox T (2021) Fighting class imbalance with contrastive learning. In: Bruijne M, Cattin PC,
Cotin S, Padoy N, Speidel S, Zheng Y, Essert C (eds) Medical Image Computing and Computer Assisted Intervention -
MICCAI 2021. Springer, Cham, pp 466–476
80. Wongvorachan T, He S, Bulut O (2023) A comparison of undersampling, oversampling, and smote methods for dealing
with imbalanced classiﬁcation in educational data mining. Information 14(1). https://doi.org/10.3390/info14010054
81. Wang L, Huang J, Huang K, Hu Z, Wang G, Gu Q (2020) Improving neural language generation with spectrum control.
In: International conference on learning representations. https://openreview.net/forum?id=ByxY8CNtvr
82. Popat K, Mukherjee S, Yates A, Weikum G (2018) DeClarE: Debunking fake news and false claims using evidence-
aware deep learning. In: Riloff E, Chiang D, Hockenmaier J, Tsujii J (eds) Proceedings of the 2018 conference on
empirical methods in natural language processing. Association for computational linguistics, Brussels, Belgium,
pp. 22–32. https://doi.org/10.18653/v1/D18-1003. https://aclanthology.org/D18-1003
83. Vo N, Lee K (2021) Hierarchical multi-head attentive network for evidence-aware fake news detection. In: Merlo P,
Tiedemann J, Tsarfaty R (eds) Proceedings of the 16th conference of the European chapter of the association for
123
Neural Computing and Applications (2025) 37:21407–21433
21432
https://doi.org/10.1007/s00521-025-11467-0

---

## Page 27
computational linguistics: main volume. Association for computational linguistics, online, pp 965–975. https://doi.org/
10.18653/v1/2021.eacl-main.83. https://aclanthology.org/2021.eacl-main.83
84. Xu W, Wu J, Liu Q, Wu S, Wang L (2022) Evidence-aware fake news detection with graph neural networks. In:
Proceedings of the ACM web conference 2022. WWW ’22. Association for computing machinery, New York, NY,
USA, pp 2501–2510. https://doi.org/10.1145/3485447.3512122. https://doi.org/10.1145/3485447.3512122
85. Devlin J, Chang MW, Lee K, Toutanova K (2019) BERT: pre-training of deep bidirectional transformers for language
understanding. In: Burstein J, Doran C, Solorio T (eds) Proceedings of the 2019 conference of the north american
chapter of the association for computational linguistics: human language technologies. Association for computational
linguistics, Minneapolis, Minnesota, vol 1 (Long and Short Papers), pp 4171–4186. https://doi.org/10.18653/v1/N19-
1423. https://aclanthology.org/N19-1423
86. Wettig A, Gao T, Zhong Z, Chen D (2023) Should you mask 15% in masked language modeling? In: Vlachos A,
Augenstein I (eds) Proceedings of the 17th conference of the European chapter of the association for computational
linguistics. Association for computational linguistics, Dubrovnik, Croatia, pp 2985–3000. https://doi.org/10.18653/v1/
2023.eacl-main.217. https://aclanthology.org/2023.eacl-main.217
87. Semnani S, Yao V, Zhang H, Lam M (2023) WikiChat: stopping the hallucination of large language model chatbots by
few-shot grounding on wikipedia. In: Bouamor H, Pino J, Bali K(eds) Findings of the association for computational
linguistics: EMNLP 2023. Association for computational linguistics, Singapore, pp 2387–2413. https://doi.org/10.
18653/v1/2023.ﬁndings-emnlp.157. https://aclanthology.org/2023.ﬁndings-emnlp.157
88. Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, Chi EH, Le QV, Zhou D (2024) Chain-of-thought prompting
elicits reasoning in large language models. In: Proceedings of the 36th international conference on neural information
processing systems. NIPS ’22. Curran Associates Inc., Red Hook, NY, USA
89. Pimentel T, Meister CI, Cotterell R (2023) On the usefulness of embeddings, clusters and strings for text generation
evaluation. In: The eleventh international conference on learning representations. https://openreview.net/forum?id=
bvpkw7UIRdU
90. HaoChen JZ, Ma T (2023) A theoretical study of inductive biases in contrastive learning. In: The eleventh international
conference on learning representations. https://openreview.net/forum?id=AuEgNlEAmed
91. Kertysova K (2018) Artiﬁcial intelligence and disinformation: How AI changes the way disinformation is produced,
disseminated, and can be countered. Secur Human Rights 29(1–4):55–81
92. Ju Y, Hu S, Jia S, Chen GH, Lyu S (2024) Improving fairness in deepfake detection. In: Proceedings of the IEEE/CVF
winter conference on applications of computer vision (WACV), pp 4655–4665
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
afﬁliations.
Authors and Afﬁliations
Iftitahu Ni’mah1,2
• Rini Wijayanti1 • Agung Santosa1 • Asril Jarin1 • Tri Sampurno1 •
Mohammad Teduh Uliniansyah1 • Meng Fang3 • Vlado Menkovski2
• Mykola Pechenizkiy
2
& Iftitahu Ni’mah
i.nimah@tue.nl; iftitahu.nimah@brin.go.id
1
Research Center for Information and Data Sciences, National Research and Innovation Agency (BRIN),
Bandung, Jawa Barat 40135, Indonesia
2
Department of Mathematics and Computer Science, Eindhoven University of Technology, Eindhoven, The
Netherlands
3
Department of Computer Science, University of Liverpool, Liverpool, UK
Neural Computing and Applications (2025) 37:21407–21433
123
https://doi.org/10.1007/s00521-025-11467-0
21433

---
