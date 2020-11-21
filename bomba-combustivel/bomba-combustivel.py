# Exercício 03: Classe “BOMBA DE COMBUSTÍVEL”
# Faça um programa completo que Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# 1) tipoCombustivel. 2) valorLitro 3) quantidadeCombustivel
# b) Possua no mínimo esses métodos:
# 1) abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo.
# 2) abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# 3) alterarValor( ) – altera o valor do litro do combustível.
# 4) alterarCombustivel( ) – altera o tipo do combustível.
# 5) alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

import time

GASOLINA = 'gasolina'
ALCOOL = 'alcool'
DIESEL = 'diesel'
TIPOS = [GASOLINA, ALCOOL, DIESEL]

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, qtdeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.qtdeCombustivel = qtdeCombustivel
        
    
    def abastecerPorValor(self, valor):
        qtdeAbastece = valor / self.valorLitro
        if qtdeAbastece <= self.qtdeCombustivel:
            self.qtdeCombustivel -= qtdeAbastece
            return qtdeAbastece 
        else:
            return 0
    
    def abastecerPorLitro(self, qtde):
        valor = self.valorLitro * qtde
        if qtde <= self.qtdeCombustivel:
            return valor
        else:
            return 0
    
    def alterarValor(self, valor):
        self.valorLitro = valor
    
    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo

    def alterarQtdeCombustivel(self,qtde):
        self.qtdeCombustivel -=  qtde

bombaGasolina = BombaCombustivel(GASOLINA, 4.89, 10000)
bombaAlcool = BombaCombustivel(ALCOOL, 3.89, 10000)
bombaDiesel = BombaCombustivel(DIESEL, 3.59, 10000)
BOMBAS = [bombaGasolina, bombaAlcool, bombaDiesel]

acao = None
while acao !=0:
    print(f"""
    *** BEM-VINDO(A) AO POSTO DE COMBUSTIVEL ***
    -----------------------------------------------
    TIPOS:   \tVALOR(R$) \tQTDE NA BOMBA(L)
    Gasolina \t{bombaGasolina.valorLitro:.2f} \t\t{bombaGasolina.qtdeCombustivel:.2f}
    Álcool \t{bombaAlcool.valorLitro:.2f} \t\t{bombaAlcool.qtdeCombustivel:.2f}
    Diesel \t{bombaDiesel.valorLitro:.2f} \t\t{bombaDiesel.qtdeCombustivel:.2f}
    ------------------------------------------------    
           O QUE DESEJA FAZER?
        1 - Abastecer
        2 - Alterar Valor do Combustivel
        0 - Sair
    """)
    acao = int(input('[0, 1 ou 2]: '))
    
    if acao == 0:
        print ('Obrigada! Volte Sempre.')
        break

    print(f"""
        ------------------------------------------------
           TIPOS:   \tVALOR(R$) \tQTDE NA BOMBA(L)
        1 - Gasolina \t{bombaGasolina.valorLitro:.2f} \t\t{bombaGasolina.qtdeCombustivel:.2f}
        2 - Álcool \t{bombaAlcool.valorLitro:.2f} \t\t{bombaAlcool.qtdeCombustivel:.2f}
        3 - Diesel \t{bombaDiesel.valorLitro:.2f} \t\t{bombaDiesel.qtdeCombustivel:.2f}
    """)
    tipoBomba = int(input('Escolha a bomba de combustivel [1, 2 ou 3]: '))
         
    bombaEscolhida = BOMBAS[tipoBomba-1]
    print(f'Você escolheu {bombaEscolhida.tipoCombustivel}')
    
    if acao == 1:
        formaAbstecimento = int(input('Qual a forma de abstecimento? [1 - por Valor ou 2 - por Litro] '))
        if formaAbstecimento == 1:
            valor = float(input('Informe o valor (R$) que deseja abastecer: '))
            qtdeLitros = bombaEscolhida.abastecerPorValor(valor)
            print(f'A quantidade a ser abastecida é {qtdeLitros:.2f} litros')
            time.sleep(1)
        elif formaAbstecimento == 2:
            qtdeLitros = int(input('Informe quantos litros deseja abastecer: '))
            valor = bombaEscolhida.abastecerPorLitro(qtdeLitros)
            print(f'O valor a pagar é {valor:.2f} reais')
            time.sleep(1)
    else:    
        time.sleep(1)
        print('------------------------------')
        novoValor = float(input('Qual o novo valor do combustivel? '))
        bombaEscolhida.alterarValor(novoValor)
        time.sleep(1)
        print(f'A bomba de {bombaEscolhida.tipoCombustivel} agora tem com valor de {novoValor:.2f} reais.')


