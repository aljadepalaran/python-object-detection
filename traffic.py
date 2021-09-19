import cv2
import cv2
import math, time
import numpy as np
import win32api, win32con
from PIL import ImageGrab

car_cascade = cv2.CascadeClassifier('resources/haarcascade_cars.xml')

def empty(a):
    pass

while True:

    image = ImageGrab.grab()
    image = np.array(image)
    grey_frame = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cars = car_cascade.detectMultiScale(grey_frame, 10, 4)

    for (x, y, w, h) in cars:
        cv2.rectangle(grey_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(grey_frame, 'car ', (x, y), (cv2.FONT_HERSHEY_SIMPLEX), 0.5, (0, 150, 0), 2)

    cv2.imshow('result', grey_frame)
    cv2.waitKey(1)

