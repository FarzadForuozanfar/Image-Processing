from operator import imul
from unittest import result
import cv2
import numpy as np

imgA = cv2.imread("a.tif")
imgB = cv2.imread("b.tif")

Result = imgB - imgA
cv2.imshow("out",Result)
cv2.waitKey()