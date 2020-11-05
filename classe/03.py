# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    
    def mudaValorLados(self, base, altura):
        self.base = base
        self.altura = altura
    
    def retornaValorlados(self):
        return self.base, self.altura

    def calculaArea(self):
        area = self.base * self.altura
        return area
    
    def calculaPerimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro

ladoA = int(input("Informe a medida do lado A do local: "))
ladoB = int(input("Informe a medida do lado B do local: "))

piso = Retangulo(ladoA, ladoB)
print("A quantidade necessaria de piso no local é de", piso.calculaArea(), "m2")
print("A quantidade necessaria de rodapé no local é de", piso.calculaPerimetro(), "m")
