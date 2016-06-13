import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

blue = 16
green = 19
yellow = 20
red = 21
blue_on = False
green_on = False
yellow_on = False
red_on = False

led_pins = [blue, green, yellow, red]
GPIO.setup(led_pins, GPIO.OUT)

def isOn(led) :
  if led == blue :
    return blue_on
  elif led == green :
    return green_on
  elif led == yellow :
    return yellow_on
  elif led == red :
    return red_on
  else :
    return false

def turn_on(led):
  if led in led_pins :
    GPIO.output(led,True)
    if led == blue :
      blue_on = True
    elif led == green :
      green_on = True
    elif led == yellow :
      yellow_on = True
    elif led == red :
      red_on = True
  
def turn_off(led):
  if led in led_pins :
    GPIO.output(led,False)
    if led == blue :
      blue_on = False
    elif led == green :
      green_on = False
    elif led == yellow :
      yellow_on = False
    elif led == red :
      red_on = False

def turn_on_all():
  GPIO.output(led_pins,True)
  blue_on = True
  green_on = True
  yellow_on = True
  red_on = True
  
def turn_off_all():
  GPIO.output(led_pins,False)
  blue_on = False
  green_on = False
  yellow_on = False
  red_on = False

def switch(led) :
  if led in led_pins :
    if isOn(led) :
      turn_off(led)
    else :
      turn_on(led)

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

