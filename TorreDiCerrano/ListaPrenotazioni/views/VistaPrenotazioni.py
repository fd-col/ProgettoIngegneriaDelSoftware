from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from ListaPrenotazioni.views.VistaNuovaPrenotazione import VistaNuovaPrenotazione
from Prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from Prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaPrenotazioni(QWidget):

    def __init__(self, email_cliente, parent = None):
        super(VistaPrenotazioni, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        self.email_cliente = email_cliente

        self.v_layout = QVBoxLayout()
        self.font = QFont("Arial", 16)

        self.label_prenotazioni = QLabel("Prenotazioni: ")
        self.label_prenotazioni.setFont(self.font)
        self.v_layout.addWidget(self.label_prenotazioni)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.h_layout = QHBoxLayout()

        self.bottone_nuova_prenotazione = QPushButton("Nuova prenotazione")
        self.bottone_nuova_prenotazione.setFont(self.font)
        self.bottone_nuova_prenotazione.clicked.connect(self.go_nuova_prenotazione)
        self.h_layout.addWidget(self.bottone_nuova_prenotazione)

        self.bottone_apri_prenotaizone = QPushButton("Apri prenotazione")
        self.bottone_apri_prenotaizone.setFont(self.font)
        self.bottone_apri_prenotaizone.clicked.connect(self.apri_prenotazione)
        self.h_layout.addWidget(self.bottone_apri_prenotaizone)

        self.bottone_elimina_prenotazione = QPushButton("Elimina prenotazione")
        self.bottone_elimina_prenotazione.setFont(self.font)
        self.bottone_elimina_prenotazione.clicked.connect(self.conferma_elimina_prenotazione)
        self.h_layout.addWidget(self.bottone_elimina_prenotazione)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.resize(300, 300)
        self.setWindowTitle("Prenotazioni")



    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.email_cliente):
            item = QStandardItem()
            item.setText("Prenotazione del " + prenotazione.data_inizio.strftime("%d/%m/%Y") + " - " + prenotazione.data_fine.strftime("%d/%m/%Y"))
            item.setEditable(False)
            item.setFont(self.font)
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
