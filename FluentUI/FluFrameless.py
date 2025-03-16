from PySide6.QtCore import Signal, Slot, Qt, QPoint, QEvent, QAbstractNativeEventFilter, Property, QRectF, QDateTime, QPointF, QSize
from PySide6.QtGui import QMouseEvent, QGuiApplication, QCursor
from PySide6.QtQuick import QQuickItem
from PySide6.QtQuick import QQuickWindow
from FluentUI.FluTools import FluTools

Tools = FluTools()

if Tools.isWin():
    from ctypes import POINTER, byref, c_bool, c_int, c_void_p, c_long, WinDLL, cast, POINTER, Structure, c_uint, c_uint16, c_short
    from ctypes.wintypes import DWORD, HWND, MSG, RECT, UINT, POINT, RECTL


    # noinspection PyPep8Naming
    def HIWORD(dword):
        return c_uint16((dword >> 16) & 0xffff).value


    # noinspection PyPep8Naming
    def LOWORD(dword):
        return c_uint16(dword & 0xffff).value


    class MARGINS(Structure):
        _fields_ = [
            ("cxLeftWidth", c_int),
            ("cxRightWidth", c_int),
            ("cyTopHeight", c_int),
            ("cyBottomHeight", c_int),
        ]


    class PWINDOWPOS(Structure):
        _fields_ = [
            ('hWnd', HWND),
            ('hwndInsertAfter', HWND),
            ('x', c_int),
            ('y', c_int),
            ('cx', c_int),
            ('cy', c_int),
            ('flags', UINT)
        ]


    # noinspection PyPep8Naming
    class NCCALCSIZE_PARAMS(Structure):
        _fields_ = [
            ('rgrc', RECT * 3),
            ('lppos', POINTER(PWINDOWPOS))
        ]


    class MINMAXINFO(Structure):
        _fields_ = [
            ("ptReserved", POINT),
            ("ptMaxSize", POINT),
            ("ptMaxPosition", POINT),
            ("ptMinTrackSize", POINT),
            ("ptMaxTrackSize", POINT),
        ]


    LPNCCALCSIZE_PARAMS = POINTER(NCCALCSIZE_PARAMS)
    qtNativeEventType = b"windows_generic_MSG"
    user32 = WinDLL("user32")
    dwmapi = WinDLL("dwmapi")
    SystemParametersInfoW = user32.SystemParametersInfoW
    SystemParametersInfoW.argtypes = [c_uint, c_uint, c_void_p, c_uint]
    SystemParametersInfoW.restype = c_bool
    PostMessageW = user32.PostMessageW
    PostMessageW.argtypes = [c_void_p, c_uint, c_uint, c_long]
    PostMessageW.restype = c_bool
    TrackPopupMenu = user32.TrackPopupMenu
    TrackPopupMenu.argtypes = [c_void_p, c_uint, c_int, c_int, c_int, c_void_p, c_void_p]
    TrackPopupMenu.restype = c_int
    EnableMenuItem = user32.EnableMenuItem
    EnableMenuItem.argtypes = [c_void_p, c_uint, c_uint]
    EnableMenuItem.restype = c_bool
    GetSystemMenu = user32.GetSystemMenu
    GetSystemMenu.argtypes = [c_void_p, c_bool]
    GetSystemMenu.restype = c_void_p
    GetKeyState = user32.GetKeyState
    GetKeyState.argtypes = [c_int]
    GetKeyState.restype = c_short
    ScreenToClient = user32.ScreenToClient
    ScreenToClient.argtypes = [c_void_p, c_void_p]
    ScreenToClient.restype = c_bool
    GetClientRect = user32.GetClientRect
    GetClientRect.argtypes = [c_void_p, c_void_p]
    GetClientRect.restype = c_bool
    SetWindowPos = user32.SetWindowPos
    SetWindowPos.argtypes = [c_void_p, c_void_p, c_int, c_int, c_int, c_int, c_uint]
    SetWindowPos.restype = c_bool
    GetWindowLongPtrW = user32.GetWindowLongPtrW
    GetWindowLongPtrW.argtypes = [c_void_p, c_int]
    GetWindowLongPtrW.restype = c_long
    SetWindowLongPtrW = user32.SetWindowLongPtrW
    SetWindowLongPtrW.argtypes = [c_void_p, c_int, c_long]
    SetWindowLongPtrW.restype = c_long
    IsZoomed = user32.IsZoomed
    IsZoomed.argtypes = [c_void_p]
    IsZoomed.restype = c_bool
    DefWindowProcW = user32.DefWindowProcW
    DefWindowProcW.argtypes = [c_void_p, c_uint, c_uint, c_long]
    DefWindowProcW.restype = c_long
    DwmIsCompositionEnabled = dwmapi.DwmIsCompositionEnabled
    DwmIsCompositionEnabled.argtypes = [c_void_p]
    DwmIsCompositionEnabled.restype = c_long
    DwmExtendFrameIntoClientArea = dwmapi.DwmExtendFrameIntoClientArea
    DwmExtendFrameIntoClientArea.argtypes = [c_void_p, c_void_p]
    DwmExtendFrameIntoClientArea.restype = c_long


    # noinspection PyPep8Naming
    def isCompositionEnabled():
        bResult = c_int(0)
        dwmapi.DwmIsCompositionEnabled(byref(bResult))
        return bool(bResult.value)


    def setShadow(hwnd):
        margins = MARGINS(1, 0, 0, 0)
        dwmapi.DwmExtendFrameIntoClientArea(hwnd, byref(margins))


