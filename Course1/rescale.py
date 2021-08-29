import cv2 as cv


""" 
! 이미지 리사이징 예제
"""
fileSource = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cat_large.jpg'
nameReadImg = fileSource + fileCategory + fileName

# 이미지 읽기
img = cv.imread(nameReadImg)

# 이미지 리사이징
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


# 비디오 읽기에 리사이징 적용해보기
fileSource = r'C:\Users\bemba\Documents\GitHub\opencv-course\Resources'
fileCategory = r'\Videos'
fileName = r'\dog.mp4'
nameReadVideo = fileSource + fileCategory + fileName
print('Read a video from ' + nameReadVideo + '\n')
capture = cv.VideoCapture(nameReadVideo)
while True:
    isTrue, frame = capture.read()

    #! 여기다가 리사이징 함수 추가
    frameResized = rescaleFrame(frame, scale = 0.25)

    # 개별의 프레임들을 imshow
    cv.imshow('dog',frameResized)

    # 키를 20번 누르거나, d가 입력되면 중지
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

