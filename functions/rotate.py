#!/usr/bin/python3
from time import sleep
import RPi.GPIO as GPIO
from config.config import *

GPIO.setmode(GPIO.BCM)         # Paramétrage de la numérotation des GPIO en mode BCM
GPIO.setwarnings(True)        # Ne pas tenir compte des alertes

GPIO.setup(BELT_ENGINE["PIN_OUT_1"], GPIO.OUT, initial=0)     # GPIO PIN_OUT configuré en sortie
GPIO.setup(BELT_ENGINE["PIN_OUT_2"], GPIO.OUT, initial=0)      # GPIO PIN_OUT configuré en sortie
GPIO.setup(BELT_ENGINE["PIN_OUT_3"], GPIO.OUT, initial=0)     # GPIO PIN_OUT configuré en sortie
GPIO.setup(BELT_ENGINE["PIN_OUT_4"], GPIO.OUT, initial=0)      # GPIO PIN_OUT configuré en sortie
GPIO.setup(BOTTLE_ENGINE["PIN_OUT_1"], GPIO.OUT, initial=0)     # GPIO PIN_OUT configuré en sortie
GPIO.setup(BOTTLE_ENGINE["PIN_OUT_2"], GPIO.OUT, initial=0)      # GPIO PIN_OUT configuré en sortie
GPIO.setup(BOTTLE_ENGINE["PIN_OUT_3"], GPIO.OUT, initial=0)     # GPIO PIN_OUT configuré en sortie
GPIO.setup(BOTTLE_ENGINE["PIN_OUT_4"], GPIO.OUT, initial=0)      # GPIO PIN_OUT configuré en sortie
GPIO.setup(BELT_LIMIT_SENSOR["PIN_SIGNAL"], GPIO.IN)
GPIO.setup(BOTTLE_LIMIT_SENSOR["PIN_SIGNAL"], GPIO.IN)

def rotate(motorType, dist, sens):
    rangefor = 0
    if sens == "down" or sens =="left":
        rangefor = range(dist)
    elif sens == "up" or sens == "right":
        rangefor = range(dist, 0, -1)

    pin_out_1 = 0
    pin_out_2 = 0
    pin_out_3 = 0
    pin_out_4 = 0
    step_sleep = 0

    if motorType == "belt":
        pin_out_1 = BELT_ENGINE["PIN_OUT_1"]
        pin_out_2 = BELT_ENGINE["PIN_OUT_2"]
        pin_out_3 = BELT_ENGINE["PIN_OUT_3"]
        pin_out_4 = BELT_ENGINE["PIN_OUT_4"]
        step_sleep = BELT_ENGINE["STEP_SLEEP"]
    elif motorType == "bottle":
        pin_out_1 = BOTTLE_ENGINE["PIN_OUT_1"]
        pin_out_2 = BOTTLE_ENGINE["PIN_OUT_2"]
        pin_out_3 = BOTTLE_ENGINE["PIN_OUT_3"]
        pin_out_4 = BOTTLE_ENGINE["PIN_OUT_4"]
        step_sleep = BOTTLE_ENGINE["STEP_SLEEP"]

    for i in rangefor:
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

        sleep(step_sleep)
