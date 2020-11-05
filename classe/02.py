# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudaValorLado(self, lado):
        self.lado = lado
        
    def retornaValorLado(self):
        return self.lado

    def calculaArea(self):
        area = self.lado ** 2
        return area

quadrado1 = Quadrado(8)
print(quadrado1.retornaValorLado())
quadrado2 = Quadrado(10)
print(quadrado2.retornaValorLado())
quadrado2.mudaValorLado(12)
print(quadrado2.retornaValorLado())
print(quadrado2.calculaArea())

