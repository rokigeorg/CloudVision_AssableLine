import RPi.GPIO as GPIO
from time import sleep


class PhotoSensor:

    def __init__(self, _ldrInput):
        self.LdrPin = _ldrInput
        self.setupGPIOs()
        self.isAllowed = True

    def setupGPIOs(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LdrPin, GPIO.IN)

    def photoTrigger(self):
        if GPIO.input(self.LdrPin):
            return False
        else:
            return True

    def checksLdrInputPin(self):
        if self.isAllowed:

            if GPIO.input(self.LdrPin):
                return False
            else:
                return True

        return False

    def setAllPinsLOW(self):
        self.log("set all pins to low")
        GPIO.output(self.LdrPin, GPIO.LOW)

    def stopLdrReading(self):
        self.isAllowed = False

    def startLdrReading(self):
        self.isAllowed = True

    def log(self, msg):
        print("> Log [PhotoSensor.py]: " + msg)


def main():
    trig = PhotoSensor(24, 23)

    try:
        while True:
            if trig.photoTrigger() == True:
                print('photo triggered')
                sleep(2)
                # capture a photo
            sleep(0.1)

    except KeyboardInterrupt:
        print('cleanup the GPIOs')
        trig.setAllPinsLOW()
        del trig

    finally:
        print('cleanup the GPIOs')
        trig.setAllPinsLOW()
        del trig


if __name__ == '__main__':
    main()
