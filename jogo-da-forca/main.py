# Utilizando LAÇOS DE REPETIÇÃO / FUNÇÃO / STRINGS
# Exercício 01: Criar o “JOGO DA FORCA”:
# a) Criar uma lista de palavras para o jogo.
# b) O jogo pergunta um número e assim é escolhido a palavra pelo índice.
# c) Utilize uma lista de strings para desenhar o boneco da meu_jogo. Assim fica mais fácil caso o jogador erre para controlar cada parte.
# d) Apresentar a palavra no final caso o jogador perca.

import time
from jogo import Jogo

palavras = ['banana', 'cachorro', 'geladeira', 'casa', 'montanha', 'chuva', 'abacaxi', 'elefante', 'janela', 'bicicleta']
numero = int(input('Para selecionar a palavra, informe um número de 1 a 10:'))
palavra_escolhida = palavras[numero - 1]
meu_jogo = Jogo(palavra_escolhida)
meu_jogo.gerarPainel()


nome = input('Qual o seu nome:')
print('Olá', nome.capitalize(), 'pronto para jogar o Jogo da Forca?!')
time.sleep(1)
print('O objetivo do jogo é adivinhar a palavra secreta')
time.sleep(1)


while True:
    meu_jogo.imprimirPainel()
    meu_jogo.imprimirForca()

    print('Letras Usadas:', meu_jogo.letrasUsadas)
    letra = input('Digite uma letra: ')
    

    meu_jogo.verificarLetra(letra)
    ganhou = meu_jogo.verificarGanhou()
    perdeu = meu_jogo.verificarPerdeu()

    if ganhou:
        print('Parabéns você acertou!!!')
        meu_jogo.imprimirPainel()
        meu_jogo.imprimirForca()
        # jogar_novamente = input('Deseja jogar novamente? [s/n]')
        # if jogar_novamente == 'n':
        break
        
    if perdeu:
        print('Não foi desta vez!!!')
        meu_jogo.revelarPalavra()
        meu_jogo.imprimirPainel()
        meu_jogo.imprimirForca()
        break
    