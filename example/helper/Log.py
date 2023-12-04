# This Python file uses the following encoding: utf-8

from PySide6.QtCore import Qt, QMessageLogContext, qInstallMessageHandler, qSetMessagePattern,qFormatLogMessage, QFile, QTextStream,QtMsgType,QStandardPaths
import sys

QT_ENDL = "\n"

g_app = ""
g_logError = False

g_logFile = None
g_logStream = None

def myMessageHandler(type, context, message):
    global g_logError, g_logFile, g_logStream
    if message.strip() == "":
        return
    finalMessage = qFormatLogMessage(type, context, message).strip()
    if type in [QtMsgType.QtInfoMsg, QtMsgType.QtDebugMsg]:
        print(finalMessage)
    else:
        print(finalMessage, file=sys.stderr)
    if g_logError:
        return
    if g_logFile is None:
        logFileName = f"debug-{g_app}.log"
        logFilePath = QStandardPaths.writableLocation(
            QStandardPaths.AppLocalDataLocation)+"/"+logFileName
        g_logFile = QFile(logFilePath)
        print("Application log file path ->", logFilePath)
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
    global g_app
    assert app.strip() != ""
    if app.strip() == "":
        return
    g_app = app
    qSetMessagePattern(
        "[%{time yyyy/MM/dd hh:mm:ss.zzz}] <%{if-info}INFO%{endif}%{if-debug}DEBUG"
        "%{endif}%{if-warning}WARNING%{endif}%{if-critical}CRITICAL%{endif}%{if-fatal}"
        "FATAL%{endif}> %{if-category}%{category}: %{endif}%{message}")
    qInstallMessageHandler(myMessageHandler)