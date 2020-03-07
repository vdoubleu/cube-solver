#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

# motor pin numbers (IN1, IN2, IN3, IN4)
MOTORS = [[17, 18, 27, 22], # pair
          [23, 24, 10, 9],  # pair
          [25, 11, 8, 7],
          [5, 6, 12, 13],
          [19, 16, 26, 20],
          [21, 2, 3, 4]]

# constants
STEPS_PER_REV = 520
DELAY = 0.0015

# full step sequence
SEQUENCE = [[0,0,1,1],
            [1,0,0,1],
            [1,1,0,0],
            [0,1,1,0]]

def setup():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    for motor in MOTORS:
        for pin in motor:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

# rotate clockwise
def rotate_cw(num_rev, *motors):
    num_steps = num_rev * STEPS_PER_REV

    for step in range(num_steps):
        for i in range(len(SEQUENCE)):
            for motor in motors:
                for j in range(len(motor)):
                    GPIO.output(motor[j], SEQUENCE[i][j])

            time.sleep(DELAY)

# rotate counterclockwise
def rotate_ccw(num_rev, *motors):
    num_steps = num_rev * STEPS_PER_REV

    for step in range(num_steps):
        for i in range(len(SEQUENCE)-1, -1, -1):
            for motor in motors:
                for j in range(len(motor)):
                    GPIO.output(motor[j], SEQUENCE[i][j])

            time.sleep(DELAY)

if __name__ == '__main__':
    setup()
    rotate_cw(1, MOTORS) # one rotation