# noinspection PyCallingNonCallable,PyPep8Naming
class FluFrameless(QQuickItem, QAbstractNativeEventFilter):
    appbarChanged = Signal()
    topmostChanged = Signal()
    maximizeButtonChanged = Signal()
    minimizedButtonChanged = Signal()
    closeButtonChanged = Signal()
    disabledChanged = Signal()
    fixSizeChanged = Signal()

    def __init__(self):
        QQuickItem.__init__(self)
        QAbstractNativeEventFilter.__init__(self)
        self._current: int = 0
        self._edges: int = 0
        self._margins: int = 8
        self._clickTimer: int = 0
        self._hitTestList: list[QQuickItem] = []
        self._appbar = None
        self._topmost: bool = False
        self._maximizeButton = None
        self._minimizedButton = None
        self._closeButton = None
        self._disabled: bool = False
        self._fixSize: bool = False
        self._isWindows11OrGreater = Tools.isWindows11OrGreater()

    @Property(QQuickItem, notify=appbarChanged)
    def appbar(self):
        return self._appbar

    @appbar.setter
    def appbar(self, value):
        self._appbar = value
        self.appbarChanged.emit()

    @Property(bool, notify=topmostChanged)
    def topmost(self):
        return self._topmost

    @topmost.setter
    def topmost(self, value):
        self._topmost = value
        self.topmostChanged.emit()

    @Property(QQuickItem, notify=maximizeButtonChanged)
    def maximizeButton(self):
        return self._maximizeButton

    @maximizeButton.setter
    def maximizeButton(self, value):
        self._maximizeButton = value
        self.maximizeButtonChanged.emit()

    @Property(QQuickItem, notify=minimizedButtonChanged)
    def minimizedButton(self):
        return self._minimizedButton

    @minimizedButton.setter
    def minimizedButton(self, value):
        self._minimizedButton = value
        self.minimizedButtonChanged.emit()

    @Property(QQuickItem, notify=closeButtonChanged)
    def closeButton(self):
        return self._closeButton

    @closeButton.setter
    def closeButton(self, value):
        self._closeButton = value
        self.closeButtonChanged.emit()

    @Property(bool, notify=disabledChanged)
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value):
        self._disabled = value
        self.disabledChanged.emit()

    @Property(bool, notify=fixSizeChanged)
    def fixSize(self):
        return self._fixSize

    @fixSize.setter
    def fixSize(self, value):
        self._fixSize = value
        self.fixSizeChanged.emit()

    @Slot()
    def onDestruction(self):
        QGuiApplication.instance().removeNativeEventFilter(self)

    def componentComplete(self):
        if self._disabled:
            return
        w = self.window().width()
        h = self.window().height()
        self._current = self.window().winId()
        self.window().setFlags(
            self.window().flags() | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        if not self._fixSize:
            self.window().setFlag(Qt.WindowType.WindowMaximizeButtonHint)
        self.window().installEventFilter(self)
        QGuiApplication.instance().installNativeEventFilter(self)
        if self._maximizeButton is not None:
            self.setHitTestVisible(self._maximizeButton)
        if self._minimizedButton is not None:
            self.setHitTestVisible(self._minimizedButton)
        if self._closeButton is not None:
            self.setHitTestVisible(self._closeButton)
        if Tools.isWin():
            hwnd = self.window().winId()
            style: DWORD = GetWindowLongPtrW(hwnd, -16)
            if self._fixSize:
                SetWindowLongPtrW(hwnd, -16, style | 0x00040000 | 0x00C00000)
            else:
                SetWindowLongPtrW(hwnd, -16, style | 0x00010000 | 0x00040000 | 0x00C00000)
            SetWindowPos(hwnd, None, 0, 0, 0, 0, 0x0004 | 0x0200 | 0x0002 | 0x0001 | 0x0020)
            if not self.window().property("_hideShadow"):
                setShadow(hwnd)
        appBarHeight = self._appbar.height()
        h = int(h + appBarHeight)
        if self._fixSize:
            self.window().setMinimumSize(QSize(w, h))
            self.window().setMaximumSize(QSize(w, h))
        else:
            self.window().setMinimumHeight(self.window().minimumHeight() + appBarHeight)
            self.window().setMaximumHeight(self.window().maximumHeight() + appBarHeight)
        self.window().resize(w, h)
        self.topmostChanged.connect(self, lambda: self._setWindowTopmost(self._topmost))
        self._setWindowTopmost(self._topmost)

    def nativeEventFilter(self, eventType, message):
        if not Tools.isWin():
            return False
        if eventType != qtNativeEventType or message is None:
            return False
        msg = MSG.from_address(message.__int__())
        hwnd = msg.hWnd
        if hwnd is None and msg is None:
            return False
        if hwnd != self._current:
            return False
        uMsg = msg.message
        wParam = msg.wParam
        lParam = msg.lParam
        if uMsg == 0x0046:
            wp = cast(lParam, POINTER(PWINDOWPOS)).contents
            if (wp is not None) and ((wp.flags & 0x0001) == 0):
                wp.flags |= 0x0100
            return False
        elif uMsg == 0x0083:
            isMaximum = bool(IsZoomed(hwnd))
            if isMaximum:
                self.window().setProperty("__margins",7)
            else:
                self.window().setProperty("__margins", 0)
            self._setMaximizeHovered(False)
            return True, 0x0100 | 0x0200
        elif uMsg == 0x0084:
            if self._isWindows11OrGreater:
                if self._hitMaximizeButton():
                    self._setMaximizeHovered(True)
                    return True, 9
                self._setMaximizeHovered(False)
                self._setMaximizePressed(False)
            nativeGlobalPos = POINT(LOWORD(lParam), HIWORD(lParam))
            nativeLocalPos = POINT(nativeGlobalPos.x, nativeGlobalPos.y)
            ScreenToClient(hwnd, byref(nativeLocalPos))
            clientRect = RECTL(0, 0, 0, 0)
            GetClientRect(hwnd, byref(clientRect))
            clientWidth = clientRect.right - clientRect.left
            clientHeight = clientRect.bottom - clientRect.top
            left = nativeLocalPos.x < self._margins
            right = nativeLocalPos.x > clientWidth - self._margins
            top = nativeLocalPos.y < self._margins
            bottom = nativeLocalPos.y > clientHeight - self._margins
            result = 0
            if not self._fixSize and not self._isFullScreen() and not self._isMaximized():
                if left and top:
                    result = 13
                elif left and bottom:
                    result = 16
                elif right and top:
                    result = 14
                elif right and bottom:
                    result = 17
                elif left:
                    result = 10
                elif right:
                    result = 11
                elif top:
                    result = 12
                elif top:
                    result = 15
            if result != 0:
                return True, result
            if self._hitAppBar():
                return True, 2
            return True, 1
        elif self._isWindows11OrGreater and (uMsg == 0x00A3 or uMsg == 0x00A1):
            if self._hitMaximizeButton():
                event = QMouseEvent(QEvent.Type.MouseButtonPress, QPoint(), QPoint(), Qt.MouseButton.LeftButton, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
                QGuiApplication.instance().sendEvent(self._maximizeButton, event)
                self._setMaximizePressed(True)
                return True, 0
        elif self._isWindows11OrGreater and (uMsg == 0x00A2 or uMsg == 0x00A5):
            if self._hitMaximizeButton():
                event = QMouseEvent(QEvent.Type.MouseButtonRelease, QPoint(), QPoint(), Qt.MouseButton.LeftButton, Qt.MouseButton.LeftButton, Qt.KeyboardModifier.NoModifier)
                QGuiApplication.instance().sendEvent(self._maximizeButton, event)
                self._setMaximizePressed(False)
        elif uMsg == 0x0085:
            return False, 0
        elif uMsg == 0x0024:
            minmaxInfo = cast(lParam, POINTER(MINMAXINFO)).contents
            pixelRatio = self.window().devicePixelRatio()
            geometry = self.window().screen().availableGeometry()
            rect = RECT()
            SystemParametersInfoW(0x0030, 0, byref(rect), 0)
            minmaxInfo.ptMaxPosition.x = rect.left
            minmaxInfo.ptMaxPosition.y = rect.top
            minmaxInfo.ptMaxSize.x = int(geometry.width() * pixelRatio)
            minmaxInfo.ptMaxSize.y = int(geometry.height() * pixelRatio)
            return False
        elif uMsg == 0x00A4:
            if wParam == 2:
                pos = self.window().position()
                offset = self.window().mapFromGlobal(QCursor.pos())
                self._showSystemMenu(QPoint(pos.x() + offset.x(), pos.y() + offset.y()))
                return True, 1
        elif uMsg == 0x0100 or uMsg == 0x0104:
            altPressed = (wParam == 0x12) or (GetKeyState(0x12) < 0)
            spacePressed = (wParam == 0x20) or (GetKeyState(0x20) < 0)
            if altPressed and spacePressed:
                pos = self.window().position()
                self._showSystemMenu(QPoint(pos.x(), int(pos.y() + self._appbar.height())))
        return False

    def eventFilter(self, watched, event):
        if self.window() is not None:
            if event.type() == QEvent.Type.MouseButtonPress:
                if self._edges != 0:
                    mouse_event = QMouseEvent(event)
                    if mouse_event.button() == Qt.MouseButton.LeftButton:
                        self._updateCursor(self._edges)
                        self.window().startSystemResize(Qt.Edge(self._edges))
                else:
                    if self._hitAppBar():
                        clickTimer = QDateTime.currentMSecsSinceEpoch()
                        offset = clickTimer - self._clickTimer
                        self._clickTimer = clickTimer
                        if offset < 300:
                            if self._isMaximized():
                                self.showNormal()
                            else:
                                self.showMaximized()
                        else:
                            self.window().startSystemMove()
            elif event.type() == QEvent.Type.MouseButtonRelease:
                self._edges = 0
            elif event.type() == QEvent.Type.MouseMove:
                if self._isMaximized() or self._isFullScreen():
                    return False
                if self._fixSize:
                    return False
                mouse_event = QMouseEvent(event)
                p = mouse_event.position().toPoint()
                if self._margins <= p.x() <= (self.window().width() - self._margins) and self._margins <= p.y() <= (self.window().height() - self._margins):
                    if self._edges != 0:
                        self._edges = 0
                        self._updateCursor(self._edges)
                    return False
                self._edges = 0
                if p.x() < self._margins:
                    self._edges |= 0x00002
                if p.x() > (self.window().width() - self._margins):
                    self._edges |= 0x00004
                if p.y() < self._margins:
                    self._edges |= 0x00001
                if p.y() > (self.window().height() - self._margins):
                    self._edges |= 0x00008
                self._updateCursor(self._edges)
        return False

    @Slot()
    def showFullScreen(self):
        self.window().showFullScreen()

    @Slot()
    def showMaximized(self):
        if Tools.isWin():
            hwnd = self.window().winId()
            user32.ShowWindow(hwnd, 3)
        else:
            self.window().showMaximized()

    @Slot()
    def showMinimized(self):
        if Tools.isWin():
            hwnd = self.window().winId()
            user32.ShowWindow(hwnd, 2)
        else:
            self.window().showMinimized()

    @Slot()
    def showNormal(self):
        self.window().showNormal()

    @Slot(QQuickItem)
    def setHitTestVisible(self, val: QQuickItem):
        self._hitTestList.append(val)

    def _containsCursorToItem(self, item: QQuickItem):
        try:
            if not item or not item.isVisible():
                return False
            point = item.window().mapFromGlobal(QCursor.pos())
            rect = QRectF(item.mapToItem(item.window().contentItem(), QPointF(0, 0)), item.size())
            if rect.contains(point):
                return True
        except RuntimeError:
            self._hitTestList.remove(item)
            return False
        return False

    def _isFullScreen(self):
        return self.window().visibility == QQuickWindow.Visibility.FullScreen

    def _isMaximized(self):
        return self.window().visibility == QQuickWindow.Visibility.Maximized

    def _updateCursor(self, edges: int):
        if edges == 0:
            self.window().setCursor(Qt.CursorShape.ArrowCursor)
        elif edges == 0x00002 or edges == 0x00004:
            self.window().setCursor(Qt.CursorShape.SizeHorCursor)
        elif edges == 0x00001 or edges == 0x00008:
            self.window().setCursor(Qt.CursorShape.SizeVerCursor)
        elif edges == 0x00002 | 0x00001 or edges == 0x00004 | 0x00008:
            self.window().setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif edges == 0x00004 | 0x00001 or edges == 0x00002 | 0x00008:
            self.window().setCursor(Qt.CursorShape.SizeBDiagCursor)

    def _setWindowTopmost(self, topmost: bool):
        if Tools.isWin():
            if topmost:
                SetWindowPos(self.window().winId(), -1, 0, 0, 0, 0, 0x0002 | 0x0001)
            else:
                SetWindowPos(self.window().winId(), -2, 0, 0, 0, 0, 0x0002 | 0x0001)
        else:
            self.window().setFlag(Qt.WindowType.WindowStaysOnTopHint, topmost)

    def _showSystemMenu(self, point: QPoint):
        if Tools.isWin():
            screen = self.window().screen()
            origin = screen.geometry().topLeft()
            nativePos = QPointF(QPointF(point - origin) * self.window().devicePixelRatio()).toPoint() + origin
            hwnd = self.window().winId()
            hMenu = GetSystemMenu(hwnd, False)
            if self._isMaximized() or self._isFullScreen():
                EnableMenuItem(hMenu, 0xF010, 0x00000003)
                EnableMenuItem(hMenu, 0xF120, 0x00000000)
            else:
                EnableMenuItem(hMenu, 0xF010, 0x00000000)
                EnableMenuItem(hMenu, 0xF120, 0x00000003)

            if not self._isMaximized() and not self._isFullScreen():
                EnableMenuItem(hMenu, 0xF000, 0x00000000)
                EnableMenuItem(hMenu, 0xF030, 0x00000000)
            else:
                EnableMenuItem(hMenu, 0xF000, 0x00000003)
                EnableMenuItem(hMenu, 0xF030, 0x00000003)
            result = TrackPopupMenu(hMenu, (0x0100 | (0x0008 if QGuiApplication.isRightToLeft() else 0x0000)), nativePos.x(),
                                    nativePos.y(), 0, hwnd, 0)
            if result:
                PostMessageW(hwnd, 0x0112, result, 0)

    def _setMaximizePressed(self, val):
        self._maximizeButton.setProperty("down", val)

    def _setMaximizeHovered(self, val):
        self._maximizeButton.setProperty("hover", val)

    def _hitAppBar(self):
        for item in self._hitTestList:
            if self._containsCursorToItem(item):
                return False
        if self._containsCursorToItem(self._appbar):
            return True
        return False

    def _hitMaximizeButton(self):
        if self._containsCursorToItem(self._maximizeButton):
            return True
        return False
