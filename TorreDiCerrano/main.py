import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Home.VistaHome import Ui_HOME

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    window = Ui_HOME()
    window.setupUi(mainwindow)
    mainwindow.show()
    app.exec_()
