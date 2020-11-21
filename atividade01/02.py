# ------LAÇOS DE REPETIÇÃO--------
# Questão 02 - Escreva um programa em Python que lê uma sequência de dígitos, sendo
# cada um dos dígitos fornecido numa linha separada, e calcula o número inteiro composto
# por esses dígitos, pela ordem fornecida. Para terminar a sequência de dígitos é fornecido
# ao programa o inteiro −1. Por exemplo, lendo os dígitos 1 5 4 5 8, o programa calcula o
# número inteiro 15458.

digito = 0
# seq_digitos = []
count = ''

while digito != '-1': # digito >= 0
    digito = (input('Digite um digito: (Ou digite "-1" para finalizar): '))
    if digito == '-1': # digito  < 0
        print('\nSequencia finalizada!')
        break
    # seq_digitos.append(digito)
    count += digito
    
# potencia_10 = pow(10, len(seq_digitos)-1)
# numero = 0
# for digito in seq_digitos:
#     numero += digito * potencia_10
#     potencia_10 /= 10

print(count)