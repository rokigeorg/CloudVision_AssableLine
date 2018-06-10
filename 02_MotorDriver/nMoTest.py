import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1E = 20#36
Motor1A = 19#35
Motor1B = 26#37

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

print "Turning motor on"
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.HIGH)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(2)

print "Stopping motor"
GPIO.output(Motor1E, GPIO.LOW)
sleep(2)

print "Turning motor on"
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(2)

print "Stopping motor"
GPIO.output(Motor1E, GPIO.LOW)

GPIO.cleanup()