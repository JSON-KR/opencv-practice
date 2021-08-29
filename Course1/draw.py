import cv2 as cv
import numpy as np


""" 
! 그리기, 텍스트 집어넣기 예제
"""

# 빈 이미지 생성
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank', blank)
cv.waitKey(0)

# 이미지에 색깔 넣어보기
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('blank', blank)
cv.waitKey(0)

# 사각형 그려보기 
cv.rectangle(blank, (0, 0), (blank.shape[1]//3, blank.shape[0]//2), (0,255,0), thickness = 2) # thickness -1: fill
cv.imshow('Rectangle', blank)
cv.waitKey(0)

# 원형 그리기
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness = 3)
cv.imshow('Circle', blank)
cv.waitKey(0)

# 라인 그리기 
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness = 5)
cv.imshow('Line', blank)
cv.waitKey(0)

# 텍스트 작성하기
cv.putText(blank, 'Hello World', (250, 100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)
cv.waitKey(0)
