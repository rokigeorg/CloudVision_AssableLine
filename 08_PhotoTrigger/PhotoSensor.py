import RPi.GPIO as GPIO
from time import sleep

class PhotoSensor:

    def __init__(self,  _ldrInput, _laserOutput):
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
        if GPIO.input(self.LdrPin):
            return False
        else:
            return True

    def setAllPinsLOW(self):
        print "set all pins to low"
        GPIO.output(self.LaserPin, GPIO.LOW)

def main():
    trig = PhotoSensor(27, 22)
    trig.laserOn()
    print 'cleanup the GPIOs'

    try:
        while True:
            if trig.photoTrigger()==True:
                print 'photo triggered'
                sleep(2)
                #capture a photo
            sleep(1)
            print "i"

    except KeyboardInterrupt:
        print 'cleanup the GPIOs'
        trig.setAllPinsLOW()
        del trig
    
    finally:
        print 'cleanup the GPIOs'
        trig.setAllPinsLOW()
        del trig

if __name__ == '__main__':
    main()
