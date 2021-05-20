from PyQt5.QtWidgets import *
from Cliente.controller.ControlloreCliente import ControlloreCliente


class VistaScannerizzaDocumento(QWidget):

    def __init__(self, controllore_cliente, parent=None):
        super(VistaScannerizzaDocumento, self).__init__(parent)

        self.controllore_cliente = controllore_cliente
        self.load_pdf_document()
        self.controllore_cliente.set_documento_identita(self.path)




    def load_pdf_document(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file',
                                                'c:\\Users\\fedju\\Downloads', "Image files (*.pdf)")
        self.path = file_name[0]
        print(self.path)    #PER VERIFICARE CHE IL PATH DEL FILE SIA CORRETTO

    #def visualizza_documento_caricato(self):
     #   documento = QFileDialog.getOpenFileName(None, "", str(self.path))
     #    return documento