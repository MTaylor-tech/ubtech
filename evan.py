import btnlib as btn
import ledlib as led
import time

#the led.startup() function cycles through the leds
#led.startup()
time.sleep(1)

print("Hello")
#to turn on all leds, use the led.turn_on_all() function:
led.turn_on_all()
time.sleep(2)
#to turn off all:
led.turn_off_all()
time.sleep(1)
led.turn_off_all()
time.sleep(1)
led.turn_on_all()
time.sleep(2)
led.turn_off_all()
time.sleep(1)
led.turn_on_all()
time.sleep(2)
led.turn_off_all()
time.sleep(1)
led.turn_on_all()
time.sleep(2)

print("Red on and off")
#to turn on a single led, use a command like this:
#your choices for leds are led.red, led.orange, led.yellow,
#     led.green, led.blue, led.purple, and led.white
led.turn_on(led.red)
time.sleep(2)
led.turn_on(led.orange)
time.sleep(2)
led.turn_on(led.yellow)
time.sleep(2)
led.turn_off(led.red)
time.sleep(1)
led.turn_on(led.green)
time.sleep(2)
led.turn_off(led.orange)
time.sleep(1)
led.turn_on(led.blue)
time.sleep(2)
led.turn_off(led.yellow)
time.sleep(1)
led.turn_on(led.purple)
time.sleep(2)
led.turn_off(led.green)
time.sleep(1)
led.turn_on(led.white)
time.sleep(2)
led.turn_off(led.blue)
time.sleep(1)
led.turn_off(led.purple)
time.sleep(1)
led.turn_off(led.white)
time.sleep(1)


print("Goodbye")
btn.GPIO.cleanup() 
