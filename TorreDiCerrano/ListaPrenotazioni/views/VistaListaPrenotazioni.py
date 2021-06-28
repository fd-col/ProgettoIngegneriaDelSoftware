from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from datetime import datetime

from ListaPrenotazioni.views.VistaListaPrenotazioniAdmin import VistaListaPrenotazioniAdmin


class VistaListaPrenotazioni(QWidget):

    def __init__(self, parent=None):
        super(VistaListaPrenotazioni, self).__init__(parent)

        self.g_layout = QGridLayout()

        self.label_prenotazioni_by_data = QLabel("\nSeleziona una data, poi premi  'Vai'  per vedere gli arrivi alla data selezionata: \n")
        self.label_prenotazioni_by_data.setStyleSheet("font: 200 14pt \"Papyrus\";\n""color: rgb(0, 0, 0);\n"
                                                    "background-color: rgb(178, 225, 255);\n"
                                                    "selection-color: rgb(170, 255, 0);")
        self.g_layout.addWidget(self.label_prenotazioni_by_data, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario.setMinimumDate(QDate(2021, 6, 1))
        self.calendario.setMaximumDate(QDate(2021, 9, 15))

        self.g_layout.addWidget(self.calendario, 1, 0)

        self.h_layout = QHBoxLayout()

        self.create_button("Mostra tutte", self.go_lista_prenotazioni, "background-color:#FFD800;")
        self.create_button("Vai", self.go_lista_prenotazioni_by_data, "background-color:#00FF00;")

        self.g_layout.addLayout(self.h_layout, 2, 0)

        self.setLayout(self.g_layout)
        self.resize(700, 600)
        self.setWindowTitle("Lista Prenotazioni")

    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("Arial", 15, 1, True))
        bottone.setStyleSheet(background_color)
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    def go_lista_prenotazioni_by_data(self):
        data_inizio_q = self.calendario.selectedDate()
        self.data_inizio = datetime(data_inizio_q.year(), data_inizio_q.month(), data_inizio_q.day())
        self.lista_prenotazioni_by_data = VistaListaPrenotazioniAdmin(self.data_inizio)
        self.lista_prenotazioni_by_data.show()

    def go_lista_prenotazioni(self):
        self.lista_prenotazioni = VistaListaPrenotazioniAdmin()
        self.lista_prenotazioni.show()
