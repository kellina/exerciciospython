# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []
soma = 0

for i in range(5):
    num = int(input('Digite um numero: '))
    numeros.append(num)
    soma = soma + numeros[i]

# soma = sum(numeros)
media = (soma / 5)

print('A soma dos números foi: %d' % soma)
print('A média dos números foi: %d' % media)
