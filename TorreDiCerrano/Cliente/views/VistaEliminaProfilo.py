from PyQt5.QtWidgets import *
from ListaClienti.controller.ControlloreListaClienti import ControlloreListaClienti

#PORCODIO, RICORDATI IL self

class VistaEliminaProfilo(QWidget):

    def __init__(self, conferma_eliminazione, parent=None):
        super(VistaEliminaProfilo, self).__init__(parent)

        self.controllore_lista_clienti = ControlloreListaClienti()
        self.email_da_eliminare = email

        self.v_layout = QVBoxLayout()

        self.label_messaggio = QLabel(" Vuoi elimanare il profilo \ned eliminare tutti i tuoi dati ?")
        self.label_messaggio.setStyleSheet("font: 75 20pt \"Arial\";color: rgb(0, 0, 0);")
        self.v_layout.addWidget(self.label_messaggio)
        
        self.h_layout = QHBoxLayout()

        self.bottone_conferma = QPushButton()
        self.bottone_conferma.setText("Conferma")
        self.bottone_conferma.setStyleSheet("font: 75 16pt \"Arial\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(255, 0, 0);")
        self.bottone_conferma.clicked.connect(conferma_eliminazione)

        self.bottone_annulla = QPushButton()
        self.bottone_annulla.setText("Annulla")
        self.bottone_annulla.setStyleSheet("font: 75 16pt \"Arial\";\n"
                                            "color: rgb(0, 0, 0);\n"
                                            "background-color: rgb(0, 255, 0);")
        self.bottone_annulla.clicked.connect(self.chiudi_finestra)

        self.h_layout.addWidget(self.bottone_conferma)
        self.h_layout.addWidget(self.bottone_annulla)
        
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)
        self.resize(250, 250)
        self.setWindowTitle("Elimina Profilo")

    def chiudi_finestra(self):
        self.close()

    def conferma_eliminazione(self):
        self.controllore_lista_clienti = ControlloreListaClienti()
        self.close()
        self.controllore_lista_clienti.elimina_cliente_by_email(self.email)
        self.controllore_lista_clienti.save_data()
