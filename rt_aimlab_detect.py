import cv2
import math, time
import numpy as np
import win32api, win32con
from PIL import ImageGrab

aimlab_cascade = cv2.CascadeClassifier('resources/haarcascade_aimlab.xml')
crosshair_cascade = cv2.CascadeClassifier('resources/haarcascade_crosshair.xml')

while True:
    # Take screenshot
    image = ImageGrab.grab()
    image = np.array(image)
    grey_frame = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    targets = aimlab_cascade.detectMultiScale(grey_frame, 1.1, 4)

    for (x, y, w, h) in targets:

        cv2.circle(image, ((x + math.floor(w / 2)), (y + math.floor(h / 2))), math.floor(h / 2), (255, 255, 0), 1)

        roi_grey = grey_frame[y:y+h, x:x+w]
        roi_colour = image[y:y+h, x:x+w]

        crosshairs = crosshair_cascade.detectMultiScale(roi_grey, 1.1, 4)

        for (cx, cy, cw, ch) in crosshairs:

            cv2.circle(roi_colour, ((cx + math.floor(cw / 2)), (cy + math.floor(ch / 2))), math.floor(ch / 2), (255, 255, 0), 1)

    cv2.imshow("Screen", image)
    cv2.waitKey(1)

cv2.waitKey(0)

