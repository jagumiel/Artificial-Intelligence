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
