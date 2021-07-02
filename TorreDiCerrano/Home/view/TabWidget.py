from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QGridLayout, \
    QListWidget, QListWidgetItem, QDialog, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QAbstractItemView

from Login.VistaLogin import VistaLogin
from Registrazione.VistaRegistrazione import VistaRegistrazione


class TabWidget(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QVBoxLayout()

        # Horizontal layout for buttons and labels
        self.h_button_layout = QHBoxLayout()

        self.bottone_info = self.create_button("", "", "", "Info", self.visualizza_info)
        self.bottone_info.setStyleSheet("color: 'black';" "border-radius: 10;")
        self.bottone_info.setIcon(QIcon("images/icon_info.png"))
        self.bottone_info.setIconSize(QSize(150, 70))

        self.bottone_login = self.create_button("        Login        ", "rgb(255,255,255)", "rgb(0, 0, 0)",
                                                "login", self.go_vista_login)
        self.bottone_registrati = self.create_button("     Registrati     ", "rgb(0,0,0)", "rgb(255, 170, 0)",
                                                "registrati", self.go_vista_registrazione)

        # add buttons to the horizontal layout on the top
        self.h_button_layout.addStretch(1)
        self.h_button_layout.addWidget(self.bottone_info)
        self.h_button_layout.addWidget(self.bottone_login)
        self.h_button_layout.addWidget(self.bottone_registrati)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab1.setStyleSheet("background-color: #FFFFF0;")
        self.tab2 = QWidget()
        self.tab2.setStyleSheet("background-color: #FFFFF0;")
        self.tab3 = QWidget()
        self.tab3.setStyleSheet("background-color: #FFFFF0;")
        self.tab4 = QWidget()
        self.tab4.setStyleSheet("background-color: #FFFFF0;")
        self.tab5 = QWidget()
        self.tab5.setStyleSheet("background-color: #FFFFF0;")

        # Add tabs
        self.tabs.addTab(self.tab1, QIcon("images/icona_home.jpg"), "Home")
        self.tabs.addTab(self.tab2, QIcon("images/icons8-pila-di-foto.gif"), "Immagini")
        self.tabs.addTab(self.tab3, QIcon("images/icons8-lista-64.png"), "Servizi")
        self.tabs.addTab(self.tab4, QIcon("images/icons8-euro-80.png"), "Prezzi")
        self.tabs.addTab(self.tab5, QIcon("images/icons8-contatti-64.png"), "Contatti")
        self.tabs.setIconSize(QSize(40, 40))

        self.tabs.setFont((QFont("Arial", 15)))
        self.tabs.setStyleSheet("QTabBar::tab { height: 50px; width: 200px; }")

        # Create first tab
        self.tab1.layout = QHBoxLayout(self)

        self.v_layout = QVBoxLayout()
        self.h_title_layout = QHBoxLayout()

        # widgets
        self.label_resort = QLabel("Resort Torre di Cerrano")
        self.label_resort.setStyleSheet("color: rgb(51, 102, 255);\n""font: 100 30pt \"Papyrus\";\n"
                                        "background-color: rgba(255, 168, 29, 0);")
        self.label_logo = QLabel()
        self.label_logo.setPixmap(QPixmap("images/icon_logo_rt.png"))

        # add widgets to horizontal title layout
        self.h_title_layout.setAlignment(Qt.AlignCenter)
        self.h_title_layout.addWidget(self.label_logo)
        self.h_title_layout.addWidget(self.label_resort)

        self.label_descrizione = QLabel("Se cerchi un Resort in Abruzzo sul mare il Resort Torre di Cerrano   "
                                        "ti Aspetta con il suo impeccabile Staff, le stanze curate ed accoglienti "
                                        "e la spiaggia dedicata con tutti i migliori servizi a disposizione dei Nostri Clienti"
                                        " nella località balneare di Pineto.\n"
                                        "Con noi puoi trascorrere tranquillamente la tua vacanza e rilassarti grazie ai servizi "
                                        "offerti. ")
        self.label_descrizione.setWordWrap(True)
        self.label_descrizione.setMargin(15)
        self.label_descrizione.setMinimumWidth(400)
        self.label_descrizione.setStyleSheet("font: 16pt \"Papyrus\";")
        self.label_descrizione.setAlignment(Qt.AlignCenter)

        # add horizontal_title_layout and label_descrizione to v_layout (vertical layout)
        self.v_layout.addLayout(self.h_title_layout)
        self.v_layout.addWidget(self.label_descrizione)

        self.label_image = self.create_label_image('images/torre_cerrano.jpg')
        self.label_image.setMargin(10)
        self.label_image.setFixedSize(1000, 650)

        # add v_layout and label_image to tab1
        self.tab1.layout.addLayout(self.v_layout)
        self.tab1.layout.addWidget(self.label_image)

        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.tab2.layout = QGridLayout(self)

        # images to insert into tab2
        self.label_travel = self.create_label_image("images/travel-1677347_1920.jpg")
        self.label_travel.setMaximumSize(400, 250)
        self.label_sea = self.create_label_image("images/sea-3704014_1920.jpg")
        self.label_sea.setMaximumSize(400, 250)
        self.label_pineta = self.create_label_image("images/pineta.jpg")
        self.label_pineta.setMaximumSize(400, 250)
        self.label_piscina = self.create_label_image("images/piscina.jpg")
        self.label_piscina.setMaximumSize(400, 250)
        self.label_pineta2 = self.create_label_image("images/pineta2.jpg")
        self.label_pineta2.setMaximumSize(400, 250)
        self.label_ombrelloni = self.create_label_image("images/ombrelloni.jpg")
        self.label_ombrelloni.setMaximumSize(400, 250)

        self.tab2.layout.addWidget(self.label_travel, 0, 0)
        self.tab2.layout.addWidget(self.label_piscina, 0, 1)
        self.tab2.layout.addWidget(self.label_ombrelloni, 0, 2)
        self.tab2.layout.addWidget(self.label_sea, 1, 0)
        self.tab2.layout.addWidget(self.label_pineta, 1, 1)
        self.tab2.layout.addWidget(self.label_pineta2, 1, 2)

        self.tab2.setLayout(self.tab2.layout)

        # Create third tab
        self.tab3.layout = QVBoxLayout(self)

        lista1 = QListWidget()
        lista1.setAlternatingRowColors(True)
        lista1.setSpacing(20)
        lista1.setStyleSheet("font: 12pt \"Papyrus\";\n""color: rgb(0, 0, 0);\n""selection-color: rgb(170, 255, 0);")
        lista1.setObjectName("listWidget")

        self.aggiungi_item(lista1, "Hotel")
        self.aggiungi_item(lista1, "Bungalow")
        self.aggiungi_item(lista1, "Ristorante")
        self.aggiungi_item(lista1, "Stabilimento balneare")
        self.aggiungi_item(lista1, "Campi sportivi")
        self.aggiungi_item(lista1, "Area ricretiva")
        self.aggiungi_item(lista1, "Piscine")
        self.aggiungi_item(lista1, "Centro benessere")
        self.aggiungi_item(lista1, "Noleggi mezzi elettrici")

        self.tab3.layout.addWidget(lista1)
        self.tab3.setLayout(self.tab3.layout)

        # Create fourth tab
        self.tab4.layout = QVBoxLayout(self)

        self.h_table_layout = QHBoxLayout()
        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()

        self.v2_layout.addSpacing(30)

        # servizi compresi
        self.label_servizi_compresi = QLabel("  Nelle offerte proposte dal Resort Torre di Cerrano "
                                             "alcuni servizi sono compresi :")
        self.label_servizi_compresi.setFont(QFont("Times new roman", 20))
        self.label_servizi_compresi.setWordWrap(True)

        # elenco dei servizi compresi
        self.check1 = self.create_check_box("Ingresso in piscina con lettini")
        self.check2 = self.create_check_box("Ombrellone, sdraio, lettino in spiaggia")
        self.check3 = self.create_check_box("Animazione grandi e piccoli")

        # add section "servizi compresi" nella prenotazione
        self.v2_layout.addWidget(self.label_servizi_compresi)
        self.v2_layout.addSpacing(30)

        self.v2_layout.addWidget(self.check1)
        self.v2_layout.addWidget(self.check2)
        self.v2_layout.addWidget(self.check3)
        self.v2_layout.addSpacing(118)

        self.create_table(3, 2, "Pacchetto del soggiorno", "  Sola colazione;  Mezza pensione;  Pensione completa; ",
                          "   30 €;   60 €;   90 €; ", True)
        self.create_table(4, 2, "Tipologia di alloggio", "  Suite;  Camera familiare;  Camera doppia;  Bungalow ",
                          "  235 €;  125 €;    80 €;  150 €", True)
        self.create_table(3, 2, "Servizi aggiuntivi", "  Noleggio mezzi elettrici;  Escursione turistica;  Centro benessere; ",
                          "  30 €;  50 €;  50 €; ", False)

        self.h_table_layout.addLayout(self.v1_layout)
        self.h_table_layout.addLayout(self.v2_layout)

        self.tab4.layout.addLayout(self.h_table_layout)
        self.tab4.setLayout(self.tab4.layout)

        # Create fifth tab
        self.tab5.layout = QVBoxLayout(self)

        self.v3_layout = QVBoxLayout()
        self.v3_layout.addSpacing(30)

        self.label_contact = QLabel()
        self.label_contact.setPixmap(QPixmap("images/contatti.jpg"))
        self.label_contact.setAlignment(Qt.AlignCenter)

        self.v3_layout.addWidget(self.label_contact)
        self.v3_layout.addSpacing(40)

        # horizontal layout che contiene le schede dei contatti
        self.h_contact_layout = QHBoxLayout()

        list1 = QListWidget()
        list1.setAlternatingRowColors(True)
        list1.setStyleSheet("background-color: #C0C0C0;")
        list2 = QListWidget()
        list2.setAlternatingRowColors(True)
        list2.setStyleSheet("background-color: #C0C0C0;")
        list3 = QListWidget()
        list3.setAlternatingRowColors(True)
        list3.setStyleSheet("background-color: #C0C0C0;")
        self.aggiungi_item(list1, "Federico C.")
        self.aggiungi_item(list1, "email - s1093242@studenti.univpm.it")
        self.aggiungi_item(list2, "Francesco C.")
        self.aggiungi_item(list2, "email - s1094929@studenti.univpm.it")
        self.aggiungi_item(list3, "Andrea C.")
        self.aggiungi_item(list3, "email - s1092302@studenti.univpm.it")

        self.h_contact_layout.addWidget(list1)
        self.h_contact_layout.addWidget(list2)
        self.h_contact_layout.addWidget(list3)

        self.v3_layout.addLayout(self.h_contact_layout)

        self.tab5.layout.addLayout(self.v3_layout)
        self.tab5.setLayout(self.tab5.layout)

        # Final layout
        self.layout.addLayout(self.h_button_layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def create_button(self, testo, text_color, background_color, nome, comando):
        bottone = QPushButton(testo)
        bottone.setStyleSheet("background-color: " + background_color + ";\n""font: 100 19pt \"Arial\";\n"
                              "color: " + text_color + ";""border-radius: 15px;")
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
        dialog = QDialog()
        dialog.setWindowTitle("Dove puoi trovarci :")

        v_layout = QVBoxLayout()
        label = QLabel()
        label.setPixmap(QPixmap("images/posizione_torre_cerrano.png"))

        v_layout.addWidget(label)

        dialog.setLayout(v_layout)
        dialog.exec()

    def aggiungi_item(self, lista, nome):
        item = QListWidgetItem(nome)
        item.setTextAlignment(Qt.AlignCenter)
        font = QFont("Arial", 16)
        font.setWeight(50)
        item.setFont(font)
        lista.addItem(item)

    def create_table(self, row, column, header, nomi, prezzi, side):
        table_widget = QTableWidget(row, column)

        # table settings
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table_widget.setFont(QFont("Arial", 18))
        table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # header
        table_widget.horizontalHeader().setFont(QFont("Times new roman", 22))
        table_widget.setHorizontalHeaderItem(0, QTableWidgetItem(header))
        table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Prezzo"))
        # add items to table
        table_widget.setItem(0, 0, QTableWidgetItem(nomi.split(";")[0]))
        table_widget.setItem(0, 1, QTableWidgetItem(prezzi.split(";")[0]))
        table_widget.setItem(1, 0, QTableWidgetItem(nomi.split(";")[1]))
        table_widget.setItem(1, 1, QTableWidgetItem(prezzi.split(";")[1]))
        table_widget.setItem(2, 0, QTableWidgetItem(nomi.split(";")[2]))
        table_widget.setItem(2, 1, QTableWidgetItem(prezzi.split(";")[2]))
        table_widget.setItem(3, 0, QTableWidgetItem(nomi.split(";")[3]))
        table_widget.setItem(3, 1, QTableWidgetItem(prezzi.split(";")[3]))
        if side is True:    # (put the table in the vertical layout on the left side)
            self.v1_layout.addWidget(table_widget)
        else:
            self.v2_layout.addWidget(table_widget)

    def create_check_box(self, text):
        check_box = QCheckBox(text)
        check_box.setFont(QFont("Arial", 16))
        check_box.setChecked(True)
        return check_box
