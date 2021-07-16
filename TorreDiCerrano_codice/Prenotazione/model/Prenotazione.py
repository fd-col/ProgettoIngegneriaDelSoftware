class Prenotazione:

    def __init__(self, email_cliente, data_inizio, data_fine, numero_persone, servizio_ristorazione, servizio_alloggio,
                 servizi_aggiuntivi, codice_ombrellone):
        self.email_cliente = email_cliente
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.numero_persone = numero_persone
        self.servizio_ristorazione = servizio_ristorazione
        self.servizio_alloggio = servizio_alloggio
        self.servizi_aggiuntivi = servizi_aggiuntivi
        self.codice_ombrellone = codice_ombrellone

    def __lt__(self, other):
        return self.data_inizio < other.data_inizio

    #Calcola il costo della prenotazione
    def get_prezzo_totale(self):

        #Numero di notti della prenotazione
        numero_notti = self.data_fine.timetuple().tm_yday - self.data_inizio.timetuple().tm_yday

        #Prezzo del servizio di pernottamento
        prezzo_pernottamento = numero_notti * self.servizio_alloggio.prezzo * self.numero_persone

        #Prezzo del servizio di ristorazione
        prezzo_ristorazione = numero_notti * self.servizio_ristorazione.prezzo * self.numero_persone

        #Prezzo dei servizi aggiuntivi
        prezzo_servizi_aggiuntivi = 0
        for servizio_aggiuntivo in self.servizi_aggiuntivi:
            if servizio_aggiuntivo.nome == "Escursione turistica":
                prezzo_servizi_aggiuntivi = prezzo_servizi_aggiuntivi + (servizio_aggiuntivo.prezzo * self.numero_persone)
            else:
                prezzo_servizi_aggiuntivi = prezzo_servizi_aggiuntivi + (servizio_aggiuntivo.prezzo * self.numero_persone * numero_notti)

        return prezzo_ristorazione+prezzo_pernottamento+prezzo_servizi_aggiuntivi

