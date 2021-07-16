from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

from Dipendente.model.Dipendente import Dipendente


class VistaInserisciDipendente(QWidget):

    def __init__(self, controller_lista_dipendenti, aggiorna_lista, parent=None):
        super(VistaInserisciDipendente, self).__init__(parent)
        self.controller = controller_lista_dipendenti
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Arial", 17)

        self.label_alto = QLabel("Compila il form con i dati del dipendente: ")
        self.label_alto.setFont(QFont("Arial", 17, 15, True))
        self.label_alto.setStyleSheet("color: rgb(0, 0, 255)")
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(25)

        self.campo_nome = self.create_format_campo("Nome")
        self.campo_cognome = self.create_format_campo("Cognome")
        self.campo_ruolo = self.create_format_campo("Ruolo")
        self.campo_id = self.create_format_campo("ID")
        self.campo_stipendio = self.create_format_campo("Stipendio (€)")

        self.v_layout.addSpacing(25)

        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(QFont("Arial", 15, 1, True))
        self.bottone_conferma.setStyleSheet("background-color: rgb(0,255,0);")
        self.bottone_conferma.clicked.connect(self.conferma_inserimento)
        self.v_layout.addWidget(self.bottone_conferma)

        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.setWindowTitle("Inserimento Dipendente")

    #Crea e aggiunge al layout verticale della finestra una label con il testo passato e al di sotto un campo per
    #l'inserimento dei dati
    def create_format_campo(self, testo):
        label = QLabel(testo)
        label.setFont(self.font_label)
        self.v_layout.addWidget(label)

        campo = QLineEdit()
        campo.setFont(self.font_label)
        self.v_layout.addWidget(campo)
        self.v_layout.addSpacing(10)
        return campo

    #Conferma l'inserimento dei dati, controlla la loro correttezza e in caso affermativo aggiunge il dipendente alla
    #lista dei dipendenti
    def conferma_inserimento(self):
        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        ruolo = self.campo_ruolo.text()

        #Controlla che l'id inserito sia un numero
        try:
            id = int(self.campo_id.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il codice ID", QMessageBox.Ok, QMessageBox.Ok)
            return False

        #Controlla che l'id inserito sia di 5 cifre e non inizi per 0
        if id > 99999 or id < 10000:
            QMessageBox.critical(self, "Errore", "L'ID deve essere composto da 5 cifre e non può cominciare con 0", QMessageBox.Ok, QMessageBox.Ok)
            return False

        #Controlla che l'id inserito non sia già utilizzato da un altro dipendente
        if not self.controlla_id_libero(id):
            QMessageBox.critical(self, "Errore", "L'ID che hai immesso è già stato utilizzato", QMessageBox.Ok, QMessageBox.Ok)
            return False

        #Controlla che lo stipendio inseito sia un numero
        try:
            stipendio = float(self.campo_stipendio.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri con il punto per lo stipendio", QMessageBox.Ok,QMessageBox.Ok)
            return False

        #Controlla che lo stipendio inserito non sia negativo
        if stipendio <= 0:
            QMessageBox.critical(self, "Errore", "Lo stipendio non può essere negativo", QMessageBox.Ok,QMessageBox.Ok)
            return False

        #Controlla che tutti i campi siano stati riempiti
        if nome == "" or cognome == "" or ruolo == "" or id == 0 or stipendio == 0.0:
            QMessageBox.critical(self, "Errore", "Completa tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return False

        self.controller.aggiungi_dipendente(Dipendente(nome, cognome, ruolo, id, stipendio))
        self.controller.save_data()
        QMessageBox.about(self, "Completato", "L'inserimento del dipendente è stato completato")
        self.aggiorna_lista()
        self.close()
        return True

    #Controlla che l'id passato come argomento non sia ancora stato utilizzato
    def controlla_id_libero(self, id):
        for dipendente in self.controller.get_lista_dipendenti():
            if dipendente.id == id:
                return False
        return True

