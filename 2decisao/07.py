# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input('Numero um: '))
num2 = int(input('Numero dois: '))
num3 = int(input('Numero três: '))

if(num1 > num2) and (num1 > num3):
    if(num2 < num3):
        print(f'O {num1} eh o maior')
        print(f'O {num2} eh o menor')
    else:
        print(f'O {num1} eh o maior')
        print(f'O {num3} eh o menor')
elif(num2 > num1) and (num2 > num3):
    if(num1 < num3):
        print(f'O {num2} eh o maior')
        print(f'O {num1} eh o menor')
    else:
        print(f'O {num2} eh o maior')
        print(f'O {num1} eh o menor')
else:
    print(f'O {num3} eh o maior')
    if(num1 < num2):
        print(f'O {num1} eh o menor')
    else:
        print(f'O {num2} eh o menor')
    