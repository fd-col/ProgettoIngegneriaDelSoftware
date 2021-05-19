class ControlloreDipendente():
    def __init__(self, dipendente):
        self.model = dipendente

    def get_nome_dipendente(self):
        return self.model.nome

    def get_cognome_dipendente(self):
        return self.model.cognome

    def get_ruolo_dipendente(self):
        return self.model.ruolo

    def get_id_dipendente(self):
        return self.model.id

    def get_stipendio_dipendente(self):
        return self.model.stipendio