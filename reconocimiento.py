import cv2
import serial
import numpy as np

#ard = serial.Serial("COM6",9600)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        #p = np.int_(x).item()
        #l = np.int_(y).item()
        #cad = str(p)+","+str(l)
        #ard.write(cad.encode('ascii'))
    cv2.imshow('Proyecto IA', img)
    k = cv2.waitKey(30)
    if k == 27:
        break
cap.release()
