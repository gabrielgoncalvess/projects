# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:18:32 2021

@author: gabre
"""

import cv2 as cv


#img = cv.imread(r"C:/Users/gabre/Desktop/jobsonn.png")
#img = cv.imread(r"C:/Users/gabre/Desktop/SUPERIOR/patrick bateman.png")
img = cv.imread(r"C:/Users/gabre/Desktop/Projects/Open CV/FACES/7127_E-1.jpg")
cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
cv.imshow("Detected Faces", img)

cv.waitKey(0)