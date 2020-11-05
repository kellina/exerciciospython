# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhece(self, ano):
        self.idade += ano
        
    def engorda(self, peso):
        self.peso  += peso

    def emagrece(self, peso):
        self.peso  -= peso
        
    def cresce(self):
        if self.idade < 21:
            self.altura += 0.05
       
pessoa1 = Pessoa("Ana", 15, 40, 1.55)
print("A pessoa 1 chama-se", pessoa1.nome, ", tem", pessoa1.idade, "anos, pesa", pessoa1.peso, "kg, e tem", pessoa1.altura, "m.")
pessoa1.envelhece(2)
pessoa1.cresce()
print("A", pessoa1.nome, "agora tem", pessoa1.idade, "anos, e está com", pessoa1.altura, "m.")

pessoa2 = Pessoa("Pedro", 22, 65, 1.70)
pessoa2.engorda(4)
print(pessoa2.nome, "tem",pessoa2.idade, "anos, está pesando", pessoa2.peso, "kg, e tem", pessoa2.altura, "m.")