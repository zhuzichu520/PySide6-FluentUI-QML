from PySide6.QtCore import qDebug, QUrl
from PySide6.QtQml import qmlRegisterType, qmlRegisterUncreatableMetaObject, qmlRegisterSingletonType

from FluentUI.Def import FluCalendarViewType
from FluentUI.Def import FluContentDialogType
from FluentUI.Def import FluNavigationViewType
from FluentUI.Def import FluPageType
from FluentUI.Def import FluSheetType
from FluentUI.Def import FluStatusLayoutType
from FluentUI.Def import FluTabViewType
from FluentUI.Def import FluThemeType
from FluentUI.Def import FluTimePickerType
from FluentUI.Def import FluTimelineType
from FluentUI.Def import FluTreeViewType
from FluentUI.Def import FluWindowType
from FluentUI.FluApp import FluApp
from FluentUI.FluCaptcha import FluCaptcha
from FluentUI.FluColors import FluColors
from FluentUI.FluFrameless import FluFrameless
from FluentUI.FluHotkey import FluHotkey
from FluentUI.FluQrCodeItem import FluQrCodeItem
from FluentUI.FluRectangle import FluRectangle
from FluentUI.FluTableModel import FluTableModel
from FluentUI.FluTableSortProxyModel import FluTableSortProxyModel
from FluentUI.FluTextStyle import FluTextStyle
from FluentUI.FluTheme import FluTheme
from FluentUI.FluTools import FluTools
from FluentUI.FluTreeModel import FluTreeModel, FluTreeNode
from FluentUI.FluWatermark import FluWatermark
from FluentUI.FluentIconDef import FluentIcons
from FluentUI.imports import resource_rc as rc

'''
The FluentUI.py module contains classes and functions to interact with FluentUI
'''

_major = 1
_minor = 0
_uri = "FluentUI"


# noinspection PyPep8Naming
def registerTypes(engine):
    qDebug(f"Load the resource '{rc.__name__}'")
    _registerTypes(_uri, _major, _minor)
    _initializeEngine(engine)


