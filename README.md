# Artificial-Intelligence
## _First steps on AI. May help for learners like me._

## Introduction
Two good definitions for Artificial Intelligence (AI) are...
- Technology that seeks to simulate the human process of learning and decision making.
- A wide-ranging branch of computer science concerned with the construction of intelligent machines that are able to perform tasks that typically require human intelligence.

AI is based on three cognitive skills:
- **Learning**: Process focused on data acquisition and the creation of rules to transform data into useful information.
- **Reasoning**: Focused on choosing the right algorithm to achieve a desired result.
- **Self-Correction**: Refining the algorithms and ensuring that they provide the most accurate results possible.

**Data ≠ Information.** Data is raw and not meaningful. Information is data that has been given meaning by way of relational connection. This "meaning" can be useful, but does not have to be.

**Knowledge ≠ Wisdom.** Knowledge is the appropriate application of Information in order to be useful, and implies know-how and understanding. Knowledge identifies specific measures to apply to the information and be able to answer questions. On the other hand, wisdom goes further, and tries to find the reason behind any decision-making. It is the process by which it is possible to discern or judge between right and wrong, good and bad.

### Talking about security...
Although it's not the main objective, this repository also aims to take care of privacy and security.
Data anonymization is possible in different ways, and sometimes we can also achieve good results.

