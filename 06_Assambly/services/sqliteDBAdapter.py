import sqlite3
from time import gmtime, strftime
import sys


class SqlImgEntry():

    def __init__(self, _filename, _pathWithImgFileName, _imgTags):
        self.filename = _filename
        self.sufix = self.extractSuffix()
        self.pathWithImgFileName = _pathWithImgFileName
        # self.rawbits = self.loadImgAsBlob()
        self.isCircle = self.containsCircleTag(_imgTags)
        self.csvlabels = _imgTags

        self.asDict = {'filename': self.filename, 'sufix': self.sufix,
                       'pathtopic': self.pathWithImgFileName,
                       'rawbits': self.loadImgAsBlob(),
                       'isCircle': self.isCircle,
                       'csvlabels': self.createCsvString(_imgTags)}

    def containsCircleTag(self, labels):
        for elm in labels:
            if "Circle" in elm.description:
                return 1
        return 0

    def extractSuffix(self):
        s = self.filename.rfind(".")
        e = len(self.filename)
        return self.filename[s: e]

    def loadImgAsBlob(self):
        file = open(self.pathWithImgFileName, "rb")
        blob = sqlite3.Binary(file.read())
        file.close()
        return  blob


    def createCsvString(self, _imgTagsList):
        print(_imgTagsList)
        return ",".join(str(elm.description) for elm in _imgTagsList)

    def log(self, msg):
        print("> Log [SqlImgEntry]: " + msg)


class SqliteDBAdapter():
    def __init__(self, _dBname, _pathWithDBname=""):
        self.dBname = _dBname
        self.pathWithDBname = "/home/pi/EmbeddedSystemsProject/06_Assambly/storage/" + _dBname
        self.conn = None
        self.cursor = None

    def log(self, msg):
        print("> Log [sqliteDBAdapter.py]: " + msg)

    def connectToDB(self):
        self.log(self.pathWithDBname)
        # create or connect to database
        self.conn = sqlite3.connect(self.pathWithDBname)
        # get the curser to do stuff in the db
        self.cursor = self.conn.cursor()

    def saveImgEntry(self, sqlImgEntry):
        # imgEntry = {'filename': "pic_16.png", 'sufix': "jpg", 'pathtopic': '/test', 'rawbits': '', 'isCircle': '1', 'csvlabels': 'ein, zwei, drei'}

        self.cursor.execute(
            "INSERT INTO Bilder(filename, sufix , pathtopic, rawbits, isCircle, csvlabels )  VALUES ( :filename, :sufix, :pathtopic, :rawbits, :isCircle, :csvlabels)",
            sqlImgEntry.asDict)

        self.conn.commit()
        self.conn.close()
