import json
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QSizePolicy, QHeaderView
from PyQt6.QtCore import Qt, QCoreApplication

class VinylTable(QTableWidget):
    def __init__(self):
        f = open('./vinyls.json')
        data = json.load(f)
        keys = data[0].keys()
        super().__init__(len(data), len(keys))

        self.setSortingEnabled(False)
        self.sortByColumn(1, Qt.SortOrder.AscendingOrder)
        
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.setHorizontalHeaderLabels(keys)

        tableSizePolicy = QSizePolicy()
        tableSizePolicy.setVerticalPolicy(QSizePolicy.Policy.Expanding)
        tableSizePolicy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
        self.setSizePolicy(tableSizePolicy)
        for row, record in enumerate(data):
            for column, key in enumerate(keys):
                item = QTableWidgetItem(record.get(key))
                self.setItem(row, column, item)
        f.close()

        self.setSortingEnabled(True)

        self.connectSignals()

    def connectSignals(self):
        self.itemChanged.connect(self.cellChanged)

    def keyPressEvent(self, e: QKeyEvent | None) -> None:
        if (e.key() == Qt.Key.Key_Delete and e.modifiers() == Qt.KeyboardModifier.ControlModifier):
            self.deleteRow(self.currentItem().row())
        return super().keyPressEvent(e)

    def cellChanged(self, item):
        objList = []
        for row in range(self.rowCount()):
            obj = {
                "Title": self.item(row, 0).text(),
                "Artist": self.item(row, 1).text(),
                "Genre": self.item(row, 2).text(),
                "Owned": self.item(row, 3).text()
            }
            objList.append(obj)
        with open('./vinyls.json', 'w', encoding='utf-8') as f:
            json.dump(objList, f, ensure_ascii=False, indent=4)

    def deleteRow(self, rowNum):
        self.setSortingEnabled(False)
        self.itemChanged.disconnect()
        self.removeRow(rowNum)
        objList = []
        for row in range(self.rowCount()):
            obj = {
                "Title": self.item(row, 0).text(),
                "Artist": self.item(row, 1).text(),
                "Genre": self.item(row, 2).text(),
                "Owned": self.item(row, 3).text()
            }
            objList.append(obj)
        with open('./vinyls.json', 'w', encoding='utf-8') as f:
            json.dump(objList, f, ensure_ascii=False, indent=4)
        self.itemChanged.connect(self.cellChanged)
        self.setSortingEnabled(True)
    
    def rowAdded(self):
        objList = []
        for row in range(self.rowCount()):
            obj = {
                "Title": self.item(row, 0).text(),
                "Artist": self.item(row, 1).text(),
                "Genre": self.item(row, 2).text(),
                "Owned": self.item(row, 3).text()
            }
            objList.append(obj)
        with open('./vinyls.json', 'w', encoding='utf-8') as f:
            json.dump(objList, f, ensure_ascii=False, indent=4)
        self.itemChanged.connect(self.cellChanged)
        self.setSortingEnabled(True)

    def filter(self, filterValue):
        matchedItems = self.findItems(filterValue, Qt.MatchFlag.MatchContains)
        for row in range(self.rowCount()):
            self.setRowHidden(row, True)
        if len(matchedItems) > 0:
            for item in matchedItems:
                if item != None:
                    self.setRowHidden(item.row(), False)
        else:
            for row in range(self.rowCount()):
                self.setRowHidden(row, True)