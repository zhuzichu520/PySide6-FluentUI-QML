import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import FluentUI
import "qrc:///example/qml/component"

FluWindow {

    id:window
    title:"SingleTask"
    width: 500
    height: 600
    fixSize: true
    launchMode: FluWindowType.SingleTask

    FluText{
        anchors.centerIn: parent
        text:"我是一个SingleTask模式的窗口，如果我存在，我就激活窗口"
    }

}
