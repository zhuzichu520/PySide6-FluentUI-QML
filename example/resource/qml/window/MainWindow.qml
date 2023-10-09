import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import Qt.labs.platform
import FluentUI

FluWindow {

    id:window
    title: "FluentUI"
    width: 1000
    height: 640
    minimumWidth: 520
    minimumHeight: 200

    FluText{
        text:"asd"
        anchors.bottom: parent.bottom
    }

    FluButton{
        anchors.centerIn: parent
        text:"123"
    }

    Rectangle{
        width: 100
        height: 100
        color:"red"
    }

}
