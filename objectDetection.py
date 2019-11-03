import cv2
import numpy as np
from objectTracker import ballTracker

# initialising the camera
cam = cv2.VideoCapture(0)
# cv2.namedWindow("preview")

while(True):
    ret, frame = cam.read()
    frame = cv2.resize(frame, (200, 200))
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # INITIALISING APRIL TAG DETECTOR
    tracker = ballTracker(frame)
    # detecting position of ball
    pos = tracker.positionTracker()
    # IF THE BALL CAN BE DETECTED
    if pos != None:
        img = tracker.draw(frame, pos)
        cv2.imshow('frame', img)
        print(pos)

    # IF NO CORNERS ARE DETECTED
    else:
        cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break