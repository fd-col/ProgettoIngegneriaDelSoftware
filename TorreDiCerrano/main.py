import sys
from PyQt5.QtWidgets import QApplication
from Home.view.VistaHome import Home

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home()
    window.show()
    app.exec_()
