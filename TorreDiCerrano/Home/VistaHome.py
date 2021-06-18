from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QPushButton, QTabWidget, QVBoxLayout, QWidget, QHBoxLayout, QLabel

from Registrazione.VistaRegistrazione import VistaRegistrazione
from Login.VistaLogin import VistaLogin


class Home(QWidget):

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setObjectName("HOME")
        self.resize(1900, 1050)
        self.setStyleSheet("background-color: #F0DC83;")

        self.layout = QVBoxLayout(self)
        self.layout.addSpacing(25)

        # Horizontal layout for buttons
        self.h_layout = QHBoxLayout()
        self.h_layout.addStretch(1)
        self.create_button("        Login        ", "rgb(255,255,255)", "rgb(0, 0, 0)",
                           "login", self.go_vista_login)
        self.create_button("     Registrati     ", "rgb(0,0,0)", "rgb(255, 170, 0)",
                           "registrati", self.go_vista_registrazione)
        self.h_layout.addSpacing(25)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 100)

        # Add tabs
        self.tabs.addTab(self.tab1, QIcon("images\\icona_home.jpg"), "Home")
        self.tabs.setIconSize(QSize(30, 30))
        self.tabs.addTab(self.tab2, "Immagini")
        self.tabs.setFont((QFont("Candara", 15)))
        self.tabs.setStyleSheet("background-color: #FFFFF0;")  #colore sfondo tabs : avorio

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)

        self.label_resort = QLabel("Resort Torre di Cerrano")
        self.label_resort.setStyleSheet("font: 20pt \"Papyrus\";")
        self.label_resort.setAlignment(Qt.AlignCenter)
        self.label_resort.setFixedHeight(50)
        self.label_image = self.create_label_image('images/torre_di_cerrano[325].jpg')

        self.tab1.layout.addWidget(self.label_resort)
        self.tab1.layout.addWidget(self.label_image)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)

        self.label_travel = self.create_label_image("images/travel-1677347_1920.jpg")
        self.label_sea = self.create_label_image("images/sea-3704014_1920.jpg")

        self.tab2.layout.addWidget(self.label_travel)
        self.tab2.layout.addWidget(self.label_sea)
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addLayout(self.h_layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        """
        self.centralwidget = QtWidgets.QWidget(HOME)
        self.centralwidget.setObjectName("centralwidget")

        self.create_button("Login", QRect(900, 20, 171, 45), "rgb(255,255,255)", "rgb(0, 0, 0)",
                           "login", self.go_vista_login)
        self.create_button("Registrati", QRect(1080, 20, 171, 45), "rgb(0,0,0)", "rgb(255, 170, 0)",
                           "registrati", self.go_vista_registrazione)

        self.create_label_image(QRect(40, 250, 991, 550), 'images/torre_di_cerrano[325].jpg')
        self.create_label_image(QRect(1050, 350, 181, 161), "images/travel-1677347_1920.jpg")
        self.create_label_image(QRect(1050, 580, 191, 121), "images/sea-3704014_1920.jpg")

        self.label_resort = QtWidgets.QLabel(self.centralwidget)
        self.label_resort.setGeometry(QtCore.QRect(70, 270, 450, 111))
        self.label_resort.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 40pt \"Papyrus\";")
        self.label_resort.setObjectName("label_5")
        self.label_benvenuto = QtWidgets.QLabel(self.centralwidget)
        self.label_benvenuto.setGeometry(QtCore.QRect(360, 90, 500, 91))
        self.label_benvenuto.setStyleSheet("color: rgb(51, 102, 255);\n""font: 100 90pt \"Papyrus\";\n"
                                           "background-color: rgba(255, 168, 29, 0);")
        self.label_benvenuto.setObjectName("label_4")

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

    def create_button(self, testo, text_color, background_color, nome, comando):
        bottone = QPushButton(testo)
        #bottone.setText(testo)
        #bottone.setGeometry(dimensioni)
        bottone.setStyleSheet("background-color: " + background_color + ";\n""font: 75 16pt \"Arial\";\n"
                              "color: " + text_color + ";")
        bottone.setDefault(True)
        bottone.setObjectName(nome)
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    def create_label_image(self, immagine):
        label = QtWidgets.QLabel()
        label.setText("")
        label.setPixmap(QtGui.QPixmap(immagine))
        label.setScaledContents(True)
        label.setObjectName("label")
        return label

    def go_vista_registrazione(self):
        self.vista_registrazione = VistaRegistrazione()
        self.vista_registrazione.show()

    def go_vista_login(self):
        self.vista_login = VistaLogin()
        self.vista_login.show()
