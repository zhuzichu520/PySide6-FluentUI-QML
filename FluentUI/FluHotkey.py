import keyboard

from PySide6.QtCore import Signal, QObject, Property


# noinspection PyPep8Naming
class FluHotkey(QObject):
    sequenceChanged = Signal()
    nameChanged = Signal()
    isRegisteredChanged = Signal()
    activated = Signal()

    def hotkeyCallback(self):
        self.activated.emit()

    def __init__(self):
        QObject.__init__(self)
        self._sequence: str = ""
        self._name: str = ""
        self._isRegistered: bool = False

        def handleSequenceChanged():
            # keyboard.remove_hotkey(self.hotkeyCallback)
            try:
                keyboard.add_hotkey(self._sequence, self.hotkeyCallback)
                self.isRegistered = True
            except RuntimeError:
                self.isRegistered = False

        self.sequenceChanged.connect(lambda: handleSequenceChanged())

    @Property(bool, notify=isRegisteredChanged)
    def isRegistered(self):
        return self._isRegistered

    @isRegistered.setter
    def isRegistered(self, value):
        self._isRegistered = value
        self.isRegisteredChanged.emit()

    @Property(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.nameChanged.emit()

    @Property(str, notify=sequenceChanged)
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value
        self.sequenceChanged.emit()
