import cv2
import numpy as np

chess_arr = np.arange(0, 640000, 1, np.uint8)
chess_arr = np.reshape(chess_arr, (800, 800))
w,h = chess_arr.shape

for i in range(0,w,w//8):
    for j in range(0,h,h//8):
        if ((i+j)/4)%2==0:
            chess_arr[i:i+100,j:j+100]=0
        else:
            chess_arr[i:i+100,j:j+100]=255

cv2.imwrite("chessTable.jpg",chess_arr)
#cv2.imshow("output",chess_arr)
chess_img = cv2.resize(chess_arr,(400,400))
cv2.imshow("output",chess_img)
cv2.waitKey()

