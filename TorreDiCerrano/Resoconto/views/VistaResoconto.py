from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QCalendarWidget, QPushButton, QMessageBox, QLineEdit
from datetime import datetime

from Resoconto.views.VistaTabellaResoconto import VistaTabellaResoconto


class VistaResoconto(QWidget):

    def __init__(self):
        super(VistaResoconto, self).__init__()
        self.spese_aggiuntive = []

        # periodo totale di cui è possibile richiedere il resoconto
        self.data_inizio = QDate(2021, 6, 1)
        self.data_fine = QDate(2021, 9, 15)

        self.layout = QGridLayout()

        # periodo inizio resoconto
        self.label_inizio = QLabel("Periodo iniziale:")
        self.label_inizio.setStyleSheet("font: 200 14pt \"Papyrus\";\n""color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(178, 225, 255);\n""selection-color: rgb(170, 255, 0);")

        self.layout.addWidget(self.label_inizio, 0, 0)

        self.calendario_inizio = QCalendarWidget()
        self.calendario_inizio.setGridVisible(True)
        self.calendario_inizio.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario_inizio.setMinimumDate(self.data_inizio)
        self.calendario_inizio.setMaximumDate(self.data_fine)
        self.layout.addWidget(self.calendario_inizio, 1, 0)

        # periodo fine resoconto
        self.label_fine = QLabel("Periodo finale:")
        self.label_fine.setStyleSheet("font: 200 14pt \"Papyrus\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(178, 225, 255);\n"
                                      "selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_fine, 0, 1)

        self.calendario_fine = QCalendarWidget()
        self.calendario_fine.setGridVisible(True)
        self.calendario_fine.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario_fine.setMinimumDate(self.data_inizio)
        self.calendario_fine.setMaximumDate(self.data_fine)
        self.layout.addWidget(self.calendario_fine, 1, 1)

        # bottone "calcola resoconto"
        self.bottone_resoconto = QPushButton("Calcola Resoconto")
        self.bottone_resoconto.setStyleSheet("background-color: rgb(170, 255, 0);""font: 15pt \"Arial\";")
        self.bottone_resoconto.clicked.connect(self.mostra_resoconto)
        self.layout.addWidget(self.bottone_resoconto, 4, 1)

        # label altre spese
        self.label_altre_spese = QLabel("Inserisci le spese aggiuntive: ")
        self.label_altre_spese.setStyleSheet("font: 200 14pt \"Papyrus\";\n""color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(178, 225, 255);\n""selection-color: rgb(170, 255, 0);")
        self.layout.addWidget(self.label_altre_spese, 2, 0)

        # aggiungi altre spese
        self.altre_spese = QLineEdit()
        self.altre_spese.setFont(QFont("Arial", 10))
        self.layout.addWidget(self.altre_spese, 3, 0)

        self.bottone_aggiungi_spesa = QPushButton("Aggiungi spesa")
        self.bottone_aggiungi_spesa.clicked.connect(self.aggiungi_spesa)
        self.bottone_aggiungi_spesa.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.bottone_aggiungi_spesa, 3, 1)

        self.setLayout(self.layout)
        self.setWindowTitle("Resoconto")
        self.resize(800, 500)

    def mostra_resoconto(self):
        data_inizio_q = self.calendario_inizio.selectedDate()
        data_inizio = datetime(data_inizio_q.year(), data_inizio_q.month(), data_inizio_q.day())

        data_fine_q = self.calendario_fine.selectedDate()
        data_fine = datetime(data_fine_q.year(), data_fine_q.month(), data_fine_q.day())

        if data_fine < data_inizio:
            QMessageBox.critical(self, "Errore",
                                 "Il periodo finale non può essere precedente al periodo iniziale da resocontare",
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        self.tabella_resoconto = VistaTabellaResoconto(data_inizio, data_fine, self.spese_aggiuntive)
        self.tabella_resoconto.show()

    def aggiungi_spesa(self):
        try:
            spesa = float(self.altre_spese.text())
            self.spese_aggiuntive.append(spesa)
        except:
            QMessageBox.critical(self, "Errore", "Inserisci solo dei numeri", QMessageBox.Ok)
            return
        self.altre_spese.setText("")