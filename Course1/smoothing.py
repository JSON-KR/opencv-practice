import cv2 as cv

# ! Average blur
cv.blur()

# ! Gaussian blur
cv.GaussianBlur()

# ! Median blur
cv.medianBlur()

# ! Bilateral blur
# 블러를 하면서도 edge를 얻을 수 있는, 최신식 블러라고 함
cv.bilateralFilter()