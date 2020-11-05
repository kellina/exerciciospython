# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um numero: '))

if num < 2:  # 0 e 1 não são primos
    print('não é primo')
elif num == 2:  # 2 é o único número par que é primo
    print('primo')
elif num % 2 == 0:  # se for par e não é 2, não é primo
    print('não é primo')
else:  # aqui eu sei que o número é ímpar
    # só testo se é divisível por números ímpares
    for i in range(3, num // 2, 2):
        if num % i == 0:
            print('não é primo')
            break  # não é primo, interrompe o for
    else:
        print('é primo')
