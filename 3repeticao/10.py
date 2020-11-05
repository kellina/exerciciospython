# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
# intervalo compreendido por eles.

num1 = int(input('Digite o menor numero: '))
num2 = int(input('Digite o maior numero: '))

for i in range(num1, num2):
    print(i, end=' ')