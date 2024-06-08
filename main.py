#!/usr/bin/python3
from functions.getLiquid import getLiquid
from time import sleep
import json
import RPi.GPIO as GPIO
from config.config import *
from functions.rotate import initPosition, rotate, presentCoktail

position = 10

global steps

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(BELT_LIMIT_SENSOR["PIN_SIGNAL"], GPIO.IN)

def initBeltPosition():
    print("----- init position -----")
    initPosition()
    rotate("belt", 4, "right")
    position = 4
    sleep(2)
    return position
        
with open('testCocktail.json') as f:
    try:
        position = initBeltPosition()
        
        steps = json.load(f)
        print(steps)

        for step in steps:
            print(f"distribute {step['pressed']*0.5}cl of {step['slot']} and wait {step['delayAfter']}")
            position = getLiquid(step['pressed'], step['slot'], position)
            sleep(step['delayAfter'])

        print(f"the cocktail is finished")
        position = presentCoktail(position)

    except:
        print(f"ERRROR")
 