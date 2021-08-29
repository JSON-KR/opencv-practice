import cv2 as cv

fileDirectory = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cats.jpg'
fileRead = fileDirectory + fileCategory + fileName

img = cv.imread(fileRead)
cv.imshow('base', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Maxval: Threshold를 넘어서는 데이터는 maxval로 처리하겠다.
# cv.THRESH_BINARY 이분처리하겠다
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)


cv.imshow('thresh', thresh)
cv.imshow('thresh_inv', thresh_inv)



# ! Adaptive Thresholding
# blocksize안에서 median이나 Gaussian처리를 하여, 해당영역의 적절한 Threshold 값을 계산해준다
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive', adaptive_thresh)

cv.waitKey(0)
