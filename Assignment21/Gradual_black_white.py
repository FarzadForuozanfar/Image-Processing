import cv2
import numpy as np

img_b_w = np.arange(0, 65536, 1, np.uint8)
img_b_w = np.reshape(img_b_w, (256, 256))
w, h = img_b_w.shape

print(img_b_w)

for i in range(w):
    for j in range(h):
        img_b_w[i][j]= 255

print(img_b_w)

for i in range (w):
    if 256 - (i + 10) < 0:
        img_b_w[i , :] = 0
    else:
        img_b_w[i , :] =  256 - (i + 10)

print(img_b_w)
cv2.imshow('B & W',img_b_w)
cv2.waitKey()