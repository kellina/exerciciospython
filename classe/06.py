# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    def __init__(self, num_canal, volume):
        self.num_canal = num_canal
        self.volume = volume
    
    def mostraCanal(self):
        self.num_canal

    def mostraVolume(self):
        self.volume

    def mudaCanal(self, num):
        num = int(input("Digite o numero do canal:"))
        if self.num_canal > 0 and self.num_canal <= 100:
            self.num_canal = num
        else:
            print("Canal inválido! O canal deve estar entre 0 e 100.")

    def mudaVolume(self, num):
        num = int(input("Digite o numero do volume:"))
        if self.volume > 0 and self.volume <= 100:
            self.volume = num
        else:
            print("O volume deve estar entre 0 e 100!")

tv1 = TV(5, 10)
print(tv1.mostraCanal(), tv1.mostraVolume())


