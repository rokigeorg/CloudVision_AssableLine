import RPi.GPIO as GPIO

class PhotoTrigger:

    def __init__(self, _laserOutput, _ldrInput):
        self.LaserPin = _laserOutput
        self.LdrPin = _ldrInput
        self.setupGPIOs()

    def setupGPIOs(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LaserPin,GPIO.OUT)
        GPIO.setup(self.LdrPin,GPIO.IN)

    def LaserOn(self):
        GPIO.output(self.LaserPin, GPIO.HIGH)

    def LaserOff(self):
        GPIO.output(self.LaserPin, GPIO.LOW)

    def PhotoTrigger(self):
        if (self.LdrPin == 1):
            return True
        else:
            return False