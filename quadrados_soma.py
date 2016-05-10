from collections import Counter

pokemon ={0:[0]}
def soma_quadrados(n):
    if n==0:
        return [0]
    quadrados=[]
    maximo=1
    while(maximo*maximo<=n):
        quadrados.append(maximo*maximo)
        maximo+=1
    while len(quadrados)>0:
        num=n

        quad=quadrados.copy()
        a=quad.pop()
        resp=[]
        while(num>0):
            if num in pokemon.keys() and num is not n:
                resp=resp+pokemon[num]
                num=0
            else:
                if len(quad)>0:
                    if num-a<0:
                       a=quad.pop()
                    else:
                        num-=a
                        resp.append(a)
                        if(num<quad[-1]):
                            a=quad.pop()
                else:
                    num-=a
                    resp.append(a)
        if n not in pokemon.keys():
            pokemon[n]=resp.copy()
        elif len(resp)<len(pokemon[n]):
            pokemon[n]=resp.copy()
        quadrados.pop()

    return pokemon[n]




import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_01(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_02(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_03(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_04(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_05(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))


    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
