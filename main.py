import os

import cvzone
from cvzone.ClassificationModule import Classifier
import cv2
from controller import rotateServo
import threading

cap = cv2.VideoCapture(0)
address="http://192.168.243.41:8080/video"
cap.open(address)
classifier = Classifier('Resources/Waste_model/keras_model.h5', 'Resources/Waste_model/labels.txt')
classIDBin=0
imgBinsList=[]
pathFolderBins='Resources/Bins'
pathList=os.listdir(pathFolderBins)
for path in pathList:
        imgBinsList.append(cv2.imread(os.path.join(pathFolderBins,path),cv2.IMREAD_UNCHANGED))
# print(imgBinsList)

classDic={
        0: 3,
        1:0,
        2:0,
        3:0,
        4:0,
        5:1,
        6:1,
        7:1,
        8:1
}
temp = 0
while True:
        _, img = cap.read()
        imgResize=cv2.resize(img,(454,340))

        imgBackground=cv2.imread('Resources/background.png')

        predection = classifier.getPrediction(img)
        print(predection[1])
        # if(predection[1]==0):
        #         print("none")
        # elif predection[1]==1:
        #         print("plastic bag")
        # elif predection[1]==2:
        #         print("plastic bottle")
        # elif predection[1]==3:
        #         print("leaf")
        # elif predection[1]==4:
        #         print("papper")

        classID=predection[1]
        if classID !=0:
                classIDBin=classDic[classID]

        imgBackground=cvzone.overlayPNG(imgBackground, imgBinsList[classIDBin],(895, 374))

        imgBackground[148:148+340,159:159+454]=imgResize


        cv2.imshow("salman", imgBackground)
        cv2.waitKey(1)

