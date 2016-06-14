#the following lines will allow you to use buttons and leds
import btnlib as btn
import ledlib as led
import time

led.startup()

while btn.isOn(btn.switch) :
  #put your code here

print "Goodbye"
btn.GPIO.cleanup()
