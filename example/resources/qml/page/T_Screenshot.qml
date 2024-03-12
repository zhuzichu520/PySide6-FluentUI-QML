import QtQuick
import QtQuick.Layouts
import QtQuick.Window
import QtQuick.Controls
import FluentUI
import Qt.labs.platform
import "qrc:///example/qml/component"

FluScrollablePage{

    title:"Screenshot"

    FluArea{
        Layout.fillWidth: true
        height: 100
        paddings: 10
        Layout.topMargin: 20

        FluFilledButton{
            anchors.verticalCenter: parent.verticalCenter
            text:"Open Screenshot"
            onClicked: {
                screenshot.open()
            }
        }
    }

    Rectangle{
        Layout.preferredHeight: 400
        Layout.preferredWidth: 400
        Layout.topMargin: 10
        Layout.leftMargin: 4
        Layout.bottomMargin: 4
        radius: 4
        color: FluTheme.dark ? FluColors.Black : FluColors.White
        FluShadow{
            radius: 4
            color: FluTheme.primaryColor
        }
        Image{
            id:image
            anchors.fill: parent
            fillMode: Image.PreserveAspectFit
            asynchronous: true
        }
    }

    FluScreenshot{
        id:screenshot
        captrueMode: FluScreenshotType.File
        saveFolder: StandardPaths.writableLocation(StandardPaths.AppLocalDataLocation)+"/screenshot"
        onCaptrueCompleted:
            (captrue)=>{
                image.source = captrue
            }
    }
}
