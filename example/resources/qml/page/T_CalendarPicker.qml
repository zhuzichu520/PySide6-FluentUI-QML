import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Window
import FluentUI
import "qrc:///example/qml/component"

FluScrollablePage{

    title:"CalendarPicker"

    FluArea{
        Layout.fillWidth: true
        Layout.topMargin: 20
        height: 350
        paddings: 10
        FluCalendarView{
        }
    }
    CodeExpander{
        Layout.fillWidth: true
        Layout.topMargin: -1
        code:'FluCalendarView{

}'
    }

    FluArea{
        Layout.fillWidth: true
        Layout.topMargin: 20
        height: 80
        paddings: 10
        ColumnLayout{
            anchors{
                verticalCenter: parent.verticalCenter
                left: parent.left
            }
            FluCalendarPicker{
                current:new Date()
                onAccepted:{
                    showSuccess(current.toLocaleString())
                }
            }
        }
    }
    CodeExpander{
        Layout.fillWidth: true
        Layout.topMargin: -1
        code:'FluCalendarPicker{

}'
    }

}
