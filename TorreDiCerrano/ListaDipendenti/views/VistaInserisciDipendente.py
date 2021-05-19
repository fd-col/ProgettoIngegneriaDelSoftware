from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Dipendente.model.Dipendente import Dipendente
from ListaDipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti


class VistaInserisciDipendente(QWidget):

    def __init__(self, controller, aggiorna_lista, parent=None):
        super(VistaInserisciDipendente, self).__init__(parent)
        self.controller = controller
        self.aggiorna_lista = aggiorna_lista

        self.v_layout = QVBoxLayout()
        self.font_label = QFont("Arial", 17)

        self.label_alto = QLabel("Compila il form di inserimento del dipendente")
        self.label_alto.setFont(self.font_label)
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(10)

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

        self.label_ruolo = QLabel("Ruolo")
        self.label_ruolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_ruolo)

        self.campo_ruolo = QLineEdit()
        self.v_layout.addWidget(self.campo_ruolo)

        self.label_id = QLabel("ID")
        self.label_id.setFont(self.font_label)
        self.v_layout.addWidget(self.label_id)

        self.campo_id = QLineEdit()
        self.v_layout.addWidget(self.campo_id)

        self.label_stipendio = QLabel("Stipendio")
        self.label_stipendio.setFont(self.font_label)
        self.v_layout.addWidget(self.label_stipendio)

        self.campo_stipendio = QLineEdit()
        self.v_layout.addWidget(self.campo_stipendio)

        self.v_layout.addSpacing(10)

        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(self.font_label)
        self.bottone_conferma.clicked.connect(self.conferma_inserimento)
        self.v_layout.addWidget(self.bottone_conferma)

        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.setWindowTitle("Inserimento Dipendente")

    def conferma_inserimento(self):
        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        ruolo = self.campo_ruolo.text()

        try:
            id = int(self.campo_id.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il codice ID", QMessageBox.Ok, QMessageBox.Ok)
            return

        if id > 99999 or id <10000:
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

