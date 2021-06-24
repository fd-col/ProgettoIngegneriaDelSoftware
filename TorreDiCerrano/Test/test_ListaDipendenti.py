from unittest import TestCase

from Dipendente.model.Dipendente import Dipendente
from ListaDipendenti.model.ListaDipendenti import ListaDipendenti


class TestListaDipendenti(TestCase):

    def crea_ambiente_test(self):
        self.lista_dipendenti = ListaDipendenti()
        dipendente = Dipendente("Tom", "Bino", "Manutenzione", 12345, 1000)
        self.lista_dipendenti.aggiungi_dipendente(dipendente)

    def test_rimuovi_dipendente_by_id(self):
        self.crea_ambiente_test()
        self.assertFalse(self.lista_dipendenti.rimuovi_dipendente_by_id(00000))
        self.assertTrue(self.lista_dipendenti.rimuovi_dipendente_by_id(12345))

    def test_get_dipendente_by_id(self):
        self.crea_ambiente_test()
        self.assertIsNone(self.lista_dipendenti.get_dipendente_by_id(00000))
        self.assertIsNotNone(self.lista_dipendenti.get_dipendente_by_id(12345))

    def test_get_lista_dipendenti(self):
        self.crea_ambiente_test()
        self.assertNotEqual(self.lista_dipendenti.get_lista_dipendenti(), [])