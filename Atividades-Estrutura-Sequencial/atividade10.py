'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

F = (C × 9/5) + 32
'''

temperatura = float(input("\nQual a temperatura em Celsius: "))

fahrenheit = (temperatura * 9 / 5) + 32

print("\nTemperatura em Celsius = {:.2f}°".format(fahrenheit))