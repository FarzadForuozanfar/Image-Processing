import cv2
import numpy as np
import random

img = cv2.imread("chess pieces.jpg", 0)
print(img.shape)

h , w = img.shape
B_W = [30,180]

result = np.zeros((h, w * 2), dtype="uint8")
print(result.shape)

noise_img = img

for i in range(h // 3):
    for j in range(w // 2):
        x = random.randint(0, h-1)
        y = random.randint(0, w-1)
        color = random.choice(B_W)
        noise_img[x][y] = color

img = cv2.imread("chess pieces.jpg", 0)
result[0:276 , 0:600] = img
result[0:276 , 600:1200] = noise_img
cv2.imshow("noise image",result)
cv2.waitKey()

