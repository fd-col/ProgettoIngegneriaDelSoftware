from unittest import TestCase

from ListaDipendenti.model.ListaDipendenti import ListaDipendenti


class TestListaDipendenti(TestCase):

    def crea_ambiente_test(self):
        self.lista_dipendenti = ListaDipendenti()

    def test_rimuovi_dipendente_by_id(self):
        self.crea_ambiente_test()
        self.assertFalse(self.lista_dipendenti.rimuovi_dipendente_by_id(00000))

    def test_get_dipendente_by_id(self):
        self.crea_ambiente_test()
        self.assertIsNone(self.lista_dipendenti.get_dipendente_by_id(00000))

    def test_get_lista_dipendenti(self):
        self.crea_ambiente_test()
        self.assertEqual(self.lista_dipendenti.get_lista_dipendenti(), [])