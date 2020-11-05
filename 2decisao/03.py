# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = input('Informe o genero [F/M]: ')
if(genero.upper() == 'F'):
    print('Feminino')
elif(genero.upper() == 'M'):
    print('Masculino')
else:
    print('Sexo invalido')