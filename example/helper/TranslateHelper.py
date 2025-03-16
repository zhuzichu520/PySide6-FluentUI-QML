from PySide6.QtCore import QObject, Signal, Property, QTranslator
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlEngine

from FluentUI.Singleton import Singleton
from example.helper.SettingsHelper import SettingsHelper


@Singleton
class TranslateHelper(QObject):
    currentChanged = Signal()
    languagesChanged = Signal()

    def __init__(self):
        QObject.__init__(self, QGuiApplication.instance())
        self._engine = None
        self._translator = None
        self._current = None
        self._languages = None
        self._languages = ['en_US', 'zh_CN']
        self._current = SettingsHelper().getLanguage()

    @Property(str, notify=currentChanged)
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
        self.currentChanged.emit()

    @Property(list, notify=languagesChanged)
    def languages(self):
        return self._languages

    @languages.setter
    def languages(self, value):
        self._languages = value
        self.languagesChanged.emit()

    def init(self, engine: QQmlEngine):
        self._engine = engine
        self._translator = QTranslator()
        QGuiApplication.installTranslator(self._translator)
        if self._translator.load(f":/example/i18n/example_{self._current}.qm"):
            self._engine.retranslate()
