import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

red = 27
yellow = 17
switch = 25
btn_pins = [red,yellow,switch]
GPIO.setup(btn_pins,GPIO.IN)

def isOn(btn) :
  if btn in btn_pins :
    if(GPIO.input(btn)) :
      return True
    else :
      return False
  else :
    print("Not a valid button")

