from picamera.array import PiRGBBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    frame = frame.array
    
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == 27:
        break
