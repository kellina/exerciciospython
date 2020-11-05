# Faça um programa que leia três números e mostre o maior deles.

num1 = int(input('Numero um: '))
num2 = int(input('Numero dois: '))
num3 = int(input('Numero três: '))

if(num1 > num2) and (num1 > num3):
    print(f'O {num1} eh o maior')   
elif(num2 > num1) and (num2 > num3):
    print(f'O {num2} eh o maior')
else:
    print(f'O {num3} eh o maior')
   