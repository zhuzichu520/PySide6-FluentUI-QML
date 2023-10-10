# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QObject, Signal, Property, QFileSystemWatcher
from PySide6.QtQml import (QmlNamedElement)

QML_IMPORT_NAME = "example"
QML_IMPORT_MAJOR_VERSION = 1


@QmlNamedElement("FileWatcher")
class FileWatcher(QObject):

    fileChanged = Signal()

    def __init__(self):
        QObject.__init__(self)
        self._path: str = ""
        self._watcher: QFileSystemWatcher = QFileSystemWatcher()

        def onFileChanged(path: str):
            self.fileChanged.emit()
            self.clean()
            self._watcher.addPath(path)
        self._watcher.fileChanged.connect(lambda path: onFileChanged(path))

        def onPathChanged():
            self.clean()
            self._watcher.addPath(self._path.replace("file:///", ""))
        self.path_changed.connect(lambda: onPathChanged())
        if (self._path != ""):
            self._watcher.addPath(self._path)

    path_changed = Signal()

    def clean(self):
        for item in self._watcher.files:
            self._watcher.removePath(item)

    @Property(str, notify=path_changed)
    def path(self):
        return self._path

    @path.setter
    def path(self, val):
        self._path = val
        self.path_changed.emit()
