from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QMessageBox

from Login.VistaLogin import VistaLogin
from Registrazione.VistaRegistrazione import VistaRegistrazione


class TabWidget(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QVBoxLayout(self)
        self.layout.addSpacing(25)

        # Horizontal layout for buttons and labels
        self.h_layout = QHBoxLayout()

        self.bottone_login = self.create_button("        Login        ", "rgb(255,255,255)", "rgb(0, 0, 0)",
                                                "login", self.go_vista_login)
        self.bottone_registrati = self.create_button("     Registrati     ", "rgb(0,0,0)", "rgb(255, 170, 0)",
                                                "registrati", self.go_vista_registrazione)
        self.label_benvenuti = QLabel("     Benvenuti          ")
        self.label_benvenuti.setStyleSheet("color: rgb(51, 102, 255);\n""font: 100 50pt \"Papyrus\";\n"
                                           "background-color: rgba(255, 168, 29, 0);")
        self.bottone_info = self.create_button("", "", "", "Info", self.visualizza_info)
        self.bottone_info.setStyleSheet("border-radius: 10px;")
        self.bottone_info.setIcon(QIcon("images\\icon_info.png"))
        self.bottone_info.setIconSize(QSize(150, 150))

        self.h_layout.addWidget(self.bottone_info)
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label_benvenuti)
        self.h_layout.addWidget(self.bottone_login)
        self.h_layout.addWidget(self.bottone_registrati)
        self.h_layout.addSpacing(25)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1, QIcon("images\\icona_home.jpg"), "Home")
        self.tabs.setIconSize(QSize(30, 30))
        self.tabs.addTab(self.tab2, QIcon("images\\icons8-pila-di-foto.gif"), "Immagini")
        self.tabs.setFont((QFont("Candara", 15)))
        self.tabs.setStyleSheet("background-color: #FFFFF0;")  # colore sfondo tabs : avorio

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)

        self.label_resort = QLabel("Resort Torre di Cerrano")
        self.label_resort.setStyleSheet("font: 20pt \"Papyrus\";")
        self.label_resort.setAlignment(Qt.AlignCenter)
        self.label_resort.setFixedHeight(70)

        self.label_image = self.create_label_image('images/torre_di_cerrano[325].jpg')

        self.tab1.layout.addWidget(self.label_resort)
        self.tab1.layout.addWidget(self.label_image)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QVBoxLayout(self)
        # images to insert into tab2
        self.label_travel = self.create_label_image("images/travel-1677347_1920.jpg")
        self.label_travel.setMinimumSize(400, 200)
        self.label_sea = self.create_label_image("images/sea-3704014_1920.jpg")
        self.label_sea.setMinimumSize(400, 200)

        self.tab2.layout.addWidget(self.label_travel)
        self.tab2.layout.addWidget(self.label_sea)
        self.tab2.setLayout(self.tab2.layout)

        self.layout.addLayout(self.h_layout)
        self.layout.addWidget(self.tabs)

    def create_button(self, testo, text_color, background_color, nome, comando):
        bottone = QPushButton(testo)
        bottone.setStyleSheet("background-color: " + background_color + ";\n""font: 75 16pt \"Arial\";\n"
                              "color: " + text_color + ";")
        bottone.setDefault(True)
        bottone.setObjectName(nome)
        bottone.clicked.connect(comando)
        return bottone

    def create_label_image(self, immagine):
        label = QLabel()
        label.setText("")
        label.setPixmap(QPixmap(immagine))
        label.setScaledContents(True)
        label.setObjectName("label")
        return label

    def go_vista_registrazione(self):
        self.vista_registrazione = VistaRegistrazione()
        self.vista_registrazione.show()

    def go_vista_login(self):
        self.vista_login = VistaLogin()
        self.vista_login.show()

    def visualizza_info(self):
        info = QMessageBox().information(self, "Informazioni", "Questo fantastico Resort è situato nella "
                                        "località balneare di Pineto(TE) e propone numerose attività dedicate a"
                                        "valorizzare il territorio abruzzese tra il mare e la montagna.",
                                         QMessageBox.Ok, QMessageBox.Ok)
        if info == QMessageBox.Ok:
            pass
