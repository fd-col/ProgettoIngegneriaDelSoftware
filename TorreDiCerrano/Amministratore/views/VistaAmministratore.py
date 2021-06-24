from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap, QKeySequence
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QShortcut, QMessageBox

from ListaDipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from ListaPrenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from Resoconto.views.VistaResoconto import VistaResoconto


class VistaAmministratore(QWidget):

    def __init__(self, nome, parent=None):
        super(VistaAmministratore, self).__init__(parent)

        self.v_layout = QVBoxLayout()

        self.label_icona = QLabel("Cliente")
        self.label_icona.setPixmap(QPixmap('images/profilo_amministratore.jpg').scaled(QSize(250,250), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.v_layout.addWidget(self.label_icona)

        self.label_nome = QLabel(nome)
        self.font_nome = QFont("Arial", 20)
        self.label_nome.setFont(self.font_nome)
        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addSpacing(20)

        # Horizontal layout for admin
        self.h_admin_layout = QHBoxLayout()

        self.label_admin = QLabel("Account Amministratore")
        self.font_admin = QFont("Arial", 16)
        self.label_admin.setFont(self.font_admin)

        self.bottone_info_shortcut = self.create_button("", self.visualizza_info_shortcut, "border-radius: 10px;",
                                                        "Alt+I", "images/icon_info.png", QSize(150, 150))
        self.h_admin_layout.addWidget(self.label_admin)
        self.h_admin_layout.addWidget(self.bottone_info_shortcut)

        self.v_layout.addLayout(self.h_admin_layout)
        self.v_layout.addSpacing(20)

        # Horizontal layout for buttons
        self.h_layout = QHBoxLayout()

        self.bottone_prenotazioni = self.create_button(" Lista Prenotazioni", self.go_lista_prenotazioni,
                                                       "background-color:#FFD800;", 'Alt+P',
                                                       "images/icon_prenotazione.png", )
        self.bottone_dipendenti = self.create_button(" Lista Dipendenti", self.go_lista_dipendenti,
                                                     "background-color:#FFD800;", 'Alt+D',
                                                     "images/icon_dipendenti.png", )
        self.bottone_resoconti = self.create_button("Resoconto", self.go_resoconto,
                                                    "background-color:#FFD800;", 'Alt+R',
                                                    "images/icon_resoconti.png", QSize(50, 50))
        self.h_layout.addWidget(self.bottone_prenotazioni)
        self.h_layout.addWidget(self.bottone_dipendenti)
        self.h_layout.addWidget(self.bottone_resoconti)

        self.v_layout.addLayout(self.h_layout)

        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setLayout(self.v_layout)
        self.setWindowTitle(nome)
        self.resize(350, 650)
        self.move(850, 130)

    def create_button(self, testo, comando, background_color, shortcut, icona, icon_size=QSize(30, 30)):
        bottone = QPushButton(testo)
        bottone.setFont(QFont("Arial", 15, 1, True))
        bottone.setStyleSheet(background_color)
        bottone.setIcon(QIcon(icona))
        bottone.setIconSize(icon_size)
        bottone.clicked.connect(comando)
        shortcut_open = QShortcut(QKeySequence(shortcut), self)
        shortcut_open.activated.connect(comando)
        return bottone

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_resoconto(self):
        self.vista_resoconto = VistaResoconto()
        self.vista_resoconto.show()

    def visualizza_info_shortcut(self):
        info = QMessageBox.information(self, "Info shortcut", "Alt+P --> bottone lista prenotazioni\n"
                                                              "Alt+D --> bottone lista dipendenti\n"
                                                              "Alt+R --> bottone resoconti", QMessageBox.Ok)
        if info == QMessageBox.Ok:
            pass
