import os
import string

import py7zr
from PySide6.QtCore import QObject, QDir, QFile, QFileDevice, Slot, QIODevice, QTextStream, QFileInfo, Signal
from PySide6.QtGui import QGuiApplication

from FluentUI.FluLogger import Logger
from FluentUI.Singleton import Singleton


class CustomFormatter(string.Formatter):
    def __init__(self, mapping):
        super().__init__()
        self.mapping = mapping

    def get_value(self, key, args, kwargs):
        if key in self.mapping:
            return self.mapping[key]
        else:
            return "{" + key + "}"


# noinspection PyPep8Naming
def copyFile(src: str, dest: str):
    outputDir = QFileInfo(dest).absoluteDir()
    if not outputDir.exists():
        outputDir.mkpath(outputDir.absolutePath())
    QFile.copy(src, dest)
    permissions = (QFileDevice.Permissions(QFileDevice.Permissions.WriteOwner) |
                   QFileDevice.Permissions(QFileDevice.Permissions.WriteUser) |
                   QFileDevice.Permissions(QFileDevice.Permissions.WriteGroup) |
                   QFileDevice.Permissions(QFileDevice.Permissions.WriteOther))
    QFile.setPermissions(dest, permissions)


# noinspection PyPep8Naming
def templateToFile(src: str, dest: str, mapping):
    formatter = CustomFormatter(mapping)
    file = QFile(src)
    if file.open(QIODevice.ReadOnly | QIODevice.Text):
        inStream = QTextStream(file)
        data: str = inStream.readAll()
        content = formatter.format(data)
        file.close()
        outputDir = QFileInfo(dest).absoluteDir()
        if not outputDir.exists():
            outputDir.mkpath(outputDir.absolutePath())
        outputFile = QFile(dest)
        if outputFile.open(QIODevice.WriteOnly | QIODevice.Text):
            outStream = QTextStream(outputFile)
            outStream << content
            outputFile.close()
        else:
            Logger().debug("Failed to open output file.")
    else:
        Logger().debug("Failed to open resource file.")


# noinspection PyPep8Naming
def extractSourceFile(out: str, password=None):
    sourcePath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "source.zip")
    with py7zr.SevenZipFile(sourcePath, mode='r', password=password) as z:
        z.extractall(path=out)


# noinspection PyPep8Naming,PyUnresolvedReferences
@Singleton
class InitializrHelper(QObject):
    error = Signal(str)
    success = Signal(str)

    def __init__(self):
        QObject.__init__(self, QGuiApplication.instance())

    def copyDir(self, fromDir: QDir, toDir: QDir, coverIfFileExists: bool) -> bool:
        _fromDir = QDir(fromDir)
        _toDir = QDir(toDir)
        if not _toDir.exists():
            if not _toDir.mkdir(toDir.absolutePath()):
                return False
        fileInfoList = _fromDir.entryInfoList()
        for fileInfo in fileInfoList:
            if fileInfo.fileName() in ('.', '..'):
                continue
            if fileInfo.isDir():
                if not self.copyDir(QDir(fileInfo.filePath()), QDir(_toDir.filePath(fileInfo.fileName())), True):
                    return False
            else:
                if coverIfFileExists and _toDir.exists(fileInfo.fileName()):
                    _toDir.remove(fileInfo.fileName())
                if not QFile.copy(fileInfo.filePath(), _toDir.filePath(fileInfo.fileName())):
                    return False
        return True

    @Slot(str, str)
    def generate(self, name: str, path: str):
        if not name:
            self.error.emit(self.tr("The name cannot be empty"))
            return
        if not path:
            self.error.emit(self.tr("The creation path cannot be empty"))
            return
        projectRootDir = QDir(path)
        if not projectRootDir.exists():
            self.error.emit(self.tr("The path does not exist"))
            return
        projectPath = projectRootDir.filePath(name)
        projectDir = QDir(projectPath)
        if projectDir.exists():
            self.error.emit(self.tr("%1 folder already exists").format(name))
            return
        projectDir.mkpath(projectPath)
        extractSourceFile(projectPath, "zhuzichu988")
        mapping = {
            'projectName': name
        }
        templateToFile(":/example/res/template/env.py.in", projectDir.filePath("env.py"), mapping)
        copyFile(":/example/res/template/favicon.icns.in", projectDir.filePath("favicon.icns"))
        copyFile(":/example/res/template/favicon.ico.in", projectDir.filePath("favicon.ico"))
        copyFile(":/example/res/template/favicon.jpg.in", projectDir.filePath("favicon.jpg"))
        copyFile(":/example/res/template/main.spec.in", projectDir.filePath("main.spec"))
        copyFile(":/example/res/template/script-build-nuitka.py.in", projectDir.filePath("script-build-nuitka.py"))
        copyFile(":/example/res/template/script-build-pyinstaller.py.in", projectDir.filePath("script-build-pyinstaller.py"))
        copyFile(":/example/res/template/script-init-venv.py.in", projectDir.filePath("script-init-venv.py"))
        copyFile(":/example/res/template/script-start.py.in", projectDir.filePath("script-start.py"))
        copyFile(":/example/res/template/script-update-resource.py.in", projectDir.filePath("script-update-resource.py"))
        copyFile(":/example/res/template/script-update-translations.py.in", projectDir.filePath("script-update-translations.py"))
        templateToFile(":/example/res/template/project/main.py.in", projectDir.filePath(f"{name}/main.py"), mapping)
        templateToFile(":/example/res/template/project/en_US.ts.in", projectDir.filePath(f"{name}/{name}_en_US.ts"), mapping)
        templateToFile(":/example/res/template/project/zh_CN.ts.in", projectDir.filePath(f"{name}/{name}_zh_CN.ts"), mapping)
        templateToFile(":/example/res/template/project/imports/resource.qrc.in", projectDir.filePath(f"{name}/imports/resource.qrc"), mapping)
        copyFile(":/example/res/template/project/imports/project/image/logo.ico.in", projectDir.filePath(f"{name}/imports/{name}/image/logo.ico"))
        templateToFile(":/example/res/template/project/imports/project/qml/App.qml.in", projectDir.filePath(f"{name}/imports/{name}/qml/App.qml"), mapping)
        templateToFile(":/example/res/template/project/imports/project/qml/main.qml.in", projectDir.filePath(f"{name}/imports/{name}/qml/main.qml"), mapping)
        self.success.emit(projectPath + "/script-start.py")
