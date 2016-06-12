import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

blue = 16
green = 19
yellow = 20
red = 21
#red_btn = 23
#yellow_btn = 24
#switch = 25

led_pins = [blue, green, yellow, red]
#button_pins = [red_btn, yellow_btn, switch]
GPIO.setup(led_pins, GPIO.OUT)

def turn_on(led):
  GPIO.output(led,0)
  
def turn_off(led):
  GPIO.output(led,1)

def turn_on_all():
  GPIO.output(led_pins,0)
  
def turn_off_all():
  GPIO.output(led_pins,1)

def startup():
  print("Startup sequence")
  time.sleep(1)
  turn_on(blue)
  time.sleep(1)
  turn_on(green)
  time.sleep(1)
  turn_off(blue)
  turn_on(yellow)
  time.sleep(1)
  turn_off(green)
  turn_on(red)
  time.sleep(1)
  turn_off(yellow)
  time.sleep(1)
  turn_off(red)

