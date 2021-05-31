from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import *

from ListaDipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from ListaPrenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni


class VistaAmministratore(QWidget):

    def __init__(self, nome, parent=None):
        super(VistaAmministratore, self).__init__(parent)

        self.v_layout = QVBoxLayout()

        self.label_nome = QLabel(nome)
        self.font_nome = QFont("Arial", 20)
        self.label_nome.setFont(self.font_nome)
        self.v_layout.addWidget(self.label_nome)

        self.label_admin = QLabel("Account Amministratore")
        self.font_admin = QFont("Arial", 16)
        self.label_admin.setFont(self.font_admin)
        self.v_layout.addWidget(self.label_admin)

        self.h_layout = QHBoxLayout()

        self.bottone_lista_dipendenti = QPushButton(" Lista Dipendenti")
        self.bottone_lista_dipendenti.setStyleSheet("background-color:#FFD800;")
        self.bottone_lista_dipendenti.setIcon(QIcon("images\icon_dipendenti.png"))
        self.bottone_lista_dipendenti.clicked.connect(self.go_lista_dipendenti)
        self.h_layout.addWidget(self.bottone_lista_dipendenti)

        self.bottone_lista_prenotazioni = QPushButton(" Lista Prenotazioni")
        self.bottone_lista_prenotazioni.setStyleSheet("background-color:#FFD800;")
        self.bottone_lista_prenotazioni.setIcon(QIcon("images\icon_prenotazione.png"))
        self.bottone_lista_prenotazioni.clicked.connect(self.go_lista_prenotazioni)
        self.h_layout.addWidget(self.bottone_lista_prenotazioni)

        self.bottone_resoconti = QPushButton("Resoconti")
        self.bottone_resoconti.setStyleSheet("background-color:#FFD800;")
        self.bottone_resoconti.setIcon(QIcon("images\icon_resoconti.png"))
        self.bottone_resoconti.setIconSize(QSize(50,50))
        self.h_layout.addWidget(self.bottone_resoconti)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)
        self.setWindowTitle(nome)
        self.resize(350, 400)

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()