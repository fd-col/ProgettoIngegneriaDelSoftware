from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont


class VistaModificaDipendente(QWidget):

    def __init__(self, controllore_dipendente, aggiorna_lista, lista_dipendenti, parent=None):
        super(VistaModificaDipendente, self).__init__(parent)
        self.controller = controllore_dipendente
        self.aggiorna_lista = aggiorna_lista
        self.lista_dipendenti = lista_dipendenti

        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Arial", 16)
        self.font_label.setBold(True)

        self.font_campi = QFont("Arial", 16)

        self.label_nome = QLabel("Nome:")
        self.label_nome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_nome)

        self.campo_nome = QLineEdit()
        self.campo_nome.setFont(self.font_campi)
        self.campo_nome.setText(self.controller.get_nome_dipendente())
        self.v_layout.addWidget(self.campo_nome)

        self.label_cognome = QLabel("Cognome:")
        self.label_cognome.setFont(self.font_label)
        self.v_layout.addWidget(self.label_cognome)

        self.campo_cognome = QLineEdit()
        self.campo_cognome.setFont(self.font_campi)
        self.campo_cognome.setText(self.controller.get_cognome_dipendente())
        self.v_layout.addWidget(self.campo_cognome)

        self.label_ruolo = QLabel("Ruolo:")
        self.label_ruolo.setFont(self.font_label)
        self.v_layout.addWidget(self.label_ruolo)

        self.campo_ruolo = QLineEdit()
        self.campo_ruolo.setFont(self.font_campi)
        self.campo_ruolo.setText(self.controller.get_ruolo_dipendente())
        self.v_layout.addWidget(self.campo_ruolo)

        self.label_id = QLabel("ID:")
        self.label_id.setFont(self.font_label)
        self.v_layout.addWidget(self.label_id)

        self.campo_id = QLineEdit()
        self.campo_id.setFont(self.font_campi)
        self.campo_id.setText(str(self.controller.get_id_dipendente()))
        self.v_layout.addWidget(self.campo_id)

        self.label_stipendio = QLabel("Stipendio:")
        self.label_stipendio.setFont(self.font_label)
        self.v_layout.addWidget(self.label_stipendio)

        self.campo_stipendio = QLineEdit()
        self.campo_stipendio.setFont(self.font_campi)
        self.campo_stipendio.setText(str(self.controller.get_stipendio_dipendente()))
        self.v_layout.addWidget(self.campo_stipendio)

        self.h_layout = QHBoxLayout()

        self.bottone_chiudi = QPushButton("Chiudi")
        self.bottone_chiudi.setFont(self.font_campi)
        self.bottone_chiudi.clicked.connect(self.chiudi_finestra)
        self.h_layout.addWidget(self.bottone_chiudi)

        self.bottone_modifica = QPushButton("Modifica")
        self.bottone_modifica.setFont(self.font_campi)
        self.bottone_modifica.clicked.connect(self.modifica_dipendente)
        self.h_layout.addWidget(self.bottone_modifica)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dipendente")
        self.resize(300, 400)

    def chiudi_finestra(self):
        self.close()

    def controlla_id_libero(self, id):
        for dipendente in self.lista_dipendenti:
            if dipendente.id == id:
                return False
        return True

    def modifica_dipendente(self):

        nome = self.campo_nome.text()
        cognome = self.campo_cognome.text()
        ruolo = self.campo_ruolo.text()

        try:
            id = int(self.campo_id.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri per il codice ID", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if id > 99999 or id < 10000:
            QMessageBox.critical(self, "Errore", "L'ID deve essere composto da 5 cifre", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.controller.get_id_dipendente() == id:
            pass
        elif not self.controlla_id_libero(id):
            QMessageBox.critical(self, "Errore", "L'ID che hai immesso è già stato utilizzato", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        try:
            stipendio = float(self.campo_stipendio.text())
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo numeri con il punto per lo stipendio", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        if stipendio <= 0:
            QMessageBox.critical(self, "Errore", "Lo stipendio non può essere negativo", QMessageBox.Ok, QMessageBox.Ok)
            return

        if nome == "" or cognome == "" or ruolo == "" or id == 0 or stipendio == 0.0:
            QMessageBox.critical(self, "Errore", "Completa tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.controller.set_nome_dipendente(nome)
        self.controller.set_cognome_dipendente(cognome)
        self.controller.set_ruolo_dipendente(ruolo)
        self.controller.set_id_dipendente(id)
        self.controller.set_stipendio_dipendente(stipendio)
        QMessageBox.about(self, "Completata", "La modifica del dipendente è stata completata")
        self.aggiorna_lista()
        self.close()
