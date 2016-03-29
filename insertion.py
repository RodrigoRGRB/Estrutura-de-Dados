import unittest

def insertion_sort(seq):
    '''
        mem O(1) pois só terá a sequencia e as variaveis
    Tempo de execução O(n²) pois possui um while dentro de outro while para percorrer a lista e realizar a ordenação
   '''
    if len(seq) <= 1:
        return seq
    else:
        listaOrd=0
        indice=0
        while indice<len(seq):
            indiceOrd=listaOrd
            if seq[indice]>seq[listaOrd]:
                ind+=1
                listaOrd+=1
            else:
                indice+=1
                listaOrd+=1
                while indiceOrd>0:
                    if seq[indiceOrd-1]>seq[indiceOrd]:
                        seq[indiceOrd-1],seq[indiceOrd]=seq[indiceOrd],seq[indiceOrd-1]
                    indiceOrd-=1

    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

if __name__ == '__main__':
    unittest.main()
