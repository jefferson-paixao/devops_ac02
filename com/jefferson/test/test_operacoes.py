from unittest import TestCase
from com.jefferson.operacoes import Operacoes

class TestOperacoes(TestCase):
    def setUp(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.multiplicacao(5,5),25,"Deveria ser 25!")
