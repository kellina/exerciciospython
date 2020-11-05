# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
media = 0
# print ('Informe as 4 notas')
for i in range(4):
	notas.append(float(input('Informe sua nota '+ str(i+1) + ': ')))
	media += notas[i]
media = media/4
print ("As notas foram: ", notas) 
print ("A media das notas foi: ", media)