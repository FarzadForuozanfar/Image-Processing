import cv2
import numpy as np
from sklearn.utils import resample

reza_img = cv2.imread("reza.jpg", 0)
messi_img = cv2.imread("messi.jpg", 0)

print(reza_img.shape, messi_img.shape)

w , h = reza_img.shape
print(h, w)

messi_img = cv2.resize(messi_img, (280,318))

result = np.zeros((w,5 * h), dtype='uint8')
print(result.shape)

test1 = reza_img // 2 + messi_img // 4
test2 = reza_img // 2 + messi_img // 2
test3 = reza_img // 4 + messi_img // 2
#final_photo[0:1000, 0:1000] = photoes_without_noise[0]
result[0:318, 0:280] = reza_img
result[0:318, 280:560] = test1
result[0:318, 560:840] = test2
result[0:318, 840:1120] = test3
result[0:318, 1120:1400] = messi_img
cv2.imshow('final_image.jpg', result)
cv2.waitKey()

