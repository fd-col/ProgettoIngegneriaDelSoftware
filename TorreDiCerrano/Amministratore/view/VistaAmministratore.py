from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

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

        self.bottonone_lista_dipendenti = QPushButton("Lista Dipendenti")
        self.h_layout.addWidget(self.bottonone_lista_dipendenti)

        self.bottone_lista_prenotazioni = QPushButton("Lista Prenotazioni")
        self.h_layout.addWidget(self.bottone_lista_prenotazioni)

        self.bottone_resoconti = QPushButton("Resoconti")
        self.h_layout.addWidget(self.bottone_resoconti)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)
        self.setWindowTitle(nome)
        self.resize(200, 200)