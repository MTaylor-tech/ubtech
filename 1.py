import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT) 
GPIO.output(16,1)
GPIO.output(19,1)
GPIO.output(20,1)
GPIO.output(21,1)

time.sleep(1) #wait 1 second
GPIO.output(16,0) #blue on

time.sleep(1)
GPIO.output(19,0) #green on

time.sleep(1)
GPIO.output(20,0) #yellow on
GPIO.output(16,1) #blue off

time.sleep(1)
GPIO.output(21,0) #red on
GPIO.output(19,1) #green off

time.sleep(1)
GPIO.output(20,1) #yellow off

time.sleep(1)
GPIO.output(21,1) #red off

GPIO.cleanup()
