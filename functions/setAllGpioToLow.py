import RPi.GPIO as GPIO
from config.config import *

def setAllGpioToLow():
    GPIO.output(BELT_ENGINE["PIN_OUT_1"], GPIO.LOW)
    GPIO.output(BELT_ENGINE["PIN_OUT_2"], GPIO.LOW)
    GPIO.output(BELT_ENGINE["PIN_OUT_3"], GPIO.LOW)
    GPIO.output(BELT_ENGINE["PIN_OUT_4"], GPIO.LOW)
    GPIO.output(BOTTLE_ENGINE["PIN_OUT_1"], GPIO.LOW)
    GPIO.output(BOTTLE_ENGINE["PIN_OUT_2"], GPIO.LOW)
    GPIO.output(BOTTLE_ENGINE["PIN_OUT_3"], GPIO.LOW)
    GPIO.output(BOTTLE_ENGINE["PIN_OUT_4"], GPIO.LOW)