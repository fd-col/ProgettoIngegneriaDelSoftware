from PyQt5.QtWidgets import QMainWindow

from Home.view.TabWidget import TabWidget


class Home(QMainWindow):

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setObjectName("HOME")
        self.setWindowTitle("RESORT TORRE DI CERRANO")
        self.resize(1650, 1000)
        self.setStyleSheet("background-color: #F0DC83;")

        self.table_widget = TabWidget()
        self.setCentralWidget(self.table_widget)
