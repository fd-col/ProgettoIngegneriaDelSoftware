from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from datetime import datetime

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from Cliente.views.VistaNuovaPrenotazione import VistaNuovaPrenotazione
from Prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from Prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaPrenotazioniCliente(QWidget):

    def __init__(self, email_cliente, parent=None):
        super(VistaPrenotazioniCliente, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        self.email_cliente = email_cliente

        self.v_layout = QVBoxLayout()

        self.label_prenotazioni = QLabel("Prenotazioni: ")
        self.label_prenotazioni.setFont(QFont("Times New Roman", 18))
        self.v_layout.addWidget(self.label_prenotazioni)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.h_layout = QHBoxLayout()

        self.create_button("Nuova prenotazione", self.go_nuova_prenotazione, "background-color: rgb(0, 255, 0);")
        self.create_button("Apri prenotazione", self.apri_prenotazione, "background-color: rgb(170,180,255);")
        self.create_button("Elimina prenotazione", self.conferma_elimina_prenotazione, "background-color: rgb(255,0,0);")

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.resize(250, 500)
        self.setWindowTitle("Prenotazioni")

    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("Arial", 14))
        bottone.setStyleSheet(background_color)
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.email_cliente):
            item = QStandardItem()
            item.setText("Prenotazione del " + prenotazione.data_inizio.strftime("%d/%m/%Y") + " - " + prenotazione.data_fine.strftime("%d/%m/%Y"))
            item.setEditable(False)
            item.setFont(QFont("Arial", 16))
            self.modello_lista_prenotazioni.appendRow(item)
        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)

    def go_nuova_prenotazione(self):
        self.vista_nuova_prenotazione = VistaNuovaPrenotazione(self.email_cliente, self.aggiorna_dati_prenotazioni)
        self.vista_nuova_prenotazione.show()

    def apri_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            da_visualizzare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.email_cliente)[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = VistaPrenotazione(ControllorePrenotazione(da_visualizzare))
        self.vista_prenotazione.show()

    def conferma_elimina_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            da_eliminare = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.email_cliente)[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da eliminare", QMessageBox.Ok,QMessageBox.Ok)
            return

        if da_eliminare.data_inizio < datetime.now():
            QMessageBox.critical(self, "Errore", "Non puoi eliminare prenotazioni passate", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Elimina prenotazione",
                               "Sei sicuro di voler elimare la prenotazione selezionata? \nPerderai la caparra versata", QMessageBox.Yes,
                               QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controllore_lista_prenotazioni.elimina_prenotazione_singola(self.email_cliente, da_eliminare.data_inizio)
            self.controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
        else:
            return
