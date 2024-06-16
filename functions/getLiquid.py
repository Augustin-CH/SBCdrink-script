#!/usr/bin/python3
from time import sleep
from functions.rotate import rotate
from config.config import *

def quantityToTime(quantity):
    return quantity * TIME_FOR_ONE_QUANTITY

def getLiquid(quantity, slot, position):

    # rotate("belt" , 850, "right") # droit
    # sleep(1)
    # rotate("belt" , 450, "left") # gauche
    # sleep(1)
    # rotate("bottle" , 450, "up") # droit
    # sleep(1)
    # rotate("bottle" , 450, "down") # gauche
    # sleep(1)


    bottleUptime = quantityToTime(quantity)
    beltRightTime = (BOTTLE_SLOT_POSITION["SLOT_" + str(slot)] - position)

    if (BOTTLE_SLOT_POSITION["SLOT_" + str(slot)] - position < 0):
        # If position is higher than slot position, go to the left
        rotate("belt", int(position - BOTTLE_SLOT_POSITION["SLOT_" + str(slot)]), "left")
    else:
        # Else, go right
        rotate("belt", int(BOTTLE_SLOT_POSITION["SLOT_" + str(slot)] - position ), "right")

    # TODO: get slot volume from api
    quantityPerTurn = 35 # 35cl par tour
    while bottleUptime > 0:
        print(f"while : {bottleUptime}")
        
        rotate("bottle" , 450, "up") # monte
        sleep(bottleUptime)
        rotate("bottle" , 90, "down")  # descend
        sleep(0.5)
        if(slot < 12):
            rotate("belt" ,80, "right")   # decale droite
        else:
            rotate("belt" ,80, "left")   # decale gauche

        sleep(1)
        rotate("bottle" ,360, "down")  # descend
        #sleep(TIME_FOR_FILL_DISPENSOR)
        #rotate("belt" ,80, "left")   # decale gauche
        sleep(1)
        bottleUptime  = bottleUptime - TIME_FOR_ONE_QUANTITY * quantityPerTurn
    
    if(slot < 12):
        position = int(BOTTLE_SLOT_POSITION["SLOT_" + str(slot)] + 80)
    else:
        position = int(BOTTLE_SLOT_POSITION["SLOT_" + str(slot)] + 80)
    return position
