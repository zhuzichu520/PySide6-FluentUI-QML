from PySide6.QtCore import Signal, Property, QPoint, QRectF
from PySide6.QtGui import QColor, QFont, QFontMetricsF
from PySide6.QtQuick import QQuickPaintedItem

from FluentUI.FluTextStyle import FluTextStyle


# noinspection PyCallingNonCallable,PyPropertyAccess,PyPep8Naming
class FluWatermark(QQuickPaintedItem):
    textChanged = Signal()
    gapChanged = Signal()
    offsetChanged = Signal()
    textColorChanged = Signal()
    rotateChanged = Signal()
    textSizeChanged = Signal()

    def __init__(self):
        QQuickPaintedItem.__init__(self)
        self._text: str = ""
        self._gap: QPoint = QPoint(100, 100)
        self._offset: QPoint = QPoint(self._gap.x() / 2, self._gap.y() / 2)
        self._textColor: QColor = QColor(222, 222, 222, 222)
        self._rotate: int = 22
        self._textSize: int = 16
        self.textColorChanged.connect(lambda: self.update())
        self.gapChanged.connect(lambda: self.update())
        self.offsetChanged.connect(lambda: self.update())
        self.textChanged.connect(lambda: self.update())
        self.rotateChanged.connect(lambda: self.update())
        self.textSizeChanged.connect(lambda: self.update())

    @Property(str, notify=textChanged)
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.textChanged.emit()

    @Property(QPoint, notify=gapChanged)
    def gap(self):
        return self._gap

    @gap.setter
    def gap(self, value):
        self._gap = value
        self.gapChanged.emit()

    @Property(QPoint, notify=offsetChanged)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
        self.offsetChanged.emit()

    @Property(QColor, notify=textColorChanged)
    def textColor(self):
        return self._textColor

    @textColor.setter
    def textColor(self, value):
        self._textColor = value
        self.textColorChanged.emit()

    @Property(int, notify=rotateChanged)
    def rotate(self):
        return self._rotate

    @rotate.setter
    def rotate(self, value):
        self._rotate = value
        self.rotateChanged.emit()

    @Property(int, notify=textSizeChanged)
    def textSize(self):
        return self._textSize

    @textSize.setter
    def textSize(self, value):
        self._textSize = value
        self.textSizeChanged.emit()

    def paint(self, painter):
        font = QFont()
        font.setFamily(FluTextStyle().family)
        font.setPixelSize(self._textSize)
        painter.setFont(font)
        painter.setPen(self._textColor)
        fontMetrics = QFontMetricsF(font)
        fontWidth = fontMetrics.horizontalAdvance(self._text)
        fontHeight = fontMetrics.height()
        stepX = fontWidth + self._gap.x()
        stepY = fontHeight + self._gap.y()
        rowCount = int(self.width() / stepX) + 1
        colCount = int(self.height() / stepY) + 1
        for r in range(rowCount):
            for c in range(colCount):
                centerX = stepX * r + self._offset.x() + fontWidth / 2.0
                centerY = stepY * c + self._offset.y() + fontHeight / 2.0
                painter.save()
                painter.translate(centerX, centerY)
                painter.rotate(self._rotate)
                painter.drawText(QRectF(-fontWidth / 2.0, -fontHeight / 2.0, fontWidth, fontHeight), self._text)
                painter.restore()
