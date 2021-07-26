'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
    sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

valordalata = 80.00
valordogalao = 25.00

metros = int(input("\nQual a quantidade de metros a ser pintada: "))

qtdlitroslata = (metros / 6) + (10/100)
qtdlata = qtdlitroslata / 18
preco18lata = round(qtdlata + 0.5) * valordalata
###################################################
qtdlitrosgalao = (metros / 6) + (10/100)
qtdgaloes = round((qtdlitrosgalao + 0.5) / 3.6)
precolatoes = round(qtdgaloes) * valordogalao


print("\nQuantidade de tinta = {:.2f} litros".format(float(qtdlitroslata)))
print("Valor pago por Latas de 18 litros = {:.2f} reais".format(preco18lata))
print("Quantidade de Latas necessário de 18 litros para pintar = {} lata(s)".format(int(round(qtdlata + 0.5))))
#################
print("\nQuantidade de Litros em Galões de 3.6 Litros = {:.2f} Litros".format(float(qtdlitrosgalao)))
print("Quantidade de Galões de 3.6 Litros para pintar = {} Galões".format(int((qtdgaloes))))
print("Valor pago por Galões de 3.6 litros = {:.2f} reais".format(precolatoes))
###############
print("\nQuantidade de Latas = {} Latas. Quantidade de Galões. = {} Galões".format(int(qtdlata), int(qtdgaloes)))