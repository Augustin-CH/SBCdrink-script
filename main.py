#!/usr/bin/python3
from functions.getLiquid import getLiquid
from time import sleep
import json
import RPi.GPIO as GPIO
from config.config import *
from functions.rotate import rotate

position = 10

global steps

GPIO.setmode(GPIO.BCM)

GPIO.setup(BELT_LIMIT_SENSOR["PIN_SIGNAL"], GPIO.IN)

def InitPosition():
    print("----- init position -----")
    while True:
        if (GPIO.input(BELT_LIMIT_SENSOR["PIN_SIGNAL"]) == 0):
            rotate("belt" ,5, "left")   # go left till the limit sensor is high
        else:
            position = 0
            return position
        
with open('testCocktail.json') as f:
    try:
        position = InitPosition()
        print("is init with", position)
        
        steps = json.load(f)
        print(steps)

        # order steps by order key
        steps.sort(key=lambda step: step['stepId'])

        for step in steps:
            print(f"distribute {step['pressed']*0.5}cl of {step['slot']} and wait {step['delayAfter']}")
            postion = getLiquid(step['pressed'], step['slot'], position)
            sleep(step['delayAfter'])
        print(f"the cocktail is finished")
    except:
        print(f"ERRROR")
 