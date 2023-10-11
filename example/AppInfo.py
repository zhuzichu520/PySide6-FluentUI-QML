# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QObject, Signal, Property
from define import Singleton


@Singleton
class AppInfo(QObject):

    versionChanged = Signal()

    def __init__(self):
        QObject.__init__(self)
        self._version = "1.6.0"

    @Property(str, notify=versionChanged)
    def version(self):
        return self._version

    @version.setter
    def version(self, val):
        self._version = val
        self.versionChanged.emit()
