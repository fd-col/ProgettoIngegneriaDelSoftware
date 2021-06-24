from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QVBoxLayout, QWidget

from Resoconto.controller.ControlloreResoconto import ControlloreResoconto


class VistaTabellaResoconto(QWidget):

    def __init__(self, data_inizio, data_fine, spese_aggiuntive):
        super(VistaTabellaResoconto, self).__init__()

        self.controller_resoconto = ControlloreResoconto()
        self.ricavi_prenotazioni = self.controller_resoconto.calcolo_ricavi_prenotazioni(data_inizio, data_fine)
        self.costo_dipendenti = self.controller_resoconto.calcola_costo_dipendenti(data_inizio, data_fine)
        self.spese_aggiuntive_totali = 0.0
        for spesa_aggiuntiva in spese_aggiuntive:
            self.spese_aggiuntive_totali = self.spese_aggiuntive_totali + spesa_aggiuntiva

        self.v_layout = QVBoxLayout()

        self.table = self.create_table(8, 2, self.ricavi_prenotazioni, self.costo_dipendenti, self.spese_aggiuntive_totali)
        self.v_layout.addWidget(self.table)

        self.setLayout(self.v_layout)
        self.move(70,50)
        self.resize(1000, 900)
        self.setWindowTitle("RESOCONTO dal " + str(data_inizio) + " al " + str(data_fine))

    def create_table(self, row, column, ricavi_prenotazioni, costo_dipendenti, spese_aggiuntive_totali):

        table_widget = QTableWidget(row, column)
        # table settings
        table_widget.setAlternatingRowColors(True)
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table_widget.setFont(QFont("Arial", 18))
        table_widget.verticalHeader().setVisible(False)
        table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # header
        font = QFont("Times new roman", 25)
        font.setBold(True)
        table_widget.horizontalHeader().setFont(font)
        table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Resoconto"))
        table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Valore (€)"))

        # add items to table
        table_widget.setItem(0, 0, QTableWidgetItem("ENTRATE"))
        table_widget.setItem(0, 1, QTableWidgetItem(""))
        table_widget.setItem(1, 0, QTableWidgetItem("       Alloggio"))
        table_widget.setItem(1, 1, QTableWidgetItem(ricavi_prenotazioni[0]))
        table_widget.setItem(2, 0, QTableWidgetItem("       Ristorante"))
        table_widget.setItem(2, 1, QTableWidgetItem(ricavi_prenotazioni[1]))
        table_widget.setItem(3, 0, QTableWidgetItem("       Aggiuntivi"))
        table_widget.setItem(3, 1, QTableWidgetItem(ricavi_prenotazioni[2]))
        table_widget.setItem(4, 0, QTableWidgetItem("USCITE"))
        table_widget.setItem(4, 1, QTableWidgetItem(""))
        table_widget.setItem(5, 0, QTableWidgetItem("       Stipendi"))
        table_widget.setItem(5, 1, QTableWidgetItem(costo_dipendenti))
        table_widget.setItem(6, 0, QTableWidgetItem("       Spese aggiuntive"))
        table_widget.setItem(6, 1, QTableWidgetItem())
        table_widget.setItem(7, 0, QTableWidgetItem("UTILE"))
        table_widget.setItem(7, 1, QTableWidgetItem(spese_aggiuntive_totali))
        return table_widget
