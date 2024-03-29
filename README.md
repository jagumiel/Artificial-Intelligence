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
- **Computer Vision (CV):** Computer Vision is a branch of computer science that specializes in developing digital systems that can process, analyze and make sense of images or videos in a similar way to human beings. The conception of computer vision is based on the instruction of computers to process an image at a pixel level as well as understand it.
- **Data Science:**
- **Big Data:**



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


## From Biology to Computing: Understanding human neurons to comprehend Neural Networks in computing.

A neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a **process that mimics the way the human brain operates**. In this sense, neural networks refer to systems of neurons, either organic or artificial in nature.

Neural networks can adapt to changing input; so the network generates the best possible result without needing to redesign the output criteria.

### Biologic Neurons:
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

### Artificial Neurons:
The artificial neuron is a simplified and simulated model of the real neuron as well as its basic characteristics.

Neural networks, which consist of artificial neurons, have an excellent behavior for helping people with complex day-to-day problems. They are able to:
- Learn and model the relationships between inputs and outputs that are non-linear and complex
- Model highly volatile data and variances needed to predict rare events.
- Reveal hidden relationships, patterns and predictions.

In the Neural Network, the neurons are arranged into multiple layers:
- **Input Layer:** This layer accepts input features. It provides information from the outside world to the network, no computation is performed at this layer, nodes here just pass on the information(features) to the hidden layer.
- **Hidden Layer:** Nodes of this layer are not exposed to the outer world, they are the part of the abstraction provided by any neural network. Hidden layer performs all sort of computation on the features entered through the input layer and transfer the result to the output layer.
- **Output Layer:** This layer bring up the information learned by the network to the outer world.

### Biologcal vs. Artificial Neurons:
**Similarities:**
- Use electrical signals to send messages.
- They have a memory that can grow.
- Able to adapt and learn.
- Need energy
- Can do math and other logical task.
- Can change and be modified.
- Transmit information.

**Differences:**
- **Size:** The human brain contains about 86 billion neurons and more than a 100 trillion synapses (connections). The number of “neurons” in artificial networks is much less than that.
- **Speed:** Biological neurons can fire about 200 times a second on average. Signals travel at different speeds depending on the type of the nerve impulse, ranging from 0.61 m/s up to 119 m/s.
- **Power consumption:** The human brain consumes about 20% of all the human body’s energy. Our machines are way less efficient than biological systems.
- **Topology:** All artificial layers compute one by one, instead of being part of a network that has nodes computing asynchronously.
- **Fault-tolerance:** Biological neuron networks due to their topology are also fault-tolerant. Information is stored redundantly so minor failures will not result in memory loss. They don’t have one “central” part.
- **Learning:** We still do not understand how brains learn, or how redundant connections store and recall information.

### Activation Functions
Activation functions are mathematical equations that determine the output of a neural network.
The function is attached to each neuron in the network, and determines whether it should be activated (“fired”) or not.
Activation functions also help normalize the output of each neuron to a range between 1 and 0 or between -1 and 1.

The Activation Functions can be basically divided into 2 types:
1. Linear Activation Functions
2. Non-linear Activation Functions

## About Computer Vision (CV)
CV works in three basic steps:
1. **Image Acquisition.** Images can be acquired in real-time through videos, photos or 3D technologies.
2. **Image Processing.** Use of Deep learning models or training models.
3. **Image Understanding.** Interpretation, identification or classification of an object.

### In which fields id CV useful?
- **Safety:** In automotive, CV enables ADAS and self-driving cars to make sense of their surroundings.
- **Health:** CV can automate tasks such as detecting cancer.
- **Security:** Plays an important role in facial recognition.
- **Entertainment:** Big role in augmentes and mixed reality.
- **Confort/home automation:** Enables the digital world to interact with the physical world.

### Some tasks we can achieve with CV
- Image Classification.
  - Objective: Categorize a entire image into a class such as “people”, “animals”, “outdoors”.
  - Input: An image with a single object (example: a photograph).
  - Output: A class label (exemple: one or more integers that are mapped to class labels).
- Object Location.
  - Objective: Locate the presence of objects in an image and indicate their location with a bounding box.
  - Input: An image with one or more objects, such as a photograph.
  - Output: One or more bounding boxes (e.g. defined by a point, width, and height).
- Object Detection.
  - Objective: Locate the presence of objects with a bounding box and predict types or classes of the located objects in an image.
  - Input: An image with one or more objects, such as a photograph.
  - Output: One or more bounding boxes (e.g. defined by a point, width, and height) and a class label for each bounding box. 
- Segmentation.
  - Objective: Identify parts of the image and understanding what object they belong to.
  - It is again divided into the following categories:
      1. Semantic segmentation.
      2. Instance segmentation.
      3. Panoptic segmentation.
- Key Point Detection.
  - Involves detecting people and localizing their key points simultaneously.
  - Keypoints are spatial locations or points in the image that define what is interesting or what stands out in the image. They are invariant to image rotation, shrinkage, translation, distortion, and so on.

### How CV fits into AI?
AI can be complemented by CV. For example, if we are running a face recognition inference, we don't need the body. We just need the cropped face to apply the algorithm over that region of the image to identify the subject. Here is explained in more detail:

**Image segmentation** partitions an image into multiple regions or pieces to be examined separately.
**Facial recognition** is an advanced type of object detection that recognizes a human face in an image and identifies a specific individual.
**Edge detection** is a technique used to identify the outside edge of an object or landscape to better identify what is in the image.
**Object detection** identifies a specific object in an image. Advanced object detection recognizes many objects in a single image. These models use an X,Y coordinate to create a bounding box and identify everything inside the box.


## TensorFlow
This **repository is strongly oriented to TensorFlow 2** Framework, particularly to TensorFlow Lite, to implement the models on embedded devices. Let's take a brief introduction to it!

TensorFlow is a free open-source platform with a variety of tools, libraries and resources for Artificial Intelligence and Machine-learning which includes Computer Vision.

It can be used to build and train Machine Learning models related to computer vision that include facial recognition, object identification, etc.

TensorFlow supports Python, C, C++, Java, JavaScript, Go, Swift, and others, without an API backward compatibility guarantee. There are also third-party packages for languages like MATLAB, C#, Julia, Scala, R, Rust, etc.

TensorFlow provides multiple APIs (Application Programming Interfaces) that can be classified into 2 major categories:
- Low level API:
  - Complete programming control
  - Recommended for machine learning researchers
  - Provides fine levels of control over the models
  - **TensorFlow Core** is the low level API of TensorFlow.
- High level API:
  - Built on top of **TensorFlow Core**
  - Easier to learn and use than **TensorFlow Core**
  - Make repetitive tasks easier and more consistent between different users
  - **tf.contrib.learn** is an example of a high level API.


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
