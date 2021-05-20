from Cliente.model.Cliente import Cliente

class ControlloreCliente():

    def __init__(self, cliente):
        self.model = cliente

    def get_nome_cliente(self):
        return self.model.nome

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_data_nascita_cliente(self):
        return self.model.dt_nascita

    def get_indirizzo_cliente(self):
        return self.model.indirizzo

    def get_telefono_cliente(self):
        return self.model.telefono

    def get_email_cliente(self):
        return self.model.e_mail

    def get_password_cliente(self):
        return self.model.password

    def get_documento_identita(self):
        return self.model.documento

    def set_documento_identita(self, path):
        #se il documento di identità non è presente, allora può essere aggiunto. Altrimenti viene restituito quello già presente
        if self.model.documento == None:
            self.model.documento = QFileDialog.getOpenFileName(None, "", str(path))
        else:
            self.get_documento_identita()

    