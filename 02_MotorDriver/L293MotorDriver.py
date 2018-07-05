import RPi.GPIO as GPIO
from time import sleep


class L293MotorDriver:
    """Common Motor driver class for the L293 H-bridge. Its written for the use on a RPi3."""

    def __init__(self, _enableGpioPin, _ch1A_GpioPin, _ch2A_GpioPin):
        GPIO.cleanup()
        self.enableGpioPin = _enableGpioPin
        self.pwmPinCh1 = _ch1A_GpioPin
        self.pwmPinCh2 = _ch2A_GpioPin
        self.setupGPIOs()

    def __del__(self):
        print "l293 delete!"
        self.resetAllPinsToDefault()
        ##GPIO.cleanup()

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

    def forward(self):
        print "forward"
        # channel 1 of th L293 drives the Motor to go forward
        self.enablePwmPins()
        # set the other channel low before forward Channel is set to high
        GPIO.output(self.pwmPinCh2, GPIO.LOW)
        GPIO.output(self.pwmPinCh1, GPIO.HIGH)


    def backward(self):
        print "backward"
        self.enablePwmPins()
        # set the other channel low before forward Channel is set to high
        GPIO.output(self.pwmPinCh1, GPIO.LOW)
        GPIO.output(self.pwmPinCh2, GPIO.HIGH)


    def setAllPinsLOW(self):
        print "set all pins to low"
        GPIO.output(self.enableGpioPin, GPIO.LOW)
        GPIO.output(self.pwmPinCh1, GPIO.LOW)
        GPIO.output(self.pwmPinCh2, GPIO.LOW)

    def resetAllPinsToDefault(self):
        print "set all pins to low"
        self.setAllPinsLOW()
        GPIO.setup(self.enableGpioPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pwmPinCh1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pwmPinCh2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



def main():
    print "###### Start the Packeage tests!!! ######"

    try:
        motor = L293MotorDriver(12, 6, 5)
        motor.forward()
        sleep(8)
        #motor.backward()
        sleep(2)
    except KeyboardInterrupt:
        print "clean up all instanes"
        del motor
    finally:
        print "clean up everthing else"
        del motor


if __name__ == "__main__":
    main()
