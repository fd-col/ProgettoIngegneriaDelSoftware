import os
import pickle

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime

from ListeServizi.model.ListeServizi import ListeServizi
from Servizio.model.Servizio import Servizio


class VistaAggiungiPrenotazione(QWidget):

    def __init__(self, parent = None):
        super(VistaAggiungiPrenotazione, self).__init__(parent)
        self.font = QFont("Arial", 16)

        self.layout = QGridLayout()

        self.label_inizio = QLabel("Seleziona la data di inizio della vacanza:")
        self.label_inizio.setFont(self.font)
        self.layout.addWidget(self.label_inizio, 0, 0)

        self.calendario_inizio = QCalendarWidget()
        self.calendario_inizio.setGridVisible(True)
        self.calendario_inizio.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        if datetime.now() > datetime(2021, 6, 1):
            self.calendario_inizio.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        else:
            self.calendario_inizio.setMinimumDate(QDate(2021, 6, 1))
        self.calendario_inizio.setMaximumDate(QDate(2021, 9, 15))
        self.layout.addWidget(self.calendario_inizio, 1, 0)

        self.label_fine = QLabel("Seleziona la data di fine della vacanza:")
        self.label_fine.setFont(self.font)
        self.layout.addWidget(self.label_fine, 0, 1)

        self.calendario_fine = QCalendarWidget()
        self.calendario_fine.setGridVisible(True)
        self.calendario_fine.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        if datetime.now() > datetime(2021, 6, 1):
            self.calendario_fine.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        else:
            self.calendario_fine.setMinimumDate(QDate(2021, 6, 1))
        self.calendario_fine.setMaximumDate(QDate(2021, 9, 15))
        self.layout.addWidget(self.calendario_fine, 1, 1)

        self.label_alloggio = QLabel("Seleziona il tipo di alloggio:")
        self.label_alloggio.setFont(self.font)
        self.layout.addWidget(self.label_alloggio, 3, 0)

        self.label_ristorazione = QLabel("Seleziona il tipo di ristorazione:")
        self.label_ristorazione.setFont(self.font)
        self.layout.addWidget(self.label_ristorazione, 3, 1)

        self.get_servizi()

        self.setLayout(self.layout)
        self.resize(1000, 600)
        self.setWindowTitle("Aggiungi Prenotazione")

    def get_servizi(self):
        self.liste_servizi = ListeServizi()

        self.menu_alloggio = QComboBox()
        self.model_menu_alloggio = QStandardItemModel(self.menu_alloggio)
        for servizio_alloggio in self.liste_servizi.get_servizi_alloggio():
            item = QStandardItem()
            item.setText(servizio_alloggio.nome)
            item.setEditable(False)
            self.model_menu_alloggio.appendRow(item)
        self.menu_alloggio.setModel(self.model_menu_alloggio)
        self.layout.addWidget(self.menu_alloggio, 4, 0)

        self.menu_ristorazione = QComboBox()
        self.model_menu_ristorazione = QStandardItemModel(self.menu_ristorazione)
        for servizio_ristorazione in self.liste_servizi.get_servizi_ristorazione():
            item = QStandardItem()
            item.setText(servizio_ristorazione.nome)
            item.setEditable(False)
            self.model_menu_ristorazione.appendRow(item)
        self.menu_ristorazione.setModel(self.model_menu_ristorazione)
        self.layout.addWidget(self.menu_ristorazione, 4, 1)

        riga_servizi_aggiuntivi = 5
        for servizio_aggiuntivo in self.liste_servizi.get_servizi_aggiuntivi():
            check_box = QCheckBox(servizio_aggiuntivo.nome)
            self.layout.addWidget(check_box, riga_servizi_aggiuntivi, 0)
            riga_servizi_aggiuntivi = riga_servizi_aggiuntivi + 1