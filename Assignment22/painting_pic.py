import cv2

mona_pic = cv2.imread("Mona_Lisa.jpg", 0)
invrted = 255 - mona_pic


blurred = cv2.GaussianBlur(invrted, (21,21), 0)
invrted_blurred = 255 - blurred
sketch = mona_pic / invrted_blurred
sketch *= 255
cv2.imwrite("result6.png", sketch)