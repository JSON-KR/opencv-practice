import cv2 as cv

""" 
! 이미지 읽어들이기 예제
"""
fileSource = r'Resources'
fileCategory = r'\Photos'
fileName = r'\cat.jpg'
nameReadImg = fileSource + fileCategory + fileName
print('Read a image from ' + nameReadImg + '\n')

# Image를 w x h x RGB 사이즈의 Matrix로 읽어들임
img = cv.imread(nameReadImg)  

# 읽어들인 Matrix를 가시화 함
cv.imshow('cat', img)

# Key를 누를때까지 Imshow를 게속 유지함
cv.waitKey(0)


""" 
! 영상 읽어들이기 예제
"""
fileSource = r'C:\Users\bemba\Documents\GitHub\opencv-course\Resources'
fileCategory = r'\Videos'
fileName = r'\dog.mp4'
nameReadVideo = fileSource + fileCategory + fileName
print('Read a video from ' + nameReadVideo + '\n')

# 전체 비디오의 정보를 받아들여서
capture = cv.VideoCapture(nameReadVideo)

# 전체 비디오가 끝날때까지 프레임을 하나하나 읽어들임
while True:
    isTrue, frame = capture.read()

    # 개별의 프레임들을 imshow
    cv.imshow('dog',frame)

    # 키를 20번 누르거나, d가 입력되면 중지
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()