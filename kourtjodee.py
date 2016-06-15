#the following lines will allow you to use buttons and leds
import btnlib as btn
import ledlib as led
import time

led.startup()

while btn.isOn(btn.switch) :
	led.turn_on_all()
	time.sleep(1)
	led.turn_off_all()
	led.turn_on(led.green)
	time.sleep(1)
	led.turn_on(led.blue)
	time.sleep(.5)
	led.turn_on(led.purple)
	time.sleep(.5)
	led.turn_on(led.red)
	time.sleep(.2)
	led.turn_on_all()
	time.sleep(1)
	led.turn_on(led.blue)
	time.sleep(.2)
	led.turn_on(led.blue)
	time.sleep(.2)
	led.turn_on(led.blue)
	time.sleep(.2)
	led.turn_on(led.blue)
	led.sleep(.5)
	led.blink(led.purple, 7, 3)


print "Goodbye"
btn.GPIO.cleanup()
