#!/usr/bin/env python

import numpy as np
import cv2
import pymeanshift as pms

cap = cv2.VideoCapture(0)

printMenu = False
mySegmenter = pms.Segmenter()
mySegmenter.spatial_radius = 6
mySegmenter.range_radius = 4.5
mySegmenter.min_density = 300
mkeyPress = False
wKeyPress = False

while(True):

    if not printMenu:
        print("This program performs a image segmentation of the images taken with the webcam.")
        print("Press -ms to execute image segmentation using mean shift algorithm.")
        print("Press -ws to execute image segmentation using watersheds algorithm.")
        print("Press q for exit.")
        printMenu = True

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Tarea2: Segmentacion de imagen',frame)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('m'):
        mKeyPress = True
        wKeyPress = False
    elif key & 0xFF == ord('w'):
        wKeyPress = True
        mKeyPress = False
    elif key & 0xFF == ord('s') and mKeyPress:
        print("Using Mean Shift Algorithm!")
        (segmentedImage, labelsImage, numberRegions) = mySegmenter(frame)
        cv2.imshow('Tarea2: Imagen Segmentada',segmentedImage)
        mKeyPress = False
    elif key & 0xFF == ord('s') and wKeyPress:
        print("Using Watersheds Algorithm!")
    else:
        mKeyPress = False
        wKeyPress = False
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
