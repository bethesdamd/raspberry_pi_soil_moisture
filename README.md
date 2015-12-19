# CODE FORTHCOMING
## Measure soil moisture using a Raspberry Pi and a Sparkfun soil moisture sensor

System will sample the sensor periodically and send the value to a Google Spreadsheet via IFTTT.com
Will use MCP3008 ADC chip.  This is not intended to be a full step by step tutorial, but rather
a quick overview for people that are familiar with projects like this.

### IFTTT.com configuration
You'll need an IFTTT account, and a Google account for Google Drive.  Configure a "Maker Channel" to accept an incoming HTTP GET.  Then connect it
to a Google channel that will add a row to a Google Drive spreadsheet.

### curl
We'll use curl to test that we can add a value to a Google spreadsheet using IFTTT.  

curl https://maker.ifttt.com/trigger/[message name]/with/key/[your ifttt key]

The message name in this case would be the temperature value.

So the above curl command should create a new row in a spreadsheet, with a column for timestamp and a column for the temperature.  You can configure IFTTT in a variety of ways but this was pretty much the default.

In the final python code we'll likely using an HTTP library to send the message to IFTTT but we could also issue a system call to curl.

### Miscellenous
You may have to do a 'pip install requests[security]' if you get a warning when the python http request is made.  This is just a warning however and doesn't appear to have any effect on the proper operation of the call.

I had to do the following to get SPI initialized on my Pi: 
sudo vi /etc/modprobe.d/raspi-blacklist.conf and comment out the line with 'spi', e.g.  blacklist spi-bcm2835 (your number may vary if you have an older Pi like I do.)
Also, add the following line to /boot/config.txt and reboot:  dtparam=spi=on
(from the bottom of this post: https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=105360)


