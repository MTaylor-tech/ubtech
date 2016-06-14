import lcddriver
import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

GPIO.output(18,True)

lcd = lcddriver.lcd()

lcd.lcd_display_string("Hello world", 1)
lcd.lcd_display_string("My name is", 2)

sleep(10)

lcd.lcd_clear()
GPIO.cleanup()
