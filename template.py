#the following lines will allow you to use buttons and leds
import btnlib as btn
import ledlib as led
import time

led.startup()

#to turn on all leds, use the led.turn_on_all() function:
led.turn_on_all()
time.sleep(2)
#to turn off all:
led.turn_off_all()

#to turn on a single led, use a command like this:
led.turn_on(led.red)
#your choices for leds are led.red, led.yellow, led.green, led.blue
time.sleep(2)
#to turn it off:
led.turn_off(led.red)

#the led.isOn(led) function tells you if a particular led is currently on
if led.isOn(led.yellow):
  print("Yellow is on")
else :
  print("Yellow is off")
time.sleep(2)
led.turn_on(led.yellow)
if led.isOn(led.yellow):
  print("Yellow is on")
else :
  print("Yellow is off")
time.sleep(2)
led.turn_off(led.yellow)

#the btn.isOn(btn) function tells you if a particular button is being pressed or if a switch is on
#your choices for buttons are currently btn.red, btn.yellow, btn.switch
while btn.isOn(btn.switch) :
  if btn.isOn(btn.red):
    led.switch(led.red)
  if btn.isOn(btn.yellow) :
    led.switch(led.yellow)

btn.GPIO.cleanup()
