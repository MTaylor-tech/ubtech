import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

blue = 16
green = 19
yellow = 20
red = 21
red_btn = 23
yellow_btn = 24
switch = 25

led_pins = [blue, green, yellow, red]
button_pins = [red_btn, yellow_btn, switch]

