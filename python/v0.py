# -*- coding: utf-8 -*-
"""
Created on Sat May 26 15:25:10 2018

To be tested with available cameras, until THE ONE arrives. Or is bought.

Goals:
    1) Connect camera DONE
    2) Detect object contours TODO
    3) Find distance to object TODO
    4) Determine object velocity TODO

"""

import cv2
import os

folderName = "cannyEdge_2"
dirName = "./" + folderName

if not os.path.exists(dirName):
    os.makedirs(dirName)

# Threshold value
thresh = 25
# Maximum value for threshold
maxThresh = 255
# Drawing contours on the frame
contourSelect = -1
contourR = 0
contourG = 255
contourB = 0
contourThick = 1
# Canny edges values
minCanny = 0
maxCanny = 50

# Camera connection
cap = cv2.VideoCapture(1)

k = 1

while True:
    # Reads frame from feed
    ok, frame = cap.read()
    # Converts frame to grayscale - Needed for thresholding and canny edge
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    # Inverts the grayscaled image - Not sure if necessary
    frame3 = cv2.bitwise_not(frame2)
    # Threshold the image (ToZero). Everything with value beneath "thresh", is turned to 0
    # th, frame4 = cv2.threshold(frame3, thresh, maxThresh, cv2.THRESH_TOZERO)
    # Canny edge detection
    edges = cv2.Canny(frame3, minCanny, maxCanny)
    # Finds the contours
    # im, contours, h = cv2.findContours(frame4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Draws the contours on the frame
    # cv2.drawContours(frame, contours, contourSelect, (contourR,contourG,contourB), contourThick)
    # Show camera feed
    cv2.imshow("Live feed", edges)    
    
    # Saving images
    cv2.imwrite(dirName + "/img_" + "%09d" % k + ".png", edges)
    k += 1
    
    # Press ESC to exit feed
    lol = cv2.waitKey(1) & 0xff
    if lol == 27: break
    