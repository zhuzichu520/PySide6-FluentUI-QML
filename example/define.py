# This Python file uses the following encoding: utf-8

from PySide6.QtCore import QObject, Signal, Property


def Singleton(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return wrapper
