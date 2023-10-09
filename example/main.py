# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# sys.path.append("D:\PyProjects\PySide6-FluentUI-QML")
import FluentUI
import resource.res as res

if __name__ == "__main__":
    print(res.__file__)
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    FluentUI.init(engine)
    print(engine.importPathList())
    qml_file = "qrc:/example/qml/App.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
