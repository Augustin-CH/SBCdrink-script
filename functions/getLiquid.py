#!/usr/bin/python3
from time import sleep
from functions.rotate import rotate

# TODO: add params slot
def getLiquid(cl):
    # TODO: determine the time for the right quantity
    rotate("bottle" ,10000, "up") # monte
    sleep(cl)
    rotate("bottle" ,1500, "down")  # descend
    sleep(1)
    rotate("belt" ,25000, "up")   # decale droite
    sleep(1)
    rotate("bottle" ,10000, "down")  # descend
    sleep(1)
    rotate("belt" ,7000, "down")   # decale gauche
    sleep(1)
    rotate("belt" ,7000, "up")   # decale droite
    sleep(1)
    rotate("belt" ,25000, "down")   # decale gauche
