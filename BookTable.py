import json
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QGridLayout, QTableWidget, QSizePolicy, QHeaderView, QCheckBox
from PyQt6.QtCore import Qt

class BookTable(QTableWidget):
    def __init__(self):
        f = open('./books.json', encoding='utf-8')
        data = json.load(f)
        keys = ["Title", "Author", "Read Date", "Read", "Owned"]
        super().__init__(len(data), len(keys))

        self.setSortingEnabled(False)
        self.sortByColumn(1, Qt.SortOrder.AscendingOrder)
        
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        self.setHorizontalHeaderLabels(keys)

        tableSizePolicy = QSizePolicy()
        tableSizePolicy.setVerticalPolicy(QSizePolicy.Policy.Expanding)
        tableSizePolicy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
        self.setSizePolicy(tableSizePolicy)
        for row, record in enumerate(data):
            item = QTableWidgetItem(record.get("Title"))
            self.setItem(row, 0, item)

            item = QTableWidgetItem(record.get("Author"))
            self.setItem(row, 1, item)

            item = QTableWidgetItem(record.get("Read Date"))
            self.setItem(row, 2, item)
            
            readCellWidget = QWidget()
            readCellLayout = QGridLayout()
            readCb = QCheckBox()
            readCb.setChecked(record.get("Read") in [True, 'True'])
            readCb.stateChanged.connect(self.writeToFile)
            readCellLayout.addWidget(readCb)
            readCellWidget.setLayout(readCellLayout)
            self.setCellWidget(row, 3, readCellWidget)

            ownedCellWidget = QWidget()
            ownedCellLayout = QGridLayout()
            ownedCb = QCheckBox()
            ownedCb.setChecked(record.get("Owned") in [True, 'True'])
            ownedCb.stateChanged.connect(self.writeToFile)
            ownedCellLayout.addWidget(ownedCb)
            ownedCellWidget.setLayout(ownedCellLayout)
            self.setCellWidget(row, 4, ownedCellWidget)

        f.close()

        self.resizeRowsToContents()
        self.setSortingEnabled(True)

        self.connectSignals()

    def connectSignals(self):
        self.itemChanged.connect(self.cellChanged)

    def keyPressEvent(self, e: QKeyEvent | None) -> None:
        if (e.key() == Qt.Key.Key_Delete and e.modifiers() == Qt.KeyboardModifier.ControlModifier):
            self.deleteRow(self.currentItem().row())
        return super().keyPressEvent(e)

    def cellChanged(self, item):
        self.writeToFile()

    def deleteRow(self, rowNum):
        self.setSortingEnabled(False)
        self.itemChanged.disconnect()
        self.removeRow(rowNum)
        self.writeToFile()
        self.itemChanged.connect(self.cellChanged)
        self.setSortingEnabled(True)
    
    def rowAdded(self):
        self.writeToFile()
        self.itemChanged.connect(self.cellChanged)
        self.setSortingEnabled(True)

    def writeToFile(self):
        objList = []
        for row in range(self.rowCount()):
            if self.item(row, 2) != None:
                readDate = self.item(row, 2).text()
            obj = {
                "Title": self.item(row, 0).text(),
                "Author": self.item(row, 1).text(),
                "Read Date": readDate,
                "Read": self.cellWidget(row, 3).children()[0].itemAtPosition(0,0).widget().isChecked(),
                "Owned": self.cellWidget(row, 4).children()[0].itemAtPosition(0,0).widget().isChecked()
            }
            objList.append(obj)
        with open('./books.json', 'w', encoding='utf-8') as f:
            json.dump(objList, f, ensure_ascii=False, indent=4)

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