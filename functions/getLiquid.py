#!/usr/bin/python3
from time import sleep
from functions.rotate import rotate
from functions.initPosition import initPosition
from config.config import *

def getLiquid(step, currentPosition, dispenserEmptyingTime, dispenserFillingTime):
    print("ICI1")
    print("currentPosition", currentPosition)

    # rotate("belt" , 850, "right") # droit
    # sleep(1)
    # rotate("belt" , 450, "left") # gauche
    # sleep(1)
    # rotate("bottle" , 450, "up") # droit
    # sleep(1)
    # rotate("bottle" , 450, "down") # gauche
    # sleep(1)

    initPosition("bottle", 150)

    pressed = step['pressed']
    delayAfter = step['delayAfter']
    slotPosition = step['position']

    if (slotPosition - currentPosition < 0):
        # If position is higher than slot position, go to the left
        rotate("belt", int(currentPosition - slotPosition), "left")
    else:
        # Else, go right
        rotate("belt", int(slotPosition - currentPosition ), "right")

    rotate("bottle", 530, "up") # monte
    sleep(pressed)
    rotate("bottle", 90, "down")  # descend
    sleep(0.5)
    # if(currentPosition < 100): # 100 a la place de 80 pour garder une marge et pas bloquer tout a gauche
    #     rotate("belt", 70, "right")   # decale droite
    # else:
    rotate("belt", 70, "left")   # decale gauche

    sleep(1)
    initPosition("bottle", 150)
    sleep(max(delayAfter - 1.5, 0)) # 1.5 secondes pour compencer le temps des actions precedentes, si inferieur a 0 sleep(0)
    
    # if(currentPosition < 100):
    #     currentPosition = int(slotPosition + 70)
    # else:
    currentPosition = int(slotPosition - 70)
    return currentPosition