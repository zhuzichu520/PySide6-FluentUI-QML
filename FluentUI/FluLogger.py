import logging
import os
import sys
import threading

from PySide6.QtCore import QDir, qInstallMessageHandler, QtMsgType, QStandardPaths, QDateTime, QSysInfo

_logging: logging.Logger
_fileHandler: logging.FileHandler
_formatFileHandler: logging.FileHandler
_stdoutHandler: logging.StreamHandler
_formatStdoutHandler: logging.StreamHandler


class _CustomFormatter(logging.Formatter):
    def format(self, record):
        record.threadId = threading.get_ident()
        return super().format(record)


# noinspection PyPep8Naming
def _getLevelByMsgType(msgType):
    if msgType == QtMsgType.QtFatalMsg:
        return logging.FATAL
    if msgType == QtMsgType.QtCriticalMsg:
        return logging.CRITICAL
    if msgType == QtMsgType.QtWarningMsg:
        return logging.WARNING
    if msgType == QtMsgType.QtInfoMsg:
        return logging.INFO
    if msgType == QtMsgType.QtDebugMsg:
        return logging.DEBUG
    return logging.DEBUG


# noinspection PyPep8Naming
def _openFormat():
    _logging.removeHandler(_fileHandler)
    _logging.removeHandler(_stdoutHandler)
    _logging.addHandler(_formatFileHandler)
    _logging.addHandler(_formatStdoutHandler)


# noinspection PyPep8Naming
def _closeFormat():
    _logging.removeHandler(_formatFileHandler)
    _logging.removeHandler(_formatStdoutHandler)
    _logging.addHandler(_fileHandler)
    _logging.addHandler(_stdoutHandler)


# noinspection PyPep8Naming
def _messageHandler(msgType, context, message):
    global _logging
    global _fileHandler
    global _formatFileHandler
    global _stdoutHandler
    global _formatStdoutHandler
    _closeFormat()
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
    level = _getLevelByMsgType(msgType)
    finalMessage = f"{QDateTime.currentDateTime().toString('yyyy/MM/dd hh:mm:ss.zzz')}[{logging.getLevelName(level)}]{fileAndLineLogStr}[{threading.get_ident()}]:{message}"
    _logging.log(level, finalMessage)
    _openFormat()


# noinspection PyPep8Naming
def LogSetup(name, level=logging.DEBUG):
    global _logging
    global _fileHandler
    global _formatFileHandler
    global _stdoutHandler
    global _formatStdoutHandler

    _logging = logging.getLogger(name)
    _logging.setLevel(level)
    logFileName = f"{name}_{QDateTime.currentDateTime().toString('yyyyMMdd')}.log"
    logDirPath = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppLocalDataLocation) + "/log"
    logDir = QDir(logDirPath)
    if not logDir.exists():
        logDir.mkpath(logDirPath)
    logFilePath = logDir.filePath(logFileName)
    _fileHandler = logging.FileHandler(logFilePath)
    _stdoutHandler = logging.StreamHandler(sys.stdout)
    _formatFileHandler = logging.FileHandler(logFilePath)
    _formatStdoutHandler = logging.StreamHandler(sys.stdout)
    fmt = _CustomFormatter("%(asctime)s[%(levelname)s][%(filename)s:%(lineno)s][%(threadId)d] %(message)s")
    _formatFileHandler.setFormatter(fmt)
    _formatStdoutHandler.setFormatter(fmt)
    _logging.addHandler(_formatStdoutHandler)
    _logging.addHandler(_formatFileHandler)
    qInstallMessageHandler(_messageHandler)
    _logging.info(f"===================================================")
    _logging.info(f"[AppName] {name}")
    _logging.info(f"[AppPath] {sys.argv[0]}")
    _logging.info(f"[ProcessId] {os.getpid()}")
    _logging.info(f"[DeviceInfo]")
    _logging.info(f"  [DeviceId] {QSysInfo.machineUniqueId().toStdString()}")
    _logging.info(f"  [Manufacturer] {QSysInfo.productVersion()}")
    _logging.info(f"  [CPU_ABI] {QSysInfo.currentCpuArchitecture()}")
    _logging.info(f"[LOG_LEVEL] {logging.getLevelName(level)}")
    _logging.info(f"[LOG_PATH] {logFilePath}")
    _logging.info(f"===================================================")


# noinspection PyPep8Naming
def Logger():
    return _logging
