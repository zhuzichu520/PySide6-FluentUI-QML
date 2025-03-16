from PySide6.QtCore import Slot, Signal, Property, QPoint, QRect, QPropertyAnimation, QPointF, Qt, QSize, QEasingCurve, SIGNAL, SLOT
from PySide6.QtGui import QPainter, QImage, QPainterPath
from PySide6.QtQuick import QQuickPaintedItem, QQuickItem, QQuickItemGrabResult


# noinspection PyTypeChecker,PyPep8Naming
class CircularReveal(QQuickPaintedItem):
    radiusChanged = Signal()
    imageChanged = Signal()
    animationFinished = Signal()
    targetChanged = Signal()

    def __init__(self):
        QQuickPaintedItem.__init__(self)
        self._target: QQuickItem = None
        self._radius: int = 0
        self._source = QImage()
        self._center: QPoint = None
        self._grabResult: QQuickItemGrabResult = None
        self.setVisible(False)
        self._anim = QPropertyAnimation(self, b"radius", self)
        self._anim.setDuration(333)
        self._anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.connect(self._anim, SIGNAL("finished()"), self, SLOT("onAnimaFinish()"))
        self.radiusChanged.connect(lambda: self.update())
        self.destroyed.connect(lambda: self.release())

    def release(self):
        self._anim.deleteLater()
        del self._grabResult
        del self._source

    def onAnimaFinish(self):
        self.update()
        self.setVisible(False)
        self.animationFinished.emit()

    @Property(int, notify=radiusChanged)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.radiusChanged.emit()

    @Property(QQuickItem, notify=targetChanged)
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
        self.targetChanged.emit()

    def paint(self, painter: QPainter):
        if self._source is None:
            return
        painter.save()
        painter.drawImage(QRect(0, 0, self.boundingRect().width(), self.boundingRect().height()), self._source)
        path = QPainterPath()
        path.moveTo(self._center.x(), self._center.y())
        path.addEllipse(QPointF(self._center.x(), self._center.y()), self._radius, self._radius)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)
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
