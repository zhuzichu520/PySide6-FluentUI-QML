import qrcode
from PIL import ImageQt
from PySide6.QtCore import Signal, Property, QRect
from PySide6.QtGui import QColor
from PySide6.QtQuick import QQuickPaintedItem


# noinspection PyUnresolvedReferences,PyPep8Naming
class FluQrCodeItem(QQuickPaintedItem):
    textChanged = Signal()
    colorChanged = Signal()
    bgColorChanged = Signal()
    sizeChanged = Signal()

    @Property(str, notify=textChanged)
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.textChanged.emit()

    @Property(QColor, notify=colorChanged)
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.colorChanged.emit()

    @Property(QColor, notify=bgColorChanged)
    def bgColor(self):
        return self._bgColor

    @bgColor.setter
    def bgColor(self, value):
        self._bgColor = value
        self.bgColorChanged.emit()

    @Property(int, notify=sizeChanged)
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self.sizeChanged.emit()

    def __init__(self):
        QQuickPaintedItem.__init__(self)
        self._text: str = ""
        self._color: QColor = QColor(0, 0, 0, 255)
        self._bgColor: QColor = QColor(255, 255, 255, 255)
        self._size: int = 100
        self.setWidth(self._size)
        self.setHeight(self._size)
        self.textChanged.connect(lambda: self.update())
        self.colorChanged.connect(lambda: self.update())
        self.bgColorChanged.connect(lambda: self.update())
        self.sizeChanged.connect(lambda: self.updateSize())

    def updateSize(self):
        self.setWidth(self._size)
        self.setHeight(self._size)
        self.update()

    def paint(self, painter):
        if self._text == "":
            return
        if len(self._text) > 1024:
            return
        painter.save()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=0
        )
        qr.add_data(self._text)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color=self._color.name(QColor.NameFormat.HexRgb), back_color=self._bgColor.name(QColor.NameFormat.HexRgb))
        image = ImageQt.toqimage(qr_image)
        painter.drawImage(QRect(0, 0, int(self.width()), int(self.height())), image)
        painter.restore()
