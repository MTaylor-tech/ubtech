import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin=4)

#set global for prevention of invalid reads
last_temp = 24.0
last_humid = 0.0

def print_temp() :
    global last_temp
    global last_humid
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
	last_temp = result.temperature
	last_humid = result.humidity
    else :
	print("Invalid reading. Using stored values.")
	print("Temperature: %d C" % last_temp)
	print("Humidity: %d %%" % last_humid)
    
def tempC() :
	global last_temp
	result = instance.read()
	if result.is_valid() :
		last_temp = result.temperature
		return result.temperature
	else :		
		return last_temp

def humid() :
	global last_humid
	result = instance.read()
	if result.is_valid() :
		last_humid = result.humidity
		return result.humidity
	else :
		return last_humid
	
def tempF() :
	global last_temp
	result = instance.read()
	if result.is_valid() :
		last_temp = result.temperature
		temp_F = 9.0/5.0 * result.temperature + 32.0
		return temp_F
	else :
		temp_F = 9.0/5.0 * last_temp + 32.0
		return temp_F
