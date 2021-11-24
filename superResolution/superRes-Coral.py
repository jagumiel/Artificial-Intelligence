"""label_image for tflite."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from pycoral.utils import edgetpu

import re
import cv2
import argparse
import numpy as np
import tflite_runtime.interpreter as tflite

from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageFont
from datetime import datetime


#Picking-up the model.
#interpreter = edgetpu.make_interpreter('4e_Tflite-uint8IO-quantized_edgetpu-noFPN.tflite')
interpreter = edgetpu.make_interpreter('ESRGAN_quant_edgetpu.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# NxHxWxC, H:1, W:2
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

vidcap = cv2.VideoCapture('/dev/video1')
success,rawImage = vidcap.read()



while success:
    
    #Resize image and adjust color (just in case it wasn't 320x320)
    img = cv2.resize(rawImage,(width, height))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # add N dim
    img = img[np.newaxis, :, :, :]
    # Cast image to Float32
    img = img.astype(np.float32)

    #Execute detection model
    interpreter.invoke()
    
    #load new image to input tensor
    interpreter.set_tensor(input_details[0]['index'], img)
    
    #get results
    output_data = interpreter.get_tensor(output_details[0]['index'])
    output_data = interpreter.get_tensor(output_details[0]['index'])
    sr_im = np.squeeze(output_data, axis=0)
    sr_im = np.clip(sr_im, 0, 255)
    sr_im = np.round(sr_im)
    sr_im = sr_im.astype(np.uint8)
    sr_im = cv2.cvtColor(sr_im, cv2.COLOR_RGB2BGR)
    
    cv2.imshow('Video Test', np.array(sr_im, dtype = np.uint8))
    
    #Wait. Also exits when q key is pressed. Needed to show the video, DO NOT DELETE.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    success,rawImage = vidcap.read()
    
    
vidcap.release()
cv2.destroyAllWindows()

print("Finished\n")