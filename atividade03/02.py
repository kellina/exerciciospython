# -------LAÇOS DE REPETIÇÃO ---------
# Questão 02 - Criar um algoritmo que entre com vários números inteiros positivos e
# imprima o produto dos números ímpares digitados e a soma dos pares.

n = int(input('Informe quantos numeros deseja digitar: '))
num = 0
soma_pares = 0
produto_impares = 1

for i in range(n):
    num = int(input('Digite o numero %d: ' % (i +1)))
    while num <= 0:
        num = int(input('Digite o numero %d: ' % (i +1)))

    if num % 2 == 0:
        soma_pares += num
    else:
        produto_impares *= num

print('A soma dos números pares digitados é:', soma_pares)
print('O produtos dos números ímpares digitados é:', produto_impares)