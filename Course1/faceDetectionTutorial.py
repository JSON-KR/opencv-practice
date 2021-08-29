import cv2 as cv 

#! Pre-trained face detection classfier
faceClassfier = cv.CascadeClassifier('haar_face.xml')

#! Read image frame from own webcam
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    #! Convert BGR to Grayscale
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #! Face detection
    faceRect = faceClassfier.detectMultiScale(frameGray, scaleFactor = 1.1)
    
    #! Draw square on the detected area
    for (x,y,w,h) in faceRect:
        cv.rectangle(frame, (x,y), (x+w,y+h), 255, 2)

    #! Show image
    cv.imshow('window', frame)

    #! Finish the program
    if cv.waitKey(20) & 0xFF == ord('q'):
        break




