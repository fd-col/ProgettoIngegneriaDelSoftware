from unittest import TestCase

from Cliente.model.Cliente import Cliente
from ListaClienti.model.ListaClienti import ListaClienti


class TestListaClienti(TestCase):

    def crea_ambiente_test(self):
        self.lista_clienti = ListaClienti()
        cliente = Cliente("Mario", "Rossi", "01/01/2000", "Via Garibaldi", "123456789", "mario@rossi.it", "abcd")
        self.lista_clienti.aggiungi_cliente(cliente)


    def test_rimuovi_cliente_by_email(self):
        self.crea_ambiente_test()
        self.assertFalse(self.lista_clienti.rimuovi_cliente_by_email("aaaaa"))
        self.assertTrue(self.lista_clienti.rimuovi_cliente_by_email("mario@rossi.it"))

    def test_get_cliente_by_email(self):
        self.crea_ambiente_test()
        self.assertIsNone(self.lista_clienti.get_cliente_by_email("aaaaa"))
        self.assertIsNotNone(self.lista_clienti.get_cliente_by_email("mario@rossi.it"))

    def test_get_lista_clienti(self):
        self.crea_ambiente_test()
        self.assertNotEqual(self.lista_clienti.get_lista_clienti(),[])
