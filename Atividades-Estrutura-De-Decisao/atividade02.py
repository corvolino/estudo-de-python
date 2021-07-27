'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

numero = float(input("\nInforme o valor: "))

if numero > 0:
    print("\nValor informado é Positivo !")
elif numero < 0:
    print("\nValor informado é Negativo !")
else:
    print("\nValor informado é igual a Zero !")
