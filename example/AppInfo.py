from PySide6.QtCore import QObject, Signal, Property
from PySide6.QtGui import QGuiApplication
from qasync import asyncSlot

from FluentUI.Singleton import Singleton
import example.helper.Async as Async
from example.component.Callback import Callback


# noinspection PyPep8Naming
@Singleton
class AppInfo(QObject):
    versionChanged = Signal()

    @Property(str, notify=versionChanged)
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value
        self.versionChanged.emit()

    def __init__(self):
        super().__init__(QGuiApplication.instance())
        self._version = "1.7.6"

    @asyncSlot(Callback)
    async def checkUpdate(self, callback: Callback):
        callback.onStart()
        try:
            r = await Async.http().get("https://api.github.com/repos/zhuzichu520/FluentUI/releases/latest")
            callback.onSuccess(await r.text())
        except Exception as exc:
            callback.onError(errorString="Error: {}".format(exc))
        finally:
            callback.onFinish()
