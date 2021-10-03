import cv2
import numpy as np

kernel = np.ones((5,5), 'uint8')

image = cv2.imread('resources/cabal_map.PNG')

image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to greyscale
image_blur = cv2.GaussianBlur(image_greyscale, (7, 7), 0) # blurs the image
image_canny = cv2.Canny(image, 100, 100) # gets edges on the image higher = less edges
image_dialation = cv2.dilate(image_canny, kernel, iterations=1) # fills edges
image_eroded = cv2.erode(image_dialation, kernel, iterations=1)

# cv2.imshow('Normal', image)
# cv2.imshow('Blurred', image_blur)
# cv2.imshow('Canny', image_canny)
# cv2.imshow('Dialated Image', image_dialation)
cv2.imshow('Eroded Image', image_eroded)

cv2.waitKey(0)