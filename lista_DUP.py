import unittest

class ListaVaziaErro(Exception):
    pass

class Noh():
    def __init__(self,valor,esquerdo=None,direito=None):
        self.valor=valor
        self.direito=direito
        self.esquerdo=esquerdo

class Lista():
    def __init__(self):
        self.tam=0
        self.primeiro=None
        self.ultimo=None

    def adicionar(self,valor):
        noh=Noh(valor)
        if self.tam==0:
            self.primeiro=noh
            self.tam=self.tam+1
        else:
            ultimo=self.ultimo
            ultimo.direito=noh
            noh.esquerdo=ultimo
            self.tam=self.tam+1
        self.ultimo=noh

    def remover(self):
        try:
            if (self.tam==1):
                self.ultimo=None
                self.primeiro=None
                self.tam=0
                return self.tam
            else:
                anterior=self.ultimo
                anterior=anterior.esquerdo
                anterior.direito=None
                self.ultimo=anterior
                self.tam=self.tam-1
                return self.tam
        except AttributeError:
            raise ListaVaziaErro

    def adicionar_a_esquerda(self,valor):
        noh=Noh(valor)
        if self.tam==0:
            self.primeiro=noh
            self.tam=self.tam+1
            self.ultimo=noh
        else:
            primeiro=self.primeiro
            primeiro.esquerdo=noh
            noh.direito=primeiro
            self.tam=self.tam+1
        self.primeiro=noh

    def remover_a_esquerda(self):
        try:
            if self.tam==1 :
                self.ultimo=None
                self.primeiro=None
                self.tam=0
                return 0
            else:
                direito=self.primeiro.direito
                self.primeiro=direito
                direito.esquerdo=None
                self.tam-=1
                return 0
        except AttributeError:
            raise ListaVaziaErro

    def __iter__(self):
        noh_atual=self.primeiro
        while noh_atual is not None:
            yield noh_atual.valor
            noh_atual=noh_atual.direito


class NohTestes(unittest.TestCase):
    def test_init_com_valores_padrao(self):
        noh = Noh(4)
        self.assertEqual(4, noh.valor)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)

    def test_init_com_no_esquerdo(self):
        esquerdo = Noh(1)
        noh = Noh(2, esquerdo)
        self.assertEqual(esquerdo, noh.esquerdo)
        self.assertIsNone(noh.direito)
        noh3 = Noh(3, esquerdo=esquerdo)
        self.assertEqual(esquerdo, noh3.esquerdo)
        self.assertIsNone(noh3.direito)

    def test_init_com_no_direito(self):
        direito = Noh(1)
        noh = Noh(2, direito=direito)
        self.assertEqual(direito, noh.direito)
        self.assertIsNone(noh.esquerdo)

    def test_init_com_no_esquerdo_e_direito(self):
        esquerdo = Noh(1)
        direito = Noh(2)
        noh = Noh(3, esquerdo, direito)
        self.assertEqual(esquerdo, noh.esquerdo)
        self.assertEqual(direito, noh.direito)


