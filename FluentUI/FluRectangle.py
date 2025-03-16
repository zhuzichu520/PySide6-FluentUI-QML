from PySide6.QtGui import QPainter, QColor, QPainterPath
from PySide6.QtCore import Signal, Property, QPointF, QSize, QRectF
from PySide6.QtQuick import QQuickPaintedItem

'''
The FluRectangle class is responsible for drawing the rectangular area of a rectangular
'''


class FluRectangle(QQuickPaintedItem):
    colorChanged = Signal()
    radiusChanged = Signal()

    @Property(QColor, notify=colorChanged)
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.colorChanged.emit()

    @Property(list, notify=radiusChanged)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.radiusChanged.emit()

    def __init__(self):
        QQuickPaintedItem.__init__(self)
        self._color = QColor(255, 255, 255, 255)
        self._radius = [0, 0, 0, 0]
        self.colorChanged.connect(lambda: self.update())
        self.radiusChanged.connect(lambda: self.update())

    def paint(self, painter: QPainter):
        painter.save()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        rect = self.boundingRect()
        radius = self._radius
        path.moveTo(rect.bottomRight() - QPointF(0, radius[2]))
        path.lineTo(rect.topRight() + QPointF(0, radius[1]))
        path.arcTo(QRectF(QPointF(rect.topRight() - QPointF(radius[1] * 2, 0)), QSize(radius[1] * 2, radius[1] * 2)), 0, 90)
        path.lineTo(rect.topLeft() + QPointF(radius[0], 0))
        path.arcTo(QRectF(QPointF(rect.topLeft()), QSize(radius[0] * 2, radius[0] * 2)), 90, 90)
        path.lineTo(rect.bottomLeft() - QPointF(0, radius[3]))
        path.arcTo(QRectF(QPointF(rect.bottomLeft() - QPointF(0, radius[3] * 2)), QSize(radius[3] * 2, radius[3] * 2)), 180, 90)
        path.lineTo(rect.bottomRight() - QPointF(radius[2], 0))
        path.arcTo(QRectF(QPointF(rect.bottomRight() - QPointF(radius[2] * 2, radius[2] * 2)), QSize(radius[2] * 2, radius[2] * 2)), 270, 90)
        painter.fillPath(path, self._color)
        painter.restore()
