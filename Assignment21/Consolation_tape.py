import cv2


deceased_img = cv2.imread("safi.jpg", 0)

for i in range(155):
    for j in range(110-i,155-i):
        if(j>=0):
          deceased_img[i][j]=0

deceased_img = cv2.resize(deceased_img,(480,320))
cv2.imshow("output",deceased_img)
cv2.waitKey()