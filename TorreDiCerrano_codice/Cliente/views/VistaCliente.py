from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QSize, Qt

from Cliente.views.VistaScannerizzaDocumento import VistaScannerizzaDocumento
from ListaClienti.controller.ControlloreListaClienti import ControlloreListaClienti
from ListaPrenotazioni.views.VistaPrenotazioniCliente import VistaPrenotazioniCliente


class VistaCliente(QWidget):

    def __init__(self, controllore_cliente, parent=None):
        super(VistaCliente, self).__init__(parent)

        self.controllore_cliente = controllore_cliente

        self.v_layout = QVBoxLayout()

        # icona profilo cliente
        self.label_icona = QLabel("Cliente")
        self.pixmap = QPixmap('images/profilo_utente.png').scaled(QSize(250,250), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label_icona.setPixmap(self.pixmap)

        self.v_layout.addWidget(self.label_icona)

        # label nome cliente
        self.label_nome = QLabel(self.controllore_cliente.get_nome_cliente() + " " + self.controllore_cliente.get_cognome_cliente())
        self.label_nome.setFont(QFont("Times New Roman", 30, 150))

        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addSpacing(40)

        # labels contenenti dati del cliente
        self.create_label("Data di nascita:  ", self.controllore_cliente.get_data_nascita_cliente().strftime('%m/%d/%Y'))
        self.create_label("Indirizzo:        ", self.controllore_cliente.get_indirizzo_cliente())
        self.create_label("Telefono:         ", self.controllore_cliente.get_telefono_cliente())
        self.create_label("Email:            ", self.controllore_cliente.get_email_cliente())

        self.v_layout.addSpacing(25)

        # horizontal layout for "documento"
        self.h_label_layout = QHBoxLayout()

        if self.controllore_cliente.get_documento_identita() is None or  self.controllore_cliente.get_documento_identita() == '':
            self.nome_documento = "Nessuno"
        else:
            self.path = self.controllore_cliente.get_documento_identita().split("/")
            self.nome_documento = self.path[-1]

        # label documento
        self.label_documento = QLabel("Documento:        " )
        self.label_documento.setStyleSheet("color: rgb(255, 0, 0);\n""font: 100 18pt \"Times New Roman\";\n"
                            "background-color: rgba(178, 225, 255, 20);")
        self.h_label_layout.addWidget(self.label_documento)

        self.label_documento_testo = QLabel(self.nome_documento)
        self.label_documento_testo.setFont(QFont("Arial", 16))
        self.h_label_layout.addWidget(self.label_documento_testo)
        self.v_layout.addLayout(self.h_label_layout)

        self.v_layout.addSpacing(25)

        self.h_layout = QHBoxLayout()

        # bottoni profilo cliente collegati alle relative funzioni
        self.create_button("Prenotazioni", self.go_lista_prenotazioni)
        self.create_button("Scannerizza documento", self.go_vista_scannerizza_documento)
        self.create_button("Elimina profilo", self.conferma_elimina_profilo)

        self.v_layout.addLayout(self.h_layout)

        self.setStyleSheet("background-color: rgb(178, 225, 255);")
        self.setLayout(self.v_layout)
        self.setWindowTitle("Profilo Cliente")
        self.rect = self.frameGeometry()
        self.setGeometry(self.rect)

    #Crea due label in un horizontal layout che poi viene aggiunto al layout verticale della finestra
    #La label più a sinistra viene creata con il testo passato nel primo parametro, la label più a destra viene creata
    #con il la stringa passata come secondo parametro
    def create_label(self, testo, text_label):
        h_layout = QHBoxLayout()

        label = QLabel(testo)
        label.setStyleSheet("color: rgb(0, 0, 0);\n""font: 200 18pt \"Times New Roman\";\n"
                            "background-color: rgba(178, 225, 255, 20);")
        h_layout.addWidget(label)

        label_di_testo = QLabel(text_label)
        label_di_testo.setFont(QFont("Arial", 16))
        h_layout.addWidget(label_di_testo)

        self.v_layout.addLayout(h_layout)

    #Crea un bottone e lo aggiunge al layout orizzontale dei bottoni
    #Riceve come argomenti il testo da mettere nei bottoni e la funzione da collegare
    def create_button(self, testo, comando):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("Arial", 15, 1, True))
        bottone.setStyleSheet("background-color:#FFD800;")
        bottone.clicked.connect(comando)
        self.h_layout.addWidget(bottone)

    # Nelle prossime funzioni ci starà anche il controllore lista clienti che serve per salvare o aggiornare i dati

    #Visualizza la lista delle prenotazioni
    def go_lista_prenotazioni(self):
        if self.controllore_cliente.get_documento_identita() is None or self.controllore_cliente.get_documento_identita() == '':
            QMessageBox.critical(self, "Errore", "Seleziona un documento prima di prenotare la tua vacanza", QMessageBox.Ok, QMessageBox.Ok)
            return
        self.vista_prenotazioni_cliente = VistaPrenotazioniCliente(self.controllore_cliente.get_email_cliente())
        self.vista_prenotazioni_cliente.show()

    #Visualizza la finestra per la scannerizzazione del documento
    def go_vista_scannerizza_documento(self):
        self.vista_scannerizza_documento = VistaScannerizzaDocumento(self.controllore_cliente)
        self.aggiorna_documento()


    #Chiede conferma per l'eliminazione del profilo e in caso affermativo lo cancella
    def conferma_elimina_profilo(self):
        self.controllore_lista_clienti = ControlloreListaClienti()
        risposta = QMessageBox.warning(self, "Elimina Profilo", "Sei sicuro di voler elimare il tuo profilo ?\nLe prenotazioni effettuate non verranno eliminate.", QMessageBox.Yes, QMessageBox.No)
        if risposta == QMessageBox.Yes:
            self.close()
            self.controllore_lista_clienti.elimina_cliente_by_email(self.controllore_cliente.get_email_cliente())
            self.controllore_lista_clienti.save_data()
        else:
            pass

    #Funzione di callback per aggiornare la label del documento di identità nella finestra
    def aggiorna_documento(self):
        if self.controllore_cliente.get_documento_identita() is None or self.controllore_cliente.get_documento_identita() == '':
            return
        self.label_documento_testo.setText(self.controllore_cliente.get_documento_identita().split("/")[-1])
        self.controllore_lista_clienti = ControlloreListaClienti()
        self.controllore_lista_clienti.get_cliente_by_email(self.controllore_cliente.get_email_cliente()).documento = self.controllore_cliente.get_documento_identita()
        self.controllore_lista_clienti.save_data()




