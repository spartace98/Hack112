# color calibration
import cv2

class colorCalibration(object):
	def __init__(self, img):
		self.img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		self.rows, self.cols, _ = self.img.shape

	def returnBounds(self):
		# crop to half the image

		red = []
		green = []
		blue = []
		for row in range(int(self.rows*0.25), int(self.rows*0.75)):
			for col in range(int(self.cols*0.25), int(self.cols*0.75)):
				pixel = self.img[row][col]
				red.append(pixel[2])
				green.append(pixel[1])
				blue.append(pixel[0])
		r1 = min(red)
		g1 = min(green)
		b1 = min(blue)
		r2 = max(red)
		g2 = max(green)
		b2 = max(blue)
		return [b1, g1, r1], [b2, g2, r2]

	def average(self, L):
		length = len(L)
		return sum(L) // length


cam = cv2.VideoCapture(0)
ret,img = cam.read()
calibration = colorCalibration(img)
print(calibration.returnBounds())


