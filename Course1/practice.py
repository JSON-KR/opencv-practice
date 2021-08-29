import cv2 as cv
import numpy as np

fileDirectory = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cats.jpg'
fileRead = fileDirectory + fileCategory + fileName


# ! Rescale
def rescaleFrame(frame, scale = 0.5):
    
    width, height = int(frame.shape[1] * scale) , int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, cv.INTER_AREA)

# ! Draw image
def drawImage(frame):
    cv.imshow('Window', frame)
    return True

# ! Covert color
def convertFrame2Gray(frame):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

# ! Canny
def cannyFrame(frame):
    return cv.Canny(frame, 150, 175, cv.BORDER_DEFAULT)

# ! Blur
def blurFrame(frame):
    return cv.blur(frame, (3,3), borderType = cv.BORDER_DEFAULT)

# ! Translate / Rotate / Flip
def translateFrame(frame, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(frame, transMat, dimensions)

def rotateFrame(frame, angle, rotPoint = None):
    (height, width) = frame.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(frame, rotMat, dimensions)

def flipFrame(frame, direction = 0):
    return cv.flip(frame, direction)


# ! Video
# fileDirectory = r'C:\Users\bemba\Documents\GitHub\opencv-course\Resources'
# fileCategory = r'\Videos'
# fileName = r'\dog.mp4'
# fileRead = fileDirectory + fileCategory + fileName

# capture = cv.VideoCapture(fileRead)

# while True:
#     isTrue, frame = capture.read()

#     cv.imshow('dog', frame)

#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break

# ! Draw
# blank = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('blank', blank)

def drawCircle(frame, radius, thickness, centerPoint = None):
    if centerPoint is None:
        centerPoint = (int(frame.shape[0]//2), int(frame.shape[1]//2))

    return cv.circle(frame, centerPoint, radius, 255, thickness)

def drawRectangle(frame, pt1, pt2, thickness):
    return cv.rectangle(frame, pt1, pt2, 255, thickness)

def drawLine(frame, pt1, pt2, thickness):
    return cv.line(frame, pt1, pt2, 255, thickness)

def putText(frame, text, pt):

    return cv.putText(frame, text, pt, cv.FONT_HERSHEY_TRIPLEX, 1, (0,0,255), 1)

# drawnImage = putText(blank, "Hello I am Son", (100,300))
# cv.imshow('circle', drawnImage)


# ! Contour
# img = cv.imread(filename=fileRead)
# gray = convertFrame2Gray(img)
# blur = blurFrame(gray)
# canny = cannyFrame(blur)


# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# blank = np.zeros(img.shape,dtype='uint8')
# contours = cv.drawContours(blank, contours, -1, (0, 100, 255), 3)

# print('Number of contours: ', len(contours))

# drawImage(contours)
# cv.waitKey(0)


# ! Bitwise
# blank = np.zeros((500, 500, 3), dtype='uint8')
# rectangle = drawRectangle(blank.copy(), (10,10), (400, 400), -1)
# circle = drawCircle(blank.copy(), 250, -1)
# bitAnd = cv.bitwise_and(rectangle, circle)

# cv.imshow('window', bitAnd)
# cv.waitKey(0)

# ! Masking
# img = cv.imread(fileRead)
# cv.imshow('img', img)

# blank = np.zeros(img.shape[:2], dtype='uint8')
# circle =drawCircle(blank, 100, -1, (blank.shape[1]//2, blank.shape[0]//2))
# masked = cv.bitwise_and(img, img, mask = circle)
# cv.imshow('win', masked)
# cv.waitKey(0)

# ! Histogram
# import matplotlib.pyplot as plt
# img = cv.imread(fileRead)
# cv.imshow('img', img)

# colors = ['b', 'g', 'r']

# for index, color in enumerate(colors):
#     print(index, color)
#     hist = cv.calcHist([img], [index], None, [256], [0, 256])
#     plt.plot(hist, color = color)

# plt.show()


# ! Thresh


# !