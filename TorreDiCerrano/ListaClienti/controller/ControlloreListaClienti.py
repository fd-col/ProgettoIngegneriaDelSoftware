from ListaClienti.model.ListaClienti import ListaClienti


class ControlloreListaClienti():

    def __init__(self):
        self.model = ListaClienti()

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    def get_lista_clienti(self):
        return self.model.get_lista_clienti()

    def get_cliente_by_email(self, email):
        return self.model.get_cliente_by_email(email)

    def elimina_cliente_by_email(self, email):
        self.model.rimuovi_cliente_by_email(email)

    def save_data(self):
        self.model.save_data()