import cv2
import numpy as np

img=np.ones([256,200])
height,width=img.shape

print(height,width)

img[45:210,25:50]=0
img[45:65,50:115]=0
img[100:117,50:115]=0
cv2.imshow('output',img)
cv2.imwrite('result_7.jpg',255*img)
cv2.waitKey()