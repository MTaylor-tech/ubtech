#A library to operate the laser on our RPi
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

laser = 22 #the pin that the laser is connected to
GPIO.setup(laser,GPIO.OUT)
GPIO.output(laser,False)
laser_on = False

def isOn() :
  return laser_on

def on() :
  global laser_on
  GPIO.output(laser,True)
  laser_on = True
  
def off() :
  global laser_on
  GPIO.output(laser,False)
  laser_on = False

def switch() :
  if isOn() :
    off()
  else :
    on()
