# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

ultimo = 1
penultimo =  0
prox = 1

while ultimo < 500:
    print('{}.'.format(prox), end='')
    prox = ultimo + penultimo
    penultimo = ultimo
    ultimo = prox
    
print('\nFim')