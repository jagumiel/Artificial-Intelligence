"""label_image for tflite."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pycoral.utils import edgetpu

import argparse
import numpy as np
import re
import glob
import cv2
#import tensorflow.lite as tflite
import tflite_runtime.interpreter as tflite

from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor


#Function to load the labels
def load_labels(path):
    """Loads the labels file. Supports files with or without index numbers."""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        labels = {}
        
        #for row_number, content in enumerate(lines):
        for x in range(3,455,5):
            pair = re.split(r'\s+', lines[x-1], maxsplit=3)
            row_number = int(pair[2].strip())
            pair = re.split(r'\"(.+?)\"', lines[x], maxsplit=1)
            labels[row_number] = pair[1].strip()
    return labels

#Load the labels
labels = load_labels('mscoco_complete_label_map_full.pbtxt')

interpreter = edgetpu.make_interpreter('3e_Tflite-uint8I-float32O-quantized_edgetpu.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# check the type of the input and output tensors
floating_modelI = input_details[0]['dtype'] == np.uint8
floating_modelO = output_details[0]['dtype'] == np.uint8
#Result: Yes. Input and output are both uint8.


# NxHxWxC, H:1, W:2
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]
img = Image.open('imgSource/out7.jpeg').resize((height,width ))

# add N dim
input_data = np.expand_dims(img, axis=0)
#Test if the array has the expected dimmensions (1, 320, 320, 3)
print(input_data.shape)

#input_data = (2.0 / 255.0) * np.float32(input_data) - 1.0
interpreter.set_tensor(input_details[0]['index'], input_data)

# ignore the 1st invoke
startTime = datetime.now()
interpreter.invoke()
delta = datetime.now() - startTime
print("Warm-up time:", '%.1f' % (delta.total_seconds() * 1000), "ms\n")


folder = "imgSource"
files = glob.glob(folder+'/*.jpeg')
numFoto=1
startTimeFullExecution=datetime.now()
for file in files:
  img = Image.open(file).resize((height,width ))
  input_data = np.expand_dims(img, axis=0)
  interpreter.set_tensor(input_details[0]['index'], input_data)
  
  startTime = datetime.now()
  interpreter.invoke()
  delta = datetime.now() - startTime
  print("Inference time:", '%.1f' % (delta.total_seconds() * 1000), "ms\n")
  
  output_data = interpreter.get_tensor(output_details[0]['index'])
  
  boxes = interpreter.get_tensor(output_details[0]['index'])
  classes = interpreter.get_tensor(output_details[1]['index'])
  scores = interpreter.get_tensor(output_details[2]['index'])
  num = interpreter.get_tensor(output_details[3]['index'])
  
  draw = ImageDraw.Draw(img)
  im_w, im_h = img.size
  
  numObj=0
  i = 0
  while  (scores[0][i]) > 0.5:
    numObj+=1
    
    (ymin, xmin, ymax, xmax) = boxes[0][i]
    (left, right, top, bottom) =(xmin*im_w, xmax*im_w, ymin*im_h, ymax*im_h)
    draw.line([(left,top),(left,bottom),(right,bottom),(right,top),(left,top)],
    width = 5, fill = 'red')
    if (classes[0][i]<91):
      # Annotate image with label and confidence score
      display_str = labels[classes[0][i]+1] + ": " + str(round((scores[0][i])*100, 2)) + "%"
      #draw.text((ymin,xmin), display_str, font=ImageFont.truetype("arial.ttf", 20))
      draw.text((left,top), display_str)
    print(scores[0][i])
    i = i + 1
    #Anado el break porque si no me hace un outbounds.
    if i == 10:
      break
    
    print("Number of objects found:","%d\n" % numObj)
  img.show()
  img.save("labeledResults/out"+str(numFoto)+"-labeled.jpeg","JPEG")
  numFoto+=1

deltaFullExecution = datetime.now() - startTimeFullExecution
print("Elapsed time:", '%.1f' % (deltaFullExecution.total_seconds() * 1000), "ms\n")
print("Average time:", '%.1f' % ((deltaFullExecution.total_seconds() * 1000)/numFoto), "ms\n")

print("Finished\n")
