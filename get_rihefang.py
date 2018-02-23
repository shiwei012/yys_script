# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
from PIL import ImageGrab
import time

deltaX = 945 - 485
deltaY = 224 - 196
threshold = 0.9
cwd = os.getcwd()
target = cwd + '/img/rihefang_target.png'
template = cv2.imread(target, 0)
# width, hight = template.shape[::-1]
tmpPicName = cwd + '/tmp.png'

def grabPic():
	im = ImageGrab.grab()
	im.save(tmpPicName, 'png')
	pass

def getLoccation(image, threshold):
	imgRgb = cv2.imread(image)
	imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
	loc = np.where(res >= threshold)
	return zip(*loc[::-1])

def mainFunc():
	while True:
		grabPic()
		loc = getLoccation(tmpPicName, threshold)
		if loc == None or len(loc) <= 0:
			time.sleep(1)
			continue
		else:
			clickX = loc[0] + deltaX
			clickY = loc[1] + deltaY
			print (clickX, clickY)
			break

mainFunc()


