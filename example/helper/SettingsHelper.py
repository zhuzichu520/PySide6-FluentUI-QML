from PySide6.QtCore import QObject, Slot, QStandardPaths, QSettings
from PySide6.QtGui import QGuiApplication

from FluentUI.Singleton import Singleton


# noinspection PyPep8Naming
@Singleton
class SettingsHelper(QObject):
    def __init__(self):
        super().__init__(QGuiApplication.instance())
        self._settings = QSettings()
        iniFileName = "example.ini"
        iniFilePath = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppLocalDataLocation) + "/" + iniFileName
        self._settings = QSettings(iniFilePath, QSettings.Format.IniFormat)

    def _save(self, key, val):
        self._settings.setValue(key, val)

    def _get(self, key, default):
        data = self._settings.value(key)
        if data is None:
            return default
        return data

    @Slot(result=int)
    def getDarkMode(self):
        return int(self._get("darkMode", 0))

    @Slot(int)
    def saveDarkMode(self, darkMode: int):
        self._save("darkMode", darkMode)

    @Slot(result=bool)
    def getUseSystemAppBar(self):
        return bool(self._get('useSystemAppBar', "false") == "true")

    @Slot(bool)
    def saveUseSystemAppBar(self, useSystemAppBar: bool):
        self._save("useSystemAppBar", useSystemAppBar)

    @Slot(result=str)
    def getLanguage(self):
        return str(self._get("language", "en_US"))

    @Slot(str)
    def saveLanguage(self, language: str):
        self._save("language", language)
