# Simple test of the Pi Cobbler cable.  Turn an LED on and then off.

import RPi.GPIO as GPIO
import time
import secrets 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 18 

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)

time.sleep(2)

GPIO.output(led,0)

GPIO.cleanup()

print secrets.config['ifttt_key']


