from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QMessageBox, \
    QGridLayout, QListWidget, QListWidgetItem

from Login.VistaLogin import VistaLogin
from Registrazione.VistaRegistrazione import VistaRegistrazione


class TabWidget(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QVBoxLayout(self)

        # Horizontal layout for buttons and labels
        self.h_button_layout = QHBoxLayout()

        self.bottone_login = self.create_button("        Login        ", "rgb(255,255,255)", "rgb(0, 0, 0)",
                                                "login", self.go_vista_login)
        self.bottone_registrati = self.create_button("     Registrati     ", "rgb(0,0,0)", "rgb(255, 170, 0)",
                                                "registrati", self.go_vista_registrazione)

        self.bottone_info = self.create_button("", "", "", "Info", self.visualizza_info)
        self.bottone_info.setStyleSheet("border-radius: 10px;")
        self.bottone_info.setIcon(QIcon("images\\icon_info.png"))
        self.bottone_info.setIconSize(QSize(150, 70))

        # add buttons to the horizontal layout
        self.h_button_layout.addStretch(1)
        self.h_button_layout.addWidget(self.bottone_info)
        self.h_button_layout.addWidget(self.bottone_login)
        self.h_button_layout.addWidget(self.bottone_registrati)


        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab1, QIcon("images\\icona_home.jpg"), "Home")
        self.tabs.setIconSize(QSize(30, 30))
        self.tabs.addTab(self.tab2, QIcon("images\\icons8-pila-di-foto.gif"), "Immagini")
        self.tabs.setIconSize(QSize(30, 30))
        self.tabs.addTab(self.tab3, QIcon("images\\icons8-pila-di-foto.gif"), "Servizi")
        self.tabs.setIconSize(QSize(30, 30))
        self.tabs.addTab(self.tab4, QIcon("images\\icons8-pila-di-foto.gif"), "Prezzi")
        self.tabs.setFont((QFont("Candara", 15)))
        self.tabs.setStyleSheet("background-color: #FFFFF0;")  # colore sfondo tabs : avorio

        # Create first tab
        self.tab1.layout = QHBoxLayout(self)

        self.v_layout = QVBoxLayout()
        self.h_title_layout = QHBoxLayout()

        # widgets
        self.label_resort = QLabel("                Resort Torre di Cerrano")
        self.label_resort.setStyleSheet("color: rgb(51, 102, 255);\n""font: 100 18pt \"Papyrus\";\n"
                                        "background-color: rgba(255, 168, 29, 0);")
        self.label_logo = QLabel()
        self.label_logo.setPixmap(QPixmap("images\\icon_logo_rt.png"))

        # add widgets to horizontal title layout
        self.h_title_layout.addWidget(self.label_resort)
        self.h_title_layout.addWidget(self.label_logo)

        self.label_descrizione = QLabel("Se cerchi un Resort in Abruzzo sul mare il Resort Torre di Cerrano   "
                                        "ti Aspetta con il suo impeccabile Staff, le stanze curate ed accoglienti "
                                        "e la spiaggia dedicata con tutti i migliori servizi a disposizione dei Nostri Clienti"
                                        "nella località balneare di Pineto.\n"
                                        "Con noi puoi trascorrere tranquillamente la tua vacanza e rilassarti grazie ai servizi "
                                        "offerti. ")
        self.label_descrizione.setWordWrap(True)
        self.label_descrizione.setMargin(15)
        self.label_descrizione.setMinimumWidth(700)
        self.label_descrizione.setStyleSheet("font: 14pt \"Papyrus\";")
        self.label_descrizione.setAlignment(Qt.AlignCenter)

        # add horizontal_title_layout and label_descrizione to v_layout (vertical layout)
        self.v_layout.addLayout(self.h_title_layout)
        self.v_layout.addWidget(self.label_descrizione)

        self.label_image = self.create_label_image('images/torre_di_cerrano[325].jpg')
        self.label_image.setScaledContents(True)
        self.label_image.setMaximumHeight(650)

        # add everything to tab1
        self.tab1.layout.addLayout(self.v_layout)
        self.tab1.layout.addWidget(self.label_image)

        self.tab1.setLayout(self.tab1.layout)


        # Create second tab
        self.tab2.layout = QGridLayout(self)
        # images to insert into tab2
        self.label_travel = self.create_label_image("images\\travel-1677347_1920.jpg")
        self.label_travel.setMaximumSize(550, 250)
        self.label_sea = self.create_label_image("images\\sea-3704014_1920.jpg")
        self.label_sea.setMaximumSize(550, 250)
        self.label_pineta = self.create_label_image("images\\pineta.jpg")
        self.label_pineta.setMaximumSize(550, 250)
        self.label_piscina = self.create_label_image("images\\piscina.jpg")
        self.label_piscina.setMaximumSize(550, 250)
        self.label_pineta2 = self.create_label_image("images\\pineta2.jpg")
        self.label_pineta2.setMaximumSize(550, 250)
        self.label_ombrelloni = self.create_label_image("images\\ombrelloni.jpg")
        self.label_ombrelloni.setMaximumSize(550, 250)

        self.tab2.layout.addWidget(self.label_travel, 0, 0)
        self.tab2.layout.addWidget(self.label_piscina, 0, 1)
        self.tab2.layout.addWidget(self.label_ombrelloni, 0, 2)
        self.tab2.layout.addWidget(self.label_sea, 1, 0)
        self.tab2.layout.addWidget(self.label_pineta, 1, 1)
        self.tab2.layout.addWidget(self.label_pineta2, 1, 2)

        self.tab2.setLayout(self.tab2.layout)


        # Create third tab
        self.tab3.layout = QVBoxLayout(self)

        self.listWidget = QListWidget()
        self.listWidget.setGeometry(QRect(40, 30, 270, 145))
        self.listWidget.setMinimumSize(QSize(261, 0))
        self.listWidget.setStyleSheet("font: 12pt \"Papyrus\";\n""color: rgb(0, 0, 0);\n"
                                      "selection-color: rgb(170, 255, 0);")
        self.listWidget.setObjectName("listWidget")
        item = QListWidgetItem(QIcon("images\\icon_info.png"), "Hotel", )
        item.setCheckState(Qt.Checked)

        font = QFont("Arial", 16)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.listWidget.addItem(item)

        self.tab3.layout.addWidget(self.listWidget)
        self.tab3.setLayout(self.tab3.layout)


        self.layout.addLayout(self.h_button_layout)
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
        info = QMessageBox().information(self, "Informazioni", "",
                                         QMessageBox.Ok, QMessageBox.Ok)
        if info == QMessageBox.Ok:
            pass
