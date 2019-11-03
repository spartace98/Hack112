import cv2
import numpy as np


# initialising the camera
cam = cv2.VideoCapture(0)
cv2.namedWindow("preview")

while(True):
    ret, frame = cam.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # INITIALISING APRIL TAG DETECTOR
    ATD = AprilTagDetector(frame)
    corners = ATD.getCorners()
    print(corners)

    # IF THE CORNERS CAN BE DETECTED
    if corners != None:
      angles = ATD.getAngles()
      print(angles[0][2])
      if abs(angles[0][2]) > 45:
        shoot = True
      else:
        shoot = False
      # initialise the draw corners function
      img_corners = DrawCorners(corners, frame).drawCorners()
      cv2.imshow('frame',img_corners)

    # IF NO CORNERS ARE DETECTED
    else:
      shoot = False
      cv2.imshow('frame', frame)

    print(shoot)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break