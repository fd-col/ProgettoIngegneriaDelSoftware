class Servizio():
    def __init__(self, nome, tipo, prezzo):
        super(Servizio, self).__init__()
        self.nome = nome
        self.tipo = tipo
        self.prezzo = prezzo
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile = False