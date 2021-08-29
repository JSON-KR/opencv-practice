
#! Read packages
import cv2
import numpy as np
import os

#! Path names & Variables
pathBase = r'Resources\Faces\train'
fileFaceDetector = 'haar_face.xml'
fileTrainedData = 'faceTrained.yml'
features = []
labels = []

# Face classfier
faceClassifier = cv2.CascadeClassifier(fileFaceDetector)

#! Read image data
# Crawling the folders
def createTraining(pathBase, features, labels, faceClassifier):
    peopleName = os.listdir(pathBase)
    for i, person in enumerate(peopleName):
        pathPerson = os.path.join(pathBase, person)
        print('Image files are being read from \n', pathPerson)

    # Read each file one by one
        pictureList = os.listdir(pathPerson)
        for picture in pictureList:
            pathPicture = os.path.join(pathPerson, picture)
        
            img = cv2.imread(pathPicture)

        #! Data pre-processing
        # Convert the image to gray color
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces in each image
            faceRect = faceClassifier.detectMultiScale(imgGray, scaleFactor = 1.1, minNeighbors = 4)

        # Extract the region of interest
            for (x, y, w, h) in faceRect:
                faceROI = imgGray[y:y+h, x:x+w]

             # Save the images as features, and coressponding labels as well
                features.append(faceROI)
                labels.append(i) 
    # Check data
    print(f'Number of features: {len(features)}')
    print(f'Number of labels: {len(labels)}')

    #! Save the features and labels as numpy array
    # Convert list to numpy array
    features = np.array(features, dtype='object')
    labels = np.array(labels)

    #print(labels)

    # Save the numpy array
    np.save('features.npy', features)
    np.save('labels.npy', labels)

# Read the function above
createTraining(pathBase, features, labels, faceClassifier)

#! Train data
features = np.array(features, dtype='object')
labels = np.array(labels)
faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceRecognizer.train(features, labels)

#! Save the trained data
faceRecognizer.save(fileTrainedData)


print('Training Done!')

