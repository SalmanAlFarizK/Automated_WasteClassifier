import os

import cvzone
from cvzone.ClassificationModule import Classifier
import cv2
import threading
from testController import rotateServo1, rotateServo2
import time
from queue import Queue

evt = threading.Condition()
flag = Queue()


def main(e):
    cap = cv2.VideoCapture(0)
    address = "http://192.168.223.95:8080/video"
    cap.open(address)
    classifier = Classifier('Resources/Waste_model/keras_model.h5', 'Resources/Waste_model/labels.txt')
    classIDBin = 0
    imgBinsList = []
    pathFolderBins = 'Resources/Bins'
    pathList = os.listdir(pathFolderBins)
    for path in pathList:
        imgBinsList.append(cv2.imread(os.path.join(pathFolderBins, path), cv2.IMREAD_UNCHANGED))

    classDic = {
        0: 5,
        1: 3,
        2: 3,
        3: 3,
        4: 3,
        5: 4,
        6: 4,
        7: 4,
        8: 4
    }
    while True:
        _, img = cap.read()
        imgResize = cv2.resize(img, (454, 340))

        imgBackground = cv2.imread('Resources/background.png')

        predection = classifier.getPrediction(img)
        print(predection[1])

        classID = predection[1]
        classIDBin = classDic[classID]
        if classID in [1, 2, 3, 4]:
            e.put(1)
        elif classID in [5, 6, 7, 8]:
            e.put(2)
        else:
            e.put(0)

        imgBackground = cvzone.overlayPNG(imgBackground, imgBinsList[classIDBin], (895, 374))

        imgBackground[148:148 + 340, 159:159 + 454] = imgResize

        cv2.imshow("salman", imgBackground)
        cv2.waitKey(1)


def rot(e):
    while True:
        if e.get() == 1:
            for i in range(0, 180):
                rotateServo1(i)
                time.sleep(.0001)
            for i in range(180, 1, -1):
                rotateServo1(i)
                time.sleep(.0001)
        elif e.get() == 2:
            for i in range(0, 180):
                rotateServo2(i)
                time.sleep(.0001)
            for i in range(180, 1, -1):
                rotateServo2(i)
                time.sleep(.0001)
        else:
            pass

        e.queue.clear()


if __name__ == '__main__':
    p1 = threading.Thread(target=main, args=(flag,))
    p2 = threading.Thread(target=rot, args=(flag,))
    p1.start()
    p2.start()
