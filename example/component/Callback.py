from PySide6.QtCore import Signal, QObject


# noinspection PyPep8Naming
class Callback(QObject):
    start = Signal()
    finish = Signal()
    error = Signal(int, str, str)
    success = Signal(str)

    def __init__(self):
        QObject.__init__(self)

    def onStart(self):
        self.start.emit()

    def onFinish(self):
        self.finish.emit()

    def onSuccess(self, result: str = ""):
        self.success.emit(result)

    def onError(self, code: int = -1, errorString: str = "", result: str = ""):
        self.error.emit(code, errorString, result)
