'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

numero1 = int(input("Informe o Primeiro número: "))
numero2 = int(input("Informe o Segundo número: "))
numero3 = int(input("Informe o Terceiro número: "))

if numero1 < numero2 and numero1 < numero3:
    if numero2 < numero3:
        print("\nNúmeros em ordem decrescente = {}, {}, {}".format(numero1,numero2,numero3))
    elif numero3 < numero2:
        print("\nNúmeros em ordem decrescente = {}, {}, {}".format(numero1,numero3,numero2))
elif numero2 < numero1 and numero2 < numero3:
    if numero1 < numero3:
        print("\nNúmeros em ordem decrescente = {}, {}, {}".format(numero2,numero1,numero3))
    elif numero3 < numero1:
        print("\nNúmeros em ordem decrescente = {}, {}, {}".format(numero2, numero3, numero1))
else:
    if numero1 < numero2:
        print("\nNúmeros em ordem decrescente = {}, {}, {}".format(numero3, numero1, numero2))
    else:
        print("\nNúmeros em ordem decrescente = {}, {}, {}".format(numero3, numero2, numero1))