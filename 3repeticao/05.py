# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

popA = int(input("População do país A: "))
popB = int(input("População do país B: "))
ano = 0

while popA > popB:
    print("População de A deve ser menor que populaçcao de B ")
    popA = int(input("População do país A: "))
    popB = int(input("População do país B: "))

taxaA = float(input("Taxa de crescimento da cidade A [%]: "))
taxaB = float(input("Taxa de crescimento da cidade B [%]: "))

while taxaA < taxaB:
    print('A taxa do A deve ser maior que a taxa de B ')
    taxaA = float(input("Taxa de crescimento da cidade A [%]: "))
    taxaB = float(input("Taxa de crescimento da cidade B [%]: "))

while popA < popB:
    ano += 1
    popA = popA * (1 + (taxaA / 100) )
    popB = popB * (1 + (taxaB / 100) )
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % popA)
    print("População B: %d\n" % popB)

print(f"A população do país A ultrapassará o B em {ano} anos.")
