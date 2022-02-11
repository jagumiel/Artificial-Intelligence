# Image Classification

**Image classification** is the prediction of a specific class or label for something that is defined by a set of data points. Image classification is a subset of the classification problem, where an entire image is assigned a label. Perhaps a picture will be classified as a daytime or nighttime shot. Or, similarly, images of cars and motorcycles will be automatically placed into their own groups. There are numerous categories/classes, that a specific image can be classified.

Image classification is a fundamental problem in computer vision and serves as the foundation of multiple
tasks like object detection, image segmentation, object tracking, action recognition, and autonomous driving.
There are some very popular datasets in Image Classification that are used across research, industry, and
hackathons.

## Some use cases:
Image classification can be applied for the following proposes:
- Labeling an x-ray as cancer or not (binary classification).
- Given portrait photographs, assign them to the name of a person (multi-class classification).
- Identification of animal and plant species (multi-class classification).

## Image Classification Models
There are a lot of models for this subject. Here are some examples:
- Deep Neural Networks: Generally, the deep learning architecture for image classification includes convolutional layers, making it a convolutional neural network (CNN).
- Very Deep Convolutional Networks for Large-Scale Image Recognition(VGG-16): The model is sequential in nature and uses lots of filters. At each stage, small 3 * 3 filters are used to reduce the number of parameters.
- Inception: In simple terms, the Inception Module performs convolutions with different filter sizes on the input, performs Max Pooling, and concatenates the result for the next Inception module. The introduction of the 1 * 1 convolution operation drastically reduces the parameters.
- ResNet50: The principal motivation behind this model was to avoid poor accuracy as the model went on to become deeper. When you work with Gradient Descent, you would have come across the Vanishing Gradient issue. The ResNet model aimed to tackle this issue.
- EfficientNet: It was developed from Google and proposes a new Scaling method called Compound Scaling.

