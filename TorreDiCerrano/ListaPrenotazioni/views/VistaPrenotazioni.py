from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni


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
        self.h_layout.addWidget(self.bottone_nuova_prenotazione)

        self.bottone_apri_prenotaizone = QPushButton("Apri prenotazione")
        self.bottone_apri_prenotaizone.setFont(self.font)
        self.h_layout.addWidget(self.bottone_apri_prenotaizone)

        self.bottone_elimina_prenotazione = QPushButton("Elimina prenotazione")
        self.bottone_elimina_prenotazione.setFont(self.font)
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