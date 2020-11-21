# ------------ LISTAS -------------
#  Questão 02 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# - "Telefonou para a vítima?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - “Tinha dívidas com a vítima?"
# - "Já trabalhou com a vítima?“
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita“;
# entre 3 e 4 "Cúmplice" e; 5 "Assassino". Caso contrário, ele será classificado como "Inocente".

lista_perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Tinha dívidas com a vítima?',  'Já trabalhou com a vítima?']
pontuação = 0

for pergunta in lista_perguntas:
    resposta = input(pergunta + ' [s/n]: ').lower()

    if resposta == 's':
        pontuação += 1

if pontuação == 2:
    print('Suspeita!')
elif pontuação >= 3 and pontuação <= 4:
    print('Cúmplice!')
elif pontuação == 5:
    print('Assassino!')
else:
    print('Inocente!')