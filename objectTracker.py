import cv2
import numpy as np

# tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']

# cv2.namedWindow("preview")
class ballTracker(object):
	# feeding a single frame into tracker
	def __init__(self, img):
		self.img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # image array
		self.orangeLower = np.array([0, 180, 220])
		self.orangeUpper = np.array([10, 220, 250])
		# print(self.img.shape)
		self.rows, self.cols, _ = self.img.shape

	# applying a gaussian blur
	def gaussianBlur(self):
		pass

	# isolate the color
	def filterImage(self):
		# for row in range(self.rows):
		# 	for col in range(self.cols):
		# 		if self.img[row][col] in self

		mask = cv2.inRange(self.img, self.orangeLower, self.orangeUpper)
		mask = cv2.resize(mask, (300, 300))
		# for i in range(self.rows):
		# 	for j in range(self.cols):
		# 		pixel = self.img[i][j]
		# 		# print(pixel)
		# 		if self.orangeLower[0]<pixel[0]<self.orangeUpper[0]\
		# 			and self.orangeLower[1]<pixel[1]<self.orangeUpper[1]\
		# 			and self.orangeLower[2]<pixel[2]<self.orangeUpper[2]:
		# 			self.img[i][j] = np.array([0, 0, 0])

		cv2.imshow("mask", mask)
		cv2.waitKey(0)

	def positionTracker(self):
		# returning the x, y coordinate of the object
		pass

img = cv2.imread("orangeBall.jpg")
img = cv2.resize(img, (300, 300))
# cv2.imshow("original", img)
tracker = ballTracker(img)
tracker.filterImage()