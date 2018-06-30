import RPi.GPIO as GPIO
from time import sleep


class LedDriver:
    """Common led driver class for the L293 H-bridge. Its written for the use on a RPi3."""

    def __init__(self, _enableGpioPin, _ch1A_GpioPin, _ch2A_GpioPin):
        self.enableGpioPin = _enableGpioPin
        self.pwmPinCh1 = _ch1A_GpioPin
        self.pwmPinCh2 = _ch2A_GpioPin
        self.setupGPIOs()

    def __del__(self):
        self.setAllPinsLOW()
        self.log("driver delete!")

    def setupGPIOs(self):
        # tell the RPi that we want toe specify all pins as GPIOpins of the Boardcom chip (BCM)
        # and not the board layout pins of the pin headers
        GPIO.setmode(GPIO.BCM)
        # set up the output pins
        GPIO.setup(self.enableGpioPin, GPIO.OUT)
        GPIO.setup(self.pwmPinCh1, GPIO.OUT)
        GPIO.setup(self.pwmPinCh2, GPIO.OUT)

    def enablePwmPins(self):
        GPIO.output(self.enableGpioPin, GPIO.HIGH)

    def disablePwmPins(self):
        GPIO.output(self.enableGpioPin, GPIO.LOW)

    def switchOn(self):
        # channel 1 of th L293 drives the Motor to go forward
        self.enablePwmPins()
        # set the other channel low before forward Channel is set to high
        GPIO.output(self.pwmPinCh1, GPIO.LOW)
        GPIO.output(self.pwmPinCh2, GPIO.HIGH)

    def switchOff(self):
        # channel 1 of th L293 drives the Motor to go forward
        self.enablePwmPins()
        # set the other channel low before forward Channel is set to high
        GPIO.output(self.pwmPinCh1, GPIO.LOW)
        GPIO.output(self.pwmPinCh2, GPIO.LOW)

    def setAllPinsLOW(self):
        self.log("set all pins to low")
        GPIO.output(self.enableGpioPin, GPIO.LOW)
        GPIO.output(self.pwmPinCh1, GPIO.LOW)
        GPIO.output(self.pwmPinCh2, GPIO.LOW)

    def resetAllPinsToDefault(self):
        self.log("set all pins to low")
        self.setAllPinsLOW()
        GPIO.setup(self.enableGpioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pwmPinCh1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pwmPinCh2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def log(self, msg):
        print("> Log [L293LedDriver.py]: " + msg)


def main():
    print("###### Start the Packeage tests!!! ######")

    try:
        light = LedDriver(13, 6, 5)
        light.switchOn()
        sleep(5)
        light.switchOff()

    except KeyboardInterrupt:
        print("clean up all instanes")
        del light
    finally:
        print("clean up everthing else")
        del light


if __name__ == "__main__":
    main()


