import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor12EN = 2
Motor1A = 3
Motor2A = 4
 
GPIO.setup(Motor12EN,GPIO.OUT)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
 
print "Turning motor on"
GPIO.output(Motor12EN,GPIO.HIGH)
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor2A,GPIO.HIGH)
 
sleep(2)
 
print "Stopping motor"
GPIO.output(Motor2A,GPIO.LOW)
 
GPIO.cleanup()
