#!/usr/bin/python3
#from functions.getLiquid import getLiquid
from time import sleep
from flask import Flask
import board
import neopixel
import time
import random

app = Flask(__name__)
pixels = neopixel.NeoPixel(board.D18, 36)
PIXEL_LENGHT = 8

@app.route("/")
def hello_world():
    while True:
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

        for x in range(24):
            lightPixel(x, color)


def mapToOuterIndex(index):
    if(index >= 24):
        return index - 24
    return index

def mapToInnerIndex(index):
    if(index >= 24):
        index = index - 24
    return 35-(index//2)

def lightPixel(index, color):
    pixels[mapToOuterIndex(index)] = (0, 0, 0)
    pixels[mapToInnerIndex(index)] = (0, 0, 0)
    pixels[mapToOuterIndex(index) + PIXEL_LENGHT] = (color)
    pixels[mapToInnerIndex(index) + PIXEL_LENGHT//2] = (color)
    time.sleep(0.03)


