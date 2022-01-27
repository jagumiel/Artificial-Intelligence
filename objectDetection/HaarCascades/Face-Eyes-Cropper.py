import cv2

FACE_DETECT= "data/haarcascades/haarcascade_frontalface_default.xml"
EYE_DETECT = "data/haarcascades/haarcascade_eye.xml"

webcam = cv2.VideoCapture('/dev/video1')
face_classifier = cv2.CascadeClassifier(FACE_DETECT)
eye_classifier = cv2.CascadeClassifier(EYE_DETECT)

if webcam.isOpened(): # try to get the first frame
    rval, frame = webcam.read()
else:
    print("Video input not detected. Exiting...")
    rval = False

while rval:
    faces = face_classifier.detectMultiScale(frame)
    i=0 # Index to display more than one detection if needed.
    for(fx, fy, fw, fh) in faces:
        cv2.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255),3)
        sub_face = frame[fy:fy+fh, fx:fx+fw]
        # Displays the cropped image of the face. Can show more than one face.
        cv2.imshow('Face %d' %i, sub_face)
        eyes = eye_classifier.detectMultiScale(sub_face)
        i=i+1
        j=0 # Index to display all the detected eyes. May display bad detections.
        for (ex,ey, ew, eh) in eyes:
            cv2.rectangle(frame, (fx+ex,fy+ey), ((fx+ex+ew), (fy+ey+eh)), (0, 255, 0), 2)
            myEyes=sub_face[ey:ey+eh, ex:ex+ew]
            cv2.imshow('Eye %d' %j, myEyes) # Index to see both eyes and glitches/artifacts.
            j=j+1
    
    cv2.imshow("Camera", frame) # Shows the whole frame with rectangles.
    rval, frame = webcam.read()

    key = cv2.waitKey(20)
    if key in [27, ord('Q'), ord('q')]: # exit on ESC
        break