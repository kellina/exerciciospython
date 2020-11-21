# ----------- DICIONÁRIOS -------------
# Questão 02 - Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
# chave, nome, idade, telefone. O programa deve ler um número indeterminado de dados,
# criar a agenda e imprimir todos os itens do dicionário no formato chave: nome-idade-
# fone.

qtde_contatos = int(input('Quantos contatos deseja inserir na agenda? '))

agenda = {}
for i in range(qtde_contatos):
    agenda[i + 1] = {}
    agenda[i + 1]['nome'] = input(f'Digite o {i + 1}º nome: ')
    agenda[i + 1]['idade'] = input(f'Digite a idade: ')
    agenda[i + 1]['fone'] = input(f'Digite o fone: ')


print('======= AGENDA ==========')
for chave, contato in agenda.items():
    print(chave, ': ', contato["nome"], '-', contato['idade'], '-', contato['fone'] )




