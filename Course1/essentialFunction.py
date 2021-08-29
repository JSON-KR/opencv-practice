import cv2 as cv

""" 
! 색상 변환
"""
fileSource = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cat.jpg'
nameReadImg = fileSource + fileCategory + fileName

img = cv.imread(nameReadImg)
cv.imshow('Cat', img)

# 색상 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Cat', gray)

""" 
! Blur
"""
blur = cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)



""" 
! Edge Cascade
"""
# 이미지에서 일정 Threshold 값을 대상으로 선들만 남김
# 블러 처리된 이미지를 대상으로 canny 처리를 하면, 자잘한 Edge들을 없앨 수 있다.
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)


"""
! Dialating
"""
# Edge Cascade에서 추출된 선들을 두께를 두껍게 해주는 처리
dialated = cv.dilate(canny, (11,11), iterations=5)
cv.imshow('Dialated', dialated)

"""
! Eroding
"""
eroded = cv.erode(dialated, (11,11), iterations=5)
cv.imshow('Eroded', eroded)


"""
! Resize
"""
# 이미지를 Resize하면, 사용하던 pixel간격들이 바뀌니까, 인터폴레이션을 해줘야함
# 작아지는 경우엔 cv.INTER_AREA, 커지는 경우엔 cv.INTER_LINEAR, cv.INTER_CUBIC
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

"""
! Cropping
"""
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)

