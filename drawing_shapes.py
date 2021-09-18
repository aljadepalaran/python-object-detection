import cv2
import numpy as np


image = np.zeros((512,512,3), 'uint8')
# print(image)
# image[:] = 255,255,0 # colour limit for whole images
cv2.line(image, (0,0), (image.shape[1], image.shape[0]), (0,255,255), 3)

cv2.rectangle(image, (0,0), (250,350), (255,0,255), 2)
# cv2.rectangle(image, (0,0), (250,350), (255,0,255), cv2.FILLED) # filled rectangle
cv2.circle(image, (400,50), 30, (255,255,0), 5)
cv2.putText(image, ' opencv ', (300,200),(cv2.FONT_HERSHEY_SIMPLEX),0.5,(0,150,0),1)

cv2.imshow('image', image)
cv2.waitKey(0)