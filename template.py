#the following lines are necessary and will allow you to use buttons and leds
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

print("Red on and off")
#to turn on a single led, use a command like this:
led.turn_on(led.red)
#your choices for leds are led.red, led.orange, led.yellow,
#     led.green, led.blue, led.purple, and led.white
time.sleep(2)
#to turn it off:
led.turn_off(led.red)
time.sleep(1)

print("Yellow with isOn test")
#the led.isOn(led) function tells you if a particular led is currently on
# same led choices
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
time.sleep(1)

print("Green and blue switch")
#the led.switch(led) function knows whether an led is on or off and switches its value
# same led choices
led.turn_on(led.green)
time.sleep(2)
led.switch(led.green)
led.switch(led.blue)
time.sleep(2)
led.switch(led.blue)
time.sleep(1)

print("Blink")
#the led.blink(led, number_of_times, seconds_between_blinks) blinks an led on and off
# default is (led.white, 5, 0.25)
led.blink() #blinks the white led 5 times for 0.25 seconds
led.blink(led.purple, 50, 0.01) #blinks the purple led 50 times in 1 second (1/100 of a second pulse length)

print("If switch is on, press yellow for yellow and red for red")
#the btn.isOn(btn) function tells you if a particular button is being pressed or if a switch is on
#your choices for buttons are currently btn.red, btn.yellow, btn.switch
while btn.isOn(btn.switch) :
  if btn.isOn(btn.red):
    led.switch(led.red)
  if btn.isOn(btn.yellow) :
    led.switch(led.yellow)
  time.sleep(0.25) #this line keeps it from checking too fast and mistaking a long press for multiple presses

print("Goodbye")
btn.GPIO.cleanup()
