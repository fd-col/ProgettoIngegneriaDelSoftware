from PyQt5.QtWidgets import *

from ListaClienti.controller.ControlloreListaClienti import ControlloreListaClienti


class VistaScannerizzaDocumento(QFileDialog):

    def __init__(self, controllore_cliente, parent=None):
        super(VistaScannerizzaDocumento, self).__init__(parent)

        self.controllore_cliente = controllore_cliente
        self.file_name = self.getOpenFileName(None, 'Seleziona il documento', "", "Image files (*.pdf)")
        self.path = self.file_name[0]
        self.controllore_cliente.set_documento_identita(self.path)
        QMessageBox.about(self, "Completato", "Il caricamento del documento è stato completato")
        self.close()