'''
Faça um Programa que leia três números e mostre o maior deles.
'''

numero1 = float(input("Informe primeiro número: "))
numero2 = float(input("Informe segundo número: "))
numero3 = float(input("Informe terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("\nPrimeiro número é o maior valor!")
elif numero2 > numero1 and numero2 > numero3:
    print("\nSegundo número é o maior valor!")
else:
    print("\nTerceiro número é o maior valor!")