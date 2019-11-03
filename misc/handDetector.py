# hand gestures detection
# need to first determine the lower and upperbound for the hand pixels
# do a precalibration based on the environment
from keras.models import load_model
import numpy as np
import cv2

class HandDetection(object):
	def __init__(self, img, lowerBound, upperBound):
		self.img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		self.handLower = np.array(lowerBound)
		self.handUpper = np.array(upperBound)
		self.rows, self.cols, _ = self.img.shape
		self.model = load_model("VGG_cross_validated.h5")

	# applying a gaussian blur
	def gaussianBlur(self):
		blurred_img = cv2.GaussianBlur(self.img, (15, 15), 0)
		return blurred_img

	def predictGesture(self):
		# predict the gesture here
		blurred_img = self.gaussianBlur()
		return blurred_img

	# isolate the color
	def filterImage(self):
		blurred_img = self.gaussianBlur()
		mask = cv2.inRange(blurred_img, self.orangeLower, self.orangeUpper)
		return mask

	def predict(self):
		pass

path = "hand.jpg"
img = cv2.imread(path)
cv2.imshow("image", img)
cv2.waitKey(0)
HandDetection(img, [40, 50, 80], [100, 100, 100])


