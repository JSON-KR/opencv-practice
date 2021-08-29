import cv2 as cv
import numpy as np
fileSource = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cat.jpg'


img = cv.imread(fileSource+fileCategory+fileName)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2+100, img.shape[0]//2), 100, 255, -1)


maskedImage = cv.bitwise_and(img, img, mask=mask)

cv.imshow('masked', maskedImage)
cv.waitKey(0)