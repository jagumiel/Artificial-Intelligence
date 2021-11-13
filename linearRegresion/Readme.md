# Linear Regression
## _Basic ML Example: One Neuron Network_

Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data. ... A linear regression line has an equation of the form Y = a + bX, where X is the explanatory variable and Y is the dependent variable.

## Folder Structure


    .
    ├── logs                                                            # EdgeTPU Compiler logs.
    ├── saved_model                                                     # Exported saved model. Raw model with chekpoints and protobuffer(.pb) file.
    │   ├── 1                                                           # First model. Not optimized for embedded devices.
	│   │	├── variables                                               # Checkpoints.
	│   │	└── saved_model.pb                                          # Protobuffer file. Needed for tflite conversion.
    │   └── 2                                                           # Second model. Optimized for embedded devices (with TPU/NPU hardware accelerators).
	│       ├── variables                                               # Checkpoints.
	│       └── saved_model.pb                                          # Protobuffer.
    ├── LinearRegressionExec.ipynb                                      # Executes the model. Select the model to run (non-optimized as default).
    ├── linearRegressionTFLite-modelGeneration(forEmbedded).ipynb       # Model generation and conversion TPU oriented.
    ├── linearRegressionTFLite-modelGeneration.ipynb                    # Model generation and conversion without optimizations.
    ├── model.tflite                                                    # Model without optimizations
    ├── model_edge.tflite                                               # Quantized model oriented for embedded devices.
    ├── model_edgetpu.tflite                                            # Model without optimizations compiled for EdgeTPU (Google Coral).
    ├── model_edge_edgetpu.tflite                                       # Quantized model compiled for EdgeTPU (Google Coral).
    └── README.md

## About the project

This is an example project to begin with Artificial Intelligence under TensorFlow 2 framework and for embedded orientation.
This example only has one neuron, is very small.

To calculate linear regression are far better ways than this. In fact, the optimization applied is worst for this example. While you should quantize other models to run them efficiently on an embedded device whith a HW accelerator (TPU or NPU), on this example doing this increase the execution time, and is explained bellow...

The non-optimized models run the whole inference in the CPU and there is only *one operation*, the _fully connected network_.
When optimized and compiled for Edge TPU there are 3 operations Quantize, Dequantize and the Fully Connected Network. The Fully Connected Network is mapped on the TPU (this is good) but there are 2 more operations that will run in the CPU and will add more instructions, increasing the execution time.