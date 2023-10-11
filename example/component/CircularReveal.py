# This Python file uses the following encoding: utf-8
from typing import Tuple
from PySide6.QtCore import QObject, Slot, Signal, Property, QPoint, QRect, QPropertyAnimation, QPointF, Qt, QSize, QEasingCurve
from PySide6.QtGui import QPainter, QImage, QPainterPath
from PySide6.QtQuick import QQuickPaintedItem, QQuickItem, QQuickItemGrabResult, QSharedPointer_QQuickItemGrabResult
from PySide6.QtQml import (QmlNamedElement)

QML_IMPORT_NAME = "example"
QML_IMPORT_MAJOR_VERSION = 1


@QmlNamedElement("CircularReveal")
class CircularReveal(QQuickPaintedItem):

    imageChanged = Signal()
    animationFinished = Signal()
    targetChanged = Signal()
    radiusChanged = Signal()

    def __init__(self):
        QQuickPaintedItem.__init__(self)
        self._target: QQuickItem = None
        self._radius: int = 0
        self._source: QImage = QImage()
        self._anim: QPropertyAnimation = QPropertyAnimation(
            self, b"radius", self)
        self._center: QPoint = None
        self._grabResult: QSharedPointer_QQuickItemGrabResult = None
        self.setVisible(False)
        self._anim.setDuration(333)
        self._anim.setEasingCurve(QEasingCurve.Type.OutCubic)

        def animFinish():
            self.update()
            self.setVisible(False)
            self.animationFinished.emit()
        self._anim.finished.connect(lambda: animFinish())
        self.radiusChanged.connect(lambda: self.update())

    def paint(self, painter: QPainter):
        if (self._source == None):
            return
        painter.save()
        painter.drawImage(
            QRect(0, 0, self.boundingRect().width(), self.boundingRect().height()), self._source)
        path = QPainterPath()
        path.moveTo(self._center.x(), self._center.y())
        path.addEllipse(QPointF(self._center.x(), self._center.y()),
                        self._radius, self._radius)
        painter.setCompositionMode(
            QPainter.CompositionMode.CompositionMode_Clear)
        painter.fillPath(path, Qt.GlobalColor.black)
        painter.restore()

    @Slot()
    def handleGrabResult(self):
        self._grabResult.data().image().swap(self._source)
        self.update()
        self.setVisible(True)
        self.imageChanged.emit()
        self._anim.start()

    @Slot(int, int, QPoint, int)
    def start(self, w: int, h: int, center: QPoint, radius: int):
        self._anim.setStartValue(0)
        self._anim.setEndValue(radius)
        self._center = center
        self._grabResult = self._target.grabToImage(QSize(w, h))
        self._grabResult.data().ready.connect(self.handleGrabResult)

    @Property(QQuickItem, notify=targetChanged)
    def target(self):
        return self._target

    @target.setter
    def target(self, val):
        self._target = val
        self.targetChanged.emit()

    @Property(int, notify=radiusChanged)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        self._radius = val
        self.radiusChanged.emit()
