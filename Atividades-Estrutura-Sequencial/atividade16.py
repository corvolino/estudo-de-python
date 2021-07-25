'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

metros = int(input("\nQual a quantidade de metros a ser pintada: "))

valordalata = 80.00

qtdlitros = metros / 3
qtdlata = qtdlitros / 18
precototal = valordalata * round(qtdlata + 0.5)

print("\nQuantidade de Litros de tinta = {} litros".format(round(int(qtdlitros))))
print("Quantidade de Latas necessário para pintar = {} lata(s)".format(round(qtdlata + 0.5)))
print("Preço total pago = {:.2f} reais".format(float(precototal)))

'''
round(variavel) arredendo o número para o valor mais próximo. round(variavel + 0.5) arredonda para cima
o valor da variavel.
'''