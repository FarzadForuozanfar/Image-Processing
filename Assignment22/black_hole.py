import cv2
import numpy as np

photoes = ([[0 for i in range(5)] for j in range(4)])
for i in range(4):
   for j in range(5):
      photoes[i][j] = cv2.imread(f"{i+1}/{j+1}.jpg" , 0)

photoes_without_noise = [0 for i in range(4)]

for i in range(4):
    for j in range(5):
        photoes_without_noise[i] += (photoes[i][j] // 5)

final_photo = np.zeros((2000, 2000), dtype=np.uint8)
print(len(photoes_without_noise))
final_photo[0:1000, 0:1000] = photoes_without_noise[0]
final_photo[0:1000, 1000:2000] = photoes_without_noise[1]
final_photo[1000:2000, 0:1000] = photoes_without_noise[2]
final_photo[1000:2000, 1000:2000] = photoes_without_noise[3]
final_photo =  cv2.resize(final_photo, (500,500))
cv2.imshow('final_image.jpg', final_photo)
cv2.waitKey()

