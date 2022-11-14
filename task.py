import cv2 
import numpy as np 


def MOUSRGB(event,x,y,flags,param): 
    global image 
    if event == cv2.EVENT_MOUSEMOVE:
        image = cv2.imread('A.jpg',1)  #any color image
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]

        cv2.putText(image,str(colorsB) + ',' + str(colorsG)+ ',' + str(colorsR), (10,500), font, 2, (255,180,0),2)

image = cv2.imread('A.jpg',1)
cv2.namedWindow('mousergb')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.setMouseCallback('mousergb',MOUSRGB)

while(1): 
    cv2.imshow('mousergb',MOUSRGB) 
    if cv2.waitKey(20) == 27: 
        break 

cv2.destroyAllWindows()