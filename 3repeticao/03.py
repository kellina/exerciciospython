# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Informe seu nome: ')
while len(nome) <= 3:
     nome = input('Informe seu nome [maior que 3 caracteres]: ')

idade = int(input('Informe sua idade: '))
while (idade <= 0) or (idade >= 150):
    idade = int(input('Informe sua idade [entre 0 e 150]: '))

salario = float(input('Informe seu salario: '))
while salario <= 0:
    salario = float(input('Informe seu salario [maior que 0]: '))

sexo = input('Informe o sexo [f/m]: ')
while (sexo != 'f') and (sexo != 'm'):
    sexo = input('Informe o sexo [f/m]: ')

estado_civil = input('Informe o estado civil [s - solteiro, c - casado, v - viuvo, d - divorciado]: ')
while estado_civil not in ('scvd'):
    estado_civil = input('Informe o estado civil [s, c, v, d]: ')

print('Nome: %s, Idade: %d, Salario: %d, Sexo: %s, Estado civil: %s' %(nome, idade, salario, sexo, estado_civil))
