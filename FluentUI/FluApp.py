from PySide6.QtCore import QObject, Signal, Property, Slot, QLocale, QTranslator
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import qmlEngine

from FluentUI.FluentIconDef import FluentIcons
from FluentUI.Singleton import Singleton

'''
The FluApp class
'''


@Singleton
class FluApp(QObject):
    useSystemAppBarChanged = Signal()
    windowIconChanged = Signal()
    localeChanged = Signal()
    launcherChanged = Signal()

    @Property(QObject, notify=launcherChanged)
    def launcher(self):
        return self._launcher

    @launcher.setter
    def launcher(self, value):
        self._launcher = value
        self.launcherChanged.emit()

    def __init__(self):
        QObject.__init__(self)
        self._engine = None
        self._translator = None
        self._useSystemAppBar: bool = False
        self._windowIcon = None
        self._locale = None
        self._launcher = None

    @Property(bool, notify=useSystemAppBarChanged)
    def useSystemAppBar(self):
        return self._useSystemAppBar

    @useSystemAppBar.setter
    def useSystemAppBar(self, value):
        self._useSystemAppBar = value
        self.useSystemAppBarChanged.emit()

    @Property(str, notify=windowIconChanged)
    def windowIcon(self):
        return self._windowIcon

    @windowIcon.setter
    def windowIcon(self, value):
        self._windowIcon = value
        self.windowIconChanged.emit()

    @Property(QLocale, notify=localeChanged)
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value
        self.localeChanged.emit()

    @Slot(QObject)
    @Slot(QObject, QLocale)
    def init(self, launcher, locale=None):
        self._launcher = launcher
        if locale is None:
            locale = QLocale.system()
        self._locale = locale
        self._engine = qmlEngine(launcher)
        translator = QTranslator()
        self._translator = translator
        QGuiApplication.installTranslator(self._translator)
        uiLanguages = self._locale.uiLanguages()
        for lang in uiLanguages:
            name = "FluentUI_" + QLocale(lang).name()
            if self._translator.load(":/FluentUI/i18n/" + name):
                self._engine.retranslate()
                break

    # noinspection PyUnresolvedReferences
    @Slot(result=list)
    @Slot(str, result=list)
    def iconData(self, keyword=None) -> list:
        if not keyword:
            keyword = ""
        arr = []
        enumType = FluentIcons.staticMetaObject.enumerator(FluentIcons.staticMetaObject.indexOfEnumerator("Type"))
        for i in range(enumType.keyCount()):
            name = enumType.key(i)
            icon = enumType.value(i)
            if keyword in name:
                obj = {"name": name, "icon": icon}
                arr.append(obj)
        return arr
