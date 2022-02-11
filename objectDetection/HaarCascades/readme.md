# Facial Recognition

## Introduction
Facial Recognition is a subpart of object detection where the primary object being detected is the human face.

Features are detected and localized as in object detection, but facial recognition not only performs detection as also recognition of the detected face. The system search for usual features and landmarks in faces like nose, eyes, and mouth and classify with the help of these features and the positioning of these landmarks.

Traditional Image Processing based methods for facial recognition include **Haar Cascades** easily accessible via the OpenCV library while more robust methods including the use of Deep Learning based algorithms are found in works like FaceNet.

Face Recognition Applications:
- Automated surveillance
- Monitoring closed circuit television
- Image database investigations
- Multimedia environments with adaptive human computer interfaces
- Airplane‐boarding gate
- Sketch‐based face reconstruction
- Forensic applications
- Face spoofing and anti‐spoofing, where a photograph or video of an authorised person's face could be used to gain access to services

## About OpenCV
**Haar Cascades** are part of the OpenCV library but... What is OpenCV?

Open CV is a open source library that contains different functions for computer vision and machine learning. 

It has different algorithms that perform different tasks like:
- Facial detection and recognition
- Object identification, monitoring moving objects
- Tracking camera movements and eye movements
- Extracting 3D models of objects
- Creating an augmented reality overlay with a scenery
- Recognizing similar images in an image database
- Etc.

It also has the following functionalities:
- Image/video I/O, processing, display (core, imgproc, highgui)
- Object/feature detection (objdetect, features2d, nonfree)
- Geometry-based monocular or stereo computer vision (calib3d, stitching, videostab)
- Computational photography (photo, video, superres)
-  Machine learning & clustering (ml, flann)
-  CUDA acceleration (gpu)

OpenCV supports various operating systems such as Windows, Android, Mac OS and Linux. Has interfaces for C++, Java, Python, MATLAB and others.

Image processing includes three steps:
- Importing the image.
- Analysing and manipulating the image.
- Output in which result can be altered image or report that is based on image analysis.
