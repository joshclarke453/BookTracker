from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.setWindowTitle("Vinyl Tracker")
window.show()  

# Start the event loop.
app.exec()