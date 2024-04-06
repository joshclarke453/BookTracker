from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLineEdit, QPushButton, QTableWidgetItem
from VinylTable import VinylTable
from PyQt6.QtCore import QCoreApplication

class AddDialog(QDialog):
    def __init__(self, table: VinylTable):
        super().__init__()
        self.table = table
        self.setModal(True)
        self.qhBoxLayout = QHBoxLayout()

        self.titleTextbox = QLineEdit()
        self.titleTextbox.setPlaceholderText("Title")

        self.artistTextbox = QLineEdit()
        self.artistTextbox.setPlaceholderText("Artist")

        self.genreTextbox = QLineEdit()
        self.genreTextbox.setPlaceholderText("Genre")

        self.ownedTextbox = QLineEdit()
        self.ownedTextbox.setPlaceholderText("Owned")

        self.addButton = QPushButton()
        self.addButton.setText("Add")

        self.qhBoxLayout.addWidget(self.titleTextbox)
        self.qhBoxLayout.addWidget(self.artistTextbox)
        self.qhBoxLayout.addWidget(self.genreTextbox)
        self.qhBoxLayout.addWidget(self.ownedTextbox)
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
            QTableWidgetItem(self.genreTextbox.text())
        )
        self.table.setItem(
            self.table.rowCount() - 1, 
            3, 
            QTableWidgetItem(self.ownedTextbox.text())
        )
        self.table.rowAdded()
        self.addButton.clicked.disconnect()
        self.close()