from enum import IntFlag

from PySide6.QtCore import QObject, QFlag


# noinspection DuplicatedCode
class FluSheetType(QObject):
    class Position(IntFlag):
        Left = 0x0000
        Top = 0x0001
        Right = 0x0002
        Bottom = 0x0004

    QFlag(Position)


class FluThemeType(QObject):
    class DarkMode(IntFlag):
        System = 0x0000
        Light = 0x0001
        Dark = 0x0002

    QFlag(DarkMode)


class FluTimelineType(QObject):
    class Mode(IntFlag):
        Left = 0x0000
        Right = 0x0001
        Alternate = 0x0002

    QFlag(Mode)


# noinspection DuplicatedCode
class FluPageType(QObject):
    class LaunchMode(IntFlag):
        Standard = 0x0000
        SingleTask = 0x0001
        SingleTop = 0x0002
        SingleInstance = 0x0004

    QFlag(LaunchMode)


class FluWindowType(QObject):
    class LaunchMode(IntFlag):
        Standard = 0x0000
        SingleTask = 0x0001
        SingleInstance = 0x0002

    QFlag(LaunchMode)


class FluTreeViewType(QObject):
    class SelectionMode(IntFlag):
        Standard = 0x0000
        Single = 0x0001
        Multiple = 0x0002

    QFlag(SelectionMode)


class FluStatusLayoutType(QObject):
    class StatusMode(IntFlag):
        Loading = 0x0000
        Empty = 0x0001
        Error = 0x0002
        Success = 0x0004

    QFlag(StatusMode)


class FluContentDialogType(QObject):
    class ButtonFlag(IntFlag):
        NeutralButton = 0x0001
        NegativeButton = 0x0002
        PositiveButton = 0x0004

    QFlag(ButtonFlag)


class FluTimePickerType(QObject):
    class HourFormat(IntFlag):
        H = 0x0000
        HH = 0x0001

    QFlag(HourFormat)


class FluCalendarViewType(QObject):
    class DisplayMode(IntFlag):
        Month = 0x0000
        Year = 0x0001
        Decade = 0x0002

    QFlag(DisplayMode)


class FluTabViewType(QObject):
    class TabWidthBehavior(IntFlag):
        Equal = 0x0000
        SizeToContent = 0x0001
        Compact = 0x0002

    QFlag(TabWidthBehavior)

    class CloseButtonVisibility(IntFlag):
        Never = 0x0000
        Always = 0x0001
        OnHover = 0x0002

    QFlag(CloseButtonVisibility)


class FluNavigationViewType(QObject):
    class DisplayMode(IntFlag):
        Open = 0x0000
        Compact = 0x0001
        Minimal = 0x0002
        Auto = 0x0002

    QFlag(DisplayMode)

    class PageMode(IntFlag):
        Stack = 0x0000
        NoStack = 0x0001

    QFlag(PageMode)
