import cv2 as cv

fileDirectory = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cat.jpg'
fileRead = fileDirectory + fileCategory + fileName

print(fileRead)

img = cv.imread(fileRead)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('hey', gray)

cv.waitKey(0)