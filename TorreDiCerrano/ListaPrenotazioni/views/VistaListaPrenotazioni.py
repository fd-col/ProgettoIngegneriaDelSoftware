from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from ListaPrenotazioni.views.VistaListaPrenotazioniAdmin import VistaListaPrenotazioniAdmin


class VistaListaPrenotazioni(QWidget):

    def __init__(self, parent=None):
        super(VistaListaPrenotazioni, self).__init__(parent)

        self.g_layout = QGridLayout()
        self.font = QFont("Arial", 16)

#FARE UN PULSANTE CHE QUANDO PREMUTO MOSTRI TUTTI LE PRENOTAZIONI PRESENTI
        #self.label_prenotazioni_presenti = QLabel("Tutte le prenotazioni presenti: ")
        #self.label_prenotazioni_presenti.setFont(self.font)
        #self.v_layout.addWidget(self.label_prenotazioni_presenti)

        self.label_prenotazioni_data = QLabel("\nSeleziona una data, poi premi  'Vai'  per vedere gli arrivi alla data selezionata: \n")
        self.label_prenotazioni_data.setStyleSheet("font: 200 14pt \"Papyrus\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(178, 225, 255);\n"
                                      "selection-color: rgb(170, 255, 0);")
        self.g_layout.addWidget(self.label_prenotazioni_data, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario.setMinimumDate(QDate(2021, 6, 1))
        self.calendario.setMaximumDate(QDate(2021, 9, 15))
        self.g_layout.addWidget(self.calendario, 1, 0)

        data_inizio_q = self.calendario.selectedDate()
        self.data_inizio = datetime(data_inizio_q.year(), data_inizio_q.month(), data_inizio_q.day())

        self.h_layout = QHBoxLayout()

        self.bottone_prenotazioni_totali = QPushButton("Mostra tutte")
        self.bottone_prenotazioni_totali.setFont(self.font)
        self.bottone_prenotazioni_totali.setStyleSheet("background-color:#FFD800;")
        self.bottone_prenotazioni_totali.clicked.connect(self.go_lista_prenotazioni)
        self.h_layout.addWidget(self.bottone_prenotazioni_totali)

        self.bottone_prenotazioni_selezionate = QPushButton("Vai")
        self.bottone_prenotazioni_selezionate.setFont(self.font)
        self.bottone_prenotazioni_selezionate.setStyleSheet("background-color:#00FF00;")
        self.bottone_prenotazioni_selezionate.clicked.connect(self.go_lista_prenotazioni_by_data)
        self.h_layout.addWidget(self.bottone_prenotazioni_selezionate)

        self.g_layout.addLayout(self.h_layout, 2, 0)

        self.setLayout(self.g_layout)
        self.resize(700, 600)
        self.setWindowTitle("Lista Prenotazioni")


    def go_lista_prenotazioni_by_data(self):
        self.lista_prenotazioni_by_data = VistaListaPrenotazioniAdmin(self.data_inizio)
        self.lista_prenotazioni_by_data.show()

    def go_lista_prenotazioni(self):
        self.lista_prenotazioni = VistaListaPrenotazioniAdmin()
        self.lista_prenotazioni.show()


