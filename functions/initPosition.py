import RPi.GPIO as GPIO
from time import sleep
from functions.rotate import rotate
from functions.setAllGpioToLow import setAllGpioToLow
from config.config import *

def searchLimite(motorType):

    print('motorType', motorType)

    pin_out_1 = 0
    pin_out_2 = 0
    pin_out_3 = 0
    pin_out_4 = 0
    pin_limit_sensor = 0
    step_sleep = 0

    if motorType == "belt":
        pin_out_1 = BELT_ENGINE["PIN_OUT_1"]
        pin_out_2 = BELT_ENGINE["PIN_OUT_2"]
        pin_out_3 = BELT_ENGINE["PIN_OUT_3"]
        pin_out_4 = BELT_ENGINE["PIN_OUT_4"]
        pin_limit_sensor = BELT_LIMIT_SENSOR["PIN_SIGNAL"]
        step_sleep = BELT_ENGINE["STEP_SLEEP"]
    elif motorType == "bottle":
        pin_out_1 = BOTTLE_ENGINE["PIN_OUT_1"]
        pin_out_2 = BOTTLE_ENGINE["PIN_OUT_2"]
        pin_out_3 = BOTTLE_ENGINE["PIN_OUT_3"]
        pin_out_4 = BOTTLE_ENGINE["PIN_OUT_4"]
        pin_limit_sensor = BOTTLE_LIMIT_SENSOR["PIN_SIGNAL"]
        step_sleep = BOTTLE_ENGINE["STEP_SLEEP"]
    i = 0

    while True:
        if (GPIO.input(pin_limit_sensor) == 0):
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

def initPosition(motorType, setPosition):
    print("----- init position -----")
    # rotate left while BELT_LIMIT_SENSOR is not pressed
    searchLimite(motorType)
    rotate(motorType, setPosition, "right")
    position = setPosition
    sleep(0.5)
    return position