from Cliente.controller.ControlloreCliente import ControlloreCliente


class VistaScannerizzaDocumento():

    def __init__(self, controllore_cliente):
        super(VistaScannerizzaDocumento, self).__init__()

        self.load_pdf_document()
        self.set_documento_identita(documento = QFileDialog.getOpenFileName(None, "", str(self.path)))
        #documento = QFileDialog.getOpenFileName(None, "", str(self.path))





    def load_pdf_document(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file',
                                                'c:\\Users\\fedju\\Downloads', "Image files (*.pdf)")
        self.path = file_name[0]
        print(self.path) #solo un controllo del path del file

    def set_documento_identita(self, documento):
        self.controllore_cliente.set_documento_identita(documento)