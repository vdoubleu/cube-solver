#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

# motor pin numbers 
# key - identifier
# value - (IN1, IN2, IN3, IN4)
MOTORS = {'LR-linear': (17, 18, 27, 22), # pair
          'FB-linear': (23, 24, 10, 9),  # pair
          'F-rotation': (25, 11, 8, 7),
          'B-rotation': (5, 6, 12, 13),
          'L-rotation': (19, 16, 26, 20),
          'R-rotation': (21, 2, 3, 4)}

# constants
STEPS_PER_REV = 520
DELAY = 0.0015
RANGES = [[0, 1, 2, 3], [3, 2, 1, 0]]

# full step sequence
SEQUENCE = [[0,0,1,1],
            [1,0,0,1],
            [1,1,0,0],
            [0,1,1,0]]

def setup():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    for motor in MOTORS.values():
        for pin in motor:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

# rotate motor
def rotate(num_rev, motors):
    num_steps = int(num_rev * STEPS_PER_REV)

    for step in range(num_steps):

        for i in range(len(SEQUENCE)):
            # direction: 0 = ccw, 1 = cw
            for motor in motors:
                for j in range(len(motor[0])):
                    GPIO.output(motor[0][j], SEQUENCE[RANGES[motor[1]][i]][j])

            time.sleep(DELAY)


if __name__ == '__main__':
    setup()
    rotate(1, [(motor, True) for motor in MOTORS.values()]) # one rotation
