#!/usr/bin/python
from Adafruit_Thermal import *
import RPi.GPIO as GPIO
import time
import random
import hints
#reset fortune Variable
Fortune = ''

def printadvice():
# Initialize the printer.  Note this will take a few seconds for the printer
# to warm up and be ready to accept commands (hence calling it explicitly vs.
# automatically in the initializer with the default auto_warm_up=True).

	printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
	fortune = random.choice(hints)

	printer.justify('C')
	printer.println('   _      _     _        ')
	printer.println('  /_\  __| |_ _(_)__ ___ ')
	printer.println(' / _ \/ _` \ V / / _/ -_)')
	printer.println('/_/ \_\__,_|\_/|_\__\___|')
	printer.println('_________________________')
	printer.feed(1)
	printer.boldOn()
	printer.println(fortune)
	printer.boldOff()
	printer.feed(2)
	printer.feed(3)
	printer.sleep()      # Tell printer to sleep
	printer.wake()       # Call wake() before printing again, even if reset
	printer.setDefault() # Restore printer to defaults
