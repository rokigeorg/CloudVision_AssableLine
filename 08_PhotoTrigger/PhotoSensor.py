import RPi.GPIO as GPIO
from time import sleep

class PhotoTrigger:

    def __init__(self, _laserOutput, _ldrInput):
        self.LaserPin = _laserOutput
        self.LdrPin = _ldrInput
        self.setupGPIOs()

    def setupGPIOs(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LaserPin,GPIO.OUT)
        GPIO.setup(self.LdrPin,GPIO.IN)

    def laserOn(self):
        GPIO.output(self.LaserPin, GPIO.HIGH)

    def laserOff(self):
        GPIO.output(self.LaserPin, GPIO.LOW)

    def photoTrigger(self):
        if (self.LdrPin == 1):
            return True
        else:
            return False

    def setAllPinsLOW(self):
        print "set all pins to low"
        GPIO.output(self.LaserPin, GPIO.LOW)

def main():
    try:
        trigger = PhotoTrigger()
        trigger.laserOn()
        sleep(5)
        trigger.laserOff()
        sleep(2)
    except KeyboardInterrupt:
        print 'cleanup'
        trigger.setAllPinsLOW()
        del trigger
    finally:
        print 'cleanup'
        trigger.setAllPinsLOW()
        del trigger