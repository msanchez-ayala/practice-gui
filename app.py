import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My window")

        label = QLabel("This is text in my window")

        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label) 

app = QApplication(sys.argv)

window = MainWindow()
window.show() 

app.exec_()