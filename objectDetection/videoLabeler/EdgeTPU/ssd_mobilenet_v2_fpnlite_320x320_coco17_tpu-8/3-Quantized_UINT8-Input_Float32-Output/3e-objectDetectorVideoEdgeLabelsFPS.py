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

#Picking-up the model.
interpreter = edgetpu.make_interpreter('3e_Tflite-uint8I-float32O-quantized_edgetpu.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# NxHxWxC, H:1, W:2
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

vidcap = cv2.VideoCapture('video_nurbu.mp4')
success,rawImage = vidcap.read()
frameCounter=0
#count=0
while success:
    
    #Resize image (just in case it wasn't 320x320)
    img = cv2.resize(rawImage,(width, height))
    # add N dim
    input_data = np.expand_dims(img, axis=0)
    
    #Execute detection model
    interpreter.invoke()
    if(frameCounter==0):
        startTime=datetime.now()
    frameCounter+=1
    
    #load new image to input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)
    
    #get results
    output_data = interpreter.get_tensor(output_details[0]['index'])
    
    boxes = interpreter.get_tensor(output_details[0]['index'])
    classes = interpreter.get_tensor(output_details[1]['index'])
    scores = interpreter.get_tensor(output_details[2]['index'])
    num = interpreter.get_tensor(output_details[3]['index'])
    
    image = Image.fromarray(img)
    draw = ImageDraw.Draw(image)
    im_w, im_h = image.size
    
    i = 0
    while  (scores[0][i]) > 0.7:
        (ymin, xmin, ymax, xmax) = boxes[0][i]
        (left, right, top, bottom) =(xmin*im_w, xmax*im_w, ymin*im_h, ymax*im_h)
        draw.line([(left,top),(left,bottom),(right,bottom),(right,top),(left,top)],
        width = 5, fill = 'red')
        if (classes[0][i]<90):
            # Annotate image with label and confidence score
            display_str = labels[classes[0][i]+1] + ": " + str(round((scores[0][i])*100, 2)) + "%"
            #draw.text((ymin,xmin), display_str, font=ImageFont.truetype("arial.ttf", 20))
            draw.text((left,top), display_str)
        
        i = i + 1
        #Break needed to avoid outbounds error.
        if i == 10:
            break
    if(frameCounter==10):
        frameCounter=0
        deltaT=datetime.now()-startTime
        fps=1000/((deltaT.total_seconds()*1000)/10)
        print("Average FPS: ", '%.1f' % fps, "fps")
    cv2.imshow('Video Test', np.array(image, dtype = np.uint8))
#    cv2.imwrite("labelledResults/frame%d.jpg" % count, np.array(image, dtype = np.uint8))     # save frame as JPEG file
#    count += 1
    #Wait. Also exits when q key is pressed. Needed to show the video, DO NOT DELETE.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    #print("Number of objects found:","%d\n" % i)
    success,rawImage = vidcap.read()
    
    
vidcap.release()
cv2.destroyAllWindows()

print("Finished\n")
