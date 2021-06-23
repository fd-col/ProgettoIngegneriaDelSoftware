from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QHBoxLayout
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem


class VistaPrenotazione(QWidget):

    def __init__(self, controllore_prenotazione, parent=None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controllore_prenotazione = controllore_prenotazione
        self.font_label = QFont("Arial", 14)

        self.v_layout = QVBoxLayout()

        # labels
        self.create_label("Email: ", self.controllore_prenotazione.get_email_prenotazione())
        self.create_label("Periodo: ", self.controllore_prenotazione.get_data_inizio_prenotazione().strftime('%d/%m/%Y')
                                + " - " + self.controllore_prenotazione.get_data_fine_prenotazione().strftime('%d/%m/%Y'))
        self.create_label("Servizio ristorazione: ", self.controllore_prenotazione.get_servizio_ristorazione().nome)
        self.create_label("Servizio alloggio: ", self.controllore_prenotazione.get_servizio_alloggio().nome)
        #self.create_label("Numero di persone: ", self.controllore_prenotazione.get_servizio_alloggio().numero_persone_max)


        # label servizi aggiuntivi
        self.label_servizi_aggiuntivi = QLabel("Servizi aggiuntivi:")
        self.label_servizi_aggiuntivi.setStyleSheet("color: rgb(0, 0, 0);\n""font: 300 18pt \"Times New Roman\";\n"
                                                    "background-color: rgba(178, 225, 255, 20);")

        self.v_layout.addWidget(self.label_servizi_aggiuntivi)
        self.v_layout.addSpacing(20)

        # lista servizi aggiuntivi
        self.lista_servizi_aggiuntivi = QListView()
        self.get_dati_lista_servizi()
        self.v_layout.addWidget(self.lista_servizi_aggiuntivi)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Prenotazione")
        self.resize(800, 500)

    def create_label(self, testo, text_label):
        h_layout = QHBoxLayout()

        label = QLabel(testo)
        label.setStyleSheet("color: rgb(0, 0, 0);\n""font: 300 18pt \"Times New Roman\";\n"
                            "background-color: rgba(178, 225, 255, 20);")
        h_layout.addWidget(label)

        label_di_testo = QLabel(text_label)
        label_di_testo.setFont(self.font_label)
        h_layout.addWidget(label_di_testo)

        self.v_layout.addLayout(h_layout)
        self.v_layout.addSpacing(20)

    def get_dati_lista_servizi(self):
        self.list_view_model = QStandardItemModel()
        for servizio in self.controllore_prenotazione.get_servizi_aggiuntivi():
            item = QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            item.setFont(self.font_label)
            self.list_view_model.appendRow(item)
            self.list_view_model.appendRow(None)
        self.lista_servizi_aggiuntivi.setModel(self.list_view_model)
