from PySide6.QtCore import QObject, Signal, Property
from PySide6.QtGui import QFont, QGuiApplication
from FluentUI.Singleton import Singleton
from FluentUI.FluTools import FluTools

'''
The FluTextStyle class is used to define the style of text 
'''


# noinspection PyCallingNonCallable,PyPep8Naming
@Singleton
class FluTextStyle(QObject):
    familyChanged = Signal()
    CaptionChanged = Signal()
    BodyChanged = Signal()
    BodyStrongChanged = Signal()
    SubtitleChanged = Signal()
    TitleChanged = Signal()
    TitleLargeChanged = Signal()
    DisplayChanged = Signal()

    def __init__(self):
        QObject.__init__(self, QGuiApplication.instance())
        self._family = QFont().defaultFamily()
        if FluTools().isWin():
            self._family = "微软雅黑"

        caption = QFont()
        caption.setPixelSize(12)
        self._Caption = caption

        body = QFont()
        body.setPixelSize(13)
        self._Body = body

        bodyStrong = QFont()
        bodyStrong.setPixelSize(13)
        bodyStrong.setWeight(QFont.Weight.DemiBold)
        self._BodyStrong = bodyStrong

        subtitle = QFont()
        subtitle.setPixelSize(20)
        subtitle.setWeight(QFont.Weight.DemiBold)
        self._Subtitle = subtitle

        title = QFont()
        title.setPixelSize(28)
        title.setWeight(QFont.Weight.DemiBold)
        self._Title = title

        titleLarge = QFont()
        titleLarge.setPixelSize(40)
        titleLarge.setWeight(QFont.Weight.DemiBold)
        self._TitleLarge = titleLarge

        display = QFont()
        display.setPixelSize(68)
        display.setWeight(QFont.Weight.DemiBold)
        self._Display = display

    @Property(str, notify=familyChanged)
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        self._family = value
        self.familyChanged.emit()

    @Property(QFont, notify=CaptionChanged)
    def Caption(self):
        return self._Caption

    @Caption.setter
    def Caption(self, value):
        self._Caption = value
        self.CaptionChanged.emit()

    @Property(QFont, notify=BodyChanged)
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, value):
        self._Body = value
        self.BodyChanged.emit()

    @Property(QFont, notify=BodyStrongChanged)
    def BodyStrong(self):
        return self._BodyStrong

    @BodyStrong.setter
    def BodyStrong(self, value):
        self._BodyStrong = value
        self.BodyStrongChanged.emit()

    @Property(QFont, notify=SubtitleChanged)
    def Subtitle(self):
        return self._Subtitle

    @Subtitle.setter
    def Subtitle(self, value):
        self._Subtitle = value
        self.SubtitleChanged.emit()

    @Property(QFont, notify=TitleChanged)
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, value):
        self._Title = value
        self.TitleChanged.emit()

    @Property(QFont, notify=TitleLargeChanged)
    def TitleLarge(self):
        return self._TitleLarge

    @TitleLarge.setter
    def TitleLarge(self, value):
        self._TitleLarge = value
        self.TitleLargeChanged.emit()

    @Property(QFont, notify=DisplayChanged)
    def Display(self):
        return self._Display

    @Display.setter
    def Display(self, value):
        self._Display = value
        self.DisplayChanged.emit()
