from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel, QKeySequence
from PyQt5.QtWidgets import QListView, QVBoxLayout, QLabel, QWidget, QPushButton, QMessageBox, QShortcut
from PyQt5.QtCore import Qt

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from Prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from Prenotazione.views.VistaPrenotazione import VistaPrenotazione


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
        self.v_layout.addSpacing(30)

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

        self.setLayout(self.v_layout)
        self.resize(900, 600)
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
            da_visualizzare = self.controllore_lista_prenotazioni.get_lista_prenotazioni()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona la prenotazione da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.vista_prenotazione = VistaPrenotazione(ControllorePrenotazione(da_visualizzare))
        self.vista_prenotazione.show()
