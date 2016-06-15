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

def print_temp() :
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
    
    
def tempC() :
	result = instance.read()
	if result.is_valid() :
		return result.temperature
		

def humid() :
	result = instance.read()
	if result.is_valid() :
		return result.humidity
	
def tempF() :
	result = instance.read()
	if result.is_valid() :
		temp_F = 9.0/5.0 * result.temperature + 32
		return temp_F
