from ListaDipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti
from ListaPrenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from Resoconto.model.Resoconto import Resoconto


class ControlloreResoconto:

    def __init__(self):
        super(ControlloreResoconto, self).__init__()
        self.model = Resoconto()
        self.controller_lista_dipendenti = ControlloreListaDipendenti()
        self.controller_lista_prenotazioni = ControlloreListaPrenotazioni()

    def calcola_costo_dipendenti(self, data_inizio, data_fine):
        return self.model.calcola_costo_dipendenti(data_inizio, data_fine, self.controller_lista_dipendenti.get_lista_dipendenti())

    def calcolo_ricavi_prenotazioni(self, data_inizio, data_fine):
        return self.model.calcola_ricavi_prenotazioni(data_inizio, data_fine, self.controller_lista_prenotazioni.get_lista_prenotazioni())
