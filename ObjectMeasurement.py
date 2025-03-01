import cv2
import numpy as np

##################
#setting webcam false at the beginning

webcam=False
path='images/1.jpg'
cap=cv2.VideoCapture(0)

#settting brightness of the window
cap.set(10,160)

#setting width and height of the window
cap.set(3,1920)
cap.set(4,1080)

#getting imagery data
while True:
    if webcam:success,img=cap.read()
    else:img=cv2.imread(path)
    #resizing image to a smaller scale
    img=cv2.resize(img,(0,0),None,0.5,0.5)
    cv2.imshow('Original',img)
    cv2.waitKey(1)