from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from TorreDiCerrano.ListeServizi.controller.ControlloreListaServizi import ControlloreListaServizi


class VistaListaServizi(QWidget):
    def __init__(self, parent=None):
        super(VistaListaServizi, self).__init__(parent)

        self.controller = ControlloreListaServizi()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.list_view_model = QStandardItemModel(self.list_view)
        for servizio in self.controller.get_lista_dei_servizi():
            item = QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(20)
            item.setFont(font)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)
        h_layout.addWidget(self.list_view)

        self.setLayout(h_layout)
        self.resize(400,300)
        self.setWindowTitle("Lista Servizi")