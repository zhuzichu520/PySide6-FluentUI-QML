import QtQuick
import QtQuick.Layouts
import QtQuick.Window
import QtQuick.Controls
import FluentUI
import "qrc:///example/qml/component"

FluScrollablePage{

    title:"Dialog"

    FluArea{
        Layout.fillWidth: true
        height: 68
        paddings: 10
        Layout.topMargin: 20
        FluButton{
            anchors.verticalCenter: parent.verticalCenter
            Layout.topMargin: 20
            text:"Show Double Button Dialog"
            onClicked: {
                double_btn_dialog.open()
            }
        }
    }
    CodeExpander{
        Layout.fillWidth: true
        Layout.topMargin: -1
        code:'FluContentDialog{
    id:dialog
    title:"友情提示"
    message:"确定要退出程序么？"
    negativeText:"取消"
    buttonFlags: FluContentDialogType.NegativeButton | FluContentDialogType.PositiveButton
    onNegativeClicked:{
        showSuccess("点击取消按钮")
    }
    positiveText:"确定"
    onPositiveClicked:{
        showSuccess("点击确定按钮")
    }
    }
    dialog.open()'
    }

    FluContentDialog{
        id:double_btn_dialog
        title:"友情提示"
        message:"确定要退出程序么？"
        buttonFlags: FluContentDialogType.NegativeButton | FluContentDialogType.PositiveButton
        negativeText:"取消"
        onNegativeClicked:{
            showSuccess("点击取消按钮")
        }
        positiveText:"确定"
        onPositiveClicked:{
            showSuccess("点击确定按钮")
        }
    }

    FluArea{
        Layout.fillWidth: true
        height: 68
        paddings: 10
        Layout.topMargin: 20
        FluButton{
            anchors.verticalCenter: parent.verticalCenter
            Layout.topMargin: 20
            text:"Show Triple Button Dialog"
            onClicked: {
                triple_btn_dialog.open()
            }
        }
    }
    CodeExpander{
        Layout.fillWidth: true
        Layout.topMargin: -1
        code:'FluContentDialog{
    id:dialog
    title:"友情提示"
    message:"确定要退出程序么？"
    negativeText:"取消"
    buttonFlags: FluContentDialogType.NeutralButton | FluContentDialogType.NegativeButton | FluContentDialogType.PositiveButton
    negativeText:"取消"
    onNegativeClicked:{
        showSuccess("点击取消按钮")
    }
    positiveText:"确定"
    onPositiveClicked:{
        showSuccess("点击确定按钮")
    }
    neutralText:"最小化"
    onNeutralClicked:{
        showSuccess("点击最小化按钮")
        }
    }
    dialog.open()'
    }

    FluContentDialog{
        id:triple_btn_dialog
        title:"友情提示"
        message:"确定要退出程序么？"
        buttonFlags: FluContentDialogType.NeutralButton | FluContentDialogType.NegativeButton | FluContentDialogType.PositiveButton
        negativeText:"取消"
        onNegativeClicked:{
            showSuccess("点击取消按钮")
        }
        positiveText:"确定"
        onPositiveClicked:{
            showSuccess("点击确定按钮")
        }
        neutralText:"最小化"
        onNeutralClicked:{
            showSuccess("点击最小化按钮")
        }
    }

    FluArea{
        Layout.fillWidth: true
        height: 68
        paddings: 10
        Layout.topMargin: 20
        FluButton{
            anchors.verticalCenter: parent.verticalCenter
            Layout.topMargin: 20
            text:"Custom Content Dialog"
            onClicked: {
                custom_btn_dialog.open()
            }
        }
    }
    CodeExpander{
        Layout.fillWidth: true
        Layout.topMargin: -1
        code:'FluContentDialog{
    id:dialog
    title:"友情提示"
    message:"数据正在加载中，请稍等..."
    negativeText:"取消加载"
    contentDelegate: Component{
        Item{
            width: parent.width
            height: 80
            FluProgressRing{
                anchors.centerIn: parent
            }
        }
    }
    onNegativeClicked:{
        showSuccess("点击取消按钮")
    }
    positiveText:"确定"
    onPositiveClicked:{
        showSuccess("点击确定按钮")
    }
    dialog.open()'
    }

    FluContentDialog{
        id:custom_btn_dialog
        title:"友情提示"
        message:"数据正在加载中，请稍等..."
        negativeText:"取消加载"
        contentDelegate: Component{
            Item{
                width: parent.width
                height: 80
                FluProgressRing{
                    anchors.centerIn: parent
                }
            }
        }
        onNegativeClicked:{
            showSuccess("点击取消按钮")
        }
        positiveText:"确定"
        onPositiveClicked:{
            showSuccess("点击确定按钮")
        }
    }
}
