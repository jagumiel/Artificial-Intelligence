# Object Detection

This folder contains different resources to execute Artificial Intelligence (AI) models on embedded systems, using Google's Edge TPU hardware accelerator.

## Directory Structure:
The directory is organized in the following manner:

    .
    ├── modelConverter              # Jupyter Notebook to convert trained models into TensorFlow Lite Models.
    ├── objectDetection             # Example algorithms to identify objects in images and videos.
    │   ├── photoLabeler            # Identifies and labels objects in photographs.
	│   │	├── ARM        	        # Independent projects adjusted to be run under the CPU.
	│   │	└── EdgeTPU             # Independent projects adjusted to be run under the Edge TPU.
    │   └── VideoLabeler            # Identifies and labels objects in photographs.
	│       ├── ARM        	        # Independent projects adjusted to be run under the CPU.
	│       └── EdgeTPU             # Independent projects adjusted to be run under the Edge TPU.
    ├── tflite-Models               # Collection of the used models in the algorithms.
    └── README.md

## Introduction
The focus of object detection is finding all objects of certain classes in an image. These detections are commonly represented with bounding boxes.

To identify a certain class of image and then detect and tabulate their appearance in an image or video, it is used image classification. For example detecting damages on an assembly line or identifying machinery that requires maintenance.

A detection pipeline contain the following steps:
- Preprocessing, region of interest extraction (ROI);
- Object classication, and verification.

In the preprocessing step, tasks such as exposure and gain adjustment, as well as camera calibration and image rectification, are usually performed.

## ML and DL approaches for Object Detection
Machine learning uses algorithmic models that allow the computer to teach itself about the context of visual data. The computer will “look” at the data and teach itself to tell one image from another, if enough data is provided through the model,. Algorithms allow the machine to learn by itself, rather than someone programming it to recognize an image.

A CNN aids a machine learning or deep learning model “look” by breaking images down into pixels that are given tags or labels. It uses the labels to perform convolutions (a mathematical operation on two functions to generate a third function) and do predictions about what it is “seeing.” The neural network runs convolutions and checks the accuracy of its predictions in a series of iterations until the predictions start to come true. Then, it is recognizing or seeing images similar to humans.

Convolutional Neural Networks (CNN) first recognize hard edges and simple shapes, then fills in information as it runs iterations of its predictions. It is used to understand single images. CNN have been applied to the object detection problem, resulting in increased performance.

The operations used in computer vision based on a Deep Learning perspective are:
- **Convolution:** is an operation in which a learnable kernel is “convolved” with the image.The kernel is slided across the image pixel by pixel, and an element-wise multiplication is performed between the kernel and the image at every pixel group.
- **Pooling:** is an operation to reduce the dimensions of an image by performing operations at a pixel level. The kernel slides across the image, and only one pixel from the corresponding pixel group is chosen for processing, reducing the image size. For example: Max Pooling, Average Pooling.
- **Non-Linear Activations:** introduce non-linearity to the neural network, as a result of enabling the stacking of multiple convolutions and pooling blocks to rise model depth.

## Target representation and localization algorithms
An image classification or image recognition model detect the probability of an object in an image. Object localization is about identifying the location of an object in the image. The algorithm will output the coordinates of the location of an object with respect to the image. The most common way to localize an object in an image is to represent its location with the help of bounding boxes. A bounding box use the following parameters:
- **bx, by:** coordinates of the center of the bounding box.
- **bw:** width of the bounding box w.r.t the image width.
- **bh:** height of the bounding box w.r.t the image height.

Image localization is a spin-off of regular CNN vision algorithms. In object localization, the algorithm predicts a set of 4 continuous numbers, that is x coordinate, y coordinate, height, and width, to draw a bounding box around an object of interest.

Initial layers are convolutional neural network layers ranging from a couple of layers to 100 layers, depending on the application, amount of data, and computational resources available. There are a pooling layer, after the CNN layers, then one or two fully connected layers. The last layer is the output layer that gives a probability of an object being present in an image. For example, an algorithm identifies 100 different objects, so the last layer gives an array length of 100 and values ranging from 0 to 1 that indicate the probability of an object being present in an image. In an image localization algorithm, everything is the same except the output layer.

Some algorithms for Localization:
- R-CNN (region-based CNN)
- Fast and Faster R-CNN (improved version of R-CNN)
- YOLO (highly efficient object detection framework)
- SSD (single shot detectors)

Thinking in images as functions mapping locations in images to pixel values, filters can be just systems that form a new, and preferably enhanced, image from a combination of the original image's pixel values.

Data association can be defined as the process of matching information about newly observed objects with information that was previously observed about them. This information may be about their identities, positions, or trajectories. 

Data association algorithms look for matches that optimize certain match criteria and are subject to physical conditions.

