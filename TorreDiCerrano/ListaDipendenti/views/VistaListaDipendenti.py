from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Dipendente.controller.ControlloreDipendente import ControlloreDipendente
from Dipendente.views.VistaModificaDipendente import VistaModificaDipendente
from ListaDipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti
from ListaDipendenti.views.VistaInserisciDipendente import VistaInserisciDipendente


class VistaListaDipendenti(QWidget):

    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)

        self.controller = ControlloreListaDipendenti()

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.font_bottoni = QFont("Arial", 16)

        self.bottone_inserisci_dipendente = QPushButton("Inserisci Dipendente")
        self.bottone_inserisci_dipendente.clicked.connect(self.go_inserisci_dipendente)
        self.bottone_inserisci_dipendente.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.bottone_inserisci_dipendente)

        self.bottone_elimina_dipendente = QPushButton("Elimina Dipendente")
        self.bottone_elimina_dipendente.setFont(self.font_bottoni)
        self.bottone_elimina_dipendente.clicked.connect(self.elimina_dipendente)
        self.h_layout.addWidget(self.bottone_elimina_dipendente)

        self.bottone_modifica_dipendente = QPushButton("Modifica Dipendente")
        self.bottone_modifica_dipendente.setFont(self.font_bottoni)
        self.bottone_modifica_dipendente.clicked.connect(self.go_modifica_dipendente)
        self.h_layout.addWidget(self.bottone_modifica_dipendente)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.setWindowTitle("Lista Dipendenti")
        self.show()

    def aggiorna_dati(self):
        self.list_view_model = QStandardItemModel(self.list_view)

        self.font_item = QFont("Arial", 16)

        for dipendente in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def go_inserisci_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.aggiorna_dati)
        self.vista_inserisci_dipendente.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def elimina_dipendente(self):
        try:
            indice = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_dipendenti()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona il dipendente da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Sei sicuro di volere eliminare il dipendente?", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.controller.elimina_dipendente_by_id(da_eliminare.id)
            QMessageBox.about(self, "Eliminato", "Il dipendente è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    def go_modifica_dipendente(self):
        try:
            indice = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_dipendenti()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona il dipendente da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return
        self.vista_modifica_dipendente = VistaModificaDipendente(ControlloreDipendente(da_visualizzare), self.aggiorna_dati, self.controller.get_lista_dipendenti())
        self.vista_modifica_dipendente.show()
