import QtQuick
import QtQuick.Layouts
import QtQuick.Window
import QtQuick.Controls
import FluentUI
import "qrc:///example/qml/component"

FluScrollablePage{

    title:"RadioButton"

    FluArea{
        Layout.fillWidth: true
        height: 68
        paddings: 10
        Layout.topMargin: 20
        Row{
            spacing: 30
            anchors.verticalCenter: parent.verticalCenter
            FluRadioButton{
                disabled: radio_button_switch.checked
            }
            FluRadioButton{
                disabled: radio_button_switch.checked
                text:"Right"
            }
            FluRadioButton{
                disabled: radio_button_switch.checked
                text:"Left"
                textRight: false
            }
        }
        FluToggleSwitch{
            id:radio_button_switch
            anchors{
                right: parent.right
                verticalCenter: parent.verticalCenter
            }
            text:"Disabled"
        }
    }
    CodeExpander{
        Layout.fillWidth: true
        Layout.topMargin: -1
        code:'FluRadioButton{
    text:"Text"
}'
    }

    FluArea{
        Layout.fillWidth: true
        height: 100
        paddings: 10
        Layout.topMargin: 20
        FluRadioButtons{
            spacing: 8
            anchors.verticalCenter: parent.verticalCenter
            anchors{
                verticalCenter: parent.verticalCenter
                left: parent.left
            }
            FluRadioButton{
                disabled: radio_button_switch2.checked
                text:"Radio Button_1"
            }
            FluRadioButton{
                disabled: radio_button_switch2.checked
                text:"Radio Button_2"
            }
            FluRadioButton{
                disabled: radio_button_switch2.checked
                text:"Radio Button_3"
            }
        }
        FluToggleSwitch{
            id:radio_button_switch2
            anchors{
                right: parent.right
                verticalCenter: parent.verticalCenter
            }
            text:"Disabled"
        }
    }
    CodeExpander{
        Layout.fillWidth: true
        Layout.topMargin: -1
        code:'FluRadioButtons{
    spacing: 8
    FluRadioButton{
        text:"Radio Button_1"
    }
    FluRadioButton{
        text:"Radio Button_2"
    }
    FluRadioButton{
        text:"Radio Button_3"
    }
}'
    }

}
