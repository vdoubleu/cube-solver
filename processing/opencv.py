from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


def video_capture():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera)

    time.sleep(0.1)

    for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
        
        frame = frame.array
        img = edge_detection(frame)
        
        cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Frame', 640, 480)
        cv2.imshow('Frame', img)

        key = cv2.waitKey(1) & 0xFF

        rawCapture.truncate(0)
        
        if key == 27:
            break
    

def edge_detection(img):

    # scale down
    scale = 40
    width = int(img.shape[1] * scale/100)
    height = int(img.shape[0] * scale/100)
    img = cv2.resize(img, (width, height), cv2.INTER_AREA)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred, 20, 40)

    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(canny, kernel, iterations=2)

    ret, thresh = cv2.threshold(dilated, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    filtered_contours = []
    mean_colours = []
    for i in range(len(contours)):
        epsilon = 0.01*cv2.arcLength(contours[i], True)
        approx = cv2.approxPolyDP(contours[i], epsilon, True)
        contours[i] = cv2.convexHull(approx)

        area = cv2.contourArea(contours[i])

        if 1000 > area > 200:
            filtered_contours.append(contours[i])
            x,y,w,h = cv2.boundingRect(contours[i])
            #img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

            # mean colour
            mask = np.zeros(img.shape[:2], np.uint8)
            mask[y:y+h, x:x+w] = 255
            mean_colours.append(cv2.mean(img, mask))

    # all contours
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

    # filtered contours
    cv2.drawContours(img, filtered_contours, -1, (0, 255, 0), 1)
    return img


if __name__ == '__main__':
    video_capture()
