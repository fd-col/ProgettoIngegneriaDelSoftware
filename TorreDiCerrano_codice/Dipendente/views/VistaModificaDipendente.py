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


        self.campo_nome = self.create_format_campo("Nome:", self.controller.get_nome_dipendente())
        self.campo_cognome = self.create_format_campo("Cognome:", self.controller.get_cognome_dipendente())
        self.campo_ruolo = self.create_format_campo("Ruolo:", self.controller.get_ruolo_dipendente())
        self.campo_id = self.create_format_campo("ID", str(self.controller.get_id_dipendente()))
        self.campo_stipendio = self.create_format_campo("Stipendio:", str(self.controller.get_stipendio_dipendente()))

        self.h_layout = QHBoxLayout()

        self.create_button("Modifica", self.modifica_dipendente, "background-color: rgb(170,180,255);")
        self.create_button("Chiudi", self.chiudi_finestra, "background-color: rgb(255,0,0);")

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle("Dipendente")
        self.resize(450, 400)

    #Cre una label con la prima stringa passata la aggiunge al layout verticale della finestra, al di sotto aggiunge un
    #campo editabile con al suo interno la stringa passata come secondo argomento
    def create_format_campo(self, testo, get_campo):
        label = QLabel(testo)
        label.setFont(self.font_label)
        self.v_layout.addWidget(label)

        campo = QLineEdit()
        campo.setFont(QFont("Arial", 16))
        campo.setText(get_campo)
        self.v_layout.addWidget(campo)
        self.v_layout.addSpacing(10)
        return campo

    #Crea un bottone con il testo, la funzione e il colore di abckground passati e lo aggiunge al layout dei bottoni
    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("Arial", 15, 1, True))
        bottone.setStyleSheet(background_color)
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    def chiudi_finestra(self):
        self.close()

    def controlla_id_libero(self, _id):
        for dipendente in self.lista_dipendenti:
            if dipendente.id == _id:
                return False
        return True

    #Controlla se i campi modificati del dipendente siano stati compilati correttamente, applica gli stessi controlli
    #della funzione conferma_inserimento() in VistaInserisciDipendente.py
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
            QMessageBox.critical(self, "Errore", "L'ID deve essere composto da 5 cifre e non può cominciare con 0", QMessageBox.Ok, QMessageBox.Ok)
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
