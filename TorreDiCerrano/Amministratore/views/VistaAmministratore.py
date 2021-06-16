from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap, QKeySequence
from PyQt5.QtWidgets import *

from ListaDipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from ListaPrenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni


class VistaAmministratore(QWidget):

    def __init__(self, nome, parent=None):
        super(VistaAmministratore, self).__init__(parent)

        self.v_layout = QVBoxLayout()

        self.label_icona = QLabel("Cliente")
        self.label_icona.setPixmap(QPixmap('images/profilo_amministratore.jpg'))
        self.label_icona.setScaledContents(False)
        self.v_layout.addWidget(self.label_icona)

        self.label_nome = QLabel(nome)
        self.font_nome = QFont("Arial", 20)
        self.label_nome.setFont(self.font_nome)
        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addSpacing(20)

        self.label_admin = QLabel("Account Amministratore")
        self.font_admin = QFont("Arial", 16)
        self.label_admin.setFont(self.font_admin)
        self.v_layout.addWidget(self.label_admin)
        self.v_layout.addSpacing(20)

        self.h_layout = QHBoxLayout()

        self.create_button(" Lista Prenotazioni", self.go_lista_prenotazioni, "background-color:#FFD800;", 'Alt+P',
                           "images\\icon_prenotazione.png", )
        self.create_button(" Lista Dipendenti", self.go_lista_dipendenti, "background-color:#FFD800;", 'Alt+D',
                           "images\\icon_dipendenti.png", )
        self.create_button("Resoconti", self.funzione_al_posto_di_resoconti, "background-color:#FFD800;", 'Alt+R',
                           "images\\icon_resoconti.png", QSize(50, 50))

        self.v_layout.addLayout(self.h_layout)

        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setLayout(self.v_layout)
        self.setWindowTitle(nome)
        self.resize(350, 400)
        self.move(750, 200)

    def funzione_al_posto_di_resoconti(self):
        pass

    def create_button(self, testo, comando, background_color, shortcut, icona, icon_size=QSize(30, 30)):
        bottone = QPushButton(testo)
        bottone.setStyleSheet(background_color)
        bottone.setIcon(QIcon(icona))
        bottone.setIconSize(icon_size)
        bottone.clicked.connect(comando)
        shortcut_open = QShortcut(QKeySequence(shortcut), self)
        shortcut_open.activated.connect(comando)
        self.h_layout.addWidget(bottone)

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()