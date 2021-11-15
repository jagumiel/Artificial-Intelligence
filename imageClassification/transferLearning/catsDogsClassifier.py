"""label_image for tflite."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pycoral.utils import edgetpu
import tflite_runtime.interpreter as tflite
import numpy as np

import pathlib
import glob
import os
import re

from PIL import Image
from pathlib import Path
from datetime import datetime


# Load TFLite model and allocate tensors.
#interpreter = edgetpu.make_interpreter('converted_model.tflite')
interpreter = edgetpu.make_interpreter('converted_model_edgetpu.tflite')
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details() #224x224x3
output_details = interpreter.get_output_details()


###### Prepare the image or the imageset.
folder = "mySquaredImgs" #(No resize needed. Already 224x224px)
files = glob.glob(folder+'/*.jpg')
labels = ['cat', 'dog']

#Results:
hit=0
miss=0
accumTime=0

for file in files:
    img = Image.open(file)
    # add N dim
    input_data = np.expand_dims(img, axis=0)
    #Input data must be float
    input_data = (2.0 / 255.0) * np.float32(input_data) - 1.0
    interpreter.set_tensor(input_details[0]['index'], input_data)


    interpreter.set_tensor(input_details[0]['index'], input_data)
    startTime = datetime.now()
    interpreter.invoke()
    delta = datetime.now() - startTime
    accumTime=accumTime+(delta.total_seconds() * 1000)

    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(output_data)
    
    myPath=os.path.splitext(file)[0]
    filename=Path(myPath).stem
    res = re.findall('([a-zA-Z ]*)\d*.*', filename)

    if(output_data[0][0]>output_data[0][1]):
        #print("Image is a "+res[0]+". AI says it's a cat. "+str(output_data[0][0]*100))
        if(res[0]=="cat"):
            hit=hit+1
        else:
            miss=miss+1
    else:
        #print("Image is a "+res[0]+". AI says it's a dog. "+str(output_data[0][1]*100))
        if(res[0]=="dog"):
            hit=hit+1
        else:
            miss=miss+1
            
print("Hits="+str(hit))
print("Misses="+str(miss))
print("Average time:", '%.1f' % (accumTime/46), "ms\n")