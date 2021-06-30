from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from Home.view.TabWidget import TabWidget


class Home(QMainWindow):

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setObjectName("HOME")
        self.setWindowTitle("RESORT TORRE DI CERRANO")
        self.setWindowState(Qt.WindowMaximized)
        self.move(50, 0)
        self.setStyleSheet("background-color: #F0DC83;")

        self.table_widget = TabWidget()
        self.setCentralWidget(self.table_widget)
