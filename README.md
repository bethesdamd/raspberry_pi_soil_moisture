# Measure soil moisture using a Raspberry Pi and a Sparkfun soil moisture sensor

System will sample the sensor periodically and send the value to a Google Spreadsheet via IFTTT.com
Will use MCP3008 ADC chip.  This is not intended to be a full step by step tutorial, but rather
a quick overview for people that are familiar with projects like this.

## IFTTT.com configuration
You'll need an IFTTT account, and a Google account for Google Drive.  Configure a "Maker Channel" to accept an incoming HTTP GET.  Then connect it
to a Google channel that will add a row to a Google Drive spreadsheet.

## curl
We'll use curl to test that we can add a value to a Google spreadsheet using IFTTT.  

curl https://maker.ifttt.com/trigger/[message name]/with/key/[your ifttt key]

The message name in this case would be the temperature value.

So the above curl command should create a new row in a spreadsheet, with a column for timestamp and a column for the temperature.

 


