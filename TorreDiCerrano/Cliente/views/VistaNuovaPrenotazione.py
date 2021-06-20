from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from ListeServizi.model.ListeServizi import ListeServizi
from Prenotazione.model.Prenotazione import Prenotazione


class VistaNuovaPrenotazione(QWidget):

    def __init__(self, email_cliente, aggiorna_dati_prenotazioni, parent=None):
        super(VistaNuovaPrenotazione, self).__init__(parent)
        self.font = QFont("Arial", 16)
        self.email_cliente = email_cliente
        self.aggiorna_dati_prenotazioni = aggiorna_dati_prenotazioni

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

        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(self.font)
        self.bottone_conferma.clicked.connect(self.aggiungi_prenotazione)
        self.layout.addWidget(self.bottone_conferma, 5, 1)

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

        self.checkbox_noleggio = QCheckBox("Noleggio Mezzi Elettrici")
        self.layout.addWidget(self.checkbox_noleggio, 5, 0)

        self.checkbox_spa = QCheckBox("Centro Benessere")
        self.layout.addWidget(self.checkbox_spa, 6, 0)

        self.checkbox_escursione = QCheckBox("Escursione Turistica")
        self.layout.addWidget(self.checkbox_escursione, 7, 0)

    def aggiungi_prenotazione(self):
        data_inizio_q = self.calendario_inizio.selectedDate()
        data_inizio = datetime(data_inizio_q.year(), data_inizio_q.month(), data_inizio_q.day())

        data_fine_q = self.calendario_fine.selectedDate()
        data_fine = datetime(data_fine_q.year(), data_fine_q.month(), data_fine_q.day())

        if data_fine <= data_inizio:
            QMessageBox.critical(self, "Errore", "La data di fine non può essere precedente la data di inizio della vacanza", QMessageBox.Ok, QMessageBox.Ok)
            return

        servizio_alloggio = self.liste_servizi.get_servizi_alloggio()[self.menu_alloggio.currentIndex()]
        servizio_ristorazione = self.liste_servizi.get_servizi_ristorazione()[self.menu_ristorazione.currentIndex()]
        servizi_aggiuntivi = []

        if self.checkbox_noleggio.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[0])

        if self.checkbox_escursione.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[1])

        if self.checkbox_spa.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[2])

        prenotazione = Prenotazione(self.email_cliente, data_inizio,data_fine, servizio_ristorazione, servizio_alloggio, servizi_aggiuntivi)

        risposta = QMessageBox.question(self, "Conferma", "Il costo della prenotazione è " + str(prenotazione.get_prezzo_totale()) + " € \nDovrai versare una caparra di " + str(prenotazione.get_prezzo_totale()*20/100.0) + " € \nConfermare?", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.No:
            return
        else:
            controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
            controllore_lista_prenotazioni.aggiungi_prenotazione(prenotazione)
            QMessageBox.about(self, "Confermata", "La Prenotazione è stata Confermata")
            controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
            self.close()





