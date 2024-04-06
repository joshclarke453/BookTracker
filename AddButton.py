from PyQt6.QtWidgets import QPushButton
from AddDialog import AddDialog
from BookTable import BookTable

class AddButton(QPushButton):
    def __init__(self, table: BookTable):
        super().__init__()
        self.table = table
        self.setText("Add")

        self.connectSignals()

    def connectSignals(self):
        self.clicked.connect(self.addButtonClicked)

    def addButtonClicked(self):
        self.dialog = AddDialog(self.table)
        self.dialog.exec()