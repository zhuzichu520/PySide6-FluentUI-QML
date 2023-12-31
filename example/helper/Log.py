# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QDir, qInstallMessageHandler, QFile, QTextStream,QtMsgType,QStandardPaths,QDateTime,qDebug,QSysInfo
import sys
import threading
from AppInfo import AppInfo
import os

QT_ENDL = "\n"

g_app = ""
g_file_path = ""
g_logError = False

g_logFile = None
g_logStream = None
g_logLevel = 4

def getLevelByMsgType(type):
    if(type == QtMsgType.QtFatalMsg):
        return 0
    if(type == QtMsgType.QtCriticalMsg):
        return 1
    if(type == QtMsgType.QtWarningMsg):
        return 2
    if(type == QtMsgType.QtInfoMsg):
        return 3
    if(type == QtMsgType.QtDebugMsg):
        return 4
    return -1

def getMsgNamebyType(type):
    if(type == QtMsgType.QtFatalMsg):
        return "Fatal"
    if(type == QtMsgType.QtCriticalMsg):
        return "Critical"
    if(type == QtMsgType.QtWarningMsg):
        return "Warning"
    if(type == QtMsgType.QtInfoMsg):
        return "Info"
    if(type == QtMsgType.QtDebugMsg):
        return "Debug"
    return "Unkown"

def myMessageHandler(type, context, message):
    global g_logError, g_logFile, g_logStream, g_logLevel
    if message.strip() == "":
        return
    if message == "Could not get the INetworkConnection instance for the adapter GUID.":
        return
    if getLevelByMsgType(type)>g_logLevel:
        return
    
    msgName = getMsgNamebyType(type)
    fileAndLineLogStr = ""
    if context.file:
        strFileTmp = context.file
        ptr = strFileTmp.rfind('/')
        if ptr != -1:
            strFileTmp = strFileTmp[ptr + 1:]
        ptrTmp = strFileTmp.rfind('\\')
        if ptrTmp != -1:
            strFileTmp = strFileTmp[ptrTmp + 1:]
        fileAndLineLogStr = f"[{strFileTmp}:{str(context.line)}]"
    finalMessage = f"{QDateTime.currentDateTime().toString('yyyy/MM/dd hh:mm:ss.zzz')}[{msgName}]{fileAndLineLogStr}[{threading.get_ident()}]:{message}"
    if type in [QtMsgType.QtInfoMsg, QtMsgType.QtDebugMsg]:
        print(finalMessage)
    else:
        print(finalMessage, file=sys.stderr)
    if g_logError:
        return
    if g_logFile is None:
        g_logFile = QFile(g_file_path)
        if not g_logFile.open(QFile.WriteOnly | QFile.Text | QFile.Append):
            print(f"Can't open file to write: {g_logFile.errorString()}", file=sys.stderr)
            g_logFile = None
            g_logError = True
            return
    if g_logStream is None:
        g_logStream = QTextStream()
        g_logStream.setDevice(g_logFile)
    g_logStream << finalMessage << QT_ENDL

def setup(app):
    global g_app,g_file_path
    assert app.strip() != ""
    if app.strip() == "":
        return
    g_app = app
    logFileName = f"{g_app}_{QDateTime.currentDateTime().toString('yyyyMMdd')}.log"
    logDirPath = QStandardPaths.writableLocation(QStandardPaths.AppLocalDataLocation)+"/log"
    logDir = QDir(logDirPath)
    if not logDir.exists():
        logDir.mkpath(logDirPath)
    g_file_path = logDir.filePath(logFileName)
    qInstallMessageHandler(myMessageHandler)
    qDebug(f"===================================================")
    qDebug(f"[AppName] {g_app}")
    qDebug(f"[AppVersion] {AppInfo()._version}")
    qDebug(f"[ProcessId] {os.getpid()}")
    qDebug(f"[DeviceInfo]")
    qDebug(f"  [DeviceId] {QSysInfo.machineUniqueId()}")
    qDebug(f"  [Manufacturer] {QSysInfo.productVersion()}")
    qDebug(f"  [CPU_ABI] {QSysInfo.currentCpuArchitecture()}")
    qDebug(f"[LOG_LEVEL] {g_logLevel}")
    qDebug(f"[LOG_PATH] {g_file_path}")
    qDebug(f"===================================================");
    