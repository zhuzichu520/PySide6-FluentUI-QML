from PySide6.QtCore import QObject, Signal, Property, QEvent, QFileSystemWatcher, QMutex, QThreadPool
from PySide6.QtGui import QColor, QGuiApplication, QPalette

from FluentUI.Def import FluThemeType
from FluentUI.FluAccentColor import FluAccentColor
from FluentUI.FluColors import FluColors
from FluentUI.FluTools import FluTools
from FluentUI.Singleton import Singleton

Tools = FluTools()

'''
The FluTheme class, which is used to define the fluent theme
'''


# noinspection PyPep8Naming
def _systemDark():
    palette = QGuiApplication.palette()
    color = palette.color(QPalette.ColorRole.Window)
    luminance = color.red() * 0.2126 + color.green() * 0.7152 + color.blue() * 0.0722
    return luminance <= 255 / 2


# noinspection PyCallingNonCallable,PyPropertyAccess,PyPep8Naming
@Singleton
class FluTheme(QObject):
    accentColorChanged = Signal()
    primaryColorChanged = Signal()
    backgroundColorChanged = Signal()
    dividerColorChanged = Signal()
    windowBackgroundColorChanged = Signal()
    windowActiveBackgroundColorChanged = Signal()
    fontPrimaryColorChanged = Signal()
    fontSecondaryColorChanged = Signal()
    fontTertiaryColorChanged = Signal()
    itemNormalColorChanged = Signal()
    itemHoverColorChanged = Signal()
    itemPressColorChanged = Signal()
    itemCheckColorChanged = Signal()
    nativeTextChanged = Signal()
    darkModeChanged = Signal()
    animationEnabledChanged = Signal()
    frameColorChanged = Signal()
    frameActiveColorChanged = Signal()
    desktopImagePathChanged = Signal()
    blurBehindWindowEnabledChanged = Signal()

    @Property(bool, notify=blurBehindWindowEnabledChanged)
    def blurBehindWindowEnabled(self):
        return self._blurBehindWindowEnabled

    @blurBehindWindowEnabled.setter
    def blurBehindWindowEnabled(self, value):
        self._blurBehindWindowEnabled = value
        self.blurBehindWindowEnabledChanged.emit()

    def __init__(self):
        QObject.__init__(self, QGuiApplication.instance())
        self._systemDark = False
        self._accentColor = None
        self._primaryColor = None
        self._backgroundColor = None
        self._dividerColor = None
        self._windowBackgroundColor = None
        self._windowActiveBackgroundColor = None
        self._fontPrimaryColor = None
        self._fontSecondaryColor = None
        self._fontTertiaryColor = None
        self._frameColor = None
        self._frameActiveColor = None
        self._itemNormalColor = None
        self._itemHoverColor = None
        self._itemPressColor = None
        self._itemCheckColor = None
        self._nativeText: bool = False
        self._blurBehindWindowEnabled: bool = False
        self._darkMode: int = 0
        self._animationEnabled: bool = False
        self._accentColor = FluColors().Blue
        self._darkMode = FluThemeType.DarkMode.Light
        self._nativeText = False
        self._animationEnabled = True
        self._systemDark = _systemDark()
        self._refreshColors()
        self._watcher = QFileSystemWatcher()
        self._mutex = QMutex()
        self._desktopImagePath = ""
        self.darkModeChanged.connect(self, lambda: {self.darkChanged.emit()})
        self.darkChanged.connect(self, lambda: self._refreshColors())
        self.accentColorChanged.connect(self, lambda: self._refreshColors())
        self.blurBehindWindowEnabledChanged.connect(self, lambda: self.checkUpdateDesktopImage())
        self.startTimer(1000)

    def timerEvent(self, event):
        self.checkUpdateDesktopImage()

    def checkUpdateDesktopImage(self):
        if not self._blurBehindWindowEnabled:
            return

        def updateImage() -> None:
            self._mutex.lock()
            path = Tools.getWallpaperFilePath()
            if self._desktopImagePath != path:
                if self._desktopImagePath != "":
                    self._watcher.removePath(self._desktopImagePath)
                self.desktopImagePath = path
                self._watcher.addPath(path)
            self._mutex.unlock()

        QThreadPool.globalInstance().start(lambda: updateImage())

    @Property(str, notify=desktopImagePathChanged)
    def desktopImagePath(self):
        return self._desktopImagePath

    @desktopImagePath.setter
    def desktopImagePath(self, value):
        self._desktopImagePath = value
        self.desktopImagePathChanged.emit()

    @Property(QColor, notify=frameActiveColorChanged)
    def frameActiveColor(self):
        return self._frameActiveColor

    @frameActiveColor.setter
    def frameActiveColor(self, value):
        self._frameActiveColor = value
        self.frameActiveColorChanged.emit()

    @Property(QColor, notify=frameColorChanged)
    def frameColor(self):
        return self._frameColor

    @frameColor.setter
    def frameColor(self, value):
        self._frameColor = value
        self.frameColorChanged.emit()

    @Property(FluAccentColor, notify=accentColorChanged)
    def accentColor(self):
        return self._accentColor

    @accentColor.setter
    def accentColor(self, value):
        self._accentColor = value
        self.accentColorChanged.emit()

    @Property(QColor, notify=primaryColorChanged)
    def primaryColor(self):
        return self._primaryColor

    @primaryColor.setter
    def primaryColor(self, value):
        self._primaryColor = value
        self.primaryColorChanged.emit()

    @Property(QColor, notify=backgroundColorChanged)
    def backgroundColor(self):
        return self._backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, value):
        self._backgroundColor = value
        self.backgroundColorChanged.emit()

    @Property(QColor, notify=dividerColorChanged)
    def dividerColor(self):
        return self._dividerColor

    @dividerColor.setter
    def dividerColor(self, value):
        self._dividerColor = value
        self.dividerColorChanged.emit()

    @Property(QColor, notify=windowBackgroundColorChanged)
    def windowBackgroundColor(self):
        return self._windowBackgroundColor

    @windowBackgroundColor.setter
    def windowBackgroundColor(self, value):
        self._windowBackgroundColor = value
        self.windowBackgroundColorChanged.emit()

    @Property(QColor, notify=windowActiveBackgroundColorChanged)
    def windowActiveBackgroundColor(self):
        return self._windowActiveBackgroundColor

    @windowActiveBackgroundColor.setter
    def windowActiveBackgroundColor(self, value):
        self._windowActiveBackgroundColor = value
        self.windowActiveBackgroundColorChanged.emit()

    @Property(QColor, notify=fontPrimaryColorChanged)
    def fontPrimaryColor(self):
        return self._fontPrimaryColor

    @fontPrimaryColor.setter
    def fontPrimaryColor(self, value):
        self._fontPrimaryColor = value
        self.fontPrimaryColorChanged.emit()

    @Property(QColor, notify=fontSecondaryColorChanged)
    def fontSecondaryColor(self):
        return self._fontSecondaryColor

    @fontSecondaryColor.setter
    def fontSecondaryColor(self, value):
        self._fontSecondaryColor = value
        self.fontSecondaryColorChanged.emit()

    @Property(QColor, notify=fontTertiaryColorChanged)
    def fontTertiaryColor(self):
        return self._fontTertiaryColor

    @fontTertiaryColor.setter
    def fontTertiaryColor(self, value):
        self._fontTertiaryColor = value
        self.fontTertiaryColorChanged.emit()

    @Property(QColor, notify=itemNormalColorChanged)
    def itemNormalColor(self):
        return self._itemNormalColor

    @itemNormalColor.setter
    def itemNormalColor(self, value):
        self._itemNormalColor = value
        self.itemNormalColorChanged.emit()

    @Property(QColor, notify=itemHoverColorChanged)
    def itemHoverColor(self):
        return self._itemHoverColor

    @itemHoverColor.setter
    def itemHoverColor(self, value):
        self._itemHoverColor = value
        self.itemHoverColorChanged.emit()

    @Property(QColor, notify=itemPressColorChanged)
    def itemPressColor(self):
        return self._itemPressColor

    @itemPressColor.setter
    def itemPressColor(self, value):
        self._itemPressColor = value
        self.itemPressColorChanged.emit()

    @Property(QColor, notify=itemCheckColorChanged)
    def itemCheckColor(self):
        return self._itemCheckColor

    @itemCheckColor.setter
    def itemCheckColor(self, value):
        self._itemCheckColor = value
        self.itemCheckColorChanged.emit()

    @Property(int, notify=darkModeChanged)
    def darkMode(self):
        return self._darkMode

    @darkMode.setter
    def darkMode(self, value):
        self._darkMode = value
        self.darkModeChanged.emit()

    @Property(bool, notify=nativeTextChanged)
    def nativeText(self):
        return self._nativeText

    @nativeText.setter
    def nativeText(self, value):
        self._nativeText = value
        self.nativeTextChanged.emit()

    @Property(bool, notify=animationEnabledChanged)
    def animationEnabled(self):
        return self._animationEnabled

    @animationEnabled.setter
    def animationEnabled(self, value):
        self._animationEnabled = value
        self.animationEnabledChanged.emit()

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.ApplicationPaletteChange or event.type() == QEvent.Type.ThemeChange:
            self._systemDark = _systemDark()
            self.darkChanged.emit()
            event.accept()
            return True
        return False

    def _dark(self):
        if self._darkMode == FluThemeType.DarkMode.Dark:
            return True
        elif self._darkMode == FluThemeType.DarkMode.Light:
            return False
        elif self._darkMode == FluThemeType.DarkMode.System:
            return self._systemDark
        return False

    darkChanged = Signal()
    dark = Property(bool, _dark, notify=darkChanged)

    def _refreshColors(self):
        isDark = self._dark()
        self.primaryColor = self._accentColor.lighter if isDark else self._accentColor.dark
        self.backgroundColor = QColor(0, 0, 0, 255) if isDark else QColor(255, 255, 255, 255)
        self.dividerColor = QColor(80, 80, 80, 255) if isDark else QColor(210, 210, 210, 255)
        self.windowBackgroundColor = QColor(32, 32, 32, 255) if isDark else QColor(237, 237, 237, 255)
        self.windowActiveBackgroundColor = QColor(26, 26, 26, 255) if isDark else QColor(243, 243, 243, 255)
        self.fontPrimaryColor = QColor(248, 248, 248, 255) if isDark else QColor(7, 7, 7, 255)
        self.fontSecondaryColor = QColor(222, 222, 222, 255) if isDark else QColor(102, 102, 102, 255)
        self.fontTertiaryColor = QColor(200, 200, 200, 255) if isDark else QColor(153, 153, 153, 255)
        self.itemNormalColor = QColor(255, 255, 255, 0) if isDark else QColor(0, 0, 0, 0)
        self.frameColor = QColor(56, 56, 56, int(255 * 0.8)) if isDark else QColor(243, 243, 243, int(255 * 0.8))
        self.frameActiveColor = QColor(48, 48, 48, int(255 * 0.8)) if isDark else QColor(255, 255, 255, int(255 * 0.8))
        self.itemHoverColor = QColor(255, 255, 255, int(255 * 0.06)) if isDark else QColor(0, 0, 0, int(255 * 0.03))
        self.itemPressColor = QColor(255, 255, 255, int(255 * 0.09)) if isDark else QColor(0, 0, 0, int(255 * 0.06))
        self.itemCheckColor = QColor(255, 255, 255, int(255 * 0.12)) if isDark else QColor(0, 0, 0, int(255 * 0.09))
