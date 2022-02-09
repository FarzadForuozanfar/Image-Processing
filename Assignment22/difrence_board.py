import cv2

test=cv2.imread('test.bmp',0)
origin=cv2.imread('origin.bmp',0)

#The reflection of the image in this(Return the virtual image to the real one)
flip_test = cv2.flip(test,1)

result=cv2.subtract(flip_test,origin)
cv2.imwrite('board.jpg',result)