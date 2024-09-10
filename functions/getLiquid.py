#!/usr/bin/python3
from time import sleep
from functions.rotate import rotate
from config.config import *

def getLiquid(step, currentPosition, dispenserEmptyingTime, dispenserFillingTime):
    print("ICI1")

    # rotate("belt" , 850, "right") # droit
    # sleep(1)
    # rotate("belt" , 450, "left") # gauche
    # sleep(1)
    # rotate("bottle" , 450, "up") # droit
    # sleep(1)
    # rotate("bottle" , 450, "down") # gauche
    # sleep(1)
    
    pressed = step['pressed']
    delayAfter = step['delayAfter']
    slotPosition = step['position']

    if (slotPosition - currentPosition < 0):
        # If position is higher than slot position, go to the left
        rotate("belt", int(currentPosition - slotPosition), "left")
    else:
        # Else, go right
        rotate("belt", int(slotPosition - currentPosition ), "right")

    rotate("bottle" , 450, "up") # monte
    sleep(pressed)
    rotate("bottle" , 90, "down")  # descend
    sleep(0.5)
    if(currentPosition < 100): # 100 a la place de 80 pour garder une marge et pas bloquer tout a gauche
        rotate("belt" ,80, "right")   # decale droite
    else:
        rotate("belt" ,80, "left")   # decale gauche

    sleep(1)
    rotate("bottle" ,360, "down")  # descend
    sleep(max(delayAfter - 1.5, 0)) # 1.5 secondes pour compencer le temps des actions precedentes, si inferieur a 0 sleep(0)
    
    if(currentPosition < 100):
        currentPosition = int(slotPosition + 80)
    else:
        currentPosition = int(slotPosition - 80)
    return currentPosition