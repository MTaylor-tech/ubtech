#https://github.com/majikpig/ubtech/

#setup and imports
import btnlib as btn;
import ledlib as led;
import laserlib as laser;
import time;
import RPi.GPIO as GPIO

# LCD setup
import lcddriver;
GPIO.setmode(GPIO.BCM);
GPIO.setup(18,GPIO.OUT);
GPIO.output(18,True);
lcd = lcddriver.lcd();

#Start coding
#Show Welcome Message
lcd.lcd_display_string("WELCOME!!",1);
time.sleep(5);
lcd.lcd_clear();
#Start While loop until switch is turned off
while btn.isOn(btn.switch) :
	sam = 0;
	laser.on();
	time.sleep(2);
	laser.off();
	time.sleep(0.25);
	if btn.isOn(btn.red):
		if btn.isOn(btn.yellow): # if yellow and red it pressed 
			laser.on();
			time.sleep(0.10);
			laser.off();
			time.sleep(0.10);
		else: #if read button pressed without yellow
			led.blink(led.red, 50, 0.1);
			led.blink(led.orange, 50, 0.1);
			led.blink(led.yellow, 50, 0.1);
			led.blink(led.green, 50, 0.1);
			led.blink(led.blue, 50, 0.1);
			led.blink(led.purple, 50, 0.1);
			led.blink();
	if btn.isOn(btn.yellow):
		while(sam == 0):
			led.turn_on(led.red);
			led.turn_on(led.yellow);
			led.turn_on(led.blue);
			led.turn_on(led.white);
			time.sleep(3);
			sam = 1;		
		led.switch(lcd.red);
		led.switch(lcd.orange);
		led.switch(lcd.yellow);
		led.switch(lcd.green);
		led.switch(lcd.blue);
		led.switch(lcd.purple);
		led.switch(lcd.white);
			
print "Goodbye"
btn.GPIO.cleanup()
