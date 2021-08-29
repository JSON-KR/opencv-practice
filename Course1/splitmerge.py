import cv2 as cv
import numpy as np

fileSource = r'Resources'
fileCategory = r'\Photos'
fileName = r'\park.jpg'
nameReadImg = fileSource + fileCategory + fileName

img = cv.imread(nameReadImg)

# ! Split
b, g, r = cv.split(img)

cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)

print('b',b.shape)
print('g',g.shape)
print('r',r.shape)

# ! Merge
merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

# ! 개별 색깔별로 보여주기
blank = np.zeros(img.shape[:2], dtype = 'uint8')
print('blank',blank.shape)

blue = cv.merge([b, blank, blank])
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])
cv.imshow('blue', blue)
cv.imshow('red', red)
cv.imshow('green', green)
cv.waitKey(0)
