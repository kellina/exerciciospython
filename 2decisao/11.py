# Raquel

salario = float(input('Informe o salário R$ '))
if(salario <= 280):
    novosalario = salario * 1.2
    reajuste = novosalario - salario
    print('Salário Antigo: {:.2f} \nReajuste de 20%'.format(salario))
    print('Valor do aumento R$ {:.2f} '.format(reajuste))
    print('\nO novo salário é R$ {:.2f}'.format(novosalario))
    
elif(salario > 280) and (salario <= 700):
    novosalario = salario * 1.15
    reajuste = novosalario - salario
    print('Salário Antigo: {:.2f} \nReajuste de 15%'.format(salario))
    print('Valor do aumento R$ {:.2f} '.format(reajuste))
    print('O novo salário é R$ {:.2f}'.format(novosalario))
    
elif(salario > 700) and (salario <= 1500):
    novosalario = salario * 1.1
    reajuste = novosalario - salario
    print('Salário Antigo: {:.2f} \nReajuste de 10%'.format(salario))
    print('Valor do aumento R$ {:.2f} '.format(reajuste))
    print('O novo salário é R$ {:.2f}'.format(novosalario))
else:
    novosalario = salario * 1.05
    reajuste = novosalario - salario
    print('Salário Antigo: {:.2f} \nReajuste de 5%'.format(salario))
    print('Valor do aumento R$ {:.2f} '.format(reajuste))
    print('O novo salário é R$ {:.2f}'.format(novosalario))