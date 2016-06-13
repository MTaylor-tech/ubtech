import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

red = 23
yellow = 24
switch = 25
btn_pins = [red,yellow,switch]
GPIO.setup(btn_pins,GPIO.IN)

def isOn(btn) :
  if btn in btn_pins :
    if(GPIO.input(btn)) :
      print("On")
      return True
    else :
      return False
  else :
    print("Not a valid button")

