from Cliente.controller.ControlloreCliente import ControlloreCliente


class VistaScannerizzaDocumento():

    def __init__(self):
        super(VistaScannerizzaDocumento, self).__init__()

        self.load_pdf_document()



    def load_pdf_document(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file',
                                                'c:\\Users\\fedju\\Downloads', "Image files (*.jpg *.jpeg *.png)")
        self.path = file_name[0]
        print(self.path)

    def visualizza_documento_caricato(self):
        document = QFileDialog.getOpenFileName(None, "", str(self.path))