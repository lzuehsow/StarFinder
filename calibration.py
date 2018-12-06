#!/usr/bin/env python
import cv2
import glob
import numpy as np
import os
from PIL import Image

class Calibration(object):
	def __init__(self):
		# termination criteria
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

		# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
		objp = np.zeros((6*7,3), np.float32)
		objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

		# Arrays to store object points and image points from all the images.
		objpoints = [] # 3d point in real world space
		imgpoints = [] # 2d points in image plane.

		# images = glob.glob('*.jpg')

		image = np.array(Image.open("photo.jpg").convert('RGBA'))
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		ret, corners = cv2.findChessboardCorners(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY), (7,6), None)
		if ret is True:
			print "Hoi"
			objpoints.append(objp)

			corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
			imgpoints.append(corners2)

			# Draw and display the corners
			img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
			cv2.imshow('img',img)
			cv2.waitKey(1)
		cv2.destroyAllWindows()

if __name__ == '__main__':
	cal = Calibration()