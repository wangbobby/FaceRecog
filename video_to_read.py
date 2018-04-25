import cv2
import numpy as np


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture("test.mp4")

if(capture.isOpened() == False):
	print "Error Ocurr.."
	
while(capture.isOpened()):
	ret, img = capture.read()
	if(ret == True):
		cv2.imshow("Face", img)
	if(cv2.waitKey(1) == ord('q')):
		break
	
capture.release()
cv2.destroyAllWindows()