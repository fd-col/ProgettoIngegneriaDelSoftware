from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel

from Dipendente.controller.ControlloreDipendente import ControlloreDipendente
from Dipendente.views.VistaModificaDipendente import VistaModificaDipendente
from ListaDipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti
from ListaDipendenti.views.VistaInserisciDipendente import VistaInserisciDipendente


class VistaListaDipendenti(QWidget):

    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)
        self.controller = ControlloreListaDipendenti()
        self.font = QFont("Arial", 16)

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.create_button("Inserisci Dipendente", self.go_inserisci_dipendente, "background-color: rgb(0, 255, 0);")
        self.create_button("Visualizza", self.visualizza_dipendente, "background-color: rgb(170,180,255);")
        self.create_button("Modifica", self.go_modifica_dipendente, "background-color:#FFD800;")
        self.create_button("Elimina Dipendente", self.elimina_dipendente, "background-color: rgb(255, 0, 0);")

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.setWindowTitle("Lista Dipendenti")
        self.show()

    def create_button(self, testo, comando, background_color):
        bottone = QPushButton(testo)
        bottone.setFont(self.font)
        bottone.setStyleSheet(background_color)
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    def aggiorna_dati(self):
        self.list_view_model = QStandardItemModel(self.list_view)

        for dipendente in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            item.setFont(self.font)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    def go_inserisci_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.aggiorna_dati)
        self.vista_inserisci_dipendente.show()

    def visualizza_dipendente(self):
        pass

    def go_modifica_dipendente(self):
        try:
            indice = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_dipendenti()[indice]
        except:
            QMessageBox.critical(self, "Errore", "Seleziona il dipendente da visualizzare", QMessageBox.Ok, QMessageBox.Ok)
            return
        self.vista_modifica_dipendente = VistaModificaDipendente(ControlloreDipendente(da_visualizzare), self.aggiorna_dati, self.controller.get_lista_dipendenti())
        self.vista_modifica_dipendente.show()

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

    def closeEvent(self, event):
        self.controller.save_data()


