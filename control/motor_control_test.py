#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# pin numbers
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

pins = [IN1, IN2, IN3, IN4]

# set up output pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# delay between steps
delay = 0.002

# full step sequence
step_count = 4
sequence = [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]]


def step(num_steps):
    for i in range(num_steps):
        for i in range(len(pins)):
            GPIO.output(pins[i], sequence[i])

        time.sleep(delay)

step(10)