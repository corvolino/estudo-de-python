'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
em graus Celsius.

    C = 5 * ((F-32) / 9).
'''

temperatura = float(input("\nQual a temperatura em Fahrenheit: "))

celsius = 5 * ((temperatura - 32) / 9)

print("\nTemperatura em Celsius = {:.2f}°".format(celsius))
# o :.2f dentro do {} significa que estou limitando o float a duas casas decimais