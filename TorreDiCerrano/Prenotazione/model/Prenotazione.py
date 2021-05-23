class Prenotazione():

    def __init__(self, email_cliente, data_inizio, data_fine, servizio_ristorazione, servizio_alloggio, servizi_aggiuntivi):
        self.email_cliente = email_cliente
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.servizio_ristorazione = servizio_ristorazione
        self.servizio_alloggio = servizio_alloggio
        self.servizi_aggiuntivi = servizi_aggiuntivi

    def __lt__(self, other):
        return self.data_inizio < other.data_inizio