The concept of **Artificial Stupidity** it also exist. There are different ways to cheat or mess with the AI algorithms. There are some example, like putting a determined sticker close to an object to make an incorrect inference or hacking the real world. (An example for the last one is [McAfee's Model Hacking ADAS](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/model-hacking-adas-to-pave-safer-roads-for-autonomous-vehicles/).

Anyway... Systems usually have a training phase in which they "learn" to detect the right patterns and to act upon their information. Once the system is fully trained, it can enter the test phase, where more examples are found. The training phase can not cover all the possible examples that the system can deal with in the real world. So, these systems are easier to fool in ways that humans cannot be.


## Directory Structure
The structure of the repository is as follows:

- `CSV_Anonymizer`: Script and csv example to anonymize the data in specific fields. It uses a SHA-256 digest, a one-way function which is used to ofuscate the content.
- `Diabetes-diag`: Artificial Intelligence algorithm example. Based on some input data it can evaluate if a person suffers or not from diabetes.
- `objectDetection`: Object detection examples based on Artificial Intelligence. Models used where trained under COCO-2017 dataset. It can run on Edge platforms.
- `tensorflow-scripts `: Not really TensorFlow. It contains some usefull scripts in Python.

## Terms related to AI
As a beginner, there were many terms that overwhelmed and misunderstood me. Artificial intelligence is already on the lips of the general public and there are specific terms in the lexicon of this field that we should be familiar with, to know exactly what we are referring to.

- **Machine Learning (ML):** It's a subset of AI. It focuses on the development of computer programs (algorithms) that can grant access to data and then use it to learn for themselves. These algorithms can learn and improve over time when exposed to new data, i.e., ML uses statistical methods to enable machines to learn and improve with experience. Its main goal is to enable computers to learn automatically without human intervention or assistance. The goal is to learn from data a specific task to maximize machine performance on this task. While AI leads to intelligence or wisdom, ML leads to knowledge.
Even here we have different types of ML Models:
  - Supervised (Inductive) Learning: Training data includes desired outputs. Classification or Regression.
  - Unsupervised Learning: Training data does not include desired outputs. Dimensionality Reduction or Clustering.
  - Semi-Supervised Learning: Training data includes a few desired outputs. Predictions in the medical field (aids professionals with tests and diagnostics).
  - Reinforced Learning: Rewards from sequence of actions. Gaming, Finance Sector, Manufacturing, Inventory Management, Robot Navigation...
- **Deep Learning (DL):** It is a subfield of machine learning based on algorithms inspired in artificial neural networks
with many layers of nodes between input and output, that are capable of identify what something is. DL leads with the transformation and extraction of feature which attempts to establish a relationship between stimuli and associated neural responses present in the brain.
The architecture of a Deep Learning model includes: 
  - Unsupervised Pre-trained Networks:
  - Convolutional Neural Networks:
  - Recurrent Neural Networks:
  - Recursive Neural Networks:
- **Neural Network (NN):** It is a component of deep learning process. Leads with the transition data in the form of input values and output values through connections.
The architecture of a Neural Network includes: 
  - Feed Forward Neural Networks:
  - Recurrent Neural Networks:
  - Symmetrically Connected Neural Networks:
- **Data Science:**
- **Big Data:**

### From Biology to Computing: Understanding human neurons to comprehend Neural Networks in computing.

A neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a **process that mimics the way the human brain operates**. In this sense, neural networks refer to systems of neurons, either organic or artificial in nature.

Neural networks can adapt to changing input; so the network generates the best possible result without needing to redesign the output criteria.

#### Biologic Neurons:
There are many types of neurons, but let's classify them on three different classes:
- **Sensory Neuron (Unipolar):** They receive stimulus, which can come from the organism itself or the environment.
- **Motor Neurons (Bipolar):** They are responsible for conducting nerve impulses to effector organs, such as muscles and glands.
- **Interneurons (Multipolar):** They guarantee the connection between neurons.

Each class of neurons has its' own roles, but all of them have three basic functions:
1. Receive signals (or information).
2. Integrate input signals (to determine wether this information should be passed or not).
3. Communicate signals to target cells (other neurons or muscle glands).

A Neuron has 3 differentiated parts:
- **Dendrite:** They are neuron extensions. They guarantee the reception of stimuli, leading the nervous impulse towards the cellular body.
- **Axon:** Extension that guarantees the conduction of the nervous impulse. Each neuron has only one axon. Around the axon is an electrical insulation called myelin sheath. The sites where this sheath fails are called Ranvier's nodules.
- **Cellular Body:** Place where the core is. Most of the cellular organelles are also located in the cellular body. In addition, it is from where the extensions of this cell originate.

The neuron collects signals from Dendrites, and the Soma cells sums up all the signals collected, and when the summation reaches the threshold the signal pass through the axon to the other neurons.

#### Artificial Neurons:


## ML and Data Mining (DM)
Both are rooted in Data Science. The limits between the two concepts are often blurred, but there are a few differences.

DM is a process for extracting useful information from a large amount of data. It is used to discover new, reliable and useful patterns in the data, to find meaning and information relevant to the company or to the person who needs it. It is used by humans.

- ML and DM are both **analytics processes**.
- ML is sometimes used as a means for carrying out useful DM activities.
- Both aim to learn from data in order to improve decision-making.
- DM is designed to extract rules from a large amount of data, while ML teaches a computer how to learn and understand information to perform complex tasks.
- DM relies on human intervention and is ultimately designed for human use. Whereas ML teaches itself and not depends on human influence or actions.
- DM cannot learn or adapt as it follows pre-set rules and is static by nature, while ML adjusts algorithms as circumstances occur.
- Data mining is used on an existing dataset to discover patterns. Machine learning, on the other hand, is trained on a training data set, which teaches the computer how to make sense of the data, and then makes predictions about new data sets.


## Data Evaluation
On this field there is also a confussing lexicon that will be explained:

### Data Evaluation Metrics:
- **Confusion Matrix:** It is a table with four different combinations of predicted and actual values.
- **Accuracy:** Measures the ability of the model to capture true positive as positive and true negative as negative. It can be a useful measure if there is the same number of samples per class, but if, on the contrary, the set of samples is unbalanced, the accuracy is not an adequate measure.
- **Classification Error:** Measures the number of instances incorrectly classified by the model, that is, the number of False Positives, also known as Type I error, and the number of False Negatives, also known as Type II error.
- **Precision:** Measures the accuracy of the model against the predicted positives and determines how many of them are actually positive. Precision is a good measure if the cost of False Positives is high (e.g.: SPAM detection).
- **Sensitivity:** Also called Recall or True Positive Rate. It calculates how many of the true positives the model captures as being positive. Recall should be the metric to be use when there is a high cost associated with false negatives (e.g. medical diagnosis).
- **F1 score:** It is adequate when it is necessary to find a balance between Precision and Sensitivity and when there is an uneven distribution of the class.
- **Specificity or True Negative Rate:** Calculates how many of the true negatives the model captures as being negative. Consider the example of a medical examination to diagnose a disease, the Specificity relates to the ability of the test to correctly reject healthy patients. A test with a higher Specificity has a lower error rate of Type I.
- **Fall-out or False Positive Rate** Calculates how many false positives the model was unable to capture as being negative.
- **K statistic:** It is a measure of the reliability among evaluators and the discrepancy between them, taking into account the possibility that the agreement may occur by chance.
- **Receiver Operating Characteristic (ROC):** It is a probability curve, and Area Under the Curve (AUC) is a separability measure that informs the ability of the model to distinguish classes. The higher the AUC, the better the model predicts 0s as being 0s and 1s as being 1s.
