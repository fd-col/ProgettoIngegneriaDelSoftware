from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QListView, QVBoxLayout, QLabel, QWidget, QPushButton, QMessageBox

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from Prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from Prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaListaPrenotazioniAdmin(QWidget):

    def __init__(self, data_inizio, parent=None):
        super(VistaListaPrenotazioniAdmin, self).__init__(parent)
        self.controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        self.data_inizio = data_inizio

        self.v_layout = QVBoxLayout()
        self.font = QFont("Arial", 16)

        self.label_prenotazioni_data = QLabel("Arrivi di oggi: ")
        self.label_prenotazioni_data.setFont(self.font)
        self.v_layout.addWidget(self.label_prenotazioni_data)

        self.lista_prenotazioni = QListView()
        self.aggiorna_dati_prenotazioni()
        self.v_layout.addWidget(self.lista_prenotazioni)

        self.bottone_dettagli_prenotaizone = QPushButton("Dettagli prenotazione")
        self.bottone_dettagli_prenotaizone.setFont(self.font)
        self.bottone_dettagli_prenotaizone.clicked.connect(self.dettagli_prenotazione)
        self.v_layout.addWidget(self.bottone_dettagli_prenotaizone)

        self.setLayout(self.v_layout)
        self.resize(700, 600)
        self.setWindowTitle("Lista Prenotazioni")



    def aggiorna_dati_prenotazioni(self):
        self.modello_lista_prenotazioni = QStandardItemModel()
        for prenotazione in self.controllore_lista_prenotazioni.get_lista_prenotazioni():

        #il confronto non funziona bene
            if self.data_inizio == prenotazione.data_inizio.strftime("%d/%m/%Y"):
                item = QStandardItem()
                item.setText("Prenotazione del " + prenotazione.data_inizio.strftime("%d/%m/%Y") + " - " + prenotazione.data_fine.strftime("%d/%m/%Y"))
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