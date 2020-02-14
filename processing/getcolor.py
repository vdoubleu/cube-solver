import cv2
import numpy as np

im = cv2.imread("rcube4.jpg")

#for resize of image
scale_percent = 20 # percent of original size
width = int(im.shape[1] * scale_percent / 100)
height = int(im.shape[0] * scale_percent / 100)
dim = (width, height)

#box dimensions
left = 750
top = 1400
size = height*5/8
margin = 50 + size 

for i in range(3):
    for j in range(3):
       mask = np.zeros(im.shape[:2], np.uint8)
       mask[top + j*margin:top+size + j*margin, left + i*margin:left+size + i*margin] = 255
       res = cv2.bitwise_and(im, im, mask = mask)

       meanColor = cv2.mean(im, mask)

       cv2.rectangle(im, (left + i*margin, top + j*margin), (size + left + i*margin, size + top + j*margin), meanColor, 10)


im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('boxes', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
