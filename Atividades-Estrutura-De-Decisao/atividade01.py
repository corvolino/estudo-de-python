'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

numero1 = float(input("\nInforme o número 1: "))
numero2 = float(input("Informe o número 2: "))

if numero1 > numero2:
    print("\nNúmero 1 maior que número 2 !")
elif numero2 > numero1:
    print("\nNúmero 2 maior que número 1 !")
else:
    print("\nNúmeros são iguais!!")
