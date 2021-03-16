# “BICHINHO VIRTUAL”
# Crie uma classe que modele um Tamagotshi (Bichinho Eletrônico):
# a) Atributos: Nome, Fome, Saúde e Idade
# OBS: o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, 
# então não devemos criar um atributo para armazenar esta informação porque ela pode ser calculada a qualquer momento.
# c) Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e 
# por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
# d) Crie uma "porta escondida" no programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. 
# Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. 

from random import randrange
import threading
import time
from time import thread_time
from colorama import init, Fore

init() #iniciar colorama de cor
class Tamagotchi:
    vocab = ['Olá!', 'Tudo bem?', 'Huurruu!', 'Oba!', 'Legal!']
    def __init__(self, nome, fome = 0, saude = 100, idade = 0, tedio = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio
        self.vocab = self.vocab[:]
        # Objeto threading que controla a execução em paralelo
        self.run = True
        self.tempo = threading.Thread(target=self.__temporizador__)
        self.tempo.start()

    def alterarNome(self, nome):
        self.nome = nome

    def vivo(self):
        return self.fome <= 10 and self.saude > 0

    def alterarFome(self, fome):
        if fome == 9:
            print(Fore.CYAN + 'Alimente seu bichinho urgente!')
        elif fome > 10:
            print('Seu bichinho morreu de fome')

    def alterarSaude(self, saude):
        self.saude = saude

    def alterarIdade(self, idade):
        self.idade = idade
     
    def retornaNome(self):
        return self.nome

    def retornaFome(self):
        return self.fome
    
    def retornaSaude(self):
        return self.saude

    def retornaIdade(self):
        return self.idade

    def __str__(self):
        return Fore.CYAN + 'Nome: ' + self.nome + '\nIdade: ' + str(self.idade) + '\nFome: ' + str(self.fome) + '\nHumor: ' + self.humor() + '\nTédio: ' + str(self.tedio)

    # temporizador feito a partir da thread. Passa o tempo automaticamente, incrementando o tédio, a fome e a idade
    # cada ciclo do run demora 12 segundos (1 dia no mundo virtual). A idade só aumenta a cada 20 ciclos de 12s. Foi o que eu quis representar 1 ano de vida dele, 260s.
    def __temporizador__(self):
        ciclos = 0
        while self.run:
            time.sleep(12)
            self.fome += 1
            self.tedio += 1
            if ciclos % 20 == 0:
                self.idade += 1
            ciclos += 1
            if not self.vivo():
                self.run = False
                print('Jogo finalizado! Seu bichinho morreu de fome')
            
    # Humor eh uma relação entre fome e saúde, então se ele tem fome é claro que vai ficar mal humorado e se estiver doente idem.
    # Os valores para fome e saúde escolhi que variassem de 0 a 10.
    # Esses dois atributos tb interferem na sobrivencia do bichinho (def vivo)
    def humor(self):
        if self.fome <= 3 and self.saude >= 3:
            return 'Feliz!'
        elif self.fome > 3 and self.saude > 3:
            return 'Faminto!' + '\nPor favor me alimente!'
    
    def tenhoTedio(self):
        if self.tedio <= 5:
            return 'Estou tão feliz! Adoro brincar!'
        elif self.tedio > 5:
            return 'Estou entediado! Vamos brincar?'

        
    def alimentar(self):
        if self.vivo():
            refeicao = int(input('Quanto de comida você quer me dar? [1 a 9]'))
            print(Fore.CYAN + '***crunch***\n mmmmm. Obrigada!')
            self.fome -= refeicao
            if self.fome < 0:
                self.fome = 0
            # O valor da fome é decrementado a medida que ele recebe refeicao.  
            print(Fore.CYAN + 'Estou cheio!')

    # Os valores de alimentar e brincar afetem  os níveis de fome e tédio.
    # Quanto mais eu brinco, mais fome sinto. A fome é incrementada na metade da brincadeira, senão ele morre mais rápido de fome.
    # Quanto mais eu brinco, menos tédio sinto.  
    def brincar(self):
        if self.vivo():
            tempo_brincadeira = int(input('Por quanto tempo você quer brincar comigo? [1 a 5 seg]'))
            print(Fore.CYAN + 'Wiiiiii!!!!\n ^_^ Obrigada por brincar comigo ^_ ^')
            self.fome += tempo_brincadeira // 2
            if self.fome < 0:
                self.fome = 0
            self.tedio -= tempo_brincadeira
            if self.tedio < 0:
                self.tedio = 0

    def falar(self):
        if self.vivo():
            print(Fore.CYAN + 'Eu sou um bichinho virtual chamado', self.nome, '.')
            print(Fore.GREEN+ self.vocab[randrange(len(self.vocab))])
    # O vocab[randrange] pega valores aleatórios definidos no inicio do programa.

  
def main():
    print(Fore.RED)
    nome_bichinho = input('Qual o nome do seu bichinho virtual? ' + Fore.GREEN)

    meu_bichinho = Tamagotchi(nome_bichinho)
    input(Fore.RED + 'Olá! Eu sou ' + meu_bichinho.nome + ', sou novo por aqui.' + '\nPressione enter para começar' + Fore.GREEN)

    escolha = None
    while escolha != 0 and meu_bichinho.vivo():
        print(Fore.RED + """ *** INTERAJA COM SEU BICHINHO *** 
            1 - Alimente seu bichinho
            2 - Fale com seu bichinho
            3 - Brinque com seu bichinho
            4 - Altere o nome do seu bichinho
            0 - Sair
        """)

        escolha = int(input(Fore.RED + 'Escolha uma opção acima: [0 a 4] ' + Fore.GREEN))
        if escolha == 0:
            print('Até Logo!')
        elif escolha == 1:
            meu_bichinho.alimentar()
        elif escolha == 2:
            meu_bichinho.falar()
        elif escolha == 3:
            meu_bichinho.brincar()
        elif escolha == 4:
            meu_bichinho.alterarNome(input('Que nome você que dar ao seu amiguinho? '))
            print('Meu nome é ', meu_bichinho.retornaNome())
        #opção secreta -> metodo especial str
        elif escolha == 9:
            print(meu_bichinho)
        else:
            print('Desculpe, essa não é uma opção válida!')
    meu_bichinho.run = False
        
main()