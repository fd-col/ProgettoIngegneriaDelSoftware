import os
import pickle


class ListaClienti():

    def __init__(self):
        super(ListaClienti, self).__init__()
        self.lista_clienti = []
        if os.path.isfile("ListaClienti/data/lista_clienti_salvata.pickle"):
            with open("ListaClienti/data/lista_clienti_salvata.pickle", "rb") as file:
                self.lista_clienti = pickle.load(file)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def rimuovi_cliente_by_email(self, email):
        for cliente in self.lista_clienti:
            if cliente.e_mail == email:
                self.lista_clienti.remove(cliente)
                return True
        return False

    def get_lista_clienti(self):
        return self.lista_clienti

    def get_cliente_by_email(self, email):
        for cliente in self.lista_clienti:
            if cliente.e_mail == email:
                return cliente
        return None

    def save_data(self):
        with open("ListaClienti/data/lista_clienti_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)