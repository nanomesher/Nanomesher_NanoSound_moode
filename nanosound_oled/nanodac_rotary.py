#!/usr/bin/python
# -*- coding: utf-8 -*-

from socketIO_client import SocketIO, LoggingNamespace
from RPi import GPIO
from time import sleep
import os

def volup():
    os.system('/var/www/vol.sh up 5')


def voldown():
    os.system('/var/www/vol.sh dn 5')


clk = 22
dt = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

clkLastState = GPIO.input(clk)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
				#print("+")
                                volup()
                        else:
				#print("-")
                                voldown()
                clkLastState = clkState
                sleep(0.01)
finally:
        GPIO.cleanup()

