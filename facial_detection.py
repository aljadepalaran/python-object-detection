import cv2
face_cascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
image = cv2.imread('resources/lena.png')

capture = cv2.VideoCapture(0)
capture.set(3, 640) # width
capture.set(4, 480) # height
capture.set(10, 100) # brightness
while True:
    success, image = capture.read()
    cv2.imshow('Video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image_grey, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('result', image)
    cv2.waitKey(1)

