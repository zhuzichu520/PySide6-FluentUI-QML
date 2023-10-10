# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QObject, Signal, Property
from PySide6.QtQml import (QmlNamedElement)

QML_IMPORT_NAME = "example"
QML_IMPORT_MAJOR_VERSION = 1


@QmlNamedElement("FileWatcher")
class FileWatcher(QObject):
    def __init__(self):
        QObject.__init__(self)
        pass
