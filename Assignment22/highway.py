import cv2
import numpy as np

test_img = cv2.imread("h0.jpg",0)
w, h = test_img.shape
image_without_cars = np.zeros((w, h), dtype='uint8')
for i in range(15):
    img = cv2.imread(f'h{i}.jpg', 0)
    image_without_cars += img // 15

cv2.imwrite('result4.jpg', image_without_cars)