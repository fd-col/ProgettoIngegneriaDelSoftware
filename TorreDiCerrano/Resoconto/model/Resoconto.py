class Resoconto:

    def __init__(self):
        super(Resoconto, self).__init__()

    def calcola_costo_dipendenti(self, data_inizio, data_fine, lista_dipendenti):
        num_giorni = (data_fine-data_inizio).days
        num_mesi = num_giorni/30.0

        costo_dipendenti = 0.0
        for dipendente in lista_dipendenti:
            costo_dipendenti = costo_dipendenti + dipendente.stipendio*num_mesi

        return  costo_dipendenti

    #Calcola i ricavi dalle prenotazioni e ritorna un array dai 3 float:
    #0) Ricavi dal servizio di alloggio
    #1) Ricavi dal servizio di ristorazione
    #2) Ricavi dai servizi aggiuntivi
    def calcola_ricavi_prenotazioni(self, data_inizio, data_fine, lista_prenotazioni):
        array_ricavi = []
        lista_prenotazioni_filtrata = []

        for prenotazione in lista_prenotazioni:
            if prenotazione.data_inizio >= data_inizio and prenotazione.data_fine <= data_fine:
                lista_prenotazioni_filtrata.append(prenotazione)
        ricavi_totali_alloggio = 0.0
        ricavi_totali_ristorazione = 0.0
        ricavi_totali_servizi_aggiuntivi = 0.0

        for prenotazione in lista_prenotazioni_filtrata:
            ricavi_servizi_aggiuntivi = 0.0
            for servizio_aggiuntivo in prenotazione.servizi_aggiuntivi:
                ricavi_servizi_aggiuntivi = ricavi_servizi_aggiuntivi + servizio_aggiuntivo.prezzo

            ricavi_alloggio = 0.0
            ricavi_ristorazione = 0.0
            num_giorni_prenotazione = (prenotazione.data_fine - prenotazione.data_inizio).days

            ricavi_alloggio = num_giorni_prenotazione*prenotazione.servizio_alloggio.prezzo
            ricavi_ristorazione = num_giorni_prenotazione*prenotazione.servizio_ristorazione.prezzo

            ricavi_totali_alloggio = ricavi_totali_alloggio + ricavi_alloggio
            ricavi_totali_ristorazione = ricavi_totali_ristorazione + ricavi_ristorazione
            ricavi_totali_servizi_aggiuntivi = ricavi_totali_servizi_aggiuntivi + ricavi_servizi_aggiuntivi

        array_ricavi.append(ricavi_totali_alloggio)
        array_ricavi.append(ricavi_totali_ristorazione)
        array_ricavi.append(ricavi_totali_servizi_aggiuntivi)

        return array_ricavi
