# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QObject, Signal, Property
from define import Singleton, PropertyAuto


@Singleton
class AppInfo(QObject):

    def __init__(self):
        QObject.__init__(self)
        self._version = "1.6.0"

    version_changed = Signal()

    @Property(str)
    def version(self):
        return self._version

    @version.setter
    def version(self, val):
        self._version = val
        self.version_changed.emit()
