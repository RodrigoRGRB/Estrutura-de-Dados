# -*- coding: utf-8 -*-

# Exercício de avaliação de expressão aritmética.
# Só podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ter análise de tempo e espaço para função avaliação

from pilha import Pilha
from fila import Fila

class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass


def analise_lexica(expressao):
    """
    Executa análise lexica transformando a expressao em fila de objetos:
    Transforma inteiros em ints
    Flutuantes em floats
    e verificar se demais caracteres são validos: +-*/(){}[]
    :param expressao: string com expressao a ser analisada
    :return: fila com tokens
    """
    fila = Fila()

    #Aqui ficam os numeros e o Token
    nt = R"0123456789.-+*/{}[]()"

    if expressao:

        valor = ''

        for a in expressao:
            if a in nt:
                if a in '.-+*/{}[]()':
                    if valor:
                        fila.enfileirar(valor)
                        valor = ''
                    fila.enfileirar(a)
                else:
                    valor = valor + a
            else:
                raise ErroLexico()

        if valor:
            fila.enfileirar(valor)

    return fila


def analise_sintatica(fila):
    """
    Função que realiza analise sintática de tokens produzidos por analise léxica.
    Executa validações sintáticas e se não houver erro retorn fila_sintatica para avaliacao

    :param fila: fila proveniente de análise lexica
    :return: fila_sintatica com elementos tokens de numeros
    """

    if fila.__len__():

        # Cria um novo objeto fila para adicionar os valores
        fila_sintetica = Fila()

        #Variavel de apoio para juntar a string
        valor = ''

        for a in range(fila.__len__()):

            if fila._deque[a] in '-+/*(){}[]':
                if valor:
                    if '.' in valor:
                        fila_sintetica.enfileirar(float(valor))
                    else:
                        fila_sintetica.enfileirar(int(valor))


                valor = ''
                fila_sintetica.enfileirar(fila._deque[a])
            else:
                valor = valor + fila._deque[a]

        if valor:
            if '.' in valor:
                fila_sintetica.enfileirar(float(valor))
            else:
                fila_sintetica.enfileirar(int(valor))

        return fila_sintetica
    else:
        raise ErroSintatico


def avaliar(expressao):
    """
    Função que avalia expressão aritmetica retornando se valor se não houver nenhum erro
    :param expressao: string com expressão aritmética
    :return: valor númerico com resultado

    tempo: O(n)
    Memoria: O(n)
    """

    if expressao:

        fila = analise_sintatica(analise_lexica(expressao))

        teste = fila.__len__()
        if teste == 1:
            return fila.primeiro()
        else:
            pilha = Pilha()

            for i in range(fila.__len__()):

                pilha.empilhar(fila._deque[i])

                if pilha.__len__() >= 3 and str(pilha.topo()) not in '-+*/(){}[]':

                    valor = pilha.topo()
                    pilha.desempilhar()

                    if pilha.topo() == '+':
                        pilha.desempilhar()
                        valor = pilha.desempilhar() + valor
                        pilha.empilhar(valor)
                        valor = ''
                    elif pilha.topo() == '-':
                        pilha.desempilhar()
                        valor = pilha.desempilhar() - valor
                        pilha.empilhar(valor)
                        valor = ''
                    elif pilha.topo() == '*':
                        pilha.desempilhar()
                        valor = pilha.desempilhar() * valor
                        pilha.empilhar(valor)
                        valor = ''
                    elif pilha.topo() == '/':
                        pilha.desempilhar()
                        valor = pilha.desempilhar() / valor
                        pilha.empilhar(valor)
                        valor = ''
                    else:
                        pilha.empilhar(valor)

                elif str(pilha.topo()) in ')}]' and i == fila.__len__() - 1:
                    pilha.desempilhar()


                    while len(pilha) > 1:

                        if str(pilha.topo()) not in '-+*/(){}[]':
                            valor = pilha.topo()
                            pilha.desempilhar()

                            if pilha.topo() == '+':
                                pilha.desempilhar()
                                valor = pilha.desempilhar() + valor
                                pilha.empilhar(valor)
                                valor = ''
                            elif pilha.topo() == '-':
                                pilha.desempilhar()
                                valor = pilha.desempilhar() - valor
                                pilha.empilhar(valor)
                                valor = ''
                            elif pilha.topo() == '*':
                                pilha.desempilhar()
                                valor = pilha.desempilhar() * valor
                                pilha.empilhar(valor)
                                valor = ''
                            elif pilha.topo() == '/':
                                pilha.desempilhar()
                                valor = pilha.desempilhar() / valor
                                pilha.empilhar(valor)
                                valor = ''
                            elif str(pilha.topo()) in '(){}[]':
                                pilha.desempilhar()
                                pilha.empilhar(valor)
                            else:
                                pilha.empilhar(valor)
                        else:
                            pilha.desempilhar()


            return pilha.topo()

    raise ErroSintatico()


import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],[e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()
