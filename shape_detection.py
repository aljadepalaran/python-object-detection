import cv2
import numpy as np

def stackImages(imgArray,scale,lables=[]):
    sizeW= imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver

def getContours(image):
    contours, hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 500:
            cv2.drawContours(image_contour, contour, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02*peri, True)
            object_corners = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if object_corners == 3: object_type = 'Triangle'
            elif object_corners == 4:
                aspect_ratio = w/float(h)
                if aspect_ratio > 0.95 and aspect_ratio < 1.05: object_type = 'Square'
                else: object_type = 'Rectangle'
            elif object_corners == 5: object_type = 'Pentagon'
            elif object_corners == 6: object_type = 'Hexagon'
            elif object_corners == 7: object_type = 'Heptagon'
            elif object_corners > 7: object_type = 'Circle'
            else: object_type = 'None'
            cv2.rectangle(image_contour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(image_contour, object_type,
                        (x+(w//2)-10,y+(h//2)-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,
                        (0,255,255),2)


# fetch image
path = 'resources/shapes.png'
image = cv2.imread(path)
image_contour = image.copy()

# preprocessing
image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_greyscale, (7,7), 1)
# edge detection
image_blank = np.zeros_like(image)
image_canny = cv2.Canny(image_blur, 50,50)
getContours(image_canny)

# output preparation and execution
image_stack = stackImages(([image, image_blank, image_contour],[image_blur, image_canny, image_greyscale]), 0.6)
cv2.imshow('stack', image_stack)
cv2.waitKey(0)