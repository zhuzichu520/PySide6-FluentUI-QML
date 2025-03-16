from PySide6.QtCore import Signal, Property, Slot, QObject, QAbstractTableModel, QModelIndex


# noinspection PyProtectedMember,PyCallingNonCallable,PyPep8Naming,PyPropertyAccess

class FluTreeNode(QObject):
    depthChanged = Signal()
    isExpandedChanged = Signal()
    checkedChanged = Signal()
    childrenChanged = Signal()
    parentChanged = Signal()
    dataChanged = Signal()

    @Property(dict, notify=dataChanged)
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.dataChanged.emit()

    @Slot(result=bool)
    def hasChildren(self):
        return len(self._children) != 0

    @Slot(int, result=bool)
    def hasNextNodeByIndex(self, index: int):
        p: FluTreeNode = self
        for i in range(self._depth - index - 1):
            p = p._parent
        if p._parent._children.index(p) == len(p._parent._children) - 1:
            return False
        return True

    @Slot(result=bool)
    def hideLineFooter(self):
        if self._parent is not None:
            if self not in self._parent._children:
                return False
            childIndex = self._parent._children.index(self)
            if childIndex == len(self._parent._children) - 1:
                return True
            if self._parent._children[childIndex + 1].hasChildren():
                return True
            return False

    @Slot(result=bool)
    def isShown(self):
        p = self._parent
        while p is not None:
            if not p.isExpanded:
                return False
            p = p._parent
        return True

    @Property(int, notify=depthChanged)
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value
        self.depthChanged.emit()

    @Property(bool, notify=isExpandedChanged)
    def isExpanded(self):
        return self._isExpanded

    @isExpanded.setter
    def isExpanded(self, value):
        self._isExpanded = value
        self.isExpandedChanged.emit()

    @Property(bool, notify=checkedChanged)
    def checked(self):
        if not self.hasChildren():
            return self._checked
        for item in self._children:
            if not item.checked:
                return False
        return True

    @checked.setter
    def checked(self, value):
        self._checked = value
        self.checkedChanged.emit()

    @Property(QObject, notify=parentChanged)
    def parent_(self):
        return self._parent

    @parent_.setter
    def parent_(self, value):
        self._parent = value
        self.parentChanged.emit()

    @Property(list, notify=childrenChanged)
    def children_(self):
        return self._children

    @children_.setter
    def children_(self, value):
        self._children = value
        self.childrenChanged.emit()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._parent = None
        self._data = None
        self._title = ""
        self._depth = 0
        self._data = None
        self._isExpanded = True
        self._checked = False
        self._children: list[FluTreeNode] = []


