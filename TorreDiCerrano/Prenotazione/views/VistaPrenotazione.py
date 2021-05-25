from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class VistaPrenotazione(QWidget):

    def __init__(self, controllore_prenotazione, parent = None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controllore_prenotazione = controllore_prenotazione
        self.v_layout = QVBoxLayout()

        self.font_label = QFont("Arial", 16)

        self.label_email = QLabel("Email: " + self.controllore_prenotazione.get_email_prenotazione())
        self.label_email.setFont(self.font_label)
        self.v_layout.addWidget(self.label_email)

        self.label_data = QLabel()
        self.label_data.setText("Periodo: " + self.controllore_prenotazione.get_data_inizio_prenotazione().strftime('%d/%m/%Y')
                                + " - " + self.controllore_prenotazione.get_data_fine_prenotazione().strftime('%d/%m/%Y'))
        self.label_data.setFont(self.font_label)
        self.v_layout.addWidget(self.label_data)

        self.label_servizio_ristorazione = QLabel("Servizio ristorazione: " + self.controllore_prenotazione.get_servizio_ristorazione().nome)
        self.label_servizio_ristorazione.setFont(self.font_label)
        self.v_layout.addWidget(self.label_servizio_ristorazione)

        self.label_servizio_alloggio = QLabel("Servizio alloggio: " + self.controllore_prenotazione.get_servizio_alloggio().nome)
        self.label_servizio_alloggio.setFont(self.font_label)
        self.v_layout.addWidget(self.label_servizio_alloggio)

        self.label_servizi_aggiuntivi = QLabel("Servizi aggiuntivi:")
        self.label_servizi_aggiuntivi.setFont(self.font_label)
        self.v_layout.addWidget(self.label_servizi_aggiuntivi)

        self.lista_servizi_aggiuntivi = QListView()
        self.get_dati_lista_servizi()
        self.v_layout.addWidget(self.lista_servizi_aggiuntivi)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Prenotazione")
        self.resize(300, 300)

    def get_dati_lista_servizi(self):
        self.list_view_model = QStandardItemModel()
        for servizio in self.controllore_prenotazione.get_servizi_aggiuntivi():
            item = QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            item.setFont(self.font_label)
            self.list_view_model.appendRow(item)
        self.lista_servizi_aggiuntivi.setModel(self.list_view_model)