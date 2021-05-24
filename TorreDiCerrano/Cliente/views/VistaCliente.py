from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


from Cliente.views.VistaScannerizzaDocumento import VistaScannerizzaDocumento
from ListaClienti.controller.ControlloreListaClienti import ControlloreListaClienti
from ListaPrenotazioni.views.VistaPrenotazioni import VistaPrenotazioni

class VistaCliente(QWidget):

    def __init__(self, controllore_cliente, parent=None):
        super(VistaCliente, self).__init__(parent)

        self.controllore_cliente = controllore_cliente

        self.v_layout = QVBoxLayout()

        self.label_nome = QLabel(self.controllore_cliente.get_nome_cliente() + " " + self.controllore_cliente.get_cognome_cliente())
        self.font_nome = QFont("Arial", 20)
        self.label_nome.setFont(self.font_nome)
        self.v_layout.addWidget(self.label_nome)

        self.label_nascita = QLabel("Data di nascita: " + self.controllore_cliente.get_data_nascita_cliente().strftime('%m/%d/%Y'))
        self.font_nascita = QFont("Arial", 16)
        self.label_nascita.setFont(self.font_nascita)
        self.v_layout.addWidget(self.label_nascita)

        self.label_indirizzo = QLabel("Indirizzo: " + self.controllore_cliente.get_indirizzo_cliente())
        self.font_indirizzo = QFont("Arial", 16)
        self.label_indirizzo.setFont(self.font_indirizzo)
        self.v_layout.addWidget(self.label_indirizzo)

        self.label_telefono = QLabel("Telefono: " + self.controllore_cliente.get_telefono_cliente())
        self.font_telefono = QFont("Arial", 16)
        self.label_telefono.setFont(self.font_telefono)
        self.v_layout.addWidget(self.label_telefono)

        self.label_email = QLabel("Email: " + self.controllore_cliente.get_email_cliente())
        self.font_email = QFont("Arial", 16)
        self.label_email.setFont(self.font_email)
        self.v_layout.addWidget(self.label_email)

        if self.controllore_cliente.get_documento_identita() is None:
            self.nome_documento = "Nessuno"
        else:
            self.path = self.controllore_cliente.get_documento_identita().split("/")
            self.nome_documento = self.path[-1]

        self.label_documento = QLabel("Documento: " + self.nome_documento)
        self.label_documento.setFont(self.font_email)
        self.v_layout.addWidget(self.label_documento)

        self.h_layout = QHBoxLayout()

        self.bottone_prenotazioni = QPushButton("Prenotazioni")
        self.bottone_prenotazioni.clicked.connect(self.go_lista_prenotazioni)
        self.h_layout.addWidget(self.bottone_prenotazioni)

        self.bottone_scannerizza = QPushButton("Scannerizza documento")
        self.h_layout.addWidget(self.bottone_scannerizza)
        self.bottone_scannerizza.clicked.connect(self.go_vista_scannerizza_documento)

        self.bottone_elimina_profilo = QPushButton("Elimina profilo")
        self.h_layout.addWidget(self.bottone_elimina_profilo)
        self.bottone_elimina_profilo.clicked.connect(self.conferma_elimina_profilo)

        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)
        self.setWindowTitle(self.controllore_cliente.get_nome_cliente() + " " + self.controllore_cliente.get_cognome_cliente())
        self.resize(325, 450)

    def go_vista_scannerizza_documento(self):
        self.vista_scannerizza_documento = VistaScannerizzaDocumento(self.controllore_cliente)
        self.aggiorna_documento()

    #Nelle prossime funzioni ci starà anche il controllore lista clienti che serve per salvare o aggiornare i dati

    def conferma_elimina_profilo(self):
        self.controllore_lista_clienti = ControlloreListaClienti()
        risposta = QMessageBox.warning(self, "Elimina Profilo", "Sei sicuro di voler elimare il tuo profilo ?\nCancellerai tutti i tuoi dati.", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.close()
            self.controllore_lista_clienti.elimina_cliente_by_email(self.controllore_cliente.get_email_cliente())
            self.controllore_lista_clienti.save_data()
        else:
            pass

    def aggiorna_documento(self):
        self.label_documento.setText("Documento: " + self.controllore_cliente.get_documento_identita().split("/")[-1])
        self.controllore_lista_clienti = ControlloreListaClienti()
        self.controllore_lista_clienti.get_cliente_by_email(self.controllore_cliente.get_email_cliente()).documento = self.controllore_cliente.get_documento_identita()
        self.controllore_lista_clienti.save_data()

    def go_lista_prenotazioni(self):
        self.vista_prenotazioni = VistaPrenotazioni(self.controllore_cliente.get_email_cliente())
        self.vista_prenotazioni.show()