# noinspection PyCallingNonCallable,PyProtectedMember,PyPropertyAccess,PyPep8Naming
class FluTreeModel(QAbstractTableModel):
    dataSourceSizeChanged = Signal()
    selectionModelChanged = Signal()
    columnSourceChanged = Signal()

    @Property(list, notify=selectionModelChanged)
    def selectionModel(self):
        return self._selectionModel

    @selectionModel.setter
    def selectionModel(self, value):
        self._selectionModel = value
        self.selectionModelChanged.emit()

    @Property(int, notify=dataSourceSizeChanged)
    def dataSourceSize(self):
        return self._dataSourceSize

    @dataSourceSize.setter
    def dataSourceSize(self, value):
        self._dataSourceSize = value
        self.dataSourceSizeChanged.emit()

    @Property(list, notify=columnSourceChanged)
    def columnSource(self):
        return self._columnSource

    @columnSource.setter
    def columnSource(self, value):
        self._columnSource = value
        self.columnSourceChanged.emit()

    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataSourceSize: int = 0
        self._columnSource = []
        self._selectionModel: list[FluTreeNode] = []
        self._rows: list[FluTreeNode] = []
        self._dataSource: list[FluTreeNode] = []
        self._root = None
        self.destroyed.connect(lambda: self.release())

    def release(self):
        self._selectionModel.clear()
        self._rows.clear()
        self._dataSource.clear()
        del self._root
        del self._selectionModel
        del self._rows
        del self._dataSource

    def rowCount(self, parent=...):
        return len(self._rows)

    def columnCount(self, parent=...):
        return len(self._columnSource)

    def data(self, index, role=...):
        if role == 0x0101:
            return self._rows[index.row()]
        elif role == 0x0102:
            return self._columnSource[index.column()]
        return {}

    def roleNames(self):
        return {0x0101: b"rowModel", 0x0102: b"columnModel", }

    def index(self, row, column, parent=...):
        if not self.hasIndex(row, column):
            return QModelIndex()
        return self.createIndex(row, column)

    def parent(self, parent=...):
        return QModelIndex()

    @Slot(int, int)
    def removeRows(self, row: int, count: int):
        if (row < 0) or (row + count) > len(self._rows) or (count == 0):
            return
        self.beginRemoveRows(QModelIndex(), row, row + count - 1)
        firstPart = self._rows[:row]
        secondPart = self._rows[row + count:]
        self._rows.clear()
        self._rows.extend(firstPart)
        self._rows.extend(secondPart)
        self.endRemoveRows()

    @Slot(int, list)
    def insertRows(self, row: int, data: list[FluTreeNode]):
        if row < 0 or row > len(self._rows) or len(data) == 0:
            return
        self.beginInsertRows(QModelIndex(), row, row + len(data) - 1)
        firstPart = self._rows[:row]
        secondPart = self._rows[row:]
        self._rows.clear()
        self._rows.extend(firstPart)
        self._rows.extend(data)
        self._rows.extend(secondPart)
        self.endInsertRows()

    @Slot(int, bool)
    def checkRow(self, row: int, checked: bool):
        itemData: FluTreeNode = self._rows[row]
        if itemData.hasChildren():
            stack = itemData.children_.copy()
            stack.reverse()
            while len(stack) > 0:
                item = stack.pop()
                if not item.hasChildren():
                    item._checked = checked
                children = item.children_.copy()
                if len(children) != 0:
                    reversed(item.children_)
                    for c in children:
                        stack.append(c)
        else:
            if itemData._checked == checked:
                return
            itemData.checked = checked

        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount() - 1, 0))

        data = []
        for item in self._dataSource:
            if not item.hasChildren():
                if item.checked():
                    data.append(item)
        self.selectionModel = data

    @Slot(list)
    def setDataSource(self, data: list[dict]):
        self._dataSource.clear()
        self._root = FluTreeNode(self)
        data.reverse()
        while len(data) > 0:
            item = data.pop()
            node = FluTreeNode(self)
            if "__depth" in item:
                node.depth = item["__depth"]
            else:
                node.depth = 0
            if "__parent" in item:
                node.parent_ = item["__parent"]
            else:
                node.parent_ = None
            node._data = item
            node.isExpanded = True
            if node.parent_ is not None:
                node.parent_.children_.append(node)
            else:
                node.parent_ = self._root
                self._root.children_.append(node)
            self._dataSource.append(node)
            if "children" in item:
                children = item["children"]
                if len(children) != 0:
                    children.reverse()
                    for child in children:
                        if "__depth" in item:
                            child["__depth"] = item["__depth"] + 1
                        else:
                            child["__depth"] = 1
                        child["__parent"] = node
                        data.append(child)
        self.beginResetModel()
        self._rows = self._dataSource
        self.endResetModel()
        self.dataSourceSize = len(self._dataSource)

    @Slot(int)
    def collapse(self, row: int):
        if not self._rows[row].isExpanded:
            return
        self._rows[row].isExpanded = False
        self.dataChanged.emit(self.index(row, 0), self.index(row, 0))
        modelData = self._rows[row]
        removeCount = 0
        for i in range(row + 1, len(self._rows)):
            obj: FluTreeNode = self._rows[i]
            if obj.depth <= modelData.depth:
                break
            removeCount += 1
        self.removeRows(row + 1, removeCount)

    @Slot(int)
    def expand(self, row: int):
        if self._rows[row].isExpanded:
            return
        self._rows[row].isExpanded = True
        self.dataChanged.emit(self.index(row, 0), self.index(row, 0))
        modelData = self._rows[row]
        insertData = []
        stack = modelData.children_.copy()
        stack.reverse()
        while len(stack) > 0:
            item = stack.pop()
            if item.isShown():
                insertData.append(item)
            children = item.children_.copy()
            if len(children) != 0:
                children.reverse()
                for c in children:
                    stack.append(c)
        self.insertRows(row + 1, insertData)

    @Slot(int)
    def getRow(self, row: int):
        return self._rows[row]

    @Slot(list)
    def setData(self, data: list[FluTreeNode]):
        self.beginResetModel()
        self._rows = data
        self.endResetModel()

    @Slot(int)
    def getNode(self, row: int):
        return self._rows[row]

    @Slot(int)
    def refreshNode(self, row: int):
        self.dataChanged.emit(self.index(row, 0), self.index(row, 0))

    @Slot(int)
    def hitHasChildrenExpanded(self, row: int):
        itemData = self._rows[row]
        if itemData.hasChildren() and itemData.isExpanded:
            return True
        return False

    @Slot()
    def allExpand(self):
        self.beginResetModel()
        data = []
        stack = self._root.children_.copy()
        stack.reverse()
        while len(stack) > 0:
            item = stack.pop()
            if item.hasChildren():
                item.isExpanded = True
            data.append(item)
            children = item.children_.copy()
            if len(children) != 0:
                children.reverse()
                for c in children:
                    stack.append(c)
        self._rows = data
        self.endResetModel()

    @Slot()
    def allCollapse(self):
        self.beginResetModel()
        stack = self._root.children_.copy()
        stack.reverse()
        while len(stack) > 0:
            item = stack.pop()
            if item.hasChildren():
                item.isExpanded = False
            children = item.children_.copy()
            if len(children) != 0:
                children.reverse()
                for c in children:
                    stack.append(c)
        self._rows = self._root.children_
        self.endResetModel()
