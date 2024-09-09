import RPi.GPIO as GPIO
from time import sleep
from functions.rotate import rotate
from functions.setAllGpioToLow import setAllGpioToLow
from config.config import *

def searchBeltLimite():
    pin_out_1 = 0
    pin_out_2 = 0
    pin_out_3 = 0
    pin_out_4 = 0
    step_sleep = 0

    pin_out_1 = BELT_ENGINE["PIN_OUT_1"]
    pin_out_2 = BELT_ENGINE["PIN_OUT_2"]
    pin_out_3 = BELT_ENGINE["PIN_OUT_3"]
    pin_out_4 = BELT_ENGINE["PIN_OUT_4"]
    step_sleep = BELT_ENGINE["STEP_SLEEP"]
    i = 0

    while True:
        if (GPIO.input(BELT_LIMIT_SENSOR["PIN_SIGNAL"]) == 0):
            if i%4==0:
                GPIO.output(pin_out_4, GPIO.HIGH)
                GPIO.output(pin_out_3, GPIO.LOW)
                GPIO.output(pin_out_2, GPIO.LOW)
                GPIO.output(pin_out_1, GPIO.LOW)
            elif i%4==1:
                GPIO.output(pin_out_4, GPIO.LOW)
                GPIO.output(pin_out_3, GPIO.LOW)
                GPIO.output(pin_out_2, GPIO.HIGH)
                GPIO.output(pin_out_1, GPIO.LOW)
            elif i%4==2:
                GPIO.output(pin_out_4, GPIO.LOW)
                GPIO.output(pin_out_3, GPIO.HIGH)
                GPIO.output(pin_out_2, GPIO.LOW)
                GPIO.output(pin_out_1, GPIO.LOW)
            elif i%4==3:
                GPIO.output(pin_out_4, GPIO.LOW)
                GPIO.output(pin_out_3, GPIO.LOW)
                GPIO.output(pin_out_2, GPIO.LOW)
                GPIO.output(pin_out_1, GPIO.HIGH)
            i = i + 1

            sleep(step_sleep)
        else:
            setAllGpioToLow()
            break

def initBeltPosition():
    print("----- init position -----")
    # rotate left while BELT_LIMIT_SENSOR is not pressed
    searchBeltLimite()
    rotate("belt", 4, "right")
    position = 4
    sleep(2)
    return position