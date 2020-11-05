# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome 
# do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Informe o nome do usuario: ').upper()
senha = input('Informe a senha: ').upper()

while senha == nome:
    print('Erro! Senha igual ao nome de usuario.')
    nome = input('Informe o nome do usuario: ').upper()
    senha = input('Informe a senha: ').upper()

print('Usuário cadastrado com sucesso!')