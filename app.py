#!/usr/bin/python3
#from functions.getLiquid import getLiquid
from time import sleep
from flask import Flask
import board
import neopixel
import time
import random
import asyncio
from threading import Thread
app = Flask(__name__)
pixels = neopixel.NeoPixel(board.D18, 36)
PIXEL_LENGHT = 8

@app.route("/")
def hello_world():
    daemon = Thread(target=launch, daemon=True, name='Monitor')
    daemon.start()
    #asyncio.run(launch())
    return "lancé"

def launch():
    while True:
        for x in range(36):
            lightPixel(x)

def mapToOuterIndex(index):
    if(index >= 36):
        return index - 36
    return index

def mapToInnerIndex(index):
    if(index >= 36):
        index = index - 36
    return 35-(index//2)

def lightPixel(index):
    color = random.randint(0, 140), random.randint(0, 140), random.randint(0, 140)
    pixels[index] = (color)
    #pixels[mapToInnerIndex(index)] = (0, 0, 0)
    #pixels[mapToOuterIndex(index) + PIXEL_LENGHT] = (color)
    #pixels[mapToInnerIndex(index) + PIXEL_LENGHT//2] = (color)
    time.sleep(0.03)

