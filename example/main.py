# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtNetwork import QNetworkProxy
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# sys.path.append("D:\PyProjects\PySide6-FluentUI-QML")
import FluentUI
from helper.SettingsHelper import SettingsHelper
from AppInfo import AppInfo
import resource.example_rc as rc
from component.CircularReveal import CircularReveal
from component.FileWatcher import FileWatcher
from component.FpsItem import FpsItem

if __name__ == "__main__":
    QNetworkProxy.setApplicationProxy(QNetworkProxy.ProxyType.NoProxy)
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Basic"
    QGuiApplication.setOrganizationName("ZhuZiChu")
    QGuiApplication.setOrganizationDomain("https://zhuzichu520.github.io")
    QGuiApplication.setApplicationName("FluentUI")
    SettingsHelper().init()
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    rootContext = engine.rootContext()
    rootContext.setContextProperty("SettingsHelper", SettingsHelper())
    rootContext.setContextProperty("AppInfo", AppInfo())
    FluentUI.init(engine)
    print(engine.importPathList())
    qml_file = "qrc:/example/qml/App.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
