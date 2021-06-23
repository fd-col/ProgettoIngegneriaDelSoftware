from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

from Dipendente.model.Dipendente import Dipendente


class VistaInserisciDipendente(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):
        super(VistaInserisciDipendente, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Arial", 17)

        self.label_alto = QLabel("Compila il form di inserimento del dipendente")
        self.label_alto.setFont(QFont("Arial", 17, 15, True))
        self.label_alto.setStyleSheet("color: rgb(0, 0, 255)")
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(25)

        self.campo_nome = self.create_format_campo("Nome")
        self.campo_cognome = self.create_format_campo("Cognome")
        self.campo_ruolo = self.create_format_campo("Ruolo")
        self.campo_id = self.create_format_campo("ID")
        self.campo_stipendio = self.create_format_campo("Stipendio")

        self.v_layout.addSpacing(25)

        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(QFont("Candara", 15, 1, True))
        self.bottone_conferma.setStyleSheet("background-color: rgb(0,255,0);")
        self.bottone_conferma.clicked.connect(self.conferma_inserimento)
        self.v_layout.addWidget(self.bottone_conferma)

        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.setWindowTitle("Inserimento Dipendente")

    def create_format_campo(self, testo):
        label = QLabel(testo)
        label.setFont(self.font_label)
        self.v_layout.addWidget(label)

        campo = QLineEdit()
        self.v_layout.addWidget(campo)
        self.v_layout.addSpacing(10)
        return campo

    def conferma_inserimento(self):
        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        ruolo = self.campo_ruolo.text()

        try:
            id = int(self.campo_id.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il codice ID", QMessageBox.Ok, QMessageBox.Ok)
            return

        if id > 99999 or id < 00000:
            QMessageBox.critical(self, "Errore", "L'ID deve essere composto da 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if not self.controlla_id_libero(id):
            QMessageBox.critical(self, "Errore", "L'ID che hai immesso è già stato utilizzato", QMessageBox.Ok, QMessageBox.Ok)
            return

        try:
            stipendio = float(self.campo_stipendio.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri con il punto per lo stipendio", QMessageBox.Ok,QMessageBox.Ok)
            return

        if stipendio <= 0:
            QMessageBox.critical(self, "Errore", "Lo stipendio non può essere negativo", QMessageBox.Ok,QMessageBox.Ok)
            return

        if nome == "" or cognome == "" or ruolo == "" or id == 0 or stipendio == 0.0:
            QMessageBox.critical(self, "Errore", "Completa tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.controller.aggiungi_dipendente(Dipendente(nome, cognome, ruolo, id, stipendio))
        self.controller.save_data()
        QMessageBox.about(self, "Completato", "L'inserimento del dipendente è stato completato")
        self.aggiorna_lista()
        self.close()

    def controlla_id_libero(self, id):
        for dipendente in self.controller.get_lista_dipendenti():
            if dipendente.id == id:
                return False
        return True

