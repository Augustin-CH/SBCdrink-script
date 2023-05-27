#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
 
vertical_out1 = 17
vertical_out2 = 18
vertical_out3 = 27
vertical_out4 = 22

horizontal_out1 = 10
horizontal_out2 = 25
horizontal_out3 = 9
horizontal_out4 = 11
# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
horizontal_step_sleep = 0.001
vertical_step_sleep = 0.001

step_count = 1000
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( vertical_out1, GPIO.OUT )
GPIO.setup( vertical_out2, GPIO.OUT )
GPIO.setup( vertical_out3, GPIO.OUT )
GPIO.setup( vertical_out4, GPIO.OUT )
GPIO.setup( horizontal_out1, GPIO.OUT )
GPIO.setup( horizontal_out2, GPIO.OUT )
GPIO.setup( horizontal_out3, GPIO.OUT )
GPIO.setup( horizontal_out4, GPIO.OUT )
 
def ReleaseMotors():
    GPIO.output( vertical_out1, GPIO.LOW )
    GPIO.output( vertical_out2, GPIO.LOW )
    GPIO.output( vertical_out3, GPIO.LOW )
    GPIO.output( vertical_out4, GPIO.LOW )
    GPIO.output( horizontal_out1, GPIO.LOW )
    GPIO.output( horizontal_out2, GPIO.LOW )
    GPIO.output( horizontal_out3, GPIO.LOW )
    GPIO.output( horizontal_out4, GPIO.LOW )

def Cleanup():
    ReleaseMotors()
    GPIO.cleanup()
    
def MoveDown(dist):
    print("move down: ", dist)
    
    for i in range(dist):
        if i%4==0:
            GPIO.output( vertical_out4, GPIO.HIGH )
            GPIO.output( vertical_out3, GPIO.LOW )
            GPIO.output( vertical_out2, GPIO.LOW )
            GPIO.output( vertical_out1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( vertical_out4, GPIO.LOW )
            GPIO.output( vertical_out3, GPIO.LOW )
            GPIO.output( vertical_out2, GPIO.HIGH )
            GPIO.output( vertical_out1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( vertical_out4, GPIO.LOW )
            GPIO.output( vertical_out3, GPIO.HIGH )
            GPIO.output( vertical_out2, GPIO.LOW )
            GPIO.output( vertical_out1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( vertical_out4, GPIO.LOW )
            GPIO.output( vertical_out3, GPIO.LOW )
            GPIO.output( vertical_out2, GPIO.LOW )
            GPIO.output( vertical_out1, GPIO.HIGH )

        time.sleep( vertical_step_sleep )
        
def MoveUp(dist):
    print("move up: ", dist)
    
    for i in range(dist, 0, -1):
        if i%4==0:
            GPIO.output( vertical_out4, GPIO.HIGH )
            GPIO.output( vertical_out3, GPIO.LOW )
            GPIO.output( vertical_out2, GPIO.LOW )
            GPIO.output( vertical_out1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( vertical_out4, GPIO.LOW )
            GPIO.output( vertical_out3, GPIO.LOW )
            GPIO.output( vertical_out2, GPIO.HIGH )
            GPIO.output( vertical_out1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( vertical_out4, GPIO.LOW )
            GPIO.output( vertical_out3, GPIO.HIGH )
            GPIO.output( vertical_out2, GPIO.LOW )
            GPIO.output( vertical_out1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( vertical_out4, GPIO.LOW )
            GPIO.output( vertical_out3, GPIO.LOW )
            GPIO.output( vertical_out2, GPIO.LOW )
            GPIO.output( vertical_out1, GPIO.HIGH )

        time.sleep( vertical_step_sleep )
        
def MoveLeft(dist):
    print("move left: ", dist)
    
    for i in range(dist, 0, -1):
        if i%4==0:
            GPIO.output( horizontal_out4, GPIO.HIGH )
            GPIO.output( horizontal_out3, GPIO.LOW )
            GPIO.output( horizontal_out2, GPIO.LOW )
            GPIO.output( horizontal_out1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( horizontal_out4, GPIO.LOW )
            GPIO.output( horizontal_out3, GPIO.LOW )
            GPIO.output( horizontal_out2, GPIO.HIGH )
            GPIO.output( horizontal_out1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( horizontal_out4, GPIO.LOW )
            GPIO.output( horizontal_out3, GPIO.HIGH )
            GPIO.output( horizontal_out2, GPIO.LOW )
            GPIO.output( horizontal_out1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( horizontal_out4, GPIO.LOW )
            GPIO.output( horizontal_out3, GPIO.LOW )
            GPIO.output( horizontal_out2, GPIO.LOW )
            GPIO.output( horizontal_out1, GPIO.HIGH )

        time.sleep( horizontal_step_sleep )

        
def MoveRight(dist):
    print("move right: ", dist)
    
    for i in range(dist):
        if i%4==0:
            GPIO.output( horizontal_out4, GPIO.HIGH )
            GPIO.output( horizontal_out3, GPIO.LOW )
            GPIO.output( horizontal_out2, GPIO.LOW )
            GPIO.output( horizontal_out1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( horizontal_out4, GPIO.LOW )
            GPIO.output( horizontal_out3, GPIO.LOW )
            GPIO.output( horizontal_out2, GPIO.HIGH )
            GPIO.output( horizontal_out1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( horizontal_out4, GPIO.LOW )
            GPIO.output( horizontal_out3, GPIO.HIGH )
            GPIO.output( horizontal_out2, GPIO.LOW )
            GPIO.output( horizontal_out1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( horizontal_out4, GPIO.LOW )
            GPIO.output( horizontal_out3, GPIO.LOW )
            GPIO.output( horizontal_out2, GPIO.LOW )
            GPIO.output( horizontal_out1, GPIO.HIGH )

        time.sleep( horizontal_step_sleep )

def GetLiquid(cl):
    MoveRight(1500)
    ReleaseMotors()
    time.sleep(1)
    MoveUp(1000)
    time.sleep(cl)
    MoveDown(150)
    ReleaseMotors()
    time.sleep(0.5)
    MoveRight(150)
    MoveDown(850)
    ReleaseMotors()
    time.sleep(1)
    MoveLeft(1650)
    time.sleep(3)
   
    
ReleaseMotors()
while True:
    GetLiquid(2)
