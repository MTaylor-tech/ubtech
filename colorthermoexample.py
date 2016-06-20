import tempsensor
import time
import btnlib as btn
import ledlib as led

red = 80
orange = 75
yellow = 70
green = 65
blue = 60
purple = 55

while btn.isOn(btn.switch): #while the switch is on:
	led.turn_on(led.white)
	temp = tempsensor.tempF() #get the temp
	print temp
	if temp > red :
		led.turn_on_all()
	elif temp > orange :
		led.turn_off(led.red)
		led.turn_on(led.orange)
		led.turn_on(led.yellow)
		led.turn_on(led.green)
		led.turn_on(led.blue)
		led.turn_on(led.purple)
	elif temp > yellow :
		led.turn_off(led.red)
		led.turn_off(led.orange)
		led.turn_on(led.yellow)
		led.turn_on(led.green)
		led.turn_on(led.blue)
		led.turn_on(led.purple)
	elif temp > green :
		led.turn_off(led.red)
		led.turn_off(led.orange)
		led.turn_off(led.yellow)
		led.turn_on(led.green)
		led.turn_on(led.blue)
		led.turn_on(led.purple)
	elif temp > blue :
		led.turn_off(led.red)
		led.turn_off(led.orange)
		led.turn_off(led.yellow)
		led.turn_off(led.green)
		led.turn_on(led.blue)
		led.turn_on(led.purple)
	elif temp > purple :
		led.turn_off(led.red)
		led.turn_off(led.orange)
		led.turn_off(led.yellow)
		led.turn_off(led.green)
		led.turn_off(led.blue)
		led.turn_on(led.purple)
	else :
		led.turn_off_all()
		led.turn_on(led.white)

	time.sleep(0.5)
	led.turn_off(led.white)
	time.sleep(0.5)

led.GPIO.cleanup()
