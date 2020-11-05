# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(5):
    num = int(input('Digite um numero: '))
    numeros.append(num)

maior = max(numeros)
print('O maior numero foi: ', maior)
