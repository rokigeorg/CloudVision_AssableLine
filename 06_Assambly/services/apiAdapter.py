import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "account.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/EmbeddedSystemsProject/06_Assambly/services/account.json"


class ApiAdapter:
    def __init__(self, _runMode):
        self.log("hey")
        self.client = vision.ImageAnnotatorClient()
        self.content = list()
        self.runMode = _runMode
        self.isPRODUCTION_MODE = True
        self.isDEBUG_MODE = False

    def detect_text(self, path):
        """Detects text in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        self.log('Texts:')

        if self.runMode == self.isDEBUG_MODE:

            for text in texts:
                print('\n"{}"'.format(text.description))

                vertices = (['({},{})'.format(vertex.x, vertex.y)
                             for vertex in text.bounding_poly.vertices])

                print('bounds: {}'.format(','.join(vertices)))

    def loadImageIntoMemory(self, _fileName):
        # Loads the image into memory
        with io.open(_fileName, 'rb') as image_file:
            self.content = image_file.read()

    def sendRequestToCloudApi(self):
        image = types.Image(content=self.content)

        # Performs label detection on the image file
        response = self.client.label_detection(image=image)
        labels = response.label_annotations

        if self.runMode == self.isDEBUG_MODE:
            print('Labels:')
            for label in labels:
                print(label.description)
        return labels

    def log(self, msg):
        print("> Log [ApiAdapter.py]: " + msg)
