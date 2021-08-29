
#! Package
import cv2
import numpy as np
import random
import os

#! Paths & Variables
pathBase = r'Resources\Faces\train'
fileFaceDetector = 'haar_face.xml'
fileTrainedData = 'faceTrained.yml'

haar_cascade = cv2.CascadeClassifier(fileFaceDetector)

#! Get random test item
def getRandomTestIndex():

    listPeople = os.listdir(pathBase)
    numberOfPeople = len(listPeople)

    # print(numberOfPeople)
    idxPerson = random.randint(0,numberOfPeople-1)
    person = listPeople[idxPerson]
    print('Person for the test is ', person)

    pathPerson = os.path.join(pathBase, person)
    listImg = os.listdir(pathPerson)

    numberOfImg = len(listImg)
    idxImg = random.randint(0, numberOfImg-1)
    pictureNumber = listImg[idxImg]
    print('Image number for the test is ', pictureNumber)

    return person, pictureNumber, listPeople

testPerson, testPicture, listPeople = getRandomTestIndex()

#! Read image
fileTest = os.path.join(pathBase, testPerson)
fileTest = os.path.join(fileTest, testPicture)

img = cv2.imread(fileTest)

#! Covert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#! Detect and classify the face
# Detector
faceRect = haar_cascade.detectMultiScale(imgGray, scaleFactor = 1.1, minNeighbors = 4)

# Classifier
faceClassifier = cv2.face.LBPHFaceRecognizer_create()
faceClassifier.read(fileTrainedData)

for (x, y, w, h) in faceRect:

    # ROI
    faceROI = imgGray[y:y+h,x:x+w]

    # Classification
    label, confidence = faceClassifier.predict(faceROI)
    print(f'\nlabel = {listPeople[label]} with a confidence of {confidence}')

    # Visualization
    cv2.putText(img, str(listPeople[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), 2)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow('test',img)
cv2.waitKey(0)