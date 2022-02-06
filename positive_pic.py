import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img_pos1 = 255 - img1
img_pos2 = 255 - img2

img_pos2 = cv2.resize(img_pos2,(400,400))
img_pos1 = cv2.resize(img_pos1,(400,400))
cv2.imshow('negative',img_pos1)
cv2.imshow('negative',img_pos2)
cv2.waitKey(0)