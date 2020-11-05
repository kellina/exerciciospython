# 22) Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, 
# por quais número ele é divisível.

num = int(input('Digite um numero: '))
mult = 0

for i in range(2, num):
    if (num % i == 0):
        print("Múltiplo de",i)
        mult += 1
if(mult == 0):
    print("É primo")
else:
    print("O numero ", num, "não é primo e tem",mult," múltiplos entre 2 e ",num)