from unittest import TestCase

from ListaClienti.model.ListaClienti import ListaClienti


class TestListaClienti(TestCase):

    def crea_ambiente_test(self):
        self.lista_clienti = ListaClienti()


    def test_rimuovi_cliente_by_email(self):
        self.crea_ambiente_test()
        self.assertFalse(self.lista_clienti.rimuovi_cliente_by_email("aaaaa"))

    def test_get_cliente_by_email(self):
        self.crea_ambiente_test()
        self.assertIsNone(self.lista_clienti.get_cliente_by_email("aaaaa"))

    def test_get_lista_clienti(self):
        self.crea_ambiente_test()
        self.assertEqual(self.lista_clienti.get_lista_clienti(),[])
