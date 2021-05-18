from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class VistaCliente(QWidget):

    def __init__(self, controllore_cliente, parent=None):
        super(VistaCliente, self).__init__(parent)

        self.v_layout = QVBoxLayout()

        self.label_nome = QLabel(controllore_cliente.get_nome_cliente() + " " + controllore_cliente.get_cognome_cliente())
        self.font_nome = QFont("Arial", 20)
        self.label_nome.setFont(self.font_nome)
        self.v_layout.addWidget(self.label_nome)

        self.label_nascita = QLabel(controllore_cliente.get_data_nascita_cliente())
        self.font_nascita = QFont("Arial", 16)
        self.label_nascita.setFont(self.font_nascita)
        self.v_layout.addWidget(self.label_nascita)

        self.label_indirizzo = QLabel(controllore_cliente.get_indirizzo_cliente())
        self.font_indirizzo = QFont("Arial", 16)
        self.label_indirizzo.setFont(self.font_indirizzo)
        self.v_layout.addWidget(self.label_indirizzo)

        self.label_telefono = QLabel(controllore_cliente.get_telefono_cliente())
        self.font_telefono = QFont("Arial", 16)
        self.label_telefono.setFont(self.font_telefono)
        self.v_layout.addWidget(self.label_telefono)

        self.label_email = QLabel(controllore_cliente.get_email_cliente())
        self.font_email = QFont("Arial", 16)
        self.label_email.setFont(self.font_email)
        self.v_layout.addWidget(self.label_email)

        self.h_layout = QHBoxLayout()

        self.bottone_prenotazioni = QPushButton("Prenotazioni")
        self.h_layout.addWidget(self.bottone_prenotazioni)

        self.bottone_scannerizza = QPushButton("Scannerizza documento")
        self.h_layout.addWidget(self.bottone_scannerizza)

        self.bottone_elimina_profilo = QPushButton("Elimina profilo")
        self.h_layout.addWidget(self.bottone_elimina_profilo)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)
        self.setWindowTitle(controllore_cliente.get_nome_cliente() + " " +controllore_cliente.get_cognome_cliente())
        self.resize(400, 600)