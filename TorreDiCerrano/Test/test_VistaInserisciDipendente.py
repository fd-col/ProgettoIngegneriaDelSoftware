from unittest import TestCase

from ListaDipendenti.views.VistaInserisciDipendente import VistaInserisciDipendente


class TestVistaInserisciDipendente(TestCase):

    def crea_campi(self):

        self.finestra_inserisci_dipendente = VistaInserisciDipendente(None, None)

        #Scrivo i campi del dipendente
        self.finestra_inserisci_dipendente.campo_nome.setText("Mario")
        self.finestra_inserisci_dipendente.campo_cognome.setText("Rossi")
        self.finestra_inserisci_dipendente.campo_ruolo.setText("Cuoco")
        self.finestra_inserisci_dipendente.campo_id.setText("12345")
        self.finestra_inserisci_dipendente.campo_stipendio.setText("2000")

    def test_conferma_inserimento(self):
        self.crea_campi()
        self.assertEqual(self.finestra_inserisci_dipendente.conferma_inserimento(), False)
        

    def test_controlla_id_libero(self):
        self.fail()
