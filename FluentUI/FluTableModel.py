from PySide6.QtCore import Signal, Property, QAbstractTableModel, Slot, QModelIndex, QObject


# noinspection PyPep8Naming,PyTypeChecker
class FluTableModel(QAbstractTableModel):
    columnSourceChanged = Signal()
    rowsChanged = Signal()

    def __init__(self):
        QAbstractTableModel.__init__(self)
        self._columnSource: list[dict] = []
        self._rows: list[dict] = []

    @Slot()
    def clear(self):
        self.beginResetModel()
        self._rows = []
        self.endResetModel()

    @Slot(int, result=dict)
    def getRow(self, rowIndex: int) -> dict:
        return self._rows[rowIndex]

    @Slot(int, dict)
    def setRow(self, rowIndex: int, row: dict):
        self._rows[rowIndex] = row
        self.dataChanged.emit(self.index(rowIndex, 0), self.index(rowIndex, self.columnCount() - 1))

    @Slot(int, dict)
    def insertRow(self, rowIndex: int, row: dict):
        self.beginInsertRows(QModelIndex(), rowIndex, rowIndex)
        self._rows.insert(rowIndex, row)
        self.endInsertRows()

    @Slot(int)
    @Slot(int, int)
    def removeRow(self, rowIndex: int, rows: int = None):
        if rows is None:
            rows = 1
        self.beginRemoveRows(QModelIndex(), rowIndex, rowIndex + rows - 1)
        self._rows = self._rows[:rowIndex] + self._rows[rowIndex + rows:]
        self.endRemoveRows()

    @Slot("QVariant")
    def appendRow(self, row: dict):
        self.insertRow(self.rowCount(), row)

    def rowCount(self, parent=...):
        return len(self._rows)

    def columnCount(self, parent=...):
        return len(self._columnSource)

    def data(self, index, role=...):
        if not index.isValid():
            return None
        if role == 0x101:
            return self._rows[index.row()]
        elif role == 0x102:
            return self._columnSource[index.column()]
        return None

    def roleNames(self):
        return {
            0x101: b"rowModel",
            0x102: b"columnModel"
        }

    @Property(list, notify=rowsChanged)
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value
        self.rowsChanged.emit()

    @Property(list, notify=columnSourceChanged)
    def columnSource(self):
        return self._columnSource

    @columnSource.setter
    def columnSource(self, value):
        self._columnSource = value
        self.columnSourceChanged.emit()
