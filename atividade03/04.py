# ----------- DICIONÁRIOS -----------
# Questão 01 - Suponha um dicionário D de estudantes, como definida no exemplo abaixo, onde cada par 
# consiste de nome do estudante e das notas do mesmo. Escreva uma função chamada “aprovados” que 
# receba como entrada o dicionário D e imprima o nome dos alunos aprovados. 
# Um aluno é aprovado quando todas as suas notas são maiores que 7. 
# Por exemplo, aprovados(D) deverá imprimir Denise.
# D={'Alano':(7.5,8.0,6.5),'Denise':(9.0,8.5,9.5),'Ana Paula':(3.5,1.0,6.5)}

def aprovados(boletins):
    print('O(s) aluno(s) aprovado(s) é(são): ')
    for nome, notas in boletins.items():
        media = sum(notas) / len(notas)
        if media > 7:
            print(nome)


total_alunos = int(input('Quantos alunos deseja informar: '))
boletins = {}
for i in range(total_alunos):
    nome = input(f'Informe o nome do {i+ 1}º aluno: ') #chave
    notas = []   #valor
    for i in range(3):
        nota = float(input(f'Informe a {i +1}ª nota do aluno: '))
        notas.append(nota)  # preenche a lista de notas
        
    boletins[nome] = notas
    
aprovados(boletins)


