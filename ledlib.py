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
  print("Checking led")
  if led == blue :
    print("Blue")
    print blue_on
    return blue_on
  elif led == green :
    print("Green")
    print green_on
    return green_on
  elif led == yellow :
    print("Yellow")
    print yellow_on
    return yellow_on
  elif led == red :
    print("Red")
    print red_on
    return red_on
  else :
    print("Not a valid LED")
    return False

def turn_on(led):
  if led in led_pins :
    print("Turning on LED")
    GPIO.output(led,True)
    if led == blue :
      print "Blue"
      blue_on = True
    elif led == green :
      print "Green"
      green_on = True
    elif led == yellow :
      print "Yellow"
      yellow_on = True
    elif led == red :
      print "Red"
      red_on = True
  else :
    print("Not in LED List")
  
def turn_off(led):
  global blue_on
  global green_on
  global red_on
  global yellow_on
  if led in led_pins :
    print("Turning off LED")
    GPIO.output(led,False)
    if led == blue :
      print "Blue"
      blue_on = False
    elif led == green :
      print "Green"
      green_on = False
    elif led == yellow :
      print "Yellow"
      yellow_on = False
    elif led == red :
      print "Red"
      red_on = False
  else :
    print("Not in LED List")

def turn_on_all():
  global blue_on
  global green_on
  global red_on
  global yellow_on
  print("Turning on all")
  GPIO.output(led_pins,True)
  blue_on = True
  green_on = True
  yellow_on = True
  red_on = True
  
def turn_off_all():
  global blue_on
  global green_on
  global red_on
  global yellow_on
  print("Turning off all")
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
  else :
    print("Not in LED List")

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

