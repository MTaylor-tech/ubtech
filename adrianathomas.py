#the following lines will allow you to use buttons and leds
import btnlib as btn
import ledlib as led
import time

#the led.startup() function cycles through the leds
led.startup()
time.sleep(1)

print("All on and off")
#to turn on all leds, use the led.turn_on_all() function:
led.turn_on_all()
time.sleep(2)
#to turn off all:
led.turn_off_all()
time.sleep(1)

print("Orange on and off")
#to turn on a single led, use a command like this:
led.turn_on(led.orange)
#your choices for leds are led.orange, led.blue, led.green, led.red
time.sleep(2)
#to turn it off:
led.turn_off(led.orange)
time.sleep(1)

print("Blue with isOn test")
#the led.isOn(led) function tells you if a particular led is currently on
if led.isOn(led.blue):
  print("Blue is on")
else :
  print("Blue is off")
time.sleep(2)
led.turn_on(led.blue)
if led.isOn(led.blue):
  print("Yellow is on")
else :
  print("Blue is off")
time.sleep(5)
led.turn_off(led.blue)
time.sleep(9)

print("Green and purple switch")
#the led.switch(led) function knows whether an led is on or off and switches its value
led.turn_on(led.green)
time.sleep(3)
led.switch(led.green)
led.switch(led.purple)
time.sleep(1)
led.switch(led.purple)
time.sleep(2)

print("If switch is on, press orange for orange and purple for purple")
#the btn.isOn(btn) function tells you if a particular button is being pressed or if a switch is on
#your choices for buttons are currently btn.orange, btn.blue, btn.switch
while btn.isOn(btn.switch) :
  if btn.isOn(btn.red):
    led.switch(led.orange)
  if btn.isOn(btn.yellow) :
    led.switch(led.purple)
  time.sleep(0.50) #this line keeps it from querying too fast and mistaking a long press for multiple presses

print("Goodbye")
btn.GPIO.cleanup()

