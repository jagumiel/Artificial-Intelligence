#On this notebook I want to detect objects in movement. That's why I am using a video to do so.

import re
import cv2
import numpy as np
import tensorflow.lite as tflite

from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageFont


#Picking-up the model.
interpreter = tflite.Interpreter('4_Tflite-uint8IO-quantized.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# NxHxWxC, H:1, W:2
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]


vidcap = cv2.VideoCapture('video_nurbu.mp4')
success,rawImage = vidcap.read()
count=0

while success:
    #resize image
    #img = cv2.resize(rawImage,(320, 320))
    img = cv2.resize(rawImage,(width, height))
    input_data = np.expand_dims(img, axis=0)
    
    #Execute detection model
    interpreter.invoke()
    
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
    
    #Drawing those objects which are above the 0.5 threshold
    i = 0
    while  (scores[0][i]/255) > 0.5:
        (ymin, xmin, ymax, xmax) = boxes[0][i]
        (left, right, top, bottom) =(xmin/255, xmax/255, ymin/255, ymax/255)
        (left, right, top, bottom) =(left*320, right*320, top*320, bottom*320)
        #print(left, right, top, bottom)
        draw.line([(left,top),(left,bottom),(right,bottom),(right,top),(left,top)],
        width = 5, fill = 'red')
        i = i + 1
        #Anado el break porque si no me hace un outbounds.
        if i == 10:
            break
        
    
    cv2.imshow('Video Test', np.array(image, dtype = np.uint8))
    cv2.imwrite("frame%d.jpg" % count, np.array(image, dtype = np.uint8))     # save frame as JPEG file
    count += 1
    #Wait. Also exits when q key is pressed. Needed to show the video, DO NOT DELETE.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    #print("Number of objects found:","%d\n" % i)
    success,rawImage = vidcap.read()
    
    
vidcap.release()
cv2.destroyAllWindows()