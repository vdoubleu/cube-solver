#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# motor pin numbers
motors = [[17, 18, 27, 22], # pair
          [23, 24, 10, 9], # pair
          [25, 11, 8, 7],
          [5, 6, 12, 13],
          [19, 16, 26, 20],
          [21, 2, 3, 4]]

# set up output pins
for motor in motors:
    for pin in motor:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

# delay between steps
delay = 0.0015

# full step sequence
step_count = 4
sequence = [[0,0,1,1],
            [1,0,0,1],
            [1,1,0,0],
            [0,1,1,0]]

def step(num_steps):
    for step in range(num_steps):
        for i in range(len(sequence)):
            for motor in motors:
                for j in range(len(motor)):
                    GPIO.output(motor[j], sequence[i][j])

            time.sleep(delay)

step(520)
