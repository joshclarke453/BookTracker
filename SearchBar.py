from PyQt6.QtWidgets import QLineEdit

class SearchBar(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Filter...")

        self.connectSignals()

    def connectSignals(self):
        pass