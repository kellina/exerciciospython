# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []

for i in range(10):
    vetor.append(i)
    # vetor.append(float(input('Numero '+ str(i+1) + ': ')))
vetor.reverse()
print(vetor)