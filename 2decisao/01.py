# coding: UTF-8
#Faca um Programa que peca dois numeros e imprima o maior deles.

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
if (num1 > num2):
    print(f'{num1} é o maior numero')
elif (num2 > num1):
    print(f'{num2} é o maior numero')
else:
    print("Os numeros são iguais.")
