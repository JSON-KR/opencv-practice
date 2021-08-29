
#! Import packages
import cv2
import numpy as np
import os

#! Specify paths and variables
pathBase = r'Resources\Faces\train'
fileFaceDetector = 'haar_face.xml'
features = []
labels = []
featureName = 'features.npy'
labelName = 'labels.npy'
fileTrainedData = 'faceTrained.yml'

#! Crawling folders
# retrieve the folder names
namePeople = os.listdir(pathBase)

# look in to folders one by one
for idx, person in enumerate(namePeople):
    # get the each folder name
    pathPerson = os.path.join(pathBase, person)
    print(person)

    #! Read the image
    # retrive the image names
    imgList = os.listdir(pathPerson)
    for img in imgList:
        # get the each image name
        fileImg = os.path.join(pathPerson, img)

        # read the image
        frame = cv2.imread(fileImg)

        #! Pre-processing for the data
        # convert to grayscale
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect face
        faceDetector = cv2.CascadeClassifier(fileFaceDetector)
        faceRect = faceDetector.detectMultiScale(frameGray, scaleFactor = 1.1, minNeighbors = 4)

        # Extract ROI
        for (x, y, w, h) in faceRect:
            faceROI = frameGray[y:y+h, x:x+w]

            # append features and labels
            features.append(faceROI)
            labels.append(idx)

#! save the features and labels
features = np.array(features, dtype='object')
labels = np.array(labels)

print(f'number of features is {len(features)}')

np.save(featureName, features)
np.save(labelName, labels)

print('--- Reading completed ---')

#! Train the image
faceTrainer = cv2.face.LBPHFaceRecognizer_create()
trainedFaceRecognizer = faceTrainer.train(features, labels)

print('--- Training completed ---')

#! Save the trained data
faceTrainer.save(fileTrainedData)

print('--- Program completed ---')