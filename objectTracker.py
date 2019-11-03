import cv2
import numpy as np

# tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']

# cv2.namedWindow("preview")
class ballTracker(object):
	# feeding a single frame into tracker
	def __init__(self, img):
		self.img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # image array
		self.orangeLower = np.array([0, 0, 0])
		self.orangeUpper = np.array([40, 40, 40])
		# cv2.imshow("filter", self.img)
		# cv2.waitKey(0)
		# print(self.img.shape)
		self.rows, self.cols, _ = self.img.shape

	# applying a gaussian blur
	def gaussianBlur(self):
		blurred_img = cv2.GaussianBlur(self.img, (15, 15), 0)
		return blurred_img

	# isolate the color
	def filterImage(self):
		blurred_img = self.gaussianBlur()
		mask = cv2.inRange(blurred_img, self.orangeLower, self.orangeUpper)
		return mask

	def positionTracker(self):
		# returning the x, y coordinate of the object
		Xvals = []
		Yvals = []
		mask = self.filterImage()

		for row in range(self.rows):
			for col in range(self.cols):
				pixel = mask[row][col]
				if pixel != 0:
					Xvals.append(col)
					Yvals.append(row)
		# if there are no orange ball found
		if Xvals == [] or Yvals == []:
			return None
		else:
			x0, x1 = min(Xvals), max(Xvals)
			y0, y1 = min(Yvals), max(Yvals)
			return x0, y0, x1, y1

	# drawing the corners on the image provided
	# so that it wont be drawing on the filtered image
	def draw(self, img, corners):
		x0, y0, x1, y1 = corners
		c1 = (x0, y0)
		c2 = (x1, y0)
		c3 = (x1, y1)
		c4 = (x0, y1)
		cv2.line(img, c1, c2, (0,255,0), 10)
		cv2.line(img, c2, c3, (0,255,0), 10)
		cv2.line(img, c3, c4, (0,255,0), 10)
		cv2.line(img, c4, c1, (0,255,0), 10)
		# img = cv2.resize(img, (300, 300))
		# cv2.imshow("original", img)
		# cv2.waitKey(10)
		posX, posY = (x0+x1)//2, (y0+y1)//2
		return img

# img = cv2.imread("orangeBall.jpg")
# # img = cv2.resize(img, (300, 300))
# # cv2.imshow("original", img)
# tracker = ballTracker(img)
# corners = tracker.positionTracker()
# print(corners)
# img = tracker.draw(img, corners)



