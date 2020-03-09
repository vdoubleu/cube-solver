#!/usr/bin/env python3
import time
from stepper_control import rotate, MOTORS

# constants
QUARTER_TURN = 0.25
HALF_TURN = 0.5
LINEAR_HALF_TURN = 0.5

# convert from rubik's cube move notation to motor action
# key - notation
# value - (motor, number of turns, clockwise)
CONVERSION = {
    'F': ('F', QUARTER_TURN, True),
    'R': ('R', QUARTER_TURN, True),
    'U': ('U', QUARTER_TURN, True),
    'L': ('L', QUARTER_TURN, True),
    'B': ('B', QUARTER_TURN, True),

    "F'": ('F', QUARTER_TURN, False),
    "R'": ('R', QUARTER_TURN, False),
    "U'": ('U', QUARTER_TURN, False),
    "L'": ('L', QUARTER_TURN, False),
    "B'": ('B', QUARTER_TURN, False),

    'F2': ('F', HALF_TURN, True),
    'R2': ('R', HALF_TURN, True),
    'U2': ('U', HALF_TURN, True),
    'L2': ('L', HALF_TURN, True),
    'B2': ('B', HALF_TURN, True),
    'D2': ('D', HALF_TURN, True)
}

# converts a series of notations to a motor sequence and executes each action
def execute_sequence(notations):

    for notation in notations.split():
        action = CONVERSION[notation]

        if action[0] == 'F':
            rotate(action[1], MOTORS['F-rotation']=action[2])
            if action[1] == QUARTER_TURN:
                rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)
                rotate(action[1], MOTORS['F-rotation']=!action[2])
                rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)
        
        elif action[0] == 'R':
            rotate(action[1], MOTORS['R-rotation']=action[2])
            if action[1] == QUARTER_TURN:
                rotate(LINEAR_HALF_TURN, MOTORS['RL-linear']=True)
                rotate(action[1], MOTORS['R-rotation']=!action[2])
                rotate(LINEAR_HALF_TURN, MOTORS['RL-linear']=True)
        
        elif action[0] == 'L':
            rotate(action[1], MOTORS['L-rotation']=action[2])
            if action[1] == QUARTER_TURN:
                rotate(LINEAR_HALF_TURN, MOTORS['RL-linear']=True)
                rotate(action[1], MOTORS['L-rotation']=!action[2])
                rotate(LINEAR_HALF_TURN, MOTORS['RL-linear']=True)
                
        elif action[0] == 'B':
            rotate(action[1], MOTORS['B-rotation']=action[2])
            if action[1] == QUARTER_TURN:
                rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)
                rotate(action[1], MOTORS['B-rotation']=!action[2])
                rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)

        elif action[0] == 'U':
            rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)
            rotate(QUARTER_TURN, MOTORS['L-rotation']=True, MOTORS['R-rotation']=False)
            rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)
            
            rotate(LINEAR_HALF_TURN, MOTORS['LR-linear']=True)
            rotate(QUARTER_TURN, MOTORS['L-rotation']=False, MOTORS['R-rotation']=True)
            rotate(LINEAR_HALF_TURN, MOTORS['LR-linear']=True)

            rotate(action[1], MOTORS['F-rotation']=action[2])
            rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)

            if action[1] == QUARTER_TURN:
                rotate(action[1], MOTORS['L-rotation']=True, MOTORS['R-rotation']=False, MOTORS['F-rotation']=!action[2])
            else:
                rotate(LINEAR_HALF_TURN, MOTORS['L-rotation']=True, MOTORS['R-rotation']=False)

            rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)

            rotate(LINEAR_HALF_TURN, MOTORS['LR-linear']=True)
            rotate(QUARTER_TURN, MOTORS['L-rotation']=False, MOTORS['R-rotation']=True)
            rotate(LINEAR_HALF_TURN, MOTORS['LR-linear']=True)

        elif action[0] == 'D':
            rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)
            rotate(QUARTER_TURN, MOTORS['L-rotation']=True, MOTORS['R-rotation']=False)
            rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)
            
            rotate(LINEAR_HALF_TURN, MOTORS['LR-linear']=True)
            rotate(QUARTER_TURN, MOTORS['L-rotation']=False, MOTORS['R-rotation']=True)
            rotate(LINEAR_HALF_TURN, MOTORS['LR-linear']=True)

            rotate(action[1], MOTORS['B-rotation']=action[2])
            rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)

            if action[1] == QUARTER_TURN:
                rotate(action[1], MOTORS['L-rotation']=True, MOTORS['R-rotation']=False, MOTORS['B-rotation']=!action[2])
            else:
                rotate(LINEAR_HALF_TURN, MOTORS['L-rotation']=True, MOTORS['R-rotation']=False)

            rotate(LINEAR_HALF_TURN, MOTORS['FB-linear']=True)

            rotate(LINEAR_HALF_TURN, MOTORS['LR-linear']=True)
            rotate(QUARTER_TURN, MOTORS['L-rotation']=False, MOTORS['R-rotation']=True)
            rotate(LINEAR_HALF_TURN, MOTORS['LR-linear']=True)
