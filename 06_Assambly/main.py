from driver.L293MotorDriver import L293MotorDriver
import RPi.GPIO as GPIO

def main():
    log("Start")

    try:
        # create all instances
        motor = L293MotorDriver(17, 27, 22)

        # Start the assableline to run forward
        motor.forward()
        motor.disablePwmPins()
    except KeyboardInterrupt:
        log("clean up all instanes")
        del motor
    finally:
        log("clean up everthing else")
        del motor
        GPIO.cleanup()



def log(str):
    print("**** " + str + " ****")


if __name__ == '__main__':
    main()
