from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLineEdit, QPushButton, QTableWidgetItem, QCheckBox, QWidget, QGridLayout, QLabel
from BookTable import BookTable
from PyQt6.QtCore import QCoreApplication

class AddDialog(QDialog):
    def __init__(self, table: BookTable):
        super().__init__()
        self.table = table
        self.setModal(True)
        self.qhBoxLayout = QHBoxLayout()

        self.titleTextbox = QLineEdit()
        self.titleTextbox.setPlaceholderText("Title")

        self.artistTextbox = QLineEdit()
        self.artistTextbox.setPlaceholderText("Author")

        self.readDateTextbox = QLineEdit()
        self.readDateTextbox.setPlaceholderText("Read Date")

        self.readCBLabel = QLabel("Read?")
        self.readCB = QCheckBox()
        self.readCB.setChecked(False)

        self.ownedCBLabel = QLabel("Owned?")
        self.ownedCB = QCheckBox()
        self.ownedCB.setChecked(False)

        self.addButton = QPushButton()
        self.addButton.setText("Add")

        self.qhBoxLayout.addWidget(self.titleTextbox)
        self.qhBoxLayout.addWidget(self.artistTextbox)
        self.qhBoxLayout.addWidget(self.readDateTextbox)
        self.qhBoxLayout.addWidget(self.readCBLabel)
        self.qhBoxLayout.addWidget(self.readCB)
        self.qhBoxLayout.addWidget(self.ownedCBLabel)
        self.qhBoxLayout.addWidget(self.ownedCB)
        self.qhBoxLayout.addWidget(self.addButton)

        self.setLayout(self.qhBoxLayout)

        self.connectSignals()

    def connectSignals(self):
        self.addButton.clicked.connect(self.addButtonClicked)

    def addButtonClicked(self):
        self.table.setSortingEnabled(False)
        self.table.itemChanged.disconnect()
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(
            self.table.rowCount() - 1, 
            0, 
            QTableWidgetItem(self.titleTextbox.text())
        )
        self.table.setItem(
            self.table.rowCount() - 1, 
            1, 
            QTableWidgetItem(self.artistTextbox.text())
        )
        self.table.setItem(
            self.table.rowCount() - 1, 
            2, 
            QTableWidgetItem(self.readDateTextbox.text())
        )
        readCellWidget = QWidget()
        readCellLayout = QGridLayout()
        readCb = QCheckBox()
        readCb.setChecked(self.readCB.isChecked())
        readCb.stateChanged.connect(self.table.writeToFile)
        readCellLayout.addWidget(readCb)
        readCellWidget.setLayout(readCellLayout)
        self.table.setCellWidget(
            self.table.rowCount() - 1, 
            3, 
            readCellWidget
        )
        
        ownedCellWidget = QWidget()
        ownedCellLayout = QGridLayout()
        ownedCb = QCheckBox()
        ownedCb.setChecked(self.ownedCB.isChecked())
        ownedCb.stateChanged.connect(self.table.writeToFile)
        ownedCellLayout.addWidget(ownedCb)
        ownedCellWidget.setLayout(ownedCellLayout)
        self.table.setCellWidget(
            self.table.rowCount() - 1, 
            4, 
            ownedCellWidget
        )
               
        self.table.rowAdded()
        self.table.resizeRowsToContents()
        self.addButton.clicked.disconnect()
        self.close()