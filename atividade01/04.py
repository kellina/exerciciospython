# ----------LISTAS--------------
# Questão 02 - Crie um programa que leia números inteiros do usuário até que uma
# linha em branco seja inserida. Uma vez que todos os números inteiros foram lidos, seu
# programa deve exibir todos os números, seguidos por todos os zeros, seguidos por
# todos os números positivos.
# Dentro de cada grupo, os números devem ser exibidos na mesma ordem em que foram
# inseridos pelo usuário.
# Por exemplo, se o usuário digitar os valores 3, -4, 1, 0, -1, 0 e -2,
# Então seu programa deve gerar os valores -4, -1, -2, 0, 0, 3 e 1.
# Seu programa deve exibir cada valor em sua própria linha.

grupo_positivos = []
grupo_negativos = []
grupo_zeros = []
entrada = ' '

while entrada != '':
    entrada = input('Digite um número [positivo/negativo/zero]: ')
    if entrada == '':
        break
    num = int(entrada)

    if num < 0:
        grupo_negativos.append(num)
    elif num > 0:
        grupo_positivos.append(num)
    else:
        grupo_zeros.append(num)

grupos = grupo_negativos + grupo_zeros + grupo_positivos
print(grupos)
grupos.sort()