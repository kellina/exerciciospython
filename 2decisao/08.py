# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

preco1 = (input('Informe o preco do 1º produto: '))
preco2 = (input('Informe o preco do 2º produto: '))
preco3 = (input('Informe o preco do 3º produto: '))

if(preco1 < preco2) and (preco1 < preco3):
    print(f'Voce deve comprar o 1º produto')   
elif(preco2 < preco1) and (preco2 < preco3):
    print(f'Voce deve comprar o 2º produto')
else:
    print(f'Voce deve comprar o 3º produto')