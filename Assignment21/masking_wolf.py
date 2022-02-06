import cv2
import numpy as np

img_wolf = cv2.imread("4.jpg", 0)
w , h = img_wolf.shape
print(img_wolf)
for i in range(w):
    for j in range(h):
        if 100 > img_wolf[i][j]:
            img_wolf[i][j] = 0

img_wolf = cv2.resize(img_wolf,(600,400))
print(img_wolf)
cv2.imshow('wolf',img_wolf)
cv2.waitKey()