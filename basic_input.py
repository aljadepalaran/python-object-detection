import cv2

# image capture
# image = cv2.imread('resources/lena.png')
# cv2.imshow('Output', image)
# cv2.waitKey(0)

# video capture
# capture = cv2.VideoCapture('resources/video.mp4')
# while True:
#     success, image = capture.read()
#     cv2.imshow('Video', image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# web cam capture
# capture = cv2.VideoCapture(0)
# capture.set(3, 640) # width
# capture.set(4, 480) # height
# capture.set(10, 100) # brightness
# while True:
#     success, image = capture.read()
#     cv2.imshow('Video', image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break