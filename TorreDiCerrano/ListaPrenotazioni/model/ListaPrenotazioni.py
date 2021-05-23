import os
import pickle


class ListaPrenotazioni():

    def __init__(self):
        self.lista_prenotazioni = []
        if os.path.isfile("TorreDiCerrano/ListaPrenotazioni/data/lista_prenotazioni_salvata.pickle"):
            with open("TorreDiCerrano/ListaPrenotazioni/data/lista_prenotazioni_salvata.pickle", "rb") as file:
                self.lista_prenotazioni = pickle.load(file)

    #Aggiungo una prenotazione e riordino la lista in base alle date
    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)
        self.lista_prenotazioni.sort()