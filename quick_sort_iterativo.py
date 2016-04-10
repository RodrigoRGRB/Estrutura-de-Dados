import unittest

def _quick_recursivo(seq, inicio, final):
    if inicio >= final:
        return seq
    else:
        indice_pivot = final
        pivot = seq[indice_pivot]
        i_menor = inicio
        i_maior = final
        while(i_menor<i_maior):
            if(seq[i_menor]<=pivot):
                i_menor+=1
            elif(seq[i_maior]>=pivot):
                i_maior-=1
            else:
                seq[i_menor],seq[i_maior]=seq[i_maior],seq[i_menor]
        seq[i_menor],seq[indice_pivot]=seq[indice_pivot],seq[i_menor]
        indice_pivot=i_menor

        _quick_recursivo(seq,inicio,indice_pivot-1)
        _quick_recursivo(seq,indice_pivot+1,final)

        return seq


def quick_sort(seq):
    return _quick_recursivo(seq, 0, len(seq) - 1)


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
