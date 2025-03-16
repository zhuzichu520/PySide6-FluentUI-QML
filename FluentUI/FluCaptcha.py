from PySide6.QtCore import Signal, Property, Qt, Slot
from PySide6.QtGui import QColor, QFont, QPen
from PySide6.QtQuick import QQuickPaintedItem

from random import randint


# noinspection PyPep8Naming
def _generaNumber(number):
    return randint(0, number - 1)


# noinspection PyCallingNonCallable,PyPep8Naming
class FluCaptcha(QQuickPaintedItem):
    fontChanged = Signal()
    ignoreCaseChanged = Signal()

    @Property(bool, notify=ignoreCaseChanged)
    def ignoreCase(self):
        return self._ignoreCase

    @ignoreCase.setter
    def ignoreCase(self, value):
        self._ignoreCase = value
        self.ignoreCaseChanged.emit()

    @Property(QFont, notify=fontChanged)
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value
        self.fontChanged.emit()

    def __init__(self):
        QQuickPaintedItem.__init__(self)
        self._ignoreCase: bool = True
        self._code = ""
        fontStype = QFont()
        fontStype.setPixelSize(28)
        fontStype.setBold(True)
        self._font = fontStype
        self.setWidth(180)
        self.setHeight(80)
        self.refresh()

    @Slot()
    def refresh(self):
        self._code = ""
        for i in range(4):
            num = _generaNumber(3)
            if num == 0:
                self._code += str(_generaNumber(10))
            elif num == 1:
                temp = ord('A')
                self._code += chr(temp + _generaNumber(26))
            elif num == 2:
                temp = ord('a')
                self._code += chr(temp + _generaNumber(26))
        self.update()

    @Slot(str, result=bool)
    def verify(self, code):
        if self._ignoreCase:
            return self._code.upper() == code.upper()
        return self._code == code

    def paint(self, painter):
        painter.save()
        painter.fillRect(self.boundingRect().toRect(), QColor(255, 255, 255, 255))
        pen = QPen()
        painter.setFont(self._font)
        for i in range(100):
            pen.setColor(QColor(_generaNumber(256), _generaNumber(256), _generaNumber(256)))
            painter.setPen(pen)
            painter.drawPoint(_generaNumber(180), _generaNumber(80))
        for i in range(5):
            pen.setColor(QColor(_generaNumber(256), _generaNumber(256), _generaNumber(256)))
            painter.setPen(pen)
            painter.drawLine(_generaNumber(180), _generaNumber(80), _generaNumber(180), _generaNumber(80))
        for i in range(4):
            pen.setColor(QColor(_generaNumber(255), _generaNumber(255), _generaNumber(255)))
            painter.setPen(pen)
            painter.drawText(15 + 35 * i, 10 + _generaNumber(15), 30, 40, Qt.AlignmentFlag.AlignCenter, self._code[i])
        painter.restore()
