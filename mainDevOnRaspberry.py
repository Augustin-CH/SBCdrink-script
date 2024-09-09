#!/usr/bin/python3
from functions.getLiquid import getLiquid
from time import sleep
import json
import RPi.GPIO as GPIO
from config.config import *
from functions.rotate import rotate
from functions.presentCocktail import presentCoktail
from functions.initBeltPosition import initBeltPosition

position = 10

global steps

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(BELT_LIMIT_SENSOR["PIN_SIGNAL"], GPIO.IN)
        
with open('testCocktail.json') as f:
    try:
        position = initBeltPosition()
        
        steps = json.load(f)
        print(steps)

        dispenserEmptyingTime = 1
        dispenserFillingTime = 1

        for step in steps:
            print(f"distribute {step['pressed']}cl of {step['slot']} and wait {step['delayAfter']}")
            position = getLiquid(step, position, dispenserEmptyingTime, dispenserFillingTime)
            sleep(step['delayAfter'])

        print(f"the cocktail is finished")
        position = presentCoktail(position)

    except:
        print(f"ERRROR")
 