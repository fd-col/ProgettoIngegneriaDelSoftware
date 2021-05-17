from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import os
import pickle

class VistaRegistrazione(QWidget):

    def __init__(self, parent=None):

        super(VistaRegistrazione, self).__init__(parent)

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Arial", 17)

        self.label_alto = QLabel("Compila il form di registrazione")
        self.label_alto.setFont(self.font_label)
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(20)

        self.label_nome = QLabel("Nome")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.v_layout.addWidget(self.campo_nome)


        self.label_cognome = QLabel("Cognome")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.v_layout.addWidget(self.campo_cognome)


        self.label_nascita = QLabel("Data di nascita (gg/mm/aaaa)")
        self.label_nascita.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nascita)

        self.campo_nascita = QLineEdit()
        self.v_layout.addWidget(self.campo_nascita)


        self.label_indirizzo = QLabel("Indirizzo")
        self.label_indirizzo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_indirizzo)

        self.campo_indirizzo = QLineEdit()
        self.v_layout.addWidget(self.campo_indirizzo)


        self.label_telefono = QLabel("Telefono")
        self.label_telefono.setFont(self.font_label)
        self.v_layout.addWidget(self.label_telefono)

        self.campo_telefono = QLineEdit()
        self.v_layout.addWidget(self.campo_telefono)


        self.label_email = QLabel("E-mail")
        self.label_email.setFont(self.font_label)
        self.v_layout.addWidget(self.label_email)

        self.campo_email = QLineEdit()
        self.v_layout.addWidget(self.campo_email)

        self.label_password = QLabel("Password")
        self.label_password.setFont(self.font_label)
        self.v_layout.addWidget(self.label_password)

        self.campo_password = QLineEdit()
        self.v_layout.addWidget(self.campo_password)

        self.v_layout.addSpacing(30)

        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(self.font_label)
        self.bottone_conferma.setStyleSheet("background-color:#ccd9ff;")
        self.v_layout.addWidget(self.bottone_conferma)
        #self.bottone_conferma.clicked.connect(self.aggiungi_cliente(...))


        self.setLayout(self.v_layout)
        self.resize(200, 600)
        self.setWindowTitle("Registrazione")


