# Raquel

lado1 = float(input('Informe um lado do triângulo: '))
lado2 = float(input('Informe o segundo lado do triângulo: '))
lado3 = float(input('Informe o terceiro lado do triângulo: '))
if((lado1 + lado2)>lado3) and ((lado1 + lado3)>lado2) and ((lado3 + lado2)>lado1):
    if(lado1 == lado2 == lado3):
        print('O triângulo é Equilátero')
    elif(lado1 == lado2) or (lado1 == lado3) or (lado3 == lado1):
        print('O triângulo é Isóceles')
    else:
        print('O triângulo é Escaleno')
else:
    print('Não é um triângulo')