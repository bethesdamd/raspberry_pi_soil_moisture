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
	value = readadc(0)  # Assumes we are wired to ADC CH0 which is pin 1
	#volts = (value * 3.3) / 1024
	#temperature = volts / (10.0 / 1000)
	#print ("%4d/1023 => %5.3f V => %4.1f C" % (value, volts, temperature))
	print(value)
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



