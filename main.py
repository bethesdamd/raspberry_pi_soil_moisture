# Read soil moisture sensor and send data to a Google Spreadsheet 
# Details:
# This will read from an MCP3008 ADC chip (https://www.adafruit.com/product/856) using SPI protocol.  The ADC reads the analog volatge output 
# of the Sparkfun soil moisture sensor (https://www.sparkfun.com/products/13322)

import secrets
import urllib2
import requests
import json
import spidev
import time

# Configuration to turn on soil sensor only when we need it to avoid oxidation
# Do this by powering the sensor from a GPIO output pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
power_sensor = 18
GPIO.setup(power_sensor, GPIO.OUT)

# Read ADC - from http://scruss.com/blog/2013/02/02/simple-adc-with-the-raspberry-pi/
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
	if adcnum > 7 or adcnum < 0:
		return -1
	r = spi.xfer2([1, 8 + adcnum << 4, 0])
	adcout = ((r[1] & 3) << 8) + r[2]
	return adcout
 
while True:
	# Turn on power to sensor
	GPIO.output(power_sensor, 1)
	value = readadc(0)  # Assumes we are wired to ADC CH0 which is pin 1
	#volts = (value * 3.3) / 1024
	#temperature = volts / (10.0 / 1000)
	#print ("%4d/1023 => %5.3f V => %4.1f C" % (value, volts, temperature))
	print(value)
	# Turn off power to sensor
	GPIO.output(power_sensor, 0)
	time.sleep(3)


# Do any needed numerical conversion of raw value

# Value to string
moisture = '99'

# IFTTT accepts the optional payload json object; 'value1' will be placed in a spreadsheet column
url ="https://maker.ifttt.com/trigger/from_raspberry_pi/with/key/" + secrets.config['ifttt_key']
payload = { 'value1': moisture }
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
# print(response)



