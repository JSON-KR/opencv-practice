import cv2 as cv
import numpy as np

""" 
! Contour 예제
"""
fileSource = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cat.jpg'
nameReadImg = fileSource + fileCategory + fileName

img = cv.imread(nameReadImg)

cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)


# Contour
# ! cv.RETR_LIST: contour들의 hierarchies들 중에서 뭘 보여줄건가 
# ! cv.CHAIN_APPROX_NONE: contour를 어떻게 근사할 것인가
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

blank = np.zeros(img.shape,dtype='uint8')


contours = cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow('Contours', contours)

cv.waitKey(0)
