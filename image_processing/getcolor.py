import cv2
import numpy as np

"""
#for resize of image
scale_percent = 20 # percent of original size
width = int(im.shape[1] * scale_percent / 100)
height = int(im.shape[0] * scale_percent / 100)
dim = (width, height)
"""

def getColors(im):
    #box dimensions
    scale_percent = 100 # percent of original size
    width = int(im.shape[1] * scale_percent / 100)
    height = int(im.shape[0] * scale_percent / 100)
    left = width/4
    top = height/4
    size = width/8
    margin = 10 + size 

    faceColors = [[0 for x in range(3)] for y in range(3)]

    for i in range(3):
        for j in range(3):
           mask = np.zeros(im.shape[:2], np.uint8)
           mask[top + j*margin:top+size + j*margin, left + i*margin:left+size + i*margin] = 255
           res = cv2.bitwise_and(im, im, mask = mask)

           meanColor = cv2.mean(im, mask)
           faceColors[i][j] = meanColor

           cv2.rectangle(im, (left + i*margin, top + j*margin), (size + left + i*margin, size + top + j*margin), meanColor, 3)

    """
    im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
    
    cv2.imshow('boxes', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

    #print(faceColors)
    return faceColors, im
