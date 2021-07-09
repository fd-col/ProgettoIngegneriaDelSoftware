from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel, QLineEdit, QShortcut
from PyQt5.QtGui import QKeySequence, QFont
from qtwidgets import PasswordEdit
import os
import json

from Amministratore.views.VistaAmministratore import VistaAmministratore
from Cliente.controller.ControlloreCliente import ControlloreCliente
from Cliente.views.VistaCliente import VistaCliente
from ListaClienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)

        self.controllore = ControlloreListaClienti()

        self.font = QFont("Arial", 15, 15, True)

        self.v_layout = QVBoxLayout()

        # titolo
        self.label_alto = QLabel("Inserisci i dati per il login: ")
        self.label_alto.setFont(self.font)
        self.label_alto.setStyleSheet("color: rgb(0, 0, 255)")
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(20)

        # campo email
        self.label_email = QLabel("E-mail")
        self.label_email.setFont(self.font)
        self.v_layout.addWidget(self.label_email)

        self.campo_email = QLineEdit()
        self.campo_email.setFont(self.font)
        self.v_layout.addSpacing(5)
        self.v_layout.addWidget(self.campo_email)

        self.v_layout.addSpacing(10)

        # campo password
        self.label_password = QLabel("Password")
        self.label_password.setFont(self.font)
        self.v_layout.addWidget(self.label_password)

        self.campo_password = PasswordEdit()
        self.campo_password.setFont(self.font)
        self.campo_password.setEchoMode(QLineEdit.Password)
        self.v_layout.addSpacing(5)
        self.v_layout.addWidget(self.campo_password)

        self.v_layout.addSpacing(20)

        # bottone login
        self.bottone_login = QPushButton("Login")
        self.bottone_login.setFont(self.font)
        self.bottone_login.setStyleSheet("background-color:#ccd9ff;")
        self.bottone_login.clicked.connect(self.login)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.login)
        self.v_layout.addWidget(self.bottone_login)

        self.setLayout(self.v_layout)
        self.resize(200, 200)
        self.setWindowTitle("Login")

    #Controlla le credenziali inserite dall'utente
    def login(self):
        email = self.campo_email.text()
        password = self.campo_password.text()

        #Controlla se le credenziali inserite sono quelle di un amministratore
        if self.controlla_admin(email, password):
            return

        #Controlla che le credenziali inserite corrispondano a quelle di un cliente
        if self.controllore.get_cliente_by_email(email) is not None:
            da_mostrare = self.controllore.get_cliente_by_email(email)

            #In caso affermativo visualizza il profilo del cliente
            if da_mostrare.password == password:
                self.vista_cliente = VistaCliente(ControlloreCliente(da_mostrare))
                self.vista_cliente.show()
                self.close()
            #Altrimenti mostra un messaggio di errore
            else:
                QMessageBox.critical(self, "Errore", "La password è errata", QMessageBox.Ok,
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Errore", "L'email inserita non è associata ad alcun cliente", QMessageBox.Ok,
                                 QMessageBox.Ok)

    #Controlla che l'email e la password inseriti coincidano con le credenziali di una admin, in caso affermativo
    #ritorna True e visualizza il profilo dell'amministratore, altrimenti ritorna False
    def controlla_admin(self, email, password):

        if os.path.isfile("Amministratore/data/lista_amministratori.json"):
            with open("Amministratore/data/lista_amministratori.json") as file:
                lista_admin = json.load(file)
                for admin in lista_admin:
                    if email == admin["email"] and password == admin["password"]:
                                self.vista_admin = VistaAmministratore(admin["nome"])
                                self.vista_admin.show()
                                self.close()
                                return True
        return False