class ListaTestes(unittest.TestCase):
    def test_init(self):
        lista = Lista()
        self.assertEquals(0, lista.tam)
        self.assertIsNone(lista.primeiro)
        self.assertIsNone(lista.ultimo)

    def test_adicionar_primeiro(self):
        lista = Lista()
        lista.adicionar(0)
        self.assertEqual(1, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(0, primeiro.valor)
        self.assertEqual(primeiro, lista.ultimo)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(primeiro.direito)

    def test_adicionar_segundo(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        self.assertEqual(2, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(0, primeiro.valor)
        ultimo = lista.ultimo
        self.assertEqual(1, ultimo.valor)
        self.assertEqual(primeiro, ultimo.esquerdo)
        self.assertEqual(ultimo, primeiro.direito)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

    def test_adicionar_terceiro(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        lista.adicionar(2)
        self.assertEqual(3, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(0, primeiro.valor)
        ultimo = lista.ultimo
        segundo = primeiro.direito
        self.assertEqual(1, segundo.valor)
        self.assertEqual(2, ultimo.valor)

        self.assertEqual(primeiro, segundo.esquerdo)

        self.assertEqual(segundo, ultimo.esquerdo)
        self.assertEqual(ultimo, segundo.direito)

        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

    def test_adicionar_primeiro_a_esquerda(self):
        lista = Lista()
        lista.adicionar_a_esquerda(0)
        self.assertEqual(1, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(0, primeiro.valor)
        self.assertEqual(primeiro, lista.ultimo)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(primeiro.direito)

    def test_adicionar_segundo_a_esquerda(self):
        lista = Lista()
        lista.adicionar_a_esquerda(0)
        lista.adicionar_a_esquerda(1)
        self.assertEqual(2, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(1, primeiro.valor)
        ultimo = lista.ultimo
        self.assertEqual(0, ultimo.valor)
        self.assertEqual(primeiro, ultimo.esquerdo)
        self.assertEqual(ultimo, primeiro.direito)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

    def test_adicionar_terceiro(self):
        lista = Lista()
        lista.adicionar_a_esquerda(0)
        lista.adicionar_a_esquerda(1)
        lista.adicionar_a_esquerda(2)
        self.assertEqual(3, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(2, primeiro.valor)
        ultimo = lista.ultimo
        segundo = primeiro.direito
        self.assertEqual(1, segundo.valor)
        self.assertEqual(0, ultimo.valor)

        self.assertEqual(primeiro, segundo.esquerdo)

        self.assertEqual(segundo, ultimo.esquerdo)
        self.assertEqual(ultimo, segundo.direito)

        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

    def test_remover_lista_vazia(self):
        lista = Lista()
        self.assertRaises(ListaVaziaErro, lista.remover)

    def test_remover_lista_1_elemento(self):
        lista = Lista()
        lista.adicionar(0)
        self.assertEqual(0, lista.remover())
        self.assertEqual(0, lista.tam)
        self.assertIsNone(lista.primeiro)
        self.assertIsNone(lista.ultimo)

    def test_remover_lista_2_elementos(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        self.assertEqual(1, lista.remover())
        self.assertEqual(1, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(primeiro, lista.ultimo)
        self.assertEqual(0, primeiro.valor)
        self.assertIsNone(primeiro.direito)
        self.assertIsNone(primeiro.esquerdo)

    def test_remover_lista_3_elementos(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        lista.adicionar(2)
        self.assertEqual(2, lista.remover())
        self.assertEqual(2, lista.tam)
        primeiro = lista.primeiro
        ultimo = lista.ultimo
        self.assertEqual(ultimo, primeiro.direito)
        self.assertEqual(primeiro, ultimo.esquerdo)
        self.assertEqual(0, primeiro.valor)
        self.assertEqual(1, ultimo.valor)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

    def test_remover_a_esquerda_lista_vazia(self):
        lista = Lista()
        self.assertRaises(ListaVaziaErro, lista.remover_a_esquerda)

    def test_remover_a_esquerda_lista_1_elemento(self):
        lista = Lista()
        lista.adicionar(0)
        self.assertEqual(0, lista.remover_a_esquerda())
        self.assertEqual(0, lista.tam)
        self.assertIsNone(lista.primeiro)
        self.assertIsNone(lista.ultimo)

    def test_remover_a_esquerda_lista_2_elementos(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        self.assertEqual(0, lista.remover_a_esquerda())
        self.assertEqual(1, lista.tam)
        primeiro = lista.primeiro
        self.assertEqual(primeiro, lista.ultimo)
        self.assertEqual(1, primeiro.valor)
        self.assertIsNone(primeiro.direito)
        self.assertIsNone(primeiro.esquerdo)

    def test_remover_a_esquerda_lista_3_elementos(self):
        lista = Lista()
        lista.adicionar(0)
        lista.adicionar(1)
        lista.adicionar(2)
        self.assertEqual(0, lista.remover_a_esquerda())
        self.assertEqual(2, lista.tam)
        primeiro = lista.primeiro
        ultimo = lista.ultimo
        self.assertEqual(ultimo, primeiro.direito)
        self.assertEqual(primeiro, ultimo.esquerdo)
        self.assertEqual(1, primeiro.valor)
        self.assertEqual(2, ultimo.valor)
        self.assertIsNone(primeiro.esquerdo)
        self.assertIsNone(ultimo.direito)

    def test_iterar_lista_vazia(self):
        lista = Lista()
        for i in lista:
            self.fail('Nao deveria executar nada')

    def test_iterar_lista_nao_vazia(self):
        lista = Lista()
        numeros = list(range(3))
        for n in numeros:
            lista.adicionar(n)

        for i, elemento_da_lista in zip(range(3), lista):
            self.assertEqual(i, elemento_da_lista)


if __name__ == '__main__':
    unittest.main()
