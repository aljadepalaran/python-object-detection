import cv2
import numpy as np

image = cv2.imread('resources/four_kings.jpg')

width,height = 250,350
points = np.float32([[99,246],[265,243],[113,490],[280,485]])
points_two = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points, points_two)
image_output = cv2.warpPerspective(image, matrix, (width, height))

cv2.imshow('image', image)
cv2.imshow('output', image_output)
cv2.waitKey(0)