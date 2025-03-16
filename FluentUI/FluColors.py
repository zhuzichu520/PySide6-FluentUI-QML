from PySide6.QtCore import QObject, Signal, Property, Slot
from PySide6.QtGui import QColor, QGuiApplication
from FluentUI.FluAccentColor import FluAccentColor
from FluentUI.Singleton import Singleton
from FluentUI.FluTools import FluTools

'''
The FluColors class is used to define the colors used in the FluentUI application
'''


# noinspection PyCallingNonCallable,PyPep8Naming,PyPropertyAccess
@Singleton
class FluColors(QObject):
    TransparentChanged = Signal()
    BlackChanged = Signal()
    WhiteChanged = Signal()
    Grey10Changed = Signal()
    Grey20Changed = Signal()
    Grey30Changed = Signal()
    Grey40Changed = Signal()
    Grey50Changed = Signal()
    Grey60Changed = Signal()
    Grey70Changed = Signal()
    Grey80Changed = Signal()
    Grey90Changed = Signal()
    Grey100Changed = Signal()
    Grey110Changed = Signal()
    Grey120Changed = Signal()
    Grey130Changed = Signal()
    Grey140Changed = Signal()
    Grey150Changed = Signal()
    Grey160Changed = Signal()
    Grey170Changed = Signal()
    Grey180Changed = Signal()
    Grey190Changed = Signal()
    Grey200Changed = Signal()
    Grey210Changed = Signal()
    Grey220Changed = Signal()
    YellowChanged = Signal()
    OrangeChanged = Signal()
    RedChanged = Signal()
    MagentaChanged = Signal()
    GreenChanged = Signal()
    BlueChanged = Signal()
    TealChanged = Signal()
    PurpleChanged = Signal()

    def __init__(self):
        QObject.__init__(self, QGuiApplication.instance())
        self._Transparent = QColor(0, 0, 0, 0)
        self._Black = QColor(0, 0, 0)
        self._White = QColor(255, 255, 255)
        self._Grey10 = QColor(250, 249, 248)
        self._Grey20 = QColor(243, 242, 241)
        self._Grey30 = QColor(237, 235, 233)
        self._Grey40 = QColor(225, 223, 221)
        self._Grey50 = QColor(210, 208, 206)
        self._Grey60 = QColor(200, 198, 196)
        self._Grey70 = QColor(190, 185, 184)
        self._Grey80 = QColor(179, 176, 173)
        self._Grey90 = QColor(161, 159, 157)
        self._Grey100 = QColor(151, 149, 146)
        self._Grey110 = QColor(138, 136, 134)
        self._Grey120 = QColor(121, 119, 117)
        self._Grey130 = QColor(96, 94, 92)
        self._Grey140 = QColor(72, 70, 68)
        self._Grey150 = QColor(59, 58, 57)
        self._Grey160 = QColor(50, 49, 48)
        self._Grey170 = QColor(41, 40, 39)
        self._Grey180 = QColor(37, 36, 35)
        self._Grey190 = QColor(32, 31, 30)
        self._Grey200 = QColor(27, 26, 25)
        self._Grey210 = QColor(22, 21, 20)
        self._Grey220 = QColor(17, 16, 15)

        yellow = FluAccentColor()
        yellow.darkest = QColor(249, 168, 37)
        yellow.darker = QColor(251, 192, 45)
        yellow.dark = QColor(253, 212, 53)
        yellow.normal = QColor(255, 235, 59)
        yellow.light = QColor(255, 238, 88)
        yellow.lighter = QColor(255, 241, 118)
        yellow.lightest = QColor(255, 245, 155)
        self._Yellow = yellow

        orange = FluAccentColor()
        orange.darkest = QColor(153, 61, 7)
        orange.darker = QColor(172, 68, 8)
        orange.dark = QColor(209, 88, 10)
        orange.normal = QColor(247, 99, 12)
        orange.light = QColor(248, 122, 48)
        orange.lighter = QColor(249, 145, 84)
        orange.lightest = QColor(250, 192, 106)
        self._Orange = orange

        red = FluAccentColor()
        red.darkest = QColor(143, 10, 21)
        red.darker = QColor(162, 11, 24)
        red.dark = QColor(185, 13, 28)
        red.normal = QColor(232, 17, 35)
        red.light = QColor(236, 64, 79)
        red.lighter = QColor(238, 88, 101)
        red.lightest = QColor(240, 107, 118)
        self._Red = red

        magenta = FluAccentColor()
        magenta.darkest = QColor(111, 0, 79)
        magenta.darker = QColor(160, 7, 108)
        magenta.dark = QColor(181, 13, 125)
        magenta.normal = QColor(227, 0, 140)
        magenta.light = QColor(234, 77, 168)
        magenta.lighter = QColor(238, 110, 193)
        magenta.lightest = QColor(241, 140, 213)
        self._Magenta = magenta

        purple = FluAccentColor()
        purple.darkest = QColor(44, 15, 118)
        purple.darker = QColor(61, 15, 153)
        purple.dark = QColor(78, 17, 174)
        purple.normal = QColor(104, 33, 122)
        purple.light = QColor(123, 76, 157)
        purple.lighter = QColor(141, 110, 189)
        purple.lightest = QColor(158, 142, 217)
        self._Purple = purple

        blue = FluAccentColor()
        blue.darkest = QColor(0, 74, 131)
        blue.darker = QColor(0, 84, 148)
        blue.dark = QColor(0, 102, 180)
        blue.normal = QColor(0, 120, 212)
        blue.light = QColor(38, 140, 220)
        blue.lighter = QColor(76, 160, 224)
        blue.lightest = QColor(96, 171, 228)
        self._Blue = blue

        teal = FluAccentColor()
        teal.darkest = QColor(0, 110, 91)
        teal.darker = QColor(0, 124, 103)
        teal.dark = QColor(0, 151, 125)
        teal.normal = QColor(0, 178, 148)
        teal.light = QColor(38, 189, 164)
        teal.lighter = QColor(77, 201, 180)
        teal.lightest = QColor(96, 207, 188)
        self._Teal = teal

        green = FluAccentColor()
        green.darkest = QColor(9, 76, 9)
        green.darker = QColor(12, 93, 12)
        green.dark = QColor(14, 111, 14)
        green.normal = QColor(16, 124, 16)
        green.light = QColor(39, 137, 57)
        green.lighter = QColor(76, 156, 76)
        green.lightest = QColor(106, 173, 106)
        self._Green = green

    @Property(QColor, notify=TransparentChanged)
    def Transparent(self):
        return self._Transparent

    @Transparent.setter
    def Transparent(self, value):
        self._Transparent = value
        self.TransparentChanged.emit()

    @Property(QColor, notify=BlackChanged)
    def Black(self):
        return self._Black

    @Black.setter
    def Black(self, value):
        self._Black = value
        self.BlackChanged.emit()

    @Property(QColor, notify=WhiteChanged)
    def White(self):
        return self._White

    @White.setter
    def White(self, value):
        self._White = value
        self.WhiteChanged.emit()

    @Property(QColor, notify=Grey10Changed)
    def Grey10(self):
        return self._Grey10

    @Grey10.setter
    def Grey10(self, value):
        self._Grey10 = value
        self.Grey10Changed.emit()

    @Property(QColor, notify=Grey20Changed)
    def Grey20(self):
        return self._Grey20

    @Grey20.setter
    def Grey20(self, value):
        self._Grey20 = value
        self.Grey20Changed.emit()

    @Property(QColor, notify=Grey30Changed)
    def Grey30(self):
        return self._Grey30

    @Grey30.setter
    def Grey30(self, value):
        self._Grey30 = value
        self.Grey30Changed.emit()

    @Property(QColor, notify=Grey40Changed)
    def Grey40(self):
        return self._Grey40

    @Grey40.setter
    def Grey40(self, value):
        self._Grey40 = value
        self.Grey40Changed.emit()

    @Property(QColor, notify=Grey50Changed)
    def Grey50(self):
        return self._Grey50

    @Grey50.setter
    def Grey50(self, value):
        self._Grey50 = value
        self.Grey50Changed.emit()

    @Property(QColor, notify=Grey60Changed)
    def Grey60(self):
        return self._Grey60

    @Grey60.setter
    def Grey60(self, value):
        self._Grey60 = value
        self.Grey60Changed.emit()

    @Property(QColor, notify=Grey70Changed)
    def Grey70(self):
        return self._Grey70

    @Grey70.setter
    def Grey70(self, value):
        self._Grey70 = value
        self.Grey70Changed.emit()

    @Property(QColor, notify=Grey80Changed)
    def Grey80(self):
        return self._Grey80

    @Grey80.setter
    def Grey80(self, value):
        self._Grey80 = value
        self.Grey80Changed.emit()

    @Property(QColor, notify=Grey90Changed)
    def Grey90(self):
        return self._Grey90

    @Grey90.setter
    def Grey90(self, value):
        self._Grey90 = value
        self.Grey90Changed.emit()

    @Property(QColor, notify=Grey100Changed)
    def Grey100(self):
        return self._Grey100

    @Grey100.setter
    def Grey100(self, value):
        self._Grey100 = value
        self.Grey100Changed.emit()

    @Property(QColor, notify=Grey110Changed)
    def Grey110(self):
        return self._Grey110

    @Grey110.setter
    def Grey110(self, value):
        self._Grey110 = value
        self.Grey110Changed.emit()

    @Property(QColor, notify=Grey120Changed)
    def Grey120(self):
        return self._Grey120

    @Grey120.setter
    def Grey120(self, value):
        self._Grey120 = value
        self.Grey120Changed.emit()

    @Property(QColor, notify=Grey130Changed)
    def Grey130(self):
        return self._Grey130

    @Grey130.setter
    def Grey130(self, value):
        self._Grey130 = value
        self.Grey130Changed.emit()

    @Property(QColor, notify=Grey140Changed)
    def Grey140(self):
        return self._Grey140

    @Grey140.setter
    def Grey140(self, value):
        self._Grey140 = value
        self.Grey140Changed.emit()

    @Property(QColor, notify=Grey150Changed)
    def Grey150(self):
        return self._Grey150

    @Grey150.setter
    def Grey150(self, value):
        self._Grey150 = value
        self.Grey150Changed.emit()

    @Property(QColor, notify=Grey160Changed)
    def Grey160(self):
        return self._Grey160

    @Grey160.setter
    def Grey160(self, value):
        self._Grey160 = value
        self.Grey160Changed.emit()

    @Property(QColor, notify=Grey170Changed)
    def Grey170(self):
        return self._Grey170

    @Grey170.setter
    def Grey170(self, value):
        self._Grey170 = value
        self.Grey170Changed.emit()

    @Property(QColor, notify=Grey180Changed)
    def Grey180(self):
        return self._Grey180

    @Grey180.setter
    def Grey180(self, value):
        self._Grey180 = value
        self.Grey180Changed.emit()

    @Property(QColor, notify=Grey190Changed)
    def Grey190(self):
        return self._Grey190

    @Grey190.setter
    def Grey190(self, value):
        self._Grey190 = value
        self.Grey190Changed.emit()

    @Property(QColor, notify=Grey200Changed)
    def Grey200(self):
        return self._Grey200

    @Grey200.setter
    def Grey200(self, value):
        self._Grey200 = value
        self.Grey200Changed.emit()

    @Property(QColor, notify=Grey210Changed)
    def Grey210(self):
        return self._Grey210

    @Grey210.setter
    def Grey210(self, value):
        self._Grey210 = value
        self.Grey210Changed.emit()

    @Property(QColor, notify=Grey220Changed)
    def Grey220(self):
        return self._Grey220

    @Grey220.setter
    def Grey220(self, value):
        self._Grey220 = value
        self.Grey220Changed.emit()

    @Property(FluAccentColor, notify=YellowChanged)
    def Yellow(self):
        return self._Yellow

    @Yellow.setter
    def Yellow(self, value):
        self._Yellow = value
        self.YellowChanged.emit()

    @Property(FluAccentColor, notify=OrangeChanged)
    def Orange(self):
        return self._Orange

    @Orange.setter
    def Orange(self, value):
        self._Orange = value
        self.OrangeChanged.emit()

    @Property(FluAccentColor, notify=RedChanged)
    def Red(self):
        return self._Red

    @Red.setter
    def Red(self, value):
        self._Red = value
        self.RedChanged.emit()

    @Property(FluAccentColor, notify=MagentaChanged)
    def Magenta(self):
        return self._Magenta

    @Magenta.setter
    def Magenta(self, value):
        self._Magenta = value
        self.MagentaChanged.emit()

    @Property(FluAccentColor, notify=PurpleChanged)
    def Purple(self):
        return self._Purple

    @Purple.setter
    def Purple(self, value):
        self._Purple = value
        self.PurpleChanged.emit()

    @Property(FluAccentColor, notify=BlueChanged)
    def Blue(self):
        return self._Blue

    @Blue.setter
    def Blue(self, value):
        self._Blue = value
        self.BlueChanged.emit()

    @Property(FluAccentColor, notify=TealChanged)
    def Teal(self):
        return self._Teal

    @Teal.setter
    def Teal(self, value):
        self._Teal = value
        self.TealChanged.emit()

    @Property(FluAccentColor, notify=GreenChanged)
    def Green(self):
        return self._Green

    @Green.setter
    def Green(self, value):
        self._Green = value
        self.GreenChanged.emit()

    @Slot(QColor, result=FluAccentColor)
    def createAccentColor(self, val):
        accentColor = FluAccentColor(self)
        accentColor.normal = val
        accentColor.dark = FluTools().withOpacity(val, 0.9)
        accentColor.light = FluTools().withOpacity(val, 0.9)
        accentColor.darker = FluTools().withOpacity(accentColor.dark, 0.8)
        accentColor.lighter = FluTools().withOpacity(accentColor.light, 0.8)
        accentColor.darkest = FluTools().withOpacity(accentColor.darker, 0.7)
        accentColor.lightest = FluTools().withOpacity(accentColor.lighter, 0.7)
        return accentColor
