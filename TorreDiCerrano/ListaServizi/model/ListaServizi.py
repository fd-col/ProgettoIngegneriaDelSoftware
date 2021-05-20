import json
import pickle
import os.path

from TorreDiCerrano.Servizio.model.Servizio import Servizio


class ListaServizi():
    def __init__(self):
        super(ListaServizi, self).__init__()
        self.lista_servizi = []
        if os.path.isfile("ListaServizi/data/lista_servizi_salvata.pickle"):
            with open("ListaServizi/data/lista_servizi_salvata.pickle", "rb") as file:
                self.lista_servizi = pickle.load(file)
        else:
            with open("ListaServizi/data/lista_servizi_iniziali.json") as file:
                lista_servizi_iniziali = json.load(file)
            for servizio_iniziale in lista_servizi_iniziali:
                self.aggiungi_servizio(Servizio(servizio_iniziale("nome"), servizio_iniziale("tipo"), servizio_iniziale("prezzo")))

    def aggiungi_servizio(self, servizio):
        self.lista_servizi.append(servizio)

    def get_servizio_by_index(self, index):
        return self.lista_servizi[index]

    def save_data(self):
        with open("ListaServizi/data/lista_servizi_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_servizi, handle, pickle.HIGHEST_PROTOCOL)
