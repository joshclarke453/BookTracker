from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout
from SearchBar import SearchBar
from AddButton import AddButton
from VinylTable import VinylTable

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.table = VinylTable()
        self.qvbLayout = QVBoxLayout()
        self.topBarLayout = QHBoxLayout()
        self.searchBar = SearchBar()
        self.addButton = AddButton(self.table)

        self.topBarLayout.addWidget(self.searchBar)
        self.topBarLayout.addWidget(self.addButton)

        self.qvbLayout.addLayout(self.topBarLayout)
        self.qvbLayout.addWidget(self.table)
        
        self.widget = QWidget()
        self.widget.setLayout(self.qvbLayout)
        self.setCentralWidget(self.widget)
        self.resize(800, 800)

        self.connectSignals()

    def connectSignals(self):
        self.searchBar.textChanged.connect(self.table.filter)