from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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
        self.bottone_nuova_prenotazione.clicked.connect(self.go_aggiungi_prenotazione)
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
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.email_cliente):
            item = QStandardItem()
            item.setText("Prenotazione del " + prenotazione.data_inizio.strftime("%d/%m/%Y") + " - " + prenotazione.data_fine.strftime("%d/%m/%Y"))
            item.setEditable(False)
            item.setFont(self.font)
            self.modello_lista_prenotazioni.appendRow(item)
        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)

    def go_aggiungi_prenotazione(self):
        self.vista_aggiungi_prenotazione = VistaNuovaPrenotazione(self.email_cliente)
        self.vista_aggiungi_prenotazione.show()

    def apri_prenotazione(self):
        prenotazione_selezionata = self.modello_lista_prenotazioni.currentRow()
        if prenotazione_selezionata == None:
            QMessageBox.critical(self, "Attenzione", "Non hai selezionato alcuna prenotazione da visualizzare",
                                 QMessageBox.Ok, QMessageBox.Ok)
        prenotazione_presa = self.controllore_lista_prenotazioni.get_lista_prenotazioni_cliente(self.email_cliente)[
            prenotazione_selezionata]
        self.vista_prenotazione = VistaPrenotazione(ControllorePrenotazione(prenotazione_presa))
        self.show()

    def conferma_elimina_prenotazione(self):
        self.controllore_prenotazione = ControllorePrenotazione()
        risposta = QMessageBox(self, "Elimina prenotazione",
                               "Sei sicuro di voler elimare la prenotazione selezionata? ", QMessageBox.Yes,
                               QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.close()
            self.controllore_lista_prenotazioni.elimina_prenotazione_singola(self.email_cliente(),
                                                                             self.controllore_prenotazione.get_data_inizio_prenotazione())
            self.controllore_lista_prenotazioni.save_data()
        else:
            pass
