from driver.L293MotorDriver import L293MotorDriver
from driver.L293LedDriver import LedDriver
from driver.PhotoSensor import PhotoSensor
import RPi.GPIO as GPIO
from time import sleep

def main():
    log("Start")
    isObjDetected = False

    try:
        # create all instances
        motor = L293MotorDriver(19, 12, 6)
        ledFlash = LedDriver(21,16,20)
        photoTrig = PhotoSensor(27)

        # Start the assableline to run forward
        ledFlash.switchOn()
        motor.forward()

        isObjDetected = ledFlash.checksLdrInputPin()

        sleep(3)

        ledFlash.switchOff()
        motor.disablePwmPins()
    except KeyboardInterrupt:
        log("clean up all instanes")
        del motor
    finally:
        log("clean up everthing else")
        del motor




def log(str):
    print("**** " + str + " ****")


if __name__ == '__main__':
    main()
