#!/usr/bin/python
from Adafruit_Thermal import *
import RPi.GPIO as GPIO
import time
import random
import hints
import printadvice

Fortune = ''
#this sets up the printer and the gpio pins for the first button press
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

#cleans up the pins to stop the printer from printing junk

def clanupgpio()
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
   inputValue = GPIO.input(18)
   if (inputValue == False):
		printer.warm_up()
		printadvice()
		cleanupgpio()
   time.sleep(0.3)



