import cv2
import numpy as np
import face_recognition

#1. Loading the images and converting them into system-readable RGB from BGR

imgElon= face_recognition.load_image_file('ImagesBasic/Elon_Musk.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Bill_Gates.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)