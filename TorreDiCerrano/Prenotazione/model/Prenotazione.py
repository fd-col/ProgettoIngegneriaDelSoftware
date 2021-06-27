class Prenotazione:

    def __init__(self, email_cliente, data_inizio, data_fine, numero_persone, servizio_ristorazione, servizio_alloggio,
                 servizi_aggiuntivi):
        self.email_cliente = email_cliente
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.numero_persone = numero_persone
        self.servizio_ristorazione = servizio_ristorazione
        self.servizio_alloggio = servizio_alloggio
        self.servizi_aggiuntivi = servizi_aggiuntivi

    def __lt__(self, other):
        return self.data_inizio < other.data_inizio

    def get_prezzo_totale(self):
        numero_notti = self.data_fine.timetuple().tm_yday - self.data_inizio.timetuple().tm_yday
        prezzo_pernottamento = numero_notti*self.servizio_alloggio.prezzo
        prezzo_ristorazione = numero_notti*self.servizio_ristorazione.prezzo
        prezzo_servizi_aggiuntivi = 0
        for servizio_aggiuntivo in self.servizi_aggiuntivi:
            prezzo_servizi_aggiuntivi = prezzo_servizi_aggiuntivi + servizio_aggiuntivo.prezzo

        return prezzo_ristorazione+prezzo_pernottamento+prezzo_servizi_aggiuntivi

