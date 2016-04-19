import unittest

class PilhaVaziaErro(Exception):
    pass

class Pilha():
    def __init__(self):
        self.lista=[]

    def topo(self):
        if self.lista:
            return self.lista[-1]
        raise PilhaVaziaErro()

    def vazia(self):
        return not bool(self.lista)

    def empilhar(self,valor):
        self.lista.append(valor)

    def desempilhar(self):
        try:
            return self.lista.pop()
        except IndexError:
            raise PilhaVaziaErro

def esta_balanceada(expressao):
    """
    Tempo: O(n)
    Memoria: O(n)
    """
    if expressao:
        pilha=Pilha()
        if expressao[0] in '}])':
            return False
        for a in expressao:
            if a in '{[(':
                pilha.empilhar(a)
            elif a in '}])':
                if a == '}' and pilha.desempilhar()!='{':
                    return False
                elif a == ']' and pilha.desempilhar()!='[':
                    return False
                elif a == ')' and pilha.desempilhar()!='(':
                    return False
        if pilha.vazia():
            return True
        return False
    else:
        return True

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
