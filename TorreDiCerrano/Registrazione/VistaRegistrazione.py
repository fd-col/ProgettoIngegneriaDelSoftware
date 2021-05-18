from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

import os
import pickle

from datetime import datetime

from Cliente.model.Cliente import Cliente
from ListaClienti.controller.ControlloreListaClienti import ControlloreListaClienti

class VistaRegistrazione(QWidget):

    def __init__(self, parent=None):
        super(VistaRegistrazione, self).__init__(parent)

        self.controller = ControlloreListaClienti()


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
        self.campo_password.setEchoMode(QLineEdit.Password)
        self.v_layout.addWidget(self.campo_password)

        self.v_layout.addSpacing(30)

        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(self.font_label)
        self.bottone_conferma.setStyleSheet("background-color:#ccd9ff;")
        self.bottone_conferma.clicked.connect(self.registra_cliente)
        self.v_layout.addWidget(self.bottone_conferma)
        #self.bottone_conferma.clicked.connect(self.aggiungi_cliente(...))


        self.setLayout(self.v_layout)
        self.resize(200, 600)
        self.setWindowTitle("Registrazione")


    def registra_cliente(self):
        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        dt_nascita = self.campo_nascita.text()
        indirizzo = self.campo_indirizzo.text()
        telefono = self.campo_telefono.text()
        email = self.campo_email.text()
        password = self.campo_password.text()

        if nome == "" or cognome == "" or dt_nascita == "" or indirizzo == "" or telefono == "" or email == "" or password == "":
            QMessageBox.critical(self, "Errore", "Compila tutti i campi richiesti", QMessageBox.Ok, QMessageBox.Ok)
        elif self.controller.get_cliente_by_email(email) is not None:
            QMessageBox.critical(self, "Errore", "L'email che hai inserito è già stata utilizzata", QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                data_nascita = datetime.strptime(dt_nascita, "%d/%m/%Y")
                da_aggiungere = Cliente(nome, cognome, data_nascita, indirizzo, telefono, email, password)
                QMessageBox.about(self, "Completata", "La registrazione è stata completata")
                self.controller.aggiungi_cliente(da_aggiungere)
                self.close()
            except:
                QMessageBox.critical(self, "Errore", "Inserisci la data di nascita nel formato richiesto", QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        self.controller.save_data()


