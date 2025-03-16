import base64
import sys

from PySide6.QtCore import QObject, Slot, QProcess, qVersion, Qt, QUrl, QFileInfo, QUuid, QSettings, QRect, QCryptographicHash, QDir, QFile, QPoint, QDateTime, QSysInfo
from PySide6.QtGui import QGuiApplication, QTextDocument, QColor, QCursor, QIcon
from PySide6.QtQuick import QQuickWindow

from FluentUI.Singleton import Singleton

if sys.platform.startswith("win"):
    from ctypes import c_bool, c_void_p, WinDLL, c_uint, create_unicode_buffer, wstring_at, addressof

    user32 = WinDLL("user32")

    SystemParametersInfoW = user32.SystemParametersInfoW
    SystemParametersInfoW.argtypes = [c_uint, c_uint, c_void_p, c_uint]
    SystemParametersInfoW.restype = c_bool


    def SystemParametersInfoW():
        bPath = create_unicode_buffer(260)
        result = bool(user32.SystemParametersInfoW(0x0073, 260, bPath, 0))
        if result:
            return str(wstring_at(addressof(bPath)))
        return None


# noinspection PyPep8Naming
@Singleton
class FluTools(QObject):

    def __init__(self):
        QObject.__init__(self, QGuiApplication.instance())

    @Slot(str)
    def clipText(self, val: str):
        QGuiApplication.clipboard().setText(val)

    @Slot(result=str)
    def uuid(self):
        return QUuid.createUuid().toString().replace('-', '').replace('{', '').replace('}', '')

    @Slot(result=bool)
    def isMacos(self):
        return sys.platform.startswith("darwin")

    @Slot(result=bool)
    def isLinux(self):
        return sys.platform.startswith("linux")

    @Slot(result=bool)
    def isWin(self):
        return sys.platform.startswith("win")

    @Slot(result=int)
    def qtMajor(self):
        return int(qVersion().split('.')[0])

    @Slot(result=int)
    def qtMinor(self):
        return int(qVersion().split('.')[1])

    @Slot(bool)
    def setQuitOnLastWindowClosed(self, val):
        QGuiApplication.setQuitOnLastWindowClosed(val)

    @Slot(int)
    def setOverrideCursor(self, val):
        QGuiApplication.setOverrideCursor(QCursor(Qt.CursorShape(val)))

    @Slot()
    def restoreOverrideCursor(self):
        QGuiApplication.restoreOverrideCursor()

    @Slot(QObject)
    def deleteLater(self, val: QObject):
        if val is not None:
            val.deleteLater()

    @Slot(QUrl, result=str)
    def toLocalPath(self, url: QUrl):
        return url.toLocalFile()

    @Slot(QUrl, result=str)
    def getFileNameByUrl(self, url: QUrl):
        return QFileInfo(url.toLocalFile()).fileName()

    @Slot(str, result=str)
    def html2PlantText(self, html: str):
        textDocument = QTextDocument()
        textDocument.setHtml(html)
        return textDocument.toPlainText()

    @Slot(result=QRect)
    def getVirtualGeometry(self):
        return QGuiApplication.primaryScreen().virtualGeometry()

    @Slot(result=str)
    def getApplicationDirPath(self):
        return QGuiApplication.applicationDirPath()

    @Slot(str, result=QUrl)
    def getUrlByFilePath(self, path: str):
        return QUrl.fromLocalFile(path)

    @Slot(QColor, float, result=QColor)
    def withOpacity(self, color: QColor, opacity: float):
        alpha = int(opacity * 255) & 0xff
        return QColor.fromRgba((alpha << 24) | (color.rgba() & 0xffffff))

    @Slot(str, result=str)
    def md5(self, val: str):
        return QCryptographicHash.hash(bytearray(val, "utf-8"), QCryptographicHash.Algorithm.Md5).toHex()

    @Slot(str, result=str)
    def sha256(self, val: str):
        return QCryptographicHash.hash(bytearray(val, "utf-8"), QCryptographicHash.Algorithm.Sha256).toHex()

    @Slot(str, result=str)
    def toBase64(self, val):
        return base64.b64encode(val)

    @Slot(str, result=str)
    def fromBase64(self, val):
        return base64.b64decode(val)

    @Slot(str, result=bool)
    def removeDir(self, path: str):
        target = QDir(path)
        return target.removeRecursively()

    @Slot(str, result=bool)
    def removeFile(self, path: str):
        target = QFile(path)
        return target.remove()

    @Slot(str)
    def showFileInFolder(self, path: str):
        if sys.platform.startswith("win"):
            process = "explorer.exe"
            arguments = ["/select,", QDir.toNativeSeparators(path)]
            QProcess.startDetached(process, arguments)
        elif sys.platform.startswith("linux"):
            fileInfo = QFileInfo(path)
            process = "xdg-open"
            arguments = [fileInfo.absoluteDir().absolutePath()]
            QProcess.startDetached(process, arguments)
        elif sys.platform.startswith("darwin"):
            process = "/usr/bin/osascript"
            arguments = ["-e", "tell application \"Finder\" to reveal POSIX file \"" + path + "\""]
            QProcess.execute(process, arguments)
            arguments = ["-e", "tell application \"Finder\" to activate"]
            QProcess.execute(process, arguments)

    @Slot(result=bool)
    def isSoftware(self):
        return QQuickWindow.sceneGraphBackend == "software"

    @Slot(result=QPoint)
    def cursorPos(self):
        return QCursor.pos()

    @Slot(result=int)
    def currentTimestamp(self):
        return QDateTime.currentDateTime()

    @Slot(result=QIcon)
    def windowIcon(self):
        return QGuiApplication.windowIcon()

    @Slot(result=int)
    def cursorScreenIndex(self):
        screenIndex = 0
        screenCount = len(QGuiApplication.screens())
        if screenCount > 1:
            pos = QCursor.pos()
            for i in range(screenCount):
                if QGuiApplication.screens()[i].geometry().contains(pos):
                    screenIndex = i
                    break
        return screenIndex

    @Slot(result=int)
    def windowBuildNumber(self):
        if self.isWin():
            regKey = QSettings("HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", QSettings.Format.NativeFormat)
            if regKey.contains("CurrentBuildNumber"):
                buildNumber = int(regKey.value("CurrentBuildNumber"))
                return buildNumber
        return -1

    @Slot(result=bool)
    def isWindows11OrGreater(self):
        var = getattr(self, "_isWindows11OrGreater", None)
        if var is None:
            if self.isWin():
                buildNumber = self.windowBuildNumber()
                if buildNumber >= 22000:
                    var = True
                else:
                    var = False
            else:
                var = False
            setattr(self, "_isWindows11OrGreater", var)
        return bool(var)

    @Slot(result=bool)
    def isWindows10OrGreater(self):
        var = getattr(self, "_isWindows10OrGreater", None)
        if var is None:
            if self.isWin():
                buildNumber = self.windowBuildNumber()
                if buildNumber >= 10240:
                    var = True
                else:
                    var = False
            else:
                var = False
            setattr(self, "_isWindows10OrGreater", var)
        return bool(var)

    @Slot(QQuickWindow, result=QRect)
    def desktopAvailableGeometry(self, window: QQuickWindow):
        return window.screen().availableGeometry()

    @Slot(result=str)
    def getWallpaperFilePath(self):
        if self.isWin():
            path = SystemParametersInfoW()
            if path is not None:
                return path
        elif self.isLinux():
            productType = QSysInfo.productType()
            if productType == "UOS":
                process = QProcess()
                args = ["--session", "--type=method_call", "--print-reply", "--dest=com.deepin.wm", "/com/deepin/wm", "com.deepin.wm.GetCurrentWorkspaceBackgroundForMonitor",
                        f"string:'${self.currentTimestamp()}'"]
                process.start("dbus-send", args)
                process.waitForFinished()
                result = process.readAllStandardOutput().trimmed()
                startIndex = result.indexOf("file:///")
                if startIndex != -1:
                    path = result.mid(startIndex + 7, result.length() - startIndex - 8)
                    return path
        elif self.isMacos():
            process = QProcess()
            args = ["-e", 'tell application "Finder" to get POSIX path of (desktop picture as alias)']
            process.start("osascript", args)
            process.waitForFinished()
            path = process.readAllStandardOutput().trimmed()
            if path.isEmpty():
                return "/System/Library/CoreServices/DefaultDesktop.heic"
            return path
        return ""
