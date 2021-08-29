import cv2 as cv
import numpy as np

fileDirectory = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cats.jpg'
fileRead = fileDirectory + fileCategory + fileName

img = cv.imread(fileRead)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# ! 라플라시안 Gradient
lap = cv.Laplacian(gray, cv.CV_64F)
# Gradient는 +-값을 가지지만, 실제 이미지 처리에서는 -를 사용할 수 없으므로 절대값처리
lap = np.uint8(np.absolute(lap))

cv.imshow('laplacian', lap)


# ! Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

sobel_xy = cv.bitwise_or(sobelx, sobely)
cv.imshow('combined', sobel_xy)


cv.waitKey(0)
