#A library to operate the IR sensor and led on our RPi
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

led = 6 #what pin is the led connected to
rcv = 5 #what pin is the receiver connected to

GPIO.setup(led,GPIO.OUT)
GPIO.setup(rcv,GPIO.IN)

def receive_message() :
  print("can't receive at this time")
  
def send_message() :
  print("can't send yet")
