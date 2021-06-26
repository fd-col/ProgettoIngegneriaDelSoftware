class ControllorePrenotazione:

    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_email_prenotazione(self):
        return self.model.email_cliente

    def get_data_inizio_prenotazione(self):
        return self.model.data_inizio

    def get_data_fine_prenotazione(self):
        return self.model.data_fine

    def get_servizio_ristorazione(self):
        return self.model.servizio_ristorazione

    def get_numero_persone(self):
        return self.model.numero_persone

    def get_servizio_alloggio(self):
        return self.model.servizio_alloggio

    def get_servizi_aggiuntivi(self):
        return self.model.servizi_aggiuntivi

    def get_prezzo_totale(self):
        return self.model.get_prezzo_totale()
