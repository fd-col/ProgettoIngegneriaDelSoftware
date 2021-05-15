from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)

        self.font = QFont("Arial", 17)

        self.v_layout = QVBoxLayout()

        self.label_alto = QLabel("Inserisci i dati per il login")
        self.label_alto.setFont(self.font)
        self.v_layout.addWidget(self.label_alto)

        self.v_layout.addSpacing(10)

        self.label_email = QLabel("E-mail")
        self.label_email.setFont(self.font)
        self.v_layout.addWidget(self.label_email)

        self.campo_email = QLineEdit()
        self.v_layout.addWidget(self.campo_email)

        self.label_password = QLabel("Password")
        self.label_password.setFont(self.font)
        self.v_layout.addWidget(self.label_password)

        self.campo_password = QLineEdit()
        self.v_layout.addWidget(self.campo_password)

        self.v_layout.addSpacing(20)

        self.bottone_login = QPushButton("Login")
        self.bottone_login.setFont(self.font)
        self.bottone_login.setStyleSheet("background-color:#ccd9ff;")
        self.v_layout.addWidget(self.bottone_login)

        self.setLayout(self.v_layout)
        self.resize(200, 200)
        self.setWindowTitle("Login")