# noinspection PyUnresolvedReferences,PyTypeChecker,PyPep8Naming,PyCallingNonCallable
def _registerTypes(uri: str, major: int, minor: int):
    qmlRegisterType(FluTreeNode, uri, major, minor, "FluTreeNode")
    qmlRegisterType(FluTreeModel, uri, major, minor, "FluTreeModel")
    qmlRegisterType(FluTableModel, uri, major, minor, "FluTableModel")
    qmlRegisterType(FluRectangle, uri, major, minor, "FluRectangle")
    qmlRegisterType(FluFrameless, uri, major, minor, "FluFrameless")
    qmlRegisterType(FluWatermark, uri, major, minor, "FluWatermark")
    qmlRegisterType(FluQrCodeItem, uri, major, minor, "FluQrCodeItem")
    qmlRegisterType(FluCaptcha, uri, major, minor, "FluCaptcha")
    qmlRegisterType(FluHotkey, uri, major, minor, "FluHotkey")
    qmlRegisterType(FluTableSortProxyModel, uri, major, minor, "FluTableSortProxyModel")

    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluAcrylic.qml"), uri, major, minor, "FluAcrylic")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluAppBar.qml"), uri, major, minor, "FluAppBar")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluFrame.qml"), uri, major, minor, "FluFrame")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluAutoSuggestBox.qml"), uri, major, minor, "FluAutoSuggestBox")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluBadge.qml"), uri, major, minor, "FluBadge")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluBreadcrumbBar.qml"), uri, major, minor, "FluBreadcrumbBar")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluButton.qml"), uri, major, minor, "FluButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluCalendarPicker.qml"), uri, major, minor, "FluCalendarPicker")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluCarousel.qml"), uri, major, minor, "FluCarousel")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluChart.qml"), uri, major, minor, "FluChart")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluCheckBox.qml"), uri, major, minor, "FluCheckBox")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluColorPicker.qml"), uri, major, minor, "FluColorPicker")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluComboBox.qml"), uri, major, minor, "FluComboBox")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluContentDialog.qml"), uri, major, minor, "FluContentDialog")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluContentPage.qml"), uri, major, minor, "FluContentPage")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluControl.qml"), uri, major, minor, "FluControl")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluCopyableText.qml"), uri, major, minor, "FluCopyableText")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluDatePicker.qml"), uri, major, minor, "FluDatePicker")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluDivider.qml"), uri, major, minor, "FluDivider")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluDropDownButton.qml"), uri, major, minor, "FluDropDownButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluExpander.qml"), uri, major, minor, "FluExpander")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluFilledButton.qml"), uri, major, minor, "FluFilledButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluFlipView.qml"), uri, major, minor, "FluFlipView")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluFocusRectangle.qml"), uri, major, minor, "FluFocusRectangle")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluIcon.qml"), uri, major, minor, "FluIcon")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluIconButton.qml"), uri, major, minor, "FluIconButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluImage.qml"), uri, major, minor, "FluImage")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluImageButton.qml"), uri, major, minor, "FluImageButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluInfoBar.qml"), uri, major, minor, "FluInfoBar")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluItemDelegate.qml"), uri, major, minor, "FluItemDelegate")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluMenu.qml"), uri, major, minor, "FluMenu")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluMenuBar.qml"), uri, major, minor, "FluMenuBar")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluMenuBarItem.qml"), uri, major, minor, "FluMenuBarItem")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluMenuItem.qml"), uri, major, minor, "FluMenuItem")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluMenuSeparator.qml"), uri, major, minor, "FluMenuSeparator")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluMultilineTextBox.qml"), uri, major, minor, "FluMultilineTextBox")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluNavigationView.qml"), uri, major, minor, "FluNavigationView")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluObject.qml"), uri, major, minor, "FluObject")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPage.qml"), uri, major, minor, "FluPage")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPagination.qml"), uri, major, minor, "FluPagination")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPaneItem.qml"), uri, major, minor, "FluPaneItem")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPaneItemEmpty.qml"), uri, major, minor, "FluPaneItemEmpty")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPaneItemExpander.qml"), uri, major, minor, "FluPaneItemExpander")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPaneItemHeader.qml"), uri, major, minor, "FluPaneItemHeader")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPaneItemSeparator.qml"), uri, major, minor, "FluPaneItemSeparator")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPasswordBox.qml"), uri, major, minor, "FluPasswordBox")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPivot.qml"), uri, major, minor, "FluPivot")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPivotItem.qml"), uri, major, minor, "FluPivotItem")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluPopup.qml"), uri, major, minor, "FluPopup")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluProgressBar.qml"), uri, major, minor, "FluProgressBar")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluProgressRing.qml"), uri, major, minor, "FluProgressRing")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluQRCode.qml"), uri, major, minor, "FluQRCode")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluRadioButton.qml"), uri, major, minor, "FluRadioButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluRadioButtons.qml"), uri, major, minor, "FluRadioButtons")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluRatingControl.qml"), uri, major, minor, "FluRatingControl")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluRemoteLoader.qml"), uri, major, minor, "FluRemoteLoader")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluScrollBar.qml"), uri, major, minor, "FluScrollBar")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluScrollIndicator.qml"), uri, major, minor, "FluScrollIndicator")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluScrollablePage.qml"), uri, major, minor, "FluScrollablePage")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluShadow.qml"), uri, major, minor, "FluShadow")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluSlider.qml"), uri, major, minor, "FluSlider")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluSpinBox.qml"), uri, major, minor, "FluSpinBox")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluStatusLayout.qml"), uri, major, minor, "FluStatusLayout")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTabView.qml"), uri, major, minor, "FluTabView")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTableView.qml"), uri, major, minor, "FluTableView")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluText.qml"), uri, major, minor, "FluText")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTextBox.qml"), uri, major, minor, "FluTextBox")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTextBoxBackground.qml"), uri, major, minor, "FluTextBoxBackground")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTextBoxMenu.qml"), uri, major, minor, "FluTextBoxMenu")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTextButton.qml"), uri, major, minor, "FluTextButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTimePicker.qml"), uri, major, minor, "FluTimePicker")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTimeline.qml"), uri, major, minor, "FluTimeline")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluToggleButton.qml"), uri, major, minor, "FluToggleButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluToggleSwitch.qml"), uri, major, minor, "FluToggleSwitch")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTooltip.qml"), uri, major, minor, "FluTooltip")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTour.qml"), uri, major, minor, "FluTour")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluTreeView.qml"), uri, major, minor, "FluTreeView")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluWindow.qml"), uri, major, minor, "FluWindow")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluWindowDialog.qml"), uri, major, minor, "FluWindowDialog")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluRangeSlider.qml"), uri, major, minor, "FluRangeSlider")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluStaggeredLayout.qml"), uri, major, minor, "FluStaggeredLayout")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluProgressButton.qml"), uri, major, minor, "FluProgressButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluLoadingButton.qml"), uri, major, minor, "FluLoadingButton")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluClip.qml"), uri, major, minor, "FluClip")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluLoader.qml"), uri, major, minor, "FluLoader")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluShortcutPicker.qml"), uri, major, minor, "FluShortcutPicker")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluSplitLayout.qml"), uri, major, minor, "FluSplitLayout")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluWindowResultLauncher.qml"), uri, major, minor, "FluWindowResultLauncher")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluLauncher.qml"), uri, major, minor, "FluLauncher")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluEvent.qml"), uri, major, minor, "FluEvent")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluSheet.qml"), uri, major, minor, "FluSheet")
    qmlRegisterType(QUrl("qrc:/FluentUI/Controls/FluGroupBox.qml"), uri, major, minor, "FluGroupBox")
    qmlRegisterSingletonType(QUrl("qrc:/FluentUI/Controls/FluRouter.qml"), uri, major, minor, "FluRouter")
    qmlRegisterSingletonType(QUrl("qrc:/FluentUI/Controls/FluEventBus.qml"), uri, major, minor, "FluEventBus")

    qmlRegisterUncreatableMetaObject(FluentIcons.staticMetaObject, uri, major, minor, "FluentIcons", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluThemeType.staticMetaObject, uri, major, minor, "FluThemeType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluPageType.staticMetaObject, uri, major, minor, "FluPageType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluWindowType.staticMetaObject, uri, major, minor, "FluWindowType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluTreeViewType.staticMetaObject, uri, major, minor, "FluTreeViewType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluStatusLayoutType.staticMetaObject, uri, major, minor, "FluStatusLayoutType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluContentDialogType.staticMetaObject, uri, major, minor, "FluContentDialogType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluTimePickerType.staticMetaObject, uri, major, minor, "FluTimePickerType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluCalendarViewType.staticMetaObject, uri, major, minor, "FluCalendarViewType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluTabViewType.staticMetaObject, uri, major, minor, "FluTabViewType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluNavigationViewType.staticMetaObject, uri, major, minor, "FluNavigationViewType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluTimelineType.staticMetaObject, uri, major, minor, "FluTimelineType", "Access to enums & flags only")
    qmlRegisterUncreatableMetaObject(FluSheetType.staticMetaObject, uri, major, minor, "FluSheetType", "Access to enums & flags only")


# noinspection PyPep8Naming,PyUnusedLocal
def _initializeEngine(engine):
    engine.rootContext().setContextProperty("FluTools", FluTools())
    engine.rootContext().setContextProperty("FluApp", FluApp())
    engine.rootContext().setContextProperty("FluTheme", FluTheme())
    engine.rootContext().setContextProperty("FluTextStyle", FluTextStyle())
    engine.rootContext().setContextProperty("FluColors", FluColors())
