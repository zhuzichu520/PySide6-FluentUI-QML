# This Python file uses the following encoding: utf-8

from PySide6.QtCore import Qt, QTimer, Signal, Property
from PySide6.QtQuick import QQuickPaintedItem
from PySide6.QtQml import (QmlNamedElement)

QML_IMPORT_NAME = "example"
QML_IMPORT_MAJOR_VERSION = 1


@QmlNamedElement("FpsItem")
class FpsItem(QQuickPaintedItem):

    fpsChanged = Signal()

    def __init__(self):
        QQuickPaintedItem.__init__(self)
        self._frameCount: int = 0
        self._fps: int = 0
        self._timer = QTimer()
        self._timer.timeout.connect(lambda: self.onTimeout())
        self.windowChanged.connect(lambda: self.onWindowChanged())
        self._timer.start(1000)

    def frameCountIncrease(self):
        self._frameCount += 1

    def onWindowChanged(self):
        if (self.window()):
            self.window().afterRendering.connect(
                lambda: self.frameCountIncrease(), Qt.ConnectionType.DirectConnection)

    def onTimeout(self):
        self.fps = self._frameCount
        self._frameCount = 0

    @Property(int, notify=fpsChanged)
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, val):
        self._fps = val
        self.fpsChanged.emit()
