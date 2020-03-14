#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
from stepper_control import setup, rotate, MOTORS

if __name__ == '__main__':

    setup()

    while (True):
        try:
            print('\nSelect which motor to calibrate:')
            print('1 - LR-linear')
            print('2 - FB-linear')
            print('3 - F-rotation')
            print('4 - B-rotation')
            print('5 - L-rotation')
            print('6 - R-rotation')
            print('7 - Exit calibration')
            i = int(input('>> ')) - 1
        except ValueError:
            continue

        print()

        if i == 7:
            break

        motor = MOTORS[list(MOTORS.keys())[i]]

        while (True):
            try:
                num_rev = float(input('Enter number of revolutions (or -1 to exit): '))
            except ValueError:
                continue

            if num_rev < 0:
                break

            rotate(num_rev, [(motor, True)]) 
