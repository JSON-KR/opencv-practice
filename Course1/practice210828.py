import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

fileDirectory = r'Resources'
fileCategory = r'\Photos'
fileName = r'\group 1.jpg'
fileRead = fileDirectory + fileCategory + fileName

# ! 이미지 읽기
# img = cv.imread(fileRead)

# ! 리사이징
# def resizeImg(frame, scale = 0.5):
#     width = int(img.shape[1] * scale)
#     height = int(img.shape[0] * scale)

#     dimensions = (width, height)

#     return cv.resize(frame, dimensions)

# cv.imshow('base', img)

# ! 노이즈 제거
# imgBlur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur', imgBlur)

# ! 그레이 변환
# imgGray = cv.cvtColor(imgBlur, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', imgGray)


# ! 히스토그램
# hist = cv.calcHist([imgGray], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.show()

# ! Canny
imgCanny = cv.Canny(imgGray, 150, 220)
cv.imshow('canny', imgCanny)

# ! Laplacian
# lap = cv.Laplacian(imgGray, cv.CV_64F)
# imgLap = np.uint8(np.absolute(lap))
# cv.imshow('laplacian', imgLap)


# ! Split
# b,g,r = cv.split(img)
# blank = np.zeros(img.shape[:2], dtype='uint8')

# blue = cv.merge([b, blank, blank])
# green = cv.merge([blank, g, blank])
# red = cv.merge([blank, blank, r])

# cv.imshow('blue', blue)
# cv.imshow('green', green)
# cv.imshow('red', red)

# ! Masking
# blank = np.zeros(img.shape[:2], dtype='uint8')
# circle = cv.circle(blank, (int(img.shape[1]//2),int(img.shape[0]//2)), 100, 255, -1)

# imgMask = cv.bitwise_and(img, img, mask = circle)
# cv.imshow('mask', imgMask)

# ! Face Detection
# haarClassfier = cv.CascadeClassifier('haar_face.xml')
# faceRect = haarClassfier.detectMultiScale(imgGray, scaleFactor = 1.1, minNeighbors = 1)

# for x, y, w, h in faceRect:
#     cv.rectangle(img, (x,y), (x+w,y+h), 255, 2)
# cv.imshow('Detected Faces', img)
# print(f'num of found face: {len(faceRect)}')
# cv.waitKey(0)


# ! Face Detection With My Own Camera
