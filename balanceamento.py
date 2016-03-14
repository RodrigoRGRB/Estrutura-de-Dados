import unittest

class PilhaVaziaErro(Exception):
    pass

class Pilha():
    def __init__(self):
        self.lista = []

    def vazio (self):
        return bool(self.lista)

    def topo (self):
        if self.lista:
            return self.lista [-1]

        raise PilhaVaziaErro()

    def empilhar(self, valor):
        return self.lista.append(valor)

    def desempilhar (self):
        try:
            return self.lista.pop()
        except:
            raise PilhaVaziaErro()

    def esta_balanceada(self):
        y = 0;
        for k in range lista.(y):
            if lista.(y)== '('
                lista.append(")")
            if lista.(y) == '{'
                lista.append("}")
            if lista.(y)==("[")
                lista.append("]")





class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))

