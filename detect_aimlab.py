import cv2
import math
aimlab_cascade = cv2.CascadeClassifier('resources/haarcascade_aimlab.xml')
image = cv2.imread('resources/sample.png')

image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', image_grey)
targets = aimlab_cascade.detectMultiScale(image_grey, 1.1, 4)

for (x, y, w, h) in targets:
    # cv2.rectangle(image, (x, y), (x + math.ceil(w*.75), y + math.ceil(h*.75)), (255, 0, 0), 1)
    cv2.circle(image, ((x+math.floor(w/2)),(y+math.floor(h/2))), math.floor(h/2), (255,255,0), 1)

cv2.imshow('result', image)
cv2.waitKey(0)

