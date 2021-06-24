from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QTextCharFormat, QColor
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QComboBox, QCheckBox, QMessageBox, \
    QPushButton
from datetime import datetime

from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from ListaServizi.model.ListeServizi import ListeServizi
from Prenotazione.model.Prenotazione import Prenotazione


class VistaNuovaPrenotazione(QWidget):

    def __init__(self, email_cliente, aggiorna_dati_prenotazioni, parent=None):
        super(VistaNuovaPrenotazione, self).__init__(parent)
        self.font = QFont("Arial", 16)
        self.email_cliente = email_cliente
        self.aggiorna_dati_prenotazioni = aggiorna_dati_prenotazioni
        self.layout = QGridLayout()

        # prenotazione data inizio vacanza
        self.label_inizio = QLabel("Seleziona la data di inizio della vacanza:")
        self.label_inizio.setStyleSheet("font: 200 14pt \"Papyrus\";\n""color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(178, 225, 255);\n""selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_inizio, 0, 0)

        self.calendario_inizio = QCalendarWidget()
        self.calendario_inizio.setGridVisible(True)
        self.calendario_inizio.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        if datetime.now() > datetime(2021, 6, 1):
            self.calendario_inizio.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        else:
            self.calendario_inizio.setMinimumDate(QDate(2021, 6, 1))
        self.calendario_inizio.setMaximumDate(QDate(2021, 9, 15))

        cell_inizio_start = QTextCharFormat()
        cell_inizio_start.setBackground(QColor("yellow"))
        cell_inizio_stop = QTextCharFormat()
        cell_inizio_stop.setBackground(QColor("red"))
        self.calendario_inizio.setDateTextFormat(self.calendario_inizio.selectedDate(), cell_inizio_start)
        self.calendario_inizio.setDateTextFormat(QDate(2021,9,14), cell_inizio_stop)

        self.layout.addWidget(self.calendario_inizio, 1, 0)

        # prenotazione data fine vacanza
        self.label_fine = QLabel("Seleziona la data di fine della vacanza:")
        self.label_fine.setStyleSheet("font: 200 14pt \"Papyrus\";\n"
                                                      "color: rgb(0, 0, 0);\n"
                                                      "background-color: rgb(178, 225, 255);\n"
                                                      "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_fine, 0, 1)

        self.calendario_fine = QCalendarWidget()
        self.calendario_fine.setGridVisible(True)
        self.calendario_fine.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        if datetime.now() > datetime(2021, 6, 1):
            self.calendario_fine.setMinimumDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        else:
            self.calendario_fine.setMinimumDate(QDate(2021, 6, 1))
        self.calendario_fine.setMaximumDate(QDate(2021, 9, 15))

        cell_fine_stop = QTextCharFormat()
        cell_fine_stop.setBackground(QColor("red"))
        self.calendario_fine.setDateTextFormat(QDate(2021, 9, 15), cell_fine_stop)

        self.layout.addWidget(self.calendario_fine, 1, 1)

        # selezione numero di persone
        self.label_numero_persone = QLabel("Seleziona il numero di persone:")
        self.label_numero_persone.setStyleSheet("font: 200 14pt \"Papyrus\";\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(178, 225, 255);\n"
                                          "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_numero_persone, 3, 0)





        # selezione tipologia di alloggio
        self.label_alloggio = QLabel("Seleziona il tipo di alloggio:")
        self.label_alloggio.setStyleSheet("font: 200 14pt \"Papyrus\";\n"
                                                      "color: rgb(0, 0, 0);\n"
                                                      "background-color: rgb(178, 225, 255);\n"
                                                      "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_alloggio, 5, 0)

        # selezione tipologia di ristorazione
        self.label_ristorazione = QLabel("Seleziona il tipo di ristorazione:")
        self.label_ristorazione.setStyleSheet("font: 200 14pt \"Papyrus\";\n"
                                                      "color: rgb(0, 0, 0);\n"
                                                      "background-color: rgb(178, 225, 255);\n"
                                                      "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_ristorazione, 8, 0)

        # selezione servizi aggiuntivi
        self.label_servizi_aggiuntivi = QLabel("Seleziona i servizi aggiunitvi:")
        self.label_servizi_aggiuntivi.setStyleSheet("font: 200 14pt \"Papyrus\";\n"
                                                      "color: rgb(0, 0, 0);\n"
                                                      "background-color: rgb(178, 225, 255);\n"
                                                      "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_servizi_aggiuntivi, 3, 1)

        self.get_servizi()

        # bottone finale di conferma
        self.bottone_conferma = QPushButton("Conferma")
        self.bottone_conferma.setFont(QFont("Arial", 15, 15, True))
        self.bottone_conferma.setStyleSheet("background-color: rgb(0,255,0);")
        self.bottone_conferma.clicked.connect(self.aggiungi_prenotazione)
        self.layout.addWidget(self.bottone_conferma, 9, 1)

        self.setLayout(self.layout)
        self.resize(1000, 600)
        self.setWindowTitle("Aggiungi Prenotazione")

    def get_servizi(self):
        self.liste_servizi = ListeServizi()

        self.menu_alloggio = QComboBox()
        self.model_menu_alloggio = QStandardItemModel(self.menu_alloggio)
        self.menu_numero_persone = QComboBox()
        self.model_menu_numero_persone = QStandardItemModel(self.menu_numero_persone)
        for servizio_alloggio in self.liste_servizi.get_servizi_alloggio():
            item1 = QStandardItem()
            item1.setText(servizio_alloggio.nome)
            item1.setEditable(False)
            item2 = QStandardItem()
            item2.setText(str(servizio_alloggio.numero_persone_max))
            item2.setEditable(False)
            self.model_menu_alloggio.appendRow(item1)
            self.model_menu_numero_persone.appendRow(item2)
        self.menu_alloggio.setModel(self.model_menu_alloggio)
        self.menu_numero_persone.setModel(self.model_menu_numero_persone)
        self.layout.addWidget(self.menu_alloggio, 6, 0)
        self.layout.addWidget(self.menu_numero_persone, 4, 0)

        self.menu_ristorazione = QComboBox()
        self.model_menu_ristorazione = QStandardItemModel(self.menu_ristorazione)
        for servizio_ristorazione in self.liste_servizi.get_servizi_ristorazione():
            item = QStandardItem()
            item.setText(servizio_ristorazione.nome)
            item.setEditable(False)
            self.model_menu_ristorazione.appendRow(item)
        self.menu_ristorazione.setModel(self.model_menu_ristorazione)
        self.layout.addWidget(self.menu_ristorazione, 9, 0)

        self.checkbox_noleggio = QCheckBox("Noleggio Mezzi Elettrici")
        self.layout.addWidget(self.checkbox_noleggio, 4, 1)

        self.checkbox_spa = QCheckBox("Centro Benessere")
        self.layout.addWidget(self.checkbox_spa, 5, 1)

        self.checkbox_escursione = QCheckBox("Escursione Turistica")
        self.layout.addWidget(self.checkbox_escursione, 6, 1)

    def aggiungi_prenotazione(self):
        data_inizio_q = self.calendario_inizio.selectedDate()
        data_inizio = datetime(data_inizio_q.year(), data_inizio_q.month(), data_inizio_q.day())

        data_fine_q = self.calendario_fine.selectedDate()
        data_fine = datetime(data_fine_q.year(), data_fine_q.month(), data_fine_q.day())

        if data_fine <= data_inizio:
            QMessageBox.critical(self, "Errore", "La data di fine non può essere precedente la data di inizio della vacanza", QMessageBox.Ok, QMessageBox.Ok)
            return

        servizio_alloggio = self.liste_servizi.get_servizi_alloggio()[self.menu_alloggio.currentIndex()]
        numero_persone = self.liste_servizi.get_servizi_alloggio()[self.menu_numero_persone.currentIndex()]
        servizio_ristorazione = self.liste_servizi.get_servizi_ristorazione()[self.menu_ristorazione.currentIndex()]
        servizi_aggiuntivi = []

        if self.checkbox_noleggio.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[0])

        if self.checkbox_escursione.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[1])

        if self.checkbox_spa.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[2])

        prenotazione = Prenotazione(self.email_cliente, data_inizio, data_fine, numero_persone, servizio_ristorazione, servizio_alloggio, servizi_aggiuntivi)

        risposta = QMessageBox.question(self, "Conferma", "Il costo della prenotazione è "
                                        + str(prenotazione.get_prezzo_totale()) + " € totali. \nDovrai versare una caparra di "
                                        + str(prenotazione.get_prezzo_totale()*20/100.0) + " €. \n\nConfermare?",
                                        QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.No:
            return
        else:
            controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
            controllore_lista_prenotazioni.aggiungi_prenotazione(prenotazione)
            QMessageBox.about(self, "Confermata", "La Prenotazione è stata Confermata")
            controllore_lista_prenotazioni.save_data()
            self.aggiorna_dati_prenotazioni()
            self.close()





