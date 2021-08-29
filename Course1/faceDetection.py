import cv2 as cv

fileDirectory = r'Resources'
fileCategory = r'\Photos'
fileName = r'\group 1.jpg'
fileRead = fileDirectory + fileCategory + fileName

img = cv.imread(fileRead)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)