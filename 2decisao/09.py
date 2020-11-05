# Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiro = int(input("Digite o 1º número: "))
segundo = int(input("Digite o 2º número: "))
terceiro = int(input("Digite o 3º número: "))

if(terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if(segundo > primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux

if(terceiro > segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(primeiro,'-',segundo,'-',terceiro)

