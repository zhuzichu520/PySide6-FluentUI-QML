import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import FluentUI

Window {
    id: app
    flags: Qt.SplashScreen
    Component.onCompleted: {
        FluApp.init(app)
        FluTheme.darkMode = SettingsHelper.getDarkMode()
        console.debug(SettingsHelper.getDarkMode())
        FluTheme.enableAnimation = true
        FluApp.routes = {
            "/":"qrc:/example/qml/window/MainWindow.qml"
        }
        FluApp.initialRoute = "/"
        FluApp.run()
    }
}
