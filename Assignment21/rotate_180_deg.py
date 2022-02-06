import cv2
import numpy as np

image = cv2.imread('3.jpg',0)
height, width = image.shape
rotate_img=np.zeros([height,width],dtype=np.uint8)

for i in range(height):
    for j in range(width):
        rotate_img[i][j]=image[height-i-1][width-j-1]

rotate_img = cv2.resize(rotate_img,(600,400))
cv2.imshow('output',rotate_img)
cv2.imwrite('3result.jpg',rotate_img)
cv2.waitKey()      