import cv2
import numpy as np

image = cv2.imread('resources/lambo.jpg')
print(image.shape)

image_resized = cv2.resize(image, (600,400))

image_cropped = image_resized[0:200, 200:500]

cv2.imshow('image', image_resized)
cv2.imshow('image_c',image_cropped)
cv2.waitKey(0)