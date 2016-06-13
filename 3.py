import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
led_channels = [16,19,20,21] # arrays
buttons_channels = [23,24,25]

GPIO.setup(led_channels,GPIO.OUT)
GPIO.output(led_channels,1)
GPIO.setup(buttons_channels,GPIO.IN)

time.sleep(1)
GPIO.output(16,0)

time.sleep(1)
GPIO.output(19,0)

time.sleep(1)
GPIO.output(20,0)
GPIO.output(16,1)

time.sleep(1)
GPIO.output(21,0)
GPIO.output(19,1)

time.sleep(1)
GPIO.output(20,1)

time.sleep(1)
GPIO.output(21,1)

areTheyOn = False
chan16 = 1 #blue
chan19 = 1
chan20 = 1
chan21 = 1
while (GPIO.input(25)):   #while switch is on
	if (GPIO.input(23)) :   # if red button is pressed
		#GPIO.output(led_channels,1)
                
	elif (GPIO.input(24)): # if yellow button is pressed
		GPIO.output(led_channels,0)
	


GPIO.cleanup()
