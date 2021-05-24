import json
import pickle
import os.path

from TorreDiCerrano.Servizio.model.Servizio import Servizio


class ListeServizi():
    def __init__(self):
        super(ListeServizi, self).__init__()

        self.lista_servizi_ristorazione = []
        self.lista_servizi_alloggio = []
        self.lista_servizi_aggiuntivi = []

        with open("ListeServizi/data/lista_servizi.json") as file:
            liste_servizi = json.load(file)

        for servizio_ristorazione in liste_servizi[0]:
                self.lista_servizi_ristorazione.append(Servizio(servizio_ristorazione["nome"], servizio_ristorazione["campo"], servizio_ristorazione["prezzo"]))

        for servizio_alloggio in liste_servizi[1]:
            self.lista_servizi_alloggio.append(Servizio(servizio_alloggio["nome"], servizio_alloggio["campo"], servizio_alloggio["prezzo"], servizio_alloggio["disponibilita_giornaliera"]))

        for servizio_aggiuntivo in liste_servizi[2]:
            self.lista_servizi_aggiuntivi.append(Servizio(servizio_aggiuntivo["nome"], servizio_aggiuntivo["campo"], servizio_aggiuntivo["prezzo"], servizio_aggiuntivo["disponibilita_giornaliera"]))

    def get_servizi_ristorazione(self):
        return self.lista_servizi_ristorazione

    def get_servizi_alloggio(self):
        return self.lista_servizi_alloggio

    def get_servizi_aggiuntivi(self):
        return self.lista_servizi_aggiuntivi

    def save_data(self):
        with open("ListeServizi/data/lista_servizi_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_servizi, handle, pickle.HIGHEST_PROTOCOL)
