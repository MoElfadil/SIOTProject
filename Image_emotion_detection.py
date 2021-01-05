# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 06:35:53 2021

@author: Mohammed
"""

import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

img = cv2.imread('sadwoman.jpg')

plt.imshow(img)
predictions = DeepFace.analyze(img)
print(predictions['dominant_emotion'])

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, predictions['dominant_emotion'], (0,50), font, 1, (0,0,255), 2, cv2.LINE_4);
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))