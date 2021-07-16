class Servizio:

    def __init__(self, nome, tipo, prezzo, numero_persone_max=None, disponibilita_giornaliera=None):
        super(Servizio, self).__init__()
        self.nome = nome
        self.tipo = tipo
        self.prezzo = prezzo
        self.numero_persone_max = numero_persone_max
        self.disponibilita_giornaliera = disponibilita_giornaliera

    def __eq__(self, other):
        return self.nome == other.nome
