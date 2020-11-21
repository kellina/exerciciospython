# ---------DICIONÁRIO----------------
# Questão 02 - Implementar o gerador de números primos como uma expressão (dica: use o módulo itertools)

from itertools import islice

def gen_primos(N): #gera primos até o numero primo de valor N
    primos = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primos):
            primos.add(n)
            yield n

lista_primos = [x for x in islice(gen_primos(50), 20)] #50 é o ultimo num primo que quero imprimir e 20 é qtde de primos.
print(lista_primos)

# print(*gen_primos(50))


# -------GERA PRIMOS 2 -------
# primos = []
# for possivelPrimo in range(2, 50):
#     # Supondo que um numero seja primo 
#     ehPrimo = True
#     for num in range(2, possivelPrimo):
#         if possivelPrimo % num == 0:
#             ehPrimo = False
      
#     if ehPrimo:
#         primos.append(possivelPrimo)
# print(primos)

# -----GERA PRIMOS 3------
# noprimes = set(j for i in range(2, 8) for j in range(i*2, 50, i))
# primes = [x for x in range(2, 50) if x not in noprimes]
# print(primes)