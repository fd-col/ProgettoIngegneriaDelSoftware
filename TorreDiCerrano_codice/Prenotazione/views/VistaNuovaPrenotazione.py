
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QTextCharFormat, QColor, QKeySequence
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QComboBox, QCheckBox, QMessageBox, \
    QPushButton, QShortcut
from datetime import datetime, timedelta

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
        self.shortcut_open = QShortcut(QKeySequence('Return'), self)
        self.shortcut_open.activated.connect(self.aggiungi_prenotazione)
        self.layout.addWidget(self.bottone_conferma, 9, 1)

        self.setLayout(self.layout)
        self.resize(1000, 600)
        self.setWindowTitle("Aggiungi Prenotazione")

    def get_servizi(self):
        self.liste_servizi = ListeServizi()

        self.font_combo_box = QFont("Arial", 12)

        # menu a tendina per stabilire il servizio di aloggio
        self.menu_alloggio = QComboBox()
        self.menu_alloggio.setFont(self.font_combo_box)
        self.model_menu_alloggio = QStandardItemModel(self.menu_alloggio)

        # menu a tendina per stabilire il numero di persone
        self.menu_numero_persone = QComboBox()
        self.menu_numero_persone.setFont(self.font_combo_box)
        self.model_menu_numero_persone = QStandardItemModel(self.menu_numero_persone)

        for servizio_alloggio in self.liste_servizi.get_servizi_alloggio():
            item = QStandardItem()
            item.setText(servizio_alloggio.nome + "(max " + str(servizio_alloggio.numero_persone_max) + " persone)")
            item.setEditable(False)
            self.model_menu_alloggio.appendRow(item)
        self.menu_alloggio.setModel(self.model_menu_alloggio)

        for numero in [1, 2, 3, 4, 5, 6, 7, 8]:
            item = QStandardItem()
            item.setText(str(numero))
            item.setEditable(False)
            self.model_menu_numero_persone.appendRow(item)
        self.menu_numero_persone.setModel(self.model_menu_numero_persone)

        self.layout.addWidget(self.menu_alloggio, 6, 0)
        self.layout.addWidget(self.menu_numero_persone, 4, 0)

        # menu a tendina per stabilire il servizio ristorazione
        self.menu_ristorazione = QComboBox()
        self.menu_ristorazione.setFont(self.font_combo_box)
        self.model_menu_ristorazione = QStandardItemModel(self.menu_ristorazione)

        for servizio_ristorazione in self.liste_servizi.get_servizi_ristorazione():
            item = QStandardItem()
            item.setText(servizio_ristorazione.nome)
            item.setEditable(False)
            self.model_menu_ristorazione.appendRow(item)
        self.menu_ristorazione.setModel(self.model_menu_ristorazione)
        self.layout.addWidget(self.menu_ristorazione, 9, 0)

        #Checkbox servizi agginitivi
        self.checkbox_noleggio = QCheckBox("Noleggio Mezzi Elettrici")
        self.checkbox_noleggio.setFont(self.font_combo_box)
        self.layout.addWidget(self.checkbox_noleggio, 4, 1)

        self.checkbox_spa = QCheckBox("Centro Benessere")
        self.checkbox_spa.setFont(self.font_combo_box)
        self.layout.addWidget(self.checkbox_spa, 5, 1)

        self.checkbox_escursione = QCheckBox("Escursione Turistica")
        self.checkbox_escursione.setFont(self.font_combo_box)
        self.layout.addWidget(self.checkbox_escursione, 6, 1)

    #Controlla i dati inseriti nella prenotazione e se sono corretti registra la prenotazione
    def aggiungi_prenotazione(self):
        #Trasforma le date prese dal calendario da QDate a datetime
        data_inizio_q = self.calendario_inizio.selectedDate()
        data_inizio = datetime(data_inizio_q.year(), data_inizio_q.month(), data_inizio_q.day())

        data_fine_q = self.calendario_fine.selectedDate()
        data_fine = datetime(data_fine_q.year(), data_fine_q.month(), data_fine_q.day())

        #Controlla che la data di fine non sai precedente a quella di inizio
        if data_fine <= data_inizio:
            QMessageBox.critical(self, "Errore", "La data di fine non può essere precedente la data di inizio della vacanza", QMessageBox.Ok, QMessageBox.Ok)
            return

        #Controlla che la data di inizio della prenotazione sia almeno domani
        if data_inizio == datetime(datetime.now().year, datetime.now().month, datetime.now().day):
            QMessageBox.critical(self, "Errore", "La prenotazione non può partire da oggi", QMessageBox.Ok, QMessageBox.Ok)
            return

        #COntrolla che la prenotazione duri almeno 3 giorni
        if data_fine-data_inizio < timedelta(days=3):
            QMessageBox.critical(self, "Errore", "La prenotazione deve essere di almeno 3 giorni", QMessageBox.Ok, QMessageBox.Ok)
            return

        #indici dei servizi selezionati
        servizio_alloggio = self.liste_servizi.get_servizi_alloggio()[self.menu_alloggio.currentIndex()]
        numero_persone = self.menu_numero_persone.currentIndex()+1
        servizio_ristorazione = self.liste_servizi.get_servizi_ristorazione()[self.menu_ristorazione.currentIndex()]
        servizi_aggiuntivi = []

        if self.checkbox_noleggio.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[0])

        if self.checkbox_escursione.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[1])

        if self.checkbox_spa.isChecked():
            servizi_aggiuntivi.append(self.liste_servizi.get_servizi_aggiuntivi()[2])

        #Controlla la disponibilità dell'alloggio per le date selezionate
        if not self.controlla_disponibilita(data_inizio, data_fine, servizio_alloggio):
            QMessageBox.critical(self, "Ci Dispiace", "Nelle date per le quali vuoi prenotare non sono disponibili posti per il tipo di alloggio scelto", QMessageBox.Ok, QMessageBox.Ok)
            return

        #In base al valore ritornato dalla funzione controlla_disponibilità, assegna un codice all'ombrellone del cliente
        if servizio_alloggio.nome == "Suite" or servizio_alloggio.nome == "Bungalow":
            codice_ombrellone = str(self.controlla_disponibilita(data_inizio, data_fine, servizio_alloggio)) + servizio_alloggio.nome[0]
        else:
            codice_ombrellone = str(self.controlla_disponibilita(data_inizio, data_fine, servizio_alloggio)) + servizio_alloggio.nome[0] + servizio_alloggio.nome[7]

        #Controlla che il numero di persone inserite sia inferiore al numero di persone massimo per il tipo di alloggio scelto
        if numero_persone > servizio_alloggio.numero_persone_max:
            QMessageBox.critical(self, "Errore", "Il numero di persone selezionato è troppo alto per il tipo di alloggio scelto", QMessageBox.Ok, QMessageBox.Ok)
            return

        prenotazione = Prenotazione(self.email_cliente, data_inizio, data_fine, numero_persone, servizio_ristorazione, servizio_alloggio, servizi_aggiuntivi, codice_ombrellone)

        #Chiede la conferma per la prenotazione
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

    #Controlla la disponibilità dell'alloggio scelto nel periodo selezionato e in caso di disponibilità ritorna il numero
    #degli alloggi dello stesso tipo occupati nel primo giorno della prenotazione
    #Questo ritorno verrà utilizzato per assegnare il codice dell'ombrellone
    def controlla_disponibilita(self, data_inizio, data_fine, servizio_alloggio):
        controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        one_day = timedelta(days=1)
        data_controllo = data_inizio

        numero_ombrellone = 0

        disponibilita_giornaliera_alloggio = servizio_alloggio.disponibilita_giornaliera
        while data_controllo <= data_fine:
            disponibilita_giornaliera_rimanente = disponibilita_giornaliera_alloggio
            for prenotazione in controllore_lista_prenotazioni.get_lista_prenotazioni():
                if data_controllo >= prenotazione.data_inizio and data_controllo <= prenotazione.data_fine and prenotazione.servizio_alloggio == servizio_alloggio:
                    disponibilita_giornaliera_rimanente = disponibilita_giornaliera_rimanente-1
            if disponibilita_giornaliera_rimanente < 1:
                return False
            if data_controllo == data_inizio:
                numero_ombrellone = disponibilita_giornaliera_rimanente
            data_controllo = data_controllo + one_day
        return numero_ombrellone
