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

