from PySide6.QtCore import QObject, Signal, Property
from PySide6.QtGui import QColor

'''
The FluAccentColor class is responsible for displaying the color of the fluent accident
'''


# noinspection PyCallingNonCallable
class FluAccentColor(QObject):
    darkestChanged = Signal()
    darkerChanged = Signal()
    darkChanged = Signal()
    normalChanged = Signal()
    lightChanged = Signal()
    lighterChanged = Signal()
    lightestChanged = Signal()

    @Property(QColor, notify=darkestChanged)
    def darkest(self):
        return self._darkest

    @darkest.setter
    def darkest(self, value):
        self._darkest = value
        self.darkestChanged.emit()

    @Property(QColor, notify=darkerChanged)
    def darker(self):
        return self._darker

    @darker.setter
    def darker(self, value):
        self._darker = value
        self.darkerChanged.emit()

    @Property(QColor, notify=darkChanged)
    def dark(self):
        return self._dark

    @dark.setter
    def dark(self, value):
        self._dark = value
        self.darkChanged.emit()

    @Property(QColor, notify=normalChanged)
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, value):
        self._normal = value
        self.normalChanged.emit()

    @Property(QColor, notify=lightChanged)
    def light(self):
        return self._light

    @light.setter
    def light(self, value):
        self._light = value
        self.lightChanged.emit()

    @Property(QColor, notify=lighterChanged)
    def lighter(self):
        return self._lighter

    @lighter.setter
    def lighter(self, value):
        self._lighter = value
        self.lighterChanged.emit()

    @Property(QColor, notify=lightestChanged)
    def lightest(self):
        return self._lightest

    @lightest.setter
    def lightest(self, value):
        self._lightest = value
        self.lightestChanged.emit()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._darkest = None
        self._darker = None
        self._dark = None
        self._normal = None
        self._light = None
        self._lighter = None
        self._lightest = None
