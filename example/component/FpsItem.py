# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QObject, Signal, Property
from PySide6.QtQuick import QQuickPaintedItem
from PySide6.QtQml import (QmlNamedElement)

QML_IMPORT_NAME = "example"
QML_IMPORT_MAJOR_VERSION = 1


@QmlNamedElement("FpsItem")
class FpsItem(QQuickPaintedItem):
    def __init__(self):
        QQuickPaintedItem.__init__(self)
        self._fps = 0
        pass

    fps_changed = Signal()

    @Property(int)
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, val):
        self._fps = val
        self.fps_changed.emit()
