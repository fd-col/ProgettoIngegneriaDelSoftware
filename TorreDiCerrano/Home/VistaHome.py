from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QPushButton, QTabWidget, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QMainWindow

from Home.TabWidget import TabWidget
from Registrazione.VistaRegistrazione import VistaRegistrazione
from Login.VistaLogin import VistaLogin


class Home(QMainWindow):

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setObjectName("HOME")
        self.setWindowTitle("RESORT TORRE DI CERRANO")
        self.resize(1910, 1000)
        self.setStyleSheet("background-color: #F0DC83;")

        self.table_widget = TabWidget()
        self.setCentralWidget(self.table_widget)

        """
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 30, 270, 145))
        self.listWidget.setMinimumSize(QtCore.QSize(261, 0))
        self.listWidget.setStyleSheet("font: 12pt \"Papyrus\";\n""color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(178, 225, 255);\n""selection-color: rgb(170, 255, 0);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)

        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        HOME.setCentralWidget(self.centralwidget)

        self.retranslateUi(HOME)
        QtCore.QMetaObject.connectSlotsByName(HOME)
        """
    def retranslateUi(self, HOME):
        _translate = QtCore.QCoreApplication.translate
        HOME.setWindowTitle(_translate("HOME", "Home"))

        self.label_resort.setText(_translate("HOME", "Resort Torre di Cerrano"))
        self.label_benvenuto.setText(_translate("HOME", " Benvenuto  "))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        item = self.listWidget.item(0)
        item.setText(_translate("HOME", "hotel"))
        item = self.listWidget.item(1)
        item.setText(_translate("HOME", "bungalow"))
        item = self.listWidget.item(2)
        item.setText(_translate("HOME", "ristorante"))
        item = self.listWidget.item(3)
        item.setText(_translate("HOME", "stabilimento balneare"))
        item = self.listWidget.item(4)
        item.setText(_translate("HOME", "campi sportivi"))
        item = self.listWidget.item(5)
        item.setText(_translate("HOME", "area ricreativa"))
        item = self.listWidget.item(6)
        item.setText(_translate("HOME", "piscine"))
        item = self.listWidget.item(7)
        item.setText(_translate("HOME", "centro benessere"))
        item = self.listWidget.item(8)
        item.setText(_translate("HOME", "noleggio mezzi elettrici"))
        self.listWidget.setSortingEnabled(__sortingEnabled)






