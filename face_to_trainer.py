import os
import cv2
import numpy as np
from PIL import Image


recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataSet'

def getImagesWithId(path):
	imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
	print (imagePaths)
	
getImagesWithId(path)