from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from datetime import datetime
from qtwidgets import PasswordEdit

from Cliente.model.Cliente import Cliente
from ListaClienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaRegistrazione(QWidget):

    def __init__(self, parent=None):
        super(VistaRegistrazione, self).__init__(parent)
        self.controller = ControlloreListaClienti()

        self.v_layout = QVBoxLayout()
        # fonts
        self.font_label1 = QFont("Arial", 17)               # font semplice per i campi del cliente
        self.font_label2 = QFont("Arial", 15, 15, True)     # font grassetto per le credenziali di accesso
        self.font_label2.setBold(True)
        self.font_label3 = QFont("Arial", 17, 15, True)     # font per il titolo del form

        # titolo
        self.label_alto = QLabel("Compila il form di registrazione: ")
        self.label_alto.setFont(self.font_label3)
        self.label_alto.setStyleSheet("color: rgb(0, 0, 255)")
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(20)

        # campi registrazione
        self.campo_nome = self.create_format_campo("Nome")
        self.campo_cognome = self.create_format_campo("Cognome")
        self.campo_nascita = self.create_format_campo("Data di nascita (gg/mm/aaaa)")
        self.campo_indirizzo = self.create_format_campo("Indirizzo")
        self.campo_telefono = self.create_format_campo("Telefono")

        self.campo_email = self.create_format_campo("E-mail")
        self.campo_password = self.create_format_password("Password")
        self.campo_conferma_password = self.create_format_password("Conferma password")

        self.v_layout.addSpacing(30)

        # bottone conferma
        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(self.font_label1)
        self.bottone_conferma.setStyleSheet("background-color:#ccd9ff;")
        self.bottone_conferma.clicked.connect(self.registra_cliente)
        self.v_layout.addWidget(self.bottone_conferma)

        self.setLayout(self.v_layout)
        self.rect = self.frameGeometry()
        self.setGeometry(self.rect)
        self.setWindowTitle("Registrazione")

    #Crea una label con la stringa passata come argomento al di sotto un campo editabile a li aggiunge al layout della finestra
    def create_format_campo(self, testo):
        label = QLabel(testo)
        label.setFont(self.font_label1)
        self.v_layout.addWidget(label)

        campo = QLineEdit()
        campo.setFont(self.font_label1)
        self.v_layout.addWidget(campo)
        return campo

    #Crea una label e al di sotto un campo con la possibilità di oscurare l'inserimento e li aggiunge al layout
    def create_format_password(self, testo):
        label = QLabel(testo)
        label.setFont(self.font_label2)
        self.v_layout.addWidget(label)

        campo = PasswordEdit()
        campo.setFont(self.font_label1)
        campo.setEchoMode(QLineEdit.Password)
        self.v_layout.addWidget(campo)
        return campo

    #Controlla i dati inseriti e registra il cliente
    def registra_cliente(self):

        #Controlla che il cliente abbai compilato tutti i campi
        if self.campo_nome.text() == "" or self.campo_cognome.text() == "" or self.campo_nascita.text() == "" or self.campo_indirizzo.text() == "" or self.campo_telefono.text() == "" or self.campo_email.text() == "" or self.campo_password.text() == "" or self.campo_conferma_password.text() == "":
            QMessageBox.critical(self, "Errore", "Compila tutti i campi richiesti", QMessageBox.Ok, QMessageBox.Ok)

        #Controlla che l'email inserita non sia già stata utilizzata da una lto cliente
        elif self.controller.get_cliente_by_email(self.campo_email.text()) is not None:
            QMessageBox.critical(self, "Errore", "L'email che hai inserito è già stata utilizzata", QMessageBox.Ok, QMessageBox.Ok)

        #Controlla che le password inserite corrispondano
        elif self.campo_password.text() != self.campo_conferma_password.text():
            QMessageBox.critical(self, "Errore", "La password inserita non corrisponde, si prega di riprovare",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            nome = self.campo_nome.text()
            cognome = self.campo_cognome.text()
            dt_nascita = self.campo_nascita.text()
            indirizzo = self.campo_indirizzo.text()
            telefono = self.campo_telefono.text()
            email = self.campo_email.text()
            password = self.campo_password.text()

            #Controlla che la data di nascita sia inserita nel formato richiesto
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

