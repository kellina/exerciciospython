# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Em que turno você estuda? [m-matutino ou v-Vespertino ou n- Noturno]: ')
if turno == 'm':
    print('Bom dia!')
elif turno == 'v':
    print('Boa tarde!')
elif turno == 'n':
    print('Boa noite!')
else:
    print('Valor inválido!')