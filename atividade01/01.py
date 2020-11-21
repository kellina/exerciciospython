# -------LAÇOS DE REPETIÇÃO-------
# Questão 01 - Escreva um programa em Python que pede ao utilizador que lhe forneça
# um inteiro correspondente a um número de segundos e que calcula o número de dias
# correspondentes a esse número de segundos. O número de dias é fornecido como um
# real. O programa termina quando o utilizador fornece um número negativo. O seu
# programa deve possibilitar a seguinte interação:
#   Escreva um número de segundos (um número negativo para terminar)  #   ? 45  
#   O número de dias correspondente é 0.0005208333333333333
#   Escreva um número de segundos (um número negativo para terminar) #   ? 6654441 
#   O número de dias correspondente é 77.01899305555555
#   Escreva um número de segundos (um número negativo para terminar) #   ? -1

segundos_dia = 86400
segundos = 0
while segundos >= 0:
    segundos = float(input('Escreva um numero de segundos (ou um numero negativo para terminar): '))
    dias = segundos / segundos_dia
    if segundos < 0:
        print('Fim da interação!', segundos)
        break

    print(f'O número de dias correspondente é {dias:.6f}')