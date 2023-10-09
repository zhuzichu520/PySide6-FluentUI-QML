# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QObject,Slot,QDataStream,QStandardPaths,QSettings,QByteArray,QIODevice,QCoreApplication,QCoreApplication
from define import singleton

@singleton
class SettingsHelper(QObject):
    def __init__(self, par=None):
        super().__init__(parent=par)
        self.__settings = QSettings()
            
    def init(self):
        applicationPath = QCoreApplication.applicationFilePath()
        iniFileName = "example.ini"
        iniFilePath = QStandardPaths.writableLocation(QStandardPaths.AppLocalDataLocation)+"/"+iniFileName
        self.__settings = QSettings(iniFilePath, QSettings.IniFormat)
        print("Application configuration file path ->", self.__settings.fileName)

    def save(self, key, val):
        data = QByteArray()
        stream = QDataStream(data, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_5_6)
        stream.writeQVariant(val)
        self.__settings.setValue(key, data)

    def get(self, key):
        data = QByteArray(self.__settings.value(key)) 
        if data.isEmpty():
            return
        stream = QDataStream(data)
        stream.setVersion(QDataStream.Qt_5_6)
        val = stream.readQVariant()
        return val
    
    @Slot(result=str)
    def getRender(self):
        return self.get("render")

    @Slot(str)
    def saveRender(self,render):
        self.save("render",render)

    @Slot(result=int)
    def getDarkMode(self):
        return self.get("darkMode")
    
    @Slot(int)
    def saveDarkMode(self,darkMode):
        self.save("darkMode",darkMode)