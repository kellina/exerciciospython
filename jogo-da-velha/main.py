# Exercício 02: Criar o jogo “JOGO DA VELHA”
# a) Serão dois jogadores
# b) O jogo pergunta onde você quer jogar e alternar entre os dois jogadores.
# c) A cada jogada, verifique se a posição esta livre.
# d) Apresentar no final se teve empate e/ou quem foi o jogador vencedor.
# Exemplo do jogo:
# X | 0 |
# ---+---+---
#   | X | X
# ---+---+---
#   |   | 0

# Exemplo das posições mapeadas para ajudar:
# 7 | 8 | 9
# ---+---+---
# 4 | 5 | 6
# ---+---+---
# 1 | 2 | 3

import time

def menu():
    print('BEM VINDO(A) AO JOGO DA VELHA')
    time.sleep(1)
    iniciar = 1
    while iniciar:
        iniciar = int(input('O que você deseja fazer? 1 - Jogar ou 0 - Sair \n'))
        time.sleep(1)

        if iniciar:
            jogar()
        else:
            print('Até a próxima!')


tabuleiro = [[0,0,0],
            [0,0,0],
            [0,0,0]]

def exibeTabuleiro():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                print('_', end=' ')
            elif tabuleiro[i][j] == 1:
                print('X', end=' ')
            elif tabuleiro[i][j] == -1:
                print('O', end=' ')
        print()

def ganhou():
    for i in range(3):
        soma = tabuleiro[i][0] + tabuleiro[i][1] + tabuleiro[i][2]
        if soma == 3 or soma == -3:
            return True
    
    for j in range(3):
        soma = tabuleiro[0][j] + tabuleiro[1][j] + tabuleiro[2][j]
        if soma == 3 or soma == -3:
            return True

    diagonal1 = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    diagonal2 = tabuleiro[2][0] + tabuleiro[1][1] + tabuleiro[0][2]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return True
    
    return False

def jogar():
    jogadas = 0
    print('Esse é o gabarito de posições:')
    print(' 1 2 3\n 4 5 6 \n 7 8 9')
    global tabuleiro 
    tabuleiro = [[0,0,0],
                [0,0,0],
                [0,0,0]]
    
    while not ganhou():
        if jogadas == 9:
            print('Os jogadores empataram.')
            break
        print('\nJogador ', jogadas % 2 + 1)
        print('--------------')
        exibeTabuleiro()
        posicao  = int(input('\nEm qual posição deseja jogar? [1 a 9]:'))
        linha = (posicao - 1) // 3
        coluna = (posicao -1) % 3
        if tabuleiro[linha][coluna] == 0:
            if(jogadas % 2 + 1)== 1:
                tabuleiro[linha][coluna] = 1
            else:
                tabuleiro[linha][coluna] = -1
        else:
            print('Essa posição não está livre')
            jogadas -= 1

        if ganhou():
            print('O jogador ',jogadas % 2 + 1,' ganhou!')
            print('Parabéns!')

        jogadas +=1

menu()