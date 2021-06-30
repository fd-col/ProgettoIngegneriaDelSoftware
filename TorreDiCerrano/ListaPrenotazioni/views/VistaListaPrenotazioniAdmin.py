from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel, QKeySequence
from PyQt5.QtWidgets import QListView, QVBoxLayout, QLabel, QWidget, QPushButton, QMessageBox, QShortcut, \
    QAbstractItemView
from PyQt5.QtCore import Qt

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from Prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from Prenotazione.views.VistaPrenotazione import VistaPrenotazione
from Servizio.model.Servizio import Servizio


class VistaListaPrenotazioniAdmin(QWidget):

    def __init__(self, data_inizio=None, parent=None):
        super(VistaListaPrenotazioniAdmin, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        self.data_inizio = data_inizio

        self.v_layout = QVBoxLayout()
        self.font = QFont("Arial", 15, 15, True)

        if data_inizio is not None:
            self.label_prenotazioni_by_data = QLabel("Arrivi del giorno " + data_inizio.strftime("%d/%m/%Y") + ":")
        else:
            self.label_prenotazioni_by_data = QLabel("Tutte le prenotazioni: ")
        self.label_prenotazioni_by_data.setStyleSheet("font:  20pt \"Papyrus\";""color: rgb(0,0,255);")
        self.label_prenotazioni_by_data.setAlignment(Qt.AlignCenter)
        self.v_layout.addWidget(self.label_prenotazioni_by_data)
        self.v_layout.addSpacing(15)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.bottone_dettagli_prenotaizone = QPushButton("Dettagli prenotazione")
        self.bottone_dettagli_prenotaizone.setFont(self.font)
        self.bottone_dettagli_prenotaizone.setStyleSheet("background-color: rgb(170,180,255);")
        self.bottone_dettagli_prenotaizone.clicked.connect(self.dettagli_prenotazione)
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.dettagli_prenotazione)
        self.v_layout.addWidget(self.bottone_dettagli_prenotaizone)
        self.v_layout.addSpacing(15)

        if data_inizio is not None:
            self.label_stato_resort = QLabel("Sommario prenotazioni:")
            self.label_stato_resort.setAlignment(Qt.AlignCenter)
            self.label_stato_resort.setStyleSheet("font:  18pt \"Papyrus\";""color: rgb(0,0,255);")
            self.v_layout.addWidget(self.label_stato_resort)
            self.lista_stato_resort = QListView()
            self.get_stato_resort(data_inizio)
            self.lista_stato_resort.setAlternatingRowColors(True)
            self.lista_stato_resort.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.v_layout.addWidget(self.lista_stato_resort)

        self.setLayout(self.v_layout)
        self.resize(900, 800)
        self.setWindowTitle("Lista Prenotazioni")

    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()

        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni():

            if self.data_inizio == prenotazione.data_inizio:
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data_inizio.strftime("%d/%m/%Y")
                             + " - " + prenotazione.data_fine.strftime("%d/%m/%Y") + " effettuata da " + prenotazione.email_cliente)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_prenotazioni.appendRow(item)
            elif self.data_inizio is None:
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data_inizio.strftime("%d/%m/%Y")
                             + " - " + prenotazione.data_fine.strftime("%d/%m/%Y") + " effettuata da " + prenotazione.email_cliente)
                item.setEditable(False)
                item.setFont(self.font)
                self.modello_lista_prenotazioni.appendRow(item)

        self.lista_prenotazioni.setModel(self.modello_lista_prenotazioni)

    def dettagli_prenotazione(self):
        try:
            indice = self.lista_prenotazioni.selectedIndexes()[0].row()
            if self.data_inizio is not None:
                lista_prenotazioni_filtrata = []
                for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni():
                    if prenotazione.data_inizio == self.data_inizio:
                        lista_prenotazioni_filtrata.append(prenotazione)
                da_visualizzare = lista_prenotazioni_filtrata[indice]
            else:
                da_visualizzare = self.controllore_lista_prenotazioni.get_lista_prenotazioni()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = VistaPrenotazione(ControllorePrenotazione(da_visualizzare))
        self.vista_prenotazione.show()

    def get_stato_resort(self, data_controllo_stato):
        self.modello_stato_resort = QStandardItemModel()

        numero_suite_occupate = 0
        numero_stanze_doppie_occupate = 0
        numero_stanze_familiari_occupate = 0
        numero_bungalow_occupati = 0

        numero_mezzi_elettrici_occupati = 0
        numero_prenotazioni_centro_benessere = 0
        numero_prenotazioni_escursione_turistica = 0

        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni():
            if data_controllo_stato >= prenotazione.data_inizio and data_controllo_stato <= prenotazione.data_fine:
                if prenotazione.servizio_alloggio == Servizio("Suite", "Alloggio", 235):
                    numero_suite_occupate = numero_suite_occupate + 1
                if prenotazione.servizio_alloggio == Servizio("Camera doppia", "Alloggio", 80):
                    numero_stanze_doppie_occupate = numero_stanze_doppie_occupate + 1
                if prenotazione.servizio_alloggio == Servizio("Camera famigliare", "Alloggio", 125):
                    numero_stanze_familiari_occupate = numero_stanze_familiari_occupate + 1
                if prenotazione.servizio_alloggio == Servizio("Bungalow", "Alloggio", 150):
                    numero_bungalow_occupati = numero_bungalow_occupati + 1

                for servizio_aggiuntivo in prenotazione.servizi_aggiuntivi:
                    if servizio_aggiuntivo == Servizio("Noleggio mezzi elettrici", "Servizi aggiuntivi", 30):
                        numero_mezzi_elettrici_occupati = numero_mezzi_elettrici_occupati + prenotazione.numero_persone
                    if servizio_aggiuntivo == Servizio("Centro benessere", "Servizi aggiuntivi", 50):
                        numero_prenotazioni_centro_benessere = numero_prenotazioni_centro_benessere + prenotazione.numero_persone
                    if servizio_aggiuntivo == Servizio("Escursione turistica", "Servizi aggiuntivi", 50):
                        numero_prenotazioni_escursione_turistica = numero_prenotazioni_escursione_turistica + prenotazione.numero_persone

        item_suite = QStandardItem()
        item_suite.setFont(self.font)
        item_suite.setEditable(False)
        item_suite.setText("Suite occupate: " + str(numero_suite_occupate))
        self.modello_stato_resort.appendRow(item_suite)

        item_camere_doppie = QStandardItem()
        item_camere_doppie.setFont(self.font)
        item_camere_doppie.setEditable(False)
        item_camere_doppie.setText("Camere doppie occupate: " + str(numero_stanze_doppie_occupate))
        self.modello_stato_resort.appendRow(item_camere_doppie)

        item_camere_famigliari = QStandardItem()
        item_camere_famigliari.setFont(self.font)
        item_camere_famigliari.setEditable(False)
        item_camere_famigliari.setText("Camere famigliari occupate: " + str(numero_stanze_doppie_occupate))
        self.modello_stato_resort.appendRow(item_camere_famigliari)

        item_bungalow = QStandardItem()
        item_bungalow.setFont(self.font)
        item_bungalow.setEditable(False)
        item_bungalow.setText("Bungalow occupati: " + str(numero_bungalow_occupati))
        self.modello_stato_resort.appendRow(item_bungalow)

        item_vuoto = QStandardItem()
        item_vuoto.setEditable(False)
        self.modello_stato_resort.appendRow(item_vuoto)

        item_mezzi_elettrici = QStandardItem()
        item_mezzi_elettrici.setFont(self.font)
        item_mezzi_elettrici.setEditable(False)
        item_mezzi_elettrici.setText("Numero mezzi elettrici noleggiati: " + str(numero_mezzi_elettrici_occupati))
        self.modello_stato_resort.appendRow(item_mezzi_elettrici)

        item_centro_benessere = QStandardItem()
        item_centro_benessere.setFont(self.font)
        item_centro_benessere.setEditable(False)
        item_centro_benessere.setText("Numero prenotazioni centro benessere: " + str(numero_prenotazioni_centro_benessere))
        self.modello_stato_resort.appendRow(item_centro_benessere)

        item_escursioni = QStandardItem()
        item_escursioni.setFont(self.font)
        item_escursioni.setEditable(False)
        item_escursioni.setText("Numero escursioni prenotate: " + str(numero_prenotazioni_escursione_turistica))
        self.modello_stato_resort.appendRow(item_escursioni)

        self.lista_stato_resort.setModel(self.modello_stato_resort)