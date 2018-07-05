from driver.L293MotorDriver import L293MotorDriver
from driver.L293LedDriver import LedDriver
from driver.PhotoSensor import PhotoSensor
from picamera import PiCamera
from services.apiAdapter import ApiAdapter
import RPi.GPIO as GPIO
from time import sleep
import time


class Hardware:

    def __init__(self, _motor, _ledFlash, _ldrReader, _camera):
        self.motor = _motor
        self.ledFlash = _ledFlash
        self.ldrReader = _ldrReader
        self.camera = _camera
        self.IMG_DIR_PATH = "/home/pi/EmbeddedSystemsProject/06_Assambly/storage/imgDir/"
        self.DIR_PATH_WITH_IMG_NAME = ""

    def takePhoto(self):
        self.ledFlash.switchOn()

        # picture taking process
        ts = time.gmtime()
        sts = "pic_" + time.strftime("%Y-%m-%d__%H_%M_%S", ts) + ".jpg"
        print(sts)
        self.IMG_DIR_PATH = "/home/pi/EmbeddedSystemsProject/06_Assambly/storage/imgDir/"
        self.DIR_PATH_WITH_IMG_NAME = self.IMG_DIR_PATH + sts
        self.camera.capture(self.DIR_PATH_WITH_IMG_NAME)

        self.ledFlash.switchOff()

    def getPathWithImgName(self):
        log("in getter:" +self.DIR_PATH_WITH_IMG_NAME )
        return self.DIR_PATH_WITH_IMG_NAME


class Network:

    def __init__(self, _apiAdapter, _pathToImg):
        log("==========")
        log(_pathToImg)
        self.apiAdapter = _apiAdapter
        self.DIR_PATH_WITH_IMG_NAME = _pathToImg
        self.fileName = self.extraxedFileName()

    def __del__(self):
        log("Delete network instance...")

    def extraxedFileName(self):
        start = self.DIR_PATH_WITH_IMG_NAME.rfind("/")
        end = len(self.DIR_PATH_WITH_IMG_NAME)
        return self.DIR_PATH_WITH_IMG_NAME[start + 1: end]

    def sendCloudVisionRequest(self):
        self.apiAdapter.loadImageIntoMemory(self.DIR_PATH_WITH_IMG_NAME)
        self.apiAdapter.sendRequestToCloudApi()
        self.apiAdapter.detect_text(self.DIR_PATH_WITH_IMG_NAME)


def main():
    log("Start")
    isObjDetected = False

    try:
        # create all instances
        motor = L293MotorDriver(12, 5, 6)
        ledFlash = LedDriver(21, 16, 20)  # TODO wie lautet die richtige pin belegung
        ldrReader = PhotoSensor(27)
        camera = PiCamera()

        hw = Hardware(motor, ledFlash, ldrReader, camera)
        apiAdapter = ApiAdapter()

        # Start the assableline to run forward

        motor.startPwmForward()
        for i in range(1, 10):
            isObjDetected = ldrReader.checksLdrInputPin()
            log("State of LDRRead: {isObjDetected}".format(isObjDetected=isObjDetected))
            if (isObjDetected):
                # handle take a photo
                hw.takePhoto()

                # handle api request and response
                nw = Network(apiAdapter,hw.getPathWithImgName())
                nw.sendCloudVisionRequest()

                # handle save photo and meta data to database

                # handle reset motor, ldrReader to continue sensoring the assambly line
                ldrReader.stopLdrReading()
            sleep(1)

        motor.stopPwm()
        ledFlash.switchOff()
        motor.disablePwmPins()
    except KeyboardInterrupt:
        log("clean up all instanes")
        del motor
    finally:
        log("clean up everthing else")
        del motor


def log(str):
    print("> Log [Main]: " + str)


if __name__ == '__main__':
    main()
