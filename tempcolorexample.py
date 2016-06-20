import tempsensor
import time
import btnlib as btn
import ledlib as led

last_temp = 70

while btn.isOn(btn.switch): #while the switch is on:
	temp = tempsensor.tempF() #get the temp
	if temp > last_temp : #if it's gotten warmer
		print "Warmer"
		if led.isOn(led.blue) :
			led.turn_off(led.blue) #turn off blue
		if led.isOn(led.yellow) :
			led.turn_off(led.yellow) #turn off yellow
		led.turn_on(led.red) #turn on red
	elif temp == last_temp : #if it's the same
		print "Same"
		if led.isOn(led.blue) :
			led.turn_off(led.blue) #turn off blue
		if led.isOn(led.red) :
			led.turn_off(led.red) #turn off red
		led.turn_on(led.yellow) #turn on yellow
	elif temp < last_temp : #if it's cooler
		print "Cooler"
		if led.isOn(led.red) :
			led.turn_off(led.red) #turn off red
		if led.isOn(led.yellow) :
			led.turn_off(led.yellow) #turn off yellow
		led.turn_on(led.blue) #turn on blue
	last_temp = temp #set the new temp
	time.sleep(2) #wait 2 seconds before checking again

led.GPIO.cleanup()
