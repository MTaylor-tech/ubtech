import tempsensor
import lcddriver
import time
import RPi.GPIO as GPIO 
import btnlib as btn


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT) #channel 18 turns on the backlight of the LCD

lcd = lcddriver.lcd() #sets up the LCD screen

while btn.isOn(btn.switch): #while the switch is on:
	if btn.isOn(btn.yellow) : #if the yellow button gets pressed
		GPIO.output(18, True) #turns on the backlight
		temp = -700
		humid = -700
		tempsensor.print_temp()
		temp = tempsensor.tempF()
		humid = tempsensor.humid()
		if temp > -700 :
			lcd.lcd_display_string("Temperature: %d F" % temp,1)
		if humid > -700 :
			lcd.lcd_display_string("Humidity: %d %%" % humid,2)
		time.sleep(5)
		GPIO.output(18, False) #turns off the backlight after 5 secs
	time.sleep(0.1)

lcd.lcd_clear()
GPIO.cleanup()
