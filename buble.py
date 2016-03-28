import unittest

'''
Para tempo de execução é O(n^2) pois tem um for dentro de um outro for que percorre a sequencia
---------------------------------------------------------------------------------------------------
Memoria é O(1) pois irá possuir a sequencia e uma variavel como flag
---------------------------------------------------------------------------------------------------
Existe se caso colocarmos um flag, se caso a sequencia já fique em ordem não haver a necessidade de verificar ela por completo
---------------------------------------------------------------------------------------------------
Bom no melhor caso (sequencia ordenada)mesmo assim ele teria que percorrer para verificar a sequencia porem nao teria
que mudar nenhum valo
'''
def bubble_sort(seq):
    pokemon = True
    for i in range(len(seq) - 1):
        for j in range(len(seq)-1):
            if seq[j]>seq[j+1]:
                pokemon = False
                seq[j],seq[j+1] = seq[j+1],seq[j]
        if (pokemon):
            print("Tá tudo tranquilo, Favorável")
            break

    return seq
    pass


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()