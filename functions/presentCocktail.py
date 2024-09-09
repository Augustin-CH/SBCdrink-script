from functions.rotate import rotate
from config.config import *

def presentCocktail(position):
    if(position > PRESENT_POSITION):
        rotate(BELT_ENGINE, position-PRESENT_POSITION, "left")
    else:
        rotate(BELT_ENGINE, PRESENT_POSITION - position, "right")