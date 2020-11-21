# ------LISTAS------------
# Questão 01 - Crie um programa que lê palavras do usuário até que o usuário entre com uma linha
# em branco. Após o usuário digitar uma linha em branco, seu programa deve exibir cada palavra
# inserida pelo usuário exatamente uma vez. As palavras devem ser exibidas na mesma ordem em que
# foram inseridos. Por exemplo, se o usuário digitar:
# primeiro
# segundo
# primeiro
# terceiro
# segundo
# Então seu programa deve exibir:
# primeiro
# segundo
# terceiro

lista_palavras = []
palavra = 0
while palavra != '':
    palavra = input("Digite uma palavra: ")
    if palavra == '':
        break
    if palavra not in lista_palavras:
        lista_palavras.append(palavra)
   
# lista_palavras.sort()

print(lista_palavras)