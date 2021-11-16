import tflite_runtime.interpreter as tflite

import pathlib
import numpy as np
#import matplotlib.pyplot as plt

from datetime import datetime
from pycoral.utils import edgetpu

######################################

# Load TFLite model and allocate tensors.
interpreter = edgetpu.make_interpreter("model_edge_edgetpu.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test the TensorFlow Lite model on random input data.
input_shape = input_details[0]['shape']
inputs, outputs = [], []
startTime = datetime.now()
for _ in range(100):
  input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
  interpreter.set_tensor(input_details[0]['index'], input_data)
  
  interpreter.invoke()
  tflite_results = interpreter.get_tensor(output_details[0]['index']) #tflite_results is the output data.
  
  inputs.append(input_data[0][0])
  outputs.append(tflite_results[0][0])

# Plot the results:
delta = datetime.now() - startTime
print("Execution Time:", '%.1f' % (delta.total_seconds() * 1000), "ms\n")
#plt.show(plt.plot(inputs, outputs, 'r'))
