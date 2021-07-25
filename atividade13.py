'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''

altura = float(input("\nInforme sua altura: "))

alturahomem = (72.7 * altura) - 58
alturamulher = (62.1 * altura) - 44.7

print("\nPeso ideal para o homem é {:.2f} kilos".format(alturahomem))
print("Peso ideal para a mulher é {:.2f} kilos".format(alturamulher))