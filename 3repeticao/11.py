# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite o menor numero: '))
num2 = int(input('Digite o maior numero: '))
soma = 0

for i in range(num1, num2):
    print(i, end=' ')
    soma = soma + i
print('\nA soma dos numeros do intervalo é: ', soma)