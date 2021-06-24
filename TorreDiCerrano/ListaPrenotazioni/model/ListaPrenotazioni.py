import os
import pickle


class ListaPrenotazioni:

    def __init__(self):
        self.lista_prenotazioni = []
        if os.path.isfile("ListaPrenotazioni/data/lista_prenotazioni_salvata.pickle"):
            with open("ListaPrenotazioni/data/lista_prenotazioni_salvata.pickle", "rb") as file:
                self.lista_prenotazioni = pickle.load(file)

    # Aggiungo una prenotazione e riordino la lista in base alle date
    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)
        self.lista_prenotazioni.sort()

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def get_lista_prenotazioni_cliente(self, email):
        lista_ritorno = []
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.email_cliente == email:
                lista_ritorno.append(prenotazione)
        return lista_ritorno

    def elimina_prenotazioni_cliente(self, email_cliente):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.email_cliente == email_cliente:
                self.lista_prenotazioni.remove(prenotazione)

    def elimina_prenotazione_singola(self, email, data_inizio):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.email_cliente == email and prenotazione.data_inizio == data_inizio:
                self.lista_prenotazioni.remove(prenotazione)
                return

    def save_data(self):
        with open("ListaPrenotazioni/data/lista_prenotazioni_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)
