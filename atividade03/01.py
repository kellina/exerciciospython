# ------LAÇOS DE REPETIÇÃO ------
# Questão 01 - Num campeonato europeu de volleyball, se inscreveram 30 países.
# Sabendo-se que na lista oficial de cada país consta, além de outros dados, peso e idade
# de 12 jogadores, criar um algoritmo que apresente as seguintes informações:
# a) o peso médio e a idade média de cada um dos times;
# b) o peso médio e a idade média de todos os participantes.

from random import randint

peso_total = 0
idade_total = 0
peso_total_time = 0
idade_total_time = 0
media_peso_time = [] # só consegui apresentar 30 pesos na forma de lista, senão teria 30 prints de média de pesos
media_idade_time = []

for times in range(30):
    for jogadores in range(12):
        peso_jogador = randint(40,90) # peso varia de 40 a 90 kg
        idade_jogador = randint(16, 40) # idade varia de 16 a 40 anos

        peso_total += peso_jogador
        peso_total_time += peso_jogador
        
        idade_total += idade_jogador
        idade_total_time += idade_jogador

        if jogadores % 12 == 0:  # Para interroper a soma dos pesos e idades a cada 12 jogadores (time), no final zera os contadores.
            media_peso_time.append(peso_total_time / 12) # add a media de 1 time na lista por vez
            media_idade_time.append(idade_total_time / 12)
            peso_total_time = 0
            idade_total_time = 0
            

peso_medio_total = peso_total / 360
idade_media_total = idade_total / 360

print('Peso médio de todos jogadores é %.2f' % peso_medio_total)
print('\nIdade média de todos os jogadores é %.2f' % idade_media_total)
print('\nPeso médio dos jogadores de cada time é: ')
print([ '%.2f' % elem for elem in media_peso_time ]) 
print('\nIdade média dos jogadores de cada time é: ')
print([ '%.2f' % elem for elem in media_idade_time ])
